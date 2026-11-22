from comun import *
T, REV, SHEET = 'EPAM', 'EPAM-V2-LTM20260930-R7', '1sQBZfuAEDlANsydbRLjKVOWUCDo7gPKsUyvfQEF_8vU'
c = json.load(open(W/'calc.json'))[T]; P2 = json.load(open(W/'epam_c2.json')); p = P2['new']
e, a = load(T); B = a['blocks']; cortar_just(B); r = Rep(B)
vc, vb, vo = c['esc']['conservador'], c['esc']['base'], c['esc']['optimista']; mos = vb*0.65; PX = 154.14; D = c['det']; tv = p['tv']; g = p['grids']; P = p['probes']
r(r'\bR6\b', 'R7', regex=True)
r('US$127–US$277', 'US$%s–US$%s' % (n(vc, 0), n(vo, 0)))
for o, nn in [('127,19', vc), ('197,32', vb), ('276,94', vo), ('128,26', mos)]: r(o, n(nn))
for o, nn in [('127', vc), ('277', vo)]: r(r'US\$%s(?!\d|[.,]\d| mil| M\b)' % o, 'US$' + n(nn, 0), regex=True)
r('-17,5 %', pc(vc/PX-1)); r('+79,7 %', pc(vo/PX-1)); r('+28,0 %', pc(vb/PX-1), cnt=2)
r('-17 %', '-' + n(100*(1-vc/PX), 0) + ' %', cnt=2); r('80 %', n(100*(vo/PX-1), 0) + ' %', cnt=2, keys=['tesis_contraria', 'supuestos'])
r('el precio supera en 20 % el precio con margen', 'el precio supera en %s %% el precio con margen' % n(100*(PX/mos-1), 0))
r('a ~US$174 (-12 %)', 'a ~US$%s (-%s %%)' % (n(P['wacc+1'], 0), n(100*(1-P['wacc+1']/vb), 0)))
for o, k in [('5.788', ('conservador', 'ev')), ('9.518', ('base', 'ev')), ('13.752', ('optimista', 'ev'))]: r('<td>%s</td>' % o, '<td>%s</td>' % n(D[k[0]][k[1]], 0), keys=['valoracion'])
r('60,3 %', pc(tv['conservador'], 1, False), keys=['valoracion']); r('67,5 %', pc(tv['base'], 1, False), keys=['valoracion']); r('70,4 %', pc(tv['optimista'], 1, False), keys=['valoracion'])
NI, SH = 425.2, 53.18
for o, s in [('15,9×', 'conservador'), ('24,7×', 'base'), ('34,6×', 'optimista')]: r(o, n(c['esc'][s]*SH/NI, 1) + '×', keys=['valoracion'])
# Puente (si existe en el bloque)
v = B['valoracion']
for o, k in [('3.094', ('base', 'sumPV')), ('10.492', ('base', 'equity'))]:
    if o in v: r(o, n(D[k[0]][k[1]], 0), keys=['valoracion'])
SC = c['sc']; sc = lambda s: n(SC[s], 2) + '×'
r('<td>Ventas/capital, años 1–5</td><td>1,80×</td><td>2,20×</td><td>2,60×</td>', '<td>Ventas/capital, años 1–5</td>' + ''.join('<td>%s</td>' % sc(s) for s in ('conservador', 'base', 'optimista')))
r('<td>Ventas/capital, años 6–10</td><td>1,60×</td><td>2,00×</td><td>2,30×</td>', '<td>Ventas/capital, años 6–10</td>' + ''.join('<td>%s</td>' % sc(s) for s in ('conservador', 'base', 'optimista')))
r('El modelo supone ventas/capital de 2,2× en el Base', 'El modelo supone ventas/capital de %s en el Base (el número actual de EPAM)' % sc('base'))
r('La eficiencia de capital es de 1,8× / 2,2× / 2,6× en los años 1–5 y de 1,6× / 2,0× / 2,3× en los años 6–10: por cada US$2,2 de ventas adicionales se invierte US$1 de capital (en buena parte capital de trabajo de cuentas por cobrar).',
  'Desde R7 el ventas/capital sale por fórmula de las anclas del Ginzu de Damodaran (enmienda del contrato del 22-nov-2026): el Base usa el número actual de EPAM (I27 = %s) en los diez años, y el Conservador (%s) y el Optimista (%s) conservan la proporción de R6. La industria del libro se corrigió a Computer Services, la que Damodaran asigna a EPAM (la plantilla traía Food Processing por defecto): su promedio global es 3,75× y su tercer cuartil 5,48×, una eficiencia que EPAM no muestra (marginal de 0,77×, porque su capital crece con adquisiciones). R6 usaba 2,2× y 2,0× sin ancla. Por cada US$%s de ventas adicionales se invierte US$1 de capital, en buena parte capital de trabajo de cuentas por cobrar.' % (sc('base'), sc('conservador'), sc('optimista'), n(SC['base'], 2)))
fm = lambda d: (lambda x: n(100*x, d) + ' %')
grid_png(T, 'fig-08-r7.png', g['f08'], PX, fm(2), fm(1)); grid_png(T, 'fig-09-r7.png', g['f09'], PX, fm(1), fm(1)); grid_png(T, 'fig-10-r7.png', g['f10'], PX, fm(1), fm(1))
barras(IMG/T/'fig-05-r7.png', [('Optimista (R7)', vo, 'opt'), ('Base (R7)', vb, 'base'), ('Precio 154,14', PX, 'precio'), ('Conservador (R7)', vc, 'cons'), ('Estrés: estancamiento', 125, 'estres'), ('Estrés: deflación por IA', 110, 'estres'), ('Estrés: retroceso', 80, 'estres')], 'US$', 'Valor por acción (US$): escenarios oficiales R7, precio del 17-nov-2026 y pruebas de estrés ilustrativas.')
for f in ('fig-05', 'fig-08', 'fig-09', 'fig-10'): r(f'/EPAM/{f}.png', f'/EPAM/{f}-r7.png', cnt=1)
anclas = {s: {'1a5': 'Empresa actual', '6a10': 'Empresa actual', 'factor': f, 'valor': SC[s]} for s, f in [('conservador', 0.8182), ('base', 1), ('optimista', 1.1818)]}
anclas.update({'anclas': {'Empresa actual': 2.1284, 'Empresa marginal (último año)': 0.7737, 'Empresa marginal (3 años)': 0.7642, 'Industria EE. UU. (promedio)': 5.1899, 'Industria global (promedio)': 3.7547, 'Global 1.er cuartil': 1.1792, 'Global mediana': 2.8054, 'Global 3.er cuartil': 5.4787},
               'industria': 'Computer Services', 'fuente': "'JMR Escenarios'!A33:G48 (fórmulas sobre 'Input sheet'!I27:N28)"})
nota = 'R7 (22-nov-2026): ventas/capital por fórmula desde el número actual de la empresa (I27 = 2,13×, ambos tramos; Conservador ×0,818 y Optimista ×1,182) e industria corregida a Computer Services (indname ene-2026; la plantilla traía Food Processing). La beta es entrada directa y no depende de la industria. Paridad libro–motor 0,0000 %.'
just = 'Ancla de Damodaran por fórmula: número actual de EPAM (I27 = 2,13×) en los años 1–5 y 6–10 (B32 = B31). Industria Computer Services: promedio global 3,75× y tercer cuartil 5,48×, que EPAM no alcanza (marginal 0,77×; el capital crece por adquisiciones). Conservador 1,74× y Optimista 2,52× conservan la proporción de R6 (1,8/2,2/2,6).'
expediente(e, T, REV, SHEET, c, anclas, nota, just_sc=just, warn='R7 (22-nov-2026): ventas/capital Base 2,2×/2,0× → 2,13× (número actual) e industria Computer Services; valor Base de US$197,32 a US$' + n(vb) + '.')
a['blocks'] = B; a['revision'] = REV
for k in ('pdf', 'informePdf'):
    if isinstance(a.get(k), str): a[k] = f'jmr-v2/informes/{T}/{REV}_INFORME_FUNDAMENTAL.pdf'
    elif isinstance(a.get(k), dict): a[k] = {**a[k], 'ruta': f'jmr-v2/informes/{T}/{REV}_INFORME_FUNDAMENTAL.pdf'}
a['revisionMetodo'] = {'fecha': '2026-11-22', 'anterior': 'EPAM-V2-LTM20260930-R6', 'alcance': 'Ventas/capital por anclas de Damodaran e industria; cifras de valoración, sensibilidades y figuras actualizadas.'}
save(T, e, a); print('OK', n(vb), len(r.log))
