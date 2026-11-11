# Etapa 4 · Sincronización y recálculo — ENTREGA

**Estado: PARCIAL (muy avanzado; ver sección 5).** Prueba obligatoria ejecutada en copias aisladas de UBER (APROBADA). Componente de sincronización probado en memoria (8/8) **y, desde que se dispuso de la cuenta de servicio, ejecutado contra la API real de Google Sheets** para el tramo D‑C → `Resumen` (4 vínculos, ciclo completo). Los demás tramos (H→D, H→M, D‑B→M, D‑O→Resumen, M→Resumen) siguen NO_EJECUTADOS. 2026‑11‑11.

## 1 · Prueba obligatoria (ejecutada, con los valores medidos)
Copias: D‑B prototipo `15P2WOocyh5d12s1dQz4-zO1Rxl80a327Ib4drkkT480`; D‑C `1evMw-L6WA86Usu1u0P3CSa1RTrzlDEJJQz6Cj3KHXlQ`. Los libros de producción **no se tocaron**.
Entrada modificada (permitida): `Input sheet!B28` (CAGR ingresos años 2–5): Base 14 % → 15 %; Conservadora 9,75 % → 11 %.

| Salida | Inicial | Tras el cambio | Esperado | Restaurado |
|---|---|---|---|---|
| DCF Base (`Valuation output!B33` y Presentación) | 98,74 | **102,91** | dependiente ✔ | 98,74 |
| Precio con MOS 35 % | 64,18 | **66,89** | dependiente ✔ | 64,18 |
| Upside vs precio | +44,0 % | **+50,0 %** | dependiente ✔ | +44,0 % |
| Valor esperado ponderado | 98,11 | **100,20** | dependiente ✔ | 98,11 |
| Diferencia múltiplos vs DCF Base (Resumen) | −28,8 % | −31,7 % | dependiente ✔ | (idem inicial) |
| DCF Conservadora en su libro | 45,29 | **46,96** | dependiente ✔ | 45,29 |
| **DCF Conservadora en el Resumen/Presentación** | 45,29 | **45,29 (sin cambio)** | **debía marcarse obsoleta** ✘ | 45,29 |
| Múltiplos (5 métodos, combinado, esperado) | 70,31 / 71,44 | sin cambio | no dependiente ✔ | sin cambio |
| Matriz WACC×g (celda Base) | 98,74 | **98,74 (sin cambio)** | debía marcarse obsoleta | 98,74 |
| «Conciliación del resumen» | CONCILIADO | **CONCILIADO** | debía pasar a PENDIENTE ✘ | CONCILIADO |
| «Control sensibilidades» (plantilla actual) | OK | **OK** ✘ | REVISAR | OK |

**Conclusión:** dentro de un libro la propagación por fórmulas funciona. **Entre libros no hay propagación ni detección**: tras editar D‑C el Resumen siguió mostrando 45,29 y `CONCILIADO`. Esto confirma E1‑1 y E1‑2.

### Defecto corregido en el prototipo
Las celdas `Sensibilidades DCF!B28:B29`, `B30` y `B42` eran constantes (0,0017; 98,7383). Se reemplazaron por `=D8‑B30`, `=D16‑B30`, `='Valuation output'!B33`, `=D39‑B30` (hojas nuevas; el motor no se toca). Repetida la prueba: con la Base en 102,91 el control mostró **−4,17** y `Presentación` pasó a **REVISAR / «Matriz OBSOLETA: rehacer corridas del motor»**; al restaurar volvió a 0,0017 y `OK`.
Nota: ese control solo cubre la matriz dentro del mismo libro. **No se puede detectar por fórmula** el rancio de D‑C, D‑O ni M (prohibido IMPORTRANGE): requiere el componente de sincronización.

## 2 · Componente de sincronización (código en `JMR-valuation`)
`scripts/floyd_sync/core.py` + `sheets_backend.py` + `tests/test_floyd_sync.py` (commit en esta rama).
- Vínculo = (libro, rango) origen → (libro, rango) destino + revisión; transformación solo `identity` (cero cálculo financiero).
- **Huella SHA‑256 del contenido canónico del rango origen leído ahora**, no de la fecha ni de lo escrito.
- Estados: `FRESCO` / `OBSOLETO` (`check`, sin escribir) / `ERROR` / `PENDIENTE`; manifiesto JSON con origen, destino, revisión, fecha, SHA origen/destino, intentos y error.
- **Idempotente** (si nada cambió, `SIN_CAMBIO`), **reanudable** (manifiesto guardado tras cada vínculo), reintentos con espera 2/4/8 s, verificación posterior por lectura, `dry_run`, **orden topológico con detección de ciclos**.
- Pruebas ejecutadas (7/7): escritura + idempotencia; detección de edición del origen y de pegado manual en el destino; dry‑run sin escrituras; reanudación tras fallo; orden y ciclos; cadena H→D→M en una corrida; verificación posterior fallida = ERROR.
- **Pendiente:** vínculos H→D (hlib/mapping por revisión), H→M, D‑B→M, D‑O→Resumen y M→Resumen sobre datos reales; integración en CI; registrar `Resumen!C10/E10/B33` con la huella nueva (hoy hash de JSON de valores transferidos).

## 3 · Estado frente a los criterios de la etapa
| Criterio | Estado |
|---|---|
| Medir inicial, cambiar entrada, recalcular, comprobar dependientes y no dependientes, restaurar y verificar | **APROBADO** (copias) |
| Sincronización H→DCF, H→M, D‑B→M, D‑C/D‑O/M→Resumen realmente ejecutable | **PARCIAL**: D‑C→Resumen ejecutado en API real (sección 4); resto NO_EJECUTADO |
| Registro origen/destino/revisión/fecha/SHA/estado/errores/orden sin ciclos | **Implementado y probado** (en memoria) |
| «No afirmar automatización funcional sin ejecutar y documentar» | **Se cumple: no se afirma** |

## 4 · Prueba real entre libros (API de Google Sheets, cuenta de servicio)
Script `JMR-valuation/scripts/floyd_sync/prueba_real_copias.py`; la credencial se lee de `GOOGLE_SERVICE_ACCOUNT_JSON_CONTENT` (no se guarda en Git) y una **lista cerrada** impide escribir fuera de las dos copias (`assert` en el backend). Evidencia: `etapa4/manifiesto_UBER_prueba.json`, `etapa4/log_paso1|2|3.json`.
Vínculos: D‑C (copia) `Valuation output!B33`, `Input sheet!B35`, `Valuation output!B17`, `Cost of capital worksheet!B62` → `Resumen de valoraciones!C5:C8` del prototipo D‑B.

| Paso | D‑C valor | Resumen C5 | Presentación Conservadora / esperado | Estado de vínculos |
|---|---|---|---|---|
| 0 inicial | 45,2912 | 45,2912 | 45,2912 / 98,1091 | 4 PENDIENTE |
| `dry_run` | — | sin escrituras | — | 4 DRY_RUN |
| 1 sync | 45,2912 | 45,2912 | 45,2912 / 98,1091 | 4 ESCRITO → 4 FRESCO |
| 2 repetir | — | — | — | 4 SIN_CAMBIO (idempotente) |
| 3 editar `Input sheet!B28` D‑C (9,75 % → 11 %) | **46,9633** | 45,2912 (rancio) | 45,2912 / 98,1091 | **`dc_valor` OBSOLETO**; los otros 3 FRESCO |
| 4 sync | 46,9633 | **46,9633** | **46,9633 / 98,5272** | solo `dc_valor` ESCRITO; 4 FRESCO |
| 5 restaurar B28 | 45,2912 | 46,9633 (rancio) | 46,9633 / 98,5272 | `dc_valor` OBSOLETO |
| 6 sync | 45,2912 | **45,2912** | **45,2912 / 98,1091** | 4 FRESCO (estado original) |

Hallazgo de la prueba real: la API limita a 60 lecturas/min por usuario; la primera corrida falló con **429**. El backend ahora reintenta con espera (429/5xx) y tiene prueba (8/8). El vínculo `dc_valor` necesitó 3 intentos por esa cuota; el manifiesto los registra.
Con esto queda demostrado que **la huella del contenido detecta el rancio que la plantilla actual no detectaba** (E1‑2) y que la propagación al Resumen/Presentación es idempotente y reversible.

## 5 · Todos los tramos definidos y ejecutados sobre copias (API real)
Definición completa en `etapa4/VINCULOS_FLOYD.md`; evidencia en `etapa4/definicion_vinculos_UBER.json`, `manifiesto_UBER_completo.json`, `log_completo_*.json`. Copias aisladas (lista cerrada de escritura): H `1DezcVZb…`, D‑B prototipo `15P2WOoc…`, D‑C `1evMw-L6…`, D‑O `115DrjMg…`, M `1pmNfv8X…`.
**Resultado: 13 vínculos (H→D ×3, H→M ×4, D→M ×3, D→Resumen ×2, M→Resumen ×1); 141 piezas, 137 idénticas a lo cargado por la IA y 4 con diferencia ≈ 2·10⁻¹² (redondeo del Ke); 18/18 controles de consistencia D↔M.**

| Paso | DCF Base / Cons. / Opt. | M múltiplos Base | Ingresos LTM en D y M | Estado |
|---|---|---|---|---|
| Inicial | 98,7383 / 45,2912 / 149,6689 | 70,3069 | 56 526 | 13 PENDIENTE |
| Sync (dry‑run antes) | sin cambio | sin cambio | sin cambio | 13 ESCRITO → 13 FRESCO |
| Repetir | — | — | — | 13 SIN_CAMBIO |
| **Editar `H!Income Statement!L3` 56 526 → 57 526** | sin cambio (rancios) | — | — | **OBSOLETO: `h_a_db`, `h_a_dc`, `h_a_do`, `h_a_m_income`**; balance, caja y precio siguen FRESCO |
| Sync | **100,4482 / 46,0556 / 152,2798** | **71,1742** | **57 526** en D‑B, D‑C, D‑O y M | 13 FRESCO; Presentación igual a D y M |
| Restaurar L3 y sync | 98,7383 / 45,2912 / 149,6689 | 70,3069 | 56 526 | idéntico al inicial |

La cascada confirma que el sistema detecta qué depende y qué no (sin falsos obsoletos) y que propaga por H → D → M → Resumen → Presentación en una sola corrida, y que es reversible. Pruebas automáticas: 13/13 (`tests/test_floyd_sync.py`).
**Estado frente al criterio de la etapa:** sincronización H→DCF, H→M, D‑B→M, D‑C/D‑O/M→Resumen **EJECUTADA en copias: APROBADO**. **Pendiente:** aplicar a los libros reales (solo tras tu aprobación, con respaldo), integrar `pytest` y `--dry-run` en CI, probar con una 2.ª empresa (CMG) para validar la generalidad de las reglas por etiqueta, y control del margen objetivo.

## Siguiente paso
Etapa 5: flujo corto compartido ChatGPT/Claude (un punto de entrada). Luego Etapa 6 (CI/pruebas) con el nuevo test. Para cerrar Etapa 4 hace falta que el usuario provea una cuenta de servicio (o autorice ejecutar el backend) para la prueba real entre libros.
