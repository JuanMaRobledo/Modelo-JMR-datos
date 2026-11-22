"""ADBE R2: tasa libre 5,15 % y prima madura 3,387 % (convención de la biblioteca). Expediente, análisis y figuras."""
import json, sys, re, copy, pathlib
sys.path.insert(0, '/tmp/claude-0/-home-user/02bdd347-b8be-5ac5-b2fc-27257db31770/scratchpad/gen'); from figtabla import tabla
A = pathlib.Path(sys.argv[1]); ORIG = pathlib.Path(sys.argv[2]); OUT = pathlib.Path(sys.argv[3])
DATA = pathlib.Path('/home/user/Modelo-JMR-datos/jmr-v2'); IMGD = DATA/'imagenes/ADBE'
REV, ANT = 'ADBE-V2-LTM20260828-R2', 'ADBE_JMR_V2_20261116_R1'
SHEET = '1gSI-IW4LMsk3eQbTTaiGonWQW1ENH20oYSJZ855l3Hk'; SHA = '163e9296edd8fffec856573bcf828cd0f37fdf81340a8430382b1613e87aea2c'
WI, WT = 0.10242696089998787, 0.08537; PX = 235.55
r1 = json.load(open(ORIG/'empresas/ADBE.json')); a1 = json.load(open(ORIG/'analisis/ADBE.json')); c = json.load(open(A/'calc.json'))
def n(v, d=2): return f'{v:,.{d}f}'.replace(',', '@').replace('.', ',').replace('@', '.')
E = c['esc']; D = c['det']; vb, vc, vo = E['base'], E['conservador'], E['optimista']; mos = vb*0.65; NI = 7284; SH = 401.4
e = copy.deepcopy(r1)
for s in e['assumptions']: e['assumptions'][s]['waccInitial'] = WI; e['assumptions'][s]['waccTerminal'] = WT
e['libro'].update({'id': f'{REV}_VALORACION', 'sha256': SHA, 'valores': dict(E), 'url': f'https://docs.google.com/spreadsheets/d/{SHEET}/edit', 'googleSheetId': SHEET, 'contratoVersion': '1.5.6',
    'costoCapital': {'formulas': True, 'tasaLibre': 0.0515, 'primaMadura': 0.03387, 'waccInicial': WI, 'waccTerminal': WT},
    'cambiosR2': "Copia de R1 con dos entradas cambiadas: 'JMR Escenarios'!C17 (tasa libre 5,12 % → 5,15 %) y 'Country equity risk premiums'!B1 (prima madura 4,41 % → 3,387 %). WACC inicial 11,47 % → 10,24 % y terminal 9,53 % → 8,537 % por fórmula. Paridad libro–motor 0,000 %.",
    'excelSha256': SHA, 'excelPendiente': 'Exportación .xlsx registrada por huella; el libro oficial es la Google Sheet.'})
e['documentLinks'] = {**r1.get('documentLinks', {}), 'workbook': f'https://docs.google.com/spreadsheets/d/{SHEET}/edit', 'workbookGoogleSheets': f'https://docs.google.com/spreadsheets/d/{SHEET}/edit', 'workbookR1': r1['libro']['url']}
e['revision'] = {'id': REV, 'anterior': ANT, 'nota': 'R2 (22-nov-2026): homologa tasa libre (5,15 %) y prima madura (3,387 %, Damodaran nov-2026) con el resto de la biblioteca. Sin otros cambios de supuestos.'}
J = e['justificaciones']
J['wacc'] = ('WACC del libro por fórmulas con beta de software de EE. UU. desapalancada 1,25 (reapalancada ~1,309), tasa libre 5,15 % y ERP 4,17 % (prima madura 3,387 % + prima geográfica 0,78 pp por ingresos fuera de EE. UU.), deuda al 5,85 % antes de impuestos y tasa marginal 25 %: WACC inicial 10,24 %.')
J['waccTerminal'] = '8,537 % = tasa libre 5,15 % + prima madura 3,387 %, la misma convención que el resto de la biblioteca (R1 usaba 5,12 % + 4,41 % = 9,53 %).'
e['warnings'] = [w for w in r1.get('warnings', []) if not w.startswith('Corrección pendiente') and '9,53' not in w] + ['R2: WACC homologado con la biblioteca; el valor Base sube de US$359,97 a US$' + n(vb) + '.']
e['estado'] = 'EN_REVISION'
# análisis
blocks = copy.deepcopy(a1['blocks'])
for k in blocks:
    i = blocks[k].find('<div id="justificacion-supuestos'); blocks[k] = blocks[k] if i < 0 else blocks[k][:i]
up = vb/PX-1
SENT = [  # frases completas (regex) → nuevas
 (r'Nuestro valor Base \(US\$360\) queda 53 % sobre el cierre de US\$235,55; el precio coincide con el precio con margen de seguridad \(US\$234\)\.', f'Nuestro valor Base (US${n(vb,0)}) queda {n(100*up,0)} % sobre el cierre de US$235,55; el precio está {n(100*(1-PX/mos),0)} % por debajo del precio con margen de seguridad (US${n(mos,0)}).'),
 (r'El precio equivale a un crecimiento de ~-0,5 % anual en los años 2 a 5, frente a 10 % en el Base, o a un margen operativo final de ~24 %, frente a 38 %\. Es decir, el mercado ya descuenta un escenario peor que nuestro Conservador en crecimiento\.', f'El precio equivale a un crecimiento de ~{n(100*c["gImp"],1)} % anual en los años 2 a 5, frente a 10 % en el Base, o a un margen operativo final de ~{n(100*c["mImp"],0)} %, frente a 38 %. Es decir, el mercado descuenta un escenario peor que nuestro Conservador en crecimiento.'),
 (r'El libro usa un WACC inicial de 11,47 % y terminal de 9,53 % \(tasa libre de 5,12 % más prima madura de 4,41 %\), más alto que el de otras empresas del conjunto\. Con un WACC terminal 1 punto mayor \(10,5 %\), el Base baja de US\$360 a ~US\$322 \(-10 %\)\.', f'El libro R2 usa un WACC inicial de 10,24 % y terminal de 8,54 % (tasa libre de 5,15 % más prima madura de 3,387 %), la misma convención que el resto del conjunto. Con un WACC terminal 1 punto mayor (9,54 %), el Base baja de US${n(vb,0)} a ~US${n(c["wt1"],0)} ({n(100*(c["wt1"]/vb-1),0)} %).'),
 (r'El precio coincide con el precio con margen de seguridad de nuestro modelo \(US\$234\)\.', f'El precio está por debajo del precio con margen de seguridad de nuestro modelo (US${n(mos,0)}).'),
 (r'A US\$236 el precio coincide con el precio con margen de seguridad \(US\$234\): el valor Base supera el precio en 53 %\.', f'A US$236 el precio está por debajo del precio con margen de seguridad (US${n(mos,0)}): el valor Base supera el precio en {n(100*up,0)} %.'),
 (r'una convención distinta a la de otras empresas del conjunto\)', 'la misma convención que el resto del conjunto desde R2)'),
 (r'Valor Base: US\$359,97 por acción, 53 % sobre el cierre de US\$235,55\. El precio con margen de seguridad \(US\$233,98\) coincide con el precio de mercado\.', f'Valor Base: US${n(vb)} por acción, {n(100*up,0)} % sobre el cierre de US$235,55. El precio con margen de seguridad (US${n(mos)}) supera al precio de mercado en {n(100*(mos/PX-1),0)} %.'),
 (r'coincide con el precio con margen de seguridad \(US\$233,98\): la acción cumple el criterio de margen del Modelo JMR\.', f'está {n(100*(1-PX/mos),0)} % por debajo del precio con margen de seguridad (US${n(mos)}): la acción cumple con holgura el criterio de margen del Modelo JMR.'),
 (r'con 7,5 % sube a ~US\$499 y con 11,5 % baja a ~US\$295, todavía por encima del precio; \(2\) incluso con crecimiento de 0 % y margen objetivo de 38 % el valor es ~US\$241, cerca del precio de mercado\.', f'con 7,5 % sube a ~US${n(c["wt75"],0)} y con 11,5 % baja a ~US${n(c["wt115"],0)}, todavía por encima del precio; (2) incluso con crecimiento de 0 % y margen objetivo de 38 % el valor es ~US${n(c["g0"],0)}, por encima del precio de mercado.'),
 (r'el crecimiento de los años 2–5 sería -0,5 % \(Base: 10,0 %\); o el margen objetivo del año 10, 24,2 % \(Base: 38,0 %\); o el WACC terminal, no se alcanza dentro de un rango razonable \(Base: 9,53 %\)\. Variando solo el crecimiento al nivel Conservador \(3,0 %\), el valor sería US\$271,08; variando solo el margen al nivel Conservador \(28,0 %\), US\$270,04\.', f'el crecimiento de los años 2–5 sería {n(100*c["gImp"],1)} % (Base: 10,0 %); o el margen objetivo, {n(100*c["mImp"],1)} % (Base: 38,0 %); o el WACC terminal, {n(100*c["wImp"],1)} % (Base: 8,54 %), fuera de un rango razonable. Variando solo el crecimiento al nivel Conservador (3,0 %), el valor sería US${n(c["gCons"])}; variando solo el margen al nivel Conservador (28,0 %), US${n(c["mCons"])}.'),
 (r'El libro usa tasa libre de 5,12 % y prima madura de 4,41 %, una convención distinta a la del resto del conjunto \(5,15 % y 3,387 %\)\.', 'R2 homologa la tasa libre (5,15 %) y la prima madura (3,387 %) con el resto del conjunto; R1 usaba R1RF y R1ERP (Base R1BASE).'),
 (r'el Conservador \(US\$170\) queda 28 % por debajo del precio, mientras que el Base queda 53 % por encima', f'el Conservador (US${n(vc,0)}) queda {n(100*(1-vc/PX),0)} % por debajo del precio, mientras que el Base queda {n(100*up,0)} % por encima'),
 (r'el precio coincide con el precio con margen de seguridad\.', 'el precio está por debajo del precio con margen de seguridad.'),
 (r'Base: US\$360 · \+53 % vs\. precio', f'Base: US${n(vb,0)} · +{n(100*up,0)} % vs. precio'),
 (r'Conservador: US\$170 · -28 % vs\. precio', f'Conservador: US${n(vc,0)} · {n(100*(vc/PX-1),0)} % vs. precio'),
 (r'Optimista: US\$462 · \+96 % vs\. precio', f'Optimista: US${n(vo,0)} · +{n(100*(vo/PX-1),0)} % vs. precio')]
TOK = [('US$359,97', f'US${n(vb)}'), ('US$170,33', f'US${n(vc)}'), ('US$461,51', f'US${n(vo)}'), ('US$233,98', f'US${n(mos)}'), ('0,65 × 359,97', f'0,65 × {n(vb)}'),
       ('US$360', f'US${n(vb,0)}'), ('US$234', f'US${n(mos,0)}'), ('11,47 % → 9,53 %', '10,24 % → 8,54 %'), ('11,47 %', '10,24 %'), ('9,53 %', '8,54 %'), ('5,12 %', '5,15 %'), ('4,41 %', '3,387 %'),
       ('Convención del libro de ADBE (10 años: 5,10 % al 17-nov)', 'Convención de la biblioteca (10 años: 5,10 % al 17-nov)'), ('Convención del libro de ADBE', 'Damodaran, nov-2026 (convención de la biblioteca)')]
hits = 0
for k in blocks:
    for old, new in SENT:
        blocks[k], cnt = re.subn(old, lambda m: new, blocks[k]); hits += cnt
    for old, new in TOK: blocks[k] = blocks[k].replace(old, new)
    blocks[k] = blocks[k].replace('R1BASE', 'US$359,97').replace('R1RF', '5,12 %').replace('R1ERP', '4,41 %')
assert hits >= 15, hits
# tablas del capítulo de valoración
v = blocks['valoracion']
puente = [('61.346', n(D['base']['sumPV'], 0)), ('83.870', n(D['base']['pvTerminal'], 0)), ('145.215', n(D['base']['ev'], 0)), ('144.491', n(D['base']['equity'], 0))]
for o, nn in puente: assert o in v, o; v = v.replace(o, nn, 1)
for o, nn in [('-27,7 %', f'{n(100*(vc/PX-1),1)} %'), ('+52,8 %', f'+{n(100*up,1)} %'), ('+95,9 %', f'+{n(100*(vo/PX-1),1)} %'), ('69.093', n(D['conservador']['ev'], 0)), ('185.975', n(D['optimista']['ev'], 0)),
              ('44,6 %', f'{n(100*D["conservador"]["pvTerminal"]/D["conservador"]["ev"],1)} %'), ('57,8 %', f'{n(100*D["base"]["pvTerminal"]/D["base"]["ev"],1)} %'), ('60,1 %', f'{n(100*D["optimista"]["pvTerminal"]/D["optimista"]["ev"],1)} %'),
              ('9,4×', f'{n(vc*SH/NI,1)}×'), ('19,8×', f'{n(vb*SH/NI,1)}×'), ('25,4×', f'{n(vo*SH/NI,1)}×')]:
    assert o in v, o; v = v.replace(o, nn, 1)
for f_ in ['fig-08', 'fig-09', 'fig-10']: v = v.replace(f'{f_}.png', f'{f_}-r2.png')
blocks['valoracion'] = v
blocks['supuestos'] = blocks['supuestos'].replace('El valor terminal pesa 58 % del valor operativo Base.', f'El valor terminal pesa {n(100*c["tv"],0)} % del valor operativo Base.')
a2 = {**a1, 'revision': REV, 'blocks': blocks}; a2.pop('justificacionSupuestos', None)
for k in ('pdf', 'informePdf'):
    if k in a2: a2[k] = f'jmr-v2/informes/ADBE/{REV}_INFORME_FUNDAMENTAL.pdf'
a2['revisionMetodo'] = {'fecha': '2026-11-22', 'anterior': ANT, 'alcance': 'WACC homologado (tasa libre y prima madura); cifras de valoración y matrices actualizadas.'}
json.dump(e, open(OUT/'empresas/ADBE.json', 'w'), ensure_ascii=False, indent=1); json.dump(a2, open(OUT/'analisis/ADBE.json', 'w'), ensure_ascii=False, indent=1)
f = c['f08']; tabla(IMGD/'fig-08-r2.png', f['rows'], f['cols'], f['m'], PX)
f = c['f09']; tabla(IMGD/'fig-09-r2.png', f['rows'], f['cols'], f['m'], PX, rfmt=lambda r: n(100*r, 1)+' %')
f = c['f10']; tabla(IMGD/'fig-10-r2.png', f['rows'], f['cols'], f['m'], PX, rfmt=lambda r: n(100*r, 1)+' %')
print('OK', n(vb), 'sustituciones', hits)
