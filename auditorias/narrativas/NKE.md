# Auditoría económica narrativa — NIKE, Inc. (NKE)

## 1. Ficha de auditoría y alcance

NIKE, Inc.; NKE Class B, NYSE; moneda USD; estados y acciones en millones. Método principal DCF FCFF Base. Revisión y auditoría 23-oct-2026 con datos/precio al 22-oct-2026, estados 31-ago-2026 y cotización congelada 22-oct-2026 de US$38,32. [Hoja examinada](https://docs.google.com/spreadsheets/d/1cFiWggFYuulRV11TDf6u9EY_CNWPBzWWsNiQ1qkrcxY/edit?usp=drivesdk), archivo`valoracion_resultados.json`, artículo`02_Analisis_NKE.md`. Revisión`NKE-JMR-20261023-R2`, SHA-256`1ff2ff5a7197fb89c712dca6ab264d3a6093ede83942c95d5859b8d1fbca0d6e`.

Esta es una ejecución separada, posterior a la redacción del análisis, por el mismo asistente. Se usa una implementación aritmética independiente, sin un segundo escritor concurrente. Se comprobaron las salidas oficiales y sus dependencias; no se afirma haber certificado todas las 64 pestañas ni ejecutado los controles del repositorio con credenciales externas. **Estado: Con reservas; auditoría condicionada. No se modificó la valoración.**

## 2. Resumen ejecutivo y relato económico central

Nike obtiene beneficio al combinar diseño, marca y distribución sobre una fabricación principalmente contratada. Esa estructura puede generar retornos altos sin fábricas propias de la misma escala. Sin embargo, inventario, descuentos y costo comercial pueden consumir caja y margen cuando el producto pierde rotación.

La tesis favorable es que innovación deportiva y normalización mayorista devuelvan una parte de la rentabilidad histórica. La hipótesis Base pide 12% de margen núcleo en año 5 y ventas LTM que pasan de 45.891 m a 48.783,55 m en año 5. No exige un crecimiento elevado sostenido, pero sí una mejora operativa clara.

La lectura neutral acepta que existe una franquicia valiosa y que su recuperación tardará varios años. La contratesis es que el problema sea de preferencia persistente: reducir costos no compensaría para siempre una pérdida de demanda a precio completo. El supuesto que más exige juicio es la durabilidad del exceso de retorno; llevar ROIC terminal a WACC reduce el valor de US$35,02 a US$28,42.

La matemática concilia. La incertidumbre normal del pronóstico está expresada como escenarios y sensibilidad. Las salvedades documentales son distintas: I+D no separado, detalle de opciones no actualizado y cobertura incompleta de determinados múltiplos/pares.

## 3. Trazabilidad, integridad y jerarquía de evidencia

| Dato | Valor | Período/perímetro | Tipo | Documento/URL/fecha | Hoja/celda | Verificación |
|---|---|---|---|---|---|---|
| Ingresos LTM | 45.891 | FY26+Q1FY27−Q1FY26 | OBSERVADO/CÁLCULO | SEC10K15-jul y 10Q2-oct-2026 | Input B12 | Conciliado |
| EBIT núcleo LTM | 3.758 | Ventas−COGS−SG&A | CÁLCULO | Mismos documentos; estados consolidados | Input B13 / Income L12 | Conciliado; distinto de EBITNike 3.853 |
| Caja+inversiones CP | 8.368 | 31-ago-2026 | OBSERVADO | 10Q balance y Nota 3 | Input B19 | Conciliado |
| Deuda contable total | 11.072 | 7.893financiera+3.179leases | OBSERVADO/CÁLCULO | 10Q balance | Input B16/B78 | Sin doble deuda |
| Deuda mercado total | 9.879 | 6.700bonos+3.179leases | OBSERVADO/CÁLCULO | 10Q Nota 3 | Cost C54/C61 | Usada en WACC; puente contable diferenciado |
| Acciones | 1.485,31 m | Portada 28-sep-2026, clases A+B | OBSERVADO | 10Q portada | Input B22 | Correctas; no promedio diluido |
| Precio | 38,32 | Cierre 22-oct-2026 | OBSERVADO | Yahoochart; fuente secundaria de mercado | Input B23 | Fechado y congelado |
| Rf/ERP | 5,29%/3,70% | Mismo corte mensual 1-oct-2026 | OBSERVADO | Damodaran ERPOct 26.xlsx | Input B35 / Country B2 | Conserva precisión 3,70% |
| Prima país | 0,87 pp adicionales | Proxy por región, no ventas-país | HIPÓTESIS/CÁLCULO | ctryprem 2026 + mezcla Nike LTM | Cost B27 | Provisional como aproximación |
| Opciones | 76,8 m;K96,44;vida 4,85 | Detalle 31-may;vida desplazada 3 meses | OBSERVADO/HIPÓTESIS | 10KNota 11 /10QNota 5–6 | Input B39:B42 | Salvedad temporal |
| Pares | 5candidatos,4P/E numéricos | Fechas de estados no idénticas | OBSERVADO/CÁLCULO | Companyfacts por emisor + cierres 22-oct | Ancla B | No certificada como ajuste homogéneo |

Cada observación original conserva etiqueta XBRL, accession, publicación, período y unidad en`observations.json`. El manifiesto protege la identidad de las fuentes descargadas. Las series históricas usan comparativos reexpresados disponibles al corte; las anclas no se presentan como un backtest sin información futura.

## 4. Historia financiera: diez años y punto de partida

Margen núcleo: media 3 a 9,49%,5 a 10,86%,10 a 11,64%;LTM 8,19%.

Se revisaron 10ejercicios FY2017–FY2026 más LTM. Los estados completos resumidos están en Nivel 2. El flujo OCF−capex es distinto de FCFF. La adopción ASC842 limita la comparación directa de capital invertido de los primeros años con los posteriores; I+D tampoco está capitalizado. No se presenta un ROIC de diez años homogéneo que no fue reconstruido.

El balance cuadra por identidad activos=pasivos+patrimonio. El detalle de algunas cuentas auxiliares históricas permanece N/D. Una reclasificación no debe tratarse como cambio económico; tampoco debe mezclarse una cifra reexpresada con una afirmación sobre lo que el mercado sabía en la fecha original.

## 5. Crecimiento de ingresos: de la historia a la proyección

La Base proyecta contracción inicial y recuperación diferenciada por región. Norteamérica se estabiliza antes que China y Converse. La trayectoria tiene CAGR1–51,23%; no es cinco años creciendo a una tasa constante. El escenario no puede justificarse por la cotización, que se incorpora después de formular la historia.

| Pregunta obligatoria | Respuesta |
|---|---|
| a. ¿Valor, año, unidad y celda? | Tasas C29:G29; diez años C29:L29; CAGR no redondeado 1,23%. |
| b. ¿Comparación histórica? | FY2025−9,84%, FY2026+0,19%, Q1FY2027−4,33% reportado. |
| c. ¿Mecanismo causal? | Renovación de producto, menor liquidación y recuperación de distribución. |
| d. ¿Qué debe ocurrir? | Mayorista mejora rotación y China deja de deteriorarse antes del crecimiento estable. |
| e. ¿Qué lo refuta? | Envíos crecientes sin venta final; descuentos y China permanecen débiles. |
| f. ¿Impacto si está equivocado? | Delta−1 pp:US$33,39; +1 pp:US$36,75. |

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Ingresos 1–5 | Historia irregular;LTM45.891 m | −7,18%,+1,24%,+4,13%,+4,48%,+3,98%; Escenarios C29:G29 | Sector Shoe globalcrecimiento 5 a 6,38%; guía FY2027caída dígitoalto | Recuperación modesta después del ajuste | Plausible; ventana rolling diferente del FY oficial | Prueba±1 pp arriba |


## 6. Márgenes operativos y normalización de beneficios

La normalización evita dos errores: extrapolar el margen LTM como estado estable o suponer que el máximo histórico vuelve inmediatamente. El primer año núcleo 5,25% y la tasa 25% producen EPS móvil GAAP cercano a 1,15; sumando la exclusión Pace 0,15, se aproxima el centro de la guía ajustada. La comparación es orientativa porque el período móvil termina en agosto y la guía fiscal en mayo.

Margen núcleo: media 3 a 9,49%,5 a 10,86%,10 a 11,64%;LTM 8,19%.

| Pregunta obligatoria | Respuesta |
|---|---|
| a. ¿Valor, año, unidad y celda? | Input B28:5,67%ajustado; objetivo Base Escenarios D5:12,42%, equivalente 12%núcleo. |
| b. ¿Comparación histórica? | La media reciente es menor que la de diez años; Nike sí ha superado 12% antes. |
| c. ¿Mecanismo causal? | Mejor precio/mezcla, menores liquidaciones, disciplina de SG&A y ahorro Pace neto. |
| d. ¿Qué debe ocurrir? | Los ahorros no se reinvierten íntegramente ni se destruye innovación al recortar. |
| e. ¿Qué lo refuta? | Mejora solo por partidas únicas o costos repetidos sin beneficio sostenible. |
| f. ¿Impacto si está equivocado? | Objetivo−1 pp:US$32,08; +1 pp:US$37,97. |

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Margen año 5 yestable | Margen núcleo: media 3 a 9,49%,5 a 10,86%,10 a 11,64%;LTM 8,19%. | Base 12%núcleo/12,42%ajustado; Valuation C46 | Shoe global 8,80%sin ajustar; no comparación idéntica con I+D | Escala de marca rentable y reducción de descuentos | Objetivo superior a industria; requiere ejecución, no solo reputación | ±1 pp mueve aproximadamente US$3poracción |

El reintegro arancelario 986 m compensó costos del mismo FY. Restar solo el reintegro generaría una normalización incompleta. El anuncio Pace es 2,5 bn de ahorros acumulados antes de cargos/reinversión; no se sumó como 2,5 bn de flujo anual.

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

La empresa subcontrata fabricación, pero no obtiene crecimiento sin invertir. El modelo utilizaΔventas/Sales-to-Capital y mantiene la reinversión mínima en 0 ante caída de ventas. Esa restricción evita asumir una liberación inmediata de inventarios y activos no demostrada.

Capital invertido LTM aproximado=15.220+11.072−8.368=17.924,00 m. NOPATajustado histórico/capital final≈17,48%. Es un ratio con capital de cierre, no el ROICde Nike sobre capital promedio. Además, omite el activo I+D, por lo que no es plenamente comparable con la tabla ajustada de industria.

| Pregunta obligatoria | Respuesta |
|---|---|
| a. ¿Valor, año, unidad y celda? | Escenarios E5:2,11; F5:1,59; G5:15,29%terminal. |
| b. ¿Comparación histórica? | Ventas/capital de cierre aproximadas 2,56; cambios de arrendamientos afectan serie. |
| c. ¿Mecanismo causal? | La reinversión financia crecimiento y mantiene la productividad del capital. |
| d. ¿Qué debe ocurrir? | La recuperación comercial se convierte en ventas sin inventarios estructuralmente mayores. |
| e. ¿Qué lo refuta? | Mucho capital nuevo con poco crecimiento o ahorro que exige inversión no modelada. |
| f. ¿Impacto si está equivocado? | ROICterminal=WACC lleva a US$28,42; efecto I+D no cuantificable sin serie. |

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| S/C y ROIC | LTM ajustado aproximado 17,48%; no ROIC10 a homogéneo | S/C2,11→1,59; ROICestable 15,29% | Shoe global S/C2,11 y ROICajustado 15,29% | Convergen margen, eficiencia, impuesto yretorno | Reserva: falta I+D; activo económico no inventado | Escenario sin exceso terminal arriba |

No se confunde margen×S/C marginal con el ROIC contable de activos existentes. Recompras y dividendos son distribución, no inversión operativa. Las correcciones de margen y transición temporal de S/C ocurrieron en Valoración R2 antes del congelamiento; esta auditoría no la modifica.

## 8. Costo del capital y riesgo

El costo de capital se calcula con beta bottom-up global porque las ventas no se concentran mayoritariamente en Estados Unidos. El riesgo de producto se incorpora en las historias. No se añade otra penalización genérica por las mismas dificultades operativas.

Ke 9,90%; WACC9,10%; betaapalancada 1,01; beta U0,89; Kd 6%[juicio]. El riesgo país utiliza proxies regionales y un incremento sobre el componente estadounidense de la tabla anual. La exposición exacta a cada país no está disponible.

| Pregunta obligatoria | Respuesta |
|---|---|
| a. ¿Valor, año, unidad y celda? | Cost B63/E63; Input B35; maduro Country B2; costo terminal Input B47. |
| b. ¿Comparación histórica? | Se usa corte mensual coherente, no una media histórica de tasas para el descuento actual. |
| c. ¿Mecanismo causal? | Beta sectorialreapalancada y pesos de deuda/patrimonio de mercado. |
| d. ¿Qué debe ocurrir? | La mezcla geográfica y costo marginal no se apartan materialmente de los proxies. |
| e. ¿Qué lo refuta? | Desglose país, spread o estructura financiera contradicen las aproximaciones. |
| f. ¿Impacto si está equivocado? | WACCinicial−1 pp:US$37,22; +1 pp:US$32,98; beta OLS:US$34,94. |

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Tasas ybeta | Beta OLSsemanal 5 a 1,02;260 observaciones | Rf 5,29% /ERPtotal 4,57% /WACC9,10% | Damodaranenero 2026 y ERP1-oct-2026 | Primapaísregional porventas, conpesos demercado | Kd ydetalle-país sonjuicios explícitos | Pruebasnuméricas arriba |


## 9. Convergencia y valor terminal

El terminal representa 64,80% delvaloroperativo Base. g 4%nominal USD respeta Rf 5,29% y WACCterminal 8,99%. No se infiere que 4%sea una predicción cierta; es la regla de corte JMR aplicada en la misma moneda.

La ventaja de marca puede sobrevivir, pero tiene que seguir produciendo retorno. El ROICterminal 15,29% es inferior al mejor régimen histórico de Nike y superior a WACC. La reserva económica es la duración de esa ventaja, además de la diferencia contable I+D. La sensibilidad a ROIC no certifica la hipótesis.

| Pregunta obligatoria | Respuesta |
|---|---|
| a. ¿Valor, año, unidad y celda? | Input B69:g 4%; B47:WACC8,99%; Escenarios G5:ROIC15,29%. |
| b. ¿Comparación histórica? | Industria global ajustada como ancla; no elmejor dato Nike. |
| c. ¿Mecanismo causal? | Se reinvierteg/ROIC y S/Cconverge hacia ROIC/[margen×(1−t)×(1+g)]. El retorno marginal relaciona reinversión_t y ΔNOPAT_(t+1); no obliga al ROIC agregado del capital existente a igualarse inmediatamente. |
| d. ¿Qué debe ocurrir? | La rentabilidad de marca permanece por encima de un negocio sin ventaja. |
| e. ¿Qué lo refuta? | La competencia elimina poder deprecio oeleva capital requerido. |
| f. ¿Impacto si está equivocado? | Valor sinexceso terminal US$28,42; matriz WACC×g mantiene el WACCinicial yrecalcula transición. |

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Convergencia terminal | No puede observarse unresultado perpetuo | g 4%; reinversiónterminal 1.495,46 m | ROICindustria 15,29% | FCFF11incluye capitalnecesario; no crecimiento gratuito | Moatdurablees juicio; sensibilidad explícita | PVterminal/EV64,80% |


## 10. Validación independiente del valor intrínseco

La implementación independiente reproduce cuatro DCF de la hoja con error inferior a 0,001poracción. Base: VPexplícito 19.308,41 m+VPterminal 35.539,64 m=EV54.848,05 m. Después se suman 8.368 m decaja y se restan 11.072 m dedeuda contable y 123,37 m de opciones; dividido por 1.485,31macciones resulta US$35,02.

El WACC usa deuda demercado 9.879 m, mientras elpuente utiliza la convencióncontable de laplantilla. Se cuantificó la alternativa: deuda demercado en elpuente lleva a US$35,83, diferencia US$0,80. Conviene homogeneizar esa convención en un cambio metodológico explícito, en vez deocultarla como prudencia.

| Pregunta obligatoria | Respuesta |
|---|---|
| a. ¿Valor, año, unidad y celda? | Valuationoutput B18:B35; opciones B30; acciones Input B22. |
| b. ¿Comparación histórica? | Se contrasta histórico, pero elvalor sale de flujos futuros y supuestoscongelados. |
| c. ¿Mecanismo causal? | FCFFdescontado yterminal económico, puente alpatrimoniocomún. |
| d. ¿Qué debe ocurrir? | Todos losreclamos están contabilizados unavez y lasunidadescoinciden. |
| e. ¿Qué lo refuta? | Doble deuda, acciones deunasolaclase, opciones duplicadas oterminal sinreinversión. |
| f. ¿Impacto si está equivocado? | Reproducciónporhistoria y raíz inversa conservadas enaudit_checks.json. |

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| DCF Base | R1base 35,43; R2corrige trayectoria y convención de reinversión | B35=35,02 | Motor propio independiente y Google Sheets | Suma flujosperpetuidadreclamos/acciones | Reserva documental enopciones, no error deigualdad | 47 controles aprobadosenalcance;4hallazgos |


## 11. Cuatro historias y probabilidades

| Historia | Crecimiento CAGR1–5 | Margen núcleoobjetivo | S/Caño 10 /ROICterminal | WACCinicial/terminal | gterminal | Valor USD/acción | Probabilidad | Confirmación/refutación |
|---|---|---|---|---|---|---|---|---|
| Base | 1,23% | 12,00% | 1,59 / 15,29% | 9,10% / 8,99% | 4,00% | 35,02 | 40,00% | Recuperación gradual de producto y distribución |
| Conservadora | -1,58% | 9,00% | 1,66 / 12,14% | 9,10% / 8,99% | 4,00% | 21,53 | 25,00% | China retrasa la recuperación y el canal sigue ajustándose |
| Disrupción | -4,51% | 4,50% | 2,45 / 8,99% | 9,10% / 8,99% | 0,00% | 8,50 | 20,00% | Deterioro de los fundamentales: pérdida persistente de relevancia |
| Optimista | 4,09% | 15,00% | 1,28 / 15,29% | 9,10% / 8,99% | 4,00% | 50,70 | 15,00% | Innovación y mayorista reactivan la demanda |

Promedio condicionado=(40%×Base+25%×Conservadora+15%×Optimista)/80%=US$33,75. La previa de declive se eligió como juicio sobre el ciclo actual. No se modificó ninguna probabilidad mediante un indicador no documentado.

### ¿Qué pasaría si todo fallara?

Disrupción US$8,50;20%. Caída de 12%,7%,3%, posterior estabilidad; gterminal 0 y ROIC=WACC. No forma parte delpromedio ordinario ni delprecio con MOS.

## 12. Valoración por múltiplos: prueba independiente y secundaria

| Método | A ajustada | B indicativa | C | Elegido Base | Métrica FY+3 | Precio FY+3 | VPcondividendos | Peso |
|---|---|---|---|---|---|---|---|---|
| EVEBITDA | 23,27 | 7,94 | 9,87 | 9,87 | 4.783,33 | 29,89 | 26,60 | 60,00% |
| EVFCFF | 42,49 | N/D | 21,44 | 21,44 | 2.202,56 | 29,89 | 26,60 | 0,00% |
| PE | 29,25 | 10,62 | 14,07 | 14,07 | 2.936,33 | 27,82 | 25,05 | 40,00% |
| PFCFE | N/D | N/D | 18,05 | N/D | 2.094,00 | N/D | N/D | 0,00% |
| POCF | 34,09 | N/D | 8,68 | 8,68 | 4.353,98 | 25,44 | 23,25 | 0,00% |
| PV | 3,79 | N/D | 0,92 | 0,92 | 44.906,61 | 27,82 | 25,05 | 0,00% |
| PBV | 11,57 | N/D | 2,45 | 2,45 | 16.839,11 | 27,82 | 25,05 | 0,00% |

Elconsolidado US$25,98 es secundario.60%EV/EBITDA y 40%P/E reflejan dos perspectivas útiles; no se cuentan EV/FCFF, P/Vy P/BV como confirmacionesadicionales cuando son transformaciones del mismo techo C. P/OCF conserva eladdback SBC, sudefinición no equivalea FCFF.

La ancla B no está certificada:UAA tiene variasclases, DECK carece de D&Aconciliada enlaextracción y los EV de pares conservanlímites debalance. Una diferencia>25% frente alos pares exige explicación, pero la explicación no sustituye la conciliación. La Optimista tiene múltiplos porencima de losactuales; su justificación es uncrecimiento FY+3 superior y margen 15% núcleo. Esa historia exige validación futura; no se declara que elmercado deba conceder ese múltiplo.

P/FCFE seleccionado permanece N/D porque loshistóricos antes denueva financiación no son un FCFEcompleto. Se excluye delponderado. Elajustepor tasas, techos C y centros se recalcularon en la valoración, sin factores genéricos Toro 0,8/0,9/1,1.

## 13. Sensibilidades económicas y escenarios alternativos

Las tres matrices DCFBase concilian con US$35,02. La familia WACCterminal×g conserva el WACCinicial, recalcula sutransición ylosdescuentos. La familia ROIC×g recalculaeficiencia yreinversión; crecimiento×margen añade undelta común alas tasas 1–5, preserva laforma yconverge alterminal.

El DCF inverso encuentra unaraíz en[−50 pp,+80 pp]:delta 1.87 pp; CAGRimplícito 3,10% frente a Base 1,23%. Reconstruye US$38,32 con error<0,001. No utiliza unmultiplicador de calibración hoja/motor.

Múltiplos:28 bloques Base,26matricesnuméricas y 2N/D correspondientes alaancla JMRP/FCFE. Hay dos anclas ydosfamilias por método. Loscentros de las 26matricescalculadas concilian; los ejes usanveces, USDmillones omárgenes/deltas económicos identificados. Las 21matricesheredadas porhistorias seocultaron para que no compitan con la salidavigente. Los N/D no se contabilizan comocentros validados.

## 14. Coherencia de hojas, cálculos y presentación

Se revisaron las salidas oficiales de Input, Valuation output, Escenarios, Resumen, Múltiplos JMR, matrices, opciones, inverso y sensibilidad. Tras la autorización del usuario se publicaron juntos valoración, análisis y auditoría de NKE-JMR-20261023-R2. La lectura de los tres registros publicados confirma el mismo hash de resultados, DCF Base US$35,02 y MOS35% US$22,77. El despliegue de producción está READY. Esto verifica la revisión publicada; no implica republicación editorial automática al editar la hoja.

Fueroncorregidos durante Valoración:promediosimple en vez deponderado;omisión de interés deleasesya reconocidos;circularidad de opciones;instrucciones demúltiploslegadas;transición S/C→ROICterminal;tasafiscal yprimer año frente ala guía;signos de salidas de caja;descuentos dedividendos poraño. Notas yselectores nativos seconservaron en la copia. Elperfil Madura conserva unselectoractivo conpesosespecíficos para NKE.

Las matrices oficiales se recalculan con fórmulas. Elinverso guarda laraíz deestaejecución yrecalcula el precio implícito:si cambian losinputs, elresidual lo marca«RECÁLCULO REQUERIDO». No seafirma un Goal Seekautomático. Algunas pestañasauxiliaresheredadas no quedaroncertificadas por completo; nopuedenpresentarse como evidencia deuncontrolexterno no ejecutado.

El registro `reference/plantillas.json` del repositorio, fechado 21-oct-2026, todavía apunta a la plantilla IA del 11-oct. Esta entrega fija explícitamente el ID de la plantilla vacía del 22-oct identificada en Drive y el ID distinto de su copia. El registro global no fue modificado; un proceso automático posterior debe usar este expediente y no sustituirlo silenciosamente por la referencia antigua.

## 15. Hallazgos priorizados y propuestas de corrección

| ID | Severidad | Tipo | Evidencia | Impacto | Mantener/ajustar/investigar | Propuesta y alternativa | Requiere aprobación | Estado |
|---|---|---|---|---|---|---|---|---|
| H01 | Alto | Dato/comparabilidad | I+D existe en SG&A, sin serie anualseparada | Valoraciónsinactivo I+D; ROICnohomogéneo conindustriaajustada | Investigar | Obtener desgloseo documentar modelo sincapitalización; no imputar 0 | No para investigar | Abierto |
| H02 | Medio | Dato | Opciones 31-may frente acorte 22-oct;10Q84,0 m antidilutivos agregados | Pruebailustrativa 84 m al mismo K/vida:US$35,02; noes límite real | Investigar | Reconstruir concesiones/expiraciones/RSUystrikes actualizados | No para investigar | Abierto |
| H03 | Medio | Método/dato | P/FCFEhistórico incluye financiación no reconstruida | Ancla JMRN/D; peso 0;2 matrices N/D | Mantenerexclusión | Reconciliar deuda y definiciones antes de darle peso | Sí si se cambia elpeso | Abierto |
| H04 | Medio | Comparables | Cobertura yhomogeneidad insuficientes para Bajustada | Paresindicativos; sin prima/descuento cuantitativo certificado | Investigar | Conciliar clases, EV, moneda, arrendamientos ycrecimiento | No para investigar | Abierto |
| J01 | Medio | Juicio | ROICterminal 15,29%>WACC8,99% | Sinexceso:US$28,42 | Revisar con evidencia | Conservar comohipótesis refutable; revisar sidemanda/preciofallan | Sí para cambiar latesis | Incertidumbredepronóstico |
| J02 | Bajo | Convención | Deudamercadoen WACC ycontableenpuente | Alternativa US$35,83; delta US$0,80 | Ajustarmétodoenrevisiónexplícita | Definir convención uniforme; no corregirsilenciosamente durantedictamen | Sí para nueva revisión | Explicado |
| J03 | Medio | Juicio | Prima paísproxy y Kd 6% | WACCinicial±1 pp:US$32,98–37,22 | Investigar | Refinar país ycurva crédito con mismafecha | Sí para nuevas entradas | Explicado |

No se requiere que un pronóstico futuro se convierta en un hecho observado para usarlo como juicio. Los hallazgos de cobertura se mantienen diferenciados de las incertidumbres económicas normales. El informe no declara «validado» el conjunto mientras existan datos/definiciones materiales pendientes.

## 16. Catalizadores, señales de refutación y seguimiento

| Métrica | Nivel observado | Señal favorable propuesta | Señal adversa propuesta | Fuente | Frecuencia |
|---|---|---|---|---|---|
| Ingresos Q1FY27 | −4% reportado;−5%neutral FX | Dos trimestres creciendo con volumen | Dos trimestres≤−5%neutral FX | 10Q/IR | Trimestral |
| Digital | −13%neutral FX | Estabilización sin mayores descuentos | Persistencia de caída≥10% | 10Q | Trimestral |
| China | 1.180 m Q1vs 1.512 m | Caída<5%y margenmejora | Ventasymargen siguen deteriorándose | 10Q | Trimestral |
| Margenbruto | 42,8%;+60pb | Mejora sin partidasúnicas | Ahorro logístico compensadopor descuentos | 10Q | Trimestral |
| Pace | 2,5 bn acumulados;1 bn cargos | Ahorro netocaja observable | Máscargos/reinversión absorbenbeneficio | 8K/IR | Trimestral |
| Retorno | ROICsujetoabasecontable | Mejora operativa sin expansión improductiva de capital | Inventarios yactivoscrecen másqueventas | Estados | Trimestral |

Los umbrales son criterios del auditor; no se presentan como guía de Nike. No se anunció una fecha de siguiente resultado que no estuviera confirmada en el expediente.

## 17. Dictamen económico y resumen para escuchar

**Tesis: Plausible con reservas.** Consistencia matemática:validada en los cuatro DCF, las sensibilidadesoficiales yel inverso examinados. Trazabilidad:conhallazgos por I+D, opciones ydefiniciones de ciertosmúltiplos/pares. Razonabilidadeconómica:elprimer añoseanclaenlaguía yla recuperaciónesposible, pero la rentabilidadterminalrequiere sosteneruna ventaja que no estádemostrada para siempre.

El supuesto másfrágil es la duracióndel exceso de ROIC; el másdefendible es partir decontracción yuna tasa fiscalnormalizada coherente conlaguía. Se publica esta revisión como versión vigente de NKE con reservas explícitas. Los datos identificados siguen pendientes para una certificación integral. **No se modificó el cálculo durante la auditoría. La publicación posterior conserva este dictamen.**

### Resumen oral

Nike tiene una marca y una distribución valiosas, pero su recuperación todavía debe verse en ventas rentables y caja. Esta revisión calcula un valor base de 35,02 dólares por acción y un precio con margen de seguridad de 22,77. La matemática de la hoja, los escenarios, las sensibilidades y el DCF inverso coincide. El resultado depende sobre todo de recuperar margen y conservar retornos superiores al costo del capital. La auditoría mantiene reservas por el gasto de investigación no separado, el detalle de opciones posterior a mayo y algunos múltiplos y comparables. Es una valoración calculada y revisable, con incertidumbres visibles. La versión publicada conserva este dictamen y las cuatro salvedades documentales.

## 18. Fuentes primarias, limitaciones y registro de versión

- **F1** [NIKE10-K FY2026,15-jul-2026](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm). Consulta 22-oct-2026; documento conservado y SHA-256 en el manifiesto.
- **F2** [NIKE10-Q31-ago-2026,2-oct-2026](https://www.sec.gov/Archives/edgar/data/320187/000032018726000193/nke-20260831.htm). Consulta 22-oct-2026; documento conservado y SHA-256 en el manifiesto.
- **F3** [Resultados y guía Q1FY2027,1-oct-2026](https://www.sec.gov/Archives/edgar/data/320187/000032018726000184/q1fy27exhibit991er.htm). Consulta 22-oct-2026; documento conservado y SHA-256 en el manifiesto.
- **F4** [Damodaran, ERP octubre 2026](https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx). Consulta 22-oct-2026; documento conservado y SHA-256 en el manifiesto.
- **F5** [Damodaran, beta global enero 2026](https://pages.stern.nyu.edu/~adamodar/pc/datasets/betaGlobal.xls). Consulta 22-oct-2026; documento conservado y SHA-256 en el manifiesto.
- **F6** [Damodaran, ROIC global enero 2026](https://pages.stern.nyu.edu/~adamodar/pc/datasets/rocGlobal.xls). Consulta 22-oct-2026; documento conservado y SHA-256 en el manifiesto.
- **F7** [Damodaran, ventas/capital global enero 2026](https://pages.stern.nyu.edu/~adamodar/pc/datasets/capexGlobal.xls). Consulta 22-oct-2026; documento conservado y SHA-256 en el manifiesto.
- **F8** [Damodaran, riesgo país 2026](https://pages.stern.nyu.edu/~adamodar/pc/datasets/ctryprem.xlsx). Consulta 22-oct-2026; documento conservado y SHA-256 en el manifiesto.
- **F9** [SEC Companyfacts NKE, consulta 22-oct-2026](https://data.sec.gov/api/xbrl/companyfacts/CIK0000320187.json). Consulta 22-oct-2026; documento conservado y SHA-256 en el manifiesto.
- **F10** [Yahoo Finance, cierres NKE hasta 22-oct-2026](https://query1.finance.yahoo.com/v8/finance/chart/NKE?range=10y&interval=1d). Consulta 22-oct-2026; documento conservado y SHA-256 en el manifiesto.
- **F12** [NIKE, transcripción oficial Q1FY2027,1-oct-2026](https://investors.nike.com/financial-information/financial-results/transcript/9591/q1-2027-transcript). Consulta 22-oct-2026; documento conservado y SHA-256 en el manifiesto.
- **F13** [Damodaran, crecimiento y reinversión, clase de valoración](https://pages.stern.nyu.edu/~adamodar/podcasts/valUGspr20/session10slides.pdf). Consulta 22-oct-2026; documento conservado y SHA-256 en el manifiesto.
- **F11** [Reglas JMR v 4,21-oct-2026](https://github.com/JuanMaRobledo/Modelo-JMR/blob/main/modelo/REGLAS_VIGENTES.md). Consulta 22-oct-2026; documento conservado y SHA-256 en el manifiesto.

Ficha cuantitativa:`valoracion_resultados.json`. Observaciones originales:`observations.json`. Fuentes descargadas y manifiesto con hashes incluidos. Tres prompts originales separados en`prompts/`; protocolo optimizado 1.0 y reglas JMRv 4 identificados. **Publicada con salvedades.**

Auditoría`prompt_version:auditoria-economica-jmr-v1.2`; reglas JMRv 4; procesooptimizado 1.0. Valoraciónauditada`NKE-JMR-20261023-R2` yhash`1ff2ff5a7197fb89c712dca6ab264d3a6093ede83942c95d5859b8d1fbca0d6e`. Artículode 18 secciones, valoración y JSONcongelados antes deldictamen. Archivoscacheados yhashes en`audit_checks.json`; pasostécnicos ypendientes en`fases_ejecucion.json` y`README.md`.

La publicación posterior fue autorizada por el usuario y verificada mediante lectura de los tres registros publicados y del despliegue de producción. Pasaron17 pruebas del motor/sincronización, los cuatro DCF,75 celdas de sensibilidad DCF y el contrato del catálogo. No se declara ejecutado controles_todas.sh ni certificadas todas las pestañas legadas. No se presenta la lectura de registros como una prueba visual del navegador autenticado o de la descarga PDF.


> **Publicación autorizada23-oct-2026.** Revisión `NKE-JMR-20261023-R2`, resultado congelado SHA-256`1ff2ff5a7197fb89c712dca6ab264d3a6093ede83942c95d5859b8d1fbca0d6e`. DCF BaseUS$35,02; MOS35%US$22,77; conserva las cuatro salvedades. La auditoría previa permanece separada de la publicación.
