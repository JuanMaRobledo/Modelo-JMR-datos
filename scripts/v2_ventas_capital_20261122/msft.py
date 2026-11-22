from comun import *
T, REV, SHEET = 'MSFT', 'MSFT-V2-LTM20260930-R6', '1l1jnSQSyVS0liZ64dEph61er9nji1qK8xBEnXkkZO20'
c = json.load(open(W/'calc.json'))[T]; p = json.load(open(W/'msft_c2.json'))['new']
e, a = load(T); B = a['blocks']; cortar_just(B); r = Rep(B)
vc, vb, vo = c['esc']['conservador'], c['esc']['base'], c['esc']['optimista']; mos = vb*0.65; PX = 506.24; D = c['det']; tv = p['tv']; g = p['grids']; P = p['probes']
up = lambda v: n(100*(v/PX-1), 0)
r(r'\bR5\b', 'R6', regex=True)
r('US$223–US$630', 'US$%s–US$%s' % (n(vc, 0), n(vo, 0)))
for o, nn in [('223,24', vc), ('462,85', vb), ('629,85', vo), ('300,85', mos)]: r(o, n(nn))
r('~US$396 (-14 %)', '~US$%s (-%s %%)' % (n(P['wacc+1'], 0), n(100*(1-P['wacc+1']/vb), 0)))
r('con 6,5 % sube a ~US$755 y con 10,5 % baja a ~US$349', 'con 6,5 %% sube a ~US$%s y con 10,5 %% baja a ~US$%s' % (n(g['f09']['m'][0][2], 0), n(g['f09']['m'][4][2], 0)))
r('el valor es ~US$359, y con 56 %, ~US$567', 'el valor es ~US$%s, y con 56 %%, ~US$%s' % (n(g['f10']['m'][2][0], 0), n(g['f10']['m'][2][4], 0)))
# pruebas de estrés: exceso fija su ventas/capital (cambia solo por el WACC inicial); estancamiento y retroceso usan el ventas/capital Base
est, ret = 162*P['est_r12']/json.load(open(W/'msft_c2.json'))['old']['probes']['est_r12'], 116*P['ret_r12']/json.load(open(W/'msft_c2.json'))['old']['probes']['ret_r12']
r('US$162</td><td>-68 %', 'US$%s</td><td>-%s %%' % (n(est, 0), n(100*(1-est/PX), 0))); r('US$116</td><td>-77 %', 'US$%s</td><td>-%s %%' % (n(ret, 0), n(100*(1-ret/PX), 0)))
r('~US$162', '~US$' + n(est, 0)); r('~US$116', '~US$' + n(ret, 0))
for o, nn in [('223', vc), ('463', vb), ('630', vo), ('301', mos)]: r(r'US\$%s(?!\d|[.,]\d| mil| M\b)' % o, 'US$' + n(nn, 0), regex=True)
r('-8,6 %', pc(vb/PX-1)); r('-55,9 %', pc(vc/PX-1)); r('+24,4 %', pc(vo/PX-1))
r('queda 9 % por debajo del cierre', 'queda %s %% por debajo del cierre' % n(100*(1-vb/PX), 0)); r('por acción, 9 % por debajo del cierre', 'por acción, %s %% por debajo del cierre' % n(100*(1-vb/PX), 0))
r('el precio supera el valor Base en 9 %', 'el precio supera el valor Base en %s %%' % n(100*(PX/vb-1), 0))
r('US$%s · -9 %% vs. precio' % n(vb, 0), 'US$%s · -%s %% vs. precio' % (n(vb, 0), n(100*(1-vb/PX), 0)))
r('-56 %', '-' + n(100*(1-vc/PX), 0) + ' %'); r('y el Optimista 24 %', 'y el Optimista %s %%' % up(vo)); r('· +24 % vs. precio', '· +%s %% vs. precio' % up(vo))
r('~16 %', '~' + n(100*p['imp']['growth2to5'], 0) + ' %'); r('~50 %', '~' + n(100*p['imp']['marginTarget'], 0) + ' %')
r('16,2 %', '%s %%' % n(100*p['imp']['growth2to5'], 1), keys=['valoracion']); r('50,2 %', '%s %%' % n(100*p['imp']['marginTarget'], 1), keys=['valoracion'])
r('el precio supera en 68 % el precio con margen', 'el precio supera en %s %% el precio con margen' % n(100*(PX/mos-1), 0))
r('El valor terminal pesa 70 % del Base', 'El valor terminal pesa %s %% del Base' % n(100*tv['base'], 0)); r('El valor terminal pesa 70 % del valor operativo', 'El valor terminal pesa %s %% del valor operativo' % n(100*tv['base'], 0))
r('Un 70 % del valor Base', 'Un %s %% del valor Base' % n(100*tv['base'], 0))
for o, k in [('1.033.423', ('base', 'sumPV')), ('2.444.060', ('base', 'pvTerminal')), ('3.477.484', ('base', 'ev')), ('3.473.347', ('base', 'equity')), ('1.679.411', ('conservador', 'ev')), ('4.730.660', ('optimista', 'ev'))]: r(o, n(D[k[0]][k[1]], 0))
r('56,4 %', pc(tv['conservador'], 1, False)); r('70,3 %', pc(tv['base'], 1, False)); r('71,9 %', pc(tv['optimista'], 1, False))
NI, SH = 142631, 7504.2
for o, s in [('11,7×', 'conservador'), ('24,4×', 'base'), ('33,1×', 'optimista')]: r(o, n(c['esc'][s]*SH/NI, 1) + '×', keys=['valoracion'])
# WACC y beta
WI = n(100*c['assumptions']['base']['waccInitial'], 2)
r('10,77 %', WI + ' %')
# ventas/capital
SC = c['sc']; sc = lambda s: n(SC[s], 2) + '×'
r('<td>Ventas/capital, años 1–5</td><td>0,55×</td><td>0,80×</td><td>1,10×</td>', '<td>Ventas/capital, años 1–5</td>' + ''.join('<td>%s</td>' % sc(s) for s in ('conservador', 'base', 'optimista')))
r('<td>Ventas/capital, años 6–10</td><td>0,90×</td><td>1,20×</td><td>1,50×</td>', '<td>Ventas/capital, años 6–10</td>' + ''.join('<td>%s</td>' % sc(s) for s in ('conservador', 'base', 'optimista')))
r('(ventas/capital de 0,55× a 1,1×)', '(ventas/capital de %s a %s, anclado en el número actual de la empresa)' % (sc('conservador'), sc('optimista')))
r('fija ventas/capital en 0,8× en los años 1–5 del Base (es decir, cada dólar de ventas nuevo exige US$1,25 de capital), muy por debajo de 3,0× de Apple o de 2,7× de NVIDIA.',
  'fija ventas/capital en %s en los diez años del Base (es decir, cada dólar de ventas nuevo exige US$%s de capital): es el número actual de Microsoft, muy por debajo de 3,0× de Apple o de 1,64× de NVIDIA.' % (sc('base'), n(1/SC['base'], 2)))
r('ventas/capital de 0,8× en el Base', 'ventas/capital de %s en el Base' % sc('base'), cnt=2)
r('Ventas/capital Base 0,8×', 'Ventas/capital Base ' + sc('base'))
r('la eficiencia de capital de 0,8× es el supuesto que más pesa', 'la eficiencia de capital de %s es el supuesto que más pesa' % sc('base'))
r('La eficiencia de capital de 0,8× y el ROIC terminal de 18 % son supuestos del libro sin serie histórica homogénea.', 'El ventas/capital de %s es el número actual de la empresa (ancla de Damodaran, enmienda del 22-nov-2026) y el ROIC terminal de 18 %% es supuesto del libro sin serie histórica homogénea.' % sc('base'))
r('La eficiencia de capital en los años 1–5 es de 0,55× / 0,80× / 1,10× (y 0,90× / 1,20× / 1,50× después): cada dólar de ventas nuevo exige entre US$0,9 y US$1,8 de capital invertido, a diferencia de NVIDIA o Apple, donde es mucho menor.',
  'Desde R6 el ventas/capital sale por fórmula de las anclas del Ginzu de Damodaran (enmienda del contrato del 22-nov-2026). El Base usa el número actual de Microsoft (I27 = %s) en los diez años, como hace Damodaran cuando la empresa difiere de su sector («look at your company\'s current number»): el promedio global de Software (System & Application) es 1,54× y su tercer cuartil 3,58×, pero el capex de IA dejó el marginal del último año en 0,14× y el de tres años en 0,37×. En su valoración de Microsoft de 2024 Damodaran digitó 3,0×, antes de la ola de capex. R5 usaba 0,80× y 1,20× sin ancla documentada. Conservador (%s) y Optimista (%s) conservan la proporción entre escenarios de R5. Cada dólar de ventas nuevo exige US$%s de capital invertido en el Base, a diferencia de NVIDIA o Apple, donde es mucho menor.' % (sc('base'), sc('conservador'), sc('optimista'), n(1/SC['base'], 2)))
# beta (WACC del libro R6)
for k in B:
    if 'beta apalancada 1,28' in B[k]: B[k] = B[k].replace('beta apalancada 1,28 (entrada directa)', 'beta desapalancada de Software (System &amp; Application) de EE. UU. 1,25, reapalancada por fórmula (≈1,28)')
r('<td>WACC inicial</td><td>%s %%</td><td>Calculado en el libro</td>' % WI, '<td>WACC inicial</td><td>%s %%</td><td>Calculado en el libro con beta sectorial de Damodaran (Software (System &amp; Application), desapalancada 1,25)</td>' % WI)
# figuras
fm = lambda d: (lambda x: n(100*x, d) + ' %')
grid_png(T, 'fig-09-r6.png', g['f09'], PX, fm(2), fm(1)); grid_png(T, 'fig-10-r6.png', g['f10'], PX, fm(1), fm(1)); grid_png(T, 'fig-11-r6.png', g['f11'], PX, fm(1), fm(1))
exc = 201*P['exc']/json.load(open(W/'msft_c2.json'))['old']['probes']['exc']
barras(IMG/T/'fig-06-r6.png', [('Optimista (R6)', vo, 'opt'), ('Precio 506,24', PX, 'precio'), ('Base (R6)', vb, 'base'), ('Conservador (R6)', vc, 'cons'), ('Estrés: exceso de capacidad de IA', exc, 'estres'), ('Estrés: estancamiento', est, 'estres'), ('Estrés: retroceso', ret, 'estres')], 'US$', 'Valor por acción (US$): escenarios oficiales R6, precio del 17-nov-2026 y pruebas de estrés ilustrativas.')
r('US$201</td><td>-60 %', 'US$%s</td><td>-%s %%' % (n(exc, 0), n(100*(1-exc/PX), 0))); r('~US$201', '~US$' + n(exc, 0))
for f in ('fig-06', 'fig-09', 'fig-10', 'fig-11'): r(f'/MSFT/{f}.png', f'/MSFT/{f}-r6.png', cnt=1)
r('salvo los indicados.', 'salvo los indicados; recalculadas con R6 (ventas/capital y WACC inicial nuevos).', keys=['destruccion'])
anclas = {s: {'1a5': 'Empresa actual', '6a10': 'Empresa actual', 'factor': f, 'valor': SC[s]} for s, f in [('conservador', 0.6875), ('base', 1), ('optimista', 1.375)]}
anclas.update({'anclas': {'Empresa actual': 0.5938, 'Empresa marginal (último año)': 0.137, 'Empresa marginal (3 años)': 0.369, 'Industria EE. UU. (promedio)': 1.538, 'Industria global (promedio)': 1.543, 'Global 1.er cuartil': 0.640, 'Global mediana': 1.528, 'Global 3.er cuartil': 3.584},
               'industria': 'Software (System & Application)', 'fuente': "'JMR Escenarios'!A33:G48 (fórmulas sobre 'Input sheet'!I27:N28)"})
nota = 'R6 (22-nov-2026): ventas/capital por fórmula desde el número actual de la empresa (I27 = 0,594×, ambos tramos; Conservador ×0,6875 y Optimista ×1,375); industria corregida a Software (System & Application) (la plantilla traía Food Processing); beta bottom-up de EE. UU. (Single Business) en lugar de la entrada directa 1,28: WACC inicial 10,77 % → 10,74 %. Paridad libro–motor 0,0000 %.'
just = 'Ancla de Damodaran por fórmula: número actual de Microsoft (I27 = 0,59×) en los años 1–5 y 6–10 (B32 = B31). El promedio global de la industria (1,54×) y su tercer cuartil (3,58×) suponen una eficiencia que el capex de IA contradice (marginal 0,14× en el último año y 0,37× en tres años). Damodaran digitó 3,0× en su valoración de 2024, antes de la ola de capex. Conservador 0,41× y Optimista 0,82× conservan la proporción de R5 (0,55/0,80/1,10).'
expediente(e, T, REV, SHEET, c, anclas, nota, just_sc=just, warn='R6 (22-nov-2026): ventas/capital Base 0,80×/1,20× → 0,59× (número actual) y WACC inicial 10,74 % con beta sectorial; valor Base de US$462,85 a US$' + n(vb) + '.')
cc = e['libro'].get('costoCapital')
if isinstance(cc, dict): cc['waccInicial'] = c['assumptions']['base']['waccInitial']; cc['beta'] = {'metodo': 'Single Business(US)', 'industria': 'Software (System & Application)', 'desapalancada': 1.25}
J = e['justificaciones']; J['wacc'] = 'Cost of capital worksheet con beta bottom-up de Damodaran (Single Business(US), Software (System & Application), desapalancada 1,25 y reapalancada por fórmula ≈1,28), ERP ponderada por regiones de ingresos 4,52 %, costo de deuda 5,49 % y tasa marginal 23 %: WACC inicial 10,74 % → terminal 8,54 %.'
a['blocks'] = B; a['revision'] = REV
for k in ('pdf', 'informePdf'):
    if isinstance(a.get(k), str): a[k] = f'jmr-v2/informes/{T}/{REV}_INFORME_FUNDAMENTAL.pdf'
    elif isinstance(a.get(k), dict): a[k] = {**a[k], 'ruta': f'jmr-v2/informes/{T}/{REV}_INFORME_FUNDAMENTAL.pdf'}
a['revisionMetodo'] = {'fecha': '2026-11-22', 'anterior': 'MSFT-V2-LTM20260930-R5', 'alcance': 'Ventas/capital por anclas de Damodaran, industria y beta sectorial; cifras de valoración, sensibilidades y figuras actualizadas.'}
save(T, e, a); print('OK', n(vb), len(r.log), 'est', n(est), 'ret', n(ret), 'exc', n(exc))
