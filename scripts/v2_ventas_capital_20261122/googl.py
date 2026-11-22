from comun import *
T, REV, SHEET = 'GOOGL', 'GOOGL-V2-LTM20260930-R2', '17rXc5-AKAmyBgJYYBsaQ1RhWaLD_WVkYm26zQHPzBr0'
c = json.load(open(W/'calc.json'))[T]; P2 = json.load(open(W/'googl_c2.json')); p = P2['new']; po = P2['old']
e, a = load(T); B = a['blocks']; cortar_just(B); r = Rep(B)
vc, vb, vo = c['esc']['conservador'], c['esc']['base'], c['esc']['optimista']; mos = vb*0.65; PX = 272.66; D = c['det']; tv = p['tv']; g = p['grids']; P = p['probes']
SC = c['sc']; sc = lambda s, d=2: n(SC[s], d) + '×'
r('LTM20260930-R1', 'LTM20260930-R2')
# cifras exactas
for o, nn in [('149,52', vc), ('286,50', vb), ('447,61', vo), ('186,23', mos), ('231,79', P['g8']), ('228,68', P['m26']), ('231,01', P['roicW']), ('165,73', P['comb'])]: r(o, n(nn))
r('USD 286,5 con holgura de 5 %', 'USD %s con holgura de %s %%' % (n(vb, 1), n(100*(vb/PX-1), 0)))
r('Base 286,5; precio con MOS 186,2', 'Base %s; precio con MOS %s' % (n(vb, 1), n(mos, 1)))
r('(286,5 → 271,3)', '(%s → %s)' % (n(vb, 1), n(P['wi+1'], 1))); r('(286,5 → 247,3)', '(%s → %s)' % (n(vb, 1), n(P['wt+1'], 1)))
r('resta ≈ USD 40', 'resta ≈ USD %s' % n(vb-P['wt+1'], 0)); r('resta ≈ USD 15', 'resta ≈ USD %s' % n(vb-P['wi+1'], 0))
S3 = ('conservador', 'base', 'optimista')
swap_row(B, 'valoracion', 'Valor de las operaciones (EV, mil M)', [n(D[s]['ev']/1000, 0) for s in S3]); swap_row(B, 'valoracion', 'Valor terminal descontado / EV', [n(100*tv[s], 1) + ' %' for s in S3])
swap_row(B, 'valoracion', 'Valor del patrimonio (mil M)', [n(D[s]['equity']/1000, 0) for s in S3]); swap_row(B, 'valoracion', 'Brecha valor/precio − 1', [n(100*(c['esc'][s]/PX-1), 1) + ' %' for s in S3])
r('<td class="num">5,1 %</td>', '<td class="num">%s %%</td>' % n(100*(vb/PX-1), 1), keys=['perfil']); r('queda 5,1 % sobre', 'queda %s %% sobre' % n(100*(vb/PX-1), 1)); r('(Base +5,1 %)', '(Base +%s %%)' % n(100*(vb/PX-1), 1))
r('el Base está en +5 %', 'el Base está en +%s %%' % n(100*(vb/PX-1), 0))
r('(−45 %)', '(−%s %%)' % n(100*(1-vc/PX), 0)); r('(+64 %)', '(+%s %%)' % n(100*(vo/PX-1), 0))
r('−45 % hasta el Conservador y +64 % hasta el Optimista', '−%s %% hasta el Conservador y +%s %% hasta el Optimista' % (n(100*(1-vc/PX), 0), n(100*(vo/PX-1), 0)))
r('está 45 % por debajo', 'está %s %% por debajo' % n(100*(1-vc/PX), 0)); r('(−32 % frente al precio actual)', '(−%s %% frente al precio actual)' % n(100*(1-mos/PX), 0))
r('El Conservador (−48 % frente al Base)', 'El Conservador (−%s %% frente al Base)' % n(100*(1-vc/vb), 0))
r('valdría USD 166, 39 % por debajo del precio', 'valdría USD %s, %s %% por debajo del precio' % (n(P['comb'], 0), n(100*(1-P['comb']/PX), 0)))
r('valor de USD 166', 'valor de USD %s' % n(P['comb'], 0))
r('≈ USD 257 (WACC inicial de 11,96 %)', '≈ USD %s (WACC inicial de 11,96 %%)' % n(P['wi1196'], 0))
r('un valor Base de USD 256,0', 'un valor Base de USD %s' % n(P['wi1203'], 1))
r('el valor baja a USD 229', 'el valor baja a USD %s' % n(P['m26'], 0))
r(r'≈ USD 186(?![\d,])', '≈ USD ' + n(mos, 0), regex=True); r('≤ USD 186', '≤ USD ' + n(mos, 0))
# DCF inverso
im, i2 = p['imp'], p['imp2']
r('crecimiento de 12,6 %', 'crecimiento de %s %%' % n(100*im['growth2to5'], 1), cnt=3); r('margen operativo objetivo de 30,5 %', 'margen operativo objetivo de %s %%' % n(100*im['marginTarget'], 1))
r('margen objetivo de 30,5 %', 'margen objetivo de %s %%' % n(100*im['marginTarget'], 1), cnt=2); r('ROIC terminal de 13,1 %', 'ROIC terminal de %s %%' % n(100*i2['roicTerminal'], 1), cnt=3)
r('WACC inicial de 10,9 %.', 'WACC inicial de %s %%.' % n(100*i2['waccInitial'], 1))
r('WACC inicial de 10,9 % (Base 9,96 %)', 'WACC inicial de %s %% (Base 9,96 %%)' % n(100*i2['waccInitial'], 1))
r('71,5 %', n(100*tv['base'], 1) + ' %', cnt=2)
for o, k in [('3.304.299', ('base', 'ev')), ('3.555.804', ('base', 'equity'))]: r(o, n(D[k[0]][k[1]], 0))
# ventas/capital
r('Por eso el DCF Base modela ventas/capital de 1,0× y no extrapola', 'Por eso el DCF Base usa el ventas/capital actual de Alphabet (%s, ancla de Damodaran por fórmula) y no extrapola' % sc('base'))
r('</strong> (1,0× en el Base;', '</strong> (%s en el Base, el número actual de la empresa;' % sc('base'))
r('ventas/capital de 1,0×;', 'ventas/capital de %s (el número actual, en los diez años);' % sc('base'))
r('ventas/capital de 0,7×–0,8×;', 'ventas/capital de %s;' % sc('conservador')); r('ventas/capital de 1,3×–1,5×;', 'ventas/capital de %s;' % sc('optimista'))
swap_row(B, 'supuestos', 'Ventas/capital años 1–5', [sc(s) for s in ('conservador', 'base', 'optimista')])
swap_row(B, 'supuestos', 'Ventas/capital años 6–10', [sc(s) for s in ('conservador', 'base', 'optimista')])
Y = YEARS[T]['new']['base']['years']
swap_row(B, 'supuestos', 'Reinversión (mil M)', [n(y['reinvestment']/1000, 0) for y in Y]); swap_row(B, 'supuestos', 'FCFF (mil M)', [n(y['fcff']/1000, 0) for y in Y])
# tablas de sensibilidad del capítulo de valoración
rs = [0.10, 0.13, 0.16, 0.19, 0.22]; cs = [SC['base']*f for f in (0.667, 0.833, 1, 1.167, 1.333)]
import subprocess
cfg = {'price': PX, 'probes': {}, 'grids': {'RS': {'rk': 'roicTerminal', 'ck': 'salesToCapital1to5', 'rows': rs, 'cols': cs, 'tie': True}}}
json.dump(cfg, open(W/'googl_rs.json', 'w'))
subprocess.run(['node', str(W/'c2.mjs'), T, str(W/'googl_rs.json'), str(W/'googl_rs_out.json')], cwd=W, check=True, capture_output=True)
RS = json.load(open(W/'googl_rs_out.json'))['new']['grids']['RS']
swap_table(B, 'valoracion', 'ROIC terminal \\ ventas/capital', html_table('ROIC terminal \\ ventas/capital', [n(100*x, 0) + ' %' for x in rs], [n(x, 2) + '×' for x in cs], RS['m']))
r('ROIC terminal × ventas/capital (años 1–5; años 6–10 = 1,2×).', 'ROIC terminal × ventas/capital (igual en los años 1–5 y 6–10, como el Base R2; centro = número actual %s).' % sc('base'))
Wg = g['W']; swap_table(B, 'valoracion', 'WACC inicial \\ g', html_table('WACC inicial \\ g', [n(100*x, 2) + ' %' for x in Wg['rows']], [n(100*x, 1) + ' %' for x in Wg['cols']], Wg['m']))
# figuras
I = IMG/T
vvp(I/'valor_vs_precio-r2.png', c['esc'], mos, PX, 'Precio 19-nov-2026: 272,66')
L, R = g['L'], g['R']
heat2(I/'sensibilidades-r2.png', {'m': L['m'], 'rl': [n(100*x, 1) + ' %' for x in L['rows']], 'cl': [n(100*x, 1) + ' %' for x in L['cols']], 'title': 'WACC terminal × g (Base, USD/acción)', 'xl': 'Crecimiento terminal g', 'yl': 'WACC terminal'},
      {'m': R['m'], 'rl': [n(100*x, 1) + ' %' for x in R['rows']], 'cl': [n(100*x, 1) + ' %' for x in R['cols']], 'title': 'Margen objetivo × crecimiento años 2–5', 'xl': 'Crecimiento anual años 2–5', 'yl': 'Margen operativo objetivo'})
estres_fig(I/'estres-r2.png', [('WACC inicial 12,0 % (beta de industria única)', P['wi1203'], False), ('Crecimiento años 2–5 = 8 %', P['g8'], False), ('Margen objetivo y año 1 = 26 %', P['m26'], False), ('ROIC terminal = WACC terminal', P['roicW'], False),
            ('Ventas/capital 0,7× / 0,8×', P['sc78'], False), ('Conservador completo', vc, False), ('Optimista completo', vo, True), ('Combinado: 8 %, 26 %, ROIC 10 %', P['comb'], False)], PX, vb, 'Precio 272,66', 'Base %s' % n(vb, 1))
for f in ('valor_vs_precio', 'sensibilidades', 'estres'): r(f'/GOOGL/{f}.png', f'/GOOGL/{f}-r2.png')
# expediente
anclas = {s: {'1a5': 'Empresa actual', '6a10': 'Empresa actual', 'factor': f, 'valor': SC[s]} for s, f in [('conservador', 0.7), ('base', 1), ('optimista', 1.3)]}
anclas.update({'anclas': {'Empresa actual': 0.9003, 'Empresa marginal (último año)': 0.3714, 'Empresa marginal (3 años)': 0.4869, 'Industria EE. UU. (promedio)': 1.3501, 'Industria global (promedio)': 1.4006, 'Global 1.er cuartil': 0.6886, 'Global mediana': 1.3611, 'Global 3.er cuartil': 3.6624},
               'industria': 'Software (Internet)', 'industriaIndname': 'Software (Entertainment)', 'razonIndustria': 'Búsqueda, nube y suscripciones describen mejor el negocio; Damodaran usó Advertising en su valoración de 2024. La beta es multinegocio y no depende de esta celda.',
               'fuente': "'JMR Escenarios'!A33:G48 (fórmulas sobre 'Input sheet'!I27:N28)"})
nota = 'R2 (22-nov-2026): ventas/capital por fórmula desde el número actual de la empresa (I27 = 0,90×, ambos tramos; Conservador ×0,7 y Optimista ×1,3). Libro convertido a Google Sheets desde el .xlsx R1 sin otros cambios. Paridad libro–motor 0,0000 %.'
just = 'Ancla de Damodaran por fórmula: número actual de Alphabet (I27 = 0,90×) en los años 1–5 y 6–10 (B32 = B31). Damodaran usó 1,2× en feb-2024, igual al número actual de entonces. El promedio global de Software (Internet) (1,40×) supone una eficiencia que el capex de IA contradice (marginal 0,37×). Conservador 0,63× y Optimista 1,17× conservan la proporción de R1 (0,7/1,0/1,3).'
expediente(e, T, REV, SHEET, c, anclas, nota, just_sc=just, warn='R2 (22-nov-2026): ventas/capital Base 1,0×/1,2× → 0,90× (número actual); valor Base de US$286,50 a US$' + n(vb) + '.')
if isinstance(e.get('informe'), dict):
    for k, v in list(e['informe'].items()):
        if isinstance(v, str) and 'R1' in v: e['informe'][k] = v.replace('-R1', '-R2')
a['blocks'] = B; a['revision'] = REV
for k in ('pdf', 'informePdf'):
    if isinstance(a.get(k), str): a[k] = f'jmr-v2/informes/{T}/{REV}_INFORME_FUNDAMENTAL.pdf'
    elif isinstance(a.get(k), dict): a[k] = {**a[k], 'ruta': f'jmr-v2/informes/{T}/{REV}_INFORME_FUNDAMENTAL.pdf'}
a['updatedAt'] = '2026-11-22'
a['revisionMetodo'] = {'fecha': '2026-11-22', 'anterior': 'GOOGL-V2-LTM20260930-R1', 'alcance': 'Ventas/capital por anclas de Damodaran; cifras de valoración, trayectorias, sensibilidades y figuras actualizadas.'}
r('Si la primera cae a 0,7×,', 'Si la primera cae a 0,7× (0,8× en los años 6–10),')
save(T, e, a); print('OK', n(vb), len(r.log))
