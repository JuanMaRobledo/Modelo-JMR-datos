# AMZN · AMZN-20261102-A12-R2 · Fase 2 · CERRADA CON CONTROLES PENDIENTES

Fecha: 2026-11-02 · Herramienta: ChatGPT Work/Codex, Google Sheets, Python y navegación. Modelo: Codex basado en GPT-6 según configuración; variante y nivel de esfuerzo no expuestos de forma verificable. No se atribuye Astra/Sol/Opus.

**sheet_id:** `1h6Xv5cNqwtKPpqI81KiZ_FNpTl4k_uQQS2QJEHphaBI` · **Método:** A/A-1.2 · **Estado:** CANDIDATO · **AISLAMIENTO=OK**.

[Hoja candidata AMZN R2](https://docs.google.com/spreadsheets/d/1h6Xv5cNqwtKPpqI81KiZ_FNpTl4k_uQQS2QJEHphaBI/edit). Cifras financieras en USD millones y acciones en millones; valores por acción en USD. Datos LTM Sep2026; mercado30-oct2026. La revisión no modifica el corte global de Cartera.

## Hecho y verificado (con evidencia)

### 1. Resultado principal y alcance

| Concepto | USD/acción | Evidencia |
|---|---:|---|
| DCF Base nativo provisional | 148.68 | [Cálculo/Dato] Valuation output!B35 / Escenarios!H5 |
| MOS35% sobre Base | 96.64 | [Cálculo/Dato] Resumen!D36 = Base×0.65 |
| Promedio ordinario condicionado a no Disrupción | 153.65 | [Cálculo/Dato] Escenarios!H10 |
| Conservadora | 91.93 | [Cálculo/Dato] Valuation output!B86 |
| Optimista | 225.33 | [Cálculo/Dato] Valuation output!B137 |
| Disrupción aparte | 59.98 | [Cálculo/Dato] Valuation output!B190 |
| Precio fechado | 240.35 | [Cálculo/Dato] Input!D1/B23, S7 |

Son resultados de trabajo con reservas económicas, **no una valoración oficial aprobada**. La corrección diagnóstica del límite de RSU con ejercicio cero lleva el Base a **146.17** y no se ha escrito sobre ninguna salida. Los múltiplos pesan cero por falta de ancla/homologación, no porque se haya probado que el DCF sea exacto. El valor capitalizado FY+3 del Resumen es otro horizonte y no sustituye el valor presente anterior.

### 2. Historia central, drivers y visión externa

Amazon combina comercio de menor margen con nube y servicios de mayor margen. La Base supone que AWS aumenta su peso mientras Norteamérica e Internacional maduran, y que publicidad y eficiencia logística compensan parte de la depreciación y del costo de capacidad. Ese mecanismo permite mejorar el margen GAAP hacia17% en diez años; no exige que el crecimiento reciente de AWS continúe indefinidamente. La amenaza es instalar capacidad antes de disponer de ingresos rentables, junto con presión competitiva en precios. La Base financia el crecimiento y conserva SBC como gasto. [Juicio: S1/S3; Escenarios fila5].

Las tasas por segmento son hipótesis nominales totales: no existe una separación cuantitativa verificable de precio/volumen/FX/adquisiciones para cada tramo. Es un puente top-down declarado, no una predicción por unidades ni consenso. Las inversiones privadas no aportan ingresos ficticios a AWS. Prime Day cambió de trimestre: no se toma el crecimiento trimestral del comercio como tasa estructural sin ajustar calendario. [Dato/Juicio:S3].

| Historia | Norteamérica años 1–5 | Internacional años 1–5 | AWS años 1–5 |
|---|---|---|---|
| Base | 8.0%, 7.0%, 6.5%, 6.0%, 5.5% | 10.0%, 9.0%, 8.0%, 7.0%, 6.0% | 35.0%, 30.0%, 25.0%, 20.0%, 17.0% |
| Conservadora | 4.0%, 4.0%, 3.5%, 3.0%, 3.0% | 5.0%, 5.0%, 4.0%, 4.0%, 3.0% | 25.0%, 20.0%, 17.0%, 14.0%, 12.0% |
| Optimista | 10.0%, 9.0%, 8.0%, 7.0%, 6.0% | 12.0%, 11.0%, 10.0%, 9.0%, 8.0% | 40.0%, 35.0%, 30.0%, 25.0%, 20.0% |

[Cálculo] Cada año se multiplica el ingreso previo de cada segmento por1+g y se suman los tres. El crecimiento consolidado es Total_t/Total_t−1−1. Años6–10 convergen desde g5 hacia4%; Disrupción estabiliza al2%. Los arrays consolidados se verifican en C29:M29/C53:M53/C77:M77/C101:M101, no en las referencias legadas InputB27/B29.

| Historia | Ventas año 5 | AWS año 5 | CAGR consolidado5años |
|---|---:|---:|---:|
| Base | 1,388,737 | 497,061 | 11.73% |
| Conservadora | 1,124,182 | 361,622 | 7.11% |
| Optimista | 1,553,789 | 594,773 | 14.27% |

La visión externa utiliza RetailGeneral US(n23) yComputerServices US(n64), enero2026, como contraste sectorial de beta, margen, ROIC y capital, no como cohorte estadística del tamaño deAmazon. Una cohorte por tamaño, ciclo y perímetro, con supervivientes y fracasos, no está certificada: mediana y percentiles10/25/75/90=N/D. No se inventan cuantiles del BaseRateBook ni consenso. AWS no es una consultora informática; el proxyComputerServices puede subestimar su beta e intensidad de infraestructura. Esta reserva permanece abierta. [S6; IndustryAveragesUS filas22/75].

### 3. Datos y conciliación de deuda, activos y reinversión

| Magnitud | Valor | Celda/documento |
|---|---:|---|
| IngresosLTM | 797,455 | [Dato/Cálculo] Input sheet!B12, S1/S8 |
| EBITLTM | 104,366 | [Dato/Cálculo] Input sheet!B13, S1/S8 |
| InteresesLTM | 4,484 | [Dato/Cálculo] Input sheet!B14, S1/S8 |
| PatrimonioSep2026 | 613,601 | [Dato/Cálculo] Input sheet!B15, S1/S8 |
| Deuda financiera+leases+financiación | 304,461 | [Dato/Cálculo] Input sheet!B16, S1/S8 |
| Caja+títulos | 114,226 | [Dato/Cálculo] Input sheet!B19, S1/S8 |
| Inversiones no operativas brutas | 294,595 | [Dato/Cálculo] Input sheet!B84, S1/S8 |
| Acciones reales al cierre | 10,811 | [Dato/Cálculo] Input sheet!B22, S1/S8 |

Se reclasificaron valores de entrada del balance, conservando activos, pasivos y patrimonio totales. En Sep2026, deuda corriente6827 y financiación corriente426 pasan a L20=7253; leases corrientes15959 a L21. L25=173125+9300=182425; L26=98824. Suma304461. Se reducen los rubros residuales correspondientes, sin duplicar deuda. FY2025 recibe el mismo tratamiento. Los9300/7800 de financiación larga son aproximaciones de cifras publicadas redondeadas, no precisión al millón certificada. [S1Notas3–5; Balance K/L19:27].

Los no operativos294595=146200 convertibles+143700 inversiones privadas+4300 warrants+395 participaciones por equity. Se separan de OtherAssets, se excluyen del capital operativo y se añaden una sola vez al patrimonio. Son activos poseídos porAmazon, no convertibles o preferentes emitidos porAmazon. El proxy económico bruto se iguala al importe contable, pero **no acredita realización neta, impuestos diferidos o liquidez**. Los pasivos fiscales vinculados y cualquier solapamiento con capital operativo requieren conciliación específica antes de aprobar. No se elimina esa reserva porque B85 digaVALIDADO. [S1Nota2; InputB83:B87].

El capital operativo inicial es613601+304461−114226−294595=509241. El ROIC nativo actual usa NOPAT histórico de la hoja; las proyecciones usan22.5% normalizado. No mezclar ambos sin identificar el impuesto. El cociente Ventas/Capital es descriptivo y distinto de S/C marginal. No se usa ΔLTM contra nueve meses para fingir un intervalo anual homogéneo.

| Período | Capex bruto | VentasPPE | D&A | ΔNWC cash-proxy | Reinversión cash-proxy | Δventas/reinv mismoFY |
|---|---:|---:|---:|---:|---:|---:|
| Dec '23 | 52,729 | 4,596 | 48,663 | 725 | 195 | 311.81 |
| Dec '24 | 82,999 | 5,341 | 52,795 | -826 | 24,037 | 2.63 |
| Dec '25 | 131,819 | 3,499 | 65,756 | 1,335 | 63,899 | 1.24 |
| LTM Sep '26 | 215,192 | 4,535 | 79,353 | 13,041 | 144,345 | N/D |

[Cálculo: CFS I:L4,7:16; IS H:L3] Reinversión cash-proxy=capex bruto−ventasPPE−D&A+ΔNWC, con ΔNWC=−Σflujos de variación operativa7:12. No incluye el ajuste I+D, nuevas obligaciones de leases ni adquisiciones operativas depuradas. La fila de compras/adquisiciones contiene inversión financiera: restarla íntegra como capex operativo duplicaría las participaciones. Por ello esta tabla es diagnóstico, no S/C económico certificado. FY2023 tiene denominador casi nulo y se excluye como ancla.

La reinversión Base del año 1=156,748, frente a144345 del proxyLTM. S/C0.75 financia más capacidad que el primer borrador1.0: no se mantuvo un supuesto favorable que contradijera la guía de capex. Los rangos finales son Base0.75/1.4; Conservadora0.60/1.0; Optimista0.95/1.7; Disrupción0.45/0.65. El desfase1 se conserva por despliegue previo de capacidad; las cuatro pruebas lag0 recalculan todos los flujos y terminal en copias independientes de código. [Juicio; S3; cálculo reproducible].

### 4. WACC, fiscalidad y ajustes contables

Detailed combina segmentación y geografía: beta desapalancada0.808202, beta reapalancada0.858362, Ke9.1509%, WACC inicial8.7576% y terminal9.49%. Se reprodujeron fuera de la hoja. Beta por mezcla de EV sectorial=Σ(ventas×EV/Sales×betaU)/Σ(ventas×EV/Sales). No es una media simple de ventas. [WACC B22/B24,C58,B63,E63 yG37:K49].

Rf=4.94% al 30-oct. ERP madura seleccionada4.55%=4.20% adjusted-payout al 1-oct +(5.29%−4.94%). Es un **juicio de rebase manteniendo retorno esperado total9.49%**, no una observación de ERP de30-oct. La alternativa cash-yield rebasada4.05% se sensibiliza. La prima geográfica total=4.55% +(0.78%×43212+0.91%×30688+1.8%×107467)/716924=4.9057867%. USA489657 yAlemania45900 no añaden CRP; ReinoUnido/Japón sí. El1.8% del resto es proxy, no desglose país certificado. [S2,S4,S5; WACCB27; tablaCountry].

Kd=4.94%+0.40%=5.34%, usando coberturaEBIT/intereses23.275 y spreadAAA de la tabla sintética, sin presentar ese resultado como rating de agencia. Se evita añadir dos veces spread soberano sobreTreasury. La deuda de mercado se aproxima descontando cupón4484 yprincipal304461 a10años:215026.26. La duración10 es juicio agregado, no vencimiento observado de cada lease o bono. Pesos de mercado suman1 y B14=E63=InputB36. Beta de regresión y su error estándar=N/D: no hay una serie homogénea de retornos ybenchmark validada; un parámetro de volatilidad no los sustituye.

Impuesto inicial22.5% normalizado y terminal25%, con convergencia en años 6–10. No se reemplaza la tasa histórica B24. El contraste exdiscretos es aproximado y no asigna con exactitud impuestos a cada ganancia privada. No se capitaliza un beneficio NOL adicional sin identificación de jurisdicción. [S1Nota7; InputB89:B93].

I+D: Base GAAP, B17=No de forma provisional porque la rúbrica tecnológica mezcla desarrollo, operación, depreciación e infraestructura. **Existe I+D; no se certifica NOAPLICA económico.** El conversor vacío no prueba inmaterialidad. La capitalización pura y su impacto permanecen N/D material. Una sensibilidad de margen±1pp se entrega únicamente como diagnóstico, no como sustituto de reconstruir activo, amortización e inversiónI+D. Leases: ASC842 reconocido114783=15959+98824, más obligaciones de financiación separadas; B18=No significa no conversión incremental, no cero arrendamientos. Compromisos aún no iniciados necesitan puente con capex futuro para no omitir ni duplicar.

RSU:223.3m, ejercicio0 y acciones reales10811m. La fórmula IFERROR(log(S/K)) devuelve d1=0 cuandoK=0 y reduce indebidamente la reclamación a26,560.77m. El límite económico sin dividendo es223.3×240.35=53,670.15m. Diferencia=2.507574USD/acción, 1.69% delBase. No se fuerza un strike pequeño, no se eliminan RSU y no se duplican acciones diluidas. El parámetro sigma35% es juicio técnico, irrelevante para el límiteK=0. La reclamación nativa se conserva solo para reconciliar el motor y se señala el defecto. [S1Nota6; OptionB18/B23/B29/B30].

### 5. Cuatro historias, probabilidades y proyecciones

| Historia | Probabilidad | Margen objetivo | S/C1–5 | S/C6–10 | ROIC terminal | g terminal | DCFhoy |
|---|---:|---:|---:|---:|---:|---:|---:|
| Base | 45.0% | 17.0% | 0.75 | 1.40 | 12.50% | 4.0% | 148.68 |
| Conservadora | 22.5% | 14.0% | 0.60 | 1.00 | 10.50% | 4.0% | 91.93 |
| Disrupción | 10.0% | 10.0% | 0.45 | 0.65 | 9.49% | 2.0% | 59.98 |
| Optimista | 22.5% | 20.0% | 0.95 | 1.70 | 15.00% | 4.0% | 225.33 |

[Juicio/Cálculo: Escenarios filas5:8] Se conserva la previa crecimiento maduro45/22.5/22.5/10. No son frecuencias estadísticas estimadas. Los indicadores siguientes se fijan prospectivamente: no se inventa un cruce retrospectivo para mover probabilidades. La función original calcular de probabilidades.py, cargada con el mapeo AMZN extraído sin ejecutar su clienteSheets, confirma la previa y cero hallazgos. Se informa como prueba equivalente, no comando integral certificado.

| Indicador y datoactual | Base/Optimista | Conservadora/Disrupción |
|---|---|---|
| Crecimiento AWS: 39.3% Q3, S3 | Base:25–35% próximo año; Optimista≥35% durante4trimestres | Conservadora<25%; Disrupción<15% durante4trimestres |
| Margen AWS: 38.7% Q3, S3 | Base≥30%; Optimista≥35% sostenible sin excluirSBC | Conservadora<28%; Disrupción<20% durante4trimestres |
| Margen EBIT consolidado: 13.09% LTM; ISL12/L3 | Base avanza hacia17% a10años; Optimista20% | Conservadora estanca14%; Disrupción cae≤10% |
| Reinversión económica cash-proxy: 144,345 USD millones LTM; CFS L4,L7:L16 | Base productividad mejora con capacidad y ventas, sin reducircapex artificialmente | Dos años inversión>150000m sin crecimiento comparable favorecenConservadora |
| FCF reportado: −42357 USD millones LTM; S1 p34, CFO−capex neto | Base recupera flujo con maduración de capacidad; Optimista antes | Negativo persistente con AWS<15% favoreceDisrupción |
| Acciones reales/RSU: 10811m /223.3m; ISL27 yS1Nota6 | Dilución neta≤2% anual; SBC sigue enEBIT | >3% anual durante2años obliga revisarclaims/denominador |
| Inversiones no operativas: 294595 USD millones proxy bruto; B84 yS1Nota2 | Realización neta y contratos respaldanvalor; no ingresos operativos duplicados | Deterioro/netotax−20% o más exige recálculo del puente, no castigoWACC adicional |
| Capex y capacidad: Guía2026~220000m,2027mayor; S1/S3 | Ventas/capital0.75 primeros5años,1.4 después si utilización mejora | Capexcrece sin utilización: reducirproductividad y margen, no sumarprimaespecífica |

Pre-mortem a tres años:

- La capacidad IA entra antes que la demanda monetizable y obliga a reinvertir sin generar ingresos suficientes.
- La competencia convierte la nube en un servicio con menor poder de precio y erosiona margen y retorno del capital nuevo.
- La publicidad y los servicios no compensan costos logísticos, depreciación, salarios y energía.
- El valor realizable neto de impuestos de inversiones privadas resulta inferior al proxy contable.
- SBC/RSU diluyen más de lo modelado y la plantilla sigue valorando incorrectamente ejercicio cero.
- La capitalización de I+D y la clasificación de leases no son homogéneas con el sector y distorsionan ROIC/reinversión.

**Base: proyección nativa anual**, fuente Valuation output filas4: 16, columnasC:M. [Cálculo]

| Año | Ventas | Margen | NOPAT | Reinversión | FCFF | WACC | ROIC sobre capital inicial |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 908,341 | 13.09% | 92,130 | 156,748 | -64,617 | 8.76% | 18.09% |
| 2 | 1,025,902 | 13.87% | 110,276 | 162,990 | -52,714 | 8.76% | 16.56% |
| 3 | 1,148,144 | 14.26% | 126,898 | 160,973 | -34,076 | 8.76% | 15.31% |
| 4 | 1,268,874 | 14.65% | 144,089 | 159,817 | -15,728 | 8.76% | 14.56% |
| 5 | 1,388,737 | 15.04% | 161,911 | 154,744 | 7,167 | 8.76% | 14.08% |
| 6 | 1,504,795 | 15.43% | 178,844 | 78,118 | 100,725 | 8.90% | 13.71% |
| 7 | 1,614,160 | 15.83% | 195,427 | 71,237 | 124,190 | 9.05% | 14.13% |
| 8 | 1,713,892 | 16.22% | 211,242 | 62,303 | 148,939 | 9.20% | 14.53% |
| 9 | 1,801,117 | 16.61% | 225,853 | 51,460 | 174,392 | 9.34% | 14.90% |
| 10 | 1,873,161 | 17.00% | 238,828 | 53,519 | 185,309 | 9.49% | 15.23% |

Terminal: NOPAT248,381, reinversión79,482=NOPAT×g/ROIC, FCFF168,899. PVterminal/EV=85.14%. ROICaño 10=15.23%, ROIC terminal=12.50%. No se impone que ROICmarginal=margen×S/C cuando desfases y capital existente no coinciden.


**Conservadora: proyección nativa anual**, fuente Valuation output filas55: 67, columnasC:M. [Cálculo]

| Año | Ventas | Margen | NOPAT | Reinversión | FCFF | WACC | ROIC sobre capital inicial |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 865,002 | 13.09% | 87,735 | 114,538 | -26,803 | 8.76% | 17.23% |
| 2 | 933,724 | 13.27% | 96,026 | 110,549 | -14,523 | 8.76% | 15.39% |
| 3 | 1,000,054 | 13.36% | 103,555 | 105,287 | -1,733 | 8.76% | 14.10% |
| 4 | 1,063,226 | 13.45% | 110,848 | 101,593 | 9,255 | 8.76% | 13.20% |
| 5 | 1,124,182 | 13.54% | 117,998 | 100,923 | 17,075 | 8.76% | 12.54% |
| 6 | 1,184,735 | 13.63% | 124,384 | 59,709 | 64,675 | 8.90% | 11.94% |
| 7 | 1,244,444 | 13.73% | 130,674 | 58,405 | 72,269 | 9.05% | 11.86% |
| 8 | 1,302,849 | 13.82% | 136,816 | 56,630 | 80,186 | 9.20% | 11.79% |
| 9 | 1,359,479 | 13.91% | 142,760 | 54,379 | 88,381 | 9.34% | 11.73% |
| 10 | 1,413,858 | 14.00% | 148,455 | 56,554 | 91,901 | 9.49% | 11.68% |

Terminal: NOPAT154,393, reinversión58,816=NOPAT×g/ROIC, FCFF95,577. PVterminal/EV=80.45%. ROICaño 10=11.68%, ROIC terminal=10.50%. No se impone que ROICmarginal=margen×S/C cuando desfases y capital existente no coinciden.


**Disrupción: proyección nativa anual**, fuente Valuation output filas159: 171, columnasC:M. [Cálculo]

| Año | Ventas | Margen | NOPAT | Reinversión | FCFF | WACC | ROIC sobre capital inicial |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 837,328 | 13.09% | 84,928 | 93,036 | -8,109 | 8.76% | 16.68% |
| 2 | 879,194 | 12.47% | 84,967 | 78,151 | 6,816 | 8.76% | 14.11% |
| 3 | 914,362 | 12.16% | 86,178 | 60,957 | 25,220 | 8.76% | 12.67% |
| 4 | 941,793 | 11.85% | 86,510 | 41,857 | 44,652 | 8.76% | 11.67% |
| 5 | 960,629 | 11.54% | 85,941 | 42,695 | 43,247 | 8.76% | 10.97% |
| 6 | 979,841 | 11.23% | 84,765 | 30,149 | 54,616 | 8.90% | 10.26% |
| 7 | 999,438 | 10.93% | 83,539 | 30,752 | 52,787 | 9.05% | 9.76% |
| 8 | 1,019,427 | 10.62% | 82,260 | 31,367 | 50,893 | 9.20% | 9.28% |
| 9 | 1,039,815 | 10.31% | 80,930 | 31,994 | 48,936 | 9.34% | 8.81% |
| 10 | 1,060,612 | 10.00% | 79,546 | 32,634 | 46,912 | 9.49% | 8.37% |

Terminal: NOPAT81,137, reinversión17,099=NOPAT×g/ROIC, FCFF64,037. PVterminal/EV=63.42%. ROICaño 10=8.37%, ROIC terminal=9.49%. No se impone que ROICmarginal=margen×S/C cuando desfases y capital existente no coinciden.


**Optimista: proyección nativa anual**, fuente Valuation output filas106: 118, columnasC:M. [Cálculo]

| Año | Ventas | Margen | NOPAT | Reinversión | FCFF | WACC | ROIC sobre capital inicial |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 929,131 | 13.09% | 94,239 | 154,003 | -59,764 | 8.76% | 18.51% |
| 2 | 1,075,435 | 14.47% | 120,601 | 165,799 | -45,198 | 8.76% | 18.18% |
| 3 | 1,232,944 | 15.16% | 144,870 | 171,040 | -26,170 | 8.76% | 17.47% |
| 4 | 1,395,431 | 15.85% | 171,438 | 166,692 | 4,745 | 8.76% | 17.14% |
| 5 | 1,553,789 | 16.54% | 199,217 | 161,572 | 37,645 | 8.76% | 17.07% |
| 6 | 1,707,282 | 17.23% | 226,572 | 84,450 | 142,122 | 8.90% | 17.06% |
| 7 | 1,850,847 | 17.93% | 253,817 | 75,551 | 178,266 | 9.05% | 17.97% |
| 8 | 1,979,283 | 18.62% | 280,054 | 63,682 | 216,372 | 9.20% | 18.82% |
| 9 | 2,087,543 | 19.31% | 304,324 | 49,119 | 255,205 | 9.34% | 19.61% |
| 10 | 2,171,044 | 20.00% | 325,657 | 51,083 | 274,573 | 9.49% | 20.34% |

Terminal: NOPAT338,683, reinversión90,315=NOPAT×g/ROIC, FCFF248,367. PVterminal/EV=81.21%. ROICaño 10=20.34%, ROIC terminal=15.00%. No se impone que ROICmarginal=margen×S/C cuando desfases y capital existente no coinciden.

**Puente Base sustituido:** EV1,529,539.13 −deuda304,461 +caja114,226 +no operativos294,595 −RSUnativas26,560.77 =patrimonio1,607,338.36; /10,811acciones=148.67619605. Minoritarios/preferentes0 segúnbalance, no por vacío. FCFF=ventas×margen×(1−t)−reinversión; TV=FCFF11/(9.49%−4%). [Valuation output!B18:B35].

### 6. Cinco múltiplos prioritarios: aplicabilidad y anclas

| Método | Estado y motivo | Peso |
|---|---|---:|
| EV/EBITDA | PENDIENTE_ANCLA: Métrica positiva; faltan serie histórica de cierres, ajuste por tasas y pares homogéneos. Sector no sustituye ancla por ciclo. | 0% |
| EV/FCFF | NO_APLICA_FY3_NEGATIVO: FCFF FY+3 negativo en las tres historias ordinarias; no fabricar múltiplos. | 0% |
| P/E | PENDIENTE_ANCLA_Y_NORMALIZACION: Interest/Other proyecta media histórica positiva, incluye partidas no operativas; normalizar y obtener ancla independiente. | 0% |
| P/FCFE | NO_APLICA_BASE_FY3_NEGATIVO: BaseFY+3 negativo; Cons/Opt positivos con dependencia deOtros ynetborrowing. Sin ancla, peso0. | 0% |
| P/OCF | PENDIENTE_ANCLA_Y_NWC: Positivo, pero NWC es residuo de conciliación delDCF yOtros requiere normalización. Sin ancla independiente. | 0% |

Se leyeron las pestañas históricas y los cinco motores. J8/J19/J30 no tienen ancla válida. Los ceros derivados de precios históricos vacíos no son múltiplos observados. No se usaron como mínimos históricos ni se fabricó una mediana. El intento de multiples_by_cycle.py falla por falta de expediente AMZN_anclas.json completo y consistente con R2; no se reutiliza un archivo legado de otra revisión. Ajuste por tasas, atípicos, comparables5–10 y anclaC de cada múltiplo de salida=N/D mientras falte el ancla primaria. P/S yP/BV opcionales con peso0, sin exigir llenarlos para elDCF.

| MétricaBase nativa | FY+1 | FY+2 | FY+3 | Fuente |
|---|---:|---:|---:|---|
| EBITDA | 197,340.15 | 231,495.62 | 265,177.71 | FinancialsMultiples!E57:G57 |
| FCFF | -64,617.46 | -52,713.86 | -34,075.51 | FinancialsMultiples!E63:G63 |
| OCF | 65,475.96 | 94,706.62 | 131,185.12 | FinancialsMultiples!E65:G65 |
| FCFE | -40,923.51 | -26,936.56 | -7,201.04 | FinancialsMultiples!E68:G68 |
| EPSproyectadonormalizacióntécnica | 9.19 | 11.00 | 12.66 | FinancialsMultiples!E72:G72 |

Las métricas monetarias están enUSD millones exceptoEPS. Se muestran como diagnóstico del motor, no se les asigna un precio relativo sin ancla. NWC proyectado es residuo para conciliar reinversión, no una previsión independiente de capital circulante. Otros/EBIT=7.87348% hereda la media histórica: no se trata automáticamente como resultado recurrente. Las matrices5×5 de múltiplos son N/D, no matrices de ceros ni valores inventados.

### 7. Sensibilidad y DCF inverso


**Matriz nativa A: curvaWACC y g**, SensibilidadDCF!A5:F10. Valores presentes por acción. [Cálculo]

| Eje Y / Eje X | 3.00% | 3.50% | 4.00% | 4.50% | 5.00% |
|---|---:|---:|---:|---:|---:|
| 7.76% | 174.72 | 182.60 | 192.14 | 203.95 | 219.00 |
| 8.26% | 155.67 | 161.39 | 168.16 | 176.34 | 186.46 |
| 8.76% | 139.69 | 143.84 | 148.68 | 154.39 | 161.29 |
| 9.26% | 126.10 | 129.11 | 132.56 | 136.55 | 141.27 |
| 9.76% | 114.43 | 116.59 | 119.02 | 121.79 | 124.99 |

**Matriz nativa B: ROIC terminal y g**, SensibilidadDCF!A16:F21. Valores presentes por acción. [Cálculo]

| Eje Y / Eje X | 3.00% | 3.50% | 4.00% | 4.50% | 5.00% |
|---|---:|---:|---:|---:|---:|
| 11.50% | 136.68 | 139.96 | 143.75 | 148.18 | 153.46 |
| 12.00% | 138.24 | 141.98 | 146.31 | 151.41 | 157.54 |
| 12.50% | 139.69 | 143.84 | 148.68 | 154.39 | 161.29 |
| 13.00% | 141.02 | 145.56 | 150.86 | 157.14 | 164.75 |
| 13.50% | 142.25 | 147.14 | 152.88 | 159.69 | 167.95 |

**Matriz nativa C: delta crecimiento y margen**, SensibilidadDCF!A27:F32. Valores presentes por acción. [Cálculo]

| Eje Y / Eje X | 13.00% | 15.00% | 17.00% | 19.00% | 21.00% |
|---|---:|---:|---:|---:|---:|
| 7.73% | 103.31 | 119.59 | 135.86 | 152.13 | 168.40 |
| 9.73% | 105.16 | 123.56 | 141.96 | 160.35 | 178.75 |
| 11.73% | 107.14 | 127.91 | 148.68 | 169.44 | 190.21 |
| 13.73% | 109.29 | 132.69 | 156.09 | 179.49 | 202.89 |
| 15.73% | 111.62 | 137.95 | 164.28 | 190.61 | 216.94 |

Los tres centros son148.67619605 y los75 recálculos independientes difieren como máximo8.527e-14USD/acción. La matrizA muestraWACC **inicial** en filas y desplaza inicial+terminal en paralelo; se corrigió el rótulo textual, no fórmulas. La matrizB alteraROIC terminal. La matrizC muestra CAGR5años en el eje pero aplica delta aditivo a los cinco crecimientos, conservando forma y recalculando transición. g5% excedeRf4.94%: sus celdas no son hipótesis monetariamente admitidas aunque calculen. La malla nativa no usa exactamente los anchos normativos±0.5pp deg y±3pp demargen.

Se adjuntan en elJSON otras tres matrices diagnósticas5×5 con ejes normativos: WACCterminal±1pp manteniendo inicial; ROIC terminal×g; deltaaños 1–5±2pp×margen±3pp. Sus centros concilian y g se limita a3.5–4.5%. **No son salidas nativas ni sustituyen el ajuste pendiente del perfil de plantilla**. No se reemplazan las fórmulas oficiales para hacerlas coincidir.

| Prueba completa, todo lo demás constante | Base/acción |
|---|---:|
| Crecimiento1–5 −2pp | 141.96 |
| Crecimiento1–5 +2pp | 156.09 |
| Margen objetivo −3pp | 117.53 |
| Margen objetivo +3pp | 179.83 |
| ROIC terminal=WACC | 130.70 |
| No operativos −20% | 143.23 |
| No operativos −50% | 135.05 |
| Lag0 Base | 147.97 |
| RSUcorrectas como diagnóstico | 146.17 |

ERPmadura alternativa4.05% rebasada: WACC inicial8.36%, terminal8.99%, Base167.04. Beta±0.25 da160.00/138.25: no es beta de regresión. Disrupción con reinversión mínima160000m en cada uno de los tres primeros años vale40.76; es un stress contractual hipotético, no guía de la compañía. RSUcorregidas y no operativos−20% simultáneos dan140.72. No se declara reserva conjunta<3%: hay incertidumbres materiales abiertas.

DCF inverso **diagnóstico externo**, no celda nativa: precio fijo240.35 del30-oct, variable delta común a g1..g5, intervalo[−9,+35]pp; barrido441puntos detecta un cruce y bisección100iteraciones. Delta=16.636884pp; CAGR Base5años=11.733329%; CAGR implícito=28.371715%. Reconstrucción=240.3500000000, error=-8.527e-14. Se recalculan diez años, convergencia, reinversión y terminal en cada iteración, sin multiplicar por un factor de calibración. No prueba qué cree realmente el mercado: otras combinaciones de margen, productividad o activos privados explican el mismo precio. La Base no se cambió para resolverlo.

El precio está61.66% sobre el Base provisional; el Base implica-38.14% frente alprecio. El mercado puede descontar mayor productividad de la infraestructura, duración de la ventaja o realización de participaciones. Esa diferencia no demuestra por sí sola que el mercado esté equivocado.

### 8. Captura y trazabilidad

CAPTURA_SHEET.json SHA256=`ad3c2174044e688e584f0b639e8777a8bf4c8e1229ae3a98e121640a1fd3b4cd`. Exportación nativa completa de46 pestañas SHA256=`0365c794f4854e42f62012d2899c4e8c9c42c157c7f4e3b8ffeab2ce45cbc72a`. El JSON candidato se construye desde las entradas y salidas capturadas; incluye procedencia por celda, controles, matrices nativas y diagnósticos separados. El paquete incluye código reproducible, series leídas, plan de entradas, intentos de comandos y hashes.

### 9. Fuentes

- **S1** [Amazon10-Q, Sep2026, presentado30-oct2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm): Balance pp5–6; notas2 pp10–12,3 pp13–14,4 pp15–16,5 pp17–18,6 pp19–20,7 p22; MD&A pp28–36. Notas puntuales de celdas.
- **S2** [Amazon10-K FY2025](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm): Estados y segmentos/geografía; notas de celdas históricas B:K.
- **S3** [AmazonQ3IR,29-oct2026](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx): Resultados por segmento, guía capex2026/2027, cambio calendarioPrimeDay.
- **S4** [USTTreasury10Y30-oct2026](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_yield_curve): Fila10/30/2026, columna10-year4.94%; InputB35.
- **S5** [Damodaran, ERP publicado1-oct2026, corte30-sep](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm): 4.20% adjusted payout;3.70% cashyield; Rf5.29%. Rebase a4.55% esJUICIO, no cotizaciónOct30.
- **S6** [Damodaran, BetasUS enero2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html): RetailGeneral n23 yComputerServices n64; caché de IndustryAveragesUS filas75/22. Precisión de caché, tabla pública redondeada.
- **S7** [PrecioAMZN30-oct2026](https://stockanalysis.com/stocks/amzn/history/?period=daily): Cierre sin ajuste240.35, proveedorS&PGlobal; contrasteYahooHistory. No cierreNov2.
- **S8** [Entrega fase1 R2](https://drive.google.com/file/d/1fE-5Vkw2ciMUGU_RqilijMUgAqwe1QlX/view): CERRADA CON CONTROLES PENDIENTES, actualización2-nov. Continuidad autorizada por README vigente y nueva invocación.

## Controles de cierre (resultado real de cada uno)

| Control | Resultado real |
|---|---|
| Recálculo cuatroDCF desde entradas | APROBADO EQUIVALENTE: máximo error8.527e-14<1e−6USD/acción. |
| Trescentros y75celdas DCF | APROBADO aritmético; máximoerror8.527e-14. Ejes/rangos distintos del contrato explicitados; corrección delperfilpendiente. |
| Probabilidades y ciclo vital | APROBADO EQUIVALENTE: crecimiento maduro45/22.5/22.5/10, suma1, ceroajustes y cerohallazgos en función original. |
| MOS | APROBADO: Resumen!D36=Base×0.65. |
| inputs_completos.py | Comando integral NO EJECUTADO con éxito: depende de model_steps/paquete/cliente. Funciónvacias original contra captura:0 blancos esenciales, sin salvedades inventadas. |
| candados.py | Comando integral NO EJECUTADO con éxito; comprobación directa15/15 del archivo canónico vigente del27-oct, no18legados. No demuestra corrección económica I+D/RSU. |
| diff_formulas_plantilla.py | NO EJECUTADO integral—requiere paquetejmr_valuation yclienteSheets. APROBADO EQUIVALENTE:20.740 fórmulas exactas enexport yD12idéntica nativamente=20.741;0reemplazos;46tabs mismoorden. |
| integridad_hojas.py | NO EJECUTADO integral—requiere checkout completo yclienteautenticado. EquivalentePARCIAL: sinerrorValue enáreasleídas, fórmulas preservadas, noescaneo oficial de todaslasdependencias. |
| controles_supuestos.py | Intento falló por dependencia probabilidades_prior antesdematerializarla; no se obtuvo ejecución integral final. Prueba económica manual mantiene reservas S1sector/mix, I+D, beta, reinversión yterminal; no se suprimen alertas conjustificaciones vacías. |
| ciclo_de_vida.py / probabilidades.py | Intentos integrales fallaron por dependencias decheckout. MapeoAMZN yreglaoriginal deprobabilidades verificados por prueba equivalente sin cambios dehoja. |
| multiples_by_cycle.py | Intento falló por expediente de anclasR2 ausente. Cinco métodos evaluados, N/D/N/A ypesos0; ninguna ancla derivada delDCF. |
| foto_supuestos.py | Intento integral fallido por dependencias. Captura completa+nativa ySHA256 generados por códigopropio. |
| Controles heredados fase1 | estados_completos/auditar_estados_sec/novedades_sec no ejecutados integralmente; revisar registrofilings hasta2-nov. Conciliaciones directas y fuentes principales conservadas. |
| Ajustes contables | RESERVA MATERIAL: RSUstrike0 erroneanativa, I+D sinhomologar, valor nooperativo bruto sinconciliación netafiscal. |
| Valor terminal | ALERTA: PVterminal/EVBase=85.14%>85%. No se redujo mediante cambios oportunistas. |
| Revisión visual | PARCIAL: navegador mostró acceso con inicio de sesión; no se solicitó login. Exportación renderizada localmente. Escenarios/tesis ajustados por legibilidad; motor local no conserva toda sensibilidad circular. Valores verificados enAPI nativa. |
| Estado/publicación | CANDIDATO. Sin catálogo, app, promoción, PR, auditoría ni certificación. |
| Aislamiento | AISLAMIENTO=OK. SoloAMZN R2; referencias sectoriales explícitas; no trasplanteR1. |

PASOS: **7/7 pasos ejecutados con el alcance indicado** (1: supuestos;1b: ciclo/probabilidades;2: historias;3: entradas/DCF/matrices;3b: múltiplos;4: recálculo;5: captura/JSON). Las comprobaciones equivalentes se ejecutaron; los comandos integrales fallidos/no disponibles y los cálculos nativos pendientes se listan, sin contarlos como aprobados. El cierre operativo no equivale a puertaA-1.2 aprobada.

## Decisiones y juicios

| Motor | Selección y mecanismo | Evidencia a favor | Evidencia contraria/refutación | Prueba deimpacto |
|---|---|---|---|---|
| Crecimiento | Segmentación NA/Internacional/AWS; Base CAGR11.7333%5años | AWSQ3acelera ycapacidad | Escala final,TAM/consensohomogéneoN/D;compresión precios | Delta±2pp en tabla |
| Margen | 17%Base,14%Cons,20%Opt; convergencia10años | Mezcla nube/publicidad ylogística | Depreciación/energía/competencia; margenAWS noeterna | Objetivo±3pp en tabla |
| Reinversión | SC0.75/1.4Base,lag1 | Capex2026~220bn ycreciente2027 | Proxyhistórico incompleto, capacidadociosa eI+D | Lag0/1 ystresspiso160bn |
| Fiscalidad | 22.5%→25% | Normalización frenteagananciasprivadas | Atribuciónfiscal exactaN/D | No se capitalizaNOL noidentificado |
| WACC | Bottom-up EV,geografía;8.757648%→9.49% | MétodoDetailed ypesos100% | ProxyComputerServices, duración10, ERP rebasado noobservado | Beta±0.25 yERPalternativa |
| Terminal | g4%,ROIC12.5%Base | Red/ecosistema yescala conspreadmoderado | Competencia; pesoVT85.14% | ROIC=WACC ymatrices completas |
| Activosprivados | Proxycontablebruto294595m | Últimoimporte reportado separado deEBIT | Liquidez,derechos,impuestosdiferidos yrestricciones | −20%/−50% ystresscombinado |
| Opciones/RSU | 223.3m/strike0; denominator10811m | Nota6 ySBCenEBIT | Defectomotor; vesting/forfeituresracionales pendientes | Límiteeconómico−2.507574USD/acción |
| I+D | ReferenciaGAAPprovisional, N/Dajustado | No mezcla100%delcostotecnológico | Existeinversión plurianual material nohomologada | Margen±1pp no sustituye capitalización |
| Múltiplos | Cincoevaluados,peso0 | Evita anclasdependientesdelDCF | Menorcontrastación externahastahomologarhistoria | MatricesN/D, nofalsas |

Sesgo agresivo: se aumentó reinversión al contrastar capex, se reconoce el exceso de valor por RSU, el proxy de beta débil y el valor bruto de participaciones. Prudencia duplicada: no se añade prima por riesgo operativo a WACC, no se resta otro fracaso y no se aplica MOS al promedio. Escenarios contienen riesgos económicos; probabilidades mantienen la previa sin recorte discrecional. Ningún supuesto se calibró al precio.

## Pendiente o bloqueado

La aprobación/publicación del valor depende de resolver: (1) fórmula oficialK=0 con versión autorizada del motor, (2) capitalizaciónI+D con historial comparable o excepción material sustentada, (3) valor realizable **neto de impuestos** y capital operativo asociado a activosprivados, (4) ERP de finalOct observado y datosgeográficos finales, (5) beta regresión/error ycohorte adecuada, (6) anclas relativas ynormalización Otros/NWC, (7) comandos oficiales con checkout/cliente que apunten explícitamente aR2 y no al catálogo legado, (8) perfil de sensibilidad e inverso nativos conformes alcontrato y (9) alertaVT. No se necesitan nuevas autorizaciones para completar controles técnicos reversibles, pero no se promueve estado por cerrar eldocumento.

Se intentó ejecutar cada uno de nueve scripts descargados: ninguno obtuvo corrida integral exitosa en este entorno aislado por dependencias/rutas de proyecto y cliente. El registro exacto está en official_attempts.json. Esto no significa que faltenPython oGitHub: ambos están disponibles. Lo pendiente es el runtime completo JMR y la autenticación/selección de la hoja para sus clientes oficiales.

## Para la fase siguiente

Leer primero esta entrega, `VALORACION_A12_EN_REVISION.json` (estadointernoCANDIDATO), `CAPTURA_SHEET.json` y SHA256SUMS, luego lahojaR2 y las pruebas de evidencia. Para análisis utilizar únicamente los valores finales de esta captura; no conservar los valores provisionales comunicados antes de ajustar reinversión. La fase3 puede preparar texto comoCANDIDATO señalando reservas, pero no convertir148.68 en valor oficial ni promoverEN_REVISION sin resolver controles aplicables.

No se añade pestañaENTREGA: se conserva el perfil de46 pestañas y el resumen se documenta en laTesis existente. Esta invocación termina en fase2. No se redactan14capítulos deResearch ni se ejecuta auditoría.

