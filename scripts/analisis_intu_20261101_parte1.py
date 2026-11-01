# -*- coding: utf-8 -*-
"""Utilidades y capítulos 1-7 del Nivel 1 de INTU (revisión INTU-20261101-A12-R1).

Las cifras de valoración salen de la captura de la hoja y del JSON de la misma revisión; los hechos del negocio, del
10-K FY2026 (acc. 0000896878-26-000037) y del comunicado del 4T FY26 con la guía FY27 (acc. 0000896878-26-000029).
"""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
REV = 'INTU-20261101-A12-R1'
CAP = json.loads((ROOT / f'evidencia/captura-hoja-20261101/{REV}_resultados_hoja.json').read_text())
D = CAP['data']
V = json.loads((ROOT / f'candidatos/valoraciones/{REV}/VALORACION_A12_EN_REVISION.json').read_text())

def n(x, d=0):
    s = f'{x:,.{d}f}'
    return s.replace(',', 'X').replace('.', ',').replace('X', '.')
def pc(x, d=1): return n(x * 100, d) + ' %'
def usd(x, d=2): return 'US$' + n(x, d)
def table(head, rows, cap=None):
    h = ''.join(f'<th>{c}</th>' for c in head)
    b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    c = f'<caption>{cap}</caption>' if cap else ''
    return f'<table>{c}<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'
def P(*a): return '<p>' + ' '.join(a) + '</p>'

K10 = '<a href="https://www.sec.gov/Archives/edgar/data/896878/000089687826000037/intu-20260731.htm">10-K FY2026</a>'
PR = '<a href="https://www.sec.gov/Archives/edgar/data/896878/000089687826000029/fy26q4earningspressrelease.htm">comunicado del 25-ago-2026</a>'

IS = D['is']; CF = D['cf']; BS = D['bs']
yrs = [str(x) for x in IS[1][1:12]]
def ser(tab, i): return tab[i][1:12]
rev = ser(IS, 2); cogs = ser(IS, 4); gp = ser(IS, 5); rd = ser(IS, 9); ebit = ser(IS, 11); ni = ser(IS, 20)
ocf = ser(CF, 12); capex = ser(CF, 14); sbc = ser(CF, 4); fcf = ser(CF, 35); buy = ser(CF, 29); div = ser(CF, 31)
VB = D['valuation_base']; ST = D['stories']
base, cons, disr, opt = ST[1], ST[2], ST[3], ST[4]
b35 = V['valorPrincipal']; mos = V['precioMOS']; price = V['precio']
sc = V['escenarios']; ve = V['valorEsperado']['valor']
proy = V['nivel2ProyeccionBase']
dm = V['descuentoMultiples']
pb = V['puenteEquity']
tv_share = pb['valorTerminalPV'] / pb['sumaPV']
cagr = lambda r: r[2]
pot = b35 / price - 1

EXTRA = {}   # subsecciones adicionales por capítulo (se completan en la parte 2)

def chapter(i, title, *body):
    return f'<section id="jmr-n1-chapter-{i}"><h2>{i}. {title}</h2>{"".join(body)}{EXTRA.get(i, "")}</section>'


def cap1():
    return chapter(1, 'Tesis y resumen ejecutivo',
    P(f'Intuit se valora aquí como lo que es hoy: la plataforma financiera de las pequeñas empresas y de los consumidores de Estados Unidos. '
      f'QuickBooks lleva la contabilidad, la nómina, los pagos y el capital de trabajo de millones de negocios; TurboTax y ProTax preparan '
      f'declaraciones de impuestos; Credit Karma conecta a consumidores con préstamos, tarjetas y seguros; Mailchimp ofrece marketing por correo. '
      f'En el ejercicio fiscal 2026, cerrado el 31 de julio, los ingresos fueron {n(rev[9])} millones de dólares (+14 %) y el beneficio operativo '
      f'GAAP {n(ebit[9])} millones ({pc(ebit[9]/rev[9])}) ({K10}).'),
    P(f'El valor intrínseco por acción de la historia Base es {usd(b35)}, calculado por la hoja oficial de la revisión con un DCF de flujos de '
      f'caja libres para la empresa a diez años. Con el margen de seguridad del 35 % del Método JMR, el precio máximo de compra es {usd(mos)}. '
      f'El precio de referencia del corte común de la cartera es {usd(price)} (cierre del 30-sep-2026), un {pc(abs(pot),1)} '
      f'{"por debajo" if pot > 0 else "por encima"} del valor Base y {"por encima" if price > mos else "por debajo"} del precio con margen de seguridad.'),
    P(f'Las cuatro historias valen {usd(sc["conservador"])} (Conservadora), {usd(sc["base"])} (Base), {usd(sc["optimista"])} (Optimista) y '
      f'{usd(sc["disrupcion"])} (Disrupción). El promedio ordinario de las tres primeras, ponderado por sus probabilidades (45 %, 22,5 % y '
      f'22,5 %), es {usd(ve)}; la Disrupción, con 10 % de probabilidad, se informa aparte y no entra en ese promedio.'),
    '<h3>Qué tiene que ser cierto</h3>' + P(
      f'La Base parte de la guía oficial para el ejercicio 2027: ingresos de 23.279 a 23.512 millones (+9 % a +10 %) y beneficio operativo GAAP de '
      f'7.408 a 7.490 millones ({PR}). Exige que los ingresos lleguen a {n(proy[4]["revenues"])} millones en el año 5 (crecimiento compuesto de '
      f'{pc(cagr(base),1)}), que el margen operativo, medido con la investigación y desarrollo capitalizada, suba hasta {pc(base[3],1)} y que '
      f'cada dólar de capital nuevo genere alrededor de un dólar de ventas. Con esos supuestos, el capital invertido rinde {pc(VB[39][2],1)} el '
      f'primer año y la empresa conserva un retorno terminal de {pc(base[6],0)}, por encima de su costo de capital.'),
    '<h3>Qué descuenta el precio</h3>' + P(
      f'A {usd(price)}, el DCF inverso de la Base indica que el mercado paga un crecimiento cercano a cero en los años 1 a 5, frente al '
      f'{pc(cagr(base),1)} compuesto de la Base. Es una lectura más cercana a la historia de Disrupción que a la Base: el mercado teme que los '
      f'agentes de inteligencia artificial abaraten la preparación de impuestos y la contabilidad, los dos negocios que más caja generan. '
      f'Esta valoración no descarta ese riesgo, pero lo pondera con un 10 % y lo valora en {usd(sc["disrupcion"])}, todavía por encima del precio de referencia.'),
    '<h3>Lo que el análisis no afirma</h3>' + P(
      'Esta revisión se prepara como candidata a EN_REVISION: las cifras son el resultado de una hoja de cálculo con sus controles técnicos '
      'aprobados (15 de 15 candados, integridad y estados completos sin hallazgos), no una opinión auditada. No se ha realizado la auditoría '
      'económica independiente ni la revisión visual con acceso autenticado. Entre el corte y la redacción la acción subió a US$341,09 (30-oct-2026); '
      'ese precio no se usa, para que la comparación con el resto de la cartera sea homogénea, y se trata como hecho posterior.'))


def cap2():
    return chapter(2, 'Modelo de negocio, segmentos y monetización',
    P(f'Intuit informa dos segmentos. Global Business Solutions atiende a pequeñas y medianas empresas y a los contadores que las asesoran; '
      f'generó 12.900 millones en el ejercicio 2026 (+16 %), de los que el «ecosistema en línea» (QuickBooks Online, pagos, nómina, capital y '
      f'Mailchimp) aportó 9.900 millones (+19 %). Consumer reúne TurboTax, Credit Karma y ProTax y generó 8.600 millones (+11 %) ({PR}). '
      f'Global Business Solutions ya pesa el 60 % de los ingresos, frente al 59 % de los dos años anteriores ({K10}).'),
    P('La lógica económica es la de una plataforma de datos financieros: cada producto capta datos del cliente (contabilidad, nómina, impuestos, '
      'historial crediticio) que mejoran el siguiente producto vendido a esa misma base. QuickBooks cobra suscripciones mensuales y comisiones '
      'por pagos y nómina; TurboTax cobra por declaración, con versiones asistidas por expertos a precios más altos; Credit Karma no cobra al '
      'usuario, sino a los bancos y aseguradoras por cada préstamo, tarjeta o póliza contratada a través de su aplicación; ProTax vende software '
      'a despachos profesionales. Por eso los ingresos de servicio son el 88 % del total (18.911 de 21.448 millones).'),
    '<h3>De dónde viene el crecimiento</h3>' + P(
      f'Los ingresos de Credit Karma crecieron 441 millones en el ejercicio: 235 de préstamos personales, 101 de tarjetas y 85 de seguros ({K10}). '
      'En QuickBooks Online Accounting el crecimiento viene de precios efectivos más altos, más clientes y una mezcla hacia planes superiores. '
      'La empresa agrupa sus apuestas de crecimiento (servicios con expertos, mercado medio con Intuit Enterprise Suite, dinero y préstamos) '
      f'en lo que llama «Big Bets»: crecieron 34 % y ya son el 30 % de los ingresos ({PR}).'),
    '<h3>Dónde se estanca</h3>' + P(
      'TurboTax es la otra cara. Las declaraciones federales hechas con TurboTax bajaron de 39,9 a 39,0 millones (−2 %): las de escritorio −7 % '
      'y las en línea −2 %. El negocio creció en ingresos por precio, por la versión asistida y por productos de dinero, no por clientes. '
      'Mailchimp tampoco crece: la guía de 2027 lo sitúa entre −1 % y 0 %. Estas dos piezas, que juntas suman unos 6.500 millones de ingresos, '
      'son las más expuestas a la inteligencia artificial de terceros y explican buena parte del escepticismo del mercado.'),
    '<h3>Cómo se traduce en la valoración</h3>' + P(
      'Para el DCF se proyectan cuatro bloques con crecimientos propios: QuickBooks y el resto de Global Business Solutions sin Mailchimp '
      '(11.617 millones de base), Mailchimp (1.267), Impuestos —TurboTax y ProTax agrupados porque la plantilla admite cuatro segmentos— '
      '(5.934) y Credit Karma (2.630). La suma reproduce los 21.448 millones del ejercicio 2026. La estacionalidad (TurboTax concentra sus '
      'ventas entre noviembre y abril) no afecta a una valoración anual, pero sí a la lectura de los trimestres.'))


def cap3():
    return chapter(3, 'Industria, mercado direccionable y crecimiento orgánico',
    P('Intuit compite en tres mercados distintos. En software de gestión para pequeñas empresas, QuickBooks es el estándar de facto en Estados '
      'Unidos y compite con soluciones contables en la nube, plataformas de pago que integran contabilidad y bancos que ofrecen herramientas '
      'propias. En preparación de impuestos individuales, TurboTax compite con despachos presenciales y con otros programas '
      'de preparación de impuestos. En marketplaces de crédito para consumidores, Credit Karma compite con agregadores y con los propios '
      'bancos. La industria de referencia de Damodaran es Software (System &amp; Application).'),
    P(f'La empresa no publica un tamaño de mercado auditado que permita convertir su crecimiento en cuota. El 10-K describe un entorno «más dinámico '
      f'y altamente competitivo» en el que los servicios se digitalizan, se vuelven inteligentes y se automatizan, y en el que el abanico de '
      f'opciones del cliente sigue creciendo ({K10}). La lectura de esta revisión es que el mercado direccionable no es el factor limitante: '
      f'el ecosistema en línea crece 19 % con apenas un 8 % de ingresos fuera de Estados Unidos, y el mercado medio con Intuit Enterprise Suite '
      f'es una extensión natural de la misma base.'),
    '<h3>Crecimiento orgánico frente a compras</h3>' + P(
      'Los ingresos pasaron de 5.177 millones en el ejercicio 2017 a 21.448 millones en el 2026. Ese salto incluye dos compras grandes, '
      'Credit Karma y Mailchimp, visibles en los crecimientos de 25 % y 32 % de los ejercicios 2021 y 2022. Sin esos años, '
      'el crecimiento orgánico se ha movido entre 13 % y 16 %. La guía de 2027 (+9 % a +10 %) es la primera desaceleración clara por debajo '
      'de ese rango y se explica por TurboTax (+2 % a +3 %), Mailchimp (−1 % a 0 %) y ProTax (+2 %), mientras QuickBooks mantiene +13 % a +14 % '
      'y Credit Karma +11 % a +13 %.'),
    table(['Ejercicio (julio)'] + yrs[-6:-1], [['Ingresos'] + [n(x) for x in rev[-6:-1]], ['Crecimiento'] + [pc(rev[i]/rev[i-1]-1, 1) for i in range(5, 10)]],
          'Ingresos y crecimiento, millones de US$ (hoja, Income Statement).'),
    '<h3>Visión externa</h3>' + P(
      'Las empresas con más de 20.000 millones de ventas rara vez sostienen crecimientos de doble dígito durante cinco años: la propia escala '
      f'frena el porcentaje. Por eso la Base desacelera de {pc(proy[0]["growth"],1)} en el primer año a {pc(proy[4]["growth"],1)} en el quinto y '
      f'converge al crecimiento terminal de {pc(base[9],0)} en el año 10. La Optimista ({pc(cagr(opt),1)} compuesto) exige que QuickBooks y '
      f'Credit Karma mantengan el ritmo actual; la Conservadora ({pc(cagr(cons),1)}) supone que la inteligencia artificial frena precios y clientes.'))


def cap4():
    return chapter(4, 'Ventajas competitivas y competencia',
    P('La ventaja principal de Intuit es el costo de cambio. Una pequeña empresa que lleva años en QuickBooks tiene allí su contabilidad, sus '
      'clientes, su nómina y la relación con su contador; cambiar de sistema implica migrar datos, reentrenar al personal y coordinarse con el '
      'asesor externo. Los contadores, a su vez, trabajan con QuickBooks y ProTax porque es lo que usan sus clientes: es un efecto de red de dos '
      'lados que se refuerza solo. En impuestos, la ventaja es la marca y los datos del año anterior, que TurboTax precarga.'),
    P(f'Credit Karma añade una ventaja de datos: conoce el perfil crediticio de sus usuarios y puede ofrecer a los bancos clientes con una probabilidad '
      f'de aprobación conocida. Su crecimiento de 20 % en el ejercicio 2026 ({PR}) muestra que esa ventaja sigue monetizándose, aunque depende del '
      f'ciclo de crédito.'),
    '<h3>La prueba de los números</h3>' + P(
      f'Una ventaja competitiva se verifica en el retorno sobre el capital. Con la investigación y desarrollo capitalizada y los arrendamientos '
      f'tratados como deuda, el capital invertido de la hoja es {n(VB[38][1])} millones y el beneficio operativo después de impuestos del año '
      f'base, {n(VB[6][1])} millones: un retorno de {pc(VB[39][1],1)}, por encima del costo de capital de {pc(V["tasas"]["wacc"],2)} a pesar de '
      'que el capital incluye 13.981 millones de plusvalía de compras pasadas. Sin la plusvalía, el retorno sobre el capital orgánico sería mucho mayor.'),
    '<h3>Qué podría erosionarla</h3>' + P(
      'La amenaza no es un competidor tradicional sino un cambio de interfaz. Si un asistente de inteligencia artificial de propósito general '
      'puede leer los extractos bancarios, clasificar gastos y preparar una declaración, parte del valor que hoy captura la interfaz de Intuit '
      'se traslada a quien controle el asistente. La respuesta de Intuit es su propio sistema operativo de inteligencia artificial generativa '
      f'(GenOS) y una estrategia de «agentes» que hacen el trabajo por el cliente con expertos humanos detrás ({K10}). La ventaja de Intuit en '
      'ese escenario son los datos propietarios y la responsabilidad legal: una declaración o una contabilidad incorrecta tiene consecuencias, '
      'y el cliente paga por la garantía.'),
    P(f'La valoración refleja esta tensión con un retorno terminal de {pc(base[6],0)} en la Base, {pc(cons[6],0)} en la Conservadora y '
      f'{pc(disr[6],0)} en la Disrupción, donde la ventaja se erosiona hasta casi igualar el costo de capital terminal de 8,99 %.'))


def cap5():
    return chapter(5, 'Ciclos empresariales, macroeconómicos y de mercado',
    '<h3>Ciclo de vida de la empresa</h3>' + P(
      'En la clasificación de Damodaran, Intuit está en la fase de crecimiento maduro: crece más que la economía, pero cada vez menos; '
      'genera mucha más caja de la que necesita reinvertir; y devuelve el excedente a los accionistas con recompras y dividendos. En esa fase '
      'el valor depende menos de cuánto crezca y más de cuánto tiempo conserve retornos superiores al costo de capital. Las probabilidades de '
      'las historias (45 % Base, 22,5 % Conservadora, 22,5 % Optimista, 10 % Disrupción) son la previa de esa etapa y el control de la cartera '
      'no detectó indicadores que obliguen a moverlas.'),
    '<h3>Ciclo macroeconómico y monetario</h3>' + P(
      'Los ingresos de Intuit son poco cíclicos en impuestos (la declaración es obligatoria) y moderadamente cíclicos en pequeñas empresas: '
      'en una recesión hay menos negocios nuevos y menos nómina que procesar. Credit Karma es la pieza más cíclica: sus ingresos dependen de '
      'que los bancos quieran prestar. Con una tasa libre de riesgo de 5,29 % a diez años en el corte, el costo de capital de la empresa es '
      f'{pc(V["tasas"]["wacc"],2)}; una bajada de un punto en el costo de capital inicial elevaría el valor Base a cerca de '
      f'{usd(V["sensibilidadDCF"]["matrices"]["waccVsTerminalGrowth"]["values"][1][2])} según la matriz de sensibilidad de la hoja.'),
    '<h3>Ciclo de mercado y sentimiento</h3>' + P(
      'Howard Marks recuerda que el riesgo es más alto cuando todos lo creen bajo, y más bajo cuando todos lo temen. En el corte, el precio de '
      f'{usd(price)} implicaba un crecimiento cercano a cero para una empresa que guía +9 % a +10 %, con una volatilidad histórica de un año de '
      '50,65 %, alta para una empresa de su tamaño. Ese es el perfil de un mercado que ha pasado del entusiasmo al miedo con un relato concreto: '
      'la inteligencia artificial como sustituta. En los últimos años Intuit cotizó entre 31,7 y 41,7 veces su EBITDA (percentiles 25 y 75 '
      'de la serie de la hoja; mediana a cinco años de 41,7 veces); en el corte, el precio implicaba una fracción de esos niveles.'),
    P('El ciclo de sentimiento no cambia el valor intrínseco, pero sí la oportunidad. Si la Base es razonable, el miedo ofrece un precio por '
      f'debajo del valor; si la Disrupción se materializa, el precio de {usd(price)} tampoco sería caro frente a su valor de {usd(sc["disrupcion"])}. '
      'El rebote a US$341,09 un mes después del corte muestra lo rápido que puede moverse ese péndulo.'))


def cap6():
    rows = [[yrs[i], n(rev[i]), n(gp[i]), pc(gp[i]/rev[i],1), n(rd[i]), n(ebit[i]), pc(ebit[i]/rev[i],1), n(ni[i])] for i in range(6, 11)]
    return chapter(6, 'Estados financieros, rentabilidad y calidad de resultados',
    P(f'El margen bruto se mantiene alrededor de 80 %: el costo de ingresos fue {n(cogs[9])} millones en el ejercicio 2026 (20 % de las ventas), '
      'compuesto por 4.016 millones de costo de servicio, 63 de producto y 174 de amortización de tecnología adquirida. El margen operativo GAAP '
      f'subió de {pc(ebit[7]/rev[7],1)} en el ejercicio 2024 a {pc(ebit[9]/rev[9],1)} en el 2026 con apalancamiento operativo en ventas y '
      f'administración ({K10}).'),
    table(['Ejercicio', 'Ingresos', 'Utilidad bruta', 'Margen bruto', 'I+D', 'EBIT', 'Margen EBIT', 'Utilidad neta'], rows,
          'Resultados, millones de US$ (hoja; coste de ventas corregido con el 10-K FY2026).'),
    '<h3>Calidad de los resultados</h3>' + P(
      f'La diferencia entre el beneficio operativo GAAP ({n(ebit[9])} millones) y el «no GAAP» que destaca la empresa (8.900 millones) es casi '
      f'enteramente la compensación en acciones ({n(sbc[9])} millones) y la amortización de intangibles comprados. Esta valoración usa el GAAP: '
      'la compensación en acciones es un costo real que se paga con dilución, y la empresa recompra acciones para compensarla. La '
      'reestructuración de 293 millones del ejercicio 2026 se trata como recurrente, porque Intuit la registró también en 2024.'),
    '<h3>Caja</h3>' + P(
      f'El flujo operativo fue {n(ocf[9])} millones y la inversión en activo fijo apenas {n(-capex[9])} millones: el flujo libre contable fue '
      f'{n(fcf[9])} millones, más que la utilidad neta ({n(ni[9])} millones), en parte por la compensación en acciones que no es salida de caja '
      'y por un menor pago de impuestos en efectivo tras la ley fiscal de 2025. Intuit también mueve mucho capital en su negocio de préstamos: '
      'compró 6.800 millones de préstamos a pequeñas empresas, cobró 4.300 y vendió 2.200 durante el ejercicio; esos flujos son operativos y '
      'el saldo de 1.468 millones forma parte del capital invertido.'),
    '<h3>Balance</h3>' + P(
      'La deuda financiera era 7.669 millones al 31-jul-2026 (1.249 con vencimiento en doce meses), frente a 7.200 millones de caja e '
      'inversiones: deuda neta casi nula. Los fondos de clientes (5.038 millones) tienen su pasivo equivalente y no se tratan como caja libre. '
      'La plusvalía (13.981 millones) y los intangibles (4.642) proceden sobre todo de Credit Karma y Mailchimp.'))


def cap7():
    return chapter(7, 'Drivers de crecimiento, márgenes e hipótesis A-1.2',
    P('El Método A-1.2 calibra la valoración con drivers explícitos: crecimiento por segmento, margen objetivo, ventas por unidad de capital '
      'nuevo, retorno terminal y costo de capital. Cada historia es una combinación coherente de esos drivers, no un ajuste del resultado.'),
    table(['Historia', 'CAGR 1–5', 'Margen objetivo', 'Ventas/capital 1–5', 'ROIC terminal', 'Valor/acción'],
          [[k, pc(r[2],1), pc(r[3],1), n(r[4],2), pc(r[6],0), usd(r[7])] for k, r in (('Conservadora', cons), ('Base', base), ('Optimista', opt), ('Disrupción', disr))],
          'Drivers por historia (Escenarios e historias).'),
    '<h3>Crecimiento</h3>' + P(
      f'El primer año de la Base reproduce la guía por segmento: QuickBooks y el resto de Global Business Solutions sin Mailchimp +13,5 %, '
      f'Credit Karma +12 %, Impuestos +2,4 % y Mailchimp −0,5 %, que suman {pc(proy[0]["growth"],2)}. Después cada bloque se modera: QuickBooks '
      'hasta +9 % en el año 5, Credit Karma hasta +7 %, Impuestos se mantiene en +2 % por precio y Mailchimp vuelve a +2 %.'),
    '<h3>Margen</h3>' + P(
      f'Con la investigación y desarrollo capitalizada a tres años, el margen operativo del año base es {pc(VB[3][1],1)} frente al 27,4 % GAAP. '
      f'El primer año proyectado ({pc(proy[0]["margin"],1)}) traslada a esa base la guía GAAP de 2027 (≈31,8 %). El margen objetivo de la Base, '
      f'{pc(base[3],1)} incluyendo el ajuste de arrendamientos, se alcanza en el año 5: equivale a un margen GAAP de alrededor de 33 %, por '
      'debajo del margen no GAAP guiado para 2027 (≈34,7 %), porque la compensación en acciones se considera un costo permanente.'),
    '<h3>Por qué estas hipótesis y no otras</h3>' + P(
      f'Una primera versión de las historias usaba ventas por capital de 1,2 a 1,8. El motor de la cartera advirtió que, con esos valores, el '
      'capital nuevo rendía entre 22 % y 50 %, más del doble del retorno terminal de cada historia, algo incoherente con una empresa cuyo retorno '
      f'ajustado actual es {pc(VB[39][1],1)}. Se bajaron a 0,8–1,1: el capital nuevo de la Base rinde ahora ≈26 %, una vez y media su retorno '
      'terminal. El cambio redujo el valor Base de 416,91 a 402,00 dólares por acción: la coherencia económica cuesta valor, y se prefiere así.'))
