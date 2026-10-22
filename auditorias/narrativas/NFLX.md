# Auditoría económica narrativa — Netflix, Inc. (NFLX)

**Dictamen: PLAUSIBLE CON RESERVAS — AUDITORÍA CONDICIONADA.** Corte de la valoración: 21 de octubre de 2026; estados a septiembre de 2026. Este informe amplía la narración y los contrastes que ya existen en el expediente. Las conciliaciones que identifica como *registradas* corresponden a verificaciones anteriores, no a una nueva lectura independiente de todos los documentos de origen. **No se modificó la valoración.**

## 1. Ficha de auditoría y alcance

| Campo | Registro examinado |
|---|---|
| Empresa, acción y mercado | Netflix, Inc.; NFLX; Nasdaq; USD por acción |
| Método principal | DCF FCFF, con valor intrínseco **Base** como referencia |
| Fecha y precio del análisis | 21-oct-2026; **US$65,04** por acción (precio histórico declarado, no cotización en vivo) |
| Corte contable | 30-sep-2026, LTM de resultados y flujos; balances de fecha puntual |
| Valor intrínseco principal | **US$48,34** por acción |
| Promedio ordinario de historias | **US$47,62**, secundario, tres historias con probabilidades renormalizadas |
| MOS definido por el analista | 35%; umbral sobre DCF Base **US$31,42** |
| Expediente | [Ver valoración publicada](https://github.com/JuanMaRobledo/Modelo-JMR-datos/blob/main/valoraciones/NFLX-1792548021734.json) y [hoja vinculada](https://docs.google.com/spreadsheets/d/11yN171o8R61n4RhZnmuZuiSyIn_DGkfTmjo7wMKqaZI/edit) |
| Alcance de esta auditoría | Lectura del JSON, tablas financieras publicadas, salvedades, manifiesto de fuentes y controles históricos declarados |
| Fuera del alcance verificado | Nueva descarga y conciliación independiente de cada fuente SEC; ejecución completa de las fórmulas de la hoja original; certificación de comparables; cierre fiscal exacto de todas las hipótesis |

Una comprobación contable no equivale a certificar una hipótesis económica. **Estado matemático**: conciliaciones estructurales y numéricas informadas; **documental**: parcial; **económico**: condicionado.

## 2. Resumen ejecutivo y relato económico central

El DCF Base plantea un negocio de contenidos por suscripción que puede seguir aumentando ingresos por una combinación de monetización, precio, alcance comercial y eficiencia. El escenario no presupone que el crecimiento de ingresos de los mejores años se repita: proyecta un CAGR aproximado de **7,99%** en los primeros cinco años, inferior al ritmo LTM documentado. La tesis es que una desaceleración comercial puede coexistir con un margen más alto si los ingresos adicionales requieren proporcionalmente menos gasto operativo.

El riesgo es que contenido, competencia, publicidad, expansión geográfica y condiciones de licencias exijan costos e inversión mayores que los incorporados. Que Netflix tenga escala no prueba por sí solo que el margen objetivo **34,00%** sea sostenible, ni que un ROIC terminal de **12,00%** compense correctamente toda reinversión futura. Esta es la historia que más importa comprobar.

Existe una contradicción específica entre artefactos: la hoja «Supuestos Recomendados» presenta **21,30%** como margen objetivo en la columna «Valor actual (Input sheet)», mientras la historia DCF Base almacenada consigna **34,00%**. Pueden existir hojas, rutas o versiones diferentes; sin inspeccionar las fórmulas no corresponde escoger arbitrariamente una de las dos. Se clasifica como **hallazgo alto de trazabilidad**, no como DCF automáticamente incorrecto.

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

### Puentes LTM de contenido que requieren conciliación

En el control reproducido a partir de la hoja publicada «Fuentes SEC y LTM» aparecen **tres partidas con diferencias materiales** al usar la identidad FY2025 + 9M2026 − 9M2025. Puede haber cambios de definición, reclasificación o errores de fuente: **todavía no se ha establecido la causa**.

| Partida (USD millones) | FY2025 + 9M2026 − 9M2025 | LTM registrado | Diferencia absoluta |
|---|---:|---:|---:|
| Adiciones de contenido | 11.890,97 | 13.916,68 | 2.025,71 |
| Amortización de contenido | 6.182,28 | 9.216,25 | 3.033,97 |
| Cambio de pasivos de contenido en CFO | 1.872,52 | −694,01 | 2.566,53 |

**Control bloqueante:** recuperar los cuatro períodos y la definición de cada renglón desde los estados/notas, y determinar si la fila reportada es comparable o se presenta con distinto perímetro. No reescribir automáticamente el LTM ni el FCFF mientras no se explique. Los demás puentes que concilian aritméticamente tampoco quedan certificados contra SEC solo por conciliar.

**Jerarquía:** documento regulatorio / estado original → normalización y fuente por línea → hoja/JSON → supuestos del analista. El registro publicado no reemplaza el documento regulatorio. No mezclar unidades USD millones con US$/acción, ni saldos de balance con flujos LTM.

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

**Historia económica:** la proyección Base propone desacelerar tras años de expansión. La hoja de supuestos registra **10,00% para el primer año** y **7,99% para el tramo años 2–5**; la historia Base contiene 10%, 9%, 8%, 7% y 6% anuales, consistentes con ese CAGR compuesto aproximado. La justificación debe desagregar precio, volumen/cuentas monetizadas, publicidad y mezcla; no hay en este expediente una conciliación granular por segmento verificada independientemente.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto |
|---|---|---|---|---|---|---|
| Crecimiento ingresos 1–5 | FY CAGR 3A 12,64%; 5A 12,57%; 9A 19,89%; LTM 14,65% | Año 1 10%; promedio años 1–5 7,99%; historia A | N/D: pares homogéneos y fuente fechada no confirmados | Monetización sostiene expansión mientras maduran mercados | Usuarios/monetización por debajo de meta, descuentos, rotación o costos de captación | Sensibilidad crecimiento disponible en hoja; recomputación completa aquí N/D |

**Seis preguntas:** valor y horizonte identificados; contraste histórico realizado; mecanismo plausible pero no demostrado; deben ocurrir monetización y retención suficientes; lo refutarían caídas de crecimiento orgánico o mayor churn; el impacto cuantitativo independiente necesita reejecutar el modelo variando únicamente crecimiento y su reinversión asociada.

## 6. Márgenes operativos y normalización de beneficios

El EBIT LTM publicado es **US$15.564,87 millones** sobre ventas de **US$49.734,63 millones**, es decir aproximadamente **31,30%**. El DCF Base registra margen sostenible **34,00%**, Conservador 30,00%, Optimista 36,00% y Disrupción 18,00%. El objetivo Base supera el último máximo anual FY2025 (29,49%), aunque supera menos al LTM. La dinámica de amortización de contenido, tecnología, marketing y escala debe distinguirse de costos no recurrentes.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto |
|---|---|---|---|---|---|---|
| EBIT / ventas | 3A 25,61%; 5A 23,10%; 10A 16,84%; LTM 31,30% | Meta historia Base 34%; **«Supuestos Recomendados» 21,30%**, discordancia por revisar | N/D peer mediana certificada | Escala y mezcla deben superar costos incrementales | Contenido/marketing consumen apalancamiento operativo | Alto; recalcular margen, impuestos, reinversión y DCF, no solo EBIT estático |

**Seis preguntas:** se conocen valores y cortes; histórico reconstruido; causalidad por demostrar; requiere contención de costos de contenido/tecnología; se refuta ante erosión del margen subyacente; el efecto por acción no puede afirmarse sin reconciliar primero la divergencia 21,30%/34,00%. La utilidad normalizada por el evento WBD usa una tasa fiscal hipotética de 25%; no se atribuye a crecimiento operativo.

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

El crecimiento a perpetuidad Base es **4,00%**, inferior a la Rf **4,91%** declarada. El centro publicado de WACC terminal de la matriz es aproximadamente **9,64%**, superior a g; esta relación es necesaria, no suficiente, para una perpetuidad sostenible. Según la auditoría anterior el valor presente terminal representa **54,56%** del valor operativo Base; ese porcentaje es **evidencia histórica declarada**, no una suma de FCFF reejecutada en esta revisión.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto |
|---|---|---|---|---|---|---|
| g, ROIC y reinversión terminal | Inflación y retorno a 10 años comparable N/D | g 4%; ROIC 12%; WACC terminal cerca de 9,64% | Referencias macro/industria sin corroboración externa actual | Ventaja residual suficiente para retornos sobre costo de capital | Compresión de moat, menor pricing, mayor costo de contenido | DCF depende materialmente del terminal; sensibilidad conjunta WACC×g y ROIC×g almacenada |

**Seis preguntas:** valores definidos; no hay histórico de valor terminal observable; hipótesis de ventaja es un juicio, no dato; exige permanencia de la rentabilidad; lo refuta convergencia a WACC o reinversión más alta; la cuantificación total de erosión requiere volver a calcular FCFF terminal y su valor presente.

## 10. Validación independiente del valor intrínseco

El DCF Base es **US$48,33563427** por acción (mostrar **US$48,34**). El umbral MOS 35% es **US$31,41816227**, de modo que la multiplicación Base×0,65 **concilia**. El DCF llevado a FY+3 que muestra la tabla de métodos es **US$64,22** para la historia Base; esto **no** es otro valor presente sino la capitalización con Ke a tres años. El DCF inverso publicado indica que el precio del análisis **US$65,04** exige CAGR 1–5 cerca de **16,12%** al mantener los demás supuestos Base fijos, frente al **7,99%** de Base (diferencia **8,13 puntos porcentuales**).

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto |
|---|---|---|---|---|---|---|
| DCF FCFF Base | Flujos y estados 2016–2025 + LTM; reconfirmación SEC N/D | Valor Base US$48,34; MOS US$31,42; FY+3 US$64,22 | Método FCFF/WACC Damodaran | Márgenes y reinversión explican valor operativo | Valores de flujos/terminal o puente EV→equity mal vinculados | 124 pruebas históricas declaradas, no una nueva reproducción integral del FCFF por año |

**Seis preguntas:** método, valor y fecha identificados; flujos históricos existen; precio actual no justifica flujos; supuestos exigen crecimiento/margen/reinversión coherentes; falsadores incluyen fallos de datos de origen y descuento; la pantalla integral reproduce las conciliaciones que admite el JSON, pero **no certifica todas las fórmulas originales**.

## 11. Cuatro historias y probabilidades

| Historia | Crecimiento CAGR 1–5 | Margen EBIT objetivo | S/C | ROIC terminal | g terminal | DCF por acción | Probabilidad original |
|---|---:|---:|---:|---:|---:|---:|---:|
| Conservador (B) | 5,00% | 30,00% | 1,15 | 9,64% | 3,00% | US$33,61 | 25% |
| **Base (A)** | **7,99%** | **34,00%** | **1,39** | **12,00%** | **4,00%** | **US$48,34** | **50%** |
| Optimista (D) | 11,58% | 36,00% | 1,80 | 15,00% | 4,50% | US$68,59 | 15% |

El promedio **ordinario** es (50%×48,335634 + 25%×33,606494 + 15%×68,588818) / 90% = **US$47,62**. Es secundario frente al Base. El 10% restante **no** se inventa ni redistribuye fuera de esa normalización.

### ¿Qué pasaría si todo fallara?

Disrupción (C): crecimiento CAGR aproximadamente **−2,41%**, margen **18,00%**, S/C **1,00**, g terminal **0%**, valor **US$14,78** y probabilidad original **10%**. Esta historia no entra en el promedio de tres, ni se transforma automáticamente en objetivo de mercado. Señales de confirmación/refutación requieren resultados de crecimiento, economía de contenido y márgenes posteriores.

Las probabilidades 50/25/10/15 suman 100%, pero el expediente no demuestra una calibración estadística externa de sus pesos; siguen siendo hipótesis.

## 12. Valoración por múltiplos: prueba independiente y secundaria

**Los siete** métodos figuran, incluso aquellos con peso cero. Precios y valores presentes Base en **US$/acción**:

| Método | Peso global | FY+3 Base | VP Base (criterio solo 3 años) | Estado A/B/C |
|---|---:|---:|---:|---|
| EV/EBITDA | 0% | 91,89 | 69,16 | A histórico disponible; B peers no certificados; C por verificar |
| EV/FCFF | 15% | 69,54 | 52,34 | A disponible; B no certificado; C por verificar |
| P/E | 15% | 76,63 | 57,67 | A disponible; B no certificado; C por verificar |
| P/FCFE | 15% | 60,10 | 45,23 | A disponible; B no certificado; C por verificar |
| P/OCF | 9% | 52,73 | 39,69 | OCF económico normalizado, no confundir con FCF |
| P/V | 6% | 77,55 | 58,37 | Denominador ventas, no margen/FCFF |
| P/BV | 0% | 87,46 | 65,82 | Patrimonio común y relevancia sectorial sujetos a revisión |

El valor relativo agregado Base hoy declarado es **US$50,60**, frente a DCF Base **US$48,34**. Los múltiplos no definen por sí mismos el valor intrínseco. El peso global DCF es 40% y los relativos 60%; se requiere comprobar la adecuación de cada denominador, las acciones diluidas, el puente EV→equity y la ausencia de doble conteo de dividendos. Los anclajes A (historia), B (pares), C (fundamentos) deben justificarse individualmente y no calibrarse para igualar el DCF. **N/D de B o C no significa que la fórmula aritmética de FY+3 esté rota.**

## 13. Sensibilidades económicas y escenarios alternativos

La hoja publicada incluye sensibilidad DCF Base frente a **WACC terminal × crecimiento perpetuo**, **ROIC terminal × g** y **margen sostenible × desplazamiento de crecimiento 1–5**. El centro visible de la primera matriz (**WACC terminal 9,64% y g 4,00%**) devuelve aproximadamente **US$48,34**, pero no se volvió a ejecutar cada combinación de flujos desde la hoja fuente aquí.

El DCF inverso contrasta crecimiento Base 7,99% con el **16,12%** necesario para justificar US$65,04 **bajo el conjunto de premisas restante fijo**. La diferencia no prueba por sí sola un precio erróneo; obliga a narrar qué aceleración adicional de monetización sería necesaria.

La corrida registra **7 centros Base** de múltiplos contrastados y **14** combinaciones de sensibilidad Conservador/Optimista como N/D. Existen proyecciones de precios para esas historias, pero **no** se declara que sus matrices completas fueron auditadas. Ejes exigidos: múltiplo real en veces y denominador económico FY+3 en sus unidades, con resultado valor por acción descontado; el eje fraccional 0,8–1,2, solo, no cumple el contrato editorial. La familia económica A/B/C requiere revisión de centros antes de tratarla como evidencia.

## 14. Coherencia de hojas, cálculos y presentación

El expediente previo declara 124 controles numéricos, 28 fórmulas críticas, 20 preflight estructurales y cero errores almacenados en 7.528 celdas de fórmula. Ese éxito **no certifica fuentes SEC ni razonabilidad de supuestos**. Corrigió tratamientos de BPA básico/diluido, faltantes no convertidos en cero, referencias de industria, partidas de tecnología/desarrollo y desfase inicial. El informe previo también confirma que el valor principal es DCF Base y que disrupción permanece aislada.

**Control abierto prioritario:** «Supuestos Recomendados» = margen objetivo 21,30% en «Valor actual (Input sheet)» frente a 34,00% en el escenario Base estructurado. Requiere localizar celda, fórmula y vigencia de cada artefacto; no corregir una cifra con otra por intuición.

Control adicional: fecha del precio del análisis separada del precio de hoy; MOS solo sobre Base; datos financiero/estadístico en nivel 2; matrices con unidades; enlaces a hoja, JSON y auditoría. Se inspeccionó el registro publicado, no se afirma sincronización bidireccional comprobada.

## 15. Hallazgos priorizados y propuestas de corrección

| ID | Severidad | Tipo | Evidencia y efecto | Acción propuesta | Estado |
|---|---|---|---|---|---|
| NFLX-01 | **Alto** | Supuesto/versión | Margen objetivo Input 21,30% frente a Base 34,00%; podría mover materialmente el FCFF | Leer celdas y reconciliar fórmula/override; mantener DCF vigente hasta verificar | Abierto |
| NFLX-02 | Alto | Fuente/ajuste | Tratamiento fiscal WBD al 25% estimado, sin efecto fiscal exacto | Reconstruir ingreso no recurrente y nota fiscal | Abierto |
| NFLX-03 | Alto | Comparables | Siete pares/métricas sin homogeneidad certificada, ancla C sin control universal | Revisar A/B/C por método, ROIC, growth, margen, deuda y denominador | Abierto |
| NFLX-04 | Medio | Riesgo | CRP 50 pb y Kd 5,85% estimados; potencial solapamiento de prima país | Revisar construcción fechada de WACC y alternativas | Abierto |
| NFLX-05 | Medio | Reinversión | S/C 1,39 tomado de agregado sectorial para margen incremental | Comparar serie propia, inversión en contenido e incremental ROIC | Abierto |
| NFLX-06 | Medio | Opciones | Plazo 4,5 años supuesto vs dato anterior 4,79 | Sensibilidad en expediente; localizar nota exacta Sep2026 | Abierto |
| NFLX-07 | Medio | Terminal | ROIC 12% persistente sin prueba de moat duradero | Probar convergencia a WACC y recalcular sensibilidad de FCFF | Abierto |
| NFLX-08 | Medio | Presentación/matrices | 14 controles de sensibilidad de historias relativas N/D | No describirlos como probados; completar solo con ejes reales y centros | Abierto |
| NFLX-09 | Medio | Contabilidad/normalización | I+D elegible no aislada; FCFF/OCF con aproximaciones; partidas N/P | Separar datos reportados, ajustes y no disponibles | Abierto |
| NFLX-10 | Medio | Documento | Sin validación nueva de todas las fuentes originales y de 18 bloques económicos | Completar evidencia y validar manualmente esta estructura ampliada | Abierto |
| NFLX-11 | **Alto** | LTM/flujo | Tres líneas de contenido no concilian FY2025+9M2026−9M2025 (diferencias > US$2.000 millones cada una) | Reconstruir línea, corte, definición y notas SEC; revisar impacto en reinversión/FCFF | Abierto |

Ningún hallazgo se marca resuelto por haber añadido una sección textual. Propuestas de corrección **no** equivalen a autorización para cambiar los datos.

## 16. Catalizadores, señales de refutación y seguimiento

| Indicador | Observado en expediente (fecha) | Señal favorable para revisar | Señal adversa | Fuente y frecuencia |
|---|---|---|---|---|
| Crecimiento de ingresos LTM | 14,65%, sep2026 | Crecimiento sostenido suficiente para primera proyección 10% | Caída persistente bajo la trayectoria Base | Estado trimestral, comparar LTM homogéneo |
| Margen EBIT LTM | 31,30%, sep2026 | Expansión sostenible hacia 34% con normalización documentada | Reversión de margen tras mayores costos de contenido/marketing | 10-Q / reportes trimestrales |
| ROIC LTM | 38,58%, sep2026 | Retorno económico compatible con reinversión eficiente | Deterioro material por capital de contenido/adquisiciones | Estados + reconstrucción anual |
| Margen FCF LTM publicado | 22,87%, sep2026 | Conversión a caja que acompañe el EBIT | Brecha caja-beneficio persistente o SBC/capex subestimado | Cash Flow Statement cada trimestre |
| Número de acciones | 4.106,33 millones, LTM | Dilución/compras reconciliadas con valor por acción | Opciones/SBC e instrumentos dilutivos no recogidos | Notas y acciones diluidas, trimestral |
| Costo de capital y terminal | Centro WACC terminal ~9,64%, g 4% | Riesgos reales justifican tasa terminal y moat | Aumento de WACC, descenso ROIC/g o prima país duplicada | Treasury, Damodaran, notas deuda; revisión por corte |

Los umbrales de «señal favorable/adversa» son **criterios propuestos para seguimiento**, no guía oficial de Netflix. No se afirma calendario de resultados futuros sin fuente confirmada.

## 17. Dictamen económico y resumen para escuchar

**Tesis: plausible con reservas.** Matemáticamente, el expediente contiene controles técnicos anteriores y las conciliaciones básicas reproducibles; documentalmente faltan confirmaciones de ajustes y fuentes; económicamente hay hipótesis exigentes de margen, reinversión y rentabilidad terminal. La discrepancia del margen entre artefactos es el bloqueo concreto más inmediato. El supuesto defendible es la moderación del crecimiento respecto del mejor pasado; los más frágiles son sostenibilidad del margen 34%, intensidad de capital marginal y ROIC terminal. El mercado al precio fechado US$65,04 supera el DCF Base US$48,34 en alrededor de **34,56%**; se trata de una comparación de supuestos a una fecha, no recomendación de operar.

### Resumen para escuchar

Netflix presenta una historia económica en la que el crecimiento se modera, pero la eficiencia operativa puede sostener el valor. Su valoración principal, el DCF Base, es de unos cuarenta y ocho dólares por acción; el precio del análisis era sesenta y cinco. El modelo exige un margen operativo objetivo de treinta y cuatro por ciento. Sin embargo, una hoja de supuestos muestra veintiuno coma tres por ciento: esa diferencia debe resolverse antes de considerar cerrada la auditoría. El crecimiento implícito que justificaría el precio del análisis es considerablemente mayor que el crecimiento Base proyectado. Las pruebas anteriores avalan diversas conciliaciones, pero no certifican las fuentes, la selección de comparables ni las ventajas competitivas de largo plazo. Por eso la valoración se mantiene **con reservas** y sin modificación de sus cifras.

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

**Versión de auditoría:** ampliación narrativa basada en el prompt `auditoria-economica-jmr-v1.2` y el expediente NFLX fechado 21-oct-2026. **Estado: AUDITORÍA CONDICIONADA**, por verificación económica y documental pendiente. Las pruebas anteriores de 124 controles, 28 fórmulas críticas y lectura de matrices siguen referidas a su corrida original; no se ejecutaron nuevamente por el mero acto de editar este Markdown. El texto permanece editable y versionado en GitHub. **No se modificó la valoración.**
