# MELI-REBOOT-3T26-R1 · Fase R4 (múltiplos y resumen)

- **Fecha:** 2026-11-10 · **Agente:** Claude (Code, nube): Sheets, SEC XBRL, 10-Q. Estado **CANDIDATO** (sin R6).
- **Libros:** 03 MÚLTIPLOS `19jUYjQ-KXnLUjvQBXzTJhIRHJgxN79BdOfoqdB7REJk` y `Resumen de valoraciones` del DCF Base `174iyMLVgEsIw8sAWHNF3_SAvcbOoZbb1dB94gUF5yLc`.

## Resultado
| Valor por acción | Conservadora | **Base** | Optimista | Esperado (25/50/25) |
|---|---|---|---|---|
| DCF (principal) | 908,33 | **2.536,95** | 4.120,94 | 2.525,79 |
| Múltiplos consolidados (secundario) | 1.116,16 | 1.782,61 | 2.486,03 | 1.791,85 |
| Combinado 75/25 (secundario) | 960,29 | 2.348,37 | 3.712,21 | — |

| Método (peso total) | Cons | Base | Opt |
|---|---|---|---|
| EV/EBITDA (12 %) | 1.243,66 | 1.951,77 | 2.669,05 |
| EV/FCFF (3 %) | 480,98 | 815,76 | 1.367,57 |
| P/E (7 %) | 1.286,02 | 2.163,11 | 3.062,37 |
| P/FCFE (1,5 %) | 791,17 | 1.106,54 | 1.434,70 |
| P/OCF (1,5 %) | 898,80 | 1.263,52 | 1.620,57 |

Los múltiplos Base quedan **29,7 % por debajo del DCF Base** y 18,1 % por encima del precio (1.510). Conciliación en `Resumen de valoraciones`: 6 controles OK, estado **CONCILIADO**. Compuerta `Supuestos y control!B60` = «LISTA PARA CALCULAR». MOS solo sobre el DCF Base: 1.649,02; el precio queda **bajo el precio con MOS** (zona «COMPRA» del Resumen).

## Qué se cargó
- **Estados desde H** (`R4_evidencia/M_MELI_payload.json`), con estas decisiones: arrendamientos operativos y **fondeo del crédito** reclasificados a «otros pasivos» (el EV del libro coincide con el del DCF: deuda = solo notas corporativas y arrendamientos financieros, 2.369); gasto por intereses = «intereses y otras pérdidas financieras» incluyendo la diferencia de cambio (derivado, −409 LTM); D&A en la fila de D&A (está dentro de costos); EPS calculados; cambio en cuentas por pagar combinado con gastos acumulados.
- **Ceros declarados por falta de dato separado (no por dato real):** deuda corporativa FY2016–FY2024 (el XBRL solo separa 2025 y LTM; antes, todo el fondeo está en «otros pasivos»), cuentas por pagar (van dentro de «gastos acumulados»), ingresos diferidos antes de 2023. No afectan los resultados del LTM, que usan los saldos de septiembre de 2026; sí afectan los ratios históricos de deuda.
- **Supuestos de las tres historias = los del DCF**, por multiplicadores sobre la base contable: crecimiento 30/22/36 % (año 1) y 19/11/23 % (años 2–5) con ancla LTM interanual de 47,07 % (ingresos de hace un año 26.193), margen objetivo en base contable 11,56/7,06/14,56 % (objetivo ajustado − 1,94 pts del ajuste de I+D), ventas/capital 3,2/2,5/3,8 y 3,0/2,3/3,4, g 4,0 %, ROIC terminal 14,0 % / costo de capital / 16,4 %, impuesto efectivo 26,46 %. Puente: caja 7.375 (del libro; la usada en el DCF es 8.126 según MELI), NWC de septiembre de 2025 −1.599 (estimación de la deuda corporativa corriente), minoritarios 0.
- **Entradas desde los tres DCF:** valor, Ke 11,88 %, Kd 6,90 %, costo de capital inicial 11,67 % y estable 8,25 %, EBIT ajustado 3.604,7, beta 0,9286, ERP 7,556 %. «SHA-256» = hash del JSON de los valores transferidos (no del libro): Cons `31153723…2006`, Opt `b5b4dd11…d56e`, M `35cbba48…739a`.
- **Cambio frente a la plantilla:** la caja del libro de Múltiplos (7.375 = efectivo + inversiones CP) no es la de 8.126 del DCF (definición de MELI, con inversiones LP y activos digitales disponibles). Efecto sobre el valor por acción de los múltiplos: ≈ 15 por acción (0,7 %).

## Múltiplos de salida y pesos (juicio mío)
| Método | Actual (LTM) | Conservadora | Base | Optimista | Peso |
|---|---|---|---|---|---|
| EV/EBITDA | 18,15x | 15,43x (−15 %) | 18,15x | 20,87x (+15 %) | 12 % |
| EV/FCFF | N/D | 30x | 35x | 40x | 3 % |
| P/E | 40,50x | 34,43x | 40,50x | 46,58x | 7 % |
| P/FCFE | 4,37x | 3,71x | 4,37x | 5,03x | 1,5 % |
| P/OCF | 5,51x | 4,68x | 5,51x | 6,34x | 1,5 % |
**Tipo «Crecimiento»** (DCF 75 %, múltiplos 25 %). Dentro de los múltiplos pesan EV/EBITDA y P/E: el EBITDA ordinario y la utilidad son los únicos que no dependen de los fondos de clientes. **EV/FCFF, P/FCFE y P/OCF se dejan con peso casi nulo porque su flujo es poco fiable en MELI**: el flujo operativo (13.896 LTM) incluye el aumento de los fondos por pagar a clientes y del fondeo del crédito; M lo proyecta con un «ajuste de flujo residual» de 23,3 % de las ventas (mediana histórica) y un P/FCFE actual de 4,4x. Se mantienen en más de 0 % solo porque el libro y el contrato exigen cinco métodos con matriz de sensibilidad. **EV/FCFF no tiene ancla histórica válida (múltiplo actual N/D): 30/35/40x son un juicio mío sin respaldo.** Medianas históricas: P/E 51–81x (sesgadas por utilidades bajas), P/FCFE 9,5–38x, P/OCF 10,9–43,9x; no se usan (tope «Conservador ≤ actual» y flujos distorsionados). P/S y P/BV no se usan.

## Adaptaciones al libro (declaradas)
1. `Supuestos y control!B23` y encabezados: precio fijo 1.510 (la plantilla trae `GOOGLEFINANCE`).
2. `J8/J19/J30` de cada método: múltiplos de salida como valores.
3. `B92:D92`: impuesto 26,46 %. `Puente EEFF!D57` y `F20`.
4. Ceros del balance listados arriba.
5. Filas de fuente, fecha y estado de `Income Statement`, `Balance Sheet` y `Cash Flow Statement`.
Error de alineación detectado y corregido durante la carga (una fila de utilidad antes de impuestos quedó desplazada en el estado de resultados); el libro vigente es el corregido.

## Controles
| Control | Estado |
|---|---|
| Compuerta B60 «LISTA PARA CALCULAR» | APROBADO |
| Conciliación `Resumen de valoraciones` (6 controles) | APROBADO · CONCILIADO |
| Controles técnicos de los cinco métodos (cobertura, sensibilidad central) | APROBADO |
| Fechas y cuadres de balance, resultados y flujo | APROBADO |
| Verificación documental contra 10-K/10-Q | **PENDIENTE** (estados «MODELADO · SIN CERTIFICAR») |
| Diferencia múltiplos vs DCF (−29,7 %) | Explicada: los múltiplos usan EBITDA y utilidad FY+3 con múltiplos de hoy; el DCF recoge diez años de crecimiento |
| Revisión de fórmulas originales de M | NO re-verificada |
| Auditoría económica independiente | **NO_EJECUTADA (R6)** |

## Siguiente paso exacto
R5: análisis N1 (14 capítulos) y N2 (12 apartados) en un Google Doc, JSON de valoración y análisis, validadores, catálogo y publicación EN_REVISION.
