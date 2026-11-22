import json, gzip, hashlib, pathlib, shutil, sys
S=pathlib.Path(sys.argv[1]); DATA=pathlib.Path('/home/user/Modelo-JMR-datos/jmr-v2')
lib=json.load(open(S/'bib_new.json')); F=lib['files']; base=json.load(open(S/'bib.json'))['files']
r8=json.load(open(S/'r8_resultado.json'))
inv=json.load(open(S/'r_new/inventario.json'))
pdfs={}
for r in inv['empresas']:
    t=r['ticker']; m=json.load(open(S/'r_new'/t/'meta.json'))
    src=S/'r_new'/t/m['pdf']; dst=DATA/'informes'/t/m['pdf']; assert dst.exists(), dst
    shutil.copyfile(src,dst); pdfs[t]={'ruta':'jmr-v2/informes/%s/%s'%(t,m['pdf']),'paginas':r['paginas'],'sha256':hashlib.sha256(dst.read_bytes()).hexdigest()}
for t,v in r8.items():
    p=pathlib.Path(v['pdf']); pdfs[t]={'ruta':'jmr-v2/'+str(p.relative_to(DATA)),'paginas':v['paginas'],'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
for t,v in pdfs.items():
    e=F['empresas/'+t+'.json']; a=F['analisis/'+t+'.json']
    inf=e.get('informe')
    if isinstance(inf,dict):
        if isinstance(inf.get('pdf'),dict): inf['pdf']['sha256']=v['sha256']
        if 'paginas' in inf: inf['paginas']=v['paginas']
    a['justificacionSupuestos'].update({'pdf':v['ruta'],'paginasPdf':v['paginas'],'sha256Pdf':v['sha256']})
    ce=e.get('cierreEditorial')
    if isinstance(ce,dict) and ce.get('completo'):
        e['cierreEditorial']={'completo':False,'pendientes':['Actualizar huellas y páginas del manifiesto de cierre (analisis/%s.cierre.json) tras la ampliación de justificaciones del 22-nov-2026; el PDF y el análisis cambiaron.'%t],'anterior':ce}
# Ningún supuesto ni valor puede haber cambiado.
for c in F['catalogo.json']['empresas']:
    t=c['ticker']; n=F['empresas/'+t+'.json']; o=base['empresas/'+t+'.json']
    assert n['assumptions']==o['assumptions'] and n['libro']['valores']==o['libro']['valores'] and n['financials']==o['financials'], t
assert F['catalogo.json']==base['catalogo.json']
raw=(json.dumps(lib,ensure_ascii=False,separators=(',',':'))+'\n').encode()
sha=hashlib.sha256(raw).hexdigest(); name='biblioteca-'+sha+'.json.gz'
(DATA/name).write_bytes(gzip.compress(raw,compresslevel=9,mtime=0))
(DATA/'biblioteca.json').write_text(json.dumps({'schemaVersion':'jmr-biblioteca-gzip-1','app':'jmr-v2','archive':name,'sha256':sha},ensure_ascii=False,indent=1)+'\n')
json.dump(pdfs,open(S/'pdfs.json','w'),indent=1)
print(name, len(pdfs),'PDF')
