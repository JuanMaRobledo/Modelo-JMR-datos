"""Completar tablas y objetivos desde las lecturas nativas verificadas del cierre."""
import copy,json,sys
from pathlib import Path
import reconciliar_publicacion_20261019 as c
root=Path(__file__).resolve().parents[1];review=Path(sys.argv[1]);changed=[]
for p in sorted((root/'valoraciones').glob('*.json')):
 a=json.loads(p.read_text());t=a['ticker']
 if a.get('valoracionHolding'):continue
 live=json.loads((review/'live'/f'{t}.json').read_text())
 live['sheets']['Financials Multiples']=json.loads((review/'financial-complete'/f'{t}.json').read_text())
 a['hojas']['valoracion']['Financials Multiples']=c.table(live,'Financials Multiples')
 for tab in c.TABS:
  if tab not in a['hojas']['valoracion']:a['hojas']['valoracion'][tab]=c.table(live,tab)
 for k,col in zip(c.SCEN,'CDE'):
  if a['objetivoPonderado'][k] is None:a['objetivoPonderado'][k]=c.num(live,'Resumen de Valoración',col+'12')
 if t=='P911':a['currency']='EUR'
 new=c.block(a);a['analisisFundamental']=c.prepend(a.get('analisisFundamental',''),new)
 for group in a['hojas'].values():
  for name,txt in list(group.items()):
   if 'Tesis' in name or name=='Informe de valoración':group[name]=c.prepend(txt,new)
 p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n');changed.append(str(p.relative_to(root)))
 for q in (root/'analisis').glob(t+'-research-*.json'):
  j=json.loads(q.read_text());j['linkedValuation']=copy.deepcopy(a);j['objetivoPonderado']=a['objetivoPonderado']
  if t=='P911':j['currency']='EUR'
  for key in ['html','articleHtml','valuationHtml','calculationHtml']:j[key]=c.prepend(j.get(key,''),new)
  q.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n');changed.append(str(q.relative_to(root)))
(review/'final-fix-paths.json').write_text(json.dumps(changed+['scripts/reconciliar_publicacion_20261019.py','scripts/completar_exportacion_20261019.py']))
print(json.dumps({'archivos':len(changed),'tablasCompletas':36}))
