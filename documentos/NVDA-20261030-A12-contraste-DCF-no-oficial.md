# NVDA · Contraste DCF cuantitativo de investigación — 30-oct-2026

**BORRADOR INDEPENDIENTE — NO ES MODELO JMR A-1.2 OFICIAL, NO PUBLICAR.** La cifra presentada es una prueba de hipótesis construida desde el `Input sheet` actual y el último informe SEC. No sustituye al DCF activo, no recalcula el motor oficial, no realiza auditoría económica y no altera la app.

## 1. Fuente histórica y ciclo de la empresa

- Fuente: [SEC del emisor](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm); [hoja histórica](https://docs.google.com/spreadsheets/d/1gbtwORZsvjhZNCV8xlNDloHYEeE09cEbXmPZOoLJ8gY/edit), fecha financiera 26-jul-2026. La fecha de precio de la ficha es **23-oct-2026** y US$210.96 es **precio congelado**, no cotización de hoy.
- Semiconductores IA experimentan superciclo de demanda de centros de datos: ingresos del 2T FY27 US$96.221 millones, +106% interanual, y guía Q3 US$108.000 millones ±2%. No basta extrapolar el pico: clientes hiperescaladores tienen su propio ciclo de gasto en centros de datos, restricciones de exportación, sustitución tecnológica y eventual presión de margen. La convergencia de ROIC marginal debe reflejar duración de moat de software/ecosistema y normalización del ciclo.
- Para lectura de política monetaria y crédito: WACC/Ke debe contrastarse con tasa libre de riesgo, ERP/CRP, spreads, riesgo de demanda y shocks de capital. Las sensibilidades de WACC no implican que el nivel actual sea validado.

## 2. Entradas del histórico y puente patrimonial

| Entrada (USD millones, salvo acciones) | Valor |
|---|---:|
| Ventas LTM | 302,970.00 |
| Acciones (millones) | 24,268.00 |
| Caja/negociables | 99,369.00 |
| Activos no operativos capturados | 39,257.00 |
| Deuda económica | 38,860.00 |
| NCI | 0.00 |
| Pasivo legal de hoja (no conciliado) | 0.00 |
| Opciones (valor de hoja no conciliado) | 0.00 |
| Tasa marginal modelada | 25.37% |

**Limitaciones de puente y ajustes**: La valoración guardada incorpora capitalización económica de I+D, deuda por arrendamientos, acciones RSU y un ajuste de activos no operativos que este benchmark **no reproduce**. Shares 24.268 millones reflejan supuesto anterior que hay que conciliar con recompras/dilución al corte. El valor terminal depende críticamente de márgenes 55% y ROIC 27,23%, no es un hecho histórico.

## 3. Supuestos por historia (juicio, no guía oficial)

| Historia | Crec. año 1 | Crec. años 2-5 | Margen EBIT año 5 → año 10 | S/C año 1-5 → 6-10 | ROIC terminal | WACC inicio → terminal | g terminal | DCF/acción proxy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Conservador | 45.00% | 20.00% | 49.00% → 43.00% | 1.60 → 0.70 | 18.00% | 12.30% → 10.20% | 3.00% | US$131.08 |
| Base | 70.00% | 28.95% | 58.69% → 55.00% | 2.00 → 0.60 | 27.23% | 11.44% → 8.99% | 4.00% | US$406.02 |
| Optimista | 85.00% | 34.00% | 63.00% → 57.00% | 2.50 → 0.80 | 30.00% | 10.80% → 8.80% | 4.00% | US$633.23 |
| Disrupción | 25.00% | 8.00% | 35.00% → 32.00% | 1.50 → 0.60 | 12.00% | 13.00% → 11.00% | 2.00% | US$47.97 |

- **Benchmark Base: US$406.02**, MOS35%: **US$263.91**; ficha previa (NO sustituida): **US$381.79**, diferencia relativa del benchmark 6.35%. Por diferencias de tratamientos contables, NO usar esta variación como prueba del valor justo.
- Valor terminal Base equivale a 76.81% del enterprise value proxy. La historia Disrupción es independiente, no entra al promedio del Base.

## 4. Proyección Base año a año

| Año | g ingresos | Ventas | Margen EBIT | EBIT | Reinversión S/C | FCFF | WACC anual |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 70.00% | 515,038.95 | 69.19% | 356,340.84 | 106,034.48 | 159,902.70 | 11.44% |
| 2 | 28.95% | 664,128.49 | 66.56% | 442,063.98 | 74,544.77 | 255,367.58 | 11.17% |
| 3 | 28.95% | 856,375.33 | 63.94% | 547,556.77 | 96,123.42 | 312,518.20 | 10.90% |
| 4 | 28.95% | 1,104,272.32 | 61.31% | 677,081.63 | 123,948.49 | 381,357.53 | 10.62% |
| 5 | 28.95% | 1,423,928.64 | 58.69% | 835,712.12 | 159,828.16 | 463,863.80 | 10.35% |
| 6 | 23.96% | 1,765,070.45 | 57.95% | 1,022,901.96 | 570,756.61 | 192,635.12 | 10.08% |
| 7 | 18.97% | 2,099,875.04 | 57.21% | 1,201,429.94 | 560,153.95 | 336,473.22 | 9.81% |
| 8 | 13.98% | 2,393,414.36 | 56.48% | 1,351,710.34 | 491,113.95 | 517,667.48 | 9.53% |
| 9 | 8.99% | 2,608,569.08 | 55.74% | 1,453,967.31 | 359,970.47 | 725,125.34 | 9.26% |
| 10 | 4.00% | 2,712,911.84 | 55.00% | 1,492,101.51 | 174,573.50 | 938,981.86 | 8.99% |

**Fórmulas utilizadas (y límites):** Ventas(t)=Ventas(t-1)×(1+g(t)); EBIT(t)=Ventas(t)×margen(t); Reinversión(t)=ΔVentas(t)/S-C(t); FCFF(t)=EBIT(t)×(1−tasa marginal)−Reinversión(t). PV(FCFF)=Σ FCFF(t)/∏(1+WACC(k)); Terminal FCFF(11)=NOPAT(11)×(1−g/ROIC); TV(10)=FCFF(11)/(WACCterminal−g); Precio=[PV(FCFF)+PV(TV)+caja+activos no operativos−deuda−NCI−pasivo legal−opciones]/acciones. g(6–10), WACC(1–10) y márgenes se interpolan linealmente. Este proxy **no contiene ajustes de capitalización de I+D, amortización, restructuración de leasing ni dilución nueva** de la plantilla original; por eso no es valor JMR A-1.2.

## 5. Matriz WACC terminal × ROIC terminal (US$/acción, Base)

| WACC/ROIC | 12.00% | 16.00% | 20.00% | 24.00% | 28.00% |
|---|---:|---:|---:|---:|---:|
| 7.99% | 415.02 | 454.50 | 478.19 | 493.98 | 505.26 |
| 8.49% | 372.54 | 406.83 | 427.40 | 441.12 | 450.91 |
| 8.99% | 338.56 | 368.71 | 386.81 | 398.87 | 407.48 |
| 9.49% | 310.75 | 337.54 | 353.61 | 364.33 | 371.98 |
| 9.99% | 287.57 | 311.57 | 325.97 | 335.57 | 342.43 |

## 6. Matriz margen EBIT terminal × Sales-to-Capital años 1-5 (US$/acción, Base)

| Margen / S/C | 0.30x | 0.50x | 0.70x | 1.00x | 2.00x |
|---|---:|---:|---:|---:|---:|
| 49.00% | 272.65 | 316.84 | 335.78 | 349.98 | 366.55 |
| 52.00% | 292.38 | 336.57 | 355.51 | 369.71 | 386.28 |
| 55.00% | 312.12 | 356.30 | 375.24 | 389.44 | 406.02 |
| 58.00% | 331.85 | 376.04 | 394.98 | 409.18 | 425.75 |
| 61.00% | 351.58 | 395.77 | 414.71 | 428.91 | 445.48 |

## 7. Sensibilidad de múltiplos justificados, sin inventar comparables

- `EV/FCFF(11) = 1/(WACCterminal−gterminal)`: Base **20.05x**.
- `EV/NOPAT(11) = (1−gterminal/ROICterminal)/(WACCterminal−gterminal)`: Base **17.10x**.
- Son ratios justificados de cierre **NO** EV/EBITDA, P/E ni cotizaciones de terceros. Para matriz oficial EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF por año 1–3 hacen falta denominadores reconciliados, anclas sectoriales/históricas verificables, tasas descuento y puente acciones/deuda. P/BV y P/S no son bloqueantes.
- El DCF inverso y sensibilidades WACC×g, ROIC×g, crecimiento×margen y S/C×margen deben recalcularse desde la plantilla, no aproximarse con mero cambio de etiqueta.

## 8. Aceptación y estado

Se requiere **copia de la plantilla oficial, datos SEC reconciliados, inputs explícitos, cuatro historias consistentes, R&D/leases/ROIC terminal, anclas de múltiplos, 5×5 DCF/múltiplos y pase CI**. Solo entonces sustituir revisión activa por una nueva **EN_REVISION**, conservando históricos conforme al catálogo; auditoría económica después de la auditoría visual del usuario. **Este documento NO certifica ninguno de esos candados.**
