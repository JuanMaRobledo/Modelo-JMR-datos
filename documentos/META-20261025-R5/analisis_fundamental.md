**Nota de publicación R4-A2 (23-oct-2026):** revisión financiera única `META-20261023-r4`, análisis de 18 secciones y auditoría económica publicados conjuntamente con reservas. La validación real de DCF, fórmulas y contrato de matrices pasó. El antiguo `controles_todas.sh META` detectó ausencia de registros en el sistema —no alteró el DCF— y exige regeneración/integración posterior. No se presenta el modelo como certificación contable o económica independiente.

---
schema: "jmr-fundamental-research-v5"
title: "Análisis fundamental de Meta Platforms, Inc."
ticker: "META"
company: "Meta Platforms, Inc."
market: "NASDAQ"
analysis_date: "2026-10-23"
information_cutoff: "2026-10-23"
financial_period: "LTM 2026-09-30"
revision: "META-20261023-r4"
currency: "USD"
language: "es"
generator: "Codex"
publication: "publicada con salvedades"
status: "CON HALLAZGOS"
---

> **Actualización posterior R4-A2 (23-oct-2026):** este expediente conserva los resultados numéricos R4. Después de distinguir materialidad y tipo de evidencia, el dictamen vigente es **VALORABLE PARA USO INTERNO CON SALVEDADES; NO CERTIFICADA; PUBLICADA CON SALVEDADES**. Los faltantes de detalle de Nuevo México, valor justo de inversiones, lease financiero y comparables no bloquean el uso interno del DCF, pero deben permanecer cuantificados y expresamente identificados. La publicación autorizada distingue los controles numéricos ya aprobados y los controles de integración legados pendientes, conservados en la auditoría. Véase [hoja, pestaña «R4 · Remediación riesgos»](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit#gid=26102306) y [PR #140](https://github.com/JuanMaRobledo/JMR-valuation/pull/140).



# Meta Platforms (META)

> **Valor intrínseco base: US$726,65 por acción**
> DCF FCFF,23-oct-2026, revisión R4. Supuestos proyectados y hallazgos económicos identificados.

Índice

1. Resumen ejecutivo
2. Modelo de negocio
3. Segmentos y geografía
4. Industria y crecimiento
5. Calidad del negocio
6. Ventaja competitiva
7. Competencia
8. Gestión y asignación de capital
9. Catalizadores
10. Riesgos
11. Bulls say / Bears say
12. Valor con criterio Damodaran
13. Filosofías de inversión
14. Noticias y eventos recientes
15. Qué vigilar
16. Preguntas abiertas
17. Fuentes
18. Control de calidad final

## 1. Resumen ejecutivo

Meta vende a los anunciantes acceso a atención y herramientas para convertirla en ventas. Facebook, Instagram, Messenger y Whats App aportan distribución y relaciones que tardan años en construirse. El problema económico de esta revisión es determinar cuánto del crecimiento publicitario podrá convertirse en efectivo para el accionista después de financiar infraestructura e investigación en inteligencia artificial. [Meta 10-K, 29-ene-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm)

La actividad comercial sigue creciendo, pero la necesidad de capital crece también. Una mejora del producto puede elevar ingresos y, simultáneamente, disminuir el efectivo distribuible durante varios años. El análisis conserva esa tensión: distingue la franquicia publicitaria rentable del retorno todavía no demostrado de cada nueva inversión en IA. Los escenarios representan desenlaces distintos de monetización y eficiencia, no diferencias arbitrarias en la tasa de descuento. [Meta resultados, 21-oct-2026](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/) [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

- El pagador principal es el anunciante. No hay una suscripción obligatoria de la audiencia que asegure una base contractual de ingresos.
- El crecimiento se explica por impresiones, precio efectivo y mezcla. El precio medio de anuncios no equivale a una tarifa fija que Meta pueda subir sin consecuencias.
- La ventaja central es distribución más aprendizaje y optimización. La amenaza más importante es perder el punto de descubrimiento o el permiso para usar señales de datos.
- La caja operativa supera el beneficio contable, pero contiene compensación en acciones y ajustes no monetarios. El CAPEX absorbe una proporción creciente de esa caja.
- La gestión dispone de horizonte y capacidad financiera para invertir. El control del fundador reduce la influencia del minoritario sobre la asignación de capital.
- Las variables decisivas son productividad del capital nuevo y margen después de sostener el servicio. Crecer sin retorno suficiente no crea valor.
- La evidencia contraria es la rigidez de contratos de capacidad y la diferencia entre adopción de nuevos productos e ingresos rentables. No hay desglose público suficiente del retorno de IA por proyecto.
- La tesis central se debilitaría si el crecimiento publicitario pierde fuerza mientras los compromisos, la depreciación y la dilución siguen aumentando. [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

En el Modelo JMR, Base conserva una desaceleración ordenada del crecimiento y una ventaja durable. Conservadora combina monetización más lenta con erosión parcial de esa ventaja; Disrupción elimina el excedente terminal; Optimista acelera monetización, sin atribuir por ello un retorno perpetuo superior al sector. Estas premisas se explican en las secciones 6 y 12. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

## 2. Modelo de negocio

| Producto / ingresos | Cliente que paga | Necesidad | Cobro | Recurrencia | Driver | Riesgo |
|---|---|---|---|---|---|---|
| Facebook/Instagram/Reels | Anunciantes | Alcance, adquisición, conversión | Subasta de anuncios | Campañas repetidas | Impresiones×precio/mezcla | Competencia y privacidad |
| Whats App / mensajería comercial | Empresas | Conversaciones y servicio | Servicios comerciales | Uso recurrente | Adopción y utilidad | Monetización aún menor |
| Reality Labs | Compradores hardware/software | Experiencias inmersivas | Venta de dispositivos/contenido | Ciclo de producto | Adopción y ecosistema | Pérdidas y sustitución |
| Agentes / enterprise anunciados | Potenciales empresas/usuarios | Automatizar tareas | Modelo comercial no cuantificado | No acreditada | Uso y retención | Costo de cómputo y competencia |

Fuente: [Meta, 10-K, 29 de enero de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm), [Meta, 10-Q, 30 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm); anuncios Muse 8-sep y enterprise 28-sep citados en sección 14. No se atribuye ingreso contractual a productos recién anunciados.

La propuesta al anunciante es una relación entre gasto y resultado: llegar a usuarios relevantes y aprender de respuesta observada. El poder de fijación de precios no procede simplemente de subir una tarifa. En una subasta, más demanda o mejor desempeño puede aumentar el valor pagado; expansión de inventario de menor monetización puede diluirlo. Por ello las mejoras de targeting deben comprobarse con actividad y precio, no solo con una narrativa tecnológica. [Meta, 10-Q, 30 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm)

La descomposición trimestral entre impresiones y precio muestra que interacción y efectividad importan además de usuarios nuevos. Una plataforma madura puede crecer monetizando mejor su base, pero repetir tasas altas indefinidamente exigiría que esa mejora no saturara al usuario ni encareciera demasiado la adquisición para el cliente. META no publica una métrica de churn contractual comparable a Saa S ni un LTV/CAC universal auditado; inventarlos daría visibilidad que la subasta no tiene. [Meta, 10-Q, 30 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm)

La estructura de costos combina infraestructura, personal, desarrollo, seguridad y operación de productos. La dependencia de proveedores de cómputo, chips, energía y sistemas móviles limita la autonomía: mejorar un algoritmo no evita tener que comprar capacidad ni resuelve cambios de permisos de terceros. Una economía por unidad útil requiere observar ingreso por interacción junto con costo de servirla; el emisor no desglosa de forma suficiente la rentabilidad incremental de cada agente. [Meta, 10-K, 29 de enero de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm) [Meta, 10-Q, 30 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm)

La recurrencia es económica, no contractual: las campañas pueden repetirse porque producen resultados, pero un anunciante puede detenerlas o trasladarlas con rapidez. Por eso no se inventan retención neta, cartera de pedidos ni tasas de cancelación propias de una empresa de suscripciones. Los pagos anticipados no transforman el negocio completo en ingresos comprometidos. El capital humano y la infraestructura sostienen el aprendizaje de los sistemas; su costo no desaparece cuando se capitaliza I+D para analizarla. [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

## 3. Segmentos y geografía

Los dos segmentos reportados son Family of Apps y Reality Labs. La participación de ingresos permite entender la dependencia comercial, mientras el resultado operativo revela dónde se consume el excedente. No se asignan ingresos específicos de Muse o rentabilidad por modelo de IA cuando la compañía no los publica. En los primeros nueve meses de 2026, Family of Apps concentra el negocio y Reality Labs continúa con pérdidas. [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

| Segmento / fuente | Ingresos 9M2026 US$ M | Peso | Resultado operativo US$ M | Lectura |
|---|---|---|---|---|
| Publicidad dentro de Fo A | 177.449,00 | 97,65% | Dentro de Fo A | Principal motor comercial |
| Otros Fo A | 2.987,00 | 1,64% | Dentro de Fo A | No atribuir todo a IA |
| Family of Apps total | 180.436,00 | 99,30% | 67.410,00 | Incluye costos de infraestructura y litigios |
| Reality Labs | 1.276,00 | 0,70% | -12.775,00 | Pérdidas grandes frente a sus ventas |
| Consolidado | 181.712,00 | 100,00% | 54.635,00 | No sumar de nuevo publicidad y Fo A |


La geografía de ingresos usa dirección del cliente, no ubicación de todos los usuarios ni de los servidores. Norteamérica aporta alrededor de dos quintas partes y no una mayoría absoluta; de ahí la elección de referencias globales. Un usuario adicional en un mercado con menor monetización no tiene el mismo efecto que uno en Norteamérica. Tampoco una prima por macroregión reproduce exactamente la exposición regulatoria o monetaria de cada país. [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

| Región | Ingresos 9M2026 US$ M | Peso calculado | Crecimiento Q3 interanual |
|---|---|---|---|
| EE. UU. y Canadá | 71.346,00 | 39,26% | 33,00% |
| Europa | 41.272,00 | 22,71% | 18,00% |
| Asia-Pacífico | 48.511,00 | 26,70% | 16,00% |
| Resto del mundo | 20.583,00 | 11,33% | 34,00% |


No se dispone en las fuentes consultadas de una concentración actual por gran anunciante o proveedor de chips expresada en porcentajes homogéneos. Esa ausencia no elimina concentración económica: sistemas móviles, capacidad de cómputo y energía pueden condicionar la operación. Los acuerdos con terceros y las participaciones en centros de datos requieren distinguir propiedad, gasto de servicio, activos en construcción y garantías. La lectura correcta de crecimiento por región tampoco permite atribuir automáticamente el cambio a precio o a volumen sin el desglose correspondiente. [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

## 4. Industria y crecimiento

El mercado económicamente relevante es publicidad digital con medición de respuesta, junto a comunicación comercial y venta de dispositivos. Un TAM de inteligencia artificial no equivale al mercado servible de anuncios de META. No se acreditó una estimación primaria homogénea del tamaño global de publicidad al corte; el análisis usa actividad del emisor y estados de competidores, sin importar cifras promocionales de mercado. [Meta, 10-K, 29 de enero de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm)

La industria puede crecer por traslado de gasto desde medios tradicionales, comercio electrónico y mejores herramientas para negocios pequeños. También está expuesta al presupuesto del anunciante y a la saturación de interacción. Competidores con intención de compra, como search o retail media, compiten por resultados y no necesitan replicar una red social completa para quitar presupuesto. La tasa histórica de META refleja tanto su industria como cambios de participación, formatos y monetización; no se asume como crecimiento permanente. [Meta, 10-K, 29 de enero de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm) [Meta, 10-Q, 30 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm)

La IA opera en ambos lados: mejorar recomendaciones y campañas puede reforzar la plataforma; asistentes que deciden dónde comprar pueden desplazar el punto de descubrimiento. La velocidad de inversión de varios competidores vuelve insuficiente medir ventaja solo por cantidad de servidores. La protección más sólida sigue siendo distribuir una herramienta útil dentro de una base existente; el riesgo es que el rendimiento publicitario adicional no cubra el aumento en costo de capacidad. [Meta, 10-Q, 30 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm)

### Las 5 fuerzas de Porter

| Fuerza | Intensidad: baja/media/alta | Evidencia | Evolución esperada | Implicación para retornos |
|---|---|---|---|---|
| Poder de proveedores | Alta | Capacidad cloud/chips/energía y sistemas móviles | Mayor si infraestructura se vuelve escasa | Menor excedente por reinversión |
| Poder de compradores | Media | Clientes pueden reasignar campañas según conversión | Mayor con medición/comparación más sencilla | Precio debe justificar ROI |
| Amenaza de nuevos entrantes | Media | Distribución social difícil; agentes pueden entrar por otra vía | Sube si intención cambia de interfaz | Capacidad tecnológica sola no preserva moat |
| Amenaza de sustitutos | Alta | Search, retail media, vídeo y agentes | Puede aumentar con automatización | Menor control de descubrimiento |
| Rivalidad existente | Alta | GOOG/PINS/SNAP/TTD y redes de vídeo compiten por atención/presupuesto | IA intensifica inversión | Retornos dependen de productividad, no carrera de gasto |

Evidencia de dependencia y competencia: [Meta, 10-K, 29 de enero de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm); capacidad contratada: [Meta, 10-Q, 30 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm). Sustitución tiene la mayor posibilidad de cambiar la economía; barreras de distribución y aprendizaje son la mejor protección observable.

El crecimiento del último trimestre no se extrapola como crecimiento del mercado total. La muestra sectorial global de Advertising incluye numerosas agencias e intermediarios con distinta intensidad de infraestructura. Se usa como referencia explícita de retorno estable, pero su relación ventas/capital no se traslada a la inversión de Meta. El tamaño global de publicidad capturable por Meta y una cuota homogénea al corte no quedaron documentados con una fuente primaria suficiente; por ello no se presenta un TAM numérico ni una cuota inventada. [Damodaran, datos globales, 05-ene-2026](https://www.stern.nyu.edu/~adamodar/pc/datasets/rocGlobal.xls)

## 5. Calidad del negocio

### Análisis financiero histórico

Se preservan las cifras de la hoja vigente para 2016–2025 y LTM a septiembre de 2026. La comparación de los tres rangos de estados antes y después de esta revisión fue exacta; esa conservación no certifica de nuevo cada renglón de diez años. El contraste documental de esta sesión se concentró en el último 10-Q, los comparativos y las partidas materiales que sostienen los supuestos. Los estados extensos quedan en el nivel 2 de la sección 12. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit) [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

#### Estado de resultados

Los ingresos FY2025 son US$200.966,00 M, frente a US$27.638,00 M en 2016. La expansión no fue uniforme: 2022 tuvo contracción de ingresos y presión de margen. El CAGR de ingresos FY2022–2025 es 19,89% y FY2020–2025 18,51%. La serie 2016–2025 contiene diez cierres y nueve intervalos; su CAGR de 24,66% no se llama CAGR de diez años. [Meta 10-K, 29-ene-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm) [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

El LTM pasa a US$241.605,00 M de ingresos y US$79.380,00 M de EBIT reportado, margen 32,86%. El cálculo de ingresos es 200.966 + 181.712 − 141.073. El EBIT usa 83.276 + 54.635 − 58.531. La menor tasa fiscal efectiva LTM eleva beneficio neto sin demostrar una mejora comparable de la operación: se conserva en los históricos y se utiliza una tasa normalizada para proyectar. I+D y depreciación ya están dentro de los gastos GAAP; no se restan dos veces. [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm) [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

El margen GAAP trimestral de Q3 contiene un cargo legal de US$9.889,00 M. La normalización de ese cargo y la capitalización de I+D responden a preguntas distintas. El DCF no convierte la desaparición de un cargo en cancelación de su obligación de pago. La sección 12 expone los tres márgenes y el puente, para evitar justificar un margen ajustado con un comparable GAAP. [Meta resultados, 21-oct-2026](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/)

#### Balance

Al 30-sep-2026, US$478.836,00 M de activos concilian con US$206.450,00 M de pasivos y US$272.386,00 M de patrimonio. Caja más valores negociables suma US$82.449,00 M, pero el efectivo restringido no se añade como si fuera libre. El inmovilizado neto aumenta a US$253.222,00 M y hay US$89.499,00 M en construcción en progreso dentro del inmovilizado bruto: es capital que todavía requiere utilización rentable. [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

La deuda económica utilizada por la hoja es US$116.026,00 M e incluye arrendamientos operativos reconocidos y una estimación de arrendamientos financieros. No es idéntica a bonos o deuda financiera pura. Las inversiones privadas de US$32.624,00 M se excluyen del capital operativo y se suman en el puente por su valor contable como proxy; su valor realizable no está comprobado. Los vencimientos completos de arrendamientos financieros actuales y su conciliación con el conversor no están desglosados con precisión suficiente para certificar ese ajuste. [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm) [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

La capacidad comprometida fuera de balance no se suma nominalmente a la deuda y se vuelve a restar en los flujos. Debe mapearse a gasto de servicio, CAPEX, arrendamientos y garantías según el contrato. Asimismo, la sanción de Nuevo México y los pagos del acuerdo con fiscales son exposiciones diferentes. Conservar un ajuste de puente no implica que cubra todas las obligaciones posibles. [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

#### Flujo de caja

El OCF LTM es US$133.087,00 M, frente a CAPEX físico de US$104.438,00 M; su diferencia de US$28.649,00 M es el FCF simple definido en esta hoja. No equivale al FCFF económico del DCF ni al FCF del emisor, que descuenta principal de arrendamientos financieros. El OCF incorpora US$26.943,00 M de compensación en acciones LTM; adicionarla en el estado de caja no elimina su costo para el accionista. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit) [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

El CAPEX/ventas pasa de 15,85% en 2021 a 34,68% en 2025 y 43,23% LTM. La tasa de reposición tecnológica y el calendario de utilización importan tanto como el monto invertido. No se publica una separación confiable entre mantenimiento y expansión para certificar que toda inversión actual sea opcional. El escenario base mantiene reinversión elevada y admite FCFF negativo inicial; su posterior recuperación depende de crecimiento útil y productividad del capital, no de una reducción automática de costos. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

#### Ratios y retornos

| Métrica | LTM | Media FY2023–25 | Media FY2021–25 | Media FY2016–25 | Definición |
|---|---|---|---|---|---|
| Margen bruto | 81,03% | 81,47% | 80,71% | 82,22% | LTM separado; medias simples FY |
| Margen EBIT GAAP | 32,86% | 39,42% | 36,55% | 39,39% | LTM separado; medias simples FY |
| OCF/ventas | 55,08% | 55,28% | 51,61% | 52,48% | LTM separado; medias simples FY |
| FCF simple/ventas | 11,86% | 29,49% | 27,62% | 30,81% | LTM separado; medias simples FY |
| CAPEX/ventas | 43,23% | 25,79% | 23,99% | 21,67% | LTM separado; medias simples FY |
| SBC/ventas | 11,15% | 10,24% | 9,75% | 9,14% | LTM separado; medias simples FY |
| I+D/ventas | 31,68% | 27,92% | 26,99% | 23,45% | LTM separado; medias simples FY |


El current ratio de 1,90× utiliza saldos de cierre. El quick ratio reproducible con caja, negociables y cuentas por cobrar es 1,67×, sin convertir otros activos corrientes en liquidez inmediata. EBIT/intereses LTM es 28,57×, una cobertura contable, no una garantía sobre pagos contractuales. Deuda económica neta/EBITDA GAAP es 0,32× y tiene un perímetro distinto de deuda financiera neta. No se presentan medias históricas de estos ratios cuando falta una serie homogénea conciliada de deuda y arrendamientos. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

ROA y ROE LTM sobre saldos finales son 15,71% y 27,63%. Los promedios de 3/5/10 años basados en saldos promedio no son comparables con esos cocientes de cierre y no se mezclan. El ROIC ajustado que muestra el DCF, 26,74%, usa impuesto efectivo LTM anormalmente bajo y capital al cierre. Con impuesto inicial normalizado de 17%, el mismo EBIT ajustado/capital produce 23,26%. Ninguna de las dos cifras es el retorno observado de la inversión nueva en IA. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

### Evaluación cualitativa de la calidad

La escala de distribución y la repetición de campañas permiten beneficios importantes a través del ciclo. La expansión de gasto físico cambia, sin embargo, la capacidad de convertir esos beneficios en efectivo. La caída del FCF simple no contradice por sí sola el crecimiento del negocio: puede ser inversión anticipada, pero solo habrá creación de valor si genera retornos superiores al costo de capital. El negocio se clasifica como crecimiento maduro para las probabilidades del modelo. No se hereda la clasificación de un informe anterior. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

### Auditoría de cifras y supuestos del Modelo JMR

Esta subsección documenta procedencia y contraste para interpretar el análisis. El dictamen financiero de la revisión se entrega en un documento separado y no se sustituye por esta tabla.

| Dato o supuesto | Valor / período | Origen y actividad | Fuente / ubicación | Resultado del contraste | Prioridad |
|---|---|---|---|---|---|
| Ingresos y EBIT | 241.605,00 / 79.380,00; LTM | Reportado/derivado; activos | 10-Q; Input B12: B13 | Conciliado; históricos intactos | Alta |
| Crecimiento Base | 22/20/17/14/11%; cinco años | Juicio activo | Historias C29: G29 | Compatible con desaceleración, no guía 2027 | Alta |
| Margen Base | 48% a 43%; ajustado I+D | Juicio activo | Input B28; Historias D5 | Debe revertirse I+D para comparar GAAP | Alta |
| Reinversión | S/C0,45 a 0,54 | Juicio y derivación activos | Input B32: B33; Historias F5 | Marginal histórico 0,47 orienta, no garantiza | Alta |
| ROIC terminal | 17,93% Base y Optimista | Referencia / juicio | Global E3; Historias N5: N8 | Sector ajustado; comparable de economía imperfecta | Alta |
| Impuestos | 17% a 25,37% | Normalización activa | Input B89: B93/B25 | No perpetúa efectivo 4,58% | Alta |
| Riesgo | WACC 10,57% a 8,99% | Derivado y referencia | Cost of capital; Input B36/B47 | CRP regional mantiene limitación | Alta |
| Terminal | g4%; Disrupción 1% | Juicio activo | Historias J5: J8 | Inferior a Rf 5,29% | Alta |
| Acciones y opciones | 2.556,24 M; opciones 20 M | Dato y modelo | Input B22/B39: B42 | RSU no se añaden además como opción | Alta |
| Fracaso / probabilidades | Fracaso 0%; historias 45/22,5/10/22,5 | Juicio activo | Input B52; Historias B5: B8 | Disrupción separada; sin doble ponderación | Media |
| Múltiplos | Siete; tres con peso | Anclas heredadas / derivación | Anclas META | Históricos y descuentos de ciclo sin soporte suficiente | Alta |
| MOS | 35% solo Base | Regla activa | Registro B52 | Conciliado con Base; no sobre promedio | Media |


| Supuesto y escenario | Historia que presupone | Evidencia favorable | Evidencia contraria | Justificación / faltante | Señal de revisión |
|---|---|---|---|---|---|
| Crecimiento Base | Mejores anuncios y monetización | Q3 +26%; precio/impresiones | Gran tamaño y competencia | No hay desglose proyectado por producto | Pérdida persistente de eficacia publicitaria |
| Margen ajustado Base | Escala absorbe parte de IA | Franquicia rentable | Más depreciación y nube | Puente de I+D explicitado; vida 3 años es juicio | Costo de servir aumenta más que monetización |
| S/C Base | Capital alto antes de uso | CAPEX y construcción | Retorno por proyecto no publicado | 0,45 calibrado frente a 0,47 marginal | CAPEX no produce ingresos tras puesta en marcha |
| ROIC Base/Optimista | Ventaja publicitaria durable | Red y campañas repetidas | Datos y distribución pueden cambiar | Sector global 17,93%; no prima perpetua arbitraria | Erosión de moat, no solo inversión anticipada |
| Conservadora | Ventaja se debilita parcialmente | Presión de costos | Escala sigue defendible | Punto medio 13,46% por regla | Mejora operativa sostenida refuta erosión |
| Disrupción | No hay exceso de retorno estable | Rigidez y sustitución posibles | Negocio actual rentable | WACC 8,99%; no libera capital automáticamente | Retornos persistentes sobre WACC refutan disrupción |


Los múltiplos históricos normalizados no contienen una muestra estadística completa en su pestaña. Las anclas de ciclo citan 2023 o combinaciones de 2020/2024/2025, pero no se certifican fecha, denominador y normalización íntegros. Sus resultados se conservan como cálculos secundarios con hallazgos, detallados en el nivel 2. No se usa esa lectura para alterar el DCF ni sus probabilidades. **Barato frente a su historia no equivale a infravalorado intrínsecamente.** [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

## 6. Ventaja competitiva

La audiencia instalada y sus relaciones sociales reducen el costo de distribuir nuevas funciones. El anunciante accede a una herramienta común para probar creatividades, audiencias y conversiones. El valor de esa combinación está en producir resultados repetibles, no simplemente en acumular usuarios. La expansión de ingresos y la persistencia de beneficios operativos son evidencia de utilidad comercial, aunque no permiten aislar el retorno de cada algoritmo. [Meta 10-K, 29-ene-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm) [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

Los costos de cambio del usuario no son absolutos: puede utilizar varios servicios y trasladar atención. Los del anunciante incluyen aprendizaje, integración y datos de campañas, pero también puede reasignar presupuesto. La defensa más importante es la relación entre rendimiento, escala y facilidad de uso. Una infraestructura de IA que cualquier competidor pueda contratar no constituye por sí misma una barrera exclusiva.

| Fuente de ventaja | Evidencia observable | Evidencia cuantitativa | Duración probable | Amenaza de erosión | Veredicto |
|---|---|---|---|---|---|
| Efectos de red | Relaciones y comunicación dentro de las apps | DAP 3,64 mil millones en septiembre | Larga si conserva utilidad | Migración de atención | Ventaja actual |
| Datos y aprendizaje | Optimización de campañas y recomendaciones | Precio/impresiones crecen; atribución causal no aislada | Depende de permisos y calidad | Privacidad y menor disponibilidad de señales | Ventaja condicionada |
| Distribución | Lanzamiento sobre audiencia existente | Fo A99,30% de ventas 9M | Durable en publicidad | Agentes capturan descubrimiento | Defendible |
| Costos de cambio | Integraciones y aprendizaje del anunciante | Retención monetaria no publicada | Media | Herramientas interoperables | Parcial |
| Escala y costo | Costos comunes distribuidos en gran volumen | EBIT positivo durante todo 2016–2025 | Puede durar más de10 años | Capacidad infrautilizada | Defendible con disciplina |
| Marca y propiedad intelectual | Productos establecidos y conocimiento técnico | No se atribuye valor separado a marca | Larga, no inmune | Daño reputacional y modelos sustituibles | Apoyo, no prueba suficiente |
| Regulación y activos escasos | Capacidad/energía ayudan a operar | Contratos elevados, no exclusividad acreditada | Limitada | Los compromisos también son pasivos económicos | No se presume moat regulatorio |


El veredicto base es **ventaja durable** en la franquicia publicitaria. No hay prueba suficiente de que una caída del ROIC causada por inversión anticipada sea pérdida de ventaja, ni prueba de que todo nuevo proyecto de IA vaya a disfrutarla. Por eso se utiliza la referencia sectorial ajustada de 17,93% para el capital nuevo estable en Base y Optimista, inferior al ROIC ajustado agregado actual. Conservadora admite debilitamiento y Disrupción elimina exceso sobre WACC. Si cae el poder de monetización por competencia o regulación, el juicio de durabilidad debe cambiar. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit) [Damodaran global, 05-ene-2026](https://www.stern.nyu.edu/~adamodar/pc/datasets/rocGlobal.xls)

## 7. Competencia

Meta compite por atención y por presupuestos que buscan resultados. Ambas competencias se cruzan, pero no son idénticas: un servicio puede captar tiempo sin monetizarlo bien, y un medio comercial puede captar presupuesto con una audiencia menor si está más cerca de la compra. El 10-K identifica competencia de plataformas y nuevos productos; esta revisión no asigna cuotas que no se hayan documentado. [Meta 10-K, 29-ene-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm)

| Competidor o sustituto | Solapamiento | Posición relativa | Ventaja principal | Debilidad / diferencia | Señal a vigilar | Fuente |
|---|---|---|---|---|---|---|
| Alphabet / You Tube | Búsqueda, vídeo y publicidad | Gran plataforma con intención comercial | Distribución y búsqueda | Mezcla con Cloud y costos corporativos impide igualdad de márgenes | Respuesta publicitaria y uso de agentes | 10-K Meta; resultados Alphabet Q2 |
| Snap | Social, vídeo y publicidad | Menor escala en la comparación cualitativa | Formatos y relaciones de audiencia | No se atribuye margen positivo sin comprobarlo | Migración de tiempo y presupuestos | 10-K Meta |
| Pinterest | Descubrimiento visual y anuncios | Contexto de descubrimiento comercial | Intención visual | Escala y economía diferentes | Conversión y adopción comercial | 10-K Meta |
| The Trade Desk | Compra y optimización programática | Intermediario, no red equivalente | Acceso a inventario de terceros | Menor control del inventario propio | Distribución de presupuestos | 10-K Meta |
| Sustitutos: retail media y agentes | Intención y transacción | No precisan replicar una red social | Cercanía a decisión de compra | Dependen de utilidad y adopción | Pérdida de descubrimiento en apps | 10-K Meta; análisis de mecanismo |


Alphabet ofrece una referencia madura, pero su margen de Google Services no es el consolidado y algunos costos de IA se registran a nivel corporativo. En Q2 2026 reportó US$39.544,00 M de EBIT de Services sobre US$94.540,00 M de ventas: 41,83%. Comparar ese margen directamente con Meta ajustada por I+D ocultaría diferencias de perímetro y contabilidad. Se utiliza como contraste de la capacidad económica de una plataforma madura, no como objetivo automático. [Alphabet resultados Q2, julio-2026](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm)

La competencia no exige que un único rival sustituya todas las apps. Varias herramientas especializadas pueden repartir el descubrimiento, la comunicación y la compra. La señal relevante es que los anunciantes obtengan mejores resultados marginales fuera de Meta, incluso si los usuarios permanecen en ella. No se certificó un cuadro de múltiplos actuales de pares con igual fecha y definición; el sector de comparables de la hoja sigue sin poblarse y no se presenta como evidencia cuantitativa vigente. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

## 8. Gestión y asignación de capital

### Equipo, gobierno e incentivos

Mark Zuckerberg combina dirección ejecutiva y presidencia; Susan Li dirige finanzas en la estructura reportada. El liderazgo del fundador favorece decisiones con horizonte largo y continuidad de producto. La experiencia de construir plataformas ayuda a distribuir innovaciones, pero no demuestra capacidad ilimitada para obtener retornos en infraestructura o servicios nuevos. El proxy y los informes permiten evaluar la estructura formal; no permiten certificar una sucesión operativa completa ni el retorno de cada equipo de IA. [Meta Proxy, 16-abr-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026025532/meta-20260416.htm) [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

Las clases de acciones tienen derechos económicos similares y votos distintos. El control del fundador limita la capacidad del minoritario para corregir decisiones de capital. La futura clase C permite emitir derechos económicos sin votos; el dividendo anunciado no crea por sí mismo valor económico y no debe aplicarse antes de su efectividad. El contrapeso del consejo y sus comités importa, pero no elimina esa concentración. [Meta Proxy, 16-abr-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026025532/meta-20260416.htm) [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

El proxy describe salario simbólico del fundador y su exposición patrimonial, además de otros beneficios de seguridad. Eso alinea parte de los incentivos con el valor del negocio, sin garantizar que todos los accionistas prefieran el mismo nivel de riesgo o las mismas apuestas. Para otros ejecutivos y empleados, las adjudicaciones de acciones influyen en retención y dilución. No se infiere disciplina de la mera existencia de incentivos accionarios: se contrasta con resultados por acción y capital necesario. [Meta Proxy, 16-abr-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026025532/meta-20260416.htm)

### Asignación de capital

| Uso de capital | Historial y magnitud | Resultado observable | Disciplina observable | Riesgo o pregunta pendiente |
|---|---|---|---|---|
| Reinversión orgánica e I+D | I+D LTM 76.544,00 M | Producto y modelos; retorno por proyecto no publicado | Amortización 3 años en modelo, no vida contable reportada | Separar mantenimiento, experimentación y crecimiento |
| Capex | 104.438,00 M LTM; guía 2026 135–145 mil M | PPE y capacidad en construcción aumentan | No se presume CAPEX opcional ni rentable por tamaño | Calendario de uso y reposición |
| Adquisiciones y desinversiones | 4.000,00 M LTM en fila de adquisiciones agregada | No hay NOPAT adquirido segregado suficiente | No imputar crecimiento comprado gratuito | Retorno sobre precio pagado N/D |
| Recompras y emisión | 26.248,00 M FY2025; cero en9M2026 | Acciones económicas 2.556,24 M, mayores que cierre 2025 | No extrapolar reducción de acciones mientras no recompra | Compensar SBC requiere efectivo o dilución |
| Dividendos | 5.398,00 M LTM según hoja | Devolución pequeña frente a inversión | Debe competir con necesidades de financiación | Dividendo en acciones C no equivale a efectivo |
| Deuda y liquidez | Emisión neta 9M24.910,00 M; caja/negociables 82.449,00 M | Financia diferencia entre operación e inversión | Liquidez disponible; obligaciones contractuales grandes | No evaluar solvencia solo con deuda/EBITDA |


La publicidad ha financiado innovación y distribuciones reales, pero el cambio reciente de recompras a financiación e infraestructura altera la experiencia del accionista. La SBC LTM de US$26.943,00 M y el aumento de acciones impiden describir toda recompra histórica como reducción permanente. No se reconstruye un precio medio de recompra actual cuando no hubo recompras en nueve meses de 2026; tampoco se utilizan promedios históricos de acciones como denominador de valor presente. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit) [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

La comunicación de resultados especifica crecimiento, gasto y dirección de inversión, pero todavía no cuantifica las economías completas de nuevos productos. La dirección prevé pérdidas de Reality Labs cercanas a US$15.000,00 M en 2027, que seguirían consumiendo excedente. Se considera una guía a vigilar y no una reducción ya ganada. La conclusión es capacidad demostrada en la franquicia y disciplina de inversión aún por probar en el nuevo ciclo, sin atribuir creación de valor a cada dólar comprometido. [Meta resultados, 21-oct-2026](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/)

## 9. Catalizadores

Un catalizador útil debe modificar información sobre capacidad de generar caja o reclamaciones del patrimonio. No se utiliza una eventual subida de la cotización como explicación circular.

| Catalizador | Signo | Horizonte | Mecanismo | Confirmación necesaria | Fecha / ventana |
|---|---|---|---|---|---|
| Monetización publicitaria de nuevas herramientas | Positivo si mejora retorno | 1–4 trimestres | Mejor conversión y precio efectivo | Resultados sin deterioro del costo de servir | Próximos resultados; fecha siguiente no verificada |
| Puesta en marcha de capacidad | Mixto | 2027 y posteriores | Depreciación y servicio crecen antes o junto a ingresos | Utilización y flujo incremental | Calendario contractual; no fecha única |
| Reducción de pérdidas de Reality Labs | Positivo condicionado | FY2027 | Libera recursos de una unidad deficitaria | Pérdida cercana a guía, sin trasladar costos artificialmente | Ejercicio 2027 |
| Apelación y garantías de Nuevo México | Negativo o alivio | Según proceso judicial | Pago, interés y posible colateral afectan caja | Resolución y provisión conciliada | Fecha judicial N/D |
| Recapitalización clase C | Mixto | Desde enero 2027 | Cambia denominadores y flexibilidad de financiación | Efectividad y fechas de distribución | 19-ene-2027 para estatuto; pago no fijado |
| Nuevos datos de inversión 2027 | Mixto | Próxima guía | Revisa reinversión y financiación requerida | Guía cuantificada y composición del CAPEX | Fecha de anuncio N/D |


La evidencia de origen es el 10-Q y el comunicado de resultados, no una previsión de revalorización. [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm) [Meta resultados, 21-oct-2026](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/)

## 10. Riesgos

La ordenación siguiente es juicio cualitativo de materialidad, no una probabilidad estadística estimada. La misma exposición no se descuenta simultáneamente en crecimiento, prima de riesgo y probabilidad sin identificar su efecto independiente. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

| Orden | Riesgo | Categoría | Probabilidad | Impacto | Mecanismo de daño | Indicador temprano | Invalidación de Base |
|---|---|---|---|---|---|---|---|
| 1 | Infraestructura de bajo retorno | Capital / tesis | Media | Muy alto | Capacidad y reposición consumen margen y FCFF | Compromisos sin monetización comparable | Retorno nuevo persistentemente inferior a WACC |
| 2 | Costos de IA y depreciación | Operativo | Alta | Alto | Aumenta costo de servir pese a más ventas | D&A/nube creciendo más rápido que ingresos | Margen no recupera nivel normalizado |
| 3 | Litigios y regulación | Legal | Alta exposición; resultado incierto | Alto | Pagos, restricciones, garantías e intereses | Órdenes y provisiones nuevas | Cambio estructural en anuncios o caja |
| 4 | Sustitución de descubrimiento | Competitivo | Media | Alto | Agentes y otros medios capturan intención | Pérdida de retorno publicitario relativo | Precio efectivo cae con actividad estable |
| 5 | Privacidad y señales de datos | Regulatorio / distribución | Media | Alto | Peor medición y segmentación | Cambios de políticas o consentimientos | Menor eficacia sin adaptación |
| 6 | Dilución y control | Gobierno | Alta exposición | Medio/alto | Acciones y adjudicaciones absorben crecimiento | SBC y acciones suben sin caja por acción | Beneficio por acción no acompaña operación |
| 7 | Ciclo publicitario y FX | Macro | Media | Medio/alto | Presupuestos se recortan o cambia mezcla | Debilidad regional y precio | Desaceleración más rápida que la senda |
| 8 | Energía, hardware y proveedores | Tecnología / suministro | Media | Alto | Retrasos o capacidad cara | Construcción sin puesta en servicio | Inversión no produce capacidad utilizable |


### Escenarios cualitativos de largo plazo

| Variable | Base | Conservadora | Disrupción | Optimista | Evidencia para cambiar |
|---|---|---|---|---|---|
| Crecimiento y participación | Monetización sostiene expansión desacelerada | Se normaliza antes | Sustitución y pérdida de utilidad | Mejor producto amplía monetización | Publicidad, conversión y mezcla |
| Precios y retención | Rendimiento justifica campañas | Menor aumento de precio efectivo | Anunciante migra presupuesto | Más resultados por campaña | Precio con volumen, no precio aislado |
| Margen | Escala absorbe parte de costos | Depreciación y nube pesan más | Infraestructura sin ingresos suficientes | Mejor productividad operativa | Margen GAAP y puente I+D |
| Reinversión y retorno | Capital alto; ventaja durable | Retorno converge parcialmente | No hay exceso terminal sobre costo | Más ingresos por inversión inicial | S/C marginal y utilización |
| Moat y sustitución | Red y aprendizaje persisten | Ventaja se debilita | Desaparece ventaja marginal estable | Distribución refuerza ventaja | Evidencia de competencia y permisos |


Cada historia corresponde a las filas activas del modelo, sin un segundo juego de escenarios editoriales. Las probabilidades mantienen la previa de crecimiento maduro; no se aumentó el riesgo de Disrupción por una caída de cotización ni se aplicó un nuevo descuento general al DCF. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

### FODA de síntesis

| Dimensión | Elementos específicos y respaldados |
|---|---|
| Fortalezas internas | Distribución instalada; herramientas comunes para anunciantes; generación operativa de caja. |
| Debilidades internas | Dependencia publicitaria; consumo de capital de nuevas apuestas; control concentrado y costo de SBC. |
| Oportunidades externas | Mejora de conversión con IA; comunicación comercial; nuevos usos distribuidos sobre las apps. |
| Amenazas externas | Desintermediación por agentes/retail media; restricciones de datos; escasez de energía y hardware. |


La infraestructura puede proteger calidad del servicio y, al mismo tiempo, reducir flexibilidad ante un cambio de demanda. El FODA conecta esa rigidez con la fortaleza de distribución, sin convertir la oportunidad tecnológica en un flujo ya ganado. [Meta 10-K, 29-ene-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm) [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

## 11. Bulls say / Bears say

| Bulls say | Bears say |
|---|---|
| La distribución existente reduce el costo de adoptar nuevas herramientas. | La adopción gratuita puede generar cómputo antes de ingresos. |
| Precio e impresiones recientes apoyan utilidad comercial del producto. | La mejora agregada no demuestra causalidad ni retorno de cada proyecto de IA. |
| La franquicia ha generado EBIT positivo a través de crisis y cambios de formato. | El ciclo actual requiere mucho más capital físico que la expansión histórica. |
| El horizonte del fundador permite invertir sin sacrificar producto por un trimestre. | Su control reduce la capacidad de frenar inversiones de baja rentabilidad. |
| La pérdida de Reality Labs puede reducirse según la nueva guía. | Incluso la guía implica pérdidas importantes y puede trasladarse gasto hacia IA. |
| Caja y valores negociables ayudan a financiar la transición. | Compromisos, litigios y SBC compiten con esa liquidez. |


Los argumentos se apoyan en las secciones anteriores y sus fuentes. El desacuerdo factual central es cuánto retorno y efectivo incremental producirán las inversiones que ahora crecen. Resolverlo requiere ingresos por uso, costo de servir y capital comprometido coherentes, no solo audiencia ni un trimestre favorable. [Meta resultados, 21-oct-2026](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/) [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

### Conclusión cualitativa

Meta conserva una franquicia publicitaria con ventaja de distribución y optimización, pero la capacidad de reinvertir rentablemente en el nuevo ciclo aún no está demostrada por proyecto. La evidencia mejora si la monetización y el efectivo por acción crecen después de sostener infraestructura y remuneración; empeora si solo aumentan uso, compromisos y depreciación. La calidad actual del negocio no resuelve por sí sola la economía de la expansión.

### Síntesis final

La historia financiera conecta expansión comercial, márgenes elevados pero variables y un aumento reciente de capital necesario. Ese cambio hace insuficiente extrapolar el beneficio contable o el retorno de los activos antiguos. La ventaja de distribución sigue siendo útil porque ofrece un canal de monetización inmediato, aunque el permiso de datos y la competencia por intención condicionan su duración. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit) [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

Las historias oficiales difieren por la rapidez con que se monetiza la inversión y por la persistencia de esa ventaja. Base admite desaceleración y gasto elevado; Optimista mejora productividad sin elevar arbitrariamente el retorno perpetuo; Conservadora incorpora erosión parcial; Disrupción no presupone una venta automática del capital comprometido. La coherencia depende de evaluar crecimiento, margen y reinversión juntos, sin escoger una cifra para alcanzar la cotización. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

Los próximos resultados útiles serán los que permitan relacionar capacidad puesta en servicio con monetización y caja después de inversión. También importarán las obligaciones legales, la emisión de acciones y las políticas de datos. Una empresa puede mejorar el producto mientras ofrece menos efectivo inmediato al propietario; distinguir esas dos dimensiones permite juzgar la tesis sin confundir calidad empresarial con atractivo de inversión. [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

## 12. Valor con criterio Damodaran

### La historia en un párrafo

En diez años, Base representa una plataforma que mantiene distribución publicitaria, monetiza mejor sus herramientas y acepta una menor velocidad de expansión conforme aumenta su tamaño. Para sostenerlo invierte antes de recibir ingresos, convierte parte de I+D en un activo analítico y absorbe depreciación física creciente. El retorno del capital nuevo converge a una referencia sectorial ajustada, no a la rentabilidad histórica más alta. El riesgo principal es que la capacidad y los costos se vuelvan permanentes sin producir monetización proporcional. Esta historia corresponde al modelo congelado R4. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Mantener crecimiento a doble dígito al inicio | Sí | Actividad reciente lo apoya | Base; desacelera, no repite 26% |
| Recuperar margen GAAP sin el cargo puntual | Sí | El cargo no es recurrente en igual monto | Base; no cancela el pasivo |
| Obtener exceso terminal sobre WACC | Sí | Distribución publicitaria defendible | Base condicionada a moat |
| Toda inversión nueva en IA será rentable | No demostrable como generalización | No hay evidencia por proyecto | No se asume |
| Mejorar productividad sin más rentabilidad perpetua | Sí | Monetización y eficiencia pueden subir antes del terminal | Optimista mantiene ROIC sectorial |


### Visión externa: tasas base

Con ingresos LTM de US$241.605,00 M, Meta pertenece holgadamente al tramo mayor de US$50.000 M en el Exhibit 4 de *The Base Rate Book* (2016), incluso ajustando el tamaño a dólares constantes. La tabla de crecimiento real a cinco años de ese grupo muestra media 1,00% y mediana 1,50%. Con inflación supuesta de2,30%, los equivalentes nominales compuestos son 3,32% y 3,83%. No se compara un CAGR nominal de Meta con una media real sin conversión. [Mauboussin y Callahan, 26-sep-2016, Exhibit 4, p25](https://mjbaldbard.wordpress.com/wp-content/uploads/2020/09/michael-mauboussin-e28093-base-rate-books-2015-2016.pdf)

| Historia | CAGR nominal 1–5 | Equivalente real con inflación 2,30% | Fracción histórica aproximada que iguala o supera |
|---|---|---|---|
| Base | 16,73% | 14,11% | Entre 3,30% y 10,30% |
| Conservadora | 8,77% | 6,33% | Entre 10,30% y 27,20% |
| Optimista | 22,16% | 19,41% | Entre 1,00% y 3,30% |
| Disrupción | 0,71% | -1,55% | Entre 61,20% y 84,00% |


Son bandas calculadas sumando los intervalos publicados, no probabilidades específicas de Meta ni interpolaciones de precisión falsa dentro de cada intervalo. La muestra de grandes empresas es amplia y heterogénea, y las distribuciones cambian con el tiempo. La justificación para una trayectoria sobre esa base histórica es la monetización reciente de una distribución instalada; la evidencia contraria es el tamaño inicial y la inversión requerida. No se utiliza la categoría IA para eximir a la empresa de la economía del crecimiento. La actualización de 2026 de los mismos autores recalca la necesidad de adaptar las tasas base y separar expansión de creación de valor. [Mauboussin y Callahan, 13-may-2026](https://www.morganstanley.com/im/publication/insights/articles/article_bayesandbaserates2_ltr.pdf)

### Piezas del valor

#### Crecimiento

La revisión mantiene 22%,20%,17%,14% y 11%, CAGR 16,73%. Es un supuesto para períodos futuros de doce meses desde el LTM, no una guía anual FY 2027 publicada. En el año 5 los ingresos alcanzan US$523.673,61 M y en el año 10 US$727.015,56 M. El tamaño absoluto hace que incluso la desaceleración necesite una gran expansión de gasto capturado. La guía de ingresos Q4 de US$73.000–76.000 M respalda un punto de partida fuerte, pero no fija la senda de cinco años. [Meta resultados, 21-oct-2026](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/) [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

| Motor | Evidencia hasta el corte | Mecanismo en Base | Límite del supuesto |
|---|---|---|---|
| Publicidad Fo A | Impresiones+10%; precio+14% Q3 | Mejor inventario y conversión; crecimiento agregado se desacelera | No se multiplican indefinidamente las tasas del trimestre |
| Otros Fo A | Ingresos distintos de anuncios existen | Aporta diversificación gradual dentro del grupo | No hay proyección separada oficial de ingresos de Muse |
| Reality Labs | Ventas pequeñas y pérdidas elevadas | No se transforma en el motor de ventas sin evidencia | Menores pérdidas son guía, no ingresos garantizados |
| Geografía | Norteamérica y resto crecen a ritmos distintos | Mezcla y monetización apoyan expansión | No existe una proyección regional conciliada independiente |
| Adquisiciones y FX | Pueden alterar crecimiento reportado | No se añade una compra futura gratuita | Sin precio y retorno adquirido no hay M&A proyectada |


El modelo activo proyecta el grupo; no contiene un plan separado por producto cuyas cifras se sumen y certifiquen el total. Esa limitación se conserva explícita. La senda de años 6–10 es9,60%,8,20%,6,80%,5,40% y 4,00%, de modo que llega al crecimiento estable. Si cambian la eficacia del anuncio o la guía de inversión, se revisan conjuntamente crecimiento y capital, no solo la cifra que más convenga al valor. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

#### Márgenes y normalización

| Medida | EBIT US$ M | Margen | Tratamiento |
|---|---|---|---|
| LTM GAAP | 79.380,00 | 32,86% | Histórico intacto |
| LTM sin cargo Q3 de9.889 | 89.269,00 | 36,95% | Normalización aislada, no el EBIT del DCF |
| LTM ajustado por I+D | 111.802,67 | 46,27% | 79.380 +76.544 −44.121,33 |
| Año 1 DCF ajustado | 141.483,89 | 48,00% | Proyección, distinta de GAAP |
| Año 1 GAAP auxiliar | 110.113,46 | 37,36% | Revierte gasto y amortización I+D |
| Objetivo ajustado desde año 5 | Variable con ventas | 43,00% | No se presenta como margen GAAP |


Se mantiene la senda ajustada 48%,46%,45%,44%,43%; luego 43%. La normalización parte de una franquicia rentable y evita perpetuar el cargo Q3, pero reconoce presión de depreciación, nube y capacidad. El año 1 GAAP auxiliar, alrededor de37,36%, es compatible con un margen menor que los mejores ejercicios. El43% ajustado no significa que Meta deba superar automáticamente a Google Services en margen reportado. Google asigna ciertos costos de IA a nivel corporativo y los perímetros difieren. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit) [Meta resultados, 21-oct-2026](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/)

La vida útil analítica de I+D sigue en tres años. El activo de investigación es US$125.558,67 M y su amortización LTM US$44.121,33 M. En el auxiliar, gasto I+D/ventas converge desde 30% hacia 25% en cuatro pasos; es una hipótesis de intensidad, no una guía de Meta. Capitalizar I+D eleva EBIT y capital invertido, pero su inversión neta debe seguir dentro de la reinversión: no se resta de nuevo al FCFF ya calculado por ventas/capital. La fiscalidad exacta de los ajustes y la vida económica de cada proyecto siguen siendo fuentes de incertidumbre. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

#### Reinversión y retorno

Ventas/capital para crecimiento incremental no equivale a ventas divididas por el saldo de capital. El modelo muestra un cociente promedio actual de0,61 y uno marginal histórico de0,47. Mantener 0,45 en los primeros cinco años exige aproximadamente US$2,22 de inversión neta por cada dólar de ventas incrementales; se aproxima a la intensidad marginal reciente y evita importar el2,59× promedio de agencias globales. No se añade el CAPEX físico además de esa reinversión total. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

El modelo tiene un año de adelanto de inversión: en año 1 financia el incremento de ingresos del año 2. Con ventas 294.758,10 y 353.709,72, la reinversión es (353.709,72−294.758,10)/0,45 = US$131.003,60 M. NOPAT de US$117.431,63 M menos esa reinversión da FCFF **−US$13.571,97 M**. La tasa de reinversión supera 100% al inicio; el modelo no oculta el déficit convirtiéndolo en caja positiva. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

El puente auxiliar físico del mismo año combina CAPEX 138.483,20, D&A35.370,97, I+D neta 31.370,43 y ΔNWC−3.479,06, todos US$M: 138.483,20−35.370,97+31.370,43−3.479,06 =131.003,60. El CAPEX resulta compatible en orden de magnitud con la guía 2026, pero cubre otro horizonte y se obtiene como residual de la reinversión; **no es evidencia independiente de un presupuesto de capacidad**. Se necesita información por contrato/proyecto para validar económicamente todo ese puente. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

En años 6–10 el S/C Base sube a 0,54×. La cifra se enlaza al retorno marginal terminal mediante ROIC/(margen×(1−impuesto)×(1+g)). No se eligen al mismo tiempo cuatro variables independientes incompatibles. Con margen 43%, impuesto 25,37%, g4% y ROIC 17,93%, el cociente exacto es 0,54×. La misma relación recalcula las sensibilidades; antes el motor dejaba fijo S/C mientras cambiaba ROIC. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

La mejora de eficiencia entre etapas es una simplificación de dos tramos y no una previsión demostrada de utilización. El ROIC medio del capital existente en año 10 es 17,89%; el marginal estable es17,93%. El de las inversiones nuevas no se obtiene dividiendo beneficios actuales por el saldo total sin corregir desfases. En adquisiciones, falta un NOPAT segregado del activo comprado: el retorno sobre el precio pagado es N/D, no cero. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

Las tres preguntas para el terminal se responden así. La compañía presenta retornos operativos superiores al costo de capital durante varios años, aunque la serie histórica no usa exactamente el mismo ajuste de I+D en todos los ejercicios. Tiene una ventaja identificable de distribución y aprendizaje, desarrollada en la sección 6. No se verificó una erosión comercial que explique por sí sola el descenso de retorno; inversión anticipada y cargos singulares son explicaciones distintas. Con ese alcance, Base conserva ventaja durable y usa el promedio global Advertising ajustado por I+D y leases:17,93%,419 empresas,05-ene-2026. La tabla de EE.UU. sería 27,72% con 52 empresas y no se utiliza porque Norteamérica no es mayoría de ventas. [Damodaran global, 05-ene-2026](https://www.stern.nyu.edu/~adamodar/pc/datasets/rocGlobal.xls) [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

El ROIC terminal de R3 era 15% Base,12% Conservadora y 20% Optimista. R4 sustituye esos valores por 17,93%,13,46% y 17,93% respectivamente, siguiendo la regla de industria/punto medio. Disrupción queda 8,99%. El cálculo de diagnóstico sin ventaja, con ROIC terminal igual al WACC y el S/C dependiente recalculado, da **US$503,08 por acción**; no es una quinta historia oficial. La referencia industrial no prueba la rentabilidad de los proyectos de IA ni certifica una perpetuidad. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

#### Riesgo

El método activo es costo de capital detallado. Beta sin caja global Advertising 1,09 se reapalanca hasta 1,12; la celda de selección dice Direct Input porque recibe esa beta calculada, no porque se haya elegido una beta de regresión sin explicación. Rf5,29% y ERP madura 3,70% corresponden al mismo corte mensual; CRP regional 1,26pp lleva ERPtotal 4,96%. WACC inicial 10,57% converge a 8,99%, igual en las cuatro historias. El modelo conserva una asignación regional aproximada de riesgo país, que no se certifica país por país en esta revisión. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

No se añadió una prima específica por litigios o competencia sobre esos tipos y además se castigaron las historias por el mismo motivo. Los pagos legales conocidos pertenecen al puente o al flujo según su perímetro, y los efectos operativos de regulación a las historias. La beta de regresión vigente no fue recuperada de una fuente reproducible; se marca N/D. La prueba adicional de beta 1,32 más adelante es un estrés explícito de+0,20, no un dato de regresión ni un cambio oficial del costo de capital. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

### Historias cuantificadas y valor esperado

| Historia | Probabilidad | Crecimiento años 1–5 | CAGR 1–5 | Margen ajustado | S/C1–5 /6–10 | ROIC terminal | DCF hoy US$ |
|---|---|---|---|---|---|---|---|
| Base | 45,00% | 22,00%; 20,00%; 17,00%; 14,00%; 11,00% | 16,73% | 43,00% | 0,45 / 0,54 | 17,93% | 726,65 |
| Conservadora | 22,50% | 13,00%; 10,00%; 8,00%; 7,00%; 6,00% | 8,77% | 37,00% | 0,40 / 0,47 | 13,46% | 423,18 |
| Optimista | 22,50% | 27,00%; 24,00%; 22,00%; 20,00%; 18,00% | 22,16% | 47,00% | 0,65 / 0,49 | 17,93% | 1.110,05 |
| Disrupción | 10,00% | 8,00%; 0,00%; -5,00%; 0,00%; 1,00% | 0,71% | 23,00% | 0,30 / 0,52 | 8,99% | 210,26 |


Base monetiza publicidad y conserva ventaja, con déficit de caja inicial por inversión. Conservadora crece más lentamente, soporta menor margen y debilita parcialmente su retorno excedente. Optimista captura una mayor mejora de producto y eficiencia inicial; no recibe por ello un retorno perpetuo 20% sin ancla. **¿Qué pasaría si todo fallara?** Disrupción pierde crecimiento y margen, no libera capital automáticamente y estabiliza retorno marginal en el costo de capital. Su g1% implica contracción real si la inflación supera esa cifra. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

Las probabilidades son juicio: previa de crecimiento maduro 45/22,5/22,5/10 en orden Base/Conservadora/Optimista/Disrupción. No se aplicaron ajustes de5pp porque no existían umbrales escritos ex ante que hubieran cruzado. Los límites propuestos para seguimiento no se usan retroactivamente para cambiar la previa. El lector puede asignar otras probabilidades sin cambiar la fuente oficial. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

El valor principal es **DCF Base US$726,65**. El promedio ordinario de Conservadora, Base y Optimista es **US$746,63**, con pesos renormalizados 50/25/25. Su rango es US$423,18–1.110,05. Disrupción, US$210,26, queda aparte con 10% de probabilidad original. Ningún promedio sustituye el Base como referencia de MOS. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

El terminal aporta 76,89% del valor operativo. FCFF estable US$188.519,03 M proviene de NOPAT US$242.638,07 M menos reinversión US$54.119,04 M, tasa g/ROIC=22,30%. Este peso hace material la hipótesis de ventaja durable; no basta comprobar que WACC es mayor que g. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

### Pre-mortem

| Fallo a tres años | Mecanismo | Evidencia que lo anticiparía | Respuesta de revisión |
|---|---|---|---|
| Capacidad sin uso rentable | CAPEX y contratos llegan antes que ventas útiles | Utilización débil y reinversión/ventas creciente | Revisar crecimiento y S/C juntos |
| Crecimiento sin margen | Inferencia/nube consume mayor ingreso | Más anuncios o uso sin EBIT normalizado | Revisar costo de servir y margen |
| Pérdida de descubrimiento | Clientes migran presupuestos | Precio y conversiones se deterioran frente a actividad | Reclasificar ventaja y ROIC terminal |
| Obligaciones absorben liquidez | Litigios, colateral o deuda desplazan inversión | Pagos y restricciones materiales nuevos | Conciliar puente sin doble conteo |
| Mejora empresarial sin mejora por acción | SBC o emisiones capturan beneficio | Acciones crecen más que caja económica | Revisar dilución y financiación |


La evidencia actual en contra de Base es la escala de compromisos y la ausencia de retorno segregado de IA, junto con las exposiciones legales. No son razones para rebajar automáticamente todas las entradas: son mecanismos que deben contrastarse con resultados futuros y, donde corresponda, incorporarse una sola vez. [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

### Indicadores y actualización de probabilidades

| Indicador | Hoy / corte | Refuerza favorables si… | Refuerza desfavorables si… |
|---|---|---|---|
| Crecimiento publicitario | Q3+26% aprox. | Mantiene mejora comercial con convergencia ordenada | Pierde impulso antes de liberar capital |
| Impresiones / precio | +10% /+14% Q3 | Crecen con respuesta útil | Precio cae pese a más inventario |
| Margen normalizado | Q3 sin cargo 35,41% | Absorbe nuevo gasto sin deteriorar producto | Depreciación y nube eliminan mejora |
| Capital incremental | S/C marginal 0,47en hoja | Mejora con capacidad operativa | Cae persistentemente |
| FCFF económico | Año 1 modelo negativo | Se recupera conforme se monetiza inversión | Déficit persiste por reposición |
| Dilución | Acciones 2.556,24M; SBC material | Mejora caja por acción | Sube denominador sin creación de caja |
| Ventaja y regulación | Persistencia condicionada | Permisos y resultado publicitario se sostienen | Restricciones alteran la unidad económica |


Son indicadores de seguimiento de R4 y se complementan con los umbrales de la sección 15. No se declara que ya hayan activado un cambio probabilístico. Para mover 5pp se documentará un umbral escrito, su cruce y evidencia fechada; máximo 15pp frente a la previa. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

### El precio al final

La referencia congelada es **US$648,85 al cierre del 22-oct-2026**. No es una cotización intradía actualizada. Frente al Base, la diferencia aritmética es 11,99%; el margen respecto al valor estimado es 10,71%. El precio con MOS 35% es **US$472,32**. Se calcula sobre Base, no sobre promedio ni sobre múltiplos. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

El DCF inverso utiliza un delta aditivo común de **-2,91%**, es decir−2,91pp, sobre los cinco crecimientos anuales. El CAGR resultante es **13,82%**, inferior al Base 16,73%; no es un crecimiento constante. Se recalculan años 6–10, impuestos, reinversión y terminal. Una raíz en intervalo−15pp a+35pp reconstruye la referencia con error 0,00US$/acción. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

| Margen ajustado estable | Beta apalancada | WACC inicial | CAGR implícito 1–5 | Error US$/acción |
|---|---|---|---|---|
| 40,00% | 1,12 | 10,57% | 15,91% | 0,00 |
| 40,00% | 1,32 | 11,50% | 17,44% | 0,00 |
| 43,00% | 1,12 | 10,57% | 13,82% | 0,00 |
| 43,00% | 1,32 | 11,50% | 15,29% | 0,00 |


Las filas de beta 1,32 son estrés de+0,20, con pesos y ERP constantes; no sustituyen la beta oficial ni una regresión que no se verificó. Cambiar margen y riesgo cambia el crecimiento que el precio exige. Con margen 43% y beta oficial, el crecimiento real equivalente al implícito es 11,26%; las bandas de la muestra histórica sitúan esa tasa entre 3,30% y 10,30% de las observaciones que igualan o superan el umbral. Ese rango no es una probabilidad de retorno bursátil. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit) [Mauboussin y Callahan, 26-sep-2016](https://mjbaldbard.wordpress.com/wp-content/uploads/2020/09/michael-mauboussin-e28093-base-rate-books-2015-2016.pdf)

El precio es compatible con una trayectoria entre Base y Conservadora bajo las demás hipótesis, pero esa lectura no demuestra que el mercado esté equivocado. Puede estar atribuyendo menor margen, más capital, obligaciones adicionales o menor duración de ventaja. La sanción de Nuevo México de US$25.000 M no está identificada como ajuste separado íntegro dentro del puente de18.590 M; no deben confundirse ambos asuntos ni duplicarse provisiones. Por ello la diferencia con cotización se interpreta con el alcance económico real de la hoja. [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm) [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

### Registro de decisión

| Campo | Revisión oficial R4 | Estimación del lector |
|---|---|---|
| Fecha | 23-oct-2026 |  |
| Historia | Publicidad rentable financia IA; eficiencia y ventaja persisten |  |
| Probabilidades B/C/O/D | 45/22,5/22,5/10% |  |
| DCF Base | 726,65 |  |
| Promedio ordinario | 746,63 |  |
| Disrupción aparte | 210,26 |  |
| Rango ordinario | 423,18–1.110,05 |  |
| Confianza | Mayor en conciliación matemática; limitada en retorno IA y ajustes patrimoniales |  |
| Qué cambia la opinión | Monetización, costo de servir, capital y reclamaciones verificables |  |
| Próxima revisión | Siguiente resultado/guía o evento material; fecha no comprobada |  |


La decisión de comprar, mantener o vender la registra el usuario. Este artículo no la sustituye.

### Nivel 2: valoración y cálculos de la misma revisión

#### Estados históricos conservados y cobertura

US$millones. Los datos siguientes son una extracción de las filas activas conservadas, no una nueva adquisición de todos los históricos. El balance completo, estados y ratios permanecen en las pestañas de la misma hoja; se incluyen magnitudes principales para trazabilidad. N/D en una partida significa ausencia identificada, nunca cero inventado. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

| Período | Ingresos | EBIT GAAP | Beneficio neto | OCF | CAPEX físico | I+D | SBC |
|---|---|---|---|---|---|---|---|
| 2016 | 27.638,00 | 12.427,00 | 10.217,00 | 16.108,00 | 4.491,00 | 5.919,00 | 3.218,00 |
| 2017 | 40.653,00 | 20.203,00 | 15.934,00 | 24.216,00 | 6.733,00 | 7.754,00 | 3.723,00 |
| 2018 | 55.838,00 | 24.913,00 | 22.112,00 | 29.274,00 | 13.915,00 | 10.273,00 | 4.152,00 |
| 2019 | 70.697,00 | 23.986,00 | 18.485,00 | 36.314,00 | 15.102,00 | 13.600,00 | 4.836,00 |
| 2020 | 85.965,00 | 32.671,00 | 29.146,00 | 38.747,00 | 15.163,00 | 18.447,00 | 6.536,00 |
| 2021 | 117.929,00 | 46.753,00 | 39.370,00 | 57.683,00 | 18.690,00 | 24.655,00 | 9.164,00 |
| 2022 | 116.609,00 | 28.944,00 | 23.200,00 | 50.475,00 | 31.186,00 | 35.338,00 | 11.992,00 |
| 2023 | 134.902,00 | 46.751,00 | 39.098,00 | 71.113,00 | 27.045,00 | 38.483,00 | 14.027,00 |
| 2024 | 164.501,00 | 69.380,00 | 62.360,00 | 91.328,00 | 37.256,00 | 43.873,00 | 16.690,00 |
| 2025 | 200.966,00 | 83.276,00 | 60.458,00 | 115.800,00 | 69.691,00 | 57.372,00 | 20.427,00 |
| LTM sep-2026 | 241.605,00 | 79.380,00 | 75.249,00 | 133.087,00 | 104.438,00 | 76.544,00 | 26.943,00 |


#### Inputs y ajustes que gobiernan los cálculos

| Entrada | Valor | Origen / ubicación |
|---|---|---|
| Ingresos LTM | 241.605,00 | Input B12; FY+9M−9M |
| EBIT GAAP LTM | 79.380,00 | Input B13; históricos intactos |
| Capital operativo con I+D | 398.897,67 | Valuation output B41; incluye activo I+D |
| Caja y negociables | 82.449,00 | Input B19; sin caja restringida |
| Inversiones | 32.624,00 | Input B20/B83; proxy contable |
| Deuda económica | 116.026,00 | Input B16; incluye leases |
| Reclamación legal modelada | 18.590,00 | Input B21; conciliación económica abierta |
| Opciones | 574,65 | Option value B30;20M, strike 2788,4 años |
| Acciones | 2.556,24M | Input B22; A+B al16-oct |
| I+D capitalizada | 3 años; activo 125.558,67 | R&D converter F7/D36 |
| Impuesto histórico / pronóstico | 4,58% /17% a 25,37% | Input B24 /B93 /B25 |
| Fracaso adicional | 0% | Input B52=No; disrupción ya tiene escenario |
| SBC | Gasto económico | No se añade al FCFF para crear valor gratis |
| Clase C | Efectividad estatuto 19-ene-2027 | Dividendo futuro; no se aplica anticipadamente |


#### De dónde sale el cálculo

Ingresos se proyectan con la senda anual. EBIT ajustado=ingresos×margen; NOPAT=EBIT×(1−impuesto); FCFF=NOPAT−reinversión. Se descuenta cada flujo a WACC anual y el terminal como FCFF 11/(WACC terminal−g). El ejemplo completo del año 1 y el puente físico se desarrollaron arriba. Las cifras no se multiplican por un factor de calibración para igualar la hoja. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

| Concepto | US$ millones |
|---|---|
| VPN FCFF 1–10 | 433.827,11 |
| VPN terminal | 1.443.772,11 |
| Valor operativo | 1.877.599,22 |
| Deuda económica | −116.026,00 |
| Otras reclamaciones legales modeladas | −18.590,00 |
| Caja y negociables | 82.449,00 |
| Inversiones no operativas (proxy contable) | 32.624,00 |
| Opciones | −574,65 |
| Patrimonio común | 1.857.481,57 |
| Acciones económicas, millones | 2.556,24 |
| Valor por acción US$ | 726,65 |



#### DCF anual — Base

| Año | Ingresos | Crecimiento | EBIT ajustado | NOPAT | Reinversión | FCFF | WACC | ROIC medio |
|---|---|---|---|---|---|---|---|---|
| 1 | 294.758,10 | 22,00% | 141.483,89 | 117.431,63 | 131.003,60 | -13.571,97 | 10,57% | 29,44% |
| 2 | 353.709,72 | 20,00% | 162.706,47 | 135.046,37 | 133.623,67 | 1.422,70 | 10,57% | 25,49% |
| 3 | 413.840,37 | 17,00% | 186.228,17 | 154.569,38 | 128.750,34 | 25.819,04 | 10,57% | 23,30% |
| 4 | 471.778,02 | 14,00% | 207.582,33 | 172.293,33 | 115.323,52 | 56.969,82 | 10,57% | 21,75% |
| 5 | 523.673,61 | 11,00% | 225.179,65 | 186.899,11 | 111.717,04 | 75.182,07 | 10,57% | 20,59% |
| 6 | 573.946,27 | 9,60% | 246.796,90 | 200.710,04 | 87.585,35 | 113.124,70 | 10,26% | 19,69% |
| 7 | 621.009,87 | 8,20% | 267.034,24 | 212.698,12 | 78.587,55 | 134.110,56 | 9,94% | 19,22% |
| 8 | 663.238,54 | 6,80% | 285.192,57 | 222.387,46 | 66.651,49 | 155.735,97 | 9,62% | 18,76% |
| 9 | 699.053,42 | 5,40% | 300.592,97 | 229.364,46 | 52.037,54 | 177.326,93 | 9,31% | 18,32% |
| 10 | 727.015,56 | 4,00% | 312.616,69 | 233.305,84 | 54.119,04 | 179.186,80 | 8,99% | 17,89% |

#### DCF anual — Conservadora

| Año | Ingresos | Crecimiento | EBIT ajustado | NOPAT | Reinversión | FCFF | WACC | ROIC medio |
|---|---|---|---|---|---|---|---|---|
| 1 | 273.013,65 | 13,00% | 131.046,55 | 108.768,64 | 68.253,41 | 40.515,23 | 10,57% | 27,27% |
| 2 | 300.315,02 | 10,00% | 130.937,35 | 108.678,00 | 60.063,00 | 48.614,99 | 10,57% | 23,26% |
| 3 | 324.340,22 | 8,00% | 134.276,85 | 111.449,79 | 56.759,54 | 54.690,25 | 10,57% | 21,14% |
| 4 | 347.044,03 | 7,00% | 136.041,26 | 112.914,25 | 52.056,60 | 60.857,64 | 10,57% | 19,34% |
| 5 | 367.866,67 | 6,00% | 136.110,67 | 112.971,86 | 51.501,33 | 61.470,52 | 10,57% | 17,76% |
| 6 | 388.467,21 | 5,60% | 143.732,87 | 116.892,19 | 43.092,55 | 73.799,65 | 10,26% | 17,00% |
| 7 | 408.667,50 | 5,20% | 151.206,98 | 120.439,38 | 41.846,18 | 78.593,20 | 9,94% | 16,48% |
| 8 | 428.283,54 | 4,80% | 158.464,91 | 123.567,77 | 40.200,23 | 83.367,54 | 9,62% | 16,00% |
| 9 | 447.128,02 | 4,40% | 165.437,37 | 126.235,33 | 38.153,67 | 88.081,66 | 9,31% | 15,53% |
| 10 | 465.013,14 | 4,00% | 172.054,86 | 128.404,54 | 39.679,82 | 88.724,73 | 8,99% | 15,09% |

#### DCF anual — Optimista

| Año | Ingresos | Crecimiento | EBIT ajustado | NOPAT | Reinversión | FCFF | WACC | ROIC medio |
|---|---|---|---|---|---|---|---|---|
| 1 | 306.838,35 | 27,00% | 147.282,41 | 122.244,40 | 113.294,16 | 8.950,24 | 10,57% | 30,65% |
| 2 | 380.479,55 | 24,00% | 181.108,27 | 150.319,86 | 128.777,70 | 21.542,17 | 10,57% | 29,35% |
| 3 | 464.185,06 | 22,00% | 220.023,72 | 182.619,68 | 142.826,17 | 39.793,51 | 10,57% | 28,49% |
| 4 | 557.022,07 | 20,00% | 262.914,42 | 218.218,96 | 154.252,26 | 63.966,70 | 10,57% | 27,84% |
| 5 | 657.286,04 | 18,00% | 308.924,44 | 256.407,28 | 153.703,81 | 102.703,47 | 10,57% | 27,33% |
| 6 | 757.193,52 | 15,20% | 355.880,95 | 289.423,74 | 190.987,23 | 98.436,51 | 10,26% | 26,51% |
| 7 | 851.085,51 | 12,40% | 400.010,19 | 318.616,12 | 166.195,86 | 152.420,26 | 9,94% | 24,84% |
| 8 | 932.789,72 | 9,60% | 438.411,17 | 341.864,26 | 129.023,38 | 212.840,88 | 9,62% | 23,59% |
| 9 | 996.219,42 | 6,80% | 468.223,13 | 357.272,98 | 81.057,04 | 276.215,93 | 9,31% | 22,64% |
| 10 | 1.036.068,20 | 4,00% | 486.952,05 | 363.412,32 | 84.299,33 | 279.112,99 | 8,99% | 21,91% |

#### DCF anual — Disrupción

| Año | Ingresos | Crecimiento | EBIT ajustado | NOPAT | Reinversión | FCFF | WACC | ROIC medio |
|---|---|---|---|---|---|---|---|---|
| 1 | 260.933,40 | 8,00% | 125.248,03 | 103.955,87 | 0,00 | 103.955,87 | 10,57% | 26,06% |
| 2 | 260.933,40 | 0,00% | 99.154,69 | 82.298,39 | 0,00 | 82.298,39 | 10,57% | 20,63% |
| 3 | 247.886,73 | -5,00% | 81.802,62 | 67.896,18 | 0,00 | 67.896,18 | 10,57% | 17,02% |
| 4 | 247.886,73 | 0,00% | 69.408,28 | 57.608,88 | 8.262,89 | 49.345,99 | 10,57% | 14,44% |
| 5 | 250.365,60 | 1,00% | 57.584,09 | 47.794,79 | 8.345,52 | 39.449,27 | 10,57% | 11,74% |
| 6 | 252.869,25 | 1,00% | 58.159,93 | 47.299,14 | 4.876,40 | 42.422,75 | 10,26% | 11,38% |
| 7 | 255.397,95 | 1,00% | 58.741,53 | 46.788,80 | 4.925,16 | 41.863,64 | 9,94% | 11,13% |
| 8 | 257.951,93 | 1,00% | 59.328,94 | 46.263,52 | 4.974,41 | 41.289,11 | 9,62% | 10,88% |
| 9 | 260.531,44 | 1,00% | 59.922,23 | 45.723,06 | 5.024,16 | 40.698,90 | 9,31% | 10,63% |
| 10 | 263.136,76 | 1,00% | 60.521,45 | 45.167,16 | 5.074,40 | 40.092,76 | 8,99% | 10,38% |


#### Sensibilidad Base

Todas las matrices muestran valor presente por acción US$, tienen el mismo centro US$726,65 y recalculan el motor completo. ROIC y margen también modifican el S/Cdependiente; WACC actualiza transición y descuento; el delta de crecimiento mantiene la forma de la senda. No son nuevos escenarios oficiales ni se publican matrices de otros escenarios. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)


#### WACC terminal × g

| Filas / columnas | 3,50% | 3,75% | 4,00% | 4,25% | 4,50% |
|---|---|---|---|---|---|
| 7,99% | 823,15 | 854,44 | 889,68 | 929,64 | 975,35 |
| 8,49% | 748,45 | 772,43 | 799,10 | 828,93 | 862,52 |
| 8,99% | 687,32 | 706,04 | 726,65 | 749,44 | 774,78 |
| 9,49% | 636,38 | 651,19 | 667,36 | 685,08 | 704,59 |
| 9,99% | 593,26 | 605,10 | 617,94 | 631,91 | 647,16 |

#### ROIC marginal terminal × g

| Filas / columnas | 3,50% | 3,75% | 4,00% | 4,25% | 4,50% |
|---|---|---|---|---|---|
| 10,76% | 564,36 | 570,29 | 576,83 | 584,08 | 592,15 |
| 14,35% | 641,21 | 655,13 | 670,46 | 687,43 | 706,29 |
| 17,93% | 687,32 | 706,04 | 726,65 | 749,44 | 774,78 |
| 21,52% | 718,07 | 739,98 | 764,10 | 790,78 | 820,43 |
| 25,11% | 740,03 | 764,22 | 790,85 | 820,30 | 853,05 |

#### Delta crecimiento 1–5 × margen EBIT ajustado

| Filas / columnas | 40,00% | 41,50% | 43,00% | 44,50% | 46,00% |
|---|---|---|---|---|---|
| -2,00% | 620,60 | 646,30 | 672,00 | 697,70 | 723,39 |
| -1,00% | 644,44 | 671,55 | 698,67 | 725,78 | 752,90 |
| 0,00% | 669,44 | 698,04 | 726,65 | 755,25 | 783,85 |
| 1,00% | 695,67 | 725,83 | 756,00 | 786,16 | 816,32 |
| 2,00% | 723,18 | 754,98 | 786,78 | 818,58 | 850,38 |


#### Múltiplos secundarios, horizonte de tres años

| Método | Múltiplo Base | VP Base US$ | Conservadora: × /VP | Optimista: × /VP | Observado congelado× | Peso |
|---|---|---|---|---|---|---|
| EV/EBITDA | 11,90× | 726,70 | 9,74× / 466,66 | 14,28× / 994,37 | 15,91× | 35,00% |
| EV/FCFF | 26,23× | 194,33 | 20,18× / 316,72 | 39,16× / 447,36 | N/D | 0,00% |
| P/E | 18,73× | 741,29 | 15,61× / 487,02 | 20,70× / 938,14 | 22,04× | 45,00% |
| P/FCFE | 15,79× | 112,07 | 13,15× / 203,36 | 24,43× / 268,44 | N/D | 0,00% |
| P/OCF | 9,73× | 670,80 | 8,58× / 462,38 | 12,75× / 999,85 | 12,46× | 0,00% |
| P/V | 5,13× | 614,85 | 4,52× / 426,88 | 7,34× / 984,37 | 6,86× | 20,00% |
| P/BV | 3,45× | 715,97 | 2,92× / 550,60 | 5,77× / 1.263,10 | 6,09× | 0,00% |


Las cifras se copian de Anclas META. VP incluye descuento a Ke y dividendos del auxiliar; el múltiplo observado usa la referencia congelada, no una cotización consultada hoy. La ponderación mecánica Base es US$711,00, Conservadora US$467,97 y Optimista US$967,18, con 35% EV/EBITDA,45% P/E y 20% P/V. No se mezcla con el DCF principal. EV/FCFF y P/FCFE tienen peso 0 por transitoriedad del flujo; P/OCF no penaliza por sí mismo inversión y SBC; P/BV mezcla intangibles e infraestructura. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

La columna C de Anclas META contiene anclas históricas ajustadas y la F aplica factores adicionales —por ejemplo 88% para EV/EBITDABase,90% para P/E y 85% para P/V— sin reconstrucción suficiente de soporte. Además, la columna E identifica su fórmula como diagnóstico terminal y no como techo FY+3. Esto no acredita el control de múltiplo justificado de la regla vigente. Se conservan las fórmulas y las salidas dependientes para revisión, con estado **CON HALLAZGOS**; no se afirma que sean múltiplos certificados. Las sensibilidades relativas existentes continúan vinculadas a esos cálculos auxiliares y no acreditan una segunda estimación independiente. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

La ausencia de una muestra completa impide afirmar barato/caro frente a la historia con confianza. **Barato frente a su historia no equivale a infravalorado intrínsecamente.** No se inventan nuevos pares, anclas ni matrices para ocultar ese faltante.

## 13. Filosofías de inversión

### Warren Buffett

La pregunta central es previsibilidad del efectivo del propietario. La publicidad es comprensible y repetitiva, pero centros de datos y opciones nuevas hacen menos estable la necesidad de capital; una buena franquicia puede producir menos efectivo distribuible mientras reinvierte. [Meta, 10-K, 29 de enero de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm) [Meta, 10-Q, 30 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm) [Meta, proxy, 16 de abril de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026025532/meta-20260416.htm)

- **Veredicto:** Mixto.
- **Encaje:** Encaja parcialmente.
- **Tres evidencias:**

1. Franquicia publicitaria rentable y distribuida.
2. Capacidad de servir muchos anunciantes con herramientas comunes.
3. Reinversión física aumenta y no tiene retorno marginal divulgado.

- **Principal objeción:** Beneficios estables no garantizan efectivo del propietario después de capacidad.
- **Pregunta pendiente:** ¿El retorno sobre capital incremental supera sostenidamente el costo, después de todo capex?

### Charlie Munger

La red y el aprendizaje pueden reforzarse entre sí; también pueden combinarse control concentrado y abundancia de caja para sostener proyectos poco rentables. El riesgo relevante es acumular compromisos mientras se acepta una narrativa tecnológica difícil de refutar. [Meta, 10-K, 29 de enero de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm) [Meta, 10-Q, 30 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm) [Meta, proxy, 16 de abril de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026025532/meta-20260416.htm)

- **Veredicto:** Mixto.
- **Encaje:** Encaja parcialmente.
- **Tres evidencias:**

1. Distribución y optimización pueden tener efectos combinados.
2. El proxy confirma control y exposición patrimonial del fundador.
3. Contratos largos y garantías JV crean complejidad fuera del beneficio corriente.

- **Principal objeción:** Los mismos incentivos que favorecen paciencia pueden reducir disciplina.
- **Pregunta pendiente:** ¿Qué hitos obligan a recortar una apuesta de baja rentabilidad?

### Peter Lynch

Encaja mejor como empresa estable rentable con nuevas líneas rápidas que como un único negocio de hipercrecimiento. La historia sencilla es mejorar campañas; la historia compleja es añadir agentes y hardware sin deteriorar beneficio por acción. [Meta, 10-K, 29 de enero de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm) [Meta, 10-Q, 30 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm) [Meta, proxy, 16 de abril de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026025532/meta-20260416.htm)

- **Veredicto:** Mixto.
- **Encaje:** Encaja parcialmente.
- **Tres evidencias:**

1. Family of Apps domina ventas.
2. Usuarios maduran mientras monetización impulsa crecimiento.
3. RL y agentes tienen economía distinta.

- **Principal objeción:** Una narrativa sencilla puede ocultar que el costo de servir cambia.
- **Pregunta pendiente:** ¿Ingresos y beneficio por acción crecen sin más deuda y dilución?

### Howard Marks

El análisis de segundo nivel separa crecimiento observable de expectativas necesarias. Un rango amplio de resultados y contratos rígidos hacen que el daño permanente dependa de capital mal invertido, aunque la cotización recupere una caída; la volatilidad por sí sola no demuestra oportunidad. [Meta, 10-K, 29 de enero de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm) [Meta, 10-Q, 30 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm) [Meta, proxy, 16 de abril de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026025532/meta-20260416.htm)

- **Veredicto:** Mixto.
- **Encaje:** Encaja parcialmente.
- **Tres evidencias:**

1. El ciclo publicitario afecta presupuesto.
2. Capacidad se contrata antes de monetización.
3. Las historias incluyen deterioro duradero de retornos.

- **Principal objeción:** El escenario central puede subestimar la rigidez de compromisos y regulación.
- **Pregunta pendiente:** ¿Qué condiciones impedirían recuperar el capital incluso con demanda en recuperación?

### Joel Greenblatt

Retorno y beneficio operativo son informativos cuando el capital empleado refleja el negocio. I+D como gasto, goodwill y arrendamientos cambian la base contable; una rentabilidad pasada alta no identifica la de los nuevos centros de datos. Se necesita normalización antes de comparar eficiencia. [Meta, 10-K, 29 de enero de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm) [Meta, 10-Q, 30 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm) [Meta, proxy, 16 de abril de 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026025532/meta-20260416.htm)

- **Veredicto:** Mixto.
- **Encaje:** Encaja parcialmente.
- **Tres evidencias:**

1. EBIT es positivo y de escala.
2. La tasa fiscal reportada distorsiona beneficio neto.
3. PPE y compromisos alteran intensidad de capital.

- **Principal objeción:** ROIC agregado mezcla inversión madura y capacidad aún no productiva.
- **Pregunta pendiente:** ¿Qué retorno normalizado queda al incluir capital físico, leases e inversión intangible consistentemente?

## 14. Noticias y eventos recientes

La ventana es26-jul–23-oct-2026. El inventario de SECsubmissions se revisó para 8-K/6-K desde el cierre financiero hasta el corte; identifica un8-K presentado 21-oct, evento 19-oct, con resultados y recapitalización. También se examinó el10-Q presentado 22-oct, incluyendo notas legales y hecho posterior. Un inventario de formularios no acredita ausencia de todo otro anuncio público. No se reutiliza la frase del informe del 11-oct que decía que no había 8-Kposteriores. [SEC submissions, consultado 23-oct-2026](https://data.sec.gov/submissions/CIK0001326801.json)

| Fecha | Acontecimiento verificado | Importancia | Impacto | ¿Cambia la tesis? | Fuente |
|---|---|---|---|---|---|
| 29–30-jul-2026 | Resultados Q2 y 10-Q | Nuevo punto previo de inversión y márgenes | Mixto | Contextualiza aceleración de capital | 10-Qjunio |
| Ago-2026; divulgado Q3 | Acuerdo con fiscales hasta 18.590M | Pagos y cambios en productos para menores | Negativo | Requiere puente y costos sin doble cómputo | 10-Qnota 10 |
| 25-sep y 21-oct-2026 | Caso privacidad Nuevo México; sanción 25.000M con interés 15% | Asunto distinto del acuerdo | Negativo | Puede afectar caja/colateral y valoración | 10-Q; apelación anunciada |
| 29-sep-2026 | Opinión fiscal suplementaria | Actualiza incertidumbre de precios de transferencia | Mixto | Revisar provisión; no perpetuar tasa efectiva baja | 10-Qnota 12 |
| 19-oct; presentado 21-oct-2026 | Recapitalización y clase C | Financiación y derechos de voto | Mixto | No aplicar dividendo antes de efectividad | 8-K;10-Qnota 14 |
| 21-oct-2026 | Resultados Q3, guía Q4 e inversión | Mantiene crecimiento y CAPEX alto | Mixto | Sustenta crecimiento inicial y presión de flujos | Comunicado IR |
| 21-oct-2026 | Guía pérdidas Reality Labs 2027 cercana 15.000M | Reducción potencial de consumo de excedente | Positivo condicionado | Verificar realización y reasignación a IA | Comunicado IR |


Fuentes directas: [Meta 10-Qjunio,30-jul-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm); [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm); [Meta resultados, 21-oct-2026](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/); [Meta 8-K,21-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066700/meta-20261019.htm). El19-ene-2027 corresponde a la efectividad prevista del estatuto de clase C; las fechas de registro y pago del dividendo serán determinadas por el consejo. No se afirma que se pagará ese mismo día.

## 15. Qué vigilar

Los umbrales cuantitativos siguientes son reglas analíticas propuestas para seguimiento de R4, salvo la guía expresa de la compañía. Derivan de las sendas del modelo o de su referencia actual; no son previsiones del emisor ni disparadores retroactivos de probabilidades. Antes de usarlos para mover 5pp se fijará su persistencia y fecha en la ficha. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

| Métrica / evento | Tesis | Umbral favorable | Alerta | Frecuencia | Próxima fecha conocida | Fuente del umbral |
|---|---|---|---|---|---|---|
| Ingresos | Base/Optimista | Senda 22% a 11% en cinco años o mejor con caja | Por debajo de senda sin compensación de capital | Trimestral | Siguiente resultado; fecha N/D | Modelo R4 |
| Impresiones y precio | Demanda útil | Ambos positivos con conversiones sostenidas | Precio negativo pese a más inventario | Trimestral | Siguiente resultado | Economía del anuncio; Q3+10/+14 |
| Audiencia DAP | Distribución | Uso estable o creciente sin perder calidad | Caída persistente y pérdida de utilidad | Trimestral | Siguiente resultado | Mecanismo de red; sin cuota inventada |
| Margen GAAP normalizado | Monetización | Sostiene coste de servir y converge en puente | Menor margen sin cargo puntual nuevo | Trimestral | Siguiente resultado | Puente I+D, no umbral GAAP 43% |
| CAPEX 2026 | Financiación | Dentro 135–145 mil M con capacidad utilizable | Supera guía sin más monetización | Trimestral | Cierre FY 2026 | Guía 21-oct |
| S/C marginal | Capital | Mejora sobre referencia 0,47 sin diferir inversión necesaria | Cae pese a puesta en servicio | Anual/LTM | Nuevo 10-Q/10-K | Hoja y definición incremental |
| FCFF | Conversión | Mejora desde déficit inicial hacia senda del modelo | Déficit persiste al madurar inversiones | Trimestral/anual | Nueva información | DCF y puente de inversión |
| Retorno estable | Moat | Evidencia respalda exceso sobre 8,99% | Competencia elimina ese exceso | Anual | Nuevo ejercicio | WACC y referencia 17,93% |
| SBC/acciones | Resultado por acción | Caja por acción crece después de remuneración | Denominador sube sin retorno proporcional | Trimestral | Nuevo 10-Q | No hay reducción neta predeterminada |
| Litigios y leases | Reclamaciones | Pagos y contratos conciliados con flujos | Obligación adicional o colateral no modelado | Por evento | Fechajudicial N/D | 10-Qnotas 8/10 |
| Clase C | Comparabilidad | Ajuste simultáneo precio/acciones al efectuarse | Solo cambia un denominador o se anticipa el split | Por evento | Estatuto 19-ene-2027; pago N/D | 10-Qnota 14 |


La lectura debe ser conjunta. Menor CAPEX puede mejorar caja hoy a costa de menor capacidad mañana; mayor OCF puede provenir de SBC o capital de trabajo; más impresiones pueden reducir la calidad del producto. El seguimiento cambia los supuestos por mecanismos observables, no por un movimiento aislado de la cotización.

## 16. Preguntas abiertas

Se resolvieron el corte LTM, el contraste entre margen GAAP y ajustado por I+D, las acciones económicas actuales y el carácter futuro de clase C. Se confirmó que el ROIC 17,93% es la referencia global después de impuestos con ajustes de I+D y leases, no el retorno de nuevos proyectos de Meta. También se documentó la sanción 25.000M de Nuevo México como asunto distinto del acuerdo 18.590M. [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm) [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit) [Damodaran,05-ene-2026](https://www.stern.nyu.edu/~adamodar/pc/datasets/rocGlobal.xls)

Después de revisar notas, comunicado, inventario 8-K y referencias de la hoja, estas preguntas siguen siendo materiales. Varias requieren divulgación adicional; no pueden resolverse obteniendo otra vez los mismos estados.

| Pregunta | Por qué importa | Evidencia disponible | Dato faltante | Respuesta que fortalece / debilita |
|---|---|---|---|---|
| ¿Qué retorno y costo de servir tiene cada uso de IA? | Distingue crecimiento de creación de valor | Uso/productos y gasto agregado | Ingresos, costo e inversión por cohorte/proyecto | Monetización cubre capital y reposición /solo crece uso |
| ¿Cuánto CAPEX es mantenimiento frente a expansión? | Evalúa gasto que no puede suspenderse | PPE, construcción, guías | Separación homogénea y vida económica de equipos | Reposición sostenible /obsolescencia acelerada |
| ¿Qué parte de contratos ya está en reinversión o gastos? | Evita omitir o duplicar pagos | Compromisos agregados yleases | Mapa por contrato, calendario yperímetro | Puente reconciliado /solapamientos |
| ¿Cómo se cubre Nuevo México en provisiones y garantías? | Afecta caja y patrimonio | Sanción, interés, apelación y devengo sinmonto aislado | Provisión atribuible, calendario ycolateral | Exposición neta acotada /salidasadicionales |
| ¿Cuál es el saldo vigente detallado de leasesfinancieros? | Completa deuda y capital invertido | Activos y pagos; proxy 1184 en registro | Pasivo yvencimientos reconciliados | Desgloseconsistente /diferencia material |
| ¿Qué valor realizable tienen inversiones privadas? | Libro no equivale a efectivo | Saldo 32624 ynotas | Valor atribuible neto ycondiciones de realización | Valor sustentado /deterioros oindisponibilidad |
| ¿Cuánta dilución requerirá financiar las apuestas? | Evalúa valor por acción | SBC, RSU yclase C | Emisión futura, usos yretorno por acción | Capital captado rentable /dilución sin retornos |
| ¿Qué muestra histórica justifica los factores de los múltiplos? | Evita prudencia o primas arbitrarias | Anclas conaños citados yfactores | Precios, denominadores ytope económico comparable | Ancla reproducible /factor sin soporte |


La última pregunta es un hallazgo de la metodología auxiliar actual, no incertidumbre normal de pronóstico. Las primeras preguntas sobre rentabilidad de productos tienen límites de divulgación; no se presentan respuestas numéricas fabricadas.

## 17. Fuentes

### Fuentes primarias

- **Form 10-Q al30-sep-2026**, Meta,22-oct-2026, consultado 23-oct-2026. [Documento](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm). Estados, segmentos, geografía, compromisos, impuestos, opciones y hechos posteriores.
- **Resultados Q3-2026**, Meta,21-oct-2026, consultado 23-oct-2026. [Comunicado](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/). Guías y métricas operativas; no previsión numérica de ingresos 2027.
- **Form 8-K**, Meta, evento 19-oct ypresentación 21-oct-2026, consultado 23-oct-2026. [Documento](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066700/meta-20261019.htm).
- **Form 10-K FY2025**, Meta,29-ene-2026, consultado 23-oct-2026. [Documento](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm). Historia empresarial y riesgos; no se vuelve a certificar toda la serie 2016–2025.
- **Proxy 2026**, Meta,16-abr-2026, consultado 23-oct-2026. [Documento](https://www.sec.gov/Archives/edgar/data/1326801/000162828026025532/meta-20260416.htm). Gobierno, incentivos y estructura de voto.
- **Form 10-Q junio 2026**, Meta,30-jul-2026, consultado 23-oct-2026. [Documento](https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm). Comparación de fase de inversión.
- **Resultados Q2-2026**, Alphabet, julio 2026, consultado 23-oct-2026. [Documento SEC](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm). Contraste de plataforma madura y perímetro de costos de IA.
- **Historial de formularios CIK 1326801**, SEC, consultado 23-oct-2026. [Registro](https://data.sec.gov/submissions/CIK0001326801.json). Inventario de8-K/6-K en el corte.

### Fuentes secundarias y sectoriales

- **Return on capital Global**, Aswath Damodaran, actualización 05-ene-2026, descargado 23-oct-2026. [Excel](https://www.stern.nyu.edu/~adamodar/pc/datasets/rocGlobal.xls). Advertising 419;17,93% ROIC después de impuestos, ajustado por I+D yleases. La muestra no reproduce exactamente la mezcla de Meta.
- **Betas Global**, Aswath Damodaran, enero 2026, consultado 23-oct-2026. [Tabla](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/BetasGlobal.html). Contraste de referencia sectorial; los valores activos y su reapalancamiento se leen de la hoja.
- **The Base Rate Book**, Michael Mauboussin y Dan Callahan,26-sep-2016, Exhibit 4p25, consultado 23-oct-2026. [Copia del informe de los autores](https://mjbaldbard.wordpress.com/wp-content/uploads/2020/09/michael-mauboussin-e28093-base-rate-books-2015-2016.pdf). Tasas reales por tamaño; se utilizan bandas publicadas, no probabilidades específicas de Meta.
- **Bayes and Base Rates 2.0**, Michael Mauboussin y Dan Callahan/Morgan Stanley,13-may-2026, consultado 23-oct-2026. [Informe](https://www.morganstanley.com/im/publication/insights/articles/article_bayesandbaserates2_ltr.pdf). Contexto de actualización de distribuciones y cautela al extrapolar crecimiento.
- **Modelo JMR META R4**,23-oct-2026. [Hoja](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit). Fuente de supuestos y cifras oficiales deesta revisión. Precio 22-oct conservado del expediente, sin actualizar cotización. Rf/ERP y CRP se conservan del cálculo detallado; su revisión integral no se afirma en esta sesión.
- **Reglas vigentesv 5 yprompt 2 actualizado**, Modelo JMR,23-oct-2026. [Reglas](https://github.com/JuanMaRobledo/Modelo-JMR/blob/main/modelo/REGLAS_VIGENTES.md) y[prompt](https://github.com/JuanMaRobledo/Modelo-JMR/blob/main/docs/prompts/research-fundamental-jmr-v5.md). Especificación editorial; no fuente de datos del emisor.

Se recuperó el artículo completo del 11-oct para preservar desarrollo pertinente de negocio, industria y filosofías. Sus valoraciones, escenarios y referencias financieras antiguas no alimentan R4. El informe corto R1 del 23-oct se sustituye por este artículo con la revisión actual de la hoja.

## 18. Control de calidad final

La revisión editorial desarrolla las 18 secciones y conserva los límites identificados; no declara resueltos los bloques marcados como limitados. El estado financiero global sigue **CON HALLAZGOS**, aunque los cálculos DCF y sus dependencias fueron reproducidos. Las limitaciones de fuente no se convierten en datos supuestos ni una tabla de títulos se presenta como certificación.

| Apartado | Ubicación / desarrollo | Cobertura | Evidencia | Limitación concreta |
|---|---|---|---|---|
| 1 | Dos párrafos,8 puntos ypremisas | Desarrollado y sustentado | 10-K,10-Q, modelo | — |
| 2 | Tabla y siete dimensiones económicas | Desarrollado y sustentado | 10-K y 10-Q | Retención contractual no publicada; no se inventa |
| 3 | Segmentos ygeografía | Desarrollado y sustentado | 10-Qnotas 2/13 | Concentración porproveedor/cliente no cuantificada |
| 4 | Industria y Porter | Limitado por evidencia identificada | 10-K; sector Damodaran | TAM/cuota primaria homogénea no documentados |
| 5.1 | Resultados, balance y caja | Desarrollado y sustentado | Estados hoja; último 10-Q | Históricos preservados, no recertificados íntegramente |
| 5.2 | Ratios 3/5/10 años | Limitado por evidencia identificada | Filas conservadas | No serie ROIC ajustada homogénea de10 años |
| 5.3 | Calidad y contraste de entradas | Desarrollado y sustentado | Celdas activas yfuentes | Ajustes de puente abiertos se explican |
| 6 | Fuentes de moat yveredicto | Desarrollado y sustentado | 10-K,10-Q, ROICsectorial | Retorno IA por proyecto no divulgado |
| 7 | Rivales ysustitutos | Limitado por evidencia identificada | 10-K; Alphabet Q2 | Pares de múltiplos a igualfecha no reconstruidos |
| 8.1 | Equipo, gobierno, incentivos | Desarrollado y sustentado | Proxy y 10-Q | Sucesión deunidad IA no verificable |
| 8.2 | Seis usos de capital | Desarrollado y sustentado | Caja, notas ymodelo | Retorno adquirido segregado N/D |
| 9 | Seis catalizadores | Desarrollado y sustentado | Comunicado,10-Q,8-K | Fechas futuras no anunciadas se indican N/D |
| 10 | Ocho riesgos, cuatro historias, FODA | Desarrollado y sustentado | Fuentes ymodelo | Probabilidades cualitativas no estadísticas |
| 11 | Bulls/Bears, conclusión, síntesis | Desarrollado y sustentado | Secciones previas | — |
| 12.1 | Historia ytasas base | Desarrollado y sustentado | Base Rate Book Exhibit 4 | Fracciones enbandas; no interpolación arbitraria |
| 12.2 | Crecimiento, margen, I+D, capital | Desarrollado y sustentado | Modelo,10-Q, guía | Proyección no desglosada por producto |
| 12.3 | ROIC, riesgo yterminal | Limitado por evidencia identificada | Sector ycosto de capital | Beta regresión y CRP paísporpaís no verificados |
| 12.4 | Cuatro DCF, promedio, disrupción | Desarrollado y sustentado | Hoja yreproducción independiente | — |
| 12.5 | Premortem, indicadores, precio, inverso | Desarrollado y sustentado | Motor yreferencia congelada | Beta alternativa esestrés explícito |
| 12.6 | Nivel 2: históricos, anuales, matrices, puente | Desarrollado y sustentado | Rangos R4 y JSON | No certifica interpretación económica completa de contratos |
| 12.7 | Múltiplos secundarios | Limitado por evidencia identificada | Anclas META | Anclas, cargos porfactores ytope FY+3 conhallazgos |
| 13 | Cinco filosofías, formatos independientes | Desarrollado y sustentado | Análisis previo pertinente actualizado | Son marcos de evaluación, no citas depersonas |
| 14 | Ventana 90 días einventariofilings | Desarrollado y sustentado | SECsubmissions,8-K,10-Q | No prueba ausencia detodoanuncio público |
| 15 | Once indicadores | Desarrollado y sustentado | Guía ysupuestos R4 | Umbrales nuevos no activan cambiosretroactivos |
| 16 | Resueltas yocho preguntas concretas | Desarrollado y sustentado | Fuentes investigadas | Faltantesmateriales específicos visibles |
| 17 | Fuentes primarias ysectoriales | Desarrollado y sustentado | Enlaces consultados | Precio es del expediente, no cierre refrescado |
| 18 | Control nominal ysemántico | Desarrollado y sustentado | Esteartículo yverificación R4 | Cobertura resuelta no seafirma enfilas limitadas |


Se comprobó igualdad de históricos en Income Statement A1: L36, Balance Sheet A1: L40 y Cash Flow Statement A1: L40 antes/después; cuatro DCF coinciden con hoja en menos de0,001US$/acción;75 celdas de sensibilidad coinciden con cálculo separado; los tres centros e inverso concilian. No se ejecutó controles_todas.sh ni se afirmó correspondencia con una app publicada. Se verificó contenido numérico y formato de celdas relevantes; el aspecto en la interfaz nativa de Google Sheets no fue renderizado en esta sesión.

1. La valoración oficial se reproduce en la sección 12 y en el recuadro inicial obligatorio; la cotización se introduce al final de la sección 12. No se emite una recomendación transaccional.
2. Las cifras materiales proceden de las fuentes enlazadas o del modelo R4; se identifican el precio congelado y los componentes de riesgo conservados que no se verificaron íntegramente de nuevo.
3. Datos, guía y proyecciones se distinguen por atribución y contexto, sin etiquetas narrativas repetitivas.
4. Los cinco marcos de inversión tienen conclusiones independientes y no se atribuyen citas inventadas a sus autores.
5. Bulls y Bears contienen seis argumentos porlado y exponen el desacuerdo operativo central.
6. Las noticias están fechadas dentro de90 días; se distingue evento, presentación yefectividad futura.
7. Se conservaron y desarrollaron los encabezados literales «Las 5 fuerzas de Porter» y «Síntesis final», y se declararon las limitaciones de evidencia en sus apartados.
8. El documento es Markdown editable, contiene exactamente 18 secciones enorden y termina enesta confirmación.


---

## Adenda posterior al análisis — riesgos económicos comprobados (R4-A1, 23-oct-2026)

El artículo original de 18 secciones conserva su integridad y su DCF US$726,65/acción; la presente adenda añade hechos de notas contables necesarios para interpretar sus supuestos.

**Riesgo legal:** el juicio Nuevo México de US$25.000M + interés de 15% sobre la sentencia es separado del arreglo multilateral. Meta afirma que registró provisión, sin desagregar su cuantía. El saldo agregado de provisiones legales reconocido (US$19.881M: corrientes 11.577 y no corrientes 8.304) **no permite imputar el caso NM**. El acuerdo de 52 procuradores incluye pagos multianuales y un tramo contingente no reconocido. La interpretación del margen debe diferenciar cargo GAAP, retorno operativo sostenible y caja efectivamente desembolsada, evitando restar el mismo costo dos veces.

**Productividad del capital:** la guía 2026 de inversión US$135–145bn, los compromisos no cancelables US$454,52bn y leases por iniciar US$355,73bn confirman alta rigidez futura. No se deben sumar las dos últimas cifras por riesgo de solapamiento, ni descontarlas completas como deuda. Un S/C 0,45 en años 1–5 y 0,54 en años 6–10 necesita demostrar que la inversión incremental que libera capacidad está contenida en Δingresos/reinversión y no se omiten contratos. ROIC marginal terminal 17,93% es una hipótesis de ventaja durable; no existe todavía evidencia de rendimiento desagregado por cada centro de datos o producto IA.

**Activos:** caja libre del puente US$82.449M excluye los US$10.800M de escrow restringido. Las inversiones de US$32.624M son valor en libros, incluyendo US$4.732M en JV datacenters, cuyos acuerdos de arrendamiento conectan la participación con los costos futuros del negocio; no presentar su valoración autónoma como justa ni independiente sin análisis de solapamiento.

**Rentabilidad y costo de capital:** la Rf 5,29% y prima madura 3,70% son ambas del snapshot Damodaran de septiembre publicado el 8 de octubre. El Tesoro del 22 de octubre (~4,96%) cambió. Es necesario fechar y sincronizar todas las primas y WACC si se adopta el nuevo corte. Ninguna de estas incertidumbres habilita optimismo artificial de márgenes, reinversión o ROIC para justificar una cotización.

**Tesis contraria ampliada:** Meta puede crecer comercialmente mientras su FCFF se deteriora si la inversión comprometida crece más deprisa que la monetización y suben los costos de cumplimiento o litigios. Un escenario de caída de ROIC hacia WACC reduce significativamente el valor terminal; la propia auditoría R4 calcula US$503,08 bajo escenario sin ventaja competitiva terminal. Esa cifra es una prueba de sensibilidad, no el DCF Base.

**Estado editorial:** tesis y estados históricos preservados; adenda R4-A1 registrada; vínculo documental/valoración R4 conciliado; auditores económicos y publicación **pendientes** de pruebas de obligaciones, capital y múltiplos. Fuente primaria [SEC 10-Q 22-oct](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm); [hoja R4](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit).


## Adenda final R4-A2 — cierre proporcional de los supuestos necesarios (23-oct-2026)

**Mismo modelo financiero:** `META-20261023-r4`. No se ha creado otra revisión de supuestos ni se recalibró la cifra DCF. El paquete R4-A2 es una **actualización del dictamen y las evidencias**, no un nuevo modelo de valoración.

Los elementos imprescindibles tienen hipótesis explícitas y pruebas: crecimiento Base anual 22%, 20%, 17%, 14% y 11%; margen EBIT *ajustado por capitalización de I+D* 48% a 43%, que no debe confundirse con el margen GAAP; Sales-to-Capital 0,45 y 0,53735 (marginal; reinversión adelantada); ROIC terminal 17,93%; tasa fiscal 17% convergente a 25,37%; WACC 10,57% inicial y 8,99% terminal; `g` perpetua de 4,00%. El año uno ya invierte US$131.003,60M, por lo que no procede añadir íntegramente a deuda los compromisos contractuales anunciados. El valor terminal aporta 76,89% del EV: la continuidad del moat es la fuente principal de sensibilidad.

Se usa US$726,65/acción como **valor intrínseco Base del modelo**, con tesis y sensibilidad contrapuesta: si el ROIC marginal de la perpetuidad convergiera al WACC, la prueba del expediente da unos US$503,08/acción (−30,77%). Eso es un caso alternativo, no el valor Base. El inverso muestra CAGR implícito de 13,82% para años 1–5 a precio congelado de US$648,85 del 22-oct.

Los faltantes secundarios se **aceptan como juicios con trazabilidad** sin inventar datos: el castigo judicial Nuevo México US$25.000M, *si fuera íntegramente adicional*, implicaría US$−9,78/acción (−1,35%), **sin** incluir interés judicial 15% ni consecuencias operativas; realizar a cero US$32.624M de inversiones privadas impactaría US$−12,76/acción (−1,76%); retirar solo el proxy leasing financiero de US$1.184M movería cerca de +0,06%, lo que **no acota** obligaciones no reveladas; una erogación extraordinaria de CAPEX no ya modelada por US$100.000M en el primer año alteraría el precio en −4,87%, pero múltiples años repetidos afectarían mucho más. **Estas sensibilidades no son sumables automáticamente**.

La provisión reconocida por el litigio de Nuevo México **no está individualizada** en el 10-Q; la provisión legal agregada es US$19.881M. El modelo deduce aparte el máximo del acuerdo multistate US$18.590M como hipótesis conservadora y no incorpora toda la multa Nuevo México como otro pasivo cierto. Las inversiones privadas US$32.624M son un proxy a valor contable y los múltiplos relativos siguen *ilustrativos/no verificados*. Nunca convertir «VALIDADO» de una celda formal en certificación económica.

**Conclusión para valoración y auditoría:** **APTO PARA VALORACIÓN PERSONAL CON SALVEDADES**. **Publicación/app:** pendiente de ejecución autenticada de `desde_cero.sh validar META`, `audit_master_formulas.py --gates --strict`, `audit_report_contract.py`, `controles_todas.sh META` y de generación y lectura visual de **Nivel 1, Nivel 2 y auditoría con la misma hoja/JSON R4**. Ninguno de estos gates se declara ejecutado ni exitoso aquí.

Fuentes: [Meta 10-Q 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm), [Damodaran 8-oct-2026](https://aswathdamodaran.substack.com/p/earnings-cashflows-and-stock-prices), [hoja Google R4](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit), [PR META R4-A2](https://github.com/JuanMaRobledo/JMR-valuation/pull/140).