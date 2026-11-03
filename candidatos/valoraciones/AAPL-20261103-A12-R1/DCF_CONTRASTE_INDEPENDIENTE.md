# AAPL FY2026 — CONTRASTE DCF INDEPENDIENTE — PROVISIONAL, NO PUBLICABLE

**Advertencia:** cálculo externo y NO el DCF nativo de la hoja JMR. Es un instrumento de prueba de coherencia, no una valoración EN_REVISION ni dato apto para catalogo.json. Debe cotejarse con el resultado de 46 pestañas, el WACC Detailed y el puente de la hoja, y modificar juicios si la evidencia lo requiere. Método de juicio A-1.2, fuente de datos SEC; corte mercado 2-nov y 10-K 3-nov no son sincrónicos.

## Datos observados

Fuente: https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm

- Ventas FY26 **478.834** USD millones; FY25 416.161 (+15,06%).
- EBIT GAAP FY26 **158.063**; I+D FY26 **45.765**; I+D tres años antes 34.550,31.370,29.915; con `R& D converter!F7=3` activo 79.255, amortización 31.945, ajuste EBIT +13.820. EBIT ajustado **171.883**, margen inicial **35,89616%**. Amortización de I+D y reinversión recurrentes NO se pueden contar dos veces.
- Caja y marketable securities FY26 **136.935** =36.305 caja +20.417 valores corrientes +80.213 valores no corrientes. Se computan **TODOS como excedentes SOLO EN ESTE CONTRASTE**; falta validar `Input!B83:B87` (cuánto es caja operativa/plusvalías/valor mercado/solape).
- Deuda en libros incl leases **94.479** =11.903 short +68.208 long +2.254 leases current +12.114 leases long, sin nueva capitalización. **No representa necesariamente deuda a valor de mercado**.
- Proxy equity bridge: caja–deuda **+42.456** M. Acciones outstanding 14.532,259 M, sin nuevos RSUs/warrants; la dilución está PENDIENTE.
- Precio de cierre 2-nov **338,32** USD, dato de mercado no usado para escoger los inputs. Fuente https://investor.apple.com/stock-price/default.aspx; el 10-K FY26 se publicó posteriormente (3-nov). Rehacer precio/múltiplos al corte definitivo.
- Fiscal tasa año1 **17%** y converge lineal hasta 21% año10. Federal 21% no igual a marginal de empresa internacional, **juicio/proxy**.
- WACC inicial **9,45%**; transición lineal a terminal **9,32%**, ambas **hipótesis externas no homologadas**; g terminal Base/C/O 4% nominal USD, terminal disrupción1%; ROIC terminal escenario varía. Tasa US10Y 2-nov=4,91%, pero ERP Damodaran noviembre requiere comprobar paridad temporal y premium regional, método Detailed y deuda a mercado.

## Convención aritmética reproducible

Para cada año t=1..10, ventas anteriores S_prev y crecimiento h_t:

`S_t=S_prev*(1+h_t)`

`EBIT_t=S_t*MargenAjustado_t`

`TasaFiscal_t=0.17+(0.21-0.17)*t/10`

`NOPAT_t=EBIT_t*(1-TasaFiscal_t)`

`Reinv_t=(S_t-S_prev)/SalesToCapital_t`

`FCFF_t=NOPAT_t-Reinv_t` (observación: partida R&D y reemplazo de inversión deben conciliar con motor oficial antes de promover).

`WACC_t=.0945+(.0932-.0945)*t/10`

`DF_t=PROD_{k=1}^t(1+WACC_k)`

`PV_op=sum(FCFF_t/DF_t)`

`S_11=S_10*(1+g_terminal)`

`NOPAT_11=S_11*MargenTerminal*(1-.21)`

`Reinv_11=NOPAT_11*g_terminal/ROIC_terminal`

`TV_10=(NOPAT_11-Reinv_11)/(WACC_terminal-g_terminal)`

`EV=PV_op+TV_10/DF_10`

`ValorAccion=(EV+42456)/14532.259`

`MOS35=ValorAccion*0.65`

**Este esquema simplifica varias partidas del FCFF JMR nativo y NO demuestra la conciliación económica total.**

## Cuatro historias: juicio inicial, NO números oficiales

| Historias | Crecimiento 1–5 | 6–10 | EBIT aj. año 5 →10 →terminal | S/C marginal 1–5 / 6–10 | ROIC terminal | g term |
|---|---:|---|---|---|---:|---:|
| Conservador | 4%/año | 4/4/4/4/4% | 33→31→31% | 1,05 / 1,30 | 12% | 4% |
| **Base** | **7%/año** | 6/5,5/5/4,5/4% | **36,3→36→35,5%** | **1,80 / 2,00** | **15%** | **4%** |
| Optimista | 9,5%/año | 7,5/6,5/5,5/5/4% | 37,5→39→38,5% | 1,70 / 2,00 | 18% | 4% |
| Disrupción | 1%/año | 0/0/0/0/0% | 29→24→24% | 0,85 / 1,00 | 9,5% | 1% |

- **Probabilidades previas empresa madura:** Base50 / Conservadora20 / Optimista20 / Disrupción10%, sujetas a criterios de cambios de 5pp verificables; disrupción **se informa separadamente** y no se confunde con el promedio usual.
- Base: iPhone/ecosistema estable, servicios creciendo a más margen, capacidad de retención; desaceleración visible a largo plazo, pese a FY26 crecimiento15%; prudencia NO está duplicada en el Base.
- Conservador: hardware desacelera y margen de servicios presionado por regulación/sustitutos, menor productividad de inversión.
- Optimista: servicios/ecosistema y funcionalidades IA capturan mayor valor sin perder escala; requiere contraevidencia sobre gasto IA y distribución.
- Disrupción: margen operativo contraído por cambio competitivo/regulatorio/cadena de abastecimiento, ventas estancadas.

### Precio estimado EXTERNO por acción (USD, no JMR oficial)

| Historia | Valor externo aproximado | MOS35% externo | EV USD M | PV flujos 1–10 | PV terminal | % EV terminal |
|---|---:|---:|---:|---:|---:|---:|
| Conservador | 125,73 | 81,73 | 1.784.718 | 861.683 | 923.035 | 51,7% |
| **Base** | **174,52** | **113,44** | **2.493.755** | **1.087.836** | **1.405.919** | **56,4%** |
| Optimista | 215,80 | 140,27 | 3.093.547 | 1.217.540 | 1.876.007 | 60,6% |
| Disrupción | 82,46 | 53,60 | 1.155.839 | 732.972 | 422.867 | 36,6% |

Un resultado de 174,52 **NO es un nuevo objetivo de precio oficial ni un resultado de la hoja**; un error material en WACC, fiscalidad, equity bridge, ventas capitalizadas u opciones puede moverlo de forma relevante. No se publica hasta reconciliarlo.

## Sensibilidad 5×5 externa (WACC terminal × ROIC terminal; Base) — USD por acción

**No sustituye las tres matrices NATIVAS obligatorias JMR.** Margen, crecimiento, g=4% y puente constantes; WACC inicial siempre WACCterminal +0,13pp, matriz ordenada por ROIC terminal [12, 13,5, 15, 16,5, 18]%.

| WACC terminal | ROIC12% | ROIC13,5% | ROIC15% | ROIC16,5% | ROIC18% |
|---|---:|---:|---:|---:|---:|
| 8,32% | 200,24 | 206,84 | 212,11 | 216,43 | 220,03 |
| 8,82% | 181,24 | 186,88 | 191,40 | 195,09 | 198,17 |
| **9,32%** | **165,73** | **170,61** | **174,52** | **177,72** | **180,39** |
| 9,82% | 152,82 | 157,09 | 160,50 | 163,29 | 165,62 |
| 10,32% | 141,89 | 145,65 | 148,65 | 151,11 | 153,16 |

### Datos de mercado observados FY26 (NO múltiplos de salida)

Con precio338,32 a 2-nov, EV=precio×14.532,259M acciones + deuda94.479 − caja136.935 (proxies):
- P/E GAAP ≈ **37,20×** (NI 132.175).
- P/OCF ≈ **33,88×** (CFO145.097).
- EV/EBITDA GAAP ≈ **28,42×** (EBIT158.063+D&A13.423).
- **NO** hay objetivos certificados por EV/FCFF, P/FCFE, o cinco múltiplos FY+3; se requiere `Financials Multiples` nativo, normalización, anclas de ciclo y factores de descuento.
- DCF inverso de contraste: manteniendo todos estos supuestos excepto la tasa, el precio338,32 requiere WACC terminal ≈ **6,64%**, no prueba de que tal costo sea correcto; mostrar sensibilidad y no calibrar hipótesis al precio.

## Auditoría independiente pendiente

1. Estimar ERP y beta bottom-up por mix de negocio/regiones al 3-nov, calcular Ke, Kd y WACC Detailed en la hoja **sin escritura manual de B36**.
2. Recalcular activos no operativos a valor de mercado y caja operativa vs caja excedente y deuda leases ya contabilizada. La diferencia puede ser material.
3. Ajustar impuestos marginales por geografía y partidas no recurrentes, acciones básicas/RSU/opciones.
4. Reconciliar reinversión ajustada I+D/Capex/CT, lag0 vs lag1 con DCF completo (NO solo primer flujo) y RONIC vs ROIC.
5. Calcular los cinco múltiplos prioritarios y anclas FY+1/2/3; comparar los cuatro escenarios **nativos** y centros de sensibilidad contra el DCF Base; controles financieros y CI.
6. La nueva revisión debe cerrar las F1–F3 y F4, archivo histórico y pruebas de producción para publicación `EN_REVISION`. Mientras tanto `CANDIDATO`.
