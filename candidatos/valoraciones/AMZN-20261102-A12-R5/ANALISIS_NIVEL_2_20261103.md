# Amazon (AMZN) · Nivel 2 JMR A-1.2 · soporte cuantitativo reproducible

**Revisión y fuente única:** `AMZN-20261102-A12-R5` · [Google Sheet R5](https://docs.google.com/spreadsheets/d/199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I/edit). Moneda USD; **cifras monetarias en millones USD**, precios en USD/acción, acciones en millones, tasas % o proporción según tabla. Corte contable **2026-09-30**, cierre mercado de referencia **2026-10-30**, precio **240,35**. Versión de metodología **A-1.2 / reglas v27**. **Documento candidato de investigación, NO certificado ni publicado.** Las tablas anuales se generaron leyendo `Valuation output` en la **misma hoja R5** sin escribir celdas.

## 1. Identidad, fuentes, fechas y unidades

Empresa Amazon.com, Inc. (`NASDAQ: AMZN`), negocios operativos retail, marketplace, publicidad, AWS. Expediente F1/F2/F3 vigente en [PR #234](https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/234); auditor técnico candidato [motor PR #203](https://github.com/JuanMaRobledo/JMR-valuation/pull/203). Anclas primarias: [10-K 2025](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm), [10-Q Sep2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm), [10-K 2022 (split)](https://www.sec.gov/Archives/edgar/data/1018724/000101872423000004/amzn-20221231.htm); cotejos por año en [F2](FASE_2_ENTREGA.md).

Distinguir **LTM**, 10 ejercicios fiscales cerrados FY2016–FY2025 y previsión FY2027–FY2036; los saldos de balance LTM son a fecha de corte, no promedio de 12 meses. La fecha de precio 30-oct y la de tasas del modelo no son idénticas: no llamar al WACC valor de mercado en tiempo real. Los años pre-2019 de leases no se reexpresan ficticiamente como contratos ASC842.

## 2. Estados históricos FY2016–FY2025 y LTM

| Año (fin fiscal salvo LTM) | Ventas | EBIT GAAP | NI GAAP | CFO | CAPEX bruto (+) | D&A flujo | Activo total | Patrimonio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2016 | 135.987 | 4.186 | 2.371 | 17.203 | 7.804 | 8.116 | 83.402 | 19.285 |
| 2017 | 177.866 | 4.106 | 3.033 | 18.365 | 11.955 | 11.478 | 131.310 | 27.709 |
| 2018 | 232.887 | 12.421 | 10.073 | 30.723 | 13.427 | 15.341 | 162.648 | 43.549 |
| 2019 | 280.522 | 14.541 | 11.588 | 38.514 | 16.861 | 21.789 | 225.248 | 62.060 |
| 2020 | 386.064 | 22.899 | 21.331 | 66.064 | 40.140 | 25.251 | 321.195 | 93.404 |
| 2021 | 469.822 | 24.879 | 33.364 | 46.327 | 61.053 | 34.433 | 420.549 | 138.245 |
| 2022 | 513.983 | 12.248 | -2.722 | 46.752 | 63.645 | 41.921 | 462.675 | 146.043 |
| 2023 | 574.785 | 36.852 | 30.425 | 84.946 | 52.729 | 48.663 | 527.854 | 201.875 |
| 2024 | 637.959 | 68.593 | 59.248 | 115.877 | 82.999 | 52.795 | 624.894 | 285.970 |
| 2025 | 716.924 | 79.975 | 77.670 | 139.514 | 131.819 | 65.756 | 818.042 | 411.065 |
| LTM Sep2026 | 797.455 | 104.366 | 134.779 | 168.300 | 215.192 | 79.353 | 1.243.390 | 613.601 |

Series base: `Income Statement!B3:L3,B12:L12,B22:L22`; `Cash Flow Statement!B4:L4,B13:L13,B15:L15`; `Balance Sheet!B16:L16,B35:L35`. Valores monetarios agregados a millones, CAPEX bruto presentado aquí en positivo por legibilidad; en flujo de caja `CF!L15=-215192`. Los indicadores históricos de primera apertura provienen de `Entradas históricas auxiliares`, no de rellenos numéricos. **Aritmética histórica F2: 88/88 identidades de estados conciliadas** según acta; no equivale a corroboración total SEC por partida.

En 9M2026 los segmentos fuente SEC: North America **333172 ventas / 26113 EBIT**; International **125094 / 4721**; AWS **125803 / 48555**; consolidado **584069 / 79389**. Amazon reportó utilidades extraordinarias en inversiones de IA no operativas, por lo que NI GAAP LTM 134779 no equivale a beneficio recurrente. FY2022 NI −2722 tiene efectos de participaciones no operativas.

## 3. Ratios económicos, ROIC, caja y balance

La hoja `Eficiencia de capital` conserva fórmulas de ROIC (NOPAT / promedio de capital invertido), ROA (NI / activos promedio) y ROE (NI / patrimonio promedio) con balances de apertura específicos. El ROIC histórico observado es **2024 19,2371% → 2025 15,9376% → LTM 13,0740%**; deterioro durante la expansión de activos y consumo de caja. Los márgenes EBIT GAAP `Income Statement!L13` son FY2024 **10,75%**, FY2025 **11,16%**, LTM **13,09%**. Crecimiento LTM comparable 15,350845%, 9M2026 vs 9M2025 15,993033%; CAGR FY2016–2025 ~20,29% (9 intervalos). La estrategia de crecimiento implica productividad incremental y no solo gasto.

Caja y valores cortos `Balance Sheet!L5=114226`; deuda de libro para puente DCF `Input sheet!B16=304841` (incluye leases actuales ya reconocidos); patrimonio contable `BS!L35=613601`, activos totales `BS!L16=1243390`; PPE neto `BS!L11=508862`. El crédito de IVA, otras cuentas y subcategorías presentadas agregadas no se convierten en cero, sino `AGREGADO_CON_PUENTE` con reporte del validador candidato. `Eficiencia de capital` rentabilidad de activos tangibles y rotación/DSO permanecen N/D sin desglose. `Cash Flow Statement!L36=-46892` es FCF **sin** incentivos; Amazon reportó **−42357** con proceeds 4535 (ver `Input sheet!B159:B164`). No confundir las definiciones.

## 4. Puente contable → económico: I+D, deuda, leases, SBC y activos financieros

| Puente o dato | Importe/condición | Ubicación y tratamiento |
|---|---:|---|
| I+D aproximada LTM | 31734,5 | `Income Statement!L10`, proxy 25% de tecnología; no gasto R&D puro SEC |
| Activo de investigación capitalizado | 78943,15 | `R& D converter!D36` |
| Amortización de investigación | 20597,6 | `R& D converter!D38` |
| Ajuste de EBIT | +11136,9 | `R& D converter!D40`, una sola vez |
| EBIT DCF base ajustado | 115502,9 | `Valuation output!B7` |
| RSU pendientes (aprox.) | 223,3 M | Nota SEC; no options Black-Scholes |
| SBC LTM | 19873 | `Cash Flow Statement!L5` |
| Deuda contable incl. leases reconocidos | 304841 | `Input sheet!B16`, evitar capitalizar ASC842 dos veces |
| Cash y valores de mercado | 114226 | `Valuation output!B29` |
| Activos no operativos privados | 288700 | `Valuation output!B30`, una vez |
| Valor de stock options | 0 condicional | `Valuation output!B32`; NO equivale a ignorar RSUs |

`Balance Sheet!L14=288700` se desglosa según SEC 2026Q3 en Anthropic notas 146200, Anthropic preferred 92500 y OpenAI preferred 50000. Son instrumentos Level 3/no cotizados, y afectan valoración patrimonial y riesgo, no ingresos operativos. Shock −25% / −50% sobre ese saldo: −6,68 / −13,35 USD/acción ceteris paribus. No usar el valor agregado 298800 de otra categoría para duplicar participaciones. La deuda a precio de mercado, beta/ERP geográfica y vesting económico de RSUs son reservas materiales no cerradas. No hay warrants/stock options modelables activos con selector B38=No. El NOL B62=No no significa pérdidas fiscales históricas cero.

## 5. Tabla exacta de drivers por historia

| Historia | Peso | CAGR 1–5 | Margen objetivo EBIT | S/C 1–5 | S/C 6–10 | ROIC term. | g terminal | DCF hoy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Base | 45% | 9,2947% | 15,8% | 0,72 | 1,65 | 11,5% | 4,0% | 149,19 |
| Conservadora | 22,5% | 6,5965% | 12,0% | 0,52 | 1,25 | 9,5% | 3,2% | 81,01 |
| Optimista | 22,5% | 12,0918% | 18,5% | 1,15 | 2,10 | 15,0% | 4,0% | 241,84 |
| Disrupción | 10% | 0,9901% | 8,5% | 0,35 | 1,05 | 7,5% | 2,5% | 62,44 |

Fuente exacta `Escenarios e historias!B5:K8,N5:N8`; peso no es calificación de inversión ni probabilidad estadística de SEC. Crecimiento Base FY+1 `Input sheet!B27=11%`, FY+2..5 `B29≈8,8725%`; margen objetivo en historia `D5=15,8%` no referencia informativa `Input B30`; S/C de historia `E5:F5` no cifra industrial referencial `Input B32:B33≈2,7255`. Capital invertido y ROIC terminal convergen según plantilla; efecto preciso de terminal depende de formula de reinversión.

## 6. Costo de capital detallado

| Componente | Cifra actual R5 | Evidencia y condición |
|---|---:|---|
| Rf nominal USD | 5,29% | `Input sheet!B35` |
| ERP madura de referencia | 3,70% | `Cost of capital worksheet!B26`; puente geográfico por cerrar |
| Enfoque WACC | Detailed multibusiness | Retail/Computer Services, `Cost of capital worksheet!B12` |
| Ke de descuento múltiplos | 8,443339% | `Descuento de múltiplos!B5` |
| WACC años 1–5 | 8,179603% | `Cost of capital worksheet!B14` |
| WACC año 6–10 | converge 8,34%→8,99% | `Valuation output!H14:L14` |
| WACC terminal | 8,99% | `Valuation output!B19`, `Input sheet!B97` |
| Tasa fiscal proyectada | 25% | `Input sheet!B90,B93` |
| Deuda | 304841 M contable | valor mercado y obligaciones #197 pendientes |

Los componentes completos de beta, estructura objetivo Kd/pesos e hipótesis por región se encuentran en `Cost of capital worksheet` y `WACC Detailed Multibusiness`; **aún no se ha certificado un puente independiente de deuda mercado/ERP regional**. Por eso se informan los valores agregados observados y no se inventan betas o spreads puntuales. El WACC terminal debe ser superior a g; Base 8,99% vs 4,0%, diferencia4,99 pp. Recalibrar a fecha común cuando cambie corte.

## 7. DCF anual completo de 10 años — cuatro historias

Las tablas siguientes proceden de las celdas numéricas **sin redondear** de `Valuation output` y se muestran redondeadas para lectura. `Reinversión` = aumento económico de capital con Sales-to-Capital y lag, **no** CAPEX bruto. NOPAT=EBIT(1−t). FCFF=NOPAT−reinversión. VP FCFF=FCFF×factor acumulado de descuento. ROIC terminal está en las historias; la trayectoria ROIC marginal se impone en conversión hacia terminal, **no se inventa una serie anual separada**. La capitalización I+D alimenta EBIT ajustado (no EBIT GAAP).


### Base

| FY proyectado | Crecimiento ventas | Ventas (M) | Margen EBIT | EBIT (M) | NOPAT (M) | Reinversión (M) | FCFF (M) | WACC | Factor VP | VP FCFF (M) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2027 | 11,00% | 885.175 | 14,48% | 128.208 | 96.156 | 121.712 | -25.555 | 8,18% | 0,9244 | -23.623 |
| 2028 | 10,00% | 973.693 | 15,01% | 146.155 | 109.616 | 125.295 | -15.679 | 8,18% | 0,8545 | -13.398 |
| 2029 | 9,00% | 1.061.325 | 15,27% | 162.102 | 121.577 | 127.949 | -6.372 | 8,18% | 0,7899 | -5.033 |
| 2030 | 8,50% | 1.151.538 | 15,54% | 178.912 | 134.184 | 129.548 | 4.636 | 8,18% | 0,7302 | 3.385 |
| 2031 | 8,00% | 1.243.661 | 15,80% | 196.498 | 147.374 | 129.980 | 17.394 | 8,18% | 0,6750 | 11.740 |
| 2032 | 7,50% | 1.336.935 | 15,80% | 211.236 | 158.427 | 52.019 | 106.408 | 8,34% | 0,6230 | 66.290 |
| 2033 | 7,00% | 1.430.520 | 15,80% | 226.022 | 169.517 | 45.950 | 123.567 | 8,50% | 0,5742 | 70.947 |
| 2034 | 6,00% | 1.516.352 | 15,80% | 239.584 | 179.688 | 43.423 | 136.265 | 8,67% | 0,5284 | 71.999 |
| 2035 | 5,00% | 1.592.169 | 15,80% | 251.563 | 188.672 | 45.377 | 143.295 | 8,83% | 0,4855 | 69.571 |
| 2036 | 4,50% | 1.663.817 | 15,80% | 262.883 | 197.162 | 41.948 | 155.214 | 8,99% | 0,4455 | 69.142 |

**Puente Base:** TV 2.679.909 millones; VP terminal 1.193.803 millones; VP flujos explícitos 321.021 millones; EV operativo 1.514.824 millones; equity 1.612.909 millones / 10.811 millones acciones = **149,19 USD/acción**. Celdas `Valuation output!B18:B35`.


### Conservadora

| FY proyectado | Crecimiento ventas | Ventas (M) | Margen EBIT | EBIT (M) | NOPAT (M) | Reinversión (M) | FCFF (M) | WACC | Factor VP | VP FCFF (M) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2027 | 8,00% | 861.251 | 14,48% | 124.743 | 93.557 | 115.192 | -21.635 | 8,18% | 0,9244 | -19.999 |
| 2028 | 7,00% | 921.539 | 13,49% | 124.319 | 93.239 | 113.243 | -20.004 | 8,18% | 0,8545 | -17.093 |
| 2029 | 6,50% | 981.439 | 12,99% | 127.524 | 95.643 | 110.034 | -14.391 | 8,18% | 0,7899 | -11.368 |
| 2030 | 6,00% | 1.040.325 | 12,50% | 130.007 | 97.505 | 105.533 | -8.028 | 8,18% | 0,7302 | -5.861 |
| 2031 | 5,50% | 1.097.543 | 12,00% | 131.705 | 98.779 | 106.377 | -7.598 | 8,18% | 0,6750 | -5.129 |
| 2032 | 5,00% | 1.152.420 | 12,00% | 138.290 | 103.718 | 43.479 | 60.239 | 8,34% | 0,6230 | 37.528 |
| 2033 | 4,80% | 1.207.737 | 12,00% | 144.928 | 108.696 | 40.387 | 68.310 | 8,50% | 0,5742 | 39.221 |
| 2034 | 4,50% | 1.262.085 | 12,00% | 151.450 | 113.588 | 39.902 | 73.686 | 8,67% | 0,5284 | 38.933 |
| 2035 | 4,00% | 1.312.568 | 12,00% | 157.508 | 118.131 | 41.418 | 76.713 | 8,83% | 0,4855 | 37.245 |
| 2036 | 3,80% | 1.362.446 | 12,00% | 163.493 | 122.620 | 35.995 | 86.625 | 8,99% | 0,4455 | 38.588 |

**Puente Conservadora:** TV 1.449.372 millones; VP terminal 645.643 millones; VP flujos explícitos 132.066 millones; EV operativo 777.709 millones; equity 875.794 millones / 10.811 millones acciones = **81,01 USD/acción**. Celdas `Valuation output!B69:B86`.


### Optimista

| FY proyectado | Crecimiento ventas | Ventas (M) | Margen EBIT | EBIT (M) | NOPAT (M) | Reinversión (M) | FCFF (M) | WACC | Factor VP | VP FCFF (M) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2027 | 14,00% | 909.099 | 14,48% | 131.673 | 98.755 | 107.195 | -8.440 | 8,18% | 0,9244 | -7.801 |
| 2028 | 13,00% | 1.027.282 | 16,09% | 165.293 | 123.970 | 115.056 | 8.914 | 8,18% | 0,8545 | 7.617 |
| 2029 | 12,00% | 1.150.555 | 16,89% | 194.370 | 145.777 | 111.554 | 34.224 | 8,18% | 0,7899 | 27.033 |
| 2030 | 11,50% | 1.282.869 | 17,70% | 227.027 | 170.270 | 110.438 | 59.832 | 8,18% | 0,7302 | 43.687 |
| 2031 | 10,00% | 1.411.156 | 18,50% | 261.064 | 195.798 | 107.002 | 88.795 | 8,18% | 0,6750 | 59.933 |
| 2032 | 9,00% | 1.538.160 | 18,50% | 284.560 | 213.420 | 55.374 | 158.046 | 8,34% | 0,6230 | 98.460 |
| 2033 | 8,00% | 1.661.213 | 18,50% | 307.324 | 230.493 | 50.786 | 179.708 | 8,50% | 0,5742 | 103.181 |
| 2034 | 7,00% | 1.777.498 | 18,50% | 328.837 | 246.628 | 44.861 | 201.767 | 8,67% | 0,5284 | 106.608 |
| 2035 | 6,00% | 1.884.148 | 18,50% | 348.567 | 261.425 | 47.104 | 214.322 | 8,83% | 0,4855 | 104.056 |
| 2036 | 5,00% | 1.978.355 | 18,50% | 365.996 | 274.497 | 39.190 | 235.306 | 8,99% | 0,4455 | 104.821 |

**Puente Optimista:** TV 4.195.382 millones; VP terminal 1.868.892 millones; VP flujos explícitos 647.594 millones; EV operativo 2.516.485 millones; equity 2.614.570 millones / 10.811 millones acciones = **241,84 USD/acción**. Celdas `Valuation output!B120:B137`.


### Disrupción

| FY proyectado | Crecimiento ventas | Ventas (M) | Margen EBIT | EBIT (M) | NOPAT (M) | Reinversión (M) | FCFF (M) | WACC | Factor VP | VP FCFF (M) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2027 | 3,00% | 821.379 | 14,48% | 118.968 | 89.226 | 23.937 | 65.289 | 8,18% | 0,9244 | 60.352 |
| 2028 | 2,00% | 837.806 | 12,09% | 101.294 | 75.970 | 0 | 75.970 | 8,18% | 0,8545 | 64.916 |
| 2029 | 1,00% | 846.184 | 10,89% | 92.180 | 69.135 | 0 | 69.135 | 8,18% | 0,7899 | 54.609 |
| 2030 | 0,00% | 846.184 | 9,70% | 82.053 | 61.540 | 23.935 | 37.605 | 8,18% | 0,7302 | 27.457 |
| 2031 | -1,00% | 837.722 | 8,50% | 71.206 | 53.405 | 48.349 | 5.056 | 8,18% | 0,6750 | 3.413 |
| 2032 | 1,00% | 846.100 | 8,50% | 71.918 | 53.939 | 20.548 | 33.391 | 8,34% | 0,6230 | 20.802 |
| 2033 | 2,00% | 863.022 | 8,50% | 73.357 | 55.018 | 25.274 | 29.743 | 8,50% | 0,5742 | 17.077 |
| 2034 | 2,50% | 884.597 | 8,50% | 75.191 | 56.393 | 26.032 | 30.361 | 8,67% | 0,5284 | 16.042 |
| 2035 | 3,00% | 911.135 | 8,50% | 77.446 | 58.085 | 26.813 | 31.271 | 8,83% | 0,4855 | 15.183 |
| 2036 | 3,00% | 938.469 | 8,50% | 79.770 | 59.827 | 22.903 | 36.924 | 8,99% | 0,4455 | 16.448 |

**Puente Disrupción:** TV 629.924 millones; VP terminal 280.608 millones; VP flujos explícitos 296.299 millones; EV operativo 576.908 millones; equity 674.993 millones / 10.811 millones acciones = **62,44 USD/acción**. Celdas `Valuation output!B173:B190`.



## 8. Valor terminal, puente EV → equity y precio Base

Modelo FCFF de diez años: `TV10 = FCFF_{11}/(WACC_terminal - g_terminal)` con la convergencia de reinversión y ROIC terminal de la hoja, sin asumir que el FCFF del año diez es flujo perpetuo sin reinversión. Para el Base, FCFF terminal ~133727 millones, TV ~2679909 millones y VP TV ~1193803 millones. **VP flujos explícitos ≈321021 millones**, **EV operativo ≈1514824 millones**, puente:
`1514824 - 304841 (deuda) - 0 (minoritarios) + 114226 (cash) + 288700 (no operativos) - 0 (opciones activas) = 1612909 millones`. Dividido por **10811 millones de acciones** ⇒ **149,19148576 USD/acción**. MOS35%=0,65×149,19148576 = **96,97446574**. En otros escenarios se conserva el mismo puente patrimonial, ajustando EV operativo; revisar supuestos de valor recuperable de activos privados por separado.

El VP terminal supone aproximadamente **78,8%** del EV operativo Base, inferior al aviso 85% de la hoja pero económicamente grande. Sus retornos dependen de que el ROIC terminal11,5% se sostenga sobre WACC terminal8,99%. Rf5,29% > g4% cumple restricción nominal ordinaria. **No se trata de certificación de estabilidad de g**.

## 9. Escenarios, probabilidades y diagnóstico de ciclos

La previa y los pesos R5 observables son Base45%, Conservadora22,5%, Optimista22,5%, Disrupción10%, sin evidencia de ajuste posterior cuantificado. Las tres historias ordinarias se renormalizan excluyendo 10% Disrupción: `(0,45×149,1915 + 0,225×81,0095 + 0,225×241,8435)/0,90 ≈ 155,3090 USD/acción`. Disrupción vale62,4357 separadamente y **no entra en el precio Base** ni en MOS35%. Escenarios corresponden a etapas de demanda/capacidad AWS, monetización de ads/retail, ciclo de inflación/moneda/crédito y cambio de percepción sobre IA; no son probabilidades inferidas de cotización.

Madurez parcial de retail y expansión AWS/IA intensiva en CAPEX: baja de ROIC reciente, FCF negativo y riesgo de desfase de utilización. Sensibilidad al capital: alterar solo S/C 1–5 a 0,50/0,55/0,72/0,90 dio **128,72/134,81/149,19/158,50** por acción en pruebas anteriores documentadas, con driver restaurado a 0,72. **La guía cualitativa de mayor CAPEX 2027 hace a 0,72 un supuesto económico por validar**, aunque el cálculo sea reproducible.

## 10. Cinco múltiplos prioritarios y valores presentes

| Método | Proyección FY+1/FY+2/FY+3 | VP FY+3 Base (I) | Promedio VP 1–3 Base (J) | Peso plantilla | Estado |
|---|---|---:|---:|---:|---|
| EV/EBITDA | 358,59 / 403,24 / 446,02 | **349,74** | **341,10** | 10% | Calculado, precio relativo secundario |
| EV/FCFF | N/D: FCFF Base FY+3 negativo | N/D | N/D | 15% | Sin denominador económico adecuado |
| P/E | N/D: beneficios GAAP no recurrentes | N/D | N/D | 5% | Normalización de NI/ganancias financieras pendiente |
| P/FCFE | N/D: flujos y deuda volátiles | N/D | N/D | 5% | FCFE per-share FY+3 no calibrado |
| P/OCF | 184,56 / 226,12 / 266,21 | **208,75** | **190,40** | 5% | Calculado, no deduce CAPEX |

Los precios FY+1/2/3 son `Descuento de múltiplos!D20:F24`; los VP por cada año son G:I; el **promedio de VP 1–3** que muestra el `Resumen de Valoración!D42,D46` está en `Descuento de múltiplos!J20,J24`. La matriz de sensibilidades en cambio tiene centro **VP3, columna I**, no ese promedio. Por tanto, **349,74 vs 341,10** y **208,75 vs 190,40** son diferencias legítimas de métrica temporal, no errores de fórmula. No mezclar resultados históricos antiguos y el cuadro actual.

En `Resumen de Valoración` se mantienen pesos positivos de métodos sin denominador; la valoración ponderada compuesta **queda vacía correctamente** por política de no inventar. No sustituir `N/D` por cero ni redistribuir pesos sin decisión validada del Método A-1.2. P/V y P/BV secundarios opcionales no contribuyen a precio final de esta revisión.

## 11. Tres sensibilidades DCF Base 5×5, sensibilidades por múltiplo e inverso

La hoja `Sensibilidad DCF` reproduce cada escenario Base **con otros dos parámetros, manteniendo el resto según fórmulas**. Cada matriz 5×5 vale USD/acción. El centro de las tres es **149,19148576**, y la hoja informa `OK` en B12, B23 y B34.

**WACC inicial × g estable; 5×5, USD/acción**

| Eje vertical / horizontal | 17.593,55% | 18.343,29% | 19.276,73% | 20.472,86% | 22.063,46% |
|---|---:|---:|---:|---:|---:|
| 7,68% | 157,10 | 162,25 | 168,51 | 176,31 | 186,30 |
| 8,18% | 141,48 | 145,00 | 149,19 | 154,29 | 160,63 |
| 8,68% | 128,34 | 130,70 | 133,45 | 136,74 | 140,72 |
| 9,18% | 117,15 | 118,66 | 120,40 | 122,44 | 124,86 |
| N/D% |  |

**ROIC terminal × g estable; 5×5, USD/acción**

| Eje vertical / horizontal | 13.810,74% | 14.062,12% | 14.358,26% | 14.714,05% | 15.151,85% |
|---|---:|---:|---:|---:|---:|
| 11,00% | 139,87 | 142,91 | 146,51 | 150,88 | 156,28 |
| 11,50% | 141,48 | 145,00 | 149,19 | 154,29 | 160,63 |
| 12,00% | 142,96 | 146,91 | 151,65 | 157,41 | 164,61 |
| 12,50% | 144,31 | 148,67 | 153,90 | 160,29 | 168,28 |
| N/D% |  |

**Crecimiento explícito años 1–5 × margen EBIT objetivo; 5×5, USD/acción**

| Eje vertical / horizontal | 10.124,73% | 11.913,13% | 13.701,53% | 15.489,94% | 17.278,34% |
|---|---:|---:|---:|---:|---:|
| 7,29% | 102,56 | 122,75 | 142,93 | 163,11 | 183,30 |
| 9,29% | 103,71 | 126,45 | 149,19 | 171,93 | 194,68 |
| 11,29% | 104,66 | 130,25 | 155,84 | 181,43 | 207,02 |
| 13,29% | 105,40 | 134,15 | 162,90 | 191,66 | 220,41 |
| N/D% |  |



En la hoja `Sensibilidad por múltiplo` hay matrices 5×5 para métodos aplicables en **historia Base solamente**, con ejes de múltiplo real y fundamental proyectado FY+3. El centro de EV/EBITDA corresponde VP3 **349,7436**, no promedio de VP3 años **341,1023**; P/OCF VP3 **208,7479** vs promedio **190,4043**. En ambos casos la igualdad del centro con `Descuento de múltiplos!I20/I24` es verificable y se preserva.

**EV/EBITDA Base (ancla FY+3)** · valor presente FY+3, no promedio de los tres vencimientos.

| Múltiplo / fundamento (USD millones) | 204.697 | 230.284 | 255.871 | 281.458 | 307.045 |
|---|---:|---:|---:|---:|---:|
| 14,77× | 226,40 | 253,81 | 281,22 | 308,63 | 336,04 |
| 16,62× | 253,81 | 284,64 | 315,48 | 346,32 | 377,15 |
| 18,46× | 281,22 | 315,48 | 349,74 | 384,01 | 418,27 |
| 20,31× | 308,63 | 346,32 | 384,01 | 421,70 | 459,38 |
| 22,15× | 336,04 | 377,15 | 418,27 | 459,38 | 500,50 |

**P/OCF Base (ancla FY+3)** · valor presente FY+3, no promedio de los tres vencimientos.

| Múltiplo / fundamento (USD millones) | 117.383 | 132.056 | 146.729 | 161.402 | 176.075 |
|---|---:|---:|---:|---:|---:|
| 15,69× | 133,60 | 150,30 | 167,00 | 183,70 | 200,40 |
| 17,65× | 150,30 | 169,09 | 187,87 | 206,66 | 225,45 |
| 19,61× | 167,00 | 187,87 | 208,75 | 229,62 | 250,50 |
| 21,58× | 183,70 | 206,66 | 229,62 | 252,58 | 275,55 |
| 23,54× | 200,40 | 225,45 | 250,50 | 275,55 | 300,60 |



EV/FCFF, P/E y P/FCFE: matrices N/D por falta de fundamento/denominador, no fallas visuales a ocultar. Las anclas LTM secundarias requieren denominadores de igual corte. **DCF inverso: N/D (no hay ejecución documentada verificable de R5 con precio 240,35 en esta entrega)**. No se calcula por intuición a partir de un premium.

## 12. Fórmulas, trazabilidad, CI y limitaciones

**Identidad matemática:** `Revenues_t = Revenues_{t-1}(1+g_t)`; `NOPAT_t = EBIT_t(1-t_t)`; `Reinvestment_t ≈ ΔRevenues/(S/C_t)` conforme al lag/celda nativa; `FCFF_t = NOPAT_t − Reinvestment_t`; `PV(FCFF_t) = FCFF_t × DF_t`; `EV = ΣPV(FCFF) + PV(TV)`; `V_equity = EV − debt − minority + cash + nonop − option_value`; `V_share=V_equity/shares`. Un error en términos de gasto fiscal firmado no autoriza aplicar el impuesto dos veces.

**Pruebas verificadas hasta ahora:** conciliaciones históricas 88/88 del expediente F2; scripts `inputs_completos=0 faltantes`, `auditar_ceros_materiales=0 alertas`, `candados=15/15`, `diff_formulas_plantilla=0 reemplazos de fórmula a constante/vacío`; 4 DCF previamente reproducidos independientemente con diferencia máxima ~5,7e−14 USD/acción. Las protecciones fiscales históricas y rating sintético se encuentran en la hoja actual R5. El nuevo perfil SEC de signo/split/fecha y el validador de vacíos legítimos requieren confirmar su **ejecución CI auténtica** para promoverlos.

**Bloqueos/pre-publicación:** auditoría SEC normalizada, casos secundarios historia, compatibilidad `controles_todas.sh` con candidate `sheet_id`, runner único que verifique hoja↔JSON↔app, cálculo inverso y observaciones sobre CAPEX FY2027, 0,72 S/C, deuda mercado y activos privados. Nivel 2 y Nivel 1 son **documentación candidata**, no dictamen de un LLM externo ni publicación `EN_REVISION`. La auditoría económica interna del constructor se documenta separadamente; la auditoría independiente será posterior a la revisión visual del usuario.

**Fuentes primarias:** [10-Q 2026Q3](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm), [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm), [10-K FY2022](https://www.sec.gov/Archives/edgar/data/1018724/000101872423000004/amzn-20221231.htm), [expediente F1/F2/F3](FASE_3_REVISION_ECONOMICA_20261103.md). Todos los cálculos de los cuatro escenarios y tablas 5×5 se tomaron de la misma hoja `sheet_id=199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I` sin reescritura.
