---
schema: "jmr-fundamental-research-v5"
title: "Análisis fundamental de Netflix, Inc."
ticker: "NFLX"
company: "Netflix, Inc."
market: "Nasdaq Global Select Market (Estados Unidos)"
analysis_date: "2026-10-25"
information_cutoff: "2026-09-30"
revision_id: "NFLX-2026-10-25"
valuation_status: "VERIFICADO con salvedades no bloqueantes (auditoría NFLX-2026-10-25) · publicación autorizada el 25-oct-2026"
valuation_sheet: "https://docs.google.com/spreadsheets/d/1ZPNMHxc7m3Iv60mdGspgi6-cc2zwf5kZ4ocsuANQUNM/edit"
results_snapshot_sha256: "6afa5b6aba533dcbd28143ba547eb3c98de1b541d5695a9a0e6351a2a06e58d5"
supersedes: "data/NFLX_Research_Fundamental_Modelo_JMR_2026-10-21.md (LTM a junio de 2026; se archiva al publicar esta revisión)"
currency: "USD"
language: "es"
generator: "Claude Code"
---

# Netflix, Inc. (NFLX)

> **Valor intrínseco base: US$70,85 por acción** · DCF FCFF Base con criterio Damodaran · corte del 30-sep-2026 · revisión `NFLX-2026-10-25`. Las cifras de valoración salen de [la hoja del Modelo JMR](https://docs.google.com/spreadsheets/d/1ZPNMHxc7m3Iv60mdGspgi6-cc2zwf5kZ4ocsuANQUNM/edit) y de la misma foto de resultados que usan la valoración y la auditoría de esta revisión; aquí no se recalculan.
>
> **Base de datos de esta revisión:** estados financieros hasta el 30 de septiembre de 2026 (10-Q del 3T26, presentado el 21 de octubre de 2026). Los últimos doce meses (LTM) van de octubre de 2025 a septiembre de 2026. Precio, tasa libre y prima de riesgo son los del corte común de la cartera (30-sep-2026). La versión anterior del artículo (21-oct-2026) usaba LTM a junio y trataba el 3T26 como hecho posterior; queda archivada con la publicación autorizada de esta revisión. La carta del 3T26 (20-oct-2026) se usa para el trimestre que ya está en los estados, y su guía del 4T26 se trata como hecho posterior.

> Alcance: análisis fundamental con fines informativos; no constituye asesoramiento financiero ni recomendación de compra o venta.

**Índice**

- [1. Resumen ejecutivo](#1-resumen-ejecutivo)
- [2. Modelo de negocio](#2-modelo-de-negocio)
- [3. Segmentos y geografía](#3-segmentos-y-geografia)
- [4. Industria y crecimiento](#4-industria-y-crecimiento)
- [5. Calidad del negocio](#5-calidad-del-negocio)
- [6. Ventaja competitiva](#6-ventaja-competitiva)
- [7. Competencia](#7-competencia)
- [8. Gestión y asignación de capital](#8-gestion-y-asignacion-de-capital)
- [9. Catalizadores](#9-catalizadores)
- [10. Riesgos](#10-riesgos)
- [11. Bulls say / Bears say](#11-bulls-say--bears-say)
- [12. Valor con criterio Damodaran](#12-valor-con-criterio-damodaran)
- [13. Filosofías de inversión](#13-filosofias-de-inversion)
- [14. Noticias y eventos recientes](#14-noticias-y-eventos-recientes)
- [15. Qué vigilar](#15-que-vigilar)
- [16. Preguntas abiertas](#16-preguntas-abiertas)
- [17. Fuentes](#17-fuentes)
- [18. Control de calidad final](#18-control-de-calidad-final)

El Nivel 2 del análisis está en `NFLX_Nivel2_Datos_Modelo_JMR_2026-10-25.md`, generado de la misma revisión sin recalcular. Contiene los estados de diez años y LTM, ratios, entradas, costo de capital, el FCFF de las cuatro historias año por año, el puente al valor por acción, múltiplos y matrices de sensibilidad.

## 1. Resumen ejecutivo

Netflix, Inc. cobra una suscripción mensual, y cada vez más publicidad, por acceder a un catálogo de series, películas, eventos en vivo y juegos que produce, licencia y distribuye con su propia red de entrega. En 2025 ingresó US$45.183 millones (+15,9%), con un margen operativo de 29,5% frente a 17,8% en 2022 ([Netflix, 10-K 2025, 23 de enero de 2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm)). En los doce meses a septiembre de 2026 los ingresos llegaron a US$49.735 millones y el margen operativo a 31,3% ([Netflix, 10-Q del 3T26, 21 de octubre de 2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm)).

La empresa dejó de publicar membresías en 2025 y dice medirse por ingresos y margen. La pregunta económica es si un negocio que llega a casi mil millones de personas puede seguir creciendo a dos dígitos y ampliando el margen cuando el tiempo de visualización crece apenas 2% al año ([Netflix, carta a accionistas del 2T26, 16 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000211/ex991_q226.htm)).

La tensión central está entre dos fuerzas. Por un lado, un crecimiento de ingresos que hoy depende del precio por miembro, de la publicidad y de los mercados fuera de Norteamérica. Por otro, un uso por miembro que casi no crece mientras YouTube, el video corto y otras plataformas compiten por la misma atención.

A favor trabajan:
- La escala de audiencia y de gasto en contenido: US$17.097 millones en adiciones de contenido en 2025 y US$19.991 millones en el LTM.
- Un margen que sube porque la amortización del contenido crece menos que los ingresos (34,6% en el 3T26).
- Una generación de caja que financió recompras récord: US$4.800 millones en el 3T26, según la [carta del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm).

En contra están la menor visibilidad de las métricas de uso, el costo creciente de los derechos deportivos y la rebaja de la meta de publicidad de 2026 (de ~US$3.000 a ~US$2.700 millones). El Modelo JMR resuelve esa tensión con cuatro historias (Base, Conservadora, Disrupción y Optimista), que se examinan en las secciones 10 y 12.

- **Qué vende y por qué paga el cliente.** Una suscripción mensual cuyo precio va del equivalente a US$1 a US$37 según país y plan, más publicidad en el plan con anuncios. Los ingresos distintos de las cuotas no fueron materiales en 2025 ([10-K 2025](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm)).
- **Calidad económica y recurrencia.** El cobro es mensual y sin contrato. Los ingresos diferidos eran US$1.780 millones al 30 de septiembre de 2026. La recurrencia depende de que el contenido mantenga la retención, y la empresa ya no publica retención ni membresías.
- **Ventaja principal y amenaza principal.** La ventaja es la escala de audiencia, distribución y gasto en contenido. La amenaza es la competencia por la atención: en junio de 2026 YouTube concentró 13,5% del tiempo de televisión en Estados Unidos y Netflix 7,9% ([MediaPost sobre The Gauge de Nielsen, julio de 2026](https://www.mediapost.com/publications/article/417308/)).
- **Situación financiera y conversión a caja.** Al 30 de septiembre de 2026 había caja e inversiones por US$8.223 millones frente a notas por US$15.132 millones, más US$2.252 millones de pasivo por arrendamientos. El flujo libre LTM fue de US$11.375 millones (operativo de US$12.308 millones menos capex de US$933 millones) e incluye la comisión de terminación de WBD. La guía de flujo libre para 2026 es de ~US$12.000 millones ([carta del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm)).
- **Gestión y asignación de capital.** Dos directores generales (Ted Sarandos y Greg Peters) y recompras de US$12.861 millones en el LTM. El intento de compra de los estudios y del streaming de Warner Bros. Discovery (WBD) terminó en febrero de 2026 con el cobro de una comisión de US$2.800 millones. Quedan US$22.300 millones de autorización de recompra.
- **Las dos variables que más determinan la tesis.** El crecimiento del ingreso por miembro y de la publicidad frente al tiempo de visualización, y el ritmo de la amortización del contenido frente a los ingresos.
- **Principal evidencia contraria.** El tiempo de visualización creció 2% en el primer semestre de 2026. La meta de publicidad de 2026 se rebajó en la carta del 3T26. El precio de la acción al corte (US$69,58) está ~42% por debajo del de un año antes.
- **Señal que invalidaría la tesis central.** Dos trimestres consecutivos de crecimiento de ingresos por debajo de 9% a moneda constante con un margen operativo que no supere 31,5%. Indicarían que el aumento de precio ya no se traduce en apalancamiento operativo.

Las cuatro historias del Modelo JMR descansan en dos supuestos cualitativos:
1. Que Netflix conserva poder de fijación de precios en sus mercados maduros. Es el que mejor soporte tiene: las alzas de 2026 se comportaron como las anteriores, según la empresa.
2. Que la publicidad gana peso en los ingresos sin diluir el margen. Es el más frágil, porque la meta de 2026 ya se ajustó a la baja.

El valor se trata solo en la sección 12.

## 2. Modelo de negocio

| Producto o fuente de ingresos | Cliente que paga | Necesidad resuelta | Forma de cobro | Recurrencia | Principal driver | Riesgo económico |
|---|---|---|---|---|---|---|
| Suscripción de streaming sin anuncios (planes estándar y premium) | Hogares y personas en numerosos países | Entretenimiento bajo demanda, local y global | Cuota mensual en moneda local, equivalente a US$1-US$37 por plan y país ([10-K 2025](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm)) | Alta pero sin contrato; cancelable cada mes | Número de miembros y precio por membresía | Rotación si el contenido pierde atractivo; sensibilidad al precio |
| Plan con anuncios | Hogares sensibles al precio | Acceso a menor costo | Cuota menor más publicidad cobrada a anunciantes | Mensual | Miembros del plan y ventas de publicidad por usuario | Tecnología publicitaria propia reciente y monetización por probar |
| Miembros adicionales (cuentas extra) | Titulares que comparten fuera del hogar | Compartir la cuenta con otro hogar | Cargo mensual extra, de US$2 a US$9 equivalentes ([10-K 2025](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm)) | Mensual | Cumplimiento de las reglas de uso | Madurez: el efecto de la medida ya se absorbió en 2023-2024 |
| Publicidad | Anunciantes | Audiencia atenta con medición | Venta directa y programática; compromisos anticipados («upfront») | Por campaña | Audiencia del plan con anuncios y precio por impresión | Ejecución del producto publicitario y competencia de plataformas abiertas |
| Productos de consumo, experiencias en vivo y otros | Consumidores | Extensión de las franquicias | Venta de producto y entradas | Puntual | Franquicias de éxito | Dependencia de pocos títulos; no material en 2025 |

La propuesta de valor es un servicio que reúne, a un precio mensual bajo, una oferta de series, películas, eventos en vivo y juegos que el cliente contrata para llenar su tiempo de ocio sin pagar por título. La empresa define su estrategia como invertir en entretenimiento original, diferenciado y exclusivo, complementado con contenido de terceros y una experiencia de descubrimiento personalizada ([Netflix, carta a accionistas del 3T26, 20 de octubre de 2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm)). La formación de ingresos combina volumen (miembros), precio (cuota por plan y por país, ajustada de vez en cuando) y mezcla (planes con y sin anuncios, regiones con distinto ingreso por membresía). En el 2T26 los ingresos crecieron 13,4% por «crecimiento de membresías, precios y publicidad», con un efecto cambiario favorable de ~1 punto, y en el 3T26 crecieron 11,8% ([carta del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm)); la compañía no publica ya el número de membresías ni el ingreso medio por membresía ([10-K 2025](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm); [carta del 2T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000211/ex991_q226.htm)).

La duración contractual es de un mes, lo que obliga a ganar cada renovación y explica por qué la empresa insiste en que la retención es «de la mejor de la industria» sin publicar la cifra; no se divulga una tasa de cancelación, por lo que se aplica la regla de insuficiencia: **“Información insuficiente en las fuentes disponibles para evaluar esto con confianza.”** La visibilidad la dan los ingresos diferidos (US$1.776 millones al 31 de diciembre de 2025 y US$1.780 millones al 30 de septiembre de 2026, equivalentes a menos de dos semanas de ingresos) y la guía trimestral, que la dirección describe como su pronóstico interno real. El poder de fijación de precios tiene evidencia directa: en el primer semestre de 2026 hubo alzas en Estados Unidos, México y España y la empresa informa que su efecto fue «consistente con alzas anteriores y con nuestras expectativas»; el efecto de la elasticidad no se cuantifica en los documentos revisados.

La estructura de costos está dominada por el contenido. En 2025 el costo de ingresos fue 52% de los ingresos (54% en 2024 y 58% en 2023) e incluye US$16.422 millones de amortización de contenido; ese año subieron US$1.121 millones por amortización y US$1.116 millones por otros costos de ingresos, estos últimos principalmente por impuestos no sobre la renta en Brasil, de los cuales US$619 millones se reconocieron en el 3T25 como cargo acumulado ([10-K 2025](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm), notas 9 y MD&A). Ventas y marketing fue US$3.301 millones (7% de los ingresos), tecnología y desarrollo US$3.391 millones (8%) y administración US$1.888 millones (4%). El gasto de contenido en efectivo es ~1,1 veces la amortización, de modo que la reinversión neta en contenido es pequeña en relación con el flujo. La economía por unidad (costo de adquisición de clientes, margen de contribución por miembro) no se publica.

Netflix depende de terceros en cuatro frentes: tiendas de aplicaciones y fabricantes de dispositivos para llegar al televisor, procesadores de pago, proveedores de contenido (estudios y ligas deportivas, por ejemplo la NFL, con una agenda ampliada anunciada en 2026) y su propia red de entrega, Open Connect, que reduce el costo de transmisión pero exige inversión. El poder de los proveedores crece con el deporte en vivo: la dirección estima que la programación en vivo será algo más de 5% del gasto de contenido de 2026 y solo ~1% de las horas vistas, aunque seis de los diez mejores días de altas de miembros de los últimos cinco años coincidieron con eventos en vivo ([carta del 2T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000211/ex991_q226.htm)).

## 3. Segmentos y geografía

Netflix opera un solo segmento operativo. Los dos directores generales, que son el máximo responsable de decisiones operativas, revisan la información de forma consolidada y asignan presupuesto con base en el margen operativo y la utilidad neta ([Netflix, 10-K 2025, 23 de enero de 2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm), nota de segmentos). Por eso el desglose publicado es regional, no por línea de negocio, y no hay beneficio por región.

La tabla usa los ingresos por región del 10-K y los LTM a septiembre de 2026, calculados como el ejercicio 2025 más los nueve meses de 2026 menos los nueve meses de 2025 ([10-Q del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm)).

| Segmento o unidad | Ingresos | Crecimiento | Margen o contribución | Peso aproximado | Tendencia | Fuente |
|---|---:|---:|---|---:|---|---|
| UCAN (Estados Unidos y Canadá) | US$19.957 M en 2025; US$21.644 M LTM | +15% en 2025; +11% en el 3T26 (igual a moneda constante) | No se publica | 43,5% | Desacelera desde 18% (4T25) por base alta; las alzas de precio de 2026 sostienen el +11% | [10-K 2025](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm); [carta del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm) |
| EMEA (Europa, Medio Oriente y África) | US$14.515 M en 2025; US$16.011 M LTM | +17% en 2025; +11% en el 3T26 (+9% a moneda constante) | No se publica | 32,2% | Desaceleración gradual con ayuda cambiaria | Ídem |
| LATAM (América Latina) | US$5.358 M en 2025; US$6.102 M LTM | +11% reportado y +23% a moneda constante en 2025; +17% en el 3T26 (+12%) | No se publica | 12,3% | Alto crecimiento local, con efecto cambiario volátil e impuestos no sobre la renta en Brasil | Ídem |
| APAC (Asia-Pacífico) | US$5.354 M en 2025; US$5.977 M LTM | +21% en 2025; +12% en el 3T26 (+15% a moneda constante) | No se publica | 12,0% | Región de mayor crecimiento a moneda constante, con India como caso destacado | Ídem |
| Total | US$45.183 M en 2025; US$49.735 M LTM | +15,9% en 2025; +13,7% en los 9M2026; +11,8% en el 3T26 | Margen operativo de 29,5% en 2025, 31,3% LTM y 34,6% en el 3T26 | 100% | Guía de 2026 de US$51.100 M (+13%) | Ídem |

La mezcla por moneda muestra una exposición cambiaria considerable. Las monedas distintas del dólar representaron 56% de los ingresos y 31% de los gastos operativos de 2025, así que una apreciación del dólar reduce el crecimiento reportado más de lo que reduce los costos. La compañía cubre parte de la exposición con contratos a plazo: en 2025 el resultado de coberturas incluido en ingresos fue una pérdida de US$91 millones, frente a una ganancia de US$124 millones en 2024.

En LATAM la diferencia entre crecimiento reportado y a moneda constante fue de 12 puntos en 2025 (en contra) y de 5 puntos en el 3T26 (a favor). Es la región con más riesgo de conversión. En EMEA y APAC la diferencia fue de un punto o menos en 2025 ([10-K 2025](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm); [carta del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm)).

No existe concentración de clientes relevante, porque el cliente es el consumidor final y el cobro es mensual. La concentración está del lado de los proveedores:
- Los estudios que licencian catálogo, cuya disposición a vender a un competidor cambia con su propia estrategia de streaming. En el 3T26 Netflix firmó una nueva licencia con Disney.
- Las ligas deportivas.
- Los fabricantes de dispositivos.

Los cambios de reporte rompen la comparabilidad en tres puntos:
1. Netflix dejó de reportar membresías y el ingreso medio por membresía durante 2025.
2. Publicará su informe de horas vistas una vez al año desde 2027.
3. En marzo de 2026 cerró una adquisición por unos US$587 millones en efectivo, cuyo aporte a ingresos no se separa ([10-Q del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm)).

La compra de WBD no se concretó y por tanto no altera el perímetro.

UCAN explica la mayor parte del valor económico: es 43,5% de los ingresos y la región con el precio por miembro más alto. Su desaceleración (+11% en el 3T26) es la variable que más pesa en la tasa de crecimiento del grupo. El mayor riesgo está repartido: en LATAM por tipo de cambio e impuestos locales (la carga de Brasil de 2025 muestra que el riesgo fiscal indirecto es real) y en UCAN por saturación. Netflix no publica beneficios por segmento y este análisis no los estima, porque no existe una metodología verificable para asignar costos de contenido a regiones.

## 4. Industria y crecimiento

El mercado económico de Netflix es el tiempo de entretenimiento en video de los hogares y el gasto que lo acompaña, que combina suscripciones, publicidad y, en menor medida, compra o alquiler de títulos. Se puede dividir en televisión lineal, streaming de suscripción y publicidad (con o sin pago), video generado por usuarios (YouTube, video corto) y juegos. La señal observable más útil es la participación en el tiempo de televisión: en junio de 2026 el streaming llegó a 48,5% del tiempo total de televisión en Estados Unidos, YouTube a 13,5%, Prime Video a 4,2%, el canal Roku a 3,0% y Netflix cayó a 7,9% desde 8,3% el mes anterior ([MediaPost sobre The Gauge de Nielsen, julio de 2026](https://www.mediapost.com/publications/article/417308/)). La misma fuente advierte que esa edición es la última con la metodología anterior, por lo que no se debe comparar mecánicamente con ediciones posteriores. En Polonia, el último dato disponible de agosto de 2026 es de 1,9% para Netflix y 2,8% para YouTube ([Nielsen, The Gauge Polonia, agosto de 2026](https://www.nielsen.com/news-center/2026/the-gauge-poland-august-2026/)).

El tamaño del mercado no se toma de un TAM promocional. Lo que se puede observar es el gasto: Netflix ingresó US$45.183 millones en 2025 (US$49.735 millones en el LTM a septiembre de 2026) y la dirección dijo en el 1S26 que su audiencia se acerca a los mil millones de personas; no hay en los documentos revisados una cifra confiable del mercado servible total. La penetración es alta en Estados Unidos, donde el crecimiento del 3T26 (+11%, igual a moneda constante) lo explican precio y publicidad más que miembros nuevos, y baja en los mercados con menor ingreso por hogar, donde los precios locales son más bajos. El 1S26 muestra 97.000 millones de horas vistas (+2%), apenas por encima del +1,5% de 2025, lo que indica que el espacio de crecimiento está más en monetizar mejor cada hora que en ganar horas.

El ciclo de la industria combina un componente macroeconómico y uno de producto. La suscripción es un gasto discrecional pequeño pero cancelable cada mes; la publicidad responde al ciclo de marketing. El año 2022, con ingresos +6,5% y margen operativo de 17,8%, muestra que una combinación de saturación en Norteamérica, competencia y cuentas compartidas puede frenar al grupo; la recuperación de 2023 en adelante la explican el cobro por cuentas compartidas, el plan con anuncios y alzas de precio. Los impulsores estructurales son la migración de la televisión lineal al streaming, la publicidad conectada, el deporte en vivo como contenido de adquisición, el contenido local exportable (más de un tercio del tiempo visto es no inglés) y las herramientas de inteligencia artificial generativa que, según la empresa, ya intervienen en unos 300 títulos de 2026 con menor costo y mayor velocidad ([Netflix, carta a accionistas del 2T26, 16 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000211/ex991_q226.htm)).

Los límites son cuatro: la competencia por la atención (plataformas abiertas, video corto, juegos), la inflación del costo del contenido y de los derechos deportivos, la regulación fiscal y de contenido local en cada país (el cargo de Brasil de 2025 es el ejemplo) y el retorno decreciente de captar miembros adicionales en mercados ya penetrados. En posición relativa, Netflix tiene la mayor escala de gasto en contenido de pago y la mayor audiencia de pago, pero comparte el tiempo de televisión con una plataforma gratuita, YouTube, que tiene casi el doble de su participación, y su ganancia de participación en los últimos meses no está demostrada: la cifra de junio de 2026 es una caída de 0,4 puntos mensual.

### Las 5 fuerzas de Porter

| Fuerza | Intensidad: baja/media/alta | Evidencia | Evolución esperada | Implicación para retornos |
|---|---|---|---|---|
| Poder de proveedores | Media-alta | Los estudios y ligas venden derechos escasos; el costo de ingresos subió US$2.237 millones en 2025, US$1.121 millones por amortización de contenido; el deporte en vivo es ~5% del gasto de contenido y ~1% de las horas ([carta del 2T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000211/ex991_q226.htm)) | Estable a creciente por la competencia de plataformas por derechos deportivos | Presiona el margen si el contenido crece más que los ingresos |
| Poder de compradores | Baja-media | El consumidor cancela cada mes y compara con alternativas gratuitas, pero ninguno pesa individualmente; las alzas de 2026 se absorbieron según la empresa | Estable; el precio sigue siendo la palanca principal | La elasticidad del precio fija el techo del crecimiento de UCAN |
| Amenaza de nuevos entrantes | Baja | Replicar la escala de gasto de ~US$20.000 millones anuales en contenido (US$19.991 millones de adiciones en el LTM) y una red global de entrega exige capital y años; los entrantes son grandes grupos ya establecidos | Estable | Protege los retornos de capital |
| Amenaza de sustitutos | Alta | YouTube concentra 13,5% del tiempo de televisión en Estados Unidos frente a 7,9% de Netflix; el video corto y los juegos compiten por la misma atención ([MediaPost/Nielsen](https://www.mediapost.com/publications/article/417308/)) | Creciente | Es la fuerza con más probabilidad de erosionar el margen y el poder de precios |
| Rivalidad existente | Alta | Disney, Amazon, Paramount Skydance y otros compiten por contenido y suscriptores; la compra de WBD por Paramount Skydance (que desplazó a Netflix en febrero de 2026) consolida a un competidor ([Netflix, 10-Q del 2T26, nota 6](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000212/nflx-20260630.htm)) | Estable a creciente con consolidación | Limita el aumento de precios y encarece los derechos |

La fuerza con más probabilidad de deteriorar la economía del negocio es la amenaza de sustitutos, porque los sustitutos no compiten en precio sino en costo cero de producción y en tiempo de atención; la que mejor protege los retornos es la baja amenaza de nuevos entrantes, que descansa en una escala de gasto en contenido que pocos grupos pueden financiar.

## 5. Calidad del negocio

La calidad histórica de Netflix es alta y mejora, y la sostenibilidad futura depende de si el contenido sigue convirtiendo gasto en ingresos con el mismo apalancamiento que entre 2022 y 2025. Esta sección separa ambas cosas. El análisis usa diez cierres anuales (2016-2025) más los últimos doce meses (LTM) a septiembre de 2026, calculados como el ejercicio 2025 más los nueve meses de 2026 menos los nueve meses de 2025 ([Netflix, 10-K 2025, 23 de enero de 2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm); [10-Q del 3T26, 21 de octubre de 2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm); [10-Q del 3T25](https://www.sec.gov/Archives/edgar/data/1065280/000106528025000406/nflx-20250930.htm)). Todas las cifras salen del snapshot SEC conciliado de la revisión `NFLX-2026-10-25` (28/28 identidades contables y 20/20 derivaciones verificadas contra las instancias XBRL) y del Nivel 2. Las acciones y el beneficio por acción de 2016-2024 se ajustaron por el desdoblamiento de diez por uno del 14 de noviembre de 2025.

### Análisis financiero histórico

#### Estado de resultados

Los ingresos pasaron de US$8.831 millones en 2016 a US$45.183 millones en 2025, un crecimiento anual compuesto de 19,9% en nueve intervalos y de 12,6% en los cinco últimos (2020-2025). La trayectoria no es lineal: 32% en 2017, 35% en 2018, 6,5% en 2022 y 6,7% en 2023, cuando la saturación en Norteamérica, la competencia y las cuentas compartidas frenaron al grupo, y 15,7% y 15,9% en 2024 y 2025 tras el cobro por cuentas compartidas, el plan con anuncios y las alzas de precio. En los nueve meses de 2026 el crecimiento fue de 13,7% (US$37.684 millones frente a US$33.132 millones) y el 3T26 aportó +11,8%; el LTM a septiembre suma US$49.735 millones. La volatilidad del crecimiento es alta, pero el punto de inflexión de 2022 muestra que el negocio ya probó que podía desacelerar a un dígito sin perder rentabilidad.

El margen bruto subió de 29,1% en 2016 a 48,5% en 2025 y 50,7% en el LTM, porque la amortización de contenido (US$16.422 millones en 2025 y US$17.529 millones en el LTM) creció 7% en 2025 mientras los ingresos crecieron 16%. El margen operativo pasó de 4,3% a 29,5% (17,8% en 2022, 20,6% en 2023, 26,7% en 2024) y el LTM es 31,3% GAAP; el cargo único de US$619 millones por impuestos no sobre la renta de Brasil del 3T25 ya quedó fuera de la ventana LTM, de modo que el margen LTM no necesita normalizarse por ese concepto ([10-K 2025](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm), nota 9). Como porcentaje de los ingresos LTM, el costo de ingresos fue 49,3% (51,5% en 2025 y 58% en 2023), ventas y marketing 7,3%, tecnología y desarrollo 7,8% y administración 4,3%. La compañía reporta bajo principios contables de Estados Unidos (GAAP) y solo usa medidas no GAAP para el flujo libre y los ingresos a moneda constante. Los elementos no recurrentes materiales de la ventana LTM son ~US$100 millones de honorarios y costos asociados a la compra fallida de WBD en el 1T26 (dentro del EBIT) y, por debajo del resultado operativo, la comisión de terminación de WBD de US$2.800 millones, registrada en otros ingresos. Esa comisión explica que la utilidad neta LTM (US$14.767 millones, 29,7% de los ingresos) sea mucho mayor que la de 2025 (US$10.981 millones, 24,3%). El beneficio por acción diluido pasó de US$1,20 en 2023 a US$1,98 en 2024, US$2,53 en 2025 y US$3,46 en el LTM, con acciones diluidas promedio que bajaron de 4.495 millones en 2023 a 4.268 millones en el LTM (−5,0%).

#### Balance

La liquidez es suficiente pero no ociosa: caja e inversiones de US$8.223 millones y un indicador de liquidez corriente de 1,07 al 30 de septiembre de 2026 (activos corrientes US$13.222 millones frente a pasivos corrientes US$12.301 millones, de los cuales US$2.475 millones son deuda de corto plazo y el resto principalmente pasivos de contenido, cuentas por pagar y gastos acumulados). La deuda son notas senior no garantizadas por US$15.132 millones en libros (US$2.475 millones corrientes y US$12.658 millones no corrientes), con cupones de 3,625% a 6,375%; los US$1.000 millones al 4,375% que vencen en noviembre de 2026 quedaron cubiertos por la emisión de US$1.000 millones al 5,250% a 2036 del 22 de julio de 2026 ([Netflix, 8-K del 22 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1065280/000119312526312575/d171951d8k.htm); [10-Q del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm), nota de deuda). La deuda neta equivale a 0,43 veces el EBITDA LTM (0,40 en 2025) y el EBIT cubre 18,2 veces el gasto por intereses LTM de US$857 millones; hay además una línea rotatoria de US$3.000 millones sin utilizar hasta abril de 2029.

El activo principal son los activos de contenido: US$34.605 millones netos al 30 de septiembre de 2026, 59% del activo total de US$58.682 millones, que se amortizan de forma acelerada (más de 90% de cada título en cuatro años) y por eso exigen reposición constante. Esta revisión corrigió un error de extracción de la anterior: desde 2024 la etiqueta XBRL genérica de intangibles netos coincide con el saldo de contenido, y tratarla como intangible genérico duplicaba el activo; el contenido se registra una sola vez ([docs/NFLX_CIERRE_SEC_2026-10-25.md](../docs/NFLX_CIERRE_SEC_2026-10-25.md)). Los compromisos de contenido eran de US$24.039 millones al cierre de 2025, de los cuales US$18.400 millones no están en el balance, y la dirección estima obligaciones por títulos futuros desconocidos de US$1.000 a US$4.000 millones en tres años ([10-K 2025](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm)). No hay plusvalía ni intangibles significativos distintos del contenido (adjudicado como «no aplica» con evidencia por periodo). El patrimonio (US$29.286 millones) refleja recompras acumuladas y no una pérdida acumulada: las utilidades retenidas son US$54.630 millones, así que no hay señal de insolvencia. Los ingresos diferidos son pequeños (US$1.780 millones) porque la facturación es mensual. Fuera de la deuda financiera están el pasivo por arrendamientos operativos de US$2.252 millones (que el Modelo JMR suma a la deuda: US$17.385 millones en total), depósitos por impuestos no sobre la renta en Brasil y beneficios fiscales no reconocidos de US$566 millones al cierre de 2025. Las pérdidas fiscales trasladables son inmateriales (0,06% del valor operativo) y se adjudicaron como omisión inmaterial, sin usar cero como dato.

#### Flujo de caja

La conversión de utilidad en caja pasó de negativa a alta. Entre 2016 y 2019 el flujo operativo fue negativo (hasta −US$2.887 millones en 2019) porque el gasto de contenido en efectivo superaba la amortización en una fase de crecimiento a crédito; desde 2020 es positivo y en 2025 fue de US$10.149 millones, 92% de la utilidad neta, con un flujo libre de US$9.461 millones (20,9% de los ingresos) tras un capex de US$688 millones (1,5% de los ingresos), todo de bajo mantenimiento porque el negocio no tiene plantas. El LTM a septiembre trae un flujo operativo de US$12.308 millones y un flujo libre de US$11.375 millones (22,9% de los ingresos) tras un capex que subió a US$933 millones (1,9%); ambos incluyen la comisión de WBD cobrada en el 1T26. Las adiciones a contenido fueron 1,04 veces la amortización en 2025 y 1,14 veces en el LTM (US$19.991 frente a US$17.529 millones), en línea con la guía de ~1,1 veces para 2026. La guía de flujo libre de 2026 bajó de ~US$12.500 millones (carta del 2T26) a ~US$12.000 millones en la [carta del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm).

La compensación basada en acciones fue de US$368 millones en 2025 (0,8% de los ingresos) y US$540 millones en el LTM (1,1%); es baja en relación con empresas comparables porque los empleados eligen entre efectivo y opciones, pero es un costo económico y sube con el precio. En asignación de capital, Netflix recompró US$9.127 millones en 2025 y US$10.782 millones en los nueve meses de 2026, de ellos US$4.800 millones en el 3T26 (63,9 millones de acciones, ~US$75 por acción). Las acciones en circulación bajaron de 4.222 a 4.106 millones entre el cierre de 2025 y el 30 de septiembre de 2026 (−2,7%), porque la emisión por ejercicio de opciones (US$184 millones en nueve meses) compensa solo una parte pequeña de la recompra bruta. Las adquisiciones de negocios fueron de US$603 millones en el LTM, casi todo la compra de marzo de 2026 (~US$587 millones). La sostenibilidad de la generación de caja depende de que el cociente entre gasto de contenido y amortización se mantenga cerca de 1,1 y de que los ingresos crezcan más que el costo del contenido.

#### Ratios y retornos

Las definiciones son las del Nivel 2 de esta revisión, que cambian dos cosas frente a la versión del 21-oct: el ROIC usa la tasa efectiva de cada año (no una tasa fija) y el capital invertido incluye los arrendamientos operativos desde 2019. Crecimiento de ingresos anual; márgenes sobre ingresos; margen de flujo libre = (flujo operativo − capex) / ingresos; ROE = utilidad neta / patrimonio contable final; ROIC = EBIT × (1 − tasa efectiva) / (patrimonio + deuda financiera + arrendamientos − caja) final. Los promedios son simples de los ratios anuales (el de diez años usa 2016-2025; el crecimiento de diez años incluye 2016 frente a 2015) y excluyen el LTM.

| Métrica | LTM o último año | Promedio 3 años | Promedio 5 años | Promedio 10 años | Dirección | Calidad de la definición |
|---|---:|---:|---:|---:|---|---|
| Crecimiento de ingresos | 15,9% (2025); +13,7% en 9M26 | 12,7% | 12,7% | 21,3% | Estable en dos dígitos tras el mínimo de 2022 | Alta: ingresos reportados |
| Margen bruto | 50,7% | 45,4% | 43,4% | 39,2% | Sube | Alta |
| Margen operativo | 31,3% | 25,6% | 23,1% | 16,8% | Sube | Alta; el LTM ya no contiene el cargo de Brasil |
| Margen neto | 24,3% (2025); 29,7% LTM con comisión de WBD | 20,9% | 18,8% | 12,9% | Sube | Media: LTM distorsionado |
| Margen de flujo libre | 20,9% (2025); 22,9% LTM | 19,7% | 12,8% | 0,3% | Sube | Media: LTM con comisión de WBD |
| ROA | 19,8% (2025); 25,2% LTM | n.d. | n.d. | n.d. | Sube | Utilidad neta / activo total final |
| ROE | 41,3% (2025); 50,4% LTM | 34,2% | 31,3% | 25,2% | Sube | Media: recompras reducen el patrimonio y la comisión infla el LTM |
| ROIC | 33,3% (2025); 33,8% LTM | 26,9% | 23,1% | 17,9% | Sube | Media: sin capitalizar contenido ni I+D; con I+D capitalizado la hoja da 30,1% |
| Rotación del capital invertido (ingresos / capital invertido) | 1,31 veces (2025); 1,29 LTM | 1,20 | 1,13 | 1,29 | Estable | Media |
| Liquidez corriente | 1,07 | 1,17 | 1,13 | 1,19 | Baja ligeramente | Alta |
| Prueba ácida | n.d. | n.d. | n.d. | n.d. | n.d. | Netflix no separa cuentas por cobrar en el balance (van en «otros activos corrientes»); no se estima |
| Deuda neta / EBITDA | 0,43 veces | 0,66 | 0,96 | 2,18 | Baja | Alta; sin arrendamientos |
| Cobertura de intereses (EBIT / gasto por intereses) | 18,2 veces | 13,9 | 11,5 | 7,8 | Sube | Alta |

### Evaluación cualitativa de la calidad

La recurrencia es de renovación mensual, no contractual: la evidencia de retención es indirecta (crecimiento de ingresos por encima de 11% con aumentos de precio) y la empresa no publica churn desde que dejó de reportar membresías. El poder de precios está respaldado por las alzas de 2026 en Estados Unidos, México y España, que según la carta del 3T26 se comportaron como las anteriores, pero la elasticidad no se cuantifica. La intensidad de capital es baja en activos fijos (capex 1,9% de los ingresos LTM) y alta en contenido (las adiciones de contenido equivalen a 40% de los ingresos LTM). El retorno incremental sobre el capital ha sido alto: entre 2022 y el LTM los ingresos subieron US$18.119 millones con US$6.821 millones de capital invertido adicional (2,66 veces) y el EBIT pasó de US$5.633 a US$15.565 millones. La resiliencia es mixta: el negocio mantuvo márgenes en 2022, pero ese año el crecimiento llegó a 6,5%. Hay dependencia mínima de adquisiciones. La capacidad de reinversión está limitada por la disciplina de gasto de contenido más que por la caja. La probabilidad de que márgenes y retornos históricos persistan es razonable para el margen bruto y operativo en el horizonte de 2026-2027, y menos segura para un ROIC de 30-34%, que se compara con una industria con un ROIC publicado de 11,04% (Damodaran, Entertainment global, enero de 2026).

### Auditoría de cifras y supuestos del Modelo JMR

El archivo examinado es [la hoja de la revisión NFLX-2026-10-25](https://docs.google.com/spreadsheets/d/1ZPNMHxc7m3Iv60mdGspgi6-cc2zwf5kZ4ocsuANQUNM/edit) (copia nueva de la plantilla IA del 25-oct-2026; la plantilla oficial no se modificó), construida con estados de la SEC al 30 de septiembre de 2026 y precio al 30 de septiembre de 2026. La importación escribió 785 celdas postverificadas una a una desde el snapshot conciliado, y las entradas del analista se aplicaron con respaldo, selector validado y etiqueta [Dato]/[Cálculo]/[Juicio] por celda. Los candados de la plantilla están en LISTO/VALIDADO. Los hallazgos que más pesan en el valor son tres: el ROIC terminal (20,58%, decisión explícita del usuario frente al 11,04% de la industria; con ROIC terminal igual al costo de capital el DCF Base sería US$56,13, −20,8%), el margen objetivo de las historias y el ventas/capital de 1,3 en los años 1-5. La auditoría independiente de esta misma revisión está en `data/NFLX_Auditoria_Valoracion_2026-10-25.md`.

| Dato o supuesto | Valor del modelo y unidad | Tipo de origen y actividad | Fuente, fecha, hoja y celda | Resultado del contraste | Prioridad e incidencia cualitativa |
|---|---|---|---|---|---|
| Ingresos LTM | US$49.734,63 M | Dato reportado derivado; activo | 10-K 2025 y 10-Q del 3T26; 'Input sheet'!B12 | Conciliado: 45.183,04 + 37.683,87 − 33.132,27 | Baja |
| EBIT GAAP LTM | US$15.564,87 M (31,30%) | Dato reportado; activo | 'Input sheet'!B13 | Conciliado con la SEC; sin ajustes manuales | Baja |
| Margen base ajustado | 33,09% | Cálculo derivado (GAAP + I+D capitalizado); activo | 'Valuation output' | Conciliado: 31,30% + 1,80 pp de I+D (EBIT +US$893,33 M) | Media |
| I+D capitalizado | Vida de 3 años; activo de I+D US$7.126,84 M | Ajuste de Damodaran; activo | 'R& D converter' | Conciliado: «Technology and development» con la etiqueta propia de Netflix, que deja en cero el residuo de la cuenta de resultados | Media |
| Arrendamientos operativos | US$2.252,24 M sumados a la deuda (B18 = No: no se reconvierten) | Dato reportado (ASC 842); activo | 'Input sheet'!B15, B18 | Conciliado; el ajuste del EBIT por el componente financiero del arrendamiento no se hace (limitación pequeña) | Baja |
| Crecimiento de las historias | Base 12% el año 1 y 9,99% compuesto en cinco años | Juicio del analista; activo | Ficha de historias; 'Escenarios e historias' | Documentado en la sección 12 | Alta |
| Margen objetivo de las historias | Base 36% · Conservadora 32% · Optimista 40% · Disrupción 22% (GAAP; el modelo usa 37,1% / 32,7% / 41,3% / 22% en base ajustada) | Juicio del analista; activo | Ficha de historias; 'Input sheet' | Requiere seguimiento: la Base supera al comparable maduro y se apoya en la publicidad; el 3T26 ya llegó a 34,6% | Alta |
| Tasa efectiva / marginal | 16,57% / 25% | Dato reportado / entrada manual; activos | 'Input sheet'!B24/B25 | Conciliado (efectiva LTM); marginal federal + estatal | Baja |
| Ventas/capital | 1,3 años 1-5 · 0,9 años 6-10 | Juicio dentro del rango empresa (1,29 LTM) / marginal (2,66 sin I+D) | 'Input sheet' | Corregido en esta revisión desde 1,6 para evitar un rendimiento marginal de ~49% con caída abrupta; ahora ≈38% → ≈26% → 20,58% | Alta |
| Costo de capital inicial / patrimonio | 10,02% / 10,34% | Cálculo derivado con insumos de Damodaran; activo | 'Cost of capital worksheet'; 'Input sheet'!B84 = VALIDADO | Conciliado: beta global reapalancada 1,03, prima ponderada por regiones 4,93%, tasa libre 5,29% al 30-sep-2026, rating A | Media |
| Costo de capital terminal | 8,99% | Regla (tasa libre + prima madura de 3,70%); activo | 'Valuation output' | Conciliado | Media |
| Crecimiento terminal | 4,0% (Disrupción 0%) | Regla del modelo: 4% nominal con techo en la tasa libre; activo | 'Valuation output'; corte vigente | Conciliado | Media |
| ROIC terminal | 20,58% (Base, Conservadora, Optimista); costo de capital (8,99%) en Disrupción | Decisión del usuario (21-oct-2026): punto medio entre el ROIC actual de la hoja (30,13%) y Entertainment (11,04%); activo | 'Input sheet'; moat_2026-09-30.json | Documentado; con ROIC terminal = costo de capital el DCF Base sería US$56,13 (−20,8%) | Alta |
| Acciones y opciones | 4.106,33 M en circulación; 120,18 M de opciones a US$41,24 (4,04 años, volatilidad 33,8%), valoradas en US$4.526,75 M | Dato reportado y Black-Scholes; activo | 'Input sheet'; 'Option value' | Conciliado; las RSU (1,87 M) no se valoran (inmaterial) | Baja |
| Deuda y caja | Deuda US$17.384,63 M (notas + arrendamientos); caja e inversiones US$8.222,95 M | Dato reportado; activo | 'Input sheet'!B16, B19 | Conciliado con el 10-Q del 3T26 | Baja |
| Probabilidades | 45% / 22,5% / 22,5% / 10% (Base / Conservadora / Optimista / Disrupción) | Regla: previa de la etapa «crecimiento maduro», sin ajustes por indicadores; activo | Ficha de historias; 'Escenarios e historias' | Conciliado con la regla | Media |
| Margen de seguridad | 35% sobre el DCF Base | Regla de la cartera; activo | 'Resumen de Valoración' | Sin fuente externa | Baja |
| Múltiplos de salida | Ver tabla de resultados | Regla por ciclo con ajuste por tasas y techo en el múltiplo justificado; secundarios | Hojas de múltiplos | Conciliado: ninguno supera su ancla C | Media |

| Supuesto activo y escenario | Historia empresarial que presupone | Evidencia favorable | Evidencia contraria | Justificación documentada o faltante | Qué debe comprobarse |
|---|---|---|---|---|---|
| Crecimiento de 9,99% anual compuesto, Base | Precio, publicidad y mercados nuevos compensan un uso casi plano | +13,7% en 9M26; alzas de 2026 absorbidas | Horas vistas +2%; desaceleración a +11,8% en el 3T26 y guía del 4T26 de US$13.400 M | Documentada en la sección 12 | Crecimiento ≥ 11% en 2027 y publicidad ≥ US$4.500 M |
| Margen GAAP de 36% en cinco años, Base | La amortización de contenido crece menos que los ingresos y la publicidad escala | 17,8% → 31,3% LTM y 34,6% en el 3T26 | El contenido en vivo es caro; guía del 4T26 de 26,0% | Documentada | Margen ≥ 34% en 2027 |
| ROIC terminal de 20,58% | La escala de audiencia y de gasto en contenido sostiene retornos sobre la industria | ROIC de 27-34% desde 2024 | La atención migra a plataformas abiertas | Decisión explícita del usuario | Participación de Netflix en el tiempo de televisión |
| Disrupción: margen de 22% y crecimiento cero desde el año 5 | Pérdida de poder de precios y estabilización sin recuperación | Competencia de YouTube y de la IA generativa | El negocio no muestra hoy ese deterioro | Documentada | Ingresos ≤ +3% dos trimestres |
| Múltiplos por ciclo | El mercado paga lo que justifican los fundamentales de cada historia | Historia propia y múltiplo justificado | Tasa libre de 5,29% frente a 1-4% en los años de múltiplos altos | Documentada (ajuste por tasas) | Múltiplo actual |

| Resultado declarado por el Modelo JMR (precio relativo, Base) | Múltiplo Conservadora (×) | Múltiplo Base (×) | Múltiplo Optimista (×) | Precio FY+3 Base | Valor hoy Base |
|---|---:|---:|---:|---:|---:|
| EV/EBITDA | 13,03x | 15,06x | 17,51x | US$83,93 | US$60,37 |
| EV/FCFF | 19,98x | 24,11x | 27,89x | US$83,97 | US$57,51 |
| P/E | 16,07x | 18,86x | 21,38x | US$83,18 | US$60,06 |
| P/FCFE | 17,44x | 20,53x | 23,23x | US$78,29 | US$57,39 |
| P/OCF | 18,31x | 22,35x | 25,71x | US$78,29 | US$54,04 |
| P/S (peso 0) | 4,12x | 5,22x | 6,34x | — | US$61,93 |
| P/BV (peso 0) | 6,73x | 8,99x | 11,29x | — | US$61,71 |
| EV/EBIT (complementario) | 13,35x | 15,41x | 17,89x | — | US$60,30 |
| P/FCF (complementario) | 19,42x | 23,67x | 27,13x | — | US$53,78 |
| Consolidado de múltiplos ponderados | n.a. | n.a. | n.a. | n.a. | US$58,09 |

Los valores de la tabla son resultados guardados del Modelo JMR al corte (horizonte FY+3 y valor presente con el costo del patrimonio de 10,34%), no una valoración propia. EV/EBIT y P/FCF no existen en la plantilla y se reproducen con su misma cadena de cálculo. Los múltiplos quedan por debajo de lo que implica el DCF porque el techo del múltiplo justificado y el ajuste por la tasa libre actual impiden aplicar los múltiplos de 2020-2025, pagados con tasas más bajas. La parte del modelo con mejor soporte son los datos de partida, los ajustes contables y el costo de capital; las más sensibles son el margen objetivo, el ROIC terminal y el crecimiento de la publicidad.

## 6. Ventaja competitiva

La pregunta es qué hace que un cliente prefiera Netflix a otra forma de gastar su tiempo, y cuánto dura esa preferencia. Se distingue entre ventajas con evidencia propia y atributos que parecen ventajas pero no lo son: el tamaño de la audiencia o un margen operativo de ~30% no demuestran por sí solos una barrera; solo lo hace una relación que se mantenga cuando un competidor intenta replicarla.

| Fuente de ventaja | Evidencia observable | Evidencia cuantitativa | Duración probable | Amenaza de erosión | Veredicto |
|---|---|---|---|---|---|
| Escala y ventaja de costos | La mayor audiencia de pago y el mayor gasto individual en contenido permiten repartir el costo de cada título entre más miembros | Adiciones a contenido de US$17.097 M en 2025 frente a ingresos de US$45.183 M; margen operativo de 17,8% a 29,5% en tres años y 31,3% en el LTM a septiembre de 2026 ([10-K 2025](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm)) | Larga, mientras el crecimiento supere el costo del contenido | Competidores consolidados (Paramount Skydance con WBD) con catálogos propios | Fuente real, de durabilidad media |
| Marca | Estatus de destino de entretenimiento global; títulos con cifras como Swapped, con 137 millones de vistas esperadas a 91 días | 19 años de streaming y una crisis superada en 2022 | Larga | La marca no impide la sustitución por contenido gratuito | Fuente real, pero débil frente a sustitutos |
| Costos de cambio | Perfiles, historial de visualización y recomendaciones personalizadas; el cambio de servicio es sin costo y mensual | Retención «industry-leading» según la empresa, sin cifra | Baja | La cancelación mensual y la proliferación de ofertas | Débil |
| Efectos de red | Limitados: el valor para un miembro no sube con otros miembros; sí lo hacen la escala de datos de recomendación y la audiencia que atrae anunciantes | Sin medición publicada | Media | Plataformas con efectos de red sociales (YouTube, video corto) | Débil, salvo en publicidad |
| Datos, ecosistema, distribución e integraciones | Red propia de entrega Open Connect; integraciones con dispositivos; suite de tecnología publicitaria propia con acceso programático | Audiencia que «se acerca a mil millones de personas» ([carta del 2T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000211/ex991_q226.htm)) | Media-larga | Los grandes grupos tecnológicos replican distribución y datos | Fuente real |
| Regulación, licencias o activos escasos | No hay licencias exclusivas; los derechos deportivos se compran por temporada | Deporte en vivo ~5% del gasto de contenido y ~1% de las horas | Baja | Competidores pueden pujar por los mismos derechos | No aplica como ventaja |

La evidencia contraria es nítida: el tiempo de visualización creció 2% en el primer semestre de 2026 y YouTube concentró 13,5% del tiempo de televisión en Estados Unidos en junio de 2026 frente a 7,9% de Netflix ([MediaPost sobre Nielsen, julio de 2026](https://www.mediapost.com/publications/article/417308/)), lo que sugiere que la ventaja no impide que la atención migre a la oferta gratuita. A favor, el ROIC después de impuestos se mantuvo en 15-34% desde 2022 (30,13% en la hoja con I+D capitalizado) con un costo de capital de 8-10%, y no se ve erosión visible en el retorno: lo que cae es la intensidad de uso, no el margen ni el retorno. La ventaja se fortalece en publicidad y escala de contenido local, permanece estable en marca y distribución y se erosiona, si algo, en costos de cambio. Veredicto: **ventaja durable**, con reserva: la fuente real es la escala combinada con el gasto en contenido, y esa escala solo es ventaja mientras los ingresos por miembro crezcan más que el costo del contenido.

La prueba de erosión que mejor separa una ventaja de un buen momento es el retorno incremental. Entre 2022 y el LTM a septiembre de 2026 Netflix sumó US$18.119 millones de ingresos con US$6.821 millones de capital invertido adicional (2,66 veces) y llevó el EBIT de US$5.633 millones a US$15.565 millones, un retorno marginal muy superior al costo de capital de 8%-10%; si la ventaja fuera solo escala pasajera, el costo de defenderla (contenido, deporte, publicidad) habría absorbido ese retorno. No lo hizo hasta ahora. Lo que sí queda sin demostrar es la parte que depende de la atención: mientras el tiempo de visualización crezca 2% anual, la ventaja se apoya en el precio por miembro y en la publicidad, dos palancas que un competidor con contenido gratuito puede acotar. Por eso el Modelo JMR no lleva el ROIC terminal al nivel actual de la hoja (30,13%), sino a 20,58%, el punto medio entre ese nivel y el promedio de la industria (11,04%), por decisión documentada del usuario del 21-oct-2026; reserva el costo de capital para la historia de Disrupción ([Aswath Damodaran, betas e industria, enero de 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)).

## 7. Competencia

| Competidor o sustituto | Área de solapamiento | Posición relativa | Ventaja principal | Debilidad principal | Señal a vigilar | Fuente |
|---|---|---|---|---|---|---|
| Disney (Disney+, Hulu, ESPN) | Series, películas, deporte y familias | Ingresos +6,8% y margen operativo de 19,3% frente al +13,7% (9M26) y 31,3% (LTM) de Netflix | Marcas y franquicias propias; deporte | Menor crecimiento y retorno; costos de transición desde el cable | Licencias de catálogo a Netflix y alzas de precio | [Yahoo Finance, DIS, 30-sep-2026](https://finance.yahoo.com/quote/DIS/) |
| Amazon Prime Video | Series, películas y deporte con Prime | 4,2% del tiempo de televisión en Estados Unidos (junio de 2026) | Se financia con el resto de Amazon | No depende solo del video, lo que reduce su disciplina de retorno | Derechos deportivos exclusivos y publicidad | [MediaPost/Nielsen](https://www.mediapost.com/publications/article/417308/) |
| Paramount Skydance con WBD (HBO Max, HBO) | Series premium, cine y estudios | WBD firmó un acuerdo con Paramount Skydance en febrero de 2026 tras terminar el suyo con Netflix | Catálogo y estudios consolidados | Deuda alta y integración compleja | Cierre de la integración y precios de HBO Max | [Netflix, 10-Q del 2T26, nota 6](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000212/nflx-20260630.htm) |
| YouTube (sustituto) | Atención en el televisor, video largo y podcasts | 13,5% del tiempo de televisión de EE.UU. (junio de 2026), casi el doble que Netflix | Contenido gratuito de creadores y publicidad masiva | Calidad y calendario irregulares | Su participación mensual en Nielsen | [MediaPost/Nielsen](https://www.mediapost.com/publications/article/417308/) |
| Spotify (audio y podcasts) | Atención y suscripciones de entretenimiento | Ingresos +13,9% y margen operativo de 13,7% | Hábito diario y base de pago | Margen menor y contenido licenciado | Video en su plataforma frente a los podcasts en video que Netflix incorporó con iHeartMedia | [Yahoo Finance, SPOT, 30-sep-2026](https://finance.yahoo.com/quote/SPOT/) |
| Roku y televisión conectada | Distribución y publicidad en la pantalla | 3,0% del tiempo de televisión (canal Roku) | Controla la interfaz del televisor | Ingresos que dependen de terceros | Cambios de acceso a la interfaz | [Yahoo Finance, ROKU, 30-sep-2026](https://finance.yahoo.com/quote/ROKU/) |

La competencia se produce por contenido y atención más que por precio: los rivales directos intentan igualar el catálogo y los sustitutos ofrecen minutos gratuitos. Netflix gana donde la producción local se exporta (Corea, España, India) y en la mezcla de plan y precio, y pierde participación mensual de horas frente a YouTube, que subió a 14,2% en julio de 2026 según una fuente secundaria ([PPC Land sobre The Gauge](https://ppc.land/nielsen-gauge/)). La amenaza de soluciones internas del estudio (cada estudio vendiendo directamente) existe pero la empresa ha respondido licenciando contenido de terceros, algo que recibió una expansión con Disney en el 3T26 ([carta del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm)). Un conjunto de herramientas especializadas, como YouTube más un plan de video corto y un servicio de deporte, puede sustituir a la plataforma completa aunque ningún rival individual lo logre, y es la hipótesis de sustitución que sostiene la historia de Disrupción.

La rivalidad se reparte en tres planos que no se comportan igual. En contenido de pago, Disney, Amazon y el grupo Paramount Skydance con WBD compiten por talento y derechos, y su capacidad de seguir gastando depende de que sus propios márgenes se lo permitan: Disney crece 6,8% con margen operativo de 19,3%, lejos del perfil de Netflix, y WBD terminó en manos de un comprador que debe integrarlo ([Yahoo Finance, DIS, 30 de septiembre de 2026](https://finance.yahoo.com/quote/DIS/); [Netflix, 10-Q del 2T26, nota 6](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000212/nflx-20260630.htm)). En atención gratuita, YouTube y el video corto no compiten por el abono sino por las horas, y es ahí donde Netflix no gana participación. En distribución, Roku y los fabricantes de televisores controlan la interfaz por la que llega el servicio, un riesgo de dependencia que la empresa mitiga con acuerdos de integración y con su propia interfaz de televisión. La lectura es que la competencia directa por suscriptores está moderada por la consolidación y la presión de márgenes de los rivales, mientras que la competencia por la atención es el verdadero frente abierto; de ahí que el seguimiento de la participación mensual de Nielsen sea el indicador más directo de que la ventaja se erosiona o se sostiene.

## 8. Gestión y asignación de capital

### Equipo, gobierno e incentivos

Los dos directores generales, Ted Sarandos y Greg Peters, dirigen la empresa y ambos figuran entre los directores; el director financiero es Spencer Neumann y el director jurídico David Hyman, que firma las actas y es secretario ([Netflix, 8-K del 5 de junio de 2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000189/nflx-20260604.htm)). El consejo nombró presidente a Jay Hoag, independiente y director líder desde 2012, con efecto al terminar la junta de junio de 2026, y eliminó la figura de director independiente líder. Anne Sweeney renunció al consejo el 26 de julio de 2026 sin discrepancias con la compañía ([Netflix, 8-K del 30 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000214/nflx-20260726.htm)). En la junta del 4 de junio de 2026 fueron elegidos doce directores; la remuneración de los ejecutivos obtuvo 2.661 millones de votos a favor y 517 millones en contra (83% de respaldo), una propuesta de actuar por consentimiento escrito recibió 44% de votos a favor y fue rechazada, y las propuestas de voto acumulativo y de informes de ESG o de «desalineación de marca» recibieron apoyo marginal.

La remuneración se paga «en el tope del mercado» y los empleados eligen entre efectivo y opciones; el 10-K describe esa política pero no detalla las métricas de incentivo de la alta dirección, que están en el proxy de abril de 2026 que no se revisó. La propiedad accionaria de directivos y sus compras o ventas recientes no figura en las fuentes revisadas: **“Información insuficiente en las fuentes disponibles para evaluar esto con confianza.”** La comunicación con inversionistas es una carta trimestral con un pronóstico interno de ingresos, margen y flujo, y la empresa recuerda que su guía es su «pronóstico real»; a cambio retiró las membresías en 2025 y limita desde 2027 el informe de horas vistas a una vez al año, lo que reduce la transparencia sobre el uso. Entre las decisiones acertadas están el plan con anuncios y el cobro por cuentas compartidas, que sostuvieron el crecimiento de 2024-2025, y la disciplina del margen; la decisión más discutible del período es la oferta por WBD, cuya negociación duró del 4 de diciembre de 2025 al 27 de febrero de 2026 y que elevó los gastos de terceros en US$107 millones en el 1S26, por honorarios legales y costos de transacción, aunque terminó con la comisión de US$2.800 millones ([Netflix, 10-Q del 2T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000212/nflx-20260630.htm), MD&A). No se juzga por el resultado ex post: pagar US$27,75 por acción en efectivo habría exigido el puente y las líneas a plazo comprometidos con bancos en diciembre de 2025 ([Netflix, 8-K del 22 de diciembre de 2025](https://www.sec.gov/Archives/edgar/data/1065280/000119312525327462/d82688d8k.htm)) y una deuda pro forma muy superior a la actual.

### Asignación de capital

| Uso de capital | Historial y magnitud | Retorno o resultado observable | Disciplina | Riesgo o pregunta pendiente |
|---|---|---|---|---|
| Reinversión orgánica e I+D | Contenido: adiciones de US$17.097 M en 2025 (US$12.555 M en 2023); tecnología y desarrollo US$3.391 M (US$3.891 M LTM) | Margen operativo +11,7 puntos entre 2022 y 2025 | Alta: relación gasto en efectivo/amortización ~1,1 | ¿Cuánto del margen se pierde si el deporte en vivo pasa de 5% a 10% del gasto? |
| Capex | US$688 M en 2025; US$933 M LTM (1,5%-1,9% de los ingresos) | Bajo en relación con el flujo | Alta | Una transacción inmobiliaria prevista para el 4T26 reduciría el flujo libre de 2026, guiado ahora en ~US$12.000 M ([carta del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm)) |
| Adquisiciones y desinversiones | Compra de unos US$587 M en marzo de 2026; oferta por WBD de US$27,75 por acción (primero mixta, luego en efectivo desde el 19 de enero de 2026), terminada el 27 de febrero de 2026 | Comisión de terminación de US$2.800 M cobrada; gastos de terceros +US$107 M en el 1S26 | Media: la oferta mostró disposición a una compra muy grande | ¿Intentará otra compra estructural? |
| Recompras y emisión de acciones | US$9.100 M y 86,5 M de acciones en 2025 (~US$105 por acción); US$10.782 M en los nueve meses de 2026, de ellos US$4.800 M en el 3T26 (63,9 M de acciones, ~US$75 por acción); autorización adicional de US$25.000 M en abril de 2026 y US$22.300 M disponibles al 3T26 ([carta del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm)) | Acciones en circulación −2,7% en nueve meses (4.222 → 4.106 M); la emisión por opciones compensa parte | Media: el precio medio de 2025 (~US$105) fue 51% superior al del corte (US$69,58) | ¿Se mantendrá el ritmo con un flujo libre de ~US$12.000 M? |
| Dividendos | Ninguno | n.a. | n.a. | Sin cambio previsto |
| Deuda y liquidez | Notas por US$15.132 M en libros al 30-sep-2026; US$1.000 M al 5,250% a 2036 emitidos en julio de 2026; revolvente de US$3.000 M sin usar | Deuda neta/EBITDA de 0,43 veces (LTM) | Alta | La compra de WBD habría exigido un puente y líneas a plazo comprometidos con bancos (8-K del 22 de diciembre de 2025) |

En recompras, el efectivo gastado en 2025 (US$9.100 millones) compró 86,5 millones de acciones, pero el ejercicio de opciones emitió 30,6 millones de acciones por US$667 millones de caja recibida, de modo que la reducción neta de acciones diluidas fue de 1,1%. La compensación basada en acciones es de US$368 millones, 4% del gasto de recompra. La evidencia más fuerte a favor de creación de valor por acción es la reducción de acciones con un ROIC de ~33%; la más fuerte en contra es que el cierre del 30 de septiembre de 2026 (US$69,58) está 34% por debajo del precio medio de compra de 2025 (~US$105). El resultado ex post no demuestra mala asignación, y el costo de oportunidad de recomprar a un precio mayor depende del valor que cada lector asigne. La conclusión se limita a la disciplina observable: la reinversión se mantiene en niveles que dejan un flujo libre creciente, y las recompras se financian con ese flujo y no con deuda.

## 9. Catalizadores

| Catalizador | Signo | Horizonte | Mecanismo de impacto | Evidencia necesaria para confirmarlo | Fecha o ventana |
|---|---|---|---|---|---|
| Resultados del 4T26 y guía de 2027 | Positivo o negativo | Corto | Confirma si el 4T26 llega a la guía (US$13.400 M y margen de 26,0%) y si el margen de 2027 se acerca a los ~34% que esperaba el consenso en abril de 2026 ([S&P Global con Visible Alpha](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/04/netflix-earnings-preview-q1-2026)) | Guía de margen 2027 ≥ 33% y crecimiento ≥ 11% ([carta del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm)) | Enero de 2027 |
| Calendario de eventos en vivo del 4T26 y 1T27 (NFL en Acción de Gracias y Navidad, un partido de final de temporada en enero, boxeo) | Positivo si atrae altas de miembros; negativo si el costo supera el aporte | Corto a mediano | El vivo es ~5% del gasto de contenido y ~1% de las horas, pero concentra los mejores días de altas de miembros | Altas de miembros y ventas de publicidad superiores al costo de los derechos | Noviembre de 2026 a enero de 2027 |
| Despliegue del plan con anuncios en 15 países nuevos y compromisos publicitarios de 2027 | Positivo | Mediano | Recupera la meta de publicidad tras la rebaja de 2026 (de ~US$3.000 a ~US$2.700 M) y sostiene el ingreso por miembro | Publicidad ≥ US$4.500 M en 2027 y comentarios de compromisos crecientes | 2027 |
| Ahorro de la reducción de personal anunciada en el 3T26 | Positivo | Mediano | El cargo de ~120 pb del 4T26 es de una vez; el ahorro mejora el margen de 2027 | Margen de 2027 ≥ 34% sin nuevos cargos | 2027 |
| Alzas de precio y acuerdos de contenido y distribución (licencia con Disney del 3T26, TF1 en Francia) | Positivo | Mediano | Mantienen el crecimiento del ingreso por miembro y suman uso | Retención estable tras las alzas y horas crecientes | 2026-2027 |
| Recompras con US$22.300 M de autorización restante | Positivo | Continuo | Reduce las acciones en circulación si el flujo libre se mantiene | Compras trimestrales ≥ US$4.000 M (US$4.800 M en el 3T26) | Cada trimestre |
| Informe anual de horas vistas (desde 2027) | Positivo o negativo | Mediano | Es la única medida pública del uso, variable central de la tesis | Horas totales ≥ +3% | Primer semestre de 2027 |
| Procesos fiscales en Brasil | Negativo | Mediano | Depósitos previstos y posibles cargos adicionales por impuestos no sobre la renta | Resolución de los procesos o nuevos cargos | Sin fecha publicada |

## 10. Riesgos

| Orden | Riesgo | Categoría | Probabilidad | Impacto | Mecanismo de daño | Indicador temprano | Señal de invalidación |
|---:|---|---|---|---|---|---|---|
| 1 | El tiempo de visualización se estanca y el precio por miembro deja de subir | Tesis | Media | Alto | El crecimiento depende de precio y publicidad; sin más uso, la rotación sube | Horas vistas ≤ +1% y alzas con cancelaciones | Ingresos ≤ +9% con margen ≤ 31,5% en 2027 |
| 2 | Sustitución de la atención por YouTube, video corto y contenido generado por IA | Competitivo y tecnológico | Media | Alto | Reduce el uso y el poder de precios | Participación de Netflix en el tiempo de televisión por debajo de 7% | Pérdida sostenida de participación durante cuatro trimestres |
| 3 | La publicidad no escala como se espera | Operativo | Media | Medio | Menor ingreso incremental de alto margen | Meta de 2026 ya rebajada de ~US$3.000 M a ~US$2.700 M (carta del 3T26) | Crecimiento publicitario < 40% en 2027 |
| 4 | Costo del contenido y de los derechos deportivos superior a los ingresos | Financiero | Media-alta | Alto | Absorbe el apalancamiento operativo | Relación gasto/amortización > 1,2 | Margen operativo ≤ 32% con ingresos creciendo ≥ 10% |
| 5 | Efecto cambiario y fiscal en mercados emergentes | Financiero y regulatorio | Alta | Medio | 56% de los ingresos está en monedas distintas del dólar; en LATAM el crecimiento reportado fue 12 puntos menor que a moneda constante en 2025 | Brecha entre crecimiento reportado y a moneda constante | Cargos fiscales adicionales por encima de ~US$700 M |
| 6 | Una compra grande o un cambio de estrategia de capital | Gobierno | Baja-media | Medio | La oferta por WBD mostró disposición a una transacción muy grande con financiación comprometida | Nuevas líneas de crédito comprometidas | Recompras detenidas por una adquisición |
| 7 | Consolidación de competidores (Paramount Skydance con WBD) | Competitivo | Media | Medio | Encarece derechos y catálogo | Anuncios de licencias exclusivas | Retiro de catálogo propio de terceros |
| 8 | Regulación de contenido, privacidad y publicidad | Regulatorio | Media | Bajo-medio | Costos de cumplimiento y cuotas de contenido local | Nuevas leyes sobre cuotas | Restricciones a la publicidad en menores |

Las categorías operativos, financieros, competitivos, tecnológicos, regulatorios, de gobierno y de tesis están cubiertas; el riesgo geopolítico no aparece como riesgo independiente porque no hay una exposición operativa localizada que lo justifique en las fuentes (la exposición a monedas emergentes ya se recoge en el riesgo 5).

### Escenarios cualitativos de largo plazo

Las cuatro historias del Modelo JMR son las mismas que se cuantifican en la sección 12; aquí se describen en términos operativos y sin calcular valor. Sus supuestos proceden de las celdas 'Input sheet'!B27-B33 y de la pestaña «Escenarios e historias».

| Variable | A · Base | B · Conservadora | C · Disrupción | D · Optimista | Evidencia que movería de escenario |
|---|---|---|---|---|---|
| Crecimiento y participación | Ingresos +12% el primer año y ~10% compuesto en cinco años | ~7% compuesto; participación estable | ~2,5% compuesto; pierde participación | ~12% compuesto; sube participación | Crecimiento trimestral de ingresos y participación en el tiempo de televisión |
| Poder de precios y retención | Alzas anuales absorbidas | Alzas con más rotación | Sin alzas posibles | Alzas sin rotación | Cancelaciones tras cada alza |
| Margen bruto y operativo | Margen operativo GAAP de 36% a cinco años | 32% | 22% | 40% | Margen trimestral frente a la guía |
| Reinversión y retorno sobre capital | Ventas/capital de 1,3 (años 1-5) y 0,9 (6-10); ROIC terminal de 20,58% (decisión del usuario) | Ventas/capital 1,1 y 0,8; ROIC terminal 20,58% | Ventas/capital 1,0 y 0,9; costo de capital terminal | Ventas/capital 1,5 y 1,1; ROIC terminal 20,58% | Relación gasto de contenido/amortización |
| Moat y sustitución | Ventaja durable | Ventaja durable bajo presión | Ventaja perdida | Ventaja reforzada por la publicidad | Participación frente a YouTube y rivales |

### FODA de síntesis

| Dimensión | Elementos específicos y respaldados |
|---|---|
| Fortalezas internas | Audiencia que se acerca a mil millones de personas; margen operativo de 17,8% a 29,5% en tres años y 34,6% en el 3T26; flujo libre guiado de ~US$12.000 M en 2026 con deuda neta de 0,43 veces el EBITDA |
| Debilidades internas | Dependencia del precio y de la publicidad para crecer mientras las horas vistas suben 2%; menor transparencia desde que dejó de publicar membresías y retención; gasto de contenido que exige reposición constante |
| Oportunidades externas | Publicidad conectada y programática; mercados de LATAM y APAC (+17% y +12% en el 3T26); deporte en vivo como contenido de adquisición; licencias de terceros y alianzas locales como la de TF1 |
| Amenazas externas | YouTube y el video corto compiten por la misma atención (13,5% del tiempo de televisión en Estados Unidos); consolidación de rivales (Paramount Skydance con WBD); riesgo cambiario y fiscal en mercados emergentes; costos crecientes de derechos |

La síntesis no repite la tabla de riesgos: la combinación más delicada es la de una debilidad interna (crecimiento apoyado en precio y publicidad) con una amenaza externa (sustitución de la atención), porque si ambas se dan a la vez, el apalancamiento operativo se revierte antes de que las fortalezas lo compensen.

## 11. Bulls say / Bears say

| Bulls say | Bears say |
|---|---|
| El margen operativo pasó de 17,8% a 29,5% en tres años, llegó a 34,6% en el 3T26 y la guía de 2026 es 31,5% con amortización de contenido creciendo solo ~10% frente a ingresos de +13% ([carta del 2T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000211/ex991_q226.htm)) | El tiempo de visualización creció solo 2% en el 1S26; el crecimiento de ingresos viene de precio, publicidad y mercados nuevos, no de uso |
| La publicidad (~US$2.700 M en 2026, ~5% de los ingresos) tiene margen incremental alto y plan de ampliación a más países | La guía del 3T26 (+12%) quedó por debajo de la expectativa del mercado de ~US$13.000 M (la acción cayó hasta 8,7%, según cobertura secundaria), el 3T26 creció 11,8% y la meta de publicidad de 2026 se rebajó a ~US$2.700 M |
| El flujo libre de ~US$12.000 M guiado para 2026 financia recompras de US$4.700-4.800 M por trimestre y mantiene la deuda neta en 0,43 veces el EBITDA | Netflix dejó de publicar membresías en 2025 y limitará el informe de horas vistas a una vez al año desde 2027, lo que reduce la visibilidad sobre retención |
| Las alzas de precio de 2026 en Estados Unidos, México y España se comportaron como las anteriores según la empresa, lo que indica poder de precios | YouTube concentra casi el doble del tiempo de televisión de Estados Unidos (13,5% frente a 7,9%) y su participación sube |
| La escala de gasto en contenido (US$17.097 M en 2025) y la red propia de entrega son difíciles de replicar; el ROIC es de ~33% | El contenido deportivo en vivo y la consolidación de rivales (Paramount Skydance con WBD) encarecen los derechos y amenazan el apalancamiento operativo |
| LATAM y APAC crecieron 21% y 16% en el 2T26 y 17% y 12% en el 3T26 con baja penetración y la mezcla de plan con anuncios abre nuevos hogares | El margen normalizado de 2025 fue 30,9% y la guía de 2026 (31,5%) implica solo 0,6 puntos de mejora subyacente |
| La oferta por WBD terminó con US$2.800 M cobrados; la gerencia mostró capacidad de negociar una transacción grande con financiación comprometida | El intento de compra mostró que la gerencia está dispuesta a una adquisición muy grande, con riesgo de dilución de retornos y de calificación |

El desacuerdo factual que resolvería la mayor parte de la divergencia es si el tiempo de visualización por hogar puede volver a crecer a ritmo medio de un dígito, porque de eso depende que el precio por miembro siga subiendo sin rotación; el resto (publicidad, contenido deportivo) son variables de segundo orden respecto a esa.

### Conclusión cualitativa

Netflix es hoy un negocio de alta calidad económica, con rentabilidad en ascenso y una ventaja de escala que no se erosiona en los datos de retorno, pero esa ventaja no ha impedido que la atención se desplace hacia plataformas gratuitas. La incertidumbre principal es el uso por miembro: mejoraría la tesis si las horas vistas aceleran por encima de 3%, si la publicidad cumple su meta de 2027 y si el margen supera 34% ese año; la empeoraría si los ingresos crecen menos de 9% o si el cociente gasto de contenido/amortización sube de 1,2.

### Síntesis final

La evolución operativa y la calidad financiera de Netflix están alineadas: los ingresos han crecido a dos dígitos en tres de los últimos cinco años, el margen operativo ganó 11,7 puntos en tres años y el flujo operativo pasó de negativo a 92% de la utilidad neta. La posición competitiva es sólida en escala y distribución, pero la tendencia de participación en el tiempo de televisión es desfavorable frente a YouTube, y las métricas de uso que la empresa publica son menos que antes; esa asimetría de información explica buena parte de la volatilidad de la acción y no permite concluir por sí sola sobre sostenibilidad.

Los escenarios guardados del Modelo JMR descansan en dos condiciones que este análisis puede evaluar cualitativamente: que el poder de fijación de precios se mantenga y que la publicidad escale sin deteriorar el margen. La primera tiene mejor soporte (tres alzas de 2026 absorbidas, ingresos de los nueve meses de 2026 +13,7%) que la segunda (la meta de ingresos publicitarios de 2026 se rebajó en la carta del 3T26). La Conservadora y la Disrupción recogen la posibilidad de que el uso no crezca y el precio deje de subir; la Optimista exige que la publicidad y el vivo ocupen un peso mayor sin presionar el costo del contenido. Ninguna se recalcula aquí.

La evidencia observable que fortalecería la tesis es un crecimiento de horas vistas superior a 3%, ingresos publicitarios de 2027 por encima de US$4.500 millones y un margen de 2027 superior a 34%; la que la debilitaría es una caída sostenida de la participación en el tiempo de televisión o un cociente de gasto de contenido/amortización por encima de 1,2. Calidad empresarial y atractivo de inversión son cosas distintas: un negocio con retornos altos puede estar bien o mal valorado, y esa comparación solo se hace en la sección 12 y al final.

## 12. Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$70,85 por acción** (Base · líder global de streaming con precio, publicidad y miembros).

**Complemento · promedio de tres historias (condicionado a que no ocurra la disrupción): US$71,05.** Los cuatro escenarios DCF activos son Base, Conservadora, Optimista y Disrupción; el rango de las tres primeras historias, sin Disrupción, es US$53,22–89,28, y la Disrupción vale US$23,11. El MOS 35% se aplica al DCF Base: US$46,05. La hoja calcula las cuatro en 'Valuation output'. Los múltiplos son lecturas secundarias: comparten crecimiento, margen e impuestos con el DCF de cada historia y sus anclas se justifican por historia.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo de la hoja: solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10. La tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El promedio de tres historias pondera Conservadora, Base y Optimista con pesos renormalizados; la Disrupción se calcula aparte. Todas las cifras salen de la foto `resultados_hoja.json` de la revisión `NFLX-2026-10-25` (sha256 `6afa5b…58d5`), la misma que usan la valoración y la auditoría. Las sensibilidades de un solo supuesto y el DCF inverso usan una réplica independiente del bloque Base que reproduce la hoja con error 0,000000 (`dcf_inverso.json`, `sensibilidades_un_supuesto.json`).

### La historia en un párrafo

En cinco a diez años Netflix es el servicio de entretenimiento por suscripción y publicidad con mayor audiencia del mundo (cerca de mil millones de personas) y el comprador individual más grande de series, películas y eventos en vivo. Los ingresos crecen ~10% anual compuesto en cinco años (12% el primer año, 8% el quinto). El aumento de precio por miembro sigue siendo la palanca principal en Estados Unidos y Canadá, pero cada vez más crecimiento sale de la publicidad (~US$2.700 millones en 2026 y planes con anuncios en 15 países nuevos en 2027) y de los mercados en crecimiento (América Latina y Asia-Pacífico, +12-17% en el 3T26). El margen operativo GAAP sube de 31,3% (LTM) a ~36% porque la amortización del contenido crece menos que los ingresos y porque la publicidad y la escala diluyen costos fijos de tecnología y administración. No llega más arriba porque el contenido, el deporte en vivo y la competencia por talento y atención (YouTube, video corto, IA generativa) mantienen alto el costo de seguir siendo «imprescindible». Reinvierte ~US$20.000 millones al año en contenido (las adiciones son ~1,1 veces la amortización) y devuelve el resto del flujo con recompras. El riesgo no es de caja: es que el tiempo de visualización (+2% en el 1S26) no crezca lo suficiente para sostener alzas de precio y que el costo del contenido absorba el apalancamiento operativo.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Los ingresos crecen ~10% compuesto en cinco años (12% el primer año) y llegan a ~US$80.000 millones | Sí | Sí: +13,7% en los nueve meses de 2026, +11,8% en el 3T26 y guía de US$51.100 millones (+13%) para 2026 ([Netflix, carta a accionistas del 3T26, 20-oct-2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm)); crecimiento de dos dígitos en las cuatro regiones, con alzas de precio que «se comportaron como las anteriores» | Probable con desaceleración: el tiempo de visualización creció solo 2% en el 1S26 (1,5% en 2025), así que el aumento viene de precio, miembros nuevos y publicidad, no de más uso por miembro; la guía del 4T26 (US$13.400 millones) implica ~+11% |
| La publicidad duplica su peso: de ~US$2.700 millones en 2026 a ~US$8.000 millones hacia 2031 | Sí | Sí: suite propia de tecnología publicitaria, acceso programático a eventos en vivo y planes con anuncios en 15 países nuevos en 2027 ([carta del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm)) | Plausible, no probable: es una línea de ~5% de los ingresos que debe crecer ~24% anual, y la meta de 2026 ya se rebajó de ~US$3.000 a ~US$2.700 millones |
| El margen operativo llega a 36% (GAAP) en cinco años | Sí | Sí: 17,8% en 2022, 20,6%, 26,7%, 29,5% en 2025, 31,3% en el LTM y 34,6% en el 3T26; guía de 31,5% para 2026 con un 4T26 de 26,0% por gasto estacional de contenido y ~120 pb de reducción de personal ([carta del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm)) | Plausible: el comparable maduro de contenido por suscripción de cable, Discovery, tuvo 31,7% en 2016 ([Discovery, Inc., XBRL de la SEC (companyfacts)](https://data.sec.gov/api/xbrl/companyfacts/CIK0001437107.json)); Netflix ya lo supera y pide ~5 puntos más por escala global y publicidad. El contenido en vivo cuesta ~5% del gasto de contenido para ~1% del tiempo de visualización |
| La caja financia el contenido, la deuda se mantiene y la recompra sigue (~US$15.000 millones al año) | Sí | Sí: flujo libre guiado de ~US$12.000 millones en 2026 y recompras de US$4.800 millones en el 3T26, con US$22.300 millones de autorización restante; deuda bruta de US$15.132 millones frente a caja de US$8.223 millones | Probable: la relación entre gasto de contenido en efectivo y amortización (~1,1 veces) es una decisión de la gerencia y puede subir si compite por más deportes o por estudios |

### Visión externa: tasas base

Con ventas LTM de US$49.735 millones (US$35.190 millones en dólares de 2015, deflactadas con el IPC-U: × 237,017 / 334,980), la empresa está en el tramo **>$25,000 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 2,1% y una mediana de 2,0% (desviación estándar 8,6%); sumando una inflación de 2,5%, la mediana nominal ronda 4,5%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| Base · líder global de streaming con precio, publicidad y miembros | 9,99% | 23% |
| Conservadora · saturación de miembros y competencia por el tiempo de pantalla | 7,19% | 34% |
| Optimista · publicidad y deportes en vivo amplían el mercado direccionable | 11,99% | 16% |

> **¿Qué pasaría si todo fallara?** Disrupción; fuera del promedio.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| Disrupción · el video generado por IA y las plataformas gratuitas comoditizan el contenido | 2,58% | 64% |

La Base (9,99% nominal) queda por encima de la mediana del tramo por razones específicas: el crecimiento actual es +11,8% a +13,7%, la publicidad partió de cero en 2022 y la penetración fuera de Norteamérica es baja. Aun así, la Base ya incorpora la regresión a la media: baja de 12% a 8% en cinco años y converge linealmente a 4% en el año 10. Que solo ~23% de las empresas de este tamaño hayan logrado ese crecimiento es la principal advertencia de la visión externa.

### Justificación de los supuestos

Cada párrafo explica un supuesto material de la tesis Base, que es el valor intrínseco principal: qué cifra se usa y con qué trayectoria, qué evidencia la respalda (fuente y fecha), el mecanismo económico, por qué se eligió frente a las alternativas, cómo cambia entre escenarios, qué observación obligaría a cambiarla y cuánto mueve el valor. Las sensibilidades son DCF completos de la Base con un solo supuesto cambiado. Donde falta soporte, el supuesto se declara provisional: que la hoja lo reproduzca aritméticamente no lo valida.

**Crecimiento: precio, publicidad y mercados nuevos; el uso por miembro no crece.** La Base crece 12% el primer año, 11%, 10%, 9% y 8% en los años 2-5 (9,99% compuesto) y converge linealmente a 4% en el año 10. El 3T26 creció 11,8% (UCAN +11%, EMEA +11%, LATAM +17%, APAC +12%) y los nueve meses 13,7%, con alzas de precio en Estados Unidos, México y España y una publicidad de ~US$2.700 millones. El año 1 (octubre de 2026 a septiembre de 2027) a 12% es coherente con la guía de 2026 (+13%) y con un 4T26 guiado de ~+11%. El tiempo de visualización creció solo 2%: el crecimiento viene del precio y de los miembros, no del uso, así que la Base desacelera un punto por año. La visión externa dice que ~23% de las empresas de su tamaño lograron al menos ese crecimiento; el desvío es específico (publicidad que parte de cero en 2022, penetración baja fuera de Norteamérica). Sensibilidad: ±2 puntos de crecimiento en los años 1-5, desvanecidos en los años 6-10, llevan el DCF Base a US$63,99 (−9,7%) y US$78,44 (+10,7%). Obligaría a revisarlo que los ingresos crezcan ≤ 9% en 2027 (hacia la Conservadora, 7,19%) o ≥ 13% (hacia la Optimista, 11,99%).

**Margen: el apalancamiento operativo sube de 31,3% a 36% GAAP; el contenido lo limita.** La hoja capitaliza tecnología y desarrollo, así que trabaja en base ajustada: el año 1 parte del margen LTM ajustado de 33,09% (31,30% GAAP + 1,80 pp de I+D capitalizado) y llega a 37,1% en el año 5 (36,0% GAAP + 1,1 pp de ajuste de I+D en estado estable al crecimiento del año 5). El margen fue 17,8% en 2022, 29,5% en 2025 y 34,6% en el 3T26; la guía de 2026 es 31,5%. Discovery llegó a 31,7% en 2016, así que 36% exige que la escala global y la publicidad compensen un costo de contenido que sigue subiendo. Sensibilidad: ±2 puntos de margen objetivo dan US$66,86 (−5,6%) y US$74,84 (+5,6%). La Conservadora (32% GAAP, 32,7% ajustado) supone que el contenido absorbe la mejora; la Disrupción (22%), pérdida de poder de precios; la Optimista (40% GAAP, 41,3% ajustado), publicidad de ~15% de los ingresos con margen alto.

**Reinversión: contenido sobre todo, con un retorno marginal que baja de forma gradual.** El ventas/capital es 1,3 en los años 1-5 (~US$0,77 de capital por dólar de ventas nuevas) y 0,9 en los años 6-10. El 1,3 coincide con el actual de la empresa (1,29 LTM) y queda muy por debajo del marginal observado entre 2022 y el LTM (2,66 sin I+D), porque el crecimiento futuro pide más contenido local, deporte en vivo y tecnología publicitaria que el crecimiento por cuentas compartidas de 2023-2025. El 0,9 de los años 6-10 es deliberadamente más bajo para que el rendimiento del capital nuevo baje de forma gradual hacia el ROIC terminal. Con el margen y el impuesto de cada tramo, el capital nuevo rinde ≈38% en los años 1-5 (0,355 × 0,83 × 1,3) y ≈26% en los años 6-10 (0,371 × 0,79 × 0,9) antes del 20,58% perpetuo. Esta revisión corrigió un primer borrador con 1,6, que daba un rendimiento marginal de ~49% con una caída abrupta a la perpetuidad. El flujo libre guiado de 2026 (~US$12.000 millones) es consistente: el FCFF del año 1 es US$10.665 millones, después de US$4.713 millones de reinversión. Con ±20% en el ventas/capital el DCF Base va de US$69,01 (−2,6%) a US$72,08 (+1,7%).

**Descuento y largo plazo: beta global del sector y una ventaja durable.** El costo de capital inicial es 10,02%: tasa libre de riesgo 5,29% al 30-sep-2026, prima de mercado madura de 3,70% de Damodaran ponderada por regiones (4,93%), beta 1,03 y costo de la deuda de 6,07% antes de impuestos con calificación A. El terminal es 8,99%. Después del año 10 el crecimiento es 4,00% y el ROIC terminal es 20,58%, por decisión documentada del usuario (ver «Ventaja competitiva y ROIC terminal»). El terminal pesa 63,8% del valor operativo. Mover solo el costo de capital inicial ±1 punto, con el terminal fijo, da US$66,81 (−5,7%) y US$75,19 (+6,1%). Mover toda la trayectoria ±1 punto (matriz A de la hoja) da US$58,24 (−17,8%) y US$89,77 (+26,7%). Con un ROIC terminal igual al costo de capital el DCF Base sería US$56,13 (−20,8%).

**Acciones, opciones y deuda.** Se usan 4.106,33 millones de acciones en circulación al 30-sep-2026 (portada del 10-Q del 3T26). Las 120,18 millones de opciones a US$41,24 (4,04 años, volatilidad 33,8%) se restan por su valor Black-Scholes de US$4.526,75 millones; las RSU (1,87 millones) no se valoran por inmateriales. La deuda es de US$17.384,63 millones: notas senior de US$15.132,39 millones más el pasivo por arrendamientos operativos de US$2.252,24 millones. La caja es US$8.222,95 millones, que ya incluye lo que queda de la comisión de WBD. Una dilución adicional de 5% llevaría el DCF Base a US$67,48 (−4,8%).

**Probabilidades y lectura del resultado.** Las probabilidades son 45% para la Base, 22,5% para la Conservadora, 22,5% para la Optimista y 10% para la Disrupción. Con ellas, el promedio de tres historias es US$71,05 frente a un DCF Base de US$70,85. Queda ligeramente por encima porque la Optimista sube más (+US$18,43) de lo que baja la Conservadora (−US$17,64). Con el margen de seguridad de 35%, el precio de compra con margen es US$46,05.

**Vida útil de I+D.** La hoja capitaliza la tecnología y el desarrollo (US$3.891 millones en el LTM) y los amortiza en 3 años: activo de I+D de US$7.126,84 millones y EBIT ajustado +US$893,33 millones. El mecanismo es que el I+D crea activos que rinden varios años: capitalizarlo mueve el gasto del EBIT al capital invertido. La vida elegida es una convención del modelo (tabla de Damodaran por sector), no un dato reportado. Una vida más larga eleva el activo y reduce el ROIC medido; una más corta hace lo contrario, y cambia también el EBIT ajustado. No se recalcula aquí porque modifica la hoja de conversión, no una entrada del DCF. Queda provisional hasta contrastarla con la duración de los beneficios de la plataforma.

**Del supuesto al valor: cómo se calcula la Base.**
1. Se parte de ventas LTM de US$49.734,63 millones. Con el crecimiento de la Base llegan a US$80.065,03 millones en el año 5 y a US$105.108,49 millones en el año 10.
2. A esas ventas se les aplica el margen operativo, que pasa de 33,09% en el año 1 a 37,1% desde el año 5. Luego se descuentan impuestos: 16,57% al principio y 25,0% a largo plazo. El resultado es el beneficio operativo después de impuestos (NOPAT): US$15.378,06 millones el primer año.
3. Crecer no es gratis: cada dólar de ventas nuevas exige capital. Esa reinversión (US$4.713,31 millones el primer año) se resta del NOPAT, y lo que queda es el flujo de caja libre de la empresa (FCFF): US$10.664,74 millones el primer año.
4. Cada flujo se trae a hoy con el costo de capital (10,02% al principio, 8,99% al final). Los diez años suman US$110.253,12 millones.
5. Después del año 10 se supone que la empresa crece 4,00% para siempre y reinvierte lo justo para ese crecimiento con un retorno de 20,58%. Esa perpetuidad vale hoy US$194.378,70 millones, 63,8% del total.
6. Flujos más terminal dan el valor de las operaciones: US$304.631,82 millones.
7. Para llegar al accionista se suma y se resta lo que no es operativo: más caja por US$8.222,95 millones, menos deuda por US$17.384,63 millones (incluye los arrendamientos) y menos opciones por US$4.526,75 millones. Queda un patrimonio común de US$290.943,40 millones.
8. Repartido entre 4.106,33 millones de acciones, da US$70,85 por acción.

Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos. El promedio de tres historias es su promedio ponderado por probabilidad.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos, con el peso de cada uno dentro de los múltiplos:

| Múltiplo | Caso Base | Peso dentro de los múltiplos |
|---|---:|---:|
| EV/EBITDA | 15,06× | 25% |
| EV/FCFF | 24,11× | 37,5% |
| P/E | 18,86× | 12,5% |
| P/FCFE | 20,53× | 12,5% |
| P/OCF | 22,35× | 12,5% |
| P/S | 5,22× | 0% |
| P/BV | 8,99× | 0% |

Los complementarios EV/EBIT (15,41×) y P/FCF (23,67×) se reproducen con la misma cadena de la plantilla y no tienen peso. Cada múltiplo se elige por ciclo, con el ajuste por la tasa libre y un techo en el ancla C, el múltiplo justificado por los fundamentales FY+3 de cada historia; los pares solo sirven de comprobación. El precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (10,34%). El consolidado ponderado de la Base es US$58,09.

Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. Por regla, las matrices de sensibilidad de múltiplos son solo de la Base: 14 matrices con ejes reales (múltiplo en veces × fundamental FY+3 en US$ millones) para el ancla JMR y para el múltiplo observado LTM, en el Nivel 2 (§7). Los siete centros JMR concilian con el valor presente FY+3 de la hoja. La tabla por método está en la sección 5 y en la valoración de esta revisión.

Sensibilidad del DCF Base (US$70,85; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp | US$66,86 | −5,6% |
| Margen objetivo +2 pp | US$74,84 | +5,6% |
| Crecimiento años 1–5 −2 pp (desvanecido en 6-10) | US$63,99 | −9,7% |
| Crecimiento años 1–5 +2 pp (desvanecido en 6-10) | US$78,44 | +10,7% |
| Ventas/capital −20% | US$69,01 | −2,6% |
| Ventas/capital +20% | US$72,08 | +1,7% |
| Costo de capital inicial +1 pp (terminal fijo) | US$66,81 | −5,7% |
| Costo de capital inicial −1 pp (terminal fijo) | US$75,19 | +6,1% |
| Crecimiento terminal −0,5 pp | US$67,68 | −4,5% |
| Crecimiento terminal +0,5 pp | US$74,73 | +5,5% |
| ROIC terminal = costo de capital | US$56,13 | −20,8% |
| Acciones +5% | US$67,48 | −4,8% |

Las filas de margen y crecimiento coinciden exactamente con la matriz C de la hoja ('Sensibilidad DCF'), lo que confirma que la réplica y la hoja calculan lo mismo.

### Piezas del valor

**Crecimiento.** Los ingresos LTM (octubre de 2025 a septiembre de 2026) suman US$49.735 millones: UCAN US$21.644 millones (43,5%), EMEA US$16.011 millones (32,2%), LATAM US$6.102 millones (12,3%) y APAC US$5.977 millones (12,0%). Son cálculo propio con el 10-K 2025 y los 10-Q del 3T25 y del 3T26 ([10-Q del 3T26, 21-oct-2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm)). Netflix reporta un solo segmento operativo: las regiones son la apertura que publica, no un segmento contable, y la publicidad está dentro de ellas. En el 3T26 los ingresos crecieron 11,8%: UCAN +11% (igual a moneda constante), EMEA +11% (+9% a moneda constante), LATAM +17% (+12%) y APAC +12% (+15%). La guía de 2026 es de US$51.100 millones (+13%) con un margen de 31,5% ([carta del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm)). El crecimiento de miembros y de precio explica casi todo; el tiempo de visualización por miembro es plano. La Base supone que los ingresos del año 1 crecen 12% y que el grupo desacelera un punto por año. Esa pendiente es similar a la de UCAN, que pasó de +18% en el 4T25 a +11% en el 3T26, compensada parcialmente por LATAM y APAC.

| US$ millones | 4T25 | 1T26 | 2T26 | 3T26 | LTM sep-26 | Peso LTM |
|---|---:|---:|---:|---:|---:|---:|
| UCAN | 5.339 | 5.245 | 5.432 | 5.628 | 21.644 | 43,5% |
| EMEA | 3.873 | 3.998 | 4.034 | 4.106 | 16.011 | 32,2% |
| LATAM | 1.418 | 1.497 | 1.584 | 1.603 | 6.102 | 12,3% |
| APAC | 1.421 | 1.509 | 1.510 | 1.537 | 5.977 | 12,0% |
| Total | 12.051 | 12.250 | 12.560 | 12.874 | 49.735 | 100% |

Los trimestres 4T25 a 2T26 son los de las cartas a accionistas. El 3T26 por región se obtiene como LTM menos esos tres trimestres y concilia con el crecimiento publicado: por ejemplo, UCAN 5.072 × 1,11 = 5.630 frente a 5.628.

**Márgenes.** El margen operativo GAAP LTM es 31,3%: EBIT de US$15.565 millones sobre US$49.735 millones. El cargo de Brasil de US$619 millones del 3T25 ya salió de la ventana LTM y no se normaliza. El LTM sí incluye ~US$100 millones de honorarios y costos de la transacción con WBD del 1T26, que NO se excluyen por inmateriales (0,2% de los ingresos). La comisión de terminación de WBD (US$2.800 millones, en «Interest and other income») está fuera del EBIT y no entra en la valoración operativa. La evolución del margen ha sido:
- 17,8% en 2022, 20,6% en 2023 y 26,7% en 2024.
- 29,5% en 2025 ([10-K 2025](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm)).
- 33,4% en el 2T26 y 34,6% en el 3T26.
- 31,5% guiado para 2026, con un 4T26 de 26,0%.

La mejora viene de que la amortización de contenido crece menos que los ingresos y de que la publicidad escala sobre una base fija de tecnología. El comparable maduro de contenido por suscripción es la red de cable de Discovery, que llegó a 31,7% en 2016, y Netflix ya lo supera. La Base usa 36% GAAP: el ~34% que el consenso esperaba para 2027 más ~2 puntos de publicidad y escala hacia 2031. Las otras historias usan:
- **Conservadora (32%):** el costo del contenido y del deporte absorbe el apalancamiento.
- **Optimista (40%):** la publicidad llega a ~15% de los ingresos con margen alto y el gasto de contenido crece la mitad que los ingresos.
- **Disrupción (22%):** se pierde el poder de fijar precios.

**Reinversión y retorno.** Netflix reinvierte sobre todo en contenido. Los activos de contenido netos suman US$34.605 millones (59% del activo total) al 30-sep-2026, y las adiciones de contenido son 1,14 veces la amortización en el LTM. Los otros activos fijos son pequeños (capex LTM de US$933 millones).

El capital invertido de la hoja es de US$45.574,77 millones, con I+D capitalizado y arrendamientos. Rinde un ROIC después de impuestos de 30,13% en el año base. El ventas/capital actual es 1,29 sin I+D. El marginal es mucho mayor: entre 2022 y el LTM los ingresos subieron US$18.119 millones con US$6.821 millones más de capital (2,66). La Base usa 1,3 en los años 1-5 y 0,9 en los años 6-10 (ver «Justificación de los supuestos»).

El flujo libre guiado para 2026 (~US$12.000 millones) es consistente con esa reinversión. La única compra relevante es la de marzo de 2026 (~US$587 millones), y la de WBD no se concretó.

| Partida | Valor | Fuente | Lectura |
|---|---:|---|---|
| Activos de contenido netos | US$34.605 M (30-sep-2026) | 10-Q del 3T26 | 59% del activo; se amortizan en ~4 años (90%) |
| Adiciones de contenido / amortización | 1,14 veces (LTM); ~1,1 (guía) | Snapshot SEC; carta del 3T26 | Reinversión neta de contenido ~14% de la amortización |
| Capital invertido de la hoja (con I+D y arrendamientos) | US$45.574,77 M | 'Valuation output' (fila 41) | ROIC después de impuestos 30,13% |
| Ventas/capital: actual / marginal 2022→LTM | 1,29 / 2,66 | Nivel 2 de la revisión | La Base usa 1,3 y 0,9 |

**Arrendamientos (criterio Damodaran).** Los arrendamientos operativos son deuda. Netflix ya los registra bajo ASC 842 y el Modelo JMR suma el pasivo contable (US$2.252,24 millones al 30-sep-2026) a la deuda y al peso de la deuda del WACC. Por eso el conversor de arrendamientos de la plantilla queda desactivado (B18 = No): reconvertirlos duplicaría la deuda. La consecuencia es que el EBIT no se ajusta por el componente financiero del alquiler. El efecto en esta revisión es una limitación pequeña, que en la versión anterior era de +0,35 pp de margen. Fuente: Damodaran, *Leases, Debt and Value*.

**Riesgo.** La beta desapalancada de Entertainment es 0,98 en la tabla global de Damodaran y 0,76 en la de Estados Unidos (enero de 2026, corregida por caja). La hoja usa la global, reapalancada con la deuda a valor de mercado de Netflix (D/E de 5,8%): 1,03, porque 56% de los ingresos está fuera de Norteamérica. La regresión semanal contra el S&P 500 da 0,93 a 2 años y 1,43 a 5 años; la de 5 años incluye la caída de 2022 y no se usa. La prima de mercado es 3,70% (octubre de 2026), ponderada por los ingresos de las cuatro regiones: 4,93%. El riesgo propio (dependencia del precio, competencia por la atención, costo de los derechos deportivos) es diversificable: va en las historias Conservadora y Disrupción, no en la tasa. La calificación A fija el costo de la deuda antes de impuestos en 6,07%.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF Base por acción |
|---|---:|---:|---:|---:|
| Hoja (bottom-up global de Entertainment, reapalancada) | 1,03 | 10,34% | 10,02% | US$70,85 |
| Referencia: bottom-up de Entertainment de EE. UU., reapalancada | 0,79 | 9,20% | 8,94% | US$75,54 |

La referencia de Estados Unidos solo se muestra como contraste y no cambia la valoración: mueve el costo de capital inicial y deja el terminal en 8,99%.

### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (hoja) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF Base de la hoja | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja durable | 30,13% | 11,04% | 8,99% | 20,58% | US$70,85 | US$56,13 |

Las fuentes de la ventaja son:
- La escala de audiencia (cerca de mil millones de personas) y de gasto en contenido.
- La distribución global.
- Diecinueve años de streaming que superaron la crisis de 2022.

La evidencia es un ROIC GAAP de 15-34% desde 2022 y de 30,13% en la hoja con I+D capitalizado, frente a un costo de capital de 9-10%.

El criterio (Damodaran, *Investment Valuation*, cap. 12) depende del tipo de ventaja:
- **Sin ventaja defendible:** el ROIC en crecimiento estable es el costo de capital.
- **Con una ventaja durable:** el promedio de la industria, sin superar el ROIC actual.
- **Si la ventaja se desvanece de forma visible:** el Modelo JMR adopta como convención el punto medio entre ambos. Esa cifra no es una regla universal de Damodaran.

**Decisión del usuario sobre el ROIC terminal (21-oct-2026).** La regla de ventaja durable llevaría el ROIC terminal al promedio de Entertainment, 11,04%. El usuario eligió el punto medio entre ese promedio y el ROIC actual de la hoja (`reference/moat_2026-09-30.json`, «Opción 2»), porque la escala de audiencia y de gasto en contenido es una ventaja que el promedio de la industria no refleja. Con el ROIC actual de esta revisión (30,13%), el punto medio es 20,58%, y se aplica igual en la Base, la Conservadora y la Optimista. La Disrupción usa el costo de capital.

La caída de la perpetuidad no es abrupta en valor, porque el ROIC terminal se aplica al capital nuevo. El rendimiento marginal baja de ≈38% (años 1-5) a ≈26% (años 6-10) y a 20,58%, mientras el ROIC medio sobre todo el capital (32,4% en el año 10) converge lentamente. La reinversión pasa de 16,0% del NOPAT en el año 10 a 19,4% en la perpetuidad. Por eso el FCFF terminal (US$24.504 millones) es casi igual al del año 10 (US$24.575 millones) pese a crecer 4%. Es un supuesto discutible pero razonable, y la auditoría lo trata como tal.

Con 11,04% el DCF Base sería US$60,98 y con el costo de capital, US$56,13. El riesgo de perder la ventaja va en la Disrupción, que usa el costo de capital. El ROIC actual de la hoja y el histórico GAAP difieren por la capitalización de I+D.

### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$70,85 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista). Conservadora, Base y Optimista se ponderan con probabilidades renormalizadas y dan un promedio de tres historias de US$71,05; la Disrupción queda aparte. Cada historia tiene su propia trayectoria de ventas, margen objetivo, reinversión, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central y el esperado, un promedio de desenlaces con pesos subjetivos.

#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$49.734,63 millones | 'Input sheet' B12: últimos doce meses de los estados de la SEC (snapshot conciliado). Por regiones: 21.644 + 16.011 + 6.102 + 5.977 = 49.735. |
| Margen inicial del DCF | 33,09% en el año 1 | Margen LTM ajustado por I+D capitalizado (31,30% GAAP + 1,80 pp). Converge al margen objetivo de cada historia en el año 5. |
| Impuesto | 16,57% en los años 1–5; 25,00% en el terminal | Tasa efectiva LTM y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales materiales (NOL adjudicado como inmaterial). |
| Descuento | WACC 10,02% → 8,99% | Tasa libre 5,29%, beta 1,03, ERP 4,93%. Constante en los años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | Base 1,3 / 0,9; Conservadora 1,1 / 0,8; Optimista 1,5 / 1,1; Disrupción 1,0 / 0,9 (años 1–5 / 6–10) | Hipótesis del analista dentro del rango empresa / marginal / sector, no datos reportados. |
| Crecimiento perpetuo | Base, Conservadora y Optimista: 4,00%; Disrupción: 0% | Crecimiento terminal del corte: 4% nominal con techo en la tasa libre. La Disrupción se estabiliza sin recuperarse: mantiene su crecimiento del año 5 (0%) en los años 6–10 y en perpetuidad (Damodaran, *The Stable Growth Rate*). |
| ROIC terminal | Base, Conservadora y Optimista: 20,58%; Disrupción: 8,99% (= WACC terminal) | Decisión del usuario del 21-oct-2026 (punto medio). La historia de erosión iguala el retorno al costo de capital. |
| Puente al patrimonio | Caja 8.222,95; deuda 17.384,63; opciones 4.526,75; acciones 4.106,33 millones | 'Valuation output' B27-B34. Acciones fijas: no se proyecta recompra ni dilución. |

#### 2. Cómo se convierte cada historia en ingresos

Ingreso del año t = ingreso del año anterior × (1 + crecimiento del año t). Las tasas de cada historia son hipótesis del analista sobre el grupo consolidado: los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo Base, año 1: 49.734,63 × 1,12 = US$55.702,79 millones. En los años 2–5 el crecimiento es 11%, 10%, 9% y 8%, y las ventas del año 5 son US$80.065,03 millones. El 9,99% de la tabla es el crecimiento anual compuesto de los cinco años, (80.065,03 / 49.734,63)^(1/5) − 1; no se usa como tasa constante.

#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En la Base, año 1: NOPAT = 55.702,79 × 33,09% × (1 − 16,57%) = US$15.378,06 millones; reinversión = (61.830,10 − 55.702,79) / 1,3 = US$4.713,31 millones; FCFF = US$10.664,74 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad, la reinversión terminal es NOPAT₁₁ × g / ROIC terminal, y el valor terminal al final del año 10 es FCFF₁₁ / (WACC terminal − g), con WACC terminal de 8,99%. La reinversión terminal sobre el NOPAT es:
- Base, Conservadora y Optimista: 19,4% (4,00% / 20,58%).
- Disrupción: 0% (g = 0).

Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.

#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en los bloques de 'Valuation output' para ingresos, crecimiento, margen operativo, impuesto, NOPAT, reinversión, flujo libre (FCFF), costo de capital, valor presente y ROIC sobre el capital invertido total. Los importes están en millones. La columna «Terminal» es el primer año de la perpetuidad y su ROIC es el ROIC terminal sobre el capital nuevo. Las tablas se generan con `scripts/jmr_research_tables.py` desde la misma foto de la revisión, sin transcripción manual.

| Base | Año base | Año 1 | Año 2 | Año 3 | Año 4 | Año 5 | Año 6 | Año 7 | Año 8 | Año 9 | Año 10 | Terminal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Crecimiento | — | 12,00 % | 11,00 % | 10,00 % | 9,00 % | 8,00 % | 7,20 % | 6,40 % | 5,60 % | 4,80 % | 4,00 % | 4,00 % |
| Ingresos | 49.734,63 | 55.702,79 | 61.830,10 | 68.013,11 | 74.134,28 | 80.065,03 | 85.829,71 | 91.322,81 | 96.436,89 | 101.065,86 | 105.108,49 | 109.312,83 |
| Margen operativo (base ajustada) | 33,09 % | 33,09 % | 34,70 % | 35,50 % | 36,30 % | 37,10 % | 37,10 % | 37,10 % | 37,10 % | 37,10 % | 37,10 % | 37,10 % |
| Impuesto | 16,57 % | 16,57 % | 16,57 % | 16,57 % | 16,57 % | 16,57 % | 18,26 % | 19,94 % | 21,63 % | 23,31 % | 25,00 % | 25,00 % |
| NOPAT | 13.730,41 | 15.378,06 | 17.896,60 | 20.141,09 | 22.449,55 | 24.780,94 | 26.028,56 | 27.123,43 | 28.039,42 | 28.753,44 | 29.246,44 | 30.416,30 |
| Reinversión | — | 4.713,31 | 4.756,16 | 4.708,60 | 4.562,11 | 4.434,37 | 6.103,45 | 5.682,31 | 5.143,30 | 4.491,82 | 4.671,49 | 5.911,82 |
| FCFF | — | 10.664,74 | 13.140,44 | 15.432,49 | 17.887,44 | 20.346,57 | 19.925,11 | 21.441,12 | 22.896,12 | 24.261,63 | 24.574,95 | 24.504,48 |
| Costo de capital | — | 10,02 % | 10,02 % | 10,02 % | 10,02 % | 10,02 % | 9,81 % | 9,61 % | 9,40 % | 9,20 % | 8,99 % | 8,99 % |
| VP del FCFF | — | 9.693,40 | 10.855,78 | 11.588,11 | 12.208,17 | 12.621,74 | 11.255,60 | 11.050,24 | 10.785,98 | 10.466,71 | 9.727,39 | — |
| ROIC | 30,13 % | 33,74 % | 35,59 % | 36,59 % | 37,57 % | 38,53 % | 37,86 % | 36,24 % | 34,82 % | 33,56 % | 32,43 % | 20,58 % |

| Conservadora | Año base | Año 1 | Año 2 | Año 3 | Año 4 | Año 5 | Año 6 | Año 7 | Año 8 | Año 9 | Año 10 | Terminal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Crecimiento | — | 10,00 % | 8,00 % | 7,00 % | 6,00 % | 5,00 % | 4,80 % | 4,60 % | 4,40 % | 4,20 % | 4,00 % | 4,00 % |
| Ingresos | 49.734,63 | 54.708,10 | 59.084,74 | 63.220,68 | 67.013,92 | 70.364,61 | 73.742,11 | 77.134,25 | 80.528,16 | 83.910,34 | 87.266,75 | 90.757,42 |
| Margen operativo (base ajustada) | 33,09 % | 33,09 % | 32,94 % | 32,86 % | 32,78 % | 32,70 % | 32,70 % | 32,70 % | 32,70 % | 32,70 % | 32,70 % | 32,70 % |
| Impuesto | 16,57 % | 16,57 % | 16,57 % | 16,57 % | 16,57 % | 16,57 % | 18,26 % | 19,94 % | 21,63 % | 23,31 % | 25,00 % | 25,00 % |
| NOPAT | 13.730,41 | 15.103,45 | 16.234,43 | 17.329,48 | 18.325,42 | 19.195,66 | 19.710,69 | 20.192,33 | 20.637,04 | 21.041,40 | 21.402,17 | 22.258,26 |
| Reinversión | — | 3.978,77 | 3.759,94 | 3.448,40 | 3.046,09 | 3.070,46 | 4.240,17 | 4.242,38 | 4.227,73 | 4.195,52 | 4.363,34 | 4.326,19 |
| FCFF | — | 11.124,68 | 12.474,49 | 13.881,08 | 15.279,33 | 16.125,20 | 15.470,52 | 15.949,95 | 16.409,31 | 16.845,89 | 17.038,83 | 17.932,07 |
| Costo de capital | — | 10,02 % | 10,02 % | 10,02 % | 10,02 % | 10,02 % | 9,81 % | 9,61 % | 9,40 % | 9,20 % | 8,99 % | 8,99 % |
| VP del FCFF | — | 10.111,44 | 10.305,61 | 10.423,18 | 10.428,13 | 10.003,07 | 8.739,22 | 8.220,22 | 7.730,15 | 7.267,49 | 6.744,40 | — |
| ROIC | 30,13 % | 33,14 % | 32,76 % | 32,50 % | 32,28 % | 32,10 % | 31,35 % | 30,08 % | 28,92 % | 27,84 % | 26,83 % | 20,58 % |

| Optimista | Año base | Año 1 | Año 2 | Año 3 | Año 4 | Año 5 | Año 6 | Año 7 | Año 8 | Año 9 | Año 10 | Terminal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Crecimiento | — | 14,00 % | 13,00 % | 12,00 % | 11,00 % | 10,00 % | 8,80 % | 7,60 % | 6,40 % | 5,20 % | 4,00 % | 4,00 % |
| Ingresos | 49.734,63 | 56.697,48 | 64.068,15 | 71.756,33 | 79.649,53 | 87.614,48 | 95.324,56 | 102.569,22 | 109.133,65 | 114.808,60 | 119.400,95 | 124.176,99 |
| Margen operativo (base ajustada) | 33,09 % | 33,09 % | 36,38 % | 38,02 % | 39,66 % | 41,30 % | 41,30 % | 41,30 % | 41,30 % | 41,30 % | 41,30 % | 41,30 % |
| Impuesto | 16,57 % | 16,57 % | 16,57 % | 16,57 % | 16,57 % | 16,57 % | 18,26 % | 19,94 % | 21,63 % | 23,31 % | 25,00 % | 25,00 % |
| NOPAT | 13.730,41 | 15.652,66 | 19.442,35 | 22.758,15 | 26.352,36 | 30.187,49 | 32.180,54 | 33.912,40 | 35.323,25 | 36.361,01 | 36.984,44 | 38.463,82 |
| Reinversión | — | 4.913,78 | 5.125,45 | 5.262,13 | 5.309,97 | 5.140,05 | 6.586,06 | 5.967,66 | 5.159,05 | 4.174,86 | 4.341,85 | 7.475,96 |
| FCFF | — | 10.738,88 | 14.316,90 | 17.496,02 | 21.042,39 | 25.047,44 | 25.594,48 | 27.944,74 | 30.164,20 | 32.186,15 | 32.642,59 | 30.987,86 |
| Costo de capital | — | 10,02 % | 10,02 % | 10,02 % | 10,02 % | 10,02 % | 9,81 % | 9,61 % | 9,40 % | 9,20 % | 8,99 % | 8,99 % |
| VP del FCFF | — | 9.760,78 | 11.827,70 | 13.137,60 | 14.361,42 | 15.537,86 | 14.458,20 | 14.402,04 | 14.209,85 | 13.885,43 | 12.920,77 | — |
| ROIC | 30,13 % | 34,35 % | 38,51 % | 40,92 % | 43,29 % | 45,61 % | 45,12 % | 43,53 % | 42,11 % | 40,84 % | 39,68 % | 20,58 % |

| Disrupción | Año base | Año 1 | Año 2 | Año 3 | Año 4 | Año 5 | Año 6 | Año 7 | Año 8 | Año 9 | Año 10 | Terminal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Crecimiento | — | 6,00 % | 4,00 % | 2,00 % | 1,00 % | 0,00 % | 0,00 % | 0,00 % | 0,00 % | 0,00 % | 0,00 % | 0,00 % |
| Ingresos | 49.734,63 | 52.718,71 | 54.827,46 | 55.924,01 | 56.483,25 | 56.483,25 | 56.483,25 | 56.483,25 | 56.483,25 | 56.483,25 | 56.483,25 | 56.483,25 |
| Margen operativo (base ajustada) | 33,09 % | 33,09 % | 28,66 % | 26,44 % | 24,22 % | 22,00 % | 22,00 % | 22,00 % | 22,00 % | 22,00 % | 22,00 % | 22,00 % |
| Impuesto | 16,57 % | 16,57 % | 16,57 % | 16,57 % | 16,57 % | 16,57 % | 18,26 % | 19,94 % | 21,63 % | 23,31 % | 25,00 % | 25,00 % |
| NOPAT | 13.730,41 | 14.554,23 | 13.106,99 | 12.334,13 | 11.412,12 | 10.366,77 | 10.157,36 | 9.947,95 | 9.738,55 | 9.529,14 | 9.319,74 | 9.319,74 |
| Reinversión | — | 2.108,75 | 1.096,55 | 559,24 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| FCFF | — | 12.445,48 | 12.010,44 | 11.774,89 | 11.412,12 | 10.366,77 | 10.157,36 | 9.947,95 | 9.738,55 | 9.529,14 | 9.319,74 | 9.319,74 |
| Costo de capital | — | 10,02 % | 10,02 % | 10,02 % | 10,02 % | 10,02 % | 9,81 % | 9,61 % | 9,40 % | 9,20 % | 8,99 % | 8,99 % |
| VP del FCFF | — | 11.311,95 | 9.922,25 | 8.841,65 | 7.788,76 | 6.430,89 | 5.737,85 | 5.126,94 | 4.587,67 | 4.110,97 | 3.688,99 | — |
| ROIC | 30,13 % | 31,93 % | 27,49 % | 25,29 % | 23,13 % | 21,01 % | 20,59 % | 20,16 % | 19,74 % | 19,31 % | 18,89 % | 8,99 % |

#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el valor por acción. Se calcula con precisión completa y se redondea solo al presentar.

| US$ millones | Base | Conservadora | Optimista | Disrupción |
|---|---:|---:|---:|---:|
| VP de los flujos de 10 años | 110.253,12 | 89.972,92 | 134.501,66 | 67.547,91 |
| VP del valor terminal | 194.378,70 | 142.243,86 | 245.807,30 | 41.034,36 |
| Valor de las operaciones | 304.631,82 | 232.216,78 | 380.308,97 | 108.582,27 |
| − Deuda (notas + arrendamientos) | 17.384,63 | 17.384,63 | 17.384,63 | 17.384,63 |
| + Caja e inversiones | 8.222,95 | 8.222,95 | 8.222,95 | 8.222,95 |
| − Opciones | 4.526,75 | 4.526,75 | 4.526,75 | 4.526,75 |
| Patrimonio común | 290.943,40 | 218.528,35 | 366.620,54 | 94.893,84 |
| Acciones (M) | 4.106,33 | 4.106,33 | 4.106,33 | 4.106,33 |
| Valor por acción (US$) | 70,85 | 53,22 | 89,28 | 23,11 |
| Peso del terminal en el valor operativo | 63,81 % | 61,25 % | 64,63 % | 37,79 % |

Ejemplo Base: (110.253,12 + 194.378,70 + 8.222,95 − 17.384,63 − 4.526,75) / 4.106,33 = US$70,85 por acción. El terminal representa 63,8% del valor operativo de la Base, así que el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente. La Disrupción depende mucho menos del terminal (37,8%).

#### 6. Promedio de tres historias (complemento), probabilidades y margen de seguridad

Las probabilidades 45% / 22,5% / 22,5% / 10% son la previa de la etapa «crecimiento maduro» de la regla de la cartera, sin ajustes, porque ningún indicador cruzó su umbral al corte (ver «Indicadores»). No se estimaron con un modelo estadístico ni se deducen de las tasas base: deben leerse como pesos discutibles y revisables, no como precisión empírica.

Promedio de tres historias = (0,45 × 70,852485 + 0,225 × 53,217489 + 0,225 × 89,281890) / 0,90 = US$71,05. La Disrupción se calcula aparte y queda excluida del promedio. La plantilla IA calculaba este promedio como media simple (AVERAGE de H5, H6 y H8, que daba US$71,12) e ignoraba las probabilidades. La auditoría de esta revisión lo registró como hallazgo AUD-01 y la fórmula se corrigió en la copia de trabajo, con respaldo, para aplicar la regla vigente de pesos renormalizados. La plantilla oficial no se modificó.

Precio con MOS = DCF Base × (1 − 35%) = US$46,05. Se conserva la regla de MOS sobre la Base.

Trazabilidad: la hoja calcula cada historia en 'Valuation output' con la estructura de Damodaran:

| Historia | Filas | Valor por acción |
|---|---|---|
| Base | 2–42 | B35 |
| Conservadora | 53–93 | B86 |
| Optimista | 104–144 | B137 |
| Disrupción | 157–197 | B190 |

La pestaña «Escenarios e historias» guarda los supuestos de cada historia y resume los resultados: A5:N8, promedio en H10, Base en H11 y rango en H12:H13. Los candados K5:K8 están en LISTO. Las fórmulas de la hoja y la réplica independiente dan el mismo valor Base. Esa concordancia verifica la aritmética, no la validez económica de los supuestos.

### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$70,85, es el valor intrínseco principal. El promedio de tres historias, US$71,05, combina solo Conservadora, Base y Optimista con pesos renormalizados y se presenta como complemento. La Disrupción describe un deterioro estructural del negocio; no presupone una quiebra.

#### Base: líder global de streaming con precio, publicidad y miembros

**Qué tiene que ocurrir.** Los ingresos crecen 12% el año 1 y desaceleran un punto por año hasta 8% en el año 5:
- El precio aporta 4-5 puntos en UCAN y EMEA.
- Los miembros nuevos en LATAM y APAC (+12-17% en el 3T26) compensan el techo de penetración en Norteamérica.
- La publicidad sube de ~5% a ~10% de los ingresos.

El margen GAAP sube de 31,3% a 36% en cinco años, porque la amortización de contenido crece más lento que los ingresos y la publicidad gana escala.

**Traducción al modelo.** Crecimiento de 12%, 11%, 10%, 9% y 8% en los años 1-5 (9,99% compuesto), con convergencia lineal a 4% en el año 10. Margen objetivo de 37,1% en base ajustada. Ventas/capital de 1,3 en los años 1-5 y 0,9 en los años 6-10. ROIC terminal de 20,58% y crecimiento terminal de 4,00%. Probabilidad de 45% y DCF de US$70,85 por acción.

**Cómo contrastarla.** Ingresos ≥ +11% en 2027, margen ≥ 34% en 2027 y publicidad ≥ US$4.500 millones en 2027.

#### Conservadora: saturación de miembros y competencia por el tiempo de pantalla

**Qué tiene que ocurrir.** El tiempo de visualización sigue creciendo ~1-2% y los miembros reaccionan a las alzas de precio con más rotación, así que el precio por miembro crece la mitad. La publicidad avanza más lento: la meta de 2026 ya se recortó a ~US$2.700 millones. Los derechos deportivos y el costo del talento suben, y el margen se estanca en 32% GAAP, apenas por encima del nivel guiado para 2026.

**Traducción al modelo.** Crecimiento de 10%, 8%, 7%, 6% y 5% en los años 1-5 (7,19% compuesto), con convergencia a 4%. Margen objetivo de 32,7% en base ajustada. Ventas/capital de 1,1 y 0,8. ROIC terminal de 20,58%, por la decisión del usuario: la erosión va en crecimiento, margen y reinversión. Crecimiento terminal de 4,00%. Probabilidad de 22,5% y DCF de US$53,22 por acción.

**Cómo contrastarla.** Ingresos ≤ +9% en 2027, tiempo de visualización ≤ +1% y margen ≤ 31,5% en 2027.

#### Disrupción · Deterioro de los fundamentales: el video generado por IA y las plataformas gratuitas comoditizan el contenido

**Qué tiene que ocurrir.** La atención de los menores de 35 años sigue migrando a YouTube, al video corto y al contenido generado por usuarios o por IA a costo casi cero. Netflix pierde poder de fijar precios, la rotación sube y los estudios retiran su catálogo para sus propias plataformas. Los ingresos del año 1 ya están en parte contratados (alzas de 2026) y luego dejan de crecer. El contenido es un costo fijo que hay que sostener para no perder más miembros: el margen baja a 22%, el ROIC después del año 10 es el costo de capital y la empresa se estabiliza sin recuperación.

**Traducción al modelo.** Crecimiento de 6%, 4%, 2%, 1% y 0% en los años 1-5 (2,58% compuesto) y 0% después. Margen objetivo de 22%. Ventas/capital de 1,0 y 0,9. ROIC terminal igual al costo de capital (8,99%) y crecimiento terminal de 0%. Probabilidad de 10% y DCF de US$23,11 por acción.

**Cómo contrastarla.** Ingresos ≤ +3% por dos trimestres, rotación al alza, y que Netflix deba recortar precios o ampliar la oferta gratuita.

#### Optimista: publicidad y deportes en vivo amplían el mercado direccionable

**Qué tiene que ocurrir.** La publicidad pasa de ~US$2.700 millones a más de US$10.000 millones en 2031, por el acceso programático y el vivo (NFL, WWE, boxeo). El plan con anuncios llega a 15 países más en 2027, y la alianza con emisoras locales (TF1) se replica. El precio sigue subiendo sin rotación y el gasto de contenido crece la mitad que los ingresos. El margen GAAP llega a 40% porque la publicidad tiene un margen incremental alto.

**Traducción al modelo.** Crecimiento de 14%, 13%, 12%, 11% y 10% en los años 1-5 (11,99% compuesto), con convergencia a 4%. Margen objetivo de 41,3% en base ajustada. Ventas/capital de 1,5 y 1,1. ROIC terminal de 20,58% y crecimiento terminal de 4,00%. Probabilidad de 22,5% y DCF de US$89,28 por acción. En esta historia el rendimiento del capital nuevo pasa de ≈36% en los años 6-10 a 20,58% en la perpetuidad. Es el salto más grande de las cuatro historias, y la auditoría lo registra como supuesto discutible.

**Cómo contrastarla.** Publicidad ≥ US$6.000 millones en 2027, ingresos ≥ +13% en 2027 y margen ≥ 35% en 2027.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Las diferencias proceden de ventas, margen, reinversión, crecimiento terminal y ROIC terminal. El crecimiento terminal es 4,00% en la Base, la Conservadora y la Optimista, y 0% en la Disrupción. Las probabilidades suman 100% y son juicio del analista, no datos publicados por la empresa. La Disrupción se separa de la Conservadora porque plantea una pérdida estructural de la ventaja; la Conservadora, una erosión gradual.

### Historias cuantificadas: DCF Base y promedio de tres historias

| Historia | Probabilidad | Crecimiento años 1-5 | CAGR de ingresos (años 1–5) | Margen objetivo (ajustado / GAAP) | Ventas/capital (1-5 · 6-10) | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,03, hoja) | Valor/acción (referencia beta 0,79) |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| **Base · líder global de streaming con precio, publicidad y miembros** | 45% | 12%, 11%, 10%, 9%, 8% | 9,99% | 37,1% / 36% | 1,3 · 0,9 | 20,58% | 4,00% | US$70,85 | US$75,54 |
| **Conservadora · saturación de miembros y competencia por el tiempo de pantalla** | 22,5% | 10%, 8%, 7%, 6%, 5% | 7,19% | 32,7% / 32% | 1,1 · 0,8 | 20,58% | 4,00% | US$53,22 | n.c. |
| **Optimista · publicidad y deportes en vivo amplían el mercado direccionable** | 22,5% | 14%, 13%, 12%, 11%, 10% | 11,99% | 41,3% / 40% | 1,5 · 1,1 | 20,58% | 4,00% | US$89,28 | n.c. |
| **Promedio de tres historias (complemento)** | 90% renormalizado |  |  |  |  |  |  | **US$71,05** | n.c. |

> **¿Qué pasaría si todo fallara?** Disrupción; fuera del promedio.

| Historia | Probabilidad | Crecimiento años 1-5 | CAGR de ingresos (años 1–5) | Margen objetivo | Ventas/capital (1-5 · 6-10) | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,03, hoja) |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| **Disrupción · el video generado por IA y las plataformas gratuitas comoditizan el contenido** | 10% | 6%, 4%, 2%, 1%, 0% | 2,58% | 22% | 1,0 · 0,9 | = costo de capital (8,99%) | 0% | US$23,11 |

«n.c.»: no calculado. La réplica independiente solo cubre el bloque Base; las otras historias con la beta de referencia no se recalculan para no publicar cifras fuera del motor de la hoja. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF Base (matriz C de 'Sensibilidad DCF'; US$ por acción; filas = CAGR de los años 1-5, columnas = margen operativo objetivo en base ajustada). Cada celda es un DCF completo y el centro concilia con el DCF Base de la hoja:

| CAGR \ Margen | 33,10% | 35,10% | 37,10% | 39,10% | 41,10% |
|---|---:|---:|---:|---:|---:|
| 5,99% | 51,50 | 54,64 | 57,78 | 60,92 | 64,06 |
| 7,99% | 56,90 | 60,45 | 63,99 | 67,53 | 71,07 |
| 9,99% | 62,87 | 66,86 | **70,85** | 74,84 | 78,83 |
| 11,99% | 69,46 | 73,95 | 78,44 | 82,93 | 87,41 |
| 13,99% | 76,73 | 81,77 | 86,81 | 91,85 | 96,89 |

La versión del 21-oct publicaba en este lugar una matriz con valores de US$14-36, incompatibles con el DCF Base de esa misma versión: era un defecto suyo. Esta revisión usa la matriz de la hoja, cuyo centro concilia.

### Pre-mortem

1. El tiempo de visualización se estanca o cae: las alzas de precio se agotan y la rotación sube, como en la Conservadora.
2. La publicidad no escala: después de la rebaja de 2026 (de US$3.000 a ~US$2.700 millones) llega otra, y el margen incremental es menor.
3. El costo del contenido y de los derechos deportivos crece más que los ingresos, y el margen no pasa de 32-33%.
4. Un dólar más fuerte recorta 1-2 puntos el crecimiento reportado de un negocio con 56% de los ingresos fuera de Norteamérica.
5. Una compra grande (un nuevo intento de estudio o de plataforma) destruye valor o pone en riesgo la calificación y la recompra.

**Evidencia en contra de la historia más probable:**
- El tiempo de visualización creció solo 2% en el 1S26, y la empresa lo publicará una vez al año desde 2027.
- El crecimiento desaceleró de +13,4% en el 2T26 a +11,8% en el 3T26.
- La meta de publicidad y la de flujo libre de 2026 se rebajaron en la carta del 3T26 ([carta del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm)).
- La guía del 4T26 (margen de 26,0%) incluye ~120 pb por reducción de personal.
- La oferta por WBD mostró que la gerencia está dispuesta a una adquisición muy grande.
- La acción cotiza ~42% por debajo del precio de un año antes.

### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| Crecimiento de ingresos (a/a) | +11,8% (3T26); +13,7% (9M26); guía 4T26 ~+11% | ≥ +11% en 2027 | ≤ +9% |
| Margen operativo | 34,6% (3T26); guía 2026 31,5% | ≥ 34% en 2027 | ≤ 31,5% |
| Ingresos de publicidad | ~US$2.700 M (2026, guía rebajada) | ≥ US$4.500 M en 2027 | Nueva rebaja o crecimiento < 40% |
| Tiempo de visualización | 97.000 M horas, +2% (1S26) | ≥ +3% | ≤ +1% |
| Gasto de contenido en efectivo / amortización | ~1,1 veces (guía); adiciones / amortización 1,14 (LTM) | ≤ 1,1 | ≥ 1,2 |
| Participación en el tiempo de TV en EE. UU. (Nielsen) | 7,9% (jun-2026) | ≥ 8,3% | ≤ 7,0% |
| Flujo libre | ~US$12.000 M (guía 2026) | Crece con el margen | Cae pese a más ingresos |
| Recompra de acciones | US$4.800 M en el 3T26; US$22.300 M de autorización restante | Sostenida sobre US$10.000 M al año | Se frena por una compra |
| Acciones en circulación | 4.106,33 M (30-sep-2026; −2,7% en nueve meses) | Bajan ≥ 2% al año | Suben |

Ningún indicador cruzó su umbral al corte: el crecimiento del 3T26 (+11,8%) quedó entre +9% y +11%, y el margen del 3T26 (34,6%) supera el umbral favorable de un trimestre, pero el umbral es anual para 2027. Por eso las probabilidades quedan en la previa. Cada trimestre conviene mover 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores. El valor de cada historia solo cambia si cambia un supuesto (crecimiento, margen, reinversión o riesgo).

### El precio al final

Precio de referencia (cierre del 30-sep-2026, corte común de la cartera): **US$69,58**.

DCF inverso: crecimiento anual de ingresos de los años 1-5 que justifica ese precio. Delta común en los años 1-5, desvanecido en los años 6-10, con los demás supuestos fijos. Entre paréntesis, la fracción de empresas de este tamaño que lo logró:

|  | Margen 35,1% | Margen 37,1% (Base) | Margen 39,1% |
|---|---:|---:|---:|
| Beta 1,03 (hoja) | 10,78% (20% de las empresas) | 9,63% (24%) | 8,57% (28%) |
| Beta 0,79 (referencia EE. UU.) | 9,51% (25%) | 8,39% (29%) | 7,34% (33%) |

Frente al DCF Base de US$70,85, el valor intrínseco principal, el precio está 1,8% por debajo. Frente al promedio de tres historias (US$71,05), está 2,1% por debajo. El precio pide casi exactamente la Base: con su margen, el DCF inverso exige un crecimiento de los años 1-5 de 9,63%, frente a 9,99% de la Base (−0,36 pp).

¿Qué sabe el mercado que yo no? Que la meta de publicidad ya se rebajó, que el uso por miembro casi no crece y que el 4T26 tendrá un margen bajo. Esos riesgos están en la Conservadora, pero el mercado puede estar dándoles más peso que el 22,5%. En sentido contrario, el crecimiento del 3T26 y su margen se cumplieron, y la recompra reduce las acciones ~3-4% al año.

Con el MOS de 35%, el precio de compra según la regla de la cartera es US$46,05. El precio actual está 51% por encima de ese nivel.

### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 (corte); revisión NFLX-2026-10-25 |  |
| Historia en una frase | Plataforma global de entretenimiento: ingresos +10% anual, publicidad que duplica su peso y margen GAAP que sube de 31% a 36% |  |
| Probabilidades | Base 45% / Conservadora 22,5% / Optimista 22,5% / Disrupción 10% |  |
| DCF Base hoy (valor intrínseco principal) | US$70,85 |  |
| Promedio de tres historias (complemento) | US$71,05 |  |
| Precio con MOS sobre el DCF Base | US$46,05 (MOS 35%) |  |
| Rango (historia más débil a más fuerte, sin Disrupción) | US$53,22 a US$89,28 |  |
| Confianza | Media-alta: el negocio genera caja y su ventaja de escala está documentada; el margen terminal, el ROIC terminal y el aporte de la publicidad no |  |
| Qué cambiaría la opinión | El tiempo de visualización, la publicidad y el costo del contenido y de los derechos deportivos |  |
| Revisión | Resultados del 4T26 y guía de 2027 (enero de 2027) |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.

### Fuentes de esta sección

- [Netflix, 10-Q del 3T26 (21-oct-2026)](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm)
- [Netflix, 10-Q del 3T25 (22-oct-2025)](https://www.sec.gov/Archives/edgar/data/1065280/000106528025000406/nflx-20250930.htm)
- [Netflix, 10-K 2025 (23-ene-2026)](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm)
- [Netflix, carta a accionistas del 3T26 (20-oct-2026)](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm)
- [Netflix, carta a accionistas del 2T26 (16-jul-2026)](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000211/ex991_q226.htm)
- [Netflix, 8-K de la terminación de la compra de WBD (27-feb-2026)](https://www.sec.gov/Archives/edgar/data/1065280/000119312526082247/d120618d8k.htm)
- [Netflix, 8-K de emisión de notas a 2036 (22-jul-2026)](https://www.sec.gov/Archives/edgar/data/1065280/000119312526312575/d171951d8k.htm)
- [Discovery, Inc., companyfacts de la SEC](https://data.sec.gov/api/xbrl/companyfacts/CIK0001437107.json)
- [Damodaran, ERP implícita de octubre de 2026](https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx)
- [Damodaran, betas por industria (enero de 2026)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
- [Mauboussin y Callahan, The Base Rate Book (2016)](https://www.credit-suisse.com/media/assets/corporate/docs/about-us/research/publications/the-base-rate-book-integrating-the-past-to-better-anticipate-the-future.pdf)
- Revisión `NFLX-2026-10-25`: `resultados_hoja.json`, `dcf_inverso.json`, `sensibilidades_un_supuesto.json`, `tablas_research.md`, `multiplos_complementarios.json`

## 13. Filosofías de inversión

Cada marco se aplica de forma independiente a los hechos de las secciones 2 a 11. No se atribuyen citas a ningún inversor ni se calcula valoración.

### Warren Buffett

El negocio es comprensible: un abono mensual por entretenimiento que se paga con tarjeta y cuyo costo principal, el contenido, se amortiza en pocos años. La economía es atractiva por el ROIC de ~33% y un margen operativo de 29,5% en 2025 (31,3% en el LTM), pero el criterio de ventaja durable y previsibilidad es más exigente: la ganancia de cada ejercicio depende de que los títulos que se financian hoy sigan atrayendo audiencia, y el gasto anual en contenido (40% de los ingresos LTM) se parece más a un costo operativo recurrente que a un capex de mantenimiento pequeño. La capacidad de reinversión es alta, el requerimiento de capital es bajo, y la gerencia ha mostrado disciplina de márgenes aunque su oferta por WBD habría cambiado el perfil de capital.

- **Veredicto:** Mixto.
- **Encaje:** Encaja parcialmente.
- **Tres evidencias:** (1) ROIC de ~33% con deuda neta de 0,43 veces el EBITDA; (2) flujo libre de US$9.461 millones en 2025 con un capex de 1,5% de los ingresos; (3) previsibilidad menor que la de un negocio de ingresos contratados, porque el crecimiento depende de precio y publicidad y el uso casi no crece.
- **Principal objeción:** una parte relevante de la «ganancia» se reinvierte cada año en contenido que debe reponerse (adiciones de US$19.991 millones frente a amortización de US$17.529 millones en el LTM), de modo que la ganancia distribuible es menor que la utilidad contable.
- **Pregunta pendiente:** ¿qué parte del gasto de contenido es mantenimiento de la audiencia actual y cuál es inversión para crecer?

### Charlie Munger

Los incentivos están alineados en la forma de pago (los empleados eligen entre efectivo y opciones, y existen 120,18 millones de opciones a US$41,24 al 30-sep-2026), la cultura está documentada en un memorándum público y el riesgo de ruina es bajo con una cobertura de intereses de 18 veces. Los efectos de segundo orden son relevantes: cada alza de precio sostiene el margen hoy pero acerca al cliente a la sustitución por una oferta gratuita, y el deporte en vivo mejora el reclutamiento de miembros a costa de un contenido caro que sube la expectativa de gasto para siempre. La complejidad contable (amortización acelerada, impuestos no sobre la renta de Brasil) existe pero no oculta la economía. Hay sesgo de narrativa en el éxito reciente: la empresa ganó la guerra del streaming en 2023-2025, y el mercado puede extrapolar esa victoria.

- **Veredicto:** Favorable.
- **Encaje:** Encaja.
- **Tres evidencias:** (1) incentivos por opciones y una remuneración «en el tope del mercado» con 83% de apoyo en la votación consultiva de 2026; (2) balance sin presión (deuda neta/EBITDA de 0,43 veces); (3) corrección de rumbo documentada en 2022-2023, con el plan con anuncios y el cobro por cuentas compartidas.
- **Principal objeción:** la oferta por WBD indica que la gerencia puede cambiar el perfil de riesgo de la compañía con una sola operación.
- **Pregunta pendiente:** ¿qué reglas de capital impiden otra compra grande en un mercado de consolidación?

### Peter Lynch

Netflix se clasifica hoy como crecimiento rápido que entra en madurez: los ingresos crecen 13% anual y el beneficio por acción diluido 28% en 2025, una combinación que la categoría de «rápida» admite hasta que el crecimiento baje de 10%. La historia es sencilla: más hogares, más precio y más publicidad. El recorrido existe en LATAM y APAC (+17% y +12% en el 3T26) y en publicidad, y la deuda es baja. La señal operativa que invalidaría la historia es la del uso: horas vistas por debajo de +1% y alzas de precio con cancelaciones.

- **Veredicto:** Favorable.
- **Encaje:** Encaja.
- **Tres evidencias:** (1) crecimiento de ingresos de dos dígitos y BPA diluido +28% en 2025; (2) recorrido en mercados de baja penetración y en publicidad; (3) recompras que reducen las acciones diluidas.
- **Principal objeción:** la categoría «rápida» presupone que el crecimiento no depende del precio, y aquí sí depende.
- **Pregunta pendiente:** ¿qué parte del crecimiento de 2027 vendrá de miembros y uso y qué parte de precio?

### Howard Marks

El ciclo de percepción importa: en 2022 el mercado castigó una desaceleración de crecimiento a 6,5%; en 2025 premió márgenes crecientes; en 2026 la acción cae al nivel de US$69,58 al 30 de septiembre, 34% por debajo del precio medio de las recompras de 2025, después de una guía por debajo de lo esperado. La expectativa observable más reciente es la guía del 4T26 (US$13.400 millones y margen de 26,0%) después de un 3T26 de +11,8%; no se infieren expectativas más precisas. El rango de resultados es amplio: desde una estabilización de ingresos con margen de 22% hasta un margen de 40% con publicidad, lo que da asimetría que no se cuantifica aquí. Una pérdida permanente exigiría que se confirme la historia de sustitución de la atención, no solo volatilidad de la cotización.

- **Veredicto:** Mixto.
- **Encaje:** Encaja parcialmente.
- **Tres evidencias:** (1) la acción cayó hasta 8,7% tras la guía del 3T26, según cobertura secundaria; (2) la tasa libre de riesgo es 5,29% frente a 3,88% a fines de 2023, lo que reduce el valor presente de flujos lejanos; (3) la cobertura de analistas ha bajado objetivos tras el 2T26, según fuentes secundarias.
- **Principal objeción:** el negocio ha superado antes períodos de pesimismo (2022) y la psicología negativa de hoy puede ser pasajera.
- **Pregunta pendiente:** ¿qué parte de la caída refleja una reducción de expectativas de crecimiento y qué parte un cambio en la tasa de descuento?

### Joel Greenblatt

El retorno sobre el capital empleado es el punto más favorable: el EBIT LTM de US$15.565 millones sobre un capital invertido de US$38.448 millones (con arrendamientos) equivale a ~40% antes de impuestos (ROIC después de impuestos de 33,8%), con eficiencia operativa creciente (margen de 17,8% a 29,5%). La normalización del beneficio exige separar la comisión de WBD (US$2.800 millones, fuera del EBIT); el cargo único de Brasil (US$619 millones, 3T25) ya salió de la ventana LTM. Entre las distorsiones contables, la amortización acelerada del contenido adelanta costos, los arrendamientos operativos (US$2.252 millones) no están en la deuda financiera y el Modelo JMR los suma y la compensación en acciones (US$540 millones en el LTM) es baja. No se calcula precio objetivo.

- **Veredicto:** Favorable.
- **Encaje:** Encaja.
- **Tres evidencias:** (1) EBIT sobre capital invertido de ~42% antes de impuestos; (2) margen operativo de 31,3% en el LTM, ya sin el cargo de Brasil; (3) capex de 1,9% de los ingresos LTM.
- **Principal objeción:** el activo principal, el contenido, no es un activo físico y su retorno depende de que cada título atraiga audiencia.
- **Pregunta pendiente:** ¿cuál es el ROIC incremental de la inversión en contenido deportivo frente a la de series originales?

## 14. Noticias y eventos recientes

Los acontecimientos cubren los 90 días anteriores al corte de mercado del 30 de septiembre de 2026 (2 de julio a 30 de septiembre) y los informes del 3T26 publicados después, que esta revisión sí incorpora a los estados. Las fuentes son todos los 8-K y 10-Q de la SEC desde el 1 de julio de 2026: cuatro 8-K (16, 22 y 30 de julio y 20 de octubre) y dos 10-Q (17 de julio y 21 de octubre), según la consulta a EDGAR del 25 de octubre de 2026. La guía del 4T26 es un hecho posterior y se trata como tal.

| Fecha | Acontecimiento verificado | Importancia para la tesis | Impacto positivo/neutral/negativo | ¿Cambia la tesis? | Fuente |
|---|---|---|---|---|---|
| 16 de julio de 2026 | Resultados del 2T26: ingresos de US$12.560 M (+13,4%) y margen operativo de 33,4%. Guía del 3T26: ingresos de US$12.860 M y margen de 33,2%. Guía de 2026: US$51.000-51.400 M, margen de 31,5% y flujo libre de ~US$12.500 M | Fija la trayectoria de 2026 | Neutral | No | [Netflix, carta a accionistas del 2T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000211/ex991_q226.htm) |
| 16 de julio de 2026 | Netflix pasará a publicar el informe de horas vistas una vez al año desde 2027; el 1S26 mostró 97.000 M de horas (+2%) | Reduce la visibilidad del uso, variable central de la tesis | Negativo | No cambia las historias, pero eleva la prioridad de vigilar el uso | Ídem |
| 16 de julio de 2026 | Alzas de precio del primer semestre en Estados Unidos, México y España con efecto «consistente con las expectativas» | Respalda el poder de precios de la Base | Positivo | No | Ídem |
| 17 de julio de 2026 | Presentación del 10-Q del 2T26, con balance, flujo y recompras de US$4.714 M en el trimestre | Confirma la comisión de WBD cobrada en el 1T26 | Neutral | No | [Netflix, 10-Q del 2T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000212/nflx-20260630.htm) |
| 22 de julio de 2026 | Emisión de US$1.000 M de notas senior al 5,250% con vencimiento en 2036, para repagar las notas al 4,375% de noviembre de 2026 | Refinancia sin aumentar la deuda neta; costo mayor | Neutral | No | [Netflix, 8-K del 22 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1065280/000119312526312575/d171951d8k.htm) |
| 30 de julio de 2026 | Renuncia de la directora Anne Sweeney al consejo, sin discrepancias con la compañía | Reduce el consejo a once directores | Neutral | No | [Netflix, 8-K del 30 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000214/nflx-20260726.htm) |
| 17 de julio de 2026 y días siguientes | Caída de la acción de hasta 8,7% en la sesión posterior a la guía, según cobertura secundaria; el mercado esperaba ~US$13.000 M de ingresos del 3T26 | Mide la expectativa del mercado; no cambia fundamentos | Negativo | No | [Capital.com](https://capital.com/en-gb/analysis/netflix-stock-forecast); [ii.co.uk](https://www.ii.co.uk/analysis-commentary/ii-view-weak-netflix-guidance-food-bears-ii539695) |
| 20 de octubre de 2026 | Resultados del 3T26: ingresos de US$12.874 M (+11,8%) y margen de 34,6%; recompras de US$4.800 M (63,9 M de acciones); flujo libre de ~US$2.900 M; publicidad de 2026 rebajada a ~US$2.700 M y flujo libre de 2026 a ~US$12.000 M; guía de 2026 de US$51.100 M (+13%) y margen de 31,5%; nueva licencia con Disney | Ancla el año 1 de las historias y confirma el margen; la rebaja de publicidad debilita la Optimista | Neutral con sesgo negativo para la publicidad | No: confirma la Base y aumenta el peso de la evidencia contraria sobre la publicidad | [Netflix, carta a accionistas del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm) |
| 21 de octubre de 2026 | Presentación del 10-Q del 3T26: balance al 30-sep-2026 (caja e inversiones de US$8.223 M, notas de US$15.132 M, 4.106,33 M de acciones) | Es la base de datos de esta revisión (LTM octubre de 2025 a septiembre de 2026) | Neutral | No | [Netflix, 10-Q del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm) |

El hecho posterior que no entra en las historias es la guía del 4T26, publicada el 20 de octubre de 2026 en la [carta del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm): ingresos de US$13.400 M y margen de 26,0%, que incluye ~120 puntos básicos de reducciones de personal. Las historias ya la contemplan a través del margen guiado de 2026 (31,5%), y el año 1 del DCF (octubre de 2026 a septiembre de 2027) parte del margen LTM.

## 15. Qué vigilar

| Métrica o evento | Tesis asociada | Umbral favorable | Señal de alerta | Frecuencia | Próxima fecha conocida | Fuente del umbral |
|---|---|---|---|---|---|---|
| Crecimiento de ingresos (a/a) | Base y Optimista | ≥ +11% en 2027 | ≤ +9% | Trimestral | Resultados del 4T26 (enero de 2027) | Guía de 2026 de +13% y 3T26 de +11,8% |
| Margen operativo | Base | ≥ 34% en 2027 | ≤ 31,5% | Trimestral | Ídem | Guía de 31,5% para 2026, 3T26 de 34,6% y consenso de abril de ~34% para 2027 |
| Ingresos de publicidad | Base y Optimista | ≥ US$4.500 M en 2027 | Nueva rebaja de la meta o crecimiento < 40% | Trimestral | Cartas trimestrales | Meta de ~US$2.700 M en 2026, rebajada desde ~US$3.000 M |
| Horas vistas totales | Todas | ≥ +3% | ≤ +1% | Anual (informe de horas desde 2027) | Primer semestre de 2027 | 1S26 de +2% y 2025 de +1,5% |
| Participación en el tiempo de televisión en Estados Unidos | Conservadora y Disrupción | ≥ 8,3% | ≤ 7,0% | Mensual | Siguiente edición de Nielsen The Gauge | Junio de 2026: 7,9% frente a 8,3% el mes anterior |
| Relación gasto de contenido en efectivo / amortización | Base | ≤ 1,1 | ≥ 1,2 | Trimestral | Cartas trimestrales | Guía de ~1,1; adiciones / amortización de 1,14 en el LTM |
| Flujo libre | Base | ≥ US$12.000 M en 2026 y creciente | Caída con ingresos al alza | Trimestral | 4T26 | Guía de ~US$12.000 M en el 3T26 (antes ~US$12.500 M) |
| Recompras de acciones | Base | ≥ US$4.000 M por trimestre | Pausa por adquisiciones | Trimestral | 10-K 2026 | US$4.800 M en el 3T26; US$22.300 M de autorización |
| Tasa de crecimiento a moneda constante frente a reportado en LATAM | Todas | Brecha < 5 puntos | Brecha > 10 puntos | Trimestral | Cartas trimestrales | 2025: +11% reportado frente a +23% constante; 3T26: +17% frente a +12% |
| Impuestos no sobre la renta de Brasil | Conservadora | Sin cargos nuevos | Cargos adicionales > US$300 M | Trimestral | 10-K 2026 | Cargo de US$619 M del 3T25 |

## 16. Preguntas abiertas

Con los documentos disponibles se resolvieron tres cuestiones:
- La comisión de WBD se cobró en el 1T26 por US$2.800 millones ([10-Q del 2T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000212/nflx-20260630.htm), nota 6).
- El vencimiento de noviembre de 2026 se refinanció con la emisión de julio ([8-K del 22 de julio de 2026](https://www.sec.gov/Archives/edgar/data/1065280/000119312526312575/d171951d8k.htm)).
- La publicidad de 2026 se guía ahora en ~US$2.700 millones ([carta del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm)).

Quedan abiertas:

| Pregunta | Por qué importa | Evidencia disponible | Dato faltante | Respuesta que fortalecería/debilitaría la tesis |
|---|---|---|---|---|
| ¿Cuál es la retención por plan y región tras las alzas de 2026? | Define si el precio puede seguir siendo la palanca de crecimiento | La empresa dice que el efecto es «consistente con alzas anteriores» | Churn por plan y región; no se publica | Retención estable fortalece la Base; un deterioro la lleva a la Conservadora |
| ¿Por qué se rebajó la meta de publicidad de 2026 y qué margen incremental tiene cada dólar de publicidad? | Sostiene el margen objetivo de 36% y la Optimista | Ingresos de ~US$2.700 M guiados; sin margen publicitario | Costo de ventas y de tecnología publicitaria; desglose de la rebaja entre precio por impresión y volumen | Un margen incremental > 50% y una rebaja por volumen temporal fortalecen la tesis |
| ¿Qué parte del gasto de contenido mantiene la audiencia actual? | Determina el ventas/capital y el ROIC marginal | Adiciones de US$19.991 M frente a amortización de US$17.529 M (LTM) | Distribución por tipo de título | Un mantenimiento bajo fortalece el ventas/capital de la Base |
| ¿Cuánto cuesta ampliar el deporte en vivo? | Es el principal riesgo de costo para el margen | ~5% del gasto de contenido en 2026 y ~1% de las horas | Contratos y plazos de la NFL, WWE y otros | Un costo incremental menor que las altas de miembros fortalece la tesis |
| ¿Cuál es el criterio de capital ante una nueva operación grande? | Cambia el perfil de riesgo y las recompras | Oferta por WBD de US$27,75 por acción y comisión de US$2.800 M | Reglas internas de apalancamiento y de recompra | Un compromiso explícito con recompras y deuda baja fortalece la tesis |
| ¿Qué parte del crecimiento de horas viene de contenido de terceros y de creadores? | Mide si la oferta ampliada (TF1, Disney, creadores, podcasts) sube el uso | Horas de TF1 «crecientes cada semana» | Horas por tipo de contenido | Un aumento de horas por miembro fortalece la tesis |
| ¿Cuánto ahorra la reducción de personal del 4T26? | Afecta el margen de 2027 frente al 36% de la Base | Cargo de ~120 pb en el 4T26 | Ahorro anual y plazo | Un ahorro ≥ 1 pp de margen en 2027 fortalece la Base |

## 17. Fuentes

### Fuentes primarias

- **Annual Report on Form 10-K 2025**, Netflix, Inc., 23 de enero de 2026, consultado el 21 de octubre de 2026. [Enlace directo](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm).
- **Quarterly Report on Form 10-Q del 3T26**, Netflix, Inc., 21 de octubre de 2026, consultado el 25 de octubre de 2026; base de los estados y del LTM de esta revisión. [Enlace directo](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm).
- **Quarterly Report on Form 10-Q del 3T25**, Netflix, Inc., 22 de octubre de 2025, consultado el 25 de octubre de 2026; nueve meses de 2025 para el LTM. [Enlace directo](https://www.sec.gov/Archives/edgar/data/1065280/000106528025000406/nflx-20250930.htm).
- **Instancias XBRL de los 10-K 2016-2025 y de los 10-Q del 3T25 y del 3T26**, SEC EDGAR, consultadas el 25 de octubre de 2026; 31.213 hechos con hash por archivo y 20 derivaciones verificadas contra la instancia citada (`reference/revisiones/NFLX-2026-10-25/NFLX_derivation_audit.json`).
- **Quarterly Report on Form 10-Q del 2T26**, Netflix, Inc., 17 de julio de 2026, consultado el 21 de octubre de 2026. [Enlace directo](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000212/nflx-20260630.htm).
- **Carta a accionistas del 2T26 (anexo 99.1 del 8-K del 16 de julio de 2026)**, Netflix, Inc., consultado el 21 de octubre de 2026. [Enlace directo](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000211/ex991_q226.htm).
- **Carta a accionistas del 3T26 (anexo 99.1 del 8-K del 20 de octubre de 2026)**, Netflix, Inc., consultada el 25 de octubre de 2026; el 3T26 entra en los estados de esta revisión y la guía del 4T26 se trata como hecho posterior. [Enlace directo](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm).
- **8-K del 5 de diciembre de 2025 (acuerdo de fusión con WBD)**, Netflix, Inc., consultado el 21 de octubre de 2026. [Enlace directo](https://www.sec.gov/Archives/edgar/data/1065280/000119312525308651/d65144d8k.htm).
- **8-K del 22 de diciembre de 2025 (financiación comprometida)**, Netflix, Inc., consultado el 21 de octubre de 2026. [Enlace directo](https://www.sec.gov/Archives/edgar/data/1065280/000119312525327462/d82688d8k.htm).
- **8-K del 20 de enero de 2026 (fusión enmendada, todo en efectivo)**, Netflix, Inc., consultado el 21 de octubre de 2026. [Enlace directo](https://www.sec.gov/Archives/edgar/data/1065280/000119312526015951/d37713d8k.htm).
- **8-K del 27 de febrero de 2026 (terminación)**, Netflix, Inc., consultado el 21 de octubre de 2026. [Enlace directo](https://www.sec.gov/Archives/edgar/data/1065280/000119312526082247/d120618d8k.htm).
- **8-K del 5 de junio de 2026 (junta anual y presidente del consejo)**, Netflix, Inc., consultado el 21 de octubre de 2026. [Enlace directo](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000189/nflx-20260604.htm).
- **8-K del 22 de julio de 2026 (notas a 2036)**, Netflix, Inc., consultado el 21 de octubre de 2026. [Enlace directo](https://www.sec.gov/Archives/edgar/data/1065280/000119312526312575/d171951d8k.htm).
- **8-K del 30 de julio de 2026 (renuncia de directora)**, Netflix, Inc., consultado el 21 de octubre de 2026. [Enlace directo](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000214/nflx-20260726.htm).
- **Company facts XBRL de Netflix y de Discovery, Inc.**, SEC, consultados el 21 de octubre de 2026. [Netflix](https://data.sec.gov/api/xbrl/companyfacts/CIK0001065280.json); [Discovery](https://data.sec.gov/api/xbrl/companyfacts/CIK0001437107.json).

### Fuentes secundarias y sectoriales

- **Streaming Climbs To 48.5%, Per Last Lame Duck Edition Of Nielsen's «Gauge»**, MediaPost, julio de 2026, consultado el 21 de octubre de 2026; se usa porque Nielsen no publica la edición completa en abierto. [Enlace directo](https://www.mediapost.com/publications/article/417308/).
- **The Gauge Polonia, agosto de 2026**, Nielsen, consultado el 21 de octubre de 2026. [Enlace directo](https://www.nielsen.com/news-center/2026/the-gauge-poland-august-2026/).
- **Nielsen Gauge**, PPC Land, consultado el 21 de octubre de 2026; fuente secundaria del dato de julio de 2026 de YouTube. [Enlace directo](https://ppc.land/nielsen-gauge/).
- **Netflix stock forecast**, Capital.com, consultado el 21 de octubre de 2026; cobertura secundaria de la reacción de la acción y de los objetivos de analistas tras el 2T26. [Enlace directo](https://capital.com/en-gb/analysis/netflix-stock-forecast).
- **ii view: weak Netflix guidance is food for bears**, Interactive Investor, consultado el 21 de octubre de 2026. [Enlace directo](https://www.ii.co.uk/analysis-commentary/ii-view-weak-netflix-guidance-food-bears-ii539695).
- **Netflix earnings preview Q2 2026**, S&P Global Market Intelligence, julio de 2026 (consenso de ingresos y margen de 2026), consultado el 21 de octubre de 2026. [Enlace directo](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/07/netflix-earnings-preview-q2-2026).
- **Netflix earnings preview Q1 2026**, S&P Global Market Intelligence con datos de Visible Alpha, abril de 2026 (consenso de margen de ~34% para 2027), consultado el 21 de octubre de 2026. [Enlace directo](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/04/netflix-earnings-preview-q1-2026).
- **Betas por industria, enero de 2026, y prima de riesgo implícita de octubre de 2026**, Aswath Damodaran, Stern School, consultados el 21 de octubre de 2026. [Betas](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html); [ERP](https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx).
- **FRED, DGS10 (Treasury a 10 años)**, al 30 de septiembre de 2026 (5,29%), consultado el 25 de octubre de 2026. [Enlace directo](https://fred.stlouisfed.org/series/DGS10).
- **The Base Rate Book**, Mauboussin y Callahan, Credit Suisse, 2016. [Enlace directo](https://www.credit-suisse.com/media/assets/corporate/docs/about-us/research/publications/the-base-rate-book-integrating-the-past-to-better-anticipate-the-future.pdf).
- **Cotizaciones y datos de pares (DIS, SPOT, ROKU, CMCSA, GOOGL)**, Yahoo Finance (auto_adjust=False), al 30 de septiembre de 2026, consultadas el 25 de octubre de 2026; también GOOGL como par de los múltiplos. [DIS](https://finance.yahoo.com/quote/DIS/); [SPOT](https://finance.yahoo.com/quote/SPOT/); [ROKU](https://finance.yahoo.com/quote/ROKU/).
- **Hoja del Modelo JMR de esta revisión**, «Modelo JMR - NFLX - copia IA 2026-10-25 - revisión SEC cerrada - NO PUBLICAR», copia nueva de la plantilla IA oficial (que no se modificó), [enlace](https://docs.google.com/spreadsheets/d/1ZPNMHxc7m3Iv60mdGspgi6-cc2zwf5kZ4ocsuANQUNM/edit), foto de resultados del 25 de octubre de 2026 (sha256 `6afa5b6aba533dcbd28143ba547eb3c98de1b541d5695a9a0e6351a2a06e58d5`).
- **Archivos de la revisión `NFLX-2026-10-25`**, `reference/revisiones/NFLX-2026-10-25/`: snapshot SEC conciliado, plan e importación verificada, entradas del analista con respaldo, foto de resultados, DCF inverso, sensibilidades de un supuesto, múltiplos por ciclo y complementarios y métricas históricas.
- **Versión anterior archivada**: análisis del 21 de octubre de 2026 (LTM a junio de 2026) sobre la hoja «prueba integral plantilla IA 2026-10-21»; sigue siendo la versión publicada hasta que se autorice esta revisión; al publicarla se archiva en `reference/archivo/NFLX_previas_2026-10-25/`. No es fuente de cifras de esta revisión.

## 18. Control de calidad final

| Sección | ¿Presente y completa? | Comprobación |
|---|---|---|
| 1. Resumen ejecutivo | Sí | Cuatro párrafos, ocho viñetas, dos variables clave, evidencia contraria e invalidación; LTM a septiembre de 2026 |
| 2. Modelo de negocio | Sí | Tabla y siete dimensiones económicas; actualizada con el 3T26 sin recortar |
| 3. Segmentos y geografía | Sí | Mezcla LTM a septiembre de 2026, monedas, concentración y comparabilidad; Netflix tiene un solo segmento y no publica beneficio por región |
| 4. Industria y crecimiento | Sí | Mercado, límites y encabezado literal «Las 5 fuerzas de Porter», con cinco filas |
| 5. Calidad del negocio | Sí | Tres estados, ratios con definiciones de la revisión y auditoría JMR sobre la hoja nueva; cobertura completa con limitación: Netflix no separa cuentas por cobrar, por lo que la prueba ácida no se estima |
| 6. Ventaja competitiva | Sí | Evidencia, duración, contraevidencia y retorno incremental 2022→LTM (2,66) |
| 7. Competencia | Sí | Seis rivales y sustitutos |
| 8. Gestión y asignación de capital | Sí | Gobierno, incentivos y seis usos de capital; cobertura completa con limitación: el proxy de 2026 no se revisó |
| 9. Catalizadores | Sí | Ocho con horizonte y confirmación; el 3T26 ya no es catalizador porque está en los estados |
| 10. Riesgos | Sí | Ocho riesgos, escenarios con los supuestos vigentes de la hoja y FODA |
| 11. Bulls say / Bears say | Sí | Siete argumentos por lado, conclusión cualitativa y «Síntesis final» explícita |
| 12. Valor con criterio Damodaran | Sí | Historia y filtro, tasas base del tamaño, justificación de supuestos con sensibilidades de la réplica verificada, piezas del valor, ROIC terminal con la decisión del usuario, trayectorias y puentes generados de la foto, cuatro historias con probabilidades, DCF Base y promedio de tres historias, pre-mortem, indicadores, precio solo al final con DCF inverso y registro de decisión |
| 13. Filosofías de inversión | Sí | Cinco marcos con formato completo e independiente, cifras al LTM de septiembre |
| 14. Noticias y eventos recientes | Sí | 90 días previos al corte más los informes del 3T26; lista completa de 8-K y 10-Q desde el 1-jul-2026 según EDGAR; guía del 4T26 como hecho posterior |
| 15. Qué vigilar | Sí | Diez indicadores con umbrales |
| 16. Preguntas abiertas | Sí | Siete preguntas específicas |
| 17. Fuentes | Sí | Primarias de la SEC con fecha de consulta, secundarias y archivos de la revisión |
| 18. Control de calidad final | Sí | Esta tabla |

| Control de la revisión | Resultado |
|---|---|
| Mismo `revision_id` y datos que la valoración y la auditoría | `NFLX-2026-10-25`; foto sha256 `6afa5b6aba533dcbd28143ba547eb3c98de1b541d5695a9a0e6351a2a06e58d5` |
| Cifras de valoración = hoja | DCF Base 70,85; Conservadora 53,22; Optimista 89,28; Disrupción 23,11; promedio 71,05; MOS 46,05 |
| Extracción SEC | 28/28 identidades, LTM PASS, cobertura PASS, 20/20 derivaciones verificadas, 46 contextos materiales adjudicados, 0 sin revisar |
| Secciones del 21-oct conservadas | 2, 4, 6, 7, 8, 10, 11 y 13, con reemplazos verificados (cada texto reemplazado debía aparecer exactamente una vez) |
| AISLAMIENTO | OK: sin cifras ni textos de otra empresa ni de la valoración NFLX anterior; los pares aparecen solo como comparables declarados |
| Estado | Auditoría independiente de la misma revisión: VERIFICADO con salvedades no bloqueantes (`data/NFLX_Auditoria_Valoracion_2026-10-25.md`); no publicada sin autorización del usuario |
