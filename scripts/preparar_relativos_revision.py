"""Importación técnica de contrastes provisionales; nunca cambia el DCF."""
import json, hashlib, copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent
METHODS=['EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF','P/V','P/BV']
def read(p): return json.loads(Path(p).read_text())
def write(p,x):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def rows(raw,title):
 s=next(s for s in raw['sheets'] if s['properties']['title']==title);out={}
 for d in s['data']:
  for i,r in enumerate(d.get('rowData',[]),d.get('startRow',0)+1):
   out[i]=[next(iter(c.get('effectiveValue',{}).values()),None) for c in r.get('values',[])]
 return out
def matrix(name,x,y,z,origin,source,limit,formula=None):
 if formula is None:
  a=(z[0][1]-z[0][0])/(y[0]*(x[1]-x[0]));b=z[0][0]-a*x[0]*y[0]
  formula={'tipo':'affine-product','factor':a,'constante':b,'descripcion':'Coeficientes de la fórmula nativa múltiplo × fundamental, puente equity/dividendos y descuento; ver captura de fórmulas.'}
 return dict(metodo=name,escenario='base',estado='OK',peso=0,ancla='PROVISIONAL',anclaCertificada=False,fuenteAncla=source,limitacion=limit,origen=origin,unidadResultado='USD/accion',fundamentalFY3=x,multiploElegido=y,matriz=z,centro=z[2][2],vp3Original=z[2][2],formula=formula)
def computed(name,fund,anchor,factor,constant,origin,source,limit):
 xs=[fund*q for q in [.8,.9,1,1.1,1.2]];ys=[anchor*q for q in [.8,.9,1,1.1,1.2]]
 return matrix(name,xs,ys,[[factor*x*y+constant for x in xs] for y in ys],origin,source,limit,{'tipo':'affine-product','factor':factor,'constante':constant,'descripcion':'VP USD/acción = factor × múltiplo × fundamental + constante. Parámetros y supuestos explícitos en evidencia.'})
def integrate(v,mats,raw,notes):
 rev=v['revisionId'];p=f'evidencia/relativos-revision-20261031/{rev}.json'
 evidence={'revisionId':rev,'sheetId':v['sheet_id'],'certificacionEconomica':'NO_CERTIFICADA','sources':raw,'supuestos':notes,'matrices':mats}
 write(ROOT/p,evidence);digest=hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
 v['sensibilidadMultiples']={'contrato':'review-relative-v1','revisionId':rev,'sourceSheetId':v['sheet_id'],'sourcePath':p,'resultadosSha256':digest,'estadoPublicacion':'INTEGRADO_EN_REVISION','controlesTecnicosAprobados':True,'certificado':False,'certificacionEconomica':'NO_CERTIFICADA','pesoEnDCFPrincipal':0,'tipo':'MULTIPLOS_BANCARIOS' if v['ticker'] in ['NU','XP'] else 'MULTIPLOS_OPERATIVOS','advertencia':'Contrastes provisionales EN_REVISION, sin certificación económica; peso cero en el DCF principal. '+notes,'matrices':mats}
 dm=v.setdefault('descuentoMultiples',{})
 # Conserva pesos históricos de la hoja en su evidencia; no se mezclan con el DCF.
 dm.update({'pesoDcf':1,'pesoMultiplos':0,'criterio':'Contraste provisional FY+3 a valor presente; peso cero en DCF','certificacionEconomica':'NO_CERTIFICADA','ponderadoHoy':None,'multiplesHoy':None,'metodos':[{'nombre':m['metodo'],'peso':0,'estado':'PROVISIONAL_NO_CERTIFICADO','base':{'vp':[None,None,m['centro']],'consolidado':m['centro']}} for m in mats]})
 return v
def main():
 cat=read(ROOT/'catalogo.json')
 for t in ['UBER','GOOGL','INTU','NU']:
  vp=next(p for p in cat['valoraciones'] if p.startswith('valoraciones/'+t+'-'));v=read(ROOT/vp);before=copy.deepcopy(v)
  capture=BASE/f'source-{t}.json'
  raw=read(capture) if capture.exists() else read(ROOT/f'evidencia/relativos-revision-20261031/{v["revisionId"]}.json')['sources'];mats=[]
  if t in ['UBER','GOOGL']:
   rs=rows(raw,'Sensibilidad por múltiplo');ds=rows(raw,'Descuento de múltiplos')
   for i,n in enumerate(METHODS):
    r=76+i*10
    if rs[r+8][8]!='OK':continue
    x=rs[r+2][1:6];y=[rs[k][0] for k in range(r+3,r+8)];z=[rs[k][1:6] for k in range(r+3,r+8)]
    assert abs(z[2][2]-rs[r+8][6])<1e-7
    if i<5:assert abs(z[2][2]-ds[20+i][8])<1e-7
    mats.append(matrix(n,x,y,z,f"'Sensibilidad por múltiplo'!A{r}:I{r+8}",'Hoja oficial; ancla JMR seleccionada existente, provisional, no independiente','Ancla ligada a precio/derivada o constante; no constituye confirmación independiente del DCF.'))
   notes='Se preservan los supuestos de la hoja como contraste; la ponderación 60/40 de la fuente no se adopta en el objetivo principal. P/BV N/D se conserva sin generar ceros.'
  elif t=='INTU':
   rs=rows(raw,'Múltiplos A - INTU')
   for i,n in enumerate(METHODS[:6]):
    r=34+i*8
    mats.append(matrix(n,rs[r][1:6],[rs[k][0] for k in range(r+1,r+6)],[rs[k][1:6] for k in range(r+1,r+6)],f"'Múltiplos A - INTU'!A{r}:F{r+6}",rs[20][0]+' '+rs[21][0],rs[22][0]))
   notes='Anexo alternativo nativo de la misma hoja, no la plantilla industrial vacía. NI/OCF/FCFE son proxies y las anclas derivadas no son estimaciones independientes. P/BV no disponible por patrimonio FY+3 sin proyectar.'
  else:
   rs=rows(raw,'FCFE bancario A');shares=rs[5][1];price=rs[6][1];ni=rs[3][1];eq=rs[4][1];fy=rs[19];ke=fy[7]
   pe=price*shares/ni;pb=price*shares/eq;pf=pe*fy[2]/fy[6]
   for name,den,anchor in [('P/E',fy[2],pe),('P/FCFE',fy[6],pf),('P/BV',fy[4],pb)]:
    mats.append(computed(name,den,anchor,1/(shares*(1+ke)**3),0,"'FCFE bancario A'!A3:J19",'FCFE bancario A: NI y patrimonio LTM, precio observado; P/FCFE equivalente al P/E proyectado','Ancla observada/derivada provisional; no comparable independiente. Precio FY+3 descontado a Ke, excluye dividendos, no es retorno total.'))
   notes=f'Banca: Ke USD {ke}, acciones {shares} millones. P/E=precio×acciones/NI LTM; P/BV=precio×acciones/patrimonio. P/FCFE=P/E×NI FY3/FCFE FY3; sin añadir caja ni restar depósitos. No incluye dividendos en el contraste de precios.'
  integrate(v,mats,raw,notes)
  assert {k:x for k,x in v.items() if k not in ['sensibilidadMultiples','descuentoMultiples']}=={k:x for k,x in before.items() if k not in ['sensibilidadMultiples','descuentoMultiples']}
  write(ROOT/vp,v);print(t,len(mats),v['valorPrincipal'])
if __name__=='__main__':main()
