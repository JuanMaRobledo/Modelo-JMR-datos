#!/usr/bin/env python3
"""Conciliación de SOLO LECTURA hoja Google ↔ JSON activo para las 23 valoraciones del catálogo.
No escribe en hojas ni en valoraciones. Salida: evidencia/reconciliacion-hoja-json-20261101/<T>.json y resumen.json."""
import json, re, sys, time
from pathlib import Path
sys.path.insert(0, '/home/user/JMR-valuation')
from jmr_valuation.io.sheets_auth import get_gspread_client
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'evidencia/reconciliacion-hoja-json-20261101'
cat = json.loads((ROOT / 'catalogo.json').read_text())
cl = get_gspread_client()
num = lambda x: isinstance(x, (int, float)) and not isinstance(x, bool)
RNG = {'b35': "'Valuation output'!B35", 'k': "'Escenarios e historias'!H5:K8", 'desc': "'Descuento de múltiplos'!A1:K60",
       'sup': "'Supuestos de los Múltiplos'!A5:H12", 'sens': "'Sensibilidad por múltiplo'!A76:I144",
       'gates': "'Input sheet'!B85", 'g2': "'Input sheet'!B108", 'g3': "'Cost of capital worksheet'!B84", 'rf': "'Input sheet'!B35", 'tw': "'Input sheet'!B47", 'tw_on': "'Input sheet'!B46",
       'price': "'Input sheet'!B23", 'dt': "'Input sheet'!B4"}
def get(sh, rng):
    try:
        r = sh.values_batch_get([rng], params={'valueRenderOption': 'UNFORMATTED_VALUE'})['valueRanges'][0]
        return r.get('values', [])
    except Exception as e:
        return {'error': str(e)[:90]}
def first(x): return x[0][0] if isinstance(x, list) and x and x[0] else None
res = {}
for p in cat['valoraciones']:
    v = json.loads((ROOT / p).read_text()); t = v['ticker']
    sid = v.get('sheet_id') or re.search(r'/d/([\w-]+)', v.get('hojaGoogle', '')).group(1)
    r = {'ticker': t, 'revision': v['revisionId'], 'sheet_id': sid}
    try:
        sh = cl.open_by_key(sid); r['titulo'] = sh.title[:70]; r['tabs'] = len(sh.worksheets())
    except Exception as e:
        r['error_abrir'] = str(e)[:100]; res[t] = r; print(t, 'NO ABRE', r['error_abrir']); continue
    d = {k: get(sh, rg) for k, rg in RNG.items()}
    time.sleep(1.2)
    r['b35'] = first(d['b35']); r['json_base'] = v['valorPrincipal']
    r['dcf_coincide'] = num(r['b35']) and abs(r['b35'] - v['valorPrincipal']) < 0.01
    k = d['k'] if isinstance(d['k'], list) else []
    r['k5_k8'] = [row[3] if len(row) > 3 else None for row in k]; r['h5_h8'] = [row[0] if row else None for row in k]
    r['gates'] = {'B85': first(d['gates']), 'B108': first(d['g2']), 'WACC_B84': first(d['g3'])}
    r['rf'] = first(d['rf']); r['wacc_terminal_override'] = [first(d['tw_on']), first(d['tw'])]
    r['precio_hoja'] = first(d['price']); r['json_precio'] = v.get('precio')
    desc = d['desc'] if isinstance(d['desc'], list) else []
    find = lambda lab: next((i for i, x in enumerate(desc) if x and str(x[0]).startswith(lab)), None)
    i_dcf = find('DCF · valor'); i_mult = find('Múltiplos consolid')
    r['desc_pesos_hoja'] = {'dcf': desc[i_dcf][1] if i_dcf is not None and len(desc[i_dcf]) > 1 else None}
    # consolidado hoy por método (bloque BASE): primera aparición de cada método tras el encabezado BASE
    i_base = next((i for i, x in enumerate(desc) if x and str(x[0]).strip().upper() == 'BASE'), None)
    cons = {}; pesos = {}
    if i_base is not None:
        for row in desc[i_base + 2:i_base + 7]:
            if row and len(row) > 9: cons[row[0]] = row[9]; pesos[row[0]] = row[1]
    r['desc_consolidado_base_hoja'] = cons; r['desc_pesos_metodos_hoja'] = pesos
    jd = v.get('descuentoMultiples') or {}
    jc = {m['nombre']: (m.get('base') or {}).get('consolidado') for m in jd.get('metodos', [])}
    jp = {m['nombre']: m.get('peso') for m in jd.get('metodos', [])}
    r['json_pesos'] = {'dcf': jd.get('pesoDcf'), 'mult': jd.get('pesoMultiplos'), 'metodos': jp}
    r['consolidado_coincide'] = {m: (num(cons.get(m)) and num(jc.get(m)) and abs(cons[m] - jc[m]) < 0.01) for m in jc}
    r['pesos_coinciden'] = (num(r['desc_pesos_hoja']['dcf']) and num(jd.get('pesoDcf')) and abs(r['desc_pesos_hoja']['dcf'] - jd['pesoDcf']) < 1e-6)
    sens = d['sens'] if isinstance(d['sens'], list) else []
    ctl = {}
    for n_, r0 in (('EV/EBITDA', 8), ('EV/FCFF', 18), ('P/E', 28), ('P/FCFE', 38), ('P/OCF', 48), ('P/V', 58), ('P/BV', 68)):
        row = sens[r0] if len(sens) > r0 else []
        ctl[n_] = row[8] if len(row) > 8 else None
    r['sens_control_hoja'] = ctl
    jm = {m.get('metodo'): m.get('estado') for m in (v.get('sensibilidadMultiples') or {}).get('matrices', []) if isinstance(m, dict)}
    r['sens_json'] = jm
    sup = d['sup'] if isinstance(d['sup'], list) else []
    r['override_manual'] = {row[0]: (str(row[4])[:12] if len(row) > 4 else None) for row in sup if row and row[0] in ('EV/FCFF', 'P/OCF', 'P/E', 'P/FCFE', 'EV/EBITDA')}
    (OUT / f'{t}.json').write_text(json.dumps(r, ensure_ascii=False, indent=1, default=str)); res[t] = r
    print(t, 'DCF', r['dcf_coincide'], 'K', r['k5_k8'], 'pesos', r['pesos_coinciden'], 'cons', sum(r['consolidado_coincide'].values()), '/', len(r['consolidado_coincide']))
(OUT / 'resumen.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str))
