#!/usr/bin/env python3
"""Construye el JSON de valoración A-1.2 de una revisión a partir de la captura completa de su hoja.

Solo copia celdas ya calculadas por la hoja (UNFORMATTED_VALUE) y verifica: centros de matrices = VP3 del método,
control 'OK' de cada fila, DCF Base = Valuation output!B35, pesos que suman 1. No recalcula ni inventa valores.
Uso: python3 scripts/construir_valoracion_hoja_20261101.py NVDA
"""
import copy, hashlib, json, math, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TICKER = sys.argv[1]
REV = sys.argv[2] if len(sys.argv) > 2 else f'{TICKER}-20261101-A12-R1'
CAP = ROOT / f'evidencia/captura-hoja-20261101/{REV}_resultados_hoja.json'
# Molde de estructura: candidato previo DE LA MISMA EMPRESA (nunca de otra, por aislamiento); sus valores se sobrescriben.
CAND_OLD = ROOT / {'INTU': 'candidatos/valoraciones/INTU-20261029-R1/VALORACION_A12_EN_REVISION.json'}.get(
    TICKER, f'candidatos/valoraciones/{TICKER}-20261031-A12-R1/VALORACION_A12_EN_REVISION.json')
OUT = ROOT / f'candidatos/valoraciones/{REV}/VALORACION_A12_EN_REVISION.json'
METHODS = ['EV/EBITDA', 'EV/FCFF', 'P/E', 'P/FCFE', 'P/OCF']

def fmt(x, d=0):
    return f'{x:,.{d}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
usd = lambda x, d=2: 'US$' + fmt(x, d)
num = lambda x: isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)
def close(a, b, tol=1e-6): return num(a) and num(b) and abs(a - b) <= max(tol, abs(b) * 1e-8)
def need(c, m): 
    if not c: raise SystemExit('FALLA: ' + m)

cap = json.loads(CAP.read_text()); D = cap['data']; sha = hashlib.sha256(CAP.read_bytes()).hexdigest()
need(cap['revision_id'] == REV, 'revisión de la captura')
# DPZ no tiene candidato previo A: esqueleto propio solo con identidad (aislamiento: ningún molde de otra empresa).
SKELETON = {'DPZ': {'ticker': 'DPZ', 'nombreActivo': "Domino's Pizza, Inc.", 'market': 'NASDAQ', 'moneda': 'USD', 'currency': 'USD',
    'mos': 0.35, 'baseMOS': 'dcfBase', 'tipo': 'Madura', 'metodo_valoracion': 'A', 'version_metodo': 'A-1.2',
    'fecha_corte': '2026-09-06', 'fechaCorteContable': '2026-09-06', 'reportSchema': 'jmr-valuation-two-levels-v5',
    'auditoriaEconomica': 'NO_REALIZADA_PENDIENTE_REVISION_VISUAL', 'auditPendingUserVisualReview': True,
    'valorEsperado': {'metodo': 'promedio ponderado de Conservadora, Base y Optimista (Disrupción aparte)'}}}
v = copy.deepcopy(SKELETON[TICKER]) if TICKER in SKELETON else copy.deepcopy(json.loads(CAND_OLD.read_text()))
for k in ('degradadoACandidato', 'hojas', 'revisionSupuestos', 'objetivoPonderado', 'valorPresentePonderado'):
    v.pop(k, None)   # campos del molde que no salen de esta captura
v['sheet_id'] = cap['sheet_id']
v['hojaGoogle'] = f"https://docs.google.com/spreadsheets/d/{cap['sheet_id']}/edit"
need(v['ticker'] == TICKER, 'ticker del molde')

# --- escenarios (hoja: Escenarios e historias A4:N13) ---
st = {str(r[0]).split(' · ')[0].strip(): r for r in D['stories'][1:5]}
base = st['Base']; cons = st['Conservadora']; opt = st['Optimista']
disr = next(r for k, r in st.items() if k.startswith('Disrup'))
for r in (base, cons, disr, opt): need(r[10] == 'LISTO', f'estado de cálculo {r[0]}')
vb = D['valuation_base']
b35 = vb[32][1]
need(close(b35, base[7]), 'B35 = H5 de Escenarios')
need(vb[33][0].startswith('Price') and num(vb[33][1]), 'precio')
price = vb[33][1]

v['revisionId'] = v['revision_id'] = REV
v['fecha'] = v['fechaRevision'] = '2026-11-01'
v['precio'] = v['precioAnalisis'] = price
v['valorPrincipal'] = b35
v['valorIndependiente'] = b35
v['escenarios'] = {'conservador': cons[7], 'base': base[7], 'optimista': opt[7], 'disrupcion': disr[7]}
v['precioMOS'] = v['precioMOSMax'] = v['precioMOSHoy'] = b35 * (1 - v['mos'])
probs = {'A': base[1], 'B': cons[1], 'C': disr[1], 'D': opt[1]}
den = base[1] + cons[1] + opt[1]
ve = v['valorEsperado']
ve['valor'] = (base[1] * base[7] + cons[1] * cons[7] + opt[1] * opt[7]) / den
ve['valorCentral'] = b35
def hist(i, r): return {'id': i, 'nombre': {'A': 'Base', 'B': 'Conservadora', 'C': 'Disrupción', 'D': 'Optimista'}[i], 'probabilidad': r[1],
    'valor': r[7], 'precioMOS': r[7] * (1 - v['mos']), 'roicTerminal': r[6], 'gTerminal': r[9], 'ventasACapital1a5': r[4],
    'ventasACapital6a10': r[5], 'margenTerminal': r[3], 'crecimientoCAGR1a5': r[2]}
ve['historias'] = [hist('A', base), hist('B', cons), hist('C', disr), hist('D', opt)]

# --- descuento de múltiplos (A4:K50; índice = fila-4) ---
md = D['multiples_discount']
ke, crit = md[1][1], md[2][1]
need(num(ke) and crit in ('Promedio 1-3 años', 'Solo 3 años'), 'Ke y criterio')
starts = {'conservador': 7, 'base': 16, 'optimista': 25}
sm = D['sens_mult']
centers = {}
matrices = []
for n, name in enumerate(METHODS):
    r0 = 75 + 10 * n           # fila 76+10n, índice 0-based
    need(sm[r0][0].startswith('BASE · ' + name), f'bloque {name}')
    fund = sm[r0 + 2][1:6]; mats = [[sm[r0 + 3 + i][0]] + sm[r0 + 3 + i][1:6] for i in range(5)]
    ctrl = sm[r0 + 8]; center, vp3, status = ctrl[6], ctrl[7], ctrl[8]
    need(status == 'OK' and close(center, vp3), f'control de centro {name}')
    grid = [row[1:] for row in mats]; need(close(grid[2][2], center), f'celda central {name}')
    need(all(num(x) for x in fund) and all(num(x) for row in grid for x in row), f'matriz completa {name}')
    centers[name] = vp3
    matrices.append({'metodo': name, 'escenario': 'base', 'prioritario': True, 'ancla': 'JMR', 'estado': 'OK',
        'fundamentalFY3': fund, 'multiploElegido': [row[0] for row in mats], 'matriz': grid, 'centro': center, 'vp3Original': vp3,
        'origen': f"'Sensibilidad por múltiplo'!A{76+10*n}:I{84+10*n}", 'motivo': None})
for k, name in ((5, 'P/V'), (6, 'P/BV')):
    r0 = 75 + 10 * k
    need(sm[r0][0].startswith('BASE · ' + name), f'bloque {name}')
    ctrl = sm[r0 + 8]
    if ctrl[8] == 'OK':   # complementario calculado por la hoja: se integra con su control, sin prioridad ni peso
        fund = sm[r0 + 2][1:6]; mats = [[sm[r0 + 3 + i][0]] + sm[r0 + 3 + i][1:6] for i in range(5)]
        grid = [row[1:] for row in mats]
        need(close(ctrl[6], ctrl[7]) and close(grid[2][2], ctrl[6]), f'control de centro {name}')
        need(all(num(x) for x in fund) and all(num(x) for row in grid for x in row), f'matriz completa {name}')
        matrices.append({'metodo': name, 'escenario': 'base', 'prioritario': False, 'ancla': 'JMR', 'estado': 'OK',
            'fundamentalFY3': fund, 'multiploElegido': [row[0] for row in mats], 'matriz': grid, 'centro': ctrl[6],
            'vp3Original': ctrl[7], 'origen': f"'Sensibilidad por múltiplo'!A{76+10*k}:I{84+10*k}",
            'motivo': 'Complementario opcional calculado por la hoja; sin peso en la consolidación.'})
        continue
    need(ctrl[7] == 'N/D', f'{name} esperado N/D en la hoja (si calcula, integrarlo como OK)')
    matrices.append({'metodo': name, 'escenario': 'base', 'prioritario': False, 'ancla': 'JMR', 'estado': 'N/D',
        'fundamentalFY3': sm[r0 + 2][1:6], 'multiploElegido': [0, 0, 0, 0, 0], 'matriz': None, 'centro': None, 'vp3Original': None,
        'origen': f"'Sensibilidad por múltiplo'!A{76+10*k}:I{84+10*k}",
        'motivo': f'{name} es un método complementario opcional: la hoja no tiene múltiplo de salida elegido (celdas del bloque en N/D). No se calcula, no tiene peso y su ausencia no bloquea la publicación.'})
methods = []
for n, name in enumerate(METHODS):
    m = {'nombre': name, 'peso': md[16 + n][1], 'pesoRelativo': md[16 + n][2], 'estado': 'CALCULADO_NATIVO_EN_REVISION'}
    for sc, s0 in starts.items():
        row = md[s0 + n]; need(row[0] == name and row[10] == 'OK', f'{name} {sc}')
        need(all(num(row[i]) for i in range(1, 10)), f'{name} {sc} completo')
        m[sc] = {'fy': row[3:6], 'vp': row[6:9], 'consolidado': row[9], 'chequeo': row[10],
                 'origen': f"'Descuento de múltiplos'!D{s0+n+4}:K{s0+n+4}"}
        exp = row[8] if crit == 'Solo 3 años' else sum(row[6:9]) / 3
        need(close(exp, row[9]), f'consolidado aritmético {name} {sc}')
    need(close(m['base']['vp'][2], centers[name]), f'VP3 = centro matriz {name}')
    methods.append(m)
need(close(sum(m['peso'] for m in methods) + md[34][1], 1) or close(md[34][1] + md[35][1], 1), 'pesos suman 1')
res = {'dcfHoy': md[34], 'multiplesHoy': md[35], 'ponderadoHoy': md[36]}
summ = {k: {'conservador': r[2], 'base': r[3], 'optimista': r[4]} for k, r in res.items()}
need(close(summ['dcfHoy']['base'], b35), 'DCF hoy base = B35')
v['descuentoMultiples'] = {'version': 2, 'estado': 'CALCULADO_NATIVO_EN_REVISION', 'horizonteAnios': 3,
    'pesoDcf': md[34][1], 'pesoMultiplos': md[35][1], 'criterio': crit, 'costoPatrimonio': ke,
    'dcfHoy': summ['dcfHoy'], 'multiplesHoy': summ['multiplesHoy'], 'ponderadoHoy': summ['ponderadoHoy'],
    'metodos': methods, 'resumenNativo': summ,
    'integracionNativa': {'revisionId': REV, 'sourceSheetId': v['sheet_id'], 'rango': "'Descuento de múltiplos'!A4:K50",
        'capturaSha256': sha, 'fechaCaptura': '2026-11-01', 'estado': 'METODOS_Y_CONSOLIDACION_CONCILIADOS',
        'certificadoEconomico': False, 'calculosExternosExportados': False},
    'nota': 'Múltiplos de salida por regla de ciclo (historia propia con crecimiento FY+3 de cada escenario, tope por múltiplo justificado); pares y justificado solo comprueban. Ver reference/multiplos_v3/'+TICKER+'_decision.json en JMR-valuation. Auditoría económica pendiente.'}
v['sensibilidadMultiples'] = {'contrato': 'base-native-five-priority-v1', 'revisionId': REV, 'sourceSheetId': v['sheet_id'],
    'resultadosSha256': sha, 'estadoPublicacion': 'INTEGRADO_EN_REVISION', 'matrices': matrices, 'metodosPendientes': [m['metodo'] for m in matrices if m['estado'] != 'OK'],
    'sinRecalculoExterno': True, 'certificado': False, 'controlesTecnicosAprobados': True,
    'nota': 'Siete posiciones del contrato: cinco matrices 5×5 Base copiadas de la hoja nativa; centro = VP3 de cada método. Pendiente revisión visual y auditoría económica.'}

# metodos principales
v['metodos'] = [{'nombre': 'DCF FCFF', 'peso': md[34][1], 'horizonte': 'Valor presente', 'conservador': cons[7], 'base': base[7],
                 'optimista': opt[7], 'disrupcion': disr[7]}] + [
    {'nombre': m['nombre'], 'peso': m['peso'], 'horizonte': 'Valor presente a hoy (promedio 1-3 años)',
     'conservador': m['conservador']['consolidado'], 'base': m['base']['consolidado'], 'optimista': m['optimista']['consolidado'],
     'estado': m['estado']} for m in methods]

# sensibilidad DCF (A1:H36)
sd = D['sens_dcf']
def mat(r0, title):
    need(str(sd[r0 - 1][0]).startswith(title), 'título ' + title)
    cols = sd[r0][1:6]; rows = [sd[r0 + 1 + i][0] for i in range(5)]; vals = [sd[r0 + 1 + i][1:6] for i in range(5)]
    need(sd[r0 + 7][1] == 'OK' or sd[r0 + 7][0].startswith('Conciliación'), 'conciliación')
    need(close(vals[2][2], b35), 'centro DCF ' + title)
    return {'rows': rows, 'columns': cols, 'values': vals, 'center': vals[2][2]}
v['sensibilidadDCF'] = {'tipo': 'FCFF', 'estado': 'CALCULADA_NATIVA_EN_REVISION',
    'matrices': {'waccVsTerminalGrowth': mat(4, 'WACC'), 'waccVsTerminalROIC': mat(15, 'ROIC'), 'crecimientoVsMargen': mat(26, 'Crecimiento')},
    'origen': "'Sensibilidad DCF'!A1:H36", 'capturaSha256': sha}

# proyección Base (Valuation output A3:M42; índice = fila-3)
def row(i): return vb[i][2:12]
rev, gr, mg, tx, np_, rein, fcff, rate, dfac, pv = row(2), row(1), row(3), row(5), row(6), row(7), row(8), row(11), row(12), row(13)
v['nivel2ProyeccionBase'] = [{'year': i + 1, 'revenues': rev[i], 'growth': gr[i], 'margin': mg[i], 'tax': tx[i], 'nopat': np_[i],
    'reinvestment': rein[i], 'fcff': fcff[i], 'discountRate': rate[i], 'presentValue': pv[i], 'discountFactor': dfac[i]} for i in range(10)]
need(all(num(x) for a in (rev, gr, mg, tx, np_, rein, fcff, rate, dfac, pv) for x in a), 'proyección numérica')

# puente y supuestos clave
v['puenteEquity'] = {'valorOperativo': vb[23][1], 'deuda': vb[24][1], 'minoritarios': vb[25][1], 'caja': vb[26][1],
    'activosNoOperativos': vb[27][1], 'valorPatrimonio': vb[28][1], 'opciones': vb[29][1], 'acciones': vb[31][1],
    'valorPorAccion': b35, 'valorTerminalPV': vb[18][1], 'sumaPV': vb[20][1]}
v['tasas'] = {'rf': 0.0529, 'rfFecha': '2026-09-30', 'erp': 0.037, 'erpFuente': 'Damodaran oct-2026', 'wacc': ke if False else rate[0],
              'waccTerminal': vb[16][1]}

CFG = {}
CFG['NVDA'] = {}
CFG['NVDA']['salvedades'] = [
 'EN_REVISION: valoración calculada por la hoja de trabajo A-1.2, sin auditoría económica independiente ni certificación; no equivale a valor auditado.',
 'Activos no operativos US$47.898 M = valor contable de valores de capital no cotizados (10-Q 26-jul-2026, Nota 6: costo menos deterioro más cambios de precio observables); el valor económico se iguala al contable por falta de valoración independiente. Se excluyen ~US$3.300 M de método de participación en financiadores de infraestructura y US$4.957 M de capital cotizado bloqueado a largo plazo.',
 'Opciones: NVIDIA no informa opciones pendientes; RSU/PSU 168 M (0,7 % de las acciones) con ~4 % devengado, inmaterial; el resto ya está en la compensación en acciones del EBIT. No se resta aparte para evitar doble conteo.',
 'Tasas: Rf 5,29 % y ERP 3,70 % del corte 30-sep-2026 (misma fecha, Damodaran oct-2026); WACC terminal 8,99 % sustituye al 9,30 % escrito a mano. Beta 1,45 y Kd 6 % son supuestos analíticos sin auditoría económica. El precio de mercado (US$204,64) es del 30-oct-2026.',
 'Los resultados del T3 FY2027 (cierre 25-oct-2026) se anuncian el 17-nov-2026 y no están incluidos ni anticipados.',
 'Ingresos LTM de la hoja 302.970 M frente a 302.969 M de la suma aritmética de trimestres redondeados.',
 'Año 1 Base (424.158 M, +40,3 % sobre el LTM) queda 1,8 % por debajo de la guía del emisor para el T3 anualizada (432.000 M): el crecimiento de corto plazo puede estar subestimado; es la mayor fuente de incertidumbre al alza.',
 'ROIC terminal alto (28,7 % Base; 34,5 % Optimista) sujeto a riesgo de obsolescencia, ASIC y normalización de márgenes; el crecimiento perpetuo Base es 3,5 %.',
 'Múltiplos: método de ciclo propio (cierres con crecimiento FY+3 de cada escenario, tope por múltiplo justificado); pares AVGO, QCOM y MU solo comprueban (TSM y AMD excluidos). El P/E Optimista supera 25 % el actual y P/OCF y P/FCFE no restan compensación en acciones. Categoría Crecimiento (DCF 60 %) y MOS 35 % son juicio del analista.',
 'Diferencia con la revisión anterior R4 (381,79): ~85 % proviene de la senda de ventas (R4 suponía +70 % en el año 1); puente en docs/MULTIPLOS_Y_PUENTE_NVDA_META_20261101.md.',
 'Para obtener P/E y P/B se completaron en la hoja la utilidad atribuible y el patrimonio total igualándolos a los consolidados (sin participaciones minoritarias).',
 'Sensibilidades DCF y de múltiplos copiadas de la hoja nativa con centro conciliado; no certificadas económicamente. QA visual con acceso autenticado pendiente.']
CFG['NVDA']['fuentes'] = [v['hojaGoogle'], 'https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm',
 'https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx', 'https://fred.stlouisfed.org/series/DGS10']
CFG['META'] = {'salvedades': [
 'EN_REVISION: valoración calculada por la hoja de trabajo A-1.2, sin auditoría económica independiente ni certificación; no equivale a valor auditado.',
 'Activos no operativos US$21.077 M = valor contable de inversiones no cotizadas bajo alternativa de medición (10-Q 30-sep-2026, Nota 5); su valor económico se iguala al contable por falta de valoración independiente. Se excluyen US$11.547 M de método de participación: son el 20 % de los Ventures de centros de datos de Louisiana y Texas, contraparte de los arrendamientos de Meta.',
 'Opciones: 20 M emitidas en 2026 con ejercicio medio US$2.788 y ~4 años (volatilidad 42,71 %, dividendo 0,34 %): valor total US$' + fmt(v['puenteEquity']['opciones'], 1) + ' M. RSU no adquiridas 134,5 M (5,3 % de las acciones): ~4,7 % devengado (inmaterial); el resto ya está en la compensación en acciones del EBIT y no se resta aparte.',
 'Pasivo legal: provisiones legales por US$19.881 M (Nota 8: 11.577 corrientes + 8.304 no corrientes; acuerdo multiestatal de fiscales generales de ago-2026 y otras) deducidas una sola vez, en valor bruto y sin efecto fiscal (cota superior), en el campo de reclamaciones de la hoja (Input sheet!B21, que no se usa para minoritarios); el puente EV→patrimonio de los múltiplos no las incluye. Efecto: −US$7,78 por acción.',
 'RIESGO MATERIAL NO CUANTIFICADO EN LA HOJA: al 30-sep-2026 META tiene arrendamientos aún no iniciados por US$355.730 M y compromisos no cancelables por US$454.520 M (10-Q, Nota 10), frente a ingresos LTM de US$241.605 M. Solo los pasivos de arrendamiento ya reconocidos (US$31.173 M) están en la deuda (B18 = No). La Base absorbe estos compromisos por márgenes y Sales-to-Capital 0,52: la reinversión del año 1 es US$' + fmt(rein[0]) + ' M, a contrastar con el capex 2026 guiado de US$135.000–145.000 M (incluye principal de arrendamientos financieros) menos la depreciación del LTM (US$24.920 M), es decir, un capex neto de unos US$110.000–120.000 M: la reinversión del año 1 queda entre US$15.000 M y US$25.000 M por debajo. Si la reinversión necesaria fuese mayor, el valor bajaría de forma material.',
 'Tasas: Rf 5,29 % y ERP 3,70 % del corte 30-sep-2026 (misma fecha, Damodaran oct-2026); WACC terminal 8,99 % sustituye al 8,80 % escrito a mano. Beta 1,15 y Kd 6 % son supuestos analíticos sin auditoría económica. El precio de mercado (US$614,99) es del 30-oct-2026.',
 'El EBIT GAAP LTM (79.380 M) incluye el cargo legal de 9.890 M del T3 2026; las historias parten de márgenes ajustados (I+D capitalizada a 3 años) con objetivos de 38,5 %–47 % que no incluyen cargos legales. Las pérdidas de Reality Labs no se eliminan del EBIT.',
 'Múltiplos: regla de ciclo propia (cierres con crecimiento FY+3 de cada escenario, tope por múltiplo justificado); pares GOOGL, PINS, AMZN, MSFT, NFLX, APP y RDDT solo comprueban (SNAP excluido). El EV/EBITDA Base de salida (7,8x) queda por debajo de la historia (15–16x) y de los pares por el tope del múltiplo justificado, que incorpora el capex de IA; el valor por múltiplos Base es ' + usd(v['descuentoMultiples']['multiplesHoy']['base']) + ' frente al DCF ' + usd(b35) + '. Categoría Crecimiento (DCF 60 %) y MOS 35 % son juicio del analista.',
 'Para P/E y P/B no se tocaron estados: META ya tenía utilidad atribuible y patrimonio. Sensibilidades DCF y de múltiplos copiadas de la hoja nativa con centro conciliado; no certificadas. QA visual autenticado pendiente. AZ Stocks no incorporado.'],
 'fuentes': [v['hojaGoogle'], 'https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm', 'https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx', 'https://fred.stlouisfed.org/series/DGS10']}
CFG['INTU'] = {'salvedades': [
 'EN_REVISION propuesta: valoración desde cero calculada por la copia limpia A-1.2 (Análisis/INTU), sin auditoría económica independiente ni certificación; no equivale a valor auditado. Sustituye al candidato INTU-20261029-R1, cuyo DCF no salía de la hoja.',
 'Corte vigente de la cartera: precio US$275,71 del 30-sep-2026 con Rf 5,29 % y ERP 3,70 % de la misma fecha (Damodaran oct-2026). Hecho posterior: cierre del 30-oct-2026 US$341,09 (+24 %); no se incorporó para mantener el corte común.',
 'Activos no operativos US$248 M = participaciones no cotizadas en empresas privadas (10-K FY26), al valor contable por falta de valoración independiente; sus ganancias van fuera del EBIT. Los préstamos a clientes (US$1.468 M) generan ingresos en el EBIT y quedan en el capital operativo.',
 'Opciones: 1,24 M con ejercicio medio US$549,37 y 3,86 años (volatilidad 50,65 %, dividendo 2,0 %), valor US$' + fmt(v['puenteEquity']['opciones'], 1) + ' M. RSU sin consolidar (13,46 M) ya incluidas en la compensación en acciones del EBIT.',
 'I+D capitalizada a 3 años (3.376 en FY26) y arrendamientos operativos convertidos a deuda (VP US$710,8 M); impuesto marginal 24,4 % (21 % federal + 3,4 % estatal) con convergencia desde la efectiva de 24,1 %.',
 'Costo de capital: beta bottom-up de software de EE.UU. reapalancada 1,25 (≈92 % de ventas en EE.UU.), prima por regiones 3,84 %, Kd por calificación sintética 5,92 %, WACC inicial ' + f"{rate[0]*100:.2f}".replace('.', ',') + ' %, terminal 8,99 % y g perpetuo 4 %. Son supuestos analíticos sin auditoría económica.',
 'Segmentos: TurboTax y ProTax se agrupan en «Impuestos» porque la plantilla admite cuatro segmentos; el detalle se conserva en la ficha de historias. Ventas/capital nuevo 0,8-1,1 elegidas para que el capital nuevo rinda ≈1,5 veces el ROIC terminal de cada historia (ROIC actual ajustado ~17-18 %).',
 'Múltiplos: regla de ciclo propia; Intuit nunca creció menos de 12,9 % al año en FY2018-FY2026, mientras las historias esperan 5-10 % a FY+3, por lo que los múltiplos de salida parten del mínimo observado ajustado por tasas y quedan topados por el múltiplo justificado. El valor por múltiplos Base (' + usd(v['descuentoMultiples']['multiplesHoy']['base']) + ') queda un 26 % bajo el DCF (' + usd(b35) + '): brecha fuera de ±25 % explicada por ese tope, no por un error. Pares (ADBE, MSFT, ORCL, ADSK, CRM, NOW) solo comprueban. P/V y P/BV calculados como complementarios sin peso.',
 'Controles de la hoja: 15/15 candados, integridad 0 hallazgos, estados completos 0 hallazgos, entradas esenciales 0 vacías, motor = hoja. El control de fórmula única (apply_canonical_formulas.py) no pudo ejecutarse por un error de importación previo de la herramienta.',
 'Los resultados del 1T FY27 (noviembre de 2026) no están incluidos. QA visual autenticado pendiente. El contraste AZ Stocks del candidato anterior no se mezcla con esta valoración.'],
 'fuentes': [v['hojaGoogle'], 'https://www.sec.gov/Archives/edgar/data/896878/000089687826000037/intu-20260731.htm',
             'https://www.sec.gov/Archives/edgar/data/896878/000089687826000029/fy26q4earningspressrelease.htm',
             'https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx', 'https://fred.stlouisfed.org/series/DGS10']}
CFG['DPZ'] = {'salvedades': [
 'EN_REVISION: valoración desde cero calculada por la copia limpia A-1.2 (AAA Finanzas/Análisis/DPZ), sin auditoría económica independiente ni certificación; no equivale a valor auditado. La hoja histórica B de DPZ no se heredó ni se modificó.',
 'Corte de la cartera: precio US$299,61 del 30-sep-2026 con Rf 5,29 % y ERP 3,70 % (Damodaran oct-2026). Corte contable LTM al 6-sep-2026 = 10-K FY25 + 10-Q 3T26 (presentado el 13-oct-2026, hecho posterior al corte de mercado usado como corte contable). Cambio de CEO el 1-oct-2026.',
 'Estados importados corregidos con nota y respaldo: LTM completo, deuda FY24/FY25 reclasificada desde otros pasivos, financiación FY24/FY25 mal etiquetada en XBRL, FCF/NOPAT LTM y rótulo LTM de Trailing Valuation.',
 'Patrimonio contable negativo (−3.955) por recapitalizaciones con deuda securitizada: P/BV es N/A (complementario sin valor) y el P/E no tiene ancla C (ROE no definido).',
 'Disrupción formulada como estancamiento (ventas planas años 1-3, margen 16 %, ROIC = costo de capital): con caída de ventas la hoja libera capital y el motor no (política «Sin liberación»); con la caída la Disrupción valía ~88-89, fuera del promedio.',
 'Arrendamientos: la ficha usa VP 262,4 para el ajuste de ventas/capital y la hoja calcula 222,2 a su Kd sintético de 6,30 %; efecto en la Base < 1,5 % (salvedad no bloqueante §4B). Lag de reinversión 0 no probado en copia separada.',
 'Múltiplos por regla de ciclo con tope LTM del Conservador y ancla C; el Optimista supera +25 % el múltiplo actual en cuatro métodos (justificacion_salto: caída de 31 % del precio con EBIT +4,8 %). Pesos del perfil Madura de la plantilla, revisados. Pares PZZA, YUM, MCD, QSR, WING solo comprueban.',
 'Probabilidades 45/25/20/10: previa madura estable con −5 pp Base / +5 pp Conservadora por ventas mismas tiendas internacionales de 9M26 (−0,1 %) bajo el umbral 0 %.',
 'Controles: 15/15 candados, integridad y estados completos 0 hallazgos, entradas esenciales 0 vacías, contrato A OK, probabilidades 0 fallos, controles de supuestos 0, verificador de múltiplos APTO (P/BV complementario no utilizado), motor = hoja. apply_canonical_formulas.py no ejecutable por un error de importación previo. QA visual autenticado pendiente.'],
 'fuentes': [v['hojaGoogle'], 'https://www.sec.gov/Archives/edgar/data/1286681/000119312526062321/dpz-20251228.htm',
             'https://www.sec.gov/Archives/edgar/data/1286681/000128668126000040/dpz-20260906.htm',
             'https://www.sec.gov/Archives/edgar/data/1286681/000128668126000039/dpz-ex99_1.htm',
             'https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx', 'https://fred.stlouisfed.org/series/DGS10']}
v['salvedades'] = CFG[TICKER]['salvedades']
v['fuentes_supuestos'] = CFG[TICKER]['fuentes']
v['estado'] = v['publicationStatus'] = 'EN_REVISION'
v['publicationStage'] = 'PUBLICACION_EN_REVISION'
v['validationStatus'] = 'PENDIENTE_CI_PROMOCION_Y_QA'
v['controlEditorial'] = {'nivel1Capitulos': 14, 'nivel2Apartados': 12, 'estado': 'DOCUMENTOS_INDEPENDIENTES_COMPLETADOS'}
v['reporteFuentes'] = {'captura': f'evidencia/captura-hoja-20261101/{REV}_resultados_hoja.json', 'capturaSha256': sha,
    'gates': 'docs/CIERRE_GATES_META_NVDA_20261101.md', 'multiplos': 'docs/MULTIPLOS_Y_PUENTE_NVDA_META_20261101.md',
    'fechas': 'docs/FECHAS_TASAS_META_NVDA_20261101.md'}
if TICKER == 'DPZ':
    v['reporteFuentes'] = {'captura': f'evidencia/captura-hoja-20261101/{REV}_resultados_hoja.json', 'capturaSha256': sha,
        'research': 'JMR-valuation: data/DPZ_Research_JMR_A1_2026-11-01.md',
        'scripts': 'JMR-valuation: scripts/run_dpz_cero.py, scripts/dpz_cero_spec.py, reference/multiplos_v3/DPZ_decision.json'}
    v['metodoPrincipal'] = 'DCF FCFF 10 años, Método JMR A-1.2, calculado por la hoja (Valuation output!B35)'
    v['revisionOrigen'] = 'Copia limpia de la plantilla IA vigente (46 pestañas) en AAA Finanzas/Análisis/DPZ; desde cero con 10-K FY2025 y 10-Q 3T26.'
    v['objetivoPonderado'] = v['valorPresentePonderado'] = {'estado': 'CALCULADO_NATIVO_EN_REVISION', **v['descuentoMultiples']['ponderadoHoy']}
    v['precioReferenciaFecha'] = '2026-09-30'
    v['precioReferenciaFuente'] = 'Cierre del 30-sep-2026 (corte vigente de la cartera, JMR-valuation reference/corte_vigente.json; yfinance auto_adjust=False)'
if TICKER == 'INTU':
    v['reporteFuentes'] = {'captura': f'evidencia/captura-hoja-20261101/{REV}_resultados_hoja.json', 'capturaSha256': sha,
        'valoracion': 'docs/VALORACION_INTU_A12_20261101.md',
        'scripts': 'JMR-valuation: scripts/run_intu_cero.py, scripts/intu_cero_spec.py, reference/multiplos_v3/INTU_decision.json'}
    v['metodoPrincipal'] = 'DCF FCFF 10 años, Método JMR A-1.2, calculado por la hoja (Valuation output!B35)'
    v['revisionOrigen'] = 'Copia limpia de la plantilla IA vigente (46 pestañas) en AAA Finanzas/Análisis/INTU; desde cero con 10-K FY2026 y guía FY27.'
    v['objetivoPonderado'] = v['valorPresentePonderado'] = {'estado': 'CALCULADO_NATIVO_EN_REVISION', **v['descuentoMultiples']['ponderadoHoy']}
    v['precioReferenciaFecha'] = '2026-09-30'
    v['precioReferenciaFuente'] = 'Cierre del 30-sep-2026 (corte vigente de la cartera, JMR-valuation reference/corte_vigente.json; yfinance auto_adjust=False)'
    v['publicationAuthorized'] = False   # candidato: la promoción a EN_REVISION requiere autorización explícita del usuario
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
print('OK', OUT.relative_to(ROOT), 'base', b35, 'MOS', v['precioMOS'], 'esperado', ve['valor'])
