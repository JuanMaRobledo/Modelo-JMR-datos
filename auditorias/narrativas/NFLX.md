# Auditoría económica narrativa — Netflix, Inc. (NFLX)

> **23-oct-2026 · Reglas JMR v5 · Auditoría independiente del análisis ampliado**
> **Valor intrínseco base: US$69,94 (DCF FCFF)** · **Estado: CON HALLAZGOS ECONÓMICOS**
> Identificador financiero: NFLX-2026-10-22-SEC9M26-JMR-review-001. Identificador editorial conjunto: NFLX-2026-10-23-V5-FULL-ANALYSIS-AUDIT-001.
> Corte SEC 30-sep-2026; precio histórico del análisis US$65,04 del 21-oct-2026, no cotización actual.

### Actualización operativa verificable — 23-oct-2026

**Respuesta de la auditoría: SÍ, es posible valorar NFLX con salvedades y publicar una estimación de valor intrínseco; NO es correcto certificar como exhaustiva la extracción SEC nueva ni presentar US$69,94 como valor indiscutible.** Esta es una valoración para investigación financiera propia, con hipótesis explícitas, no una opinión de auditoría financiera externa. El DCF FCFF Base y su identificador financiero se mantienen sin cambios; este apéndice corrige el registro de limitaciones técnicas y de publicación.

| Componente | Evidencia contrastada | Situación y tratamiento |
|---|---|---|
| 10-Q SEC a septiembre 2026 | Fuente primaria publicada; activos de contenido netos US$34.605,48 M, deuda y acciones observables | **Apto como fuente primaria**, cotejando cada concepto utilizado con contexto, corte, unidad y escala |
| Valoración existente | DCF Base US$69,94; escenario ROIC terminal=WACC US$56,08; MOS 35% US$45,46 | **Utilizable con salvedades económicas**; valor central no equivale a certeza |
| Historias de crecimiento | 20 valores de crecimiento de los años 1–5 coinciden con la corrida JMR; supuestos editables, no forzar fórmulas artificiales | Corregida la clasificación de entradas manuales en el detector de integridad |
| Controles de archivos de auditoría | Catálogo público excluye archivos históricos; workflow «Control JMR de ponderaciones» ha pasado | Incidencia de inventario **resuelta**, separada de la exactitud económica |
| Nuevo extractor SEC — PR JMR-valuation #137 | 22 pruebas aisladas aprobadas; caché enlazada a SHA-256 y URL de origen; bloqueos de faltantes y conflictos | **No integrado ni probado como importación completa a Sheets**. No emplear su resultado como certificación financiera |
| Cobertura del extractor nuevo | 294 combinaciones partida/período sin valor en el expediente previo | **Pendiente de clasificar por materialidad y fuente**: no son 294 errores demostrados de la valoración vigente ni pueden llenarse con ceros |
| Control integral NFLX | Ejecuciones del release gate han fallado por detecciones de entradas legítimas o rótulos; detector corregido para números fijos documentados y para excluir textos | Exigir corrida íntegra verde **sobre la versión exacta** antes de certificar una nueva liberación financiera |
| Análisis fundamental editorial | 25 puntos de control: 18 sustentados, siete limitados por evidencia | Se puede publicar como **análisis completo en estructura y honesto en límites**, no como cobertura documental absoluta |

**Salvedades económicas que permanecen abiertas, ordenadas por su posible efecto:** (1) demostrar la persistencia del ROIC terminal 21,52% frente al WACC 9,16% y la industria 11,04%; (2) verificar que Sales-to-Capital Base 2,00x y la reinversión neta representen realmente el costo de renovación y monetización del contenido; (3) recalcular y justificar pares y anclas de los siete múltiplos, en particular EV/FCFF, P/FCFE y tratamiento del EBITDA de contenido; (4) atribuir la prima país extra de 0,50 puntos porcentuales y el costo de deuda a fuentes y exposición geográfica; (5) normalizar el cobro extraordinario WBD de US$2.800 M y confirmar el impuesto aplicable; (6) comprobar opciones/SBC, arrendamientos, acciones promedio ajustadas por split y efecto neto de recompras; (7) recuperar proxy e incentivos de directivos, TAM geográfico monetizable, cohortes/retención y publicidad comparables, si la información pública existe.

**Criterio operativo de publicación:** el registro de valoración existente puede mostrarse y utilizarse con estas advertencias porque su hipótesis base es explícita y reproducible. **No debe sustituirse por un recálculo procedente del extractor nuevo** hasta confirmar cobertura material, preservación de fórmulas y validaciones de Sheets, DCF, múltiplos y control integral. Un problema de CI no prueba por sí solo un DCF incorrecto; un CI verde tampoco demuestra que todos los supuestos económicos sean plausibles. La incertidumbre se muestra en la auditoría, no se oculta ni se convierte en datos inventados.

**Fuentes y trazabilidad de esta actualización:** [SEC 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm), [carta Q3 2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm), [PR #137](https://github.com/JuanMaRobledo/JMR-valuation/pull/137), [pruebas SEC aprobadas](https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/40017974176), [workflow de liberación](https://github.com/JuanMaRobledo/JMR-valuation/actions/workflows/nflx-final-gate-20261022.yml). Revisión financiera: `NFLX-2026-10-22-SEC9M26-JMR-review-001`; revisión editorial original v5 preservada. Actualización limitada a auditoría y controles, sin modificación del DCF.

## 1. Ficha de auditoría y alcance

Emisor: Netflix, Inc. (NFLX, NASDAQ), servicio de entretenimiento y publicidad, USD, millones USD salvo valor por acción. Método intrínseco: FCFF descontado a WACC. Corte financiero: 30-sep-2026, diez años FY2016–2025 más LTM; valoración económica del 22-oct-2026 y revisión editorial del 23-oct-2026. Precio de análisis histórico: US$65,04, 21-oct-2026, no una cotización vigente.

Revisión financiera inalterada: NFLX-2026-10-22-SEC9M26-JMR-review-001. Revisión editorial común a análisis/auditoría: NFLX-2026-10-23-V5-FULL-ANALYSIS-AUDIT-001. Hojas y datos: https://docs.google.com/spreadsheets/d/11yN171o8R61n4RhZnmuZuiSyIn_DGkfTmjo7wMKqaZI/edit. Datos primarios: [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm), [10-K 2025](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm), [carta a accionistas Q3](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm). Reglas v5, 23-oct-2026, §9. Se leyó el artículo ampliado de Nivel1, su Nivel2 y el JSON de valoración antes de escribir esta auditoría.

**Estado inicial: CON HALLAZGOS** sobre sustento económico y límites de evidencia. No significa que el DCF sea aritméticamente erróneo. Esta es auditoría económica crítica, no auditoría financiera externa, y no introduce cambios en fórmulas, cálculos ni supuestos oficiales.

## 2. Resumen ejecutivo y relato económico central

Netflix monetiza una base internacional recurrente con suscripciones, precios, publicidad y contenido original o licenciado. La escala permite distribuir costos tecnológicos y creativos, pero el contenido requiere efectivo anticipado y renovación. El crecimiento observado desde FY2016, cuando EBIT era 4,30% de ingresos, hasta el 29,49% FY2025 y 31,30% LTM septiembre-2026 apoya una ventaja operativa tangible.

La compañía guió FY2026 a US$51.100 millones de ingresos, crecimiento +13% y margen EBIT 31,5%. Q3 presentó margen 34,6% favorecido por calendario de gastos; no es prueba de margen estable. También recortó previsión publicitaria de aproximadamente US$3.000 a US$2.700 millones por retrasos del producto. La tesis Base exige pricing y publicidad suficientes para conseguir EBIT36% en año5 sin aumentar desproporcionadamente pagos por contenido.

La principal incertidumbre es cuánto tiempo Netflix podrá obtener un ROIC terminal21,52%, por encima del 11,04% de referencia Entertainment y del WACC9,16%. Ese foso explica buena parte del valor terminal. El supuesto se defiende con marca, escala y distribución, pero se enfrenta a YouTube, videos gratuitos, grandes estudios, ligas deportivas y una oferta de contenido que exige capital recurrente.

**Lectura favorable:** crece publicidad y eficiencia sin deteriorar retención. **Lectura neutral:** Netflix conserva escala y caja pero el ROIC tiende a nivel sectorial. **Contratesis:** el precio pierde elasticidad, sube gasto de contenido y competencia erosiona el retorno marginal. Las tres deben medirse, no seleccionarse en función del precio objetivo.

## 3. Trazabilidad, integridad y jerarquía de evidencia

| Concepto | Dato y fecha | Fuente y ubicación | Control |
|---|---:|---|---|
| Ingresos 2025 | US$45.183,04 M | [10-K 2025](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm), Income Statement FY25 | Comprobado |
| EBIT 2025 | US$13.326,60 M | 10-K 2025 / Income Statement FY25 | Comprobado |
| Ingresos LTM sep-26 | US$49.734,63 M | [10-Q sep-26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm), FY25+9M26−9M25 | Comprobado |
| EBIT LTM sep-26 | US$15.564,87 M | 10-Q y hoja, GAAP | Comprobado |
| CFO LTM | US$12.307,94 M | Cash Flow Statement | Incluye WBD |
| CAPEX PPE LTM | US$932,88 M de salida | Cash Flow Statement | No es toda la reinversión económica |
| Comisión WBD | US$2.800 M | 10-Q nota 6, 1T26, bajo EBIT | No recurrente |
| Caja+inversiones | US$8.222,95 M | Balance 30-sep-26 | Modelo frente a SEC |
| Deuda económica DCF | US$15.158 M | Puente EV-equity; deuda SEC nota7 | Valor aproximado sujeto a ajustes |
| Contenido neto | US$34.605,48 M | 10-Q nota5 | Verificado |
| Compromisos contenido | US$25.222,80 M | 10-Q nota9 | US$19.600 M aún no reconocidos |
| WACC/Ke | 9,16% / 9,44% | Hoja WACC y Damodaran referencia | Reconstrucción interna, no certificación CRP |
| Precio histórico | US$65,04 | Expediente 21-oct-26 | No cotización actual |

El LTM no corresponde a diciembre-2025 ni a junio-2026. Es la suma del ejercicio 2025 y nueve meses de 2026 menos los nueve meses comparables de 2025. El ingreso extraordinario WBD se registra en interés y otros, debajo del EBIT, y la caja operativa incorpora la entrada; no se puede tratar como flujo recurrente.

Se preservaron cifras históricas y no se construyeron peers inexistentes. La valoración de opciones y asignación de deuda entre tramos contiene juicios; el detalle fiscal de la comisión WBD no quedó certificado de manera independiente.

## 4. Historia financiera: diez años y punto de partida

| Año | Ventas USD M | EBIT USD M | Margen EBIT |
|---|---:|---:|---:|
| 2016 | 8.830,67 | 379,79 | 4,30% |
| 2017 | 11.692,71 | 838,68 | 7,17% |
| 2018 | 15.794,34 | 1.605,23 | 10,16% |
| 2019 | 20.156,45 | 2.604,25 | 12,92% |
| 2020 | 24.996,06 | 4.585,29 | 18,34% |
| 2021 | 29.697,84 | 6.194,51 | 20,86% |
| 2022 | 31.615,55 | 5.632,83 | 17,82% |
| 2023 | 33.723,30 | 6.954,00 | 20,62% |
| 2024 | 39.000,97 | 10.417,61 | 26,71% |
| 2025 | 45.183,04 | 13.326,60 | 29,49% |
| LTM 30-sep-26 | 49.734,63 | 15.564,87 | 31,30% |

Ingresos CAGR de 2016 a 2025: aproximadamente 19,89%; de 2020 a 2025: 12,57%; de 2022 a 2025: 12,64%. El margen tuvo contracción significativa en 2022, por lo que no procede extrapolar una línea recta hasta perpetuidad. El crecimiento del decenio mezcla lanzamiento internacional y madurez; la Base 9,99% CAGR a cinco años no debe compararse con una fase de penetración equivalente.

CFO 2019 −US$2.887 M, FY2023 US$7.274 M, FY2025 US$10.149 M y LTM US$12.308 M. El FCF CFO−CAPEX mejoró, pero parte del LTM incluye US$2.800 M de cobro WBD y la inversión en contenido pasa por pagos y obligaciones ajenos al CAPEX PPE. En sep-26 la obligación contractual por contenido ascendía a US$25.223 M y el activo neto US$34.605 M.

ROIC contable LTM 38,58% con capital medio frente a 35,87% con saldo final: distintas convenciones, no necesariamente incongruentes. ROIC de nuevos proyectos y ROIC económico ajustado por contenido siguen limitados por datos.

## 5. Crecimiento de ingresos: de la historia a la proyección

La Base proyecta crecimiento anual 12%, 11%, 10%, 9% y 8% en los cinco primeros años, CAGR geométrico 9,99%. De 2022 a 2025 las ventas habían crecido ~12,64% compuesto, mientras la guía FY2026 era +13%; el año uno es plausible pero no garantizado. Los incrementos deben venir de precio, miembros, FX neutral, mezcla de planes y anuncios; la nueva publicidad no puede justificar simultáneamente todo el crecimiento y todos los márgenes.
**Seis preguntas sobre crecimiento:**

1. **Valor y ubicación.** Escenarios e historias C29:G29, 12/11/10/9/8%, CAGR9,99%, años6–10 desaceleración.
2. **Historia y pares.** CAGR histórico 9a19,89%; 5a12,57%; 3a12,64%; LTM+14,65%; guía FY2026 +13%.
3. **Causa económica.** Precio, distribución, anuncios y penetración remanente incrementan ingresos por hora/miembro.
4. **Hechos que exige.** Mantener engagement y traducir ads en crecimiento real sin gasto proporcional de contenido.
5. **Evidencia que lo refutaría.** Ingresos FX neutrales sostenidos por debajo del 8%, churn mayor y nueva rebaja ads.
6. **Impacto sobre valor.** Menos ventas reducen EBIT y FCFF; la sensibilidad crecimiento×margen es el examen cuantitativo obligatorio, no se inventa un delta aislado.


| Métrica y horizonte | Histórico | Modelo | Fuente externa | Causalidad y condición | Refutador | Prueba |
|---|---|---|---|---|---|---|
| Crecimiento FY+1 | guía FY2026+13% | 12% | Carta Q3 | Pricing+ads | FX neutral <8% por dos cortes | Matriz ingresos×EBIT |
| CAGR 1–5 | 5 años a 2025 ~12,57% | 9,99% | SEC 10-K/Q | Maduración con expansión internacional | Ads/miembros no sostienen crecimiento | DCF inverso8,19% |
| Crecimiento Conservadora | FY2022–23 6–7% | CAGR5,00% | SEC | Saturación y menor monetización | Ads se recupera >meta | DCF45,02 |
| Crecimiento Optimista | FY2025 +15,85% | CAGR11,58% | SEC | Publicidad y pricing sin churn | Retrasos comerciales persisten | DCF93,00 |

Dictamen: crecimiento central razonable como juicio, sin recorte duplicado por cautela. El descenso de guía de publicidad ya justifica el ajuste de probabilidad desde Optimista hacia Conservadora.

## 6. Márgenes operativos y normalización de beneficios

El EBIT GAAP de Netflix FY2025 29,49% sobre ingresos y LTM sep-26 31,30% no debe confundirse con el 34,6% del Q3 influido por calendario de costos. La guía FY2026 31,5% ancla mejor el primer año. El salto a 36% en cinco años supone productividad del catálogo, menor costo relativo de distribución y monetización publicitaria con margenes incrementales suficientemente altos.
**Seis preguntas sobre margen EBIT:**

1. **Valor y ubicación.** Base año1 ~32%, objetivo año5 36% (Escenarios D5); Conservadora32,5%, Optimista40%, Disrupción18%.
2. **Historia y pares.** Márgenes FY2016 4,30%, FY2023 20,62%, FY2024 26,71%, FY2025 29,49%, LTM31,30%.
3. **Causa económica.** Catálogo reproducible y publicidad distribuyen costos fijos sobre nuevas ventas.
4. **Hechos que exige.** No elevar compensaciones, licencias y marketing más rápido que ingresos.
5. **Evidencia que lo refutaría.** Deterioro de retención con precio y costo por derecho deportivo creciente.
6. **Impacto sobre valor.** EBIT=ingresos×margen, cambia impuestos, NOPAT y FCFF. Sensibilidad crecimiento×margen disponible en hoja.


Un punto contable crucial: la comisión de cancelación WBD de US$2.800 M en primer trimestre 2026 se reconoció bajo EBIT y también en CFO; no explica expansión del margen operativo, pero sí distorsiona EPS y OCF. La normalización usada para P/E ajusta impuesto a 25% como hipótesis. Sin confirmar carga fiscal específica no se certifica la rentabilidad neta recurrente.

EV/EBITDA es especialmente delicado porque el contenido se capitaliza y amortiza; comparar un EBITDA que añade amortización de contenidos con otro que no la añade impide comparar múltiplos. Su peso cero en el modelo es defendible.

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

Ventas/capital marginal no es rotación contable de activos. Es el ingreso incremental por reinversión económica proyectada y determina reinversión = Δingresos / Sales-to-Capital. El período 2022–25 arroja 4,57x, 2023–LTM ~1,95x y 2025–LTM ~1,09x. El enorme rango limita cualquier precisión falsa.
**Seis preguntas sobre ventas/capital:**

1. **Valor y ubicación.** Base E5=2,00x años1–5, F5=1,60x años6–10; Conservadora1,40→1,20; Optimista2,50→1,90.
2. **Historia y pares.** Datos incrementales 4,57/1,95/1,09x según ventana; sector1,39x referencia distinta.
3. **Causa económica.** Escala de distribución y contenido preexistente permite ventas nuevas con menor capital marginal.
4. **Hechos que exige.** La renovación de títulos no absorbe mayor caja que crecimiento y mantiene retorno incremental.
5. **Evidencia que lo refutaría.** Pagos de contenido/subscripciones o inventario de derechos aumentan más que ingresos.
6. **Impacto sobre valor.** S/C menor exige reinvertir más por cada USD de ventas; reduce FCFF y DCF; no simular impacto no calculado.


**Seis preguntas sobre ROIC terminal:**

1. **Valor y ubicación.** G5 / Input B50 =21,52% en historias ordinarias; Disrupción=WACC9,16%.
2. **Historia y pares.** ROIC LTM38,58% con capital promedio vs 35,87% con cierre, referencia industria11,04%, WACC9,16%.
3. **Causa económica.** Marca, datos, red de distribución y catálogo sostienen exceso de rentabilidad.
4. **Hechos que exige.** Demostrar retorno marginal elevado por otra década y margen36% maduro.
5. **Evidencia que lo refutaría.** Nuevos derechos consumen caja y rendimiento cae al nivel industrial/WACC.
6. **Impacto sobre valor.** Sensibilidad registrada: DCF Base69,94 vs ROIC=WACC56,08; caída13,86 por acción.


| Indicador de capital | Dato registrado | Lectura crítica |
|---|---|---|
| CAPEX PPE LTM | US$932,88 M | No representa todo el contenido. |
| Activos de contenido netos | US$34.605,48 M | Valor contable, distinto del costo económico de renovar. |
| Obligaciones por contenido | US$25.222,80 M | No todas son deuda financiera, sí compromisos de caja. |
| Recompras LTM | US$12.861 M | Reducen acciones/patrimonio; pueden elevar ratios contables. |
| ROIC terminal | 21,52% | Excepcional frente a referencia industrial; requiere prueba de moat. |

Problema de transición: con margen terminal de 36%, impuesto25% y S/C marginal1,60, el rendimiento incremental aproximado antes de terminal sería 43,2%, y el modelo cae abruptamente a ROIC estable21,52%. Puede justificarse por pérdida gradual del foso, pero faltan evidencias cuantificadas del trayecto, no es problema que se pueda cerrar con una nota genérica.

## 8. Costo del capital y riesgo

La tasa de descuento del modelo para FCFF es WACC9,16%; el Ke aplicado a equity y múltiplos es9,44%. El libro registra Rf USD ajustada4,91%, ERP efectiva4,42%, beta reapalancada~1,024 y Kd antes de impuestos5,85%. Son parámetros coherentes algebraicamente, pero un costo de capital reproducible por fórmula no es evidencia de que cada insumo esté bien elegido.
**Seis preguntas sobre WACC y Ke:**

1. **Valor y ubicación.** WACC9,1645%, Ke9,4355%; g4%, impuesto marginal25% en hoja.
2. **Historia y pares.** Referencias Damodaran/US Treasury del corte; la tasa genérica 8,99% de referencia no equivale al WACC Netflix.
3. **Causa económica.** Beta y prima por país resumen riesgo de renta variable y deuda financiera.
4. **Hechos que exige.** Misma fecha para Rf, ERP madura y la exposición geográfica; sin doble conteo de riesgos de flujo.
5. **Evidencia que lo refutaría.** CRP extra de 50pb sin reparto por países demostrado, costo deuda de mercado diferente.
6. **Impacto sobre valor.** Matriz WACC×g y sensibilidad CRP0/50/100pb registrada; no sustituye una nueva certificación.


**Hallazgo medio:** el CRP adicional0,50% es un juicio sin reconciliación verificable país por país; no se debe llamarlo prima Damodaran exacta por facturar internacionalmente. La beta, spreads y deuda deben actualizarse a un corte unificado. No se manipulan tasas para acercar el resultado al precio observado.

## 9. Convergencia y valor terminal

El g terminal de Base es 4,00% nominal USD y WACC9,16%, por lo que WACC>g. La reinversión de perpetuidad es NOPAT×g/ROIC y, con ROIC21,52%, consume aproximadamente18,59% del NOPAT. La fórmula no garantiza sostenibilidad del 21,52%; es una hipótesis de foso competitivo duradero.

**Seis preguntas sobre valor terminal:**

1. **Valor y ubicación.** g Base4%; ROIC21,52%; margen36% y tasa marginal25%, WACC9,16%; VP terminal≈US$184.991 M.
2. **Historia y pares.** FY2025 EBIT29,49%; LTM31,30%; referencia ROIC sector11,04%; inflación+PIB nominal USD de largo plazo.
3. **Causa económica.** Monetización de audiencia continúa tras diez años sin requerir inversión desproporcionada.
4. **Hechos que exige.** Renovar catálogo con ROIC superior al WACC y competencia contenida, sin cambio abrupto del modelo.
5. **Evidencia que lo refutaría.** Márgenes se estancan y ROIC converge a industria/WACC, gastos por derechos presionan.
6. **Impacto sobre valor.** ROIC=WACC reduce precio a ~US$56,08; PV terminal representa 61,96% del EV.


**Hallazgo de consistencia de reglas v5:** la historia Optimista usa g terminal4,5% y la regla general define 4% nominal USD. La Optimista no supera el Rf ajustado4,91%, pero su excepción requiere justificación expresa en la ficha de escenarios; no se corrige silenciosamente desde Auditoría. Conservadora usa g3%, Disrupción0%.

## 10. Validación independiente del valor intrínseco

El último JSON de valoración incluye un registro de reproducción independiente de **333 identidades** para las cuatro historias: ingresos, EBIT, NOPAT, reinversión, FCFF, factores de descuento, valor terminal y equity. Esta auditoría editorial comprobó salidas principales con la hoja, sin volver a ejecutar todas las 333 identidades ni una batería nueva de SEC.

| Concepto del DCF Base | US$ millones |
|---|---:|
| VP de diez años de FCFF | 113.569,66 |
| VP terminal | 184.991,41 |
| Valor operativo | 298.561,07 |
| Deuda económica | −15.158,00 |
| Caja | +8.222,95 |
| Valor de opciones/otras reclamaciones | −4.290,87 |
| Patrimonio común | 287.335,15 |
| Acciones millones | 4.108,19 |
| **DCF Base por acción** | **US$69,94** |

**Seis preguntas sobre valor intrínseco:**

1. **Valor y ubicación.** Valuation output Base US$69,94 hoy; valor de compra MOS35% US$45,46; precio histórico US$65,04.
2. **Historia y pares.** LTM SEC septiembre2026 y modelo JMR; ancla externa del precio no es cotización actual.
3. **Causa económica.** La escala genera FCFF sostenido, descontado a WACC, luego ajustado por deuda, caja, opciones y acciones.
4. **Hechos que exige.** Puente EV-equity evita doble conteo de leasing/deuda/opciones y las acciones económicas son correctas.
5. **Evidencia que lo refutaría.** Reclamaciones de opciones, SBC o arrendamientos distintas a las contabilizadas.
6. **Impacto sobre valor.** DCF inverso precio65,04 exige CAGR8,19%; no confundir con objetivo FY+3 US$83,43.


La cifra de múltiplos FY+3 US$83,43 es objetivo auxiliar 40% DCF/60% múltiplos en un horizonte distinto; no debe llamarse valor intrínseco Base. La pérdida por cruce de ROIC a WACC es una prueba de sensibilidad, no un forecast.

## 11. Cuatro historias y probabilidades

| Historia | CAGR años1–5 | Margen | S/C 1–5 / 6–10 | ROIC terminal | g terminal | DCF US$/acción | Probabilidad |
|---|---:|---:|---|---:|---:|---:|---:|
| Base | 9,99% | 36% | 2,00 / 1,60x | 21,52% | 4,0% | 69,94 | 45% |
| Conservadora | 5,00% | 32,5% | 1,40 / 1,20x | 21,52% | 3,0% | 45,02 | 27,5% |
| Optimista | 11,58% | 40% | 2,50 / 1,90x | 21,52% | 4,5% | 93,00 | 17,5% |
| Disrupción | −2,41% | 18% | 1,00 / 1,00x | WACC9,16% | 0% | 15,55 | 10% |

Probabilidad previa de crecimiento maduro 45/22,5/22,5/10%; la reducción de la meta ads de3.000 a2.700M trasladó5pp desde Optimista hacia Conservadora. Los pesos suman100%. El promedio de las tres ordinarias se renormaliza dividiendo por90% y resulta US$66,81; Disrupción retiene10% solo como dato y se expone en «¿Qué pasaría si todo fallara?», **no se promedia con los otros tres**.

Dos reservas persisten: Conservadora y Optimista comparten ROIC terminal21,52% a pesar de condiciones operativas tan diferentes; y Optimista usa g4,5% por encima del g central4%. No son errores de la aritmética publicada, sí hipótesis económicas que necesitan una historia más explícita antes de considerarse certificadas.

## 12. Valoración por múltiplos: prueba independiente y secundaria

La valoración de múltiplos es un método secundario. Debe corregirse el múltiplo histórico por diferencias de tasas y seleccionar cierre de ciclo semejante a los fundamentales FY+3, con tope al múltiplo justificado. Comparables que mezclan compañías de parques, redes, publicidad y plataformas no son homogéneos automáticamente.

| Método | Múltiplo Base aplicado | Peso entre múltiplos | VP/acción Base | Riesgo específico |
|---|---:|---:|---:|---|
| EV/EBITDA | 8,80x | 0% | 43,73 | Amortización de contenido no comparable. |
| EV/FCFF | 22,28x | 35% | 66,66 | No usar CFO−CAPEX como FCFF. |
| P/E | 17,63x | 35% | 56,27 | WBD distorsiona beneficio bajo EBIT. |
| P/FCFE | 19,21x | 10% | 50,40 | Deuda/recompras y FCFE neto. |
| P/OCF | 20,23x | 10% | 57,82 | CFO incluye WBD y variación contenido. |
| P/Ventas | 4,50x | 10% | 56,24 | Depende de margen objetivo y mix. |
| P/BV | 5,00x | 0% | 69,04 | Recompras alteran libro y ROE. |

El valor presente ponderado de múltiplos Base es US$59,47. Los topes ancla C proceden del corte anterior y no se revalidaron independientemente con pares de igual denominador al 21-oct; esta es una reserva material sobre el método secundario, no una razón para cambiar el DCF. El Nivel2 del nuevo artículo retiró las matrices por escenarios no Base y conserva tablas de cálculo, respetando la prioridad de sensibilidad del DCF Base exigida en las reglas v5. La ancla de múltiplo de mercado observada contemporánea por método queda N/D cuando no está contrastada.

## 13. Sensibilidades económicas y escenarios alternativos

Las sensibilidades principales son WACC×g, ROIC×g y delta-crecimiento de ingresos×margen EBIT Base; el inverso recalcula cinco años sin cambiar los demás supuestos. El registro del modelo informa crecimiento implícito8,19% para precio histórico65,04, frente a Base9,99%, con reproducción algebraica del precio dentro de la tolerancia.

| Prueba en hoja | DCF por acción | Interpretación |
|---|---:|---|
| ROIC terminal=WACC9,16% | US$56,08 | Desaparece renta económica extraordinaria. |
| ROIC terminal12% | US$61,79 | Cerca de retorno industrial de referencia. |
| ROIC terminal21,52% | US$69,94 | Supuesto oficial más exigente. |
| Inverso al precio65,04 | CAGR8,19% | Expectativas algo menores que Base. |

La sensibilidad del capital requerido ante S/C menor (por ejemplo hacia1,40x) sería importante, pero no debe añadirse un precio contrafactual sin recalcular los diez años y la perpetuidad. El precio FY+3 auxiliar83,43 no debe mezclarse con los valores presentes.

## 14. Coherencia de hojas, cálculos y presentación

**Control numérico y de identidad del artículo:** revisión fuente NFLX-2026-10-22-SEC9M26-JMR-review-001, nuevo identificador editorial NFLX-2026-10-23-V5-FULL-ANALYSIS-AUDIT-001; mismo DCF69,94, promedio ordinario66,81, MOS45,46 y Disrupción15,55. El artículo muestra recuadro de Base al principio y exactamente18 secciones; Nivel2 mantiene estados, ratios, inputs, cálculos y tablas a partir de la revisión de valoración, evitando publicar sensibilidades de historias no Base como si fueran sensibilidad principal.

**Cobertura semántica exigida por §9 v5:** la matriz del artículo consta de **25 controles**: **18 desarrollados y sustentados; 7 limitados por evidencia identificada**. Los siete son (1) TAM homogéneo por región, (2) sostenibilidad económica de foso y ROIC terminal, (3) gobierno/incentivos individuales de proxy2026, (4) capital económico de contenido y ROIC incremental por cohorte, (5) CRP/Ke por distribución geográfica verificable, (6) comparables y anclas de múltiplos del corte, (7) indicadores de churn/monetización por cohorte no publicados.

No hay secciones reducidas únicamente a un título o enlace. Sin embargo, la regla §9 declara que «limitado por evidencia» **no** equivale a cobertura totalmente resuelta. El análisis está sustancialmente ampliado y documenta lo que falta; no se debe certificar como completo sin ese matiz. La salida del control de publicación del modelo debe referirse a un commit de CI específico: el historial visible contiene corridas failure, y no se ejecutó una nueva suite verde en esta auditoría editorial. La hoja conserva internamente una salvedad económica sobre anclas C.

## 15. Hallazgos priorizados y propuestas de corrección

| Prioridad | Hallazgo / explicación | Efecto potencial | Corrección propuesta en un ciclo distinto |
|---|---|---|---|
| Alta | ROIC terminal21,52% > industria11,04% y WACC9,16% sin prueba de persistencia indefinida. | DCF cae de69,94 a56,08 si ROIC=WACC. | Investigar retorno marginal y duración del moat; aplicar nueva valoración si cambia. |
| Alta | Activos/obligaciones de contenido requieren reinversión sostenida; S/C reciente1,09x frente a Base2,00x. | FCFF podría estar alto por reinversión subestimada. | Conciliar pagos de contenido, amortización y capital por 3–5 años. |
| Alta | Múltiplos ancla C y peers del nuevo corte sin reconstrucción homogénea. | VP múltiples59,47 sujeto a reservas. | Regenerar criterios de ciclo y denominadores EV/FCFF/EBITDA. |
| Media | Prima país adicional50pb no atribuida a geografía económica exacta. | Riesgo de CRP duplicado o sesgo de WACC. | Usar Damodaran del mismo corte con exposiciones por país verificables. |
| Media | Conservadora conserva terminal21,52% como Optimista. | Downside terminal puede ser poco severo. | Justificar o cambiar por un ciclo posterior de Valoración, no Auditoría. |
| Media | g Optimista4,50% supera el nominal USD central4%. | Perpetuidad Optimista podría ser agresiva. | Documentar excepción con techo Rf; revisar nueva regla si procede. |
| Media | WBD US$2.800M e impuesto normalizado a25%. | EPS/OCF y múltiplos pueden alterarse. | Conciliar impuesto del cobro y flujo ordinario. |
| Editorial | Siete filas de cobertura limitadas; no auditar como resueltas. | Tesis y control editorial aún con evidencia material incompleta. | Recuperar proxy, TAM, cohortes y pares cuando se publiquen. |
| Operativo | Corridas CI históricas de la valoración incluyen failure. | No declarar VALIDADO tras modificar solo informes. | Ejecutar controles_todas.sh NFLX y documentar log asociado. |

La auditoría identifica correcciones, **no las ejecuta**. Ningún hallazgo se cierra cambiando arbitrariamente la valoración para acercarla a la cotización.

## 16. Catalizadores, señales de refutación y seguimiento

| Indicador | Horizonte / fuente | Confirmación | Falsación y respuesta |
|---|---|---|---|
| Publicidad vs guía FY2026 US$2.700M | Carta Q4 y 2027 | Recuperación del rollout y monetización | Nueva rebaja relevante: revisar probabilidad con indicador umbral. |
| Ingresos FX neutrales por región | Dos ejercicios SEC | Avance sobre mercados maduros | <8% sostenido: revaluar 12/11/10/9/8% Base. |
| Margen EBIT GAAP anual | 2027–2030 | Avance hacia36% sin timing | Estancamiento ~31–32%: revisar gastos contenido/ads. |
| Obligaciones contenido y flujo ajustado | 10-Q y 10-K | Crecimiento CFO recurrente tras gastos | Renovación consume más caja que incremental. |
| ROIC del capital nuevo | 2027–2030 | Spread sostenible con inversión | Retorno converge a industria/WACC. |
| Recompra/SBC y opciones | SEC+proxy | Acciones netas caen comprando con disciplina | Emisión, strike y precios recompras erosionan equity. |
| WACC y geografía | Treasury/Damodaran fechados | Ke9,44% coherente con exposición | CRP doble contado o Kd no representativo. |

Una publicación del próximo 10-Q sí justificaría reauditar los hechos cambiados; no debe crearse una auditoría repetida sin información nueva que solo recopile las mismas dudas.

## 17. Dictamen económico y resumen para escuchar

**Dictamen económico: CON HALLAZGOS; nueva redacción sustantiva y concordante, pero con reservas críticas.**

Resumen para escuchar: Netflix tiene un negocio sólido y rentable, pasó de ventas US$8.831M en 2016 a US$45.183M en 2025 y LTM US$49.735M. El margen EBIT avanzó hasta 31,30% en el LTM, y el DCF Base del Modelo JMR vale US$69,94 por acción. El problema decisivo es la permanencia de un ROIC terminal21,52% cuando hay competidores gratuitos, pagos elevados por contenido y una referencia industrial cercana al 11,04%. Si el ROIC terminal converge al WACC, la sensibilidad del modelo marca US$56,08. La mejora contable es un hecho; el foso perpetuo es una hipótesis.

El nuevo análisis conserva los 18 apartados, incorpora la historia de diez años, la economía del contenido, geografías, Porter, asignación de capital, escenarios, cinco filosofías y tablero de vigilancia. Su matriz verifica25 temas,18 resueltos con evidencia y7 limitados. La auditoría NO autocertifica estos7 como terminados; la actualización operativa al principio del documento registra ejecuciones posteriores y sus resultados independientes.

**Lectura ordenada:** DCF Base69,94 principal; promedio tres66,81 complementario; disrupción15,55 aparte; precio con MOS35%=45,46; múltiplos VP59,47 secundarios. El precio de análisis65,04 corresponde al21-oct y no es una observación de ahora. No es recomendación mecánica de compra, venta o mantenimiento.

## 18. Fuentes primarias, limitaciones y registro de versión

**Fuentes consultadas:** Netflix [10-Q septiembre2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm), notas5/6/7/9, segmentos, deuda y compromisos; Netflix [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm), cifras y contexto de 2023–2025 más historia en hoja; [carta Q3 publicada 20-oct-2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm), guía2026, margen y publicidad; [hoja oficial JMR](https://docs.google.com/spreadsheets/d/11yN171o8R61n4RhZnmuZuiSyIn_DGkfTmjo7wMKqaZI/edit); [reglas JMR v5](https://github.com/JuanMaRobledo/Modelo-JMR/blob/main/modelo/REGLAS_VIGENTES.md), especialmente §9. Referencia de industria/Ke sectorial conservada del modelo vigente, no reextraída de otra fecha.

Revisión financiera fija: NFLX-2026-10-22-SEC9M26-JMR-review-001. Nueva revisión de artículo/auditoría: NFLX-2026-10-23-V5-FULL-ANALYSIS-AUDIT-001. Fecha auditoría 23-oct-2026. La auditoría anterior está preservada en auditorias/archivo/NFLX-auditoria-2026-10-22.md y no se mezcla con las cifras nuevas. Se publica solo la narrativa de auditoría y el artículo: la valoración, inputs, fuente SEC y escenarios no cambian.

**Limitaciones formales:** no se obtuvo TAM regional monetizable por fuente homogénea, proxy completo individual2026, resultados por cohortes/título, desglose país que certifique la prima extra50pb, anclas de peers de igual fecha ni evidencia de que ROIC terminal21,52% persista indefinidamente. Hubo nuevas ejecuciones del control histórico, algunas fallidas por clasificación de celdas en el detector. El resultado de la nueva puerta financiera debe verificarse en GitHub; el recuento de secciones no constituye certificación financiera. El juicio queda expuesto y se indica qué evidencia levantaría cada reserva.

**Fin de la auditoría independiente de NFLX según prompt 3 v1.2 y reglas JMR v5.**

