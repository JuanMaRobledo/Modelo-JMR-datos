# Nivel 2 · Cálculos, estados y soportes

Revisión AMZN-20261102-A12-R2, estado CANDIDATO. Este anexo reproduce las cifras conservadas sin volver a calibrar ni ejecutar el DCF.

## 1. Identificación, fuentes y unidades

**Revisión:** AMZN-20261102-A12-R2. Método A/A-1.2. Estado CANDIDATO. No se promueve a EN_REVISION. Acción común NASDAQ:AMZN, USD; financieros y acciones en millones; precios y valores en USD/acción.

| Referencia | Fecha/período | Fuente |
|---|---|---|
| Corte de investigación | 2026-11-02 | FASE_2_ENTREGA y metadatos |
| Mercado | 2026-10-30 | Input sheet!D1/B23; no precio Nov2 |
| Estadosbase | LTM terminado2026-09-30 | Income Statement/Cash Flow Statement!L |
| Balanceactual | 2026-09-30 | Balance Sheet!L |
| Historia | FY2016–FY2025 | Estados!B:K;10observaciones y9intervalos |
| Hoja | 1h6Xv5cNqwtKPpqI81KiZ_FNpTl4k_uQQS2QJEHphaBI | https://docs.google.com/spreadsheets/d/1h6Xv5cNqwtKPpqI81KiZ_FNpTl4k_uQQS2QJEHphaBI/edit |
| Captura fase 2 | ad3c2174044e688e584f0b639e8777a8bf4c8e1229ae3a98e121640a1fd3b4cd | SHA256 CAPTURA_SHEET.json |
| Lecturahistóricafase 3 | 42f3a30f080fae26c1d11a13d4eed46b4f54d93a70c0a158f3d4c22e7932b36f | historical_read.json |


La investigación macro y de gobierno utiliza información publicada antes del corte. El precio de mercado conservado permanece fijo. Las tablas se generan desde la captura y el JSON de R2. Las notas identifican datos, cálculos y juicios; no se transcriben cifras a mano.

| Código | Documento | Localizador |
|---|---|---|
| S1 | [Amazon10-Q, Sep2026, presentado30-oct2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm) | Balance pp5–6; notas2 pp10–12,3 pp13–14,4 pp15–16,5 pp17–18,6 pp19–20,7 p22; MD&A pp28–36. Notas puntuales de celdas. |
| S2 | [Amazon10-K FY2025](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm) | Estados y segmentos/geografía; notas de celdas históricas B:K. |
| S3 | [Amazon Q3IR,29-oct2026](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx) | Resultados por segmento, guía capex2026/2027, cambio calendario Prime Day. |
| S4 | [USTTreasury10Y30-oct2026](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_yield_curve) | Fila10/30/2026, columna10-year4.94%; Input B35. |
| S5 | [Damodaran, ERP publicado1-oct2026, corte30-sep](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm) | 4.20% adjusted payout;3.70% cashyield; Rf5.29%. Rebase a4.55% es JUICIO, no cotización Oct30. |
| S6 | [Damodaran, Betas US enero2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html) | Retail General n23 y Computer Services n64; caché de Industry Averages US filas75/22. Precisión de caché, tabla pública redondeada. |
| S7 | [Precio AMZN30-oct2026](https://stockanalysis.com/stocks/amzn/history/?period=daily) | Cierre sin ajuste240.35, proveedor S&PGlobal; contraste Yahoo History. No cierre Nov2. |
| S8 | [Entrega fase1 R2](https://drive.google.com/file/d/1fE-5Vkw2ciMUGU_RqilijMUgAqwe1QlX/view) | CERRADA CON CONTROLES PENDIENTES, actualización2-nov. Continuidad autorizada por README vigente y nueva invocación. |
| F2 | [Entrega y JSON AMZN R2, fase 2](https://chatgpt.com/library?file_id=libfile_52c828369dac819198bffd18acf78c38&account_id=personal) | FASE_2_ENTREGA.md, versión2; JSON y captura SHA256ad3c2174044e688e584f0b639e8777a8bf4c8e1229ae3a98e121640a1fd3b4cd |
| M1 | [FOMC, decisión28-oct2026](https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm) | Mantiene3.75–4.00%; comunicado publicado28-oct2026. Nivel y decisión, no trayectoria completa de tipos. |
| M2 | [BEA, PIBQ3 avance,29-oct2026](https://www.bea.gov/index.php/news/2026/gdp-advance-estimate-3rd-quarter-2026) | PIBreal3.4%SAAR Q3;2.2%Q2. Datos de primera estimación conocidos al corte. |
| M3 | [BLS, IPCseptiembre publicado14-oct2026](https://www.bls.gov/cpi/news.htm) | Titular3.7%interanual; subyacente2.6%. Archivo mensual vigente al corte; no sustituir por octubre publicado posteriormente. |
| M4 | [Federal Reserve SLOOSjulio2026, publicado3-ago2026](https://www.federalreserve.gov/data/sloos/sloos-202607.htm) | Crédito C&I y hogares, cambios en Q2 y nivel de estándares. Rezago explícito; no encuesta noviembre. |
| G1 | [Amazon Proxy2026](https://s2.q4cdn.com/299287126/files/doc_financials/2026/ar/Amazon-2026-Proxy-Statement.pdf) | Remuneración e incentivos, pp56–61. Sin inferir porcentajes de control no comprobados. |


## 2. Estados históricos y LTM

### Income Statement

| Partida / celda | Dec '16 | Dec '17 | Dec '18 | Dec '19 | Dec '20 | Dec '21 | Dec '22 | Dec '23 | Dec '24 | Dec '25 | LTM Sep '26 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Total Revenues [3] | 135.987 | 177.866 | 232.887 | 280.522 | 386.064 | 469.822 | 513.983 | 574.785 | 637.959 | 716.924 | 797.455 |
| Total Revenues %Chg [4] | N/D | 30,80 % | 30,93 % | 20,45 % | 37,62 % | 21,70 % | 9,40 % | 11,83 % | 10,99 % | 12,38 % | 11,23 % |
| Cost of Sales [5] | 88.265 | 111.934 | 139.156 | 165.536 | 233.307 | 272.344 | 288.831 | 304.739 | 326.288 | 356.414 | 387.773 |
| Gross Profit [6] | 47.722 | 65.932 | 93.731 | 114.986 | 152.757 | 197.478 | 225.152 | 270.046 | 311.671 | 360.510 | 409.682 |
| Gross Profit Margin [7] | 35,09 % | 37,07 % | 40,25 % | 40,99 % | 39,57 % | 42,03 % | 43,81 % | 46,98 % | 48,85 % | 50,29 % | 51,37 % |
| Selling, General & Administrative Expenses [8] | 9.665 | 13.743 | 18.150 | 24.081 | 28.676 | 41.374 | 54.129 | 56.186 | 55.266 | 58.301 | 58.705 |
| Depreciation & Amortization Expenses [9] | 8.116 | 11.478 | 15.341 | 21.789 | 25.180 | 34.433 | 41.921 | 48.663 | 52.795 | 65.756 | 79.353 |
| Research & Development Expenses [10] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Other Operating Expenses [11] | 33.871 | 48.083 | 63.160 | 76.364 | 101.182 | 131.225 | 158.775 | 177.008 | 187.812 | 222.234 | 246.611 |
| Operating Profit [12] | 4.186 | 4.106 | 12.421 | 14.541 | 22.899 | 24.879 | 12.248 | 36.852 | 68.593 | 79.975 | 104.366 |
| Operating Margin [13] | 3,08 % | 2,31 % | 5,33 % | 5,18 % | 5,93 % | 5,30 % | 2,38 % | 6,41 % | 10,75 % | 11,16 % | 13,09 % |
| Interest and Investment Income [14] | 100 | 202 | 440 | 832 | 555 | 448 | 989 | 2.949 | 4.677 | 4.381 | 4.747 |
| Interest Expense [15] | -484 | -848 | -1.417 | -1.600 | -1.647 | -1.809 | -2.367 | -3.182 | -2.406 | -2.274 | -4.484 |
| Interest Expense, Net [16] | -384 | -646 | -977 | -768 | -1.092 | -1.361 | -1.378 | -233 | 2.271 | 2.107 | 263 |
| Non-Operating Income [17] | 90 | 346 | -183 | 203 | 2.371 | 14.633 | -16.806 | 938 | -2.250 | 15.229 | 69.536 |
| Total Non-Operating Income [18] | -294 | -300 | -1.160 | -565 | 1.279 | 13.272 | -18.184 | 705 | 21 | 17.336 | 69.799 |
| Income Before Provision for Income Taxes [19] | 3.892 | 3.806 | 11.261 | 13.976 | 24.178 | 38.151 | -5.936 | 37.557 | 68.614 | 97.311 | 174.165 |
| Provision for Income Taxes [20] | 1.425 | 769 | 1.197 | 2.374 | 2.863 | 4.791 | -3.217 | 7.120 | 9.265 | 19.087 | 38.885 |
| Consolidated Net Income [21] | 2.371 | 3.033 | 10.073 | 11.588 | 21.331 | 33.364 | -2.722 | 30.425 | 59.248 | 77.670 | 134.779 |
| Net Income Attributable to Common Shareholders [22] | 2.371,00 | 3.033,00 | 10.073,00 | 11.588,00 | 21.331,00 | 33.364,00 | -2.722,00 | 30.425,00 | 59.248,00 | 77.670,00 | 134.779,00 |
| Basic EPS [23] | 0,25 | 0,32 | 1,03 | 1,17 | 2,13 | 3,30 | -0,27 | 2,95 | 5,66 | 7,29 | 12,49 |
| Diluted EPS [24] | 0,24 | 0,31 | 1,01 | 1,15 | 2,09 | 3,24 | -0,27 | 2,90 | 5,53 | 7,17 | 12,35 |
| Basic Weighted Average Shares Outstanding [25] | 9.480,00 | 9.600,00 | 9.740,00 | 9.880,00 | 10.005,00 | 10.117,00 | 10.189,00 | 10.304,00 | 10.473,00 | 10.656,00 | 10.788,00 |
| Diluted Weighted Average Shares Outstanding [26] | 9.680,00 | 9.860,00 | 10.000,00 | 10.080,00 | 10.198,00 | 10.296,00 | 10.189,00 | 10.492,00 | 10.721,00 | 10.827,00 | 10.915,00 |
| Shares Outstanding [27] | 9.540,00 | 9.680,00 | 9.820,00 | 9.960,00 | 10.060,00 | 10.180,00 | 10.242,00 | 10.383,00 | 10.593,00 | 10.731,00 | 10.811,00 |
| EBITDA [28] | 12.302 | 15.584 | 27.762 | 36.330 | 48.079 | 59.312 | 54.169 | 85.515 | 121.388 | 145.731 | 183.719 |
| Effective Tax Rate [29] | 36,61 % | 20,20 % | 10,63 % | 16,99 % | 11,84 % | 12,56 % | -54,19 % | 18,96 % | 13,50 % | 19,61 % | 22,33 % |
| EBITDA Margin [30] | 9,05 % | 8,76 % | 11,92 % | 12,95 % | 12,45 % | 12,62 % | 10,54 % | 14,88 % | 19,03 % | 20,33 % | 23,04 % |


### Balance Sheet

| Partida / celda | Dec '16 | Dec '17 | Dec '18 | Dec '19 | Dec '20 | Dec '21 | Dec '22 | Dec '23 | Dec '24 | Dec '25 | LTM Sep '26 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cash and Cash Equivalents [3] | 19.334 | 20.522 | 31.750 | 36.092 | 42.122 | 36.220 | 53.888 | 73.387 | 78.779 | 86.810 | 55.783 |
| Short-Term Investments [4] | 6.647 | 10.464 | 9.500 | 18.929 | 42.274 | 59.829 | 16.138 | 13.393 | 22.423 | 36.219 | 58.443 |
| Total Cash and Cash Equivalents [5] | 25.981 | 30.986 | 41.250 | 55.021 | 84.396 | 96.049 | 70.026 | 86.780 | 101.202 | 123.029 | 114.226 |
| Accounts Receivable [6] | 8.339 | 13.164 | 16.677 | 20.816 | 24.542 | 32.891 | 42.360 | 52.253 | 55.451 | 67.729 | 98.242 |
| Other Receivables [7] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Total Trade Receivables [8] | 8.339 | 13.164 | 16.677 | 20.816 | 24.542 | 32.891 | 42.360 | 52.253 | 55.451 | 67.729 | 98.242 |
| Other Current Assets [9] | 11.461 | 16.047 | 17.174 | 20.497 | 23.795 | 32.640 | 34.405 | 33.318 | 34.214 | 38.325 | 42.632 |
| Total Current Assets [10] | 45.781 | 60.197 | 75.101 | 96.334 | 132.733 | 161.580 | 146.791 | 172.351 | 190.867 | 229.083 | 255.100 |
| Net Property, Plant & Equipment [11] | 29.114 | 48.866 | 61.797 | 72.705 | 113.114 | 160.281 | 186.715 | 204.177 | 252.665 | 357.025 | 508.862 |
| Net Intangible Assets [12] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Goodwill [13] | 3.784 | 13.350 | 14.548 | 14.754 | 15.017 | 15.371 | 20.288 | 22.789 | 23.074 | 23.273 | 23.743 |
| Long-Term Investments [14] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 65.359 | 294.595 |
| Other Long-Term Assets [15] | 4.723 | 8.897 | 11.202 | 41.455 | 60.331 | 83.317 | 108.881 | 128.537 | 158.288 | 143.302 | 161.090 |
| Total Assets [16] | 83.402 | 131.310 | 162.648 | 225.248 | 321.195 | 420.549 | 462.675 | 527.854 | 624.894 | 818.042 | 1.243.390 |
| Accounts Payable [18] | 25.309 | 34.616 | 38.192 | 47.183 | 72.539 | 78.664 | 79.600 | 84.981 | 94.363 | 121.909 | 158.715 |
| Accrued Expenses [19] | 13.739 | 18.170 | 23.663 | 32.439 | 44.138 | 51.775 | 62.566 | 64.709 | 66.965 | 58.215 | 54.347 |
| Short-Term Debt [20] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3.106 | 7.253 |
| Current Portion of Leases [21] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 14.199 | 15.959 |
| Unearned Revenue [22] | 4.768 | 5.097 | 6.536 | 8.190 | 9.708 | 11.827 | 13.227 | 15.227 | 18.103 | 20.576 | 21.708 |
| Other Current Liabilities [23] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Total Current Liabilities [24] | 43.816 | 57.883 | 68.391 | 87.812 | 126.385 | 142.266 | 155.393 | 164.917 | 179.431 | 218.005 | 257.982 |
| Long-Term Debt [25] | 7.694 | 24.743 | 23.495 | 23.414 | 31.816 | 48.744 | 67.150 | 58.314 | 52.623 | 73.448 | 182.425 |
| Leases [26] | 0 | 0 | 0 | 39.791 | 52.573 | 67.651 | 72.968 | 77.297 | 78.277 | 87.339 | 98.824 |
| Other Long-Term Liabilities [27] | 12.607 | 20.975 | 27.213 | 12.171 | 17.017 | 23.643 | 21.121 | 25.451 | 28.593 | 28.185 | 90.558 |
| Total Long-Term Liabilities [28] | 20.301 | 45.718 | 50.708 | 75.376 | 101.406 | 140.038 | 161.239 | 161.062 | 159.493 | 188.972 | 371.807 |
| Total Liabilities [29] | 64.117 | 103.601 | 119.099 | 163.188 | 227.791 | 282.304 | 316.632 | 325.979 | 338.924 | 406.977 | 629.789 |
| Additional Paid-in Capital [31] | 17.186 | 21.389 | 26.791 | 33.658 | 42.865 | 55.538 | 75.066 | 99.025 | 120.864 | 140.024 | 154.924 |
| Accumulated Other Comprehensive Income [32] | -985 | -484 | -1.035 | -986 | -180 | -1.376 | -4.487 | -3.040 | -34 | 28.230 | 102.278 |
| Retained Earnings [33] | 4.916 | 8.636 | 19.625 | 31.220 | 52.551 | 85.915 | 83.193 | 113.618 | 172.866 | 250.536 | 364.123 |
| Total Common Shareholders' Equity [34] | 19.285,00 | 27.709,00 | 43.549,00 | 62.060,00 | 93.404,00 | 138.245,00 | 146.043,00 | 201.875,00 | 285.970,00 | 411.065,00 | 613.601,00 |
| Total Shareholders' Equity [35] | 19.285,00 | 27.709,00 | 43.549,00 | 62.060,00 | 93.404,00 | 138.245,00 | 146.043,00 | 201.875,00 | 285.970,00 | 411.065,00 | 613.601,00 |
| Total Liabilities and Shareholders' Equity [36] | 83.402,00 | 131.310,00 | 162.648,00 | 225.248,00 | 321.195,00 | 420.549,00 | 462.675,00 | 527.854,00 | 624.894,00 | 818.042,00 | 1.243.390,00 |


### Cash Flow Statement

| Partida / celda | Dec '16 | Dec '17 | Dec '18 | Dec '19 | Dec '20 | Dec '21 | Dec '22 | Dec '23 | Dec '24 | Dec '25 | LTM Sep '26 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Net Income [3] | 2.371 | 3.033 | 10.073 | 11.588 | 21.331 | 33.364 | -2.722 | 30.425 | 59.248 | 77.670 | 134.779 |
| Depreciation & Amortization [4] | 8.116 | 11.478 | 15.341 | 21.789 | 25.180 | 34.433 | 41.921 | 48.663 | 52.795 | 65.756 | 79.353 |
| Share-Based Compensation Expense [5] | 2.975,00 | 4.215,00 | 5.418,00 | 6.864,00 | 9.208,00 | 12.757,00 | 19.621,00 | 24.023,00 | 22.011,00 | 19.467,00 | 19.873,00 |
| Other Adjustments [6] | -1.532 | -3.702 | -380 | -2.567 | -5.985 | -24.103 | 6.226 | -17.440 | -19.003 | -22.044 | -52.664 |
| Changes in Trade Receivables [7] | -3.436 | -4.780 | -4.615 | -7.681 | -8.169 | -18.163 | -21.897 | -8.348 | -3.249 | -7.333 | -21.559 |
| Changes in Accounts Payable [8] | 5.030 | 7.100 | 3.263 | 8.193 | 17.480 | 3.602 | 2.945 | 5.473 | 2.972 | 11.231 | 13.272 |
| Changes in Accrued Expenses [9] | 1.724 | 283 | 472 | -1.383 | 5.754 | 2.123 | -1.558 | -2.428 | -2.904 | -5.019 | -7.918 |
| Changes in Income Taxes Payable [10] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Changes in Unearned Revenue [11] | 1.955 | 738 | 1.151 | 1.711 | 1.265 | 2.314 | 2.216 | 4.578 | 4.007 | -214 | 3.164 |
| Changes in Other Operating Activities [12] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Cash from Operating Activities [13] | 17.203 | 18.365 | 30.723 | 38.514 | 66.064 | 46.327 | 46.752 | 84.946 | 115.877 | 139.514 | 168.300 |
| Capital Expenditure [15] | -7.804 | -11.955 | -13.427 | -16.861 | -40.140 | -61.053 | -63.645 | -52.729 | -82.999 | -131.819 | -215.192 |
| Proceeds from Sale of Property, Plant & Equipment [16] | 1.067 | 1.897 | 2.104 | 4.172 | 5.096 | 5.657 | 5.324 | 4.596 | 5.341 | 3.499 | 4.535 |
| Purchases of Investments [17] | -7.240 | -12.731 | -7.100 | -31.812 | -72.479 | -60.157 | -2.565 | -1.488 | -26.005 | -54.770 | -102.931 |
| Proceeds from Sale of Investments [18] | 4.577 | 9.677 | 8.240 | 22.681 | 50.237 | 59.384 | 31.601 | 5.627 | 16.403 | 44.386 | 74.400 |
| Payments for Business Acquisitions [19] | -116 | -13.972 | -2.186 | -2.461 | -2.325 | -1.985 | -8.316 | -5.839 | -7.082 | -3.841 | -65.156 |
| Proceeds from Business Divestments [20] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Other Investing Activities [21] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Cash from Investing Activities [22] | -9.516 | -27.084 | -12.369 | -24.281 | -59.611 | -58.154 | -37.601 | -49.833 | -94.342 | -142.545 | -304.344 |
| Issuance of Short-Term Debt [24] | 0 | 0 | 0 | 0 | 6.796 | 7.956 | 41.553 | 18.129 | 5.142 | 9.320 | 22.882 |
| Net Issuance / (Repayments) of Short-Term Debt [25] | 0 | 0 | 0 | 0 | -6.177 | -7.753 | -37.554 | -25.677 | -5.060 | -8.426 | -22.735 |
| Issuance of Long-Term Debt [26] | 618 | 16.228 | 768 | 2.273 | 10.525 | 19.003 | 21.166 | 0 | 0 | 15.673 | 130.027 |
| Repayments of Long-Term Debt [27] | -327 | -1.301 | -668 | -2.684 | -1.553 | -1.590 | -1.258 | -3.676 | -9.182 | -5.021 | -4.021 |
| Net Issuance / (Repayments) of Long-Term Debt [28] | 291 | 14.927 | 100 | -411 | 8.972 | 17.413 | 19.908 | -3.676 | -9.182 | 10.652 | 126.006 |
| Issuance of Common Shares [29] | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| Repurchases of Common Shares [30] | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | -6.000,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| Net Issuance / (Repurchases) of Common Shares [31] | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | -6.000,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| Common Share Dividends Paid [32] | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| Other Financing Activities [33] | -4.007 | -4.999 | -7.786 | -9.655 | -10.695 | -11.325 | -8.189 | -4.655 | -2.712 | -1.885 | -2.014 |
| Cash from Financing Activities [34] | -3.716 | 9.928 | -7.686 | -10.066 | -1.104 | 6.291 | 9.718 | -15.879 | -11.812 | 9.661 | 124.139 |
| Free Cash Flow [36] | 9.399 | 6.410 | 17.296 | 21.653 | 25.924 | -14.726 | -16.893 | 32.217 | 32.878 | 7.695 | -46.892 |
| NOPAT [37] | 2.653 | 3.276 | 11.101 | 12.071 | 20.187 | 21.755 | 18.886 | 29.866 | 59.331 | 64.288 | 81.065 |
| Net Change in Cash [40] | 3.759 | 1.922 | 10.317 | 4.237 | 5.967 | -5.900 | 17.776 | 19.637 | 8.422 | 7.794 | -11.750 |


Se conservan los rótulos nativos para localizar filas. Las tasas, márgenes y crecimientos se presentan como porcentajes; precios y resultados por acción con dos decimales. Los ceros de presentación, especialmente I+D y partidas históricas agregadas, no acreditan inexistencia económica. Las notas de cada celda permanecen en la captura original. Balance K/L incorpora las reclasificaciones de fase 2; no se extienden silenciosamente a otros cierres. Las variaciones operativas agregadas pueden contener componentes distintos del rótulo abreviado.

| Segmento | Ingresos LTMUSDm | Fuente |
|---|---|---|
| North America | 460.255 | WACC!H37:H39 / JSON.segmentos |
| International | 175.818 | WACC!H37:H39 / JSON.segmentos |
| AWS | 161.382 | WACC!H37:H39 / JSON.segmentos |


Los años de proyección son intervalos desde el LTM de partida, no previsiones de cierre fiscal homologadas a cada comunicado. No se anualiza un trimestre como si fuera el LTM ni se mezclan fechas de balance con duraciones de resultados sin identificarlas.

## 3. Ratios y economía del negocio

| Período | Ventas | Margen EBIT | FCF netode PPE | CFO/Ventas | SBC/Ventas | Ventas/acción | Accionesreales |
|---|---|---|---|---|---|---|---|
| Dec '16 | 135.987 | 3,08 % | 10.466 | 12,65 % | 2,19 % | 14,25 | 9.540 |
| Dec '17 | 177.866 | 2,31 % | 8.307 | 10,33 % | 2,37 % | 18,37 | 9.680 |
| Dec '18 | 232.887 | 5,33 % | 19.400 | 13,19 % | 2,33 % | 23,72 | 9.820 |
| Dec '19 | 280.522 | 5,18 % | 25.825 | 13,73 % | 2,45 % | 28,16 | 9.960 |
| Dec '20 | 386.064 | 5,93 % | 31.020 | 17,11 % | 2,39 % | 38,38 | 10.060 |
| Dec '21 | 469.822 | 5,30 % | -9.069 | 9,86 % | 2,72 % | 46,15 | 10.180 |
| Dec '22 | 513.983 | 2,38 % | -11.569 | 9,10 % | 3,82 % | 50,18 | 10.242 |
| Dec '23 | 574.785 | 6,41 % | 36.813 | 14,78 % | 4,18 % | 55,36 | 10.383 |
| Dec '24 | 637.959 | 10,75 % | 38.219 | 18,16 % | 3,45 % | 60,22 | 10.593 |
| Dec '25 | 716.924 | 11,16 % | 11.194 | 19,46 % | 2,72 % | 66,81 | 10.731 |
| LTM Sep '26 | 797.455 | 13,09 % | -42.357 | 21,10 % | 2,49 % | 73,76 | 10.811 |

| CAGR | Intervalos | Resultado | Fuente |
|---|---|---|---|
| FY2022–FY2025 | 3 | 11,73 % | IS!H3:K3 |
| FY2020–FY2025 | 5 | 13,18 % | IS!F3:K3 |
| FY2016–FY2025 | 9 | 20,29 % | IS!B3:K3 |

Cálculo descriptivo: FCF neto de PPE = CFO + compras de propiedad y equipo con signo negativo + ventas e incentivos de PPE. Difiere del FCFF del DCF en impuesto, SBC, reinversión y financiación. Ventas por acción utiliza acciones reales al cierre, no medias diluidas.

Capital operativo nativo actual: 509.241. ROIC nativo actual: 15,92 %. Ventas/capital promedio: 1,5660. Fuentes: Valuation output!B41:B42 e Input sheet!B12. El ROIC actual usa el impuesto histórico; la previsión parte del normalizado. La identidad no resuelve los impuestos asociados a inversiones privadas.

| Período | Reinv.cashproxy | ΔNWCproxy | Δventas/reinv.mismo FY |
|---|---|---|---|
| Dec '23 | 195 | 725 | 311,81 |
| Dec '24 | 24.037 | -826 | 2,63 |
| Dec '25 | 63.899 | 1.335 | 1,24 |
| LTM Sep '26 | 144.345 | 13.041 | N/D—LTM/FYnohomogéneo |


Reinversión proxy = capex bruto − ventas de PPE − D&A + ΔNWC. Faltan adquisiciones operativas depuradas, nuevo activo I+D y altas de leases. El denominador casi nulo de FY2023 se excluye como ancla. Los desgloses históricos incompletos impiden presentar una serie económica homogénea de deuda o ROIC rellenando huecos con ceros.

## 4. Puente contable a económico

| Concepto | Tratamiento R2 | Fuente / reserva |
|---|---|---|
| I+D | B17=No; referencia GAAP provisional | Capitalizaciónpurayhomologación N/Dmaterial. NO significa inexistente; cero ISfila10 es presentación. |
| Leasesreconocidos | 114.783 | BS!L21+L26; no añadir nuevamente VPdelconversor. |
| Financiacióninstalaciones | 426corriente+9300largo, dentrodeuda | Nota4, largo redondeado; no duplicar leases. |
| Deudatotal | 304.461 | L20+L21+L25+L26; reclasificaciónsin alterar totales. |
| Caja+títulos | 114.226 | Input B19/BSL5; restriccionesytributaciónnoajustadas sinpuente. |
| No operativos | 294.595 | Proxybrutocontable; excluircapital B83 y sumarsolo unavez alpatrimonio. Neto fiscal pendiente. |
| RSU | 223,3 millones; ejercicio 0 | Input B38:B42; SBC sigue dentro EBIT y acciones reales10811m. |
| Preferentespropias/minoritarios | 0reportadoconsolidado | No confundir preferentesposeídas con emitidas. |
| Adquisiciones | No asignaciónparticular completada | Compras/inversionesincluyen activosfinancieros: no restar íntegramente comocapexoperativo. Globalstarpendientecierre; no SOTPnuevo. |

Reclamación RSU nativa: 26.560,77 millones. Límite económico de ejercicio cero, ya calculado en F2: 53.670,15. Diferencia por acción: 2,507574; Base diagnóstico: US$ 146,17. No se sustituye ninguna fórmula. Los estados lógicos NO APLICA y VALIDADO no certifican el tratamiento económico.

La falta de conciliación fiscal de los activos privados puede afectar tanto el patrimonio como el denominador del ROIC. No se presume que esta reserva sea independiente o inmaterial respecto de las demás. Tampoco se declara cumplido el límite conjunto de materialidad.

## 5. Supuestos efectivos por historia

| Historia | Prob | Margen | S/C1–5 | S/C6–10 | ROIC terminal | gterminal | DCF hoy |
|---|---|---|---|---|---|---|---|
| Base | 45,0 % | 17,00 % | 0,75 | 1,40 | 12,50 % | 4,00 % | US$ 148,68 |
| Conservadora | 22,5 % | 14,00 % | 0,60 | 1,00 | 10,50 % | 4,00 % | US$ 91,93 |
| Disrupción | 10,0 % | 10,00 % | 0,45 | 0,65 | 9,49 % | 2,00 % | US$ 59,98 |
| Optimista | 22,5 % | 20,00 % | 0,95 | 1,70 | 15,00 % | 4,00 % | US$ 225,33 |

| Historia / fuente | g1 | g2 | g3 | g4 | g5 | g6 | g7 | g8 | g9 | g10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Base / Escenarios e historias!fila5 | 13,90 % | 12,94 % | 11,92 % | 10,52 % | 9,45 % | 8,36 % | 7,27 % | 6,18 % | 5,09 % | 4,00 % |
| Conservadora / Escenarios e historias!fila6 | 8,47 % | 7,94 % | 7,10 % | 6,32 % | 5,73 % | 5,39 % | 5,04 % | 4,69 % | 4,35 % | 4,00 % |
| Disrupción / Escenarios e historias!fila7 | 5,00 % | 5,00 % | 4,00 % | 3,00 % | 2,00 % | 2,00 % | 2,00 % | 2,00 % | 2,00 % | 2,00 % |
| Optimista / Escenarios e historias!fila8 | 16,51 % | 15,75 % | 14,65 % | 13,18 % | 11,35 % | 9,88 % | 8,41 % | 6,94 % | 5,47 % | 4,00 % |

Las historias utilizan Escenarios e historias, filas 5:8 y rangos C29:M29, C53:M53, C77:M77 y C101:M101. Las celdas Input sheet!B27/B29/B32/B33 son referencias legadas. El primer año conserva el margen LTM y los posteriores siguen la convergencia nativa de la hoja.

Impuesto inicial: 22,50 %; terminal: 25,00 %. Desfase inversión/ventas: un año. Convergencia de margen: diez años. Crecimiento estable USD: 4,00 %, salvo Disrupción. Las notas de las entradas contienen procedencia y juicio.

**Discrepancia favorable POR_REVISAR_CALIBRACION:** S3 proyecta crecimiento AWS superior al 40 % para 2027 y 2028. La Base comienza con 35 % y 30 %. Los horizontes fiscales y LTM no son idénticos, y falta un puente que explique la diferencia. La redacción no cambia el modelo ni convierte la guía en ingreso realizado. Cohorte homogénea y consenso del corte: N/D. Fuentes: F2/S1/S3/S6.

## 6. Costo de capital descompuesto

| Componente | Valor | Fuente |
|---|---|---|
| Rf | 4,9400 % | Input sheet!B35 |
| ERPgeográficatotal | 4,9058 % | Cost of capital worksheet!B27 |
| Beta U | 0,808202 | Cost of capital worksheet!B24 |
| Beta L | 0,858362 | Cost of capital worksheet!C58 |
| Ke | 9,1509 % | Cost of capital worksheet!B63 |
| Kdantesimpuestos | 5,3400 % | Cost of capital worksheet!B38 |
| Impuestomarginal | 25,0000 % | Cost of capital worksheet!B39 |
| Equitymercado | 2.598.423,850000 | Cost of capital worksheet!B61 |
| Deudamercadoestimada | 215.026,262138 | Cost of capital worksheet!C61 |
| Peso Equity | 92,3572 % | Cost of capital worksheet!B62 |
| Peso Deuda | 7,6428 % | Cost of capital worksheet!C62 |
| Sumapesos | 1,000000 | Cost of capital worksheet!E62 |
| WACC inicial | 8,7576 % | Cost of capital worksheet!E63 |
| WACC terminal | 9,4900 % | Input sheet!B97 |

Ke = Rf + betaL × ERP. BetaL = betaU × [1 + (1−t)D/E]. BetaU se pondera por ventas × EV/Sales sectorial. Kd combina Rf y spread de cobertura sintética, sin atribuirlo a una agencia. Deuda de mercado = Intereses × [1−(1+Kd)^−duración]/Kd + Deuda contable/(1+Kd)^duración. WACC = Ke × E/(D+E) + Kd × (1−t) × D/(D+E).

ERP madura: 4,55 % = 4,20 % publicada el 1 de octubre + (5,29 % de Rf septiembre − 4,94 % de Rf octubre). Es un juicio de rebase, no una observación de ERP del 30 de octubre. La ponderación geográfica usa los ingresos y CRP documentados en F2 y la tabla Country. El resto internacional es un proxy. WACC terminal = Rf + ERP madura = 9,49 %. Beta de regresión y error estándar: N/D.

La evidencia macro de fase 3 contextualiza el riesgo y no reemplaza las entradas de valoración. La tasa de fondos federales y el Treasury a diez años tienen definiciones y plazos distintos.

## 7. Proyección explícita anual completa

### Base — ventas, rentabilidad y reinversión

| Año | Ventas | g | Margen | EBIT | t | NOPAT | Reinv | FCFF |
|---|---|---|---|---|---|---|---|---|
| 1 | 908.341 | 13,90 % | 13,09 % | 118.878 | 22,50 % | 92.130 | 156.748 | -64.617 |
| 2 | 1.025.902 | 12,94 % | 13,87 % | 142.292 | 22,50 % | 110.276 | 162.990 | -52.714 |
| 3 | 1.148.144 | 11,92 % | 14,26 % | 163.739 | 22,50 % | 126.898 | 160.973 | -34.076 |
| 4 | 1.268.874 | 10,52 % | 14,65 % | 185.921 | 22,50 % | 144.089 | 159.817 | -15.728 |
| 5 | 1.388.737 | 9,45 % | 15,04 % | 208.917 | 22,50 % | 161.911 | 154.744 | 7.167 |
| 6 | 1.504.795 | 8,36 % | 15,43 % | 232.264 | 23,00 % | 178.844 | 78.118 | 100.725 |
| 7 | 1.614.160 | 7,27 % | 15,83 % | 255.460 | 23,50 % | 195.427 | 71.237 | 124.190 |
| 8 | 1.713.892 | 6,18 % | 16,22 % | 277.950 | 24,00 % | 211.242 | 62.303 | 148.939 |
| 9 | 1.801.117 | 5,09 % | 16,61 % | 299.143 | 24,50 % | 225.853 | 51.460 | 174.392 |
| 10 | 1.873.161 | 4,00 % | 17,00 % | 318.437 | 25,00 % | 238.828 | 53.519 | 185.309 |


| Año | S/C | Capital final | ROIC capital inicial | WACC | Factor de descuento | VPFCFF |
|---|---|---|---|---|---|---|
| 1 | 0,75 | 665.989 | 18,09 % | 8,76 % | 0,91947557 | -59.414 |
| 2 | 0,75 | 828.979 | 16,56 % | 8,76 % | 0,84543532 | -44.566 |
| 3 | 0,75 | 989.952 | 15,31 % | 8,76 % | 0,77735712 | -26.489 |
| 4 | 0,75 | 1.149.769 | 14,56 % | 8,76 % | 0,71476088 | -11.242 |
| 5 | 0,75 | 1.304.513 | 14,08 % | 8,76 % | 0,65720516 | 4.710 |
| 6 | 1,40 | 1.382.631 | 13,71 % | 8,90 % | 0,60347136 | 60.785 |
| 7 | 1,40 | 1.453.868 | 14,13 % | 9,05 % | 0,55338661 | 68.725 |
| 8 | 1,40 | 1.516.171 | 14,53 % | 9,20 % | 0,50677794 | 75.479 |
| 9 | 1,40 | 1.567.632 | 14,90 % | 9,34 % | 0,46347319 | 80.826 |
| 10 | 1,40 | 1.621.151 | 15,23 % | 9,49 % | 0,42330184 | 78.442 |


Fuente: Valuation output filas 4:16 y 40:42, columnas C:L. Capital final agrega reinversión del mismo año; ROIC de ese año usa capital de inicio. No mezclar ambos denominadores. Un FCFF negativo se mantiene; no se sustituye por cero.

### Conservadora — ventas, rentabilidad y reinversión

| Año | Ventas | g | Margen | EBIT | t | NOPAT | Reinv | FCFF |
|---|---|---|---|---|---|---|---|---|
| 1 | 865.002 | 8,47 % | 13,09 % | 113.206 | 22,50 % | 87.735 | 114.538 | -26.803 |
| 2 | 933.724 | 7,94 % | 13,27 % | 123.904 | 22,50 % | 96.026 | 110.549 | -14.523 |
| 3 | 1.000.054 | 7,10 % | 13,36 % | 133.619 | 22,50 % | 103.555 | 105.287 | -1.733 |
| 4 | 1.063.226 | 6,32 % | 13,45 % | 143.030 | 22,50 % | 110.848 | 101.593 | 9.255 |
| 5 | 1.124.182 | 5,73 % | 13,54 % | 152.256 | 22,50 % | 117.998 | 100.923 | 17.075 |
| 6 | 1.184.735 | 5,39 % | 13,63 % | 161.538 | 23,00 % | 124.384 | 59.709 | 64.675 |
| 7 | 1.244.444 | 5,04 % | 13,73 % | 170.815 | 23,50 % | 130.674 | 58.405 | 72.269 |
| 8 | 1.302.849 | 4,69 % | 13,82 % | 180.021 | 24,00 % | 136.816 | 56.630 | 80.186 |
| 9 | 1.359.479 | 4,35 % | 13,91 % | 189.086 | 24,50 % | 142.760 | 54.379 | 88.381 |
| 10 | 1.413.858 | 4,00 % | 14,00 % | 197.940 | 25,00 % | 148.455 | 56.554 | 91.901 |


| Año | S/C | Capital final | ROIC capital inicial | WACC | Factor de descuento | VPFCFF |
|---|---|---|---|---|---|---|
| 1 | 0,60 | 623.779 | 17,23 % | 8,76 % | 0,91947557 | -24.645 |
| 2 | 0,60 | 734.328 | 15,39 % | 8,76 % | 0,84543532 | -12.278 |
| 3 | 0,60 | 839.615 | 14,10 % | 8,76 % | 0,77735712 | -1.347 |
| 4 | 0,60 | 941.208 | 13,20 % | 8,76 % | 0,71476088 | 6.615 |
| 5 | 0,60 | 1.042.131 | 12,54 % | 8,76 % | 0,65720516 | 11.222 |
| 6 | 1,00 | 1.101.839 | 11,94 % | 8,90 % | 0,60347136 | 39.030 |
| 7 | 1,00 | 1.160.244 | 11,86 % | 9,05 % | 0,55338661 | 39.993 |
| 8 | 1,00 | 1.216.874 | 11,79 % | 9,20 % | 0,50677794 | 40.636 |
| 9 | 1,00 | 1.271.253 | 11,73 % | 9,34 % | 0,46347319 | 40.962 |
| 10 | 1,00 | 1.327.808 | 11,68 % | 9,49 % | 0,42330184 | 38.902 |


Fuente: Valuation output filas 55:67 y 91:93, columnas C:L. Capital final agrega reinversión del mismo año; ROIC de ese año usa capital de inicio. No mezclar ambos denominadores. Un FCFF negativo se mantiene; no se sustituye por cero.

### Disrupción — ventas, rentabilidad y reinversión

| Año | Ventas | g | Margen | EBIT | t | NOPAT | Reinv | FCFF |
|---|---|---|---|---|---|---|---|---|
| 1 | 837.328 | 5,00 % | 13,09 % | 109.584 | 22,50 % | 84.928 | 93.036 | -8.109 |
| 2 | 879.194 | 5,00 % | 12,47 % | 109.635 | 22,50 % | 84.967 | 78.151 | 6.816 |
| 3 | 914.362 | 4,00 % | 12,16 % | 111.197 | 22,50 % | 86.178 | 60.957 | 25.220 |
| 4 | 941.793 | 3,00 % | 11,85 % | 111.625 | 22,50 % | 86.510 | 41.857 | 44.652 |
| 5 | 960.629 | 2,00 % | 11,54 % | 110.892 | 22,50 % | 85.941 | 42.695 | 43.247 |
| 6 | 979.841 | 2,00 % | 11,23 % | 110.085 | 23,00 % | 84.765 | 30.149 | 54.616 |
| 7 | 999.438 | 2,00 % | 10,93 % | 109.201 | 23,50 % | 83.539 | 30.752 | 52.787 |
| 8 | 1.019.427 | 2,00 % | 10,62 % | 108.237 | 24,00 % | 82.260 | 31.367 | 50.893 |
| 9 | 1.039.815 | 2,00 % | 10,31 % | 107.192 | 24,50 % | 80.930 | 31.994 | 48.936 |
| 10 | 1.060.612 | 2,00 % | 10,00 % | 106.061 | 25,00 % | 79.546 | 32.634 | 46.912 |


| Año | S/C | Capital final | ROIC capital inicial | WACC | Factor de descuento | VPFCFF |
|---|---|---|---|---|---|---|
| 1 | 0,45 | 602.277 | 16,68 % | 8,76 % | 0,91947557 | -7.456 |
| 2 | 0,45 | 680.428 | 14,11 % | 8,76 % | 0,84543532 | 5.763 |
| 3 | 0,45 | 741.385 | 12,67 % | 8,76 % | 0,77735712 | 19.605 |
| 4 | 0,45 | 783.243 | 11,67 % | 8,76 % | 0,71476088 | 31.916 |
| 5 | 0,45 | 825.938 | 10,97 % | 8,76 % | 0,65720516 | 28.422 |
| 6 | 0,65 | 856.086 | 10,26 % | 8,90 % | 0,60347136 | 32.959 |
| 7 | 0,65 | 886.838 | 9,76 % | 9,05 % | 0,55338661 | 29.211 |
| 8 | 0,65 | 918.205 | 9,28 % | 9,20 % | 0,50677794 | 25.792 |
| 9 | 0,65 | 950.200 | 8,81 % | 9,34 % | 0,46347319 | 22.680 |
| 10 | 0,65 | 982.834 | 8,37 % | 9,49 % | 0,42330184 | 19.858 |


Fuente: Valuation output filas 159:171 y 195:197, columnas C:L. Capital final agrega reinversión del mismo año; ROIC de ese año usa capital de inicio. No mezclar ambos denominadores. Un FCFF negativo se mantiene; no se sustituye por cero.

### Optimista — ventas, rentabilidad y reinversión

| Año | Ventas | g | Margen | EBIT | t | NOPAT | Reinv | FCFF |
|---|---|---|---|---|---|---|---|---|
| 1 | 929.131 | 16,51 % | 13,09 % | 121.599 | 22,50 % | 94.239 | 154.003 | -59.764 |
| 2 | 1.075.435 | 15,75 % | 14,47 % | 155.614 | 22,50 % | 120.601 | 165.799 | -45.198 |
| 3 | 1.232.944 | 14,65 % | 15,16 % | 186.929 | 22,50 % | 144.870 | 171.040 | -26.170 |
| 4 | 1.395.431 | 13,18 % | 15,85 % | 221.210 | 22,50 % | 171.438 | 166.692 | 4.745 |
| 5 | 1.553.789 | 11,35 % | 16,54 % | 257.054 | 22,50 % | 199.217 | 161.572 | 37.645 |
| 6 | 1.707.282 | 9,88 % | 17,23 % | 294.249 | 23,00 % | 226.572 | 84.450 | 142.122 |
| 7 | 1.850.847 | 8,41 % | 17,93 % | 331.787 | 23,50 % | 253.817 | 75.551 | 178.266 |
| 8 | 1.979.283 | 6,94 % | 18,62 % | 368.493 | 24,00 % | 280.054 | 63.682 | 216.372 |
| 9 | 2.087.543 | 5,47 % | 19,31 % | 403.078 | 24,50 % | 304.324 | 49.119 | 255.205 |
| 10 | 2.171.044 | 4,00 % | 20,00 % | 434.209 | 25,00 % | 325.657 | 51.083 | 274.573 |


| Año | S/C | Capital final | ROIC capital inicial | WACC | Factor de descuento | VPFCFF |
|---|---|---|---|---|---|---|
| 1 | 0,95 | 663.244 | 18,51 % | 8,76 % | 0,91947557 | -54.952 |
| 2 | 0,95 | 829.043 | 18,18 % | 8,76 % | 0,84543532 | -38.212 |
| 3 | 0,95 | 1.000.083 | 17,47 % | 8,76 % | 0,77735712 | -20.343 |
| 4 | 0,95 | 1.166.775 | 17,14 % | 8,76 % | 0,71476088 | 3.392 |
| 5 | 0,95 | 1.328.347 | 17,07 % | 8,76 % | 0,65720516 | 24.741 |
| 6 | 1,70 | 1.412.797 | 17,06 % | 8,90 % | 0,60347136 | 85.767 |
| 7 | 1,70 | 1.488.347 | 17,97 % | 9,05 % | 0,55338661 | 98.650 |
| 8 | 1,70 | 1.552.030 | 18,82 % | 9,20 % | 0,50677794 | 109.653 |
| 9 | 1,70 | 1.601.148 | 19,61 % | 9,34 % | 0,46347319 | 118.281 |
| 10 | 1,70 | 1.652.232 | 20,34 % | 9,49 % | 0,42330184 | 116.227 |


Fuente: Valuation output filas 106:118 y 142:144, columnas C:L. Capital final agrega reinversión del mismo año; ROIC de ese año usa capital de inicio. No mezclar ambos denominadores. Un FCFF negativo se mantiene; no se sustituye por cero.

## 8. Valor terminal y puente hasta la acción

| Historia | NOPAT11 | g | ROIC | WACC | Reinversión11 | FCFF11 | TV | VPterminal | VPflujos1–10 |
|---|---|---|---|---|---|---|---|---|---|
| Base | 248.381 | 4,00 % | 12,50 % | 9,49 % | 79.482 | 168.899 | 3.076.488 | 1.302.283 | 227.256 |
| Conservadora | 154.393 | 4,00 % | 10,50 % | 9,49 % | 58.816 | 95.577 | 1.740.925 | 736.937 | 179.090 |
| Disrupción | 81.137 | 2,00 % | 9,49 % | 9,49 % | 17.099 | 64.037 | 854.971 | 361.911 | 208.750 |
| Optimista | 338.683 | 4,00 % | 15,00 % | 9,49 % | 90.315 | 248.367 | 4.523.998 | 1.915.017 | 443.203 |

| Historia | EV | −Deuda | +Caja | +No operativos | −RSU | Equitycomún | Acciones | Valor hoy |
|---|---|---|---|---|---|---|---|---|
| Base | 1.529.539 | 304.461 | 114.226 | 294.595 | 26.561 | 1.607.338 | 10.811 | US$ 148,68 |
| Conservadora | 916.027 | 304.461 | 114.226 | 294.595 | 26.561 | 993.826 | 10.811 | US$ 91,93 |
| Disrupción | 570.661 | 304.461 | 114.226 | 294.595 | 26.561 | 648.461 | 10.811 | US$ 59,98 |
| Optimista | 2.358.220 | 304.461 | 114.226 | 294.595 | 26.561 | 2.436.019 | 10.811 | US$ 225,33 |

| Historia | PVterminal/EV | Fuente |
|---|---|---|
| Base | 85,14 % | Valuationoutput!B21/B26 |
| Conservadora | 80,45 % | Valuationoutput!B72/B77 |
| Disrupción | 63,42 % | Valuationoutput!B176/B181 |
| Optimista | 81,21 % | Valuationoutput!B123/B128 |

TV = FCFF11/(WACC terminal−g). Reinversión11 = NOPAT11×g/ROIC terminal. El descuento utiliza productos de tasas anuales. Minoritarios y preferentes siguen el tratamiento de F2. MOS sobre Base = US$ 148,68×0,65 = US$ 96,64; fuente Resumen de Valoración!D36. No extender el MOS al promedio o a otros escenarios.

El Base nativo y el diagnóstico de RSU no son intercambiables. El peso del terminal mantiene su alerta. Las salidas de esta sección se leen de la captura; no se recalcula el DCF en el artículo.

## 9. Escenarios y ciclos

| Historia | Previa | Ajuste | Final | Valor hoy |
|---|---|---|---|---|
| Base | 45,0 % | 0pp; sincrucedisparadordocumentado | 45,0 % | US$ 148,68 |
| Conservadora | 22,5 % | 0pp; sincrucedisparadordocumentado | 22,5 % | US$ 91,93 |
| Disrupción | 10,0 % | 0pp; sincrucedisparadordocumentado | 10,0 % | US$ 59,98 |
| Optimista | 22,5 % | 0pp; sincrucedisparadordocumentado | 22,5 % | US$ 225,33 |

Promedio ordinario = (pBase×VBase + pCons×VCons + pOpt×VOpt)/(pBase+pCons+pOpt) = US$ 153,65. Fuente: Escenarios e historias!I5/I6/I8 y H10. Disrupción queda fuera. Las probabilidades no se modifican por el diagnóstico editorial.

| Plano | Dato/lecturaal corte | Transmisióna Amazon | Estado |
|---|---|---|---|
| Damodaran | Crecimientomaduro; resultados e inversión propios | Demanda,nuevocapital,ROIC terminal | Previa F2conservada |
| Actividad | PIBQ3 3.4%SAAR; Q2 2.2%;29-oct | Consumo ypresupuestos declientes | Dato M2; no tasa de ventas nominales |
| Inflación | IPCsept3.7%yoy; subyacente2.6% | Costo ymezcla deconsumo | Dato M3; períodoidentificado |
| Monetario | FOMCmantiene3.75–4.00%;28-oct | Financiacióncapacidad ydescuento | M1; no trayectoria completa |
| Crédito | SLOOSjulio publicado3-ago; C&Iestableyconsumomixto | Clientes,vendedoresydemanda | M4rezagado; noviembreaún N/D |
| Marks/psicología | Cotizaciónsupera Base R2; sentimientoposicionamiento N/D | Exigencia deexpectativas ydistancia alvalor | Inferenciaacotada, noextremodemercadocertificado |


| Indicador | Actual / fuente | Base/Optimista | Cons/Disrupción |
|---|---|---|---|
| Crecimiento AWS | 39.3% Q3, S3 | Base:25–35% próximo año; Optimista≥35% durante4trimestres | Conservadora<25%; Disrupción<15% durante4trimestres |
| Margen AWS | 38.7% Q3, S3 | Base≥30%; Optimista≥35% sostenible sin excluir SBC | Conservadora<28%; Disrupción<20% durante4trimestres |
| Margen EBIT consolidado | 13.09% LTM; ISL12/L3 | Base avanza hacia17% a10años; Optimista20% | Conservadora estanca14%; Disrupción cae≤10% |
| Reinversión económica cash-proxy | 144,345 USDm LTM; CFS L4,L7:L16 | Base productividad mejora con capacidad y ventas, sin reducircapex artificialmente | Dos años inversión>150000m sin crecimiento comparable favorecen Conservadora |
| FCF reportado | −42357 USDm LTM; S1 p34, CFO−capexneto | Base recupera flujo con maduración de capacidad; Optimista antes | Negativo persistente con AWS<15% favorece Disrupción |
| Acciones reales/RSU | 10811m /223.3m; ISL27 y S1Nota6 | Dilución neta≤2% anual; SBC sigue en EBIT | >3% anual durante2años obliga revisarclaims/denominador |
| Inversiones no operativas | 294595 USDm proxy bruto; B84 y S1Nota2 | Realización neta y contratos respaldanvalor; no ingresos operativos duplicados | Deterioro/netotax−20% o más exige recálculo del puente, no castigo WACC adicional |
| Capex y capacidad | Guía2026~220000m,2027mayor; S1/S3 | Ventas/capital0.75 primeros5años,1.4 después si utilización mejora | Capexcrece sin utilización: reducirproductividad y margen, no sumarprimaespecífica |


Los umbrales son prospectivos. No se atribuyen cruces a series de trimestres que no se verificaron. La guía favorable de AWS plantea una revisión de calibración, no un traslado automático de probabilidad.

## 10. Cinco múltiplos prioritarios y complementarios opcionales

| Método | Estado | Peso | Motivo |
|---|---|---|---|
| EV/EBITDA | PENDIENTE_ANCLA | 0% | Métrica positiva; faltan serie histórica de cierres, ajuste por tasas y pares homogéneos. Sector no sustituye ancla por ciclo. |
| EV/FCFF | NO_APLICA_FY3_NEGATIVO | 0% | FCFF FY+3 negativo en las tres historias ordinarias; no fabricar múltiplos. |
| P/E | PENDIENTE_ANCLA_Y_NORMALIZACION | 0% | Interest/Other proyecta media histórica positiva, incluye partidas no operativas; normalizar y obtener ancla independiente. |
| P/FCFE | NO_APLICA_BASE_FY3_NEGATIVO | 0% | Base FY+3 negativo; Cons/Opt positivos con dependencia de Otros ynetborrowing. Sin ancla, peso0. |
| P/OCF | PENDIENTE_ANCLA_Y_NWC | 0% | Positivo, pero NWC es residuo de conciliación del DCF y Otros requiere normalización. Sin ancla independiente. |

### Conservadora — fundamentales nativos
| Método | FY+1 | FY+2 | FY+3 | Múltiplosalida | Precio FY+3 | VP hoy |
|---|---|---|---|---|---|---|
| EV/EBITDA | 187.924,54 | 205.093,29 | 221.973,89 | N/D — anclapendiente | N/D | N/D |
| EV/FCFF | -26.802,87 | -14.523,14 | -1.732,61 | N/D — anclapendiente | N/D | N/D |
| P/E (EPS) | 8,75 | 9,58 | 10,33 | N/D — anclapendiente | N/D | N/D |
| P/FCFE | -7.882,14 | 4.632,06 | 17.463,50 | N/D — anclapendiente | N/D | N/D |
| P/OCF | 97.083,46 | 119.309,69 | 141.663,05 | N/D — anclapendiente | N/D | N/D |

### Base — fundamentales nativos
| Método | FY+1 | FY+2 | FY+3 | Múltiplosalida | Precio FY+3 | VP hoy |
|---|---|---|---|---|---|---|
| EV/EBITDA | 197.340,15 | 231.495,62 | 265.177,71 | N/D — anclapendiente | N/D | N/D |
| EV/FCFF | -64.617,46 | -52.713,86 | -34.075,51 | N/D — anclapendiente | N/D | N/D |
| P/E (EPS) | 9,19 | 11,00 | 12,66 | N/D — anclapendiente | N/D | N/D |
| P/FCFE | -40.923,51 | -26.936,56 | -7.201,04 | N/D — anclapendiente | N/D | N/D |
| P/OCF | 65.475,96 | 94.706,62 | 131.185,12 | N/D — anclapendiente | N/D | N/D |

### Optimista — fundamentales nativos
| Método | FY+1 | FY+2 | FY+3 | Múltiplosalida | Precio FY+3 | VP hoy |
|---|---|---|---|---|---|---|
| EV/EBITDA | 201.856,97 | 249.125,34 | 295.859,62 | N/D — anclapendiente | N/D | N/D |
| EV/FCFF | -59.764,14 | -45.197,73 | -26.169,81 | N/D — anclapendiente | N/D | N/D |
| P/E (EPS) | 9,40 | 12,03 | 14,46 | N/D — anclapendiente | N/D | N/D |
| P/FCFE | -36.192,02 | -18.312,87 | 3.175,49 | N/D — anclapendiente | N/D | N/D |
| P/OCF | 73.306,93 | 109.734,26 | 151.973,70 | N/D — anclapendiente | N/D | N/D |

Métricas en USD millones, excepto EPS en USD por acción. Fuente: Financials Multiples!E:G, filas Base 57/63/72/68/65; desplazamiento −39 para Conservadora y +40 para Optimista. Estas proyecciones no certifican normalización de Otros, NWC o financiación. Sin un múltiplo válido no se obtiene precio relativo ni valor presente, aunque los dividendos de la hoja sean cero.

Los múltiplos de salida J8/J19/J30 permanecen pendientes. Los ceros causados por precios históricos vacíos no son observaciones. Faltan la serie homogénea, ajuste por tasas y anclas independientes. P/S y P/BV son opcionales con peso cero. N/D no equivale a un precio objetivo de cero.

## 11. Sensibilidades DCF y de múltiplos más inverso

### Matriznativa 1 — WACC inicial y g (curva paralela)

| Eje Y/Eje X | 3,00 % | 3,50 % | 4,00 % | 4,50 % | 5,00 % |
|---|---|---|---|---|---|
| 7,76 % | US$ 174,72 | US$ 182,60 | US$ 192,14 | US$ 203,95 | US$ 219,00 |
| 8,26 % | US$ 155,67 | US$ 161,39 | US$ 168,16 | US$ 176,34 | US$ 186,46 |
| 8,76 % | US$ 139,69 | US$ 143,84 | US$ 148,68 | US$ 154,39 | US$ 161,29 |
| 9,26 % | US$ 126,10 | US$ 129,11 | US$ 132,56 | US$ 136,55 | US$ 141,27 |
| 9,76 % | US$ 114,43 | US$ 116,59 | US$ 119,02 | US$ 121,79 | US$ 124,99 |


Fuente Sensibilidad DCF!A5:F10; centro=US$ 148,68. Se leen los 25 resultados de la captura, no se crean en la redacción.

### Matriznativa 2 — ROIC terminal yg

| Eje Y/Eje X | 3,00 % | 3,50 % | 4,00 % | 4,50 % | 5,00 % |
|---|---|---|---|---|---|
| 11,50 % | US$ 136,68 | US$ 139,96 | US$ 143,75 | US$ 148,18 | US$ 153,46 |
| 12,00 % | US$ 138,24 | US$ 141,98 | US$ 146,31 | US$ 151,41 | US$ 157,54 |
| 12,50 % | US$ 139,69 | US$ 143,84 | US$ 148,68 | US$ 154,39 | US$ 161,29 |
| 13,00 % | US$ 141,02 | US$ 145,56 | US$ 150,86 | US$ 157,14 | US$ 164,75 |
| 13,50 % | US$ 142,25 | US$ 147,14 | US$ 152,88 | US$ 159,69 | US$ 167,95 |


Fuente Sensibilidad DCF!A16:F21; centro=US$ 148,68. Se leen los 25 resultados de la captura, no se crean en la redacción.

### Matriznativa 3 — CAGRinicial/delta ymargen

| Eje Y/Eje X | 13,00 % | 15,00 % | 17,00 % | 19,00 % | 21,00 % |
|---|---|---|---|---|---|
| 7,73 % | US$ 103,31 | US$ 119,59 | US$ 135,86 | US$ 152,13 | US$ 168,40 |
| 9,73 % | US$ 105,16 | US$ 123,56 | US$ 141,96 | US$ 160,35 | US$ 178,75 |
| 11,73 % | US$ 107,14 | US$ 127,91 | US$ 148,68 | US$ 169,44 | US$ 190,21 |
| 13,73 % | US$ 109,29 | US$ 132,69 | US$ 156,09 | US$ 179,49 | US$ 202,89 |
| 15,73 % | US$ 111,62 | US$ 137,95 | US$ 164,28 | US$ 190,61 | US$ 216,94 |


Fuente Sensibilidad DCF!A27:F32; centro=US$ 148,68. Se leen los 25 resultados de la captura, no se crean en la redacción.

La matriz nativa A muestra WACC inicial y desplaza toda la curva en paralelo; la B modifica ROIC terminal; la C conserva la forma de las tasas iniciales y desvanece el delta hacia g. La columna g=5 % supera la Rf de 4,94 % y es inadmisible como elección central. Las anchuras de la malla difieren del contrato y siguen pendientes; no se alteran fórmulas para ocultarlo.

### Diagnóstico F2 externo — terminal_wacc_g

| Eje Y/Eje X | 3,50 % | 3,75 % | 4,00 % | 4,25 % | 4,50 % |
|---|---|---|---|---|---|
| 8,49 % | US$ 171,14 | US$ 175,39 | US$ 180,08 | US$ 185,30 | US$ 191,15 |
| 8,99 % | US$ 156,25 | US$ 159,39 | US$ 162,81 | US$ 166,57 | US$ 170,73 |
| 9,49 % | US$ 143,84 | US$ 146,16 | US$ 148,68 | US$ 151,41 | US$ 154,39 |
| 9,99 % | US$ 133,33 | US$ 135,05 | US$ 136,89 | US$ 138,88 | US$ 141,02 |
| 10,49 % | US$ 124,32 | US$ 125,57 | US$ 126,91 | US$ 128,34 | US$ 129,87 |


### Diagnóstico F2 externo — terminal_roic_g

| Eje Y/Eje X | 3,50 % | 3,75 % | 4,00 % | 4,25 % | 4,50 % |
|---|---|---|---|---|---|
| 11,50 % | US$ 139,96 | US$ 141,78 | US$ 143,75 | US$ 145,87 | US$ 148,18 |
| 12,00 % | US$ 141,98 | US$ 144,06 | US$ 146,31 | US$ 148,75 | US$ 151,41 |
| 12,50 % | US$ 143,84 | US$ 146,16 | US$ 148,68 | US$ 151,41 | US$ 154,39 |
| 13,00 % | US$ 145,56 | US$ 148,10 | US$ 150,86 | US$ 153,86 | US$ 157,14 |
| 13,50 % | US$ 147,14 | US$ 149,89 | US$ 152,88 | US$ 156,13 | US$ 159,69 |


### Diagnóstico F2 externo — growth_delta_margin

| Eje Y/Eje X | 14,00 % | 15,50 % | 17,00 % | 18,50 % | 20,00 % |
|---|---|---|---|---|---|
| -2,00 % | US$ 114,36 | US$ 128,16 | US$ 141,96 | US$ 155,76 | US$ 169,55 |
| -1,00 % | US$ 115,91 | US$ 130,57 | US$ 145,23 | US$ 159,90 | US$ 174,56 |
| 0,00 % | US$ 117,53 | US$ 133,10 | US$ 148,68 | US$ 164,25 | US$ 179,83 |
| 1,00 % | US$ 119,22 | US$ 135,75 | US$ 152,29 | US$ 168,83 | US$ 185,36 |
| 2,00 % | US$ 120,99 | US$ 138,54 | US$ 156,09 | US$ 173,64 | US$ 191,19 |


Los tres diagnósticos ya calculados en F2 son externos. No sustituyen las matrices nativas. Aíslan WACC terminal con inicial constante, ROIC terminal y crecimiento/margen con los rangos indicados. Sus centros concilian con el Base, pero no acreditan la corrección del perfil de plantilla.

| Métodoprioritario | Matriz Base5×5 | Ejes/centro | Razón |
|---|---|---|---|
| EV/EBITDA | N/D o NO APLICA | No haymúltiploelegidoy VP3válidos | Métrica positiva; faltan serie histórica de cierres, ajuste por tasas y pares homogéneos. Sector no sustituye ancla por ciclo. |
| EV/FCFF | N/D o NO APLICA | No haymúltiploelegidoy VP3válidos | FCFF FY+3 negativo en las tres historias ordinarias; no fabricar múltiplos. |
| P/E | N/D o NO APLICA | No haymúltiploelegidoy VP3válidos | Interest/Other proyecta media histórica positiva, incluye partidas no operativas; normalizar y obtener ancla independiente. |
| P/FCFE | N/D o NO APLICA | No haymúltiploelegidoy VP3válidos | Base FY+3 negativo; Cons/Opt positivos con dependencia de Otros ynetborrowing. Sin ancla, peso0. |
| P/OCF | N/D o NO APLICA | No haymúltiploelegidoy VP3válidos | Positivo, pero NWC es residuo de conciliación del DCF y Otros requiere normalización. Sin ancla independiente. |


### DCF inverso: diagnóstico externo heredado
| Campo | Resultado |
|---|---|
| Preciofijo/fecha | US$ 240,35 /2026-10-30 |
| Variable | Deltacomúnaditivo en g1..g5; reconverge6..10,terminalfijo |
| Intervalo | [−9,+35]pp; barrido441puntos |
| Raízseleccionada | 16,636884pp |
| CAGRBase5años | 11,733329 % |
| CAGRimplícito | 28,371715 % |
| Precioreconstruido | US$ 240,35 |
| Error USD/acción | -8.527e-14 |
| Cruceslocalizados | 1 |
| Límite | Condicional aotrosinputs; no expectativas de mercado observadas; nodato nativo |


## 12. Trazabilidad, reconciliaciones y límites

| Historia | Salida | Errorrecálculo previo | Alcance |
|---|---|---|---|
| Base | US$ 148,68 | 0.000e+00 | Resultado de fase 2 conservado; no reejecuta DCF |
| Conservadora | US$ 91,93 | -2.842e-14 | Resultado de fase 2 conservado; no reejecuta DCF |
| Disrupción | US$ 59,98 | -1.421e-14 | Resultado de fase 2 conservado; no reejecuta DCF |
| Optimista | US$ 225,33 | -8.527e-14 | Resultado de fase 2 conservado; no reejecuta DCF |

Los centros de las tres matrices nativas son US$ 148,68. Error máximo del recálculo previo de sus celdas: 8.527e-14. Las probabilidades suman 1,0000. El hash de la captura está en la identificación y en el manifiesto del expediente.

La prueba heredada de F2 comparó 20.740 fórmulas exactas en exportación y D12 idéntica de forma nativa: 20.741 fórmulas conservadas, con 46 pestañas en el mismo orden. Se hereda la evidencia y su alcance; no se afirma haber repetido los comandos oficiales. Esta fase solo realiza lecturas de la hoja.

Los controles locales comprueban estructura, extensión, anclas, fuentes, fórmulas literales y reproducción de cifras. Son distintos de los workflows completos de catálogo, ponderaciones, integridad, profundidad, no regresión y pruebas de app. Estos últimos requieren un checkout completo y el proceso autorizado de publicación; siguen NO EJECUTADOS en esta fase.

Reservas: defecto RSU con ejercicio cero; I+D sin homologar; valor neto fiscal de activos privados; ERP rebasada; beta, cohortes y anclas pendientes; peso del terminal; guía favorable de AWS sin conciliación; adquisición y compromisos que requieren un puente específico. No se compensan reservas para simular inmaterialidad.

Las conclusiones afectadas se mantienen provisionales. No se promueve a EN_REVISION, no se abre PR ni se declara publicación o auditoría. La preparación editorial no equivale a integración en el catálogo.

### Valuation output!C5

```text
=IF('Input sheet'!$A$1="";"";IF('Escenarios e historias'!$K$5="LISTO";B5*(1+C4);""))
```

### Valuation output!D6

```text
=IF('Input sheet'!$A$1="";"";IF('Escenarios e historias'!$K$5="LISTO";IF(D3>'Input sheet'!$B$31;$C$46;$C$46-(($C$46-$C$6)/'Input sheet'!$B$31)*('Input sheet'!$B$31-D3));""))
```

### Valuation output!C8

```text
=IF('Input sheet'!$A$1="";"";IF('Escenarios e historias'!$K$5="LISTO";'Input sheet'!$B$93;""))
```

### Valuation output!C9

```text
=IF('Input sheet'!$A$1="";"";IF('Escenarios e historias'!$K$5="LISTO";IF(C7>0;IF(C7<B12;C7;C7-(C7-B12)*C8);C7);""))
```

### Valuation output!C10

```text
=IF('Input sheet'!$A$1="";"";IF('Escenarios e historias'!$K$5="LISTO";LET(reinv;IF('Input sheet'!$B$57="No";(D5-C5)/C40;IF('Input sheet'!$B$58=0;(C5-B5)/C40;IF('Input sheet'!$B$58=2;(E5-D5)/C40;IF('Input sheet'!$B$58=3;(F5-E5)/C40;(D5-C5)/C40))));IF(AND(reinv<0;'Input sheet'!$B$98="Sin liberación");0;reinv));""))
```

### Valuation output!C11

```text
=IF('Input sheet'!$A$1="";"";IF('Escenarios e historias'!$K$5="LISTO";C9-C10;""))
```

### Valuation output!H14

```text
=IF('Input sheet'!$A$1="";"";IF('Escenarios e historias'!$K$5="LISTO";G14-($G14-$M14)/5;""))
```

### Valuation output!D15

```text
=IF('Input sheet'!$A$1="";"";IF('Escenarios e historias'!$K$5="LISTO";C15*(1/(1+D14));""))
```

### Valuation output!M10

```text
=IF('Input sheet'!$A$1="";"";IF('Escenarios e historias'!$K$5="LISTO";LET(reinv;M9*(M4/M42);IF(AND(reinv<0;'Input sheet'!$B$98="Sin liberación");0;reinv));""))
```

### Valuation output!B20

```text
=IF('Input sheet'!$A$1="";"";IF('Escenarios e historias'!$K$5="LISTO";B18/(B19-M4);""))
```

### Valuation output!B21

```text
=IF('Input sheet'!$A$1="";"";IF('Escenarios e historias'!$K$5="LISTO";B20*L15;""))
```

### Valuation output!B26

```text
=IF('Input sheet'!$A$1="";"";IF('Escenarios e historias'!$K$5="LISTO";B23*(1-B24)+B25*B24;""))
```

### Valuation output!B27

```text
=IF('Input sheet'!$A$1="";"";IF('Escenarios e historias'!$K$5="LISTO";(IF('Input sheet'!$B$18="Yes";'Input sheet'!$B$16+'Input sheet'!$B$79;'Input sheet'!$B$16))+IF(AND(ISNUMBER('Cost of capital worksheet'!$B$41);'Cost of capital worksheet'!$B$41>0);IF('Input sheet'!$B$116="Incluida en balance y gastos";'Cost of capital worksheet'!$B$44-'Cost of capital worksheet'!$B$41;'Cost of capital worksheet'!$B$44);0);""))
```

### Valuation output!B31

```text
=IF('Input sheet'!$A$1="";"";IF('Escenarios e historias'!$K$5="LISTO";B26-B27-B28+B29+B30;""))
```

### Valuation output!B32

```text
=IF('Input sheet'!$A$1="";"";IF('Escenarios e historias'!$K$5="LISTO";IF('Input sheet'!$B$38="No";0;'Option value'!$B$30);""))
```

### Valuation output!B33

```text
=IF('Input sheet'!$A$1="";"";IF('Escenarios e historias'!$K$5="LISTO";B31-B32-N('Input sheet'!$B$76);""))
```

### Valuation output!B35

```text
=IF('Input sheet'!$A$1="";"";IF('Escenarios e historias'!$K$5="LISTO";B33/B34;""))
```

### Cost of capital worksheet!B24

```text
=IF('Input sheet'!$A$1="";"";IF('Input sheet'!$A$1="";"";IFERROR(IF(B22="Direct Input";B23/(1+(1-B39)*(C61/B61));IF(B22="Single Business(US)";VLOOKUP('Input sheet'!B9;'Industry Averages(US)'!A3:G96;7;FALSE);IF(B22="Multibusiness(US)";K49;IF(B22="Single Business(Global)";VLOOKUP('Input sheet'!B10;'Industry Averages (Global)'!A3:G96;7;FALSE);IF(B22="Multibusiness(Global)";K65;"")))));"")))
```

### Cost of capital worksheet!C54

```text
=IF('Input sheet'!$A$1="";"";IF('Input sheet'!$A$1="";"";IFERROR(B32*(1-(1+B38)^(-B33))/B38+B31/(1+B38)^B33;"")))
```

### Cost of capital worksheet!C58

```text
=IF('Input sheet'!$A$1="";"";IF('Input sheet'!$A$1="";"";IFERROR(IF(B22="Direct Input";B23;B24*(1+(1-B39)*(C61/B61)));"")))
```

### Cost of capital worksheet!B63

```text
=IF('Input sheet'!$A$1="";"";IF('Input sheet'!$A$1="";"";IFERROR(B25+C58*B28;"")))
```

### Cost of capital worksheet!E63

```text
=IF('Input sheet'!$A$1="";"";IF('Input sheet'!$A$1="";"";IFERROR(B62*B63+C62*C63+D62*D63;"")))
```
