# Etapa 4 · Sincronización y recálculo — ENTREGA

**Estado: PARCIAL.** Prueba obligatoria ejecutada en copias aisladas de UBER (APROBADA para lo que mide). Componente de sincronización **escrito y probado sin red** (7/7 pruebas); su backend real contra Google Sheets **NO_EJECUTADO** (sin credenciales de API en esta sesión). 2026‑11‑11.

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
- **NO_EJECUTADO:** `GoogleSheetsBackend` (necesita cuenta de servicio con edición en los libros); definición de los vínculos H→D (hlib/mapping por revisión), H→M y el Resumen sobre datos reales; integración en CI. Falta además registrar `Resumen!C10/E10/B33` con la huella nueva (hoy hash de JSON de valores transferidos).

## 3 · Estado frente a los criterios de la etapa
| Criterio | Estado |
|---|---|
| Medir inicial, cambiar entrada, recalcular, comprobar dependientes y no dependientes, restaurar y verificar | **APROBADO** (copias) |
| Sincronización H→DCF, H→M, D‑B→M, D‑C/D‑O/M→Resumen realmente ejecutable | **NO_EJECUTADO** (componente probado en memoria; sin credenciales) |
| Registro origen/destino/revisión/fecha/SHA/estado/errores/orden sin ciclos | **Implementado y probado** (en memoria) |
| «No afirmar automatización funcional sin ejecutar y documentar» | **Se cumple: no se afirma** |

## Siguiente paso
Etapa 5: flujo corto compartido ChatGPT/Claude (un punto de entrada). Luego Etapa 6 (CI/pruebas) con el nuevo test. Para cerrar Etapa 4 hace falta que el usuario provea una cuenta de servicio (o autorice ejecutar el backend) para la prueba real entre libros.
