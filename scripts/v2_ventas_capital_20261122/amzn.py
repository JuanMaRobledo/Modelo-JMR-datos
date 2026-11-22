from comun import *
import numpy as np, subprocess
T, REV, SHEET = 'AMZN', 'AMZN-V2-LTM20260930-R2', '1ZAAdEPBsLUmT2PoKjJt9jTs-mZKdMHqMZ_mOdkH9_0Y'
c = json.load(open(W/'calc.json'))[T]; P2 = json.load(open(W/'amzn_c2.json')); p = P2['new']
e, a = load(T); B = a['blocks']; cortar_just(B); r = Rep(B)
vc, vb, vo = c['esc']['conservador'], c['esc']['base'], c['esc']['optimista']; mos = vb*0.65; PX = 257.37; D = c['det']; tv = p['tv']; g = p['grids']; P = p['probes']
SC = c['sc']; sc = lambda s, d=2: n(SC[s], d) + '×'; S3 = ('conservador', 'base', 'optimista')
NOOP = vb - 303.2e3/10929
g21 = float(subprocess.run(['node', str(W/'solve.mjs'), T, '{"marginTarget":0.21}', 'growth2to5', '-0.2', '0.6', str(PX)], cwd=W, capture_output=True, text=True).stdout.split('new')[1]) / 100
r('LTM20260930-R1', 'LTM20260930-R2'); r('abrir la revisión R2', 'abrir la revisión R3')
for o, nn in [('115,63', vc), ('196,96', vb), ('348,78', vo), ('128,02', mos)]: r(o, n(nn))
r(r'USD 128(?![\d,])', 'USD ' + n(mos, 0), regex=True); r(r'USD 116(?![\d,])', 'USD ' + n(vc, 0), regex=True); r(r'USD 349(?![\d,])', 'USD ' + n(vo, 0), regex=True); r(r'USD 197(?![\d,])', 'USD ' + n(vb, 0), regex=True)
r('a 197 (Base)', 'a %s (Base)' % n(vb, 0)); r('≈ USD %s' % n(mos, 0), '≈ USD %s' % n(mos, 0))
r('<td class="num">-23 %</td>', '<td class="num">%s %%</td>' % n(100*(vb/PX-1), 0), keys=['perfil'])
# tabla de resultados por escenario y puente
v = B['valoracion']
for s, ev0 in [('Conservador', '1.109'), ('Base', '1.998'), ('Optimista', '3.657')]:
    k = s.lower(); old = '<td class="">%s</td><td class="num">%s</td>' % (s, ev0)
    i = v.find(old); assert i >= 0, old; j = v.find('</tr>', i)
    v = v[:i] + '<td class="">%s</td><td class="num">%s</td><td class="num">%s</td><td class="num">%s %%</td><td class="num">%s %%</td>' % (s, n(D[k]['ev']/1000, 0), n(c['esc'][k]), n(100*(c['esc'][k]/PX-1), 0), n(100*tv[k], 0)) + v[j:]
v = v.replace('<td class="num">-50 %</td>', '<td class="num">%s %%</td>' % n(100*(mos/PX-1), 0), 1)
for o, nn in [('<td class="num">1.998</td>', n(D['base']['ev']/1000, 0)), ('<td class="num">2.153</td>', n(D['base']['equity']/1000, 0))]:
    assert o in v, o; v = v.replace(o, '<td class="num">%s</td>' % nn, 1)
B['valoracion'] = v
# estrés
def fila(lbl, val):
    return '<tr><td class="">%s</td><td class="num">%s</td><td class="num">%s %%</td></tr>' % (lbl, n(val), n(100*(val/vb-1), 1))
ST = [('Base', vb), ('Margen objetivo 14 % (sin expansión)', P['m14']), ('Crecimiento 2–5 = 8 %', P['g8']), ('ROIC terminal = WACC (8,54 %)', P['roicW']), ('Ventas/capital 0,7× en los diez años (capex sin retorno)', P['sc07']),
      ('WACC inicial 10,44 % (+1 pp)', P['wi+1']), ('Sin activos no operativos (Anthropic/OpenAI a cero)', NOOP), ('Combinado: margen 14 %, g 8 %, S/C 0,7×, ROIC = WACC', P['comb'])]
swap_table(B, 'destruccion', 'Margen objetivo 14 % (sin expansión)', '<table><thead><tr><th class="">Prueba</th><th class="num">Valor por acción (USD)</th><th class="num">Frente al Base</th></tr></thead><tbody>' + ''.join(fila(l, x) for l, x in ST) + '</tbody></table>')
r('(margen 14 %, g 8 %, ventas/capital 0,7× y ROIC = WACC) el valor es USD 114, 56 % inferior al precio', '(margen 14 %%, g 8 %%, ventas/capital 0,7× en los diez años y ROIC = WACC) el valor es USD %s, %s %% inferior al precio' % (n(P['comb'], 0), n(100*(1-P['comb']/PX), 0)))
r('sin ellas el Base es USD 169', 'sin ellas el Base es USD %s' % n(NOOP, 0))
# precio frente a escenarios y consenso
r('el precio está a +31 % del Base, 26 % por debajo del Optimista y 123 % por encima del Conservador', 'el precio está a +%s %% del Base, %s %% por debajo del Optimista y %s %% por encima del Conservador' % (n(100*(PX/vb-1), 0), n(100*(1-PX/vo), 0), n(100*(PX/vc-1), 0)))
r('+67 % sobre el Base y 6 % por debajo del Optimista', '+%s %% sobre el Base y %s %% por debajo del Optimista' % (n(100*(328.54/vb-1), 0), n(100*(1-328.54/vo), 0)))
im = p['imp']
r('crecimiento anual de 22,3 % en los años 2–5', 'crecimiento anual de %s %% en los años 2–5' % n(100*im['growth2to5'], 1)); r('margen operativo objetivo de 21,4 %', 'margen operativo objetivo de %s %%' % n(100*im['marginTarget'], 1))
r('con margen de 21 %, crecimiento de 13,7 %', 'con margen de 21 %%, crecimiento de %s %%' % n(100*g21, 1))
r('crecimiento de 22 % durante cuatro años o margen de 21 %', 'crecimiento de %s %% durante cuatro años o margen de %s %%' % (n(100*im['growth2to5'], 0), n(100*im['marginTarget'], 0)))
r('Ninguna prueba individual lleva el valor por debajo de USD 150, pero la suma de varias sí lo acerca a USD 114', 'Ninguna prueba individual lleva el valor muy por debajo de USD 150 (la más severa, margen objetivo de 14 %%, da USD %s), pero la suma de varias lo acerca a USD %s' % (n(P['m14'], 0), n(P['comb'], 0)))
r('crecimiento de 22,3 % anual en los años 2–5 o margen operativo de 21,4 %', 'crecimiento de %s %% anual en los años 2–5 o margen operativo de %s %%' % (n(100*im['growth2to5'], 1), n(100*im['marginTarget'], 1)))
r('un margen de seguridad de USD 128,', 'un margen de seguridad de USD %s,' % n(mos, 0))
# ventas/capital
swap_row(B, 'supuestos', 'Ventas/capital años 1–5', [n(SC[s], 2) for s in S3]); swap_row(B, 'supuestos', 'Ventas/capital años 6–10', [n(SC[s], 2) for s in S3])
r('<td class="">1,0× y 1,6×</td>', '<td class="">%s en los diez años (número actual; ancla de Damodaran)</td>' % sc('base'))
Y = YEARS[T]['new']
r('el año 1 del Base reinvierte ≈ 120 mil M', 'el año 1 del Base reinvierte ≈ %s mil M' % n(Y['base']['years'][0]['reinvestment']/1000, 0))
for s, lab in [('conservador', 'Conservador'), ('base', 'Base'), ('optimista', 'Optimista')]:
    yy = Y[s]['years']; swap_row(B, 'supuestos', lab + ' · FCFF (mil M)', [n(yy[i]['fcff']/1000, 0) for i in (0, 2, 4, 9)])
r('Ventas/capital 0,8–1,3×', 'Ventas/capital %s–%s' % (n(SC['conservador'], 2), sc('optimista')))
r('exigen ventas/capital cercano a 1,0× para que el Base se cumpla', 'exigen sostener el ventas/capital actual (%s) para que el Base se cumpla' % sc('base'))
r('si el capex no genera ventas/capital de 1,0×, se queda largo', 'si el capex no sostiene el ventas/capital actual de %s, se queda largo' % sc('base'))
# figuras (estilo AMZN)
plt.rcParams.update({'font.family': 'Liberation Sans'}); I = IMG/T
FUENTE = lambda fig, t: fig.text(0.01, 0.015, t, color='#7d8b96', fontsize=8.5)
def sty(ax):
    for s_ in ('top', 'right'): ax.spines[s_].set_visible(False)
    for s_ in ('left', 'bottom'): ax.spines[s_].set_color('#c5ced6')
fig, ax = plt.subplots(figsize=(8.3, 4.1), dpi=150)
lab = ['Conservador', 'Base', 'Optimista', 'Base con MOS 35 %']; val = [vc, vb, vo, mos]
ax.bar(lab, val, color=['#a8c3d3', '#5b8baa', '#1d3449', '#c4a282'], width=0.55)
for i, x in enumerate(val): ax.text(i, x + 4, n(x), ha='center', fontsize=10)
ax.axhline(PX, color='#b5554b', ls='--', lw=1.3); ax.text(3.45, PX + 6, 'Precio 19-nov-2026: 257,37', ha='right', color='#b5554b', fontsize=10)
ax.set_ylabel('USD por acción'); sty(ax); FUENTE(fig, 'Fuente: libro oficial %s (Simple Ginsu); MOS solo sobre el Base. Elaboración JMR.' % REV)
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(I/'valor_vs_precio-r2.png'); plt.close(fig)
def heatA(ax, M, rl, cl, title, xl, yl, center):
    M = np.array(M, float); ax.imshow(M, cmap='Blues', aspect='auto', vmin=M.min()*0.95, vmax=M.max()*1.02)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]): ax.text(j, i, n(M[i, j], 0), ha='center', va='center', fontsize=10, color='white' if M[i, j] > M.min() + 0.6*(M.max()-M.min()) else '#1d3449', fontweight='bold' if (i, j) == center else 'normal')
    ax.set_xticks(range(len(cl))); ax.set_xticklabels(cl, fontsize=9); ax.set_yticks(range(len(rl))); ax.set_yticklabels(rl, fontsize=9)
    ax.set_title(title, fontsize=11); ax.set_xlabel(xl, fontsize=10); ax.set_ylabel(yl, fontsize=10)
    for s_ in ax.spines.values(): s_.set_visible(False)
def pair(path, A1, A2, foot):
    fig, axs = plt.subplots(1, 2, figsize=(9.2, 4.2), dpi=150)
    heatA(axs[0], *A1); heatA(axs[1], *A2); FUENTE(fig, foot); fig.tight_layout(rect=(0, 0.05, 1, 1)); fig.savefig(path); plt.close(fig)
pct = lambda x, d=2: n(100*x, d)
L, R, Wg = g['L'], g['R'], g['W']
pair(I/'sensibilidades-r2.png', (L['m'], [pct(x) for x in L['rows']], [pct(x, 1) for x in L['cols']], 'Base: WACC terminal × g (USD/acción)', 'g terminal, %', 'WACC terminal, %', (2, 2)),
     (R['m'], [pct(x, 0) for x in R['rows']], [pct(x, 0) for x in R['cols']], 'Base: margen objetivo × crecimiento 2–5', 'Crecimiento anual años 2–5, %', 'Margen operativo objetivo, %', (2, 2)),
     'Fuente: motor JMR V2 (cada celda recalcula el DCF completo). Centro = valor Base USD %s. Elaboración JMR.' % n(vb))
rs = [0.08537, 0.10, 0.12, 0.14, 0.16]; cs = [SC['base']*f for f in (0.667, 0.833, 1, 1.167, 1.333)]
json.dump({'price': PX, 'probes': {}, 'grids': {'S': {'rk': 'roicTerminal', 'ck': 'salesToCapital1to5', 'rows': rs, 'cols': cs, 'tie': True}}}, open(W/'amzn_s.json', 'w'))
subprocess.run(['node', str(W/'c2.mjs'), T, str(W/'amzn_s.json'), str(W/'amzn_s_out.json')], cwd=W, check=True, capture_output=True)
Sg = json.load(open(W/'amzn_s_out.json'))['new']['grids']['S']
pair(I/'sensibilidades2-r2.png', (Wg['m'], [pct(x) for x in Wg['rows']], [pct(x, 1) for x in Wg['cols']], 'Base: WACC inicial × g (USD/acción)', 'g terminal, %', 'WACC inicial, %', (2, 2)),
     (Sg['m'], [pct(x, 1) for x in rs], [n(x, 2) for x in cs], 'Base: ROIC terminal × ventas/capital', 'Ventas/capital (años 1–10)', 'ROIC terminal, %', (1, 2)),
     'Fuente: motor JMR V2. En la segunda matriz el Base es ROIC 10 %% y ventas/capital %s (número actual, ambos tramos). Elaboración JMR.' % sc('base'))
fig, ax = plt.subplots(figsize=(9.0, 4.4), dpi=150)
labs = [l for l, _ in ST][::-1]; vals = [x for _, x in ST][::-1]
ax.barh(labs, vals, color=['#b5554b'] + ['#a8c3d3']*6 + ['#5b8baa'], height=0.6)
for i, x in enumerate(vals): ax.text(x + 3, i, n(x, 0), va='center', fontsize=10)
ax.axvline(PX, color='#c4a282', ls='--', lw=1.3); ax.text(PX + 2, len(vals) - 0.6, 'Precio', color='#c4a282', fontsize=10)
ax.set_xlabel('USD por acción'); sty(ax); FUENTE(fig, 'Fuente: motor JMR V2. Pruebas ilustrativas NO oficiales, sin probabilidad, que no modifican el valor publicado. Elaboración JMR.')
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(I/'estres-r2.png'); plt.close(fig)
fig, ax = plt.subplots(figsize=(8.3, 3.9), dpi=150); x = np.arange(3); wdt = 0.34
bs = [13, 17, 13]; rq = [100*im['growth2to5'], 100*im['marginTarget'], 100*g21]
ax.bar(x - wdt/2, bs, wdt, color='#a8c3d3', label='Supuesto Base'); ax.bar(x + wdt/2, rq, wdt, color='#1d3449', label='Requerido para USD 257,37')
for i in range(3): ax.text(i - wdt/2, bs[i] + 0.4, n(bs[i], 0) + ' %', ha='center'); ax.text(i + wdt/2, rq[i] + 0.4, n(rq[i], 1) + ' %', ha='center')
ax.set_xticks(x); ax.set_xticklabels(['Crecimiento 2–5\n(margen 17 %)', 'Margen objetivo\n(crecimiento 13 %)', 'Crecimiento 2–5\n(margen 21 %)']); ax.set_ylabel('%'); ax.legend(frameon=False, loc='upper right'); sty(ax)
FUENTE(fig, 'Fuente: motor JMR V2 (resolución numérica con el resto de supuestos del Base). Elaboración JMR.'); fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(I/'inversa-r2.png'); plt.close(fig)
ev, debt, cash, noop = D['base']['ev']/1000, -205, 56, 303
fig, ax = plt.subplots(figsize=(8.6, 4.2), dpi=150)
eq = D['base']['equity']/1000; steps = [('Valor de las\noperaciones', 0, ev, '#1d3449', ev), ('− Deuda y\narrendamientos', ev + debt, -debt, '#b5554b', debt), ('+ Efectivo', ev + debt, cash, '#4c8c6a', cash), ('+ Activos no\noperativos', ev + debt + cash, noop, '#4c8c6a', noop), ('Patrimonio\n(USD %s/acc.)' % n(vb), 0, eq, '#5b8baa', eq)]
for i, (l, b0, h, col, lab_) in enumerate(steps): ax.bar(i, h, bottom=b0, color=col, width=0.55); ax.text(i, b0 + h + 20, n(lab_, 0), ha='center', fontsize=10)
ax.set_xticks(range(5)); ax.set_xticklabels([s_[0] for s_ in steps]); ax.set_ylabel('mil M USD'); sty(ax)
FUENTE(fig, 'Fuente: libro oficial (hoja Valuation output) y 10-Q 3T26. Acciones diluidas: 10.929 M. Elaboración JMR.'); fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(I/'puente-r2.png'); plt.close(fig)
for f in ('valor_vs_precio', 'sensibilidades', 'sensibilidades2', 'estres', 'inversa', 'puente'): r(f'/AMZN/{f}.png', f'/AMZN/{f}-r2.png')
r('WACC inicial × g y ROIC terminal × ventas/capital.', 'WACC inicial × g y ROIC terminal × ventas/capital (ambos tramos).')
anclas = {s: {'1a5': 'Empresa actual', '6a10': 'Empresa actual', 'factor': f, 'valor': SC[s]} for s, f in [('conservador', 0.8), ('base', 1), ('optimista', 1.3)]}
anclas.update({'anclas': {'Empresa actual': 1.0460, 'Empresa marginal (último año)': 0.2309, 'Empresa marginal (3 años)': 0.4013, 'Industria EE. UU. (promedio)': 3.5063, 'Industria global (promedio)': 2.7255, 'Global 1.er cuartil': 0.6763, 'Global mediana': 1.7213, 'Global 3.er cuartil': 3.1833},
               'industria': 'Retail (General)', 'fuente': "'JMR Escenarios'!A33:G48 (fórmulas sobre 'Input sheet'!I27:N28)"})
nota = 'R2 (22-nov-2026): ventas/capital por fórmula desde el número actual de la empresa (I27 = 1,05×, ambos tramos; Conservador ×0,8 y Optimista ×1,3). Libro convertido a Google Sheets desde el .xlsx R1 sin otros cambios. Paridad libro–motor 0,0000 %.'
just = 'Ancla de Damodaran por fórmula: número actual de Amazon (I27 = 1,05×) en los años 1–5 y 6–10 (B32 = B31). La ola de capex en IA deja el marginal en 0,23×; el promedio global de Retail (General) (2,73×, valor por defecto del Ginzu) corresponde a minoristas sin nube. Damodaran usó 2,0× en feb-2024, cerca del marginal de entonces. Conservador 0,84× y Optimista 1,36× conservan la proporción de R1 (0,8/1,0/1,3); R1 subía a 1,6× en los años 6–10 sin ancla.'
expediente(e, T, REV, SHEET, c, anclas, nota, just_sc=just, warn='R2 (22-nov-2026): ventas/capital Base 1,0×/1,6× → 1,05× (número actual, ambos tramos); valor Base de US$196,96 a US$' + n(vb) + '.')
a['blocks'] = B; a['revision'] = REV
for k in ('pdf', 'informePdf'):
    if isinstance(a.get(k), str): a[k] = f'jmr-v2/informes/{T}/{REV}_INFORME_FUNDAMENTAL.pdf'
    elif isinstance(a.get(k), dict): a[k] = {**a[k], 'ruta': f'jmr-v2/informes/{T}/{REV}_INFORME_FUNDAMENTAL.pdf'}
a['updatedAt'] = '2026-11-22'
a['revisionMetodo'] = {'fecha': '2026-11-22', 'anterior': 'AMZN-V2-LTM20260930-R1', 'alcance': 'Ventas/capital por anclas de Damodaran; cifras de valoración, trayectorias, estrés, sensibilidades y figuras actualizadas.'}
save(T, e, a); print('OK', n(vb), len(r.log), 'noop', n(NOOP), 'g21', g21)
