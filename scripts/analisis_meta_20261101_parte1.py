# -*- coding: utf-8 -*-
"""Utilidades y capítulos 1-7 del Nivel 1 de META (revisión META-20261101-A12-R1). Cifras desde la captura de la hoja."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
REV = 'META-20261101-A12-R1'
CAP = json.loads((ROOT / f'evidencia/captura-hoja-20261101/{REV}_resultados_hoja.json').read_text())
D = CAP['data']
V = json.loads((ROOT / f'candidatos/valoraciones/{REV}/VALORACION_A12_EN_REVISION.json').read_text())

def n(x, d=0):
    if isinstance(x, str):
        try: x = float(x)
        except ValueError: return 'N/D'
    if x is None: return 'N/D'
    return f'{x:,.{d}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
def pc(x, d=1): return n(x * 100, d) + ' %'
def usd(x, d=2): return 'US$' + n(x, d)
def table(head, rows, cap=None):
    h = ''.join(f'<th>{c}</th>' for c in head)
    b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    c = f'<caption>{cap}</caption>' if cap else ''
    return f'<table>{c}<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'
def P(*a): return '<p>' + ' '.join(a) + '</p>'

IS = D['is']; CF = D['cf']
yrs = [str(x) for x in IS[1][1:12]]
def ser(t, i): return t[i][1:12]
rev = ser(IS, 2); gp = ser(IS, 5); rd = ser(IS, 9); ebit = ser(IS, 11); ni = ser(IS, 20); ebitda = ser(IS, 27)
ocf = ser(CF, 12); capex = ser(CF, 14); sbc = ser(CF, 4); fcf = ser(CF, 35); buy = ser(CF, 29); div = ser(CF, 31)
VB = D['valuation_base']; ST = D['stories']
base, cons, disr, opt = ST[1], ST[2], ST[3], ST[4]
b35 = V['valorPrincipal']; mos = V['precioMOS']; price = V['precio']
sc = V['escenarios']; ve = V['valorEsperado']['valor']
proy = V['nivel2ProyeccionBase']; dm = V['descuentoMultiples']; pb = V['puenteEquity']
tv_share = pb['valorTerminalPV'] / pb['sumaPV']
da_ltm = ebitda[10] - ebit[10]
legal = 19881
SD1 = V['sensibilidadDCF']['matrices']['waccVsTerminalGrowth']; SD3 = V['sensibilidadDCF']['matrices']['crecimientoVsMargen']

def chapter(i, title, *body):
    return f'<section id="jmr-n1-chapter-{i}"><h2>{i}. {title}</h2>{"".join(body)}</section>'

def cap1():
    return chapter(1, 'Tesis y resumen ejecutivo',
    P(f'Meta Platforms es la mayor máquina de publicidad digital del mundo y, al mismo tiempo, una de las mayores apuestas de inversión en infraestructura de inteligencia artificial de la historia corporativa. El Método JMR A-1.2 arroja un valor Base de {usd(b35)} por acción, calculado por la hoja oficial de trabajo (<code>Valuation output!B35</code>), un precio de entrada con margen de seguridad del 35 % de {usd(mos)} y una cotización de referencia de {usd(price)} al cierre del 30 de octubre de 2026. La acción cotiza {pc(1-price/b35,0)} por debajo del valor Base, pero {pc(price/mos-1,0)} por encima del precio con margen de seguridad: hay descuento frente al caso central, no el suficiente para cumplir la disciplina de la casa.'),
    P(f'Los cuatro escenarios valen {usd(sc["conservador"])} (Conservadora), {usd(sc["base"])} (Base), {usd(sc["optimista"])} (Optimista) y {usd(sc["disrupcion"])} (Disrupción); el promedio ordinario ponderado de las tres primeras historias es {usd(ve)}. La Optimista supera en {pc(sc["optimista"]/b35-1,0)} al Base y la Conservadora queda {pc(1-sc["conservador"]/b35,0)} por debajo: el rango se explica casi por completo por dos variables que hoy no se observan, cuánto retorno producirá el gasto de capital en IA y cuántos años sostendrá Meta márgenes superiores al 40 %.'),
    '<h3>La tensión central</h3>' + P(
      f'El negocio publicitario es excepcionalmente rentable y crece con fuerza: los ingresos del tercer trimestre de 2026 fueron 64.601 millones (+26 % interanual) y los de los doce meses a septiembre, {n(rev[10])} millones. Pero el flujo de caja libre de esos doce meses fue de solo {n(fcf[10])} millones, frente a {n(fcf[9])} en {yrs[9]} y {n(fcf[8])} en {yrs[8]}, porque el capex pasó de {n(-capex[9])} a {n(-capex[10])} millones. La empresa convierte en inversión una parte creciente de lo que gana. La valoración depende de si ese capital genera retornos suficientes: la Base supone un retorno sobre el capital invertido que baja de {pc(VB[39][2],0)} a {pc(base[6],1)} en el terminal.'),
    '<h3>Lo que el análisis no afirma</h3>' + P(
      f'La revisión se publica como EN_REVISION: tiene controles técnicos aprobados pero no auditoría económica ni verificación visual autenticada. Hay tres salvedades que el lector debe conocer desde el principio. Primera, Meta tiene arrendamientos aún no iniciados por 355.730 millones y compromisos no cancelables por 454.520 millones que la hoja no convierte en deuda. Segunda, se deducen 19.881 millones de provisiones legales, en valor bruto y sin efecto fiscal. Tercera, el valor por múltiplos ({usd(dm["multiplesHoy"]["base"])} en la Base) está {pc(1-dm["multiplesHoy"]["base"]/b35,0)} por debajo del DCF, una brecha que el capítulo 13 explica y no oculta.'))

def cap2():
    return chapter(2, 'Modelo de negocio, segmentos y monetización',
    P('Meta informa dos segmentos: Family of Apps (Facebook, Instagram, Messenger, WhatsApp y otros servicios) y Reality Labs (realidad virtual y aumentada, gafas y hardware de consumo). En el tercer trimestre de 2026 Family of Apps aportó 64.158 millones de los 64.601 millones de ingresos (99,3 %) y Reality Labs 443 millones; en los nueve meses, 180.436 y 1.276 millones sobre 181.712 millones. La publicidad, con 63.061 millones en el trimestre (+26 % interanual) y 177.449 millones en nueve meses, es el 97,6 % del total. Otros ingresos (WhatsApp Business, Meta Verified y otros) suman 1.097 millones. Es un negocio de un solo motor.'),
    P('El motor se mide con tres números. Primero, las personas activas diarias en la Familia de aplicaciones: 3.640 millones en septiembre de 2026 (+3 % interanual). Segundo, las impresiones publicitarias entregadas, que aumentaron 10 % interanual en el trimestre. Tercero, el precio medio por anuncio, que aumentó 14 %. Es decir, algo más de la mitad del crecimiento viene de cobrar más por cada anuncio mostrado y el resto de mostrar más: el producto de ingresos (impresiones por precio) crece alrededor de 25 %, mientras que los usuarios crecen solo 3 %. Que el precio por anuncio suba tanto depende de la calidad de la segmentación y de la medición, es decir, de los modelos de IA que Meta usa para clasificar y recomendar, y esa es la razón económica del gasto de capital que se analiza en el capítulo 8.'),
    '<h3>Rentabilidad por segmento</h3>' + P(
      'El resultado operativo del tercer trimestre fue de 17.117 millones en Family of Apps (margen de 27 %) y una pérdida de 4.129 millones en Reality Labs, con un total de 12.988 millones que incluye el cargo legal de 9.890 millones. En los nueve meses, Family of Apps generó 67.410 millones de resultado operativo. La pérdida de Reality Labs, del orden de 18.000 a 19.000 millones anuales según la guía de la compañía, no se elimina del EBIT de la valoración: es un costo real de una opción de largo plazo cuyo valor no está en los flujos proyectados, y por eso las historias no la tratan como un negocio descontinuado.'),
    '<h3>Estructura de costos</h3>' + P(
      'En el tercer trimestre de 2026 el costo de ingresos fue de 13.369 millones (20,7 % de los ingresos), la investigación y desarrollo de 20.054 millones (31,0 %), marketing y ventas de 3.333 millones (5,2 %) y administración y generales de 14.857 millones (23,0 %). Sin el cargo legal de 9.890 millones, la administración habría sido de 4.967 millones (7,7 %). Hay dos partidas que explican la presión sobre el margen: el costo de ingresos, que incluye depreciación de centros de datos, costos de infraestructura y de capacidad de nube de terceros, y la investigación y desarrollo, que incluye la compensación en acciones de los equipos de IA. Ambas crecen entre 38 % y 48 % interanual en nueve meses, mientras los ingresos crecen 29 %.'),
    '<h3>Dónde se vende</h3>' + table(['Región (dirección del cliente)', 'T3 2026 (M US$)', '9M 2026 (M US$)', 'Peso T3'], [
        ['Estados Unidos y Canadá', '26.217', '71.346', pc(26217/64601)], ['Europa', '14.023', '41.272', pc(14023/64601)],
        ['Asia-Pacífico', '16.993', '48.511', pc(16993/64601)], ['Resto del mundo', '7.368', '20.583', pc(7368/64601)], ['Total', '64.601', '181.712', '100,0 %']],
        'Ingresos por geografía (10-Q, 30-sep-2026).') +
    P('Estados Unidos y Canadá aportan 40,6 % de los ingresos con una fracción pequeña de los usuarios; Asia-Pacífico y el resto del mundo concentran el crecimiento de usuarios pero monetizan menos por persona. Esa asimetría es la fuente de crecimiento orgánico más visible: cerrar parte de la brecha de monetización por usuario sin necesidad de más usuarios.'))

def cap3():
    return chapter(3, 'Industria, mercado direccionable y crecimiento orgánico',
    P('Meta compite en el mercado de la publicidad digital, que se ha concentrado en pocas plataformas capaces de ofrecer escala de audiencia y medición del retorno. Su mercado no está limitado por usuarios, que ya son 3.640 millones de personas al día, sino por el gasto publicitario total que los anunciantes están dispuestos a trasladar de medios tradicionales y de otros canales digitales, y por la eficacia con que la plataforma convierte atención en ventas medibles.'),
    f'<h3>Un crecimiento que ha cambiado de naturaleza</h3>' + P(
      f'Entre {yrs[3]} y {yrs[9]} los ingresos crecieron de {n(rev[3])} a {n(rev[9])} millones, una tasa compuesta de {pc((rev[9]/rev[3])**(1/6)-1,1)} anual, con una sola caída (el año fiscal {yrs[6]}: {pc(rev[6]/rev[5]-1,1)}). En los doce meses a septiembre de 2026 llegaron a {n(rev[10])} millones. El crecimiento de 2026 (+26 % en el tercer trimestre, +28,8 % en nueve meses) es el más alto en cinco años y viene acompañado de un aumento del precio por anuncio de 14 %, no solo de volumen.'),
    '<h3>Por qué la Base desacelera</h3>' + P(
      f'La senda Base de crecimiento anual de ingresos es {", ".join(pc(p["growth"],1) for p in proy)}. Parte de {pc(proy[0]["growth"],1)} en el primer año, por debajo del 26 % del tercer trimestre, y converge a {pc(proy[9]["growth"],1)} en el año 10. La razón es aritmética: si el precio por anuncio subiera 14 % durante cuatro años consecutivos, se acumularía un aumento de 69 %, y la serie histórica no ofrece evidencia de que esa elasticidad se sostenga. El supuesto Base es que los aumentos de precio se normalizan hacia la inflación más una prima por mejor medición.'),
    P(f'Con un LTM de {n(rev[10])} millones, un crecimiento de {pc(proy[0]["growth"],1)} implica {n(proy[0]["revenues"])} millones en los doce meses siguientes. Esa cifra es {pc(proy[0]["revenues"]/(64601*4)-1,1)} superior al tercer trimestre anualizado (64.601 × 4 = 258.404 millones); para alcanzarla exigiría un crecimiento secuencial de alrededor de 4,7 % por trimestre durante los cuatro trimestres siguientes (partiendo de los 64.601 millones del tercer trimestre). Es una trayectoria exigente pero compatible con la del último año: el crecimiento interanual de 26 % equivale a unos 6 % secuenciales, de modo que la Base supone cierta desaceleración y no una aceleración.'),
    '<h3>Fuentes de crecimiento que el modelo no necesita</h3>' + P(
      'La hoja no modela explícitamente nuevos productos de IA generativa (asistentes, suscripciones, publicidad conversacional) ni el hardware de Reality Labs como fuentes separadas de ingreso. Si tienen éxito, aparecen en la historia Optimista (crecimiento compuesto de ' + pc(opt[2], 1) + ' en cinco años y margen objetivo de ' + pc(opt[3], 0) + '); si no, no deterioran la Base. Esta asimetría es deliberada: el modelo valora lo que Meta ya sabe hacer y trata lo demás como opcionalidad dentro de los escenarios extremos.'),
    P('La principal restricción al crecimiento no está en la demanda sino en la regulación y el contexto legal. El propio 10-Q describe investigaciones de fiscales generales y litigios sobre salud mental de menores y redes sociales, además de un escrutinio creciente de las aplicaciones de IA; ambos pueden obligar a cambiar prácticas de producto y de uso de datos que sostienen la segmentación publicitaria.'))

def cap4():
    return chapter(4, 'Ventajas competitivas y competencia',
    P('La ventaja de Meta se apoya en cuatro pilares. El primero es el efecto de red: 3.640 millones de personas al día en cuatro aplicaciones que se refuerzan entre sí, algo que ningún competidor puede replicar con inversión. El segundo, la medición: millones de anunciantes que han construido sus campañas, sus catálogos y sus métricas sobre las herramientas de Meta, con costos de cambio reales. El tercero, los datos: la combinación de señales de comportamiento dentro de la plataforma que alimentan modelos de predicción de conversión. El cuarto, la escala de cómputo que le permite entrenar y operar esos modelos a un costo por usuario que pocos pueden igualar.'),
    '<h3>Competidores y sustitutos</h3>' + P(
      'La competencia por el presupuesto publicitario viene de Google (búsqueda y vídeo), de plataformas de vídeo corto con algoritmos de recomendación, del comercio electrónico con redes de publicidad propias y de las plataformas de publicidad móvil basadas en aplicaciones. La competencia por la atención, a su vez, viene de cualquier producto de consumo que reduzca el tiempo en las aplicaciones de Meta, incluidos los asistentes conversacionales de IA. Ninguno de esos competidores ha reducido el crecimiento de ingresos de Meta en el último año, pero el mercado es dinámico y cualquier cambio de plataforma móvil (sistemas operativos, privacidad, distribución de aplicaciones) puede alterar la economía de la segmentación, como ocurrió en 2022.'),
    f'<h3>La renta que se puede disipar</h3>' + P(
      f'El margen operativo ajustado de {pc(VB[3][1],1)} en el LTM es muy superior al de {yrs[6]} ({pc(ebit[6]/rev[6],1)} GAAP). Una parte es ventaja estructural y otra es el resultado de un ciclo de eficiencia (la plantilla bajó 15 % interanual a 66.775 personas) y de un aumento de precios que se apoya en la mejora del producto. La Base converge a un margen objetivo de {pc(base[3],0)}, la Conservadora a {pc(cons[3],1)}, la Optimista a {pc(opt[3],0)} y la Disrupción a {pc(disr[3],1)}. Hay un hecho que condiciona toda esa discusión: los costos de infraestructura crecen mucho más rápido que los ingresos. El costo de ingresos subió de 25.269 a 34.917 millones entre los nueve meses de 2025 y los de 2026 (+38 %) y la investigación y desarrollo de 40.237 a 59.409 millones (+48 %), por encima del 29 % de crecimiento de ingresos.'),
    P('Por eso la ventaja competitiva de Meta debe leerse con dos preguntas encadenadas. ¿Puede mantener el crecimiento de precio por anuncio? Y, si lo mantiene, ¿cuánto de esa capacidad depende de un nivel de gasto en computación que sus competidores más pequeños no pueden sostener? La respuesta afecta a la duración del foso: una escala de capital que excluye a los competidores es una ventaja; una carrera de gasto en la que Meta debe invertir cada vez más solo para mantener su posición no lo es. El análisis supone lo primero en la Base y lo segundo en la Conservadora y la Disrupción.'),
    P('Un riesgo competitivo adicional es el regulatorio, que opera como un competidor indirecto: el acuerdo multiestatal de agosto de 2026 por 9.890 millones, las investigaciones sobre aplicaciones de IA y las cuestiones de privacidad en Europa restringen lo que Meta puede hacer con los datos que sostienen su ventaja. La hoja no modela una restricción regulatoria estructural; lo hace de forma implícita en el escenario de Disrupción.'))

def cap5():
    return chapter(5, 'Ciclos empresariales, macroeconómicos y de mercado',
    '<h3>Ciclo de la empresa</h3>' + P(
      f'Meta atraviesa una fase de reinversión acelerada tras una fase de eficiencia. La historia reciente tiene tres momentos. En {yrs[5]} y {yrs[6]}, el cambio de privacidad en el sistema operativo móvil dominante, la desaceleración publicitaria y el gasto en el metaverso redujeron el EBIT de {n(ebit[5])} a {n(ebit[6])} millones y los ingresos cayeron {pc(1-rev[6]/rev[5],1)}. En {yrs[7]} y {yrs[8]} vino el ciclo de eficiencia: el margen operativo GAAP pasó de {pc(ebit[6]/rev[6],1)} a {pc(ebit[8]/rev[8],1)}. Desde 2025, el ciclo es de inversión: el capex pasó de {n(-capex[8])} millones en {yrs[8]} a {n(-capex[10])} en el LTM, y el margen GAAP LTM bajó a {pc(ebit[10]/rev[10],1)} por el cargo legal y el costo de computación.'),
    '<h3>Ciclo macroeconómico, monetario y de crédito</h3>' + P(
      'La publicidad es procíclica: los anunciantes recortan presupuesto antes de que lo hagan los consumidores, y los de pequeña y mediana escala, que son los que más crecen en las plataformas de Meta, son los más sensibles. El Treasury a 10 años cerró en 5,29 % el 30 de septiembre y 4,94 % el 30 de octubre de 2026. Para Meta el crédito importa de otra forma: en mayo de 2026 emitió 25.000 millones en bonos sénior de seis series, y la deuda de largo plazo y su parte corriente suman 83.669 millones. El mercado de crédito financia una parte creciente del gasto de capital, directamente y mediante vehículos conjuntos de centros de datos (capítulo 8). Una subida de tasas encarece ese financiamiento y reduce el rendimiento de proyectos que tienen un horizonte de retorno largo.'),
    '<h3>Ciclo de mercado y ánimo inversor</h3>' + P(
      f'En el marco de Howard Marks, la pregunta es qué descuenta la cotización. El múltiplo precio/utilidad histórico al cierre fiscal fue {n(D["trailing"][12][7],1)}x en {D["trailing"][1][7]}, {n(D["trailing"][12][8],1)}x en {D["trailing"][1][8]}, {n(D["trailing"][12][9],1)}x en {D["trailing"][1][9]} y {n(D["trailing"][12][10],1)}x en {D["trailing"][1][10]}, y es {n(D["trailing"][12][11],1)}x sobre la utilidad LTM. El precio sobre flujo de caja libre, en cambio, pasó de {n(D["trailing"][15][8],1)}x a {n(D["trailing"][15][11],1)}x: el mercado paga algo menos por las utilidades y más del doble por cada dólar de caja libre, porque la caja libre cayó. Esa divergencia es el resumen del ciclo de inversión: las utilidades siguen creciendo y la caja que queda para el accionista se contrae.'),
    '<h3>Cómo entra cada ciclo en la valoración</h3>' + P(
      'El ciclo empresarial entra por la senda de crecimiento (de 20 % a 4,5 %) y por el margen objetivo; el ciclo de inversión, por la razón ventas/capital de 0,52 en los primeros cinco años; el ciclo macroeconómico, por el costo de capital (tasa libre de 5,29 % y prima de 3,70 % del mismo corte, WACC inicial de ' + pc(V['tasas']['wacc'], 2) + ' y terminal de 8,99 %); y el ciclo de mercado, por los múltiplos de salida de la regla de ciclo. Ninguno sustituye a las hipótesis explícitas de cada historia.'))

def cap6():
    rows = [[yrs[i], n(rev[i]), pc(gp[i]/rev[i],1), n(rd[i]), n(ebit[i]), pc(ebit[i]/rev[i],1), n(ni[i]), n(ocf[i]), n(-capex[i]), n(fcf[i])] for i in range(11)]
    return chapter(6, 'Estados financieros, rentabilidad y calidad de resultados',
    table(['Año fiscal', 'Ingresos', 'Margen bruto', 'I+D', 'EBIT', 'Margen EBIT', 'Utilidad neta', 'Flujo operativo', 'Capex', 'FCF'], rows,
          'Serie histórica de la hoja (millones de US$; LTM = doce meses a 30-sep-2026).'),
    P(f'La serie describe un negocio de márgenes muy altos que está reinvirtiendo con intensidad creciente. El margen bruto es de {pc(gp[10]/rev[10],1)} en el LTM, el flujo operativo de {n(ocf[10])} millones es {pc(ocf[10]/rev[10],0)} de los ingresos, pero el capex absorbe {pc(-capex[10]/ocf[10],0)} de ese flujo y deja {n(fcf[10])} millones de caja libre.'),
    '<h3>Calidad de los resultados</h3>' + P(
      f'Cuatro advertencias separan la utilidad contable de la caja del negocio. Primera, el EBIT GAAP LTM de {n(ebit[10])} millones incluye un cargo legal de 9.890 millones registrado en el tercer trimestre de 2026 por el acuerdo multiestatal de agosto; sin él, el EBIT sería 89.270 millones. Segunda, la tasa efectiva de impuestos del LTM es de solo {pc(VB[5][1],1)} en la hoja porque en los nueve meses de 2026 la provisión fue de 1.028 millones, un nivel que el modelo no extrapola: usa 17 % en la proyección y 25,37 % en la convergencia. Tercera, la compensación en acciones de {n(sbc[10])} millones LTM equivale a {pc(sbc[10]/rev[10],1)} de los ingresos y {pc(sbc[10]/ocf[10],0)} del flujo operativo; el EBIT GAAP ya la descuenta, el flujo operativo no. Cuarta, el resultado no operativo ("interest and other income") fue de −1.126 millones en nueve meses de 2026 por pérdidas no realizadas netas de 2.680 millones en inversiones, y no forma parte del EBIT ni del flujo del DCF.'),
    '<h3>El tratamiento de la I+D</h3>' + P(
      f'La compañía gastó {n(rd[10])} millones en I+D en los doce meses. La hoja la capitaliza con vida útil de tres años, lo que añade 32.423 millones al EBIT (de 79.380 a 111.803 millones) y 125.559 millones al capital invertido como activo de investigación. El resultado es un margen ajustado de {pc(VB[3][1],1)} en el año base y de {pc(proy[0]["margin"],1)} en el primer año proyectado, no comparable con el margen GAAP de {pc(ebit[10]/rev[10],1)}. Todos los márgenes objetivo de las historias son márgenes ajustados.'),
    P(f'El balance muestra caja y valores negociables de 82.449 millones (11.222 de efectivo y 71.227 de valores), inversiones no cotizadas de 32.624 millones, propiedades y equipo de 253.222 millones (frente a 176.400 al cierre de 2025), activos de derecho de uso de arrendamientos de 26.576 millones, deuda de largo plazo de 80.922 millones más 2.747 corrientes, pasivos por arrendamientos de 31.173 millones y un patrimonio de 272.386 millones. Los impuestos a largo plazo por pagar son 20.521 millones.'))

def cap7():
    cp = [('Conservadora', cons), ('Base', base), ('Optimista', opt), ('Disrupción', disr)]
    rows = [[k, pc(r[1],1), pc(r[2],1), pc(r[3],1), n(r[4],2), n(r[5],2), pc(r[6],1), pc(r[9],1)] for k, r in cp]
    return chapter(7, 'Drivers de crecimiento, márgenes e hipótesis A-1.2',
    P('El Método A-1.2 estima los supuestos con evidencia del negocio y clases de referencia, y los introduce en la hoja, que calcula el valor. Cada historia tiene su crecimiento anual, su margen objetivo, su eficiencia de capital, su retorno terminal y su crecimiento perpetuo. Ninguna cifra de valor se escribe a mano.'),
    table(['Historia', 'Probabilidad', 'CAGR años 1–5', 'Margen EBIT objetivo', 'Ventas/capital 1–5', 'Ventas/capital 6–10', 'ROIC terminal', 'g terminal'], rows, 'Supuestos de las cuatro historias (hoja Escenarios e historias).'),
    '<h3>Crecimiento</h3>' + P(
      f'La senda Base es {", ".join(pc(p["growth"],1) for p in proy)}. Está anclada en el crecimiento de 26 % del tercer trimestre y de 28,8 % de los nueve meses, con una desaceleración que descuenta que el aumento de 14 % en el precio por anuncio no se repetirá año tras año. La Conservadora crece {pc(cons[2],1)} compuesto y la Optimista {pc(opt[2],1)}.'),
    '<h3>Márgenes</h3>' + P(
      f'El margen ajustado parte de {pc(proy[0]["margin"],1)} y converge linealmente al objetivo en el año 5 ({pc(base[3],0)} en la Base). Es una caída de unos {n((proy[0]["margin"]-base[3])*100,1)} puntos que recoge la depreciación y los costos de computación de la nueva infraestructura, que entran en la cuenta de resultados con retraso respecto del capex. El margen ajustado del LTM ({pc(VB[3][1],1)}) está unos 13 puntos por encima del GAAP ({pc(ebit[10]/rev[10],1)}) porque capitaliza la I+D y no depende del cargo legal; el objetivo de 44 % ajustado debe compararse con el 46,3 % actual y no con el margen GAAP.'),
    '<h3>Impuestos y otros</h3>' + P(
      'La tasa usada en la proyección es 17 % y converge a la marginal de 25,37 % hacia el final del período explícito. No se proyectan pérdidas fiscales ni preferentes, y la probabilidad de fracaso es cero. Los cargos legales no se proyectan en los márgenes objetivo, de modo que no hay doble conteo con la deducción del pasivo legal ya devengado en el puente a patrimonio.'),
    '<h3>Qué no se modela</h3>' + P(
      'La hoja no proyecta unidades de usuarios, impresiones ni precio por anuncio por separado: la senda de ingresos es un supuesto agregado. No modela ingresos de nuevos productos de IA ni del hardware de Reality Labs como líneas independientes, ni un cambio de régimen regulatorio más allá de lo que recoge la Disrupción. Tampoco modela la recompra de acciones como creación de valor: el DCF se calcula antes de distribuciones.'),
    P('Los controles de la hoja exigen que el crecimiento terminal no supere la tasa libre de riesgo (5,29 %), que el ROIC terminal sea coherente con g y la reinversión, que la Disrupción no libere capital de forma automática cuando caen las ventas (política «Sin liberación») y que ningún escenario tenga flujos negativos sin justificación. Los cuatro estados de cálculo están en LISTO.'))
