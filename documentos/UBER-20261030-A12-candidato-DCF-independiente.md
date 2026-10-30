# UBER — candidato cuantitativo de contraste · 30-oct-2026
**Estado:** BORRADOR DE INVESTIGACIÓN, **NO** valoración oficial Método A-1.2; **no publicar** ni modificar el catálogo, la hoja original, la valoración vigente o la auditoría. Este documento añade un benchmark DCF independiente reproducible para decidir los supuestos y reconstruir el expediente oficial. No representa recomendación de compraventa.

## 1. Referencias de fecha y fuentes

- Valuación activa **UBER-REC-20261027-R1** (histórico): DCF Base **US$73,27422321/acción**, MOS35% **US$47,62824509**; precio guardado US$68,51 del **30-sep-2026**. Archivo `valoraciones/UBER-1789655192522.json`; análisis `analisis/UBER-research-1789655244618-k9n7u.json`.
- Hoja vigente **UBER — Valoración JMR vigente**, pestañas `Input sheet` y `Resumen de Valoración`: https://docs.google.com/spreadsheets/d/1R3V8gISxXCYIujVFSITu0svVBC3AsN4GF_pQHHLs5dw/edit. Datos LTM almacenados y precio de referencia histórico, **no actualizados en vivo**.
- Fuente primaria financiera: Uber Q2 2026, 5-ago-2026: https://investor.uber.com/news-events/news/press-release-details/2026/Uber-Announces-Results-for-Second-Quarter-2026/default.aspx y SEC 10-Q https://www.sec.gov/Archives/edgar/data/1543151/000154315126000032/uber-20260630.htm. El beneficio neto de Q2 incorpora aproximadamente US$1.600 M de revalorizaciones de participaciones (resultado no operativo); **no usarlo como EBIT operativo normalizado**.

## 2. Diagnóstico económico previo al recálculo

La plataforma combina movilidad, entrega y Freight. El crecimiento de reservas brutas del 2T26 (24% reportado, 22% a moneda constante) supera al de ingresos (12%), por lo que no debe suponerse una proporción fija entre Gross Bookings e ingresos reconocidos. El ingreso operativo GAAP trimestral fue US$1.890 M sobre ingresos US$14.191 M. Aumentar sostenidamente el margen consolidado del ~12,1% LTM almacenado a 22,29% año 5 y 20% año 10 exige demostrar economías de escala y sostener poder de negociación frente a conductores, comercios y reguladores.

El ciclo de empresa corresponde a una plataforma de escala creciente en fase de monetización y expansión de rentabilidad, no a una startup prebeneficio; su ventaja depende de liquidez de mercado y densidad bilateral, sujeta a inversión en demanda. La fase macro/monetaria importa principalmente por gasto discrecional de viajes, coste de financiación, inflación salarial y efectos cambiarios. La aparición de redes de vehículos autónomos puede capturar economía de intermediación o erosionarla; se modela mediante historias alternativas, no sumando simultáneamente una prima artificial de WACC y una reducción duplicada de margen.

El límite crucial de reinversión es **no sumar** `(ΔVentas / Sales-to-Capital)` al mismo CAPEX neto/cambio de capital de trabajo ya incorporado: ambas son formas alternativas de estimar necesidades. Aquí se adopta exclusivamente el puente marginal sales-to-capital.

## 3. Inputs y trazabilidad (US$ millones salvo porcentaje/acciones)

| Variable | Valor | Naturaleza |
|---|---:|---|
| Ingresos LTM de hoja `Input sheet!B12` | 55,227 | Histórico guardado |
| EBIT LTM `Input sheet!B13` | 6,700 | Histórico guardado |
| Acciones `Input sheet!B22` (millones) | 2,042.56 | Hoja guardada; requiere dilución actualizada |
| Caja/negociables `Input sheet!B19` | 5,391 | Hoja guardada |
| Deuda económica `Input sheet!B16` | 12,723 | Hoja guardada; conciliar leases |
| Participaciones no controladoras `Input sheet!B21` | 1,083 | Hoja guardada |
| Tasa fiscal normalizada usada | 25.00% | Marginal de la hoja, juicio prospectivo |
| Inversión marginal, método explícito | `ΔIngresos / S/C` | Hipótesis, no CAPEX más S/C |
| Crédito por caja extraordinaria/opciones/SBC no validado | **N/D** | No se añade supuesto beneficio |

## 4. Cuatro historias de contraste (no oficiales)

| Historia | Crec. año 1 | Crec. años 2-5 | EBIT margen año 5 / 10 | S/C años 1-5 / 6-10 | ROIC terminal | WACC inicial/terminal | g terminal | DCF proxy por acción |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Conservador | 10.00% | 6.50% | 18.00% / 15.00% | 1.50/1.60 | 10.00% | 11.50% / 10.50% | 3.00% | **US$31.66** |
| Base | 12.90% | 10.46% | 22.29% / 20.00% | 2.20/2.00 | 12.00% | 10.31% / 9.79% | 4.00% | **US$68.24** |
| Optimista | 16.00% | 14.00% | 26.00% / 23.50% | 2.80/2.50 | 16.00% | 9.50% / 9.30% | 4.00% | **US$121.70** |
| Disrupción | 8.00% | 4.00% | 11.00% / 9.00% | 1.20/1.30 | 9.00% | 12.50% / 11.50% | 2.00% | **US$12.08** |

- Valor Base proxy: **US$68.24**, MOS35% **US$44.36**. Contraste con DCF histórico US$73,27: diferencia **-6.87%**. La diferencia **no** demuestra error en la hoja; el modelo original capitaliza I+D, ajusta contratos de arrendamiento y emplea trayectorias propias no replicadas aquí.
- Peso del valor terminal sobre EV Base proxy: **59.50%**, dependencia material de margen y ROIC terminal.
- La historia de disrupción **no** se promedia dentro del Base.

## 5. Proyección Base anual reproducible

| Año | Crecimiento ingresos | Ingresos | Margen EBIT | EBIT | NOPAT | Reinversión | FCFF | WACC anual |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 12.90% | 62,351 | 14.29% | 8,910 | 6,682 | 3,238 | 3,444 | 10.31% |
| 2 | 10.46% | 68,873 | 16.29% | 11,219 | 8,415 | 2,965 | 5,450 | 10.26% |
| 3 | 10.46% | 76,077 | 18.29% | 13,915 | 10,436 | 3,275 | 7,161 | 10.20% |
| 4 | 10.46% | 84,035 | 20.29% | 17,051 | 12,788 | 3,617 | 9,171 | 10.14% |
| 5 | 10.46% | 92,825 | 22.29% | 20,691 | 15,518 | 3,995 | 11,523 | 10.08% |
| 6 | 9.17% | 101,335 | 21.83% | 22,124 | 16,593 | 4,255 | 12,338 | 10.02% |
| 7 | 7.88% | 109,317 | 21.37% | 23,365 | 17,524 | 3,991 | 13,533 | 9.96% |
| 8 | 6.58% | 116,514 | 20.92% | 24,370 | 18,278 | 3,599 | 14,679 | 9.91% |
| 9 | 5.29% | 122,680 | 20.46% | 25,098 | 18,823 | 3,083 | 15,740 | 9.85% |
| 10 | 4.00% | 127,587 | 20.00% | 25,517 | 19,138 | 2,454 | 16,684 | 9.79% |

**Fórmulas efectivas**: `Revenues_t = Revenues_(t-1)*(1+g_t)`; `EBIT_t = Revenues_t*EBIT_margin_t`; `Reinversión_t = (Revenues_t-Revenues_(t-1))/SalesToCapital_t`; `FCFF_t = EBIT_t*(1-tasa fiscal)-Reinversión_t`. `PV(FCFF_t)=FCFF_t/∏(1+WACC_k)`, `NOPAT_11=Revenue_10*(1+g_terminal)*margin_10*(1-tax)`, `FCFF_11=NOPAT_11*(1-g_terminal/ROIC_terminal)`, `TV_10=FCFF_11/(WACC_terminal-g_terminal)`, `EquityValue=EV+Caja-Deuda-NCI`, `Precio=EquityValue/Acciones`. Interpolaciones lineales para WACC años 1–10, margen 1–5 y 6–10, y crecimiento 6–10. No se incorpora por separado D&A, I+D capitalizada, arrendamientos o ajuste adicional de SBC: **limitación material de alcance** de este benchmark.

## 6. Sensibilidad económica del Base

### WACC terminal × ROIC terminal (US$/acción)

| WACC terminal / ROIC terminal | 8% | 10% | 12% | 14% | 16% |
|---|---:|---:|---:|---:|---:|
| 8.79% | 66.59 | 74.76 | 80.21 | 84.10 | 87.02 |
| 9.29% | 61.62 | 68.85 | 73.67 | 77.11 | 79.69 |
| 9.79% | 57.48 | 63.93 | 68.24 | 71.32 | 73.62 |
| 10.29% | 53.97 | 59.79 | 63.66 | 66.43 | 68.50 |
| 10.79% | 50.97 | 56.23 | 59.74 | 62.25 | 64.13 |

### EBIT margen terminal × S/C primeros 5 años (US$/acción)

| Margen / S/C | 1,6x | 1,9x | 2,2x | 2,5x | 2,8x |
|---|---:|---:|---:|---:|---:|
| 16.00% | 55.00 | 56.35 | 57.33 | 58.08 | 58.67 |
| 18.00% | 60.45 | 61.80 | 62.79 | 63.53 | 64.12 |
| 20.00% | 65.90 | 67.26 | 68.24 | 68.99 | 69.57 |
| 22.00% | 71.36 | 72.71 | 73.69 | 74.44 | 75.03 |
| 24.00% | 76.81 | 78.16 | 79.15 | 79.89 | 80.48 |

### Múltiplos *justificados* por fundamentos, no comparables observados

Para FCFF terminal creciente, `EV/FCFF_(11) = 1/(WACC_terminal - g)`: en Base equivale a **17.27x**. Para NOPAT terminal, `EV/NOPAT_(11) = (1-g/ROIC)/(WACC_terminal-g)`: **11.51x**. No confundir con EV/EBITDA ni con múltiplos de empresas comparables; construir sensibilidades propias EV/EBITDA, EV/FCFF, P/E, P/FCFE y P/OCF **tras** conciliar denominadores, pares históricos y puente EV-equity de los años 1–3. P/BV y P/S son complementarios, no bloqueantes.

## 7. Cierre y controles faltantes

Este benchmark no reemplaza la R1, **no queda marcado A-1.2, publicado ni auditado**. Faltan recaptura de 10-Q y precio/acciones al corte 29–30 oct; capitalización I+D y amortización; deuda por arrendamientos sin doble conteo; dilución por SBC; fuente de WACC/CRP y ROIC; reconciliación de FCFF calculado con la hoja oficial; escenarios por la plantilla oficial; 5 sensibilidades de múltiplos prioritarios con bases verificadas y sensibilidad DCF; chequeos de catálogo y gate CI. **Auditoría económica independiente solo después de revisión visual del usuario.**
