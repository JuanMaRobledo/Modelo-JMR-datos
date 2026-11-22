import json, gzip, hashlib, pathlib, shutil, subprocess
S = pathlib.Path('/tmp/claude-0/-home-user/02bdd347-b8be-5ac5-b2fc-27257db31770/scratchpad/sc6'); DATA = pathlib.Path('/home/user/Modelo-JMR-datos/jmr-v2')
XL = json.load(open(S/'xlsx_sha.json'))
for t, d in {'NVDA': '11l8CYR0R26QxAMy-atCouNQoxMbkV2it', 'MSFT': '1mQDAS6jRMYMXLAsyXpxlipshQDB-sWE3', 'GOOGL': '1rlh7a4ajgslrqszdZu2btiIOJVCyimUH', 'AMZN': '1QjCWYpu0ZDq74Zxq4Hq8gPyZ3EDWfI0K', 'EPAM': '1gyVOpRWUpuRuqC77lalsbuCEnZ1KdZWn', 'ONON': '1BSXE23qPakQuDDxanG5MG1SQb-2ymLxz'}.items(): XL[t]['drive'] = d
NEWSHEET = {'EPAM': '1RST5bVljIl9Go2Ioj6E5Rkq1HhpeMrD5VFRVQ8pyatg', 'ONON': '1UpNANvTTVYxhuMYTyQJISRppxBgoVVF5PdaXWcIzRoE'}
SIX = ['MSFT', 'NVDA', 'GOOGL', 'AMZN', 'ONON', 'EPAM']
m = json.load(open(DATA/'biblioteca.json')); pub = json.loads(gzip.open(DATA/m['archive']).read())['files']
new = json.load(open(S/'lib_b.json'))['files']
O = S/'final_origen'
if O.exists(): shutil.rmtree(O)
for k, v in pub.items():
    if k == 'catalogo.json': continue
    p = O/k; p.parent.mkdir(parents=True, exist_ok=True); json.dump(v, open(p, 'w'), ensure_ascii=False, indent=1)
inv = json.load(open(S/'r_in/inventario.json'))['empresas']; info = {}
for r in inv:
    t = r['ticker']; meta = json.load(open(S/'r_in'/t/'meta.json'))
    src = S/'r_in'/t/meta['pdf']; dst = DATA/'informes'/t/meta['pdf']
    if not dst.exists(): shutil.copyfile(src, dst)
    assert dst.read_bytes() == src.read_bytes(); info[t] = {'ruta': 'jmr-v2/informes/%s/%s' % (t, meta['pdf']), 'paginas': r['paginas'], 'sha256': hashlib.sha256(dst.read_bytes()).hexdigest()}
for t in SIX:
    e = new['empresas/%s.json' % t]; a = new['analisis/%s.json' % t]; v = info[t]
    e['estado'] = pub['empresas/%s.json' % t]['estado']
    L = e['libro']; X = XL[t]
    if t in NEWSHEET:
        sid = NEWSHEET[t]; url = 'https://docs.google.com/spreadsheets/d/%s/edit' % sid
        L['url'] = url; L['googleSheetId'] = sid
        if isinstance(L.get('googleSheets'), dict): L['googleSheets'] = {**L['googleSheets'], 'id': sid, 'url': url}
        e['documentLinks'] = {**e.get('documentLinks', {}), 'workbook': url, 'workbookGoogleSheets': url}
    L['sha256'] = X['sha256']
    if 'sha256Formato' in L: L['sha256Formato'] = X['sha256']
    exc = {'id': X['archivo'], 'url': 'https://drive.google.com/file/d/%s/view' % X['drive'], 'sha256': X['sha256'], 'origen': 'Exportación .xlsx de la Google Sheet oficial, 22-nov-2026'}
    L['excel'] = {**exc, 'anterior': L['excel']} if isinstance(L.get('excel'), dict) else exc
    L['excelSha256'] = X['sha256']
    inf = e.get('informe')
    if isinstance(inf, dict):
        for k_ in list(inf):
            if isinstance(inf[k_], str) and inf[k_].endswith('.pdf'): inf[k_] = v['ruta']
        if isinstance(inf.get('pdf'), dict): inf['pdf'].update({'ruta': v['ruta'], 'sha256': v['sha256']})
        if 'sha256Pdf' in inf: inf['sha256Pdf'] = v['sha256']
        if 'paginas' in inf: inf['paginas'] = v['paginas']
    ce = e.get('cierreEditorial')
    if isinstance(ce, dict):
        e['cierreEditorial'] = {'completo': False, 'pendientes': ['Nueva revisión %s (22-nov-2026, ventas/capital según Damodaran): rehacer el manifiesto de cierre (analisis/%s.cierre.json) con las huellas y páginas del nuevo PDF.' % (e['revision']['id'], t)], 'anterior': ce if not ce.get('anterior') else ce.get('anterior')}
    json.dump(e, open(O/'empresas'/f'{t}.json', 'w'), ensure_ascii=False, indent=1); json.dump(a, open(O/'analisis'/f'{t}.json', 'w'), ensure_ascii=False, indent=1)
subprocess.run(['node', '/home/user/Modelo-JMR-datos/scripts/v2_correcciones_20261122/lib_desde_origen.mjs', str(O), str(S/'lib_final.json')], check=True)
lib = json.load(open(S/'lib_final.json')); F = lib['files']
# controles: nada fuera de las seis cambia salvo su fila de catálogo
for k in pub:
    if k == 'catalogo.json': continue
    if not any(k.endswith('/%s.json' % t) for t in SIX): assert F[k] == pub[k], k
c0 = {x['ticker']: x for x in pub['catalogo.json']['empresas']}; c1 = {x['ticker']: x for x in F['catalogo.json']['empresas']}
assert set(c0) == set(c1); print('catálogo cambia en', sorted(t for t in c0 if c0[t] != c1[t]))
raw = (json.dumps(lib, ensure_ascii=False, separators=(',', ':')) + '\n').encode()
sha = hashlib.sha256(raw).hexdigest(); name = 'biblioteca-' + sha + '.json.gz'
(DATA/name).write_bytes(gzip.compress(raw, compresslevel=9, mtime=0))
(DATA/'biblioteca.json').write_text(json.dumps({'schemaVersion': 'jmr-biblioteca-gzip-1', 'app': 'jmr-v2', 'archive': name, 'sha256': sha}, ensure_ascii=False, indent=1) + '\n')
json.dump(info, open(S/'pdfs6.json', 'w'), indent=1); print(name, info)
