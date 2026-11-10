# MSFT-REBOOT-3T26-R1 · Fase R2 (históricos)

- **Fecha:** 2026-11-10 · **Agente:** Claude (Code, nube): SEC XBRL (10-K FY2026 y 10-Q 1T-FY2027), Alpha Vantage, Google Sheets. Estado **CANDIDATO**.
- **Libro:** 01 HISTÓRICOS `1t5ZM7SQF-An3WMJXfdYb0Q_XGHeJuiBY_rervY7eK8E`. Evidencia: `R2_evidencia/` (`msft.py` con los tags, `payload_MSFT.json` con lo escrito, `fuentes_MSFT.json`).

## Qué se cargó
Income Statement, Balance Sheet, Cash Flow Statement (FY2017–FY2026, años fiscales al 30 de junio, + LTM al 30-sep-2026), entradas auxiliares, precios de cierre fiscal en `Trailing Valuation`, `Guía y empresa` y `Fuentes y clasificación`. Solo se escribieron entradas; los ratios son las fórmulas de la plantilla (leí márgenes y valoración histórica: sin errores). LTM = FY2026 + 3M-FY2027 − 3M-FY2026: ingresos 346.445, EBIT 163.191 (47,1 %), utilidad neta 142.631, flujo operativo 195.878, capex 135.921.

## Clasificación (decisiones mías)
- **Utilidad neta ≠ utilidad operativa:** incluye ganancias y pérdidas de las inversiones en OpenAI y de otras inversiones (−5.163 M en FY2025, +10.447 M en FY2026, +14.549 M LTM), que no entran al EBIT.
- **Arrendamientos financieros (66.594 M en junio de 2026; 70.973 M en septiembre)** no tienen línea propia en el balance: están en «otros pasivos». Se leen de la nota de arrendamientos y **se tratarán como deuda** (su amortización está en el EBIT, su interés no). Efecto: sin ellos, la deuda parecería 40.294 M (la deuda con bonos) en vez de ≈ 107.000 M.
- **Capex = efectivo pagado por propiedades y equipo** (115.948 M en FY2026). No incluye 24.608 M de activos recibidos por arrendamientos financieros; la inversión total en centros de datos es mayor que el capex del flujo de caja.
- **D&A** = depreciación + amortización de las notas (redondeadas a 100 M) para los años; LTM de la línea «depreciación, amortización y otros» del 10-Q.
- **Impuestos FY2018** (19.903 M) incluyen el cargo por la reforma tributaria de EE. UU.

## Error mío corregido
En las cargas de CMG, UBER y MELI (y en MSFT hasta este momento) el signo de los cambios en **cuentas por pagar, impuestos e ingresos diferidos** salió invertido (el código los trataba como activos). **En MSFT está corregido** (verificado: cuentas por pagar FY2026 +5.268; ingresos diferidos +9.361). En los libros de CMG, UBER y MELI esas líneas del flujo de caja (filas 8–11) tienen el signo contrario; el flujo operativo total y «otros ajustes» (derivado) no cambian, y los DCF y múltiplos no las usan, pero **el cuadro de flujo está mal etiquetado**. Queda para corregir antes de R6 (no se hizo en esta sesión).

## Controles
| Control | Estado |
|---|---|
| Balance cuadra (A = L+E) en los 11 períodos | APROBADO |
| CFO + CFI + CFF vs Δ caja | PARCIAL: la diferencia es el efecto cambiario (máx. 210) |
| LTM = FY2026 + 3M-FY27 − 3M-FY26 reproducido con las cifras del 10-Q (balance, flujo operativo 58.000 M del trimestre) | APROBADO |
| Verificación documental fila por fila contra los 10-K | NO_EJECUTADO |
| `AISLAMIENTO=OK` | Verificado: solo SEC XBRL, 10-K/10-Q y precios; la ficha A-1.2 archivada no se usó |

**PASOS 3/3.** Siguiente paso exacto: R3, tres historias de MSFT con evidencia del 10-Q (Azure, ciclo de inversión en IA, RPO de 683 mil M, margen), costo de capital, motor original y sensibilidades.
