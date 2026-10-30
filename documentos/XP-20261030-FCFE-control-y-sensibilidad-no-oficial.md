# XP · expediente FCFE reproducible de contraste — 30 de octubre de 2026

**Estado:** CONTRASTE DEL EXPEDIENTE FCFE HISTÓRICO, NO nuevo Método A-1.2, NO AUDITORÍA ECONÓMICA, NO LISTO PARA PUBLICAR. No reemplaza `XP-JMR-20261026-R2`, no se modifica ninguna hoja, JSON activo ni catálogo.

## 1. Fuente, empresa, riesgo y ciclo

- Documento de trabajo original: `valoraciones/XP-20261026-R2.json`, escenario de cuatro historias y matrices de sensibilidad ya calculadas; hoja oficial [XP — JMR 20261026 R2](https://docs.google.com/spreadsheets/d/18DYy3HRcy8SCBue16aBoba3ELBZ0pyjoFO472dic0-I/edit).
- [Investor Relations XP](https://investors.xpinc.com/en/): al corte informado 2T26 los activos de clientes eran ~R$1,534 billones, ingresos brutos LTM ~R$20.200 millones y EBT LTM ~R$6.000 millones. **Activos de clientes NO son capital disponible del grupo**.
- Precio de mercado de la ficha: **US$15,37 fechado 26-oct-2026**; no confundir con cotización actual.
- Empresa de servicios financieros y distribución de productos de inversión. Ciclo empresarial: escala de plataforma y transición a oferta diversificada de intermediación; depende de confianza, flujos de clientes, mercado de capitales y ciclo brasileño de tasas/crédito. La transmisión monetaria puede elevar ingresos de cartera mientras reduce nuevos flujos o valor de activos. La volatilidad de BRL/USD y el costo de equity requieren tratamiento separado. Usar ROE, beneficios atribuibles y capital económico y regulatorio; NO EV/EBITDA ni FCFF de industrial.

## 2. Valoraciones históricas reconstruidas del JSON fuente

| Historia | Probabilidad guardada | Ke BRL | g terminal | ROE terminal | FCFE/acción USD |
|---|---:|---:|---:|---:|---:|
| Base · expansión con normalización fiscal | 45.00% | 14.93% | 5.00% | 17.77% | **13.53** |
| Conservadora · presión competitiva y menor retorno | 22.50% | 14.93% | 5.00% | 15.01% | **10.43** |
| Disrupción · Deterioro de los fundamentales | 10.00% | 14.93% | 2.00% | 15.01% | **6.99** |
| Optimista · mayor monetización y escala | 22.50% | 14.93% | 5.00% | 17.77% | **15.38** |

Disrupción se presenta separada y no pondera el valor Base. No interpretar las probabilidades como mediciones estadísticas. El valor intrínseco financiero principal **ya existente** es US$13.53, margen de seguridad del 35% US$8.79. Capitaliza beneficios distribuibles, no utilidad neta total sin deducir capital requerido.

## 3. Puente FCFE Base reconstruido del expediente (BRL millones, salvo acciones)

| Concepto | Fuente guardada | Valor |
|---|---|---:|
| PV FCFE años 1–10 | `escenariosDCF[A].pv_explicit` | 22,263.12 |
| Valor terminal descontado | `escenariosDCF[A].pv_terminal` | 16,757.35 |
| Valor patrimonial | Suma FCFE explícito + TV | 39,020.47 |
| Acciones equivalentes (millones) | `shares_equiv_m` | 524.27 |
| Equity/acción BRL | `value_brl` | R$74.43 |
| Tipo de presentación BRL/USD implícito | `value_brl/value_usd` | 5.50 |
| Precio USD/acción | `value_usd` | US$13.53 |
| PV terminal / equity | `terminal_weight_equity` | 42.95% |
| Ke primer año BRL | `ke_brl` | 14.93% |
| Ke terminal BRL | `keT_brl` | 15.01% |
| ROE terminal | `roeT_effective` | 17.77% |
| Crecimiento perpetuo BRL | `gT` | 5.00% |

**Conciliación aritmética:** PV flujos 22,263.12 + PV terminal 16,757.35 = 39,020.47, frente al equity informado 39,020.47; residuo BRL M 0.00. Precio implícito BRL/acción calculado `Equity / acciones` = R$74.43. Tipo FX es conversión de presentación en el modelo previo, NO escenario cambiario prospectivo.

## 4. Proyección Base (existente y verificable, no recalculada con plantilla nueva)

| Año | Ingresos (BRL M) | g | EBT margen | Beneficio neto (BRL M) | Reinversión (BRL M) | FCFE (BRL M) | ROE objetivo | Capital libro req. | RWA (BRL M) | CET1 proxy |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 20,652.21 | 8.00% | 30.16% | 5,722.80 | 4,146.77 | 1,576.03 | 21.53% | 28,977.84 | 107,896.50 | 9.04% |
| 2 | 22,717.43 | 10.00% | 30.37% | 6,272.87 | 2,321.51 | 3,951.36 | 21.65% | 31,299.36 | 118,686.16 | 9.19% |
| 3 | 24,762.00 | 9.00% | 30.58% | 6,812.23 | 2,192.93 | 4,619.30 | 21.76% | 33,492.28 | 129,367.91 | 9.28% |
| 4 | 26,742.96 | 8.00% | 30.79% | 7,328.91 | 2,009.97 | 5,318.94 | 21.88% | 35,502.25 | 139,717.34 | 9.31% |
| 5 | 28,614.97 | 7.00% | 31.00% | 7,810.49 | 2,767.09 | 5,043.40 | 22.00% | 38,269.34 | 149,497.56 | 9.63% |
| 6 | 30,503.56 | 6.60% | 30.70% | 8,095.50 | 2,875.76 | 5,219.73 | 21.15% | 41,145.10 | 159,364.39 | 9.93% |
| 7 | 32,394.78 | 6.20% | 30.40% | 8,355.75 | 2,981.85 | 5,373.90 | 20.31% | 44,126.95 | 169,244.99 | 10.24% |
| 8 | 34,273.68 | 5.80% | 30.10% | 8,587.99 | 3,086.12 | 5,501.87 | 19.46% | 47,213.07 | 179,061.20 | 10.54% |
| 9 | 36,124.45 | 5.40% | 29.80% | 8,789.18 | 3,189.89 | 5,599.29 | 18.62% | 50,402.96 | 188,730.50 | 10.84% |
| 10 | 37,930.68 | 5.00% | 29.50% | 8,956.61 | 2,520.15 | 6,436.46 | 17.77% | 52,923.11 | 198,167.03 | 10.96% |

**Relaciones que deben comprobarse:** `FCFE_t = Beneficio atribuible_t − reinversión de equity_t`; `PV(FCFE_t) = FCFE_t / producto(1+Ke_BRL,k)`; `FCFE_terminal = NI_terminal × (1 − g/ROE_terminal)`; `TV = FCFE_terminal/(Ke_terminal−g_terminal)`, con distribución de capital limitada por RWA, CET1 y restricciones jurídicas reales. El motor guardado presenta un **CET1 proxy** pero aún no acredita el puente completo de capital consolidado → capital de cada entidad regulada → dividendos remesables.

## 5. Sensibilidades nativas del expediente antiguo: matrices 5×5

### Ke terminal × g (precio por acción USD)

| Nivel y / nivel x | -1.00% | -0.50% | +0.00% | +0.50% | +1.00% |
|---|---:|---:|---:|---:|---:|
| -0.50% | 14.24 | 13.82 | 13.44 | 13.10 | 12.78 |
| -0.25% | 14.31 | 13.88 | 13.49 | 13.13 | 12.81 |
| +0.00% | 14.38 | 13.93 | 13.53 | 13.16 | 12.83 |
| +0.25% | 14.46 | 14.00 | 13.58 | 13.20 | 12.86 |
| +0.50% | 14.54 | 14.06 | 13.63 | 13.24 | 12.88 |

Valor central registrado: **US$13.53**; se contrasta contra FCFE Base **US$13.53**. Desplazamientos (deltas) sobre supuestos del expediente, NO tasas absolutas.

### ROE terminal × g (precio por acción USD)

| Nivel y / nivel x | -2.00% | -1.00% | +0.00% | +1.00% | +2.00% |
|---|---:|---:|---:|---:|---:|
| -0.50% | 12.39 | 12.94 | 13.44 | 13.89 | 14.30 |
| -0.25% | 12.40 | 12.97 | 13.49 | 13.95 | 14.36 |
| +0.00% | 12.42 | 13.00 | 13.53 | 14.00 | 14.43 |
| +0.25% | 12.43 | 13.04 | 13.58 | 14.06 | 14.51 |
| +0.50% | 12.45 | 13.07 | 13.63 | 14.13 | 14.58 |

Valor central registrado: **US$13.53**; se contrasta contra FCFE Base **US$13.53**. Desplazamientos (deltas) sobre supuestos del expediente, NO tasas absolutas.

### Crecimiento de ingresos × margen EBT (precio por acción USD)

| Nivel y / nivel x | -2.00% | -1.00% | +0.00% | +1.00% | +2.00% |
|---|---:|---:|---:|---:|---:|
| -3.00% | 12.64 | 12.88 | 13.11 | 13.34 | 13.56 |
| -1.50% | 12.91 | 13.12 | 13.33 | 13.55 | 13.78 |
| +0.00% | 13.10 | 13.31 | 13.53 | 13.76 | 14.00 |
| +1.50% | 13.28 | 13.50 | 13.73 | 13.97 | 14.23 |
| +3.00% | 13.46 | 13.69 | 13.93 | 14.19 | 14.45 |

Valor central registrado: **US$13.53**; se contrasta contra FCFE Base **US$13.53**. Desplazamientos (deltas) sobre supuestos del expediente, NO tasas absolutas.


## 6. Sensibilidad por múltiplos: criterios económicos

Los múltiplos de validación para una financiera son P/E y P/FCFE y, secundariamente, P/BV con ROE ajustado y capital regulatorio. `P/BV_{justificado}=(ROE-g)/(Ke-g)` solo bajo hipótesis de distribución y crecimiento estables; NO sustituye la conciliación de patrimonio propio. EV/EBITDA y EV/FCFF industriales son **no aplicables**. Los múltiplos ya almacenados no demuestran una matriz de sensibilidades nuevas bajo Método A-1.2; no se deben fabricar comparables ni precios. El P/S tampoco es prioritario.

## 7. Bloqueos concretos antes de rehacer XP con Método A-1.2

1. En la lectura conectada del 30-oct-2026, `Input sheet!A10:D55` y `Resumen de Valoración!A1:H25` contienen rótulos pero **valores vacíos**: la valoración FCFE vive en el JSON independiente, no en la plantilla industrial.
2. Confirmar estados financieros 20-F y último trimestre, consistencia BRL vs USD, acciones equivalentes y estructura de capital.
3. Sustituir asignación proxy del capital regulatorio (no acreditada) por reconciliación regulatoria de CET1, Tier1, RWA, buffers, restricciones por entidad, utilidad remesable.
4. Justificar prima de riesgo Brasil / Ke USD / Ke BRL, crecimiento nominal perpetuo y sensibilidad de ROE terminal a mayor competencia.
5. Reejecutar los cuatro escenarios desde el motor financiero actualizado, con nuevas matrices de sensibilidad FCFE y P/E–P/FCFE y controles técnicos.
6. Tras validación oficial y CI, actualizar una sola ficha como `EN_REVISION`, y dejar la auditoría económica para la revisión visual posterior.

**Resultado de esta operación:** trazabilidad de escenarios y sensibilidades anteriores, no valoración A-1.2 definitiva.
