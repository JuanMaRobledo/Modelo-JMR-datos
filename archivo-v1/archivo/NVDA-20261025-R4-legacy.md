# Auditoría JMR · NVDA · recaptura del 2026-10-26

**Revisión financiera: NVDA-20261025-R4** · cierre RECAPTURA-20261025-FORMULAS-PROPIAS · sustituye a NVDA-20261025-R3.

**Dictamen vigente: VERIFICADO CON SALVEDADES en el alcance documentado.** Sin cambios de supuestos, probabilidades ni pesos.

**Qué cambió:** se migraron a la plantilla las fórmulas propias de la hoja; solo cambian los valores a un año de P/FCFE (precio y VP de FY+1); precio objetivo ponderado, DCF Base y MOS idénticos.

**Controles ejecutados:** `controles_todas.sh` sin fallas y verificador de la recaptura con 0 fallas. [Registro](https://github.com/JuanMaRobledo/JMR-valuation/tree/main/reference/revisiones/Recaptura-Publicacion-20261025).

**Salvedades vigentes:** CAGR Base36,28% y escala año5 son hipótesis exigentes; no las certifica un TAM independiente. ROIC marginal estable27,23% requiere ventaja durable; prueba sin moat USD286.10. I+D/ventas7,79% y vida3años son juicios; GAAP año5≈56,23%,58% es referencia estable. Múltiplos secundarios comparten techo fundamental; no son siete confirmaciones independientes. Serie ROIC histórica ajustada3/5/10años N/D; límites de geografía por sede, concesiones y pares explícitos. Controles centrales ejecutados sobre captura directa de valores y fórmulas; historial Drive y comparación con hojas no capturadas no certificados.

**No re-ejecutado:** `engine_verification` de la app y revisión visual; los archivos de verificación de la carpeta de documentos son de la revisión anterior y están rotulados como heredados.

### Antecedente de auditoría conservado · no es el dictamen técnico vigente

Lo que sigue describe la situación anterior a esta recaptura; las reservas económicas/documentales siguen vigentes.

---
# Auditoría económica narrativa — NVIDIA (NVDA)

Revisión auditada: **NVDA-20261025-R4**. Informe de auditoría: **NVDA-AUD-20261024-R2**. Corte de valoración y precio: **23 de octubre de 2026**. Emisión: **24 de octubre de 2026**. Moneda: USD; cifras financieras en millones salvo indicación. Dictamen técnico del expediente: **consistente en los controles ejecutados**. Tesis económica: **Exigente**. Estado técnico: controles ejecutados según el registro adjunto; publicación autorizada. Las limitaciones de evidencia y las reservas económicas permanecen explícitas.

## 1. Ficha de auditoría y alcance

[OBSERVADO] NVIDIA Corporation, NVDA, acción común negociada en Nasdaq; ISIN no comprobado en este expediente. Empresa operativa del sector semiconductores y computación acelerada. Método principal FCFF descontado al WACC. Precio de referencia USD 210,96, cierre del 23-oct-2026; no se incorpora una cotización posterior. Último balance utilizado: 26-jul-2026. Flujos LTM: FY2026 más H1 FY2027 menos H1 FY2026.

Se examinaron la [hoja nativa](https://docs.google.com/spreadsheets/d/1gbtwORZsvjhZNCV8xlNDloHYEeE09cEbXmPZOoLJ8gY/edit), su exportación, data.json, assumptions.json, scenarios.json, results.json, multiples-inputs.json, multiples-results.json, matrices.json, verification.json y el artículo completo de esta revisión. Se revisaron fuentes SEC descargadas, archivos de Damodaran y cotizaciones históricas identificadas en el registro. La revisión usa una reproducción matemática separada del cálculo nativo; la realizó el mismo asistente que preparó el expediente. **No constituye revisión por una persona o firma independiente, ni auditoría contable.**

El cálculo se contrasta con19 controles propios,18 estados nativos y los scripts centrales vigentes fijados al commit596276eb337c45edf84cf53d29a7ceec848fb40e. El transporte de lectura usa la captura directa del conector de Google Sheets, identificada y fechada, con valores y fórmulas reales; no simula nuevas consultas ni un historial de revisiones no capturado. El control de fórmulas se limita a las pestañas y rangos capturados; no certifica por comparación mayoritaria las demás empresas de la cartera. La evidencia de ejecución y de publicación se conserva en archivos separados. Esta distinción evita equiparar18 controles propios con18 candados de la plantilla.

## 2. Resumen ejecutivo y relato económico central

[OBSERVADO] NVIDIA obtiene ingresos de hardware, sistemas, redes y software para computación acelerada. La propuesta económica combina rendimiento, herramientas de desarrollo, bibliotecas y capacidad para integrar grandes sistemas. Compute & Networking representa alrededor del 90,9% del ingreso LTM. El gasto de sus clientes en infraestructura de IA es el motor inmediato, pero ese gasto debe terminar respaldado por usos con rentabilidad suficiente.

[HIPÓTESIS] La historia Base sostiene que inferencia, entrenamiento y nuevos usos empresariales amplían la demanda mientras CUDA, redes e integración conservan una parte importante de las rentas. Los ingresos crecen 36,28% compuesto durante cinco años, hasta USD 1,424 billones en el año 5. Esto exige un mercado mucho mayor, capacidad física disponible y clientes capaces de monetizarla. La existencia del ecosistema no demuestra por sí sola esa escala de ingresos.

[INFERENCIA] La interpretación neutral reconoce una compañía extraordinariamente rentable que atraviesa una expansión cíclica difícil de extrapolar. La contratesis adversa combina exceso de infraestructura, mayor eficiencia por dólar de cómputo, chips diseñados por clientes y concentración de compradores. En ella pueden caer a la vez crecimiento y margen, mientras los compromisos financieros limitan la flexibilidad.

[MODELO] El DCF Base de USD 381,79 depende principalmente de volumen y duración de rentas, y una parte importante del valor operativo proviene del terminal. La diferencia frente al precio observado no constituye una constatación de infravaloración independiente de los supuestos. La contradicción que debe resolver la empresa es transformar el gasto excepcional de sus compradores en una demanda duradera y financiable.

## 3. Trazabilidad, integridad y jerarquía de evidencia

| Dato | Valor | Período / tipo | Documento y fecha | Hoja / referencia | Verificación |
|---|---|---|---|---|---|
| Ingresos / EBIT | 302.970 / 197.579 | LTM / observado | 10-Q 26-ago + 10-K 25-feb-2026 | Income Statement!L3/L12 | Conciliado |
| CFO / CAPEX | 134.360 / 7.354 | LTM / observado | Mismos estados | Cash Flow Statement; data.json | FCF 127.006 |
| Deuda y leases / activos líquidos | 38.860 / 99.369 | 26-jul-2026 / observado | 10-Q, notas | Input sheet!B16/B19 | Sin duplicaciones identificadas |
| Acciones del puente | 24.268 millones | Portada 21-ago + RSU julio / modelo | 10-Q y nota SBC | Input sheet!B22 | Básicas + concesiones conocidas |
| Precio | 210,96 USD | 23-oct-2026 / observado | Histórico Yahoo, consulta 23-oct | assumptions.json | Fecha congelada |
| Rf / ERP madura | 5,29% / 3,69748% | 1-oct-2026 / fuente económica | ERPOct26 B10/C45 | Input sheet!B35; Country ERP | Mismo archivo |
| Tax inicial / marginal | 17% / 25,37% | Normalización / modelo | Guía 16–18%; archivo industria | Input sheet!B90/B25 | Juicios separados de realizados |

La jerarquía aplicada es documento SEC original, notas y estados; después datos XBRL con acceso y período identificados; luego archivos de tasas/industria; finalmente cotizaciones y juicio. `provenance.json` conserva etiquetas, fechas, unidades y accession; `normalization-log.json` registra ajustes. Una etiqueta XBRL no sustituye el examen de la nota cuando existe ambigüedad. Los datos de pares tienen períodos fiscales diferentes, explícitos en peers.json.

Las ventas geográficas están clasificadas por sede del cliente; no equivalen a ubicación final de uso ni a un mapa completo de riesgo económico. Los USD 30.000 millones aproximados de ganancias de inversión incluidos en el beneficio neto LTM no se extrapolan como beneficio operativo recurrente en los múltiplos normalizados.

## 4. Historia financiera: diez años y punto de partida

El anexo Nivel 2 contiene los diez FY2017–FY2026 y LTM, sin mezclar stock de balance con flujo anual. Ingresos pasan de 6.910 a 215.938 millones entre FY2017 y FY2026; el LTM alcanza 302.970 millones. FY2023 evidencia que el crecimiento y los márgenes no avanzan de manera uniforme: EBIT de 4.224 millones frente a 10.041 en FY2022, antes del salto de los años siguientes.

| Métrica | FY2026 | Media 3 FY | Media 5 FY | Media 10 FY | LTM |
|---|---|---|---|---|---|
| Ingresos | 215,938.00 | 135,785.67 | 92,249.00 | 51,717.80 | 302,970.00 |
| EBIT | 130,387.00 | 81,604.00 | 51,815.40 | 27,540.30 | 197,579.00 |
| CFO | 102,718.00 | 64,965.67 | 41,929.20 | 22,914.60 | 134,360.00 |
| CAPEX | 6,042.00 | 3,449.00 | 2,631.20 | 1,614.20 | 7,354.00 |
| FCF | 96,676.00 | 61,516.67 | 39,298.00 | 21,300.40 | 127,006.00 |
| SBC | 6,386.00 | 4,890.67 | 3,877.00 | 2,282.10 | 7,241.00 |
| Margen EBIT | 60.38% | 58.97% | 45.98% | 37.66% | 65.21% |

Los promedios de margen son medias aritméticas de ratios anuales, no margen sobre la suma de ventas. El rango GAAP anual de diez años es 15.66% a 62.42%. La tabla anual permite identificar el cambio de régimen mejor que una media única. CAPEX reportado es inversión física, no toda la reinversión económica; I+D y capital de trabajo requieren tratamiento adicional.

[NO VERIFICADO] No se presenta una serie de ROIC ajustado históricamente homogénea a tres, cinco y diez años con cohortes equivalentes para cada año. Tampoco una serie ajustada completa de capital incremental y recompras. Estos promedios quedan N/D; no se sustituyen por el ROIC actual ni por margen multiplicado por ventas/capital. El dato de inversiones privadas FY2017–FY2019 no se presume cero. Son límites de comparación histórica; no alteran el puente actual ni certifican persistencia de retornos.

## 5. Crecimiento de ingresos: de la historia a la proyección

La Base conserva el liderazgo durante una fase de expansión, pero lo desacelera con la escala. Compute & Networking crece 75%, 50%, 32%, 23% y 17%; Graphics, 20%, 15%, 12%, 10% y 8%. El crecimiento agregado resultante es 70,00%, 47,75%, 31,00%, 22,44% y 16,65%. Años 6–10 convergen gradualmente al 4%. El año 1 mantiene un punto de partida extraordinario; el argumento favorable requiere adopción y suministro suficientes, no solo demanda anunciada.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Ingresos, años 1–10 | FY2017 6.910; FY2026 215.938; LTM 302.970; historia anual y medias en §4 | CAGR 1–5 36,28%; año 5 1.423.928,64; Escenarios e historias / Valuation output | Pares SEC con menor margen y modelos distintos; no certifican TAM | Expandir inferencia y oferta; clientes monetizan capacidad; mantener cuota | ASIC, limitaciones energéticas, pedidos decrecientes o retornos bajos del comprador | −5 pp anuales iniciales: USD 301,70; +5 pp: USD 481,98 |

Las seis preguntas quedan respondidas en la fila: valor/horizonte/celda; referencia histórica; mecanismo; condiciones necesarias; falsadores; y efecto cuantificado. La cifra exigida del año 5 debe compararse con ingresos económicos efectivamente monetizables y no con un TAM sumado entre entrenamiento, inferencia y gasto total de centros de datos. No se encontró una estimación independiente que certifique esa escala exacta. El inverso del precio necesita 23,61% de CAGR a cinco años bajo los demás supuestos Base; es una transformación condicional del modelo, no una previsión de consenso.

## 6. Márgenes operativos y normalización de beneficios
La escala, el software y el costo de cambiar plataformas sostienen rentas; concentración, ASIC y costos de sistemas completos pueden erosionarlas. R1 trasladaba a la madurez un ajuste histórico de I+D y leases de4,18 puntos sobre ventas. Esa extrapolación no se conserva: R2 utiliza un puente prospectivo por cohortes, manteniendo el calendario original de diez años y su transición de margen.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Margen económico objetivo / referencia GAAP estable | Medias GAAP58,97/45,98/37,66%; LTM65,21% | 58,6906% económico año5;58% GAAP estable; Escenarios!D5 / Puente I+D | Pares SEC con mezcla distinta; no comparar GAAP con económico | I+D recurrente mantiene plataforma; amortización de3cohortes | Vida3años e I+D/ventas7,79% son hipótesis; obsolescencia y competencia pueden cambiar ambas | −5pp objetivo: USD350.13 |

Se parte de gasto23.592 y cohortes previas15.384/10.569/7.812; amortización11.255 y activo37.371. Se proyecta I+D con intensidad7,7869% de ventas y amortización lineal de tres cohortes previas. Con crecimiento estable4%, el aporte neto de I+D es0,5838puntos; leases añaden0,1068. El margen económico estable es58%+0,5838+0,1068=58,6906%. Esto reduce la distorsión de perpetuar el ajuste del período de expansión.

El margen económico inicial común es69,1872%; la plantilla lo lleva al objetivo en año5 con su denominador cinco. En cada año GAAP=económico−I+D neta/ventas−ajuste leases. La Base implica aproximadamente56,23% GAAP en año5, con recuperación posterior conforme madura la amortización;58% describe el estado estable y no una celda GAAP forzada en año5. Las cuatro historias tienen el mismo margen económico inicial por diseño de la plantilla; sus cohortes e implicaciones GAAP posteriores difieren.

En52 períodos de conciliación (cuatro historias por13años de diagnóstico) se comprueba Δactivo I+D=gasto−amortización. El DCF utiliza diez años; los tres adicionales sirven para observar la aproximación a estabilidad. La prueba alternativa con calendario DCF de13años vale384,50; no es la Base oficial381,79 y su diferencia aproximada0,71% es un contraste metodológico. No se añadió un descuento adicional por esa diferencia. La capitalización no crea caja: la inversión se paga y su costo se refleja en amortización y reinversión.
## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

El modelo fabless transfiere parte importante de la inversión fabril a proveedores, pero no elimina la necesidad de I+D, inventarios, anticipos, financiación y compromisos de capacidad. El capital invertido ajustado inicial es 154.689 millones, que incluye 37.371 de activo de I+D. Ventas/capital actual es 1,96 veces; la Base usa 2 veces en años 1–5. En años 6–10 disminuye hasta 0,5977 veces para sustentar el retorno marginal estable con la convención de capital de apertura de la plantilla.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| S/C inicial; ROIC marginal estable | LTM S/C 1,96; serie ROIC homogénea 3/5/10 N/D | 2,00 años 1–5; 27,22697% terminal; Input / Escenarios | Damodaran US semiconductores ajustado I+D/leases, 5-ene-2026 | Modelo fabless y reutilización de software; proveedores amplían capacidad | Anticipos, inventarios y nube elevan capital; retornos por nueva inversión disminuyen | S/C −20%: USD 375,82; industria global: USD 366,10 |

La reinversión explícita es Δventas/Sales-to-Capital, sin sumar nuevamente todo el CAPEX. Ante caídas de ventas no se reconoce una liberación automática de capital. El ROIC medio explícito sobre capital acumulado y el retorno marginal terminal son métricas distintas: el 27,23% terminal no implica que el retorno medio del año 10 se reduzca instantáneamente a esa cifra. No se usa una recompra para crear valor por acción sin su correspondiente desembolso.


El cociente tardío0,597701 se deriva de ROIC/[margen económico×(1−tax)×(1+g)], con la convención de capital de apertura. No representa el Sales-to-Capital observado de la industria. La reinversión total Δventas/S2C ya incorpora inversión neta en I+D: el puente resta esta última para identificar el otro capital; no vuelve a sumarla. Ante contracción puede aparecer depreciación neta o reducción del otro capital, un límite económico a vigilar. El tratamiento no usa un CAPEX ficticio para cuadrar caja.

El ROIC actual ajustado y normalizado a17% es112,81% sobre cierre,149,36% sobre promedio y220,96% sobre apertura; esos denominadores cambian la interpretación. El marginal estable27,23% no constituye una caída instantánea del retorno medio del stock. La falta de cohortes homogéneas para cada ejercicio antiguo limita la serie3/5/10años: se conserva N/D y no se rellena con el retorno actual.
## 8. Costo del capital y riesgo

La tasa inicial utiliza riesgo de negocio por industria y financiación medida a mercado. Una beta de regresión mucho mayor existe como contraste, sin seleccionarla retrospectivamente para obtener el precio deseado. La exposición país por sede del cliente es una aproximación limitada; no se añade después una prima genérica por todos los riesgos que ya afectan los flujos.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| WACC / Ke iniciales y convergencia | Tasas históricas se usan en ancla A; no hay media de beta empresarial certificada | 11,4423% / 11,4931%; terminal 8,98748%; Detailed | Damodaran 1-oct / enero 2026; beta alternativa OLS 1,860385 | Riesgo desciende con escala y madurez; deuda pequeña a mercado | Concentración y ciclo mantienen beta elevada; geografía de sede es proxy | Beta regresión: USD 352,55; WACC inicial y estable +1 pp: USD 314,82 |

[MODELO] Rf 5,29%; ERP madura 3,697480421%; CRP incremental ponderada 0,403090517%; beta desapalancada corregida por caja 1,5046492755 y apalancada 1,5127415454. Ke 11,493104%; WACC inicial 11,442323%. Fuente Rf/ERP: celdas B10/C45 de ERPOct26, corte 1-oct-2026; industria y primas país: archivos enero 2026. No son cortes idénticos, y la diferencia queda explícita.

El submétodo Detailed enlaza `Cost of capital worksheet!B14`, `E63` e `Input sheet!B36`. Pesos de equity y deuda son valores de mercado; bonos 31.400 millones y leases 5.494. El Kd de 5,89% es Rf más 60 pb por juicio, no una rentabilidad de bono observada. Los campos heredados de rating AA y vencimiento once años no determinan el resultado activo. Los factores de descuento son productos de tasas anuales, no una tasa media aplicada a todos los años.

## 9. Convergencia y valor terminal

Una ventaja durable puede justificar retornos superiores al costo de capital, pero exige que el ecosistema siga aportando rendimiento y costos de cambio después de diez años. La persistencia no queda probada por la cuota actual. La Base usa el ROIC ajustado de industria estadounidense y el escenario de erosión lo reduce; disrupción elimina el exceso de retorno.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| g, ROIC y margen estable | Ingresos/margen históricos §4; no se observa un estado estable de NVIDIA | g 4%; ROIC 27,23%; margen ajustado 58,69%; Input!B47 y Valuation output | Industria US 27,23%; global 20,54%; enero 2026 | Costos de cambio y sistemas completos mantienen ventaja y reinversión productiva | Commoditización o sustitución destruyen exceso de retorno | Sin moat: USD 286,10; global ROIC: USD 366,10 |

El g de 4% nominal USD es inferior al Rf 5,29% y al WACC estable 8,98748%. La reinversión terminal equivale a g/ROIC, aproximadamente 14,69% del NOPAT Base. FY11 incorpora crecimiento, impuesto marginal y reinversión sostenible. El VP terminal representa 67.39% del valor operativo. El denominador WACC−g positivo es necesario, pero no prueba razonabilidad económica.

## 10. Validación independiente del valor intrínseco

Se reprodujeron diez años, impuestos, márgenes, reinversión, tasas anuales, descuento y terminal de las cuatro historias. La diferencia frente a los valores nativos fue inferior a 10⁻⁹ USD por acción en las lecturas de precisión completa. La exportación XLSX conserva cachés redondeadas y puede recalcular de manera diferente en motores ajenos a Google; la hoja nativa y el expediente congelado son la referencia de esta revisión.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Valor por acción hoy / dilución / puente | Básicas actuales y promedio diluido difieren; comparación homogénea §3 | USD 381.790067281; Valuation output!B35; 24.268m acciones | No depende de precio objetivo de analistas | Cada flujo remunera capital después de reinversión; activos fuera de operación se suman una vez | Dilución omitida, activos duplicados, compra deducida dos veces o pasivo clasificado mal | Controles independientes 19/19; +50m acciones: USD 381,01 |

Puente actual, millones: VP operativo 9,165,515.35; más líquidos99.369 y privados51.157; menos compra anunciada11.900 y deuda/leases38.860. Ajuste neto+99.766; equity 9,265,281.35; dividido entre24.268millones de acciones, USD381.79. Los valores cotizados42.783 ya están en99.369 y no se suman otra vez.

Se comprobaron `R& D converter`: gasto actual 23.592, cohortes 15.384/10.569/7.812, amortización 11.255, activo 37.371 y ajuste EBIT 12.337. `Operating lease converter`: deuda ya reconocida 5.494, deuda incremental cero y ajuste de EBIT 323,60. `Option value`: no se creó un Black–Scholes ficticio para RSU. Se agregaron 168 millones de RSU/PSU a 24.100 millones de acciones básicas de portada, mientras el promedio diluido LTM 24.397,5 se conserva como métrica diferente.

[NO VERIFICADO] No se contó con un registro completo de cada concesión y eventual instrumento residual para certificar ausencia absoluta de opciones. La cifra de portada está redondeada; se probó un límite de +50 millones de acciones y +10% de las RSU conocidas. Esas pruebas acotan los efectos especificados, no cualquier concesión desconocida de tamaño arbitrario. Bancos/FCFE y holdings/SOTP no aplican al método principal de esta compañía operativa.

## 11. Cuatro historias y probabilidades
| Historia | CAGR1–5 | GAAP estable / económico objetivo | S/C1–5 | ROIC estable | g | USD/acción | Probabilidad | Mecanismo |
|---|---|---|---|---|---|---|---|---|
| Base | 36.28% | 58.00% / 58.69% | 2.00 | 27.23% | 4.00% | 381.79 | 40.00% | Plataforma de IA mantiene liderazgo; crecimiento se modera con escala |
| Conservadora | 19.69% | 48.00% / 48.69% | 1.65 | 18.11% | 4.00% | 149.58 | 22.50% | Capex cliente se modera y ASIC reducen rentas; erosión parcial |
| Disrupción | -0.22% | 25.00% / 25.41% | 1.30 | 8.99% | 2.00% | 37.05 | 15.00% | Sobreinversión, sustitución y financiación de clientes destruyen rentas |
| Optimista | 47.20% | 62.00% / 62.69% | 2.40 | 27.23% | 4.00% | 639.44 | 22.50% | Inferencia y sistemasintegrados amplían cuota y mercado durante más años |

Las probabilidades conservan la previa de alto crecimiento rentable:40/22,5/22,5/15 para Base/Conservadora/Optimista/Disrupción, sin ajustes ad hoc. El promedio ordinario normaliza las tres historias sobre85%: USD388.52. No reemplaza al DCF Base ni al MOS. El precio MOS35% sobre Base es USD248.16.

### ¿Qué pasaría si todo fallara?

La Disrupción combina sustitución, contracción tras exceso de capacidad y deterioro de financiación de clientes. Su CAGR1–5 es−0,22%, referencia GAAP estable25%, g2% y ROIC igual al WACC estable: USD37.05. La probabilidad15% es un juicio de la regla, no una frecuencia estadística. No entra en el promedio ordinario ni garantiza un suelo.
## 12. Valoración por múltiplos: prueba independiente y secundaria

Se calcularon EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF, P/V y P/BV para tres historias y horizontes FY+1/+2/+3: 63 precios presentes. Se preservó la cadena original Financials Multiples → proyección → puente → dividendos → descuento. Los cinco métodos originales mantuvieron sus fórmulas; PV y PBV siguen la misma arquitectura. Peso cero no equivale a cálculo omitido.

| Método | Salida C / Base / O × | Base FY+3 con dividendos | VP Base FY+3 | Peso interno |
|---|---|---|---|---|
| EV/EBITDA | 11.26 / 16.22 / 18.86 | 411.04 | 296.84 | 15.00% |
| EV/FCFF | 15.00 / 22.44 / 26.72 | 411.04 | 296.84 | 30.00% |
| P/E | 13.97 / 20.12 / 23.40 | 408.49 | 295.00 | 25.00% |
| P/FCFE | 14.47 / 21.07 / 24.67 | 382.56 | 276.29 | 20.00% |
| P/OCF | 14.24 / 21.38 / 25.49 | 408.49 | 295.00 | 10.00% |
| P/V | 6.30 / 9.87 / 10.59 | 408.49 | 295.00 | 0.00% |
| P/BV | 4.11 / 7.43 / 9.63 | 408.49 | 295.00 | 0.00% |

La ancla A usa historia propia con ajuste por tasas (k histórico−g)/(k actual−g), acotado entre 0,6 y 1,4, y filtros explícitos de etapa y valores extremos. La B usa AMD, Broadcom, Qualcomm, Arm y Marvell con fechas y modelos distintos; TSM se excluyó por falta de estados actuales compatibles. No se toma una mediana de esos modelos como múltiplo automático de NVIDIA. La C es un techo justificado en dos etapas: flujos FY+4/+5 y fase estable, evitando tratar FY+3 como compañía madura mientras aún crece rápidamente. Las anclas y filtros completos están en multiples-inputs.json.

P/E y demás ratios de equity usan utilidades normalizadas sin perpetuar ganancias de inversiones; P/OCF no equivale a FCF. Los múltiplos de EV restan deuda y añaden activos financieros en su puente. PBV concilia patrimonio mediante beneficio menos dividendos más crédito patrimonial SBC, sin inventar nuevas recompras; esta es una simplificación de proyección y no una previsión de cada movimiento OCI. Dividendo supuesto USD 1 anual por acción; descuento a Ke 11,4931%.

**Reserva metodológica:** varios métodos dan el mismo valor FY+3 porque el techo fundamental expresa flujos equivalentes. No son siete opiniones independientes ni una confirmación externa del DCF. La C comparte márgenes, tasas y retornos; la aproximación ROE terminal≈ROIC es secundaria dada la baja deuda. Los pesos internos son 15/30/25/20/10/0/0; el bloque combinado usa 75% DCF y 25% múltiplos, pero el valor principal sigue siendo exclusivamente el DCF Base.

## 13. Sensibilidades económicas y escenarios alternativos
Se ejecutaron ocho matrices DCF Base de5×5: WACC estable×g; ROIC estable×g; crecimiento×margen económico; ROIC×WACC estable; ventas/capital×margen económico; WACC inicial×crecimiento; impuesto marginal×crecimiento; WACC estable×escala mecánica del TV. Los200precios coinciden con reproducción separada, con error máximo2,28×10⁻¹³, y los ocho centros reproducen USD381.79. Los ejes de margen usan margen económico ajustado, no58% GAAP. Variar g recalcula convergencia y reinversión; escalar TV es solo diagnóstico mecánico.

| Prueba sobre Base | USD/acción | Cambio frente a Base |
|---|---|---|
| growth_minus5pp | 301.70 | -20.98% |
| growth_plus5pp | 481.98 | 26.24% |
| margin_minus5pp | 350.13 | -8.29% |
| s2c_minus20pct | 375.82 | -1.56% |
| wacc_plus1pp | 314.82 | -17.54% |
| ROIC estable igual a WACC | 286.10 | -25.06% |

El DCF inverso reproduce el precio fechado de210,96 con delta común−12,544765puntos en los cinco crecimientos iniciales. Recalcula los años6–10 y la reinversión. El CAGR implícito es23,6057% frente a36,28% Base; error de reconstrucción inferior a3×10⁻¹⁴. En[−25,+75]puntos, con malla0,1y bisección, se encuentra una raíz; no se afirma unicidad fuera del intervalo. Las cuatro combinaciones de margen/beta dan CAGR implícitos entre24,63% y26,25% para margen55%, y23,61%–25,22% para58%.

Aunque son opcionales por§8 de las reglas vigentes, R2 completa28matrices relativas: siete métodos, anclas JMR y múltiplo observado normalizado de NVDA, y familias Tradicional y Económica. Todas son Base, de5×5precios presentes en USD/acción. Tradicional cruza múltiplo real y fundamental FY+3; Económica cruza múltiplo y delta de crecimiento inicial que recalcula Financials Multiples. El centro JMR replica el VP FY+3 de cada método; el observado replica su propia ancla y no debe coincidir con el DCF. Hay28centros conciliados,700celdas numéricas y cero N/D. La hoja las identifica como captura calculada y muestra una alerta si cambian las entradas; no se atribuye actualización automática al inverso ni a estas tablas congeladas.
## 14. Coherencia de hojas, cálculos y presentación

Valoración, artículo completo de18secciones, nivel2, cuatro historias y auditoría usan NVDA-20261025-R4 y el mismo corte. Pasan19/19controles propios;18/18estados nativos y cero entradas esenciales faltantes. La perturbación nativa Input!B28+1punto produce Base382,226540788 y el centro reproduce ese cambio; al restaurar la fórmula vuelve a381,790067281. El inverso advierte que debe recalcularse tras una modificación.

Se comprobó sustantivamente el artículo: negocio y segmentos, industria, cinco fuerzas, calidad por estado, ventaja, cinco pares, gobierno y capital, catalizadores, ocho riesgos, FODA, seis argumentos por lado, cuatro historias, tasas base, DCF y siete múltiplos, cinco filosofías, noticias, seguimiento, preguntas abiertas y fuentes. La sección 18 del artículo registra ubicación y límites; Nivel 1 contiene el texto completo y Nivel 2 las tablas financieras. La cobertura histórica de ROIC y algunos datos de pares conserva límites explícitos; un título no los resuelve.

No se presupone sincronización automática con la app, ni se certifican todas las pestañas heredadas de la plantilla por revisar las salidas activas. Se conservó el original. Las versiones sustituidas se separan de la carpeta activa; el archivo no se usa como fuente vigente.


El motor web inicialmente recuperaba ΔNWC y nueva deuda con FY como base, pese a proyectar desde LTM. Se corrigió la importación para usar E4/(1+g1), coherente con los ingresos proyectados. Se preservaron las fórmulas de precios. Los63valores presentes concuerdan con la hoja (máxima diferencia5,69×10⁻¹⁴), además de las cuatro historias DCF con sus inputs propios,200sensibilidades e inverso. La regresión conserva NKE y las convenciones anteriores de NFLX. Las19pruebas de CI pasan. Commit desplegado de la app:39185d0831c92c66c709d45f263b5a6ef9211f05; Vercel reporta READY en producción. El comprobante de publicación de datos se conserva después de la escritura, sin atribuir al despliegue del motor la publicación del contenido.
## 15. Hallazgos priorizados y propuestas de corrección
| ID / severidad | Evidencia | Impacto / decisión | Estado |
|---|---|---|---|
| A01 Alto | CAGR36,28%; ingresos año5USD1,424billones | Crecimiento−5pp: USD301.70 | Reserva económica; no cambia probabilidades |
| A02 Alto | ROIC estable27,23% frente a costo8,99% | Sin moat: USD286.10 | Conservar como hipótesis explícita y seguir retornos nuevos |
| A03 Medio | Ancla C comparte márgenes, tasas y retornos | Siete métodos no son siete confirmaciones | Documentado; secundarios |
| A04 Bajo | Redondeo acciones/RSU, activos y tasas | Pruebas acotadas debajo | No bloqueante en límites especificados |
| A05 Medio | Serie ROIC histórica homogénea N/D | Limita comparación3/5/10años | No inventada; cobertura limitada |
| A06 Resuelto R2 | Ajuste histórico I+D perpetuado | Normalización prospectiva y puente de cohortes | Corregido antes de publicar |
| A07 Resuelto R2 | Importación FY/LTM de ΔNWC y deuda | 63precios ahora concilian | App#94,19tests CI aprobados |
| A08 Proceso | Controles centrales sobre captura identificada | Cero sustitución de criterios financieros | Alcance y log adjuntos |

Las siguientes pruebas alteran una exposición a la vez sobre el DCF R2. No son ajustes adoptados ni probabilidades. Se usan límites explícitos y trazables; no se trata un juicio de crecimiento o de moat como una falta documental de baja materialidad.

| ID | Exposición / alternativa | USD/acción alternativo | Impacto absoluto | Decisión |
|---|---|---|---|---|
| L01 | other_country_crp_0_3pct | 380.75 | 0.27% | No cruza precio/MOS en límite probado |
| L02 | debt_market_vs_book | 381.87 | 0.02% | No cruza precio/MOS en límite probado |
| L03 | private_equity_zero | 379.68 | 0.55% | No cruza precio/MOS en límite probado |
| L04 | guarantees_full_gross_no_discount | 377.32 | 1.17% | No cruza precio/MOS en límite probado |
| L05 | shares_rounding_upper_bound | 381.01 | 0.21% | No cruza precio/MOS en límite probado |
| L06 | known_rsu_increment_plus10pct | 381.53 | 0.07% | No cruza precio/MOS en límite probado |
| L07 | lease_EBIT_adjustment_zero | 381.07 | 0.19% | No cruza precio/MOS en límite probado |
| L08 | kd_plus_1pp | 381.67 | 0.03% | No cruza precio/MOS en límite probado |

La suma conservadora de efectos individuales es2.51%, inferior al3%; cada uno es inferior al2%. No es una simulación conjunta exacta ni una garantía sobre instrumentos desconocidos. Las garantías brutas108.500millones se contrastan con deducción total sin descuento; no se clasifican automáticamente como deuda actual, pues el pago depende del contrato y puede solaparse con costos operativos. Compromisos de suministro y nube siguen siendo reservas económicas que deben contrastarse con utilización y cobros. La distinción entre riesgo de historia y datos limitados es material para interpretar el resultado.
## 16. Catalizadores, señales de refutación y seguimiento

| Métrica | Nivel al corte | Favorable (juicio) | Adverso (juicio) | Fuente / frecuencia |
|---|---|---|---|---|
| Ventas | LTM 302.970 millones, 26-jul | Trayectoria consistente con crecimiento Base | Dos reportes por debajo de la trayectoria sin compensación | SEC / trimestral |
| Margen EBIT GAAP | LTM 65,21% | Normalización compatible con objetivo 58% | Compresión persistente por debajo de objetivo | SEC / trimestral |
| Conversión de caja | CFO 134.360; FCF 127.006 LTM | Caja acompaña ventas tras capital de trabajo | Cobros e inventarios crecen más que ventas | SEC / trimestral |
| Capital y compromisos | S/C ajustado 1,96; garantías 108.500 millones | Capital adicional genera retorno y clientes pagan | Activación de garantías o dependencia de financiación | Notas SEC / trimestral y hecho material |
| Poder de plataforma | Cuota exacta homogénea N/D; ecosistema documentado | Adopción de sistemas y software con retorno al cliente | ASIC o alternativas reducen rentas y precio | IR, clientes y SEC / trimestral |
| Dilución | 24.100m básicas portada; 168m RSU conocidas | SBC y recompras se concilian con caja | Emisiones sin retorno compensatorio | SEC y proxy / trimestral |

Los umbrales son criterios propuestos por el auditor para refutar la historia; no son guías oficiales ni reglas para cambiar probabilidades automáticamente. La frecuencia es trimestral salvo hecho material. Próxima fecha exacta de resultados: N/D, no confirmada en este expediente. No se creó un seguimiento automático.

## 17. Dictamen económico y resumen para escuchar
**Tesis: Exigente.** La integración del ecosistema, la generación de caja y la baja deuda financiera son los apoyos más defendibles. La extensión del crecimiento hastaUSD1,424billones de ventas en año5 es el supuesto más frágil. Crecimiento inicial cinco puntos menor daUSD301.70; eliminar exceso de retorno terminal daUSD286.10. Estas pruebas mantienen otros supuestos y no sustituyen una historia adversa coherente.

**Consistencia matemática:** cuatro DCF reproducidos,63precios de siete múltiplos,200sensibilidades DCF,28centros relativos, inverso y puente de cohortes. **Trazabilidad:** fuentes materiales identificadas; se conservan límites de sede geográfica, concesiones, redondeo, pares y serie histórica homogénea de capital. **Razonabilidad económica:** liderazgo duradero es plausible, pero la escala proyectada es exigente; pares y precio no certifican esa expectativa. El registro de controles centrales y la evidencia de publicación detallan qué se verificó directamente y qué quedó limitado por acceso o cobertura.

**Decisión:** adoptar la normalización prospectiva de I+D y el calendario original de diez años, conservar ROIC marginal27,23% y las trayectorias de crecimiento, y publicar valoración, análisis y auditoría separados. El valor oficial esUSD381.79, con MOS35%USD248.16, a precio fechadoUSD210,96. La diferencia favorable de precio es condicional a la historia; no es una meta incondicional ni una certificación externa. La modificación de R1 se hizo en el ciclo R2 antes del cierre de esta auditoría y queda documentada.

### Resumen para escuchar

NVIDIA conserva una posición excepcional en computación acelerada. La revisión normaliza el efecto de investigación y desarrollo para evitar trasladar al futuro un beneficio contable propio del crecimiento actual. La Base vale381dólares con79centavos; el precio con margen de seguridad de35porciento es248dólares con16centavos. La principal reserva sigue siendo económica: se exige crecer aproximadamente36porciento anual durante cinco años y conservar rentas altas. El escenario de disrupción vale37dólares con5centavos. Las cuentas y las sensibilidades se han reproducido; los límites de las fuentes y del acceso se documentan junto a los resultados. Las tres piezas se publican con esta misma revisión.


### Cierre de los controles ejecutados R2

La ejecución de controles_todas.sh NVDA terminó «CONTROLES: sin fallas»: probabilidades sin fallos, supuestos sin hallazgos, integridad sin hallazgos en los rangos capturados, estados completos sin hallazgos, cero entradas esenciales vacías,18/18candados y materialidad «VERIFICADO», con cota agregada2,51091%. La ejecución adicional de consistencia con lectura de hoja dio M1/M2/M3/I1/H1/H2/H3=OK; H1 compara Base381,790067281y promedio388,523012076, y H2 los tres múltiplos y combinados. El transporte usa captura directa del conector del24-oct-2026 a las16:33:52UTC; no es una consulta posterior ni certifica el historial Drive. El texto heredado «última edición por una persona (?)» es indeterminado al no disponer del historial y no prueba una edición humana.

El despliegue de la app está READY en producción con commit39185d0831c92c66c709d45f263b5a6ef9211f05. El intento de lectura del visor por el acceso disponible devolvió401 de autenticación. Esto limita la comprobación visual de la sesión de producción; no se eliminó protección ni se presenta una revisión local como acceso autenticado. El comprobante posterior registra por separado la publicación y lectura del catálogo y de las tres piezas en el repositorio que consume la app.

## 18. Fuentes primarias, limitaciones y registro de versión

- [NVIDIA 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm), presentado 26-ago-2026, semestre y balance al 26-jul-2026: ingresos, resultados, caja, inversiones, deuda, leases, compromisos, acciones y compensación. Consultado 23-oct-2026; copia local y extracción en fuentes.
- [NVIDIA 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm), presentado 25-feb-2026, FY terminado 25-ene-2026: base anual y políticas. Comparativos históricos completados con SEC Companyfacts y 10-K FY2018/FY2019/FY2021; accesiones en provenance.json.
- [SEC 8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000078/nvda-20260902.htm), presentado 3-sep-2026: compra anunciada y contraprestación. No se incorporan sinergias no demostradas.
- [Proxy](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000036/nvda-20260512.htm), 12-may-2026: gobierno e incentivos; no sustituye un inventario actualizado de concesiones.
- [ERP octubre](https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx), corte 1-oct-2026; industria y primas país enero 2026, archivos de Damodaran incluidos en fuentes. Beta de regresión: 104 retornos semanales NVDA/SPY, 1-nov-2024 a 23-oct-2026; precios ajustados por splits, sin dividendos.
- SEC Companyfacts de AMD, Broadcom, Qualcomm, Arm y Marvell; accesiones y períodos en peers.json. Cotizaciones Yahoo del 23-oct-2026; no se homogeneizan sin ajuste modelos de licencias, móviles, ASIC y GPU.
- Mauboussin y Callahan, The Base Rate Book, 26-sep-2016; marco de tasas base, no predicción específica de NVIDIA. Damodaran, notas de múltiplos en dos etapas: fundamento de anclas, no validación del valor resultante.

`prompt_version: auditoria-economica-jmr-v1.2`; reglas prevalentes: REGLAS_VIGENTES v9,24-oct-2026; auditoría NVDA-AUD-20261024-R2. El código central usado se fija al commit596276eb337c45edf84cf53d29a7ceec848fb40e; la captura nativa está fechada y conserva origen, ID y rangos. El historial de revisiones de Drive no se capturó y no se certifica. Los commits de publicación de datos y la comprobación posterior se adjuntan en el comprobante de publicación. No se certifican noticias futuras, una fecha de resultados no confirmada ni un registro completo de concesiones. Fuentes, cálculos y manifiesto permiten reproducir el expediente; el manifiesto no acredita una auditoría externa.

