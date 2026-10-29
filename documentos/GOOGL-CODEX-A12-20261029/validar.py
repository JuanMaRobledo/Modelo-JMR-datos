"""Validación acotada sobre lecturas nativas; no sustituye controles globales JMR."""
import json
import math
from pathlib import Path

p=Path(__file__).resolve().parent

def flat(name):
 x=json.loads((p/name).read_text());out={}
 for s in x['sheets']:
  for b in s.get('data',[]):
   for r,row in enumerate(b.get('rowData',[]),b.get('startRow',0)+1):
    for c,cell in enumerate(row.get('values',[]),b.get('startColumn',0)+1):out[(s['properties']['title'],r,c)]=cell
 return out

cells=flat('captura-nativa.json');cells.update(flat('captura-entradas-final.json'))
def v(tab,r,c=2):
 x=cells.get((tab,r,c),{}).get('effectiveValue',{})
 if 'errorValue' in x:raise ValueError((tab,r,c,x))
 return next(iter(x.values()),None)

checks=[]
def check(name,ok,detail=None):checks.append({'control':name,'estado':'APROBADO' if ok else 'FALLIDO','detalle':detail})
def eq(a,b):return math.isclose(a,b,rel_tol=1e-10,abs_tol=1e-6)

record=json.loads((p/'valoracion-propuesta.json').read_text())
for name,off,srow in [('Base',0,5),('Conservador',51,6),('Optimista',102,8),('Disrupción',155,7)]:
 df=1;pv=0
 for c in range(3,13):
  df/=1+v('Valuation output',14+off,c)
  cash=v('Valuation output',11+off,c)
  assert eq(cash,v('Valuation output',9+off,c)-v('Valuation output',10+off,c))
  pv+=cash*df
 tv=v('Valuation output',11+off,13)/(v('Valuation output',14+off,13)-v('Valuation output',4+off,13))*df
 bridge=sum(v('Valuation output',r+off)*sgn for r,sgn in [(27,-1),(28,-1),(29,1),(30,1),(32,-1)])-v('Input sheet',76)
 price=(pv+tv+bridge)/v('Valuation output',34+off)
 check('Replay financiero acotado '+name,eq(price,v('Escenarios e historias',srow,8)) and v('Escenarios e historias',srow,11)=='LISTO',{'precio':price,'VPexplicito':pv,'VPterminal':tv})
check('Probabilidades suman100%',eq(sum(v('Escenarios e historias',r,2) for r in range(5,9)),1))
check('Promedio ordinario excluye disrupción',eq(v('Escenarios e historias',10,8),sum(v('Escenarios e historias',r,2)*v('Escenarios e historias',r,8) for r in [5,6,8])/.9))
check('MOS35% sobreDCFBase',eq(record['precioMOS'],v('Valuation output',35)*.65))
check('WACCDetailed nativo',v('Cost of capital worksheet',84)=='VALIDADO' and v('Cost of capital worksheet',12)=='Detailed')
check('Casos especiales nativos',v('Input sheet',108)=='VALIDADO')
check('Reinversión terminal g/ROIC',eq(v('Valuation output',10,13),v('Valuation output',9,13)*v('Valuation output',4,13)/v('Valuation output',42,13)))
check('CentroWACC/g nativo',eq(v('Sensibilidad DCF',8,4),record['valorPrincipal']))
check('CentroROIC/g nativo',eq(v('Sensibilidad DCF',19,4),record['valorPrincipal']))
check('Centrocrecimiento/margen nativo',eq(v('Sensibilidad DCF',30,4),record['valorPrincipal']))
s=json.loads((p/'sensibilidades-nativas.json').read_text())
check('CentroS/C en copia independiente',any(eq(z['value'],record['valorPrincipal']) and z['stc15']==.45 and z['stc610']==.65 for z in s['stc']))
check('Reinversión no suma CapEx además deS/C',all('Puente' not in cells[('Valuation output',10,c)]['userEnteredValue']['formulaValue'] for c in range(3,13)))
check('Métodos complementarios completos',False,'Celdas preferentes de entrada contienen fórmula semilla que devuelve blanco cuando existen preferentes. Faltan anclas históricas verificadas. NO APROBADO PARA PUBLICAR.')
checks += [{'control':t,'estado':'NO_EJECUTADO'} for t in ['Auditoría económica','Historia primaria10años línea a línea','Profundidad editorial18secciones','Integridad global46pestañas','DCF inverso','Pipeline oficial desde_cero/valorar']]
output={'revision_id':record['revision_id'],'alcance':'CONTROLES_ACOTADOS_NO_CERTIFICACION','can_publish':False,'controles':checks}
(p/'controles.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(output,ensure_ascii=False,indent=2))
