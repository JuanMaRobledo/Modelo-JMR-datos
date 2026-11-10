# CMG-REBOOT-3T26-R1 · Fase R4 (múltiplos y resumen)

- **Fecha:** 2026-11-10 · **Agente:** Claude (Code, nube): Sheets, SEC XBRL · esfuerzo: alto.
- **Libros:** 03 MÚLTIPLOS `1jdUkjDwPG79FmSGLbZfQd-xTXMVBC8xJ9wG2imACeK0` y `Resumen de valoraciones` del DCF Base `1asO4BR42MypptINAooJ3hP6joY5fFUYDB5IM2NSDo7U`. Estado **CANDIDATO** (R5 pendiente; sin R6).

## Resultado
| Valor por acción | Conservadora | **Base** | Optimista | Esperado (25/50/25) |
|---|---|---|---|---|
| DCF (principal) | 17,69 | **32,28** | 40,47 | 30,68 |
| Múltiplos consolidados (secundario) | 26,32 | 35,46 | 44,33 | 35,39 |
| Combinado 65/35 (secundario) | 20,71 | 33,40 | 41,82 | — |
| Múltiplos frente al precio (34,43) | −23,6 % | +3,0 % | +28,8 % | +2,8 % |

Los múltiplos Base quedan **9,8 % por encima del DCF Base** y **3 % por encima del precio**. Conciliación en `Resumen de valoraciones`: 6 controles OK, estado **CONCILIADO**. Compuerta `Supuestos y control!B60` = «LISTA PARA CALCULAR».

## Qué se cargó
- **Estados desde H (por etiqueta):** FY2016–FY2025 + LTM en `Income Statement`, `Balance Sheet`, `Cash Flow Statement` (`R4_evidencia/M_CMG_payload.json`). Diferencias de formato: inventarios separados (fila 8) y otros activos corrientes derivados; EPS calculados como utilidad / acciones (no reportados); cambios en cuentas por pagar, impuestos y deferidos en las filas de la plantilla, con las provisiones acumuladas en «otros»; efecto cambiario/otros derivado (fila 39).
- **Arrendamientos (decisión del usuario):** los pasivos por arrendamiento se **reclasificaron a «otros pasivos»** (filas 23 y 27) y las filas de deuda (21 y 26) quedan en 0, de modo que deuda financiera = 0 y EV = capitalización − caja. Coherente con el DCF, cuyo EBIT ya deduce el alquiler. Efecto: EV/EBITDA LTM 19,5x (con arrendamientos habría sido 22,1x).
- **Intereses:** CMG no tiene deuda; filas de ingresos y gasto por intereses = 0 (el ingreso por intereses está dentro de «otros no operativos», 34,9 M LTM).
- **Supuestos de las tres historias = los del DCF** (por multiplicadores sobre la base contable de M): crecimiento 9,5/6,4/11,0 % año 1 y 8,8/6,4/10,9 % años 2–5 (ancla LTM interanual 7,86 %), margen objetivo 16/13/18 % (ancla 14,12 %, sin ajuste por I+D), ventas/capital 2,7/2,2/2,9 y 2,9/2,4/3,2, g 4,0 %, ROIC terminal 18,36 % o costo de capital (Cons), impuesto efectivo 24,74 % en FY+1…FY+3. **Ventas/capital FY6–10 de referencia = 2,9 (de la Base), no la industria**: M no trae un dato de industria para Restaurant/Dining.
- **Entradas desde los tres DCF** (hoja `Entradas desde DCF`): valor por acción, Ke, Kd, WACC inicial y estable, EBIT, beta y ERP. «Huella SHA-256» = hash del JSON de los valores transferidos (valor, WACC, Ke, beta, ERP), no del libro entero.
- Opciones/SOSARs (12,268 M a 39,51) y activos no operativos (100,365 M) se cargaron en el puente (`Supuestos B61`, `Puente EEFF`). **M no descuenta el valor de las opciones** (126,7 M ≈ 0,10 US$ por acción en el DCF).

## Múltiplos de salida y pesos (juicio mío)
| Método | Actual | Conservadora (−15 %) | Base (= actual) | Optimista (+15 %) | Peso total |
|---|---|---|---|---|---|
| EV/EBITDA | 19,52x (LTM) | 16,59x | 19,52x | 22,45x | 8 % |
| EV/FCFF | 42,62x (FY2025; LTM N/D) | 36,23x | 42,62x | 49,01x | 5 % |
| P/E | 31,62x | 26,88x | 31,62x | 36,36x | 12 % |
| P/FCFE | 28,84x | 24,51x | 28,84x | 33,17x | 7 % |
| P/OCF | 18,55x | 15,77x | 18,55x | 21,33x | 3 % |
**Regla (distinta de AAPL):** las medianas históricas de CMG (EV/EBITDA 33,4x a 10 años; P/E 59,8x) están muy por encima de los múltiplos actuales porque la empresa crece mucho menos y con menor margen que en 2021–24. Usarlas violaría el tope «Conservador ≤ actual». Por eso la Base mantiene el múltiplo actual (sin expansión ni compresión), la Conservadora lo comprime 15 % (crecimiento 6,4 %, margen 13 %) y la Optimista lo expande 15 % (menos del tope de +25 % que exigiría justificación). **Pesos**, tipo «Madura», DCF 65 % y múltiplos 35 %: P/E 12 % (sin deuda, EPS por recompras), EV/EBITDA 8 % (alquiler ya en el EBITDA y fuera del EV), P/FCFE 7 %, EV/FCFF 5 % (el FCFF está deprimido por capex de expansión y su LTM no calcula), P/OCF 3 % (CFO con partidas no explicadas, ver abajo). P/S y P/BV no se usan.

## Adaptaciones al libro (todas declaradas; no cambian la matemática de múltiplos)
1. `Supuestos y control!B23`: precio fijo 34,43 (la plantilla trae `GOOGLEFINANCE`).
2. `Income Statement` filas 13–14: ceros (sin deuda; el ingreso por intereses no se separa en XBRL).
3. `J8/J19/J30` de cada método: múltiplos de salida como valores (sustituyen la fórmula por defecto).
4. `B92:D92`: impuesto 24,74 % (efectivo, igual que el DCF).
5. `Puente EEFF!D57` (NWC comparable al 30-sep-2025 = −797,6) y `F20` (activos no operativos FY−1 = 197,1).
6. `Supuestos B55` = 2,9 (ver arriba).
7. Corrección de signo de impuestos FY2018 (+91,883) también en este libro.

## Controles
| Control | Estado |
|---|---|
| Compuerta `B60` = «LISTA PARA CALCULAR» | APROBADO |
| Controles de los cinco métodos (cobertura, signos, sensibilidad central) | APROBADO; POCF con «REVISAR · AJUSTES >10 %» y EV/EBITDA con «COMPROBAR D&A» |
| Estados de M con cuadres propios (activo, pasivo, patrimonio, CFO/CFI/CFF) | APROBADO |
| Conciliación `Resumen de valoraciones` (6 controles) | APROBADO · CONCILIADO |
| Cierres de fechas entre los tres estados | APROBADO |
| Verificación documental contra los 10-K/10-Q | **PENDIENTE** (todas las verificaciones quedan «PENDIENTE») |
| «Otros ajustes» del flujo LTM (804 M) | PENDIENTE (afecta el CFO proyectado de P/OCF) |
| `Estado de fuentes primarias` = PENDIENTE; EV/FCFF LTM sin calcular | PARCIAL |
| Sensibilidad 5×5 por múltiplo | Disponible en cada hoja de método (solo Base); falta derivar la versión a valor presente para el JSON (R5) |
| Auditoría económica independiente | **NO_EJECUTADO (R6)** |

## Siguiente paso exacto
R5: escribir el análisis (N1 de 14 capítulos y N2 de 12 apartados) con cifras de H, los tres DCF y M, generar los JSON `contratoLibros=jmr-reboot-3libros-v1`, correr `validar_reboot.cjs` y publicar EN_REVISION si pasa la puerta.
