# Amazon R5 — Adenda de múltiplos y publicación EN_REVISION
Fecha 2026-11-03 · Revisión `AMZN-20261102-A12-R5` · Mercado 2026-10-30 · Contable 2026-09-30. Este documento **sustituye únicamente el diagnóstico de múltiplos pendientes** en los borradores técnicos anteriores; no cambia ningún supuesto o precio del DCF.

## Decisión conservando cálculos del DCF
Valor principal **DCF Base FCFF US$149,19148575564947** por acción y **MOS35% US$96,97446574117215**; precio de mercado fechado US$240,35. Cuatro historias: Conservadora81,0095; Base149,1915; Optimista241,8435; Disrupción62,4357 (separada). El resultado ponderado por DCF y relativos **US$190,5097762 Base** es secundario y **nunca reemplaza el valor principal**.

## Anclas provisionales y pruebas de trazabilidad
| Método | Criterio y evidencia | Múltiplo Base | VP FY+3 / centro Base 5x5 | VP consolidado hoy (1–3) | Peso final |
|---|---|---:|---:|---:|---:|
| EV/EBITDA | Hoja `EVEBITDA`; cinco por cinco nativo | 18,4620× | US$349,7436 | US$341,1023 | 16% |
| EV/FCFF | FCFF Base FY+3 **−US$6.371,9154 millones** (Valuation output!E11); precio económico no definido | **N/A** | **N/A** | **N/A** | **0%** |
| P/E | `PE!J19`: mínimo P/E positivo FY2023–24 (51,8519×; 39,2249×); FY2022 con pérdida y FY2025 excluido por ganancias financieras extraordinarias (Income Statement!K18=US$17.336 M). No afirma normalización exhaustiva | **39,2249×** | **US$373,1235** | **US$361,6629** | **8%** |
| P/FCFE | `PFCFE!J19`: mediana FY2024–25 de 78,4763× y 57,4774×; FY2022 flujo negativo y FY2023 denominador pequeño elevaba a 193,45× | **67,9768×** | **US$82,0177** | **US$28,1643** | **8%** |
| P/OCF | Hoja `POCF`, ancla histórica nativa | **19,6147×** | **US$208,7479** | **US$190,4043** | **8%** |

P/V y P/BV: N/D opcionales, sin múltiplos elegidos, matrices numéricas ni peso. Las cuatro matrices nativas de Base constan de 25 valores financieros cada una, con centro FY+3 conciliado; origen `Sensibilidad por múltiplo!A76:I144` y `Descuento de múltiplos!A11:K34`.

**Salvedad particularmente material:** P/FCFE Base implica precio FY+1 de **−US$32,73**, por reinversión; VP Base consolidado de tres años **US$28,16** frente a VP FY+3 de **US$82,02**. No interpretar como ancla estabilizada ni asumir que la mediana de dos cierres es certificación de flujo sostenible. La ancla P/E tampoco constituye una auditoría independiente de ganancias normalizadas. Los cuatro múltiplos son **contrastaciones EN_REVISION**, no pronósticos certificados.

## Ponderación reproducible: usar selector nativo, no valores manuales
`Resumen de Valoración!F8="No"` excluye EV/FCFF por FCFF FY+3 negativo. Las fórmulas existentes recalculan `B6:B11`: DCF60%, EV/EBITDA16%, EV/FCFF0%, P/E8%, P/FCFE8%, P/OCF8%, suma 100%. No hay que reescribir estas ponderaciones ni el DCF al reproducir el caso. Se mantienen las tres sensibilidades DCF 5×5 con centro 149,1915.

## Evidencia y límites de la publicación
- Fuente de celdas congelada: `evidencia/captura-hoja-20261103/AMZN-20261102-A12-R5_captura_numerica.json`; el JSON de valoración contiene su SHA-256 en `sensibilidadMultiples.resultadosSha256`.
- Identidad `ticker/revisionId/sheet_id/corte` idéntica en valoración y análisis. Los dos niveles de texto se integran en el análisis activo y conservan vínculo a la fuente escrita en este expediente.
- Los controles del motor anteriores aprobaron 52 regresiones, conciliación SEC 20/20, cobertura histórica con tres salvedades secundarias, candados15/15 y cero sustituciones de fórmulas.
- La integración de la publicación se somete por separado a cuatro workflows del catálogo y a verificación visual de la app; la existencia del JSON no prueba por sí sola despliegue.
- **No hay auditoría económica definitiva:** revisar costo de capital/deuda valor mercado, CAPEX-S/C y desfase, ROIC terminal y valor Level3 de Anthropic/OpenAI, SBC y dilución.

La condición `EN_REVISION` distingue claramente esta valoración de una certificada; permite inspección y comentarios sin alterar la hoja ni los valores principales.
