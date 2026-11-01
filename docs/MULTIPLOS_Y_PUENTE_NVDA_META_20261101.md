# NVDA y META · múltiplos A-1.2 y puente NVDA R4 → A-1.2 · 1-nov-2026

**Estado: hojas de trabajo completas en DCF y múltiplos; NO publicado ni auditado.** Continúa `CIERRE_GATES_META_NVDA_20261101.md`. Pendientes al final.

## 1. Cambios en las hojas de trabajo (todos por valores o por las fórmulas ya usadas en la plantilla)
- `Input sheet!D1` = precio de corte (META 614,99; NVDA 204,64): estaba vacío y dejaba en cero la columna LTM de `Trailing Valuation`.
- `Trailing Valuation`: etiquetas de cierre (B2:L2), precio de cierre fiscal en fila 3 (Yahoo, sin ajuste por dividendos, con splits) y filas 4–24 con las fórmulas de `refresh_native_model.py::_TRAILING_VALUATION_ROWS`. Antes la hoja tenía solo encabezados.
- NVDA: `Income Statement!B22:L22` (utilidad atribuible) = utilidad consolidada (sin participaciones minoritarias) y `Balance Sheet!B35:L35` = patrimonio común: ambas estaban vacías y bloqueaban P/E y P/B.
- `Resumen de Valoración!G3:G4` = «Crecimiento» y MOS 35 % (juicio del analista, pesos de la tabla de la plantilla: DCF 60 %, EV/EBITDA 10 %, EV/FCFF 15 %, P/E, P/FCFE y P/OCF 5 % cada uno).
- Múltiplos de salida (J8/J19/J30) escritos con `apply_multiples_v3.py` (regla por ciclo). Insumos versionados en `JMR-valuation/reference/multiplos_v3/{NVDA,META}_{anclas,ciclo,decision}.json`.

## 2. Múltiplos de salida (veces)
| | EV/EBITDA | EV/FCFF | P/E | P/FCFE | P/OCF |
|---|---|---|---|---|---|
| NVDA Cons/Base/Opt | 13,7 / 21,0 / 29,1 | 20,2 / 29,9 / 37,5 | 17,8 / 22,5 / 35,2 | 18,6 / 27,5 / 35,3 | 17,6 / 24,2 / 29,4 |
| NVDA LTM | 24,4 | 38,6 | 25,9 | 39,1 | 37,0 |
| META Cons/Base/Opt | 7,4 / 8,5 / 13,6 | 20,4 / 21,1 / 21,7 | 17,7 / 21,4 / 22,0 | 17,9 / 18,5 / 19,0 | 8,7 / 9,6 / 11,4 |
| META LTM | 15,4 | 56,0 | 21,0 | 54,9 | 11,8 |

Valor por múltiplos consolidado a hoy (VP, `Descuento de múltiplos`, chequeo VP3 < FY+3 = OK en los 3 escenarios): NVDA 129,0 / 233,5 / 362,8 frente a DCF Base 201,8; META 388,6 / 412,6 / 574,4 frente a DCF Base 783,4.
Las diez matrices 5×5 Base (cinco métodos × dos empresas) calculan en la hoja y su centro coincide con el VP3 de cada método (control `OK`).

## 3. Puente NVDA R4 (381,79) → A-1.2 (201,80), sustituyendo supuestos de R4 sobre la hoja A-1.2, de uno en uno
| Paso | Base | Δ |
|---|---:|---:|
| A-1.2 inicial | 201,80 | |
| g terminal 3,5 % → 4,0 % | 211,11 | +9,31 |
| Rf 4,94 % → 5,29 % | 207,14 | −3,97 |
| WACC terminal 9,30 % → 8,99 % | 216,47 | +9,33 |
| margen objetivo 53,0 % → 58,7 % | 238,58 | +22,11 |
| Ventas/capital 2,2→2,0 y 0,7→0,598 | 236,32 | −2,26 |
| **Senda de crecimiento R4 (70 % año 1 … 4 %; CAGR 36,3 % vs 23,6 %)** | **393,96** | **+157,64** |
| Activos no operativos 47.898 → 39.257 | 393,61 | −0,35 |
| Residuo hasta R4 381,79 (WACC inicial R4 11,44 % vs 10,66 %, y diferencias de motor) | | −11,82 |

**Lectura (corregida el 1-nov-2026):** ~85 % de la brecha es la senda de ventas. R4 suponía +70 % en el año 1 (≈515.000 M, promedio de 128.760 M por trimestre); A-1.2 usa +40 % (424.158 M). **Corrección:** una versión anterior de este documento afirmaba que los 515.000 M «no están respaldados por la evidencia» comparándolos con el año fiscal que cierra en enero; era un error, porque el «año 1» de la hoja son los doce meses posteriores al LTM (ago-2026 a jul-2027). Frente a la evidencia: el trimestre de julio anualizado es 384.884 M, la guía del emisor para el trimestre siguiente (108.000 M ±2 %) anualizada es 432.000 M, y el año 1 Base queda **1,8 % por debajo de esa guía**, es decir, supone crecimiento secuencial casi nulo después del trimestre ya guiado. Los 515.000 M de R4 exigen ~12 % de crecimiento secuencial por trimestre durante cuatro trimestres (los datos recientes son +17,9 % entre T1 y T2 y +12 % guiado para T3). Ninguna de las dos sendas está contradicha por los datos; la A-1.2 Base es la más prudente y esa prudencia es la mayor fuente de incertidumbre al alza del valor. El resto (margen, tasas, ROIC) se compensa en parte. El puente es secuencial: el orden afecta el reparto entre pasos, no la suma. Los supuestos de R4 vienen de `valoraciones/NVDA-20261025-R4.json`; su motor era distinto, por eso hay residuo.

## 4. Salvedades (publicar EN_REVISION solo con ellas explícitas)
1. **Fechas mezcladas:** pares a 30-sep-2026 (`corte_vigente.json`), precios propios a 30-oct-2026; Rf de la hoja 4,94 % frente a ERP de Damodaran de oct-2026 (3,70 %, calculada con Rf 5,29 %). (Resuelto en `FECHAS_TASAS_META_NVDA_20261101.md`.)
2. **META:** valor por múltiplos (412,6) ≈ la mitad del DCF (783,4). EV/EBITDA y P/OCF quedan por debajo de su historia por el tope del múltiplo justificado (capex de IA en el FCFF de FY+3). Es una diferencia de método, no un error de cálculo; la ponderación DCF 60 % la amortigua pero no la elimina.
3. NVDA P/E Optimista supera 25 % el múltiplo actual; TSM y AMD excluidos de la mediana de pares; SNAP excluido en META (justificación en cada `_decision.json`).
4. Pasivo legal de META sin deducir (ver documento anterior).
5. Categoría «Crecimiento» y MOS 35 %: juicio del analista, revisable.
6. En la sesión se probó un modo «WACC directo» que dejó K5 en PENDIENTE; se revirtió. Hoja verificada tras cada prueba: Base 201,80 y K5:K8 = LISTO.

## 5. Pendiente para publicar
Exportar a JSON (valoración con cuatro escenarios, matrices y descuento), Nivel 1 (14 capítulos) y Nivel 2 (12 apartados) con los nuevos números, conciliar hoja↔JSON↔análisis↔app, CI, y sustitución en el catálogo conservando R5/R4 como histórico. No iniciado.
