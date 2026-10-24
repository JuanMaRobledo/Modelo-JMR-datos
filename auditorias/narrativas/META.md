> **Adenda de sensibilidades DCF · 23-oct-2026, misma revisión META-20261023-r4.** El anexo vigente `Sensibilidad DCF` contiene **8 matrices de 5×5 y 200 precios por acción**, sin interpolación de múltiplos. Se comprobó que los **8 centros son US$726,6456435543839**, idénticos a `Valuation output!B35` de la hoja R4. El valor terminal descontado representa **76,89% del valor presente operativo** (no del patrimonio por acción); el ROIC terminal incremental **17,93%** y WACC terminal **8,99%** son hipótesis económicas materiales, no observaciones SEC. El estrés TV 80–120% no cambia la tasa de g. Las sensibilidades de siete múltiplos se exponen solo para Base y los cálculos de Conservador/Optimista permanecen en la hoja. Esta conciliación numérica no significa certificación externa ni elimina las salvedades previas.

## Dictamen vigente de cierre — 23 de octubre de 2026

**Resultado: DEFINITIVA CON SALVEDADES PARA USO PERSONAL.** El modelo JMR R4 se cierra sin cambios en el flujo ni en los supuestos: DCF FCFF Base **US$726,65** por acción, promedio condicionado de tres historias **US$746,63**, MOS 35% **US$472,32**. El corte del precio US$648,85 es del 22-oct-2026. La estimación del capital nuevo terminal **ROIC 17,93%** y la reinversión IA constituyen las hipótesis económicas materiales; su riesgo permanece en sensibilidades (ROIC terminal=WACC ≈US$503,08). Nuevo México, inversiones privadas y leasing tienen salvedades cuantificadas; los múltiplos secundarios quedan ilustrativos con **peso cero en la valoración principal**.

**Evidencia técnica realmente aprobada:** [GitHub Actions](https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/40022435462), controles de estructura DCF/fuentes, fórmula maestra estricta con envolturas protectoras y contrato de las tres matrices. En el repositorio de la app están publicados valoración, 18 secciones de análisis con Nivel 2 y esta auditoría con la misma revisión financiera `META-20261023-r4`; el [PR de publicación #132](https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/132) está integrado. El script legado `controles_todas.sh META` **NO** aprobó: faltaba `reference/damodaran/META.json` y la dependencia `yfinance`, además de referencias de publicación ausentes cuando se ejecutó, antes de la integración. Este fallo se registra como deuda técnica y **no** se declara superado ni se convierte automáticamente en error del DCF.

**Alcance de “definitiva”:** la estimación actual JMR utilizable, reproducible y trazable. No es certeza del valor de mercado, validación del rendimiento futuro de IA, auditoría legal ni certificación independiente. Reabrir cuando cambien materialmente los datos SEC, el costo de capital, el ROIC/capex o la exposición legal. Esta sección es el dictamen vigente y reemplaza cualquier rótulo histórico «pendiente de publicar» conservado en las etapas de preparación anteriores.

**Nota de publicación R4-A2 (23-oct-2026):** revisión financiera única `META-20261023-r4`, análisis de 18 secciones y auditoría económica publicados conjuntamente con reservas. La validación real de DCF, fórmulas y contrato de matrices pasó. El antiguo `controles_todas.sh META` detectó ausencia de registros en el sistema —no alteró el DCF— y exige regeneración/integración posterior. No se presenta el modelo como certificación contable o económica independiente.

> **Actualización posterior R4-A2 (23-oct-2026):** este expediente conserva los resultados numéricos R4. Después de distinguir materialidad y tipo de evidencia, el dictamen vigente es **VALORABLE PARA USO INTERNO CON SALVEDADES; NO CERTIFICADA; PUBLICADA CON SALVEDADES**. Los faltantes de detalle de Nuevo México, valor justo de inversiones, lease financiero y comparables no bloquean el uso interno del DCF, pero deben permanecer cuantificados y expresamente identificados. La publicación autorizada distingue los controles numéricos ya aprobados y los controles de integración legados pendientes, conservados en la auditoría. Véase [hoja, pestaña «R4 · Remediación riesgos»](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit#gid=26102306) y [PR #140](https://github.com/JuanMaRobledo/JMR-valuation/pull/140).

# Auditoría económica narrativa — Meta Platforms, Inc. (META)

## 1. Ficha de auditoría y alcance

[OBSERVADO] Se examina Meta Platforms, Inc. (META), clase A, NASDAQ, moneda USD, estados en millones, método principal DCF FCFF. Fecha de valoración y auditoría: 23 de octubre de 2026. Corte financiero: LTM al 30 de septiembre. Precio del análisis: cierre del 22 de octubre, US$648,85; no se obtuvo un nuevo precio de hoy.

[MODELO] Revisión **META-20261023-r4**, misma hoja, resultados JSON y artículo de esta entrega. El alcance comprende los cinco supuestos solicitados y sus dependencias, el contraste de partidas materiales y la coherencia editorial. La revisión la realiza el mismo agente en una fase posterior; no constituye una auditoría contable ni una revisión independiente por otra persona. **Estado: CON HALLAZGOS. Auditoría condicionada.** [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

La fase de valoración terminó antes de este examen. Durante la auditoría no se modifican la hoja, los supuestos, el JSON ni el análisis. Las correcciones ya realizadas se identifican como anteriores al dictamen.

## 2. Resumen ejecutivo y relato económico central

[OBSERVADO] Meta monetiza atención y resultados para anunciantes a través de sus aplicaciones. Family of Apps aporta la gran mayoría de ingresos y financia infraestructura y apuestas de distinto perfil económico. Reality Labs sigue consumiendo recursos; el uso de IA no equivale automáticamente a ingresos o rentabilidad segregados. [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

[INFERENCIA] La lectura favorable sostiene que distribución y mejores herramientas comerciales rentabilizarán la nueva capacidad. La neutral admite crecimiento con mayor capital necesario y menor caja disponible. La adversa contempla pérdida de descubrimiento, restricciones de datos o costos que crecen más que la monetización.

[MODELO] Base empieza con crecimiento de 22%, desacelera y mantiene margen ajustado estable de 43%. El ROIC marginal terminal de 17,93% presupone una ventaja publicitaria durable después del año diez. El modelo no demuestra que cada proyecto de IA merezca ese retorno.

[NO VERIFICADO] El supuesto de duración y productividad del capital nuevo domina la incertidumbre económica. La contradicción que debe resolver la empresa es si la capacidad contratada genera suficiente efectivo después de reposición, remuneración y obligaciones. La historia no se deduce del resultado del DCF.

## 3. Trazabilidad, integridad y jerarquía de evidencia

| Dato | Valor | Período / perímetro | Tipo | Fuente / ubicación | Verificación |
|---|---|---|---|---|---|
| Ingresos | 241.605,00 | LTM sep-2026 | Derivado | 10-Q; Input B12 | 200.966 +181.712 −141.073 |
| EBIT | 79.380,00 | GAAP LTM | Derivado | 10-Q; Input B13 | 83.276 +54.635 −58.531 |
| Caja y negociables | 82.449,00 | Saldo al 30-sep | Observado | 10-Q; Input B19 | Sin añadir efectivo restringido |
| CAPEX físico | 104.438,00 | LTM | Derivado | Cash Flow L15 | Distinto de reinversión total |
| I+D | 76.544,00 | LTM | Derivado | R&D converter F8 | Ajuste analítico activo |
| Acciones | 2.556,24 M | 16-oct-2026 | Observado | Portada 10-Q; Input B22 | Clases A+B, no promedio EPS |
| Impuesto | 4,58% histórico;17% a 25,37% proyectado | LTM / futuro | Mixto | Input B24/B93/B25 | No perpetúa el efectivo bajo |
| Deuda económica | 116.026,00 | Incluye leases | Modelo | Input B16; notas | Proxy financiero pendiente |
| ROIC sectorial | 17,93% | Global, I+D y leases ajustados | Referencia | Damodaran 05-ene; Global E3 | Archivo original contrastado |
| Precio | 648,85 | Cierre 22-oct | Expediente | Input B23 | Conservado; no refrescado |
| Rf / ERP madura | 5,29% /3,70% | Corte mensual | Expediente | Cost of capital | No readquiridas íntegramente |
| Pares homogéneos | N/D | Igual fecha y definición | No verificado | Sector vacío | No se inventan |

[Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm) [Meta 10-K, 29-ene-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm) [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

## 4. Historia financiera: diez años y punto de partida

[OBSERVADO] Los estados contienen 2016–2025 y LTM. Se verificó igualdad exacta antes y después en Income Statement A1: L36, Balance Sheet A1: L40 y Cash Flow Statement A1: L40. Conservar esos rangos no recertifica cada renglón de diez ejercicios.

Ingresos pasan de 27.638 en 2016 a 200.966 en 2025. Su CAGR usa nueve intervalos. Los CAGR de tres y cinco años son 19,89% y 18,51%. El margen GAAP anual oscila entre24,82% y 49,70%; el LTM baja a 32,86%. CAPEX/ventas aumenta de15,85% en2021 a 34,68% en2025 y 43,23% LTM. El artículo presenta la tabla anual y las medias de3/5/10años de márgenes, CAPEX, I+D, SBC y conversión.

[NO VERIFICADO] No se reconstruyó una serie homogénea de ROIC ajustado por I+D, leases e impuestos normalizados para diez años. No se mezclan saldos finales con saldos promedio ni se fabrican medias. Las anomalías fiscales y legales se separan de la operación. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit) [Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

## 5. Crecimiento de ingresos: de la historia a la proyección

[HIPÓTESIS] Mejorar la utilidad de los anuncios sostiene expansión sobre una distribución instalada. La senda desacelera y no perpetúa el26% trimestral. No existe una proyección por producto que concilie independientemente el total. [Meta resultados, 21-oct-2026](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/)

| Métrica y horizonte | Histórico:3/5/10 años, LTM | Modelo: valor/año/celda | Industria o pares | Historia causal y requisitos | Evidencia contraria / juicio | Prueba o impacto |
|---|---|---|---|---|---|---|
| Ingresos1–5 | CAGR3años19,89%;5años18,51%; LTM241.605 | 22/20/17/14/11%; Historias C29: G29 | Tasas base por tamaño, Exhibit4 | Más respuesta útil y monetización | Gran tamaño; guía2027 no cuantificada | Matriz crecimiento/margen e inverso |
| Pregunta | Respuesta |
|---|---|
| a. Valor, unidad, año y celda | CAGR16,73%; año1 Input B27=22% |
| b. Contraste histórico | CAGR y medias son medidas diferentes; diez cierres2016–25 son nueve intervalos |
| c. Mecanismo causal | Mejores campañas atraen presupuesto |
| d. Hechos necesarios | Precio, impresiones, conversión y capital coherentes |
| e. Falsadores | Menor eficacia y necesidad creciente de inversión |
| f. Impacto o prueba | Delta−1pp, margen43%: US$698,67; +1pp: US$756,00, copiados de matriz R4 |


## 6. Márgenes operativos y normalización de beneficios

[OBSERVADO] EBIT GAAP LTM79.380 más ajuste neto de I+D32.422,67 produce EBIT ajustado111.802,67. Normalizar el cargo legal Q3 de9.889 es otra operación. El margen48% a 43% del DCF no es margen GAAP. Antes de la auditoría se corrigió el margen auxiliar para que su numerador coincidiera con el EBIT GAAP presentado. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

| Métrica y horizonte | Histórico:3/5/10 años, LTM | Modelo: valor/año/celda | Industria o pares | Historia causal y requisitos | Evidencia contraria / juicio | Prueba o impacto |
|---|---|---|---|---|---|---|
| Margen EBIT | LTM GAAP32,86%; rango anual24,82–49,70%; medias en artículo | 48% a 43%; Input B28/Historias D5 | Google Services41,83%, perímetro distinto | Escala absorbe parte de D&A y nube | Mayor costo de servir; I+D3años es juicio | Margen40% /46%: US$669,44 /783,85 |
| Pregunta | Respuesta |
|---|---|
| a. Valor, unidad, año y celda | 43% ajustado desde año5;48% año1 |
| b. Contraste histórico | Separación de GAAP, normalización legal y capitalización I+D |
| c. Mecanismo causal | Productividad y normalización compensan parte de infraestructura |
| d. Hechos necesarios | Monetización crece con capacidad utilizable |
| e. Falsadores | Costos aumentan más que ingresos sin mejora del producto |
| f. Impacto o prueba | Sensibilidad recalcula margen y S/C dependiente; no se ejecuta una corrección en auditoría |


## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

[MODELO] Reinversión usa ventas incrementales con adelanto de un año y S/C0,45 a 0,54. No se añaden otra vez CAPEX o I+D. El retorno marginal estable no equivale al ROIC contable medio. El puente físico es residual y no constituye evidencia independiente de un presupuesto por proyecto. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

| Métrica y horizonte | Histórico:3/5/10 años, LTM | Modelo: valor/año/celda | Industria o pares | Historia causal y requisitos | Evidencia contraria / juicio | Prueba o impacto |
|---|---|---|---|---|---|---|
| S/C y ROIC | Marginal0,47; promedio0,61; ROIC actual26,74% con impuesto efectivo | Input B32; Historias F5/G5; ROIC17,93% terminal | Advertising global419, ajustado | Utilización rentable y ventaja durable | No hay retorno segregado por proyecto | ROIC10,76% /25,11%: US$576,83 /790,85 |
| Pregunta | Respuesta |
|---|---|
| a. Valor, unidad, año y celda | S/C0,45/0,54; reinversión año1 US$131.003,60M |
| b. Contraste histórico | La intensidad de CAPEX aumenta; no hay ROIC ajustado homogéneo de diez años |
| c. Mecanismo causal | Se invierte antes de monetizar; maduración mejora eficiencia |
| d. Hechos necesarios | Capital utilizable y reposición sostenible |
| e. Falsadores | Contratos y reposición absorben el incremento de NOPAT |
| f. Impacto o prueba | Diagnóstico sin ventaja: US$503,08; recalcula también la reinversión vinculada |


## 8. Costo del capital y riesgo

[MODELO] WACC inicial10,57% a terminal8,99%; beta sectorial reapalancada1,12; ERP total4,96%; Rf5,29%. Se usan los mismos tipos en todas las historias y no se añadió una prima específica por litigios o competencia. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

| Métrica y horizonte | Histórico:3/5/10 años, LTM | Modelo: valor/año/celda | Industria o pares | Historia causal y requisitos | Evidencia contraria / juicio | Prueba o impacto |
|---|---|---|---|---|---|---|
| WACC | Las medias históricas no sustituyen el corte actual | Input B36/B47 | Corte mensual conservado y beta global | Pesos de mercado y riesgo sistemático | CRP regional aproximada; leases pendientes | WT7,99% /9,99%, g4%: US$889,68 /617,94 |
| Pregunta | Respuesta |
|---|---|
| a. Valor, unidad, año y celda | Rf5,29%; ERP madura3,70%; CRP1,26pp |
| b. Contraste histórico | Corte fechado, no promedio3/5/10años |
| c. Mecanismo causal | Convergencia del riesgo a empresa madura |
| d. Hechos necesarios | Perímetro de deuda, caja y beta consistente |
| e. Falsadores | Descalce de fechas o doble prima por riesgo operativo |
| f. Impacto o prueba | Factores compuestos reproducidos; beta+0,20 es estrés, no regresión |

[NO VERIFICADO] No se readquirieron íntegramente el archivo mensual y el reparto de CRP por país. La limitación no queda cerrada por copiar las celdas.

## 9. Convergencia y valor terminal

[HIPÓTESIS] La franquicia publicitaria mantiene rentas después del año10. Base y Optimista usan industria ajustada; Conservadora admite erosión parcial. g4% nominal USD no supera Rf5,29%; Disrupción conserva g1%. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

| Métrica y horizonte | Histórico:3/5/10 años, LTM | Modelo: valor/año/celda | Industria o pares | Historia causal y requisitos | Evidencia contraria / juicio | Prueba o impacto |
|---|---|---|---|---|---|---|
| Terminal | No hay historia observada de la perpetuidad; sector17,93% | g4%; WT8,99%; ROIC17,93%; impuesto25,37% | Damodaran global05-ene-2026 | Moat y monetización persistentes | Sector mezcla agencias y plataformas; IA no aislada | Terminal76,89% del EV; sin ventaja US$503,08 |
| Pregunta | Respuesta |
|---|---|
| a. Valor, unidad, año y celda | Historias G5/J5; Input B25/B47 |
| b. Contraste histórico | ROIC actual26,74% efectivo;23,26% normalizado;17,93% sectorial |
| c. Mecanismo causal | Excedente estable por distribución defendible |
| d. Hechos necesarios | Ventaja y productividad sobreviven diez años |
| e. Falsadores | Competencia o regulación eliminan el exceso |
| f. Impacto o prueba | Reinversión10 y 11 concilia; matriz ROIC/g cuantifica el efecto |

NOPAT11 US$242.638,07M menos reinversión US$54.119,04M produce FCFF US$188.519,03M.

## 10. Validación independiente del valor intrínseco

[OBSERVADO] La reproducción separada coincide con cuatro historias en menos de0,001US$/acción. Es comprobación numérica y no certificación económica externa. VPNflujos: US$433.827,11M; VPNterminal: US$1.443.772,11M. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

| Concepto | US$ millones |
|---|---|
| VPN FCFF1–10 | 433.827,11 |
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


| Métrica y horizonte | Histórico:3/5/10 años, LTM | Modelo: valor/año/celda | Industria o pares | Historia causal y requisitos | Evidencia contraria / juicio | Prueba o impacto |
|---|---|---|---|---|---|---|
| DCF Base | R3 US$682,69; informe R1 desfasado US$756,50 | Valuation output B35=726,65 | No se ancla a un objetivo externo | Flujos, descuento y puente coherentes | El cuadre no resuelve reclamaciones o valor realizable | Error numérico<0,001; dictamen condicionado |
| Pregunta | Respuesta |
|---|---|
| a. Valor, unidad, año y celda | DCF Base US$726,65; acciones2.556,24M |
| b. Contraste histórico | Versiones anteriores se identifican y no mezclan |
| c. Mecanismo causal | Cambio de ROIC y reinversión, no ajuste para alcanzar precio |
| d. Hechos necesarios | Puente completo sin doble conteo |
| e. Falsadores | Pasivo omitido o activo no realizable |
| f. Impacto o prueba | Inverso13,82%; centros y matrices reproducidos sin factor de calibración |


## 11. Cuatro historias y probabilidades

| Historia | Crecimiento1–5 | Margen ajustado | S/C; ROIC terminal | WACC | g | DCFUS$ | Probabilidad | Confirmación o refutación |
|---|---|---|---|---|---|---|---|---|
| Base | 22,00%; 20,00%; 17,00%; 14,00%; 11,00% | 43,00% | 0,45; 17,93% | 10,57% a 8,99% | 4,00% | 726,65 | 45,00% | Monetización y productividad frente a rigidez y erosión |
| Conservadora | 13,00%; 10,00%; 8,00%; 7,00%; 6,00% | 37,00% | 0,40; 13,46% | 10,57% a 8,99% | 4,00% | 423,18 | 22,50% | Monetización y productividad frente a rigidez y erosión |
| Optimista | 27,00%; 24,00%; 22,00%; 20,00%; 18,00% | 47,00% | 0,65; 17,93% | 10,57% a 8,99% | 4,00% | 1.110,05 | 22,50% | Monetización y productividad frente a rigidez y erosión |
| Disrupción | 8,00%; 0,00%; -5,00%; 0,00%; 1,00% | 23,00% | 0,30; 8,99% | 10,57% a 8,99% | 1,00% | 210,26 | 10,00% | Monetización y productividad frente a rigidez y erosión |

[MODELO] Se conserva la previa de crecimiento maduro sin ajustes. Promedio ordinario US$746,63, denominador0,90. MOS35% solo sobre Base: US$472,32.

### ¿Qué pasaría si todo fallara?

Disrupción conserva10% de probabilidad, US$210,26, g1% y ROIC=WACC8,99%. No libera capital automáticamente cuando cae demanda. Representa deterioro económico, no únicamente quiebra. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

## 12. Valoración por múltiplos: prueba independiente y secundaria

| Método | Múltiplo Base | VP Base US$ | Conservadora | Optimista | Observado | Peso |
|---|---|---|---|---|---|---|
| EV/EBITDA | 11,90× | 726,70 | 9,74× / 466,66 | 14,28× / 994,37 | 15,91× | 35,00% |
| EV/FCFF | 26,23× | 194,33 | 20,18× / 316,72 | 39,16× / 447,36 | N/D | 0,00% |
| P/E | 18,73× | 741,45 | 15,61× / 487,18 | 20,70× / 938,31 | 22,04× | 45,00% |
| P/FCFE | 15,79× | 112,23 | 13,15× / 203,52 | 24,43× / 268,61 | N/D | 0,00% |
| P/OCF | 9,73× | 670,96 | 8,58× / 462,54 | 12,75× / 1.000,01 | 12,46× | 0,00% |
| P/V | 5,13× | 615,01 | 4,52× / 427,05 | 7,34× / 984,53 | 6,86× | 20,00% |
| P/BV | 3,45× | 716,13 | 2,92× / 550,77 | 5,77× / 1.263,27 | 6,09× | 0,00% |

[NO VERIFICADO] Ancla A cita años sin reconstrucción suficiente; ancla B de pares está vacía; ancla C terminal no acredita el techo FY+3. No se validó íntegramente el ajuste por tasas acotado0,6–1,4. Los factores adicionales88/90/85% Base carecen de soporte suficiente y pueden introducir prudencia duplicada.

EV/EBITDA omite la inversión necesaria; P/E depende de normalización fiscal y operativa; P/V exige margen sostenible. Los otros cuatro métodos tienen peso cero por transitoriedad de flujos, SBC o intangibles. El consolidado mecánico US$711,00 no es una prueba independiente del DCF. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

## 13. Sensibilidades económicas y escenarios alternativos


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

#### Delta crecimiento1–5 × margen EBIT ajustado

| Filas / columnas | 40,00% | 41,50% | 43,00% | 44,50% | 46,00% |
|---|---|---|---|---|---|
| -2,00% | 620,60 | 646,30 | 672,00 | 697,70 | 723,39 |
| -1,00% | 644,44 | 671,55 | 698,67 | 725,78 | 752,90 |
| 0,00% | 669,44 | 698,04 | 726,65 | 755,25 | 783,85 |
| 1,00% | 695,67 | 725,83 | 756,00 | 786,16 | 816,32 |
| 2,00% | 723,18 | 754,98 | 786,78 | 818,58 | 850,38 |

[OBSERVADO]75celdas contrastadas, centros US$726,65 y error inferior a 0,001US$/acción. El inverso del cierre22-oct usa delta−2,91pp y CAGR13,82%, con error0,00.

[NO VERIFICADO] Las sensibilidades relativas auxiliares dependen de anclas con hallazgos; no se certificaron todas sus familias. Las matrices opcionales del§8 no se convierten en un nuevo requisito del núcleo DCF. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

## 14. Coherencia de hojas, cálculos y presentación

[OBSERVADO] Hoja, JSON y documentos identifican R4, Base726,65, promedio746,63, MOS472,32 e inverso13,82%. La discrepancia del artículo R1 quedó corregida en la fase anterior. La coincidencia no implica actualización automática de la app.

El examen editorial revisó negocio, segmentos, geografía, Porter, tres estados, gobierno, riesgos, filosofías, tesis contraria y explicación de supuestos. Se preservó desarrollo pertinente del artículo completo anterior sin reutilizar su valoración. Hay recuadro inicial, nivel2 y tabla de cobertura con limitaciones. La extensión no se usa como prueba de completitud.

[NO VERIFICADO] No se certifica cobertura resuelta para los pares homogéneos, ROIC histórico ajustado, proyección por producto y contratos por proyecto. Sus faltantes están identificados en el artículo. No se ejecutó controles_todas.sh, render nativo ni verificación en la app. [Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

## 15. Hallazgos priorizados y propuestas de corrección

| ID | Severidad | Tipo | Evidencia | Impacto | Propuesta | Estado |
|---|---|---|---|---|---|---|
| F01 | Alto | Dato/supuesto | Nuevo México25.000M distinto del acuerdo18.590M | Neto N/D; bruto9,78US$/acción antes de descuento/provisión/impuesto | Conciliar provisión, garantías, interés y pagos | Abierto |
| F02 | Alto | Dato/supuesto | Leases financieros1184M como proxy | Afecta capital, WACC y puente | Obtener pasivo y vencimientos actuales sin solapamiento | Abierto |
| F03 | Alto | Supuesto | I+D3años y puente físico residual | Capital y FCFF dependen de vidas/intensidad | Contrastar cohortes y proyectos cuando existan datos | Incertidumbre explícita |
| F04 | Alto | Método | Anclas relativas, factores y techo FY+3 | Ponderado sin independencia demostrada | Reconstruir ciclo, tasas y techo, sin inventar anclas | Abierto |
| F05 | Medio | Dato/supuesto | Privadas32624M a libros | Aporte12,76US$/acción aprox. | Validar valor atribuible y condiciones de realización | Abierto |
| F06 | Medio | Dato | CRP regional y corte de tasas conservados | WACC conserva límite externo | Revalidar fecha y asignación por país | Abierto |
| F07 | Bajo | Presentación | Artículo R1 no correspondía a hoja R3 | Versión incoherente | R4 común en entregables | Cerrado antes de auditoría |
| F08 | Alto | Fórmula | Sensibilidad dejaba fijo S/C al variar ROIC | Interdependencia incompleta | 76bloques corregidos;75resultados contrastados | Cerrado antes de auditoría |

Las correcciones futuras se proponen para una fase de valoración, sin ejecutarlas en esta auditoría. La investigación documental no requiere una autorización nueva; se conserva la instrucción de no publicar. No se confunden hipótesis discutibles con errores de dato confirmados.

## 16. Catalizadores, señales de refutación y seguimiento

| Métrica | Observado/fecha | Favorable | Adversa | Fuente | Frecuencia |
|---|---|---|---|---|---|
| Impresiones/precio | +10/+14% Q3 | Más respuesta útil | Precio cae pese a más inventario | Resultados21-oct | Trimestral |
| CAPEX | Guía135–145mil M2026 | Capacidad utilizable y monetización | Sobreinversión sin retorno | Resultados21-oct | Trimestral |
| S/C marginal | 0,47en hoja | Mejora después de puesta en servicio | Cae persistentemente | Modelo R4 | LTM/anual |
| Margen | 32,86% GAAP LTM | Mejora con puente conciliado | Costo de servir absorbe expansión | 10-Q/modelo | Trimestral |
| SBC/acciones | 26943MLTM;2556,24Macciones | Crece caja por acción | Dilución sin beneficio económico | 10-Q/modelo | Trimestral |
| Litigios | Orden21-oct2026 | Exposición neta conciliada | Colateral o pagos adicionales | 10-Qnota10 | Por evento |

[HIPÓTESIS] Los umbrales del artículo son criterios analíticos salvo guía citada. No se afirma la fecha del siguiente reporte sin comprobarla.

## 17. Dictamen económico y resumen para escuchar

**Dictamen: Plausible con reservas. Auditoría condicionada. Estado global: CON HALLAZGOS.**

La consistencia matemática del DCF, las sensibilidades y el inverso fue comprobada. La trazabilidad cubre partidas materiales y conservación de históricos, sin recertificar toda la serie. Crecimiento y margen tienen una historia defendible; el retorno terminal sigue la regla sectorial, pero presupone ventaja durable. Los relativos y reclamaciones todavía requieren evidencia.

El supuesto más frágil es la productividad del capital nuevo y su persistencia. El punto de partida comercial de publicidad es más defendible. El terminal domina el valor. La decisión analítica es conservar R4 para revisión e investigar los hallazgos abiertos. Durante esta fase **no se modificó la valoración**.

### Resumen para escuchar

Meta mantiene un negocio publicitario rentable y una distribución difícil de replicar. El modelo revisado conserva crecimiento fuerte al principio y después lo desacelera. También reconoce inversión elevada y flujo económico negativo inicial. El cambio principal consiste en ligar el retorno estable a una referencia sectorial y recalcular la reinversión que depende de ese retorno. Los cuatro escenarios y las matrices coinciden con la hoja, pero eso comprueba la matemática, no la rentabilidad futura de todos los proyectos. Siguen abiertas la conciliación de obligaciones legales y arrendamientos y la justificación de algunos múltiplos. El análisis completo identifica esas limitaciones. La revisión queda preparada, con hallazgos y publicada con salvedades; no constituye una recomendación de comprar o vender.

## 18. Fuentes primarias, limitaciones y registro de versión

[Meta 10-Q, 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)

[Meta resultados, 21-oct-2026](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/)

[Meta 10-K, 29-ene-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm)

[Meta Proxy, 16-abr-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026025532/meta-20260416.htm)

[Modelo JMR META R4, 23-oct-2026](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)

[Damodaran ROIC global,05-ene-2026](https://www.stern.nyu.edu/~adamodar/pc/datasets/rocGlobal.xls)

Todos fueron consultados el23-oct-2026. Los límites de cada fuente se identifican en el artículo. Para el contraste de plataforma madura y tasas base se consultaron además los documentos de Alphabet Q2 y Mauboussin2016/2026 allí enlazados. El precio se conserva del expediente y no se presenta como cierre recién consultado.

**Registro:**auditoría META-R4; prompt_version: auditoria-economica-jmr-v1.2 con actualización editorial23-oct; hoja R4, JSONMETA_resultados_R4 yartículo de esta entrega. No hay commit de publicación ni escritura en Modelo-JMR-datos.

**Control de entrega:**18H2 exactos; seis preguntas y tabla por supuesto en5–10; datos, crecimiento, margen, capital, tasas, terminal, DCF, siete relativos, sensibilidad e inverso; cuatro historias, promedio ordinario, Disrupción aparte y MOS sobre Base; hallazgos, señales, dictamen y resumen oral. Las anclas y familias relativas no verificadas permanecen identificadas. No se ejecutó auditoría por otra persona, controles integrales del repositorio, render nativo ni comprobación en app. **Auditoría condicionada, publicada con salvedades y controles técnicos documentados.**


---

## Adenda de auditoría independiente de fórmulas vs evidencia económica — R4-A1 (23-oct-2026)

**Dictamen complementario: CON HALLAZGOS MATERIALES, gate económico BLOQUEADO.** Los escenarios R4 matemáticamente consistentes (Base US$726,65) no deben describirse como pasivos y activos certificados. La adenda no modifica celdas del DCF, por lo que los controles numéricos R4 siguen referidos a la misma base.

| Control | Revisión desde fuente primaria | Estado al cierre |
|---|---|---|
| F01 Nuevo México | Orden 21-oct US$25.000M + 15% post-judgment; Meta registró provisión no cuantificada individualmente | ABIERTO (incremental no identificable) |
| F01 Acuerdo 52 estados | Tope US$18.590M; US$12.700M cuotas 10 años y US$5.300M condicionales no provisionados | DOCUMENTADO; PV/caja de la ficha antigua por revisar |
| F01 Provisión legal consolidada | US$11.577M corrientes + US$8.304M no corrientes = US$19.881M; incluye muchos asuntos, no identificable por juicio | DATO CORREGIDO; imputación sigue ABIERTO |
| F02 Leases reconocidos | Pasivos operativos US$31.173M; ROU financieros US$11.704M no son pasivo; proxy deuda 1.184M FY2025 | ABIERTO pasivo financiero 2026 y solapamientos |
| F02 Contratos futuros | US$355.730M por leases sin comenzar y US$454.520M de compromisos no cancelables; US$14.720M de nube contingente | DOCUMENTADO, flujo marginal por contrastar |
| F05 Participaciones | US$32.624M a libros, US$4.732M en JV de data centers | ABIERTO fair value y solapamiento |
| F06 Rf/ERP | 5,29%/3,70% corresponden al 30-sep Damodaran, no al 22-oct | CORREGIDO EL ETIQUETADO DE FECHA; WACC nuevo no ejecutado |
| F04 múltiplos | Sin serie completada en «Múltiplos históricos»; 88/90/85% discrecionales sin prueba | ABIERTO, valor ponderado no independiente |
| Caja restringida | Escrow US$10.800M excluido de cash+marketable 82.449M | CERRADO sin doble deducción |

**Nueva evidencia cuantitativa inspeccionada en vivo:** la hoja [R4 · Remediación riesgos](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit) incluye sensibilidades enlazadas al mismo DCF US$726,64564 y 2.556,241253M acciones: NM incremental 0/5/12,5/25bn → US$726,65/724,69/721,76/716,87; inversiones privadas a 0/50/100/150% de libros → US$713,88/720,26/726,65/733,03; CAPEX extra en el año 1 de 0/10/50/100bn (WACC inicial 10,57%) → US$726,65/723,11/708,96/691,27. **Cada choque solo es pertinente si NO está incluido en la valoración corriente.** No aplicar choques uno detrás de otro sin puente completo.

**Riesgo de falsa validación formal:** 'Input sheet'!B85 = «VALIDADO» se deriva de 'Input sheet'!B86 = «Sin solapamiento», que es una **afirmación a verificar**, no una prueba empírica de realizabilidad. Cambiarla directamente invalidaría K5–K8 y ocultaría los resultados DCF oficiales por fórmula. Por ello se mantuvo la hoja de resultados intacta y se registró **bloqueo económico separado**; no se considerará un gate aprobado hasta conciliar el supuesto y ejecutar las pruebas del repositorio en un entorno autenticado.

El manifiesto 'reference/fuentes/META_manifest.json' ya está creado en [PR #140, borrador](https://github.com/JuanMaRobledo/JMR-valuation/pull/140) y documenta las fuentes. Es condición formal necesaria, **no suficiente**. Faltan extracción/verificación de pasivo financiero lease 2026, conciliación provisión NM vs multistate, valoración realizable de JV, flujos netos comprometidos, reconstrucción de anclas y prueba real 'desde_cero.sh validar META' + 'audit_master_formulas.py --gates --strict' + 'audit_report_contract.py' + render app.

**Cierre R4-A1:** corroborado matemáticamente y reconciliado documentalmente donde fue posible; **no publicado** y no certificable sin datos que el emisor no individualiza públicamente. Fuente: [Form 10-Q META 30-sep](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm); [Damodaran 8-oct](https://aswathdamodaran.substack.com/p/earnings-cashflows-and-stock-prices).


## Adenda final R4-A2 — cierre proporcional de los supuestos necesarios (23-oct-2026)

**Mismo modelo financiero:** `META-20261023-r4`. No se ha creado otra revisión de supuestos ni se recalibró la cifra DCF. El paquete R4-A2 es una **actualización del dictamen y las evidencias**, no un nuevo modelo de valoración.

Los elementos imprescindibles tienen hipótesis explícitas y pruebas: crecimiento Base anual 22%, 20%, 17%, 14% y 11%; margen EBIT *ajustado por capitalización de I+D* 48% a 43%, que no debe confundirse con el margen GAAP; Sales-to-Capital 0,45 y 0,53735 (marginal; reinversión adelantada); ROIC terminal 17,93%; tasa fiscal 17% convergente a 25,37%; WACC 10,57% inicial y 8,99% terminal; `g` perpetua de 4,00%. El año uno ya invierte US$131.003,60M, por lo que no procede añadir íntegramente a deuda los compromisos contractuales anunciados. El valor terminal aporta 76,89% del EV: la continuidad del moat es la fuente principal de sensibilidad.

Se usa US$726,65/acción como **valor intrínseco Base del modelo**, con tesis y sensibilidad contrapuesta: si el ROIC marginal de la perpetuidad convergiera al WACC, la prueba del expediente da unos US$503,08/acción (−30,77%). Eso es un caso alternativo, no el valor Base. El inverso muestra CAGR implícito de 13,82% para años 1–5 a precio congelado de US$648,85 del 22-oct.

Los faltantes secundarios se **aceptan como juicios con trazabilidad** sin inventar datos: el castigo judicial Nuevo México US$25.000M, *si fuera íntegramente adicional*, implicaría US$−9,78/acción (−1,35%), **sin** incluir interés judicial 15% ni consecuencias operativas; realizar a cero US$32.624M de inversiones privadas impactaría US$−12,76/acción (−1,76%); retirar solo el proxy leasing financiero de US$1.184M movería cerca de +0,06%, lo que **no acota** obligaciones no reveladas; una erogación extraordinaria de CAPEX no ya modelada por US$100.000M en el primer año alteraría el precio en −4,87%, pero múltiples años repetidos afectarían mucho más. **Estas sensibilidades no son sumables automáticamente**.

La provisión reconocida por el litigio de Nuevo México **no está individualizada** en el 10-Q; la provisión legal agregada es US$19.881M. El modelo deduce aparte el máximo del acuerdo multistate US$18.590M como hipótesis conservadora y no incorpora toda la multa Nuevo México como otro pasivo cierto. Las inversiones privadas US$32.624M son un proxy a valor contable y los múltiplos relativos siguen *ilustrativos/no verificados*. Nunca convertir «VALIDADO» de una celda formal en certificación económica.

**Conclusión para valoración y auditoría:** **APTO PARA VALORACIÓN PERSONAL CON SALVEDADES**. **Publicación/app:** valoración, análisis de dos niveles y auditoría narrativa están publicados y enlazados a la hoja/JSON R4; pruebas DCF, fórmulas y contrato de reporte autenticadas aprobadas. El control legado integral no pasó por faltantes de integración y dependencias; no se declara conforme.

Fuentes: [Meta 10-Q 22-oct-2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm), [Damodaran 8-oct-2026](https://aswathdamodaran.substack.com/p/earnings-cashflows-and-stock-prices), [hoja Google R4](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit), [PR META R4-A2](https://github.com/JuanMaRobledo/JMR-valuation/pull/140).