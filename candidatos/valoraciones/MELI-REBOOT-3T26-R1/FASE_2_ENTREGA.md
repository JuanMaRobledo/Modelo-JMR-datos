# MELI-REBOOT-3T26-R1 · Fase R2 (históricos)

- **Fecha:** 2026-11-10 · **Agente:** Claude (Code, nube): SEC XBRL (companyfacts, 10-K FY2025 y 10-Q 3T-2026), Alpha Vantage, Google Sheets. Estado **CANDIDATO**.
- **Libro:** 01 HISTÓRICOS `15Z4mnTqLAm05V0svSMbKS1jZB9VEMKRwCO6z4GwvyPI`. Evidencia: `R2_evidencia/` (`meli.py` con los tags usados, `payload_MELI.json` con lo escrito, `fuentes_MELI.json` con el tag y la factura de cada fila).

## Qué se cargó
Income Statement, Balance Sheet, Cash Flow Statement (FY2016–FY2025 + LTM al 30-sep-2026), entradas auxiliares (inventarios; saldos iniciales para FY2016 y LTM), precios de cierre en `Trailing Valuation`, `Guía y empresa` y `Fuentes y clasificación`. Solo se escribieron entradas; ratios, márgenes, eficiencia, salud financiera y por acción son las fórmulas de la plantilla (las leí: sin errores). LTM = FY2025 + 9M-2026 − 9M-2025: ingresos 38.523 (= 28.893 + 29.764 − 20.134, verificado contra el 10-Q), EBIT 2.859 (= 3.201 + 1.970 − 2.312).

## Clasificación (decisiones mías; detalle en `Fuentes y clasificación`)
- **Ingresos** = «ingresos netos y financieros» (incluye intereses de la cartera de crédito). FY2019–FY2020 usan `RevenueFromContractWithCustomer…` (sin tag `Revenues`).
- **Costo de ingresos** incluye costos de envío, costo de ventas de productos, comisiones de cobranza, impuestos sobre ventas y los **costos de fondeo de la cartera fintech** (lo dice el 10-Q). Por eso el EBIT ya está después del costo del financiamiento del crédito.
- **Otros gastos operativos (derivado)** = provisión para cuentas incobrables (3.091 FY2025; 4.845 LTM) y otros. La provisión del trimestre es 12,5 % de los ingresos.
- **Balance:** fondos por pagar a clientes (17.400), montos por pagar de tarjetas (5.464) y efectivo restringido (14.559) están en «otros» y **no son deuda ni caja corporativa**. La cartera (préstamos 12.451 + 589, tarjetas 9.055 + 145) está en «otros activos corrientes/no corrientes». «Préstamos y otras obligaciones financieras» (6.909 + 6.281) están en deuda CP/LP **provisionalmente**: ver el hallazgo siguiente.
- **Flujo operativo** inflado por fondos de clientes y cartera: 13.896 LTM frente a utilidad neta de 1.890. MELI mismo reporta un «flujo libre ajustado» (9M-2026: 443) que descuenta clientes, cambios de cartera y préstamos fintech, porque considera esos pasivos «el capital de trabajo del negocio fintech».
- **SBC (F5)** = gasto del plan LTRP liquidado en efectivo (tag `StockOptionPlanExpense`), no acciones.

## Hallazgo que cambia el tratamiento acordado (R1)
En R1 el usuario eligió un solo FCFF consolidado, con los préstamos y obligaciones financieras como **deuda**. Al leer el 10-Q se ve que el EBIT ya descuenta el costo de fondeo del crédito (está en «costo de ingresos y gastos financieros») y que el emisor trata ese fondeo como capital de trabajo operativo. Restar ese financiamiento como deuda **doble cuenta** su costo. Para R3 propongo el tratamiento consistente: **deuda del puente = solo deuda corporativa y de comercio** (notas 2031/2033/2036 = 2.253 y arrendamientos financieros 116, total ≈ 2.369) y fondeo del crédito (bancos, bills y certificados, deuda colateralizada, notas comerciales, etc., ≈ 10.8 mil M) como pasivo operativo. Esto es una salvedad material para R6 (no se puede separar con certeza el fondeo corporativo del fintech con las etiquetas XBRL). Si el usuario prefiere restar todo como deuda, hay que sumar de vuelta el costo de fondeo al EBIT; no se hizo.

## Controles
| Control | Estado |
|---|---|
| Balance cuadra (A = L+E) en los 11 períodos | APROBADO (diferencia 0) |
| CFO + CFI + CFF vs Δ caja (con restringida) | PARCIAL: la diferencia es el efecto cambiario; 938 en FY2023, −143 LTM |
| LTM reproducido contra el texto del 10-Q (ingresos, EBIT, utilidad antes de impuestos) | APROBADO |
| Comparabilidad FY2016–FY2018 (estructura de costos distinta: margen bruto 64 % → 48 %) | PARCIAL, declarada |
| Gasto por intereses (F15): sin tag us-gaap | PARCIAL, derivado de la diferencia EBIT → utilidad antes de impuestos |
| Verificación documental fila por fila contra los 10-K | NO_EJECUTADO |
| `AISLAMIENTO=OK` | Verificado: solo SEC XBRL, 10-K/10-Q y precios de mercado; el archivo Floyd/A-1.2 de MELI no se usó |

**PASOS 3/3.** Siguiente paso exacto: R3, escribir tres historias de MELI con evidencia del 10-Q (mercados, crédito, margen, costo de capital), cargar los tres `Input sheet` y correr el motor original.
