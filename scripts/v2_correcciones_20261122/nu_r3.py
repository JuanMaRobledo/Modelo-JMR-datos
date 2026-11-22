"""NU R3: valoración bancaria (Equity Excess Return de Damodaran) con contraste FCFF R2.
Escribe empresas/NU.json y analisis/NU.json en la carpeta de trabajo (origen) y el HTML R8 del informe."""
import json, sys, re, copy, hashlib, pathlib
from bs4 import BeautifulSoup
W = pathlib.Path(sys.argv[1]); ORIG = pathlib.Path(sys.argv[2]); INF = pathlib.Path('/home/user/Modelo-JMR-datos/jmr-v2/informes/NU')
REV, ANT = 'NU-V2-LTM20260930-R3', 'NU-V2-LTM20260930-R2'
r2 = json.load(open(ORIG/'empresas/NU.json')); a2 = json.load(open(ORIG/'analisis/NU.json'))
x = json.load(open(W/'NU_R3_exportado.json')); c = json.load(open(W/'calc.json'))
E = c['esc']; B = x['assumptions']['base']; P = 11.27; SH = x['financials']['shares']
def n(v, d=2): return f'{v:,.{d}f}'.replace(',', '@').replace('.', ',').replace('@', '.')
def pc(v, d=1): return n(100*v, d) + ' %'
vb, vc, vo = E['base']['v'], E['conservador']['v'], E['optimista']['v']; mos = vb*0.65; up = vb/P-1; ke = E['base']['ke']
LIBRO_ID = '1DgFEV57MVCOc2yJG0jLVx9evTDxHiKfh'; LIBRO_URL = f'https://drive.google.com/file/d/{LIBRO_ID}/view'
IMG = 'https://raw.githubusercontent.com/JuanMaRobledo/Modelo-JMR-datos/main/jmr-v2/imagenes/NU/'
# ---------------- Expediente ----------------
e = copy.deepcopy(x)
for k in ['cik', 'sector', 'exchange', 'logoUrl', 'logoSource', 'ltm', 'financialPresentation', 'sources', 'annualReportDocuments', 'quarterlyReportDocuments']:
    if k in r2: e[k] = r2[k]
e['company'] = r2['company']; e['units'] = 'millones'; e['priceAsOf'] = r2['priceAsOf']; e['estado'] = 'EN_REVISION'
e['history'] = [h for h in x['history'] if h.get('netIncome') is not None]
for h in e['history']:
    if h['year'] == 2026: h['periodo'] = 'LTM 30-sep-2026'
    else: h['periodo'] = f'FY{h["year"]}'
e['revision'] = {'id': REV, 'anterior': ANT, 'nota': ('R3 (22-nov-2026): Nu se valora como banco (perfil «banco», método de exceso de retorno sobre patrimonio, '
    'réplica verificada de eqexret de Damodaran) porque el 86,1 % de sus ingresos son intereses, capta US$47.487 M de depósitos y su crecimiento está limitado por el CET1. '
    'Ke 10,94 % = 5,15 % + 0,76 × 7,62 %. El FCFF de R2 (US$16,65) se conserva como contraste. Mismo corte LTM 30-sep-2026 y precio 20-nov-2026.')}
lib = e['libro']; lib.update({'id': 'NU-V2-LTM20260930-R3_VALORACION.xlsx', 'url': LIBRO_URL, 'driveFileId': LIBRO_ID, 'contratoVersion': '1.5.6',
    'plantilla': 'eqexret.xls (Aswath Damodaran, NYU Stern; descargado 22-nov-2026) convertido a .xlsx; hojas JMR inyectadas con scripts/v2-libro-financiero.py',
    'costoCapital': {'formulas': True, 'tasaLibre': B['riskFree'], 'erp': B['erp'], 'beta': B['beta'], 'ke': ke,
                     'fuenteBeta': 'Damodaran betaGlobal.xls (5-ene-2026): Bank (Money Center) 0,697; Financial Svcs. (Non-bank & Insurance) 0,823; promedio 0,76'},
    'contrasteFCFF': {'revision': ANT, 'motor': 'fcffsimpleginzu', 'valores': r2['libro']['valores'], 'sha256': r2['libro']['sha256']}})
e['documentLinks'] = {**r2.get('documentLinks', {}), 'workbook': LIBRO_URL, 'workbookExcel': LIBRO_URL, 'workbookR2FCFF': r2['documentLinks']['workbook']}
e['informe'] = {'pdf': f'jmr-v2/informes/NU/{REV}_INFORME_FUNDAMENTAL.pdf', 'html': f'{REV}_INFORME_FUNDAMENTAL.html', 'imagenes': 'jmr-v2/imagenes/NU/'}
e['cierreEditorial'] = {'completo': False, 'pendientes': ['Manifiesto de cierre R3 (analisis/NU.cierre.json) con huellas de análisis, PDF, plantilla y libro.', 'Auditoría independiente (P02).']}
e['analysis'] = {**r2.get('analysis', {}), 'conclusion': f'Valorada como banco (exceso de retorno, Ke {pc(ke,2)}), el Base es US${n(vb)} por acción, apenas {pc(up)} sobre el cierre de US${n(P)}; el precio supera el precio con MOS (US${n(mos)}). La acción descuenta un ROE de ~{pc(c["roeImplicito"],0)} en los años 1–5: la tesis depende de sostener una rentabilidad sobre patrimonio cercana a la actual tras normalizar impuestos y mora.'}
esc_txt = {
 'conservador': ('Mora 90+ persistentemente alta, impuesto pleno de 34 % y competencia de Itaú y Mercado Pago: ROE de 20 % en los años 1–5 y, a largo plazo, igual al costo del patrimonio (sin ventaja).', 0.85),
 'base': ('Nu normaliza su tasa fiscal parcialmente y estabiliza la morosidad: ROE de 26 % (frente a 30,5 % LTM sobre patrimonio promedio) con retención de 80 % para sostener el CET1, y ventaja de costo digital persistente (ROE estable 18 %).', 0.80),
 'optimista': ('Nu sostiene el ROE actual (~30 %) mientras México y Colombia escalan, y conserva una ventaja de costo excepcional (ROE estable 22 %).', 0.80)}
J = {}
J['metodo'] = ('Perfil «banco», método de exceso de retorno (Equity Excess Return de Damodaran): Nu no paga dividendos (DDM no representativo) y retiene capital por exigencia regulatoria. '
  'Damodaran: «For a financial service firm, debt is more raw material than source of capital» y «In general, steer away from valuing the entire firm. Focus on equity value» '
  '(The Valuation of Financial Service Firms, diapositivas 12–13). El 86,1 % de los ingresos de 9M26 son intereses y ganancias financieras, capta US$47.487 M de depósitos y su cartera bruta es US$41.600 M: '
  'es asset-light en activos físicos, no en balance. La guía sectorial JMR admite FCFF solo para fintech de pagos sin captación ni riesgo de crédito propio.')
J['ke'] = (f'Ke {pc(ke,2)} = tasa libre 5,15 % + beta 0,76 × ERP 7,62 %. Beta: promedio de las betas apalancadas globales de Damodaran (5-ene-2026) de Bank (Money Center) 0,697 y Financial Svcs. (Non-bank & Insurance) 0,823, '
  'por ser banco digital y financiera de consumo sin garantías; en bancos la beta ya incorpora el apalancamiento y no se reapalanca con depósitos. ERP 7,62 % = prima madura 3,387 % + prima país regional 4,233 % (Brasil 90 % de ingresos). '
  f'Común a los tres escenarios y a perpetuidad (el riesgo país no desaparece). Con la beta de R2 (0,806) el Base sería US${n(c["sensBeta"]["b0806"])}.')
J['roe'] = ('Se aplica en los años 1–5 y luego converge al estable. LTM 27,3 % sobre patrimonio final y 30,5 % sobre promedio, con tasa efectiva de 15,2 %; FY2024 25,8 % y FY2025 25,4 %. '
  'Base 26 %: normalización parcial del impuesto hacia 34 % y costo de riesgo estable; Conservador 20 % (impuesto pleno y mora alta); Optimista 30 % (ROE actual sostenido).')
J['retencion'] = ('Retención: dividendos 0 y recompras de US$500 M (13 % de la utilidad LTM). Base 80 %: el patrimonio crece ~21 % anual (ROE × retención), similar a los activos ponderados por riesgo, '
  'para sostener el CET1 de 12,1 % sobre el mínimo de 7,0 %. Conservador 85 % (más capital por crecimiento con menor ROE).')
J['roeEstable'] = ('ROE estable desde el año 10: Base 18 % (ventaja de costo digital: eficiencia 19,3 % y costo por cliente de US$1,1/mes frente a la banca tradicional), Conservador = Ke (sin renta económica), Optimista 22 %. '
  'Payout estable = 1 − g/ROE (78 % en Base).')
J['terminal'] = 'Crecimiento estable 4 % nominal en USD, inferior a la tasa libre de 5,15 %; Ke estable igual al inicial.'
J['capitalRegulatorio'] = 'CET1 del conglomerado prudencial Tipo 3 de Brasil 12,1 % (mínimo 7,0 %) al 30-sep-2026 (Form 6-K 3T26, Slide 22); cayó 90 pb en nueve meses mientras los APR crecían 28,3 %.'
J['contrasteFCFF'] = (f'R2 (FCFF Simple Ginsu, WACC 11,29 %, ventas/capital 1,8×) daba US${n(r2["libro"]["valores"]["base"])}. El FCFF excluye depósitos de la deuda y su WACC equivale en la práctica al costo del patrimonio, '
  'pero el ventas/capital de 1,8× supone menos capital por dólar de ingresos que el actual (ingresos/patrimonio = 1,46×), lo que subestima la retención exigida por el CET1. Se conserva como contraste, no como valor principal.')
J['escenarios'] = {}
for s, (t, ret) in esc_txt.items():
    a = x['assumptions'][s]; v = E[s]['v']
    J['escenarios'][s] = {
     'tesis': f'{t} Valor US${n(v)} por acción (mismo motor que el libro).',
     'crecimiento': f'El patrimonio crece ROE × retención = {pc(a["roeHighGrowth"]*a["retentionHighGrowth"])} anual en los años 1–5 y converge a {pc(a["stableGrowth"])} perpetuo. ' + J['retencion'],
     'margenes': f'ROE de alto crecimiento {pc(a["roeHighGrowth"])}. ' + J['roe'],
     'reinversion': f'Retención {pc(a["retentionHighGrowth"],0)} de la utilidad como capital común regulatorio (reinversión del banco). ' + J['capitalRegulatorio'],
     'roic': f'ROE estable {pc(a["roeStable"])} frente a Ke {pc(ke,2)}. ' + J['roeEstable'],
     'descuento': J['ke'],
     'terminal': J['terminal'] + f' Payout estable {pc(1-a["stableGrowth"]/a["roeStable"],0)}.',
     'evidencia': 'Form 20-F FY2025 y Form 6-K 3T26: utilidad neta LTM US$3.918,9 M, patrimonio común US$14.342,6 M, depósitos US$47.487 M, cartera bruta US$41.600 M, CET1 12,1 %; libro R3 recalculado (paridad libro–motor 0,000 %).',
     'contraevidencia': 'La mora 90+ subió a 7,3 % y las provisiones crecieron con fuerza; la tasa efectiva de 15,2 % puede normalizarse hacia 34 %; el CET1 cae si los APR crecen más que el patrimonio; concentración en Brasil (90 % de ingresos) y control de voto del fundador (74,4 %).'}
e['justificaciones'] = J
w = [x for x in r2.get('warnings', []) if not re.search(r'WACC|FCFF|Ginsu|S2C|V13|V14|Corrección pendiente', x)]
w += [f'R3 cambia el método a banco (exceso de retorno) y el valor Base de US$16,65 (R2, FCFF) a US${n(vb)}; R2 se conserva como contraste y en el historial.',
      'Datos 2017–2019 N/D en el libro; la historia útil empieza en FY2020 (pérdidas 2020–2022).',
      'Pendiente de auditoría independiente (P02).']
e['warnings'] = w
# ---------------- Análisis: capítulos reescritos ----------------
yb = E['base']['years']
def tabla(cab, filas):
    return '<table><thead><tr>' + ''.join(f'<th>{h}</th>' for h in cab) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{v}</td>' for v in f) + '</tr>' for f in filas) + '</tbody></table>'
A = {s: x['assumptions'][s] for s in ['conservador', 'base', 'optimista']}
filas_sup = [
 ['ROE de alto crecimiento (años 1–5)'] + [pc(A[s]['roeHighGrowth']) for s in A],
 ['Retención de utilidades (1 − payout)'] + [pc(A[s]['retentionHighGrowth'], 0) for s in A],
 ['Crecimiento del patrimonio implícito (ROE × retención)'] + [pc(A[s]['roeHighGrowth']*A[s]['retentionHighGrowth']) for s in A],
 ['ROE estable (año 10 en adelante)'] + [pc(A[s]['roeStable']) for s in A],
 ['Payout estable (1 − g / ROE estable)'] + [pc(1-A[s]['stableGrowth']/A[s]['roeStable'], 0) for s in A],
 ['Costo del patrimonio (Ke)'] + [pc(ke, 2)]*3, ['Crecimiento estable (g)'] + [pc(A[s]['stableGrowth']) for s in A],
 ['Años de alto crecimiento (convergencia en la segunda mitad)'] + ['10']*3,
 ['Valor por acción'] + [f'US${n(E[s]["v"])}' for s in A]]
sup = f'''<div class="essential"><div class="label">Lo esencial</div><ul>
<li><strong>Método R3:</strong> Nu se valora como <strong>banco</strong> con el modelo de <strong>exceso de retorno sobre patrimonio</strong> de Damodaran (<code>eqexret</code>): valor = patrimonio común + valor presente de (ROE − Ke) × patrimonio. Sustituye al FCFF de R2, que se conserva como contraste.</li>
<li><strong>Costo del patrimonio {pc(ke,2)}</strong> = 5,15 % + 0,76 × 7,62 % (beta global de bancos y financieras de consumo; ERP de Brasil/LatAm), común a los tres escenarios y a perpetuidad.</li>
<li><strong>Base:</strong> ROE de 26 % en los años 1–5 (normalización parcial del impuesto), retención de 80 % para sostener el CET1 y ROE estable de 18 % → <strong>US${n(vb)}</strong>. Conservador US${n(vc)} · Optimista US${n(vo)}.</li>
<li>El precio de US${n(P)} equivale a un ROE sostenido de ~{pc(c["roeImplicito"],0)} en los años 1–5: el mercado descuenta casi exactamente el Base.</li></ul></div>
<h3>Por qué un banco y no una fintech operativa</h3>
<p>Damodaran distingue a las empresas financieras porque en ellas <em>«debt is more raw material than source of capital»</em> y recomienda <em>«In general, steer away from valuing the entire firm. Focus on equity value»</em>; para medir la reinversión propone <em>«treat retained earnings as an investment in equity capital which generates growth possibilities»</em> (<em>The Valuation of Financial Service Firms</em>, diapositivas 12–13). La pregunta decisiva no es si la empresa tiene sucursales, sino si capta y presta: el carácter <em>asset-light</em> de Nu es físico (no tiene red de oficinas), no financiero.</p>
<p>Los estados de Nu lo confirman: el <strong>86,1 %</strong> de los ingresos IFRS de 9M26 son intereses y ganancias financieras; capta <strong>US$47.487 M</strong> de depósitos; su cartera bruta es de <strong>US$41.600 M</strong>; y su crecimiento está limitado por el <strong>CET1</strong> (12,1 % frente a un mínimo de 7,0 %, con caída de 90 pb en nueve meses mientras los activos ponderados por riesgo crecían 28,3 %). Activos totales de US$87.429 M sobre un patrimonio de US$14.343 M (6,1×). La guía sectorial JMR solo admite FCFF para una fintech de pagos «sin captación ni riesgo crediticio propio». MercadoLibre es distinto: Damodaran la valora con FCFF porque su núcleo es el comercio y el crédito es un segmento; en Nu el crédito es el negocio.</p>
<h3>Supuestos por escenario</h3>
{tabla(['Supuesto', 'Conservador', 'Base', 'Optimista'], filas_sup)}
<p class="source">Fuente: libro oficial {REV}_VALORACION.xlsx («JMR Escenarios» → «Inputs» de eqexret), recalculado con LibreOffice; mismo motor V2 «exceso» (paridad 0,000 %).</p>
<h3>De historia a números</h3>
<p><strong>ROE de alto crecimiento.</strong> {J["roe"]} <em>Contraevidencia:</em> la mora 90+ subió a 7,3 % y las provisiones crediticias crecieron con más fuerza que la cartera; un costo de riesgo más alto o una carga fiscal plena llevarían el ROE hacia el 20 % del Conservador.</p>
<p><strong>Retención y capital regulatorio.</strong> {J["retencion"]} En este modelo retener más solo crea valor si el ROE supera al Ke; por eso la prueba relevante de capital es un ROE menor por exigir más patrimonio para la misma utilidad (prueba S3 del capítulo de destrucción de valor).</p>
<p><strong>ROE estable.</strong> {J["roeEstable"]} <em>Contraevidencia:</em> la competencia de Itaú, Bradesco, Mercado Pago y los bancos digitales puede erosionar la ventaja de costo; con ROE estable igual al Ke el Base caería a US${n(c["sensRoe"]["rows"][2][0])}.</p>
<p><strong>Costo del patrimonio.</strong> {J["ke"]}</p>
<p><strong>Crecimiento estable.</strong> {J["terminal"]}</p>
<figure><img alt="Patrimonio y ROE proyectados" src="{IMG}trayectorias_r3.png"/><figcaption>Patrimonio común al inicio de cada año y ROE proyectado frente al Ke en los tres escenarios (motor V2 «exceso», libro R3).</figcaption></figure>
<h3>Proyección del escenario Base (US$ millones)</h3>
{tabla(['Año', 'Patrimonio inicial', 'ROE', 'Utilidad neta', 'Costo del patrimonio', 'Exceso de retorno', 'Payout'], [[r['t'], n(r['bv'],0), pc(r['roe']), n(r['ni'],0), n(r['bv']*ke,0), n(r['exc'],0), pc(r['payout'],0)] for r in yb])}
<p class="source">Fuente: motor V2 «exceso» (réplica de eqexret): patrimonio_t+1 = patrimonio_t + utilidad × retención; costo = patrimonio × Ke.</p>
{BeautifulSoup(open(W/"hechos_posteriores.html").read(),"html.parser").find("h3")}{BeautifulSoup(open(W/"hechos_posteriores.html").read(),"html.parser").find("p")}
<div class="reading"><strong>Nuestra lectura.</strong> El Base no exige que Nu mantenga su ROE actual: supone una normalización a 26 % y, a largo plazo, 18 %, todavía muy por encima del Ke. Aun así, el valor apenas supera el precio: el mercado ya paga la ventaja estructural y deja poco margen para errores en mora o impuestos.</div>'''
pvExcT = E['base']['pvExc']*SH; pvTVT = E['base']['pvTV']*SH; eq = vb*SH
val = f'''<div class="essential"><div class="label">Lo esencial</div><ul>
<li>Con el método bancario de Damodaran, Nu vale <strong>US${n(vb)} por acción en el Base</strong> ({"+" if up>=0 else ""}{pc(up)} sobre el cierre de US${n(P)} del 20-nov-2026), en un rango de <strong>US${n(vc)}</strong> (Conservador) a <strong>US${n(vo)}</strong> (Optimista).</li>
<li>El precio con margen de seguridad de 35 % es <strong>US${n(mos)}</strong>: la acción cotiza {pc(P/mos-1,0)} por encima, así que no ofrece margen de seguridad.</li>
<li>El valor R2 con FCFF (US$16,65) sobrestimaba el valor porque exigía menos capital por dólar de ingresos que el que hoy inmoviliza Nu.</li></ul></div>
<h3>Del patrimonio contable al valor del patrimonio (Base · US$ millones)</h3>
{tabla(['Componente', 'US$ millones', 'US$ por acción', '% del valor'], [
 ['Patrimonio común al 30-sep-2026', n(x['financials']['bookEquity'],1), n(E['base']['bv0']), pc(E['base']['bv0']/vb)],
 ['+ VP del exceso de retorno, años 1–10', n(pvExcT,1), n(E['base']['pvExc']), pc(E['base']['pvExc']/vb)],
 ['+ VP del exceso de retorno terminal', n(pvTVT,1), n(E['base']['pvTV']), pc(E['base']['pvTV']/vb)],
 ['= Valor del patrimonio', n(eq,1), n(vb), '100,0 %'], ['÷ Acciones diluidas (millones)', n(SH,1), '', '']])}
<p class="source">Fuente: libro oficial {REV}_VALORACION.xlsx y motor V2. Los depósitos y el fondeo forman parte de la intermediación: no se restan como deuda ni se suma la liquidez operativa.</p>
<figure><img alt="Valor por escenario frente al precio" src="{IMG}valor_vs_precio_r3.png"/><figcaption>Valor intrínseco por escenario, precio con MOS y descomposición del Base frente al cierre de US${n(P)}.</figcaption></figure>
<h3>Resumen de escenarios y conciliación libro ↔ motor</h3>
{tabla(['Escenario', 'Libro (LibreOffice)', 'Motor V2', 'Diferencia', 'vs. precio'], [[s.capitalize(), f'US${n(x["libro"]["valores"][s],4)}', f'US${n(E[s]["v"],4)}', pc(abs(E[s]['v']/x['libro']['valores'][s]-1),3), pc(E[s]['v']/P-1)] for s in A])}
<h3>Sensibilidades 5×5 (motor completo)</h3>
<figure><img alt="Sensibilidades" src="{IMG}sensibilidades_r3.png"/><figcaption>Izquierda: Ke × crecimiento estable. Derecha: ROE de alto crecimiento × ROE estable. El recuadro marca el Base.</figcaption></figure>
<p>El valor es más sensible a la rentabilidad que al descuento: pasar de un ROE estable de 18 % a 14 % reduce el Base a US${n(c["sensRoe"]["rows"][2][1])}, mientras que +50 pb de Ke lo reducen a US${n(c["sensKeG"]["rows"][3]["cells"][2])}.</p>
<h3>Contraste con el FCFF de R2</h3>
<p>{J["contrasteFCFF"]} Además, R2 usaba una beta de «Business & Consumer Services» (0,806); con ella el Base bancario sería US${n(c["sensBeta"]["b0806"])}. El método FCFF es un contraste útil para leer la economía operativa, no una alternativa para promediar.</p>
<h3>Inverso y múltiplos (diagnóstico)</h3>
{tabla(['Medida', 'Al precio (US$11,27)', 'Al valor Base'], [
 ['ROE de alto crecimiento implícito', pc(c['roeImplicito']), pc(A['base']['roeHighGrowth'])],
 ['ROE estable implícito (con ROE 26 % en años 1–5)', pc(c['roeEstableImplicito']), pc(A['base']['roeStable'])],
 ['P/VL (patrimonio común US$2,94 por acción)', n(c['mult']['pbvPrecio'])+'×', n(c['mult']['pbvBase'])+'×'],
 ['P/U (utilidad LTM US$0,80 por acción)', n(c['mult']['pePrecio'],1)+'×', n(c['mult']['peBase'],1)+'×']])}
<p class="source">Los múltiplos son diagnóstico, no un segundo valor para promediar. P/VL superior a 3× solo se sostiene con un ROE muy superior al Ke.</p>
<div class="reading"><strong>Nuestra lectura.</strong> Valorada como lo que es —un banco de alta rentabilidad—, Nu no está barata: el precio coincide con un ROE sostenido de ~25 %, que es exactamente lo que el Base supone tras normalizar impuestos. El potencial depende de que el ROE no baje de ese nivel; el margen de seguridad exigiría un precio cercano a US${n(mos)}.</div>'''
est = c['estres']
destr = open(W/'destruccion_inicio.html').read().replace('llevando el valor hacia USD 5–7/acción', f'llevando el valor hacia US$5–9 por acción') + f'''<h3>Pruebas de estrés ilustrativas (no oficiales · motor de exceso de retorno)</h3>
<figure><img alt="Pruebas de estrés" src="{IMG}estres_r3.png"/><figcaption>Impacto de cuatro pruebas de estrés ilustrativas (no oficiales) recalculadas con el motor V2 «exceso» frente al Base R3 y al cierre de US${n(P)}.</figcaption></figure>
{tabla(['Prueba', 'Valor por acción', 'vs. Base', 'vs. precio'], [['Base R3', f'US${n(vb)}', '—', pc(vb/P-1)]] + [[l, f'US${n(v)}', pc(v/vb-1), pc(v/P-1)] for l, v in est])}
<p class="source">Fuente: simulaciones ilustrativas no oficiales con el motor V2 «exceso» sobre la base R3 (acciones diluidas 4.881,1 M). En este modelo retener más capital crea valor mientras el ROE supere al Ke; por eso el estrés de capital se expresa como menor ROE sobre un patrimonio exigido mayor.</p>
<div class="reading"><strong>Nuestra lectura.</strong> Un deterioro de crédito o fiscal (S1) o un shock de riesgo país (S2) llevan el valor a US$8–9; el choque combinado (S4) lo reduce a US${n(est[3][1])}. Como el precio ya coincide con el Base, el balance riesgo/retorno es desfavorable mientras no baje la mora.</div>'''
blocks = copy.deepcopy(a2['blocks'])
for k in blocks:
    i = blocks[k].find('<div id="justificacion-supuestos'); blocks[k] = blocks[k] if i < 0 else blocks[k][:i]
blocks['supuestos'], blocks['valoracion'], blocks['destruccion'] = sup, val, destr
R = [  # (capítulo, texto antiguo exacto o regex, nuevo)
 ('perfil', r'Valorada como <strong>fintech operativa bajo Damodaran Simple Ginsu \(FCFF\)</strong>.*?</strong>\.', f'Valorada como <strong>banco con el modelo de exceso de retorno sobre patrimonio de Damodaran</strong> (Ke <strong>{pc(ke,2)}</strong> = 5,15 % + 0,76 × 7,62 %; ROE de alto crecimiento 26 %, retención 80 % para sostener el CET1 y ROE estable 18 %), el valor intrínseco Base es <strong>US${n(vb)}</strong> ({pc(up)} vs. US${n(P)}), con precio MOS 35 % en <strong>US${n(mos)}</strong> y rango <strong>US${n(vc)} – US${n(vo)}</strong>. El FCFF de R2 (US$16,65) se conserva como contraste.'),
 ('introduccion', r'La pregunta central de este informe es si a USD 11,27.*?\)\.', f'La pregunta central de este informe es si a US${n(P)} el mercado paga correctamente la rentabilidad de la mayor fintech de crédito de Latinoamérica: valorada como banco, el Base es <strong>US${n(vb)}</strong> ({pc(up)}), y el precio supera el margen de seguridad de 35 % (<strong>US${n(mos)}</strong>), porque descuenta un ROE sostenido de ~25 %.'),
 ('negocio', r'Por ello, al valorarla como fintech operativa bajo Damodaran Simple Ginsu.*?\)\.', 'Por ello la valoramos como banco: el crédito y la captación son el negocio, la reinversión es el capital común que exige el CET1 y el valor depende de la diferencia entre el ROE y el costo del patrimonio, no de un flujo de caja «de la empresa» que trate los depósitos como deuda.'),
 ('calidad', r'por ello, el DCF modela la reinversión vía Sales-to-Capital económico \(1,8×\) en lugar de proyectar CFO contable distorsionado por flotantes\.', 'por ello la valoración no proyecta el CFO contable: mide la reinversión como capital común retenido para sostener el CET1 (retención de 80 % en el Base).'),
 ('calidad', r'razón por la cual nuestro DCF exige un <em>Sales-to-Capital</em> conservador de 1,8× en el escenario Base\.', 'razón por la cual nuestra valoración bancaria exige retener 80 % de la utilidad en el escenario Base para que el patrimonio crezca al ritmo de los activos ponderados por riesgo.'),
 ('competencia', r'justifica un ROIC terminal del 18 % en nuestro escenario Base \(por encima del WACC terminal del 11,71 %\)', f'justifica un ROE estable del 18 % en nuestro escenario Base (por encima del costo del patrimonio de {pc(ke,2)})'),
 ('ciclos', r'Implicación en el DCF Simple Ginsu', 'Implicación en la valoración'),
 ('ciclos', r'WACC inicial 11,29 % → terminal 11,29 % reteniendo riesgo país', f'Costo del patrimonio {pc(ke,2)} constante, con ERP de Brasil/LatAm 7,62 %'),
 ('ciclos', r'exige capital adicional \(S2C 1,8×\) mientras retiene la prima país de Latinoamérica hasta perpetuidad', 'retiene 80 % de la utilidad como capital regulatorio y mantiene la prima país de Latinoamérica en el costo del patrimonio a perpetuidad'),
 ('riesgos', r'reduce proporcionalmente ingresos y FCFF en USD y sube el WACC', 'reduce proporcionalmente utilidad y patrimonio en USD y sube el costo del patrimonio'),
 ('riesgos', r'WACC conserva prima país LatAm en perpetuidad', 'el costo del patrimonio conserva la prima país LatAm en perpetuidad'),
 ('riesgos', r'S2C 1,8× en Base', 'retención de 80 % en el Base'),
 ('riesgos', r'están internalizados en nuestro WACC \(11,29 % → 11,29 %\) y tasa marginal \(34 %\)', f'están internalizados en nuestro costo del patrimonio ({pc(ke,2)}) y en un ROE de alto crecimiento (26 %) que ya descuenta la normalización fiscal hacia 34 %'),
 ('tesis_contraria', r'a USD 11,27 la acción ofrece un potencial atractivo de <strong>\+47,8 %</strong> hasta nuestro Base \(<strong>USD 16,65</strong>\), muy próximo al punto de compra disciplinado con MOS 35 % \(<strong>USD 10,82</strong>\)\.', f'a US${n(P)} la acción cotiza cerca de nuestro Base bancario (<strong>US${n(vb)}</strong>, {pc(up)}) y por encima del precio con MOS 35 % (<strong>US${n(mos)}</strong>): no hay margen de seguridad.'),
 ('tesis_contraria', r'Eficiencia de capital \(S2C\)', 'Capital regulatorio (retención)'),
 ('tesis_contraria', r'Aplicamos la regla Damodaran–MELI §6: exigimos <strong>S2C 1,8×</strong> en Base \(coherente con 1,70× histórico de Ventas/Capital\), no 4–5× de software\.', 'Valoramos a Nu como banco: exigimos retener <strong>80 %</strong> de la utilidad en el Base para que el patrimonio acompañe el crecimiento de los activos ponderados por riesgo.'),
 ('tesis_contraria', r'El mercado descuenta hoy una desaceleración extrema.*?\(USD 10,82\)\.', f'El mercado descuenta hoy un ROE sostenido de ~25 %, prácticamente el del Base (US${n(vb)}); el precio supera el umbral con MOS 35 % (US${n(mos)}).'),
 ('conclusiones', r'cuyo valor intrínseco Base bajo Damodaran Simple Ginsu es <strong>USD 16,65</strong> \(\+47,8 % sobre el cierre de USD 11,27\)\.', f'cuyo valor intrínseco Base, valorada como banco con el modelo de exceso de retorno de Damodaran, es <strong>US${n(vb)}</strong> ({pc(up)} sobre el cierre de US${n(P)}).'),
 ('conclusiones', r'el precio actual ya está cerca del umbral con margen de seguridad 35 % \(<strong>USD 10,82</strong>, a 4,1 % de distancia\)\. Una corrección adicional hacia <strong>USD 9,50–10,00</strong>', f'el precio actual está {pc(P/mos-1,0)} por encima del umbral con margen de seguridad 35 % (<strong>US${n(mos)}</strong>). Una corrección hacia <strong>US$7,50–8,00</strong>'),
 ('conclusiones', r'La caída de 41 % la acerca por primera vez en dos años a nuestra zona de compra con margen de seguridad \(USD 10,82\), por lo que merece seguimiento prioritario', f'Aun tras caer 41 %, el precio coincide con nuestro Base bancario y no alcanza la zona de compra con margen de seguridad (US${n(mos)}), por lo que merece seguimiento prioritario'),
 ('fuentes', r'<li><strong>Override de WACC terminal con fórmula \(avisos V13/V14\):</strong>.*?</li>', f'<li><strong>Libro R3 (banco):</strong> <code>{REV}_VALORACION.xlsx</code> construido sobre <code>eqexret</code> de Damodaran (descargado de NYU Stern el 22-nov-2026) con hojas «JMR Estados», «JMR Indicadores», «JMR Escenarios» y «JMR Fuentes»; recalculado con LibreOffice y conciliado con el motor V2 (0,000 %). Betas: <code>betaGlobal.xls</code> (5-ene-2026). Contraste: libro R2 FCFF.</li>'),
 ('fuentes', r'<strong>FCFF:</strong> flujo de caja libre para la firma\.', '<strong>Exceso de retorno:</strong> (ROE − Ke) × patrimonio; método principal de R3. <strong>FCFF:</strong> flujo de caja libre para la firma (contraste R2). <strong>Ke:</strong> costo del patrimonio.'),
 ('fuentes', r'<strong>S2C \(Sales-to-Capital\):</strong>.*?<strong>WACC:</strong> costo promedio ponderado de capital\.', '<strong>ROE:</strong> utilidad neta sobre patrimonio común. <strong>S2C:</strong> ventas/capital (supuesto del FCFF de R2). <strong>WACC:</strong> costo promedio ponderado de capital (solo en el contraste R2).')]
for k, old, new in R:
    nb, cnt = re.subn(old, lambda m: new, blocks[k], count=1, flags=re.S)
    assert cnt == 1, (k, old[:60]); blocks[k] = nb
a3 = {**a2, 'revision': REV, 'fecha': '2026-11-22', 'blocks': blocks, 'pdf': e['informe']['pdf']}
a3.pop('justificacionSupuestos', None)
a3['revisionMetodo'] = {'fecha': '2026-11-22', 'anterior': ANT, 'alcance': 'Método bancario (exceso de retorno) en lugar de FCFF; capítulos de supuestos, valoración y destrucción reescritos y cifras actualizadas en los demás.'}
json.dump(e, open(W/'origen/empresas/NU.json', 'w'), ensure_ascii=False, indent=1)
json.dump(a3, open(W/'origen/analisis/NU.json', 'w'), ensure_ascii=False, indent=1)
# ---------------- HTML R8 ----------------
s = BeautifulSoup(open(INF/f'{ANT}_INFORME_FUNDAMENTAL.html').read(), 'html.parser')
prof = s.find('section', id='perfil')
prof.find('p', class_='thesis').string = (f'Nu Holdings construyó la mayor fintech de Latinoamérica (142,6 M clientes, eficiencia 19,3 %, utilidad neta LTM US$3.919 M y ROE 32 % en el 3T26). '
    f'Valorada como banco (exceso de retorno, Ke {pc(ke,2)}), el Base es US${n(vb)} ({pc(up)} sobre US${n(P)}) y el precio con MOS 35 % es US${n(mos)}: el mercado ya descuenta un ROE sostenido de ~25 %.')
vals = {'Valor intrínseco base (R2)': ('Valor intrínseco base (R3)', f'US${n(vb)}'), 'Potencial sobre el cierre': (None, f'{"+" if up>=0 else ""}{pc(up)}'),
        'Precio con margen de seguridad (35 %)': (None, f'US${n(mos)}'), 'Sector · Perfil': (None, 'Fintech de crédito · Banco'), 'Revisión de valoración': (None, 'R3 · LTM 30-sep-2026')}
for d in prof.find('aside').find_all('div'):
    lab = d.find('span', class_='label')
    if lab and lab.get_text() in vals:
        nl, nv = vals[lab.get_text()]
        if nl: lab.string = nl
        d.find('strong').string = nv
leg = s.find('section', class_='legal'); ps = leg.find_all('p')
ps[2].clear(); ps[2].append(BeautifulSoup(f'Revisión <strong>{REV}</strong>, corte contable LTM al 30-sep-2026 y precio de cierre al 20-nov-2026 (US${n(P)}). Estado técnico: <strong>EN REVISIÓN</strong> (sin auditoría independiente ni aprobación personal). Sustituye a R2 (FCFF Simple Ginsu) tras la revisión del método del 22-nov-2026: Nu capta depósitos y asume riesgo de crédito, por lo que se valora como banco; R2 se conserva como contraste.', 'html.parser'))
ps[3].clear(); ps[3].append(BeautifulSoup(f'Conforme al contrato JMR V2.0 v1.5.6 y al proceso sectorial de bancos, el cálculo se ejecuta en el libro oficial <code>{REV}_VALORACION.xlsx</code>, construido sobre el modelo original <em>Equity Excess Return</em> de Damodaran (<code>eqexret</code>) con estados, escenarios y fuentes enlazados por fórmulas: patrimonio común US$14.342,6 M, utilidad neta LTM US$3.918,9 M, Ke {pc(ke,2)} (5,15 % + 0,76 × 7,62 %), CET1 12,1 % (mín. 7,0 %), tres escenarios (Conservador US${n(vc)} · Base US${n(vb)} · Optimista US${n(vo)}), MOS 35 % solo sobre el Base (US${n(mos)}) y paridad libro ↔ motor de 0,000 %. La maquetación reproduce NVIDIA R6 y MercadoLibre R8.', 'html.parser'))
for k in ['introduccion', 'negocio', 'calidad', 'direccion', 'competencia', 'ciclos', 'riesgos', 'destruccion', 'tesis_contraria', 'supuestos', 'valoracion', 'conclusiones', 'fuentes']:
    sec = s.find('section', id=k); kick = sec.find('div', class_='kicker'); h1 = sec.find('h1')
    for ch in list(sec.children):
        if ch not in (kick, h1): ch.extract()
    frag = BeautifulSoup(blocks[k].replace(IMG, '../../imagenes/NU/'), 'html.parser')
    for q in frag.find_all('blockquote'): q.name = 'div'; q['class'] = 'reading'
    sec.append(frag)
s.title.string = f'Nu Holdings · {REV} · Informe fundamental' if s.title else None
out = INF/f'{REV}_INFORME_FUNDAMENTAL.html'; out.write_text(str(s), encoding='utf-8')
print('OK', n(vb), n(mos), out)
