# Vínculos Floyd R1–R6 definidos (sin IMPORTRANGE)

Definición ejecutable en `JMR-valuation/scripts/floyd_sync/vinculos_floyd.py` y `reglas_estados.py`. Cada tramo mueve solo **celdas de entrada** (constantes); los resultados siguen calculándolos las fórmulas del libro origen. Evidencia sobre copias de UBER: `definicion_vinculos_UBER.json`.
Criterio de aceptación de una definición: **escribir lo que el vínculo escribiría produce, en UBER, el mismo contenido que había cargado la IA** (salvo diferencias explicadas abajo).

| Tramo | Vínculo(s) | Origen → destino | Piezas | Coincidencia con lo cargado |
|---|---|---|---|---|
| H → D (×3: B, C, O) | `h_a_db`, `h_a_dc`, `h_a_do` | `IS!L3,L12,L15`; `BS!L35`; `BS!L20+L25`; `BS!L3+L4`; `Trailing Valuation!L3` → `Input sheet!B11,B12,B13,B14,B15,B18,B22`; `IS!L10,K10,J10,I10` → `R& D converter!F7,B11,B12,B13` | 11 c/u | 33/33 |
| H → M precio | `h_a_m_precio` | `Trailing Valuation!L3` → `Supuestos y control!B23` | 1 | 1/1 |
| H → M estados | `h_a_m_income`, `_balance`, `_cash` | por **etiqueta**, solo filas de M que son constantes | 17 + 31 + 26 | 74/74 |
| D → M | `db_a_m`, `dc_a_m`, `do_a_m` | 8 celdas por libro (`Valuation output!B33,B17,B5`; `Cost of capital worksheet!B62,B37,C57,B27`; `Input sheet!B35`) → `Entradas desde DCF!B/C/D5:12` | 8 c/u | 21/24 (3 por redondeo del Ke, ver abajo) |
| D‑C, D‑O → Resumen | `dc_a_resumen`, `do_a_resumen` | `Valuation output!B33,B17`, `Input sheet!B35`, `Cost of capital worksheet!B62` → `Resumen!C5:C8` / `E5:E8` | 4 c/u | 8/8 |
| M → Resumen | `m_a_resumen` | `Resumen de Valoración!B7:B11` (normalizado a 100 %), `C7:E11`, `C65:E65`, `Entradas desde DCF!B6` → `Resumen!B24:B28, C24:E28, C29:E29, D32` | 4 | 3/4 (redondeo) |

**Reglas por etiqueta H→M (mecánicas):** igual etiqueta → copia; `Interest Expense` → signo negativo; `Total Cash…` = Cash + ST investments; `Total Trade Receivables` = Accounts Receivable; `Accrued Expenses`/`Unearned Revenue` → vacío = 0; `Changes in Other Operating Activities` = Changes in Accrued + Changes in Other. **Política de arrendamientos «otros_pasivos»** (decisión del usuario en la revisión): `Other Current/Long-Term Liabilities` suman la porción de arrendamientos de H (en blanco si falta el dato principal: no se inventan ceros), y `Leases` y `Current Portion of Long-Term Debt` quedan en 0.
**Nunca se escribe en filas con fórmulas de M.**

**Diferencias explicadas (4 piezas):** el Ke cargado a mano en M (`0,1048752249`, 10 decimales) frente al Ke vivo de D (`0,104875224898`): diferencia ≈ 2·10⁻¹². El vínculo escribe el valor exacto.
**Entradas declaradas (no vínculos; criterio de la IA o fuentes externas) — 18 filas de M:** EPS básico/diluido (M los calcula con su base), ajuste de método de participación, Inventories (y su variación), efecto cambiario, y las filas de fuente/fecha/verificación documental. En D: `B16/B17` (¿I+D? ¿arrendamientos?), `B19` activos no operativos, `B20` minoritarios, `B21` acciones en circulación (portada más reciente), `B23` tasa efectiva, y todos los drivers de las tres historias.

**Controles de consistencia D ↔ M (solo lectura):** 18/18 `CONSISTENTE` en UBER (crecimiento año 1, CAGR 2–5, ventas/capital 1–5 y 6–10, g terminal, ROIC terminal efectivo — si el selector «override» está en No, el efectivo es el costo de capital terminal). El margen objetivo no se controla por tener M una base contable distinta (ajuste de I+D); queda como pendiente.
**Orden y dependencias:** `order()` + `despues=` (dependencias que pasan por fórmulas: entrada de D → resultado de D → M/Resumen). Orden efectivo: H→D, H→M, D→M, D→Resumen, M→Resumen.
**Huellas:** `registrar_huellas()` escribe en el Resumen de D‑B la huella de grupo (SHA‑256 de las huellas de origen) y la fecha de carga, sustituyendo el hash del JSON de valores de la plantilla.
