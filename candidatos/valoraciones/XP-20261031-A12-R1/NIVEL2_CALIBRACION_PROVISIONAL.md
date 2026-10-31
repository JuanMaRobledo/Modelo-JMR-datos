# XP — Nivel 2 reproducible · Método A-1.2 / FCFE nominal BRL

**Fecha de análisis:** 31-oct-2026. **Corte de estados:** 30-jun-2026. **Precio referencia:** US$14,29 (30-oct). **Unidad:** reales brasileños millones (FCFE/patrimonio), tasas nominales BRL, FX BRL/USD y USD/acción. **Estado:** candidato, NO publicar.

## 1. Fuentes originales
Estados y presentación 2T26 de XP (SEC), resultado atribuible de 1H26/2025, balances junio 2026, control del histórico 2018–2025 y modelo R2 sin reemplazar. Ingresos LTM R$19.122,419m, utilidad atribuible R$5.316,803m, equity atribuible R$24.831,073m. La serie previa 2018–2022 contiene reconstrucciones que deben completarse con documentos originales antes de certificar comparables a largo plazo.

## 2. Puente de capital y perímetro regulatorio
BIS gerencial 20,3%, CET1 gerencial 17,1%, RWA grupo 126.600m; Pilar3: RWA 99.904,171m, CET1 7.675,252m (7,68%). El motor reusa capital contable de la matriz con el proxy prudencial de un perímetro distinto. **Esta incompatibilidad limita la credibilidad del FCFE distribuible**. La cifra 7,68% es ratio observado, no mínimo legal; se debe obtener requerimiento prudencial y buffer por sociedad. El factor de asignación de patrimonio retenido a CET1 = 50% es un supuesto sujeto a revisión y tiene impacto directo sobre FCFE año 1.

## 3. Tasa de descuento en misma moneda
- Rf USD 10Y (30-oct): **4,94%**; ERP madura Damodaran oct **3,70%**.
- Beta XP analítica (revisión heredada): **0,98**; CRP Brasil julio (Damodaran): **3,10%**. Shock país adicional **2,00%**, supuesto no cotizado, sensibilidad obligatoria.
- Ke USD = Rf + beta×ERP + CRP + shock = **13,67%**.
- Conversión BRL nominal: `KeBRL = (1+KeUSD)×(1+infBRL)/(1+infUSD)-1` = **14,44%**.
- Ke terminal BRL (beta de madurez 1) **14,52%**.
- FX Banco Central do Brasil PTAX 30-oct: **5,42 BRL por USD**. Se aplica al patrimonio final, no a cada flujo si el descuento se hace en BRL.

## 4. Acciones y dilución
Básicas de clase A+B netas de autocartera: 507,48 millones. RSU/PSU pendientes: 17,67 millones; vesting candidato 95,00%. Acciones equivalentes: **524,27 millones**. Debe verificarse plan de incentivos, treasury shares, derechos clases A/B y vesting; evitar doble conteo de SBC y RSU.

## 5. Fórmulas realmente utilizadas
Ingreso[t] = Ingreso[t−1]×(1+g[t]); EBT[t] = Ingresos[t]×margen EBT[t]; impuesto[t] según trayectoria anual; utilidad atribuible[t] = EBT[t]×(1−tasa efectiva[t])×proporción de matriz. RWA[t] crece según g de ingresos y multiplicador del motor 1,0 (hipótesis). Equity requerido se deriva de utilidad atribuible del año posterior y ROE proyectado; reserva regulatoria basada en RWA por ratio objetivo CET1 y capital asignado; retención de capital = mayor entre aumento de patrimonio económico y requerimiento prudencial. **FCFE[t] = utilidad atribuible[t] − retención[t]**.

Para descuento nominal BRL: `factor[t] = producto (1+KeBRL[t])`; `VP FCFE[t]=FCFE[t]/factor[t]`; patrimonio = ΣVP FCFE explícito + VP del terminal; `valor USD/acción = patrimonio(BRL millones)/acciones equivalentes(millones)/FX(BRL/USD)`. Terminal `FCFE11=NI11−g×equity10`, `TV=FCFE11/(KeBRLterminal−g)`, y VP terminal = TV/factor10.

## 6. Cuatro escenarios y probabilidad

| Historia | Probabilidad | DCF USD/acc | MOS35 USD/acc | VP terminal/equity |
|---|---:|---:|---:|---:|
| Base | 45,00% | 14,48 | 9,41 | 44,69% |
| Conservadora | 22,50% | 10,82 | 7,03 | 39,45% |
| Disrupción | 10,00% | 7,31 | 4,75 | 20,77% |
| Optimista | 22,50% | 16,61 | 10,79 | 54,99% |

El promedio ponderado de Base, Conservador y Optimista normalizado por 90% = **US$14,09**; Disrupción 10% se muestra separada. El DCF Base principal candidato = US$14,48, precio con MOS35 = US$9,41. Diferencia frente al mercado US$14,29 = 1,30%; con MOS requerido, no ofrece margen suficiente.

## 7. Proyección FCFE Base 10 años (BRL millones)
| Año | Ingresos | Utilidad atribuible | RWA | Equity requerido | Retención | FCFE | Ke BRL | VP FCFE |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 20.652,21 | 5.722,80 | 107.896,50 | 28.977,84 | 4.146,77 | 1.576,03 | 14,44% | 1.377,12 |
| 2 | 22.717,43 | 6.272,87 | 118.686,16 | 31.299,36 | 2.321,51 | 3.951,36 | 14,44% | 3.016,91 |
| 3 | 24.762,00 | 6.812,23 | 129.367,91 | 33.492,28 | 2.192,93 | 4.619,30 | 14,44% | 3.081,77 |
| 4 | 26.742,96 | 7.328,91 | 139.717,34 | 35.502,25 | 2.009,97 | 5.318,94 | 14,44% | 3.100,68 |
| 5 | 28.614,97 | 7.810,49 | 149.497,56 | 38.269,34 | 2.767,09 | 5.043,40 | 14,44% | 2.568,99 |
| 6 | 30.503,56 | 8.095,50 | 159.364,39 | 41.145,10 | 2.875,76 | 5.219,73 | 14,46% | 2.322,94 |
| 7 | 32.394,78 | 8.355,75 | 169.244,99 | 44.126,95 | 2.981,85 | 5.373,90 | 14,47% | 2.089,18 |
| 8 | 34.273,68 | 8.587,99 | 179.061,20 | 47.213,07 | 3.086,12 | 5.501,87 | 14,49% | 1.868,24 |
| 9 | 36.124,45 | 8.789,18 | 188.730,50 | 50.402,96 | 3.189,89 | 5.599,29 | 14,50% | 1.660,50 |
| 10 | 37.930,68 | 8.956,61 | 198.167,03 | 52.923,11 | 2.520,15 | 6.436,46 | 14,52% | 1.666,78 |

## 8. EV/equity aplicable a financiera
No se calcula EV industrial, no se sustrae deuda de intermediación como si fuese deuda corporativa operativa. **Patrimonio presente Base = R$41.139,99 millones**, con VP explícito R$22.753,10m y VP terminal R$18.386,88m. Divide por 524,27m acciones y por 5,42 BRL/USD para obtener US$14,48.

## 9. Sensibilidad DCF en BRL y salida USD
Tres matrices nativas 5×5: `Ke terminal × g`, `ROE terminal × g`, `Δcrecimiento × margen EBT`. Los ejes se vincularon a los supuestos activos del motor XP, no a números estáticos de la revisión R2. Sus celdas centrales, en USD/acción, concilian con el Base: **US$14,48**. El crecimiento en perpetuidad es 5% para el Base (en BRL nominales), estrictamente inferior a Ke BRL terminal 14,52%; revisar coherencia con inflación nominal de largo plazo y ciclo económico.

## 10. Múltiplos nativos financieros y anclas
Los centros FY+3 descontados a hoy de las cuatro matrices 5×5 actuales son:
- P/E: US$14,70, peso 70,00%. Ancla disponible condicionada.
- P/FCFE: US$14,02, peso 0,00%. No hay ancla independiente para ponderar.
- P/BV: US$13,18, peso 30,00%. Ancla disponible condicionada.
- P/S: US$12,99, peso 0,00%. No hay ancla independiente para ponderar.
Cada celda aplica `((múltiplo×fundamentalFY3/acciones)/factorKe3 + VP_dividendosBRL/acción)/FX`. Se cotejó el centro contra `XP Múltiplos!I[fila]`, con diferencia 0 para P/E, P/FCFE, P/BV y P/S. Los cuatro centros **no deben** coincidir obligatoriamente con el DCF: son métodos secundarios. **P/FCFE tiene peso 0 por falta de ancla histórica independiente** y P/S peso 0 por ser secundario.

## 11. Comparación AZ Stocks
Pendiente cálculo separado de DCF perpetuidad/ROE y salida por múltiplos con supuestos independientes. Para intermediario financiero AZ debe respetar FCFE, Ke BRL y capital regulatorio: no sustituir por FCFF industrial ni EBITDA como método central. No forzar concordancia de valores por modificar Ke o pesos de múltiplos arbitrariamente.

## 12. Pendientes antes de publicación
- Confirmar perímetros de CET1/RWA, mínimo y buffer regulatorio, capacidad de dividendos de cada entidad y holding, y factor 50% de capital retenido.
- Validar el coste de equity: beta .98, prima país julio 3,10% y shock adicional de 2pp discrecional. Ejecutar sensibilidad de shock ±2pp/FX y exposición a tasas locales.
- RSU/PSU, dilución A/B, autocartera y recompra posteriores a junio de 2026.
- Anclas P/E y P/BV independientes, fuente actualizada de P/FCFE si va a ponderar, y verificar matriz Base contra hoja de cada método.
- Cierre de control financiero PR #211 y auditoría visual de la ficha antes de auditoría económica. **El catálogo y la valoración anterior siguen intactos.**

### Referencias
[XP 2T26 SEC](https://www.sec.gov/Archives/edgar/data/1787425/000095010326012481/dp251884_6k-ex9901.htm), [BCB PTAX 30-oct](https://fincast.info/pairs/usd-brl/archive), [Damodaran 2026](https://aswathdamodaran.substack.com/p/country-risk-determinants-measures), [US Treasury](https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield-historical-data), [hoja XP](https://docs.google.com/spreadsheets/d/1C8TU1AJMxy0JmU4KsBNdp1dYzBSoli7CLtnjQI3SsnQ/edit), [snapshot FCFE JSON](./CALIBRACION_FCFE_PROVISIONAL.json).

**Calibración económica candidata; no dictamen de inversión ni publicación.**
