# UBER-REBOOT-3T26-R1 · Fase R4 (múltiplos y resumen)

- **Fecha:** 2026-11-10 · **Agente:** Claude (Code, nube): Sheets, SEC XBRL, 10-Q/10-K. Esta entrega **reemplaza** la R4 que otro agente (ChatGPT) había escrito el mismo día (múltiplos Base 81,56; EV/FCFF N/D): por decisión del usuario, Claude rehízo R4 y R5 y los libros de Sheets contienen los valores de esta entrega.
- **Libros:** 03 MÚLTIPLOS `19fe8FcQ32d3yf169i-XA7F-c4IGhWTCNl_QO4WgCwA4` y `Resumen de valoraciones` del DCF Base `14QlydMFli2pxdG4agUYOAXL8QIE99P-3UDE7vwK8CaM`. Estado **CANDIDATO** (sin R6).

## Resultado
| Valor por acción | Conservadora | **Base** | Optimista | Esperado (25/50/25) |
|---|---|---|---|---|
| DCF (principal, beta 1,20) | 45,29 | **98,74** | 149,67 | 98,11 |
| Múltiplos consolidados (secundario) | 40,24 | 70,31 | 104,90 | 71,44 |
| Combinado 75/25 (secundario) | 44,03 | 91,63 | 138,48 | — |

| Método (peso total) | Cons | Base | Opt |
|---|---|---|---|
| EV/EBITDA (10 %) | 48,40 | 72,61 | 97,59 |
| EV/FCFF (6 %) | 26,72 | 47,44 | 72,46 |
| P/E (5 %) | 47,08 | 106,13 | 178,86 |
| P/FCFE (2 %) | 19,45 | 35,68 | 55,10 |
| P/OCF (2 %) | 43,73 | 72,46 | 103,63 |

Los múltiplos Base quedan **28,8 % por debajo del DCF Base** y 2,5 % por encima del precio (68,59). Conciliación en `Resumen de valoraciones`: 6 controles OK, estado CONCILIADO. Compuerta `Supuestos y control!B60` = «LISTA PARA CALCULAR». **MOS solo sobre el DCF Base:** 64,18; el precio queda entre el MOS y el DCF Base.

**Diferencia material por explicar:** el P/E da 106 (Base) y 179 (Opt) porque la utilidad neta proyectada es alta frente a una utilidad LTM distorsionada por partidas no operativas; con peso 5 % su efecto es limitado, pero es la cifra menos fiable. P/FCFE y EV/FCFF son bajos por el FCFF/FCFE deprimidos por impuestos y reinversión, y pesan poco.

## Error propio corregido durante R4
En `Entradas desde DCF!B6:D6` había cargado como Ke el costo de capital inicial (10,00 %) en lugar del Ke real (10,49 %, `Cost of capital worksheet!B62`). Los valores presentes de los múltiplos usaban 10,00 %. Se corrigió a 0,1048752249 y se recalcularon todos los múltiplos, el Resumen y las huellas SHA-256 (M: `d39a4531…44c4`; Cons `b594687d…899d`; Opt `f82f812a…aee`). Las cifras de esta tabla son las posteriores a la corrección.

## Qué se cargó
- **Estados desde H (por etiqueta):** FY2017–FY2025 + LTM (`R4_evidencia/M_UBER_payload.json`). Arrendamientos reclasificados a «otros pasivos» (filas 23/27; filas de deuda 21/26 en 0), por decisión del usuario. Gasto por intereses con signo negativo (fila 14); ajuste del método de participación en la fila 30; EPS calculados.
- **Supuestos de las tres historias = los del DCF**, por multiplicadores sobre la base contable de M: crecimiento 11/7/13 % (año 1) y 14/9,75/16,25 % (años 2–5) con ancla LTM interanual 13,94 % (ingresos de hace un año 49.610), margen objetivo en base reportada 16,36/11,36/20,36 % (objetivos ajustados − 1,64 pts del ajuste de I+D), ventas/capital 2,8/2,0/3,4 y 2,5/1,8/3,0, g 4,0 %, ROIC terminal 13,23 % / costo de capital / 18,21 %, impuesto 25,17 %.
- **Entradas desde los tres DCF:** valor, Ke 10,49 %, Kd 6,10 %, costo de capital inicial 10,00 % y estable 8,25 %, EBIT 7.961, beta 1,20, ERP 4,69 %. «SHA-256» = hash del JSON de los valores transferidos (no del libro entero).
- Puente: caja 10.068, activos no operativos 11.473, minoritarios 1.304, 2.107,437 M de acciones, opciones 5,549 M a 52,23.

## Múltiplos de salida y pesos (juicio mío)
| Método | Cons | Base | Opt | Criterio |
|---|---|---|---|---|
| EV/EBITDA | 15,96x | 18,78x | 21,60x | −15 % / actual / +15 % |
| EV/FCFF | 26,78x | 31,50x | 36,23x | actual = FY2025 (LTM N/D) |
| P/E | 16,73x | 28,58x | 40,42x | Cons = mediana 5 años; Opt = TTM; Base = punto medio (el TTM está distorsionado por partidas no operativas) |
| P/FCFE | 8,26x | 9,72x | 11,18x | −15 % / actual / +15 % |
| P/OCF | 11,09x | 13,05x | 15,01x | −15 % / actual / +15 % |
**Tipo «Crecimiento»**: DCF 75 %, múltiplos 25 % (EV/EBITDA 10 %, EV/FCFF 6 %, P/E 5 %, P/FCFE 2 %, P/OCF 2 %). P/S y P/BV no se usan. EV/EBITDA pesa más porque Uber tiene EBITDA positivo y sin efecto de estructura de capital; P/E y flujos al accionista pesan poco por las partidas no operativas.

## Diferencias con la R4 de ChatGPT (reemplazada)
Allí EV/FCFF era N/D (peso 0) y los pesos eran 10/0/4/7/4 %. Aquí EV/FCFF se calcula con el valor de FY2025 (31,50x) y pesa 6 %. Queda como punto a decidir en R6 si el EV/FCFF debe excluirse por la normalización fiscal de 2024–2025.

## Controles
| Control | Estado |
|---|---|
| Compuerta B60 «LISTA PARA CALCULAR» | APROBADO |
| Conciliación `Resumen de valoraciones` (6 controles) | APROBADO |
| Ke de M = Ke del DCF Base | APROBADO (tras la corrección) |
| Fechas y cuadres de estados | APROBADO |
| Verificación documental contra 10-K/10-Q | **PENDIENTE** (estados «MODELADO · SIN CERTIFICAR») |
| M no descuenta el valor de las opciones (185,8 M ≈ 0,09 US$/acción) | Declarado |
| Revisión de fórmulas originales de M | NO re-verificada |
| Auditoría económica independiente | **NO_EJECUTADA (R6)** |
