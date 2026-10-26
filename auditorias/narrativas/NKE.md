# Auditoría JMR · NKE · recaptura del 2026-10-26

**Revisión financiera: NKE-JMR-20261025-R6** · cierre RECAPTURA-20261025-FORMULAS-PROPIAS · sustituye a NKE-JMR-20261025-R5.

**Dictamen vigente: VERIFICADO CON SALVEDADES en el alcance documentado.** Sin cambios de supuestos, probabilidades ni pesos.

**Qué cambió:** se alinearon con la plantilla las fórmulas propias de la hoja (resumen y EV incluidos); P/E, P/FCFE (peso 0) y P/OCF cambian ligeramente y el precio ponderado Base pasa de 33,98 a 33,95; DCF Base y MOS idénticos.

**Controles ejecutados:** `controles_todas.sh` sin fallas y verificador de la recaptura con 0 fallas. [Registro](https://github.com/JuanMaRobledo/JMR-valuation/tree/main/reference/revisiones/Recaptura-Publicacion-20261025).

**Salvedades vigentes:** NIKE no divulga I+D separada del SG&A; capitalización exacta imposible. Registro como limitación de ROIC y contraste sectorial, no como ausencia de gasto. Opciones: 76,8 millones detalladas al 31-may-2026; datos Q1FY27 de instrumentos mixtos (84 millones) no sustituyen opciones; valor de opciones reconocido US$123,37m; sensibilidad máxima examinada ~US$0,008/acción. P/FCFE cerrado: FCFE reportado preservado; normalizado después de SBC, financiación neta 0 explícita. Salidas 11,66× / 17,62× / 17,62×; VP a 3 años US$14,52 / US$22,80 / US$25,51. Peso 0 por volatilidad del flujo; no cambia DCF ni ponderado. Comparabilidad y pronóstico siguen siendo juicios. Comparables DECK/CROX/LULU/COLM recomputados con EV caja, leases y acciones económicas; homogeneización IFRS/USGAAP de EBITDA y arrendamientos aún limitada. UAA excluida. 12/12 conciliaciones de inversión y financiación cerradas; tres desgloses no publicados de pasivos operativos permanecen N/D sin afectar FCFF. El control técnico R4 se completó el 25-oct-2026 sobre captura directa identificada.

**No re-ejecutado:** `engine_verification` de la app y revisión visual; los archivos de verificación de la carpeta de documentos son de la revisión anterior y están rotulados como heredados.

### Antecedente de auditoría conservado · no es el dictamen técnico vigente

Lo que sigue describe la situación anterior a esta recaptura; las reservas económicas/documentales siguen vigentes.

---
# NKE · Cierre de múltiplos y correspondencia de entrega

Fecha: 2026-10-23. Revisión vigente: `NKE-JMR-20261025-R6`. Fuente: [hoja original](https://docs.google.com/spreadsheets/d/1wWS0qNCWvSrYCI53kk7H1zBshn-RJWjeKFu10sHCNWw/edit).

**Cierre de cálculo: 7/7 métodos, 21/21 escenarios, 63/63 precios y 63/63 descuentos comprobados. DCF Base: US$35,02; precio con MOS 35%: US$22,77.**

Cada entrada y salida proviene de las fórmulas de Financials Multiples y del descuento de la misma hoja. Las comprobaciones independientes reproducen precio, dividendos y descuento. Un peso cero conserva los tres resultados. Este cierre no transforma las reservas económicas anteriores en una certificación integral.

| Método | Conservador VP | Base VP | Optimista VP | Peso relativo |
|---|---:|---:|---:|---:|
| EV/EBITDA | 15,16 | 26,60 | 73,76 | 60,00% |
| EV/FCFF | 15,16 | 26,60 | 56,64 | 0,00% |
| P/E | 14,64 | 24,98 | 57,02 | 40,00% |
| P/FCFE | 14,68 | 23,97 | 27,50 | 0,00% |
| P/OCF | 14,46 | 23,19 | 52,02 | 0,00% |
| P/V | 14,64 | 24,98 | 57,02 | 0,00% |
| P/BV | 14,64 | 24,98 | 57,02 | 0,00% |

P/FCFE: históricos normalizados = OCF + capex firmado + financiación neta − SBC; la fila de FCFE reportado permanece preservada. Proyecciones = FCFF − interés neto después de impuestos + financiación neta, explícitamente cero. SBC sigue como gasto en EBIT y no se resta por segunda vez. Se restauraron las fórmulas FY+3 sustituidas por N/D. El techo del ancla C limita g al 4% estable y no perpetúa la recuperación de corto plazo. Los múltiplos de salida son 11,66×, 17,62× y 17,62×; el peso cero obedece a volatilidad de caja, sin efecto en DCF ni ponderado.

Se mantiene la convención publicada Solo 3 años en la entrada C6 del descuento. Las sensibilidades de P/FCFE Base y sus anclas calculan resultados; las matrices de otras historias no se presentan.

## Reservas que permanecen

- NIKE no divulga I+D separada del SG&A; capitalización exacta imposible. Registro como limitación de ROIC y contraste sectorial, no como ausencia de gasto.
- Opciones: 76,8 millones detalladas al 31-may-2026; datos Q1FY27 de instrumentos mixtos (84 millones) no sustituyen opciones; valor de opciones reconocido US$123,37m; sensibilidad máxima examinada ~US$0,008/acción.
- P/FCFE cerrado: FCFE reportado preservado; normalizado después de SBC, financiación neta 0 explícita. Salidas 11,66× / 17,62× / 17,62×; VP a 3 años US$14,68 / US$23,97 / US$25,51. Peso 0 por volatilidad del flujo; no cambia DCF ni ponderado. Comparabilidad y pronóstico siguen siendo juicios.
- Comparables DECK/CROX/LULU/COLM recomputados con EV caja, leases y acciones económicas; homogeneización IFRS/USGAAP de EBITDA y arrendamientos aún limitada. UAA excluida.
- 12/12 conciliaciones de inversión y financiación FY2022-LTM cerradas; 3 desgloses no publicados de pasivos operativos marcados N/D sin afectar FCFF; controles_todas.sh previo FALLIDO en R3 (nueve filas, tres candados legados), no hay gate integral R4 certificado.

El control integral legado `controles_todas.sh` no se declara aprobado por este cierre. Su estado y los límites de certificación permanecen registrados; las verificaciones realizadas aquí son las descritas en el expediente de múltiplos.

Evidencia reproducible: [NKE.json](https://github.com/JuanMaRobledo/Modelo-JMR-datos/blob/main/evidencia/cierre-siete-multiplos-20261023/NKE.json). Valoración, análisis y este cierre comparten revisión.

---

## Auditoría anterior conservada como historial; los pendientes P/FCFE anteriores quedan sustituidos por el cierre anterior

# Auditoría JMR R4 — NIKE, Inc. (NKE) · PUBLICADA CON HALLAZGOS

## 1. Dictamen y control de versiones

**Dictamen: PUBLICABLE CON SALVEDADES; NO «VALIDADO INTEGRAL».** Revisión `NKE-JMR-20261023-R4`. Corte financiero 31-ago-2026; precio congelado 22-oct-2026 de US$38,32. Hoja revisada: [NKE R4](https://docs.google.com/spreadsheets/d/1wWS0qNCWvSrYCI53kk7H1zBshn-RJWjeKFu10sHCNWw/edit). Artículo: [Análisis Nivel 1 y Nivel 2](https://modelo-jmr.vercel.app/research.html?id=research-20261023-r2). DCF Base: **US$35,02**, MOS35%: **US$22,77**. El hash `ba82dff650baffc66557e69c85f1faca69688b1c6d7b9e4894ec974233ca9545` representa el **resultado del motor DCF R3 conservado sin cambios**, no todos los datos de la copia R4. No hay nuevo DCF recomputado por motor independiente en R4; las cuatro historias y 75 sensibilidades tienen pruebas heredadas de R3, no re-certificación integral.

**Integridad de publicación R4**: `revisionId` del registro de valoración, artículo, auditoría, manifiesto y catálogo coinciden en R4; la hoja editable corresponde al ID 1wWS0qNCWvSrYCI53kk7H1zBshn-RJWjeKFu10sHCNWw. La fecha de análisis no cambia el último dato disponible. El usuario autorizó expresamente publicar con análisis y auditoría.

## 2. Hallazgos resueltos con documentos de NIKE

| Prueba reproducible | Resultado R4 | Materialidad DCF | Evidencia |
|---|---|---|---|
| Compras/vencimientos de inversiones FY2022–2026+LTM | 6 conciliaciones exactas de flujo de inversión; residuo 0 USDm | No modifica FCFF proyectado | Pestaña «Control SEC · flujos 2022-LTM», filas 8–14; 10-K/10-Q oficiales |
| Deuda neta, emisiones, recompras y dividendos | 6 conciliaciones exactas de financiación; residuo 0 USDm | No modifica WACC ni puente debt/leases | Misma pestaña filas 15–22; notas fuente en «Cash Flow Statement» |
| FCFE histórico | FY2023 4.368; FY2024 6.617; FY2025 2.268; FY2026 2.184; LTM 2.105 USDm, antes de ajuste SBC | No entra en DCF FCFF; P/FCFE sigue peso 0 | «FCFE · conciliación SEC», fórmula OCF + capex firmado + deuda neta |
| Comparables EV por clases económicas y balance | DECK 7,92×; CROX 7,94×; LULU 4,87×; COLM 9,62× (EV/EBITDA incluyendo leases) | Contraste secundario sin cambio automático del múltiplo publicado | «Pares · conciliación SEC», fuentes SEC trimestrales |
| CapEx, OCF y deuda puente | El DCF FCFF Base US$35,02 y MOS US$22,77 permanecen idénticos tras correcciones de filas auxiliares | Directo, probado por lectura nativa de R4 | «Presentación» B5/B7 y «Valuation output» |
| Opciones, arrendamientos, WACC | Option value B30 = US$123,37m; leases activados; costo de capital «Detailed — Damodaran», control «VALIDADO» mecánico | Valor de opciones ~0,083 USD/acción; WACC específico base ~9,10% | «Input sheet» B17:B18; «Option value» B30; «Cost of capital worksheet» B84:B85 |

Las doce pruebas contables de R4 son **comprobaciones de suma de caja**, no nuevas validaciones de supuestos económicos, descuento o valor terminal. El DCF y el margen se mantienen por elección metodológica justificada por resultados de R3; las correcciones de FCFE son auxiliares y no se utilizaron silenciosamente para cambiar el valor principal.

## 3. Materialidad: qué limita la certificación y qué no

**Material para el valor intrínseco:** la convergencia de ROIC marginal terminal (15,29%) frente a WACC (~9,10%) es una hipótesis central. El DCF pasaría de 35,02 a **US$28,42** con ROIC terminal=WACC; el resultado cambia ~US$6,61/acción. La ventaja competitiva no está demostrada por los flujos y debe permanecer como sensibilidad fundamental. Los márgenes proyectados y crecimiento se mantienen como juicio, no hecho.

**Hallazgos documentales no bloqueantes del DCF Base:**

- I+D no segregada del SG&A en los 10-K: no se asigna cero ni se capitaliza un gasto inventado. ROIC ajustado industrial no es plenamente homogéneo. Afecta comparabilidad y puede influir en hipótesis de largo plazo, pero no se cuantifica efecto sin datos.
- Detalle de opciones entre mayo y agosto 2026: 76,8m opciones divulgadas mayo, strike medio 96,44, vida proxy 4,85 años. Los 84m instrumentos antidilutivos del 10-Q mezclan clases distintas. El valor reconocido en modelo es 123,37m (0,083 USD/acción); estrés simple de reclasificación 84m de opciones de iguales términos desplaza ~0,0078 USD/acción, **supuesto ilustrativo y no cota de otras estructuras**.
- P/FCFE: flujos históricos SEC reconstruidos, pero costos SBC y anclas/matrices sin homologación económica completa. Método P/FCFE **ponderación cero** y **cuatro sensibilidades N/D**; por definición no modifica el DCF Base.
- Comparables: EV y acciones económicas corregidos; EBITDA de arrendamientos no homogéneo, otras diferencias USGAAP/IFRS. Valoración por múltiplos es secundaria; R4 distingue *indicativo* de *certificado*. No usar el promedio de pares como valor sin conciliar denominadores.
- Tres filas de flujo de capital de trabajo (cuentas por pagar, impuestos por pagar, ingresos diferidos) se publican agregadas dentro de otras variaciones de pasivos y permanecen **N/D explícito**. OCF oficial sí concilia, por lo que imputarlas individualmente no es necesario para FCFF.
- Estado del control heredado: el intento real de `controles_todas.sh` contra R3 terminó en **FALLO**, aunque probabilidades y supuestos aprobaron, y M1/M2/M3 de consistencia pasaron tras actualizar contrato. Restaron fallas de integridad sobre POCF!H33, históricos y tres «candados» M34:M36 de una plantilla anterior. **No se ha ejecutado satisfactoriamente contra R4; no confundir con validación.** Logs: [última corrida diagnóstica R3](https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/40020134229).

**Estado de cierre:** valoración DCF publicable según materialidad; auditoría **CON HALLAZGOS**, estado técnico integral **PENDIENTE**. Quedan pendientes únicamente: (1) sensibilidad económica de I+D/ROIC sin fuente segregada, (2) stock options post-mayo por concesión, (3) homologación de múltiplos y FCFE de peso cero, y (4) ejecución satisfactoria del gate sobre R4. Estos límites se muestran y no impiden ocultamente acceso a los datos.

## 4. Fuentes y registros de revisión

- [10-K FY2026 de NIKE](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm).
- [10-Q NIKE al 31-ago-2026](https://www.sec.gov/Archives/edgar/data/320187/000032018726000193/nke-20260831.htm).
- [Hoja oficial R4, datos SEC y pruebas reproducibles](https://docs.google.com/spreadsheets/d/1wWS0qNCWvSrYCI53kk7H1zBshn-RJWjeKFu10sHCNWw/edit).
- [Resultado de motor R3 congelado (histórico, DCF conservado)](https://github.com/JuanMaRobledo/Modelo-JMR-datos/blob/main/documentos/NKE-20261023-R3/valoracion_resultados.json).

---

## Evidencia histórica de auditoría R3 — conserva controles previos, NO es nueva ejecución sobre R4

# Auditoría económica narrativa — NIKE, Inc. (NKE)

## 1. Ficha de auditoría y alcance

[OBSERVADO] NIKE, Inc.; NKE Class B, NYSE; USD; estados y acciones en millones. Método principal: DCF FCFF Base. Corte de información/precio 22-oct-2026; estados 31-ago-2026; auditoría 23-oct-2026. Cotización fija 38,32 del 22-oct; no se obtuvo otra cotización para mezclar períodos. [Hoja de valoración](https://docs.google.com/spreadsheets/d/1cFiWggFYuulRV11TDf6u9EY_CNWPBzWWsNiQ1qkrcxY/edit), [resultados congelados](https://github.com/JuanMaRobledo/Modelo-JMR-datos/blob/main/documentos/NKE-20261023-R3/valoracion_resultados.json), [artículo revisado](https://modelo-jmr.vercel.app/research.html?id=research-20261023-r2).

Revisión **NKE-JMR-20261023-R3**, SHA-256 **ba82dff650baffc66557e69c85f1faca69688b1c6d7b9e4894ec974233ca9545**. ReglasJMRv 5 y nuevos encabezados de análisis/auditoría del 23-oct-2026, fijados al commit 7e6ee50dca69a05839cd819ef33ba813ef0aa2f4. El prompt de valoración v 5 no cambió materialmente respecto a la revisión previa.

Esta fase se ejecuta después de valoración y análisis, por el mismo asistente en ejecución separada, sin otro escritor concurrente. Se emplea una ecuación de auditoría distinta del script de valoración. Se examinan cuatro DCF,75celdas DCF,24centros numéricos de múltiplos,4bloques N/D,registros y rangos usados de 64pestañas. No acredita todas las celdas de las cuadrículas ni auditoría contable. **Estado integral CON HALLAZGOS. Dictamen: Con reservas; auditoría condicionada. No se modificó la valoración ni el artículo durante esta fase.**

## 2. Resumen ejecutivo y relato económico central

Nike obtiene beneficio al combinar diseño, marca y distribución sobre una fabricación principalmente contratada. Esa estructura puede generar retornos altos sin fábricas propias de la misma escala. Sin embargo, inventario, descuentos y costo comercial pueden consumir caja y margen cuando el producto pierde rotación.

La tesis favorable es que innovación deportiva y normalización mayorista devuelvan una parte de la rentabilidad histórica. La hipótesis Base pide 12% de margen núcleo en año 5 y ventas LTM que pasan de 45.891 m a 48.783,55 m en año 5. No exige un crecimiento elevado sostenido, pero sí una mejora operativa clara.

La lectura neutral acepta que existe una franquicia valiosa y que su recuperación tardará varios años. La contratesis es que el problema sea de preferencia persistente: reducir costos no compensaría para siempre una pérdida de demanda a precio completo. El supuesto que más exige juicio es la durabilidad del exceso de retorno; llevar ROIC terminal a WACC reduce el valor de US$35,02 a US$28,42.

La matemática concilia. La incertidumbre normal del pronóstico está expresada como escenarios y sensibilidad. Las salvedades documentales son distintas: I+D no separado, detalle de opciones no actualizado y cobertura incompleta de determinados múltiplos/pares.

## 3. Trazabilidad, integridad y jerarquía de evidencia

| Dato | Valor | Período/perímetro | Tipo | Documento/URL/fecha | Hoja/celda | Verificación |
|---|---|---|---|---|---|---|
| Ingresos LTM | 45.891 | FY 26+Q 1FY 27−Q 1FY 26 | OBSERVADO/CÁLCULO | SEC 10K 15-jul y 10Q 2-oct-2026 | Input B 12 | Conciliado |
| EBIT núcleo LTM | 3.758 | Ventas−COGS−SG&A | CÁLCULO | Mismos documentos; estados consolidados | Input B 13 / Income L 12 | Conciliado; distinto de EBITNike 3.853 |
| Caja+inversiones CP | 8.368 | 31-ago-2026 | OBSERVADO | 10Q balance y Nota 3 | Input B 19 | Conciliado |
| Deuda contable total | 11.072 | 7.893financiera+3.179leases | OBSERVADO/CÁLCULO | 10Q balance | Input B 16/B 78 | Sin doble deuda |
| Deuda mercado total | 9.879 | 6.700bonos+3.179leases | OBSERVADO/CÁLCULO | 10Q Nota 3 | Cost C 54/C 61 | Usada en WACC; puente contable diferenciado |
| Acciones | 1.485,31 m | Portada 28-sep-2026, clases A+B | OBSERVADO | 10Q portada | Input B 22 | Correctas; no promedio diluido |
| Precio | 38,32 | Cierre 22-oct-2026 | OBSERVADO | Yahoochart; fuente secundaria de mercado | Input B 23 | Fechado y congelado |
| Rf/ERP | 5,29%/3,70% | Mismo corte mensual 1-oct-2026 | OBSERVADO | Damodaran ERPOct 26.xlsx | Input B 35 / Country B 2 | Conserva precisión 3,70% |
| Prima país | 0,87 pp adicionales | Proxy por región, no ventas-país | HIPÓTESIS/CÁLCULO | ctryprem 2026 + mezcla Nike LTM | Cost B 27 | Provisional como aproximación |
| Opciones | 76,8 m;K 96,44;vida 4,85 | Detalle 31-may;vida desplazada 3 meses | OBSERVADO/HIPÓTESIS | 10KNota 11 /10QNota 5–6 | Input B 39:B 42 | Salvedad temporal |
| Pares | 5candidatos,4P/E numéricos | Fechas de estados no idénticas | OBSERVADO/CÁLCULO | Companyfacts por emisor + cierres 22-oct | Ancla B | No certificada como ajuste homogéneo |

Cada observación original conserva etiqueta XBRL, accession, publicación, período y unidad en`observations.json`. El manifiesto protege la identidad de las fuentes descargadas. Las series históricas usan comparativos reexpresados disponibles al corte; las anclas no se presentan como un backtest sin información futura.

## 4. Historia financiera: diez años y punto de partida

[OBSERVADO/CÁLCULO] Se conservan diez ejercicios FY 2017–FY 2026 más LTM 31-ago-2026, con interpretación y tablas completas en Nivel 2. La rentabilidad reciente está por debajo del régimen histórico; no se usa el máximo como estado normal automático.

| Métrica | LTM /últimoFY | Media 3FY | Media 5FY | Media 10FY | Definición y límite |
|---|---:|---:|---:|---:|---|
| Crecimiento anual ingresos | −1,18% LTMinteranual | −3,12% | 1,03% | 3,94% | Medias de variaciones anuales, no CAGR |
| Margen bruto | 43,07% | 43,40% | 43,94% | 44,10% | Ventas menosCOGS /ventas |
| Margen EBIT núcleo | 8,19% | 9,49% | 10,86% | 11,64% | No incluye otros resultados |
| Margen OCF−capex | 4,59% | 8,22% | 8,73% | 9,18% | No FCFFniFCFE |
| ROIC núcleo /capitalfinal | 16,63% | 24,86% | 29,31% | N/Dhomogéneo | Impuestoefectivo,leases;sinI+Dcapitalizado |
| Ventas /capitalfinal | 2,56× | 3,10× | 3,15× | N/Dhomogéneo | Capital=patrimonio+deuda+leases−caja |
| Quick ratio | 1,19× | 1,34× | 1,45× | 1,49× | Caja+inversionesCP+AR /pasivoscorrientes |
| Deuda neta/EBITDA | 0,60× | 0,30× | 0,22× | 0,10× | Leasesincluidos;preASC 842nolaplenaequivalencia |
| OCF/utilidadneta | 0,90× | 1,12× | 1,08× | 1,25× | SBCseañadeaOCF,peroesun costoeconómico |

Fuente:10-K/10-Q y serieSECnormalizada. Las medias excluyen LTM. ASC 842 y la falta de I+D separado impiden afirmar un ROIC homogéneo de diez años. Pandemia, fiscalidad extraordinaria FY 2018, recompras y mezcla comercial afectan la comparación. La subida deROE no prueba mayor productividad si reduce su denominador la recompra.

[CÁLCULO] LTMventas=46.398+11.213−11.720=45.891. ComparadorLTMprevio=46.309+11.720−11.589=46.440. El−1,09%deR 2 comparabaLTMconFY;R 3corrige a−1,18% interanual. Las acciones promedio no son flujos sumables: R 3 reconstruye aproximadamente 1.481,56m básicas y 1.482,31m diluidas por duración de 365/92días. Son aproximaciones desde cifras redondeadas, distintas de 1.485,31m acciones de cierre utilizadas en DCF.

El balance concilia activos=pasivos+patrimonio. Inventarios 7.846 e inversionesCPFY 2017 de 2.371 se recuperaron de fuentes accesibles. Se completó el módulo histórico con observaciones fechadas del paquete; los faltantes iniciales de clases/EV siguen N/D. No se presenta ese módulo como un backtest sin información futura.

## 5. Crecimiento de ingresos: de la historia a la proyección

La Base proyecta contracción inicial y recuperación diferenciada por región. Norteamérica se estabiliza antes que China y Converse. La trayectoria tiene CAGR 1–51,23%; no es cinco años creciendo a una tasa constante. El escenario no puede justificarse por la cotización, que se incorpora después de formular la historia.

| Pregunta obligatoria | Respuesta |
|---|---|
| a. ¿Valor, año, unidad y celda? | Tasas C 29:G 29; diez años C 29:L 29; CAGR no redondeado 1,23%. |
| b. ¿Comparación histórica? | FY 2025−9,84%, FY 2026+0,19%, Q 1FY 2027−4,33% reportado. |
| c. ¿Mecanismo causal? | Renovación de producto, menor liquidación y recuperación de distribución. |
| d. ¿Qué debe ocurrir? | Mayorista mejora rotación y China deja de deteriorarse antes del crecimiento estable. |
| e. ¿Qué lo refuta? | Envíos crecientes sin venta final; descuentos y China permanecen débiles. |
| f. ¿Impacto si está equivocado? | Delta−1 pp:US$33,39; +1 pp:US$36,75. |

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Ingresos 1–5 | Historia irregular;LTM 45.891 m | −7,18%,+1,24%,+4,13%,+4,48%,+3,98%; Escenarios C 29:G 29 | Sector Shoe globalcrecimiento 5 a 6,38%; guía FY 2027caída dígitoalto | Recuperación modesta después del ajuste | Plausible; ventana rolling diferente del FY oficial | Prueba±1 pp arriba |


## 6. Márgenes operativos y normalización de beneficios

La normalización evita dos errores: extrapolar el margen LTM como estado estable o suponer que el máximo histórico vuelve inmediatamente. El primer año núcleo 5,25% y la tasa 25% producen EPS móvil GAAP cercano a 1,15; sumando la exclusión Pace 0,15, se aproxima el centro de la guía ajustada. La comparación es orientativa porque el período móvil termina en agosto y la guía fiscal en mayo.

Margen núcleo: media 3 a 9,49%,5 a 10,86%,10 a 11,64%;LTM 8,19%.

| Pregunta obligatoria | Respuesta |
|---|---|
| a. ¿Valor, año, unidad y celda? | Input B 28:5,67%ajustado; objetivo Base Escenarios D 5:12,42%, equivalente 12%núcleo. |
| b. ¿Comparación histórica? | La media reciente es menor que la de diez años; Nike sí ha superado 12% antes. |
| c. ¿Mecanismo causal? | Mejor precio/mezcla, menores liquidaciones, disciplina de SG&A y ahorro Pace neto. |
| d. ¿Qué debe ocurrir? | Los ahorros no se reinvierten íntegramente ni se destruye innovación al recortar. |
| e. ¿Qué lo refuta? | Mejora solo por partidas únicas o costos repetidos sin beneficio sostenible. |
| f. ¿Impacto si está equivocado? | Objetivo−1 pp:US$32,08; +1 pp:US$37,97. |

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Margen año 5 yestable | Margen núcleo: media 3 a 9,49%,5 a 10,86%,10 a 11,64%;LTM 8,19%. | Base 12%núcleo/12,42%ajustado; Valuation C 46 | Shoe global 8,80%sin ajustar; no comparación idéntica con I+D | Escala de marca rentable y reducción de descuentos | Objetivo superior a industria; requiere ejecución, no solo reputación | ±1 pp mueve aproximadamente US$3poracción |

El reintegro arancelario 986 m compensó costos del mismo FY. Restar solo el reintegro generaría una normalización incompleta. El anuncio Pace es 2,5 bn de ahorros acumulados antes de cargos/reinversión; no se sumó como 2,5 bn de flujo anual.

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

La empresa subcontrata fabricación, pero no obtiene crecimiento sin invertir. El modelo utilizaΔventas/Sales-to-Capital y mantiene la reinversión mínima en 0 ante caída de ventas. Esa restricción evita asumir una liberación inmediata de inventarios y activos no demostrada.

Capital invertido LTM aproximado=15.220+11.072−8.368=17.924,00 m. NOPATajustado histórico/capital final≈17,48%. Es un ratio con capital de cierre, no el ROICde Nike sobre capital promedio. Además, omite el activo I+D, por lo que no es plenamente comparable con la tabla ajustada de industria.

| Pregunta obligatoria | Respuesta |
|---|---|
| a. ¿Valor, año, unidad y celda? | Escenarios E 5:2,11; F 5:1,59; G 5:15,29%terminal. |
| b. ¿Comparación histórica? | Ventas/capital de cierre aproximadas 2,56; cambios de arrendamientos afectan serie. |
| c. ¿Mecanismo causal? | La reinversión financia crecimiento y mantiene la productividad del capital. |
| d. ¿Qué debe ocurrir? | La recuperación comercial se convierte en ventas sin inventarios estructuralmente mayores. |
| e. ¿Qué lo refuta? | Mucho capital nuevo con poco crecimiento o ahorro que exige inversión no mode lada. |
| f. ¿Impacto si está equivocado? | ROIC terminal=WACC lleva a US$28,42; efecto I+D no cuantificable sin serie. |

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| S/C y ROIC | LTM ajustado aproximado 17,48%; no ROIC 10 a homogéneo | S/C 2,11→1,59; ROICestable 15,29% | Shoe global S/C 2,11 y ROICajustado 15,29% | Convergen margen, eficiencia, impuesto yretorno | Reserva: falta I+D; activo económico no inventado | Escenario sin exceso terminal arriba |

No se confunde margen×S/C marginal con el ROIC contable de activos existentes. Recompras y dividendos son distribución, no inversión operativa. Las correcciones de margen y transición temporal de S/C ocurrieron en Valoración R 2 antes del congelamiento; esta auditoría no la modifica.

## 8. Costo del capital y riesgo

El costo de capital se calcula con beta bottom-up global porque las ventas no se concentran mayoritariamente en Estados Unidos. El riesgo de producto se incorpora en las historias. No se añade otra penalización genérica por las mismas dificultades operativas.

Ke 9,90%; WACC 9,10%; betaapalancada 1,01; beta U 0,89; Kd 6%[juicio]. El riesgo país utiliza proxies regionales y un incremento sobre el componente estadounidense de la tabla anual. La exposición exacta a cada país no está disponible.

| Pregunta obligatoria | Respuesta |
|---|---|
| a. ¿Valor, año, unidad y celda? | Cost B 63/E 63; Input B 35; maduro Country B 2; costo terminal Input B 47. |
| b. ¿Comparación histórica? | Se usa corte mensual coherente, no una media histórica de tasas para el descuento actual. |
| c. ¿Mecanismo causal? | Beta sectorialreapalancada y pesos de deuda/patrimonio de mercado. |
| d. ¿Qué debe ocurrir? | La mezcla geográfica y costo marginal no se apartan materialmente de los proxies. |
| e. ¿Qué lo refuta? | Desglose país, spread o estructura financiera contradicen las aproximaciones. |
| f. ¿Impacto si está equivocado? | WACC inicial−1 pp:US$37,22; +1 pp:US$32,98; beta OLS:US$34,94. |

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Tasas ybeta | Beta OLSsemanal 5 a 1,02;260 observaciones | Rf 5,29% /ERPtotal 4,57% /WACC 9,10% | Damodaranenero 2026 y ERP 1-oct-2026 | Primapaísregional porventas, conpesos demercado | Kd ydetalle por país sonjuicios explícitos | Pruebasnuméricas arriba |


## 9. Convergencia y valor terminal

El terminal representa 64,80% del valoroperativo Base. g 4%nominal USD respeta Rf 5,29% y WACC terminal 8,99%. No se infiere que 4%sea una predicción cierta; es la regla de corte JMR aplicada en la misma moneda.

La ventaja de marca puede sobrevivir, pero tiene que seguir produciendo retorno. El ROIC terminal 15,29% es inferior al mejor régimen histórico de Nike y superior a WACC. La reserva económica es la duración de esa ventaja, además de la diferencia contable I+D. La sensibilidad a ROIC no certifica la hipótesis.

| Pregunta obligatoria | Respuesta |
|---|---|
| a. ¿Valor, año, unidad y celda? | Input B 69:g 4%; B 47:WACC 8,99%; Escenarios G 5:ROIC 15,29%. |
| b. ¿Comparación histórica? | Industria global ajustada como ancla; no elmejor dato Nike. |
| c. ¿Mecanismo causal? | Se reinvierteg/ROIC y S/Cconverge hacia ROIC/[margen×(1−t)×(1+g)]. El retorno marginal relaciona reinversión_t y ΔNOPAT_(t+1); no obliga al ROIC agregado del capital existente a igualarse inmediatamente. |
| d. ¿Qué debe ocurrir? | La rentabilidad de marca permanece por encima de un negocio sin ventaja. |
| e. ¿Qué lo refuta? | La competencia elimina poder deprecio oeleva capital requerido. |
| f. ¿Impacto si está equivocado? | Valor sin exceso terminal US$28,42; matriz WACC×g mantiene el WACC inicial yrecalcula transición. |

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Convergencia terminal | No puede observarse unresultado perpetuo | g 4%; reinversiónterminal 1.495,46 m | ROICindustria 15,29% | FCFF 11incluye capitalnecesario; no crecimiento gratuito | Moatdurablees juicio; sensibilidad explícita | PVterminal/EV 64,80% |


## 10. Validación independiente del valor intrínseco

La implementación independiente reproduce cuatro DCF de la hoja con error inferior a 0,001poracción. Base: VPexplícito 19.308,41 m+VPterminal 35.539,64 m=EV 54.848,05 m. Después se suman 8.368 m decaja y se restan 11.072 m dedeuda contable y 123,37 m de opciones; dividido por 1.485,31macciones resulta US$35,02.

El WACC usa deuda demercado 9.879 m, mientras elpuente utiliza la convencióncontable de la plantilla. Se cuantificó la alternativa: deuda demercado en elpuente lleva a US$35,83, diferencia US$0,80. Conviene homogeneizar esa convención en un cambio metodológico explícito, en vez deocultarla como prudencia.

| Pregunta obligatoria | Respuesta |
|---|---|
| a. ¿Valor, año, unidad y celda? | Valuationoutput B 18:B 35; opciones B 30; acciones Input B 22. |
| b. ¿Comparación histórica? | Se contrasta histórico, pero el valor sale de flujos futuros y supuestoscongelados. |
| c. ¿Mecanismo causal? | FCFFdescontado yterminal económico, puente alpatrimoniocomún. |
| d. ¿Qué debe ocurrir? | Todos losreclamos están contabilizados unavez y lasunidadescoinciden. |
| e. ¿Qué lo refuta? | Doble deuda, acciones de unasolaclase, opciones duplicadas oterminal sinreinversión. |
| f. ¿Impacto si está equivocado? | Reproducciónporhistoria y raíz inversa conservadas enaudit_checks.json. |

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| DCF Base | R 1base 35,43; R 2corrige trayectoria y convención de reinversión | B 35=35,02 | Motor propio independiente y Google Sheets | Suma flujosperpetuidadreclamos/acciones | Reserva documental enopciones, no error deigualdad | 53 controles aprobados en alcance;5 hallazgos |


## 11. Cuatro historias y probabilidades

| Historia | Crecimiento CAGR 1–5 | Margen núcleoobjetivo | S/Caño 10 /ROIC terminal | WACC inicial/terminal | gterminal | Valor USD/acción | Probabilidad | Confirmación/refutación |
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
| PE | 29,25 | 10,62 | 14,07 | 14,07 | 2.936,33 | 27,74 | 24,98 | 40,00% |
| PFCFE | N/D | N/D | 18,05 | N/D | 2.231,18 | N/D | N/D | 0,00% |
| POCF | 34,09 | N/D | 8,68 | 8,68 | 4.353,98 | 25,36 | 23,19 | 0,00% |
| PV | 3,79 | N/D | 0,92 | 0,92 | 44.906,61 | 27,74 | 24,98 | 0,00% |
| PBV | 11,57 | N/D | 2,45 | 2,45 | 16.839,11 | 27,74 | 24,98 | 0,00% |

El consolidado US$25,96 es secundario.60%EV/EBITDA y 40%P/E reflejan dos perspectivas útiles; no se cuentan EV/FCFF, P/Vy P/BV como confirmacionesadicionales cuando son transformaciones del mismo techo C. P/OCF conserva eladdback SBC, su definición no equivalea FCFF.

El ancla B no está certificada:UAA tiene variasclases, DECK carece de D&Aconciliada en laextracción y los EV de pares conservanlímites debalance. Una diferencia>25% frente alos pares exige explicación, pero la explicación no sustituye la conciliación. La Optimista tiene múltiplos porencima de losactuales; su justificación es uncrecimiento FY+3 superior y margen 15% núcleo. Esa historia exige validación futura; no se declara que el mercado deba conceder ese múltiplo.

P/FCFE seleccionado permanece N/D porque loshistóricos antes denueva financiación no son un FCFEcompleto. Se excluye delponderado. El ajuste por tasas, techos C y centros se recalcularon en la valoración, sin factores genéricos Toro 0,8/0,9/1,1.

## 13. Sensibilidades económicas y escenarios alternativos

[MODELO] Las tres matrices del DCF Base tienen centro 35,02. Se reprodujeron sus 75celdas con ecuaciones independientes: WACC terminal×g recalcula transición y descuento; ROIC terminal×g recalcula capital/reinversión; crecimiento×margen desplaza las cinco tasas originales y recalcula toda la trayectoria.

El inverso central encuentra una raíz en−50pp a+80pp, añade 1,87pp comunes y produce CAGR 3,10% frente a 1,23% Base; recompone 38,32 con error inferior a 0,001. Las alternativas congeladas deValoración con márgenes núcleo 11% y 13% ybetas bottom-up/OLS están reproducidas en sección 12 del artículo. Exigen CAGR aproximadamente 5,01%/5,06% y 1,42%/1,46%, respectivamente. No son nuevasvaloracionesoficiales ni una probabilidad revelada del mercado.

Múltiplos:28bloques Base,24numéricos y 4N/D,todosP/FCFE. Se retiró también el ancla observada que utilizaba un flujo sin financiación conciliada. Dos anclas y dosfamilias por método: múltiplo real en veces frente a fundamentalFY+3 o driver económico que recalcula el denominador. Los 24centros coinciden con el valor relativo específico del método/ancla; losN/Dno secuentan como validación. Las matrices Conservadora/Optimista heredadas permanecen fuera de la familia oficial.

[HIPÓTESIS] La prueba más importante eserosión del retorno terminal:35,02→28,42 conROIC=WACC. La diferencia cuantifica dependencia delmoat; no demuestra que Nike carezca de él. La prueba de margen ±1pp produce 32,08/37,97 yla de crecimiento ±1pp 33,39/36,75. No se suman esos efectos como independientes.

## 14. Coherencia de hojas, cálculos y presentación

[OBSERVADO] Hoja,resultado congelado,artículo ydictamen se identifican como **NKE-JMR-20261023-R3** y comparten **ba82dff650baffc66557e69c85f1faca69688b1c6d7b9e4894ec974233ca9545**. El paquete para publicación conserva las rutas estables del visor/análisis y vincula su expedienteR 3. El nombre histórico de un archivo terminadoR 2no define su revisión vigente; la determina revisionId. La evidencia originalR 2no se elimina.

En controles previos a esta auditoría se corrigieron:comparador de crecimientoLTM, suma inválida de promedios de acciones, inversiónCPFY 2017 ausente, anclaobservadaP/FCFE no conciliada y auxiliares históricos vacíos. Estos últimos originaban 45errores deMEDIAN/AVERAGE sobre rangos sin datos. Se incorporaron observaciones históricas ya trazadas y se dejóFCFE N/D donde no corresponde usarFCF; no se rellenaron errores con cero. La relectura de los rangos usados de 64pestañas devuelve cero erroresdecelda en ese alcance. El DCF y el relativo ponderado permanecen 35,02 y 25,98.

Se comprobó semánticamente la ampliación del artículo respecto alR 2,que era demasiado breve en negocio,gobierno,competencia,calidadfinanciera,filosofías y seguimiento. ElR 3tiene 18secciones,subsecciones obligatorias,Porter de 5fuerzas,Síntesis final de 3párrafos,tabla por estado financiero/ratios ymatriz de 30apartados/subapartados. El recuadroBase aparece primero;Nivel 1conserva el artículo yNivel 2contiene cálculos. No se usa el conteo de títulos para validar la evidencia.

La actualización incorporó los 8-K deagosto/septiembre:DavidDenton es CFO actual ycontroller interino,existe autorización adicional de 16maccionesESPP yelconsejo aumentóa 12conAlexandreArnault. La autorización deacciones no se sumócomo emisión realizada. Limitaciones editoriales identificadas:TAM/cuota homogénea,economíaunitaria/retención,ROIC 10añoscomparable,I+D,desglose deopciones ypares. Los apartados están desarrollados con alcance explícito,pero esas limitaciones impiden calificarlos de evidencia plenamente resuelta.

No se afirma una prueba visual autenticada delvisoryPDF. El cierre de publicación requiere leer de nuevo lasrutas,y contrastar revisión,huella y cifras delcontenido servido. Un despliegueREADYpor sí solo no sustituye esa comprobación de datos.

## 15. Hallazgos priorizados y propuestas de corrección

| ID | Severidad | Tipo | Evidencia | Impacto | Mantener/ajustar/investigar | Propuesta y alternativa | Requiere aprobación | Estado |
|---|---|---|---|---|---|---|---|---|
| H 01 | Alto | Comparabilidad | I+D en gastos,sin serie separada | ROIC no plenamente homogéneo con industria;impacto no cuantificable sin serie | Investigar | Obtener desglose y vida útil,o mantener modelo sin capitalización explícito | No para investigar | Límite documental abierto |
| H 02 | Medio | Dato | Opcionesmayo frente a corteoctubre | Reclamo patrimonial 123,37;no límite exacto con agregado 84m | Investigar | Movimientos por opción,ejercicio,plazo yRSU | No para investigar | Límite documental abierto |
| H 03 | Medio | Definición | FCFE histórico no concilia financiación | Peso 0;cuatro matricesN/D;DCF yponderado sin efecto | Mantener exclusión | Conciliar financiación antes de restituir anclas | Nueva revisión si se da peso | Presentación corregida;fuente limitada |
| H 04 | Medio | Pares | AnclaBno completamente homologada | Contraste indicativo,no cuantificación independiente certificada | Investigar | Conciliar EV,clases,D&A,moneda,leases yriesgo | No para investigar | Límite documental abierto |
| H 05 | Alto | Control operativo | Script legado intentado,no completado en este entorno | Impide estadoVALIDADO integral | Completar entorno yregistro | Conectar módulos,registro de hoja nueva yautenticación;no alterar las pruebas | No para verificación autorizada | CON HALLAZGOS |
| J 01 | Medio | Juicio | ROIC terminal 15,29%>WACC 8,99% pese a erosión reciente | Sinexceso terminal 28,42 vs 35,02 | Revisar con hechos | Exigir recuperación de preferencia yretorno;alternativa terminalsin exceso | Nueva revisión dehistoria | Hipótesis refutable |
| J 02 | Bajo | Convención | DeudamercadoenWACC,contableenpuente | Alternativa 35,83;diferencia 0,80 | Homogeneizar método | Regla explícita para puente,no recorte oculto | Cambio metodológico explícito | Explicado |
| J 03 | Medio | Juicio | Kd 6% yprimapaísregionalproxy | WACC inicial±1pp:32,98–37,22 | Investigar | Países yspreadmarginal almismocorte | Nuevaentrada documentada | Explicado |
| C 01 | Medio | Cálculo auxiliar | LTMcomparado conFY ypromedios deacciones sumados | YoY−1,18%;EPSaprox 2,09;DCFsin cambio | Mantener corrección | Duración de períodos ydenominador correctos | Autorizado por revisión | Cerrado enValoraciónR 3 |
| C 02 | Medio | Presentación/fórmula auxiliar |45errores por módulo histórico vacío | Cero errores en rangos reexportados;sin cambioDCF | Mantener | Histórico trazado yFCF≠FCFE | Autorizado por revisión | Cerrado enValoraciónR 3 |
| C 03 | Medio | Completitud | R 2no desarrollaba mínimos del nuevo prompt | Podía omitir riesgos yhechos de gobierno | Mantener ampliación | Artículo íntegro ymatriz de 30apartados | Autorizado | Cerrado con límites documentales |

Los hallazgos documentales no se confunden con incertidumbre normal del pronóstico. La auditoría no modifica inputs para lograr un dictamen favorable. Las correcciones cerradas ocurrieron en el componente responsable antes del congelamiento final del artículo; la presente fase solo verifica yrecomienda.

## 16. Catalizadores, señales de refutación y seguimiento

| Métrica | Nivel observado | Señal favorable propuesta | Señal adversa propuesta | Fuente | Frecuencia |
|---|---|---|---|---|---|
| Ingresos Q 1FY 27 | −4% reportado;−5%neutral FX | Dos trimestres creciendo con volumen | Dos trimestres≤−5%neutral FX | 10Q/IR | Trimestral |
| Digital | −13%neutral FX | Estabilización sin mayores descuentos | Persistencia de caída≥10% | 10Q | Trimestral |
| China | 1.180 m Q 1vs 1.512 m | Caída<5%y margenmejora | Ventasy margen siguen deteriorándose | 10Q | Trimestral |
| Margenbruto | 42,8%;+60pb | Mejora sin partidasúnicas | Ahorro logístico compensadopor descuentos | 10Q | Trimestral |
| Pace | 2,5 bn acumulados;1 bn cargos | Ahorro netocaja observable | Máscargos/reinversión absorbenbeneficio | 8K/IR | Trimestral |
| Retorno | ROICsujetoabasecontable | Mejora operativa sin expansión improductiva de capital | Inventarios yactivoscrecen másqueventas | Estados | Trimestral |

Los umbrales son criterios del auditor; no se presentan como guía de Nike. No se anunció una fecha de siguiente resultado que no estuviera confirmada en el expediente.

## 17. Dictamen económico y resumen para escuchar

**Dictamen económico: Plausible con reservas. Estado integral: CON HALLAZGOS.**

**Consistencia matemática:**53comprobaciones validadas en el alcance:cuatroDCF,75celdasDCF,inverso,centrosrelativos,puentes,auxiliares ycontroleseditoriales. Loscinco registros conhallazgos corresponden aI+D, opciones,pares,financiaciónFCFE ypuerta legada no completada;no son cincoerrores deDCF. Los bloquesN/Dse verifican como ausencias,no como resultadosnuméricos.

**Trazabilidad documental:** estadosrecientes yfuenteshistóricas están identificados,pero quedan límites explícitos. **Razonabilidad económica:** recuperación gradual es defendible,con evidencia favorable ycontraria; la persistencia delmoat esmás frágil que el punto de partida contable. LaBaseexige recuperación de margen por producto/mezcla/costos,no solo el retorno automático de ventas a su máximo. Clasificar la empresa en declive para laprevia ymantener ventaja durable enBase no es imposible,pero requiere distinguir faseactual de resultados yfranquicia de largo plazo.

Decisión analítica:conservar el cálculo como estimación revisable conhallazgos,seguir señales de demanda/calidaddecaja yrevisar formalmente el retorno terminal si continúa la erosión. No se emite recomendación decompra/venta. **No se modificó la valoración ni el artículo durante la auditoría.**

### Resumen oral

Nike conserva una marca y una distribución valiosas, pero la recuperación debe aparecer en ventas rentables y caja. La revisión mantiene un valor base de 35,02dólares y un precio con margen de seguridad de 22,77. Los cuatro escenarios,las sensibilidades yel inverso concilian con la hoja. Se corrigieron comparaciones LTM,acciones promedio yel uso de un flujo sin financiación como FCFE. El análisis amplía los dieciocho apartados e incorpora los cambios recientes de equipo ygobierno. El resultado depende de recuperar margen yconservar retornos superiores al costo del capital. Persisten límites en investigación ydesarrollo,opciones ycomparables,además de una puerta decontrol legada no completada. El dictamen es plausible con reservas,con hallazgos visibles ysin certificación integral.

## 18. Fuentes primarias, limitaciones y registro de versión

`prompt_version: auditoria-economica-jmr-v1.2` conampliación editorial 23-oct-2026;ReglasJMRv 5;protocolooptimizado 1.1. Prompts fijados al commit 7e6ee50dca69a05839cd819ef33ba813ef0aa2f4. Revisiónauditada **NKE-JMR-20261023-R3**;huella **ba82dff650baffc66557e69c85f1faca69688b1c6d7b9e4894ec974233ca9545**. La ejecución separada yorden de congelamiento constan en`fases_ejecucion.json`.

- [10-KFY 2026,15-jul-2026](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm):negocio,estados,compromisos ypolíticas.
- [10-Q 31-ago,2-oct-2026](https://www.sec.gov/Archives/edgar/data/320187/000032018726000193/nke-20260831.htm):LTM,segmentos,caja,deuda ycontingencias.
- [Guía/Pace,1-oct-2026](https://www.sec.gov/Archives/edgar/data/320187/000032018726000184/q1fy27exhibit991er.htm):ancla temporal ycostos.
- [Proxy,15-jul-2026](https://www.sec.gov/Archives/edgar/data/320187/000032018726000089/nke-20260715.htm)y 8-Kde 10-ago/10-sep/16-sep:remuneración,gobierno,cambiodeCFO/controlleryESPP. Accesiones enbibliografía del artículo.
- [SEC Companyfacts](https://data.sec.gov/api/xbrl/companyfacts/CIK0000320187.json):observaciones yperíodos;archivodel 22-oct,no se incorporanhechos posterioresalcorte.
- [DamodaranERP 1-oct](https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx),betaGlobal,rocGlobal,capexGlobal yctrypremenero 2026:tasas yreferencias. Cadaarchivo yURL figuran enbibliografíadel análisis.
- [AdidasFY 2025](https://report.adidas-group.com/2025/en/) y[OnQ 2,11-ago-2026](https://investors.on-running.com/news/news-details/2026/On-Reports-Results-for-the-Second-Quarter-and-Six-Month-Period-Ended-June-30-2026/default.aspx):contraste decompetencia,márgenes ymezcla,sin homologación automática.
- [TheBaseRateBook,26-sep-2016](https://josephnoko.com/wp-content/uploads/2024/04/The-Base-Rate-Book-Michael-Mauboussin.pdf):Exhibit 4,cohorte>25bnreales 2015;bandas defrecuencia,no probabilidadesNike.
- [ReglasJMRv 5](https://github.com/JuanMaRobledo/Modelo-JMR/blob/7e6ee50dca69a05839cd819ef33ba813ef0aa2f4/modelo/REGLAS_VIGENTES.md):método ycompletitud.

Consulta derevisión 23-oct-2026;documentos originales reutilizados con susperíodos yprocedencia. Datosdescargados,análisis previo ynuevo,registrodecontroles,exportaciónnativa yhuellas se conservan. El resultadoR 2 anterior queda como antecedente,sin emitirle retroactivamenteun dictamenR 3.

Limitaciones deejecución:`controles_todas.sh NKE`se intentó yno completó por componentes/registro delentorno legado;log incluido. No se afirma una ejecución deproducción validada deesecontrol. Tampoco una prueba visual de sesiónautenticada ni latarjetaPDF. Las verificaciones depublicación porrutas,revisionId,huella yDCF se registran por separado después deescribir elpaquete,con autorización vigente. Ruta prevista:`Modelo-JMR-datos/auditorias/narrativas/NKE.md`. Elestadofinanciero integral permaneceCON HALLAZGOS aunque lasrutas estén sincronizadas.

