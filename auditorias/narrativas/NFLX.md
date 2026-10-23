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

**Salvedades económicas que permanecen abiertas, ordenadas por su posible efecto:** (1) demostrar la persistencia del ROIC terminal 21,52% frente al WACC 9,16% y la industria 11,04%; (2) verificar que Sales-to-Capital Base 2,00x y la reinversión neta representen realmente el costo de renovación y monetización del contenido; (3) recalcular y justificar pares y anclas de los siete múltiplos, en particular EV/FCFF, P/FCFE y tratamiento del EBITDA de contenido; (4) atribuir la prima país extra de 0,50 puntos porcentuales y el costo de deuda a fuentes y exposición geográfica; (5) normalizar el cobro extraordinario WBD de US$2.800 M y confirmar el impuesto aplicable; (6) comprobar opciones/SBC, arrendamientos, acciones promedio ajustadas por split y efecto neto de recompras; (7) analizar efectos de incentivos del proxy disponible, TAM geográfico monetizable, cohortes/retención y publicidad comparables, si la información pública existe.

**Criterio operativo de publicación:** el registro de valoración existente puede mostrarse y utilizarse con estas advertencias porque su hipótesis base es explícita y reproducible. **No debe sustituirse por un recálculo procedente del extractor nuevo** hasta confirmar cobertura material, preservación de fórmulas y validaciones de Sheets, DCF, múltiplos y control integral. Un problema de CI no prueba por sí solo un DCF incorrecto; un CI verde tampoco demuestra que todos los supuestos económicos sean plausibles. La incertidumbre se muestra en la auditoría, no se oculta ni se convierte en datos inventados.

**Fuentes y trazabilidad de esta actualización:** [SEC 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm), [carta Q3 2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm), [PR #137](https://github.com/JuanMaRobledo/JMR-valuation/pull/137), [pruebas SEC aprobadas](https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/40017974176), [workflow de liberación](https://github.com/JuanMaRobledo/JMR-valuation/actions/workflows/nflx-final-gate-20261022.yml). Revisión financiera: `NFLX-2026-10-22-SEC9M26-JMR-review-001`; revisión editorial original v5 preservada. Actualización limitada a auditoría y controles, sin modificación del DCF.

### Cierre probatorio de salvedades — fuentes SEC verificadas, 23-oct-2026

**Alcance del cierre.** Cada punto se distingue entre **HECHO CERRADO**, **HIPÓTESIS JUSTIFICADA CON RESERVA** y **NO CERTIFICABLE CON LA INFORMACIÓN ACTUAL**. Una justificación económica razonada no convierte una proyección en un hecho ni obliga a alterar el DCF. Se conserva la revisión financiera `NFLX-2026-10-22-SEC9M26-JMR-review-001` y su valor Base US$69,94; no se ha calculado una nueva valoración. Las cifras monetarias SEC de esta sección se expresan en millones de USD salvo indicación distinta. Fuente principal: [Netflix 10-Q SEC Q3 2026, presentación 21-oct-2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm), y [carta Q3](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm). La verificación es de hechos publicados y reconciliaciones descritas, no una auditoría externa.

| Riesgo o salvedad | Conclusión probatoria | Efecto sobre la decisión |
|---|---|---|
| Ausencia del proxy y compensación de ejecutivos | **HECHO CERRADO:** existe [DEF 14A de 16-abr-2026](https://www.sec.gov/Archives/edgar/data/1065280/000119312526159286/d20613ddef14a.htm); documenta remuneración e incentivos | Retirar «proxy 2026 no obtenido». Queda como riesgo económico si los incentivos mejoran el valor por acción |
| Opciones, RSU/PSU, split y recompra | **HECHO CERRADO en cantidades SEC**; valorización exacta de opciones **por conciliar** | No presumir cero dilución ni deducir que las recompras siempre agregan valor |
| Cobro WBD y clasificación | **HECHO CERRADO:** US$2.800 en «Interest and other income», fuera del EBIT; incluido en CFO | No se incorpora a EBIT/FCFF recurrente; el impuesto atribuible al ingreso no está revelado separadamente |
| Contenido y caja | **HECHO CERRADO en pagos/amortización/obligaciones**; **HIPÓTESIS** en productividad marginal futura | La Base S/C 2,00x requiere sensibilidad y vigilancia, no certificación ex ante |
| ROIC terminal 21,52% | **HIPÓTESIS EXIGENTE**, no verificable de forma definitiva antes de la perpetuidad | Mostrar ROIC=WACC US$56,08 y ROIC 12%=US$61,79 junto a US$69,94 |
| Prima geográfica 0,50 pp / Kd | **JUICIO DE ANALISTA**, no tasa observada ni CRP por países reconstruida | Mantener como reserva explícita; análisis de sensibilidad y futura reconciliación |
| Anclas de siete múltiplos | **VALORES CALCULADOS**, pero comparabilidad y archivos de cotización contemporáneos **no certificados** | Uso secundario, nunca sustituye DCF Base |
| Cohortes, churn, TAM e ingresos publicitarios por unidad | **EVIDENCIA PARCIAL**: orientación cualitativa y publicidad reportada; no series homogéneas completas | No fabricar monetización individual/cohortes ni TAM regional |
| 294 huecos del nuevo extractor SEC | **LIMITACIÓN DEL EXTRACTOR DE PR #137**, no 294 errores verificados en el DCF actual | Exigir clasificación por materialidad/periodo; no sustituir por cero ni activar publicación automática |

**1. Ingresos, crecimiento y margen EBIT — defendibles como proyección, no como promesa.** El 10-Q Q3 registra ingresos trimestrales US$12.874,18 M (+11,8% interanual) y la carta estima para FY2026 US$51.100 M, aproximadamente +13%, con margen operativo 31,5%. La Base 12%→11%→10%→9%→8% a cinco años (CAGR 9,99%) es prudente **respecto del dato reciente**, pero depende de continuidad de precios, retención, publicidad y expansión internacional; no se extrapola el crecimiento histórico de penetración inicial. EBIT objetivo36% en cinco años es una expansión de 4,5 pp frente a la guía 2026, plausible con escala y publicidad, pero no garantizada. Optimista40% exige mucha más productividad; Conservadora32,5% es una historia alternativa. El EBIT GAAP excluye el ingreso extraordinario WBD, que se contabilizó por debajo de resultado operativo. [10-Q: resultados y segmentación](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm); [carta Q3 2026, guía](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm).

**2. Contenido, FCFF y Sales-to-Capital — evidencia real, productividad futura no demostrada.** Los primeros nueve meses de 2026 registran adiciones/pagos operativos por activos de contenido de US$14.934,23 M y amortización de contenido de US$12.764,66 M; razón de **1,17x** y diferencia neta **US$2.169,57 M** antes de efectos de pasivos de contenido y otras partidas. Netflix prevé aproximadamente 1,1x para el año completo. El balance al 30-sep tiene activos netos de contenido **US$34.605,48 M**; los compromisos futuros contractuales suman **US$25.222,80 M**, sin que esto represente íntegramente deuda financiera. El desembolso de PPE de nueve meses fue US$693,54 M, **no** toda la reinversión económica. Una S/C Base de 2,00x en años1–5 y1,60x en6–10 es una convención de retorno sobre inversión incremental entre observaciones históricas muy distintas (1,09x a 4,57x según ventana), no una medida de productividad demostrada. La hipótesis es **plausible con reserva material**: valorar una plataforma de contenido como si solo invirtiera en PPE sería un error. No se cambian los US$69,94 sin un replay completo de ingresos, reinversión y valor terminal. [10-Q estado de flujos, nota5 y nota9](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm); [carta Q3: ratio ~1,1x](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm).

**3. ROIC, duración del foso y perpetuidad — no puede cerrarse como hecho.** El ROIC contable LTM documentado en el modelo (35,87% capital final o38,58% capital medio) describe rendimientos pasados que incorporan recompras y capital contable. El ROIC **terminal** 21,52% fue un juicio de modelación entre observación ajustada y referencia de industria (11,04%), no una cifra SEC. El spread de ROIC terminal sobre WACC9,16% equivale a **12,36 puntos porcentuales** sostenidos indefinidamente. Marca, tecnología, licencias, distribución y escala lo hacen concebible, mientras que derechos deportivos, contenido obligatorio y competencia constituyen refutaciones posibles. Como el valor presente terminal representa aproximadamente **61,96% del EV**, la hipótesis es material: US$69,94 Base frente a US$61,79 con ROIC12% y US$56,08 con ROIC=WACC. **Dictamen: conservar el Base como hipótesis exigente y nunca presentar el ROIC21,52% como certificado**. La Conservadora retiene ese ROIC; esto reduce su severidad terminal y debe seguir constando como sesgo favorable del escenario, aunque el crecimiento y márgenes sean conservadores. [Sensibilidades del expediente JMR, revisión indicada](https://github.com/JuanMaRobledo/JMR-valuation); [10-Q y compromisos de contenido](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm).

**4. WACC, riesgo geográfico y deuda — fórmula reproducible, fuente de la prima incompleta.** El libro usa WACC9,1645%, Ke9,4355%, Rf ajustada4,91%, ERP efectiva4,42%, beta reapalancada~1,024 y costo supuesto de deuda antes de impuestos **5,85%**. El manifiesto financiero define expresamente Kd5,85% como *hipótesis*, no como rendimiento de mercado de un bono específico. Se corrigió la narrativa de supuestos que mostraba erróneamente 6,18% sin corresponder al valor aplicado. La ERP madura 3,70% concuerda con la estimación implícita de [Damodaran en octubre 2026](https://aswathdamodaran.substack.com/p/earnings-cashflows-and-stock-prices); el diferencial soberano 0,22pp y la adición geográfica de **0,50pp** son ajustes del modelo, no prima país certificada. El 10-Q sí presenta ingresos UCAN, EMEA, LATAM y APAC, **pero EMEA y APAC no equivalen a un único país de riesgo** y el reparto por países no se publica allí. La adición de 0,50pp puede defenderse como amortiguador discrecional, sin presentarla como CRP Damodaran calculada por geografía; debe mantenerse la sensibilidad 0/50/100pb y evitar doble cobro de riesgo en FCFF y WACC. La deuda total SEC al 30-sep es US$15.132,39 M; la deuda económica en puente DCF es ~US$15.158 M por convenciones del modelo: diferencia pequeña que no justifica afirmar una YTM observada. [10-Q deuda y segmentos](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm); [Damodaran octubre](https://aswathdamodaran.substack.com/p/earnings-cashflows-and-stock-prices).

**5. WBD, beneficio neto y FCF normalizado — imputación correcta, tasa fiscal no identificable.** Netflix recibió en febrero 2026 US$2.800 M por la cancelación del contrato WBD; SEC confirma registro en `Interest and other income (expense)` en1T26 y entrada de efectivo en CFO. Por tanto no debe inflar EBIT, tasa de reinversión operativa ni crecimiento sostenible. CFO nueve meses fue US$10.196,30 M y FCF no GAAP US$9.502,76 M **ambos incluyen el cobro**; su remoción bruta ilustrativa antes de considerar efecto tributario deja respectivamente ~US$7.396,30 M y ~US$6.702,76 M. Esto **no equivale a FCF ajustado después de impuestos**, porque SEC no identifica la carga tributaria específica del acuerdo. La tasa efectiva observada nueve meses es 17%, mientras que el modelo usa 25% marginal para normalizar P/E. Sobre 4.251,30 M acciones diluidas promedio9M, sustraer el ingreso después de impuestos ilustrativo sería ~US$0,49 por acción al25% o ~US$0,55 al17%; el intervalo es una sensibilidad **no** una tasa fiscal atribuida a WBD. **Hecho contable cerrado; tasa fiscal específica abierta y no crucial para DCF FCFF si el cobro no se capitaliza como operación.** [10-Q nota6, flujos y tasas](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm); [reconciliación FCF en carta](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm).

**6. Acciones, opciones, remuneración y arrendamientos — documentación SEC suficiente para auditar cantidades, no valoración total de opciones.** El 10-Q identifica un split **10 por 1 del 14-nov-2025**, reexpresión retrospectiva de acciones y EPS, acciones en circulación al30-sep de **4.106,33 M**, acciones diluidas promedio9M **4.251,30 M**, opciones pendientes **120,18 M** con ejercicio promedio US$41,24, RSU/PSU no consolidadas **1,87 M** y gasto SBC9M **US$405,44 M**. Netflix recompró **130,35 M** de acciones por aproximadamente **US$10.700 M** en los nueve meses. El modelo divide el equity por **4.108,19 M** de acciones y resta un ajuste de opciones de US$4.290,87 M: la diferencia con las acciones SEC de cierre es ~1,86 M (0,05%), pero las opciones **requieren cotejo exacto de vencimientos, strikes y valoración** para descartar doble cómputo con dilución; no basta el strike medio. En la [DEF 14A 2026](https://www.sec.gov/Archives/edgar/data/1065280/000119312526159286/d20613ddef14a.htm) sí constan incentivos individuales, PSU vinculadas a TSR relativo S&P500 y RSU con consolidación temporal. Los pasivos por arrendamiento y sus activos de derecho de uso están detallados en nota5 del 10-Q y deben contarse simétricamente. **Se cierra la falsa «falta de proxy» y la falta de cifras generales de opciones; sigue abierta la reproducción independiente del ajuste US$4.290,87 M.** [10-Q nota10, split, leases y recompra](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm).

**7. Múltiplos y visibilidad de comparables — segunda opinión, no sustituto del DCF.** El expediente tiene EV/FCFF, P/E, P/FCFE, P/OCF, P/V y P/BV con pesos auxiliares, y EV/EBITDA con **peso cero** dada la no homogeneidad de amortización de contenido entre pares. La existencia de cálculos y matrices no demuestra que las anclas de cada peer usen misma fecha, enterprise value comparable, obligaciones de contenido, normalización WBD y dilución. Los múltiplos históricos/ciclo siguen informativos, pero **no pueden certificarse con el material recuperado**. Para cerrar definitivamente harían falta tabla par-a-par de precios/EV al21-oct-2026, denominadores auditados, política de amortización y descuento de FY+3 a hoy. Se mantiene la cifra secundaria publicada, sin elevar su rango a valor intrínseco. Cualquier ausencia específica deberá señalar «no observable» en vez de inventar peers o cotizaciones.

**8. TAM, publicidad, retención y cohortes — distinguir dirección estratégica de series cuantificadas.** La carta Q3 señala respuesta a aumentos de precios consistente con expectativas y mejora interanual de churn; presenta expansión del producto publicitario y nuevos países para2027, y un ejemplo regional de India con crecimiento de horas de visualización del24% y de ingresos FX-neutrales de aproximadamente18% enQ3. El [proxy](https://www.sec.gov/Archives/edgar/data/1065280/000119312526159286/d20613ddef14a.htm) informa que el ingreso por publicidad 2025 superó US$1.500 M. Ninguno de esos hechos aporta **márgenes unitarios de la publicidad por país, cohortes completas o un TAM regional monetizable uniformemente**. Por tanto, la hipótesis de publicidad en la Base es respaldada en dirección, no en cada unidad de flujo descontado. [Carta Q3](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm); [proxy 2026](https://www.sec.gov/Archives/edgar/data/1065280/000119312526159286/d20613ddef14a.htm).

**9. Extracción y control de liberación — decisiones independientes del juicio económico.** El PR [#137](https://github.com/JuanMaRobledo/JMR-valuation/pull/137) incorpora caché por URL+SHA, bloqueo conservador y pruebas SEC; **sus 294 huecos no demuestran por sí solos que 294 cifras oficiales de la hoja sean erróneas**. Sin inspeccionar la lista detallada y clasificarlos en críticos / suplibles por fuente primaria / no material / no aplicable, no puede certificarse el importador automático. Separadamente, los intentos del `release gate` encontrados mostraron falsos positivos del detector de integridad sobre supuestos manuales y rótulos; se reforzó la comparación de crecimientos de los diez años y terminal contra valores versionados. La **publicación de la auditoría narrativa no equivale a un gate completo verde del proceso financiero**. Registrar una corrida verde requiere URL y SHA exactos; no alterar la historia de resultados para esconder fallas. [Pruebas SEC](https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/40017974176); [revisión integral](https://github.com/JuanMaRobledo/JMR-valuation/actions/workflows/nflx-final-gate-20261022.yml).

**Comprobación cuantitativa adicional del riesgo y los pares.** El registro financiero de la valoración contiene un ejercicio controlado de la prima discrecional de país, manteniendo inalterados los FCFF Base: **sin prima extra, US$77,55 por acción**; **con 0,50 pp, US$69,94**; **con 1,00 pp, US$63,63**. Esta prueba permite justificar que 0,50 pp es un amortiguador plausible y conservador respecto de 0,00 pp, **no** que exista una prima geográfica de exactamente 50 pb. El impacto es material: −US$7,61 de 0 a50pb y −US$6,31 de50 a100pb (sensibilidad no lineal por valor terminal). Los pesos de capital del expediente son aproximadamente 94,63% equity y5,37% deuda; el Kd utilizado de5,85% es internamente consistente con una aproximación de yields de bonos USD largos del orden de5,8–6,2% registrada para septiembre, pero la propia metodología indica que **no se calcularon YTM de mercado verificadas a 21-oct**.

La hoja `reference/multiplos_v3/NFLX_anclas.json` permite trazar los **cuatro pares históricos usados**: DIS (Disney), SPOT (Spotify), ROKU y CMCSA (Comcast). Sus `fecha_precio` están identificadas como **30-sep-2026**, no21-oct-2026, de modo que **la ancla contemporánea del corte no está certificada**. DIS integra parques, medios y streaming; SPOT negocio musical/plataforma; ROKU hardware/anuncios/plataforma; CMCSA distribución e infraestructura. Por eso ni los ingresos, ni el margen EBIT, ni la amortización de contenido y el capital físico son equiparables sin ajustes. Los cinco métodos con historia/pares explícitos en el archivo son EV/EBITDA, EV/FCFF, P/E, P/FCFE y P/OCF; el JSON público incluye también P/V y P/BV. El método EV/EBITDA tiene peso 0%; la valoración intrínseca principal es DCF Base sin ponderación con múltiplos. Los múltiplos EV/FCFF y P/FCFE descartan periodos de FCF negativo o cercano a cero en la historia antigua y recortan múltiplos extremos: práctica justificable **estadísticamente**, pero no certificación económica de comparables. **Cierre:** la selección tiene lógica como contraste aproximado, no permite afirmar un valor por múltiplos certificado sin reconstrucción de cotizaciones, empresa comparable, EV y caja en una fecha unificada. Expediente fuente: `JMR-valuation/reference/multiplos_v3/NFLX_anclas.json`, revisión financiera indicada.

**Dictamen actualizado, limitado al corte:** (a) hechos SEC **suficientes para sostener un DCF exploratorio reproducible**; (b) DCF US$69,94 **plausible con reservas fuertes** en ROIC/S2C y prima geográfica; (c) valor de referencia alternativo US$56,08 cuando se retira la ventaja competitiva terminal, útil para comprobar fragilidad; (d) comparables y extractor sin certificación integral; (e) **no hay base para declarar demostrada la rentabilidad terminal durante décadas**. Se puede valorar así; no se puede cerrar científicamente cada supuesto futuro, y el deber de la auditoría es dejarlo contrastable y falsable.

---

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

**Cobertura semántica exigida por §9 v5:** la matriz del artículo consta de **25 controles**: **18 desarrollados y sustentados; 7 limitados por evidencia identificada**. Los siete son (1) TAM homogéneo por región, (2) sostenibilidad económica de foso y ROIC terminal, (3) gobierno/incentivos con proxy2026 localizado, impacto económico no cuantificado, (4) capital económico de contenido y ROIC incremental por cohorte, (5) CRP/Ke por distribución geográfica verificable, (6) comparables y anclas de múltiplos del corte, (7) indicadores de churn/monetización por cohorte no publicados.

No hay secciones reducidas únicamente a un título o enlace. Sin embargo, la regla §9 declara que «limitado por evidencia» **no** equivale a cobertura totalmente resuelta. El análisis está sustancialmente ampliado y documenta lo que falta; no se debe certificar como completo sin ese matiz. La salida del control de publicación del modelo debe referirse a un commit de CI específico: el historial visible contiene corridas failure, y no se ejecutó una nueva suite verde en esta auditoría editorial. La hoja conserva internamente una salvedad económica sobre anclas C.

### Actualización cuantificada JMR v6 — 23-oct-2026 · NO reemplaza todavía la revisión publicada

**Corrección material demostrada y segregada:** en la [copia de trabajo NFLX JMR v6](https://docs.google.com/spreadsheets/d/15QDfNDg_2TG90sFFFvUyeYvI6rL9-AwfwUHI7XmHgPQ/edit) se concilian los ingresos LTM de las cuatro regiones (US$49.734,633M) contra el 10-Q 9M 2026 y 10-K FY2025. Se activa `Cost of capital worksheet!B26=Operating regions` y se usa ERP madura **3,92% respecto a Rf neta de spread soberano** más CRP por región de tablas Damodaran. El WACC calculado pasa de **9,16447% a 9,86851%** (Ke 10,17945%, beta 1,02386, Kd 5,85%), y el DCF Base de **US$69,94 a US$61,12 por acción** (−12,62%). Una cifra preliminar basada en ERP madura 3,70% *combinada con Rf ya neta* fue descartada por incoherencia metodológica. Las primas de EMEA, LATAM y APAC siguen siendo aproximaciones regionales, no CRP exacta de cada país. Fuentes: [SEC Q3 2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm), [Damodaran 8-oct-2026](https://aswathdamodaran.blogspot.com/2026/10/stock-prices-earnings-and-cashflows-ai.html?m=0).

**Resultados calculados exclusivamente en copia (no oficiales publicados):** Conservadora **US$40,12**, Base **US$61,12**, Optimista **US$80,28**, Disrupción **US$14,39**. Promedio ordinario de las tres primeras **US$58,43**. MOS35% sobre Base ≈ **US$39,72**. El precio de referencia **US$65,04** sigue siendo el del 21-oct-2026.

**Las otras tres salvedades examinadas:** opciones Black-Scholes estándar vs. dilución real y plazo 3,5–5,5 años: variación limitada a aproximadamente **US$0,09/acción (0,15%)**; leases reconocidos US$2.252,237M y posible exceso bruto US$366,346M: cota **US$0,089/acción (0,15%) en el puente de deuda**, no evaluación íntegra de arrendamientos en FCFF; tecnología y desarrollo mezclados con operaciones no equivalen a I+D puro: sensibilidad *hipotética* de capitalización de hasta 100% del gasto con 3–5 años, aproximadamente **−US$0,54 a −US$0,81/acción (0,88–1,32%)** bajo flujos y tasas constantes. El impacto conjunto de las tres pruebas acotadas permanece bajo 1,62%, pero ninguna prueba resuelve por sí sola duración de ventaja, ROIC terminal, reinversión real ni nuevos comparables.

**Dictamen de control:** el ajuste ERP/WACC es **material y corregido en copia**, y no debe etiquetarse no bloqueante. Las tres salvedades adicionales son **inmateriales solo en los rangos expresamente ensayados**, quedan registradas y no deberían bloquear por sí solas. **No se actualiza ni certifica la valoración publicada US$69,94**, porque su JSON incluye derivados y HTML antiguos, y falta ejecutar el gate integral y regenerar valoración, múltiplos, artículo y auditoría bajo el mismo identificador. La diferencia entre la copia candidata y lo visible en la app es intencional hasta aprobar esa sincronización. Ver [expediente con ecuaciones, fuentes, límites y celdas](../../evidencia/NFLX-20261023-v6/materialidad-ajustes.md).

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
| Editorial | Siete filas de cobertura limitadas; no auditar como resueltas. | Tesis y control editorial aún con evidencia material incompleta. | Consultar la DEF 14A 2026 ya disponible; cuantificar incentivos, TAM, cohortes y pares cuando exista desglose comparable. |
| Operativo | Corridas CI históricas de la valoración incluyen failure. | No declarar VALIDADO tras modificar solo informes. | Ejecutar controles_todas.sh NFLX y documentar log asociado. |

### Revisión adicional JMR v6 — clasificación de salvedades y conversores, 23-oct-2026

**Alcance:** comprobación directa de valores y fórmulas visibles de la [hoja NFLX](https://docs.google.com/spreadsheets/d/11yN171o8R61n4RhZnmuZuiSyIn_DGkfTmjo7wMKqaZI/edit), sin cambiar el DCF, entradas, escenarios o artículos. Esta revisión registra hallazgos nuevos bajo [reglas v6 §4A–4B](https://github.com/JuanMaRobledo/Modelo-JMR/blob/main/modelo/REGLAS_VIGENTES.md). **Ninguno queda exonerado como inmaterial** sin ejecutar y guardar el recálculo adverso requerido por `scripts/materialidad_salvedades.py`: la mera presencia de un conversor no implica que sus cifras entren en el valor.

| ID y referencia | Evidencia de la hoja revisada | Prueba económica requerida | Impacto máximo verificado | Dictamen provisional |
|---|---|---|---|---|
| **NFLX-RD** · `Input sheet!B17`, `R& D converter!F7:F8,D36,D38,D40` | Capitalización desactivada (`No`), gasto actual tecnología/desarrollo ≈ US$3.890,81M, activo del conversor ≈ US$3.890,81M y amortización corriente del conversor nula al no estar completa la vida amortizable. | Verificar fracción de gasto realmente plurianual, vida 2–3 años apropiada o alternativa documentada, trayectoria histórica de amortización; recalcular EBIT, capital invertido, reinversión/ROIC, historias y valor Base. No agregar el activo del conversor sin terminarlo. | **N/D**, no medida | **Pendiente de prueba de materialidad**; puede ser NO APLICA o ajuste sustancial, aún no probado |
| **NFLX-LEASE** · `Input sheet!B18,B78:B81`, `Operating lease converter` | `B18=No`; nota de la hoja indica ASC 842 y pasivos de lease ya reconocidos. El conversor adicional carece de calendario de compromisos. | Conciliar pasivos lease y gasto con deuda del puente EV→equity/WACC y capital operativo; demostrar que `No` significa **sin deuda incremental** y que no hay doble conteo u omisión. | **N/D** | **Conciliación pendiente**, no imputar 0 por intuición |
| **NFLX-OPT** · `Input sheet!B38:B42`, `Option value!B29:B30`, `Valuation output!B32:B35` | Opciones activas: ≈120,18M; plazo 4,5 años (estimado); ejercicio US$41,24; volatilidad 36,96%. Black-Scholes de `B29` es convencional pese al título “Dilution-adjusted”. Se descuentan US$4.290,87M del patrimonio. El denominador `Input sheet!B22` enlaza acciones actuales ajustadas, no las acciones diluidas promedio del LTM. | Verificar opciones/RSU y vencimientos con filing, método realmente ajustado por dilución, volatilidad, SBC ya expensado, unidades y no duplicación con denominador; valorar extremos de vida 3,5–5,5 años y comparar con alternativa consistente. | **N/D**, no medida para la incertidumbre | **Tratamiento conectado al DCF; precisión económica pendiente** |
| **NFLX-WACC** · `Cost of capital worksheet!B12,B14,E63`, `Input sheet!B36` | `Detailed` activo y WACC ≈9,1645% enlazado a DCF; Ke ≈9,4355%, Kd antes de impuestos 5,85%, pesos patrimonio/deuda 94,63%/5,37%. | Confirmar beta bottom-up, Kd de deuda, Rf y ERP del mismo corte, pesos de mercado y exclusión de lease duplicado; contraste con otro método solo como sensibilidad, no sustituir el Detailed. | **N/D** | **Conexión aritmética observada; sustento económico debe auditarse** |
| **NFLX-ERP** · `Cost of capital worksheet!B26:B28,G22:K33` | `B26=Will Input` y ERP directa 4,42%; calculadora de ventas por región sin datos. | Reconstruir ponderación de exposición geográfica o probar que ERP calculada externamente ya la incorpora con fuentes, moneda y fecha. Recalcular WACC y Base para la diferencia plausible de CRP. | **N/D** | **Pendiente documental potencialmente material** |

**Regla de cierre JMR v6:** un límite individual probado inferior al 2% y acumulado conservador inferior al 3%, sin cruzar precio con MOS, decisión o fallar un candado esencial, pasa a **salvedad NO BLOQUEANTE** y permite VERIFICADO si el resto de controles está aprobado. Las cinco filas de arriba **todavía no cuentan** con intervalos recálculados auditados: por tanto, no han sido clasificadas como inmateriales ni se cambia aquí el dictamen previo ni el DCF Base US$69,94. Registro de control de código: [PR de reglas #90](https://github.com/JuanMaRobledo/Modelo-JMR/pull/90) y [PR de prueba de materialidad #142](https://github.com/JuanMaRobledo/JMR-valuation/pull/142), ambos integrados; **no equivalen a una corrida satisfactoria por empresa**.

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

**Limitaciones formales:** no se obtuvo TAM regional monetizable por fuente homogénea ni se cuantificó impacto de incentivos del proxy2026, resultados por cohortes/título, desglose país que certifique la prima extra50pb, anclas de peers de igual fecha ni evidencia de que ROIC terminal21,52% persista indefinidamente. Hubo nuevas ejecuciones del control histórico, algunas fallidas por clasificación de celdas en el detector. El resultado de la nueva puerta financiera debe verificarse en GitHub; el recuento de secciones no constituye certificación financiera. El juicio queda expuesto y se indica qué evidencia levantaría cada reserva.

**Fin de la auditoría independiente de NFLX según prompt 3 v1.2 y reglas JMR v5.**

