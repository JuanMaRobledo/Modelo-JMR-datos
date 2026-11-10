# CMG-REBOOT-3T26-R1 · Fase R5 (análisis y publicación)

- **Fecha:** 2026-11-10 · **Agente:** Claude (Code, nube). Estado: **EN_REVISION** (sin auditoría independiente R6).
- **Documento de análisis:** Google Doc `1jlt6v-PWeZOckqaLJWs6nClg2GyayuhQFOt-A4rCwlY` (N1 de 14 capítulos, ~3.500 palabras; N2 de 12 apartados). Generado desde HTML por `R5_evidencia/`.
- **JSON:** `valoraciones/CMG-REBOOT-3T26-R1.json` y `analisis/CMG-research-CMG-REBOOT-3T26-R1.json` (`contratoLibros=jmr-reboot-3libros-v1`).
- **Catálogo:** CMG Reboot reemplaza a `CMG-FLOYD-20261108-R1`, cuyos dos JSON se movieron sin cambios a `archivo-v1/` (reversible por git). Activas: UBER (Floyd), CMG y AAPL (Reboot).
- **Fuentes nuevas en R5:** texto del 10-Q 3T-2026 (restaurantes, ventas comparables, costos por línea, canal digital, compensación en acciones).

## Validadores
| Control | Estado |
|---|---|
| `validar_reboot.cjs` (CMG y AAPL) | APROBADO |
| `validar_catalogo.cjs`, `auditar_integridad.cjs`, `auditar_profundidad.cjs`, `validar_profundidad_floyd.cjs` (UBER) | APROBADO |
| `scripts/tests/validar_catalogo.test.cjs` | 7/7 (contadores del archivo actualizados a 46 y 71) |
| Resto de `scripts/tests` | 19 fallos previos ajenos (dependen de archivos movidos a `archivo-v1/` en el reinicio) |

## Declarado, no ejecutado
- R6 (auditoría independiente), QA visual de la app con el registro de CMG y CI del repositorio.
- Verificación documental de la serie histórica; desglose de «otros ajustes» del flujo LTM (804 M).
- Integridad de fórmulas y comentarios del motor en las copias de CMG.
- El documento se subió convertido desde HTML y **no se releyó completo** tras la conversión (en AAPL sí).
- N1 de ~3.500 palabras: menos que el análisis Floyd anterior de CMG (6.800); no se declara investigación extensa definitiva.

## Siguiente paso exacto
R6 de CMG (otra sesión o agente): revisar márgenes y ventas/capital de las tres historias, la beta de industria, el tratamiento de arrendamientos y los múltiplos de salida. En paralelo, R3 de UBER.
