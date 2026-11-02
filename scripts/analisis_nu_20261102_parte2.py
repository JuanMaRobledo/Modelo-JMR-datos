#!/usr/bin/env python3
"""NU-20261102-A12-R1 · Nivel 2 (12 apartados reproducibles). Tablas leídas de la captura de la hoja (SHA-256) y de los estados fuente."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
REV = 'NU-20261102-A12-R1'
V = json.loads((ROOT / f'candidatos/valoraciones/{REV}/VALORACION_A12_EN_REVISION.json').read_text())
CAPT = json.loads((ROOT / f'evidencia/captura-hoja-20261102/{REV}_resultados_hoja.json').read_text())
EST = json.loads(Path('/home/user/JMR-valuation/reference/desde_cero/NU/estados_fuente_2026-10-11.json').read_text())
F = CAPT['data']['fcfe']; FORM = CAPT['formulas']['fcfe']; S = CAPT['data']['sens']; M = CAPT['data']['mult']
INI = {'Base': 34, 'Conservadora': 54, 'Optimista': 74, 'Disrupción': 94}
KEY = {'Base': 'Base', 'Conservadora': 'Conservador', 'Optimista': 'Optimista', 'Disrupción': 'Disrupcion'}


def cell(t, r, c):
    row = t[r - 1] if r - 1 < len(t) else []
    return row[c] if c < len(row) else None


def n(x, d=0):
    if x is None or x == '':
        return 'N/D'
    return f'{x:,.{d}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
pc = lambda x, d=1: 'N/D' if x is None else n(x * 100, d) + ' %'
usd = lambda x, d=2: 'US$' + n(x, d)
P = lambda t: f'<p>{t}</p>'


def tabla(cap, heads, rows):
    h = ''.join(f'<th>{x}</th>' for x in heads)
    b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table><caption>{cap}</caption><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'


def motor(esc):
    """Recálculo independiente en Python del motor FCFE con las entradas leídas de la hoja."""
    b = INI[esc]; sc = 23 + list(INI).index(esc)
    ke = cell(F, sc, 3); roet = cell(F, sc, 4); g = cell(F, 20, 1)
    rev = cell(F, 16, 1); E = cell(F, 18, 1); pv = 0; ni = 0
    for y in range(1, 11):
        gr, m, roe = cell(F, b + y, 1), cell(F, b + y, 3), cell(F, b + y, 5)
        rev *= 1 + gr; ni = rev * m; eq = ni / roe; pv += (ni - (eq - E)) / (1 + ke) ** y; E = eq
    pv += ni * (1 + g) * (1 - g / roet) / (ke - g) / (1 + ke) ** 10
    dias = cell(F, 5, 1)
    return pv * (1 + ke) ** (dias / 365) / cell(F, 19, 1)


S2 = []


def sec(t, *p):
    S2.append((t, ''.join(p)))


# --- 1 históricos
per = EST['periodos']; r_, b_ = EST['resultados'], EST['balance']
filas = []
for lab, key, d in [('Ingresos totales', 'ingresos_totales', 0), ('Utilidad bruta', 'utilidad_bruta', 0), ('Gastos operativos totales', 'gastos_operativos_total', 0),
                    ('Utilidad antes de impuestos', 'utilidad_antes_impuestos', 0), ('Impuestos', 'impuestos', 0), ('Utilidad neta de la controladora', 'utilidad_controladora', 0),
                    ('BPA diluido (US$)', 'bpa_diluido', 4), ('Acciones diluidas promedio (M)', 'acciones_diluidas_prom_millones', 1)]:
    filas.append([lab] + [n(x, d) for x in r_[key]])
udm = lambda v: v[4] + v[6] - v[5]
filas[0].append(n(udm(r_['ingresos_totales']), 0)); filas[3].append(n(udm(r_['utilidad_antes_impuestos']), 0)); filas[5].append(n(udm(r_['utilidad_controladora']), 0))
for i in (1, 2, 4, 6, 7): filas[i].append('')
heads = ['Concepto (US$ M)'] + per + ['UDM jun-26']
sec('1. Históricos y base de datos',
    P('Series NIIF en millones de US$ (20-F 2023 y 2025 y 6-K del 2T26; transcritas en reference/desde_cero/NU/estados_fuente_2026-10-11.json y verificadas contra el 20-F 2025 y el 6-K del 2T26 en esta revisión). 1S25 y 1S26 son los seis primeros meses; UDM = 2025 + 1S26 − 1S25. La pérdida de 2021 y 2022 incluye en 2022 US$355,6 millones de terminación de un plan de acciones contingentes (partida de una vez).'),
    tabla('Estado de resultados', heads, filas),
    tabla('Balance (US$ M, cierres de diciembre y 30-jun-2026)', ['Concepto'] + ['2021', '2022', '2023', '2024', '2025', '30-jun-26'],
          [['Activos totales'] + [n(x, 0) for x in b_['activos_totales']], ['Depósitos'] + [n(x, 0) for x in b_['depositos']],
           ['Patrimonio de la controladora'] + [n(x, 0) for x in b_['patrimonio_controladora']]]),
    P('Las 46 pestañas de la plantilla tienen sus tres estados completos (control estados_completos = 0 hallazgos); el balance UDM de la hoja corresponde al 30-jun-2026. El importador estándar no lee XBRL NIIF, por lo que las series provienen de los 20-F y del 6-K, con nota por celda.'))

# --- 2 fuentes
ent = [('Precio (cierre 30-oct-2026)', cell(F, 6, 1), "Input sheet!D1", 'Yahoo Finance, NYSE, auto_adjust=False'),
       ('Tasa libre (Treasury 10 años)', cell(F, 7, 1), "Input sheet!B35", 'Departamento del Tesoro de EE.UU., 30-oct-2026'),
       ('Prima madura', cell(F, 8, 1), "Country equity risk premiums!B2", 'Damodaran, oct-2026'),
       ('Prima país ponderada', cell(F, 15, 1), "NU FCFE!B15", 'Tabla Damodaran de la hoja (enero) ponderada por ingresos 1S26 (nota 34 del 6-K)'),
       ('Ingresos UDM', cell(F, 16, 1), "NU FCFE!B16", '20-F 2025 + 6-K 2T26'),
       ('Utilidad atribuible UDM', cell(F, 17, 1), "NU FCFE!B17", '20-F 2025 + 6-K 2T26'),
       ('Patrimonio atribuible 30-jun-26', cell(F, 18, 1), "NU FCFE!B18", '6-K 2T26, estado de situación financiera'),
       ('Acciones diluidas (M)', cell(F, 19, 1), "NU FCFE!B19", '6-K 2T26, promedio ponderado diluido 1S26'),
       ('g terminal', cell(F, 20, 1), "NU FCFE!B20", '4 % con techo en la tasa libre (regla de la casa)')]
sec('2. Fuentes y trazabilidad de las entradas',
    tabla('Entradas del motor y su origen', ['Entrada', 'Valor', 'Celda', 'Fuente'], [[a, (n(b, 4) if b is not None and abs(b) < 1 else n(b, 3)), c, d] for a, b, c, d in ent]),
    P('Clasificación: precio, tasas, estados y acciones son datos; la prima país ponderada es un cálculo; beta, márgenes, ROE y crecimiento son juicios del analista, documentados en el apartado 3. Contradicciones materiales reconocidas: la utilidad del 1S26 incluye US$991 millones de impuesto diferido; la prima país es de enero; el consenso de analistas no se usó como ancla.'))

# --- 3 supuestos
rows3 = []
for esc, b in INI.items():
    for lab, col, fmt in (('Crec. ingresos', 1, pc), ('Margen neto', 3, pc), ('ROE', 5, pc)):
        rows3.append([esc, lab] + [fmt(cell(F, b + y, col)) for y in range(1, 11)])
sc_rows = [[esc, n(cell(F, 23 + i, 1), 2), n(cell(F, 23 + i, 2), 1), pc(cell(F, 23 + i, 3), 2), pc(cell(F, 23 + i, 4), 1), pc(cell(F, 23 + i, 5), 1)] for i, esc in enumerate(INI)]
sec('3. Supuestos por historia',
    tabla('Parámetros de costo del patrimonio y terminal', ['Historia', 'Beta', '× prima país', 'Ke', 'ROE terminal', 'Probabilidad previa'], sc_rows),
    tabla('Trayectorias anuales (años 1 a 10)', ['Historia', 'Variable'] + [f'A{y}' for y in range(1, 11)], rows3),
    P('Justificación: ver capítulos 7, 10 y 11 del Nivel 1. Los márgenes netos están normalizados a una tasa efectiva cercana al 26 % porque el UDM contiene beneficio de impuesto diferido. La Disrupción tiene ROE terminal igual al Ke (sin ventaja residual).'))

# --- 4 fórmulas
fl = lambda a: next((r for r in range(1, len(FORM) + 1) if False), None)
f35 = {k: cell(FORM, 35, i) for k, i in (('Ingresos', 2), ('Utilidad', 4), ('Patrimonio requerido', 6), ('Δ patrimonio', 7), ('FCFE', 8), ('Factor', 9), ('VP', 10))}
f36 = cell(FORM, 36, 7)
sec('4. Fórmulas efectivamente utilizadas',
    P('Fórmulas literales de Google Sheets (pestaña «NU FCFE», historia Base, año 1; separador «;» y coma decimal por la configuración regional es_ES de la hoja):'),
    tabla('Fórmulas del año 1', ['Concepto', 'Fórmula'], [[k, f'<code>{v}</code>'] for k, v in f35.items()] + [['Δ patrimonio (años 2 a 10)', f'<code>{f36}</code>']]),
    tabla('Fórmulas del resumen de la historia Base', ['Concepto', 'Fórmula'],
          [['VP FCFE', f'<code>{cell(FORM, 45, 1)}</code>'], ['FCFE terminal', f'<code>{cell(FORM, 46, 1)}</code>'], ['Valor terminal', f'<code>{cell(FORM, 47, 1)}</code>'],
           ['VP valor terminal', f'<code>{cell(FORM, 48, 1)}</code>'], ['Valor del patrimonio', f'<code>{cell(FORM, 49, 1)}</code>'], ['Valor por acción', f'<code>{cell(FORM, 50, 1)}</code>']]),
    P('Fórmulas algebraicas: Utilidad = Ingresos × Margen neto; Patrimonio requerido = Utilidad ÷ ROE; FCFE = Utilidad − (Patrimonio requerido_t − Patrimonio requerido_t−1), con el patrimonio contable del 30-jun-2026 como punto de partida; Ke = Rf + β × ERP madura + Prima país ponderada; Valor terminal = Utilidad_10 × (1+g) × (1 − g/ROE_T) ÷ (Ke − g). Todas las celdas de resultado son fórmulas; no hay cifras escritas a mano en salidas.'))

# --- 5 proyección Base
b = INI['Base']
pr = [[f'A{y}', n(cell(F, b + y, 2)), pc(cell(F, b + y, 1)), pc(cell(F, b + y, 3)), n(cell(F, b + y, 4)), pc(cell(F, b + y, 5)), n(cell(F, b + y, 6)), n(cell(F, b + y, 7)), n(cell(F, b + y, 8)), n(cell(F, b + y, 10))] for y in range(1, 11)]
sec('5. Proyección Base a diez años',
    tabla('Historia Base (US$ M)', ['Año', 'Ingresos', 'Crec.', 'Margen neto', 'Utilidad', 'ROE', 'Patrimonio requerido', 'Δ patrimonio', 'FCFE', 'VP FCFE'], pr),
    P('El año 1 corresponde a los doce meses a junio de 2027. El FCFE es bajo al comienzo porque el crecimiento alto exige retener patrimonio; crece más rápido que la utilidad cuando el crecimiento se modera.'))

# --- 6 DCF
rs = [['VP de los FCFE años 1–10', n(cell(F, b + 11, 1))], ['FCFE terminal (año 11)', n(cell(F, b + 12, 1))], ['Valor terminal en el año 10', n(cell(F, b + 13, 1))],
      ['VP del valor terminal', n(cell(F, b + 14, 1))], ['Valor del patrimonio al 30-jun-2026', n(cell(F, b + 15, 1))],
      ['Capitalización al Ke hasta el 30-oct-2026 (días)', n(cell(F, 5, 1))], ['Acciones diluidas (M)', n(cell(F, 19, 1), 1)], ['Valor por acción (US$)', n(cell(F, b + 16, 1), 4)]]
sec('6. DCF, valor terminal y puente a patrimonio',
    tabla('Puente del DCF FCFE Base (US$ M salvo por acción)', ['Concepto', 'Valor'], rs),
    P('No hay puente EV → equity: el FCFE ya es del accionista. Depósitos, fondeo en mercados y arrendamientos NIIF 16 son parte de la operación bancaria; las participaciones en asociadas (US$93 millones) y los minoritarios (US$2 millones) son inmateriales y no se ajustan. El valor terminal es '
      f'{pc(cell(F, b + 14, 1) / cell(F, b + 15, 1), 0)} del valor del patrimonio.'))

# --- 7 escenarios
esc_rows = []
for i, (esc, bb) in enumerate(INI.items()):
    esc_rows.append([esc, pc(cell(F, 23 + i, 5), 1), pc(cell(F, 23 + i, 3), 2), n(cell(F, bb + 10, 4)), n(cell(F, bb + 15, 1)), usd(cell(F, bb + 16, 1)), usd(cell(F, bb + 16, 1) * 0.65)])
sec('7. Cuatro escenarios',
    tabla('Resultados por historia', ['Historia', 'Prob. previa', 'Ke', 'Utilidad año 10', 'Patrimonio al corte (US$ M)', 'Valor por acción', 'Valor × 0,65'], esc_rows),
    P(f'Promedio ponderado ordinario (Conservadora, Base y Optimista, pesos renormalizados): {usd(cell(F, 10, 8))}. Disrupción aparte: {usd(cell(F, 8, 8))}. MOS 35 % sobre la Base: {usd(cell(F, 12, 8))}. Precio observado {usd(cell(F, 6, 1))}.'))

# --- 8 múltiplos
mr = []
for r in range(22, 34):
    mr.append([cell(M, r, 0), cell(M, r, 1), n(cell(M, r, 2), 1), n(cell(M, r, 3)), n(cell(M, r, 4)), pc(cell(M, r, 6), 2), usd(cell(M, r, 7)), cell(M, r, 8)])
sec('8. Valoración por múltiplos y descuento a valor presente',
    P('Contrato: precio FY+3 = múltiplo de salida × métrica FY+3 ÷ acciones; valor presente = precio FY+3 ÷ (1+Ke)^(3 − días/365). FY+3 = junio de 2029. Métricas: utilidad (P/E), FCFE (P/FCFE) y patrimonio requerido (P/BV) del año 3 de cada historia. Peso en el valor principal: 0 en los tres.'),
    tabla('Cálculo por método e historia', ['Método', 'Historia', 'Múltiplo salida', 'Métrica FY+3 (US$ M)', 'Precio FY+3', 'Ke', 'VP por acción', 'Estado'], mr),
    P('Anclas: serie propia de NU (P/E 39,3× / 26,4× / 28,9× en diciembre de 2023-2025; P/BV 6,3× / 6,8× / 7,3×) y pares brasileños (P/E mediano 5,7×; P/BV mediano 0,85×). Los pares son de mercado, independientes del precio de NU y de los demás métodos; los múltiplos de salida son juicios entre ambos extremos. EV/EBITDA, EV/FCFF y P/OCF: N/A justificado (banco). P/FCFE: PENDIENTE_ANCLA con peso 0.'))


def grid(cap, top_row, tab, fmtr, fmtc, off=1):
    heads = [''] + [fmtc(cell(tab, top_row + 1, j)) for j in range(1, 6)]
    rows = [[fmtr(cell(tab, top_row + 2 + i, 0))] + [n(cell(tab, top_row + 2 + i, j), 2) for j in range(1, 6)] for i in range(5)]
    return tabla(cap, heads, rows)


sec('9. Sensibilidades del DCF',
    P('Matrices 5×5 de la hoja («NU Sensibilidad»), historia Base, valor por acción en US$. El centro de cada matriz iguala el valor Base (control = 0).'),
    grid('Ke (filas) × g terminal (columnas)', 4, S, lambda x: pc(x, 2), lambda x: pc(x, 1)),
    grid('ROE terminal (filas) × g terminal (columnas), con Ke Base', 13, S, lambda x: pc(x, 1), lambda x: pc(x, 1)),
    grid('Utilidad relativa a la Base (filas) × Ke (columnas)', 22, S, lambda x: n(x, 2) + '×', lambda x: pc(x, 2)),
    tabla('DCF inverso', ['Medida', 'Valor'], [['Precio de mercado', usd(cell(S, 32, 1))], ['Utilidad relativa implícita (Ke Base)', pc(cell(S, 33, 1), 1)], ['Ke implícito (flujos Base)', pc(cell(S, 34, 1), 2)]]),
    tabla('Alternativa de capital (no principal): patrimonio = τ × APR aproximado', ['τ'] + [pc(cell(S, 59, j), 0) for j in range(1, 5)],
          [['Valor por acción'] + [usd(cell(S, 71, j)) for j in range(1, 5)], ['vs. Base'] + [pc(cell(S, 72, j), 0) for j in range(1, 5)]]))

mats = []
for r in range(30, 75):
    a = cell(M, r, 0)
    if isinstance(a, str) and a.startswith('Matriz P/'): mats.append((a, r))
sec('10. Sensibilidades de cada múltiplo (matrices 5×5 Base)',
    P('Eje vertical: múltiplo de salida (veces). Eje horizontal: métrica FY+3 en US$ millones (80 % a 120 % de la Base). Celda: valor presente por acción con la fórmula del método. Centro igual al VP de la Base (control = 0). Solo historia Base. La segunda ancla observada al corte (múltiplo actual: P/E 15,8×, P/BV 4,3×) no se mezcla con las elegidas.'),
    *[grid(a, r, M, lambda x: n(x, 1) + '×', lambda x: n(x, 0)) for a, r in mats])

# --- 11 conciliaciones
conc = []
for esc in INI:
    sheet = cell(F, INI[esc] + 16, 1); py = motor(esc)
    conc.append([esc, usd(sheet, 6), usd(py, 6), n(abs(sheet - py), 8), 'OK' if abs(sheet - py) < 1e-6 else 'REVISAR'])
sec('11. Conciliaciones',
    tabla('Hoja de Google Sheets frente a recálculo independiente en Python (mismas entradas)', ['Historia', 'Hoja', 'Python', 'Diferencia', 'Control'], conc),
    P('Otros controles: centros de las seis matrices 5×5 iguales al valor Base o al VP3 del método (diferencia 0); probabilidades suman 100 %; promedio ponderado = Σ valor × peso renormalizado; MOS = Base × 0,65; precio de la hoja = cierre 30-oct-2026; '
      'estados completos (0 hallazgos); integridad de hojas (0 hallazgos); captura de la hoja con SHA-256 en evidencia/captura-hoja-20261102. Cadena de trazabilidad: fuente (20-F/6-K) → hoja Google → captura JSON → este análisis → aplicación.'))

# --- 12 limitaciones
sec('12. Limitaciones y salvedades',
    '<ul>' + ''.join(f'<li>{s}</li>' for s in V['salvedades']) + '</ul>',
    P('Extensión especializada: la plantilla corporativa de 46 pestañas no tiene motor FCFE bancario; se añadieron tres pestañas («NU FCFE», «NU Sensibilidad», «NU Múltiplos») sin modificar las fórmulas oficiales. Las matrices de sensibilidad de las cinco pestañas de múltiplos industriales (EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF) se vaciaron porque devolvían #DIV/0! sin el motor FCFF; sus fórmulas originales están respaldadas en JMR-valuation/reference/backups/nu_a12_matrices_plantilla.json. La pestaña «Resumen de Valoración» de la plantilla no refleja el FCFE: el valor de referencia es el de «NU FCFE».'))


def nivel2_html():
    cuerpo = ''.join(f'<h2 id="jmr-n2-{i+1}">{t}</h2>{b}' for i, (t, b) in enumerate(S2))
    refs = ('<h2>Referencias</h2><ul><li>Nu Holdings Ltd., Formulario 20-F 2025 (SEC, 8-abr-2026).</li><li>Nu Holdings Ltd., 6-K de estados intermedios del 2T26 (SEC, 13-ago-2026).</li>'
            '<li>Nu Holdings Ltd., comunicado de resultados del 2T26 (6-K, 13-ago-2026).</li><li>Nu Holdings Ltd., 6-K del 23-oct-2026.</li><li>Departamento del Tesoro de EE.UU., curva de rendimiento diaria (30-oct-2026).</li>'
            '<li>Damodaran, tablas de prima de riesgo país y betas por industria (hoja de la revisión).</li><li>Yahoo Finance: cierres y múltiplos de pares (2-nov-2026).</li></ul>')
    cab = (f'<h1>Nu Holdings — Nivel 2 reproducible · Método A-1.2 / FCFE nominal US$</h1><p><strong>Fecha de análisis:</strong> 2-nov-2026. <strong>Corte de estados:</strong> 30-jun-2026. '
           f'<strong>Precio referencia:</strong> {usd(V["precio"])} (30-oct-2026). <strong>Unidad:</strong> millones de US$ salvo valores por acción. <strong>Estado:</strong> EN_REVISION, pendiente de auditoría económica.</p>')
    return f'<article data-jmr-revision="{REV}" data-nivel="2" data-metodo="A-1.2">{cab}{cuerpo}{refs}</article>'


if __name__ == '__main__':
    import re
    h = nivel2_html()
    print(len(S2), 'apartados', len(re.sub(r'<[^>]+>', ' ', h).split()), 'palabras', [c[4] for c in conc])
