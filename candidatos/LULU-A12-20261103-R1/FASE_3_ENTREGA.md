# LULU A-1.2 — Fase 3: calibración económica y control de supuestos

**Revisión:** LULU-20261103-A12-R1 · **Corte de mercado:** 03/11/2026 · **contable:** 02/08/2026 · **moneda:** USD millones salvo por acción. **Hoja oficial:** https://docs.google.com/spreadsheets/d/1XY_iXmarfM0ESnzu3RMV5E4TkgrJAy9-XzJ2PxndHz4/edit

## Resumen de pruebas nativas, no certificación económica

| Componente | Dato/hipótesis | Evidencia | Estado |
|---|---|---|---|
| Base operativa | Ingresos LTM 11.093,955m; GAAP EBIT 1.978,775m | SEC FY2025 10-K + H1 FY2026/2025 10-Q, puente FY + H1 − H1 | CONCILIADO |
| EBIT DCF | GAAP − IEEPA refund134,5m + interés leasing proxy94,2096m = 1.938,4846m | Input B13, Aux C65/C84, SEC descuento leases4,4% | CÁLCULO con salvedad |
| Crecimiento año1 | FY2026 guía10.350–10.500m + juicio H1FY2027 +1%; LTM→forward −5,589374% | Aux C94:C101, Input B27, Valuation output C4:C5 | MODELO, no dato futuro |
| Márgenes | 14,2% año1→17,5% año10, vs FY2024 23,67% y FY2025 19,91% | Valuation output C6:L6, SEC | HIPÓTESIS JUSTIFICADA |
| Reinversión | S/C marginal años1-5 1,8; años6-10 1,77 vs sector Apparel1,77 | Input B32:B33, Damodaran Apparel; histórico marginal FY2021-25 1,87 vs FY2023-25 ~0,95 | HIPÓTESIS JUSTIFICADA, desfase probado |
| ROIC existente | FY2025 35,16%, LTM26,52%, año10 sobre capital acumulado 23,09% | Eficiencia de capital LTM y Valuation output L42 | VERIFICADO CÁLCULO |
| RONIC marginal terminal | 14% Base, 11,5% conservador, 16% optimista, 9,5% disrupción | Escenarios G5:G8, Input B50 | JUICIO; no igual ROIC capital existente |
| WACC inicial | Rf5,29%, ERP4,41% mismo corte Damodaran nov2026; beta0,894879; Ke9,2364%; Kd contractual4,4%; pesos equity84,9026/deuda15,0974; WACC8,3136% | Cost of capital worksheet B84 VALIDADO, estructura ASC842 | HOJA VALIDADA, costo marginal deuda reserva |
| WACC terminal | 9,70%, > g3%, ROIC marginal14% > g | Valuation output B19 y terminal M | REGLAS ARITMÉTICAS OK |
| Equity bridge | EV16.875,727m; leases2.141,127m; caja1.389,737m; opciones34,186m; acciones112,585m | Valuation output B21:B35 | CONCILIADO Nativo |
| DCF Base/MOS | 142,915585 / 92,895130 USD | Valuation output B35, Resumen | VERIFICADO cálculo |
| Historias | Base142,916, Conserv105,698, Optim184,562, Disrupt73,999 | Escenarios e historias H5:H8; cuatro K="LISTO" | CÁLCULO NATIVO |
| DCF sensibilidades | 3 grillas5×5, centros iguales Base exacto | Sensibilidad DCF A4:F34, snapshot JSON SHA256 | 3/3 OK |
| Cinco múltiplos | EV/EBITDA7,5068x, EV/FCFF21,63x, P/E12,8728x, P/FCFE22,0561x, P/OCF12,3938x | Descuento de múltiplos FY+1/2/3 y anclas FY2022–25 | 5/5 resultados, reservas |
| Matrices de múltiplos | 5 prioritarias Base5×5; P/V y P/BV N/D peso cero | Sensibilidad por múltiplo A76:I144, fotografía con hash | 5/5 centros OK |
| Integral FY+3 | DCF capitalizado+cinco múltiplos ponderados=164,3064 USD en FY+3 | Resumen de Valoración D12, categoría Madura | CÁLCULO; NO VALOR PRESENTE |
| Principal vs mercado | DCF Base142,9156 presente; cotización106,95, MOS35 umbral92,895 | Cotización 03/11/2026, DCF principal | NO equiparar horizonte FY3 con presente |

## Prueba de cambios económicos, copiadas y preservadas

| Alternativa | Hoja | DCF Base | Impacto vs libro oficial |
|---|---|---:|---:|
| Original: lag reinversión1 año y ROIC marginal terminal14%, Kd4,4% | [Oficial](https://docs.google.com/spreadsheets/d/1XY_iXmarfM0ESnzu3RMV5E4TkgrJAy9-XzJ2PxndHz4/edit) | 142,915585 | 0 |
| Lag0 (solo desfase, mismos supuestos restantes) | [Lag0](https://docs.google.com/spreadsheets/d/1OjGuh2aG3CRnwWj05FpO8YdB16aPxwS75jGa_pAi_U0/edit) | 144,987046 | +2,071461 (+1,45%) |
| ROIC **marginal terminal**23,09134% en lugar de 14%, mismos flujos años1–10 | [ROIC alternativo](https://docs.google.com/spreadsheets/d/1SiNePF2CAxL_QJSQp42ydkHCpz-J2Z71hhQY_2GEwXU/edit) | 152,065041 | +9,149456 (+6,40%) |
| Kd 6,29% (proxy nuevo financiamiento Treasury5,29%+1pp) vs Kd contractual4,4% | [Kd alternativo](https://docs.google.com/spreadsheets/d/1T-YV7ZzxxzTJbBpFcnB9-BmhRe7_dXPIzJye4dDDQ5s/edit) | 141,049397 | −1,866188 (−1,31%) |

**Aclaración económica:** la tasa ROIC año10 que arroja el libro sobre TODO el capital acumulado es 23,09134%, mientras que la tasa que determina reinversión perpetua es un **ROIC/RONIC marginal sobre la INVERSIÓN NUEVA** del 14%. Diferencia 9,09134 pp; no se interpreta como caída súbita del EBIT sobre el capital heredado. El diferencial por nueva competencia justificaría RONIC terminal inferior; la sensibilidad cuantifica que adoptar RONIC=ROIC año10 sumaría US$9,15 por acción. Es hipótesis crítica que deberá revisar F5 con cohortes de tiendas y retornos de proyectos nuevos. No se sustituyeron fórmulas para forzar convergencia mecánica.

**Otra reserva:** en una estructura financiada con arrendamientos existentes, el costo contractual4,4% puede quedar debajo de Rf5,29% de noviembre 2026; para NUEVA financiación no es una tasa de mercado. La sensibilidad Kd6,29% constituye juicio, no spread crediticio comprobado. La contabilidad ASC842 exige consistencia en EBIT más costo implícito de rentas y pasivo sin doble conteo. El ajuste de interés aproximado se registra como proxy, no como ingreso GAAP.

## Gates de transición

La hoja pasó sus controles nativos, y las sensibilidades de dos parámetros fueron hechas en **copias aisladas**, no por edición de estructura. El Nivel1 completo y Nivel2 están en el PR #243 junto al JSON y fuente SHA256. La promoción del PR a producción solo puede ejecutarse después de que los cuatro workflows CI relevantes y el gate de no regresión pasen, se compruebe que el catálogo conserva todas las empresas y se verifique la ficha real. El análisis continúa EN_REVISION, **sin certificación económica**.
