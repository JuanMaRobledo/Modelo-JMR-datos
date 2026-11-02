#!/usr/bin/env python3
"""Construye VALORACION_A12_EN_REVISION.json de NU-20261102-A12-R1 SOLO con celdas calculadas por la hoja (captura con SHA-256).
Controles internos: centros de matrices = valor Base / VP3, probabilidades suman 1, MOS = Base*0,65. Sin molde de otra revisión."""
import hashlib, json, math, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
REV = 'NU-20261102-A12-R1'
CAP = ROOT / f'evidencia/captura-hoja-20261102/{REV}_resultados_hoja.json'
OUT = ROOT / f'candidatos/valoraciones/{REV}'; OUT.mkdir(parents=True, exist_ok=True)
cap = json.loads(CAP.read_text()); sha = hashlib.sha256(CAP.read_bytes()).hexdigest()
D = cap['data']; F, S, M = D['fcfe'], D['sens'], D['mult']
def cell(t, r, c): 
    row = t[r - 1] if r - 1 < len(t) else []
    return row[c] if c < len(row) else None   # c: 0=A
def need(c, m):
    if not c: raise SystemExit('FALLA: ' + m)
close = lambda a, b, t=1e-6: abs(a - b) <= max(t, abs(b) * 1e-9)
INI = {'Base': 34, 'Conservador': 54, 'Optimista': 74, 'Disrupcion': 94}
val = {k: cell(F, b + 16, 1) for k, b in INI.items()}
resum = {k: cell(F, 5 + i, 8) for i, k in enumerate(INI)}
for k in INI: need(close(val[k], resum[k]), f'resumen = bloque {k}')
price = cell(F, 6, 1); need(price == 11.61, 'precio 11,61')
base = val['Base']; mos = cell(F, 12, 8); need(close(mos, base * 0.65), 'MOS35 = Base x 0,65')
prom = cell(F, 10, 8)
probs = {k: cell(F, 23 + i, 5) for i, k in enumerate(INI)}; need(close(sum(probs.values()), 1.0), 'probabilidades suman 1')
w3 = sum(probs[k] for k in ('Base', 'Conservador', 'Optimista'))
need(close(prom, sum(val[k] * probs[k] for k in ('Base', 'Conservador', 'Optimista')) / w3), 'promedio ponderado ordinario')
ke = {k: cell(F, 23 + i, 3) for i, k in enumerate(INI)}; roet = {k: cell(F, 23 + i, 4) for i, k in enumerate(INI)}
g = cell(F, 20, 1)
# sensibilidades DCF
def grid(top, rows=5):
    cols = [cell(S, top + 1, j) for j in range(1, 6)]
    rws = [cell(S, top + 2 + i, 0) for i in range(rows)]
    vals = [[cell(S, top + 2 + i, j) for j in range(1, 6)] for i in range(rows)]
    return rws, cols, vals
s1 = grid(4); s2 = grid(13); s3 = grid(22)
need(close(s1[2][2][2], base, 1e-6) and close(s2[2][2][2], base, 1e-6) and close(s3[2][2][2], base, 1e-6), 'centros 5x5 = Base')
inv = {'precio': cell(S, 32, 1), 'utilidadRelativaImplicita': cell(S, 33, 1), 'keImplicito': cell(S, 34, 1)}
alt = {'tau': [cell(S, 59, j) for j in range(1, 5)], 'valor': [cell(S, 71, j) for j in range(1, 5)]}
# múltiplos
rows = {}
for r in range(22, 34):
    m, h = cell(M, r, 0), cell(M, r, 1)
    rows[(m, h)] = {'multiplo': cell(M, r, 2), 'metricaFY3': cell(M, r, 3), 'precioFY3': cell(M, r, 4), 'anios': cell(M, r, 5), 'ke': cell(M, r, 6), 'vp': cell(M, r, 7), 'estado': cell(M, r, 8)}
def mat(top):
    cols = [cell(M, top + 1, j) for j in range(1, 6)]
    rws = [cell(M, top + 2 + i, 0) for i in range(5)]
    return rws, cols, [[cell(M, top + 2 + i, j) for j in range(1, 6)] for i in range(5)]
tops = {}
for r in range(30, 75):
    a = cell(M, r, 0)
    if isinstance(a, str) and a.startswith('Matriz P/'): tops[a.replace('Matriz ', '')] = r
for m, top in tops.items():
    need(close(mat(top)[2][2][2], rows[(m, 'BASE')]['vp']), f'centro matriz {m} = VP3')
metodos_mult = []
for m in ('P/E', 'P/FCFE', 'P/BV'):
    metodos_mult.append({'nombre': m, 'peso': 0, 'estado': 'CALCULADO_CONTRASTE' if m != 'P/FCFE' else 'PENDIENTE_ANCLA',
        'valorHoy': {k.lower(): rows[(m, h)]['vp'] for k, h in (('conservador', 'CONSERVADORA'), ('base', 'BASE'), ('optimista', 'OPTIMISTA'), ('disrupcion', 'DISRUPCIÓN'))},
        'multiploSalida': {k.lower(): rows[(m, h)]['multiplo'] for k, h in (('conservador', 'CONSERVADORA'), ('base', 'BASE'), ('optimista', 'OPTIMISTA'), ('disrupcion', 'DISRUPCIÓN'))}})
na = lambda n, why: {'nombre': n, 'peso': 0, 'estado': 'N/A', 'valorHoy': None, 'motivo': why}
metodos = [{'nombre': 'DCF FCFE financiero', 'peso': 1, 'horizonte': 'Valor presente', 'conservador': val['Conservador'], 'base': base,
            'optimista': val['Optimista'], 'disrupcion': val['Disrupcion'], 'estado': 'CALCULADO_NATIVO_FCFE', 'rutaSheet': "NU FCFE!B50,B70,B90,B110"}] + metodos_mult + [
    na('EV/EBITDA', 'No interpretable en un banco: depósitos y fondeo son operativos; no hay EBITDA industrial.'),
    na('EV/FCFF', 'FCFF industrial no aplica a un banco; el motor principal es FCFE a Ke.'),
    na('P/OCF', 'El flujo operativo de un banco incluye variación de cartera y depósitos: no es flujo al accionista.')]
# --- contrato review-relative-v1 (mismo que XP): evidencia hasheada + matrices afines producto múltiplo × fundamental ---
import hashlib as _h
LIM = {'P/E': 'Múltiplos de salida elegidos entre la serie propia de NU (26–39× en 2023–2025) y los pares brasileños (mediana 5,7×); son juicios, no confirmación independiente del DCF. Peso 0 y sin certificación económica.',
       'P/BV': 'Múltiplos de salida elegidos entre el P/BV propio (6,3–7,3×) y los pares brasileños (mediana 0,85×), sin ajuste por ROE sostenible auditado. Peso 0 y sin certificación económica.',
       'P/FCFE': 'Ancla no comparable: el FCFE de un banco en crecimiento acelerado es residual tras la retención de capital y no existen pares con la misma definición. Peso 0; el resultado no es una estimación de valor.'}
FUE = {'P/E': 'Serie propia de NU (cierre de diciembre / BPA diluido NIIF del 20-F) y P/E trailing de ITUB, BBD, PAGS, INTR y STNE (Yahoo Finance, 2-nov-2026).',
       'P/BV': 'P/BV propio de NU (patrimonio atribuible del 20-F) y P/BV trailing de ITUB, BBD, PAGS, INTR y STNE (Yahoo Finance, 2-nov-2026).',
       'P/FCFE': 'Sin ancla independiente: se usa el mismo orden de magnitud del P/E como referencia provisional; no hay serie histórica de FCFE comparable.'}
mats_rel = []
for m, top in tops.items():
    rws, cols, mz = mat(top)
    fac = mz[0][0] / (rws[0] * cols[0])
    for i_ in range(5):
        for j_ in range(5): need(close(mz[i_][j_], fac * rws[i_] * cols[j_], 1e-9), f'matriz {m} afín en ({i_},{j_})')
    mats_rel.append({'metodo': m, 'escenario': 'base', 'estado': 'OK', 'peso': 0, 'ancla': 'PROVISIONAL', 'anclaCertificada': False,
        'fuenteAncla': FUE[m], 'limitacion': LIM[m], 'origen': f"'NU Múltiplos'!A{top}:F{top+6}", 'unidadResultado': 'USD/accion',
        'fundamentalFY3': cols, 'multiploElegido': rws, 'matriz': mz, 'centro': rows[(m, 'BASE')]['vp'], 'vp3Original': rows[(m, 'BASE')]['vp'],
        'formula': {'tipo': 'affine-product', 'factor': fac, 'constante': 0.0,
                    'descripcion': 'VP US$/acción = múltiplo × métrica FY+3 ÷ acciones diluidas ÷ (1+Ke)^(3 − días/365); constante 0 (sin dividendos).'}})
(ROOT / 'evidencia/relativos-revision-20261031').mkdir(parents=True, exist_ok=True)
_ev = {'revisionId': REV, 'sheetId': cap['sheet_id'], 'certificacionEconomica': 'NO_CERTIFICADA', 'sources': {'captura': f'evidencia/captura-hoja-20261102/{REV}_resultados_hoja.json', 'capturaSha256': sha},
       'supuestos': 'Multiplos de salida por historia en NU Múltiplos!C22:C33; Ke por historia en NU FCFE!D23:D26.', 'matrices': mats_rel}
_evp = ROOT / f'evidencia/relativos-revision-20261031/{REV}.json'
_evp.write_text(json.dumps(_ev, ensure_ascii=False, indent=2) + '\n')
SENS_MULT = {'contrato': 'review-relative-v1', 'revisionId': REV, 'sourceSheetId': cap['sheet_id'], 'sourcePath': f'evidencia/relativos-revision-20261031/{REV}.json',
    'resultadosSha256': _h.sha256(_evp.read_bytes()).hexdigest(), 'estadoPublicacion': 'INTEGRADO_EN_REVISION', 'controlesTecnicosAprobados': True, 'certificado': False,
    'certificacionEconomica': 'NO_CERTIFICADA', 'pesoEnDCFPrincipal': 0, 'tipo': 'MULTIPLOS_BANCARIOS',
    'advertencia': 'Matrices aritméticamente conciliadas con la hoja; anclas parciales (serie propia y pares) sin certificar económicamente. Peso cero y no auditadas.', 'matrices': mats_rel}

hist_names = {'Base': 'Base', 'Conservador': 'Conservadora', 'Optimista': 'Optimista', 'Disrupcion': 'Disrupción'}
ids = {'Base': 'A', 'Conservador': 'B', 'Disrupcion': 'C', 'Optimista': 'D'}
def cagr5(k):
    b = INI[k]; return (cell(F, b + 5, 4) / cell(F, 17, 1)) ** 0.2 - 1
hist = [{'id': ids[k], 'nombre': hist_names[k], 'probabilidad': probs[k], 'valor': val[k], 'precioMOS': (val[k] * 0.65),
         'Ke': ke[k], 'ROEterminal': roet[k], 'gTerminal': g, 'crecimientoNIprimeros5': cagr5(k),
         'ROE1': cell(F, INI[k] + 1, 5), 'ROE10': cell(F, INI[k] + 10, 5)} for k in INI]
# proyección Base
proy = [{'anio': y, 'ingresos': cell(F, 34 + y, 2), 'margenNeto': cell(F, 34 + y, 3), 'utilidad': cell(F, 34 + y, 4), 'ROE': cell(F, 34 + y, 5),
         'patrimonioRequerido': cell(F, 34 + y, 6), 'deltaPatrimonio': cell(F, 34 + y, 7), 'FCFE': cell(F, 34 + y, 8), 'VP': cell(F, 34 + y, 10)} for y in range(1, 11)]
capital = [{'anio': y, 'APR': cell(F, 123 + y, 1), 'capitalObjetivo': cell(F, 123 + y, 2), 'patrimonioROE': cell(F, 123 + y, 3), 'exceso': cell(F, 123 + y, 4), 'patrimonioSobreAPR': cell(F, 123 + y, 5)} for y in range(1, 11)]
pct = lambda x, d=2: f'{x*100:.{d}f}'.replace('.', ',') + ' %'
usd = lambda x, d=2: 'US$' + f'{x:,.{d}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
sal = [
 'Auditoría económica NO realizada (pendiente de la revisión visual del usuario). Estado EN_REVISION no equivale a valor certificado.',
 f'El costo del patrimonio es el juicio más sensible: Base Ke {pct(ke["Base"])} (Rf 4,94 %, beta 0,76, prima madura 3,70 %, prima país ponderada {pct(cell(F,15,1))}). El DCF inverso indica que el precio de US$11,61 equivale a Ke {pct(inv["keImplicito"],1)} con los flujos Base, o a {pct(inv["utilidadRelativaImplicita"],0)} de la utilidad Base con el Ke Base.',
 f'Reserva material de capital: el modelo mide el capital con utilidad/ROE; el control regulatorio (APR aproximado por ingresos) muestra patrimonio/APR subiendo de {pct(capital[0]["patrimonioSobreAPR"],0)} a {pct(capital[-1]["patrimonioSobreAPR"],0)}. Si el patrimonio se mantuviera en 40 % del APR el valor subiría a {usd(alt["valor"][3])} (35 %: {usd(alt["valor"][2])}; 30 %: {usd(alt["valor"][1])}). El APR por país (Brasil prudencial, México, Colombia) no se proyecta entidad por entidad.',
 'El CET1 de Brasil (11,9 %, conglomerado prudencial) no cubre el perímetro completo; México y Colombia solo informan índices de capital total. No se compara con el patrimonio contable consolidado, que incluye impuestos diferidos activos (US$3.649 M), plusvalía e intangibles.',
 'ROE terminal Base 16 % (ventaja durable según la regla de moat, entre el costo del patrimonio y el ROE actual de 29–33 %): juicio del analista, con matriz ROE terminal × g en la hoja.',
 'Múltiplos: P/E y P/BV son contrastes con peso 0; sus múltiplos de salida son juicios entre la serie propia de NU (26–39× P/E 2023–2025) y los pares brasileños (3–9×); no son una confirmación independiente del DCF. P/FCFE queda PENDIENTE_ANCLA (peso 0): el FCFE de un banco en crecimiento acelerado es residual y no comparable.',
 'Calidad de utilidades: de la utilidad del 1S26 (US$1.932 M), US$991 M son beneficio de impuesto diferido (impuesto corriente US$1.249 M frente a utilidad antes de impuestos de US$2.191 M; tasa efectiva contable 11,8 % frente a 28,7 % en el 1S25). Los márgenes netos de las historias se normalizan a una tasa efectiva cercana al 26 % (la de 2025); el UDM de 18,65 % de margen neto está inflado por ese efecto y el impuesto diferido crece con la cartera (activo por impuesto diferido US$3.649 M).',
 'Contexto de mercado posterior a las elecciones de Brasil del 25-oct-2026 (prensa: caída de acciones brasileñas, Selic 13,75 % con riesgo de alza en el Copom del 4-nov). La prima país de Damodaran de la hoja es la de enero y no incorpora ese movimiento.',
 'Dilución: se usan 4.908,8 M de acciones diluidas (promedio 1S26) con el gasto en acciones dentro de la utilidad; sin recompras proyectadas. El programa de US$1.000 M (US$500,4 M ejecutados al 30-jun-2026) no se suma al FCFE.',
 'Capital de la matriz Nu Holdings (Caimán) vs. subsidiarias: no se modela la repatriación de dividendos ni el impuesto de retención.',
 'Control de integridad de hoja abierto (igual que XP): scripts/integridad_hojas.py NU devuelve 4 hallazgos («sin valor comparable de historia A-D en Escenarios e historias!H5:H8») porque esas celdas son fórmulas del motor FCFF industrial de la plantilla, que no se alimenta en un banco y no se sobrescriben con cifras. El valor oficial de esta revisión está en NU FCFE; estados completos = 0 hallazgos; las matrices industriales vaciadas se respaldaron.',
 'Hechos posteriores al corte contable relevantes: lanzamiento del banco en México (ago-2026), licencia bancaria completa en Brasil en trámite, renuncia del CTO (6-K del 23-oct-2026); ninguno cambia las cifras del modelo.']
v = {
 'ticker': 'NU', 'nombreActivo': 'Nu Holdings Ltd. (NYSE: NU)', 'revisionId': REV, 'revision_id': REV,
 'fecha': '2026-11-02', 'fechaRevision': '2026-11-02', 'fechaCorteContable': '2026-06-30', 'fecha_corte': '2026-06-30',
 'moneda': 'USD', 'currency': 'USD', 'monedaEstados': 'USD', 'unidadesEstados': 'US$ millones', 'market': 'US',
 'precio': price, 'precioAnalisis': price, 'precioReferenciaFecha': '2026-10-30',
 'precioReferenciaFuente': 'Cierre NYSE 30-oct-2026 (Yahoo Finance, auto_adjust=False)',
 'tipo': 'Financiera · banco digital (Brasil, México, Colombia)',
 'metodo_valoracion': 'A', 'version_metodo': 'A-1.2', 'metodoPrincipal': 'DCF FCFE financiero', 'metodoCalculoPrimario': 'FCFE en US$ descontado a Ke en US$; patrimonio requerido = utilidad / ROE',
 'hojaGoogle': f"https://docs.google.com/spreadsheets/d/{cap['sheet_id']}/edit", 'sheet_id': cap['sheet_id'],
 'estado': 'EN_REVISION', 'publicationStatus': 'EN_REVISION', 'publicationStage': 'PREPUBLICACION_CONTROLADA',
 'publicationAuthorized': False, 'publicadaEnApp': False, 'valorVigenteEnCatalogo': False,
 'auditPendingUserVisualReview': True, 'auditoriaEconomica': 'NO_REALIZADA_PENDIENTE_REVISION_VISUAL', 'certificacionEconomica': 'NO_CERTIFICADA',
 'validationStatus': 'CONTROLES_HOJA_APROBADOS_PENDIENTE_CI_Y_QA', 'reportSchema': 'jmr-valuation-two-levels-v5',
 'valorPrincipal': base, 'valorIndependiente': base, 'mos': 0.35, 'precioMOS': mos, 'precioMOSMax': mos, 'precioMOSHoy': mos, 'baseMOS': 'dcfBase',
 'escenarios': {'conservador': val['Conservador'], 'base': base, 'optimista': val['Optimista'], 'disrupcion': val['Disrupcion']},
 'valorEsperado': {'valor': prom, 'valorCentral': base, 'tipoPromedio': '3_historias_renormalizado', 'disrupcionSeparada': True, 'escenariosUnificados': True, 'historias': hist},
 'metodos': metodos,
 'descuentoMultiples': {'version': 2, 'estado': 'COMPARACION_SECUNDARIA_EN_REVISION', 'horizonteAnios': 3, 'pesoDcf': 1, 'pesoMultiplos': 0,
     'metodos': [{'nombre': m['nombre'], 'peso': 0, 'estado': m['estado'], 'base': {'vp': [None, None, m['valorHoy']['base']], 'consolidado': m['valorHoy']['base']}} for m in metodos_mult],
     'nota': 'Contraste FY+3 → valor presente a Ke de cada historia. Peso 0: anclas parciales (serie propia y pares), sin certificación.'},
 'sensibilidadDCF': {'tipo': 'FCFE', 'estado': 'CALCULADA_NATIVA_EN_HOJA', 'centro': base, 'centroConciliado': True, 'fuente': "NU Sensibilidad!A4:F29",
     'matrices': [{'title': 'Ke × g terminal', 'rows': s1[0], 'columns': s1[1], 'values': s1[2], 'rowsLabel': 'Ke', 'columnsLabel': 'g'},
                  {'title': 'ROE terminal × g', 'rows': s2[0], 'columns': s2[1], 'values': s2[2], 'rowsLabel': 'ROE terminal', 'columnsLabel': 'g'},
                  {'title': 'Utilidad relativa (margen/escala) × Ke', 'rows': s3[0], 'columns': s3[1], 'values': s3[2], 'rowsLabel': 'Utilidad relativa a la Base', 'columnsLabel': 'Ke'}],
     'dcfInverso': inv, 'alternativaCapital': alt},
 'sensibilidadMultiples': SENS_MULT,
 'supuestosModeloA': {'horizonteAnios': 10, 'unidades': 'US$ millones', 'rf': cell(F, 7, 1), 'erpMadura': cell(F, 8, 1), 'crpPonderada': cell(F, 15, 1),
     'ingresosUDM': cell(F, 16, 1), 'utilidadAtribuibleUDM': cell(F, 17, 1), 'patrimonioAtribuible': cell(F, 18, 1), 'accionesDiluidasM': cell(F, 19, 1),
     'gTerminal': g, 'ke': ke, 'roeTerminal': roet, 'metodoReinversion': 'patrimonio requerido = utilidad / ROE; FCFE = utilidad − variación del patrimonio requerido',
     'controlCapitalRegulatorio': capital, 'capitalRegulatorio2T26': {'brasil': {'APR': 35710.139, 'CET1': 4262.877, 'CET1ratio': 0.119, 'CAR': 0.157}, 'mexico': {'capital': 427.572, 'indice': 0.149}, 'colombia': {'capital': 179.741, 'indice': 0.153}}},
 'nivel2ProyeccionBase': proy,
 'fuentes_supuestos': ['https://www.sec.gov/Archives/edgar/data/1691493/000129281426002166/nuform20f_2025.htm',
     'https://www.sec.gov/Archives/edgar/data/1691493/000129281426004225/nufs2q26_6k.htm',
     'https://www.sec.gov/Archives/edgar/data/1691493/000129281426004222/nupr2q26_6k.htm',
     'https://www.sec.gov/Archives/edgar/data/1691493/000129281426005000/nu20261023_6k.htm',
     'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value_month=202610',
     'https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html'],
 'salvedades': sal,
 'reporteFuentes': {'captura': f'evidencia/captura-hoja-20261102/{REV}_resultados_hoja.json', 'sha256': sha},
 'revisionOrigen': 'NU-20261029-R1 (candidato, conservada sin cambios); esta revisión es una copia limpia de la plantilla IA vigente sin supuestos heredados.',
 'controlEditorial': {'nivel1Capitulos': 14, 'nivel2Apartados': 12, 'estado': 'PENDIENTE'}}
(OUT / 'VALORACION_A12_EN_REVISION.json').write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
print('OK', {k: round(x, 4) for k, x in val.items()}, 'prom', round(prom, 4), 'MOS', round(mos, 4), sha[:12], 'matrices', list(tops))
