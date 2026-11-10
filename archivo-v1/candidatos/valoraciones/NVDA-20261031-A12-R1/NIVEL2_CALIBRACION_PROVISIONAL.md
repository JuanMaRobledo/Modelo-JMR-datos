# NVDA · Nivel 2 reproducible JMR A-1.2 (candidato / NO PUBLICAR)

**Corte contable:** 26-jul-2026, Q2 fiscal 2027 · **Fecha económica:** 31-oct-2026 · **Precio de mercado:** US$204,64 cierre 30-oct-2026 · **Unidad:** millones USD, salvo por acción.
**No se utilizaron resultados Q3FY27**: NVIDIA los publicará el 17-nov-2026, aunque el trimestre terminó el 25-oct.

## 1. Fuente histórica y puente de ventas
FY2026 US$215.938m + Q1FY27 US$81.615m + Q2FY27 US$96.221m − Q1FY26 US$44.062m − Q2FY26 US$46.743m = **US$302.969m**. La copia de la hoja fuente indica **US$302.970m**: diferencia de **US$1m**, aún sin regularizar por redondeos/categoría. Para no modificar históricos se usa 302.970m como dato de la hoja en esta simulación, con salvedad abierta. El EBIT LTM es 130.387 +53.536 +63.734 −21.638 −28.440 = **197.579m**.

## 2. Normalización de I+D y otros gastos
El conversor I+D capitalizada en vida de 3 años computa **US$12.337m** de ajuste EBIT y US$37.371m de activo I+D, derivado de US$23.592m de gasto LTM. Margen EBIT inicial analítico = (197.579+12.337)/302.970 = **69,29%**. Hay que conservar en reinversión el tratamiento económico de I+D capitalizada y evitar sumar otra vez los gastos como capex físico. La compensación en acciones no es caja libre de costo económico para el accionista: debe rastrearse en dilución/SBC y acciones.

## 3. Geografía y ciclo económico de semiconductores
La demanda de GPU y redes IA combina inversión de hyperscalers, laboratorios y empresas, con riesgo de concentración, exportaciones a China, HBM/packaging, energía y desarrollo ASIC. El capex de clientes es ingreso potencial para NVIDIA, no su propio gasto de reinversión. La guía de 3T FY27 es **US$108.000m ±2%** de ventas (no un trimestre reportado).

## 4. WACC y capitalización
`Rf=4,94%`, `ERP octubre=3,70%`, beta apalancada preliminar **1,45**, `Kd=6%`, marginal **25,37%**; deuda total libro **38.860m = 1.000 corto + 32.366 largo + 509 lease corto + 4.985 lease largo**. Los lease GAAP ya están dentro del pasivo contable, por lo que `Input sheet!B18=No` evita volver a incluirlos. La estructura de mercado del libro y la fórmula Detailed producen **WACC 10,28%** con control técnico `VALIDADO`. Beta, precio de deuda, riesgo geográfico y mercado aún requieren auditoría económica. WACC terminal candidato **9,30%**.

## 5. Fiscalidad
El impuesto FY2027 esperado por NVIDIA es 16–18% excluyendo efectos discretos. Se usa **17%** años 1–5, subiendo gradualmente a **25,37%** en el año 10, como tasa marginal de largo plazo. No se adopta la tasa extraordinaria de ningún trimestre como efectiva perpetua.

## 6. Métodos de proyección
`Revenues[t] = Revenues[t−1] × (1+g[t])`; `EBIT = revenues×margin`; `NOPAT = EBIT×(1−tax)`; `Reinvestment[t] = (Revenues[t+1]−Revenues[t]) / SalesToCapital[t]` (adelanto un año, como libro); `FCFF = NOPAT−Reinvestment`. En disrupción se evita liberar automáticamente capital cuando caen las ventas, registrando cero reinversión negativa hasta demostrar desinversiones reales. `PVFCFF[t] = FCFF[t]×producto(1/(1+WACC[i]))`; `Terminal FCFF = Terminal NOPAT × (1−g/ROICterminal)`.

## 7. Cuatro escenarios

| Historia | Probabilidad | CAGR 5a | EBIT maduro | S/C 1–5 | S/C 6–10 | ROIC terminal | g | DCF/acc. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Base | 45,00% | 23,65% | 53,00% | 2,20 | 0,70 | 28,66% | 3,50% | US$201,45 |
| Conservadora | 22,50% | 15,19% | 43,00% | 1,40 | 0,62 | 20,49% | 3,00% | US$107,74 |
| Disrupción | 10,00% | 4,48% | 30,00% | 0,85 | 0,65 | 14,77% | 1,50% | US$49,60 |
| Optimista | 22,50% | 32,17% | 57,00% | 2,80 | 0,78 | 34,51% | 4,00% | US$344,61 |

Disrupción se presenta por separado; la media ponderada de las tres restantes es **US$213,81** por acción, no el valor Base principal. El **Base candidato** es US$201,45, MOS35% US$130,94, por lo que al cierre US$204,64 no existe margen de seguridad del 35% en este conjunto de hipótesis.

## 8. Proyección de diez años Base

| Año | Ingresos | Crecimiento | Margen EBIT | NOPAT | Reinversión | FCFF | WACC | PV FCFF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 424.158 | 40,00% | 69,29% | 243.922 | 53.984 | 189.939 | 10,28% | 172.240 |
| 2 | 542.922 | 28,00% | 62,77% | 282.865 | 54.292 | 228.573 | 10,28% | 187.960 |
| 3 | 662.365 | 22,00% | 59,51% | 327.188 | 51.183 | 276.006 | 10,28% | 205.816 |
| 4 | 774.967 | 17,00% | 56,26% | 361.859 | 45.794 | 316.066 | 10,28% | 213.727 |
| 5 | 875.713 | 13,00% | 53,00% | 385.226 | 41.795 | 343.431 | 10,28% | 210.591 |
| 6 | 967.663 | 10,50% | 53,00% | 417.090 | 117.502 | 299.588 | 10,08% | 166.884 |
| 7 | 1.049.914 | 8,50% | 53,00% | 443.227 | 97.492 | 345.735 | 9,89% | 175.265 |
| 8 | 1.118.159 | 6,50% | 53,00% | 462.116 | 87.855 | 374.261 | 9,69% | 172.965 |
| 9 | 1.179.657 | 5,50% | 53,00% | 477.067 | 75.835 | 401.232 | 9,50% | 169.349 |
| 10 | 1.232.742 | 4,50% | 53,00% | 487.597 | 61.637 | 425.960 | 9,30% | 164.489 |

## 9. Puente valor empresa/patrimonio
PV FCFF explícito **US$1.839.284m**, PV terminal **US$2.949.641m**, EV **US$4.788.925m**. Equity candidato: EV − 38.860m deuda + 99.369m caja + **39.257m de inversión no operativa usada solo como proxy de valor contable**, antes de ajuste de RSU/SBC; resulta **US$4.888.691m**. Dividir por **24.268m acciones** = **US$201,45**. El libro original declaró que no hay opciones de ejercicio; las RSU no equivalen a opciones, pero quedan pendientes de conciliación y no se pueden asumir sin costo.

## 10. Sensibilidades
Dos matrices 5×5 independientes: `WACC × g` y `WACC × ROIC terminal`. Sus celdas centrales concilian exactamente con US$201,45. La sensibilidad específica a S/C de madurez: a S/C 0,70 implica ROIC 28,66% y DCF ~201,45; elevar S/C 0,84 implica ROIC 34,39% y DCF ~205,72, diferencia de ~US$4,27. Esto muestra que modificar un solo ratio para justificar el antiguo valor US$381,79 sería inadecuado.

## 11. Múltiplos, AZ Stocks y estructura de salida
Falta recapturar y conciliar de la hoja: EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF, con P/S y P/BV secundarios; diferenciar estimaciones FY+3, múltiplos contratados, descontados a hoy y centros de sensibilidad 5×5. No se fabrican matrices N/A con 0. AZ Stocks será un contraste DCF perpetuidad separado.

## 12. Control pendiente y decisión
El gate del motor independiente reproduce los cuatro DCF y matrices, pero la hoja base sigue sin publicar y `Escenarios e historias!K5:K8` conserva `PENDIENTE`. Falta valor económico de participaciones, retención económica de SBC/RSU, otras contingencias y fuentes de múltiplos; la limpieza de PR211 no ha recuperado CI. La nueva revisión no debe reemplazar NVDA R4 ni etiquetarse `EN_REVISION` hasta reconciliar la proyección con el archivo oficial y completar QA.

**Fuentes:** [NVIDIA Q2FY27](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027); [10-Q](https://investor.nvidia.com/files/doc_financials/2027/NVDA-2027-Q2-10Q-Final-including-exhibits.pdf); [Anuncio Q3FY27](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx); [Damodaran octubre](https://aswathdamodaran.blogspot.com/2026/10); [Treasury 30-oct](https://ploveranalytics.com/us-treasury.html); [hoja A-1.2](https://docs.google.com/spreadsheets/d/1gN_WFYyGzdLjgYr_0AEHGDdBIeCiNVnDFy0wkH0vB0Y/edit).

**Documento analítico sujeto a revisión; no constituye certificación ni publicación.**
