# F2 · CMG · Modelo JMR Floyd · CMG-FLOYD-20261108-R1 — entrega: CERRADA CON CONTROLES PENDIENTES

**Fecha:** 2026-11-08 · **Corte:** FY2016–FY2025 + LTM al 30-sep-2026 · **Herramienta/modelo:** Claude Code, `claude-sonnet-5-5` (esfuerzo no reportado) · **AISLAMIENTO=OK** · **PASOS: 5/6 ejecutados** (H1, conciliaciones, ratios, H2, huella; el script oficial `estados_completos.py` / `auditar_ceros_materiales.py` / `auditar_estados_sec.py` NO EJECUTADO como script: se hicieron las pruebas equivalentes a mano descritas abajo).
**Libros:** Históricos `14ONchw6fXR9tSQs_OlQ3_Nio6d1vobUcH9LLgyZ6REs` (pestañas de históricos visibles, resto ocultas; pestaña `Fuentes y clasificación`) · Valoración `1f7BMt0ynbvjFUT84ftUmkPfxyJvmPvcqQ-7GW7EWtAY`.

## H1 · Históricos
Diez ejercicios (Dec-16 … Dec-25) y LTM Sep-26 de resultados, balance y flujo de caja, desde XBRL SEC (último 10-K que informa cada FY; 10-K FY25 y 10-Q 3T-26). Cada partida material tiene fuente (tag us-gaap), clasificación (reportada / derivada / residual conciliado / incluida en otra línea / no aplicable / pendiente) y nota en `Fuentes y clasificación` (42 filas). Precios de cierre fechados y ajustados por el split 50:1 en `Trailing Valuation` fila 3; acciones ≤ FY2021 × 50. LTM de flujos = FY25 + 9M-26 − 9M-25; balance = 30-sep-2026; saldos iniciales del LTM = 30-sep-2025.

## Conciliaciones (APROBADO)
- EBIT = ingresos − costos y gastos: diferencia 0,0 en 11/11 columnas; EBT − impuesto − utilidad neta: 0,0 (FY2018: el tag XBRL del impuesto trae signo invertido, −91,9; se registra gasto de 91,9 = EBT 268,5 − NI 176,6).
- Balance: activos − pasivos − patrimonio = 0,0 y L+E − activos = 0,0 en 11/11. Cifras del 30-sep-2026 cotejadas con el texto del 10-Q (efectivo 634.210, inversiones 268.354, activos 9.432.683, pasivos 6.977.539, EBIT 9M 1.374.622). FY2025 cotejado con el 10-K (ingresos 11.925.601; EBIT 1.935.798).
- Flujo: CFO + CFI + CFF − Δ caja = efecto cambiario (|≤2,1|), 11/11.
- Ratios por fórmula de la plantilla, no pegados. Reproducción independiente: ROE FY25 = 1.535,8 / ((2.830,6 + 3.655,5)/2) = 47,36 % (hoja 47,36 %); ROE LTM = 1.377,2 / ((2.455,1 + 3.221,8)/2) = 48,52 % (hoja 48,52 %); ROIC FY25 = 1.479,4 / 6.815,3 = 21,71 % (hoja 21,71 %); P/E FY25 = 37,00 / 1,147 = 32,3x (hoja 32,35x).

## Hallazgos y clasificaciones relevantes
1. **Interés y otros:** CMG presenta una sola línea «Interest and other income, net» (73,7 en FY25; 21,6 en 9M-26, cae por menor inversión en valores del Tesoro). No hay gasto por intereses: sin deuda.
2. **CFO LTM de 2.348 inflado:** el cambio en impuestos por pagar aporta +222,0 (9M-26 +203,7 frente a −42,4 en 9M-25: pago diferido, no recurrente). Normalizado ≈ 2.126. Afecta a múltiplos P/OCF y P/FCFE (F3).
3. **Recompras:** 2.425,5 en FY25 y 2.206,7 LTM, con patrimonio contable de 2.455 (el capital invertido contable es pequeño; ROE 48 %).
4. **Arrendamientos ASC 842:** pasivo 5.599,0 (CP 321,6 + LP 5.277,5) y activo por derecho de uso 4.928,1 al 30-sep-2026; el gasto está en ocupación (EBIT).
5. **Costos:** margen por restaurante (antes de D&A, G&A, preapertura) 23,8 % LTM frente a 26,7 % en FY24; labor 25,6 % de los ingresos (+0,6 pp), otros costos 15,5 % (+1,0 pp), G&A 6,0 % (+0,5 pp) en 9M-26.
6. **SBC:** 111,9 LTM (≈0,9 % de ingresos); dilución neta negativa por recompras (acciones 1.438,6 M en FY16 ajustadas → 1.265,0 M).

## H2 · Traspaso unidireccional (`JMR-valuation/reference/modelo_floyd_2026-11-08/cmg/h2.py`)
FY-2 (2023), FY-1 (2024), FY (2025) y LTM, columnas I:L, desde Históricos a Valoración, sin `IMPORTRANGE`, solo celdas sin fórmula en el destino. 316 celdas escritas, 98 con fórmula omitidas. Conciliación posterior: 484 celdas comparadas, 14 diferencias, todas **celdas con fórmula** del destino (`Income Statement!I4` y `Entradas históricas auxiliares!I17:I30`, saldos iniciales de FY-2 que dependen de FY-3, fuera del alcance de H2): ratios de FY-2 que exigen balance de apertura quedan en blanco en Valoración y están completos en Históricos. Fórmulas y selectores de la plantilla intactos; `Huella motor` 0/0 tras la carga.
Se sustituyeron las etiquetas «FY-n» de la fila 2 por fechas (Dec-23…, LTM Sep-26): la fórmula de `Input sheet!D12` las exige («Years since last 10K» = 0,75).

## Pendientes (no bloquean F3)
- FY2016: desglose de compras/ventas de inversiones no disponible en el XBRL (CFI de +326,8 reconciliado; 585,6 sin clasificar en «Other Investing»). PENDIENTE; inmaterial para el DCF (historia de 2016).
- Inversiones LP separadas solo desde FY2020; en FY16-19 pueden estar dentro de otros activos. PENDIENTE.
- Scripts oficiales `estados_completos.py`, `auditar_ceros_materiales.py`, `auditar_estados_sec.py`, `diff_formulas_plantilla.py`: NO EJECUTADOS (pruebas equivalentes manuales y `Huella motor` documentadas). Impacto: control de huella cubierto por la hoja; cotejo de ceros hecho a mano en D&A (no cero), I+D (no aplicable), SBC (no cero), deuda (cero sustentado), arrendamientos (reportados).
- Métricas operativas (restaurantes, AUV, comparables, costos de apertura) fuera de los estados: se documentan en F3 desde 10-K/10-Q.

## Siguiente: F3 con los libros conciliados.
