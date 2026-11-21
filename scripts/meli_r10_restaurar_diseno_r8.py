#!/usr/bin/env python3
"""Rehacer el PDF MELI con la composición exacta R8, sin alterar su valoración R10."""
import pathlib, gzip, hashlib, json, copy, html, re
import fitz
from bs4 import BeautifulSoup
from weasyprint import HTML
ROOT=pathlib.Path(__file__).resolve().parents[1]
DATA=ROOT/'jmr-v2'
R8=DATA/'informes/MELI/MELI-V2-LTM20260930-R8_INFORME_FUNDAMENTAL.pdf'
MANIFEST=DATA/'biblioteca.json'
PDF_REL='jmr-v2/informes/MELI/MELI-V2-LTM20260930-R10_INFORME_FUNDAMENTAL.pdf'
HTML_REL='jmr-v2/informes/MELI/MELI-V2-LTM20260930-R10_INFORME_FUNDAMENTAL.html'
PDF=ROOT/PDF_REL
HTML_OUT=ROOT/HTML_REL
REV='MELI-V2-LTM20260930-R10'
EXPECTED={'conservador':1110.0353123134807,'base':2367.5914843010655,'optimista':3601.4948815116336}
KEYS=['perfil','introduccion','negocio','calidad','direccion','competencia','ciclos','riesgos','destruccion','tesis_contraria','supuestos','valoracion','conclusiones','fuentes']
TITLES={'perfil':'Perfil de la empresa y tesis','introduccion':'Introducción','negocio':'Modelo de negocio','calidad':'Calidad del negocio','direccion':'Equipo directivo y gestión del capital','competencia':'Competitividad','ciclos':'Los tres ciclos: empresa, macroeconomía y mercado','riesgos':'Riesgos','destruccion':'¿Qué podría destruir a la empresa?','tesis_contraria':'Los alcistas frente a los bajistas','supuestos':'Supuestos y escenarios','valoracion':'Valoración','conclusiones':'Conclusiones y plan de seguimiento','fuentes':'Anexo: fuentes, limitaciones y glosario'}
fmt=lambda x,n=2:'US$'+f'{x:,.{n}f}'.replace(',','@').replace('.',',').replace('@','.')
man=json.loads(MANIFEST.read_text())
raw=gzip.decompress((DATA/man['archive']).read_bytes())
assert hashlib.sha256(raw).hexdigest()==man['sha256']
lib=json.loads(raw);f=lib['files'];m=f['empresas/MELI.json'];doc=f['analisis/MELI.json']
assert m['revision']['id']==doc['revision']==REV
assert len(doc['blocks'])==14
assert all(abs(m['libro']['valores'][k]-v)<.02 for k,v in EXPECTED.items())
assert R8.is_file()
original={k:copy.deepcopy(v) for k,v in f.items() if k not in ('empresas/MELI.json','analisis/MELI.json')}
price=1355.49;mos=EXPECTED['base']*.65;shares=50.696802
# La cotización es la figura histórica original R8, hasta el 17-nov; precio DCF a 19-nov.
chart=DATA/'qa/MELI-R10-ED4/cotizacion-original-R8.png';chart.parent.mkdir(parents=True,exist_ok=True)
with fitz.open(R8) as src:
 assert len(src)==31
 src[1].get_pixmap(matrix=fitz.Matrix(2,2),clip=fitz.Rect(55,557,542,731),alpha=False).save(chart)
def prepare(source):
 soup=BeautifulSoup(source,'html.parser')
 for e in soup.find_all(['script','iframe','style','object','embed']):e.decompose()
 for p in list(soup.find_all('p')):
  if p.get_text(' ',strip=True).lower().replace('.','')=='lo esencial':
   nxt=p.find_next_sibling()
   if nxt and nxt.name=='ul':
    box=soup.new_tag('aside',**{'class':'essential'})
    heading=soup.new_tag('div',**{'class':'kicker'});heading.string='LO ESENCIAL'
    box.append(heading);box.append(nxt.extract());p.replace_with(box)
 for q in soup.find_all('blockquote'):q['class']='reading'
 for t in soup.find_all('table'):t['class']='finance'
 for g in soup.find_all('img'):
  src=g.get('src','')
  prefix='https://raw.githubusercontent.com/JuanMaRobledo/Modelo-JMR-datos/main/'
  if src.startswith(prefix):
   p=ROOT/src[len(prefix):]
   assert p.is_file(),p
   g['src']=p.resolve().as_uri()
  elif src.startswith(('file:','data:image/')):pass
  else:raise ValueError('Imagen sin fuente autorizada '+src)
 for g in soup.find_all('figure'):g['class']='fig'
 return str(soup)
blocks={k:prepare(doc['blocks'][k]) for k in KEYS}
CSS=r"""
:root{--blue:#5b8baa;--navy:#1c344a;--ink:#1e2830;--pale:#a8c3d3;--wash:#f1f5f7}
@page{size:A4;margin:16mm 15mm 16mm;@bottom-left{content:"Modelo JMR V2 · MercadoLibre · En revisión";font:6.5pt Arial,sans-serif;color:#555}@bottom-right{content:counter(page) - 1;font:7pt Arial,sans-serif;color:#555}}
@page cover{margin:0;@bottom-left{content:none}@bottom-right{content:none}}
*{box-sizing:border-box}body{margin:0;color:var(--ink);background:white;font:10pt/1.43 "Liberation Serif",Georgia,serif}
p{margin:0 0 7pt;orphans:3;widows:3}h1,h2,h3,h4{break-after:avoid}
.cover{page:cover;break-after:page;height:297mm;min-height:297mm;background:var(--blue);color:white;display:flex;flex-direction:column;justify-content:space-between;padding:29mm 22mm 21mm}
.cover .brand{font:700 10pt/1.45 Arial,sans-serif;letter-spacing:1px}.cover .brand small{display:block;font:8pt Arial,sans-serif;letter-spacing:1px}
.cover .middle h1{font:normal 39pt "Liberation Serif",Georgia,serif;margin:0 0 17pt}.cover .middle p{font:italic 17pt/1.37 "Liberation Serif",Georgia,serif;max-width:141mm}
.cover .bottom{border-top:.6pt solid #b9d3e1;padding-top:12pt;display:flex;justify-content:space-between;font:7.2pt Arial,sans-serif;letter-spacing:1.5px}
.page,.chapter{break-before:page}.kicker,.label{font:8pt/1.3 Arial,sans-serif;color:var(--blue);letter-spacing:1.35px;text-transform:uppercase}
.profile h1{font:normal 28pt/1.2 "Liberation Serif",Georgia,serif;border-bottom:.6pt solid #ced7dc;padding-bottom:8pt;margin:9pt 0 14pt}
.profile-grid{display:grid;grid-template-columns:1.75fr 1fr;gap:10mm}
.profile .thesis{font:italic 12.6pt/1.44 "Liberation Serif",Georgia,serif;margin:10pt 0 14pt}.profile p{line-height:1.43}
.profile .right>div{border-top:.6pt solid #d4e0e6;padding:6pt 0}.profile .right>div:first-child{border-top:2pt solid var(--ink)}
.profile .right .label{font-size:7.2pt}.profile .right strong{display:block;font:normal 12pt "Liberation Serif",Georgia,serif;margin-top:5pt}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:8pt;border-top:.8pt solid var(--ink);padding:11pt 5pt;margin:14pt 0}
.metrics small{display:block;color:#7b868f;font:6.5pt Arial,sans-serif;letter-spacing:1px;text-transform:uppercase;margin-bottom:6pt}
.metrics strong{font:11pt "Liberation Serif",Georgia,serif}
.stock{border-top:.5pt solid #d4dee3;padding-top:10pt}.stock img{max-width:100%;height:auto;max-height:49mm;display:block;margin:auto}
.stock figcaption,.fig figcaption{font:7pt/1.3 Arial,sans-serif;color:#697984;text-align:center}
.legal h1,.toc-page h1{font:normal 26pt "Liberation Serif",Georgia,serif;margin:0 0 12pt}
.legal h3{color:var(--blue);font:9pt Arial,sans-serif;letter-spacing:1px;text-transform:uppercase;margin:18pt 0 7pt}
.toc{padding:0;list-style:none}.toc li{display:flex;gap:12pt;border-bottom:.6pt solid #e1e6ea;padding:8pt 0;font-size:10.5pt}
.toc .num{color:var(--blue);font:8pt Arial,sans-serif;width:20pt}
.chapter>.kicker{margin-bottom:8pt}.chapter>h1{font:normal 25pt/1.18 "Liberation Serif",Georgia,serif;border-bottom:.7pt solid #aac0cb;padding-bottom:9pt;margin:0 0 14pt}
.chapter p{font-size:9.7pt}.chapter h2{font:italic bold 12pt "Liberation Serif",Georgia,serif;margin:13pt 0 6pt}
.chapter h3,.chapter h4{font:italic bold 10.5pt "Liberation Serif",Georgia,serif;margin:13pt 0 5pt}
.chapter ul,.chapter ol{padding-left:18pt;margin:7pt 0 9pt}.chapter li{margin:3pt 0}
.chapter .essential{background:var(--wash);border-top:1pt solid var(--blue);padding:8pt 10pt;margin:10pt 0 13pt}
.chapter .essential .kicker{font-size:7pt}.chapter .essential ul{font:8pt/1.4 Arial,sans-serif;padding-left:14pt;margin:6pt 0}
.chapter .reading{background:var(--wash);border-left:2pt solid var(--blue);padding:10pt 12pt;margin:12pt 0;font-style:italic}
.chapter table{width:100%;max-width:100%;border-collapse:collapse;font:7.4pt/1.28 Arial,sans-serif;margin:7pt 0}
.chapter th{background:var(--blue);color:white;text-align:left}.chapter th,.chapter td{padding:3pt 4pt;border-bottom:.5pt solid #d8e1e6;vertical-align:top;overflow-wrap:break-word}
.chapter tbody tr:nth-child(even){background:#f8fafb}.chapter tr{break-inside:avoid}
.chapter figure{break-inside:avoid;margin:11pt 0}.chapter img{display:block;margin:auto;width:auto!important;max-width:100%!important;max-height:92mm!important;height:auto!important;object-fit:contain!important}
.chapter figure figcaption{font:7pt Arial,sans-serif;color:#76828c;margin-top:5pt}
.chapter .table-scroll{overflow:visible!important}
"""
def fragment(x):return BeautifulSoup(x,'html.parser')
s=BeautifulSoup('<html lang="es"><head><meta charset="utf-8"><title>MELI R10 · Informe fundamental · diseño R8</title></head><body></body></html>','html.parser')
style=s.new_tag('style');style.string=CSS;s.head.append(style);body=s.body
body.append(fragment("""<section class="cover"><div class="brand">MODELO JMR<small>Análisis fundamental · V2</small></div>
<div class="middle"><h1>MercadoLibre</h1>
<p>La mayor empresa de comercio electrónico y fintech de Latinoamérica crece 45 % y sacrifica margen para ganar hábito. ¿Cuánto vale esa inversión?</p></div>
<div class="bottom"><span>INFORME FUNDAMENTAL · EN REVISIÓN ECONÓMICA</span><span>NOVIEMBRE 2026</span></div></section>"""))
upside=100*(EXPECTED['base']/price-1)
profile=('<section class="page profile"><div class="kicker">PERFIL DE LA EMPRESA</div><h1>MercadoLibre</h1>'
'<div class="profile-grid"><div class="left"><div class="label">TESIS</div>'
'<p class="thesis">MercadoLibre combina el comercio electrónico, la logística y Mercado Pago en un ecosistema latinoamericano de gran escala. Crece 45 % en el 3T26, pero su rentabilidad enfrenta costos de crédito y envíos. El DCF Base R10 de '+fmt(EXPECTED['base'])+' por acción depende de recuperar márgenes sin deteriorar la calidad del negocio.</p>'
'<div class="label">LA EMPRESA</div>'
'<p>Marketplace, publicidad, distribución, billetera, pagos, tarjetas y préstamos operan de forma complementaria en Brasil, México, Argentina y otros mercados. La fintech introduce riesgos de fondeo, provisiones y capital que no se interpretan como los de una plataforma sin cartera crediticia.</p>'
'<p>Ingresos LTM de US$38.523 millones y EBIT reportado US$2.859 millones (margen 7,42 %). El EBIT ajustado por capitalización de I+D del modelo asciende a US$3.604,67 millones (9,36 %). La diferencia es analítica, no un margen realizado.</p></div>'
'<aside class="right"><div><span class="label">VALOR INTRÍNSECO BASE (R10)</span><strong>'+fmt(EXPECTED['base'],0)+'</strong></div>'
'<div><span class="label">POTENCIAL SOBRE PRECIO FECHADO</span><strong>+'+f'{upside:.1f}'+' %</strong></div>'
'<div><span class="label">PRECIO CON MOS (35 %)</span><strong>'+fmt(mos,0)+'</strong></div>'
'<div><span class="label">SECTOR</span><strong>Comercio electrónico y fintech</strong></div>'
'<div><span class="label">MERCADO · MONEDA</span><strong>NASDAQ · USD</strong></div>'
'<div><span class="label">REVISIÓN</span><strong>R10 · EN REVISIÓN</strong></div></aside></div>'
'<div class="metrics"><div><small>PRECIO (19-NOV-2026)</small><strong>'+fmt(price)+'</strong></div>'
'<div><small>RANGO 52 SEMANAS</small><strong>N/D verificado</strong></div>'
'<div><small>CRECIMIENTO 3T26</small><strong>+45 %</strong></div>'
'<div><small>CAPITALIZACIÓN</small><strong>~US$'+f'{shares*price/1000:.1f}'+' mil M</strong></div></div>'
'<figure class="stock"><div class="kicker">COTIZACIÓN, ÚLTIMOS 5 AÑOS</div><img src="'+chart.resolve().as_uri()+'">'
'<figcaption>Serie original de MELI R8 hasta 17-nov-2026, fuente Alpha Vantage. Precio DCF R10 fechado 19-nov-2026.</figcaption></figure></section>')
body.append(fragment(profile))
body.append(fragment("""<section class="page legal"><h1>Aviso legal</h1>
<p>Análisis educativo. No constituye asesoramiento financiero, oferta ni recomendación individualizada. Los riesgos de mercado pueden incluir pérdida total de capital.</p>
<h3>Estado de este estudio</h3><p>Revisión MELI-V2-LTM20260930-R10, corte contable LTM al 30-sep-2026. La maquetación reproduce el PDF MELI R8 y el patrón de NVIDIA R6. Se conserva íntegra la valoración R10 y sus salvedades. Estado EN REVISIÓN; no es aprobación personal.</p>
<h3>Cómo se elaboró</h3><p>Hechos de los reportes 10-K/10-Q, expediente de estados financieros, libro y fuentes secundarias identificadas. El análisis conserva las cifras reportadas, los ajustes de I+D de Damodaran y la separación de FY y LTM. El fondeo de Mercado Pago, arrendamientos y WACC requieren auditoría económica.</p></section>"""))
toc=s.new_tag('section',**{'class':'page toc-page'});h=s.new_tag('h1');h.string='Contenido';toc.append(h);ol=s.new_tag('ol',**{'class':'toc'})
for i,k in enumerate([x for x in KEYS if x!='perfil'],1):
 li=s.new_tag('li');label=s.new_tag('span',**{'class':'num'});label.string=f'{i:02}' if k!='fuentes' else 'A';li.append(label)
 name=s.new_tag('span');name.string=TITLES[k];li.append(name);ol.append(li)
toc.append(ol);body.append(toc)
for i,k in enumerate([x for x in KEYS if x!='perfil'],1):
 sec=s.new_tag('section',**{'class':'chapter'})
 n=s.new_tag('div',**{'class':'kicker'});n.string='SECCIÓN '+f'{i:02}' if k!='fuentes' else 'ANEXO';sec.append(n)
 title=s.new_tag('h1');title.string=TITLES[k];sec.append(title)
 sec.append(fragment(blocks[k]));body.append(sec)
text=str(s);HTML_OUT.parent.mkdir(exist_ok=True,parents=True);HTML_OUT.write_text(text,encoding='utf-8')
HTML(string=text,base_url=ROOT.as_uri()).write_pdf(PDF)
with fitz.open(PDF) as d:
 assert 24<=len(d)<=85,('Paginas inesperadas',len(d))
 assert 'La mayor empresa de comercio electrónico' in d[0].get_text()
 assert 'PERFIL' in d[1].get_text()
 alltext=' '.join(p.get_text() for p in d)
 assert 'Contenido' in alltext and '2.367' in alltext and '1.538' in alltext
 blank=[i+1 for i,p in enumerate(d) if len(p.get_text().strip())<8 and not p.get_image_info()]
 overs=[]
 for i,p in enumerate(d):
  for im in p.get_image_info():
   box=im['bbox']
   if box[0]<-1 or box[2]>p.rect.width+1:overs.append(i+1)
 assert not blank,('Paginas vacias',blank)
 assert not overs,('Imagenes recortadas',overs)
 assert sum(len(p.get_image_info()) for p in d)>=8
 pages=len(d)
 print('PDF_VALIDADO_R8',json.dumps({'paginas':pages,'imagenes':sum(len(p.get_image_info()) for p in d),'sinVacias':True,'sinRecortes':True},ensure_ascii=False))
m['informe']['pdf']={'ruta':PDF_REL,'sha256':hashlib.sha256(PDF.read_bytes()).hexdigest()}
m['informe']['html']=HTML_REL.split('/')[-1]
m['informe']['paginas']=pages
m['cierreEditorial']={'completo':False,'revision':REV,'contratoVersion':'1.5.4',
 'referenciaVisual':'PDF MELI R8 original de 31 páginas + NVIDIA R6',
 'pendientes':['Auditoría económica independiente y aprobación personal']}
doc['editorialVersion']='R10-ED4-ESTILO-R8'
doc['designReference']='MELI R8 + NVIDIA R6, sin diseño alternativo'
assert all(f[k]==v for k,v in original.items()),'Cambiaron archivos de otras empresas'
assert all(abs(m['libro']['valores'][k]-v)<.02 for k,v in EXPECTED.items())
assert len(f['catalogo.json']['empresas'])==19 and len(f)==39
new_raw=(json.dumps(lib,ensure_ascii=False,separators=(',',':'))+'\n').encode()
sha=hashlib.sha256(new_raw).hexdigest()
name='biblioteca-'+sha+'.json.gz'
(DATA/name).write_bytes(gzip.compress(new_raw,compresslevel=9,mtime=0))
MANIFEST.write_text(json.dumps({'schemaVersion':'jmr-biblioteca-gzip-1','app':'jmr-v2','archive':name,'sha256':sha},ensure_ascii=False,indent=1)+'\n')
print('RESTAURACION_LISTA',json.dumps({'pdf':PDF_REL,'pdfsha':m['informe']['pdf']['sha256'],
 'librarysha':sha,'paginas':pages,'valorBase':EXPECTED['base'],'MOS':mos,'otrasEmpresasSinCambio':18},ensure_ascii=False))
