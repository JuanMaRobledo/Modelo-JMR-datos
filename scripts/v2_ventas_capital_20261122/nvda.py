from comun import *
T, REV, SHEET = 'NVDA', 'NVDA-V2-FY26Q2FY27-R7', '18oyHpi4AMa6HEGvybWEr8a6GaW4LeKElj19qDSyPNjI'
c = json.load(open(W/'calc.json'))[T]; p = json.load(open(W/'nvda_c2.json'))['new']
e, a = load(T); B = a['blocks']; cortar_just(B); r = Rep(B)
vc, vb, vo = c['esc']['conservador'], c['esc']['base'], c['esc']['optimista']; mos = vb*0.65; PX = 155.46; D = c['det']; tv = p['tv']
# 1) etiquetas de revisión
r('una nueva revisión (R7)', 'una nueva revisión (R8)'); r('Una revisión R7 debe', 'Una revisión R8 debe'); r(r'\bR6\b', 'R7', regex=True)
# 2) cifras exactas
for o, nn in [('105,19', n(vc)), ('212,33', n(vb)), ('350,35', n(vo)), ('138,01', n(mos)), ('189,78', n(p['probes']['wacc+1'])), ('147,94', n(p['probes']['gCons'])), ('173,40', n(p['probes']['mCons']))]: r(o, nn)
r('US$105–US$350', 'US$%s–US$%s' % (n(vc, 0), n(vo, 0)))
for o, nn in [('105', vc), ('212', vb), ('350', vo), ('138', mos)]: r(r'US\$%s(?!\d|[.,]\d| mil| M\b)' % o, 'US$' + n(nn, 0), regex=True)
r('+36,6 %', pc(vb/PX-1)); r('-32,3 %', pc(vc/PX-1)); r('+125,4 %', pc(vo/PX-1))
r('37 % sobre el cierre', n(100*(vb/PX-1), 0) + ' % sobre el cierre', cnt=2); r('+37 %', '+' + n(100*(vb/PX-1), 0) + ' %')
r('−32 %', '−' + n(100*(1-vc/PX), 0) + ' %'); r('-32 % vs. precio', '-' + n(100*(1-vc/PX), 0) + ' % vs. precio'); r('+125 %', '+' + n(100*(vo/PX-1), 0) + ' %')
r('~14 %', '~' + n(100*p['imp']['growth2to5'], 0) + ' %', cnt=5)
r('el precio actual está 12,6 % por encima', 'el precio actual está %s %% por encima' % n(100*(PX/mos-1), 1))
r('Como 60 % del valor Base es terminal', 'Como %s %% del valor Base es terminal' % n(100*tv['base'], 0))
r('(−10,6 %)', '(−%s %%)' % n(100*(1-p['probes']['wacc+1']/vb), 1))
r('60,2 %', pc(tv['base'], 1, False)); r('50,8 %', pc(tv['conservador'], 1, False)); r('64,7 %', pc(tv['optimista'], 1, False))
for o, k in [('2.008.027', ('base', 'sumPV')), ('5.042.719', ('base', 'ev')), ('5.147.250', ('base', 'equity')), ('2.445.387', ('conservador', 'ev')), ('8.388.630', ('optimista', 'ev'))]: r(o, n(D[k[0]][k[1]], 0))
NI, SH = 226257, 24242
for o, s in [('11,3×', 'conservador'), ('22,7×', 'base'), ('37,5×', 'optimista')]: r(o, n(c['esc'][s]*SH/NI, 1) + '×', keys=['valoracion'])
g = p['grids']
r('lo lleva a US$142 con el margen Base (US$118–166 según el margen)', 'lo lleva a US$%s con el margen Base (US$%s–%s según el margen)' % (n(g['f11']['m'][0][2], 0), n(g['f11']['m'][0][0], 0), n(g['f11']['m'][0][4], 0)))
r('(US$187–223 con g de 3 %)', '(US$%s–%s con g de 3 %%)' % (n(g['f12']['m'][0][2], 0), n(g['f12']['m'][4][2], 0)))
r('<strong>14,2 %</strong> (Base: 22 %)', '<strong>%s %%</strong> (Base: 22 %%)' % n(100*p['imp']['growth2to5'], 1)); r('<strong>29,4 %</strong> (Base: 44 %)', '<strong>%s %%</strong> (Base: 44 %%)' % n(100*p['imp']['marginTarget'], 1)); r('<strong>12,0 %</strong> (Base: 8,54 %)', '<strong>%s %%</strong> (Base: 8,54 %%)' % n(100*p['imp']['waccTerminal'], 1))
# 3) ventas/capital
r('<td>Ventas/capital, años 1–5</td><td>2,2×</td><td>2,7×</td><td>3,4×</td>', '<td>Ventas/capital, años 1–5</td>' + ''.join('<td>%s×</td>' % n(c['sc'][s], 2) for s in ('conservador', 'base', 'optimista')))
r('<td>Ventas/capital, años 6–10</td><td>1,8×</td><td>2,2×</td><td>2,7×</td>', '<td>Ventas/capital, años 6–10</td>' + ''.join('<td>%s×</td>' % n(c['sc'][s], 2) for s in ('conservador', 'base', 'optimista')))
r('Ventas/capital 2,7× (Base)', 'Ventas/capital 1,64× (Base)')
r('Con ventas/capital de 2,7× en los años 1 a 5 (Base), por cada US$2,70 de ventas adicionales la empresa necesita invertir US$1 de capital.',
  'Desde R7 el ventas/capital sale por fórmula de las anclas del Ginzu de Damodaran (enmienda del contrato del 22-nov-2026). El Base usa el tercer cuartil global de semiconductores (N27 = 1,64×) en los dos tramos: por cada US$1,64 de ventas adicionales la empresa invierte US$1 de capital. Es el criterio que Damodaran aplicó a MercadoLibre en 2026 (=N27) para una empresa más eficiente que su sector; en sus libros de NVIDIA de 2023 y 2024 enlazó la mediana del sector (M27) y en enero de 2025 digitó 2,5×. El ancla queda cerca del número actual de NVIDIA (1,47×) y del incremental de tres años (1,51×); R6 usaba 2,7× y 2,2× sin ancla documentada. Conservador (1,34×) y Optimista (2,07×) conservan la proporción entre escenarios de R6.')
r('Las eficiencias de capital no provienen de una serie histórica homogénea de capital ajustado.', 'El ventas/capital se ancla en el tercer cuartil global de Damodaran (datos de enero de 2026), no en una serie histórica homogénea de capital ajustado.')
r('Cada valor incluye la caja y los activos no operativos del libro', 'Recalculadas con los supuestos R7: las pruebas que no fijan su propio ventas/capital cambian menos de 0,3 % y quedan iguales al redondeo. Cada valor incluye la caja y los activos no operativos del libro')
# 4) figuras
fm = lambda d: (lambda x: n(100*x, d) + ' %')
grid_png(T, 'fig-10-r7.png', g['f10'], PX, fm(2), fm(1)); grid_png(T, 'fig-11-r7.png', g['f11'], PX, fm(0), fm(0)); grid_png(T, 'fig-12-r7.png', g['f12'], PX, lambda x: n(100*x, 1 if x < 0.1 else 0) + ' %', fm(1))
barras(IMG/T/'fig-07-r7.png', [('Optimista (R7)', vo, 'opt'), ('Base (R7)', vb, 'base'), ('Precio 155,46', PX, 'precio'), ('Conservador (R7)', vc, 'cons'), ('Estrés: commoditización', 54, 'estres'), ('Estrés: estancamiento', 49, 'estres'), ('Estrés: retroceso', 29, 'estres'), ('Estrés: retroceso severo', 18, 'estres')], 'US$', 'Valor por acción (US$): escenarios oficiales R7, precio del 17-nov-2026 y pruebas de estrés ilustrativas.')
for f in ('fig-07', 'fig-10', 'fig-11', 'fig-12'): r(f'/NVDA/{f}.png', f'/NVDA/{f}-r7.png', cnt=1)
# 5) expediente
anclas = {'conservador': {'1a5': 'Global 3.er cuartil', '6a10': 'Global 3.er cuartil', 'factor': 0.8148, 'valor': c['sc']['conservador']},
          'base': {'1a5': 'Global 3.er cuartil', '6a10': 'Global 3.er cuartil', 'factor': 1, 'valor': c['sc']['base']},
          'optimista': {'1a5': 'Global 3.er cuartil', '6a10': 'Global 3.er cuartil', 'factor': 1.2593, 'valor': c['sc']['optimista']},
          'anclas': {'Empresa actual': 1.4724, 'Empresa marginal (último año)': 1.3627, 'Empresa marginal (3 años)': 1.5058, 'Industria EE. UU. (promedio)': 1.2067, 'Industria global (promedio)': 1.1093, 'Global 1.er cuartil': 0.4886, 'Global mediana': 0.8872, 'Global 3.er cuartil': 1.6404},
          'industria': 'Semiconductor', 'fuente': "'JMR Escenarios'!A33:G48 (fórmulas sobre 'Input sheet'!I27:N28)"}
nota = 'R7 (22-nov-2026): ventas/capital por fórmula desde las anclas de Damodaran (tercer cuartil global de semiconductores, N27 = 1,64× en ambos tramos; Conservador ×0,815 y Optimista ×1,259). Sin otros cambios de supuestos; mismo corte LTM 26-jul-2026. Paridad libro–motor 0,0000 %.'
just = 'Ancla de Damodaran por fórmula: tercer cuartil global de semiconductores (N27 = 1,64×) en los años 1–5 y 6–10 (B32 = B31). Precedentes: MercadoLibre 2026 (=N27); NVIDIA 2023/24 (=M27, mediana); NVIDIA ene-2025 (2,5× digitado). Cerca del número actual de NVIDIA (1,47×) y del incremental de tres años (1,51×). Conservador 1,34× y Optimista 2,07× conservan la proporción de R6 (2,2/2,7/3,4).'
expediente(e, T, REV, SHEET, c, anclas, nota, just_sc=just, warn='R7 (22-nov-2026): ventas/capital de 2,7× → 1,64× (ancla N27 de Damodaran); valor Base de US$212,33 a US$' + n(vb) + '.')
e['sensitivity5x5'] = c['s5']
a['blocks'] = B; a['revision'] = REV
for k in ('pdf', 'informePdf'):
    if isinstance(a.get(k), str): a[k] = f'jmr-v2/informes/{T}/{REV}_INFORME_FUNDAMENTAL.pdf'
    elif isinstance(a.get(k), dict): a[k] = {**a[k], 'ruta': f'jmr-v2/informes/{T}/{REV}_INFORME_FUNDAMENTAL.pdf'}
a['revisionMetodo'] = {'fecha': '2026-11-22', 'anterior': 'NVDA-V2-FY26Q2FY27-R6', 'alcance': 'Ventas/capital por anclas de Damodaran; cifras de valoración, sensibilidades y figuras actualizadas.'}
save(T, e, a); print('OK', n(vb), r.log[:3], len(r.log))
