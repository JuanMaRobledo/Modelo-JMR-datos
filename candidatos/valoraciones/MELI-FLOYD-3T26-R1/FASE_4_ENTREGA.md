# F4 · MELI-FLOYD-3T26-R1 · CANDIDATO

**MELI · Floyd · acción ordinaria Nasdaq · USD.** Corte contable 30-sep-2026, precio US$1.510 al 6-nov-2026. Corrección del 8-nov-2026 (Colombia). OpenAI Codex en ChatGPT Work, familia GPT-6, variante y esfuerzo no expuestos a la sesión. Rama `meli-floyd-3t26-r1`, base de trabajo `451d84ba675f42998c2488d5f617acd9c19d2f57`, [PR #260](https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/260).

[H1](https://docs.google.com/spreadsheets/d/1TF8KaMkn-Wc3csoCK1z9-IierhPhOBZwwdX7fiBYN6Q/edit) · [H2](https://docs.google.com/spreadsheets/d/1wkFwjzufTR8KqrLSc7gxmxuB_qepFjEDc-LMuFi5oR0/edit) · [Documento de análisis](https://docs.google.com/document/d/1bv2hPD1XvgVM2Vz3WjQdX8Sh1bLo0FXEhqPc3GZCxVk/edit) · [Análisis versionado](ANALISIS_N1_N2.md) · [Cierre F3](FASE_3_ENTREGA.md).

**PASOS F4 0/3 cerrados de punta a punta.** Edición del candidato completada y controles de catálogo vigente ejecutados. El cierre previo F2/F3 y la integración de MELI siguen pendientes.

| Control | Estado | Evidencia |
|---|---|---|
| Identidad y corte de artefactos | APROBADO | Metadatos de Google y rutas del PR. H1, H2 y la Maestra tienen IDs distintos. Aislamiento integral no declarado. |
| Estructura editorial candidata | APROBADO | Nivel 1 de 14 capítulos y Nivel 2 de 12 apartados verificados por conteo de encabezados en Git y relectura del documento nativo. Base SOTP N/D y única definición del inverso. Las cifras de la réplica se limitaron a la conciliación histórica. |
| Profundidad y conciliación financiera MELI | PARCIAL | Se conserva el análisis de hechos, ciclos, tres historias y puente de fuentes. Falta la evidencia de una foto H2 oficial para completar resultados, comparables y matrices. |
| Catálogo vigente | APROBADO | `node scripts/validar_catalogo.cjs` exit 0 en la rama. MELI R1 sigue fuera del catálogo activo. Este resultado no acredita a MELI. |
| Profundidad estructural del catálogo vigente | APROBADO | `node scripts/validar_profundidad_floyd.cjs` exit 0. UBER y CMG evaluadas. El script emitió aviso editorial de UBER. MELI R1 queda fuera del alcance. |
| Hoja → JSON → visor y control visual de la app para MELI | NO_EJECUTADO | Base, esperado, MOS, inverso y anclas oficiales N/D. Sin JSON de publicación ni promoción de MELI. |
| F5 | NO_EJECUTADO | Auditoría económica reservada a sesión independiente. |

**Estado CANDIDATO.** Sin cambio de catálogo ni despliegue. La huella de H2 se verificó en el alcance indicado en F3.

**Primer siguiente paso exacto.** Cerrar las aperturas de Fintech en H2 `Tesis de Inversión y Supuestos!B81:F81`, `B93:F93` y `B105:F105` y anexar el resultado atribuible a cada bloque con eliminaciones. Solo después se activan DCF/inverso y múltiplos, se extrae JSON y se ejecutan los controles de MELI en el visor.


## Verificación incremental · 8-nov-2026 · GPT-6 (ChatGPT)

Modelo/herramienta real: GPT-6 con conectores GitHub y Google Drive/Sheets/Docs y cotejo SEC; esfuerzo de razonamiento no expuesto. No se utilizaron Work, terminal Node/Python, CI, Vercel ni visor autenticado. Mismo PR #260, revisión y rama.

| Control | Estado actual | Evidencia y límites |
|---|---|---|
| Corrección de fuente primaria en análisis | APROBADO | El Google Doc existente y el análisis versionado ANALISIS_N1_N2.md incorporan en Nivel 2 §4: (a) los fondos de clientes no fondean la cartera, (b) las medidas de liquidez US$8.126m y US$6.902m no son caja libre de Commerce, (c) grupo emisor/garantes S-X 13-01 no equivale a Commerce o Fintech. Concuerda con H2 Tesis de Inversión y Supuestos!D44/D56/D61/D66. Lectura posterior de Sheets y Docs confirmó las ediciones. |
| Nivel 1 (14 capítulos) y Nivel 2 (12 apartados) | PARCIAL para F4 financiera | Se conserva la estructura de la revisión con un único valor central SOTP=N/D. Las cifras de corridas Python anteriores figuran solo en conciliación. Faltan proyección H2, inverso, sensibilidad y múltiplos reales para completar tablas y juicio sobre precio. |
| Integridad / fórmula | PARCIAL | Huella motor!F2:F3 leídos directamente: 0 diferencias dentro de 1.883 fórmulas registradas. No se ejecutó diff integral externo. Control de integridad!B2=PLANTILLA y B4=0/3 LISTO, de modo que no hay gate de empresa. |
| Hoja→JSON→visor MELI y validadores de publicación | NO_EJECUTADO en esta sesión | No hubo extracción JSON ni validación de MELI con node scripts/validar_catalogo.cjs, ni de profundidad Floyd, ni QA visual de app. Los exits 0 registrados en la entrega anterior comprobaron otro catálogo con MELI Floyd fuera de su alcance. No se publicaron ni fusionaron cambios. |
| Catálogo por lectura, no por validador | APROBADO para alcance de lectura | catalogo.json de main y de la rama conserva idéntico SHA c7e6e771c29f74813b319adc828b68f6255b0bbc: MELI Floyd R1 no aparece en valoraciones ni analisis activos; A3 aparece solo en archivoFloyd. Esta comprobación de contenido no sustituye node scripts/validar_catalogo.cjs. |
| Auditoría F5 | NO_EJECUTADO | Reservada por contrato a otra sesión/revisor. |

Resultado: CANDIDATO, no EN_REVISION. PASOS F4 de punta a punta siguen 0/3; esta corrección editorial no sustituye el cierre económico de F3. El análisis no puede declarar una cifra central hasta que el motor H2 la produzca.

Primer siguiente paso exacto: completar H2 Tesis de Inversión y Supuestos!B81:F81, B93:F93 y B105:F105 con aperturas por entidad y eliminaciones; adjuntar utilidad atribuible a Mercado Pago y EBIT Commerce/corporativo; después ejecutar SOTP/DCF inverso/múltiplos/matrices de la misma H2 y los gates, incluido node scripts/validar_catalogo.cjs, antes de cualquier EN_REVISION.


## Corrección visual de libros · 8-nov-2026 · GPT-6 (ChatGPT)

- **APROBADO — Presentación visible:** H1 y H2 cuentan con pestaña `Presentación` sin imágenes; H1 resume históricos reales desde `Resumen/Resultados/Balance/Flujos`; H2 muestra precio de corte US$1.510, método SOTP y DCF Base/MOS/esperado **N/D** hasta que lo calcule H2.
- **APROBADO — disposición visual:** H1 contiene 19 pestañas, 11 normalizadas de estados/ratios antes de las fuentes SEC. H2 oculta de modo reversible las 11 pestañas históricas dependientes del motor.
- **PARCIAL — separación real:** los tabs históricos continúan en H2 (ocultos), porque eliminarlos produciría referencias rotas en `Input sheet`, `Trailing Valuation` y módulos vinculados. No se afirma que la transferencia H1→H2 ni la migración estén terminadas.
- **APROBADO en alcance registrado — huella:** relectura `Huella motor!F2=0`, `F3=1883`. **NO_EJECUTADO** control integral de eliminación/sincronización ni `validar_catalogo.cjs` para MELI.
- **Estado CANDIDATO:** análisis y salida siguen N/D por faltantes de perímetro SOTP. Sin publicación; F5 independiente.

**Primer siguiente paso exacto:** migrar y probar los vínculos históricos H1→H2 para poder retirar físicamente las pestañas ocultas; completar independientemente apertura por entidad, EBIT Commerce y utilidad/FCFE de Mercado Pago antes de activar cifras de valoración.


## Estado de entrega tras reestructuración definitiva · 8-nov-2026 · GPT-6 (ChatGPT)

La sección previa «once pestañas ocultas» quedó **SUPERADA**: H2 conserva **45** pestañas y las once históricas fueron **eliminadas físicamente** después de migrar sus datos/415 referencias a una sola `Traspaso H1`, de origen estático (sin IMPORTRANGE). H1 contiene **19** pestañas con Presentación y paneles de estados/ratios normalizados; las dos Presentaciones carecen de imágenes. Pruebas: **12.155 celdas**, **1.554 valores**, **0 diferencias** fuente/traspaso; lecturas de la huella 0 diferencias sobre 1.883 fórmulas registradas; no hay vínculos remanentes a las pestañas eliminadas en el alcance escaneado.

Se actualizó **el mismo** Google Doc Nivel 1/Nivel 2 y `ANALISIS_N1_N2.md` para añadir: desglose de ingresos LTM (Commerce 21.749 y Fintech 16.774 US$m), alcance F2 y sincronización no automática, I+D como proxy y deuda US GAAP arrendamientos. No se cambiaron 14 capítulos ni 12 apartados.

**F4 SIGUE NO COMPLETADA:** faltan importes del SOTP oficial, N1/N2 cuantitativos de esos importes, matrices, valor inverso, anclas, gates de MELI, JSON de publicación, catálogo y QA de app. `Input sheet!A1` está en blanco a propósito porque activarlo antes de completar la economía producía errores de división por cero; ninguna valoración fue calculada. F5 queda reservada a auditor independiente. **No publicar ni pasar a EN_REVISION; estado CANDIDATO.**

**Primer siguiente paso material:** publicar por fuente entidad los tres bloques de apertura de Fintech en `Tesis de Inversión y Supuestos!B81:F81, B93:F93, B105:F105`, el EBIT Commerce/corporativo y el resultado de Mercado Pago con eliminaciones, cargas de capital y fondeo. Ejecutar posteriormente los tres escenarios, SOTP, múltiplos, matrices, inverse DCF y validación de JSON/catálogo/visor sobre ese libro.


## F4 · actualización por conciliación externa del 8-nov-2026

El análisis Nivel 2 existente y el documento Google nativo fueron ampliados **sin cambiar los 14 capítulos del Nivel 1 ni los 12 apartados del Nivel 2**; el anexo reconcilia datos SEC FY25/3T26, AZ Stocks y otros valuadores con la hoja H2 de esta **misma revisión**.

La simulación SOTP condicional de la Base fue **corregida de US$908,88→US$971,35/acción** por doble uso de intereses/FX corporativos frente a bonos. Conservadora393,31, Optimista1.806,77, esperado1.039,48, MOS condicional631,38; todas esas cifras son H2 Tesis, **no DCF/SOTP oficial**. Reconciliación NOPAT–NI 0, cuatro identidades FCF ajustado cero, 0 errores rango evaluado, huella registrada 0/1.883. Se documenta brecha AZ US$2.339 y terminal 13× EBITDA no equivalente a perpetuidad.

**F4 sigue 0/3 oficial**: Base/MOS/esperado oficiales en Presentación H2 continúan N/D, Input A1 vacío por protección, 0/3 escenarios oficiales listos, sin nuevos JSON/catálogo/visor, sin publicación ni fusión. F5 reservada. [FASE_3_ENTREGA.md](FASE_3_ENTREGA.md) documenta controles realizados y no ejecutados.


## F4 · actualización de conclusiones económicas V4, mantener candidato (8-nov-2026)

El análisis Google Docs N1/N2 y el markdown `ANALISIS_N1_N2.md` recibieron un anexo detallado de la **nueva valoración condicional V4**, sin reemplazar el Nivel 1 de 14 capítulos, el Nivel 2 original de 12 secciones ni crear otra revisión. H1 `Mercado Pago!A30:E52` incorpora un ancla parcial de capital regulatorio brasileño IF.data BCB, separado de los estados SEC y en reales brasileños; H2 `Tesis!A121:L584` incorpora crecimiento y margen por Commerce/Fintech, S/C terminal calculado con ROIC, retención mínima económica crediticia y 4 matrices 5×5 exactas.

**Resultado de contraste, no oficial:** conservadora **444,72**, Base **1.022,40**, optimista **1.624,71**, esperado **1.028,92**, MOS35% condicional **664,56 USD/acción**. DCF inverso aproximadamente 20,1% margen EBIT Commerce terminal para precio6-nov26 US$1.510. F3 incluye cifras anteriores y puente de auditoría; el cambio final desde la versión V3 US$1.053,41 proviene de moderar ROE marginal Fintech22→19 y ROE terminal15→14 al contrastar Brasil IF.data. La fuente Brasil NO permite convertir capital a equity distribuible mundial.

Pruebas: cuatro centros de matrices igualan Base1.022,3986; convergencia ROIC_incremental año10 al objetivo cero; piso de retención crédito verificado, bisección inversa 26 iteraciones error ~0,00002; barrido de 44 pestañas no puente con ~24.407 fórmulas y 0 errores; huella de 1.883 registrada con 0 diferencias; H1 flujos SEC ajustados 4/4. **Estos son controles técnicos internos, NO el CI externo, NI las compuertas económicas/F5**.

**Estado oficial sin cambiar: CANDIDATO; PR #260 abierto en borrador.** En `Input sheet!A1` se conserva vacío el disparador; `Presentación` muestra precio mercado y los tres valores oficiales N/D; el bloque condicional separado se etiqueta como tal; 0/3 historias oficiales LISTO. F4 no puede concluir sin EBIT Commerce verificado, utilidad Fintech por entidad, RWA/patrimonio/regulación por país y cash/deuda intragrupo, Ke/WACC y anclas por múltiplos; no se publica, no se fusiona, no se falsea un MOS.



## Control F4 complementario y prohibición de publicación artificial · 8-nov-2026 · GPT-6

**Ejecutor de este control:** GPT-6, ChatGPT con conectores GitHub/Google Drive; esfuerzo de razonamiento no expuesto. **Revisión:** MELI-FLOYD-3T26-R1; corte 30-sep-2026; precio de referencia US$1.510 (06-nov-2026). Lectura directa de documentos existentes y fuentes SEC/NYU/U.S. Treasury. No se ejecutaron en este tramo comandos locales Node/CI, auditoría F5 ni QA visual autenticado.

El informe existente conserva sus **14 capítulos Nivel 1** y **12 apartados Nivel 2**, revisión única y anexos condicionales. Se identificó evidencia nueva de compromisos cloud/logística/almacenes (US$1.695m, US$263m y US$2.116m pendientes) y recurso limitado de las titulizaciones de crédito. Se añadió nota económica a la misma revisión, sin asignar todo el gasto al año 1 ni deuda no atribuida a Commerce. Fuente: [10-Q 3T26](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000029/meli-20260930.htm).

**Lecturas directas de H2:** `Input sheet!A1` sigue en blanco; `Cost of capital worksheet!B14` condicionado/no valorado, selectores B22/B26 sin cierre; `Tesis!B61:C66` y aperturas `B81:F81/B93:F93/B105:F105` N/D; `Escenarios e historias!H5/H6/H8` sin valor oficial, `K5/K6/K8` PENDIENTE. El libro muestra explícitamente Base/Esperado/MOS N/D y evita pasar al catálogo el V4. La simulación V4, aunque con grillas 5×5 y comprobaciones internas anteriores, no reemplaza un FCFE bancario ni una foto nativa de `Valuation output`.

**Gates de publicación MELI:** integridad selectiva de celdas **APROBADO por lectura**, separación H1/H2 **APROBADO por metadatos**, revisión económica Commerce/Fintech **BLOQUEADA materialmente**, DCF/SOTP Floyd nativo **NO_EJECUTADO**, múltiplos por bloques y sensibilidad oficial **NO_EJECUTADO**, JSON/catálogo/CI/visor **NO_EJECUTADO**, QA visual **NO_EJECUTADO**, F5 **RESERVADA A INDEPENDIENTE**. La rama PR #260 se mantiene **abierta en borrador**; MELI Floyd no está en el catálogo activo y su antecedente A3 figura en el archivo. No fusionar, sustituir ni publicar en estas condiciones. Se evita que un candidato no calculado sustituya indebidamente la ficha vigente.

**Primer siguiente paso exacto:** cerrar F3 con saldos iniciales y utilidad/EBIT por segmento y país, deducir capital efectivamente liberable y comprobar Ke/WACC; luego ejecutar H2 nativo, cinco métodos/matrices pertinentes y gates MELI, y solo entonces completar F4/pasar a EN_REVISION si todo aprueba. La auditoría F5 permanece fuera del alcance.


## Continuación F4 · 9-nov-2026 · presentación Commerce-only sin Fintech

Se recibió orden de **valorar exclusivamente Commerce sin sumar la parte Fintech**. Se documentó en el **mismo** expediente, libro H2 y análisis nativo la **subvaloración condicional**: Conservadora EV US$17.466,30m/US$344,52 EV por acción, Base EV US$42.059,11m/**US$829,62 EV por acción**, Optimista US$65.323,95m/US$1.288,52 EV por acción. Esperado EV US$41.707,59m/US$822,69 EV/acción. Si se asignan **hipotéticamente** US$2.253m de bonos corporativos a Commerce, equity Base ilustrativo es US$39.806,11m/**US$785,18 por acción**, MOS35% sobre ese equity supuesto **US$510,37**. El valor intrínseco de la acción completa MELI es N/D: omitir Fintech no lo convierte en cero económico.

Se añadieron fórmulas enlazadas y matriz 5×5 `Tesis de Inversión y Supuestos!A586:J605` sin alterar fórmulas madre ni la pestaña de valoración principal. Lectura posterior confirmó centro `D600=829,62` y residuo `B603=0,0000`; 0/3 historias oficiales LISTO, `Input sheet!A1` vacío. La dependencia del VP terminal Commerce Base es 95,07%; margen inicial Commerce y asignación de costes corporativos no divulgados por vertical, WACC y deuda/activo segregados aún no están validados. Los resultados no se mezclan con SOTP V4 ni se envían al JSON/catálogo.

**Estado: CANDIDATO.** Se efectuaron la lectura/escritura/relectura parcial de H2 y actualización documental. **NO_EJECUTADO:** CI de publicación de MELI, prueba integral del modelo, extracción JSON, fusión, despliegue, QA visual o auditoría F5. La orden de omitir Fintech **no** autoriza presentar Commerce EV/acción como valor oficial de MELI.

**Primer siguiente paso exacto:** completar EBIT y costes corporativos atribuibles a Commerce, deuda neta segregada y WACC de la unidad; comprobar ajuste económico de flujos por servicios de pago prestados por Fintech antes de activar el FCFF principal y aspirar a EN_REVISION.
