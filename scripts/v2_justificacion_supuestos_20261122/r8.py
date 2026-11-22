"""Inserta la sección «Justificación de cada supuesto» en los informes de diseño R8 (MELI, BSX, NU)
y la empalma en el PDF de XRX (sin HTML fuente), conservando diseño, portada y resto de páginas."""
import json, pathlib, re, sys, hashlib, fitz
from bs4 import BeautifulSoup
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from render_r8 import render, fetch
from weasyprint import HTML
S = pathlib.Path(sys.argv[1]); INF = pathlib.Path('/home/user/Modelo-JMR-datos/jmr-v2/informes')
lib = json.load(open(S/'bib_new.json')); F = lib['files']
MARCA = 'justificacion-supuestos-20261122'
def adaptar(frag, estilo):
    s = BeautifulSoup(frag, 'html.parser')
    for q in s.find_all('blockquote'):
        if estilo == 'meli': q['class'] = 'reading'
        else: q.name = 'div'; q['class'] = 'reading'
    if estilo == 'meli':
        for t in s.find_all('table'): t['class'] = 'finance'
    return s
res = {}
for t, estilo in [('BSX', 'r8'), ('NU', 'r8'), ('MELI', 'meli')]:
    e = F['empresas/'+t+'.json']; rev = e['revision']['id'] if isinstance(e['revision'], dict) else e['revision']
    hp = INF/t/f'{rev}_INFORME_FUNDAMENTAL.html'; pp = hp.with_suffix('.pdf')
    soup = BeautifulSoup(hp.read_text(encoding='utf-8'), 'html.parser')
    sec = [x for x in soup.find_all('section') if x.get('id') == 'supuestos' or (x.find('h1') and 'Supuestos y escenarios' in x.find('h1').get_text())]
    assert len(sec) == 1, t; sec = sec[0]
    old = sec.find(id=MARCA)
    if old: old.decompose()
    if t == 'MELI':
        for th in sec.find_all('th'):
            if 'reconstruida desde la auditoría de R9' in th.get_text():
                th.string = 'Hipótesis R10 verificadas en «Input sheet» del libro R10 (B26:B32, 22-nov-2026)'
        for p in sec.find_all('p'):
            if p.get_text().strip().startswith('Verificar contra Input sheet'):
                p.clear(); em = soup.new_tag('em')
                em.string = ('Verificado el 22-nov-2026 contra «Input sheet» del libro R10 (Google Sheets, fecha de valoración 19-nov-2026): '
                             'crecimiento 30 % / 20 %, margen 12 % → 15 % en el año 5, ventas/capital 3,5×, WACC 10,68 % inicial y terminal (override), ROIC terminal 18 % y g 4 %.')
                p.append(em)
    frag = (S/'frag'/f'{t}.html').read_text()
    sec.append(adaptar(frag, estilo))
    hp.write_text(str(soup), encoding='utf-8')
    n = render(hp, pp)
    res[t] = {'html': str(hp), 'pdf': str(pp), 'paginas': n, 'sha256': hashlib.sha256(pp.read_bytes()).hexdigest()}
# ---- XRX: empalme del capítulo 10 ----
t = 'XRX'; e = F['empresas/XRX.json']; rev = e['revision']['id']
pp = INF/t/f'{rev}_INFORME_FUNDAMENTAL.pdf'
orig = fitz.open(pp)
ini = [i for i, p in enumerate(orig) if p.get_text().startswith('SECCIÓN 10\nSupuestos y escenarios')]
fin = [i for i, p in enumerate(orig) if p.get_text().startswith('SECCIÓN 11\nValoración')]
assert len(ini) == 1 and len(fin) == 1, (ini, fin)
a, b = ini[0], fin[0]            # páginas [a, b) del capítulo 10 (índice 0)
bsx = (INF/'BSX'/'BSX-V2-LTM20260930-R2_INFORME_FUNDAMENTAL.html').read_text(encoding='utf-8')
css = bsx[bsx.index('<style>')+7:bsx.index('</style>')].replace('Modelo JMR V2 · Boston Scientific · En revisión', 'Modelo JMR V2 · XRX · EN REVISIÓN')
css += '@page:first{counter-reset:page %d}' % (a+1)
cuerpo = BeautifulSoup(F['analisis/XRX.json']['blocks']['supuestos'], 'html.parser')
for q in cuerpo.find_all('blockquote'): q.name = 'div'; q['class'] = 'reading'
html = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>XRX capítulo 10</title><style>'+css+'</style></head><body>'
        '<section class="chapter" id="supuestos" style="break-before:auto"><div class="kicker">SECCIÓN 10</div><h1>Supuestos y escenarios</h1>'
        + str(cuerpo) + '</section></body></html>')
tmp = S/'xrx_cap10.pdf'; (S/'xrx_cap10.html').write_text(html, encoding='utf-8')
HTML(string=html, base_url=(INF/'BSX').resolve().as_uri()+'/', url_fetcher=fetch).write_pdf(tmp)
cap = fitz.open(tmp); delta = len(cap) - (b - a)
out = fitz.open()
out.insert_pdf(orig, from_page=0, to_page=a-1)
out.insert_pdf(cap)
out.insert_pdf(orig, from_page=b, to_page=len(orig)-1)
# Renumerar el pie de las páginas posteriores al capítulo (mismo tipo y posición).
if delta:
    for i in range(a+len(cap), len(out)):
        pg = out[i]; viejo = str(i+1-delta); nuevo = str(i+1)
        hits = [r for r in pg.search_for(viejo) if r.y0 > pg.rect.height-40 and r.x0 > pg.rect.width*0.8]
        assert hits, ('pie no encontrado', i+1)
        r = hits[-1]
        sp = [s for blk in pg.get_text('dict')['blocks'] for l in blk.get('lines', []) for s in l['spans'] if s['text'].strip() == viejo and s['bbox'][1] > pg.rect.height-40]
        size = sp[-1]['size'] if sp else 7; color = sp[-1]['color'] if sp else 0x555555
        pg.add_redact_annot(r, fill=(1, 1, 1)); pg.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
        rgb = tuple(((color >> k) & 255)/255 for k in (16, 8, 0))
        pg.insert_text((r.x1 - fitz.get_text_length(nuevo, fontname='helv', fontsize=size), r.y1 - 1.6), nuevo, fontname='helv', fontsize=size, color=rgb)
out.save(S/'xrx_new.pdf', garbage=3, deflate=True)
pathlib.Path(pp).write_bytes((S/'xrx_new.pdf').read_bytes())
res['XRX'] = {'pdf': str(pp), 'paginas': len(out), 'capitulo10': [a+1, a+len(cap)], 'delta': delta, 'sha256': hashlib.sha256(pp.read_bytes()).hexdigest()}
json.dump(res, open(S/'r8_resultado.json', 'w'), indent=1)
print(json.dumps(res, indent=1))
