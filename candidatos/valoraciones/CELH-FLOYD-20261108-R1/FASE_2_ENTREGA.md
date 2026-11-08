# F2 · CELH · Modelo JMR Floyd · CELH-FLOYD-20261108-R1 — entrega: CERRADA CON CONTROLES PENDIENTES

**Fecha:** 2026-11-08 · **Corte:** FY2016–FY2025 + LTM al 30-sep-2026 · **Herramienta/modelo:** Claude Code, `claude-sonnet-5-5` (esfuerzo no reportado) · **AISLAMIENTO=OK** · **PASOS: 5/6 ejecutados** (H1, conciliaciones, ratios, H2, huella ejecutados; los scripts oficiales `estados_completos.py` / `auditar_ceros_materiales.py` / `auditar_estados_sec.py` NO EJECUTADOS: se hicieron las pruebas equivalentes descritas abajo).
**Libros:** Históricos `1MLwY0b7u4pKUgu5hDzj0hN2S73yu_Ng323zAcUCY8qg` · Valoración `1i7KsD5LJ98XOVjVPrS355weuaSuNo_ISuMVSHS_4MhU`.

## H1 · Históricos
Diez ejercicios (Dec-16 … Dec-25) y LTM Sep-26 de resultados, balance y flujo de caja, desde XBRL de la SEC (último 10-K que informa cada FY; 10-K FY25 y 10-Q 3T-26). Cada partida lleva la etiqueta us-gaap y la clasificación en la nota de la hoja de origen. LTM de flujos = FY25 + 9M-26 − 9M-25; balance = 30-sep-2026; saldos de apertura = 31-dic-2015. Precios de cierre fechados en `Trailing Valuation` fila 3, **ajustados por el split 3:1 de nov-2023** (Alpha Vantage, cierre ajustado); acciones y promedios ponderados anteriores al split multiplicados por 3 (acciones en circulación hasta 2021 y promedios hasta 2020; 2021-2025 ya vienen ajustados en el 10-K FY23).

## Conciliaciones (APROBADO, por script reproducible)
- Ingresos − costo − SG&A − otros − EBIT = 0 en 11/11 columnas (el rubro «otros gastos operativos» recoge solo las comisiones por terminación de distribuidores: 327,5 en FY25 y 169,5 LTM).
- EBT − impuesto − utilidad neta = 0 en 11/11.
- Activos = pasivos + mezzanine + patrimonio en 11/11 (el mezzanine de PepsiCo, 824,5 en 2022-2024 y 1.760,0 en 2025 y 3T-26, se suma a «Total Shareholders' Equity»; el patrimonio común es la fila 34).
- Flujo: CFO + CFI + CFF + tipo de cambio = variación de caja y caja restringida (|diferencia| < 0,05) en 11/11.
- Cotejo directo con el 10-Q 3T-26 (EBIT 9M 386.310, ingresos 9M 2.447.768, caja 700.617, activos 5.152.385, pasivos 2.117.042, CFO 9M 450.184, recompras 167.541 + 10.037) y con el 10-K FY25 (ingresos 2.515.269; EBIT 141.062). Las recompras de 9M-26 (167,5 M) no están en el XBRL consultado y se tomaron del texto del 10-Q.

## Clasificación de partidas sin cifra separada
| Partida | Estado | Nota |
|---|---|---|
| Depreciación en el estado de resultados (fila 9) y I+D (fila 10) | incluida en otra línea / no aplicable | la D&A está en costo de ventas y SG&A (flujo de caja: 29,5 FY25; 38,8 LTM); CELH no reporta I+D |
| Inversiones a corto plazo y largas (filas 4 y 14) | no aplicable | el balance no las muestra; se registra 0 con esa justificación |
| Arrendamientos (filas 21 y 26) | reportado hasta FY25; **LTM = 0 por no desglosado** | el 10-Q 3T-26 no separa el arrendamiento operativo (FY25: 4,5 + 13,8); queda dentro de otros pasivos. Inmaterial |
| Efectivo restringido | reportado | 141,1 a dic-2025 (pago a distribuidores, dentro de otros activos corrientes); 0 al 30-sep-2026 |
| Impuesto 2019 | cero explícito | utilidad neta = utilidad antes de impuestos |
| Intereses pre-2022 | neto | solo el XBRL neto está disponible (−0,2 a −0,5) |
| Deuda corriente 2016-2024 | cero explícito | sin deuda a largo plazo hasta 2025 (excepto 2018-2019, deuda corriente de 8,6) |

## Hallazgos relevantes
1. **Resultados 2025 y 2026 distorsionados por una sola partida:** 327,5 M de comisiones por terminación de distribuidores en FY25 (246,7 M en el 3T-25) y 88,8 M en 9M-26. EBIT LTM sin ellas: 582,0 M (18,4 %).
2. **Adquisiciones:** Alani Nu (1.278,8 M en efectivo, abr-2025) y Rockstar (28-ago-2025, a cambio de preferentes Serie B y del capitaneo con PepsiCo): el LTM incluye 12 meses de Alani Nu y ~10 de Rockstar.
3. **Deuda:** préstamo a plazo de 900 M (2025), saldo de principal 693,0 M al 30-sep-2026.
4. **Concentración con parte relacionada (PepsiCo):** 1.501,4 M de 2.447,8 M de ingresos en 9M-26 (61 %), 390,3 M de cuentas por cobrar, 734,5 M de «deferred other costs» no corrientes y 456,2 M de ingresos diferidos no corrientes.
5. **CFO inestable:** FY25 incluye +255 de ingresos diferidos y +45 de acumulados; LTM 330,7 vs FY25 359,4. Afecta a P/OCF y P/FCFE (contrastes sin peso).
6. **Ratios históricos** por fórmula de la plantilla (no pegados). ROIC/ROE de 2016-2018 no son interpretables (capital invertido muy pequeño).

## H2 · Traspaso unidireccional (`h2.py`, en el expediente de la sesión)
FY-2 (2023), FY-1 (2024), FY (2025) y LTM, columnas I:L, desde Históricos a Valoración, sin `IMPORTRANGE`, solo celdas sin fórmula en el destino: 308 celdas escritas, 0 omitidas por fórmula. Fórmulas y selectores de la plantilla intactos; `Huella motor` 0 diferencias tras la carga. Etiquetas «FY-n» de la fila 2 sustituidas por fechas (Dec-23 … LTM Sep-26), exigido por `Input sheet!D12` (años desde el último 10-K = 0,75).

## Pendientes (no bloquean F3)
- Scripts oficiales `estados_completos.py`, `auditar_ceros_materiales.py`, `auditar_estados_sec.py`, `diff_formulas_plantilla.py`: NO EJECUTADOS. Cubierto por conciliaciones por script propio y por `Huella motor`. Impacto: la verificación de ceros se hizo a mano en D&A, I+D, SBC, deuda, arrendamientos.
- Promedios ponderados del LTM: se usaron los 9M-26 (254,8 y 257,3 M) por no existir un promedio móvil de 12 meses; el efecto es solo sobre el EPS LTM.
- Verificación primaria del precio de cierre ajustado de 2016-2020: una sola fuente (Alpha Vantage).
- Métricas de marca (Alani Nu, Celsius, Rockstar), cuota y distribución: fuera de los estados; se documentan en F3 desde el 10-Q y la presentación de resultados.

## Siguiente: F3 con los libros conciliados.
