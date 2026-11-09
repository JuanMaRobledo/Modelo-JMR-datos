# CMG-REBOOT-3T26-R1 · Fase R2 (Históricos)

- **Libro:** 01 HISTÓRICOS `1fWez5DOCZv7RBUCCzKgrEUZa4imFmRCyVzFxuxirizI` · estado **CANDIDATO** (sin R6).
- **Fecha:** 2026-11-09 · **Agente:** Claude (Code, nube): SEC XBRL `companyfacts`, Alpha Vantage, Sheets.
- **Alcance:** FY2016–FY2025 + LTM (10 años completos). LTM = FY2025 + 9M-2026 − 9M-2025 (flujos) y saldos al 2026-09-30 (10-Q del 3T-2026).
- **Cómo se cargó:** `R2_evidencia/` (`hlib.py`, `mapping.py`, `payload.py`, empresa). Solo se escribieron las celdas de entrada de `Income Statement`, `Balance Sheet`, `Cash Flow Statement`, `Entradas históricas auxiliares` y `Trailing Valuation` fila 3; los ratios son las fórmulas de la plantilla. Insumo único: SEC XBRL; **no** se usó el libro Floyd previo como dato.

## Clasificación y límites
- Costo de ventas = costos operativos del restaurante (alimentos, mano de obra, ocupación y otros); G&A en SG&A; D&A como línea; «Otros gastos operativos» derivado (pre-apertura, deterioro y bajas: 105 en LTM).
- Split 50:1 (jun-2024): acciones promedio FY2016–2021 y acciones de portada FY2016–2023 ×50.
- Arrendamientos ASC 842 desde FY2019; sin deuda financiera en todo el período; sin dividendos.
- Interés e ingresos por inversiones no se separan en XBRL (filas 14–16 vacías); el «otro ingreso no operativo» es neto.
- **REVISAR en R3:** «Otros ajustes» del flujo LTM = 804 (frente a 107 en FY2025): partidas no monetarias del 9M-2026 sin desglosar; no afecta el DCF (que parte del EBIT).

## Controles
| Control | Estado |
|---|---|
| Activos = pasivos + patrimonio en los 11 períodos | APROBADO (diferencia 0,0) |
| CFO + CFI + CFF vs variación de caja | APROBADO con diferencias ≤ 2 (caja restringida y cambio) |
| Ingresos LTM 12.713 y EBIT LTM 1.795 | APROBADO frente a XBRL; coincide con el LTM de la revisión Floyd (solo contraste, no insumo) |
| Fórmulas de ratios sin errores (Salud Financiera, Márgenes, Eficiencia) | APROBADO (muestra revisada) |
| Verificación documental contra el 10-K de cada año | **PENDIENTE** (solo XBRL; contraste externo no ejecutado) |
| Precios de cierre fiscal | Alpha Vantage ajustado por split; no contrastados con otra fuente |

## Siguiente paso exacto
R3: fijar las tres historias (crecimiento, margen, ventas/capital, ROIC terminal, fracaso solo en la Conservadora), cargar las entradas comunes del motor Ginzu en los tres libros DCF y calcular costo de capital común con Rf 4,86 % y ERP madura 3,387 %. Según la instrucción del usuario (reconfigurar desde las Floyd), las historias de partida son las de la revisión Floyd vigente, revisadas contra estos Históricos antes de usarlas.
