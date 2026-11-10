# UBER-REBOOT-3T26-R1 · R3 — cierre del DCF con beta 1,20

**Fecha de revisión:** 2026-11-10. **Modelo/ejecutor:** GPT-6, ChatGPT, herramientas GitHub/Google Sheets conectadas. **Estado:** R3 cálculos y sensibilidades conciliados; integridad completa de todas las fórmulas y comentarios por copia **NO_EJECUTADA**; publicación R5 y auditoría R6 **NO_EJECUTADAS**.

## Identidad e insumos
- Emisor UBER; corte contable 2026-09-30, precio de referencia fechado **68,59 USD** (2026-11-06). Ejecución sobre la revisión ya existente; no se creó otro libro ni se usó el archivo histórico Floyd como fuente.
- H: https://docs.google.com/spreadsheets/d/176tcVAz_RzHluf4kyjEEsMjDcDosldPdB5FBifO9YQA/edit
- DCF Base: https://docs.google.com/spreadsheets/d/14QlydMFli2pxdG4agUYOAXL8QIE99P-3UDE7vwK8CaM/edit
- DCF Conservadora: https://docs.google.com/spreadsheets/d/1TUDP8WvRpjtm5AbCpGkKkfyAlItRuufIAAEkFp95aHA/edit
- DCF Optimista: https://docs.google.com/spreadsheets/d/1f7Fzs7TBezRNa4E0lwHoh8fcPXTGn0d09HTatCaDLRU/edit
- Múltiplos: https://docs.google.com/spreadsheets/d/19fe8FcQ32d3yf169i-XA7F-c4IGhWTCNl_QO4WgCwA4/edit
- Análisis (sexto archivo): pendiente de R5.
- **Decisión expresa del usuario:** beta apalancada = **1,20** en los tres motores, como `Cost of capital worksheet!B21 = Direct Input` y `B22=1.20`. La beta bottom-up = 0,822 de la entrega antigua se conserva solo como sensibilidad histórica, **no es el supuesto vigente**.

## Valores vivos conciliados (USD/acción)
| DCF | Conservadora | Base | Optimista |
|---|---:|---:|---:|
| `Valuation output!B33` | 45,29115176 | **98,73828566** | 149,66887071 |
| Probabilidad | 25% | 50% | 25% |
| WACC inicial (común) | 9,999723886% | 9,999723886% | 9,999723886% |
| WACC estable | 8,247% | 8,247% | 8,247% |
| Costo de patrimonio Ke | 10,48752249% | 10,48752249% | 10,48752249% |

**Promedio ponderado:** 98,10914844 USD. **MOS 35% exclusivamente sobre DCF Base:** 64,17988568 USD. Precio fechado 68,59: descuento frente al Base `1−68.59/98.73828566=30,53%`; **NO cumple MOS 35%** a este precio de referencia.

## Supuestos y relato económico vigente
- LTM ingresos **56.526 USDm**; EBIT contable **7.034 USDm**; EBIT ajustado por capitalización de I+D **7.961 USDm** (costos de I+D LTM 4.152; vida tres años); efectivo más inversiones CP 10.068 USDm; deuda 15.664 USDm sin capitalización adicional ASC842; activos no operativos 11.473 USDm como proxy libro; minoritarios 1.304 USDm; acciones ajustadas 2.107,437 millones.
- Rf 4,86%; ERP geográfica efectiva 4,6896021%; Ke 10,4875%; costo de deuda antes de impuesto 6,10%, estimado y aún pendiente de verificación de rating; WACC inicial 9,9997% y estable 8,247%. La ERP madura 3,387% y el mix geográfico proceden de la entrega R3 anterior.
- Año 1 / crecimiento CAGR años 2–5: Conservadora 7,0% / 9,75%; Base 11,0% / 14,0%; Optimista 13,0% / 16,25%.
- Margen operativo objetivo ajustado: 13% / 18% / 22%, sobre 14,08% actual; ventas/capital años 1–5: 2,0 / 2,8 / 3,4; años 6–10: 1,8 / 2,5 / 3,0; ROIC terminal 8,247% / 13,23% / 18,21%; g terminal 4,0% en las tres historias.
- Historias y probabilidades 25/50/25 conservadas. La asignación de riesgo a la plataforma (beta 1,20), márgenes y ROIC son juicios de valoración, no datos contables reportados. Riesgo de autonomía, seguros, litigios, S/C y valor de participadas no certifican por sí solos el escenario.

## Sensibilidades verificadas contra el motor vivo — beta 1,20
Las celdas de las dos matrices 5×5 se sustituyeron por **50 valores recalculados con cambios temporales exclusivamente de entradas**, restaurando al final `Input sheet!B26=.11, B28=.14, B29=.18, B68=.04` y `Cost of capital worksheet!B22=1.20`.

- **Matriz A** `Sensibilidades DCF!B6:F10`: CAGR años 2–5 (10%,12%,14%,16%,18%) × margen ajustado (14%,16%,18%,20%,22%). Centro **98,7382856555**.
- **Matriz B** `Sensibilidades DCF!B14:F18`: WACC inicial aprox. 9%,9,5%,10%,10,5%,11% (recalculado vía beta temporal; costo estable fijo) × g terminal 3%,3,5%,4%,4,5%,4,8%. Centro **98,7382856555**.
- `Sensibilidades DCF!B28:B29` se convirtió a fórmulas de diferencia entre centros y `Valuation output!B33`, ambas objetivo **0**. `B30` y `B31` vinculados al valor y precio vivos.
- **DCF inverso** sobre precio 68,59 USD: crecimiento anual igual para años 1–5 ≈6,15% con margen Base; margen objetivo ≈12,6412% con crecimiento Base; crecimiento ≈8,51% con margen objetivo 16%; WACC inicial ≈16,51% manteniendo WACC estable 8,247%. Son contrafactuales de una variable, NO reemplazan la beta 1,20 aprobada.

## Comprobaciones
| Control | Resultado |
|---|---|
| Tres historias calculadas del modelo vivo, costos comunes y orden Conservadora ≤ Base ≤ Optimista | **APROBADO** |
| Ponderaciones 25/50/25; MOS = 0,65 × DCF Base | **APROBADO** |
| Matrices A y B 5×5 por corridas; ambos centros iguales al Base; retorno a entradas originales | **APROBADO** |
| DCF inverso con distintas entradas, restauración final | **APROBADO** |
| Fuentes primarias, caja restringida, inversiones y NOL con dictamen económico final | **PARCIAL** (ver R2, R6) |
| Huella integral fórmulas/comentarios **de cada copia** contra el archivo maestro Damodaran | **NO_EJECUTADO** (en R1 la plantilla sí se cotejó, no estas copias) |
| Análisis R5, integración app y auditoría independiente R6 | **NO_EJECUTADO** |

**PASOS R3: 5/6 técnicos/económicos realizados; compuerta documental de motor sin verificar.** No significa publicación ni certificación.

## Continuidad
R4 utilizará este conjunto y **solo** el H Reboot; traspaso H→M y DCF→M, cinco múltiplos y matrices de sensibilidad individuales. La hoja de Múltiplos se mantiene secundaria; su propia puerta puede declarar `NO PUBLICAR` hasta cubrir fuentes y métodos. El estado vigente de catálogo para UBER continúa siendo Floyd anterior; esta revisión Reboot permanece **CANDIDATO**. 
