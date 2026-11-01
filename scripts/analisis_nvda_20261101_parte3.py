# -*- coding: utf-8 -*-
"""Nivel 2 (12 apartados) y ensamblado del análisis de NVDA (revisión NVDA-20261101-A12-R1)."""
import json, re
from analisis_nvda_20261101_parte2 import *

def h2(i, t): return f'<h2 id="jmr-n2-{i}">{i}. {t}</h2>'
def ul(items): return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'
mat = lambda m: [[n(v, 2) for v in row] for row in m['values']]

def n2_1():
    rows = [[yrs[i], n(rev[i]), n(gp[i]), n(rd[i]), n(IS[8][1+i]), n(ebit[i]), n(IS[27][1+i]), pc(IS[28][1+i],1) if isinstance(IS[28][1+i],(int,float)) else 'N/D', n(ni[i]), n(IS[25][1+i])] for i in range(11)]
    cf_rows = [[yrs[i], n(ocf[i]), n(-capex[i]), n(fcf[i]), n(sbc[i]), n(buy[i]), n(div[i])] for i in range(11)]
    return (h2(1, 'Históricos y base de datos') +
      P('Series de la hoja de trabajo (millones de US$ salvo acciones en millones y tasas). Diez años fiscales más los doce meses a 26-jul-2026 (LTM). El LTM de ingresos de la hoja (302.970) difiere en 1 millón de la suma aritmética de trimestres redondeados (302.969).') +
      table(['Año', 'Ingresos', 'Utilidad bruta', 'I+D', 'SG&A', 'EBIT', 'EBITDA', 'Tasa efectiva', 'Utilidad neta', 'Acciones diluidas (prom.)'], rows, 'Estado de resultados.') +
      table(['Año', 'Flujo operativo', 'Capex', 'FCF', 'Compensación en acciones', 'Recompras', 'Dividendos'], cf_rows, 'Flujo de caja.'))

def n2_2():
    inp = {r[0]: r for r in D['input'] if r}
    def g(k): 
        for kk, r in inp.items():
            if str(kk).startswith(k): return r[1]
    rows = [['Ingresos LTM', n(float(g('Revenues'))), '[Dato] 10-K FY2026 + 10-Q T2 FY27 (LTM = FY26 + 1S27 − 1S26)'],
            ['EBIT LTM (GAAP)', n(float(g('Operating income or EBIT'))), '[Dato] ídem'],
            ['I+D LTM capitalizada (vida 3 años)', '23.592', '[Dato] gasto; [Juicio] vida útil de 3 años'],
            ['Deuda total (con arrendamientos GAAP)', n(float(g('Book value of debt'))), '[Dato] 10-Q: 1.000 + 32.366 + 509 + 4.985'],
            ['Caja y valores negociables', n(float(g('Cash and Marketable'))), '[Dato] 10-Q: 22.443 + 76.926'],
            ['Activos no operativos (valor contable)', '47.898', '[Dato] 10-Q Nota 6; [Juicio] valor económico = contable'],
            ['Acciones en circulación (millones)', '24.268', '[Dato] 10-Q'],
            ['Precio de referencia', usd(price), '[Dato] cierre 30-oct-2026 (Yahoo Finance)'],
            ['Tasa libre de riesgo', '5,29 %', '[Dato] FRED DGS10 30-sep-2026 (misma fecha que la prima)'],
            ['Prima de riesgo de acciones', '3,70 %', '[Dato] Damodaran, oct-2026'],
            ['Beta apalancada', '1,45', '[Juicio] supuesto analítico, sin auditar'],
            ['Costo de la deuda antes de impuestos', '6,0 %', '[Juicio] preliminar'],
            ['Tasa marginal / efectiva proyectada', '25,37 % / 17 %', '[Dato] / [Juicio]'],
            ['WACC terminal', '8,99 %', '[Cálculo] 5,29 % + 3,70 %'],
            ['Año de convergencia del margen', '5', '[Juicio]']]
    return (h2(2, 'Fuentes y trazabilidad de las entradas') +
      P(f'Cada entrada se clasifica como [Dato] (fuente primaria), [Cálculo] o [Juicio] del analista. La captura completa de la hoja se guarda en <code>evidencia/captura-hoja-20261101/{REV}_resultados_hoja.json</code> con SHA-256 <code>{CAP["data_sha256"]}</code> (el hash del contenido; el hash del archivo está en <code>sensibilidadMultiples.resultadosSha256</code> de la valoración).') +
      table(['Entrada', 'Valor', 'Origen'], rows, 'Entradas principales de la hoja.') +
      ul(['NVIDIA, Formulario 10-Q T2 FY2027, período 26-jul-2026, SEC, acceso 0001045810-26-000075.',
          'Damodaran, prima de riesgo implícita de octubre de 2026 (ERPOct26.xlsx).', 'FRED, serie DGS10 (5,29 % el 30-sep-2026; 4,94 % el 30-oct-2026).',
          'Yahoo Finance, cierres diarios sin ajuste por dividendos (precios al cierre fiscal, pares y precio de referencia).',
          'Hoja Google de trabajo NVDA Método A-1.2 (id 1gN_WFYyGzdLjgYr_0AEHGDdBIeCiNVnDFy0wkH0vB0Y), marcada «NO PUBLICAR».']))

def path_tab(key, label):
    t = D[key]; row = t[0 + 1] if False else None
    return t

def n2_3():
    hs = [('Conservadora', cons, D['growth_cons']), ('Base', base, D['growth_base']), ('Optimista', opt, D['growth_opt']), ('Disrupción', disr, D['growth_disr'])]
    rows = [[k, pc(r[1],1), pc(r[2],2), pc(r[3],1), n(r[4],2), n(r[5],2), pc(r[6],2), pc(r[9],1), usd(r[7])] for k, r, _ in hs]
    prow = []
    for k, r, g in hs:
        vals = [x for x in g[0][0:12] if isinstance(x, (int, float))][:10] if g and g[0] else []
        prow.append([k] + [pc(x, 1) for x in vals])
    return (h2(3, 'Supuestos por historia') +
      table(['Historia', 'Prob.', 'CAGR 1–5', 'Margen objetivo', 'S/C 1–5', 'S/C 6–10', 'ROIC terminal', 'g', 'Valor/acción'], rows, 'Cuatro historias (Escenarios e historias).') +
      table(['Historia'] + [f'Año {i}' for i in range(1, 11)], prow, 'Crecimiento anual de ingresos introducido por historia.') +
      P('Los márgenes objetivo se alcanzan linealmente en el año 5 desde el margen ajustado del primer año (69,3 %). Las probabilidades suman 100 %; el promedio ordinario usa solo las tres primeras historias con pesos renormalizados.'))

def n2_4():
    return (h2(4, 'Fórmulas efectivamente utilizadas') +
      ul(['<strong>Reinversión:</strong> Reinv<sub>t</sub> = (Ingresos<sub>t+1</sub> − Ingresos<sub>t</sub>) / S/C, con S/C = 2,2 (años 1–5) y 0,7 (años 6–10) en la Base; un año de desfase. Año 1: (542.922 − 424.158) / 2,2 = 53.984.',
          '<strong>Flujo:</strong> FCFF<sub>t</sub> = EBIT<sub>t</sub> (1 − tasa<sub>t</sub>) − Reinv<sub>t</sub>. Año 1: 243.922 − 53.984 = 189.939.',
          '<strong>EBIT ajustado:</strong> EBIT GAAP + gasto de I+D del año − amortización del activo de investigación (vida 3 años): 197.579 + 23.592 − 11.255 = 209.916 en el LTM.',
          '<strong>Descuento:</strong> factor acumulado ∏(1 + WACC<sub>t</sub>)<sup>−1</sup>, con WACC inicial ' + pc(wacc0, 2) + ' convergiendo al terminal ' + pc(waccT, 2) + ' a partir del año 6.',
          f'<strong>Terminal:</strong> VT = FCFF<sub>11</sub> / (WACC<sub>T</sub> − g), con FCFF<sub>11</sub> = NOPAT<sub>11</sub> (1 − g / ROIC<sub>T</sub>) = {n(tcf)}; VT = {n(tv)}; VP(VT) = {n(pvtv)}.',
          '<strong>Patrimonio:</strong> Valor operativo − deuda − minoritarios + caja + activos no operativos − opciones; valor por acción = patrimonio / acciones.',
          '<strong>MOS 35 %:</strong> precio de entrada = Base × (1 − 0,35). Promedio ordinario = Σ p<sub>i</sub> V<sub>i</sub> / Σ p<sub>i</sub> para Conservadora, Base y Optimista.',
          '<strong>Múltiplos:</strong> Precio<sub>FY+k</sub> = múltiplo de salida × métrica<sub>FY+k</sub> (más dividendos acumulados, puente EV a patrimonio según el método); VP<sub>k</sub> = Precio<sub>FY+k</sub> / (1 + Ke)<sup>k</sup>, con Ke = ' + pc(dm['costoPatrimonio'], 2) + '; consolidado = promedio de VP<sub>1</sub>, VP<sub>2</sub> y VP<sub>3</sub> (criterio «Promedio 1-3 años»).',
          '<strong>Matriz de múltiplo:</strong> celda = VP<sub>3</sub> + (m′·f′ − m<sub>0</sub>·f<sub>0</sub>) / acciones / (1 + Ke)<sup>3</sup>; el centro coincide con el VP<sub>3</sub> del método.']))

def n2_5():
    rows = [[f'{p["year"]}', n(p['revenues']), pc(p['growth'],1), pc(p['margin'],1), n(p['nopat']), n(p['reinvestment']), n(p['fcff']), pc(p['discountRate'],2), n(p['discountFactor'],4), n(p['presentValue'])] for p in proy]
    return (h2(5, 'Proyección Base a diez años') +
      table(['Año', 'Ingresos', 'Crecimiento', 'Margen EBIT', 'NOPAT', 'Reinversión', 'FCFF', 'WACC', 'Factor', 'VP'], rows, 'Proyección de la historia Base (millones de US$).'))

def n2_6():
    rows = [['Suma de VP de los 10 años', n(pv10)], ['Flujo terminal (año 11)', n(tcf)], ['WACC terminal', pc(waccT, 2)], ['Valor terminal', n(tv)], ['VP del valor terminal', n(pvtv)],
            ['Valor operativo', n(pb['sumaPV'])], ['– Deuda', n(pb['deuda'])], ['+ Caja y valores', n(pb['caja'])], ['+ Activos no operativos', n(pb['activosNoOperativos'])],
            ['Patrimonio', n(pb['valorPatrimonio'])], ['Acciones', n(pb['acciones'])], ['Valor por acción', usd(b35)]]
    return (h2(6, 'DCF, valor terminal y puente a patrimonio') +
      table(['Concepto', 'Millones de US$'], rows, 'Valuation output (Base).') +
      P(f'El valor terminal pesa {pc(tv_share,1)} del valor operativo. El ROIC implícito en el terminal es {pc(base[6],2)} con crecimiento de {pc(base[9],1)} y reinversión terminal de {pc(base[9]/base[6],1)} del NOPAT. No hay opciones que restar, ni acciones preferentes, ni pérdidas fiscales acumuladas, ni probabilidad de fracaso.'))

def n2_7():
    out = []
    for k, key, r in (('Conservadora', 'valuation_cons', cons), ('Base', 'valuation_base', base), ('Optimista', 'valuation_opt', opt), ('Disrupción', 'valuation_disr', disr)):
        t = D[key]
        find = lambda lab: next(i for i, x in enumerate(t) if x and str(x[0]).startswith(lab))
        rv = t[find('Revenues')][2:12]; fc = t[find('FCFF')][2:12]; est = t[find('Estimated value')][1]
        assert abs(est - r[7]) < 1e-6, (k, est, r[7])
        out.append([k, pc(r[1],1), n(rv[0]), n(rv[4]), n(rv[9]), n(fc[0]), n(fc[9]), n(t[find('Terminal cash')][1]), usd(est)])
    return (h2(7, 'Cuatro escenarios') +
      table(['Historia', 'Prob.', 'Ingresos año 1', 'Ingresos año 5', 'Ingresos año 10', 'FCFF año 1', 'FCFF año 10', 'Flujo terminal', 'Valor/acción'], out, 'Resultados nativos por historia (Valuation output).') +
      P(f'Promedio ordinario ponderado (sin Disrupción): {usd(ve)}. Disrupción, informada aparte: {usd(disr[7])}. Precio de entrada con MOS 35 % sobre la Base: {usd(mos)}. Ninguna historia libera capital automáticamente cuando caen las ventas (política «Sin liberación»).'))

def n2_8():
    out = []
    for m in dm['metodos']:
        for sc_ in ('conservador', 'base', 'optimista'):
            x = m[sc_]
            out.append([m['nombre'], sc_.capitalize(), pc(m['peso'],1), n(x['fy'][0],2), n(x['fy'][1],2), n(x['fy'][2],2), n(x['vp'][0],2), n(x['vp'][1],2), n(x['vp'][2],2), n(x['consolidado'],2), x['chequeo']])
    s = dm['resumenNativo']
    summ = [['DCF (60 %)', usd(s['dcfHoy']['conservador']), usd(s['dcfHoy']['base']), usd(s['dcfHoy']['optimista'])],
            ['Múltiplos consolidados (40 %)', usd(s['multiplesHoy']['conservador']), usd(s['multiplesHoy']['base']), usd(s['multiplesHoy']['optimista'])],
            ['Ponderado DCF + múltiplos', usd(s['ponderadoHoy']['conservador']), usd(s['ponderadoHoy']['base']), usd(s['ponderadoHoy']['optimista'])]]
    return (h2(8, 'Valoración por múltiplos y descuento a valor presente') +
      P('Cinco múltiplos prioritarios, todos aplicables. Precio FY+k es el precio objetivo más dividendos acumulados; VP k lo descuenta a hoy con el Ke de la hoja. Chequeo = VP a 3 años menor que el precio FY+3.') +
      table(['Método', 'Escenario', 'Peso', 'Precio FY+1', 'Precio FY+2', 'Precio FY+3', 'VP 1 año', 'VP 2 años', 'VP 3 años', 'Consolidado hoy', 'Chequeo'], out, 'Descuento de múltiplos (hoja).') +
      table(['Valor a hoy', 'Conservador', 'Base', 'Optimista'], summ, 'Resumen DCF + múltiplos.') +
      P('P/S y P/BV no se calculan ni ponderan (opcionales); su ausencia no bloquea la publicación. No hay métodos en «N/D» ni «PENDIENTE_ANCLA».'))

def n2_9():
    ms = V['sensibilidadDCF']['matrices']
    def t(m, rl, cl, cap): return table([rl + ' \\ ' + cl] + [pc(c, 1) for c in m['columns']], [[pc(r, 2)] + row for r, row in zip(m['rows'], mat(m))], cap)
    return (h2(9, 'Sensibilidades del DCF') +
      t(ms['waccVsTerminalGrowth'], 'WACC', 'g', 'WACC (fila) por crecimiento terminal (columna), US$/acción; centro = ' + usd(ms['waccVsTerminalGrowth']['center'])) +
      t(ms['waccVsTerminalROIC'], 'ROIC terminal', 'g', 'ROIC terminal por crecimiento terminal, US$/acción; centro = ' + usd(ms['waccVsTerminalROIC']['center'])) +
      t(ms['crecimientoVsMargen'], 'CAGR 1–5', 'Margen', 'Crecimiento compuesto 1–5 por margen objetivo, US$/acción; centro = ' + usd(ms['crecimientoVsMargen']['center'])) +
      P('Los tres centros coinciden con el valor Base de la hoja; los cinco ejes se recalculan en la propia hoja («Sensibilidad DCF»).'))

def n2_10():
    parts = ''
    for m in V['sensibilidadMultiples']['matrices']:
        parts += table(['Múltiplo \\ Fundamental FY+3'] + [n(f, 0) for f in m['fundamentalFY3']],
                       [[n(mu, 2) + 'x'] + [n(v, 2) for v in row] for mu, row in zip(m['multiploElegido'], m['matriz'])],
                       f'{m["metodo"]}: VP a 3 años por acción; centro = {usd(m["centro"])} (= VP3 del método, control OK).')
    return (h2(10, 'Sensibilidades de cada múltiplo (matrices 5×5 Base)') +
      P('Eje vertical: múltiplo de salida en veces; eje horizontal: fundamental FY+3 en las unidades de la hoja; cada celda es el valor presente por acción a hoy. Solo se publican matrices de la historia Base y de los cinco métodos prioritarios aplicables.') + parts)

def n2_11():
    rows = [['Valor Base', 'Valuation output!B35', 'valorPrincipal', usd(b35), 'OK'], ['MOS 35 %', 'B35 × 0,65', 'precioMOS', usd(mos), 'OK'],
            ['Cuatro escenarios', 'Escenarios e historias!H5:H8', 'escenarios', ' / '.join(usd(sc[k]) for k in ('conservador', 'base', 'optimista', 'disrupcion')), 'OK'],
            ['Estados de cálculo', 'Escenarios e historias!K5:K8', '—', 'LISTO ×4', 'OK'],
            ['Inversiones no operativas', 'Input sheet!B85', '—', 'VALIDADO', 'OK'], ['Opciones y casos especiales', 'Input sheet!B108', '—', 'VALIDADO', 'OK'],
            ['WACC', 'Cost of capital worksheet!B84', '—', 'VALIDADO', 'OK'], ['Descuento VP3 < FY+3', 'Descuento de múltiplos!K', 'descuentoMultiples', '15/15 OK', 'OK'],
            ['Centros de matrices de múltiplos', 'Sensibilidad por múltiplo!I', 'sensibilidadMultiples', '5/5 OK', 'OK'], ['Centros de sensibilidad DCF', 'Sensibilidad DCF', 'sensibilidadDCF', '3/3 OK', 'OK']]
    puente = [['g terminal 3,5 % → 4,0 %', '+9,31'], ['Rf 4,94 % → 5,29 %', '−3,97'], ['WACC terminal 9,30 % → 8,99 %', '+9,33'], ['Margen objetivo 53,0 % → 58,7 %', '+22,11'],
              ['Ventas/capital 2,2→2,0 y 0,7→0,598', '−2,26'], ['Senda de crecimiento de R4 (70 % en el año 1)', '+157,64'], ['Activos no operativos 47.898 → 39.257', '−0,35'], ['Residuo hasta R4 (381,79)', '−11,82']]
    return (h2(11, 'Conciliaciones') +
      table(['Concepto', 'Celda de la hoja', 'Campo del JSON', 'Valor', 'Estado'], rows, 'Hoja ↔ JSON ↔ análisis.') +
      P('<strong>Puente R4 → A-1.2.</strong> Sobre la hoja A-1.2 (205,95 tras alinear fechas; 201,80 antes) se sustituyeron uno a uno los supuestos de la revisión R4 (381,79). Cada paso es el valor acumulado que calcula la propia hoja; el orden afecta el reparto, no la suma. Las cifras se obtuvieron antes de alinear las tasas del 30-sep y se conservan como evidencia (<code>evidencia/cierre-gates-meta-nvda-20261101/puente_NVDA_R4_a_A12.json</code>).') +
      table(['Paso', 'Δ US$/acción'], puente, 'Puente desde R4 (calculado sobre la base de 201,80).') +
      P('<strong>Frente al candidato de 31-oct-2026</strong> (Base 201,45, sin salida nativa): la hoja suma 47.898 de activos no operativos y no resta opciones, y desde el 1-nov usa Rf 5,29 % y WACC terminal 8,99 %, con lo que la Base pasa a 205,95. <strong>AZ Stocks</strong> permanece como contraste independiente y no se incorpora en esta revisión.'))

def n2_12():
    return (h2(12, 'Limitaciones y salvedades') + ul(V['salvedades']) +
      P('Esta revisión está EN_REVISION: tiene controles técnicos aprobados pero no auditoría económica independiente ni QA visual autenticado, y no debe presentarse como valoración auditada o certificada.'))

def n2_ref():
    return '<h2 id="jmr-n2-ref">Referencias</h2>' + ul([
      'NVIDIA Corp., Form 10-Q (26-jul-2026), SEC EDGAR, 0001045810-26-000075.', 'Damodaran, A., Implied Equity Risk Premium, oct-2026.', 'FRED, DGS10.',
      'Repositorio Modelo-JMR-datos: docs/CIERRE_GATES_META_NVDA_20261101.md, docs/MULTIPLOS_Y_PUENTE_NVDA_META_20261101.md, docs/FECHAS_TASAS_META_NVDA_20261101.md.',
      'Repositorio JMR-valuation: reference/multiplos_v3/NVDA_{anclas,ciclo,decision}.json.'])

def build():
    chapters = [cap1, cap2, cap3, cap4, cap5, cap6, cap7, cap8, cap9, cap10, cap11, cap12, cap13, cap14]
    titles = [re.search(r'<h2>(.*?)</h2>', f()).group(1) for f in chapters]
    nav = '<nav aria-label="Índice del análisis fundamental" data-jmr-n1-standard="14-20261031"><ol>' + ''.join(f'<li><a href="#jmr-n1-chapter-{i+1}">{t}</a></li>' for i, t in enumerate(titles)) + '</ol></nav>'
    head = (f'<header><h1>NVIDIA — análisis fundamental Método JMR A-1.2</h1><p>EN_REVISION. Estados al 26-jul-2026 (T2 FY2027); precio de referencia {usd(price)} al 30-oct-2026. Valor Base {usd(b35, 6)}; MOS35 {usd(mos, 6)}. '
            'Tasas del corte 30-sep-2026 (Rf y prima de la misma fecha). Auditoría económica no realizada; sin QA visual autenticado.</p></header>')
    article = f'<article data-jmr-revision="{REV}" data-metodo="A-1.2">' + head + nav + ''.join(f() for f in chapters) + '</article>'
    calc = (f'<article data-jmr-revision="{REV}" data-nivel="2" data-metodo="A-1.2"><h1>NVIDIA — Nivel 2 reproducible · Método A-1.2 / FCFF nominal USD</h1>'
            f'<p><strong>Fecha de análisis:</strong> 1-nov-2026. <strong>Corte de estados:</strong> 26-jul-2026. <strong>Precio referencia:</strong> {usd(price)} (30-oct). <strong>Unidad:</strong> millones de US$ salvo valores por acción. <strong>Estado:</strong> EN_REVISION, pendiente de auditoría económica.</p>'
            + ''.join(f() for f in (n2_1, n2_2, n2_3, n2_4, n2_5, n2_6, n2_7, n2_8, n2_9, n2_10, n2_11, n2_12, n2_ref)) + '</article>')
    return article, calc

if __name__ == '__main__':
    article, calc = build()
    w = lambda h: len(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h)).split())
    print('N1 palabras', w(article), 'H2', len(re.findall('<h2', article)), '| N2 palabras', w(calc), 'H2', len(re.findall('<h2', calc)))
    out = {
      'id': f'research-{REV}', 'ticker': 'NVDA', 'company': 'NVIDIA Corporation', 'title': 'NVIDIA Corporation · Modelo JMR A-1.2 · Análisis fundamental',
      'date': '2026-11-01', 'revisionId': REV, 'revision_id': REV, 'valoracionRevisionId': REV, 'price': price, 'priceFetchedAt': '2026-10-30',
      'estado': 'EN_REVISION', 'publicationStage': 'PUBLICACION_EN_REVISION', 'metodo_valoracion': 'A', 'version_metodo': 'A-1.2',
      'linkedValuation': {'sourcePath': f'valoraciones/{REV}.json', 'revisionId': REV, 'valorPrincipal': b35, 'metodo_valoracion': 'A', 'version_metodo': 'A-1.2'},
      'remotePath': f'analisis/NVDA-research-20261101-A12-R1.json', 'html': article + calc, 'articleHtml': article, 'calculationHtml': calc,
      'jmrNarrative': {'version': 'A-1.2-20261101', 'nivel1Capitulos': 14, 'nivel2Apartados': 12},
      'documentoNivel1': 'scripts/analisis_nvda_20261101_parte1.py', 'documentoNivel2': 'scripts/analisis_nvda_20261101_parte3.py',
      'salvedades': 'EN_REVISION: sin auditoría económica ni QA visual autenticado. Ver capítulo 14 y apartado 12 del Nivel 2.',
      'controlCobertura': {'secciones': 14, 'niveles': 'N1_14_N2_12', 'revisionFinanciera': REV, 'auditoriaEconomicaEjecutada': False},
      'estandarizacionEditorial20261031': {'nivel1Capitulos': 14, 'indiceInteractivo': True, 'ciclosSeparados': True, 'calculosModificados': False,
                                           'auditoriaEconomicaEjecutada': False, 'completitudInvestigacion': 'EN_REVISION_SALVEDADES'}}
    dest = ROOT / f'candidatos/valoraciones/{REV}/ANALISIS_A12_EN_REVISION.json'
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n'); print('escrito', dest.relative_to(ROOT))
