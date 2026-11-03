# AMZN · Fase 2 — históricos financieros completos (JMR A-1.2 R5)
**Fecha de ejecución:** 2026-11-02. **Estado:** `CANDIDATO_HISTORICOS_COMPLETOS`, cerrado con controles económicos y scripts oficiales pendientes. **No publicado. No merge.**
**Una única revisión:** `AMZN-20261102-A12-R5`, en [Hoja Google Sheets R5](https://docs.google.com/spreadsheets/d/199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I/edit), carpeta `Análisis/AMZN`, 46 pestañas. No se utilizaron datos/escenarios/precios de R2, R3 ni R4. Se partió exclusivamente de [FASE_1_ENTREGA.md](FASE_1_ENTREGA.md) y [INVENTARIO_ENTRADAS_F1.md](INVENTARIO_ENTRADAS_F1.md), sin reemplazar los DCF ni escenarios de F1.

## 1. Cobertura efectiva y correspondencia de las hojas
- **10 ejercicios fiscales 2016–2025:** `Income Statement!B:K` (resultados, interés, impuesto firmado, EBIT, ni, acciones básicas/diluidas); `Balance Sheet!B:K` (activos, caja, inversiones bursátiles, inventarios, AR & others, PPE, goodwill, leases, deuda corriente/largo, equity); `Cash Flow Statement!B:K` (NI, D&A, SBC, ajustes, CFO, CAPEX bruto, incentivos, compra/venta de inversiones, CFI, CFF, FX, variación de caja). `Entradas históricas auxiliares!B3:K3` enlaza inventario nativo; resto de saldos de apertura `B17:K30` a `Balance Sheet` original.
- **Apertura anterior al primer FY:** 31-dic-2015, `Entradas históricas auxiliares!B17:B30` (activos64747, equity13384, deuda corriente238, leases corrientes3126, deuda LT8227, leases LT5948, caja+inversiones19808, AP20397, inventarios10243, PPE21838, goodwill3759, pasivo corriente33887). No se fabricó cuenta de AR netas puras (SEC dice «Accounts receivable, net and other»). Usar el balance FY2015 **reexpresado en el 10-K de 2016** en vez de una versión antigua de 2015 que difiere en clasificación.
- **FY2026 LTM al 30-sep-2026:** `Income Statement!L`, `Balance Sheet!L`, `Cash Flow Statement!L` ya construidos en F1; comparables 9M2025 columna M y 9M2026 columna N; fórmula 12 meses `FY2025+9M2026−9M2025` para resultados y flujo LTM SEC directo, **no FY2026 completo**.
- **Apertura propia del LTM:** balances 30-sep-2025 del 10-Q Q3 2025 en `Entradas históricas auxiliares!L17:L30`: activos727921, equity369631, deuda corriente **4498** = deuda que vence3997 + préstamos cortos220 + financiación281, leases corrientes13321, deuda LT57942 = deuda LT50742 + financing obligations7200, lease LT84677, caja+valores94197, cuentas por pagar106032, inventarios41494, PPE324435, goodwill23260, pasivos corrientes195196. Inventarios cierre 30-sep-2026 `L3` es fórmula `='Balance Sheet'!L9`. **No sustituir la apertura Sep2025 por Dec2025**.
- **Cierres bursátiles FY fechados y ajustados split 20:1:** `Trailing Valuation!B3:K3`: 2016=37,4935; 2017=58,4735; 2018=75,0985; 2019=92,3920; 2020=162,8460; 2021=166,7170; 2022=84,00; 2023=151,94; 2024=219,39; 2025=230,82 USD. `L3` precio del 30-oct-2026 USD240,35 (F1), **no FY2026**. Acciones históricas emitidas y promedio EPS armonizadas para split a través de `Income Statement!B25:K27`, sin pegar EPS.
- **Métricas derivadas** se recalculan con fórmulas nativas: `Márgenes`, `Eficiencia de capital` (ROIC, ROA, ROE, ciclos), `Salud Financiera`, `Por acción`, `Financials Multiples`, `Trailing Valuation`, `Múltiplos históricos`. Se conservaron intactas las fórmulas núcleo del DCF, escenarios y sensibilidades.

## 2. Fuente primaria por tramo
| Período | Fuente | URL |
|---|---|---|
| FY2015 apertura, nota leases exacta | Amazon 2016 10-K y 2015 10-K como precisión de leases | [2016 10-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872417000011/amzn-20161231x10k.htm), [2015 10-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872416000172/amzn-20151231x10k.htm) |
| FY2016–2018 operaciones y cash flow | Amazon 2018 10-K (comparables retrospectivos FY2016/17) | https://www.sec.gov/Archives/edgar/data/1018724/000101872419000004/amzn-20181231x10k.htm |
| FY2016–17 balance y desglose de deuda/leases | 2017 10-K, junto con nota 2016 más exacta | https://www.sec.gov/Archives/edgar/data/1018724/000101872418000005/amzn-20171231x10k.htm |
| FY2018 balance, debt/lease | Amazon 2018 10-K | https://www.sec.gov/Archives/edgar/data/1018724/000101872419000004/amzn-20181231x10k.htm |
| FY2019–20 tres estados y ASC842 | Amazon 2020 10-K | https://www.sec.gov/Archives/edgar/data/1018724/000101872421000004/amzn-20201231.htm |
| FY2021 resultados y cash flows, FY2020 comparativo, FY2022 y FY2021 balance | Amazon 2022 10-K | https://www.sec.gov/Archives/edgar/data/1018724/000101872423000004/amzn-20221231.htm |
| FY2023–25, notas posteriores | Amazon 2025 10-K y 2024 10-K | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm |
| 30-sep-2025 balance de apertura LTM | Amazon 2025 Q3 10-Q | https://www.sec.gov/Archives/edgar/data/1018724/000101872425000123/amzn-20250930.htm |
| LTM30-sep-2026, 9M2025/26 | Amazon 2026 Q3 10-Q | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm |
| Precios split-adjusted a último cierre FY | Macrotrends tabla anual y SEC historical secondary offering para comprobación 2016/17 | https://www.macrotrends.net/stocks/charts/AMZN/amazon/stock-price-history y https://www.sec.gov/Archives/edgar/data/312070/000110465918014950/a18-7371_47424b2.htm |

Cada dato escrito en Sheets tiene **nota de celda** con período, URL, signo/clasificación. Sin importar datos de otras empresas ni historial de AMZN R4.

## 3. Serie histórica verificada (USD millones, salvo ROIC)
| FY | Ventas | EBIT GAAP | NI GAAP | CFO | CAPEX bruto (salida) | ROIC fórmula |
|---|---:|---:|---:|---:|---:|---:|
| 2016 | 135987 | 4186 | 2371 | 17203 | 7804 | 21,37% |
| 2017 | 177866 | 4106 | 3033 | 18365 | 11955 | 12,00% |
| 2018 | 232887 | 12421 | 10073 | 30723 | 13427 | 24,01% |
| 2019 | 280522 | 14541 | 11588 | 38514 | 16861 | 17,73% |
| 2020 | 386064 | 22899 | 21331 | 66064 | 40140 | 20,80% |
| 2021 | 469822 | 24879 | 33364 | 46327 | 61053 | 14,97% |
| 2022 | 513983 | 12248 | −2722 | 46752 | 63645 | 8,99% |
| 2023 | 574785 | 36852 | 30425 | 84946 | 52729 | 11,58% |
| 2024 | 637959 | 68593 | 59248 | 115877 | 82999 | 19,24% |
| 2025 | 716924 | 79975 | 77670 | 139514 | 131819 | 15,94% |
| LTM sep-2026 | 797455 | 104366 | 134779 | 168300 | 215192 | 13,07% |

**Importante:** NI de 2021/22 distorsionado por revaloración de Rivian; NI 2025/2026 por ganancias/perdidas de inversiones de Anthropic/OpenAI. No usar NI GAAP LTM como ganancia operativa normalizada (fase 3).

## 4. Conciliaciones independientes efectivamente ejecutadas (API Google Sheets + cálculos externos a fórmulas)
- Para **cada uno de los 10 FY**: `Ventas - COGS - SG&A - R&D_PROXY - Otros gastos = EBIT GAAP`: 10/10 diferencia **0**. El ingreso neto se concilia incluyendo actividad de inversiones en método de participación **después de impuesto**, sin forzar `EBT+Tax=NI` cuando la fuente presenta rubro adicional; FY2022 NI negativa se conserva.
- Para **cada uno de los 10 FY**: `NI+D&A+SBC+Ajustes+ΔAR+ΔAP+ΔAccrued+ΔDeferred+Otros(inventario y otros)=CFO`; `CAPEX bruto + incentivos + compras y ventas de inversiones + otros=CFI`; `CFO+CFI+CFF+FX=variación caja`: 10/10 por cada identidad, diferencia **0 USD M**.
- Para **cada uno de los 10 balances FY**: `Activos corrientes`, `Activos totales`, `Pasivo corriente`, `Pasivo total+equity=activos`: 10/10 por identidad, diferencia **0**; FY2015 apertura y Q3 2025 contrastados aparte con SEC.
- **Precio FY y shares:** 10/10 FY tienen precio fechado normalizado y acciones split adjusted. FY2016-19 acciones pre-split x20, FY2020/21 usan cifras reexpresadas del 10-K 2022. No mezclar splits ni precios contemporáneos.
- **Verificación ROIC/ROE/ROA directa independiente en FY2024, FY2025 y LTM Sep2026**: coincide a precisión de cálculo con `Eficiencia de capital!J/K/L3:5`; ROIC 19,2371% → 15,9376% → 13,0740%; ROA 10,2794% /10,7656%/13,6740%; ROE 24,2897%/22,2858%/27,4155%. Los ROIC contienen capital invertido promedio con deuda/lease/caja, no afirmación de economía normalizada.
- **Inventario:** `Entradas históricas auxiliares!B3:K3` y `L3` son referencias a balance, no cifras pegadas; turnover del inventario y márgenes se computan. FY2016 apertura inventarios 10243; LTM apertura Sep2025 inventarios41494.
- **Errores visibles** `#ERROR`, `#REF`, `#DIV/0` en las regiones inspeccionadas de los estados y sensibilidades: **0 detectados**. DCF F1 **NO cambió** tras F2: Base149,1914858; Conservador81,0095172; Optimista241,8435161; Disrupción62,4357315. WACC 8,1796%, I+D capitalizada proxy activo78943,15; escenarios `LISTO` y tres matrices centrales DCF `OK`. El ponderado general continúa en blanco por los tres múltiplos F1 pendientes, como debe ser.
- **Scripts oficiales del motor** `estados_completos.py`, `auditar_estados_sec.py`, `auditar_ceros_materiales.py`, `diff_formulas_plantilla.py`, `candados.py` **NO EJECUTADOS** desde su runtime autenticado. Esta auditoría API es **equivalencia parcial documentada**, no CI completa ni certificación.

## 5. Clasificación de datos no publicados y cambios contables — NO rellenar con cero
- **I+D:** `Technology & Content / Technology & Infrastructure` es gasto agregado SEC. La reclasificación del **25% como I+D es PROXY ECONÓMICO de F1**, no dato revelado; la contrapartida en `Income Statement!B10:K11` deja EBIT GAAP intacto. No reestimar hasta F3.
- **Cuentas por cobrar:** SEC consolida **Accounts receivable, net and other**, registrado en BS fila6; fila8 para AR comerciales puros queda en blanco (no puede inventarse). En consecuencia DSO, quick ratio y ciclo de caja completo que dependan de la cifra separada quedan **N/D**, sin reemplazo por 0.
- **Intangibles netos:** goodwill separado, otros intangibles no desglosados de modo comparable para los diez balances; filas dependientes de intangibles puros N/D, no cero.
- **Leases pre/post ASC842:** en 2016–18 sólo capital leases/finance leases RECONOCIDOS, current+LT, se extraen de otros pasivos y se evita doble contabilización. Operativos **no se reconocían en BS** antes de 2019; desde 2019 ASC842 incluye activos ROU, leasing operativo+financiero actuales. **No es comparable sin normalización** el ROIC, deuda y lease pasivos 2016–18 vs 2019–25. No se inventó una capitalización retroactiva sin contratos completos.
- **Financing obligations** de instalaciones a largo plazo: SEC algunos años dentro de otros pasivos; se separaron en F1 (2021 en adelante) y en apertura Sep2025; años históricos pre2021 no totalmente reexpresados por indisponibilidad de desglose homogéneo. **Caveat económico en serie de deuda/ROIC** para F3.
- **CFO/CFF históricas reexpresadas:** FY2016–17 usadas comparativas del 2018 10-K (adopciones contables/efecto restricted cash y tax benefit) en lugar de cifras antiguas no comparables. CF 2018–20 toma 2020 10-K, 2021 toma 2022 10-K; amortización y 'other operating' reagrupadas SEC en 2022 sin cambiar CFO.
- **Impuesto efectivo:** signo negativo como gasto (positivo como devolución) preservado en `Income Statement!row20`; diferencias net income vs EBT+tax provienen de **equity-method investment activity net of tax**. Normalización NI excepcional es F3.
- **Acciones preferentes:** SEC «none issued» => cero verificado en `Entradas históricas auxiliares!B5:K5`. **NCI:** cero en presentación del patrimonio consolidado solo como puente, sin afirmar ausencia de intereses contractuales en activos participados.
- **Dividendos comunes:** cero verificado en `Cash Flow Statement!B32:K32` (Amazon 2017 10-K reporta nunca pagados y no hay cash dividends en financiamiento reportado posteriormente); no un relleno de columna genérica.
- **No operativos y EV:** early marketable securities pueden contener participaciones estratégicas (Rivian) además de cash equivalents. Los múltiplos EV históricos deben distinguir cartera financiera de cash líquido antes de considerarse anclas económicas, no se imputa valor económico ficticio de participaciones en 2016–20.
- **Flujos financieros:** FY2016–17 SEC denomina `Proceeds / repayments of long-term debt and other`; se conserva esa agrupación y se asigna el residual a `Cash Flow Statement!row25/33`. No se presenta el residual como deuda de corto plazo puramente bancaria. FY2018–21 mayor separación por SEC; sujeto a refinamiento de FCFE en F3.

## 6. Impacto sobre valoración y criterios para F3
- F2 **no cambió** escenarios, WACC, hipótesis I+D ni resultado de F1 por reflejo. DCF Base US$149,19, MOS35% US$96,97 como candidato, sin publicación.
- El histórico confirma las ventas crecientes (FY2016 135987 → FY2025 716924; CAGR 9 intervalos ≈20,29%) y **ROIC decreciente reciente:** FY2024 19,24%; FY2025 15,94%; LTM Sep2026 13,07%, bajo CAPEX significativamente creciente (FY2024 82999 → FY2025 131819 → LTM 215192). No asumir recuperación sin evidencia operativa. Análisis económico corresponde F3.
- **Ninguna valoración por múltiplos fue promovida:** EV/EBITDA y P/OCF siguen candidatos (F1 VP3 349,74 /179,15); EV/FCFF N/A por proyección negativa; P/E exige normalización de ingresos no recurrentes; P/FCFE ancla inconsistente y motor [issue #199](https://github.com/JuanMaRobledo/JMR-valuation/issues/199). Mantener resumen ponderado en blanco.
- F3 debe evaluar: CAPEX IA y reinversión, Sales-to-Capital 1–5 vs 6–10, ROIC marginal y terminal con clasificación lease pre/post ASC842, márgenes, WACC deuda mercado [issue #197](https://github.com/JuanMaRobledo/JMR-valuation/issues/197), valor de participaciones Anthropic/OpenAI, gastos de SBC+RSUs/dilución, normalización de NI y múltiplos, comparabilidad de deuda y cobros comerciales N/D.
- F4 publicación reservada a gates oficiales y autorización de esa fase. **No se realizó F3, F4, F5, PR merge ni despliegue.**

**Dictamen F2:** `CANDIDATO_HISTORICOS_COMPLETOS`: 10FY + LTM, apertura 2015 y Sep2025 enlazadas, indicadores nativos comprobados, fuentes y clasificaciones auditables, controles directos pasan sin diferencias. Las limitaciones identificadas quedan explícitas y no se fabricaron datos; scripts oficiales todavía no ejecutados, la auditoría económica y publicación quedan pendientes.
