#!/usr/bin/env python3
"""Resuelve la retención de pesos de NKE, PYPL, EPAM, ZTS, NVO y ONON: integra desde la hoja los 15 descuentos nativos y los pesos
(categoría de empresa de la hoja), regenera la sección de múltiplos del Nivel 2 y conserva los originales en evidencia/descuentos-20261101/respaldo/.
No cambia DCF, MOS, escenarios, supuestos ni matrices."""
import copy, hashlib, json, re, shutil, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from integrar_descuentos_nativos import integrate
EV = ROOT / 'evidencia/descuentos-20261101'
cat = json.loads((ROOT / 'catalogo.json').read_text())
info = json.loads((EV / 'categorias_pesos.json').read_text())
SIX = ['NKE', 'PYPL', 'EPAM', 'ZTS', 'NVO', 'ONON']
RAZON = {
 'NKE': 'Madura: marca global consolidada con crecimiento moderado y márgenes cíclicos; el DCF pesa 40 % y los relativos 60 %, con más peso en EV/EBITDA y P/E, los múltiplos que más usa el mercado para consumo maduro.',
 'PYPL': 'Madura: plataforma de pagos con crecimiento de un dígito y recompras; mismo reparto que NKE, con EV/EBITDA y P/E como relativos principales.',
 'EPAM': 'Genérico: servicios de TI sin rasgo dominante de crecimiento ni defensivo; reparto equilibrado 50 % DCF y 10 % por cada uno de los cinco relativos.',
 'ZTS': 'Defensiva: salud animal con demanda estable y caja predecible; 30 % DCF y 70 % relativos, con P/E y EV/EBITDA como anclas de mercado.',
 'NVO': 'Biotech/Farma: valor concentrado en flujos de cartera de productos; 55 % DCF y relativos con más peso en EV/FCFF (20 %) por la caja operativa.',
 'ONON': 'Crecimiento: marca de rápido crecimiento con márgenes aún en convergencia; 60 % DCF y 40 % relativos, con más peso en EV/FCFF y EV/EBITDA.'}
MET = ['EV/EBITDA', 'EV/FCFF', 'P/E', 'P/FCFE', 'P/OCF']
num = lambda x: isinstance(x, (int, float)) and not isinstance(x, bool)
f2 = lambda x, d=2: f'{x:,.{d}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
pc = lambda x: f2(x * 100, 1) + ' %'

def bloque(t, v, d, rows, sha):
    cab = ''.join(f'<th>{c}</th>' for c in ['Método', 'Peso total', 'Escenario', 'FY+1', 'FY+2', 'FY+3', 'VP1', 'VP2', 'VP3', 'Consolidado hoy'])
    filas = ''
    for m in d['metodos']:
        for sc in ('conservador', 'base', 'optimista'):
            x = m[sc]; filas += '<tr>' + ''.join(f'<td>{c}</td>' for c in [m['nombre'], pc(m['peso']), sc] + [f2(z) for z in x['fy'] + x['vp']] + [f2(x['consolidado'])]) + '</tr>'
    s = d['resumenNativo']
    resu = ''.join(f'<tr><td>{k}</td>' + ''.join(f'<td>{f2(s[key][sc])}</td>' for sc in ('conservador', 'base', 'optimista')) + '</tr>'
                   for k, key in (('DCF', 'dcfHoy'), ('Múltiplos consolidados', 'multiplesHoy'), ('Ponderado DCF + múltiplos', 'ponderadoHoy')))
    return (f'<p>Estado técnico: METODOS_Y_CONSOLIDACION_CONCILIADOS. Auditoría económica independiente pendiente. Pesos de la hoja por categoría de empresa «{info[t]["categoria"][0][0]}» '
            f'(juicio del analista, no evidencia): DCF {pc(d["pesoDcf"])} y múltiplos {pc(d["pesoMultiplos"])}. {RAZON[t]}</p>'
            f'<div class="table-scroll"><table><thead><tr>{cab}</tr></thead><tbody>{filas}</tbody></table></div>'
            f'<div class="table-scroll"><table><thead><tr><th>Valor a hoy (US$/acción)</th><th>Conservador</th><th>Base</th><th>Optimista</th></tr></thead><tbody>{resu}</tbody></table></div>'
            f'<p>Fotografía SHA256: <code>{sha}</code>. Valores y fórmulas conservados en evidencia/descuentos-20261101/; la versión anterior (pesos genéricos 60/40 y escenarios conservador y optimista sin resultado) se conserva en evidencia/descuentos-20261101/respaldo/. '
            'P/S y P/BV son complementarios opcionales y no se calculan ni ponderan.</p></section>')

resumen = {}
for t in SIX:
    vp = next(p for p in cat['valoraciones'] if '/' + t + '-' in p); ap = next(p for p in cat['analisis'] if '/' + t + '-' in p)
    v0 = json.loads((ROOT / vp).read_text()); a0 = json.loads((ROOT / ap).read_text()); rev = v0['revisionId']
    bk = EV / 'respaldo' / t; bk.mkdir(parents=True, exist_ok=True)
    for src in (vp, ap):
        if not (bk / Path(src).name).exists(): shutil.copy(ROOT / src, bk / Path(src).name)
    uf = EV / f'{rev}-UNFORMATTED_VALUE.json'; ff = EV / f'{rev}-FORMULA.json'
    cap = json.loads(uf.read_text()); frm = json.loads(ff.read_text())
    sha = hashlib.sha256(uf.read_bytes()).hexdigest()
    v = integrate(copy.deepcopy(v0), cap, frm, sha)
    rows = cap['values']; d = v['descuentoMultiples']
    d['pesoDcf'] = rows[37][1]; d['pesoMultiplos'] = rows[38][1]; d['criterio'] = rows[5][1]; d['costoPatrimonio'] = rows[4][1]
    d['chequeo'] = 'CONCILIADO_NATIVO_EN_REVISION'
    assert abs(d['pesoDcf'] + d['pesoMultiplos'] - 1) < 1e-9 and abs(sum(m['peso'] for m in d['metodos']) - d['pesoMultiplos']) < 1e-9, t
    ii = d['integracionNativa']; ii['fechaCaptura'] = '2026-11-01'; ii['categoriaEmpresa'] = info[t]['categoria'][0][0]
    ii['justificacionPesos'] = RAZON[t]; ii['respaldoAnterior'] = f'evidencia/descuentos-20261101/respaldo/{t}/'
    for m in v['metodos']:
        if 'DCF' in m['nombre']: m['peso'] = d['pesoDcf']
        elif m['nombre'] in MET: m['peso'] = next(x['peso'] for x in d['metodos'] if x['nombre'] == m['nombre'])
    for k in v0:   # nada fuera de descuentoMultiples y metodos puede cambiar
        if k not in ('descuentoMultiples', 'metodos'): assert v[k] == v0[k], (t, k)
    assert v['valorPrincipal'] == v0['valorPrincipal']
    (ROOT / vp).write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
    a = copy.deepcopy(a0); h = a['calculationHtml']
    i = h.index('<p>Estado técnico:'); j = h.index('</p></section>', h.index('Fotografía SHA256', i)) + len('</p></section>')
    a['calculationHtml'] = h[:i] + bloque(t, v, d, rows, sha) + h[j:]
    a['html'] = a['articleHtml'] + a['calculationHtml']
    (ROOT / ap).write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
    resumen[t] = {'categoria': info[t]['categoria'][0][0], 'pesoDcf': d['pesoDcf'], 'pesoMultiplos': d['pesoMultiplos'], 'pesos': {m['nombre']: m['peso'] for m in d['metodos']},
                  'antes': {'pesoDcf': v0['descuentoMultiples'].get('pesoDcf'), 'pesoMultiplos': v0['descuentoMultiples'].get('pesoMultiplos')}, 'ponderadoHoy': d['ponderadoHoy'], 'dcfHoy': d['dcfHoy'], 'multiplesHoy': d['multiplesHoy']}
    print(t, rev, 'DCF', round(d['pesoDcf'], 3), 'mult', round(d['pesoMultiplos'], 3), 'ponderado base', round(d['ponderadoHoy']['base'], 2), 'DCF base', round(d['dcfHoy']['base'], 2))
(EV / 'resumen_resolucion.json').write_text(json.dumps(resumen, ensure_ascii=False, indent=1))
