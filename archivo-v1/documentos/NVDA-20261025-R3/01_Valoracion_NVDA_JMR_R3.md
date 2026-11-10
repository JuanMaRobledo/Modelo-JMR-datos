# Valoración JMR — NVIDIA (NVDA)

**DCF Base: USD 381,79 por acción. Precio con MOS de 35%: USD 248,16.**

Emisión: 24-oct-2026 · Corte: 23-oct-2026 · Revisión: NVDA-20261025-R3. Precio de referencia: USD 210,96 al cierre del 23-oct-2026. Estados en USD millones; acciones en millones; valores por acción en USD. Separadores de las tablas: coma de miles y punto decimal. [Hoja nativa con fórmulas](https://docs.google.com/spreadsheets/d/1gbtwORZsvjhZNCV8xlNDloHYEeE09cEbXmPZOoLJ8gY/edit).

## 1. Empresa, método y alcance

NVIDIA Corporation, NVDA, Nasdaq. Empresa operativa: FCFF descontado a WACC es el método principal. La expansión de computación acelerada y el ecosistema de software sostienen la historia; competencia, sustitución y retorno del cliente limitan su duración. Los múltiplos son un contraste secundario. La revisión R2 se publica con análisis y auditoría separados, con las reservas documentadas.

## 2. Histórico y punto de partida

| FY / período | Ingresos | EBIT | Utilidad neta | CFO | CAPEX pagado | SBC | FCF CFO−CAPEX |
|---|---|---|---|---|---|---|---|
| FY2017 | 6,910.00 | 1,934.00 | 1,666.00 | 1,672.00 | 176.00 | 247.00 | 1,496.00 |
| FY2018 | 9,714.00 | 3,210.00 | 3,047.00 | 3,502.00 | 593.00 | 391.00 | 2,909.00 |
| FY2019 | 11,716.00 | 3,804.00 | 4,141.00 | 3,743.00 | 600.00 | 557.00 | 3,143.00 |
| FY2020 | 10,918.00 | 2,846.00 | 2,796.00 | 4,761.00 | 489.00 | 844.00 | 4,272.00 |
| FY2021 | 16,675.00 | 4,532.00 | 4,332.00 | 5,822.00 | 1,128.00 | 1,397.00 | 4,694.00 |
| FY2022 | 26,914.00 | 10,041.00 | 9,752.00 | 9,108.00 | 976.00 | 2,004.00 | 8,132.00 |
| FY2023 | 26,974.00 | 4,224.00 | 4,368.00 | 5,641.00 | 1,833.00 | 2,709.00 | 3,808.00 |
| FY2024 | 60,922.00 | 32,972.00 | 29,760.00 | 28,090.00 | 1,069.00 | 3,549.00 | 27,021.00 |
| FY2025 | 130,497.00 | 81,453.00 | 72,880.00 | 64,089.00 | 3,236.00 | 4,737.00 | 60,853.00 |
| FY2026 | 215,938.00 | 130,387.00 | 120,067.00 | 102,718.00 | 6,042.00 | 6,386.00 | 96,676.00 |
| LTM | 302,970.00 | 197,579.00 | 192,880.00 | 134,360.00 | 7,354.00 | 7,241.00 | 127,006.00 |

LTM = FY2026 + H1 FY2027 − H1 FY2026. Balance actual al 26-jul-2026. Los stocks no se suman como flujos. En FY2017 se separan 31 de patrimonio temporal y 796 de deuda convertible corriente, según el comparativo del 10-K FY2018. La utilidad neta LTM incorpora ganancias de inversiones que se eliminan de los beneficios normalizados para múltiplos.

## 3. Datos y fuentes materiales

| Dato | Valor | Período / tipo | Documento y fecha | Hoja / referencia | Verificación |
|---|---|---|---|---|---|
| Ingresos / EBIT | 302.970 / 197.579 | LTM / observado | 10-Q 26-ago + 10-K 25-feb-2026 | Income Statement!L3/L12 | Conciliado |
| CFO / CAPEX | 134.360 / 7.354 | LTM / observado | Mismos estados | Cash Flow Statement; data.json | FCF 127.006 |
| Deuda y leases / activos líquidos | 38.860 / 99.369 | 26-jul-2026 / observado | 10-Q, notas | Input sheet!B16/B19 | Sin duplicaciones identificadas |
| Acciones del puente | 24.268 millones | Portada 21-ago + RSU julio / modelo | 10-Q y nota SBC | Input sheet!B22 | Básicas + concesiones conocidas |
| Precio | 210,96 USD | 23-oct-2026 / observado | Histórico Yahoo, consulta 23-oct | assumptions.json | Fecha congelada |
| Rf / ERP madura | 5,29% / 3,69748% | 1-oct-2026 / fuente económica | ERPOct26 B10/C45 | Input sheet!B35; Country ERP | Mismo archivo |
| Tax inicial / marginal | 17% / 25,37% | Normalización / modelo | Guía 16–18%; archivo industria | Input sheet!B90/B25 | Juicios separados de realizados |

Fuentes materiales: [10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm), [10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm), 8-K sobre adquisición anunciada, archivos de Damodaran y cotizaciones fechadas. La procedencia por concepto y período está en `fuentes/provenance.json`; las normalizaciones, en `fuentes/normalization-log.json`. Se distinguen datos reportados, cálculos y juicios. Los datos no disponibles no se rellenan con cero.

## 4. Ajustes económicos y dilución

I+D LTM de 23.592; cohortes previas 15.384, 10.569 y 7.812; vida útil supuesta tres años. Amortización 11.255; activo de I+D 37.371; ajuste de EBIT 12.337. El convertidor de arrendamientos usa deuda ya reconocida de 5.494 y ajuste financiero de EBIT de 323,60, sin añadir de nuevo el pasivo.

El puente divide entre 24.100 millones de acciones básicas de portada más 168 millones de RSU/PSU conocidas: 24.268 millones. El promedio diluido LTM 24.397,5 millones se conserva separado. No se utiliza Black–Scholes para inventar un costo de opciones sobre RSU. La auditoría explicita la limitación del registro completo de concesiones y prueba redondeo y dilución adicional.

## 5. Crecimiento por historias

| Historia / segmento | Año 1 | Año 2 | Año 3 | Año 4 | Año 5 |
|---|---|---|---|---|---|
| Base · Compute & Networking | 75.00% | 50.00% | 32.00% | 23.00% | 17.00% |
| Base · Graphics | 20.00% | 15.00% | 12.00% | 10.00% | 8.00% |
| Conservadora · Compute & Networking | 50.00% | 25.00% | 15.00% | 10.00% | 8.00% |
| Conservadora · Graphics | 12.00% | 8.00% | 6.00% | 5.00% | 4.00% |
| Disrupción · Compute & Networking | 20.00% | -10.00% | -10.00% | 0.00% | 2.00% |
| Disrupción · Graphics | 5.00% | -5.00% | -5.00% | 0.00% | 2.00% |
| Optimista · Compute & Networking | 90.00% | 65.00% | 45.00% | 32.00% | 23.00% |
| Optimista · Graphics | 30.00% | 20.00% | 15.00% | 12.00% | 10.00% |

La agregación usa los segmentos LTM: Compute & Networking 275.409 y Graphics 27.561 millones. La Base produce crecimiento agregado de 70,00%, 47,75%, 31,00%, 22,44% y 16,65%; CAGR de cinco años 36,28% y ventas año 5 de 1.423.928,64 millones. Años 6–10 convergen desde el crecimiento del año 5 hasta el g estable. No se anualiza un solo trimestre ni se confunde LTM con FY2027 completo.

## 6. Márgenes, impuestos y cuatro historias

| Historia | Probabilidad | CAGR1–5 | GAAP estable / económico objetivo | S/C1–5 | ROIC terminal | g terminal | DCF USD/acción |
|---|---|---|---|---|---|---|---|
| Base | 40.00% | 36.28% | 58.00% / 58.69% | 2.00 | 27.23% | 4.00% | 381.79 |
| Conservadora | 22.50% | 19.69% | 48.00% / 48.69% | 1.65 | 18.11% | 4.00% | 149.58 |
| Disrupción | 15.00% | -0.22% | 25.00% / 25.41% | 1.30 | 8.99% | 2.00% | 37.05 |
| Optimista | 22.50% | 47.20% | 62.00% / 62.69% | 2.40 | 27.23% | 4.00% | 639.44 |

La escala, el software y el costo de cambiar plataformas sostienen rentas; concentración, ASIC y costos de sistemas completos pueden erosionarlas. R1 trasladaba a la madurez un ajuste histórico de I+D y leases de4,18 puntos sobre ventas. Esa extrapolación no se conserva: R2 utiliza un puente prospectivo por cohortes, manteniendo el calendario original de diez años y su transición de margen.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Margen económico objetivo / referencia GAAP estable | Medias GAAP58,97/45,98/37,66%; LTM65,21% | 58,6906% económico año5;58% GAAP estable; Escenarios!D5 / Puente I+D | Pares SEC con mezcla distinta; no comparar GAAP con económico | I+D recurrente mantiene plataforma; amortización de3cohortes | Vida3años e I+D/ventas7,79% son hipótesis; obsolescencia y competencia pueden cambiar ambas | −5pp objetivo: USD350.13 |

Se parte de gasto23.592 y cohortes previas15.384/10.569/7.812; amortización11.255 y activo37.371. Se proyecta I+D con intensidad7,7869% de ventas y amortización lineal de tres cohortes previas. Con crecimiento estable4%, el aporte neto de I+D es0,5838puntos; leases añaden0,1068. El margen económico estable es58%+0,5838+0,1068=58,6906%. Esto reduce la distorsión de perpetuar el ajuste del período de expansión.

El margen económico inicial común es69,1872%; la plantilla lo lleva al objetivo en año5 con su denominador cinco. En cada año GAAP=económico−I+D neta/ventas−ajuste leases. La Base implica aproximadamente56,23% GAAP en año5, con recuperación posterior conforme madura la amortización;58% describe el estado estable y no una celda GAAP forzada en año5. Las cuatro historias tienen el mismo margen económico inicial por diseño de la plantilla; sus cohortes e implicaciones GAAP posteriores difieren.

En52 períodos de conciliación (cuatro historias por13años de diagnóstico) se comprueba Δactivo I+D=gasto−amortización. El DCF utiliza diez años; los tres adicionales sirven para observar la aproximación a estabilidad. La prueba alternativa con calendario DCF de13años vale384,50; no es la Base oficial381,79 y su diferencia aproximada0,71% es un contraste metodológico. No se añadió un descuento adicional por esa diferencia. La capitalización no crea caja: la inversión se paga y su costo se refleja en amortización y reinversión.

Impuesto inicial normalizado17% durante cinco años, dentro de la guía16–18%, con convergencia a25,37% en los años6–10.

## 7. Reinversión y retornos


El modelo fabless transfiere parte importante de la inversión fabril a proveedores, pero no elimina la necesidad de I+D, inventarios, anticipos, financiación y compromisos de capacidad. El capital invertido ajustado inicial es 154.689 millones, que incluye 37.371 de activo de I+D. Ventas/capital actual es 1,96 veces; la Base usa 2 veces en años 1–5. En años 6–10 disminuye hasta 0,5977 veces para sustentar el retorno marginal estable con la convención de capital de apertura de la plantilla.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| S/C inicial; ROIC marginal estable | LTM S/C 1,96; serie ROIC homogénea 3/5/10 N/D | 2,00 años 1–5; 27,22697% terminal; Input / Escenarios | Damodaran US semiconductores ajustado I+D/leases, 5-ene-2026 | Modelo fabless y reutilización de software; proveedores amplían capacidad | Anticipos, inventarios y nube elevan capital; retornos por nueva inversión disminuyen | S/C −20%: USD 375,82; industria global: USD 366,10 |

La reinversión explícita es Δventas/Sales-to-Capital, sin sumar nuevamente todo el CAPEX. Ante caídas de ventas no se reconoce una liberación automática de capital. El ROIC medio explícito sobre capital acumulado y el retorno marginal terminal son métricas distintas: el 27,23% terminal no implica que el retorno medio del año 10 se reduzca instantáneamente a esa cifra. No se usa una recompra para crear valor por acción sin su correspondiente desembolso.


El cociente tardío0,597701 se deriva de ROIC/[margen económico×(1−tax)×(1+g)], con la convención de capital de apertura. No representa el Sales-to-Capital observado de la industria. La reinversión total Δventas/S2C ya incorpora inversión neta en I+D: el puente resta esta última para identificar el otro capital; no vuelve a sumarla. Ante contracción puede aparecer depreciación neta o reducción del otro capital, un límite económico a vigilar. El tratamiento no usa un CAPEX ficticio para cuadrar caja.

El ROIC actual ajustado y normalizado a17% es112,81% sobre cierre,149,36% sobre promedio y220,96% sobre apertura; esos denominadores cambian la interpretación. El marginal estable27,23% no constituye una caída instantánea del retorno medio del stock. La falta de cohortes homogéneas para cada ejercicio antiguo limita la serie3/5/10años: se conserva N/D y no se rellena con el retorno actual.

## 8. Costo de capital

Rf 5,29% y ERP madura 3,697480421%, del archivo octubre 2026 con corte 1-oct. CRP incremental ponderada por geografía LTM 0,403090517%; los datos de país e industria proceden de enero 2026. La clasificación por sede del cliente limita la interpretación geográfica.

Beta sectorial corregida por caja 1,5046492755, apalancada 1,5127415454. Submétodo Detailed: Ke 11,493104%, WACC inicial 11,442323%, WACC estable 8,987480%. Equity de mercado 5.119.577,28 millones; bonos 31.400; leases 5.494. Kd de 5,89% es juicio explícito Rf + 60 pb. Campos de rating/vencimiento heredados no se presentan como un rating actual certificado. La beta alternativa por regresión 1,860385 produce WACC 12,857661% y DCF USD 352,55.

## 9. Valor terminal y DCF completos

g estable Base/Conservadora/Optimista4%, Disrupción2%; inferior al Rf y al WACC estable. ROIC marginal Base27,23%; global como contraste20,54%. La alternativa global daUSD366.10. El VP terminal representa67.39% del valor operativo Base. Cada historia conserva impuestos, reinversión y transición propios.

### Base

| Año | Crecimiento | Ingresos | Margenajustado | NOPAT | S/C | Reinversión | FCFF | WACC | VP FCFF |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 70.00% | 515,038.95 | 69.19% | 295,762.90 | 2.00 | 106,034.48 | 189,728.43 | 11.44% | 170,248.09 |
| 2 | 47.75% | 760,982.80 | 64.99% | 410,477.81 | 2.00 | 122,971.93 | 287,505.88 | 11.44% | 231,497.56 |
| 3 | 31.00% | 996,890.47 | 62.89% | 520,357.41 | 2.00 | 117,953.83 | 402,403.58 | 11.44% | 290,744.40 |
| 4 | 22.44% | 1,220,637.50 | 60.79% | 615,880.23 | 2.00 | 111,873.52 | 504,006.71 | 11.44% | 326,765.12 |
| 5 | 16.65% | 1,423,928.64 | 58.69% | 693,641.06 | 2.00 | 101,645.57 | 591,995.49 | 11.44% | 344,403.55 |
| 6 | 14.12% | 1,625,038.70 | 58.69% | 775,642.50 | 1.72 | 116,955.71 | 658,686.78 | 10.95% | 345,378.71 |
| 7 | 11.59% | 1,813,424.61 | 58.69% | 847,743.89 | 1.44 | 130,907.15 | 716,836.74 | 10.46% | 340,275.21 |
| 8 | 9.06% | 1,977,753.57 | 58.69% | 905,133.72 | 1.16 | 141,831.55 | 763,302.17 | 9.97% | 329,484.23 |
| 9 | 6.53% | 2,106,918.70 | 58.69% | 943,547.04 | 0.88 | 147,085.96 | 796,461.08 | 9.48% | 314,032.11 |
| 10 | 4.00% | 2,191,195.45 | 58.69% | 959,760.86 | 0.60 | 141,001.51 | 818,759.35 | 8.99% | 296,202.80 |

Terminal: | Ingresos11 | NOPAT11 | Reinversión11 | FCFF11 | VPterminal | Valor/acción |
|---|---|---|---|---|---|
| 2,278,843.27 | 998,151.29 | 146,641.57 | 851,509.72 | 6,176,483.58 | 381.79 |

### Conservadora

| Año | Crecimiento | Ingresos | Margenajustado | NOPAT | S/C | Reinversión | FCFF | WACC | VP FCFF |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 46.54% | 443,981.82 | 69.19% | 254,958.10 | 1.65 | 85,461.71 | 169,496.39 | 11.44% | 152,093.37 |
| 2 | 23.82% | 549,729.66 | 60.99% | 278,275.81 | 1.65 | 64,089.60 | 214,186.21 | 11.44% | 172,461.12 |
| 3 | 14.45% | 629,188.71 | 56.89% | 297,090.65 | 1.65 | 48,157.00 | 248,933.65 | 11.44% | 179,859.40 |
| 4 | 9.72% | 690,340.68 | 52.79% | 302,477.06 | 1.65 | 37,061.80 | 265,415.26 | 11.44% | 172,077.96 |
| 5 | 7.79% | 744,083.73 | 48.69% | 300,707.97 | 1.65 | 32,571.55 | 268,136.42 | 11.44% | 155,992.97 |
| 6 | 7.03% | 796,377.97 | 48.69% | 315,350.62 | 1.42 | 36,935.46 | 278,415.16 | 10.95% | 145,985.42 |
| 7 | 6.27% | 846,318.85 | 48.69% | 328,228.08 | 1.18 | 42,263.51 | 285,964.57 | 10.46% | 135,744.52 |
| 8 | 5.51% | 892,984.89 | 48.69% | 339,048.04 | 0.95 | 49,252.67 | 289,795.37 | 9.97% | 125,092.01 |
| 9 | 4.76% | 935,464.19 | 48.69% | 347,551.77 | 0.71 | 59,552.38 | 287,999.40 | 9.48% | 113,553.64 |
| 10 | 4.00% | 972,882.76 | 48.69% | 353,524.07 | 0.48 | 78,095.70 | 275,428.37 | 8.99% | 99,641.80 |

Terminal: | Ingresos11 | NOPAT11 | Reinversión11 | FCFF11 | VPterminal | Valor/acción |
|---|---|---|---|---|---|
| 1,011,798.07 | 367,665.03 | 81,219.53 | 286,445.51 | 2,077,751.91 | 149.58 |

### Disrupción

| Año | Crecimiento | Ingresos | Margenajustado | NOPAT | S/C | Reinversión | FCFF | WACC | VP FCFF |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 18.64% | 359,429.85 | 69.19% | 206,403.84 | 1.30 | 43,430.65 | 162,973.18 | 11.44% | 146,239.94 |
| 2 | -9.60% | 324,933.82 | 51.68% | 139,366.49 | 1.30 | 0.00 | 139,366.49 | 11.44% | 112,216.85 |
| 3 | -9.58% | 293,815.04 | 42.92% | 104,666.98 | 1.30 | 0.00 | 104,666.98 | 11.44% | 75,623.93 |
| 4 | 0.00% | 293,815.04 | 34.16% | 83,314.54 | 1.30 | 0.00 | 83,314.54 | 11.44% | 54,015.72 |
| 5 | 2.00% | 299,691.34 | 25.41% | 63,201.34 | 1.30 | 4,520.23 | 58,681.11 | 11.44% | 34,138.74 |
| 6 | 2.00% | 305,685.17 | 25.41% | 63,165.18 | 1.13 | 5,290.53 | 57,874.65 | 10.95% | 30,346.25 |
| 7 | 2.00% | 311,798.87 | 25.41% | 63,102.30 | 0.97 | 6,329.73 | 56,772.57 | 10.46% | 26,949.37 |
| 8 | 2.00% | 318,034.85 | 25.41% | 63,011.64 | 0.80 | 7,806.63 | 55,205.01 | 9.97% | 23,829.59 |
| 9 | 2.00% | 324,395.55 | 25.41% | 62,892.11 | 0.63 | 10,068.52 | 52,823.59 | 9.48% | 20,827.51 |
| 10 | 2.00% | 330,883.46 | 25.41% | 62,742.60 | 0.46 | 13,962.22 | 48,780.37 | 8.99% | 17,647.29 |

Terminal: | Ingresos11 | NOPAT11 | Reinversión11 | FCFF11 | VPterminal | Valor/acción |
|---|---|---|---|---|---|
| 337,501.13 | 63,997.45 | 14,241.47 | 49,755.98 | 257,606.95 | 37.05 |

### Optimista

| Año | Crecimiento | Ingresos | Margenajustado | NOPAT | S/C | Reinversión | FCFF | WACC | VP FCFF |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 84.54% | 559,106.40 | 69.19% | 321,068.79 | 2.40 | 106,723.50 | 214,345.29 | 11.44% | 192,337.42 |
| 2 | 62.12% | 906,402.38 | 66.59% | 500,954.85 | 2.40 | 144,706.66 | 356,248.19 | 11.44% | 286,848.35 |
| 3 | 43.58% | 1,301,384.90 | 65.29% | 705,221.16 | 2.40 | 164,576.05 | 540,645.11 | 11.44% | 390,626.60 |
| 4 | 31.24% | 1,707,939.18 | 63.99% | 907,114.18 | 2.40 | 169,397.62 | 737,716.57 | 11.44% | 478,287.37 |
| 5 | 22.58% | 2,093,566.08 | 62.69% | 1,089,349.21 | 2.40 | 160,677.88 | 928,671.33 | 11.44% | 540,270.51 |
| 6 | 18.86% | 2,488,471.12 | 62.69% | 1,268,715.87 | 2.03 | 194,351.36 | 1,074,364.51 | 10.95% | 563,336.99 |
| 7 | 15.15% | 2,865,402.20 | 62.69% | 1,430,818.78 | 1.66 | 226,544.80 | 1,204,273.98 | 10.46% | 571,656.78 |
| 8 | 11.43% | 3,192,957.68 | 62.69% | 1,560,873.16 | 1.30 | 252,794.41 | 1,308,078.75 | 9.97% | 564,640.50 |
| 9 | 7.72% | 3,439,316.67 | 62.69% | 1,645,211.84 | 0.93 | 265,572.75 | 1,379,639.09 | 9.48% | 543,970.05 |
| 10 | 4.00% | 3,576,889.33 | 62.69% | 1,673,482.99 | 0.56 | 245,856.69 | 1,427,626.30 | 8.99% | 516,472.76 |

Terminal: | Ingresos11 | NOPAT11 | Reinversión11 | FCFF11 | VPterminal | Valor/acción |
|---|---|---|---|---|---|
| 3,719,964.91 | 1,740,422.31 | 255,690.96 | 1,484,731.35 | 10,769,599.65 | 639.44 |

## 10. Puente a equity, promedio y margen de seguridad

| Componente Base | USD millones |
|---|---|
| VP operativo | 9,165,515.35 |
| Caja y valores líquidos | 99,369.00 |
| Inversiones privadas | 51,157.00 |
| Compra anunciada Hugging Face | -11,900.00 |
| Deuda y leases | -38,860.00 |
| Equity | 9,265,281.35 |

Las inversiones cotizadas42.783 ya están entre los líquidos. La compra anunciada se deduce una sola vez, sin sinergias añadidas. Puente neto+99.766;24.268millones de acciones. DCF BaseUSD381.79; promedio ordinario condicionado sobre85%USD388.52; Disrupción aparte. MOS35%USD248.16. El precio fechado210,96 está44.74% por debajo de Base; esa diferencia depende de las hipótesis.

## 11. Siete métodos por múltiplos


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


## 12. Sensibilidades e inverso

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

## 13. Verificación y limitaciones

Pasaron19/19controles propios,18/18estados nativos, cero entradas esenciales faltantes y las19pruebas CI del motor. Las ocho matrices DCF y63precios relativos se reproducen con precisión completa. La puerta central se ejecuta con scripts vigentes fijados por commit y captura real de valores/fórmulas; el log adjunto conserva los resultados y las limitaciones de cobertura.

La hoja nativa es referencia. El XLSX de exportación puede conservar cachés redondeadas y recalcular distinto en motores ajenos. No se sustituyen fórmulas por cifras del informe. No se certifica el historial de revisiones de Drive ni la comparación mayoritaria con hojas no capturadas. Las salvedades económicas y documentales se detallan en la auditoría separada.

## 14. Conclusión y estado

Adopto margen económico normalizado58,6906% y calendario original de diez años, con ROIC estable27,23%, S/C inicial2y crecimiento Base de36,28% compuesto a cinco años. DCF BaseUSD381.79, ConservadoraUSD149.58 y DisrupciónUSD37.05. La tesis sigue siendo Exigente. Valoración, artículo completo de18secciones y auditoría de18secciones se publican separados bajo la misma revisión; las versiones previas se conservan archivadas.


## Anexo R2. Normalización económica, capital e I+D

La escala, el software y el costo de cambiar plataformas sostienen rentas; concentración, ASIC y costos de sistemas completos pueden erosionarlas. R1 trasladaba a la madurez un ajuste histórico de I+D y leases de4,18 puntos sobre ventas. Esa extrapolación no se conserva: R2 utiliza un puente prospectivo por cohortes, manteniendo el calendario original de diez años y su transición de margen.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Margen económico objetivo / referencia GAAP estable | Medias GAAP58,97/45,98/37,66%; LTM65,21% | 58,6906% económico año5;58% GAAP estable; Escenarios!D5 / Puente I+D | Pares SEC con mezcla distinta; no comparar GAAP con económico | I+D recurrente mantiene plataforma; amortización de3cohortes | Vida3años e I+D/ventas7,79% son hipótesis; obsolescencia y competencia pueden cambiar ambas | −5pp objetivo: USD350.13 |

Se parte de gasto23.592 y cohortes previas15.384/10.569/7.812; amortización11.255 y activo37.371. Se proyecta I+D con intensidad7,7869% de ventas y amortización lineal de tres cohortes previas. Con crecimiento estable4%, el aporte neto de I+D es0,5838puntos; leases añaden0,1068. El margen económico estable es58%+0,5838+0,1068=58,6906%. Esto reduce la distorsión de perpetuar el ajuste del período de expansión.

El margen económico inicial común es69,1872%; la plantilla lo lleva al objetivo en año5 con su denominador cinco. En cada año GAAP=económico−I+D neta/ventas−ajuste leases. La Base implica aproximadamente56,23% GAAP en año5, con recuperación posterior conforme madura la amortización;58% describe el estado estable y no una celda GAAP forzada en año5. Las cuatro historias tienen el mismo margen económico inicial por diseño de la plantilla; sus cohortes e implicaciones GAAP posteriores difieren.

En52 períodos de conciliación (cuatro historias por13años de diagnóstico) se comprueba Δactivo I+D=gasto−amortización. El DCF utiliza diez años; los tres adicionales sirven para observar la aproximación a estabilidad. La prueba alternativa con calendario DCF de13años vale384,50; no es la Base oficial381,79 y su diferencia aproximada0,71% es un contraste metodológico. No se añadió un descuento adicional por esa diferencia. La capitalización no crea caja: la inversión se paga y su costo se refleja en amortización y reinversión.

El modelo fabless transfiere parte importante de la inversión fabril a proveedores, pero no elimina la necesidad de I+D, inventarios, anticipos, financiación y compromisos de capacidad. El capital invertido ajustado inicial es 154.689 millones, que incluye 37.371 de activo de I+D. Ventas/capital actual es 1,96 veces; la Base usa 2 veces en años 1–5. En años 6–10 disminuye hasta 0,5977 veces para sustentar el retorno marginal estable con la convención de capital de apertura de la plantilla.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| S/C inicial; ROIC marginal estable | LTM S/C 1,96; serie ROIC homogénea 3/5/10 N/D | 2,00 años 1–5; 27,22697% terminal; Input / Escenarios | Damodaran US semiconductores ajustado I+D/leases, 5-ene-2026 | Modelo fabless y reutilización de software; proveedores amplían capacidad | Anticipos, inventarios y nube elevan capital; retornos por nueva inversión disminuyen | S/C −20%: USD 375,82; industria global: USD 366,10 |

La reinversión explícita es Δventas/Sales-to-Capital, sin sumar nuevamente todo el CAPEX. Ante caídas de ventas no se reconoce una liberación automática de capital. El ROIC medio explícito sobre capital acumulado y el retorno marginal terminal son métricas distintas: el 27,23% terminal no implica que el retorno medio del año 10 se reduzca instantáneamente a esa cifra. No se usa una recompra para crear valor por acción sin su correspondiente desembolso.


El cociente tardío0,597701 se deriva de ROIC/[margen económico×(1−tax)×(1+g)], con la convención de capital de apertura. No representa el Sales-to-Capital observado de la industria. La reinversión total Δventas/S2C ya incorpora inversión neta en I+D: el puente resta esta última para identificar el otro capital; no vuelve a sumarla. Ante contracción puede aparecer depreciación neta o reducción del otro capital, un límite económico a vigilar. El tratamiento no usa un CAPEX ficticio para cuadrar caja.

El ROIC actual ajustado y normalizado a17% es112,81% sobre cierre,149,36% sobre promedio y220,96% sobre apertura; esos denominadores cambian la interpretación. El marginal estable27,23% no constituye una caída instantánea del retorno medio del stock. La falta de cohortes homogéneas para cada ejercicio antiguo limita la serie3/5/10años: se conserva N/D y no se rellena con el retorno actual.


## Anexo R2. Sensibilidad relativa Base: dos anclas y dos familias

### EV/EBITDA · JMR · Tradicional

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Fundamental FY+3 (USD millones) / Múltiplo real (veces) | 12.98 | 14.60 | 16.22 | 17.84 | 19.46 |
|---|---|---|---|---|---|
| 483,483.93 | 191.91 | 215.23 | 238.55 | 261.86 | 285.18 |
| 543,919.42 | 215.23 | 241.46 | 267.69 | 293.92 | 320.15 |
| 604,354.92 | 238.55 | 267.69 | 296.84 | 325.98 | 355.12 |
| 664,790.41 | 261.86 | 293.92 | 325.98 | 358.04 | 390.10 |
| 725,225.90 | 285.18 | 320.15 | 355.12 | 390.10 | 425.07 |

Centro: USD296.84; control OK.

### EV/EBITDA · JMR · Económica

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Delta crecimiento años1–3 (puntos decimales) / Múltiplo real (veces) | 12.98 | 14.60 | 16.22 | 17.84 | 19.46 |
|---|---|---|---|---|---|
| -0.04 | 220.13 | 246.98 | 273.82 | 300.66 | 327.50 |
| -0.02 | 229.21 | 257.19 | 285.17 | 313.15 | 341.13 |
| 0.00 | 238.55 | 267.69 | 296.84 | 325.98 | 355.12 |
| 0.02 | 248.13 | 278.48 | 308.82 | 339.16 | 369.50 |
| 0.04 | 257.98 | 289.55 | 321.12 | 352.70 | 384.27 |

Centro: USD296.84; control OK.

### EV/EBITDA · Observado · Tradicional

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Fundamental FY+3 (USD millones) / Múltiplo real (veces) | 19.91 | 22.39 | 24.88 | 27.37 | 29.86 |
|---|---|---|---|---|---|
| 483,483.93 | 291.53 | 327.30 | 363.07 | 398.83 | 434.60 |
| 543,919.42 | 327.30 | 367.54 | 407.78 | 448.01 | 488.25 |
| 604,354.92 | 363.07 | 407.78 | 452.48 | 497.19 | 541.90 |
| 664,790.41 | 398.83 | 448.01 | 497.19 | 546.37 | 595.56 |
| 725,225.90 | 434.60 | 488.25 | 541.90 | 595.56 | 649.21 |

Centro: USD452.48; control OK.

### EV/EBITDA · Observado · Económica

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Delta crecimiento años1–3 (puntos decimales) / Múltiplo real (veces) | 19.91 | 22.39 | 24.88 | 27.37 | 29.86 |
|---|---|---|---|---|---|
| -0.04 | 334.82 | 376.00 | 417.18 | 458.35 | 499.53 |
| -0.02 | 348.75 | 391.67 | 434.59 | 477.51 | 520.43 |
| 0.00 | 363.07 | 407.78 | 452.48 | 497.19 | 541.90 |
| 0.02 | 377.77 | 424.32 | 470.87 | 517.42 | 563.96 |
| 0.04 | 392.87 | 441.31 | 489.74 | 538.18 | 586.62 |

Centro: USD452.48; control OK.

### EV/FCFF · JMR · Tradicional

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Fundamental FY+3 (USD millones) / Múltiplo real (veces) | 17.95 | 20.20 | 22.44 | 24.69 | 26.93 |
|---|---|---|---|---|---|
| 349,438.17 | 191.91 | 215.23 | 238.55 | 261.86 | 285.18 |
| 393,117.94 | 215.23 | 241.46 | 267.69 | 293.92 | 320.15 |
| 436,797.71 | 238.55 | 267.69 | 296.84 | 325.98 | 355.12 |
| 480,477.48 | 261.86 | 293.92 | 325.98 | 358.04 | 390.10 |
| 524,157.26 | 285.18 | 320.15 | 355.12 | 390.10 | 425.07 |

Centro: USD296.84; control OK.

### EV/FCFF · JMR · Económica

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Delta crecimiento años1–3 (puntos decimales) / Múltiplo real (veces) | 17.95 | 20.20 | 22.44 | 24.69 | 26.93 |
|---|---|---|---|---|---|
| -0.04 | 222.33 | 249.45 | 276.57 | 303.69 | 330.80 |
| -0.02 | 230.34 | 258.46 | 286.58 | 314.70 | 342.82 |
| 0.00 | 238.55 | 267.69 | 296.84 | 325.98 | 355.12 |
| 0.02 | 246.95 | 277.14 | 307.34 | 337.53 | 367.72 |
| 0.04 | 255.54 | 286.81 | 318.08 | 349.35 | 380.62 |

Centro: USD296.84; control OK.

### EV/FCFF · Observado · Tradicional

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Fundamental FY+3 (USD millones) / Múltiplo real (veces) | 33.34 | 37.51 | 41.68 | 45.85 | 50.01 |
|---|---|---|---|---|---|
| 349,438.17 | 351.81 | 395.11 | 438.41 | 481.71 | 525.01 |
| 393,117.94 | 395.11 | 443.82 | 492.54 | 541.25 | 589.97 |
| 436,797.71 | 438.41 | 492.54 | 546.67 | 600.79 | 654.92 |
| 480,477.48 | 481.71 | 541.25 | 600.79 | 660.33 | 719.87 |
| 524,157.26 | 525.01 | 589.97 | 654.92 | 719.87 | 784.83 |

Centro: USD546.67; control OK.

### EV/FCFF · Observado · Económica

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Delta crecimiento años1–3 (puntos decimales) / Múltiplo real (veces) | 33.34 | 37.51 | 41.68 | 45.85 | 50.01 |
|---|---|---|---|---|---|
| -0.04 | 408.30 | 458.66 | 509.02 | 559.39 | 609.75 |
| -0.02 | 423.17 | 475.40 | 527.62 | 579.84 | 632.07 |
| 0.00 | 438.41 | 492.54 | 546.67 | 600.79 | 654.92 |
| 0.02 | 454.01 | 510.09 | 566.17 | 622.24 | 678.32 |
| 0.04 | 469.98 | 528.05 | 586.13 | 644.20 | 702.27 |

Centro: USD546.67; control OK.

### P/E · JMR · Tradicional

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Fundamental FY+3 (USD millones) / Múltiplo real (veces) | 16.10 | 18.11 | 20.12 | 22.13 | 24.15 |
|---|---|---|---|---|---|
| 391,248.59 | 189.67 | 213.08 | 236.48 | 259.89 | 283.30 |
| 440,154.66 | 213.08 | 239.41 | 265.74 | 292.07 | 318.41 |
| 489,060.74 | 236.48 | 265.74 | 295.00 | 324.26 | 353.51 |
| 537,966.81 | 259.89 | 292.07 | 324.26 | 356.44 | 388.62 |
| 586,872.88 | 283.30 | 318.41 | 353.51 | 388.62 | 423.73 |

Centro: USD295.00; control OK.

### P/E · JMR · Económica

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Delta crecimiento años1–3 (puntos decimales) / Múltiplo real (veces) | 16.10 | 18.11 | 20.12 | 22.13 | 24.15 |
|---|---|---|---|---|---|
| -0.04 | 218.00 | 244.95 | 271.89 | 298.84 | 325.79 |
| -0.02 | 227.12 | 255.20 | 283.29 | 311.38 | 339.46 |
| 0.00 | 236.48 | 265.74 | 295.00 | 324.26 | 353.51 |
| 0.02 | 246.11 | 276.57 | 307.03 | 337.49 | 367.95 |
| 0.04 | 255.99 | 287.69 | 319.38 | 351.08 | 382.77 |

Centro: USD295.00; control OK.

### P/E · Observado · Tradicional

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Fundamental FY+3 (USD millones) / Múltiplo real (veces) | 24.97 | 28.10 | 31.22 | 34.34 | 37.46 |
|---|---|---|---|---|---|
| 391,248.59 | 292.95 | 329.26 | 365.58 | 401.89 | 438.21 |
| 440,154.66 | 329.26 | 370.12 | 410.97 | 451.83 | 492.68 |
| 489,060.74 | 365.58 | 410.97 | 456.36 | 501.76 | 547.15 |
| 537,966.81 | 401.89 | 451.83 | 501.76 | 551.69 | 601.63 |
| 586,872.88 | 438.21 | 492.68 | 547.15 | 601.63 | 656.10 |

Centro: USD456.36; control OK.

### P/E · Observado · Económica

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Delta crecimiento años1–3 (puntos decimales) / Múltiplo real (veces) | 24.97 | 28.10 | 31.22 | 34.34 | 37.46 |
|---|---|---|---|---|---|
| -0.04 | 336.90 | 378.71 | 420.52 | 462.32 | 504.13 |
| -0.02 | 351.04 | 394.62 | 438.20 | 481.77 | 525.35 |
| 0.00 | 365.58 | 410.97 | 456.36 | 501.76 | 547.15 |
| 0.02 | 380.51 | 427.77 | 475.03 | 522.29 | 569.55 |
| 0.04 | 395.84 | 445.02 | 494.20 | 543.37 | 592.55 |

Centro: USD456.36; control OK.

### P/FCFE · JMR · Tradicional

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Fundamental FY+3 (USD millones) / Múltiplo real (veces) | 16.86 | 18.96 | 21.07 | 23.18 | 25.28 |
|---|---|---|---|---|---|
| 349,753.14 | 177.70 | 199.61 | 221.52 | 243.43 | 265.34 |
| 393,472.28 | 199.61 | 224.26 | 248.90 | 273.55 | 298.20 |
| 437,191.43 | 221.52 | 248.90 | 276.29 | 303.68 | 331.06 |
| 480,910.57 | 243.43 | 273.55 | 303.68 | 333.80 | 363.93 |
| 524,629.71 | 265.34 | 298.20 | 331.06 | 363.93 | 396.79 |

Centro: USD295.00; control OK.

### P/FCFE · JMR · Económica

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Delta crecimiento años1–3 (puntos decimales) / Múltiplo real (veces) | 16.86 | 18.96 | 21.07 | 23.18 | 25.28 |
|---|---|---|---|---|---|
| -0.04 | 218.64 | 245.67 | 272.70 | 299.73 | 326.76 |
| -0.02 | 227.45 | 255.57 | 283.70 | 311.83 | 339.96 |
| 0.00 | 221.52 | 248.90 | 276.29 | 303.68 | 331.06 |
| 0.02 | 245.76 | 276.18 | 306.59 | 337.01 | 367.43 |
| 0.04 | 255.28 | 286.88 | 318.49 | 350.10 | 381.70 |

Centro: USD295.00; control OK.

### P/FCFE · Observado · Tradicional

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Fundamental FY+3 (USD millones) / Múltiplo real (veces) | 34.20 | 38.47 | 42.75 | 47.02 | 51.30 |
|---|---|---|---|---|---|
| 349,753.14 | 382.33 | 429.82 | 477.30 | 524.79 | 572.28 |
| 393,472.28 | 429.82 | 483.24 | 536.66 | 590.09 | 643.51 |
| 437,191.43 | 477.30 | 536.66 | 596.02 | 655.38 | 714.75 |
| 480,910.57 | 524.79 | 590.09 | 655.38 | 720.68 | 785.98 |
| 524,629.71 | 572.28 | 643.51 | 714.75 | 785.98 | 857.21 |

Centro: USD596.02; control OK.

### P/FCFE · Observado · Económica

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Delta crecimiento años1–3 (puntos decimales) / Múltiplo real (veces) | 34.20 | 38.47 | 42.75 | 47.02 | 51.30 |
|---|---|---|---|---|---|
| -0.04 | 441.11 | 495.95 | 550.78 | 605.62 | 660.45 |
| -0.02 | 458.97 | 516.04 | 573.11 | 630.17 | 687.24 |
| 0.00 | 477.30 | 536.66 | 596.02 | 655.38 | 714.75 |
| 0.02 | 496.12 | 557.84 | 619.55 | 681.26 | 742.97 |
| 0.04 | 515.43 | 579.56 | 643.68 | 707.81 | 771.94 |

Centro: USD596.02; control OK.

### P/OCF · JMR · Tradicional

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Fundamental FY+3 (USD millones) / Múltiplo real (veces) | 17.11 | 19.25 | 21.38 | 23.52 | 25.66 |
|---|---|---|---|---|---|
| 368,133.13 | 189.67 | 213.08 | 236.48 | 259.89 | 283.30 |
| 414,149.77 | 213.08 | 239.41 | 265.74 | 292.07 | 318.41 |
| 460,166.42 | 236.48 | 265.74 | 295.00 | 324.26 | 353.51 |
| 506,183.06 | 259.89 | 292.07 | 324.26 | 356.44 | 388.62 |
| 552,199.70 | 283.30 | 318.41 | 353.51 | 388.62 | 423.73 |

Centro: USD295.00; control OK.

### P/OCF · JMR · Económica

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Delta crecimiento años1–3 (puntos decimales) / Múltiplo real (veces) | 17.11 | 19.25 | 21.38 | 23.52 | 25.66 |
|---|---|---|---|---|---|
| -0.04 | 220.09 | 247.30 | 274.51 | 301.72 | 328.93 |
| -0.02 | 228.19 | 256.41 | 284.63 | 312.85 | 341.07 |
| 0.00 | 236.48 | 265.74 | 295.00 | 324.26 | 353.51 |
| 0.02 | 244.98 | 275.30 | 305.62 | 335.93 | 366.25 |
| 0.04 | 253.67 | 285.08 | 316.48 | 347.89 | 379.30 |

Centro: USD295.00; control OK.

### P/OCF · Observado · Tradicional

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Fundamental FY+3 (USD millones) / Múltiplo real (veces) | 32.22 | 36.25 | 40.27 | 44.30 | 48.33 |
|---|---|---|---|---|---|
| 368,133.13 | 355.07 | 399.15 | 443.23 | 487.31 | 531.39 |
| 414,149.77 | 399.15 | 448.74 | 498.33 | 547.92 | 597.52 |
| 460,166.42 | 443.23 | 498.33 | 553.43 | 608.54 | 663.64 |
| 506,183.06 | 487.31 | 547.92 | 608.54 | 669.15 | 729.76 |
| 552,199.70 | 531.39 | 597.52 | 663.64 | 729.76 | 795.88 |

Centro: USD553.43; control OK.

### P/OCF · Observado · Económica

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Delta crecimiento años1–3 (puntos decimales) / Múltiplo real (veces) | 32.22 | 36.25 | 40.27 | 44.30 | 48.33 |
|---|---|---|---|---|---|
| -0.04 | 412.37 | 463.61 | 514.85 | 566.09 | 617.34 |
| -0.02 | 427.61 | 480.76 | 533.91 | 587.06 | 640.21 |
| 0.00 | 443.23 | 498.33 | 553.43 | 608.54 | 663.64 |
| 0.02 | 459.23 | 516.33 | 573.43 | 630.53 | 687.63 |
| 0.04 | 475.60 | 534.75 | 593.90 | 653.04 | 712.19 |

Centro: USD553.43; control OK.

### P/V · JMR · Tradicional

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Fundamental FY+3 (USD millones) / Múltiplo real (veces) | 7.90 | 8.88 | 9.87 | 10.86 | 11.85 |
|---|---|---|---|---|---|
| 797,512.37 | 189.67 | 213.08 | 236.48 | 259.89 | 283.30 |
| 897,201.42 | 213.08 | 239.41 | 265.74 | 292.07 | 318.41 |
| 996,890.47 | 236.48 | 265.74 | 295.00 | 324.26 | 353.51 |
| 1,096,579.51 | 259.89 | 292.07 | 324.26 | 356.44 | 388.62 |
| 1,196,268.56 | 283.30 | 318.41 | 353.51 | 388.62 | 423.73 |

Centro: USD295.00; control OK.

### P/V · JMR · Económica

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Delta crecimiento años1–3 (puntos decimales) / Múltiplo real (veces) | 7.90 | 8.88 | 9.87 | 10.86 | 11.85 |
|---|---|---|---|---|---|
| -0.04 | 218.00 | 244.95 | 271.89 | 298.84 | 325.79 |
| -0.02 | 227.12 | 255.20 | 283.29 | 311.38 | 339.46 |
| 0.00 | 236.48 | 265.74 | 295.00 | 324.26 | 353.51 |
| 0.02 | 246.11 | 276.57 | 307.03 | 337.49 | 367.95 |
| 0.04 | 255.99 | 287.69 | 319.38 | 351.08 | 382.77 |

Centro: USD295.00; control OK.

### P/V · Observado · Tradicional

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Fundamental FY+3 (USD millones) / Múltiplo real (veces) | 13.52 | 15.21 | 16.90 | 18.59 | 20.28 |
|---|---|---|---|---|---|
| 797,512.37 | 322.96 | 363.03 | 403.10 | 443.17 | 483.23 |
| 897,201.42 | 363.03 | 408.11 | 453.18 | 498.26 | 543.34 |
| 996,890.47 | 403.10 | 453.18 | 503.27 | 553.35 | 603.44 |
| 1,096,579.51 | 443.17 | 498.26 | 553.35 | 608.45 | 663.54 |
| 1,196,268.56 | 483.23 | 543.34 | 603.44 | 663.54 | 723.64 |

Centro: USD503.27; control OK.

### P/V · Observado · Económica

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Delta crecimiento años1–3 (puntos decimales) / Múltiplo real (veces) | 13.52 | 15.21 | 16.90 | 18.59 | 20.28 |
|---|---|---|---|---|---|
| -0.04 | 371.46 | 417.59 | 463.71 | 509.84 | 555.97 |
| -0.02 | 387.06 | 435.14 | 483.22 | 531.30 | 579.38 |
| 0.00 | 403.10 | 453.18 | 503.27 | 553.35 | 603.44 |
| 0.02 | 419.57 | 471.72 | 523.86 | 576.01 | 628.15 |
| 0.04 | 436.49 | 490.75 | 545.01 | 599.27 | 653.53 |

Centro: USD503.27; control OK.

### P/BV · JMR · Tradicional

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Fundamental FY+3 (USD millones) / Múltiplo real (veces) | 5.94 | 6.68 | 7.43 | 8.17 | 8.91 |
|---|---|---|---|---|---|
| 1,060,151.14 | 189.67 | 213.08 | 236.48 | 259.89 | 283.30 |
| 1,192,670.04 | 213.08 | 239.41 | 265.74 | 292.07 | 318.41 |
| 1,325,188.93 | 236.48 | 265.74 | 295.00 | 324.26 | 353.51 |
| 1,457,707.82 | 259.89 | 292.07 | 324.26 | 356.44 | 388.62 |
| 1,590,226.71 | 283.30 | 318.41 | 353.51 | 388.62 | 423.73 |

Centro: USD295.00; control OK.

### P/BV · JMR · Económica

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Delta crecimiento años1–3 (puntos decimales) / Múltiplo real (veces) | 5.94 | 6.68 | 7.43 | 8.17 | 8.91 |
|---|---|---|---|---|---|
| -0.04 | 225.14 | 252.98 | 280.82 | 308.66 | 336.50 |
| -0.02 | 230.76 | 259.30 | 287.84 | 316.38 | 344.92 |
| 0.00 | 236.48 | 265.74 | 295.00 | 324.26 | 353.51 |
| 0.02 | 242.33 | 272.32 | 302.31 | 332.29 | 362.28 |
| 0.04 | 248.29 | 279.02 | 309.76 | 340.49 | 371.22 |

Centro: USD295.00; control OK.

### P/BV · Observado · Tradicional

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Fundamental FY+3 (USD millones) / Múltiplo real (veces) | 17.89 | 20.12 | 22.36 | 24.59 | 26.83 |
|---|---|---|---|---|---|
| 1,060,151.14 | 566.20 | 636.67 | 707.15 | 777.62 | 848.09 |
| 1,192,670.04 | 636.67 | 715.96 | 795.24 | 874.52 | 953.80 |
| 1,325,188.93 | 707.15 | 795.24 | 883.33 | 971.42 | 1,059.51 |
| 1,457,707.82 | 777.62 | 874.52 | 971.42 | 1,068.32 | 1,165.22 |
| 1,590,226.71 | 848.09 | 953.80 | 1,059.51 | 1,165.22 | 1,270.93 |

Centro: USD883.33; control OK.

### P/BV · Observado · Económica

VP FY+3; Ke y dividendos por año; fórmulas originales Financials Multiples verificadas contra63precios nativos

| Delta crecimiento años1–3 (puntos decimales) / Múltiplo real (veces) | 17.89 | 20.12 | 22.36 | 24.59 | 26.83 |
|---|---|---|---|---|---|
| -0.04 | 672.99 | 756.81 | 840.64 | 924.46 | 1,008.28 |
| -0.02 | 689.90 | 775.83 | 861.77 | 947.70 | 1,033.63 |
| 0.00 | 707.15 | 795.24 | 883.33 | 971.42 | 1,059.51 |
| 0.02 | 724.74 | 815.03 | 905.32 | 995.61 | 1,085.90 |
| 0.04 | 742.69 | 835.23 | 927.76 | 1,020.29 | 1,112.83 |

Centro: USD883.33; control OK.

