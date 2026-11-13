# CMG R4 · materialidad del tratamiento ASC 842 (5-nov-2026)

**Estado:** CANDIDATO, **NO** publicable conforme §4B/§6; prueba económica **no certificada**, no análisis F5 independiente.

## Evidencia y cálculo

- Pasivo lease corriente SEC USD 321,557 M y no corriente USD 5.277,474 M; total USD 5.599,031 M. ROU USD 4.928,149 M.
- EBIT GAAP LTM USD 1.794,941 M. El gasto de arrendamiento está dentro del resultado operativo (rent-as-operating).
- Interés implícito estimado **proxy** = 0,0548 × promedio de lease FY25/Q3 2026 = USD 292,490753 M. No es una cuenta publicada separadamente.
- EBIT lease-adjusted proxy = USD 2.087,431753 M; margen 16,4190 % vs GAAP 14,1184 %.
- Capitalización de mercado USD 44.526,944 M; deuda de arrendamientos reconocida USD 5.599,031 M, proporción de deuda 11,17 % vs 5,24 % del cálculo anterior que valoraba como bono de cupón cero USD 2.462,069 M.
- Con beta sectorial reapalancada por pasivo lease y costo deuda 6 % asumido, WACC proxy 8,1839818783 % vs WACC inicial previo 8,2484040294 %.

## DCF en una COPIA separada, sin alterar Base ni fórmulas Damodaran

| Captura | Supuestos cambiados | USD/acción |
|---|---|---:|
| 1 | Base sin recast | **24,9573584990** |
| 2 | EBIT actual → 2.087,431753 M y margen próximo año → 16,81873789 %, WACC igual | 25,4221297886 |
| 3 | Además WACC proxy 8,18398188 % | **25,5340648116** |

Variación 3 vs 1: **+2,31076663 %**, superior al umbral individual de **2 %** de materialidad JMR. Aun así, NO es un escenario económicamente coherente completo: faltan reinversión lease-adjusted y ROU, costo marginal del leasing, ROIC económico/terminal, tasa de descuento en valor residual, impuestos, y una reconciliación de la política de arrendamientos.

Copia de prueba: https://docs.google.com/spreadsheets/d/1hCu-nFkyAEIXqbz5985Nei7Fc_hU7P1BWW-YPmRhFE8/edit

Hoja de auditoría contable (fórmulas vivas): https://docs.google.com/spreadsheets/d/1hSKPKEUsCtQdpZp30__zCDFCqpMifbco05LsNhG8dX0/edit#gid=2051105005

## Gate para publicación

1. Elegir un tratamiento contable homogéneo (arrendamientos como gasto, sin pasivo lease en EV, o como deuda con EBIT/reinversión/ROIC y WACC reexpresados).
2. Recalcular Base, Conservador, Optimista y Disrupción sobre copias limpias, no ajustar cifras para llegar al precio de mercado.
3. Reconciliar 5 múltiplos, 3 sensibilidades DCF 5×5, análisis N1/N2 y test completo de publicación; CI y vista productiva comprobada.
4. Hasta entonces **no fusionar/prorratear valor R4 en catalogo.json**. A3 es la única revisión visible autorizada.