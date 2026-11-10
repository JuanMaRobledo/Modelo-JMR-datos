# UBER-REBOOT-3T26-R1 · Fase R4 (múltiplos y resumen)

- **Fecha:** 2026-11-10 · **Agente:** Claude (Code, nube): Sheets, SEC XBRL, 10-Q/10-K · esfuerzo: alto.
- **Libros:** 03 MÚLTIPLOS `19fe8FcQ32d3yf169i-XA7F-c4IGhWTCNl_QO4WgCwA4` y `Resumen de valoraciones` del DCF Base `14QlydMFli2pxdG4agUYOAXL8QIE99P-3UDE7vwK8CaM`. Estado **CANDIDATO** (R5 pendiente; sin R6).

## Resultado
| Valor por acción | Conservadora | **Base** | Optimista | Esperado (25/50/25) |
|---|---|---|---|---|
| DCF (principal, beta 1,20) | 45,29 | **98,74** | 149,67 | 98,11 |
| Múltiplos consolidados (secundario) | 40,65 | 71,05 | 106,02 | 72,19 |
| Combinado 75/25 (secundario) | 44,13 | 91,82 | 138,76 | — |

| Método (peso total) | Cons | Base | Opt |
|---|---|---|---|
| EV/EBITDA (10 %) | 48,90 | 73,37 | 98,63 |
| EV/FCFF (6 %) | 26,98 | 47,94 | 73,24 |
| P/E (5 %) | 47,56 | 107,25 | 180,78 |
| P/FCFE (2 %) | 19,65 | 36,05 | 55,68 |
| P/OCF (2 %) | 44,18 | 73,22 | 104,73 |

Los múltiplos Base quedan **28,0 % por debajo del DCF Base** y 3,6 % por encima del precio (68,59). Conciliación en `Resumen de valoraciones`: 6 controles OK. Compuerta `Supuestos y control!B60` = «LISTA PARA CALCULAR». **Margen de seguridad solo sobre el DCF Base:** 64,18; precio entre MOS y DCF Base.

**Diferencia material por explicar:** el P/E da 107 (Base) y 181 (Opt) porque la utilidad neta Base proyectada es alta frente a una utilidad LTM distorsionada por pérdidas no operativas; con peso de 5 % su efecto en el combinado es limitado, pero es la cifra menos fiable. P/FCFE (19,65–55,68) y EV/FCFF son bajos por el FCFF deprimido por impuestos y reinversión; por eso pesan poco.

## Qué se cargó
- **Estados desde H (por etiqueta):** FY2017–FY2025 + LTM en Income Statement, Balance Sheet y Cash Flow (`R4_evidencia/M_UBER_payload.json`). Arrendamientos reclasificados a «otros pasivos» (filas 23/27; filas de deuda 21/26 con 0 solo en arrendamientos), por decisión del usuario. Gastos por intereses negativos (fila 14); ajuste por método de participación en fila 30; EPS calculados.
- **Supuestos de las tres historias = los del DCF**, por multiplicadores sobre la base contable de M: crecimiento año 1 y 2–5 (ancla LTM interanual 13,94 % con ingresos LTM de hace un año 49.610), margen objetivo en base reportada (16,36 / 11,36 / 20,36 % = objetivos ajustados − 1,64 pts del ajuste de I+D), ventas/capital 2,8/2,0/3,4 (1–5) y 2,5/1,8/3,0 (6–10), g 4,0 %, ROIC terminal 13,23 % / costo de capital / 18,21 %, impuesto 25,17 %.
- **Entradas desde los tres DCF:** valor, Ke 10,49 %, Kd 6,10 %, costo de capital inicial 10,00 % y estable 8,25 %, EBIT 7.961, beta 1,20, ERP 4,69 %. «SHA-256» = hash del JSON de los valores transferidos (no del libro entero): Cons `b594687d…899d`, Opt `f82f812a…aee`; M `53c5a66a…105f` (valores por método, combinado y pesos).
- Puente: caja 10.068, activos no operativos 11.473, minoritarios 1.304, 2.107,437 M de acciones, opciones 5,549 M a 52,23.

## Múltiplos de salida y pesos (juicio mío)
| Método | Cons | Base | Opt | Criterio |
|---|---|---|---|---|
| EV/EBITDA | 15,96x | 18,78x | 21,60x | −15 % / actual / +15 % |
| EV/FCFF | 26,78x | 31,50x | 36,23x | actual = FY2025 (LTM N/D) |
| P/E | 16,73x | 28,58x | 40,42x | Cons = mediana 5 años; Opt = TTM; Base = punto medio (el TTM está distorsionado por pérdidas no operativas) |
| P/FCFE | 8,26x | 9,72x | 11,18x | −15 % / actual / +15 % |
| P/OCF | 11,09x | 13,05x | 15,01x | −15 % / actual / +15 % |
**Tipo «Crecimiento»**: DCF 75 %, múltiplos 25 % (EV/EBITDA 10 %, EV/FCFF 6 %, P/E 5 %, P/FCFE 2 %, P/OCF 2 %). P/S y P/BV no se usan. El peso mayor va a EV/EBITDA porque Uber tiene EBITDA positivo y sin efecto de estructura de capital; P/E y flujos al accionista pesan poco por las partidas no operativas y las inversiones valoradas.

## Controles
| Control | Estado |
|---|---|
| Compuerta B60 «LISTA PARA CALCULAR» | APROBADO |
| Conciliación `Resumen de valoraciones` (6 controles) | APROBADO |
| Fechas y cuadres de estados | APROBADO |
| Verificación documental contra 10-K/10-Q | **PENDIENTE** (verificaciones en «PENDIENTE»; estados «MODELADO · SIN CERTIFICAR») |
| M no descuenta el valor de las opciones (185,8 M ≈ 0,09 US$/acción) | Declarado |
| Revisión de fórmulas originales de M | NO re-verificada |
| Auditoría económica independiente | **NO_EJECUTADA (R6)** |

## Siguiente paso exacto
R5: escribir el análisis (N1 de 14 capítulos y N2 de 12 apartados) en Google Doc, generar los JSON `jmr-reboot-3libros-v1`, validar y publicar EN_REVISION, reemplazando UBER Floyd en el catálogo.
