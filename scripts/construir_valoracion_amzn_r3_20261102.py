#!/usr/bin/env python3
"""Construye el JSON de valoración A-1.2 de AMZN-20261102-A12-R3 a partir de la captura completa de su hoja (fase 2, 2-nov-2026).

Misma regla que construir_valoracion_hoja_20261101.py: solo copia celdas ya calculadas por la hoja (UNFORMATTED_VALUE) y verifica
centros de matrices = VP3 del método, controles OK, DCF Base = Valuation output!B35 y pesos que suman 1. No recalcula ni inventa.
Diferencias de AMZN: EV/FCFF y P/FCFE son N/A por flujo FY+3 negativo (la hoja calcula su VP negativo con el ancla C como múltiplo de
salida y peso 0, como SHAK/MELI); P/V y P/BV son complementarios no utilizados (N/D). Aislamiento: esqueleto propio de AMZN.
Uso: python3 scripts/construir_valoracion_amzn_r3_20261102.py
"""
import hashlib, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TICKER, REV = 'AMZN', 'AMZN-20261102-A12-R3'
CAP = ROOT / f'evidencia/captura-hoja-20261102/{REV}_resultados_hoja.json'
OUT = ROOT / f'candidatos/valoraciones/{REV}/VALORACION_A12_EN_REVISION.json'
INV = ROOT / f'candidatos/valoraciones/{REV}/dcf_inverso_r3.json'
METHODS = ['EV/EBITDA', 'EV/FCFF', 'P/E', 'P/FCFE', 'P/OCF']
NA_FLUJO = {'EV/FCFF': 'FCFF FY+3 negativo en Conservadora, Base y Optimista (Financials Multiples G24/G63/G103: −1.733 / −34.076 / −26.170): la ola de capex de IA mantiene la reinversión por encima del NOPAT en FY+3. El múltiplo de salida (ancla C) solo sirve para que la hoja calcule el VP negativo; método sin peso.',
            'P/FCFE': 'FCFE FY+3 negativo en la Base (Financials Multiples G68: −7.201) y casi nulo en la Optimista (3.175): denominador no interpretable. El múltiplo de salida (ancla C) solo sirve para que la hoja calcule el VP negativo; método sin peso.'}

def fmt(x, d=0): return f'{x:,.{d}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
usd = lambda x, d=2: 'US$' + fmt(x, d)
num = lambda x: isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)
def close(a, b, tol=1e-6): return num(a) and num(b) and abs(a - b) <= max(tol, abs(b) * 1e-8)
def need(c, m):
    if not c: raise SystemExit('FALLA: ' + m)

cap = json.loads(CAP.read_text()); D = cap['data']; sha = hashlib.sha256(CAP.read_bytes()).hexdigest()
need(cap['revision_id'] == REV and cap['sheet_id'] == '1yzSqSP3Qopz3lPBNKsyXCsNSgioxZkoWOrZ6eaTjBvA', 'identidad de la captura')
v = {'ticker': 'AMZN', 'nombreActivo': 'Amazon.com, Inc.', 'market': 'NASDAQ', 'moneda': 'USD', 'currency': 'USD', 'mos': 0.35,
     'baseMOS': 'dcfBase', 'tipo': 'Crecimiento maduro', 'metodo_valoracion': 'A', 'version_metodo': 'A-1.2',
     'fecha_corte': '2026-10-30', 'fechaCorteContable': '2026-09-30', 'reportSchema': 'jmr-valuation-two-levels-v5',
     'auditoriaEconomica': 'NO_REALIZADA_PENDIENTE_REVISION_VISUAL', 'auditPendingUserVisualReview': True,
     'valorEsperado': {'metodo': 'promedio ponderado de Conservadora, Base y Optimista (Disrupción aparte)'}}
v['sheet_id'] = cap['sheet_id']
v['hojaGoogle'] = f"https://docs.google.com/spreadsheets/d/{cap['sheet_id']}/edit"

# --- escenarios ---
st = {str(r[0]).split(' · ')[0].strip(): r for r in D['stories'][1:5]}
base, cons, opt = st['Base'], st['Conservadora'], st['Optimista']
disr = next(r for k, r in st.items() if k.startswith('Disrup'))
for r in (base, cons, disr, opt): need(r[10] == 'LISTO', f'estado de cálculo {r[0]}')
vb = D['valuation_base']; b35 = vb[32][1]
need(close(b35, base[7]), 'B35 = H5 de Escenarios')
need(vb[33][0].startswith('Price') and num(vb[33][1]), 'precio'); price = vb[33][1]
v['revisionId'] = v['revision_id'] = REV
v['fecha'] = v['fechaRevision'] = '2026-11-02'
v['precio'] = v['precioAnalisis'] = price
v['valorPrincipal'] = v['valorIndependiente'] = b35
v['escenarios'] = {'conservador': cons[7], 'base': base[7], 'optimista': opt[7], 'disrupcion': disr[7]}
v['precioMOS'] = v['precioMOSMax'] = v['precioMOSHoy'] = b35 * (1 - v['mos'])
den = base[1] + cons[1] + opt[1]
ve = v['valorEsperado']; ve['valor'] = (base[1] * base[7] + cons[1] * cons[7] + opt[1] * opt[7]) / den; ve['valorCentral'] = b35
def hist(i, r): return {'id': i, 'nombre': {'A': 'Base', 'B': 'Conservadora', 'C': 'Disrupción', 'D': 'Optimista'}[i], 'probabilidad': r[1],
    'valor': r[7], 'precioMOS': r[7] * (1 - v['mos']), 'roicTerminal': r[6], 'gTerminal': r[9], 'ventasACapital1a5': r[4],
    'ventasACapital6a10': r[5], 'margenTerminal': r[3], 'crecimientoCAGR1a5': r[2]}
ve['historias'] = [hist('A', base), hist('B', cons), hist('C', disr), hist('D', opt)]

# --- descuento de múltiplos ---
md = D['multiples_discount']; ke, crit = md[1][1], md[2][1]
need(num(ke) and crit in ('Promedio 1-3 años', 'Solo 3 años'), 'Ke y criterio')
starts = {'conservador': 7, 'base': 16, 'optimista': 25}
methods = []
for n, name in enumerate(METHODS):
    na = name in NA_FLUJO
    m = {'nombre': name, 'peso': md[16 + n][1], 'pesoRelativo': md[16 + n][2],
         'estado': 'N/A: flujo negativo' if na else 'CALCULADO_NATIVO_EN_REVISION'}
    for sc, s0 in starts.items():
        row = md[s0 + n]; need(row[0] == name, f'{name} {sc}')
        need(all(num(row[i]) for i in range(1, 10)), f'{name} {sc} completo')
        if not na: need(row[10] == 'OK', f'{name} {sc} control')
        m[sc] = {'fy': row[3:6], 'vp': row[6:9], 'consolidado': row[9], 'chequeo': row[10],
                 'origen': f"'Descuento de múltiplos'!D{s0+n+4}:K{s0+n+4}"}
        exp = row[8] if crit == 'Solo 3 años' else sum(row[6:9]) / 3
        need(close(exp, row[9]), f'consolidado aritmético {name} {sc}')
    if na:
        need(m['peso'] == 0 and m['base']['fy'][2] < 0 and m['base']['vp'][2] < 0, f'{name}: N/A exige peso 0 y FY+3/VP3 negativos')
        m['motivo'] = NA_FLUJO[name]
    methods.append(m)
need(close(sum(m['peso'] for m in methods) + md[34][1], 1) or close(md[34][1] + (md[35][1] or 0), 1), 'pesos suman 1')

# --- matrices 5×5 Base (Sensibilidad por múltiplo) ---
sm = D['sens_mult']; matrices = []; centers = {}
for n, name in enumerate(METHODS):
    r0 = 75 + 10 * n
    need(sm[r0][0].startswith('BASE · ' + name), f'bloque {name}')
    fund = sm[r0 + 2][1:6]; mats = [[sm[r0 + 3 + i][0]] + sm[r0 + 3 + i][1:6] for i in range(5)]; ctrl = sm[r0 + 8]
    chosen = next(m for m in methods if m['nombre'] == name)
    if name in NA_FLUJO:
        need(ctrl[7] == 'N/D' and close(ctrl[6], chosen['base']['vp'][2]) and ctrl[6] < 0, f'{name}: VP3 negativo nativo')
        matrices.append({'metodo': name, 'escenario': 'base', 'prioritario': True, 'ancla': 'JMR', 'estado': 'N/A', 'estadoFuente': 'N/D',
            'fundamentalFY3': fund, 'multiploElegido': [row[0] for row in mats], 'matriz': None, 'centro': None,
            'vp3Original': chosen['base']['vp'][2], 'origen': f"'Sensibilidad por múltiplo'!A{76+10*n}:I{84+10*n}",
            'motivo': 'Flujo proyectado FY+3 y VP3 negativos en esta revisión; el múltiplo no representa un precio económico interpretable. Método sin ponderación (peso cero). La hoja original permanece N/D.'})
        continue
    center, vp3, status = ctrl[6], ctrl[7], ctrl[8]
    need(status == 'OK' and close(center, vp3), f'control de centro {name}')
    grid = [row[1:] for row in mats]; need(close(grid[2][2], center), f'celda central {name}')
    need(all(num(x) for x in fund) and all(num(x) for row in grid for x in row), f'matriz completa {name}')
    need(close(chosen['base']['vp'][2], vp3), f'VP3 = centro matriz {name}')
    centers[name] = vp3
    matrices.append({'metodo': name, 'escenario': 'base', 'prioritario': True, 'ancla': 'JMR', 'estado': 'OK',
        'fundamentalFY3': fund, 'multiploElegido': [row[0] for row in mats], 'matriz': grid, 'centro': center, 'vp3Original': vp3,
        'origen': f"'Sensibilidad por múltiplo'!A{76+10*n}:I{84+10*n}", 'motivo': None})
for k, name in ((5, 'P/V'), (6, 'P/BV')):
    r0 = 75 + 10 * k
    need(sm[r0][0].startswith('BASE · ' + name), f'bloque {name}'); ctrl = sm[r0 + 8]
    need(ctrl[7] == 'N/D', f'{name} esperado N/D')
    matrices.append({'metodo': name, 'escenario': 'base', 'prioritario': False, 'ancla': 'JMR', 'estado': 'N/D',
        'fundamentalFY3': sm[r0 + 2][1:6], 'multiploElegido': [0, 0, 0, 0, 0], 'matriz': None, 'centro': None, 'vp3Original': None,
        'origen': f"'Sensibilidad por múltiplo'!A{76+10*k}:I{84+10*k}",
        'motivo': f'{name} es un método complementario opcional: la hoja no tiene múltiplo de salida elegido. No se calcula, no tiene peso y su ausencia no bloquea la publicación (REGLAS §5A).'})
res = {'dcfHoy': md[34], 'multiplesHoy': md[35], 'ponderadoHoy': md[36]}
summ = {k: {'conservador': r[2] if len(r) > 2 else None, 'base': r[3] if len(r) > 3 else None, 'optimista': r[4] if len(r) > 4 else None} for k, r in res.items()}
need(close(summ['dcfHoy']['base'], b35), 'DCF hoy base = B35')
v['descuentoMultiples'] = {'version': 2, 'estado': 'CALCULADO_NATIVO_EN_REVISION', 'horizonteAnios': 3, 'pesoDcf': md[34][1],
    'pesoMultiplos': md[35][1] or 0, 'criterio': crit, 'costoPatrimonio': ke, 'dcfHoy': summ['dcfHoy'], 'multiplesHoy': summ['multiplesHoy'],
    'ponderadoHoy': summ['ponderadoHoy'], 'metodos': methods, 'resumenNativo': summ,
    'integracionNativa': {'revisionId': REV, 'sourceSheetId': v['sheet_id'], 'rango': "'Descuento de múltiplos'!A4:K50", 'capturaSha256': sha,
        'fechaCaptura': '2026-11-02', 'estado': 'METODOS_Y_CONSOLIDACION_CONCILIADOS', 'certificadoEconomico': False, 'calculosExternosExportados': False},
    'nota': 'Múltiplos de salida por regla de ciclo (cierres FY2022-FY2025 y LTM con crecimiento a ±2 pp del FY+3 de cada historia, ajuste por tasas, tope LTM del Conservador y ancla C en P/E); EV/EBITDA y P/OCF sin ancla C por conversión FY+3 transitoria (ver reference/multiplos_v3/AMZN_anclas.json en JMR-valuation). Pesos: DCF 100 %, múltiplos 0 (contraste secundario). Auditoría económica pendiente.'}
v['sensibilidadMultiples'] = {'contrato': 'base-native-five-priority-v1', 'revisionId': REV, 'sourceSheetId': v['sheet_id'], 'resultadosSha256': sha,
    'estadoPublicacion': 'INTEGRADO_EN_REVISION', 'matrices': matrices, 'metodosPendientes': [m['metodo'] for m in matrices if m['estado'] not in ('OK', 'N/A')],
    'sinRecalculoExterno': True, 'certificado': False, 'controlesTecnicosAprobados': True,
    'nota': 'Tres matrices 5×5 Base nativas (EV/EBITDA, P/E, P/OCF) con centro = VP3; EV/FCFF y P/FCFE N/A por flujo FY+3 negativo con VP3 nativo negativo; P/V y P/BV complementarios no utilizados.'}
v['metodos'] = [{'nombre': 'DCF FCFF', 'peso': md[34][1], 'horizonte': 'Valor presente', 'conservador': cons[7], 'base': base[7], 'optimista': opt[7], 'disrupcion': disr[7]}] + [
    {'nombre': m['nombre'], 'peso': m['peso'], 'horizonte': 'Valor presente a hoy (promedio 1-3 años)', 'conservador': m['conservador']['consolidado'],
     'base': m['base']['consolidado'], 'optimista': m['optimista']['consolidado'], 'estado': m['estado']} for m in methods]

# --- sensibilidad DCF ---
sd = D['sens_dcf']
def mat(r0, title):
    need(str(sd[r0 - 1][0]).startswith(title), 'título ' + title)
    cols = sd[r0][1:6]; rows = [sd[r0 + 1 + i][0] for i in range(5)]; vals = [sd[r0 + 1 + i][1:6] for i in range(5)]
    need(close(vals[2][2], b35), 'centro DCF ' + title)
    return {'rows': rows, 'columns': cols, 'values': vals, 'center': vals[2][2]}
v['sensibilidadDCF'] = {'tipo': 'FCFF', 'estado': 'CALCULADA_NATIVA_EN_REVISION',
    'matrices': {'waccVsTerminalGrowth': mat(4, 'WACC'), 'waccVsTerminalROIC': mat(15, 'ROIC'), 'crecimientoVsMargen': mat(26, 'Crecimiento')},
    'origen': "'Sensibilidad DCF'!A1:H36", 'capturaSha256': sha}
inv = json.loads(INV.read_text())
need(abs(inv['reconstructed_price'] - price) < 1e-6, 'DCF inverso reproduce el precio')
v['dcfInverso'] = {**inv, 'variable': 'delta común aditivo al crecimiento de los años 1-5; años 6-10 convergen a g', 'calculo': 'Externo reproducible (fase 2, replicador independiente que reproduce B35 con error 0); no es salida nativa de la hoja.'}

def row(i): return vb[i][2:12]
rev, gr, mg, tx, np_, rein, fcff, rate, dfac, pv = row(2), row(1), row(3), row(5), row(6), row(7), row(8), row(11), row(12), row(13)
v['nivel2ProyeccionBase'] = [{'year': i + 1, 'revenues': rev[i], 'growth': gr[i], 'margin': mg[i], 'tax': tx[i], 'nopat': np_[i], 'reinvestment': rein[i],
    'fcff': fcff[i], 'discountRate': rate[i], 'presentValue': pv[i], 'discountFactor': dfac[i]} for i in range(10)]
need(all(num(x) for a in (rev, gr, mg, tx, np_, rein, fcff, rate, dfac, pv) for x in a), 'proyección numérica')
v['puenteEquity'] = {'valorOperativo': vb[23][1], 'deuda': vb[24][1], 'minoritarios': vb[25][1], 'caja': vb[26][1], 'activosNoOperativos': vb[27][1],
    'valorPatrimonio': vb[28][1], 'opciones': vb[29][1], 'acciones': vb[31][1], 'valorPorAccion': b35, 'valorTerminalPV': vb[18][1], 'sumaPV': vb[20][1]}
need(close(vb[27][1], 240155), 'no operativos netos de impuesto diferido')
v['tasas'] = {'rf': 0.0494, 'rfFecha': '2026-10-30', 'erp': 0.0379, 'erpFuente': 'Damodaran 1-nov-2026, T12m (ERPNov26.xlsx; T.Bond 4,94 %)',
              'erpInicialConPaises': 0.0379 + (0.0078*43212+0.0091*30688+0.018*107467)/716924, 'wacc': rate[0], 'waccTerminal': vb[16][1],
              'betaDesapalancada': 1.0512340814661552, 'betaRegresion60m': {'beta': 1.491, 'errorEstandar': 0.212, 'r2': 0.46, 'nota': 'contraste; la Ke usa la bottom-up'}}
v['salvedades'] = [
 'EN_REVISION: valoración calculada por la hoja A-1.2 (Análisis/AMZN), sin auditoría económica independiente de R3 ni certificación. R3 sustituye a la candidata R2 (auditada PENDIENTE el 2-nov-2026) aplicando las correcciones que la regla admite; la fase 4 de R3 debe hacerla otra sesión u otro LLM.',
 'Corte: precio 240,35 USD del 30-oct-2026, Treasury 10A 4,94 % del 30-oct y prima madura 3,79 % de Damodaran al 1-nov-2026 (calculada con ese mismo Treasury). Es un corte propio de la revisión; la Cartera global conserva el corte del 30-sep (REGLAS §4 y README de fases).',
 'Costo de capital: beta bottom-up multinegocio Retail (General) ×2 + Software (System & Application) para AWS, desapalancada 1,05; beta de regresión 60m 1,49 (EE 0,21) solo como contraste. WACC inicial ' + fmt(rate[0]*100, 2) + ' %, terminal 8,73 % (beta 1), g 4 %.',
 'No operativos 240.155 M = valor contable de Anthropic (notas 146.200 + preferentes 92.500), OpenAI (50.000), otras privadas, warrants y método de participación (294.595, 10-Q T3-26 nota 2) MENOS impuesto diferido estimado 54.440 (34.608 observado en AOCI + preferentes con base 12.100 a 24,67 %). Nivel 3, sin descuento adicional; riesgo correlacionado con la demanda de AWS.',
 'Opciones: 223,3 M RSU con ejercicio técnico 0,01 USD (con 0 exacto la fórmula nativa valoraba cada RSU a la mitad); reclamación 53.668 M restada una vez; acciones reales 10.811 M; la SBC sigue en el EBIT.',
 'Arrendamientos: pasivos ASC 842 reconocidos (114.783 M) en la deuda, sin conversión adicional (REGLAS §4A). La auditoría de R2 señaló que, con US GAAP, el EBIT incluye la renta operativa completa (efecto estimado +6 %); es una cuestión de regla para todas las empresas de EE.UU., no se aplica solo a AMZN.',
 'ROIC terminal por regla de foso (reference/moat_2026-09-30.json): Base 16,5 % (ventaja durable), Conservadora 12,62 % (desvanece), Optimista 20 %, Disrupción 8,73 % (= costo de capital). El valor terminal es ' + fmt(vb[18][1] / vb[20][1] * 100, 1) + ' % del VP operativo.',
 'I+D no capitalizada (B17 = No): estimación 73-96 mM; la capitalización consistente no cambia el FCFF (auditoría R2, C-10). Impuesto normalizado 22,5 % → 25 % (REGLAS §4: tasa efectiva); el impuesto en caja (~6,5 % del EBIT por depreciación al 100 %) queda como sensibilidad al alza (+4 % con 15 %), no aplicada.',
 'Múltiplos: cinco prioritarios evaluados con la hoja nativa; EV/EBITDA, P/E y P/OCF calculados con matrices 5×5 (regla por ciclo, ajuste por tasas, ancla C en P/E); EV/FCFF y P/FCFE N/A por flujo FY+3 negativo. La C de EV/EBITDA y P/OCF no se calcula por conversión FY+3 transitoria (juicio documentado). El EV histórico de la plantilla no resta inversiones no operativas (infla EV/EBITDA FY25 y LTM). Pesos: DCF 100 %.',
 'Precios de cierre históricos, etiquetas de periodo y entradas auxiliares completados en R3 (faltaban desde la fase 1 de R2); filas de memoria de FCF apalancado/no apalancado completadas. Sensibilidades DCF y de múltiplos copiadas de la hoja nativa; DCF inverso externo reproducible.']
v['fuentes_supuestos'] = [v['hojaGoogle'], 'https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm',
    'https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm', 'https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPNov26.xlsx',
    'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_yield_curve']
v['estado'] = v['publicationStatus'] = 'EN_REVISION'
v['publicationStage'] = 'PUBLICACION_EN_REVISION'
v['validationStatus'] = 'PENDIENTE_CI_PROMOCION_Y_QA'
v['publicationAuthorized'] = False
v['controlEditorial'] = {'nivel1Capitulos': 14, 'nivel2Apartados': 12, 'estado': 'DOCUMENTOS_INDEPENDIENTES_COMPLETADOS'}
v['reporteFuentes'] = {'captura': f'evidencia/captura-hoja-20261102/{REV}_resultados_hoja.json', 'capturaSha256': sha,
    'entregaFase2': f'candidatos/valoraciones/{REV}/FASE_2_ENTREGA.md', 'auditoriaPrevia': 'candidatos/valoraciones/AMZN-20261102-A12-R2/AUDITORIA_ECONOMICA_AMZN_R2.md',
    'multiplos': 'JMR-valuation: reference/multiplos_v3/AMZN_anclas.json, AMZN_ciclo.json, AMZN_decision.json, AMZN_ciclo_resultado.json'}
v['metodoPrincipal'] = 'DCF FCFF 10 años, Método JMR A-1.2, calculado por la hoja (Valuation output!B35)'
v['revisionOrigen'] = {'anterior': 'AMZN-20261102-A12-R2', 'motivo': 'R3 = copia de la hoja R2 con las correcciones de la auditoría fase 4 que la regla admite (prima del corte, impuesto diferido de participaciones, beta, ROIC terminal por foso, RSU) y los cinco múltiplos completados. R2 queda como candidata no publicada.'}
v['objetivoPonderado'] = v['valorPresentePonderado'] = {'estado': 'CALCULADO_NATIVO_EN_REVISION', **summ['ponderadoHoy']}
v['precioReferenciaFecha'] = '2026-10-30'
v['precioReferenciaFuente'] = 'Cierre del 30-oct-2026 (Input sheet!B23; Alpha Vantage TIME_SERIES_DAILY)'
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
print('OK', OUT.relative_to(ROOT), 'base', round(b35, 4), 'MOS', round(v['precioMOS'], 4), 'esperado', round(ve['valor'], 4))
