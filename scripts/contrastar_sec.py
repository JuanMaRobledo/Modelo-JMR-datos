#!/usr/bin/env python3
"""Contrasta cada valoración guardada con la SEC (XBRL companyfacts, data.sec.gov).

Para cada empresa calcula, con el último informe 10-Q/10-K (o 20-F/40-F/6-K si hay XBRL):
  ingresos LTM, activos totales, patrimonio y deuda financiera;
y busca esas cifras en el análisis y el registro guardados. Un acierto prueba que el registro usa ese dato; un fallo NO prueba un error
(puede estar redondeado, en otra unidad o con otra definición): queda como «no encontrado» para revisión manual.
También informa si el registro usa un período anterior al último publicado y cuántos 8-K/6-K salieron después de su fecha.

Uso: python3 scripts/contrastar_sec.py [TICKER ...]   · escribe auditorias/revision-2026-10-26/sec/<T>.json y SEC.md
"""
import json, glob, re, sys, os, time, datetime as dt, urllib.request

UA = 'JMR Valuation juan0804@gmail.com'
SALIDA = 'auditorias/revision-2026-10-26'
COLOMBIA = {'GRUPOARGOS', 'GRUPOSURA', 'PFDAVVNDA', 'PFGRUPOARG', 'PFGRUPSURA'}
ALIAS = {'GOOG': 'GOOGL'}
REV = ['Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax', 'RevenueFromContractWithCustomerIncludingAssessedTax',
       'SalesRevenueNet', 'SalesRevenueGoodsNet', 'RevenuesNetOfInterestExpense', 'Revenue']
FORMS = ('10-Q', '10-K', '20-F', '40-F', '6-K', '10-K/A', '10-Q/A')


def get(url):
    time.sleep(0.2)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def d(s):
    return dt.date.fromisoformat(s)


def dur(x):
    return (d(x['end']) - d(x['start'])).days if x.get('start') else None


def serie(facts, tags, unit='USD'):
    out = []
    for ns in ('us-gaap', 'ifrs-full'):
        for t in tags:
            for u, xs in (facts.get(ns, {}).get(t, {}).get('units', {})).items():
                if unit == 'USD' and u == 'shares':
                    continue
                for x in xs:
                    if x.get('form') in FORMS:
                        out.append(dict(x, tag=t, unit=u, ns=ns))
        if out:
            break
    return out


def ltm(xs, fin):
    """Ingresos LTM para el cierre `fin` (fecha ISO): FY, o FY + YTD actual − YTD anterior."""
    cur = [x for x in xs if x['end'] == fin and x.get('start')]
    if not cur:
        return None
    anual = [x for x in cur if 350 <= dur(x) <= 380]
    if anual:
        return max(anual, key=lambda x: x['filed'])['val'], 'FY'
    ytd = max(cur, key=lambda x: (dur(x), x['filed']))
    s = d(ytd['start'])
    fy = [x for x in xs if x.get('start') and 350 <= dur(x) <= 380 and abs((d(x['end']) - s).days + 1) <= 10]
    prev = [x for x in xs if x.get('start') and abs((d(x['start']) - s).days - 365) <= 10 + 0 and abs((d(x['start']) - s).days + 365) <= 10]
    prev = [x for x in xs if x.get('start') and abs((d(x['start']) - (s - dt.timedelta(days=365))).days) <= 10 and abs((d(x['end']) - (d(fin) - dt.timedelta(days=365))).days) <= 10]
    if not fy or not prev:
        return None
    return max(fy, key=lambda x: x['filed'])['val'] + ytd['val'] - max(prev, key=lambda x: x['filed'])['val'], f"FY + {dur(ytd)}d − {dur(ytd)}d"


def instante(facts, tags, fin):
    for ns in ('us-gaap', 'ifrs-full'):
        for t in tags:
            xs = [x for u, v in facts.get(ns, {}).get(t, {}).get('units', {}).items() if u != 'shares' for x in v
                  if x.get('end') == fin and not x.get('start') and x.get('form') in FORMS]
            if xs:
                return max(xs, key=lambda x: x['filed'])['val']
    return None


def variantes(v, escala):
    """Formas en que el registro puede escribir una cifra, en millones (o en la escala dada)."""
    m = abs(v) / escala
    out = set()
    for k in (round(m) - 1, round(m), round(m) + 1):
        out |= {f'{k:,}', f'{k:,}'.replace(',', '.'), f'{k}'}
    out |= {f'{m:,.1f}', f'{m:,.1f}'.replace(',', 'X').replace('.', ',').replace('X', '.')}
    return {o for o in out if len(o.replace(',', '').replace('.', '')) >= 4}


def texto_registro(t):
    partes = []
    for p in glob.glob(f'analisis/{t}-*.json') + glob.glob(f'valoraciones/{t}-*.json'):
        partes.append(json.dumps(json.load(open(p, encoding='utf-8')), ensure_ascii=False))
    s = ' '.join(partes)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', s)


def encontrar(texto, vs):
    for x in sorted(vs, key=len, reverse=True):
        if re.search(r'(?<![\d.,])' + re.escape(x) + r'(?![\d])', texto):
            return x
    return None


def numeros(texto):
    """Todas las cifras del texto en forma de float, aceptando . o , como separador de miles o decimal."""
    out = []
    for m in re.finditer(r'(?<![\w.,])(\d{1,3}(?:[.,]\d{3})+(?:[.,]\d{1,2})?|\d+[.,]\d{1,2}|\d{3,})(?![\w])', texto):
        g = m.group(1)
        for sep_miles, sep_dec in ((',', '.'), ('.', ',')):
            try:
                out.append(float(g.replace(sep_miles, '').replace(sep_dec, '.')))
            except ValueError:
                pass
    return out


def cercano(texto, objetivo_M, tol=0.01):
    """Cifra del texto más próxima a `objetivo_M` (millones) dentro de la tolerancia relativa, o None."""
    mejor = None
    for x in set(numeros(texto)):
        if objetivo_M and abs(x - objetivo_M) <= abs(objetivo_M) * tol and x != 0:
            if mejor is None or abs(x - objetivo_M) < abs(mejor - objetivo_M):
                mejor = x
    return mejor


def fecha_registro(t):
    for p in glob.glob(f'valoraciones/{t}-*.json'):
        r = json.load(open(p, encoding='utf-8'))
        m = re.search(r'(\d{1,2})-(ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)\w*-(\d{4})', str(r.get('fecha', '')) + ' ' + str(r.get('precioReferenciaFuente', '')))
        meses = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
        if m:
            return dt.date(int(m.group(3)), meses.index(m.group(2)) + 1, int(m.group(1)))
        return d(str(r.get('savedAt'))[:10])


def analizar(t, ciks):
    sym = ALIAS.get(t, t)
    if sym not in ciks:
        return {'ticker': t, 'estado': 'SIN SEC', 'nota': 'No figura en company_tickers.json de la SEC (no presenta ante la SEC como emisor de EE.UU.).'}
    cik = f'{ciks[sym]:010d}'
    cf = get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json')
    facts = cf['facts']
    rev = serie(facts, REV)
    if not rev:
        return {'ticker': t, 'cik': cik, 'estado': 'SIN XBRL', 'nota': 'Sin ingresos en XBRL (20-F/6-K sin datos estructurados o tags no estándar).'}
    fines = sorted({x['end'] for x in rev if x.get('start')}, reverse=True)
    sub = get(f'https://data.sec.gov/submissions/CIK{cik}.json')['filings']['recent']
    informes = [(f, e, fo) for f, e, fo in zip(sub['filingDate'], sub['reportDate'], sub['form']) if fo in ('10-Q', '10-K', '20-F', '40-F')]
    ultimo_fin = max((e for _, e, _ in informes if e), default=None)
    texto = texto_registro(t)
    res = {'ticker': t, 'cik': cik, 'ultimo_informe': ultimo_fin, 'periodos': []}
    candidatos = [f for f in fines if f <= (ultimo_fin or '9999')][:4]
    escala = 1e6
    for fin in candidatos:
        l = ltm(rev, fin)
        if not l:
            continue
        v, how = l
        activos = instante(facts, ['Assets'], fin)
        patr = instante(facts, ['StockholdersEquity', 'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest', 'Equity'], fin)
        deuda = instante(facts, ['LongTermDebt', 'DebtAndCapitalLeaseObligations', 'LongTermDebtAndCapitalLeaseObligations'], fin)
        if deuda is None:
            partes = [instante(facts, k, fin) for k in (['LongTermDebtNoncurrent'], ['LongTermDebtCurrent', 'DebtCurrent'], ['CommercialPaper', 'ShortTermBorrowings'])]
            deuda = sum(p for p in partes if p) or None
        fila = {'cierre': fin, 'ingresos_ltm_M': round(v / escala, 1), 'metodo': how}
        for nombre, val in (('ingresos_ltm', v), ('activos', activos), ('patrimonio', patr), ('deuda', deuda)):
            if val is None:
                fila[nombre] = {'sec_M': None, 'en_registro': None}
                continue
            hit = encontrar(texto, variantes(val, escala))
            fila[nombre] = {'sec_M': round(val / escala, 1), 'en_registro': hit}
            if not hit and nombre == 'ingresos_ltm':
                fila[nombre]['aproximado_1pct'] = cercano(texto, val / escala)
        res['periodos'].append(fila)
    # período que usa el registro: el más reciente cuyo ingreso LTM aparece
    exacto = next((p['cierre'] for p in res['periodos'] if p['ingresos_ltm']['en_registro']), None)
    aprox = next((p['cierre'] for p in res['periodos'] if p['ingresos_ltm'].get('aproximado_1pct')), None)
    cand = [c for c in (exacto, aprox) if c]
    usado = max(cand) if cand else None       # el período más reciente que el registro reproduce (exacto o a ≤1 %)
    if usado and ultimo_fin and (d(ultimo_fin) - d(usado)).days > 400:
        res['coincidencia_descartada'] = usado  # cifra antigua que coincide por azar: no prueba nada
        usado = None
    res['periodo_usado'] = usado
    res['exacto'] = bool(usado) and usado == exacto
    res['forma_ultimo'] = next((fo for f, e, fo in informes if e == ultimo_fin), None)
    primero = res['periodos'][0]['cierre'] if res['periodos'] else None
    res['xbrl_al_dia'] = bool(primero and ultimo_fin and (d(ultimo_fin) - d(primero)).days <= 45)
    res['actualizado'] = bool(usado and usado == primero)
    fr = fecha_registro(t)
    posteriores = [(f, fo) for f, fo in zip(sub['filingDate'], sub['form']) if fo in ('8-K', '6-K') and d(f) > fr]
    res['fecha_registro'] = fr.isoformat()
    res['8K_posteriores'] = len(posteriores)
    res['8K_lista'] = posteriores[:8]
    res['informes_posteriores'] = [(f, e, fo) for f, e, fo in informes if d(f) > fr]
    if not res['xbrl_al_dia']:
        res['estado'] = 'XBRL SIN EL ÚLTIMO INFORME'
    elif not res['periodo_usado']:
        res['estado'] = 'SIN CONCILIAR'
    elif res['actualizado']:
        res['estado'] = 'CONCILIADO' if res['exacto'] else 'CONCILIADO ≤1 %'
        if res.get('forma_ultimo') in ('20-F', '40-F'):
            res['estado'] += ' (solo 20-F anual)'
    else:
        res['estado'] = 'PERIODO ANTERIOR'
    if res['forma_ultimo'] in ('20-F', '40-F'):
        res['nota'] = 'Emisor extranjero: el último informe con XBRL es anual; los trimestres van en 6-K sin datos estructurados.'
    return res


def main(argv):
    ciks = {v['ticker']: v['cik_str'] for v in get('https://www.sec.gov/files/company_tickers.json').values()}
    tickers = argv or sorted({json.load(open(p, encoding='utf-8'))['ticker'] for p in glob.glob('valoraciones/*.json')} - COLOMBIA)
    os.makedirs(f'{SALIDA}/sec', exist_ok=True)
    todos = []
    for t in tickers:
        try:
            r = analizar(t, ciks)
        except Exception as e:  # noqa: BLE001
            r = {'ticker': t, 'estado': 'ERROR', 'nota': f'{type(e).__name__}: {e}'}
        json.dump(r, open(f'{SALIDA}/sec/{t}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        todos.append(r)
        print(t, r['estado'], r.get('periodo_usado'), r.get('ultimo_informe'), flush=True)
    return todos


if __name__ == '__main__':
    main(sys.argv[1:])
