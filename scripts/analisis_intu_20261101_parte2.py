# -*- coding: utf-8 -*-
"""Capítulos 8-14 del Nivel 1 de INTU (revisión INTU-20261101-A12-R1)."""
from analisis_intu_20261101_parte1 import *

def vrow(i): return VB[i][2:12]
sc_ratio = vrow(37); inv_cap = vrow(38); roic = vrow(39)
tcf = VB[15][1]; tv = VB[17][1]; pvtv = VB[18][1]; pv10 = VB[19][1]
wacc0 = V['tasas']['wacc']; waccT = V['tasas']['waccTerminal']
rein = [p['reinvestment'] for p in proy]

SD3 = V['sensibilidadDCF']['matrices']['crecimientoVsMargen']; SD1 = V['sensibilidadDCF']['matrices']['waccVsTerminalGrowth']
SD2 = V['sensibilidadDCF']['matrices']['waccVsTerminalROIC']
TV = D['trailing']
ltm_mult = {'EV/EBITDA': TV[20][11], 'EV/FCFF': TV[23][11], 'P/E': TV[12][11], 'P/FCFE': TV[15][11], 'P/OCF': TV[14][11]}
def mult_row(tab):
    t = D['mult_' + tab]
    return [t[7][7], t[18][7], t[29][7]]
MT = {'EV/EBITDA': 'EVEBITDA', 'EV/FCFF': 'EVFCFF', 'P/E': 'PE', 'P/FCFE': 'PFCFE', 'P/OCF': 'POCF'}
fx = lambda x: (n(x, 1) + 'x') if isinstance(x, (int, float)) else 'N/D'


def cap8():
    rows = [[f'Año {i+1}', n(proy[i]['revenues']), n(rein[i]), n(sc_ratio[i], 2), n(inv_cap[i]), pc(roic[i], 1)] for i in (0, 1, 2, 4, 9)]
    return chapter(8, 'Reinversión, capital invertido y Sales-to-Capital',
    P('La reinversión es el puente entre el crecimiento y el flujo libre. Una empresa de software reinvierte sobre todo en investigación y '
      'desarrollo, en compras de otras empresas y, en el caso de Intuit, en los préstamos que concede a sus clientes. La inversión en activo fijo '
      f'es pequeña: {n(-capex[9])} millones en el ejercicio 2026 frente a {n(rd[9])} millones de investigación y desarrollo.'),
    P(f'En el Método A-1.2 la reinversión se calcula como el aumento de ventas dividido por la relación ventas/capital nuevo. En la Base esa relación '
      f'es 1,0 antes de añadir el capital de los arrendamientos ({n(sc_ratio[0],2)} con ellos): cada dólar adicional de ventas exige alrededor de un '
      f'dólar de capital nuevo. Con ello, la reinversión del primer año es {n(rein[0])} millones, alrededor de un tercio del beneficio operativo '
      'después de impuestos, y el flujo libre para la empresa es el resto.'),
    table(['Año', 'Ingresos', 'Reinversión', 'Ventas/capital', 'Capital invertido', 'ROIC'], rows, 'Reinversión y retorno en la historia Base (Valuation output).'),
    '<h3>Por qué 1,0 y no la media del sector</h3>' + P(
      'La media de Damodaran para software de aplicaciones es 1,54. Intuit, con su plusvalía y su investigación capitalizada, rota su capital '
      'histórico a unas 0,8 veces. Para el capital nuevo se elige 1,0 en la Base, 0,9 en la Conservadora, 0,8 en la Disrupción y 1,1 en la '
      'Optimista: incluye que Intuit seguirá comprando empresas, como ha hecho en la última década, y que el negocio de préstamos crece con '
      'el capital propio. La prueba de coherencia es el retorno del capital nuevo, margen × (1 − impuesto) × ventas/capital: en la Base es '
      'cercano a 26 %, una vez y media el retorno terminal de 18 %, lo que deja espacio a que los retornos excedentes se reduzcan con el tiempo.'),
    '<h3>Retornos que se sostienen</h3>' + P(
      f'El retorno sobre el capital invertido sube de {pc(roic[0],1)} en el primer año a {pc(roic[9],1)} en el décimo porque el margen mejora más '
      'deprisa que el capital. Después del año 10, el terminal se calcula con un retorno de 18 %: la reinversión terminal es el crecimiento '
      f'dividido por ese retorno ({pc(base[9]/base[6],1)} del beneficio después de impuestos), lo que deja un flujo terminal de {n(tcf)} millones.'))


def cap9():
    sh = pb['acciones']
    return chapter(9, 'Accionistas, dilución, recompras y gobierno',
    P(f'Intuit devuelve casi todo su flujo libre. En el ejercicio 2026 recompró acciones por {n(-buy[9])} millones (+96 % frente al año anterior) '
      f'y pagó {n(-div[9])} millones en dividendos. Las recompras redujeron un 2 % el promedio de acciones diluidas pese a la emisión por '
      f'compensación en acciones; quedan 7.900 millones de autorización y el dividendo trimestral subió 15 %, a 1,38 dólares ({PR}).'),
    P(f'La hoja valora el patrimonio con {n(sh,1)} millones de acciones en circulación. Las acciones restringidas sin consolidar (13,46 millones) '
      'no se restan aparte: su costo ya está en la compensación en acciones que reduce el beneficio operativo GAAP de cada año proyectado. '
      'Las opciones son pocas y están fuera del dinero: 1,24 millones con un precio medio de ejercicio de 549,37 dólares y 3,86 años de plazo '
      f'({K10}). Valoradas con su volatilidad histórica de 50,65 % y un dividendo de 2,0 %, valen {n(pb["opciones"],1)} millones, que se restan del patrimonio.'),
    '<h3>Recompras a qué precio</h3>' + P(
      'Las recompras crean valor solo si se hacen por debajo del valor intrínseco. Esta revisión no reconstruye el precio medio pagado en el '
      f'ejercicio; con un valor Base de {usd(b35)} y un precio en el corte de {usd(price)}, las recompras al precio de esa fecha habrían sido '
      'favorables para los accionistas que no venden. A precios cercanos al valor, son neutrales.'),
    '<h3>Gobierno</h3>' + P(
      'El presidente y consejero delegado, Sasan Goodarzi, ha concentrado la estrategia en la plataforma de agentes de inteligencia artificial '
      'con expertos humanos y en las «Big Bets». La empresa tiene una sola clase de acciones, sin estructuras de control dual. El riesgo de '
      'gobierno relevante para el inversor es la asignación de capital: las dos compras grandes de la década añadieron 13.981 millones de '
      'plusvalía que todavía deben justificarse con retornos; Mailchimp no crece.'))


def cap10():
    return chapter(10, 'Coste de capital, tasas y fechas',
    P('Todas las tasas son de la misma fecha, el 30-sep-2026, corte común de la cartera: rendimiento del bono del Tesoro a diez años de 5,29 % '
      '(FRED, DGS10) y prima de riesgo de acciones implícita de 3,70 % (Damodaran, octubre de 2026). El precio de referencia es el cierre de '
      f'ese mismo día, {usd(price)}.'),
    table(['Componente', 'Valor', 'Fuente o criterio'],
          [['Beta apalancada', '1,25', 'Bottom-up, Software (System & Application), tabla de EE.UU.; ~92 % de ventas en EE.UU.'],
           ['Prima de riesgo por regiones', '3,84 %', 'EE.UU. 92 % + internacional sin desglose 8 % (10-K FY2026)'],
           ['Costo del patrimonio', pc(dm['costoPatrimonio'], 2), 'Rf + beta × prima'],
           ['Costo de la deuda antes de impuestos', '5,92 %', 'Calificación sintética (EBIT/intereses ≈ 23 veces)'],
           ['Peso de la deuda', '9,3 %', 'Valor de mercado, con arrendamientos'],
           ['WACC inicial', pc(wacc0, 2), 'Cost of capital worksheet (Detailed, VALIDADO)'],
           ['WACC terminal', pc(waccT, 2), 'Rf + prima madura del corte'],
           ['Crecimiento terminal', pc(base[9], 1), 'Corte vigente (4 % con techo en la Rf)']],
          'Costo de capital (hoja).'),
    P(f'El WACC inicial de {pc(wacc0,2)} converge en los años 6 a 10 al terminal de {pc(waccT,2)}, que supone que Intuit será entonces una empresa '
      'de riesgo medio. La beta bottom-up se prefiere a la de regresión porque la acción ha tenido en 2026 una volatilidad atípica (50,65 % a un '
      'año) que mide sentimiento, no riesgo del negocio.'),
    '<h3>Fechas</h3>' + P(
      'Estados financieros: ejercicio cerrado el 31-jul-2026 (10-K presentado el 9-sep-2026). Guía: comunicado del 25-ago-2026. Mercado: 30-sep-2026. '
      'Hecho posterior conocido y no incorporado: cierre de US$341,09 el 30-oct-2026. Próximo dato relevante: resultados del primer trimestre '
      'del ejercicio 2027, en noviembre de 2026, con la guía de 4.294 a 4.313 millones de ingresos (+11 %).'))


def cap11():
    return chapter(11, 'Historias, probabilidades y señales de refutación',
    '<h3>Base (45 %): plataforma que crece con QuickBooks y Credit Karma mientras TurboTax se estanca</h3>' + P(
      f'La guía de 2027 se cumple y los segmentos se moderan con la escala. El margen GAAP sube a ~33 % por apalancamiento operativo. Valor {usd(sc["base"])}. '
      'Se refuta si Global Business Solutions crece menos de 11 % en el ejercicio 2028 o si el margen GAAP no supera el 32 %.'),
    '<h3>Conservadora (22,5 %): la inteligencia artificial comprime precios</h3>' + P(
      f'Asistentes gratuitos frenan las subidas de precio y aceleran la pérdida de clientes de TurboTax; QuickBooks crece pero más despacio '
      f'({pc(cagr(cons),1)} compuesto para la empresa). El margen se queda cerca de la guía. Valor {usd(sc["conservador"])}. Se confirma con caídas '
      'de unidades de TurboTax de 4 % o más.'),
    '<h3>Optimista (22,5 %): la inteligencia artificial propia amplía el mercado</h3>' + P(
      f'Los agentes de Intuit cobran más por cliente, Intuit Enterprise Suite gana empresas medianas y Credit Karma crece con el crédito '
      f'({pc(cagr(opt),1)} compuesto). El margen sube a 39 % en la base del modelo. Valor {usd(sc["optimista"])}. Se confirma con Global Business '
      'Solutions por encima de 14 % en 2028.'),
    '<h3>Disrupción (10 %): agentes de terceros vuelven commodity el producto</h3>' + P(
      f'Las grandes plataformas de inteligencia artificial preparan impuestos y llevan libros casi sin costo; Intuit pierde precio y clientes y '
      f'gasta más para defenderse; el retorno cae hacia el costo de capital. Valor {usd(sc["disrupcion"])}. Es la historia que el precio del corte '
      'parece descontar, y por eso es la más importante de vigilar.'),
    table(['Indicador', 'Último dato', 'Hacia la Optimista', 'Hacia la Conservadora'],
          [['Crecimiento de Global Business Solutions (sin Mailchimp)', '+13–14 % (guía 2027)', '≥ 13 %', '≤ 10 %'],
           ['Declaraciones federales de TurboTax', '39,0 M, −2 % (2026)', 'Estables o mejor', '−4 % o peor'],
           ['Margen operativo GAAP', '≈31,8 % (guía 2027)', '≥ 32 %', '< 29 %'],
           ['Crecimiento de Credit Karma', '+11–13 % (guía 2027)', '≥ 12 %', '≤ 6 %']],
          'Señales de refutación (ficha de historias).'),
    P('Las probabilidades son juicio del analista, no frecuencias observadas. El control de la cartera las compara con la previa de la etapa de '
      'crecimiento maduro y los ajustes por indicadores; en esta revisión coinciden.'))


def cap12():
    return chapter(12, 'Valor intrínseco, MOS, precio y puente a equity',
    P(f'La suma del valor presente de los flujos de los diez años es {n(pv10)} millones y la del valor terminal, {n(pvtv)} millones: el terminal '
      f'pesa {pc(tv_share,1)} del valor operativo de {n(pb["sumaPV"])} millones, un nivel normal para una empresa que todavía crece.'),
    table(['Concepto', 'Millones de US$'],
          [['Valor operativo', n(pb['sumaPV'])], ['– Deuda (bonos y arrendamientos)', n(pb['deuda'])], ['+ Caja e inversiones', n(pb['caja'])],
           ['+ Activos no operativos', n(pb['activosNoOperativos'])], ['= Patrimonio', n(pb['valorPatrimonio'])], ['– Opciones', n(pb['opciones'], 1)],
           ['Acciones (millones)', n(pb['acciones'], 1)], ['Valor por acción', usd(b35)]],
          'Puente a patrimonio (Valuation output).'),
    P(f'El precio máximo de compra con margen de seguridad del 35 % es {usd(mos)}. En el corte, el precio de {usd(price)} quedaba '
      f'{pc(price/mos-1,1)} por encima de ese nivel y {pc(1-price/b35,1)} por debajo del valor Base: la acción estaba barata frente a la Base, '
      'pero no lo bastante como para cubrir con holgura un error de diagnóstico. Si la Disrupción tiene más probabilidad de la asignada, el '
      'margen de seguridad es justamente lo que protege.'),
    P(f'El valor esperado de las tres historias ordinarias es {usd(ve)}, prácticamente igual a la Base, porque la Conservadora y la Optimista '
      'están a distancias parecidas. El valor principal sigue siendo la Base, como establece el Método JMR; la ponderación con los múltiplos '
      f'({usd(dm["ponderadoHoy"]["base"])}) es una referencia relativa, no el valor intrínseco.'))


def cap13():
    rows = []
    for m in dm['metodos']:
        rows.append([m['nombre'], fx(ltm_mult[m['nombre']]), ' / '.join(fx(x) for x in mult_row(MT[m['nombre']])),
                     usd(m['base']['consolidado']), pc(m['peso'], 0)])
    S1 = SD1['values']; S3 = SD3['values']
    return chapter(13, 'Múltiplos y sensibilidades',
    P('Los cinco múltiplos prioritarios se calculan con la regla de ciclo de la cartera: el múltiplo de salida de cada escenario es el que Intuit '
      'tuvo cuando crecía como ese escenario espera crecer dentro de tres años, ajustado por la diferencia de tipos de interés y limitado por el '
      'múltiplo que justifican los fundamentales de la propia historia. Los pares (Adobe, Microsoft, Oracle, Autodesk, Salesforce y ServiceNow) '
      'solo comprueban.'),
    table(['Método', 'Actual (LTM)', 'Salida Cons/Base/Opt', 'Valor Base hoy', 'Peso'], rows, 'Múltiplos (Descuento de múltiplos y Trailing Valuation).'),
    P(f'El resultado es exigente con Intuit. Como la empresa nunca creció menos de 12,9 % al año en la última década y las historias esperan 5 % a 10 '
      'dentro de tres años, la regla parte del mínimo histórico ajustado por tipos y lo recorta al múltiplo justificado. El valor por múltiplos '
      f'de la Base, {usd(dm["multiplesHoy"]["base"])}, queda un 26 % por debajo del DCF: la brecha supera el ±25 % que la cartera usa como '
      'alarma, y se explica por ese recorte, no por un error de cálculo. Leído al revés, el mercado de otras empresas de software paga múltiplos '
      'mayores, y la historia de Intuit a múltiplos de su propia historia valdría mucho más que su DCF.'),
    '<h3>Sensibilidades del DCF</h3>' + P(
      f'Con el crecimiento terminal fijo en {pc(base[9],0)}, subir el costo de capital medio punto reduce el valor Base a {usd(S1[3][2])} y bajarlo '
      f'medio punto lo eleva a {usd(S1[1][2])}. Con el costo fijo, un crecimiento terminal de 3 % lo reduce a {usd(S1[2][0])}. En la matriz de '
      f'crecimiento y margen, dos puntos menos de crecimiento compuesto en los años 1 a 5 llevan el valor a {usd(S3[1][2])}, y dos puntos menos '
      f'de margen objetivo, a {usd(S3[2][1])}. Las tres matrices tienen su centro en {usd(b35)} y se calculan en la propia hoja.'))


def cap14():
    return chapter(14, 'Catalizadores, riesgos, fuentes y decisiones pendientes',
    '<h3>Catalizadores</h3>' + P(
      'Resultados del primer trimestre del ejercicio 2027 (noviembre de 2026), con la guía de +11 % en ingresos. Temporada de impuestos de 2027 '
      '(enero a abril): unidades y precio de TurboTax. Adopción de los agentes de inteligencia artificial en QuickBooks e Intuit Enterprise Suite. '
      'Ritmo de recompras con la autorización restante de 7.900 millones.'),
    '<h3>Riesgos</h3>' + P(
      'Sustitución por asistentes de inteligencia artificial de terceros en impuestos y contabilidad. Pérdida de clientes de TurboTax. '
      'Ciclo de crédito, que afecta a Credit Karma y a la cartera de préstamos a pequeñas empresas. Regulación de impuestos y de datos personales. '
      'Mailchimp sin crecimiento. Errores en las hipótesis de margen, ventas por capital y retorno terminal, que la sensibilidad muestra materiales.'),
    '<h3>Fuentes</h3>' + P(
      f'Intuit, {K10}, presentado el 9-sep-2026 (SEC, acceso 0000896878-26-000037); Intuit, {PR} con la guía del ejercicio 2027 (SEC, acceso '
      '0000896878-26-000029); Damodaran, prima implícita de octubre de 2026; FRED, DGS10; hoja oficial de la revisión en AAA Finanzas / Análisis / INTU.'),
    '<h3>Decisiones pendientes</h3>' + P(
      'Promoción a EN_REVISION en el catálogo, sujeta a la autorización del usuario y a los controles del repositorio. Revisión visual con acceso '
      'autenticado. Auditoría económica independiente (prompt 3/3). Actualización del corte de mercado de la cartera, que movería el precio de '
      'referencia a US$341,09. Contraste con AZ Stocks, que se mantiene separado y no se mezcla con esta valoración.'))


# ---------------- subsecciones adicionales (profundidad del Nivel 1) ----------------
import analisis_intu_20261101_parte1 as _p1
HM = json.loads((ROOT.parent / 'JMR-valuation/reference/historical_multiples/INTU.json').read_text()) if (ROOT.parent / 'JMR-valuation/reference/historical_multiples/INTU.json').exists() else {}
hm = dict(HM.get('consolidado_vp') or {})

_p1.EXTRA.update({
 2: '<h3>La guía de 2027 línea por línea</h3>' + table(['Línea', 'Guía FY2027 (millones)', 'Crecimiento guiado'],
      [['Global Business Solutions (sin Mailchimp)', '13.068–13.158', '+13 % a +14 %'], ['TurboTax', '5.377–5.453', '+2 % a +3 %'],
       ['Credit Karma', '2.919–2.973', '+11 % a +13 %'], ['ProTax', '659–662', '+2 %'], ['Mailchimp', '1.256–1.266', '−1 % a 0 %'],
       ['Total', '23.279–23.512', '+9 % a +10 %'], ['Beneficio operativo GAAP', '7.408–7.490', '+26 % a +27 %'], ['Beneficio operativo no GAAP', '8.063–8.145', '+17 % a +18 %']],
      'Guía del ejercicio 2027 (comunicado del 25-ago-2026).') + P(
      'La guía contiene dos mensajes. El primero es de mezcla: los negocios que crecen a doble dígito ya son más de dos tercios de los ingresos, '
      'de modo que el crecimiento total depende cada vez menos de TurboTax. El segundo es de margen: el beneficio operativo GAAP crece casi tres '
      'veces más deprisa que los ingresos, porque la reestructuración de 2026 no se repite y porque los gastos de ventas y administración crecen '
      'menos que las ventas. La Base toma la guía de ingresos casi en su punto medio (+9,4 %) y una mejora de margen algo menor que la guiada, '
      'para no depender de que todo el ahorro se materialice.'),
 3: '<h3>Dinámica competitiva por negocio</h3>' + P(
      'En contabilidad para pequeñas empresas el factor decisivo es el ecosistema: integraciones con bancos, con plataformas de pago y, sobre '
      'todo, con los contadores. Un competidor puede ofrecer un programa más barato, pero no puede ofrecer de inmediato la red de profesionales '
      'que conocen QuickBooks. En impuestos individuales el factor decisivo es la confianza y la comodidad: el usuario vuelve porque sus datos '
      'están ahí y porque el producto asume parte del riesgo de error. En crédito al consumidor el factor decisivo es la calidad del emparejamiento '
      'entre usuario y prestamista, que mejora con los datos. Los tres negocios comparten una amenaza: que el punto de entrada del cliente deje '
      'de ser la aplicación de Intuit y pase a ser un asistente de inteligencia artificial general. Por eso esta revisión no trata la inteligencia '
      'artificial como un riesgo genérico, sino como el eje que separa la Optimista de la Disrupción.'),
 4: '<h3>Mapa competitivo</h3>' + table(['Negocio', 'Fuente de la ventaja', 'Amenaza principal', 'Señal a vigilar'],
      [['QuickBooks y servicios en línea', 'Costos de cambio, red de contadores, datos', 'Contabilidad automática en bancos y plataformas de pago', 'Crecimiento de clientes y precio efectivo'],
       ['TurboTax', 'Marca, datos del año anterior, garantía', 'Asistentes de IA que preparan declaraciones', 'Declaraciones federales y precio medio'],
       ['Credit Karma', 'Datos crediticios y emparejamiento', 'Ciclo de crédito; agregadores', 'Ingresos por vertical (préstamos, tarjetas, seguros)'],
       ['ProTax', 'Base instalada en despachos', 'Automatización del trabajo profesional', 'Crecimiento y retención de despachos'],
       ['Mailchimp', 'Escala en pymes', 'Alternativas de marketing más baratas', 'Vuelta al crecimiento']],
      'Ventajas y amenazas (juicio del analista con la descripción del 10-K FY2026).'),
 6: '<h3>Conversión de caja en el tiempo</h3>' + table(['Ejercicio', 'Utilidad neta', 'Flujo operativo', 'FCF', 'Compensación en acciones', 'FCF − compensación'],
      [[yrs[i], n(ni[i]), n(ocf[i]), n(fcf[i]), n(sbc[i]), n(fcf[i] - sbc[i])] for i in range(6, 11)], 'Flujo de caja, millones de US$ (hoja).') + P(
      'Restar la compensación en acciones del flujo libre da una medida más prudente de la caja realmente disponible para el accionista: en el '
      'ejercicio 2026 fueron unos 6.600 millones. Es la cifra que conviene comparar con las recompras, y explica por qué la empresa ha podido '
      'recomprar más de lo que emite y aun así pagar dividendos crecientes. La subida del flujo operativo en 2026 tiene un componente fiscal '
      'transitorio (menor pago de impuestos en efectivo); la valoración no lo extrapola, porque usa la tasa marginal a largo plazo.'),
 8: '<h3>Compras: el capital que más pesa</h3>' + P(
      'La plusvalía de 13.981 millones es el recuerdo contable de las compras de la última década. Que el retorno ajustado del capital siga en torno '
      'a 18 % con esa plusvalía dentro indica que, en conjunto, las compras no han destruido valor; pero no todas rinden igual. Credit Karma crece '
      'al 20 % y es un motor de la Base; Mailchimp no crece y su guía para 2027 es plana. La ventas/capital de 1,0 deja espacio a compras futuras '
      'de un tamaño similar al de los últimos años. Una compra grande que no aporte crecimiento haría que la ventas/capital real fuese menor y, con '
      'ella, el valor: es uno de los riesgos de ejecución que el inversor debe seguir.'),
 9: '<h3>Qué significa para el accionista</h3>' + P(
      f'Con {n(pb["acciones"],1)} millones de acciones, cada 1.000 millones de valor operativo equivalen a unos {n(1000/pb["acciones"],2)} dólares por '
      'acción. La política de devolución hace que el valor por acción crezca más que el valor de la empresa: si Intuit recompra al precio del corte, '
      'cada dólar invertido compra más valor del que cuesta. El riesgo es el inverso: recomprar mucho a precios altos, como pudo ocurrir cuando la '
      'acción cotizaba a múltiplos de 40 veces el EBITDA, transfiere valor a quienes venden.'),
 10: '<h3>Cuánto importa cada componente</h3>' + P(
      'La beta y la prima de riesgo explican casi todo el costo de capital: la deuda pesa menos del 10 % del capital, de modo que el costo de la '
      'deuda apenas lo mueve. Una beta de 1,0 en lugar de 1,25 bajaría el costo del patrimonio cerca de un punto y elevaría el valor de forma '
      'material; una prima de riesgo de 4,5 % lo reduciría en una proporción parecida. Por eso la revisión documenta el origen de cada componente '
      'y no usa una tasa genérica. La matriz WACC × crecimiento terminal del capítulo 13 cuantifica ese efecto sobre el valor Base.'),
 12: '<h3>Leer el precio al revés</h3>' + P(
      'El DCF inverso responde a la pregunta: ¿qué crecimiento haría que el valor de la Base fuese igual al precio? Manteniendo margen, ventas por '
      'capital, costo de capital y terminal de la Base, el precio del corte se justifica con un crecimiento cercano a cero en los años 1 a 5. Es '
      'una expectativa muy por debajo de la guía de la propia empresa y de cualquier año de su historia reciente. O el mercado espera una Disrupción '
      'severa, o paga una prima de riesgo mucho mayor que la que usa esta valoración. La subida del precio a US$341,09 en octubre sugiere que parte '
      'de ese pesimismo se corrigió después del corte.'),
 13: '<h3>Múltiplos históricos como contraste</h3>' + P(
      f'Una lectura independiente aplica a la métrica Base del año 3 los múltiplos que Intuit tuvo en su historia y descuenta el resultado a hoy: '
      f'con el mínimo válido da {usd(hm["min"]) if hm.get("min") else "N/D"}, con el percentil 25 {usd(hm["p25"]) if hm.get("p25") else "N/D"} y con la mediana a cinco años '
      f'{usd(hm["mediana_5a"]) if hm.get("mediana_5a") else "N/D"}. No entra en el DCF ni en la ponderación, porque esos múltiplos se pagaron cuando Intuit crecía más y '
      'los tipos de interés eran más bajos. Sirve para mostrar el tamaño del cambio de percepción: incluso con el múltiplo más bajo de su historia, '
      'la Base valdría más que su DCF. Con el precio del corte, la acción cotizaba a 16,7 veces su utilidad y 11,3 veces su EBITDA de los últimos '
      'doce meses, mínimos de la serie de la hoja.'),
 14: '<h3>Plan de seguimiento</h3>' + table(['Cuándo', 'Qué mirar', 'Qué cambiaría'],
      [['Noviembre de 2026', 'Ingresos y margen del primer trimestre frente a la guía (+11 %)', 'Una desviación de varios puntos movería la Base'],
       ['Enero–abril de 2027', 'Unidades y precio de TurboTax', 'Caídas de 4 % o más hacia la Conservadora'],
       ['Todo el año', 'Crecimiento de QuickBooks y del mercado medio', 'Ritmo sostenido de 13 % o más hacia la Optimista'],
       ['Todo el año', 'Productos de IA de terceros en impuestos y contabilidad', 'Adopción masiva hacia la Disrupción'],
       ['Cada trimestre', 'Recompras, dividendos y compras', 'Una compra grande sin crecimiento reduce el valor']],
      'Seguimiento de la tesis.') + P(
      'Esta revisión debe actualizarse cuando cambie el corte de mercado de la cartera, cuando Intuit publique sus resultados del primer trimestre '
      'del ejercicio 2027 o si alguna señal de la tabla se mueve claramente hacia la Conservadora o la Disrupción.'),
})

_p1.EXTRA.update({
 1: '<h3>La decisión en una frase</h3>' + P(
      f'Intuit es un negocio de alta calidad que el mercado valoraba en el corte como si dejara de crecer. La Base, construida con la guía oficial y '
      f'con hipótesis de reinversión prudentes, vale {usd(b35)}; el precio de compra disciplinado es {usd(mos)}. Por encima de ese precio, la compra '
      'depende de la convicción del inversor en que la inteligencia artificial será, para Intuit, más una herramienta que un sustituto. Por debajo, '
      'el margen de seguridad cubre incluso un error importante en el diagnóstico. Esta revisión no emite una recomendación de compra o venta: '
      'establece el valor, el precio máximo y las señales que confirmarían o refutarían la tesis.'),
 5: '<h3>Cómo se combinan los tres ciclos</h3>' + P(
      'Los tres ciclos no apuntan en la misma dirección. El ciclo de vida empuja hacia un crecimiento menor y una devolución de caja mayor. El ciclo '
      'macroeconómico es neutral: tipos de interés altos encarecen el capital, pero la demanda de impuestos y contabilidad es poco sensible a la '
      'economía. El ciclo de sentimiento, en cambio, estaba en un extremo de pesimismo. Cuando el ciclo de vida y el de sentimiento coinciden en '
      'una narrativa de declive, el precio suele exagerar el cambio de los fundamentales. La disciplina del Método JMR consiste en no dejarse '
      'arrastrar por ninguno de los dos extremos: el valor se calcula con la guía y con retornos coherentes, y el margen de seguridad absorbe el '
      'resto. En términos de Marks, el momento no lo decide la valoración, pero la valoración indica de qué lado del péndulo conviene estar.'),
 7: '<h3>Supuestos que más mueven el valor</h3>' + P(
      'Tres supuestos concentran casi toda la incertidumbre. El crecimiento de QuickBooks, que pesa más de la mitad de los ingresos y en la Base '
      'pasa de 13,5 % a 9 % en cinco años. El margen objetivo, que en la Base supone un margen GAAP de unos 33 % frente al 27,4 % del ejercicio '
      '2026. Y el retorno terminal, que en la Base es 18 % y decide cuánto valor aporta el crecimiento después del año 10. La investigación y '
      'desarrollo capitalizada no cambia el flujo de caja, sino cómo se mide el capital y el margen: sin capitalizarla, el retorno sobre el capital '
      'parecería más alto y la reinversión más baja, con un valor parecido. Se capitaliza porque es la forma más honesta de medir el capital que '
      'sostiene los ingresos de una empresa de software.'),
 11: '<h3>Por qué estas probabilidades</h3>' + P(
      'La previa de la etapa de crecimiento maduro reparte 45 % a la historia central, 22,5 % a cada alternativa simétrica y 10 % a la ruptura. '
      'Podría argumentarse que la Disrupción merece más peso en 2026. Esta revisión la deja en 10 % por dos razones: la guía de la propia empresa '
      'sigue siendo de crecimiento de doble dígito en la mayor parte del negocio, y la Disrupción ya está representada con un valor muy por debajo '
      'del de la Base. Si el usuario o la auditoría económica consideran que su probabilidad es mayor, el efecto sobre el valor esperado es '
      'directo: el promedio ordinario del Método JMR excluye la Disrupción, pero en un valor esperado que la incluya, cada 10 puntos que pasen de la Base a la Disrupción restan unos 21 dólares por acción.'),
})

_p1.EXTRA[12] = _p1.EXTRA.get(12, '') + '<h3>Rango razonable de valor</h3>' + P(
    f'El valor no es un punto sino un rango. Entre la Conservadora ({usd(sc["conservador"])}) y la Optimista ({usd(sc["optimista"])}) cabe la mayor parte '
    'de los resultados plausibles si la tesis de plataforma se mantiene; la Disrupción marca el suelo razonable si no se mantiene. Las matrices de '
    'sensibilidad muestran que cambios moderados en el costo de capital, el crecimiento o el margen mueven la Base en decenas de dólares, no en '
    'cientos. El margen de seguridad del 35 % es más amplio que esas variaciones, lo que lo convierte en una protección adecuada frente a errores '
    'de estimación, aunque no frente a una Disrupción completa.')
_p1.EXTRA[3] = _p1.EXTRA.get(3, '') + '<h3>Qué no se modela</h3>' + P(
    'La valoración no proyecta nuevas compras grandes ni la entrada en negocios distintos de los actuales; tampoco una expansión internacional '
    'significativa, que hoy es apenas el 8 % de los ingresos. Tampoco supone cambios regulatorios en la preparación de impuestos. Si alguno de '
    'esos factores se materializa, se trataría como nueva evidencia y daría lugar a una revisión, no a un ajuste silencioso de esta. La '
    'disciplina de no incorporar opcionalidades sin evidencia es deliberada: el valor de la Base debe sostenerse con lo que la empresa ya '
    'hace y con lo que ha guiado públicamente.')
_p1.EXTRA[10] = _p1.EXTRA.get(10, '') + '<h3>El corte común y el hecho posterior</h3>' + P(
    f'El Método JMR exige que el precio y las tasas sean de la misma fecha y que todas las empresas de la cartera usen el mismo corte, para '
    f'que sus potenciales sean comparables. Por eso esta revisión usa {usd(price)} del 30-sep-2026 aunque se redacta el 1-nov-2026, cuando la '
    'acción cerró a US$341,09. Con ese precio, el potencial hasta la Base se reduciría a cerca del 18 % y la acción quedaría por encima del '
    'precio de compra con margen de seguridad. Cuando la cartera adopte un corte nuevo se actualizarán a la vez el precio, la tasa libre de '
    'riesgo y la prima de riesgo, y la valoración se recalculará en la hoja; ningún precio se cambia a mano en el informe.')
_p1.EXTRA[6] = _p1.EXTRA.get(6, '') + '<h3>Una corrección de datos documentada</h3>' + P(
    'Al revisar los estados de la hoja se detectó que el importador de la SEC no reconocía las etiquetas de coste de ventas de Intuit y las '
    'dejaba en cero, dentro de otros gastos operativos. Para los ejercicios 2024 a 2026 y el LTM se reemplazaron por las cifras del 10-K '
    '(3.465, 3.848 y 4.253 millones), compensando otros gastos para no mover el beneficio operativo; la corrección queda respaldada y anotada '
    'en cada celda. No cambia el valor, porque el DCF parte del beneficio operativo, pero sí la lectura del margen bruto, que pasa de un '
    'imposible 100 % a un 80 % coherente con el negocio. Los ejercicios anteriores a 2024 conservan la presentación del importador.')
