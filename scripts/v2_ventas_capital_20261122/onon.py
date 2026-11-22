from comun import *
import numpy as np
T, REV, SHEET = 'ONON', 'ONON-V2-LTM20260930-R2', '1MTw9sJGSD2Ab5ffktD5Wsm6v3lZIh4x5GVo-PUAMK1c'
c = json.load(open(W/'calc.json'))[T]; G = json.load(open(W/'onon_g.json'))['new']; pr = G['pr']
e, a = load(T); B = a['blocks']; cortar_just(B); r = Rep(B)
vc, vb, vo = c['esc']['conservador'], c['esc']['base'], c['esc']['optimista']; mos = vb*0.65; PX = 27.28; FX = 0.84129; D = c['det']; S3 = ('conservador', 'base', 'optimista')
tv = {s: D[s]['pvTerminal']/D[s]['ev'] for s in S3}; SC = c['sc']; sc = lambda s, d=2: n(SC[s], d) + '×'; u = lambda x, d=1: n(x/FX, d)
r('LTM20260930-R1', 'LTM20260930-R2'); r('libro R1', 'libro R2')
# valores
r('39,87 / 72,77 / 106,73', '%s / %s / %s' % (n(vc), n(vb), n(vo)), cnt=2); r('USD 47,4 / 86,5 / 126,9', 'USD %s / %s / %s' % (u(vc), u(vb), u(vo)), cnt=2)
r('CHF 39,87 (USD 47,4)', 'CHF %s (USD %s)' % (n(vc), u(vc))); r('CHF 72,77 (USD 86,5)', 'CHF %s (USD %s)' % (n(vb), u(vb))); r('CHF 106,73 (USD 126,9)', 'CHF %s (USD %s)' % (n(vo), u(vo))); r('CHF 47,30 (USD 56,2)', 'CHF %s (USD %s)' % (n(mos), u(mos)))
r('+167 %', '+%s %%' % n(100*(vb/PX-1), 0))
r('CHF 72,8 por acción (USD 86,5)', 'CHF %s por acción (USD %s)' % (n(vb, 1), u(vb)), cnt=2); r('CHF 47,3 (USD 56,2)', 'CHF %s (USD %s)' % (n(mos, 1), u(mos)))
r('vale 72,8 CHF por acción', 'vale %s CHF por acción' % n(vb, 1)); r('CHF 47,3', 'CHF ' + n(mos, 1)); r('Base CHF 72,8', 'Base CHF ' + n(vb, 1)); r('(CHF 39,9;', '(CHF %s;' % n(vc, 1)); r('USD 47,4) supera al precio en 46 %', 'USD %s) supera al precio en %s %%' % (u(vc), n(100*(vc/PX-1), 0)))
r('en 73 %', 'en %s %%' % n(100*(mos/PX-1), 0), keys=['conclusiones'])
r('2,7 veces', n(vb/PX, 1) + ' veces', cnt=8); r('sino 1,5–1,8 veces', 'sino %s–%s veces' % (n(G['G1'][4][2]/PX, 1), n(G['G1'][3][3]/PX, 1)))
r('Base 72,7673 CHF', 'Base %s CHF' % n(vb, 4))
# costo de capital y combinaciones
g1 = G['G1']; lo, hi = min(g1[3][2], g1[3][3], g1[4][2], g1[4][3]), max(g1[3][2], g1[3][3], g1[4][2], g1[4][3])
r('CHF 40–48', 'CHF %s–%s' % (n(lo, 0), n(hi, 0)), cnt=5)
r('sería CHF 26,6, equivalente al precio de mercado', 'sería CHF %s, algo por debajo del precio de mercado' % n(g1[5][0], 1)); r('(CHF 26,6)', '(CHF %s)' % n(g1[5][0], 1))
r('baja el Base de CHF 73 a 36; con g de 2 % baja a CHF 41', 'baja el Base de CHF %s a %s; con g de 2 %% baja a CHF %s' % (n(vb, 0), n(g1[3][0], 0), n(g1[3][2], 0)))
g3 = G['G3']; r('(CHF 70–74)', '(CHF %s–%s)' % (n(g3[0][2], 0), n(g3[4][2], 0)))
r('25,1', n(pr['c2'], 1), cnt=4)
r('en CHF %s (−66 %%), 8 %% menos que el precio' % n(pr['c2'], 1), 'en CHF %s (−%s %%), %s %% menos que el precio' % (n(pr['c2'], 1), n(100*(1-pr['c2']/vb), 0), n(100*(1-pr['c2']/PX), 0)))
r('el Base en CHF 38,2 (−48 %)', 'el Base en CHF %s (−%s %%)' % (n(pr['c1'], 1), n(100*(1-pr['c1']/vb), 0)))
r('baja a CHF 50 (−31 %)', 'baja a CHF %s (−%s %%)' % (n(pr['g5'], 0), n(100*(1-pr['g5']/vb), 0))); r('el valor es CHF 54 (−25 %)', 'el valor es CHF %s (−%s %%)' % (n(pr['m12'], 0), n(100*(1-pr['m12']/vb), 0)))
r('deja el Base en CHF 46 (−37 %)', 'deja el Base en CHF %s (−%s %%)' % (n(pr['usd'], 0), n(100*(1-pr['usd']/vb), 0)))
for o, k in [('CHF 50,3', 'g5'), ('CHF 54,5', 'm12'), ('CHF 67,0', 'roicW'), ('CHF 66,0', 'g0')]: r(o, 'CHF ' + n(pr[k], 1))
r('CHF 45,9', 'CHF ' + n(pr['usd'], 1), cnt=2); r('68 % sobre el precio', '%s %% sobre el precio' % n(100*(pr['usd']/PX-1), 0))
# peso del terminal
TVB = n(100*tv['base'], 0) + ' %'
for k in ('perfil', 'introduccion', 'riesgos', 'tesis_contraria', 'conclusiones'):
    if '79 %' in B[k]: B[k] = B[k].replace('79 %', TVB)
# tablas de valoración
swap_row(B, 'valoracion', 'Valor presente de los flujos de 10 años', [n(D[s]['sumPV'], 0) for s in S3]); swap_row(B, 'valoracion', 'Valor de las operaciones<', [n(D[s]['ev'], 0) for s in S3]) if False else None
v = B['valoracion']
for s_old, s_new in [('<td class="">Valor de las operaciones</td><td class="num">12.814</td><td class="num">23.885</td><td class="num">35.316</td>', '<td class="">Valor de las operaciones</td>' + ''.join('<td class="num">%s</td>' % n(D[s]['ev'], 0) for s in S3)),
                     ('<td class="">Valor del patrimonio</td><td class="num">13.420</td><td class="num">24.492</td><td class="num">35.922</td>', '<td class="">Valor del patrimonio</td>' + ''.join('<td class="num">%s</td>' % n(D[s]['equity'], 0) for s in S3))]:
    assert s_old in v, s_old[:50]; v = v.replace(s_old, s_new)
B['valoracion'] = v
swap_row(B, 'valoracion', 'Valor por acción (CHF)', [n(c['esc'][s]) for s in S3]); swap_row(B, 'valoracion', 'Valor por acción (USD, ÷ 0,84129)', [u(c['esc'][s]) for s in S3])
swap_row(B, 'valoracion', 'Brecha valor / precio', ['+%s %%' % n(100*(c['esc'][s]/PX-1), 0) for s in S3])
swap_row(B, 'valoracion', 'Peso del valor terminal en el valor de las operaciones', [n(100*tv[s], 0) + ' %' for s in S3])
swap_row(B, 'valoracion', 'Valor de las operaciones / ventas LTM (×)', [n(D[s]['ev']/3357.4, 1) + '×' for s in S3]); swap_row(B, 'valoracion', 'Valor de las operaciones / EBIT LTM (×)', [n(D[s]['ev']/514.4, 1) + '×' for s in S3])
r('valor de las operaciones CHF 23.885 M = PV de los flujos de 10 años (CHF 5.018 M, 21 %) + PV del valor terminal (CHF 18.868 M, 79 %)', 'valor de las operaciones CHF %s M = PV de los flujos de 10 años (CHF %s M, %s %%) + PV del valor terminal (CHF 18.868 M, %s)' % (n(D['base']['ev'], 0), n(D['base']['sumPV'], 0), n(100*(1-tv['base']), 0), TVB))
r('patrimonio de CHF 24.492 M', 'patrimonio de CHF %s M' % n(D['base']['equity'], 0))
r('(EV de CHF 23.885 M / EBIT LTM de 514 M = 46×', '(EV de CHF %s M / EBIT LTM de 514 M = %s×' % (n(D['base']['ev'], 0), n(D['base']['ev']/514.4, 0))); r('EV/ventas 7,1×)', 'EV/ventas %s×)' % n(D['base']['ev']/3357.4, 1))
# supuestos: ventas/capital y trayectoria del Base
v = B['supuestos']
for s, old in [('Conservador', '2,0×'), ('Base', '3,0×'), ('Optimista', '4,0×')]:
    i = v.find('<td class="">%s</td>' % s, v.find('Sales/capital')); j = v.find(old, i); assert 0 < j - i < 400, s; v = v[:j] + sc(s.lower()) + v[j+len(old):]
B['supuestos'] = v
r('Ventas sobre capital invertido: 2,1× hoy; el Base usa 3,0× por el crecimiento con capital de trabajo ligero.', 'Ventas sobre capital invertido: %s hoy, y ese es el Base (ancla «Empresa actual» de Damodaran por fórmula, igual en los dos tramos); coincide con el promedio global del calzado (2,11×, valor por defecto del Ginzu) y queda bajo el tercer cuartil (2,41×). R1 usaba 3,0×, extrapolando el 4,8× incremental de 2022–2025, que no se repite si el plan exige tiendas propias e inventario.' % sc('base'))
Y = YEARS[T]['new']['base']['years']; v = B['supuestos']; i = v.find('<th class="num">VP del FCFF</th>'); j = v.find('</table>', i); seg = v[i:j]
for y in Y:
    a0 = seg.find('<tr><td class="">%d</td>' % y['year']); b0 = seg.find('</tr>', a0); cells = re.findall(r'<td class="num">([^<]*)</td>', seg[a0:b0])
    cells[5:8] = [n(y['reinvestment'], 0), n(y['fcff'], 0), n(y['pvFcff'], 0)]
    seg = seg[:a0] + '<tr><td class="">%d</td>' % y['year'] + ''.join('<td class="num">%s</td>' % x for x in cells) + seg[b0:]
B['supuestos'] = v[:i] + seg + v[j:]
# figuras (estilo ONON)
I = IMG/T; plt.rcParams.update({'font.family': 'DejaVu Sans'})
NAV, STL, LBL, RED, TANc = '#1d3449', '#5b8baa', '#a8c3d3', '#b5554b', '#c4a282'
foot = 'Fuente: SEC EDGAR (20-F FY2025, 6-K 3T26, XBRL IFRS), libro %s; elaboración JMR. CHF millones.' % REV
def st(ax):
    for s_ in ('top', 'right'): ax.spines[s_].set_visible(False)
fig, ax = plt.subplots(figsize=(11, 3.7), dpi=150)
vals = [vc, vb, vo]; ax.bar(['Conservador', 'Base', 'Optimista'], vals, color=[LBL, NAV, STL], width=0.55)
for i, x in enumerate(vals): ax.text(i, x + 2, 'CHF %s  |  USD %s' % (n(x, 1), u(x)), ha='center', fontweight='bold', fontsize=10)
ax.axhline(PX, color=RED, ls='--', lw=1.6, label='Precio de mercado: CHF 27,28 (USD 32,43)'); ax.axhline(mos, color=TANc, ls=':', lw=1.8, label='Precio con MOS 35 %% sobre el Base: CHF %s' % n(mos, 1))
ax.set_ylim(0, vo*1.25); ax.set_ylabel('CHF por acción'); ax.legend(frameon=False, loc='upper left', fontsize=9); ax.set_title('Valor intrínseco por acción frente al precio de mercado', fontweight='bold'); st(ax)
fig.text(0.01, 0.02, 'Libro y motor V2 coinciden (< 0,001 %). USD = CHF ÷ 0,84129 (18-nov-2026). ' + foot, color='#7d8b96', fontsize=8); fig.subplots_adjust(left=0.08, right=0.66, bottom=0.18, top=0.9); fig.savefig(I/'valor_vs_precio-r2.png'); plt.close(fig)
fig, axs = plt.subplots(1, 3, figsize=(13, 3.6), dpi=150)
def hm(ax, M, rl, cl, tt, xl, yl, ctr, d=0):
    M = np.array(M); ax.imshow(M, cmap='Blues', aspect='auto', vmin=M.min()*0.9, vmax=M.max()*1.6)
    for i_ in range(M.shape[0]):
        for j_ in range(M.shape[1]): ax.text(j_, i_, n(M[i_, j_], d), ha='center', va='center', fontsize=10, fontweight='bold' if (i_, j_) == ctr else 'normal', color='#1d3449')
    ax.set_xticks(range(len(cl))); ax.set_xticklabels(cl); ax.set_yticks(range(len(rl))); ax.set_yticklabels(rl); ax.set_title(tt, fontweight='bold', fontsize=11); ax.set_xlabel(xl); ax.set_ylabel(yl)
    for s_ in ax.spines.values(): s_.set_visible(False)
A = G['axes']
hm(axs[0], G['G1'], [n(100*x, 1) + ' %' for x in A['wis']], [n(100*x, 1) + ' %' for x in A['gs']], 'Base: WACC inicial × g terminal', 'g terminal', 'WACC inicial', (0, 0))
hm(axs[1], G['G2'], [n(100*x, 0) + ' %' for x in A['mts']], [n(100*x, 0) + ' %' for x in A['g25']], 'Base: crecimiento 2–5 × margen objetivo', 'crecimiento compuesto', 'margen objetivo', (2, 2))
hm(axs[2], G['G3'], [n(100*x, 0) + ' %' for x in A['rs']], [n(x, 2) + '×' for x in A['scs']], 'Base: ROIC terminal × ventas/capital', 'ventas/capital (ambos tramos)', 'ROIC terminal', (2, 2))
fig.text(0.01, 0.02, 'CHF por acción; el WACC terminal se ajusta con el inicial (inicial − 0,82 pp, con piso en g + 1,2 pp). Negrita = Base.\n' + foot, color='#7d8b96', fontsize=8); fig.tight_layout(rect=(0, 0.1, 1, 1)); fig.savefig(I/'sensibilidades-r2.png'); plt.close(fig)
fig, ax = plt.subplots(figsize=(13, 3.7), dpi=150)
items = [('margen objetivo 12 %', pr['m12']), ('crecimiento 2–5 = 5 %', pr['g5']), ('ROIC terminal = WACC (3,97 %)', pr['roicW']), ('WACC 8 % / WACC terminal 6,5 % / g 2 %', pr['usd']), ('combinado: crecimiento 5 % y margen 12 %', pr['c1']), ('combinado + WACC 8 %, terminal 6,5 %, g 2 %', pr['c2']), ('g terminal 0 %', pr['g0'])]
yy = list(range(len(items)))[::-1]; ax.barh(yy, [x for _, x in items], color=STL, height=0.8)
for y_, (_, x) in zip(yy, items): ax.text(x + 0.5, y_, '%s  (%s %%)' % (n(x, 1), n(100*(x/vb-1), 0)), va='center', fontsize=9)
ax.axvline(PX, color=RED, ls='--', lw=1.6); ax.axvline(vb, color=NAV, lw=1.8); ax.set_yticks(yy); ax.set_yticklabels([l for l, _ in items], fontsize=9); ax.set_xlim(0, vb*1.3)
ax.set_xlabel('CHF por acción (línea azul: Base %s; línea roja: precio 27,3)' % n(vb, 1)); ax.set_title('Pruebas de estrés ilustrativas sobre el Base (no oficiales)', fontweight='bold'); st(ax)
fig.text(0.2, 0.02, foot, color='#7d8b96', fontsize=8); fig.tight_layout(rect=(0, 0.05, 1, 1)); fig.savefig(I/'estres-r2.png'); plt.close(fig)
fig, ax = plt.subplots(figsize=(13, 3.7), dpi=150); M = np.array(G['PI'])
ax.imshow(M, cmap='RdYlBu', aspect='auto', vmin=PX - 12, vmax=PX + 30, alpha=0.6)
for i_ in range(M.shape[0]):
    for j_ in range(M.shape[1]): ax.text(j_, i_, n(M[i_, j_], 0), ha='center', va='center', fontsize=10, color=RED if M[i_, j_] <= PX else '#1d3449', fontweight='bold' if abs(M[i_, j_] - PX) < 3 or (i_, j_) == (3, 5) else 'normal')
ax.set_xticks(range(len(A['pg']))); ax.set_xticklabels([n(100*x, 0) + ' %' for x in A['pg']]); ax.set_yticks(range(len(A['pm']))); ax.set_yticklabels([n(100*x, 0) + ' %' for x in A['pm']])
ax.set_xlabel('crecimiento compuesto años 2–5'); ax.set_ylabel('margen operativo objetivo'); ax.set_title('Valor por acción (CHF) con WACC 8 %, terminal 6,5 %, g 2 %', fontweight='bold')
for s_ in ax.spines.values(): s_.set_visible(False)
fig.text(0.01, 0.02, 'Rojo = valor igual o inferior al precio de mercado (CHF 27,28). Base: crecimiento 13 %%, margen 16 %% → CHF %s. ' % n(pr['usd'], 1) + foot, color='#7d8b96', fontsize=8); fig.subplots_adjust(left=0.08, right=0.56, bottom=0.2, top=0.88); fig.savefig(I/'precio_implicito-r2.png'); plt.close(fig)
for f in ('valor_vs_precio', 'sensibilidades', 'estres', 'precio_implicito'): r(f'/ONON/{f}.png', f'/ONON/{f}-r2.png')
r('ROIC terminal × sales/capital (CHF por acción)', 'ROIC terminal × ventas/capital (CHF por acción)', cnt=None)
anclas = {s: {'1a5': 'Empresa actual', '6a10': 'Empresa actual', 'factor': f, 'valor': SC[s]} for s, f in [('conservador', 0.6667), ('base', 1), ('optimista', 1.3333)]}
anclas.update({'anclas': {'Empresa actual': 2.1392, 'Empresa marginal (último año)': 0.7885, 'Empresa marginal (3 años)': 2.0577, 'Industria EE. UU. (promedio)': 2.6221, 'Industria global (promedio)': 2.1149, 'Global 1.er cuartil': 1.0041, 'Global mediana': 1.5694, 'Global 3.er cuartil': 2.4146},
               'industria': 'Shoe', 'fuente': "'JMR Escenarios'!A33:G48 (fórmulas sobre 'Input sheet'!I27:N28)"})
nota = 'R2 (22-nov-2026): ventas/capital por fórmula desde el número actual de la empresa (I27 = 2,14×, ambos tramos; Conservador ×0,667 y Optimista ×1,333). Sin otros cambios de supuestos. Paridad libro–motor 0,0000 %.'
just = 'Ancla de Damodaran por fórmula: número actual de On (I27 = 2,14×) en los años 1–5 y 6–10 (B32 = B31); coincide con el promedio global del calzado (K27 = 2,11×, valor por defecto del Ginzu) y queda bajo el tercer cuartil (2,41×). El 4,8× incremental de 2022–2025 no se extrapola porque el plan exige tiendas propias e inventario. Conservador 1,43× y Optimista 2,85× conservan la proporción de R1 (2,0/3,0/4,0).'
expediente(e, T, REV, SHEET, c, anclas, nota, just_sc=just, warn='R2 (22-nov-2026): ventas/capital 3,0× → 2,14× (número actual, ambos tramos); valor Base de CHF 72,77 a CHF ' + n(vb) + '.')
a['blocks'] = B; a['revision'] = REV
for k in ('pdf', 'informePdf'):
    if isinstance(a.get(k), str): a[k] = f'jmr-v2/informes/{T}/{REV}_INFORME_FUNDAMENTAL.pdf'
    elif isinstance(a.get(k), dict): a[k] = {**a[k], 'ruta': f'jmr-v2/informes/{T}/{REV}_INFORME_FUNDAMENTAL.pdf'}
a['updatedAt'] = '2026-11-22'
a['revisionMetodo'] = {'fecha': '2026-11-22', 'anterior': 'ONON-V2-LTM20260930-R1', 'alcance': 'Ventas/capital por anclas de Damodaran; cifras de valoración, trayectoria, estrés, sensibilidades y figuras actualizadas.'}
save(T, e, a); print('OK', n(vb), len(r.log), 'G1 range', lo, hi)
