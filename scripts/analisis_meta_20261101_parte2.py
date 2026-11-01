# -*- coding: utf-8 -*-
"""Capítulos 8-14, Nivel 2 y ensamblado del análisis de META (revisión META-20261101-A12-R1)."""
import re
from analisis_meta_20261101_parte1 import *

def vrow(i): return VB[i][2:12]
sc_ratio = vrow(37); inv_cap = vrow(38); roic = vrow(39)
tcf = VB[15][1]; tv = VB[17][1]; pvtv = VB[18][1]; pv10 = VB[19][1]
wacc0 = V['tasas']['wacc']; waccT = V['tasas']['waccTerminal']
rein = [p['reinvestment'] for p in proy]
TV = D['trailing']
DV_G = (SD3['values'][3][2] - SD3['values'][2][2]) / ((SD3['rows'][3] - SD3['rows'][2]) * 100)
DV_M = (SD3['values'][2][3] - SD3['values'][2][2]) / ((SD3['columns'][3] - SD3['columns'][2]) * 100)
DV_W_UP = SD1['values'][3][2] - SD1['values'][2][2]; DV_W_DN = SD1['values'][1][2] - SD1['values'][2][2]
DV_G_LO = SD1['values'][2][1] - SD1['values'][2][2]; DV_G_HI = SD1['values'][2][3] - SD1['values'][2][2]
MT = {'EV/EBITDA': 'EVEBITDA', 'EV/FCFF': 'EVFCFF', 'P/E': 'PE', 'P/FCFE': 'PFCFE', 'P/OCF': 'POCF'}
ltm_mult = {'EV/EBITDA': TV[20][11], 'EV/FCFF': TV[23][11], 'P/E': TV[12][11], 'P/FCFE': TV[15][11], 'P/OCF': TV[14][11]}
def mult_row(tab): t = D['mult_' + tab]; return [t[7][7], t[18][7], t[29][7]]

def cap8():
    rows = [[f'Año {i+1}', n(proy[i]['revenues']), n(rein[i]), n(sc_ratio[i], 2), n(inv_cap[i]), pc(roic[i], 0)] for i in (0, 1, 2, 4, 9)]
    return chapter(8, 'Reinversión, capital invertido y compromisos de capacidad',
    P('La reinversión es lo que la empresa debe invertir para crecer y lo que se resta del flujo antes de descontarlo. En el Método A-1.2 la reinversión de cada año es el incremento de ingresos del año siguiente dividido por la razón ventas/capital (Sales-to-Capital), con un año de desfase. En el año 1, ' + n(rein[0]) + ' millones equivalen al aumento de ingresos del año 2 (' + n(proy[1]['revenues'] - proy[0]['revenues']) + ' millones) dividido por 0,52.'),
    table(['Año', 'Ingresos', 'Reinversión', 'Ventas/capital', 'Capital invertido', 'ROIC'], rows, 'Reinversión y retorno en la historia Base (hoja Valuation output).'),
    '<h3>Qué significa una razón de 0,52</h3>' + P(
      f'Una razón ventas/capital de 0,52 significa que cada dólar de capital incremental compra 52 centavos de ingresos adicionales; es decir, para crecer un dólar de ingresos hay que invertir 1,92 dólares. Es una cifra baja, que refleja que Meta se ha convertido en un operador intensivo en capital: el capital invertido analítico pasa de {n(VB[38][1])} millones en el año base a {n(inv_cap[9])} millones en el año 10. El ROIC cae de {pc(roic[0],0)} en el año 1 a {pc(roic[9],0)} en el año 10 y converge a {pc(base[6],1)} en el terminal. Esa caída es el costo que la Base asigna a la infraestructura de IA: cada dólar nuevo rinde menos que el promedio histórico. La Conservadora usa 0,43 y la Optimista 0,68; la Disrupción 0,35.'),
    '<h3>El contraste con el capex real</h3>' + P(
      f'El capex pasó de {n(-capex[8])} millones en {yrs[8]} a {n(-capex[9])} en {yrs[9]} y a {n(-capex[10])} en el LTM. La guía de la compañía para 2026 es de 135.000 a 145.000 millones, incluido el principal de arrendamientos financieros. La depreciación y amortización del LTM es de {n(da_ltm)} millones (EBITDA menos EBIT), así que el capex neto del LTM es de unos {n(-capex[10]-da_ltm)} millones y, con la guía, el capex neto de 2026 estaría entre unos 110.000 y 120.000 millones. La reinversión del año 1 de la Base ({n(rein[0])} millones) queda por encima del capex neto del LTM pero entre 15.000 y 25.000 millones por debajo del neto guiado para 2026, sin contar el capital de trabajo ni la I+D capitalizable que la misma fórmula debería cubrir. Es una brecha que no puede ignorarse: si la reinversión necesaria fuera mayor, el flujo del año 1 (' + n(proy[0]['fcff']) + ' millones) sería menor y el valor bajaría.'),
    '<h3>Lo que el balance no muestra</h3>' + P(
      'El 10-Q informa dos cifras que no están en el balance. Primera, arrendamientos operativos y financieros aún no iniciados por 355.730 millones, que comenzarán entre el resto de 2026 y 2036 con plazos de más de uno a 30 años y corresponden a centros de datos, infraestructura energética, colocación y red. Segunda, compromisos contractuales no cancelables por 454.520 millones, que corresponden sobre todo a capacidad de computación en la nube de terceros, servidores y equipos de red, contratos de servicio de energía y hardware de consumo. Ambas cifras se comparan con unos ingresos LTM de 241.605 millones y un valor operativo de la Base de ' + n(pb['sumaPV']) + ' millones.'),
    P('Estos compromisos no son deuda de balance, y la hoja solo incluye como deuda los pasivos de arrendamiento ya reconocidos (31.173 millones, dentro de los 116.026 de deuda total), de modo que no hay doble conteo. Pero tampoco se pueden ignorar: cuando cada arrendamiento comience, su costo entrará en el EBIT o en la reinversión. Si estos costos ya están en el margen objetivo y en la razón ventas/capital de la Base, la valoración los absorbe; si no, la Base sobrestima el valor. La hoja no permite verificarlo, y por eso es la primera salvedad económica del expediente. Como orden de magnitud, 355.730 millones equivalen a 139 dólares por acción sin descontar; el valor presente sería menor, y parte de lo que financian ya está en los flujos proyectados.'),
    '<h3>Los Ventures de centros de datos</h3>' + P(
      'Meta tiene un 20 % de dos sociedades conjuntas para construir campus de centros de datos: Louisiana (octubre de 2025, costo total estimado de 27.000 millones) y Texas (julio de 2026, 14.000 millones). Las comprometidas aportaciones pro rata aparecen en el balance como inversiones por método de participación (11.547 millones). Meta firmó contratos de arrendamiento con ambas: el de Louisiana comienza en 2029 y el de Texas en 2028, con un plazo inicial de cuatro años y opciones de renovación hasta 20, y garantizó valores residuales cuyo pago máximo sería la diferencia entre el valor razonable y el umbral si decide no renovar. No se ha registrado pasivo porque el pago no se considera probable. Por esa naturaleza, la hoja no trata los 11.547 millones como activo no operativo: son la contraparte de los arrendamientos que Meta pagará, y sumar su valor al patrimonio contaría dos veces la misma capacidad.'))

def cap9():
    return chapter(9, 'Accionistas, dilución, recompras y gobierno',
    P('Meta tiene dos clases de acciones, A y B, con diferente poder de voto, y está dirigida por su fundador, Mark Zuckerberg. Esa estructura concentra el control y reduce la influencia de los accionistas minoritarios sobre decisiones de asignación de capital como la actual; es una ventaja de continuidad estratégica y un riesgo de gobierno que ninguna cifra de la hoja captura. Esta revisión no evalúa el gobierno corporativo: se limita a lo que los estados financieros revelan sobre la asignación del capital.'),
    '<h3>Retorno de caja al accionista</h3>' + P(
      f'Meta no recompró acciones en los nueve meses de 2026: el 10-Q indica que quedan 25.030 millones autorizados y sin utilizar. En {yrs[9]} había recomprado {n(-buy[9])} millones y en {yrs[8]} {n(-buy[8])} millones. El dividendo es de 0,525 dólares trimestrales por acción (2,10 dólares anuales, un rendimiento de 0,34 % sobre {usd(price)}) y los pagos en nueve meses fueron de 4.060 millones. La caja libre del LTM, {n(fcf[10])} millones, cubre los dividendos ({n(-div[10])} millones) pero deja poco margen: el cambio de política respecto de {yrs[9]} (cuando se devolvieron {n(-buy[9]-div[9])} millones) es la señal más clara de que la compañía ha puesto la inversión en infraestructura por encima de la recompra.'),
    '<h3>Dilución y compensación en acciones</h3>' + P(
      f'La compensación en acciones fue de {n(sbc[10])} millones en el LTM ({pc(sbc[10]/rev[10],1)} de los ingresos). Además, los impuestos pagados por la liquidación neta de premios (efectivo que Meta desembolsa para retener acciones en nombre de los empleados) fueron de 12.768 millones en nueve meses de 2026, un 61 % de la compensación en acciones de esos nueve meses (21.053 millones): en la práctica Meta recompra acciones para compensar la emisión, por lo que la compensación en acciones es un costo en efectivo y no una partida contable. Las acciones en circulación al 30 de septiembre eran 2.556 millones, frente a 2.530 al cierre de {yrs[9]} (+1,0 %), y las diluidas promedio del trimestre 2.573 millones.'),
    '<h3>Opciones y RSU</h3>' + P(
      'Meta emitió en 2026 opciones no estatutarias sobre 20 millones de acciones, con precio de ejercicio medio de 2.788 dólares (4,5 veces el precio actual) y un plazo remanente de cuatro años; su gasto no reconocido es de 399 millones a tres años. Es un instrumento de alta convexidad que el modelo valora con Black-Scholes ajustado por dilución: con una volatilidad histórica anual de 42,71 % y un dividendo de 0,34 %, cada opción vale unos ' + usd(pb['opciones'] / 20) + ' y las 20 millones suman ' + n(pb['opciones'], 1) + ' millones, que se restan una sola vez del patrimonio. Las RSU no adquiridas son 134,5 millones (5,3 % de las acciones) con un valor medio de concesión de 589,66 dólares y un gasto no reconocido de 75.590 millones a unos tres años. Dado que 79.290 millones es el valor de concesión total (134,5 millones por 589,66), solo ~4,7 % está devengado (unos 6,3 millones de acciones, 0,25 % del patrimonio). Esa fracción es inmaterial y no se resta aparte; el 95 % restante todavía no se ha ganado y su costo ya está en la compensación en acciones del EBIT futuro, donde se trata como un costo real.'),
    P('La regla de la casa es restar los derechos pendientes una sola vez, sin usar a la vez acciones diluidas que ya los incorporen. La hoja usa las 2.556 millones de acciones básicas, resta el valor de las opciones y no resta las RSU por la razón dada. Los controles de opciones y casos especiales de la hoja (celda B108) quedaron VALIDADOS con esta documentación.'))

def cap10():
    return chapter(10, 'Coste de capital, tasas y fechas',
    P(f'El costo de capital inicial de la hoja es {pc(wacc0,2)} y el terminal {pc(waccT,2)}. El costo del patrimonio resulta de la tasa libre de riesgo (5,29 %, Treasury a 10 años del 30 de septiembre de 2026), la prima de riesgo de Damodaran de octubre de 2026 (3,70 %) y una beta apalancada de 1,15 introducida como supuesto analítico: 5,29 % + 1,15 × 3,70 % = 9,545 %. El costo de la deuda antes de impuestos es 6,0 % (4,48 % después de impuestos) y el peso de la deuda a valor de mercado es de alrededor de 4,6 % (75.394 millones frente a 1,57 billones de capitalización), por lo que el WACC de {pc(wacc0,2)} está muy cerca del costo del patrimonio.'),
    '<h3>La decisión de fechas</h3>' + P(
      'La versión previa de la hoja usaba la tasa libre de riesgo del 30 de octubre (4,94 %) junto con la prima de Damodaran de octubre, calculada con 5,29 % el 30 de septiembre. Esa mezcla de fechas subestima el costo del patrimonio, porque la prima es la diferencia entre el rendimiento esperado del mercado y la tasa libre de su propia fecha. Se alineó el par publicado (5,29 % y 3,70 %) y el costo terminal se fijó en su suma, 8,99 %, en lugar del 8,80 % escrito a mano. El efecto sobre la Base fue de −4,9 % (de 783,42 a 745,29 dólares). Cuando Damodaran publique la prima de noviembre, con datos del 30 de octubre, habrá que actualizar tasa, prima y terminal a la vez.'),
    '<h3>Sensibilidad</h3>' + P(
      f'Con g de 3,5 %, subir 50 puntos básicos el WACC resta {usd(abs(DV_W_UP))} por acción y bajarlos suma {usd(DV_W_DN)}; medio punto menos de crecimiento perpetuo resta {usd(abs(DV_G_LO))} y medio punto más suma {usd(DV_G_HI)}. La beta de 1,15 es la entrada más débil del costo de capital: no se contrastó con una regresión ni con una beta de negocio por sector, y una beta de 1,30 elevaría el costo del patrimonio en unos 55 puntos básicos con el efecto correspondiente sobre el valor. El control técnico del WACC (celda B84) está VALIDADO, pero verifica coherencia aritmética, no precisión económica.'),
    P('Otros puntos a resolver en una auditoría económica: la deuda de mercado es un cálculo del modelo y no el valor razonable de los bonos; la prima de riesgo del país es cero porque Meta se considera estadounidense aunque cerca de 59 % de sus ingresos proviene de fuera de Estados Unidos y Canadá; y el costo de la deuda de 6 % es preliminar. Ninguno altera la estructura del cálculo.'))

def cap11():
    hs = [('Conservadora', cons), ('Base', base), ('Optimista', opt), ('Disrupción', disr)]
    rows = [[k, pc(r[1],1), usd(r[7]), usd(r[7]*(1-V['mos'])), pc(r[7]/price-1,0)] for k, r in hs]
    return chapter(11, 'Historias, probabilidades y señales de refutación',
    table(['Historia', 'Probabilidad', 'Valor por acción', 'Precio con MOS 35 %', 'vs. precio ' + usd(price)], rows, 'Cuatro historias de la hoja (Escenarios e historias).'),
    P(f'Las probabilidades suman 100 %. El promedio ordinario usa Conservadora, Base y Optimista con pesos renormalizados y arroja {usd(ve)}; la Disrupción, con {usd(disr[7])}, se informa aparte porque describe un deterioro de los fundamentos que no se promedia con los casos ordinarios.'),
    '<h3>Base (45 %): la inversión en IA rinde menos que la media histórica, pero rinde</h3>' + P(
      f'Ingresos crecen {pc(base[2],1)} anual compuesto en cinco años, el margen ajustado baja a {pc(base[3],0)}, la razón ventas/capital es {n(base[4],2)} y luego {n(base[5],2)}, y el ROIC converge a {pc(base[6],1)}. Señal de que se cumple: crecimiento interanual de ingresos entre 15 % y 25 % con aumento de precio por anuncio de un dígito alto o doble dígito bajo, y margen operativo ajustado estable por encima del 40 %. Señal de que falla: precio por anuncio estancado mientras el capex y el costo de ingresos siguen creciendo a más del doble que los ingresos.'),
    '<h3>Conservadora (22,5 %): la monetización de la IA tarda más</h3>' + P(
      f'Crece {pc(cons[2],1)} compuesto, con margen de {pc(cons[3],1)} y eficiencia de capital {n(cons[4],2)}. Representa un ciclo publicitario más débil o una rentabilidad menor de la infraestructura. Valor {usd(cons[7])}, {pc(1-cons[7]/price,0)} por debajo del precio actual: el modelo asigna una probabilidad de casi uno en cuatro a que esta historia sea la correcta.'),
    '<h3>Optimista (22,5 %): la IA mejora el precio y abre nuevas líneas</h3>' + P(
      f'Crece {pc(opt[2],1)} compuesto con margen de {pc(opt[3],0)}, razón ventas/capital de {n(opt[4],2)} y ROIC terminal de {pc(opt[6],1)}. Supone que la inversión en cómputo produce mejoras sostenidas en el precio por anuncio y productos nuevos con ingresos propios. Valor {usd(opt[7])}, {pc(opt[7]/price-1,0)} por encima del precio. Es la historia con más opcionalidad y también la que más depende de resultados aún no observados.'),
    '<h3>Disrupción (10 %): el gasto no se recupera</h3>' + P(
      f'Crece {pc(disr[2],1)}, el margen cae a {pc(disr[3],1)}, la razón ventas/capital es {n(disr[4],2)} y el ROIC terminal {pc(disr[6],1)}, con g de {pc(disr[9],1)}. El mecanismo es causal: un salto tecnológico o regulatorio reduce la eficacia de la segmentación o la monetización de la IA mientras el gasto comprometido (355.730 millones de arrendamientos no iniciados y 454.520 de compromisos) sigue siendo exigible. No se libera capital cuando caen las ventas. Valor {usd(disr[7])}.'),
    P('Las señales de refutación son públicas y trimestrales: crecimiento de impresiones y de precio por anuncio, margen operativo ajustado, capex y guía de capex del año siguiente, costo de ingresos como porcentaje de los ingresos, arrendamientos aún no iniciados y evolución de los litigios regulatorios.'))

def cap12():
    rows = [['Valor operativo (suma de valores presentes)', n(pb['sumaPV'])], ['– Deuda (incluye pasivos de arrendamiento reconocidos)', n(pb['deuda'])], ['– Reclamaciones: provisiones legales (campo B21)', n(pb['minoritarios'])],
            ['+ Caja y valores negociables', n(pb['caja'])], ['+ Activos no operativos (valor contable)', n(pb['activosNoOperativos'])],
            ['= Valor del patrimonio', n(pb['valorPatrimonio'])], ['– Opciones', n(pb['opciones'], 1)], ['Acciones (millones)', n(pb['acciones'], 2)], ['Valor por acción', usd(pb['valorPorAccion'])]]
    return chapter(12, 'Valor intrínseco, MOS, precio y puente a equity',
    table(['Puente EV a patrimonio (millones de US$)', 'Valor'], rows, 'Valuation output, historia Base.'),
    P(f'El valor Base por acción es {usd(b35)}. Con un margen de seguridad de 35 %, el precio de entrada es {usd(mos)}. La cotización de {usd(price)} equivale al {pc(price/b35,1)} del valor Base: el mercado descuenta menos que el caso central, pero para cumplir la disciplina de la casa el precio debería bajar un {pc(1-mos/price,0)} adicional. A {usd(price)} la acción no está en zona de compra.'),
    '<h3>Qué descuenta el precio</h3>' + P(
      f'Con la matriz de sensibilidad de crecimiento compuesto de los años 1 a 5 por margen objetivo, el precio de {usd(price)} queda por debajo de la fila más baja de la matriz con el margen Base de {pc(base[3],0)}: a un crecimiento compuesto de {pc(SD3["rows"][0],1)} el valor es {usd(SD3["values"][0][2])}. Extrapolando linealmente, el precio corresponde a un crecimiento compuesto de unos {pc(SD3["rows"][0]-(SD3["values"][0][2]-price)/((SD3["values"][1][2]-SD3["values"][0][2])/(SD3["rows"][1]-SD3["rows"][0])),0)} anual durante cinco años con el margen Base, frente a {pc(base[2],1)} de la Base (valor {usd(SD3["values"][2][2])}). Con {pc(SD3["rows"][4],1)} el valor sería {usd(SD3["values"][4][2])}. Dicho de otro modo, el mercado descuenta bastante menos crecimiento que la Base (o un margen más bajo para el mismo crecimiento): para el mismo crecimiento de la Base, el margen implícito sería inferior al 40 %.'),
    '<h3>Activos no operativos, pasivo legal y opciones</h3>' + P(
      'Los 21.077 millones de activos no operativos son el valor contable de inversiones no cotizadas bajo la alternativa de medición (costo de 21.119 millones más ajustes observables de 582 y menos deterioros de 624). No se suman los 11.547 millones por método de participación, que son los Ventures de centros de datos. Las ganancias o pérdidas de estas inversiones se registran en “otros ingresos (gastos), netos” debajo del resultado operativo, de modo que no están en el EBIT ni en el flujo del DCF (celda B85 VALIDADA). La caja de 82.449 millones incluye 71.227 de valores negociables.'),
    P(f'Las provisiones legales de 19.881 millones (11.577 corrientes y 8.304 no corrientes, según la nota 8 del 10-Q) se restan en el puente una sola vez, en valor bruto y sin efecto fiscal, usando el campo de reclamaciones de la hoja, que no se emplea para participaciones minoritarias porque Meta no las tiene. Su efecto es −7,78 dólares por acción. Es una cota superior: parte de lo que se paga puede ser deducible, y las multas a gobiernos normalmente no lo son. Las opciones restan {n(pb["opciones"],1)} millones. El puente EV a patrimonio de los múltiplos no incluye las provisiones legales, una limitación que se declara.'))

def cap13():
    rows = []
    for m in dm['metodos']:
        nm = m['nombre']; mt = mult_row(MT[nm])
        rows.append([nm, pc(m['peso'],1), f'{n(mt[0],1)}x / {n(mt[1],1)}x / {n(mt[2],1)}x', n(ltm_mult[nm],1)+'x', usd(m['base']['vp'][2]), usd(m['base']['consolidado'])])
    return chapter(13, 'Múltiplos y sensibilidades',
    P('Los cinco múltiplos prioritarios (EV/EBITDA, EV/FCFF, P/E, P/FCFE y P/OCF) son aplicables a Meta porque tiene beneficios y flujos positivos y un denominador FY+3 positivo en todos los escenarios. P/S y P/BV se dejan fuera: no añaden contraste fiable en una empresa con margen operativo superior a 30 % y no tienen múltiplo de salida elegido en la hoja. Ninguno de los cinco tiene peso cero.'),
    table(['Método', 'Peso total', 'Múltiplo de salida FY+3 (Cons. / Base / Opt.)', 'Múltiplo LTM', 'VP a 3 años (Base)', 'Consolidado hoy (Base)'], rows, 'Valoración por múltiplos descontada a valor presente (Descuento de múltiplos).'),
    '<h3>Cómo se eligió el múltiplo de salida</h3>' + P(
      'La regla de ciclo de la casa elige, para cada escenario, el múltiplo que Meta tuvo en cierres fiscales cuyo crecimiento se parecía al que ese escenario espera en FY+3, con los múltiplos históricos llevados al costo de capital actual y limitado por el múltiplo que justifican los fundamentos del propio escenario. Los pares (GOOGL, PINS, AMZN, MSFT, NFLX, APP y RDDT; SNAP excluido por EBITDA negativo) solo comprueban.'),
    '<h3>Por qué los múltiplos quedan muy por debajo del DCF</h3>' + P(
      f'El valor por múltiplos consolidado a hoy es {usd(dm["multiplesHoy"]["base"])} en la Base, {pc(1-dm["multiplesHoy"]["base"]/b35,0)} por debajo del DCF de {usd(b35)}; el ponderado (60 % DCF y 40 % múltiplos) es {usd(dm["ponderadoHoy"]["base"])}. La brecha tiene una causa concreta: el tope del múltiplo justificado. El múltiplo justificado de cada método se deriva del flujo libre del año FY+3, que está deprimido por la inversión en infraestructura (el FCFF del año 3 es de {n(proy[2]["fcff"])} millones sobre NOPAT de {n(proy[2]["nopat"])}). Así, el EV/EBITDA Base de salida es de solo {n(mult_row("EVEBITDA")[1],1)}x frente a {n(ltm_mult["EV/EBITDA"],1)}x en el LTM, a 15-16x de la historia y a 18-21x de los pares. Es decir, los múltiplos asumen que la intensidad de capital actual se mantiene hasta FY+3, mientras que el DCF supone que la reinversión baja en la segunda mitad del período explícito (de {n(rein[0])} a {n(rein[9])} millones en el año 10). La diferencia entre ambos métodos es la diferencia entre esas dos visiones de la rentabilidad de la inversión en IA.'),
    P(f'Tres cautelas más. Primera, el P/FCFE LTM de {n(ltm_mult["P/FCFE"],1)}x y el EV/FCFF LTM de {n(ltm_mult["EV/FCFF"],1)}x están inflados porque el flujo de caja libre LTM es pequeño ({n(fcf[10])} millones); no son referencias de mercado normales. Segunda, P/OCF y P/FCFE no restan la compensación en acciones. Tercera, la categoría «Crecimiento» que fija los pesos y el MOS de 35 % son juicio del analista. Las cinco matrices 5×5 de sensibilidad Base (apartado 10 del Nivel 2) calculan en la hoja y su centro coincide con el valor presente a tres años de cada método.'),
    P('La comparación con AZ Stocks, que debe mantenerse como contraste independiente y no mezclarse con el Método A-1.2, no se incorporó en esta revisión: queda pendiente y no se ha inventado ninguna cifra para suplirla.'))

def cap14():
    return chapter(14, 'Catalizadores, riesgos, fuentes y decisiones pendientes',
    '<h3>Catalizadores</h3>' + P('Los próximos resultados trimestrales y la guía de capex del año siguiente permitirán contrastar la reinversión de la Base (' + n(rein[0]) + ' millones en el año 1) con el gasto real. Importan igualmente el precio por anuncio, el inicio de los arrendamientos de los Ventures de Texas (2028) y Louisiana (2029), la resolución de los litigios estatales pendientes y la evolución de los productos de IA con monetización propia.'),
    '<h3>Riesgos</h3>' + P('Intensidad de capital: arrendamientos no iniciados por 355.730 millones y compromisos no cancelables por 454.520 millones. Regulación y litigios: el acuerdo multiestatal de agosto de 2026 (9.890 millones de cargo), otros litigios estatales aún abiertos con posibles multas y cambios obligados de prácticas, y el escrutinio de las aplicaciones de IA. Competencia por el presupuesto publicitario. Dependencia de un solo motor de ingresos (97,6 % publicidad). Gobierno: estructura de dos clases de acciones. Valoración: el precio ya descuenta un crecimiento compuesto cercano al de la Base.'),
    '<h3>Salvedades abiertas de la valoración</h3>' + P('1) EN_REVISION sin auditoría económica. 2) Arrendamientos no iniciados y compromisos no cancelables sin cuantificar en la valoración; reinversión del año 1 por debajo del capex neto guiado. 3) Provisiones legales deducidas en bruto y sin efecto fiscal; no incluidas en el puente de múltiplos. 4) Activos no operativos a valor contable. 5) Beta de 1,15 y costo de la deuda de 6 % no auditados; precio al 30 de octubre y tasas al 30 de septiembre. 6) Brecha de 46 % entre múltiplos y DCF por el tope del múltiplo justificado. 7) Categoría «Crecimiento» y MOS de 35 %: juicio del analista; AZ Stocks pendiente. 8) QA visual autenticado pendiente.'),
    '<h3>Qué mueve el valor y cuánto</h3>' + P(
      f'Las matrices de sensibilidad ordenan las hipótesis por su efecto sobre el valor Base de {usd(b35)}: cada punto porcentual de crecimiento compuesto en los años 1 a 5 vale unos {usd(DV_G)} por acción; cada punto de margen objetivo, unos {usd(DV_M)}; subir 50 puntos básicos el WACC resta {usd(abs(DV_W_UP))} y bajarlos suma {usd(DV_W_DN)}; medio punto menos de crecimiento perpetuo resta {usd(abs(DV_G_LO))} y medio punto más suma {usd(DV_G_HI)}. El margen y el crecimiento pesan mucho más que el ROIC terminal. La deducción de las provisiones legales (7,78 dólares) es menor que medio punto de margen, pero es la única cifra de esta lista que está respaldada por un saldo contable.'),
    '<h3>Qué nos haría cambiar de opinión</h3>' + P('Subiría la probabilidad de la historia Optimista: un precio por anuncio que siga creciendo a doble dígito mientras el capex por dólar de ingreso adicional cae, o ingresos de productos de IA con monetización directa. Subiría la probabilidad de la Conservadora: un crecimiento de ingresos que baje de 15 % mientras el costo de ingresos y la investigación y desarrollo siguen creciendo a más del doble de ritmo, o una guía de capex del año siguiente superior a la actual sin aceleración de ingresos. Activaría la Disrupción: una restricción regulatoria que limite el uso de datos para segmentación, o un cambio de plataforma móvil que reduzca la eficacia publicitaria, con compromisos de infraestructura todavía exigibles. En ningún caso habría que cambiar la estructura del modelo, solo las probabilidades y, si los datos lo justifican, el crecimiento y la reinversión de los dos primeros años.'),
    '<h3>Fuentes</h3>' + P('Meta Platforms, Formulario 10-Q del tercer trimestre de 2026 (30 de septiembre de 2026, SEC, acceso 0001628280-26-066773); hoja de trabajo Método A-1.2 de META y su captura con hash SHA-256 (<code>evidencia/captura-hoja-20261101</code>); Damodaran, prima implícita de octubre de 2026; FRED, serie DGS10; Yahoo Finance, cierres históricos y de pares; documentos del repositorio: CIERRE_GATES, MULTIPLOS_Y_PUENTE, FECHAS_TASAS (1 de noviembre de 2026) y el expediente de pasivo legal.'))

# ---------------- Nivel 2 ----------------
def h2(i, t): return f'<h2 id="jmr-n2-{i}">{i}. {t}</h2>'
def ul(items): return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'
mat = lambda m: [[n(v, 2) for v in row] for row in m['values']]

def n2_1():
    rows = [[yrs[i], n(rev[i]), n(gp[i]), n(rd[i]), n(IS[8][1+i]), n(ebit[i]), n(ebitda[i]), n(ni[i]), n(IS[25][1+i]) if isinstance(IS[25][1+i], (int, float)) else 'N/D'] for i in range(11)]
    cf_rows = [[yrs[i], n(ocf[i]), n(-capex[i]), n(fcf[i]), n(sbc[i]), n(-buy[i]), n(-div[i])] for i in range(11)]
    return (h2(1, 'Históricos y base de datos') + P('Series de la hoja de trabajo (millones de US$ salvo acciones y tasas). Diez años fiscales más los doce meses a 30-sep-2026 (LTM).') +
      table(['Año', 'Ingresos', 'Utilidad bruta', 'I+D', 'SG&A', 'EBIT', 'EBITDA', 'Utilidad neta', 'Acciones diluidas'], rows, 'Estado de resultados.') +
      table(['Año', 'Flujo operativo', 'Capex', 'FCF', 'Compensación en acciones', 'Recompras', 'Dividendos'], cf_rows, 'Flujo de caja.'))

def n2_2():
    rows = [['Ingresos LTM', n(rev[10]), '[Dato] 10-K FY2025 + 10-Q 3T26 (LTM = FY25 + 9M26 − 9M25)'], ['EBIT LTM (GAAP)', n(ebit[10]), '[Dato] ídem; incluye cargo legal de 9.890'],
            ['I+D LTM capitalizada (vida 3 años)', n(rd[10]), '[Dato] gasto; [Juicio] vida útil de 3 años'], ['Ajuste al EBIT por I+D', '32.423', '[Cálculo] conversor de I+D de la hoja'],
            ['Deuda total (con pasivos de arrendamiento reconocidos)', '116.026', '[Dato] 10-Q'], ['Caja y valores negociables', '82.449', '[Dato] 10-Q: 11.222 + 71.227'],
            ['Activos no operativos (valor contable)', '21.077', '[Dato] 10-Q Nota 5; [Juicio] valor económico = contable'], ['Provisiones legales deducidas', '19.881', '[Dato] 10-Q Nota 8: 11.577 + 8.304; [Juicio] bruto, sin efecto fiscal'],
            ['Acciones en circulación (millones)', '2.556,24', '[Dato] 10-Q'], ['Opciones', '20 M a US$2.788, 4 años, vol. 42,71 %', '[Dato] 10-Q; [Cálculo] volatilidad histórica 1 año'],
            ['Precio de referencia', usd(price), '[Dato] cierre 30-oct-2026 (Yahoo Finance)'], ['Tasa libre de riesgo', '5,29 %', '[Dato] FRED DGS10 30-sep-2026'], ['Prima de riesgo de acciones', '3,70 %', '[Dato] Damodaran, oct-2026'],
            ['Beta apalancada', '1,15', '[Juicio] supuesto analítico, sin auditar'], ['Costo de la deuda antes de impuestos', '6,0 %', '[Juicio] preliminar'], ['WACC terminal', '8,99 %', '[Cálculo] 5,29 % + 3,70 %'], ['Año de convergencia del margen', '5', '[Juicio]']]
    return (h2(2, 'Fuentes y trazabilidad de las entradas') +
      P(f'Cada entrada se clasifica como [Dato], [Cálculo] o [Juicio]. La captura completa de la hoja se guarda en <code>evidencia/captura-hoja-20261101/{REV}_resultados_hoja.json</code> con SHA-256 de contenido <code>{CAP["data_sha256"]}</code>.') +
      table(['Entrada', 'Valor', 'Origen'], rows, 'Entradas principales de la hoja.') +
      ul(['Meta Platforms, Form 10-Q 3T 2026, período 30-sep-2026, SEC, acceso 0001628280-26-066773.', 'Damodaran, prima de riesgo implícita de octubre de 2026.', 'FRED, serie DGS10 (5,29 % el 30-sep; 4,94 % el 30-oct-2026).',
          'Yahoo Finance, cierres sin ajuste por dividendos.', 'Hoja Google de trabajo META Método A-1.2 (id 1lpE-L0Ai2NrWDhzBhtdeOMASwo7XRleUEMEMl3K34ss), marcada «NO PUBLICAR».']))

def find(t, lab): return next(i for i, x in enumerate(t) if x and str(x[0]).startswith(lab))

def n2_3():
    hs = [('Conservadora', cons, D['growth_cons']), ('Base', base, D['growth_base']), ('Optimista', opt, D['growth_opt']), ('Disrupción', disr, D['growth_disr'])]
    rows = [[k, pc(r[1],1), pc(r[2],2), pc(r[3],1), n(r[4],2), n(r[5],2), pc(r[6],2), pc(r[9],1), usd(r[7])] for k, r, _ in hs]
    prow = []
    for k, r, g in hs:
        vals = [x for x in g[0][0:12] if isinstance(x, (int, float))][:10] if g and g[0] else []
        prow.append([k] + [pc(x, 1) for x in vals])
    return (h2(3, 'Supuestos por historia') +
      table(['Historia', 'Prob.', 'CAGR 1–5', 'Margen objetivo', 'S/C 1–5', 'S/C 6–10', 'ROIC terminal', 'g', 'Valor/acción'], rows, 'Cuatro historias (Escenarios e historias).') +
      table(['Historia'] + [f'Año {i}' for i in range(1, 11)], prow, 'Crecimiento anual de ingresos por historia.') +
      P('Los márgenes objetivo se alcanzan linealmente en el año 5 desde el margen ajustado del año base. El promedio ordinario usa solo las tres primeras historias con pesos renormalizados.'))

def n2_4():
    return (h2(4, 'Fórmulas efectivamente utilizadas') + ul([
      f'<strong>Reinversión:</strong> Reinv<sub>t</sub> = (Ingresos<sub>t+1</sub> − Ingresos<sub>t</sub>) / S/C, con S/C = 0,52 (años 1–5) y 0,55 (años 6–10) en la Base; un año de desfase. Año 1: ({n(proy[1]["revenues"])} − {n(proy[0]["revenues"])}) / 0,52 = {n(rein[0])}.',
      f'<strong>Flujo:</strong> FCFF<sub>t</sub> = EBIT<sub>t</sub> (1 − tasa<sub>t</sub>) − Reinv<sub>t</sub>. Año 1: {n(proy[0]["nopat"])} − {n(rein[0])} = {n(proy[0]["fcff"])}.',
      f'<strong>EBIT ajustado:</strong> EBIT GAAP + gasto de I+D − amortización del activo de investigación (vida 3 años): {n(ebit[10])} + 32.423 = 111.803 en el LTM.',
      f'<strong>Descuento:</strong> factor acumulado ∏(1 + WACC<sub>t</sub>)<sup>−1</sup>, con WACC inicial {pc(wacc0,2)} convergiendo al terminal {pc(waccT,2)} desde el año 6.',
      f'<strong>Terminal:</strong> VT = FCFF<sub>11</sub> / (WACC<sub>T</sub> − g), con FCFF<sub>11</sub> = NOPAT<sub>11</sub> (1 − g / ROIC<sub>T</sub>) = {n(tcf)}; VT = {n(tv)}; VP(VT) = {n(pvtv)}.',
      '<strong>Patrimonio:</strong> valor operativo − deuda − reclamaciones (provisiones legales) + caja + activos no operativos − opciones; valor por acción = patrimonio / acciones.',
      '<strong>MOS 35 %:</strong> precio de entrada = Base × (1 − 0,35). Promedio ordinario = Σ p<sub>i</sub> V<sub>i</sub> / Σ p<sub>i</sub> (Conservadora, Base, Optimista).',
      '<strong>Múltiplos:</strong> Precio<sub>FY+k</sub> = múltiplo de salida × métrica<sub>FY+k</sub> (más dividendos acumulados); VP<sub>k</sub> = Precio<sub>FY+k</sub> / (1 + Ke)<sup>k</sup>, con Ke = ' + pc(dm['costoPatrimonio'], 2) + '; consolidado = promedio de VP<sub>1</sub>, VP<sub>2</sub> y VP<sub>3</sub>.',
      '<strong>Matriz de múltiplo:</strong> celda = VP<sub>3</sub> + (m′·f′ − m<sub>0</sub>·f<sub>0</sub>) / acciones / (1 + Ke)<sup>3</sup>; el centro coincide con el VP<sub>3</sub> del método.']))

def n2_5():
    rows = [[f'{p["year"]}', n(p['revenues']), pc(p['growth'],1), pc(p['margin'],1), n(p['nopat']), n(p['reinvestment']), n(p['fcff']), pc(p['discountRate'],2), n(p['discountFactor'],4), n(p['presentValue'])] for p in proy]
    return h2(5, 'Proyección Base a diez años') + table(['Año', 'Ingresos', 'Crecimiento', 'Margen EBIT', 'NOPAT', 'Reinversión', 'FCFF', 'WACC', 'Factor', 'VP'], rows, 'Proyección de la historia Base (millones de US$).')

def n2_6():
    rows = [['Suma de VP de los 10 años', n(pv10)], ['Flujo terminal (año 11)', n(tcf)], ['WACC terminal', pc(waccT, 2)], ['Valor terminal', n(tv)], ['VP del valor terminal', n(pvtv)],
            ['Valor operativo', n(pb['sumaPV'])], ['– Deuda', n(pb['deuda'])], ['– Provisiones legales', n(pb['minoritarios'])], ['+ Caja y valores', n(pb['caja'])], ['+ Activos no operativos', n(pb['activosNoOperativos'])],
            ['Patrimonio antes de opciones', n(pb['valorPatrimonio'])], ['– Opciones', n(pb['opciones'], 1)], ['Acciones', n(pb['acciones'], 2)], ['Valor por acción', usd(b35)]]
    return (h2(6, 'DCF, valor terminal y puente a patrimonio') + table(['Concepto', 'Millones de US$'], rows, 'Valuation output (Base).') +
      P(f'El valor terminal pesa {pc(tv_share,1)} del valor operativo. El ROIC implícito en el terminal es {pc(base[6],2)} con crecimiento de {pc(base[9],1)} y reinversión terminal de {pc(base[9]/base[6],1)} del NOPAT. No hay preferentes, pérdidas fiscales acumuladas ni probabilidad de fracaso.'))

def n2_7():
    out = []
    for k, key, r in (('Conservadora', 'valuation_cons', cons), ('Base', 'valuation_base', base), ('Optimista', 'valuation_opt', opt), ('Disrupción', 'valuation_disr', disr)):
        t = D[key]; rv = t[find(t, 'Revenues')][2:12]; fc = t[find(t, 'FCFF')][2:12]; est = t[find(t, 'Estimated value')][1]
        assert abs(est - r[7]) < 1e-6, (k, est, r[7])
        out.append([k, pc(r[1],1), n(rv[0]), n(rv[4]), n(rv[9]), n(fc[0]), n(fc[9]), n(t[find(t, 'Terminal cash')][1]), usd(est)])
    return (h2(7, 'Cuatro escenarios') + table(['Historia', 'Prob.', 'Ingresos año 1', 'Ingresos año 5', 'Ingresos año 10', 'FCFF año 1', 'FCFF año 10', 'Flujo terminal', 'Valor/acción'], out, 'Resultados nativos por historia.') +
      P(f'Promedio ordinario ponderado (sin Disrupción): {usd(ve)}. Disrupción, informada aparte: {usd(disr[7])}. Precio de entrada con MOS 35 % sobre la Base: {usd(mos)}. Ninguna historia libera capital automáticamente cuando caen las ventas.'))

def n2_8():
    out = []
    for m in dm['metodos']:
        for sc_ in ('conservador', 'base', 'optimista'):
            x = m[sc_]; out.append([m['nombre'], sc_.capitalize(), pc(m['peso'],1)] + [n(v, 2) for v in x['fy'] + x['vp']] + [n(x['consolidado'], 2), x['chequeo']])
    s = dm['resumenNativo']
    summ = [['DCF (60 %)'] + [usd(s['dcfHoy'][k]) for k in ('conservador', 'base', 'optimista')], ['Múltiplos consolidados (40 %)'] + [usd(s['multiplesHoy'][k]) for k in ('conservador', 'base', 'optimista')],
            ['Ponderado DCF + múltiplos'] + [usd(s['ponderadoHoy'][k]) for k in ('conservador', 'base', 'optimista')]]
    return (h2(8, 'Valoración por múltiplos y descuento a valor presente') + P('Cinco múltiplos prioritarios, todos aplicables. Chequeo = VP a 3 años menor que el precio FY+3.') +
      table(['Método', 'Escenario', 'Peso', 'Precio FY+1', 'Precio FY+2', 'Precio FY+3', 'VP 1 año', 'VP 2 años', 'VP 3 años', 'Consolidado hoy', 'Chequeo'], out, 'Descuento de múltiplos (hoja).') +
      table(['Valor a hoy', 'Conservador', 'Base', 'Optimista'], summ, 'Resumen DCF + múltiplos.') +
      P('P/S y P/BV no se calculan ni ponderan (opcionales). No hay métodos en «N/D» ni «PENDIENTE_ANCLA» entre los cinco prioritarios. La brecha entre el valor por múltiplos y el DCF se explica en el capítulo 13.'))

def n2_9():
    ms = V['sensibilidadDCF']['matrices']
    def t(m, rl, cl, cap): return table([rl + ' \\ ' + cl] + [pc(c, 1) for c in m['columns']], [[pc(r, 2)] + row for r, row in zip(m['rows'], mat(m))], cap)
    return (h2(9, 'Sensibilidades del DCF') + t(ms['waccVsTerminalGrowth'], 'WACC', 'g', 'WACC por crecimiento terminal, US$/acción; centro = ' + usd(ms['waccVsTerminalGrowth']['center'])) +
      t(ms['waccVsTerminalROIC'], 'ROIC terminal', 'g', 'ROIC terminal por crecimiento terminal; centro = ' + usd(ms['waccVsTerminalROIC']['center'])) +
      t(ms['crecimientoVsMargen'], 'CAGR 1–5', 'Margen', 'Crecimiento compuesto 1–5 por margen objetivo; centro = ' + usd(ms['crecimientoVsMargen']['center'])) +
      P('Los tres centros coinciden con el valor Base de la hoja; los ejes se recalculan en la propia hoja («Sensibilidad DCF»).'))

def n2_10():
    parts = ''
    for m in [x for x in V['sensibilidadMultiples']['matrices'] if x['estado'] == 'OK']:
        parts += table(['Múltiplo \\ Fundamental FY+3'] + [n(f, 0) for f in m['fundamentalFY3']], [[n(mu, 2) + 'x'] + [n(v, 2) for v in row] for mu, row in zip(m['multiploElegido'], m['matriz'])],
                       f'{m["metodo"]}: VP a 3 años por acción; centro = {usd(m["centro"])} (= VP3 del método, control OK).')
    return (h2(10, 'Sensibilidades de cada múltiplo (matrices 5×5 Base)') + P('Eje vertical: múltiplo de salida en veces; eje horizontal: fundamental FY+3; cada celda es el valor presente por acción a hoy. Las posiciones sexta y séptima del contrato (P/V y P/BV, complementarios opcionales) están en N/D porque la hoja no tiene múltiplo de salida elegido; no tienen peso y no bloquean la publicación.') + parts)

def n2_11():
    rows = [['Valor Base', 'Valuation output!B35', 'valorPrincipal', usd(b35), 'OK'], ['MOS 35 %', 'B35 × 0,65', 'precioMOS', usd(mos), 'OK'],
            ['Cuatro escenarios', 'Escenarios e historias!H5:H8', 'escenarios', ' / '.join(usd(sc[k]) for k in ('conservador', 'base', 'optimista', 'disrupcion')), 'OK'],
            ['Estados de cálculo', 'Escenarios e historias!K5:K8', '—', 'LISTO ×4', 'OK'], ['Inversiones no operativas', 'Input sheet!B85', '—', 'VALIDADO', 'OK'], ['Opciones y casos especiales', 'Input sheet!B108', '—', 'VALIDADO', 'OK'],
            ['WACC', 'Cost of capital worksheet!B84', '—', 'VALIDADO', 'OK'], ['Descuento VP3 < FY+3', 'Descuento de múltiplos!K', 'descuentoMultiples', '15/15 OK', 'OK'],
            ['Centros de matrices de múltiplos', 'Sensibilidad por múltiplo!I', 'sensibilidadMultiples', '5/5 OK', 'OK'], ['Centros de sensibilidad DCF', 'Sensibilidad DCF', 'sensibilidadDCF', '3/3 OK', 'OK']]
    puente = [['Base antes de alinear fechas (Rf 4,94 %, terminal 8,80 %)', '783,42'], ['Alinear Rf 5,29 %, ERP 3,70 % y terminal 8,99 %', '−38,13 → 745,29'], ['Deducir provisiones legales 19.881 M (campo B21)', '−7,78 → 737,51']]
    return (h2(11, 'Conciliaciones') + table(['Concepto', 'Celda de la hoja', 'Campo del JSON', 'Valor', 'Estado'], rows, 'Hoja ↔ JSON ↔ análisis.') +
      table(['Paso sobre la hoja', 'Valor por acción'], puente, 'De la hoja de 31-oct al valor publicado (US$ por acción).') +
      P('<strong>Frente a la revisión anterior META R5</strong> (Base 726,65): la hoja A-1.2 da 737,51, una diferencia de +1,5 %, pero con supuestos, método de reinversión e historias distintos. No se construyó un puente paso a paso R5 → A-1.2, a diferencia de NVDA, porque la brecha neta es pequeña; hacerlo es una tarea pendiente si se desea explicar los componentes que se compensan. <strong>Frente al candidato de 31-oct</strong> (780,63, sin salida nativa): la hoja suma 21.077 de activos no operativos, resta opciones y provisiones legales y usa tasas alineadas. <strong>AZ Stocks</strong> permanece como contraste independiente y no se incorpora en esta revisión.'))

def n2_12():
    return h2(12, 'Limitaciones y salvedades') + ul(V['salvedades']) + P('Esta revisión está EN_REVISION: tiene controles técnicos aprobados pero no auditoría económica independiente ni QA visual autenticado, y no debe presentarse como valoración auditada o certificada.')

def n2_ref():
    return '<h2 id="jmr-n2-ref">Referencias</h2>' + ul(['Meta Platforms, Form 10-Q (30-sep-2026), SEC EDGAR, 0001628280-26-066773.', 'Damodaran, A., Implied Equity Risk Premium, oct-2026.', 'FRED, DGS10.',
      'Repositorio Modelo-JMR-datos: docs/CIERRE_GATES_META_NVDA_20261101.md, docs/MULTIPLOS_Y_PUENTE_NVDA_META_20261101.md, docs/FECHAS_TASAS_META_NVDA_20261101.md.', 'Repositorio JMR-valuation: reference/multiplos_v3/META_{anclas,ciclo,decision}.json.'])

def build():
    chapters = [cap1, cap2, cap3, cap4, cap5, cap6, cap7, cap8, cap9, cap10, cap11, cap12, cap13, cap14]
    titles = [re.search(r'<h2>(.*?)</h2>', f()).group(1) for f in chapters]
    nav = '<nav aria-label="Índice del análisis fundamental" data-jmr-n1-standard="14-20261031"><ol>' + ''.join(f'<li><a href="#jmr-n1-chapter-{i+1}">{t}</a></li>' for i, t in enumerate(titles)) + '</ol></nav>'
    head = (f'<header><h1>Meta Platforms — análisis fundamental Método JMR A-1.2</h1><p>EN_REVISION. Estados al 30-sep-2026 (3T 2026); precio de referencia {usd(price)} al 30-oct-2026. Valor Base {usd(b35, 6)}; MOS35 {usd(mos, 6)}. '
            'Tasas del corte 30-sep-2026 (Rf y prima de la misma fecha). Auditoría económica no realizada; sin QA visual autenticado.</p></header>')
    article = f'<article data-jmr-revision="{REV}" data-metodo="A-1.2">' + head + nav + ''.join(f() for f in chapters) + '</article>'
    calc = (f'<article data-jmr-revision="{REV}" data-nivel="2" data-metodo="A-1.2"><h1>Meta Platforms — Nivel 2 reproducible · Método A-1.2 / FCFF nominal USD</h1>'
            f'<p><strong>Fecha de análisis:</strong> 1-nov-2026. <strong>Corte de estados:</strong> 30-sep-2026. <strong>Precio referencia:</strong> {usd(price)} (30-oct). <strong>Unidad:</strong> millones de US$ salvo valores por acción. <strong>Estado:</strong> EN_REVISION, pendiente de auditoría económica.</p>'
            + ''.join(f() for f in (n2_1, n2_2, n2_3, n2_4, n2_5, n2_6, n2_7, n2_8, n2_9, n2_10, n2_11, n2_12, n2_ref)) + '</article>')
    return article, calc

if __name__ == '__main__':
    article, calc = build()
    w = lambda h: len(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h)).split())
    print('N1 palabras', w(article), 'H2', len(re.findall('<h2', article)), '| N2 palabras', w(calc), 'H2', len(re.findall('<h2', calc)))
    out = {'id': f'research-{REV}', 'ticker': 'META', 'company': 'Meta Platforms, Inc.', 'title': 'Meta Platforms, Inc. · Modelo JMR A-1.2 · Análisis fundamental',
      'date': '2026-11-01', 'revisionId': REV, 'revision_id': REV, 'valoracionRevisionId': REV, 'price': price, 'priceFetchedAt': '2026-10-30',
      'estado': 'EN_REVISION', 'publicationStage': 'PUBLICACION_EN_REVISION', 'metodo_valoracion': 'A', 'version_metodo': 'A-1.2',
      'linkedValuation': {'sourcePath': f'valoraciones/{REV}.json', 'revisionId': REV, 'valorPrincipal': b35, 'metodo_valoracion': 'A', 'version_metodo': 'A-1.2'},
      'remotePath': 'analisis/META-research-20261101-A12-R1.json', 'html': article + calc, 'articleHtml': article, 'calculationHtml': calc,
      'jmrNarrative': {'version': 'A-1.2-20261101', 'nivel1Capitulos': 14, 'nivel2Apartados': 12},
      'documentoNivel1': 'scripts/analisis_meta_20261101_parte1.py', 'documentoNivel2': 'scripts/analisis_meta_20261101_parte2.py',
      'salvedades': 'EN_REVISION: sin auditoría económica ni QA visual autenticado. Ver capítulo 14 y apartado 12 del Nivel 2.',
      'controlCobertura': {'secciones': 14, 'niveles': 'N1_14_N2_12', 'revisionFinanciera': REV, 'auditoriaEconomicaEjecutada': False, 'seccionesAntesEstandarizacion': 14,
                           'notaConteos': 'secciones cuenta capítulos N1; entradas y resoluciones anteriores se conservan como inventario de evidencia, no como certificación.'},
      'estandarizacionEditorial20261031': {'nivel1Capitulos': 14, 'indiceInteractivo': True, 'ciclosSeparados': True, 'calculosModificados': False, 'auditoriaEconomicaEjecutada': False, 'completitudInvestigacion': 'EN_REVISION_SALVEDADES'}}
    dest = ROOT / f'candidatos/valoraciones/{REV}/ANALISIS_A12_EN_REVISION.json'
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n'); print('escrito', dest.relative_to(ROOT))
