"""Completa el contrato de integridad (valorPrincipal, seleccionMultiples, sensibilidadMultiples) de un registro recuperado.

Solo LEE la hoja de Google del registro (credencial de servicio de JMR-valuation) y copia cifras ya calculadas por sus fórmulas:
nunca recalcula precios, no cambia supuestos ni pesos. Falla si el DCF Base de la hoja no coincide con el registro o si una
matriz de sensibilidad de múltiplos no concilia con su VP FY+3.

Uso (desde Modelo-JMR-datos, con JMR-valuation hermano):  python3 scripts/completar_contrato_registro.py TICKER [TICKER ...]
"""
import copy, glob, json, math, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT.parent / 'JMR-valuation')]
from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

METHODS = ['EV/EBITDA', 'EV/FCFF', 'P/E', 'P/FCFE', 'P/OCF', 'P/V', 'P/BV']
TABS = ['EVEBITDA', 'EVFCFF', 'PE', 'PFCFE', 'POCF', 'PV', 'PBV']
SCEN = ['conservador', 'base', 'optimista']
fin = lambda x: isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)  # noqa: E731
near = lambda a, b: fin(a) and fin(b) and abs(a - b) <= max(1e-7, abs(b) * 1e-10)  # noqa: E731


def cell(grid, a):
    m = re.match(r'([A-Z]+)(\d+)', a)
    col = 0
    for ch in m[1]:
        col = col * 26 + ord(ch) - 64
    r, c = int(m[2]) - 1, col - 1
    try:
        v = grid[r][c]
    except IndexError:
        return None
    return v if v != '' else None


def sincronizar_cinco_metodos(a, dm):
    """Lleva a la copia del registro las cifras de EV/EBITDA, EV/FCFF, P/E, P/FCFE y P/OCF que calcula 'Descuento de múltiplos'."""
    d = a['descuentoMultiples']
    pesos_m = sum(x['peso'] for x in d['metodos'])
    for mi, m in enumerate(METHODS[:5]):
        x = next(z for z in d['metodos'] if z['nombre'] == m)
        y = next(z for z in a['metodos'] if z['nombre'] == m)
        for si, k in enumerate(SCEN):
            r = [11, 20, 29][si] + mi
            fy = [cell(dm, f'{c}{r}') for c in 'DEF']
            vp = [cell(dm, f'{c}{r}') for c in 'GHI']
            if not all(fin(v) for v in fy + vp):
                continue
            x[k].update(fy=fy, vp=vp, consolidado=cell(dm, f'J{r}'))
            y[k] = fy[2]
    act = [z for z in d['metodos'] if z['peso'] > 0]
    d['vp3'] = {k: sum(z['peso'] * z[k]['vp'][2] for z in act) / pesos_m for k in SCEN}
    for k in SCEN:
        d['consolidado'][k] = {'fy': [sum(z['peso'] * z[k]['fy'][n] for z in act) / pesos_m for n in range(3)],
                               'vp': [sum(z['peso'] * z[k]['vp'][n] for z in act) / pesos_m for n in range(3)], 'consolidado': d['multiplesHoy'][k]}
    d['chequeo'] = {'multiplosFY3SinDescontar': {k: cell(dm, f'{c}47') for k, c in zip(SCEN, 'CDE')},
                    'multiplosVP3': {k: cell(dm, f'{c}48') for k, c in zip(SCEN, 'CDE')},
                    'resultado': {k: cell(dm, f'{c}49') for k, c in zip(SCEN, 'CDE')}}
    for k, c in zip(SCEN, 'CDE'):
        v = cell(dm, f'{c}50')
        if fin(v):
            a['objetivoPonderado'][k] = v
    a['valorPresentePonderado'] = d['ponderadoHoy']


def main(tickers):
    gc = get_gspread_client()
    for t in tickers:
        p = glob.glob(str(ROOT / f'valoraciones/{t}-*.json'))[0]
        a = json.load(open(p))
        sid = re.search(r'/d/([\w-]+)', a['hojaGoogle'])[1]
        sh = gc.open_by_key(sid)
        rng = ["'Sensibilidad por múltiplo'!A1:I230", "'Resumen de Valoración'!A1:E40"] + [f"'{x}'!A1:J45" for x in TABS] + ["'Descuento de múltiplos'!A1:K50"]
        vr = sh.values_batch_get(rng, params={'valueRenderOption': 'UNFORMATTED_VALUE'})['valueRanges']
        sens, resumen, tabs = vr[0].get('values', []), vr[1].get('values', []), [x.get('values', []) for x in vr[2:9]]
        sincronizar_cinco_metodos(a, vr[9].get('values', []))
        base = cell(resumen, 'D32')
        dcf = (a.get('valorEsperado') or {}).get('dcfBase')
        if not near(base, dcf):
            raise SystemExit(f'{t}: DCF Base de la hoja {base} != registro {dcf}; requiere auditar supuestos')
        controles = []
        for k in SCEN:
            for mi, m in enumerate(METHODS):
                if k != 'base':  # regla vigente (REGLAS_VIGENTES §8): matrices de múltiplos solo en Base
                    controles.append({'metodo': m, 'escenario': k, 'centro': None, 'vp3Original': None, 'estado': 'N/D', 'formulaErrors': [],
                                      'motivo': 'Sin matriz por regla vigente: sensibilidad de múltiplos solo Base'})
                    continue
                r = 76 + mi * 10
                centro, original = cell(sens, f'D{r + 5}'), cell(sens, f'G{r + 8}')
                if not (fin(centro) and fin(original) and near(centro, original)):
                    raise SystemExit(f'{t}: matriz Base {m} no concilia (centro {centro} vs VP FY+3 {original})')
                controles.append({'metodo': m, 'escenario': k, 'centro': centro, 'vp3Original': original, 'estado': 'OK', 'formulaErrors': []})
        ok = sum(c['estado'] == 'OK' for c in controles)
        a['valorPrincipal'] = base
        a['metodoPrincipal'] = 'DCF FCFF'
        a['sensibilidadMultiples'] = {'version': 'matrices-por-bloque-20261027', 'methods': 7, 'scenarios': SCEN, 'disrupcionFuera': True, 'sourceSheet': sid,
                                      'lastExport': '2026-10-27', 'controlesOK': ok, 'noDisponibles': 21 - ok, 'errores': 0, 'controles': controles,
                                      'seleccion': 'Pesos y criterio de la hoja vigente; contadores por matriz, no por celda',
                                      'economica': {'controlesOK': 0, 'noDisponibles': 0, 'errores': 0, 'controles': [], 'version': '20261027',
                                                    'nota': 'Matrices económicas no incluidas en la plantilla vigente (22-oct-2026)'}}
        pesos = {m['nombre']: m['peso'] for m in a['metodos']}
        total = sum(pesos[m] for m in METHODS)
        estados = {m['nombre']: m.get('estado') for m in a['descuentoMultiples']['metodos']}
        metodos = []
        for m, tab, g in zip(METHODS, TABS, tabs):
            w = pesos[m]
            salida = {k: (cell(g, f'J{r}') if fin(cell(g, f'J{r}')) else None) for k, r in zip(SCEN, (8, 19, 30))}
            calc_ok = all(c['estado'] == 'OK' for c in controles if c['metodo'] == m and c['escenario'] == 'base')  # solo Base tiene matriz
            metodos.append({'nombre': m, 'rol': 'Seleccionado' if w > 0 else 'No ponderar',
                            'criterio': 'Múltiplo de salida y peso leídos de la hoja vigente (27-oct-2026); anclas y pares sin recertificar.',
                            'control': 'OK · advertencias económicas' if calc_ok else 'N/D', 'controlCalculo': 'OK' if calc_ok else 'N/D',
                            'pesoRelativo': w / total if total else 0, 'pesoValido': w / total if total else 0, 'pesoVigente': w,
                            'estado': estados.get(m), 'historico': None, 'justificadoEstable': None, 'proxySectorial': None, 'salida': salida})
        a['seleccionMultiples'] = {'version': f'{t}-seleccion-20261027', 'noReponderaDCF': True, 'metodos': metodos,
                                   'advertencia': 'Pesos y múltiplos de salida leídos de la hoja vigente. Los pares y anclas no se presumen homogéneos ni actuales.'}
        json.dump(a, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        open(p, 'a').write('\n')
        for q in glob.glob(str(ROOT / f'analisis/{t}-research-*.json')):  # análisis vinculado: misma copia del registro
            j = json.load(open(q))
            for k in ('valorPrincipal', 'metodoPrincipal', 'sensibilidadMultiples', 'seleccionMultiples'):
                j[k] = copy.deepcopy(a[k])
            sp = (j.get('linkedValuation') or {}).get('sourcePath')
            j['linkedValuation'] = copy.deepcopy(a)
            j['linkedValuation']['sourcePath'] = sp or str(Path(p).relative_to(ROOT))
            open(q, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, separators=(',', ':')) + '\n')
        print(t, 'principal', base, 'matrices OK', ok, 'N/D', 21 - ok)


if __name__ == '__main__':
    main([x.upper() for x in sys.argv[1:]])
