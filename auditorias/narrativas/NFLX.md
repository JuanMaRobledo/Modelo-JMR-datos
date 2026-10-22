**Dictamen: PLAUSIBLE CON RESERVAS — AUDITORÍA CONDICIONADA.** Corte de la valoración: 21 de octubre de 2026; estados a septiembre de 2026. Este informe amplía la narración y los contrastes que ya existen en el expediente. Las conciliaciones que identifica como *registradas* corresponden a verificaciones anteriores, no a una nueva lectura independiente de todos los documentos de origen. **No se modificó la valoración.**


**Actualización del 22-oct-2026 — crecimiento autorizado por el analista:** el Base pasa de 10/9/8/7/6 % (CAGR 7,99 %) a **12/11/10/9/8 %** (CAGR **9,99 %**). En la hoja viva recalculada, el DCF Base pasa de US$48,34 a **US$52,03** (+7,64%); múltiplos Base de US$50,60 a **US$51,57**; promedio ordinario a **US$49,67**. Los años 6–10, margen EBIT 32→34%, impuestos, S/C, WACC y terminal **no cambiaron**. El cambio de crecimiento es un supuesto sujeto a corroboración; los 124 controles independientes pertenecen a la corrida previa y **no se reejecutaron** en este corte.

## 1. Ficha de auditoría y alcance

| Campo | Registro examinado |
|---|---|
| Empresa, acción y mercado | Netflix, Inc.; NFLX; Nasdaq; USD por acción |
| Método principal | DCF FCFF, con valor intrínseco **Base** como referencia |
| Fecha y precio del análisis | 21-oct-2026; **US$65,04** por acción (precio histórico declarado, no cotización en vivo) |
| Corte contable | 30-sep-2026, LTM de resultados y flujos; balances de fecha puntual |
| Valor intrínseco principal | **US$52,03** por acción |
| Promedio ordinario de historias | **US$49,67**, secundario, tres historias con probabilidades renormalizadas |
| MOS definido por el analista | 35%; umbral sobre DCF Base **US$33,82** |
| Expediente | [Ver valoración publicada](https://github.com/JuanMaRobledo/Modelo-JMR-datos/blob/main/valoraciones/NFLX-1792548021734.json) y [hoja vinculada](https://docs.google.com/spreadsheets/d/11yN171o8R61n4RhZnmuZuiSyIn_DGkfTmjo7wMKqaZI/edit) |
| Alcance de esta auditoría | Lectura del JSON, tablas financieras publicadas, salvedades, manifiesto de fuentes y controles históricos declarados |
| Fuera del alcance verificado | Nueva descarga y conciliación independiente de cada fuente SEC; ejecución completa de las fórmulas de la hoja original; certificación de comparables; cierre fiscal exacto de todas las hipótesis |

Una comprobación contable no equivale a certificar una hipótesis económica. **Estado matemático**: conciliaciones estructurales y numéricas informadas; **documental**: parcial; **económico**: condicionado.

## 2. Resumen ejecutivo y relato económico central

El DCF Base plantea un negocio de contenidos por suscripción que puede seguir aumentando ingresos por una combinación de monetización, precio, alcance comercial y eficiencia. El escenario no presupone que el crecimiento de ingresos de los mejores años se repita: proyecta un CAGR aproximado de **9,99%** en los primeros cinco años, inferior al ritmo LTM documentado. La tesis es que una desaceleración comercial puede coexistir con un margen más alto si los ingresos adicionales requieren proporcionalmente menos gasto operativo.

El riesgo es que contenido, competencia, publicidad, expansión geográfica y condiciones de licencias exijan costos e inversión mayores que los incorporados. Que Netflix tenga escala no prueba por sí solo que el margen objetivo **34,00%** sea sostenible, ni que un ROIC terminal de **12,00%** compense correctamente toda reinversión futura. Esta es la historia que más importa comprobar.

La discrepancia aparente **quedó aclarada con lectura de las fórmulas originales**: el **21,30%** de «Input sheet» B30 es una **referencia histórica no activa**; el DCF Base usa **32,00% de margen EBIT en el año 1** («Input sheet» B28) y **34,00% como margen objetivo** («Escenarios e historias» D5). Se aclararon etiquetas y vínculos de presentación, sin alterar los supuestos activos ni la valoración.

La contratesis adversa combina desaceleración más intensa, erosión del margen y mayor costo de retención o captación de usuarios. En el estrés de disrupción, el valor publicado es **US$14,78**. Se presenta separado para no diluir el escenario ordinario. La tesis favorable también debe explicar por qué el crecimiento, la monetización y la disciplina de capital podrían conservar el diferencial de rentabilidad; su respaldo empírico no queda cerrado aquí.

## 3. Trazabilidad, integridad y jerarquía de evidencia

| Dato | Período/unidad | Registro | Evidencia declarada | Estado de esta revisión |
|---|---|---:|---|---|
| Ingresos | FY2025, USD millones | 45.183,04 | Income Statement / SEC 10-K | Transcrito; sin reconfirmación externa |
| Ingresos LTM | Sep2026, USD millones | 49.734,63 | FY2025 + 9M2026 − 9M2025 | Puente reproducible desde hoja de fuentes |
| EBIT operativo LTM | Sep2026, USD millones | 15.564,87 | Income Statement y Márgenes | Consistencia con margen reportado; ajustes por revisar |
| ROIC LTM | Sep2026 | 38,58% | Eficiencia de capital | Ratio publicado, denominador económico sin nueva revisión |
| Rf | 21-oct-2026, USD | 4,91% | Treasury menos spread declarado | Hipótesis/metodología por verificar |
| Beta sectorial desapalancada | Año de referencia 2026 | 0,98 | Damodaran, Entertainment Global | Reapalancamiento y fecha requieren auditoría independiente |
| ERP/CRP | Corte indicado en fuente | ERP 4,20% + spread 0,22% y CRP 0,50 pp | Manifiesto de fuentes | Riesgo de solapamiento no descartado |
| Deuda (Kd) | Corte sep2026 | 5,85% | Notas de deuda / estimación | No es cotización observable exacta |
| Precio | 21-oct-2026 | US$65,04 | Yahoo histórico declarado | No sustituir con «precio hoy» |
| Acciones | LTM, millones | 4.106,33 | Income Statement | Debe revisarse conversión de split y dilución de opciones |

### Conciliación SEC corregida: falso positivo de la auditoría anterior

**Revisión del 22-oct-2026:** las tres diferencias de contenido difundidas en la primera auditoría fueron un **error del propio validador**, no de la fuente contable: se aplicó el puente FY2025 + 9M2026 − 9M2025 a filas 37–39 que contienen una serie histórica de 2016–2025, **sin ese encabezado temporal**. El validador ahora exige columnas identificadas y enlace SEC en la fuente de cada fila; solo usa las filas 3–36 del bloque LTM.

| Flujo de contenido (USD millones) | FY2025 | 9M2025 | 9M2026 | LTM calculado | Contraste |
|---|---:|---:|---:|---:|---|
| Adiciones de contenido | −17.096,617 | −12.039,405 | −14.934,230 | **−19.991,442** | Coincide |
| Amortización de contenido | 16.422,166 | 11.657,930 | 12.764,663 | **17.528,899** | Coincide |
| Cambio de pasivos de contenido en CFO | −610,838 | −601,043 | −43,070 | **−52,865** | Coincide |

Fuentes primarias contrastadas: [Netflix FY2025 10-K SEC](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm) (estado de flujo) y [Netflix 9M2026 10-Q SEC](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm) (ambos nueve meses). Los **34 puentes** del bloque específico son aritméticamente reproducibles. La revisión de fuente primaria se realizó para estas tres partidas; no afirmar que todas las demás filas ya fueron verificadas una por una contra SEC.

**Conclusión:** NFLX-11 se cierra como falsa alerta de conciliación. No modificar los importes LTM, no ajustar el FCFF por las diferencias ficticias y conservar el hallazgo como aprendizaje del validador. Las dudas económicas sobre la capitalización y amortización de contenido siguen siendo relevantes, aunque estos puentes sean correctos.

**Jerarquía:** documento regulatorio → normalización por línea y período → hoja/JSON → supuestos del analista. No mezclar unidades USD millones con US$/acción ni saldos de balance con flujos LTM.

## 4. Historia financiera: diez años y punto de partida

La serie publicada abarca 2016–2025 y un LTM separado a septiembre de 2026. Valores históricos **redondeados**:

| Indicador | 2016 | 2025 | LTM sep2026 | Promedio FY 3A | Promedio FY 5A | Promedio FY 10A |
|---|---:|---:|---:|---:|---:|---:|
| Ingresos (USD millones) | 8.830,67 | 45.183,04 | 49.734,63 | 39.302,44 | 35.844,14 | 26.069,09 |
| Margen operativo | 4,30% | 29,49% | 31,30% | 25,61% | 23,10% | 16,84% |
| ROIC | N/P | 36,66% | 38,58% | 29,64% | 26,23% | 22,45%* |

*El promedio ROIC de hasta 10 ejercicios utiliza **nueve** valores disponibles; 2016 es N/P por desglose faltante. No se convirtió el faltante en cero.*

Los ingresos crecieron a CAGR de aproximadamente **12,64%** en FY2022–FY2025, **12,57%** en FY2020–FY2025 y **19,89%** en FY2016–FY2025. No deben confundirse estas trayectorias de cierre fiscal con el crecimiento LTM de **14,65%** que aparece en la hoja. El margen LTM supera el máximo anual FY2025; eso exige revisar la naturaleza del corte, los efectos no recurrentes y la normalización, no asumir que el nuevo nivel sea permanente.

El flujo de caja libre publicado se presenta en su hoja, pero la definición de FCFF económico, los costos de contenido y el tratamiento de SBC requieren su propia conciliación. Las recompras y el cambio en número de acciones pueden aportar al valor por acción sin aumentar por sí mismos el valor empresarial.

## 5. Crecimiento de ingresos: de la historia a la proyección

**Historia económica:** la proyección Base propone desacelerar tras años de expansión. La hoja de supuestos registra **12,00% para el año 1**, **9,99% como CAGR de los años 1–5** y **9,49% como CAGR de los años 2–5**. Las tasas anuales reales del DCF son 12%, 11%, 10%, 9% y 8%. La etiqueta anterior que llamaba al 9,99% «años 2–5» era incorrecta. La justificación debe desagregar precio, volumen/cuentas monetizadas, publicidad y mezcla; no hay en este expediente una conciliación granular por segmento verificada independientemente.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto |
|---|---|---|---|---|---|---|
| Crecimiento ingresos 1–5 | FY CAGR 3A 12,64%; 5A 12,57%; 9A 19,89%; LTM 14,65% | Año 1 12%; promedio años 1–5 9,99%; historia A | N/D: pares homogéneos y fuente fechada no confirmados | Monetización sostiene expansión mientras maduran mercados | Usuarios/monetización por debajo de meta, descuentos, rotación o costos de captación | Sensibilidad crecimiento disponible en hoja; recomputación completa aquí N/D |

**Seis preguntas:** valor y horizonte identificados; contraste histórico realizado; mecanismo plausible pero no demostrado; deben ocurrir monetización y retención suficientes; lo refutarían caídas de crecimiento orgánico o mayor churn; el impacto cuantitativo independiente necesita reejecutar el modelo variando únicamente crecimiento y su reinversión asociada.

## 6. Márgenes operativos y normalización de beneficios

El EBIT LTM publicado es **US$15.564,87 millones** sobre ventas de **US$49.734,63 millones**, es decir aproximadamente **31,30%**. El DCF Base registra margen sostenible **34,00%**, Conservador 30,00%, Optimista 36,00% y Disrupción 18,00%. El objetivo Base supera el último máximo anual FY2025 (29,49%), aunque supera menos al LTM. La dinámica de amortización de contenido, tecnología, marketing y escala debe distinguirse de costos no recurrentes.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto |
|---|---|---|---|---|---|---|
| EBIT / ventas | 3A 25,61%; 5A 23,10%; 10A 16,84%; LTM 31,30% | Año 1 Base 32%; meta Base 34%; referencia histórica 21,30% **no activa** | N/D peer mediana certificada | Escala y mezcla deben superar costos incrementales | Contenido/marketing consumen apalancamiento operativo | Sensibilidad al margen, impuestos y reinversión del DCF, por confirmar con nueva corrida |

**Seis preguntas:** se conocen valores y cortes; histórico reconstruido; causalidad por demostrar; requiere contención de costos de contenido/tecnología; se refuta ante erosión del margen subyacente; el efecto por acción requiere sensibilidad de FCFF ejecutada. La referencia 21,30% no alimenta las historias; el nuevo crecimiento Base fue decidido por el analista, manteniendo margen y demás supuestos. La utilidad normalizada por el evento WBD usa una tasa fiscal hipotética de 25%; no se atribuye a crecimiento operativo.

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

La historia Base usa **Sales-to-Capital de 1,39** y **ROIC terminal de 12,00%**; este último es inferior al ROIC LTM publicado (38,58%). La caída terminal del ROIC puede representar competencia o reversión de rentas superiores, pero necesita evidencia del capital invertido y de activos de contenido. El supuesto 1,39 procede de una referencia sectorial amplia y **no está certificado como eficiencia marginal propia**. No debe confundirse capex contable con la reinversión económica total.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto |
|---|---|---|---|---|---|---|
| Reinversión/Sales-to-Capital/ROIC | ROIC FY 3A 29,64%; 5A 26,23%; hasta 9A 22,45%; LTM 38,58% | S/C 1,39; ROIC terminal 12,00% | Ancla sectorial global referida; homogeneidad N/D | Negocio retiene retornos incrementales positivos mientras reinvierte en contenido/mercado | Contenido/acquisiciones exigen más capital por dólar de ventas | Material; prueba reinversión = Δventas/S-C pendiente de reproducir en celdas |

**Seis preguntas:** la tasa y período están identificados; el histórico contable está disponible pero requiere conciliación económica; la tesis presume escala; debería observarse conversión de ingresos a caja; se refuta por mayor capital de contenido/captación; sensibilidad ROIC terminal×g existe en hoja, pero no se ha ejecutado aquí un nuevo DCF completo.

## 8. Costo del capital y riesgo

El expediente declara Rf USD **4,91%**, beta sectorial desapalancada **0,98**, referencias Damodaran para ERP y un spread país que requiere cuidado para no duplicar riesgo. Kd **5,85%** y CRP adicional **0,50 pp** son estimaciones del analista. El descuento de múltiplos emplea Ke **9,94%**. La sensibilidad almacenada tiene centro en WACC terminal cercano a **9,64%** y g **4,00%**; distinguir WACC de Ke y sus fechas es obligatorio.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto |
|---|---|---|---|---|---|---|
| Rf, ERP, beta, Ke, WACC y Kd | Curvas, spreads y beta vigentes a corte; serie 3/5/10 N/D | Rf 4,91%; Ke 9,94%; Kd estimado 5,85%; WACC terminal ≈9,64% registrado | Treasury, Damodaran y notas SEC declarados | Riesgo consistente en moneda y negocio durante 10 años | Primas duplicadas o beta no comparable | Alta sensibilidad a WACC; validar hoja Cost of capital y matriz WACC×g |

**Seis preguntas:** tasas y fechas declaradas; faltan series equivalentes de riesgo para 3/5/10; hipótesis ligadas a estructura de capital; deben sostenerse spreads, beta y pesos; evidencia contraria son cambios de crédito/geografía o doble conteo; la matriz WACC/g permite explorar dirección, pero todas sus celdas requieren control formal.

## 9. Convergencia y valor terminal

El crecimiento a perpetuidad Base es **4,00%**, inferior a la Rf **4,91%** declarada. El centro publicado de WACC terminal de la matriz es aproximadamente **9,64%**, superior a g; esta relación es necesaria, no suficiente, para una perpetuidad sostenible. Según la auditoría anterior el valor presente terminal representa **55,77%** del valor operativo Base; ese porcentaje es **evidencia histórica declarada**, no una suma de FCFF reejecutada en esta revisión.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto |
|---|---|---|---|---|---|---|
| g, ROIC y reinversión terminal | Inflación y retorno a 10 años comparable N/D | g 4%; ROIC 12%; WACC terminal cerca de 9,64% | Referencias macro/industria sin corroboración externa actual | Ventaja residual suficiente para retornos sobre costo de capital | Compresión de moat, menor pricing, mayor costo de contenido | DCF depende materialmente del terminal; sensibilidad conjunta WACC×g y ROIC×g almacenada |

**Seis preguntas:** valores definidos; no hay histórico de valor terminal observable; hipótesis de ventaja es un juicio, no dato; exige permanencia de la rentabilidad; lo refuta convergencia a WACC o reinversión más alta; la cuantificación total de erosión requiere volver a calcular FCFF terminal y su valor presente.

## 10. Validación independiente del valor intrínseco

El DCF Base es **US$52,02842282** por acción (mostrar **US$52,03**). El umbral MOS 35% es **US$33,81847483**, de modo que la multiplicación Base×0,65 **concilia**. El DCF llevado a FY+3 que muestra la tabla de métodos es **US$69,13** para la historia Base; esto **no** es otro valor presente sino la capitalización con Ke a tres años. El DCF inverso publicado indica que el precio del análisis **US$65,04** exige CAGR 1–5 cerca de **16,12%** al mantener los demás supuestos Base fijos, frente al **9,99%** de Base (diferencia **6,13 puntos porcentuales**).

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto |
|---|---|---|---|---|---|---|
| DCF FCFF Base | Flujos y estados 2016–2025 + LTM; reconfirmación SEC N/D | Valor Base US$52,03; MOS US$33,82; FY+3 US$69,13 | Método FCFF/WACC Damodaran | Márgenes y reinversión explican valor operativo | Valores de flujos/terminal o puente EV→equity mal vinculados | 124 pruebas históricas declaradas, no una nueva reproducción integral del FCFF por año |

**Seis preguntas:** método, valor y fecha identificados; flujos históricos existen; precio actual no justifica flujos; supuestos exigen crecimiento/margen/reinversión coherentes; falsadores incluyen fallos de datos de origen y descuento; la pantalla integral reproduce las conciliaciones que admite el JSON, pero **no certifica todas las fórmulas originales**.

## 11. Cuatro historias y probabilidades

| Historia | Crecimiento CAGR 1–5 | Margen EBIT objetivo | S/C | ROIC terminal | g terminal | DCF por acción | Probabilidad original |
|---|---:|---:|---:|---:|---:|---:|---:|
| Conservador (B) | 5,00% | 30,00% | 1,15 | 9,64% | 3,00% | US$33,61 | 25% |
| **Base (A)** | **9,99%** | **34,00%** | **1,39** | **12,00%** | **4,00%** | **US$52,03** | **50%** |
| Optimista (D) | 11,58% | 36,00% | 1,80 | 15,00% | 4,50% | US$68,59 | 15% |

El promedio **ordinario** es (50%×52,028423 + 25%×33,606494 + 15%×68,588818) / 90% = **US$49,67**. Es secundario frente al Base. El 10% restante **no** se inventa ni redistribuye fuera de esa normalización.

### ¿Qué pasaría si todo fallara?

Disrupción (C): crecimiento CAGR aproximadamente **−2,41%**, margen **18,00%**, S/C **1,00**, g terminal **0%**, valor **US$14,78** y probabilidad original **10%**. Esta historia no entra en el promedio de tres, ni se transforma automáticamente en objetivo de mercado. Señales de confirmación/refutación requieren resultados de crecimiento, economía de contenido y márgenes posteriores.

Las probabilidades 50/25/10/15 suman 100%, pero el expediente no demuestra una calibración estadística externa de sus pesos; siguen siendo hipótesis.

## 12. Valoración por múltiplos: prueba independiente y secundaria

**Los siete** métodos figuran, incluso aquellos con peso cero. Precios y valores presentes Base en **US$/acción**:

| Método | Peso global | FY+3 Base | VP Base (criterio solo 3 años) | Estado A/B/C |
|---|---:|---:|---:|---|
| EV/EBITDA | 0% | 96,48 | 72,61 | A histórico disponible; B peers no certificados; C por verificar |
| EV/FCFF | 15% | 68,92 | 51,87 | A disponible; B no certificado; C por verificar |
| P/E | 15% | 81,11 | 61,04 | A disponible; B no certificado; C por verificar |
| P/FCFE | 15% | 59,68 | 44,92 | A disponible; B no certificado; C por verificar |
| P/OCF | 9% | 52,66 | 39,63 | OCF económico normalizado, no confundir con FCF |
| P/V | 6% | 81,90 | 61,64 | Denominador ventas, no margen/FCFF |
| P/BV | 0% | 89,55 | 67,40 | Patrimonio común y relevancia sectorial sujetos a revisión |

El valor relativo agregado Base hoy declarado es **US$51,57**, frente a DCF Base **US$52,03**. El **objetivo secundario FY+3** canónico (DCF 40% + siete múltiplos 60%, capitalizado a Ke) es **US$68,76**, distinto del DCF Base de US$52,03 al presente. Se detectó una tabla heredada de seis métodos en «Resumen de Valoración» cuyas ponderaciones no coincidían con los siete métodos canónicos; se desacopló el cálculo principal de esa tabla y se vinculó a «Descuento de múltiplos», sin modificar pesos de los siete métodos. Los múltiplos no definen por sí mismos el valor intrínseco. El peso global DCF es 40% y los relativos 60%; se requiere comprobar la adecuación de cada denominador, las acciones diluidas, el puente EV→equity y la ausencia de doble conteo de dividendos. Los anclajes A (historia), B (pares), C (fundamentos) deben justificarse individualmente y no calibrarse para igualar el DCF. **N/D de B o C no significa que la fórmula aritmética de FY+3 esté rota.**

## 13. Sensibilidades económicas y escenarios alternativos

Las matrices de Google Sheets se recalcularon de forma automática con la nueva trayectoria (sin repetir la contrastación independiente de las 75 celdas). La hoja publicada incluye sensibilidad DCF Base frente a **WACC terminal × crecimiento perpetuo**, **ROIC terminal × g** y **margen sostenible × desplazamiento de crecimiento 1–5**. El centro visible de la primera matriz (**WACC terminal 9,64% y g 4,00%**) devuelve aproximadamente **US$52,03**, pero no se volvió a ejecutar cada combinación de flujos desde la hoja fuente aquí.

El DCF inverso contrasta crecimiento Base 9,99% con el **16,12%** necesario para justificar US$65,04 **bajo el conjunto de premisas restante fijo**. La diferencia no prueba por sí sola un precio erróneo; obliga a narrar qué aceleración adicional de monetización sería necesaria.

La corrida registra **7 centros Base** de múltiplos contrastados y **14** combinaciones de sensibilidad Conservador/Optimista como N/D. Existen proyecciones de precios para esas historias, pero **no** se declara que sus matrices completas fueron auditadas. Ejes exigidos: múltiplo real en veces y denominador económico FY+3 en sus unidades, con resultado valor por acción descontado; el eje fraccional 0,8–1,2, solo, no cumple el contrato editorial. La familia económica A/B/C requiere revisión de centros antes de tratarla como evidencia.

## 14. Coherencia de hojas, cálculos y presentación

El expediente previo declara 124 controles numéricos, 28 fórmulas críticas, 20 preflight estructurales y cero errores almacenados en 7.528 celdas de fórmula. Ese éxito **no certifica fuentes SEC ni razonabilidad de supuestos**. Corrigió tratamientos de BPA básico/diluido, faltantes no convertidos en cero, referencias de industria, partidas de tecnología/desarrollo y desfase inicial. El informe previo también confirma que el valor principal es DCF Base y que disrupción permanece aislada.

**Control de interpretación resuelto:** el 21,30% de margen en Input B30 es una referencia histórica que **no alimenta** el DCF. La historia Base activa conserva margen inicial 32,00% y objetivo 34,00%. La tasa de crecimiento Base anual del año 2 es 11%, distinta del CAGR 1–5 9,99% y del CAGR 2–5 9,49%. Las etiquetas ya se aclararon y posteriormente el analista elevó deliberadamente la trayectoria de crecimiento. Las cifras de DCF y múltiplos sí se recalcularon. Los restantes controles económicos y de LTM continúan pendientes.

Control adicional: fecha del precio del análisis separada del precio de hoy; MOS solo sobre Base; datos financiero/estadístico en nivel 2; matrices con unidades; enlaces a hoja, JSON y auditoría. Se inspeccionó el registro publicado, no se afirma sincronización bidireccional comprobada.

## 15. Hallazgos priorizados y propuestas de corrección

| ID | Severidad | Tipo | Evidencia y efecto | Acción propuesta | Estado |
|---|---|---|---|---|---|
| NFLX-01 | Resuelto — presentación | Etiquetas de márgenes/CAGR | Referencia histórica EBIT 21,30% no activa; año 1 32%, objetivo 34%; CAGR 1–5 9,99% y 2–5 9,49% | Etiquetas aclaradas; DCF posteriormente recalculado por nueva hipótesis de crecimiento | Cerrado |
| NFLX-02 | Medio | Ajuste fiscal WBD | Netflix recibió US$2.800 millones fuera de EBIT; el impuesto específico no está desglosado en 10-Q | Mantener 25% como hipótesis de NI normalizada, sin atribuir ese porcentaje a declaración SEC; DCF EBIT directo no incluye pago | Abierto como divulgación, no como error DCF |
| NFLX-03 | Alto | Comparables | Siete pares/métricas sin homogeneidad certificada, ancla C sin control universal | Revisar A/B/C por método, ROIC, growth, margen, deuda y denominador | Abierto |
| NFLX-04 | Medio | Riesgo | CRP 50 pb y Kd 5,85% estimados; potencial solapamiento de prima país | Revisar construcción fechada de WACC y alternativas | Abierto |
| NFLX-05 | Medio | Reinversión | S/C 1,39 tomado de agregado sectorial para margen incremental | Comparar serie propia, inversión en contenido e incremental ROIC | Abierto |
| NFLX-06 | Medio | Opciones | Plazo 4,5 años supuesto vs dato anterior 4,79 | Sensibilidad en expediente; localizar nota exacta Sep2026 | Abierto |
| NFLX-07 | Medio | Terminal | ROIC 12% persistente sin prueba de moat duradero | Probar convergencia a WACC y recalcular sensibilidad de FCFF | Abierto |
| NFLX-08 | Medio | Presentación/matrices | 14 controles de sensibilidad de historias relativas N/D | No describirlos como probados; completar solo con ejes reales y centros | Abierto |
| NFLX-09 | Medio | Contabilidad/normalización | I+D elegible no aislada; FCFF/OCF con aproximaciones; partidas N/P | Separar datos reportados, ajustes y no disponibles | Abierto |
| NFLX-10 | Medio | Documento | Sin validación nueva de todas las fuentes originales y de 18 bloques económicos | Completar evidencia y validar manualmente esta estructura ampliada | Abierto |
| NFLX-11 | **Cerrado — falso positivo** | LTM/flujo | El validador confundió las filas históricas 2016–2025 con el bloque FY/9M/LTM. Las 34 filas válidas concilian aritméticamente; se verificaron tres partidas de contenido con SEC | Se corrigió código y pruebas automáticas; no cambiar FCFF ni datos históricos | Cerrado |
| NFLX-12 | **Alto** | Riesgo / fuentes | Treasury US 10Y 21-oct-2026 = 5,13% frente a Rf activa 4,91%; ERP4,92% incorpora ancla enero2026 de 4,42% y prima país0,50pp. | Verificar fecha y geografía de Rf/ERP/CRP y revalorar WACC de forma conjunta antes de cambiar el DCF principal | Abierto |
| NFLX-13 | **Cerrado — presentación** | Hoja de tesis | «Tesis de Inversión y Supuestos» conservaba casillas [TICKER]/[XX] y filas sin completar | Se completó con historias, cifras ligadas por fórmula a tres escenarios y advertencias sobre descuentos | Cerrado |
| NFLX-14 | Medio | Auditoría independiente | 124 pruebas históricas no reejecutadas desde crecimiento Base 9,99% | Reproducir 124 controles económicos, contables, hipótesis y reportes en esta versión | Abierto |

Ningún hallazgo se marca resuelto por haber añadido una sección textual. Propuestas de corrección **no** equivalen a autorización para cambiar los datos.

### Sensibilidades de hipótesis sin alterar el DCF principal

Son simulaciones económicas **aisladas** sobre la estructura publicada; no reemplazan una corrida íntegra del DCF con un conjunto nuevo de supuestos.

| Variable | Caso | Valor indicativo US$/acción |
|---|---|---:|
| Ventas/capital incremental | 1,00 en años 1–10 | **49,77** |
| Ventas/capital incremental | 1,39 (actual) | **52,03** |
| Ventas/capital incremental | 1,80 en años 1–10 | **53,35** |
| ROIC terminal | Convergencia a WACC 9,64% | **48,29** |
| ROIC terminal | Mantener 12,00% (actual) | **52,03** |
| Vida residual opciones | 3,5 años, Black–Scholes indicativo | **52,09** |
| Vida residual opciones | 4,5 años (actual) | **52,03** |
| Vida residual opciones | 5,5 años, Black–Scholes indicativo | **51,97** |

El S/C se modifica únicamente en la reinversión explícita **Δingresos/S/C** de años 1–10, dejando inmóvil la reinversión terminal, los impuestos, EBIT y descuento; se vuelve a descontar el cambio anual. ROIC terminal: reinversión = NOPAT × g/ROIC; se mantiene el resto. Opciones: Black–Scholes con S=65,04, strike=41,24, volatilidad=36,96%, Rf=4,91% y 120,175117 millones de opciones; no es precio observable de las opciones.

**Costo de capital:** el [Treasury estadounidense](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=202610&type=daily_treasury_yield_curve) reporta **5,13% a 10 años el 21-oct-2026**. «Origen de los Supuestos» pide explícitamente ese vencimiento y fecha; la hoja usa 4,91%. Además, el ERP de 4,92% procede de un dato Maduro/Estados Unidos 4,42% identificado como enero 2026 y 0,50 pp de prima adicional. No se cambió Rf en el DCF sin auditar y fechar coherentemente ERP, exposición geográfica y riesgo de deuda. El resultado US$52,03 **no está certificado como valor con tasas de mercado del 21-oct-2026**.

**Crecimiento y márgenes:** la [guía trimestral Netflix Q3 2026](https://ir.netflix.net/files/doc_financials/2026/q3/FINAL-Q3-26-Shareholder-Letter.pdf) prevé ingresos FY2026 US$51.100 millones (+13%) y margen EBIT 31,5%. El «año 1» del DCF comienza desde LTM septiembre2026 y no coincide con FY2026. Crecer 12/11/10/9/8% es una hipótesis del analista, no guía oficial.

**Comparables:** la pestaña «Sector» conserva encabezados pero ninguna fila de empresas y denominadores certificados. El hecho de calcular siete precios no equivale a certificar los múltiplos; las alternativas de 0% peso también deben informarse, pero no mezclarse indiscriminadamente.

## 16. Catalizadores, señales de refutación y seguimiento

| Indicador | Observado en expediente (fecha) | Señal favorable para revisar | Señal adversa | Fuente y frecuencia |
|---|---|---|---|---|
| Crecimiento de ingresos LTM | 14,65%, sep2026 | Crecimiento sostenido suficiente para primera proyección 12% | Caída persistente bajo la trayectoria Base | Estado trimestral, comparar LTM homogéneo |
| Margen EBIT LTM | 31,30%, sep2026 | Expansión sostenible hacia 34% con normalización documentada | Reversión de margen tras mayores costos de contenido/marketing | 10-Q / reportes trimestrales |
| ROIC LTM | 38,58%, sep2026 | Retorno económico compatible con reinversión eficiente | Deterioro material por capital de contenido/adquisiciones | Estados + reconstrucción anual |
| Margen FCF LTM publicado | 22,87%, sep2026 | Conversión a caja que acompañe el EBIT | Brecha caja-beneficio persistente o SBC/capex subestimado | Cash Flow Statement cada trimestre |
| Número de acciones | 4.106,33 millones, LTM | Dilución/compras reconciliadas con valor por acción | Opciones/SBC e instrumentos dilutivos no recogidos | Notas y acciones diluidas, trimestral |
| Costo de capital y terminal | Centro WACC terminal ~9,64%, g 4% | Riesgos reales justifican tasa terminal y moat | Aumento de WACC, descenso ROIC/g o prima país duplicada | Treasury, Damodaran, notas deuda; revisión por corte |

Los umbrales de «señal favorable/adversa» son **criterios propuestos para seguimiento**, no guía oficial de Netflix. No se afirma calendario de resultados futuros sin fuente confirmada.

## 17. Dictamen económico y resumen para escuchar

**Tesis: plausible con reservas.** Matemáticamente, el expediente contiene controles técnicos anteriores y las conciliaciones básicas reproducibles; documentalmente faltan confirmaciones de ajustes y fuentes; económicamente hay hipótesis exigentes de margen, reinversión y rentabilidad terminal. La aparente discrepancia del margen quedó aclarada al verificar qué celdas alimentan el DCF; siguen abiertos la consistencia de fuentes restantes, la vigencia del WACC y los supuestos económicos. El supuesto Base actualizado supone mayor monetización que la anterior trayectoria, pero sigue por debajo del ritmo histórico de cinco años; los más frágiles son sostenibilidad del margen 34%, intensidad de capital marginal y ROIC terminal. El mercado al precio fechado US$65,04 supera el DCF Base US$52,03 en alrededor de **25,01%**; se trata de una comparación de supuestos a una fecha, no recomendación de operar.

### Resumen para escuchar

Netflix presenta una historia económica en la que el crecimiento se modera, pero la eficiencia operativa puede sostener el valor. Su valoración principal, el DCF Base, es de unos cincuenta y dos dólares por acción; el precio del análisis era sesenta y cinco. El modelo exige un margen operativo objetivo de treinta y cuatro por ciento. La hoja también mostraba veintiuno coma tres por ciento, pero es una referencia histórica, no la hipótesis activa. Las fórmulas muestran margen inicial de treinta y dos y objetivo de treinta y cuatro por ciento. El crecimiento implícito que justificaría el precio del análisis es considerablemente mayor que el crecimiento Base proyectado. Las pruebas anteriores avalan diversas conciliaciones, pero no certifican las fuentes, la selección de comparables ni las ventajas competitivas de largo plazo. Por eso la valoración se mantiene **con reservas** y sin modificación de sus cifras.

## 18. Fuentes primarias, limitaciones y registro de versión

| Fuente | Documento y enlace declarado | Fecha/corte | Respaldaría | Límite |
|---|---|---|---|---|
| SEC / Netflix | [10-Q y notas](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm) | Sep2026, publicado 21-oct-2026 según manifiesto | Resultados, balance, deuda, ajustes | En esta revisión no se abrió de nuevo cada línea |
| SEC / Netflix | [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm) | Dic2025 | Serie FY / LTM | Reconfirmación externa pendiente |
| US Treasury | [Tasas Treasury](https://home.treasury.gov/resource-center-data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026) | 21-oct-2026 declarado | Rf y moneda USD | Selección plazo/spread por revisar |
| Damodaran | [ERP](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm), [betas sectoriales](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/BetasGlobal.html) | Corte ERP oct2026; beta ene2026 declarado | ERP y beta | Homogeneidad sector/país e interacción CRP pendientes |
| Precio histórico | [Yahoo chart](https://query1.finance.yahoo.com/v8/finance/chart/NFLX?interval=1d) | 21-oct-2026 declarado | US$65,04 | Precio de corte, no cotización actual |
| Valoración/hojas | [Expediente JSON](https://github.com/JuanMaRobledo/Modelo-JMR-datos/blob/main/valoraciones/NFLX-1792548021734.json) · [Google Sheets](https://docs.google.com/spreadsheets/d/11yN171o8R61n4RhZnmuZuiSyIn_DGkfTmjo7wMKqaZI/edit) | 21-oct-2026 | Fórmulas, escenarios, matrices y supuestos | Datos publicados sin auditoría completa en vivo de fórmulas |
| Antecedente preservado | [Narrativa anterior](https://github.com/JuanMaRobledo/Modelo-JMR-datos/blob/main/auditorias/historicas/NFLX-2026-10-21-auditoria-previa.md) | 21-oct-2026 | Detalle original de 124 pruebas, opciones, WBD y ajustes | Registro histórico, no reemplaza esta conclusión |

**Aclaración editorial del 22-oct-2026:** comprobadas las referencias Input B27–B30, escenario Base y proyección Valuation output. No se reemplazó un supuesto económico por el dato histórico. Se sincronizaron las etiquetas de márgenes y los dos CAGR con el JSON de la app.

**Revisión del 22-oct-2026:** fuentes SEC del contenido contrastadas y falso error LTM descartado. Nueva discrepancia Rf contra 10Y Treasury oficial (5,13% vs 4,91%) señalada y pendiente de revisión integral del WACC. Ajuste explícito de revenue growth Base a 12/11/10/9/8%; actualización automática de FCFF, escenarios, múltiples siete métodos, matrices y valor principal desde Sheets. No modifica el margen EBIT ni cierra salvedades de fuentes o comparables.

**Versión de auditoría:** ampliación narrativa basada en el prompt `auditoria-economica-jmr-v1.2` y el expediente NFLX fechado 21-oct-2026. **Estado: AUDITORÍA CONDICIONADA**, por verificación económica y documental pendiente. Las pruebas anteriores de 124 controles, 28 fórmulas críticas y lectura de matrices siguen referidas a su corrida original; no se ejecutaron nuevamente por el mero acto de editar este Markdown. El texto permanece editable y versionado en GitHub. **No se modificó la valoración.**
