# UBER-REBOOT-3T26-R1 · Fase R3 (historias y DCF)

- **Fecha:** 2026-11-10 · **Agente:** Claude (Code, nube): Sheets, SEC (10-K FY2025 y 10-Q 3T-2026, XBRL y texto), LibreOffice (recálculo local del motor).
- **Libros:** DCF Base `14QlydMFli2pxdG4agUYOAXL8QIE99P-3UDE7vwK8CaM` · Conservadora `1TUDP8WvRpjtm5AbCpGkKkfyAlItRuufIAAEkFp95aHA` · Optimista `1f7Fzs7TBezRNa4E0lwHoh8fcPXTGn0d09HTatCaDLRU`. Estado **CANDIDATO** (R4 pendiente; sin R6). La revisión Floyd `UBER-FLOYD-3T26` sigue activa en el catálogo.
- **Motor:** fcffsimpleginzu original; entradas en `Input sheet`, `Cost of capital worksheet`, `R& D converter` y `Country equity risk premiums!B1`. Cálculo iterativo habilitado y arreglo de `Option value!B17`. **Integridad de fórmulas y comentarios no re-verificada** en estas copias.

## Resultado
| | Conservadora | **Base** | Optimista | Esperado (25/50/25) |
|---|---|---|---|---|
| Valor por acción | 49,54 | **108,62** | 164,91 | 107,92 |
| Frente al precio (68,59, 6-nov-2026) | −27,8 % | **+58,4 %** | +140,4 % | +57,3 % |

**Precio con MOS 35 % = 0,65 × 108,62 = 70,60 USD.** El precio de mercado (68,59) está **por debajo** del precio con MOS: según esta revisión Uber estaría en zona de compra. **Esta conclusión depende del costo de capital** (ver «Punto crítico»). Réplica local = Google Sheets en las tres historias (49,5444 / 108,6198 / 164,9058).

## Punto crítico para R6: la beta
Las reglas (§4A) piden WACC «Detailed» con beta bottom-up multinegocio cuando hay líneas de negocio distintas. Se aplicó: Mobility → Transportation (0,712), Delivery → Business & Consumer Services (0,806), Freight → Trucking (0,869), ponderadas por ingresos LTM → beta desapalancada 0,770, apalancada 0,822, Ke 8,72 %, **costo de capital inicial 8,37 %**. La revisión Floyd usó una beta directa de 1,20 y ERP de 4,08 % (WACC 9,37 %). **Con beta 1,20 en este mismo libro el costo de capital sería 10,00 % y el DCF Base 98,74** (MOS 64,18, por debajo del precio: no habría zona de compra). Mi opinión: las medias de «Transportation» y «Trucking» describen empresas de activos físicos y pueden subestimar el riesgo de una plataforma de consumo discrecional; la asignación de industrias es un juicio mío, no un dato. No se cambió la regla; se deja la sensibilidad en la hoja y este aviso.

## Entradas comunes
| Entrada | Valor | Fuente / criterio |
|---|---|---|
| Ingresos LTM · EBIT LTM | 56.526 · 7.034 | H (XBRL): FY2025 + 9M-2026 − 9M-2025 |
| Año anterior (FY2025) | 52.017 · 5.565 | 10-K |
| I+D capitalizada | Sí, 3 años | I+D LTM 4.152; FY2025 3.402; FY2024 3.109; FY2023 3.164 → EBIT ajustado 7.961, margen 14,08 % |
| Patrimonio contable | 28.575 | Total con no controladoras |
| Deuda | 15.664 | Deuda LP neta (incluye notas convertibles y canjeables); **sin arrendamientos** (1.897 + 176), por la regla acordada |
| Caja | 10.068 | Efectivo 9.558 + inversiones CP 510. **Excluye** caja e inversiones restringidas (11.372), que respaldan las reservas de seguros (13.709) |
| Activos no operativos | 11.473 | Inversiones 7.975 (Didi 2.061; Grab 1.667; Aurora 870; otras) + método de participación 3.498 (Delivery Hero 3.372), a valor en libros. Floyd usó 12.567; la diferencia (1.094) no la pude reconstruir |
| Minoritarios | 1.304 | No redimibles 916 + redimibles 388 (valor en libros) |
| Acciones | 2.107,437 | 2.041,898 (portada del 10-Q) + 65,539 RSU no devengadas (todas; conservador) |
| Opciones | 5,549 M a 52,23 · 4,27 años · volatilidad 40 % | 10-Q Nota 7; **volatilidad supuesta**; valor 185,8 M |
| Impuesto efectivo / marginal | 25,17 % / 25 % | 1.238 / 4.919 LTM; FY2024–25 tuvieron beneficios por liberación de provisión, no representativos |
| Tasa libre · g terminal | 4,86 % · 4,0 % | FRED DGS10; regla |
| ERP | 4,69 % inicial | Regiones (ingresos LTM): Norteamérica 29.543 (3,60 %), EMEA 15.905 (5,87 %), Asia 6.987 (4,88 %), Latinoamérica 4.091 (7,62 %); madura 3,387 % |
| Costo de la deuda | 6,10 % antes de impuestos (entrada directa) | **Estimación mía**: Rf 4,86 % + diferencial ≈ 1,25 % observado en las notas a 10 años de 2024; vencimiento medio 7,5 años (calculado de la Nota 5). No verifiqué la calificación crediticia |
| Pesos de mercado | 91,75 % / 8,25 % | Capitalización 144.549; deuda a mercado 12.998 |
| Costo de capital | **8,37 % inicial** · 8,25 % estable | Común a las tres historias |

## Historias (punto de partida: Floyd; cambios declarados)
**Tipo: crecimiento**; probabilidades 50 / 25 / 25 (las de Floyd). Sin fracaso: cobertura de intereses de 14x.
| Palanca | Conservadora | **Base** | Optimista |
|---|---|---|---|
| Crecimiento año 1 (B26) | 7,0 % | 11,0 % | 13,0 % |
| CAGR años 2–5 (B28) | 9,75 % | 14,0 % | 16,25 % |
| CAGR 5 años resultante | 9,2 % | 13,4 % | 15,6 % |
| Margen año 1 → objetivo año 5 (ajustado por I+D) | 14,08 % → 13 % | 14,08 % → 18 % | 14,08 % → 22 % |
| Ventas/capital 1–5 · 6–10 | 2,0 · 1,8 | 2,8 · 2,5 | 3,4 · 3,0 |
| ROIC terminal | costo de capital (8,25 %) | 13,23 % | 18,21 % |
| Valor por acción | 49,54 | 108,62 | 164,91 |

- CAGR a 5 años, márgenes y ventas/capital son los de Floyd. El año 1 se fijó por debajo del resto porque el cambio de modelo de negocio en Reino Unido reduce los ingresos reportados de Mobility (−1.100 M en el 3T-2026; Mobility −2 % con reservas brutas +18 %): los ingresos crecieron 9,6 % en el trimestre y 12 % en nueve meses.
- **ROIC terminal por la regla (§4):** industria ponderada por segmentos = 18,21 %. Optimista: ventaja durable = industria. Base: ventaja que se desvanece = punto medio con el costo de capital (13,23 %), porque Uber gana sobre su costo de capital hace menos de tres años (EBIT positivo desde 2023; ROIC actual 14,3 %). Conservadora: sin ventaja. Floyd usaba 14 / 9 / 17 %.
- Diferencia frente a Floyd (Base 100,19): costo de capital 8,37 % frente a 9,37 % (sube el valor) y activos no operativos 11.473 frente a 12.567 (lo baja).

### Pruebas de las tres preguntas
- **Posible:** ingresos del año 5 de 105.972 M (×1,9) y del año 10 muy superiores; participación de mercado **N/D** (sin TAM verificado de movilidad y reparto). Las reservas brutas crecen 18 % en Mobility.
- **Plausible:** margen objetivo 18 % frente a 9,2 % de las industrias ponderadas y 14,1 % hoy: **REVISAR**; se apoya en el apalancamiento operativo observado (EBIT de −1.832 en FY2022 a 7.034 LTM). Juicio: **Con reserva**.
- **Probable:** 13,4 % anual a cinco años frente a 18 % en FY2024–25 y 12 % en 2026; valor terminal = 72 % del valor operativo. Juicio: **Con reserva** (dependencia alta del valor terminal y de la conducción autónoma, no modelada).

## DCF inverso y sensibilidades (hoja `Sensibilidades DCF` del libro Base)
- El precio de 68,59 equivale a creer, una variable a la vez: **crecimiento de 4,35 % anual** cinco años, o **margen objetivo de 11,55 %**, o 6,6 % de crecimiento con margen de 16 %. Con el costo de capital inicial no se llega: aun con 15 % el valor es 74,44.
- Matriz A (CAGR × margen): 71,59 a 158,67. Matriz B (costo de capital inicial × g): 92,92 a 128,05. El precio queda por debajo de todas las celdas.

## Controles
| Control | Estado |
|---|---|
| Réplica local vs Google Sheets (tres historias) | APROBADO |
| Costo de capital común; probabilidades 100 %; Cons ≤ Base ≤ Opt; costo de capital estable > g | APROBADO |
| Beta bottom-up por la regla | APLICADA, **en disputa** (ver punto crítico) |
| Activos no operativos a valor en libros (participaciones cotizadas y no cotizadas) | PARCIAL: no se llevaron a valor de mercado |
| Reservas de seguros y caja restringida fuera del puente | SUPUESTO declarado |
| Costo de la deuda y volatilidad de opciones | ESTIMADOS |
| Motor original sin cambios | NO re-verificado |
| Auditoría económica independiente | **NO_EJECUTADA (R6)** |

## Siguiente paso exacto
R4: cargar 03 MÚLTIPLOS (`19fe8FcQ32d3yf169i-XA7F-c4IGhWTCNl_QO4WgCwA4`) con los estados de H y los supuestos de la Base, elegir múltiplos de salida y pesos, y conciliar el `Resumen de valoraciones`. Antes conviene que el usuario decida si acepta la beta bottom-up o prefiere otra.
