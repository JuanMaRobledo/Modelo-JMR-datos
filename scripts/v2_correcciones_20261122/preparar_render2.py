import json,sys,pathlib,shutil
lib=json.load(open(sys.argv[1])); out=pathlib.Path(sys.argv[2]); F=lib['files']
HOM=sys.argv[3].split(',')
if out.exists(): shutil.rmtree(out)
out.mkdir(parents=True); inv=[]
for t in HOM:
  e=F['empresas/'+t+'.json']; a=F['analisis/'+t+'.json']
  p=a.get('pdf') or a.get('informePdf'); p=p if isinstance(p,str) else p['ruta']
  (out/t).mkdir(); json.dump(a,open(out/t/'analisis.json','w'),ensure_ascii=False)
  rev=e['revision']['id'] if isinstance(e['revision'],dict) else e['revision']
  json.dump({'ticker':t,'company':e['company'],'estado':e['estado'],'revision':rev,'asOf':e['asOf'],'pdf':p.split('/')[-1]},open(out/t/'meta.json','w'),ensure_ascii=False)
  inv.append({'ticker':t,'estado':'CANDIDATO_JSON'})
json.dump({'empresas':inv},open(out/'inventario.json','w'))
