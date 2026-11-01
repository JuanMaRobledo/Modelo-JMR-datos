# META y NVDA · alineación de fechas de tasas · 1-nov-2026

**Problema:** las hojas usaban Rf 4,94 % (Treasury 10 años del 30-oct-2026, FRED) con la ERP de Damodaran de oct-2026 (3,70 %), que se calculó con Rf 5,29 % al 30-sep. La regla del repositorio exige tasa libre y prima de la **misma fecha**. Además el WACC terminal estaba escrito a mano (META 8,80 %, NVDA 9,30 %) sin excepción documentada.

**Cambio (solo `Input sheet`, ambas hojas):** `B35` Rf 4,94 % → **5,29 %** (30-sep-2026, `reference/corte_vigente.json`; coincide con la tasa de Damodaran) y `B47` WACC terminal → **8,99 %** (= Rf 5,29 % + ERP madura 3,70 %, `costo_capital_terminal` del corte). ERP 3,70 % sin cambio. Beta (META 1,15; NVDA 1,45), Kd, g 3,5 % y ROIC terminal sin tocar. Valores previos en `evidencia/cierre-gates-meta-nvda-20261101/fechas_tasas_antes_despues.json`.

| | Base antes | Base después | Cons. | Disrupción | Opt. | WACC inicial | WACC terminal |
|---|---:|---:|---:|---:|---:|---|---|
| META | 783,42 | **745,29** | 464,96 | 239,95 | 1.094,55 | 8,98 % → 9,31 % | 8,80 % → 8,99 % |
| NVDA | 201,80 | **205,95** | 109,66 | 50,08 | 354,62 | 10,28 % → 10,62 % | 9,30 % → 8,99 % |

K5:K8 = LISTO, `Cost of capital!B84` = VALIDADO, `B85`, `B92`, `B108` VALIDADO en ambas. Después se recalcularon anclas justificadas y se reaplicaron las decisiones de múltiplos (misma regla por ciclo):

| Consolidado de múltiplos hoy (Cons./Base/Opt.) | DCF Base | Brecha Base múltiplos vs DCF |
|---|---:|---:|
| META 367,94 / 399,88 / 567,32 | 745,29 | −46 % |
| NVDA 124,40 / 228,80 / 360,40 | 205,95 | +11 % |

Chequeo VP3 < FY+3 `OK` (6/6) y control de centro de las 10 matrices 5×5 `OK`.

**Qué queda de fechas:** el precio de mercado de cada empresa sigue al 30-oct-2026 (META 614,99; NVDA 204,64) como cotización de referencia; las tasas de descuento están a 30-sep (par publicado). Los pares de múltiplos están a 30-sep. Cuando Damodaran publique la ERP de nov-2026 (con datos del 30-oct) habrá que actualizar Rf, ERP y terminal juntos. Este cambio altera los valores de la hoja respecto a los candidatos y a `CIERRE_GATES_META_NVDA_20261101.md`, que quedan como estado previo.
