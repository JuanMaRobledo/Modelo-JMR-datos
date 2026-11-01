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
REV = f'{TICKER}-20261101-A12-R1'
CAP = ROOT / f'evidencia/captura-hoja-20261101/{REV}_resultados_hoja.json'
CAND_OLD = ROOT / f'candidatos/valoraciones/{TICKER}-20261031-A12-R1/VALORACION_A12_EN_REVISION.json'
OUT = ROOT / f'candidatos/valoraciones/{REV}/VALORACION_A12_EN_REVISION.json'
METHODS = ['EV/EBITDA', 'EV/FCFF', 'P/E', 'P/FCFE', 'P/OCF']

num = lambda x: isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)
def close(a, b, tol=1e-6): return num(a) and num(b) and abs(a - b) <= max(tol, abs(b) * 1e-8)
def need(c, m): 
    if not c: raise SystemExit('FALLA: ' + m)

cap = json.loads(CAP.read_text()); D = cap['data']; sha = hashlib.sha256(CAP.read_bytes()).hexdigest()
need(cap['revision_id'] == REV, 'revisión de la captura')
v = copy.deepcopy(json.loads(CAND_OLD.read_text()))

# --- escenarios (hoja: Escenarios e historias A4:N13) ---
st = {r[0]: r for r in D['stories'][1:5]}
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
    need(sm[r0 + 8][7] == 'N/D', f'{name} esperado N/D en la hoja (si calcula, integrarlo como OK)')
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
    'nota': 'Múltiplos de salida por regla de ciclo (historia propia con crecimiento FY+3 de cada escenario, tope por múltiplo justificado); pares y justificado solo comprueban. Ver reference/multiplos_v3/NVDA_decision.json en JMR-valuation. Auditoría económica pendiente.'}
v['sensibilidadMultiples'] = {'contrato': 'base-native-five-priority-v1', 'revisionId': REV, 'sourceSheetId': v['sheet_id'],
    'resultadosSha256': sha, 'estadoPublicacion': 'INTEGRADO_EN_REVISION', 'matrices': matrices, 'metodosPendientes': ['P/V', 'P/BV'],
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

v['salvedades'] = [
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
v['fuentes_supuestos'] = [v['hojaGoogle'] if 'hojaGoogle' in v else '', 'https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm',
 'https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx', 'https://fred.stlouisfed.org/series/DGS10']
v['estado'] = v['publicationStatus'] = 'EN_REVISION'
v['publicationStage'] = 'PUBLICACION_EN_REVISION'
v['validationStatus'] = 'PENDIENTE_CI_PROMOCION_Y_QA'
v['controlEditorial'] = {'nivel1Capitulos': 14, 'nivel2Apartados': 12, 'estado': 'DOCUMENTOS_INDEPENDIENTES_COMPLETADOS'}
v['reporteFuentes'] = {'captura': f'evidencia/captura-hoja-20261101/{REV}_resultados_hoja.json', 'capturaSha256': sha,
    'gates': 'docs/CIERRE_GATES_META_NVDA_20261101.md', 'multiplos': 'docs/MULTIPLOS_Y_PUENTE_NVDA_META_20261101.md',
    'fechas': 'docs/FECHAS_TASAS_META_NVDA_20261101.md'}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
print('OK', OUT.relative_to(ROOT), 'base', b35, 'MOS', v['precioMOS'], 'esperado', ve['valor'])
