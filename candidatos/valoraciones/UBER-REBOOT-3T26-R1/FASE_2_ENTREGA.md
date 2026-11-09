# UBER-REBOOT-3T26-R1 · Fase R2 (Históricos)

- **Libro:** 01 HISTÓRICOS `176tcVAz_RzHluf4kyjEEsMjDcDosldPdB5FBifO9YQA` · estado **CANDIDATO** (sin R6).
- **Fecha:** 2026-11-09 · **Agente:** Claude (Code, nube): SEC XBRL `companyfacts`, Alpha Vantage, Sheets.
- **Alcance:** FY2017–FY2025 + LTM (FY2016 sin dato XBRL: anterior a la salida a bolsa; balance desde FY2018). LTM = FY2025 + 9M-2026 − 9M-2025 (flujos) y saldos al 2026-09-30 (10-Q del 3T-2026).
- **Cómo se cargó:** `R2_evidencia/` (`hlib.py`, `mapping.py`, `payload.py`, empresa). Solo se escribieron las celdas de entrada de `Income Statement`, `Balance Sheet`, `Cash Flow Statement`, `Entradas históricas auxiliares` y `Trailing Valuation` fila 3; los ratios son las fórmulas de la plantilla. Insumo único: SEC XBRL; **no** se usó el libro Floyd previo como dato.

## Clasificación y límites
- Costo de ventas = costo de ingresos sin D&A; SG&A = ventas y marketing + G&A; D&A e I+D como líneas; «Otros gastos operativos» derivado = operaciones y soporte (línea sin etiqueta us-gaap), litigios y otros (3.198 en LTM).
- **Inversiones en otras empresas (Aurora, Didi, Grab, etc.):** fila 14 = acciones sin valor razonable fácil + método de participación (7.856 al 3T-2026). Los valores disponibles para la venta de largo plazo y las inversiones restringidas (seguros) quedan en «otros activos LP»: **clasificación a decidir en R3** al armar el puente (activos no operativos y caja).
- Caja: efectivo y equivalentes 9.558 (LTM); la caja restringida y las inversiones de corto plazo están aparte o dentro de «otros activos corrientes».
- FY2018: capital preferente convertible fuera del patrimonio (patrimonio negativo en FY2017–18).
- Impuestos: beneficio por liberación de valuation allowance en FY2024–25 (−5.758, −4.346): la tasa efectiva histórica no es normal.
- Participaciones no controladoras no redimibles incluidas en el patrimonio total; el redimible queda en otros pasivos LP.
- Gastos por intereses y de inversiones disponibles desde FY2018 (InterestExpenseNonoperating/InterestExpense).

## Controles
| Control | Estado |
|---|---|
| Activos = pasivos + patrimonio (FY2018–LTM) | APROBADO (diferencia 0) |
| CFO + CFI + CFF vs variación de caja | Diferencias hasta ±267 por caja restringida y efecto cambiario (declarado) |
| Ingresos LTM 56.526; EBIT LTM 7.034; utilidad neta 3.584 | APROBADO frente a XBRL; coincide con el LTM de la revisión Floyd (solo contraste, no insumo) |
| Fórmulas de ratios sin errores | APROBADO (Salud Financiera y Eficiencia de capital revisadas) |
| Verificación documental contra el 10-K | **PENDIENTE** |
| Clasificación de inversiones LP | PENDIENTE (R3) |

## Siguiente paso exacto
R3: fijar las tres historias (crecimiento, margen, ventas/capital, ROIC terminal, fracaso solo en la Conservadora), cargar las entradas comunes del motor Ginzu en los tres libros DCF y calcular costo de capital común con Rf 4,86 % y ERP madura 3,387 %. Según la instrucción del usuario (reconfigurar desde las Floyd), las historias de partida son las de la revisión Floyd vigente, revisadas contra estos Históricos antes de usarlas.
