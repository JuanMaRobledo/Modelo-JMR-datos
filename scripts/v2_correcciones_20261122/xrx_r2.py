"""XRX R2: déficit de pensiones como deuda y probabilidad de fracaso por calificación (Damodaran). Expediente, análisis, figuras y HTML R8."""
import json, sys, re, copy, pathlib
from bs4 import BeautifulSoup
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, numpy as np
X = pathlib.Path(sys.argv[1]); ORIG = pathlib.Path(sys.argv[2]); OUT = pathlib.Path(sys.argv[3])
DATA = pathlib.Path('/home/user/Modelo-JMR-datos/jmr-v2'); INF = DATA/'informes/XRX'; IMGD = DATA/'imagenes/XRX'
REV, ANT = 'XRX-V2-LTM20260930-R2', 'XRX-V2-LTM20260930-R1'
SHEET = '1obFz8FAtO0Yrew82swVnjxlXtxYwN9YYww1GcDKCE70'; SHA = '568f80f6add69d1a0f98027705fb09428ad2219a2afd50883558e8c8e673741a'
r1 = json.load(open(ORIG/'empresas/XRX.json')); a1 = json.load(open(ORIG/'analisis/XRX.json')); c = json.load(open(X/'calc.json'))
def n(v, d=2): return f'{v:,.{d}f}'.replace(',', '@').replace('.', ',').replace('@', '.')
def pc(v, d=1): return n(100*v, d) + ' %'
def us(v, d=2): return ('−' if v < 0 else '') + f'US$ {n(abs(v), d)}'
L = {'conservador': dict(pv10=2020.05, pvtv=1017.02, sum=3037.07, p=0.5038, proc=759.27, op=1889.51, eq=-1445.29, v=-10.89188252420846),
     'base': dict(pv10=2112.93, pvtv=1162.09, sum=3275.02, p=0.5038, proc=1637.51, op=2450.04, eq=-884.76, v=-6.667651903896354),
     'optimista': dict(pv10=2647.07, pvtv=1752.94, sum=4400.01, p=0.2374, proc=2200.00, op=3877.73, eq=542.93, v=4.091569689269134)}
P = 0.85; vb = L['base']['v']; PEN, PENT = 655, 497.8
# ---------- expediente ----------
e = copy.deepcopy(r1); f = e['financials']
f['debt'] = round(4228 + PENT, 1); f['ajustesDeuda'] = PENT
for p in e['provenance']:
    if p['destino'] == 'financials.debt':
        p['ajuste'] = round(8 + PENT, 1); p['pagina'] += f'; + US$ {n(PENT,1)} M de déficit neto de pensiones y salud de jubilados después de impuestos (financials.ajustesDeuda)'
e['provenance'].append({'destino': 'financials.ajustesDeuda', 'documento': 'Form 10-K FY2025, Nota 18 (beneficios posteriores al empleo)', 'periodo': '31-dic-2025', 'pagina': 'Nota 18: déficit neto consolidado de pensiones y salud de jubilados US$655 M antes de impuestos; × (1 − 24 %)',
    'moneda': 'USD', 'unidades': 'USD millones', 'valorReportado': PENT, 'ajuste': 0, 'celdaDestino': "'JMR Escenarios'!C35 → 'Input sheet'!B15"})
for s, (pr, rr) in {'conservador': (0.5038, 0.25), 'base': (0.5038, 0.5), 'optimista': (0.2374, 0.5)}.items():
    e['assumptions'][s]['failureProbability'] = pr; e['assumptions'][s]['recoveryRate'] = rr
lib = e['libro']; lib.update({'id': f'{REV}_VALORACION.xlsx', 'sha256': SHA, 'valores': {k: v['v'] for k, v in L.items()}, 'googleSheetId': SHEET,
    'editableUrl': f'https://docs.google.com/spreadsheets/d/{SHEET}/edit', 'url': f'https://docs.google.com/spreadsheets/d/{SHEET}/edit',
    'driveFileId': None, 'excelPendiente': 'Exportación .xlsx (sha256 arriba) no subida a Drive: supera el límite del conector (3,6 MB).',
    'cambiosR2': 'Copia de R1: «JMR Escenarios» filas 33–38 (pensión 655 × (1 − 24 %) = 497,8; probabilidad de fracaso desde «Failure Rate worksheet»: CCC/C 50,38 %, B 23,74 %; recuperación 25 %/50 %/50 %) e «Input sheet» B15 y B51:B54 enlazados por fórmula.',
    'paridad': 'Motor V2 frente a libro: −0,06 % (Conservador), −0,12 % (Base), +0,34 % (Optimista); dentro de ±0,5 %. Diferencia por el tratamiento de la recuperación en caso de fracaso.'})
e['revision'] = {'id': REV, 'anterior': ANT, 'nota': 'R2 (22-nov-2026): déficit de pensiones después de impuestos (US$497,8 M) restado como deuda y probabilidad de fracaso por calificación crediticia (Damodaran «Failure Rate worksheet»): CCC/C 50,38 % en Conservador y Base, B 23,74 % en Optimista. El patrimonio común del Base es negativo.'}
e['documentLinks'] = {**r1['documentLinks'], 'workbook': f'https://docs.google.com/spreadsheets/d/{SHEET}/edit', 'workbookR1': r1['documentLinks']['workbook']}
e['informe'] = {**r1['informe'], 'pdf': f'jmr-v2/informes/XRX/{REV}_INFORME_FUNDAMENTAL.pdf', 'html': f'{REV}_INFORME_FUNDAMENTAL.html'}
e['estado'] = 'EN_PROCESO'
e['cierreEditorial'] = {'completo': False, 'pendientes': ['Manifiesto de cierre R2 con huellas.', 'Auditoría independiente (P02).']}
J = e['justificaciones']
J['puente'] = f'Déficit neto de pensiones y salud de jubilados de US$655 M antes de impuestos (10-K FY2025, Nota 18) restado como obligación asimilable a deuda después de impuestos (US$497,8 M), como recomienda Damodaran. Deuda del puente: 4.228 + 497,8 = US$4.725,8 M.'
J['fracaso'] = ('Probabilidad de fracaso por calificación (Damodaran, «Failure Rate worksheet», impago acumulado a 10 años): CCC/C 50,38 % en Conservador y Base (calificación vigente S&P CCC+ negativa / Moody\'s Caa2) y B 23,74 % en Optimista (supone superar el muro de 2028–2029). '
    'Recuperación: 50 % del valor razonable (supuesto por defecto de Damodaran) y 25 % en el Conservador por subordinación a deuda garantizada. El costo de la deuda en el WACC no captura el riesgo de que el patrimonio se extinga.')
J['patrimonioNegativo'] = (f'El patrimonio común del Base es negativo ({us(L["base"]["eq"],1)} M; {us(vb)} por acción). Con responsabilidad limitada el valor DCF del accionista es nulo: la cotización de US$0,85 refleja el valor de opción de que la empresa supere el muro de vencimientos. '
    f'Aun sin fracaso, restar las pensiones deja {us(c["sinFracaso"])} por acción; el margen objetivo necesario para un patrimonio nulo es ~{pc(c["mtCero"])} (Base 5,8 %).')
e['warnings'] = [w for w in r1['warnings'] if not w.startswith('Corrección pendiente') and 'pensiones' not in w] + [
    f'R2: pensiones restadas como deuda y probabilidad de fracaso CCC/C 50,38 %: Base {us(vb)} por acción (patrimonio negativo; valor económico del accionista nulo). R1 daba US$3,31.',
    'La copia .xlsx del libro R2 no se subió a Drive (límite del conector); el libro oficial R2 es la Google Sheet enlazada.']
e['analysis'] = {**r1.get('analysis', {}), 'conclusion': J['patrimonioNegativo']}
# ---------- figuras ----------
NAVY, BLUE, LIGHT, TAN, RED, GRID = '#1d3449', '#5b8baa', '#a8c3d3', '#c4a282', '#c0394b', '#e3e8ec'
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 11, 'axes.edgecolor': '#b9c6cf', 'axes.titleweight': 'bold', 'axes.titlecolor': NAVY, 'axes.titlesize': 13})
def lim(ax): ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False); ax.grid(color=GRID, lw=.8); ax.set_axisbelow(True)
fig, (a, b) = plt.subplots(1, 2, figsize=(11.5, 4.6), gridspec_kw={'width_ratios': [1.2, 1]})
lab = ['Conservador', 'Base', 'Optimista']; val = [L[k]['v'] for k in ['conservador', 'base', 'optimista']]
a.barh(lab, val, color=[LIGHT, NAVY, BLUE], height=.55); a.axvline(P, color=RED, ls='--', lw=2, label='Cierre 20-nov-2026: US$ 0,85'); a.axvline(0, color='#555', lw=1)
for i, v in enumerate(val): a.text(v + (0.3 if v >= 0 else -0.3), i, us(v), va='center', ha='left' if v >= 0 else 'right', fontweight='bold', color=NAVY)
a.set_xlim(-19, 7); a.set_title('Valor del patrimonio por acción (R2)'); a.set_xlabel('US$ por acción (negativo = sin valor para el accionista)'); a.legend(frameon=False, loc='lower right', fontsize=9); lim(a); a.grid(axis='y', visible=False)
B = L['base']; steps = [('VP flujos\naños 1–10', B['pv10']), ('VP terminal', B['pvtv']), ('Ajuste por\nfracaso', B['op'] - B['sum']), ('Deuda +\npensiones', -4725.8), ('Preferentes\ny NCI', -230), ('Caja + XFS', 1621)]
cum = 0
for i, (lab_, v) in enumerate(steps):
    b.bar(i, v, bottom=cum if v >= 0 else cum + v, color=BLUE if v >= 0 else RED, width=.6); cum += v
    b.text(i, max(cum, cum - v) + 120, n(v, 0), ha='center', fontsize=8.5, color=NAVY)
b.bar(len(steps), cum, color=NAVY, width=.6); b.text(len(steps), 120, n(cum, 0), ha='center', fontsize=9, fontweight='bold', color=NAVY)
b.set_xticks(range(len(steps) + 1)); b.set_xticklabels([s[0] for s in steps] + ['Patrimonio\ncomún'], fontsize=8); b.axhline(0, color='#555', lw=1)
b.set_title('Puente del Base (US$ millones)'); lim(b); b.grid(axis='x', visible=False)
fig.text(0.5, 0.01, f'Fuente: libro oficial {REV} (Google Sheets) y cierre 20-nov-2026. Pensiones: 10-K FY2025 Nota 18. Fracaso: Damodaran «Failure Rate worksheet». Elaboración JMR.', ha='center', color='#7d8b96', fontsize=8.5)
fig.tight_layout(rect=(0, .05, 1, 1)); fig.savefig(IMGD/'valor_vs_precio_r2.png', dpi=150); plt.close(fig)
fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.4))
def heat(ax, M, rl, cl, tit, xl, yl, ci, cj):
    M = np.array(M); ax.imshow(M >= P, cmap=matplotlib.colors.ListedColormap(['#f4e3e3', '#e3efe6']), aspect='auto', vmin=0, vmax=1)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]): ax.text(j, i, n(M[i, j]), ha='center', va='center', fontsize=9.5, color=NAVY, fontweight='bold' if (i, j) == (ci, cj) else 'normal')
    ax.add_patch(plt.Rectangle((cj - .5, ci - .5), 1, 1, fill=False, ec=NAVY, lw=2)); ax.set_xticks(range(len(cl))); ax.set_xticklabels(cl); ax.set_yticks(range(len(rl))); ax.set_yticklabels(rl)
    ax.set_title(tit, fontsize=11.5); ax.set_xlabel(xl); ax.set_ylabel(yl)
heat(axs[0], c['mWT']['rows'], [pc(x, 2) for x in c['mWT']['wt']], [pc(x) for x in c['mWT']['g']], 'WACC terminal × crecimiento perpetuo', 'g', 'WACC terminal', 2, 2)
heat(axs[1], c['mMP']['rows'], [pc(x) for x in c['mMP']['mt']], [pc(x, 2) for x in c['mMP']['p']], 'Margen objetivo × probabilidad de fracaso', 'Probabilidad de fracaso', 'Margen objetivo', 2, 4)
fig.text(0.5, 0.01, 'Fuente: motor V2 sobre el expediente R2 (paridad con el libro ±0,34 %). Verde: valor ≥ precio US$ 0,85; rosado: inferior. Recuadro = Base.', ha='center', color='#7d8b96', fontsize=8.5)
fig.tight_layout(rect=(0, .05, 1, 1)); fig.savefig(IMGD/'sensibilidades_r2.png', dpi=150); plt.close(fig)
# ---------- análisis ----------
IMG = 'https://raw.githubusercontent.com/JuanMaRobledo/Modelo-JMR-datos/main/jmr-v2/imagenes/XRX/'
def tabla(cab, filas): return '<table><thead><tr>' + ''.join(f'<th>{h}</th>' for h in cab) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{v}</td>' for v in r) + '</tr>' for r in filas) + '</tbody></table>'
S3 = ['conservador', 'base', 'optimista']
puente = tabla(['Componente (US$ millones)', 'Conservador', 'Base', 'Optimista'], [
 ['VP flujos FCFF (años 1–10)'] + [n(L[s]['pv10'], 1) for s in S3], ['VP valor terminal (g 1,0 %; WACC terminal 8,54 %)'] + [n(L[s]['pvtv'], 1) for s in S3],
 ['Valor operativo antes de fracaso'] + [n(L[s]['sum'], 1) for s in S3], ['Probabilidad de fracaso (impago acumulado a 10 años)'] + [pc(L[s]['p'], 2) for s in S3],
 ['Recuperación en caso de fracaso (% del valor)'] + ['25 %', '50 %', '50 %'], ['Valor de los activos operativos tras fracaso'] + [n(L[s]['op'], 1) for s in S3],
 ['(−) Deuda financiera (incl. US$8 M arrendamientos financieros)'] + ['−4.228,0']*3, ['(−) Déficit de pensiones después de impuestos (10-K Nota 18)'] + ['−497,8']*3,
 ['(−) Preferentes Serie A y participaciones minoritarias'] + ['−230,0']*3, ['(+) Caja libre'] + ['+412,0']*3, ['(+) Cartera financiera XFS neta'] + ['+1.209,0']*3,
 ['<strong>Valor del patrimonio común</strong>'] + [f'<strong>{n(L[s]["eq"], 1)}</strong>' for s in S3], ['Acciones (millones)'] + ['132,694']*3,
 ['<strong>Valor por acción (US$)</strong>'] + [f'<strong>{us(L[s]["v"])}</strong>' for s in S3], ['Valor económico para el accionista (responsabilidad limitada)'] + ['US$ 0,00', 'US$ 0,00', us(L['optimista']['v'])]])
val = f'''<div class="essential"><div class="label">Lo esencial</div><ul><li>Con el déficit de pensiones restado como deuda y una probabilidad de fracaso coherente con la calificación CCC (50,38 %, Damodaran), el patrimonio común del Base es <strong>negativo</strong>: {us(vb)} por acción (Conservador {us(L["conservador"]["v"])}; Optimista {us(L["optimista"]["v"])}).</li>
<li>Con responsabilidad limitada, el valor DCF del accionista es <strong>nulo</strong> en Base y Conservador. La cotización de US$ 0,85 es valor de opción: paga la posibilidad de que Xerox supere el muro de vencimientos 2028–2031. No aplica precio con margen de seguridad.</li>
<li>R1 (US$ 3,31) omitía las pensiones y suponía 0 % de fracaso en el Base; aun sin fracaso, restar las pensiones deja {us(c["sinFracaso"])} por acción.</li></ul></div>
<h2>11.1 Resumen de resultados y puente de valor</h2>
<p>La valoración se ejecutó por fórmulas en el libro oficial <code>{REV}_VALORACION</code> (Google Sheets, copia de R1 con los ajustes R2 enlazados al «Input sheet») y se contrastó con el motor JavaScript del visor V2 (diferencias de −0,06 % a +0,34 %, dentro de ±0,5 %).</p>
<figure><img src="{IMG}valor_vs_precio_r2.png" alt="Valor por escenario y puente del Base"/><figcaption>Valor del patrimonio por acción en los tres escenarios frente al cierre de US$ 0,85 y puente del Base (US$ millones).</figcaption></figure>
{puente}
<p class="source">Fuente: libro oficial {REV} («Valuation output» por escenario). El ajuste por fracaso sigue a Damodaran: valor = valor operativo × (1 − p) + p × recuperación × valor operativo.</p>
<h2>11.2 Sensibilidades 5×5</h2>
<figure><img src="{IMG}sensibilidades_r2.png" alt="Sensibilidades R2"/><figcaption>Izquierda: WACC terminal × crecimiento perpetuo. Derecha: margen operativo objetivo × probabilidad de fracaso. El recuadro marca el Base.</figcaption></figure>
<p>Las tasas terminales no rescatan al accionista: incluso con WACC terminal de 6,54 % y g de 2 % el valor sigue siendo negativo. Solo una combinación de margen objetivo cercano a 7,8 % y baja probabilidad de fracaso deja valor positivo. Cada +100 pb de margen objetivo añaden {us(c["m100"])} por acción.</p>
<h2>11.3 Inverso y diagnóstico</h2>
{tabla(['Medida', 'Resultado', 'Lectura'], [
 ['Valor sin riesgo de fracaso (solo pensiones)', us(c['sinFracaso']), 'Las pensiones bastan para eliminar el patrimonio común.'],
 ['Valor sin pensiones, con fracaso CCC', us(c['sinPension']), 'El riesgo de impago también lo elimina por sí solo.'],
 ['Margen objetivo para un patrimonio nulo (fracaso 50,38 %)', pc(c['mtCero']), 'Frente a 5,8 % del Base y márgenes reportados negativos en LTM.'],
 ['Margen objetivo que justifica US$ 0,85', pc(c['mtPrecio']), 'El mercado no descuenta un DCF: paga una opción sobre la refinanciación.']])}
<aside class="reading"><strong>Nuestra lectura.</strong> El activo operativo de Xerox tiene valor (US$ 3.275 M antes de fracaso), pero los acreedores, las pensiones y los preferentes tienen prioridad sobre él. En el Base no queda nada para el accionista común; comprar a US$ 0,85 es comprar una opción de reestructuración exitosa, no un valor intrínseco con margen de seguridad.</aside>'''
blocks = copy.deepcopy(a1['blocks'])
for k in blocks:
    i = blocks[k].find('<div id="justificacion-supuestos'); blocks[k] = blocks[k] if i < 0 else blocks[k][:i]
blocks['valoracion'] = val
d = blocks['destruccion']; j = d.find('<h2>8.2 Pruebas de estrés')
est = [('Base R2 (referencia)', vb)] + [tuple(x) for x in c['estres']]
blocks['destruccion'] = d[:j] + f'''<h2>8.2 Pruebas de estrés cuantitativas (ilustrativas, no oficiales · motor JMR V2)</h2>
<p><em>Nota metodológica: las pruebas usan el mismo motor FCFF sobre la base R2 (pensiones restadas y fracaso CCC); no sustituyen los tres escenarios oficiales del libro.</em></p>
{tabla(['Prueba sobre el Base R2', 'US$ por acción', 'Valor económico'], [[l, us(v), 'US$ 0,00' if v < 0 else us(v)] for l, v in est])}
<p class="source">Fuente: cálculos ilustrativos no oficiales con el motor V2. El capital común tiene responsabilidad limitada (piso económico US$ 0,00).</p>
<aside class="reading"><strong>Nuestra lectura.</strong> Todas las pruebas profundizan un patrimonio que ya es negativo en el Base: el riesgo de Xerox no es perder parte del valor, sino que el accionista común quede subordinado por completo en una reestructuración.</aside>'''
R = [('perfil', r'<li><strong>Valor intrínseco Base:</strong>.*?</li>', f'<li><strong>Valor intrínseco Base (R2):</strong> patrimonio común negativo ({us(vb)} por acción) al restar las pensiones (US$ 497,8 M) y aplicar la probabilidad de impago CCC (50,38 %); valor económico del accionista: US$ 0,00. Sin precio con MOS.</li>'),
 ('perfil', r'<li><strong>Rango de escenarios:</strong>.*?</li>', f'<li><strong>Rango de escenarios:</strong> Conservador {us(L["conservador"]["v"])} · Base {us(vb)} · Optimista {us(L["optimista"]["v"])} (fracaso con calificación B, 23,74 %).</li>'),
 ('perfil', r'el valor Base \(\$3,31\) ofrece \+289,7 % teórico, pero 74 pb menos de margen o deducir las pensiones anulan el patrimonio común\.', 'con las pensiones restadas como deuda y el riesgo de impago de un emisor CCC, el DCF no deja valor al accionista en el Base: los US$ 0,85 pagan una opción sobre la refinanciación.'),
 ('riesgos', r'Alto \(±100 pb margen = ±\$3,31/acc\.\)', f'Alto (±100 pb de margen objetivo = ±{us(c["m100"])} por acción)'),
 ('supuestos', r'el impacto sobre el valor Base es exactamente <strong>\$0,00</strong> \(\$3,3121 vs\. \$3,3121\)', 'el impacto sobre el valor Base fue exactamente <strong>$0,00</strong> en la prueba de R1 ($3,3121 vs. $3,3121), y no cambia en R2'),
 ('conclusiones', r'<li> ?Veredicto técnico \(en revisión\):.*?</li>', f'<li>Veredicto técnico (en revisión): con pensiones como deuda y fracaso CCC, el patrimonio común del Base es negativo ({us(vb)} por acción; valor económico US$ 0,00) frente a un precio de US$ 0,85; solo el Optimista ({us(L["optimista"]["v"])}) deja valor.</li>'),
 ('conclusiones', r'que sustentan un valor operativo Base de \$3\.276 millones \(lo que deja \$439,5 millones o <strong>\$3,31 por acción</strong> para el accionista común tras acreditar los \$1\.209 millones de cartera XFS\)', 'que sustentan un valor operativo Base de $3.275 millones antes de fracaso ($2.450 millones tras aplicar el riesgo de impago CCC), insuficiente para cubrir deuda, pensiones y preferentes: el patrimonio común del Base es <strong>negativo ($−885 millones)</strong>'),
 ('conclusiones', r'aunque matemáticamente el cierre de \$0,85 cotiza 60,5 % por debajo del precio con margen de seguridad del 35 % \(\$2,15\), el perfil', 'el cierre de $0,85 no tiene respaldo en el valor intrínseco del Base (no existe precio con margen de seguridad) y el perfil'),
 ('fuentes', r'\(US\$ 3,31 × 0,65 = US\$ 2,15\)', '(no aplicable en R2: el Base no tiene valor positivo para el accionista)'),
 ('fuentes', r'<strong>FCFF:</strong>', '<strong>Probabilidad de fracaso:</strong> impago acumulado a 10 años por calificación (Damodaran «Failure Rate worksheet»; CCC/C 50,38 %, B 23,74 %). <strong>Déficit de pensiones:</strong> obligación asimilable a deuda, restada después de impuestos. <strong>FCFF:</strong>')]
for k, old, new in R:
    nb, cnt = re.subn(old, lambda m: new, blocks[k], count=1, flags=re.S); assert cnt == 1, (k, old[:50]); blocks[k] = nb
a2 = {**a1, 'revision': REV, 'blocks': blocks}; a2.pop('justificacionSupuestos', None)
for k in ('pdf', 'informePdf'):
    if k in a2: a2[k] = e['informe']['pdf']
a2['revisionMetodo'] = {'fecha': '2026-11-22', 'anterior': ANT, 'alcance': 'Pensiones como deuda y probabilidad de fracaso por calificación; valoración, destrucción, perfil, conclusiones y fuentes actualizados.'}
json.dump(e, open(OUT/'empresas/XRX.json', 'w'), ensure_ascii=False, indent=1); json.dump(a2, open(OUT/'analisis/XRX.json', 'w'), ensure_ascii=False, indent=1)
# ---------- HTML R8 desde el esqueleto de NU R3 ----------
s = BeautifulSoup(open(DATA/'informes/NU/NU-V2-LTM20260930-R3_INFORME_FUNDAMENTAL.html').read(), 'html.parser')
st = s.find('style'); st.string = st.string.replace('Modelo JMR V2 · Nu Holdings · En revisión', 'Modelo JMR V2 · XRX · EN PROCESO')
cov = s.find('section', class_='cover'); cov.find('h1').string = 'Xerox Holdings Corporation'
for sp in cov.find('div', class_='bottom').find_all('span')[:1]: sp.string = 'INFORME FUNDAMENTAL · EN PROCESO'
cov.find('p').string = 'Xerox adquirió Lexmark para duplicar escala en un negocio en declive secular, pero carga $4.228 millones de deuda con calificación CCC+ y cotiza a $0,85. ¿Sobrevive el capital común al muro de vencimientos 2028–2031?'
pr = s.find('section', id='perfil'); pr.find('h1').string = 'Xerox Holdings Corporation'
pr.find('p', class_='thesis').string = f'La acción común de Xerox cotiza como una opción apalancada sobre las sinergias de Lexmark y el refinanciamiento de $3.538 millones de deuda entre 2028 y 2031. Con las pensiones restadas como deuda y el riesgo de impago de un emisor CCC, el DCF R2 deja un patrimonio común negativo en el Base ({us(vb)} por acción): los $0,85 pagan una opción, no un valor intrínseco.'
lp = pr.find('div', class_='left').find_all('p')
lp[1].string = 'Xerox Holdings Corporation (NASDAQ: XRX; Norwalk, Connecticut) fabrica e integra equipos de impresión de oficina y producción, servicios gestionados de impresión (MPS) y soluciones de TI. Tras adquirir Lexmark (1-jul-2025) e ITsavvy (nov-2024), sus ingresos LTM al 30-sep-2026 fueron $7.664 millones (90,7 % Print & Other; 9,3 % IT Solutions).'
lp[2].string = 'El salto inorgánico encubre una contracción orgánica proforma de −5,0 % en 9M 2026. Con $4.228 millones de deuda, calificación CCC+/Caa2, un déficit de pensiones de $655 millones antes de impuestos y $3.538 millones de vencimientos entre 2028 y 2031, el capital común depende de convertir la cartera XFS ($1.209 millones) y las sinergias de Lexmark en desapalancamiento.'
vals = [('Valor intrínseco base (R2)', us(vb)), ('Valor económico para el accionista', 'US$ 0,00'), ('Precio con margen de seguridad (35 %)', 'No aplica'), ('Sector · Perfil', 'Equipos de oficina y TI · Operativa'), ('Mercado · Moneda', 'NASDAQ · USD'), ('Revisión de valoración', 'R2 · LTM 30-sep-2026')]
for dv, (lab_, v) in zip(pr.find('aside').find_all('div', recursive=False), vals): dv.find('span').string = lab_; dv.find('strong').string = v
mets = [('Precio (20-nov-2026)', 'US$ 0,85'), ('Rango 52 semanas', 'US$ 0,85 – 3,62'), ('Variación 5 años', '−95,7 %'), ('Capitalización', 'US$ 113 M')]
for dv, (lab_, v) in zip(pr.find('div', class_='metrics').find_all('div', recursive=False), mets): dv.find('div').string = lab_; dv.find('strong').string = v
fig_ = pr.find('figure'); fig_.find('div', class_='kicker').string = 'Cotización semanal, últimos 5 años (USD)'
fig_.find('img')['src'] = '../../imagenes/XRX/cotizacion_5a.png'; fig_.find('figcaption').string = 'Fuente: Yahoo Finance / NASDAQ. Cierres semanales del 22-nov-2021 al 20-nov-2026 (USD, sin ajustar por dividendos).'
leg = s.find('section', class_='legal'); ps = leg.find_all('p')
ps[0].string = 'Este informe se elaboró con fines informativos, educativos y de análisis financiero bajo el Modelo JMR V2.0. No constituye asesoría financiera personalizada, recomendación de compra o venta ni oferta de ningún instrumento. Las proyecciones reflejan supuestos explícitos sujetos a incertidumbre sustancial, especialmente en emisores con calificación especulativa (CCC+/Caa2).'
ps[1].string = 'Las cifras históricas proceden de documentos presentados ante la SEC por Xerox Holdings Corporation (CIK 0001770450): Forms 10-K FY2017–FY2025 y Form 10-Q 3T26 (5-nov-2026). Precio de referencia: US$ 0,85 al cierre del 20-nov-2026.'
ps[2].clear(); ps[2].append(BeautifulSoup(f'Revisión <strong>{REV}</strong> (sustituye a R1 del 21-nov-2026). Estado: <strong>EN PROCESO</strong> (control V03: el patrimonio común del Base es negativo, por lo que no existe precio objetivo válido); sin auditoría independiente ni aprobación del propietario. Corte contable LTM al 30-sep-2026.', 'html.parser'))
ps[3].clear(); ps[3].append(BeautifulSoup(f'Perfil operativa y motor FCFF (fcffsimpleginzu de Damodaran) por fórmulas en el libro <code>{REV}_VALORACION</code> (Google Sheets). R2 resta el déficit de pensiones después de impuestos (US$ 497,8 M; 10-K Nota 18) y aplica la probabilidad de fracaso por calificación de la hoja «Failure Rate worksheet» (CCC/C 50,38 %; B 23,74 %). Paridad con el motor V2 dentro de ±0,5 %. La maquetación reproduce NVIDIA R6 y MercadoLibre R8.', 'html.parser'))
toc = s.find('ol', class_='toc')
for li in toc.find_all('li'):
    a_ = li.find('a')
    if a_ and a_['href'] == '#destruccion': a_.string = '¿Qué podría destruir a Xerox Holdings Corporation?'
TT = {'destruccion': '¿Qué podría destruir a Xerox Holdings Corporation?'}
for k in ['introduccion', 'negocio', 'calidad', 'direccion', 'competencia', 'ciclos', 'riesgos', 'destruccion', 'tesis_contraria', 'supuestos', 'valoracion', 'conclusiones', 'fuentes']:
    sec = s.find('section', id=k); kick = sec.find('div', class_='kicker'); h1 = sec.find('h1')
    if k in TT: h1.string = TT[k]
    for ch in list(sec.children):
        if ch not in (kick, h1): ch.extract()
    fr = BeautifulSoup(blocks[k].replace(IMG, '../../imagenes/XRX/'), 'html.parser')
    for q in fr.find_all('blockquote'): q.name = 'div'; q['class'] = 'reading'
    sec.append(fr)
if s.title: s.title.string = f'Xerox Holdings Corporation · {REV} · Informe fundamental'
(INF/f'{REV}_INFORME_FUNDAMENTAL.html').write_text(str(s), encoding='utf-8'); print('OK', us(vb))
