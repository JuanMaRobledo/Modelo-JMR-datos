# MSFT-REBOOT-3T26-R1 · Fase R4 (múltiplos y resumen)

- **Fecha:** 2026-11-10 · **Agente:** Claude (Code, nube): Sheets, SEC XBRL, 10-Q. Estado **CANDIDATO** (sin R6).
- **Libros:** 03 MÚLTIPLOS `1m_mbps0ZIVzsDUNyz76UzPGhei5YLuWwnSffk10496o` y `Resumen de valoraciones` del DCF Base `19f9zo6xbYTnrjoAZwVf5ViHzVCEnkde9no2cryOBQjA`.

## Resultado
| Valor por acción | Conservadora | **Base** | Optimista | Esperado (25/50/25) |
|---|---|---|---|---|
| DCF (principal) | 232,38 | **496,21** | 676,08 | 475,22 |
| Múltiplos consolidados (secundario) | 366,43 | 503,13 | 657,02 | 507,43 |
| Combinado 65/35 (secundario) | 279,30 | 498,63 | 669,41 | — |

| Método (peso total) | Cons | Base | Opt |
|---|---|---|---|
| EV/EBITDA (8 %) | 389,59 | 544,27 | 679,17 |
| EV/FCFF (8 %) | 377,91 | 500,23 | 710,15 |
| P/E (10 %) | 358,64 | 506,22 | 634,77 |
| P/FCFE (4 %) | 347,44 | 458,93 | 652,57 |
| P/OCF (5 %) | 341,77 | 471,10 | 584,62 |

Los múltiplos Base quedan **1,4 % por encima del DCF Base** y 5,2 % por debajo del precio (530,61). Conciliación en `Resumen de valoraciones`: 6 controles OK, estado **CONCILIADO**. Compuerta `Supuestos y control!B60` = «LISTA PARA CALCULAR». MOS solo sobre el DCF Base: precio con MOS 322,54; el precio queda **sobre el DCF Base** (−6,9 %): sin margen de seguridad.

## Qué se cargó
- **Estados desde H** (`R4_evidencia/M_MSFT_payload.json`). Decisiones: arrendamientos financieros (70.973) reclasificados a deuda (fila 22, restados de otros pasivos de largo plazo; la separación corriente/no corriente no es posible en XBRL); arrendamientos operativos NO son deuda; AP, deuda de corto plazo e ingresos diferidos numéricos para que ΔNWC y el residual de flujo operativo calculen.
- **Supuestos de las tres historias = los del DCF** por multiplicadores sobre la base contable (crecimiento, margen en base reportada, ventas/capital 1–5 y 6–10, ROIC, g = 4 %/4,86 %). Ancla LTM de ingresos hace un año 293.812; impuesto efectivo 19,68 %; marginal 23 % (estimación); Kd 5,2 % (estimación).
- **Entradas desde los tres DCF:** valores 232,38/496,21/676,08, Ke 10,64 %, costo de capital inicial 10,49 % y estable 8,25 %, beta 1,2785, ERP 4,524 %. «SHA-256» = hash del JSON de los valores transferidos (no del libro): Cons `c9438157…0831`, Opt `08cf8698…fc3c`, M `68a8107a…8cab`.

## Múltiplos de salida y pesos (juicio mío)
| Método | Actual (LTM) | Conservadora | Base | Optimista | Peso |
|---|---|---|---|---|---|
| EV/EBITDA | 19,36x | 16,46x | 19,36x | 22,26x | 8 % |
| EV/FCFF | N/D | 40,55x | 47,70x | 54,86x | 8 % |
| P/E | 27,63x | 23,49x | 27,63x | 31,77x | 10 % |
| P/FCFE | 75,64x | 37,91x | 44,60x | 51,29x | 4 % |
| P/OCF | 20,12x | 17,10x | 20,12x | 23,14x | 5 % |

**Tipo «Madura»** (DCF 65 %, múltiplos 35 %). **EV/FCFF y P/FCFE usan la mediana de 5 años (47,70x y 44,60x) como Base**: el FCFF/FCFE de los últimos doce meses está deprimido por el aumento de capex de IA y el múltiplo actual no es válido (N/D) o es extremo (75,64x). Es un juicio mío con respaldo en la serie histórica (10 años: 41,64x/38,83x; 5 años: 47,70x/44,60x). Conservador/Optimista = Base −15 %/+15 %.

## Decisiones de método declaradas
| Decisión | Fuente/criterio | Efecto |
|---|---|---|
| Arrendamientos financieros como deuda (EBIT no incluye su interés) | 10-K/10-Q, nota de arrendamientos | ≈ −9,5 por acción |
| Arrendamientos operativos no son deuda | Regla del usuario | — |
| OpenAI y otras inversiones (37.808) a valor en libros como no operativas | 10-Q | Efecto conocido: valor de mercado puede ser distinto |
| Capex excluye 24.608 de activos por arrendamientos financieros | Coherencia con deuda | — |
| Beta bottom-up EE. UU. 1,28 (observada ≈ 1,0) | Damodaran | Con beta 1,00 la Base sería 533,88 |
| EV/FCFF y P/FCFE con medianas de 5 años | ver arriba | — |
| Ceros declarados para datos no separables | XBRL | No afectan LTM |

## Adaptaciones al libro
1. Precio fijo 530,61 en `Supuestos y control!B23` (la plantilla trae `GOOGLEFINANCE`).
2. `J8/J19/J30` de cada método: múltiplos de salida como valores.
3. `B92:D92`: impuesto 19,68 %. `Puente EEFF!D57` y `F20`.
4. Filas de fuente, fecha y estado en los tres estados.
5. Rango temporal `R7:T12` usado para leer precisión completa y **borrado** después.

## Controles
| Control | Estado |
|---|---|
| Compuerta B60 «LISTA PARA CALCULAR» | APROBADO |
| Conciliación `Resumen de valoraciones` (6 controles) | APROBADO · CONCILIADO |
| Matrices 5×5 de los cinco métodos leídas (centro = Base) | APROBADO |
| Verificación documental contra 10-K/10-Q | **PENDIENTE** |
| Revisión de fórmulas originales de M | NO re-verificada |
| Auditoría económica independiente | **NO_EJECUTADA (R6)** |

## Siguiente paso exacto
R5: Nivel 1 (14 capítulos), Nivel 2 (12 apartados), JSON de valoración y análisis, catálogo. Luego R6 en sesión independiente.
