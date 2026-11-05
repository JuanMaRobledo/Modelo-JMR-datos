import json,math,openpyxl
from pathlib import Path
from model import RAW,SCENARIOS,calculate,derive,SOURCES
P=Path(__file__).parent;data=json.loads((P/'results.json').read_text());v=data['results'];b=v['Base'];d=b['derived'];ids=json.loads((P/'identities.json').read_text())
native=openpyxl.load_workbook(P/'aux_native_final.xlsx',data_only=True)
def f(x,n=2):return f'{x:,.{n}f}'
def pct(x):return f'{100*x:.2f}%'
def table(headers,rows):return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join(['---']*len(headers))+'|']+['| '+' | '.join(str(x) for x in r)+' |' for r in rows])
text=f'''# Chipotle Mexican Grill (CMG) — nueva revisión integral candidata

Método JMR A-1.2 · revisión **CMG-20261105-A12-R4** · corte financiero **30-sep-2026** · corte de mercado **04-nov-2026** · elaboración **05-nov-2026, Colombia**.

**Estado: CANDIDATO CON RESERVAS MATERIALES. No es una valoración publicada, certificada ni lista para promover.** El auxiliar económico calcula cuatro historias reproducibles. La copia de la plantilla IA conserva sus fórmulas y notas, pero presenta discrepancias previas respecto al original y un error de referencias que impide conciliar su salida. No se modificó la ficha publicada, el catálogo ni la aplicación. No se abrió PR de publicación porque no pasaron todos los controles.

## Lectura de los resultados

{table(['Historia','Valor auxiliar por acción USD','Probabilidad JMR'],[[k,f(z['value']),pct(z['assumptions']['weight'])] for k,z in v.items()])}

**Base auxiliar: US${f(b['value'])}; precio con MOS35%: US${f(b['mos'])}.** El promedio condicionado a Conservadora/Base/Optimista es US${f(sum(v[k]['value']*SCENARIOS[k]['weight'] for k in ['Base','Conservadora','Optimista'])/.90)}. Disrupción queda fuera de ese promedio. Estas ponderaciones son convenciones JMR, no probabilidades estadísticas estimadas ni prescripciones universales de Damodaran.

Frente al cierre de referencia de US$35,20, el Base auxiliar representa {pct(b['value']/35.2-1)}. La erosión del ROIC14% hacia WACC durante cinco a diez años adicionales produce **US${f(data['duration'][0]['value'])}–{f(data['duration'][1]['value'])}**. Esta alternativa tiene relevancia suficiente para presentarse junto al Base, porque la permanencia de la ventaja es la duda económica central.

## Archivos y autoridad

- [Hoja candidata, copia de la plantilla IA](https://docs.google.com/spreadsheets/d/{ids['candidate']}/edit).
- [Auxiliar económico JMR con cuatro historias, matrices y auditoría](https://docs.google.com/spreadsheets/d/{ids['aux']}/edit).
- [Fotografía de la revisión anterior, preservada en Archivo/CMG](https://docs.google.com/spreadsheets/d/{ids['archive']}/edit).
- [Biblioteca Damodaran–JMR, rama del PR184](https://github.com/JuanMaRobledo/Modelo-JMR/tree/docs/biblioteca-damodaran-jmr-v1-20261105/docs/biblioteca-damodaran).

Se leyeron REGLAS_VIGENTES v33, Método A-1.2, HISTORIAS_A_NUMEROS v2 y los cinco documentos pedidos de la biblioteca. DUOL se utilizó exclusivamente como referencia de razonamiento y problemas de auditoría. No se importó ningún supuesto de DUOL a CMG. La plantilla se identificó mediante `JMR-valuation/reference/plantillas.json`, blob b64c57ed0db55f305edd806d94f14866dcadaee8. Su registro declara47 pestañas, mientras la hoja IA viva copiada tiene51. Se conservaron las51, incluida la restauración de Stories to Numbers, Valuation as picture, Diagnostics y Answer keys.

# Nivel 1 — Análisis fundamental

## 1. Tesis de inversión y conclusión

Chipotle combina un producto reconocible, menú relativamente acotado y operación directa de restaurantes. Esa combinación permite que mejoras pequeñas en velocidad, utilización de cocina y frecuencia se transmitan al beneficio de muchos locales. También hace que una expansión mal ejecutada absorba capital real: construcción, equipos, personal, contratos de alquiler y trabajo de supervisión. No es una plataforma que pueda duplicar ventas prácticamente sin infraestructura adicional.

La tesis Base es que la marca y la operación permiten seguir abriendo locales rentables y recuperar parte de la rentabilidad corporativa reciente. La compañía todavía tiene recorrido físico hasta una red próxima a su aspiración norteamericana de7.000 restaurantes, pero los mejores emplazamientos no son ilimitados. El análisis concede retornos por encima del costo de capital y no interpreta la maduración como desaparición automática de toda ventaja.

La valoración anterior de US$25,25 no constituye una meta. El nuevo auxiliar queda en US$24,31 por una combinación distinta de crecimiento, margen económico, inversión y rentabilidad estable. La cercanía de los números no demuestra que ambos modelos fueran correctos ni permite restar sus cambios como si fueran una revisión de un único supuesto. La revisión oficial nueva sigue pendiente de conciliación técnica y económica completa.

## 2. La empresa y su modelo económico

El negocio consolidado procede fundamentalmente de restaurantes propios. Cada restaurante vende comida y bebidas a un cliente que paga prácticamente de inmediato. No existe una gran cartera de clientes que financiar. La frescura de ingredientes limita inventarios y la relación con proveedores permite cierto financiamiento operativo. El capital de trabajo puede ser negativo sin que eso signifique que no exista inversión para crecer.

Los restaurantes asociados en otros países tienen una economía distinta. Sus ventas brutas pertenecen al operador y no deben agregarse como ventas consolidadas de Chipotle. La compañía tenía20 unidades internacionales operadas por socios a septiembre de2026. En el modelo de ingresos se usa una aproximación por unidades propias y ventas promedio calibrada al consolidado. Las regalías no se desglosan de forma suficiente para crear una proyección independiente fiable. La pequeña diferencia se identifica como límite de agregación y no se rellena con una comisión inventada.

La expresión «restaurantes propios» se refiere a la operación. **No significa que Chipotle sea propietaria de los inmuebles.** Gran parte del soporte inmobiliario se arrienda. Confundir operación directa con propiedad del edificio produce un ROIC demasiado alto y una inversión por apertura demasiado pequeña.

## 3. Industria, competencia y ventaja competitiva

La ventaja potencial empieza en una marca asociada a una propuesta concreta, facilidad de personalización y un formato operativo repetible. La escala puede mejorar compras, aprendizaje, contratación, tecnología y publicidad por local. Chipotlane facilita recogida de pedidos digitales y puede reducir fricción en momentos de alta demanda. Todo ello permite formular una hipótesis de mayor productividad, pero no prueba por sí solo una renta extraordinaria perpetua.

Los costos de cambio del consumidor son reducidos. Una persona puede sustituir Chipotle por otros formatos rápidos, comida preparada, restaurantes locales o comida en casa. No se identificó un efecto de red que obligue a los clientes a permanecer. La fidelidad se infiere de la evolución del tráfico y de la resistencia de la demanda, no de cohortes de retención que el emisor no publica. No se atribuyen porcentajes de fidelización no verificados.

El poder de precios tiene límites visibles. En el tercer trimestre, el precio del menú aumentó2,7%, pero el ticket creció1,3% por una mezcla adversa de1,4%. Esa diferencia desaconseja equiparar subida de precios con mayor disposición de pago del cliente. La marca puede preservar valor y aun así necesitar promociones, innovación y mejor servicio para sostener frecuencia.

## 4. Motores del crecimiento futuro

El auxiliar no empieza con un CAGR elegido. Parte de4.267 restaurantes propios, una media aproximada de unidades durante el LTM y una venta por unidad calibrada a ingresos. Proyecta nuevas unidades netas y comparables. Base añade350 unidades al principio y reduce gradualmente la expansión hasta210 en el año10. La red final alcanza7.227 unidades propias globales, no7.227 unidades norteamericanas ni ventas de socios convertidas artificialmente en propias.

Los comparables Base son2% el primer año,2,5% durante varios años de recuperación y convergen a2%. El crecimiento del consolidado comienza cerca de10,7%, porque combina comparables con el arrastre de aperturas del LTM, y se desacelera hacia5,3% antes de la estabilidad. La media de dos cierres de unidades es una aproximación a la exposición anual, no una reconstrucción mensual de fechas de apertura. Debe contrastarse con cohortes y rampas de maduración cuando estén disponibles.

La expansión internacional admite más recorrido en Optimista, pero exige adaptación, selección de socios y disciplina operativa. No se usa como una línea de ventas exponencial para compensar la saturación doméstica. El escenario optimista termina con8.177 unidades propias globales, una exigencia superior a la aspiración norteamericana vigente y, por tanto, dependiente de nueva evidencia de ejecución.

## 5. Ciclos de la empresa, del mercado y de la macroeconomía

Se clasifica a Chipotle en crecimiento maduro: tiene escala, beneficios y flujo operativo, mientras todavía reinvierte en expansión física. No se trata como una empresa estable sin oportunidades ni como una empresa joven capaz de sostener indefinidamente tasas históricas. La transición se expresa en menos aperturas incrementales, inversión continua y rendimientos marginales más modestos.

La inflación alimentaria y salarial afecta directamente al resultado de restaurante. Una mejora de costos de ingredientes puede coexistir con presión de nómina y gasto corporativo. El crédito también entra por el costo de arrendar nuevos emplazamientos, aunque la compañía no tenga deuda bancaria dispuesta. Por eso un balance sin préstamos no equivale a un negocio sin obligaciones financieras económicas.

El entorno monetario se incorpora con Treasury fechado y prima de patrimonio del mes. No se sumó una prima discrecional al WACC para el mismo riesgo de pérdida de tráfico que ya aparece en los flujos de Disrupción. El movimiento del precio tras resultados revela cambios de expectativas, pero no demuestra que la macroeconomía o el sentimiento hayan alcanzado un máximo o mínimo. No se asigna una fase precisa del ciclo de Howard Marks sin evidencia suficiente.

## 6. Historia financiera y calidad de resultados

Los ingresos FY2025 fueron11.925,6M y el EBIT GAAP1.935,8M. En el LTM hasta septiembre de2026, los ingresos subieron a12.713,5M, mientras el EBIT disminuyó a1.794,9M. Por tanto, la expansión de unidades no se convirtió proporcionalmente en beneficio corporativo. La divergencia obliga a justificar cualquier recuperación del margen y a distinguir crecimiento de ventas de creación de valor.

El CFO LTM fue2.348,0M y el CAPEX838,1M. El CFO se beneficia de movimientos fiscales: la variación LTM de impuestos por pagar/cobrar aporta aproximadamente222,0M. No se extrapoló ese beneficio de caja como si fuese rentabilidad operativa recurrente. Las recompras tampoco son CAPEX ni reinversión operativa. La reclasificación en el candidato separa recompras, transacciones de planes y retenciones fiscales, conservando el total de financiación.

La información histórica2016–2022 se preserva en la fotografía anterior como evidencia heredada, sin afirmar recertificación integral de cada partida en esta revisión. Las partidas materiales recientes2023–2025 y LTM se cotejaron con estados SEC pertinentes. Esto no equivale a completar los diez años más precios históricos anuales y controles de ratios exigidos por una F2 integral. Esa cobertura pendiente se mantiene visible.

## 7. Reinversión, eficiencia del capital y ROIC

Este es el centro de la revisión. El ROIC elevado sin arrendamientos no representa la economía de replicar un restaurante. El capital económico del auxiliar incluye pasivos reconocidos de arrendamiento y excluye caja e inversiones no operativas. El EBIT económico añade un interés implícito estimado, conservando la amortización económica del uso del activo. La tasa y el interés son proxies identificados, no una cifra que Chipotle haya presentado como gasto financiero separado.

Con períodos de septiembre comparables, el capital inicial es6.433,0M y el final7.051,2M. El NOPAT ajustado dividido entre su media produce un ROIC aproximado de23,19%. Este retorno corresponde al conjunto de activos existentes. No es el rendimiento que obtiene automáticamente cada nuevo dólar ni el ROIC marginal perpetuo.

El costo de una apertura no termina en el CAPEX. El proxy de1,55M de inversión física más1,40M de valor presente de alquiler representa2,95M por local. Con ventas maduras3,106M, margen económico18,5% e impuesto25%, el retorno unitario indicativo es14,61%. Si el capital necesario sube a3,50M, ese retorno cae a12,31%; con4M, a10,77%. Estas cifras explican por qué el ROIC terminal14% puede ser defendible, pero condicionado al mantenimiento de la productividad. No convierten el proxy de alquiler por local en un dato observado de nuevas aperturas.

El Sales-to-Capital Base se revisó desde una propuesta inicial1,4×/1,3× a1,5×/1,4× después de contrastarlo con CAPEX, ROU y capital de trabajo. El puente normalizado reciente indica cerca de964M de reinversión y el primer año proyectado requiere993M. Se asume menor eficiencia después del quinto año porque los emplazamientos adicionales necesitan más capital por unidad de ingreso y la productividad inicial deja de mejorar al mismo ritmo. El rango se prueba en matriz, no se oculta dentro de un precio único.

La reinversión pasa de791,4M en año10 a1.142,0M en estabilidad. El FCFF disminuye de3.051,8M a2.854,9M aunque el NOPAT crece4%. La causa es el cambio del rendimiento de nuevas inversiones a14%, no una caída de ventas ni un error de resta. El retorno de la cohorte financiada en año10 y el retorno de las inversiones nuevas desde año11 son magnitudes distintas. El salto44,3% en reinversión requiere una transición económica mejor probada y se conserva como reserva material, con sensibilidad de erosión adicional.

## 8. Dirección, gobierno y asignación de capital

La ejecución requiere formar gerentes, controlar seguridad alimentaria y mantener consistencia en miles de cocinas. Abrir restaurantes sin una organización que los supervise puede elevar ventas y reducir simultáneamente el retorno marginal. El seguimiento debe incluir aperturas netas, maduración y gastos de soporte, no solo el anuncio del número bruto de nuevos locales.

Las recompras reducen acciones y utilizan caja disponible. Son convenientes para el accionista solo si el precio pagado y la estructura financiera permiten crear valor frente a alternativas. En el DCF no se suman las recompras como un beneficio adicional después de reducir las acciones. La SBC permanece como costo en EBIT, las RSU/PSU esperadas se reconocen en el denominador y las opciones pendientes se valoran y restan una vez. Esa política debe revisarse si cambian los premios o el payout de las PSU.

## 9. Nuestro proceso de valoración

Se emplea FCFF como eje económico: ingresos, margen, NOPAT, reinversión y descuento. El auxiliar JMR reproduce esas identidades en fórmulas nativas y se contrasta con un cálculo independiente en Python. No se presenta como un libro original de Damodaran: es una extensión separada autorizada para resolver puentes y escenarios sin editar sus fórmulas.

El libro original identificado es Starbucks2025.xlsx, SHA256220f0ce81d1fba0142adde46cd828940b8a84c6aa0dc8c63ff241a48b7e24a6d. Se usa como patrón de fórmulas y notas, jamás como fuente de ventas o supuestos de CMG. La comparación reveló diferencias de layout y adaptaciones JMR anteriores. Un cotejo por coordenadas produce1.309 diferencias diagnósticas, que no equivalen a1.309 errores semánticos. Las discrepancias materiales demostradas se describen en Nivel2.

## 10. Supuestos económicos y su justificación

La Base permite crecimiento rentable, recuperación del margen corporativo y rendimiento de nuevas unidades superior al WACC. El margen18,5% es económico después del recast financiero y no se compara directamente con el restaurant-level margin. Equivale aproximadamente a un margen GAAP corporativo cercano al nivel de16% si la carga implícita de intereses de alquiler conserva un peso semejante. La reconciliación futura exacta debe moverse junto a los contratos y la red, no mantenerse como un descuento fijo sin evidencia.

El WACC comienza en8,17% y llega a9,18% en estabilidad. Que la tasa terminal sea superior a la inicial es admisible: la beta sectorial actual es inferior a uno, mientras la convención estable de la plantilla equivale a Rf+4,5pp. No se eligió una tasa terminal menor para aumentar el valor. El crecimiento4% respeta la Rf nominal4,68% y queda por debajo del WACC.

El ROIC14% concede un exceso de4,82pp sobre el WACC estable. La objeción más fuerte es que una marca sin costos de cambio relevantes no pueda conservarlo perpetuamente. La respuesta honesta no es afirmar que toda marca tiene un foso amplio: la economía por local indica capacidad de generar ese retorno si productividad, precios y costos de emplazamiento se mantienen. Su persistencia sigue siendo una hipótesis, por eso la erosión finita recibe visibilidad semejante.

## 11. Valoración por escenarios

Conservadora combina menor frecuencia, aperturas más lentas y menor margen. Optimista requiere más tráfico, throughput y capacidad de ejecución, con reinversión eficiente pero positiva. Disrupción modela una pérdida persistente de propuesta de valor y no agrega una probabilidad de quiebra sobre el mismo daño ya descontado en flujos. Las historias son mecanismos distintos y no variaciones porcentuales uniformes del Base.

Las tres historias principales son posibles en capacidad, pero su plausibilidad difiere. La Base utiliza aperturas próximas a la guía inicial y un comparable positivo moderado. La Optimista necesita evidencia adicional de productividad y expansión. Disrupción es un caso de daño estructural, no la continuación automática de un trimestre débil. El juicio «probable» de Base significa central y defendible bajo la información disponible, no una moda o mediana estimada de una distribución.

## 12. Riesgos e invalidación de la tesis

Los riesgos decisivos son pérdida sostenida de frecuencia, deterioro sanitario, inflación de nómina e ingredientes, precios que cambien la mezcla del pedido y selección de ubicaciones de menor rendimiento. La expansión puede ocultar debilidad de unidades maduras durante varios trimestres. También importa que el gasto en equipos y remodelaciones se traduzca en capacidad o ahorro verificable, en lugar de convertirse en una inversión recurrente mayor sin mejora de ventas.

Un comparable positivo originado exclusivamente en precios no confirma la tesis con la misma fuerza que más transacciones. Un margen de restaurante estable tampoco basta si aumentan G&A, depreciación, preaperturas y compensación. Las señales deben medirse conjuntamente y con la definición contable correcta.

## 13. Qué debe ocurrir para que Base sea correcto

Durante los próximos cuatro reportes, la tesis necesita transacciones comparables no negativas de manera sostenida, ejecución de un ritmo de aperturas cercano a la guía y evidencia de que la inversión adicional mejora servicio o productividad. El retorno ajustado de la red debe permanecer por encima del costo de capital sin depender de liberar capital de trabajo indefinidamente.

Dos trimestres consecutivos de transacciones negativas, EBIT GAAP corporativo persistentemente por debajo de14% sin una causa transitoria convincente, o costos de apertura y alquiler que eleven el capital normalizado por local por encima de3,5M justificarían revisar Base. Son disparadores analíticos JMR y no promesas de venta automática. Para Optimista haría falta tráfico y ticket creciendo a la vez, mejoras verificables de throughput y aperturas internacionales con economía comparable al negocio probado.

## 14. Decisión y seguimiento

El negocio puede conservar calidad económica y cotizar por encima de un valor central defendible. Con el cierre de referencia de35,20, el mercado exige resultados más próximos al Optimista o una ventaja más persistente que la Base auxiliar. Un inverso que solo altera comparables necesita aproximadamente{pct(data['inverse']['constant_comps_needed'])} anual constante, manteniendo el resto fijo. Esa es una solución condicionada, no la única historia implícita en el precio.

No se propone sustituir la valoración publicada hasta corregir la conciliación de plantilla, completar los controles y cerrar las reservas indicadas. El expediente permite revisar y discutir los cinco supuestos con números reproducibles. El MOS35% se aplica exclusivamente al Base, no al promedio ni a Disrupción.

# Nivel 2 — Auditoría reproducible

## 1. Identificación, fuentes y unidades

Todos los cálculos monetarios se expresan en USD millones y las acciones en millones. Los informes SEC presentan miles; se dividieron entre1.000. Los datos por acción conservan USD. El cierre de mercado se consultó después de escribir la historia y los supuestos iniciales; el precio anterior había sido visible al recuperar su expediente histórico.

{table(['Fuente','Período / uso'],[[f'[SEC10-Q Q3 2026]({SOURCES["Q3"]})','Estados, leases, acciones, opciones, tráfico y unidades'],[f'[SEC10-K FY2025]({SOURCES["FY25"]})','Estados2023–2025, contratos, costos de apertura y CAPEX'],['[SEC10-Q Q3 2025](https://www.sec.gov/Archives/edgar/data/1058090/000105809025000088/cmg-20250930.htm)','Balance inicial LTM y ventas9M2024'],['[SEC10-K FY2024](https://www.sec.gov/Archives/edgar/data/1058090/000105809025000014/cmg-20241231.htm)','Balance2023/2024 y comparativos'],[f'[Beta sectorial]({SOURCES["beta"]})','64 empresas Restaurant/Dining, enero2026; beta sin deuda0,78 redondeada'],[f'[ERP mensual]({SOURCES["ERP"]})','1-nov-2026:4,41% sobre Treasury; spread soberano0,22pp'],[f'[Treasury]({SOURCES["Rf"]})','10 años04-nov-2026:4,90%'],[f'[Precio histórico]({SOURCES["price"]})','Cierre04-nov-2026:35,20; contrastado con otras fuentes de mercado'],['[ROIC sectorial](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/roc.html)','Restaurantes: lease&R&D ajustado18,36%; no predicción específica de CMG'],['[Leases: nota de Damodaran](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/opler%26d.htm)','Consistencia de EBIT, capital, deuda y retorno'],[f'[Valor terminal]({SOURCES["terminal"]})','Reinversión y exceso de retorno'],['[Narrative and Numbers](https://pages.stern.nyu.edu/adamodar/New_Home_Page/numbers&narrative.htm)','Portal e índices; videos no examinados íntegramente ni transcritos']])}

Los juicios de margen, crecimiento por unidades, eficiencia marginal, ROIC y probabilidades son del analista/JMR. No se atribuyen a Damodaran como conclusiones sobre CMG. La referencia original no autoriza reproducir comentarios extensos en el artículo; se conservan en sus archivos.

## 2. Estados históricos y LTM

{table(['USD M','FY2023','FY2024','FY2025','LTM Sep2026'],[['Ingresos','9.871,649','11.313,853','11.925,601',f(d['revenue'],3)],['EBIT GAAP','1.557,813','1.916,333','1.935,798',f(d['ebit'],3)],['Beneficio neto','1.228,737','1.534,110','1.535,761','1.377,177'],['D&A','319,394','335,030','361,382',f(d['da'],3)],['CFO','1.783,477','2.105,076','2.113,926',f(d['cfo'],3)],['CAPEX bruto','560,731','593,603','666,336',f(d['capex'],3)],['SBC en flujos','124,016','131,730','119,543',f(d['sbc'],3)],['Caja e inversiones corrientes','1.295,447','1.422,915','1.049,136',f(d['cash_total'],3)],['Leases corrientes+largos','4.051,625','4.540,618','5.075,814',f(d['lease'],3)],['Patrimonio','3.062,207','3.655,546','2.830,607','2.455,144']])}

LTM = FY2025+9M2026−9M2025. Ejemplo de ingresos:11.925,601+9.729,966−8.942,090=12.713,477. Ejemplo EBIT:1.935,798+1.374,622−1.515,479=1.794,941. El LTM comparable anterior es11.313,853+8.942,090−8.468,543=11.787,400. Por tanto, el aumento entre LTM homogéneos es926,077, no787,876 (que mezcla LTM y FY).

El detalle capturado por línea está en Income Statement, Balance Sheet y Cash Flow Statement del candidato para2023–2025/LTM. La estructura no contiene líneas separadas de capital común y autocartera: APIC y retained earnings se corrigieron a sus cifras SEC, mientras el total de patrimonio incluye common stock y treasury stock. En2023, retained earnings6.056,985M y treasury stock−4.944,656M explican por qué no debe confundirse el saldo neto1.112,329M con retained earnings publicado. Años2016–2022 no se rellenaron en la copia nueva por mera herencia. Permanecen en la fotografía histórica con estado no recertificado. Faltan los precios FY fechados y la comprobación integral de ratios de dos períodos para completar el gate histórico.

## 3. Ratios y economía del negocio

Margen GAAP LTM=14,1184%; EBIT económico proxy={f(d['ebit_adjusted'],3)}; margen económico={pct(d['ebit_adjusted']/d['revenue'])}. Capital operativo final={f(d['capital'],3)}. Capital inicial Sep25=3.221,838+4.980,117−698,743−722,531−347,694=6.432,987. ROIC ajustado sobre capital promedio≈23,19%; es estimado por el recast, no un ratio publicado por CMG.

El ratio de ventas/capital final≈{f(d['revenue']/d['capital'])}× es promedio y descriptivo. El S/C marginal1,5× es una hipótesis distinta. El RONIC anual se muestra como ΔNOPAT/reinversión del período anterior en las hojas auxiliares. Incluye cambios de margen sobre la red y, por tanto, no identifica aisladamente el rendimiento de la cohorte nueva.

## 4. Puente contable a económico

{table(['Arrendamientos y puente','USD M / tratamiento'],[['Pasivo corriente','321,557'],['Pasivo largo','5.277,474'],['Total reconocido','5.599,031; se resta una sola vez'],['ROU activo','4.928,149'],['Pasivo inicial Sep25','4.980,117'],['Interés implícito estimado',f(d['lease_interest_proxy'],3)+' =media Sep25/Sep26×5,48%'],['Renta fija LTM proxy',f(d['fixed_rent_proxy'],3)+'; escala FY25 por ocupación, no divulgación directa'],['Amortización ROU proxy',f(d['rou_da_proxy'],3)+' =renta fija−interés'],['CAPEX neto físico',f(d['capex']-d['da'],3)],['Adiciones ROU LTM',f(d['lease_add'],3)+'; incluye renovaciones'],['Reinversión antes de NWC',f(d['capex']-d['da']+d['lease_add']-d['rou_da_proxy'],3)]])}

No se añade una segunda deuda por el conversor a los5.599,031M ya reconocidos. El tratamiento financiero del auxiliar exige que la inversión marginal incluya uso de activos arrendados. La comparación operativa experimental que restaba un neto ROU fijo cada año se retiró por incoherente. En su lugar se comprueba una equivalencia financiera FCFF→FCFE con deuda/EV constante y Ke compatible; no se proclama una segunda estimación económica independiente del alquiler.

En el FY2025, los compromisos reconocidos de alquiler sumaban pagos nominales7.474,530M, menos interés imputado2.398,716M, con pasivo5.075,814M. Había834,442M adicionales de pagos de contratos firmados sin comenzar. No se restaron automáticamente como deuda nueva sin el activo, el calendario y las ventas asociadas. El cronograma FY2025 no se presenta como calendario actualizado a Sep26.

I+D no se publica separadamente en el estado utilizado. Se clasifica como no desglosada/incluida en gastos y tecnología, no como cero económico. No se capitalizan publicidad o tecnología por un monto inventado. Los software/equipos ya capitalizados permanecen en PP&E. La salvedad se conserva sin afirmar un conversor I+D certificado.

Caja corriente={f(d['cash_total'],3)}; caja restringida35,799 excluida. Inversiones largas100,365 a valor contable como proxy económico; una pérdida total reduciría el valor en aproximadamente0,079USD/acción, inferior a0,4% individual, aunque no sustituye una tasación. Acciones base1.264,975 más RSU/PSU esperadas4,690 dan1.269,665. SOSAR12,268M, strike39,51, madurez4,2años, volatilidad sectorial41,15% como proxy: valor opciones≈{f(d['option_value'],3)}M. No se asume que una opción fuera de dinero no tenga valor.

## 5. Supuestos efectivos por historia

{table(['Historia','Unidades año10','Ventas año10 M','Margen económico','S/C1–5 /6–10','ROIC marginal terminal','g'],[[k,z['rows'][9]['units'],f(z['rows'][9]['revenue']),pct(z['assumptions']['margin']),str(z['assumptions']['sc1'])+' / '+str(z['assumptions']['sc2']),pct(z['assumptions']['roic']),pct(z['assumptions']['g'])] for k,z in v.items()])}

Las hojas Base/Conservadora/Optimista/Disrupcion del auxiliar contienen las aperturas netas y los comparables por año. No se interpretan como guía del emisor. Un supuesto neto evita ignorar cierres: la prueba alternativa con ocho cierres anuales reduce el valor alrededor de0,8%, con el resto igual. La reconstrucción de ingresos se basa en una media de dos extremos, no en una curva mensual de maduración.

## 6. Costo de capital

{table(['Parámetro','Valor / fórmula'],[['Treasury10Y','4,90%'],['Spread soberano USD','0,22pp'],['Rf ajustada','4,68%'],['ERP sobre Treasury','4,41%'],['ERP sobre Rf ajustada','4,63%'],['Beta sin deuda','0,78; redondeo de tabla sectorial'],['Beta con deuda',f(d['beta'],6)],['Ke inicial',pct(d['ke'])],['Kd antes de impuestos','6,00%; juicio, no cupón emitido'],['Peso deuda a mercado',pct(d['debt_weight'])],['WACC inicial',pct(d['wacc'])],['WACC estable',pct(d['wacc_terminal'])+' =Rf+4,5pp'],['Impuesto marginal','25%']])}

Beta=0,78×[1+(1−25%)D/E]; Ke=Rf+beta×ERP; WACC=Ke×E/(D+E)+Kd×(1−t)×D/(D+E). No existe deuda dispuesta en la línea bancaria de500M a Sep26. Los leases se usan como financiación económica y no se equipara su tasa incremental con un interés bancario observado. La geografía extranjera es pequeña; falta un desglose país suficiente para una prima geográfica ponderada completa. No se inventó una prima de fuera de EE.UU.

## 7. Proyección explícita anual completa
'''
for k,z in v.items():
 text+=f'\n### {k}\n\n'+table(['Año','Unidades','Ventas','g','Margen','NOPAT','Reinversión','FCFF','WACC','Capital inicial'],[[r['year'],r['units'] or 'estable',f(r['revenue']),pct(r['growth']),pct(r['margin']),f(r['nopat']),f(r['reinvestment']),f(r['fcff']),pct(r['wacc']),f(r['capital_begin'])] for r in z['rows']])+'\n'
text+=f'''
Ingresos=unidades promedio×AUV; AUV crece con comparables. EBIT=ventas×margen. NOPAT=EBIT×(1−25%). Con lag1, inversión del año t=MAX(0,(ventas t+1−ventas t)/S/C). El modelo no libera automáticamente capital fijo cuando caen ventas. El lag0 se prueba por separado, incluido terminal. FCFF=NOPAT−reinversión. El ROIC sobre capital promedio, sobre capital inicial y el proxy marginal se calculan por separado en filas37–39 del auxiliar.

## 8. Terminal y puente a la acción

{table(['Base','USD M salvo indicación'],[['Valor operativo EV',f(b['enterprise'],3)],['VP terminal',f(b['pv_terminal'],3)],['Peso terminal / EV',pct(b['terminal_weight'])],['Caja disponible',f(d['cash_total'],3)],['Inversiones proxy',f(RAW['long_investments'],3)],['Deuda lease reconocida',f(d['lease'],3)],['Opciones',f(d['option_value'],3)],['Patrimonio común',f(b['equity'],3)],['Acciones incluyendoRSU/PSU',f(d['shares_total'],3)],['Valor por acción',f(b['value'],6)],['MOS35%',f(b['mos'],6)]])}

Reinversión estable=NOPAT11×g/ROIC marginal terminal. TV10=FCFF11/(WACCestable−g). El g de4% está por debajo de Rf4,68% y WACC9,18%. Las matrices usan3%,3,5%,4%,4,3%,4,6%; no incluyen5% como caso elegible. La transición al ROIC14% explica el salto de inversión del terminal y sigue requiriendo una historia más gradual contrastada con renovación de capital.

## 9. Escenarios, ciclos y duración de ventaja

La previa de crecimiento maduro B/C/O/D=45/22,5/22,5/10% se mantuvo sin ajustes no medidos. No se ponderó Disrupción en el esperado ordinario. Las pruebas3P de capacidad se apoyan en unidades, no en un TAM fabricado. No se obtuvo una distribución homogénea de percentiles de retornos de cadenas operadas directamente. El promedio sectorial mezcla franquicias y operación propia, por lo que se trata como referencia imperfecta.

{table(['ROIC inicial después año10','Años de erosión hasta WACC','Valor auxiliar'],[[pct(x['start']),x['years'],f(x['value'])] for x in data['duration']])}

Estos diagnósticos de duración sustituyen únicamente los flujos posteriores al año10 y conservan el núcleo explícito. Son extensiones auxiliares JMR, no una fórmula nueva atribuida a Damodaran. No se usaron para sobrescribir el libro original.

## 10. Múltiplos prioritarios

Se calcularon cinco comparaciones secundarias con anclasFY+1/+2/+3 y matrices propias. **Su selección económica no está cerrada ni aprobada conforme al contrato JMR. No se usaron para construir un precio ponderado publicable.** La tabla sectorial17,49×EV/EBITDA para empresas con EBITDA positivo es una referencia de enero2026, no un múltiplo independiente actualizado por empresa, ni está plenamente conciliada con el recast de leases de CMG. Las otras anclas son hipótesis para inspección, pendientes de anclas históricas homogéneas, ajuste de tasas y límite fundamental.

{table(['Método','Ancla de trabajo','Fundamental FY+1','FY+2','FY+3','VP+3 auxiliar'],[[native['Multiplos'].cell(i,j).value if j in [3,4] else f(native['Multiplos'].cell(i,j).value) for j in [3,4,5,6,7,10]] for i in range(6,11)])}

Los denominadores de EBITDA y OCF son económicos estimados. El OCF futuro aún necesita conciliar capital de trabajo y SBC con CFO contable. El P/FCFE depende de la política de financiación auxiliar y no se presenta como dinero distribuible publicado. EV/FCFF es muy sensible a la fase de reinversión. Esa dispersión explica por qué no es legítimo promediar automáticamente los cinco precios. P/S y P/BV no se usan ni se ponderan.

## 11. Sensibilidades, DCF inverso y pruebas dinámicas

Cuatro matrices DCF5×5: WACC×g; ROIC marginal terminal×g; comparables×margen; S/C1–5×S/C6–10. El cambio de crecimiento se aplica al motor de comparables que construye ingresos por unidades, no a un CAGR aislado. Hay cinco matrices de múltiplos Base, cada una con su propio fundamentalFY+3. Sus nueve centros concilian, pero ese control matemático no valida la selección económica de los múltiplos.
'''
for name,obj in data['sensitivity'].items():
 text+='\n### '+name+'\n\n'+table(['Δfila / Δcol']+[pct(y) for y in obj['y']],[[pct(x)]+[f(z) for z in row] for x,row in zip(obj['x'],obj['values'])])+'\n'
text+=f'''
Las tablas anteriores reproducen el cálculo independiente; los mismos valores se verifican en fórmulas nativas del auxiliar. En WACC se mueve toda la curva, incluido terminal. El S/C adicional está en la hoja nativa. La prueba dinámica nativa cambió S/C1–5 de1,5 a1,65 y después restauró1,5, comprobando tanto valor como reinversión. Se conservan las lecturas de ida y vuelta en evidencia. Con el saldo lease anterior a la última corrección de período, esa prueba mostró24,313500→24,609290→24,313500; la corrección posterior de interés cambia el Base a24,310268 y se vuelve a verificar la conciliación nativa/Python.

El inverso exige comparables constantes≈{pct(data['inverse']['constant_comps_needed'])} al variar solo ese motor. No infiere una única expectativa de mercado. Lag0 da US${f(data['lag'][0]['value'])}; lag1 US${f(data['lag'][1]['value'])}. Se comparan todos los flujos, no solo la inversión inicial. El lag1 se conserva por la necesidad de invertir y abrir antes de obtener ventas maduras.

## 12. Trazabilidad, comparación anterior y controles

{table(['Supuesto','Publicado anterior A3','Nuevo auxiliar R4','Consecuencia económica'],[['Valor Base','25,246495',f(b['value'],6),'Cambio total≈−3,71%; no atribución aditiva porque cambia arquitectura'],['Crecimiento','Año1 9%; CAGR1–5≈8,40%','Motores: año1≈10,74%; senda anual en tabla','Mayor base de ventas futura, condicionada a aperturas/comparables'],['Margen','GAAP/base14,2%; objetivo17%','GAAP LTM14,118%; económico inicial≈16,40%; objetivo18,5%','No comparar17% y18,5% sin recast: cambia definición'],['S/C1–5 /6–10','2,20 /2,05','1,50 /1,40','Mayor inversión por dólar incremental; incluye leases'],['ROIC terminal','19%','14%','Más reinversión estable y menos valor del crecimiento'],['WACC inicial /estable','7,8109% /8,75%','8,1708% /9,18%','Mayor descuento por tasas y estructura contemporáneas'],['Arrendamientos','5.599,031M reconocidos; tratamiento anterior a revisar','Reconocidos una vez; recast separado','Evita confundir renta operativa y deducción financiera'],['Acciones','1.264,970M en expediente','1.264,975M+4,690M RSU/PSU','Denominador económico mayor y opciones restadas una vez']])}

**Integridad ejecutada:** comparación de las21.856 fórmulas preexistentes,464 notas y33 validaciones entre copia limpia y candidato exportado. No se cambió ninguna fórmula preexistente ni nota, se conservaron las51 pestañas. Input!D12 mostró una diferencia en el caché de exportación `__xludf.DUMMYFUNCTION`; se verificó por conector que la fórmula nativa es idéntica. Las fórmulas nuevas en estados JMR ocupan entradas previamente vacías y reemplazan salidas pegadas por cálculos trazables; no se escribieron en fórmulas originales.

**Diferencias previas con el original:** el original identificado tiene17 hojas; el JMR51. Se preservaron ambos. El cotejo por coordenadas informa estructura/adaptaciones y no acredita equivalencia semántica. La plantilla viva tiene al menos dos problemas materiales comprobados: (1) Valuation output!B27 suma el VP completo del conversor al pasivo registrado si Input!B18=Yes, sin consumir el puente incrementalB79; (2) el cálculo de WACC de los años6–10 produce #VALUE al sumar la referenciaCountry equity risk premiums!B1, que en la plantilla actual devuelve el textoCMG. La propagación afecta valor terminal y equity. No se corrigieron silenciosamente estas fórmulas; activar una salida falsa o pegar el valor auxiliar sobre ellas sería incompatible con el encargo.

**Comprobaciones del auxiliar:** cuatro valores nativos frente a cálculo independiente, identidades NOPAT−reinversión, reinversión estable, cuatro centros DCF y cinco centros de múltiplos, equivalencia FCFE/FCFF de las cuatro historias, ausencia de errores en el auxiliar exportado, prueba dinámica y restauración, y conciliación CFO por cuatro períodos tras reclasificar ajustes y variaciones de leases. Los resultados están enverification.json. La equivalencia FCFE se obtiene con D/EV constante, Ke compatible y ajuste de financiación inicial: no constituye validación independiente de la deuda futura.

**Scripts oficiales:** se recuperaron scripts relevantes. El lanzamiento de diff_formulas_plantilla.py no pudo arrancar por ausencia del paquetejmr_valuation en este entorno; las credenciales de conectores no se trasladaron a un CLI. Se ejecutó una comparación equivalente de exportaciones y lecturas nativas, con sus límites. controles_todas.sh, estados_completos.py, auditar_estados_sec.py, candados.py y CI de publicación NO se certifican como ejecutados/aprobados. El candidato tiene historias oficialesPENDIENTE y no puede pasar de estado por un control auxiliar.

**Revisión económica separada:** otro agente revisó el código y las identidades en modo solo lectura dentro de la misma sesión. Señaló y motivó la retirada de la comparación operativa incorrecta, la separación de ROIC inicial/promedio/marginal, los límites del g, el puente de inversión y el efecto material del fade. No constituye auditoría F5 independiente en otra sesión ni un dictamenAUDITADO.

### Bloqueos materiales para promover

1. Resolver la integración del núcleo original y las referencias rotas mediante mantenimiento separado o un adaptador JMR que permita conciliar la copia oficial, sin modificar fórmulas/comentarios originales. La hoja oficial y el auxiliar todavía no producen una misma salida certificada.
2. Completar el roll-forward de ROU: altas nuevas, renovaciones, bajas, pagos, interés y amortización al mismo corte. El recast actual es económico y trazable, pero utiliza proxies. Acotar inversión de mantenimiento y de expansión durante los diez años.
3. Cerrar la duración del exceso de ROIC y el cambio de reinversión10→11. El Base14% perpetuo es una hipótesis condicionada; el valor20,69–21,14 con ventaja finita es material.
4. Cerrar anclas de múltiplos, normalización de denominadores, ajustes de tasas y límites fundamentales. Las matrices existentes prueban matemáticas, no selección económica final.
5. Completar la historia financiera y los controles de publicación: precios históricos fechados/splits, indicadores de dos períodos, suite técnica y conciliación hoja–JSON–análisis. No hay QA de producción porque no se desplegó.

### Estado de entrega

AISLAMIENTO=OK. Se preservó la publicación anterior y su fotografía en Archivo/CMG. La nueva copia y el auxiliar están en Análisis/CMG. Se entregan investigación, cuatro historias, proyecciones, sensibilidades, comparación y pruebas como candidato. **No se afirma que el proceso integral haya quedado aprobado.** La orden de preparar PR de publicación estaba condicionada a superar todos los controles y esa condición aún no se cumple. No se solicitó autorización para fusionar porque no hay un resultado publicable que aprobar.
'''
close=json.loads((P/'closure_results.json').read_text())
text=text.replace('El OCF futuro aún necesita conciliar capital de trabajo y SBC con CFO contable.','El OCF económico normalizado incorpora ahora ΔNWC, con NWC/ventas de−4,5%, y conserva SBC como costo sin añadirla otra vez. No equivale a CFO GAAP: usa amortización ROU estimada y excluye movimientos fiscales transitorios; su múltiplo necesita anclas homogéneas.')
text=text.replace('El salto44,3% en reinversión requiere una transición económica mejor probada y se conserva como reserva material, con sensibilidad de erosión adicional.','El salto44,3% se contrasta al cierre con transiciones graduales de cinco y diez años, que elevan el valor a24,57–24,80. Su impacto es menor que el de extinguir por completo la ventaja competitiva.')
text=text.replace('3. Cerrar la duración del exceso de ROIC y el cambio de reinversión10→11. El Base14% perpetuo es una hipótesis condicionada; el valor20,69–21,14 con ventaja finita es material.','3. La duración del exceso de ROIC es un riesgo económico explícito: Base14% perpetuo frente a20,69–21,14 por acción con ventaja finita. La transición10→11 ya se probó en cinco y diez años; no se confunde la incertidumbre de la tesis con un error aritmético.')
text+='''

## 13. Cierre adicional reproducible — 5 de noviembre de 2026

El cierre no cambia el Base ni lo promueve a resultado aprobado. Añade la pestaña independiente **Cierre JMR** al auxiliar; la copia IA conserva sus51 pestañas. El auxiliar tiene11, porque no es la plantilla oficial.

### Arrendamientos: residuos visibles

Pasivo final = pasivo inicial + altas estimadas + interés estimado − pagos + residual. Las altas ROU se usan como proxy de altas de obligaciones; pueden diferir por incentivos, anticipos y modificaciones. El residual no se atribuye a una causa no verificada.

'''+table(['Puente LTM, USD M','Pasivo lease','Activo ROU'],[
['Saldo inicial Sep25','4.980,117','4.385,099'],
['Altas ROU; proxy de altas de pasivo',f(d['lease_add'],3),f(d['lease_add'],3)],
['Interés estimado / bajas',f(d['lease_interest_proxy'],3),'−9,194'],
['Pagos / amortización estimada','−'+f(d['lease_cash'],3),'−'+f(d['rou_da_proxy'],3)],
['Residual sin clasificación probada',f(close['lease_liability_residual'],3),f(close['rou_residual'],3)],
['Saldo observado Sep26',f(d['lease'],3),f(RAW['rou'],3)]])+'''

Los residuos equivalen al0,55% del pasivo final y−0,12% del ROU. La proximidad del puente no valida por sí sola el interés ni la amortización estimados: errores en componentes pueden compensarse. El límite material permanece en la identificación de altas por aperturas/renovaciones y la senda futura de contratos; no en ocultar estos residuos mediante una partida inventada.

### Transición terminal sin salto inmediato

La rentabilidad marginal implícita en financiar el crecimiento estable con la inversión del año10 es NOPAT10×g/reinversión10 =19,425%. En dos extensiones JMR se conserva el pronóstico de los diez años y se hace converger ese retorno hacia14% durante cinco o diez años adicionales. La primera reinversión crece4%, acompasada con el NOPAT; después aumenta a medida que cae el rendimiento marginal. Al terminar cada transición se aplica la identidad estable con14%.

'''+table(['Transición después año10','Valor / acción','Incremento frente Base'],[[str(x['years'])+' años',f(x['value'],6),pct(x['value']/b['value']-1)] for x in close['transition']])+'''

Ambas conservan14% después de la transición. Son diferentes de extinguir el exceso de retorno hasta WACC. La selección Base exige que marca, productividad y ejecución permitan sostener retornos marginales superiores al costo de capital; si no ocurre, la alternativa de ventaja finita resulta más pertinente. No se atribuye esta selección a Damodaran.

### OCF y cinco múltiplos

Se corrigieron los tres denominadoresFY+1/+2/+3 de P/OCF para restar ΔNWC. Fórmula normalizada: NOPAT−interés financiero×(1−tasa)+D&A física+amortización ROU−ΔNWC. NWC=−4,5% de ventas; el crecimiento libera ese capital de trabajo en esta hipótesis. SBC sigue en gastos y no se suma al flujo normalizado. Las cinco matrices permanecen calculadas y sus centros concilian con cada salida propia. La corrección no aporta por sí sola anclas históricas comparables ni aprueba los cinco múltiplos.

### Evidencia de este cierre

`close_review.py` genera el puente y las dos transiciones, `closure_results.json` conserva el cálculo independiente y `closure_native.json` la lectura de fórmulas y valores de Google Sheets. `verify_close.py` contrasta los resultados y el libro auxiliar exportado. Los nuevos diagnósticos se agregan a las29 comprobaciones anteriores; no se presentan como suite oficial de publicación.

El expediente queda **entregado para revisión, con promoción bloqueada**. No se abrió un PR de publicación ni se fusionó o desplegó. Para aprobar la integración se necesitan una solución autorizada y comprobada al defecto de la plantilla, conciliación completa del recast, cierre económico de anclas de múltiplos y los controles oficiales con la historia financiera exigida. La publicación anterior permanece vigente.
'''
(P/'CMG_R4_ANALISIS_NIVEL_1_2.md').write_text(text,encoding='utf8')
print(len(text),'chars',len(text.split()),'words')
