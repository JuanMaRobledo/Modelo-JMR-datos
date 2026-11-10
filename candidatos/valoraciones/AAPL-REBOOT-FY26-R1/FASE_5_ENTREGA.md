# AAPL-REBOOT-FY26-R1 · Fase R5 (análisis y publicación)

- **Fecha:** 2026-11-09 · **Agente:** Claude (Code, nube). Estado: **EN_REVISION** (sin auditoría independiente R6).
- **Documento de análisis:** Google Doc `1CxPNSRM5GcV0UvMgxiaByM5xOQ55b1peHqMOT_c8n60` (N1 de 14 capítulos, ~3.600 palabras; N2 de 12 apartados con proyección anual de las tres historias, puente a la acción, cinco múltiplos, matrices y DCF inverso). Se creó nuevo desde HTML porque el borrador `1GR89k…` era una copia de la plantilla Floyd; ese borrador **no se borró** y queda sin uso.
- **JSON:** `valoraciones/AAPL-REBOOT-FY26-R1.json` y `analisis/AAPL-research-AAPL-REBOOT-FY26-R1.json` (`contratoLibros=jmr-reboot-3libros-v1`, seis URLs en `libros`). Generados por `R5_evidencia/build_json.py` desde las evidencias R2/R3 y las lecturas de M.
- **Catálogo:** AAPL agregado a `valoraciones`, `analisis`, `seleccionesDefinitivas` y `controlModeloA` (método `Reboot`).

## Validadores
| Control | Estado |
|---|---|
| `scripts/validar_reboot.cjs` (nuevo): libros distintos, tres historias, esperado, MOS sobre Base, matrices 5×5 DCF y de múltiplos con centro conciliado, SHA-256, pesos, 14+12 secciones, cifras clave citadas en el texto | APROBADO |
| `validar_catalogo.cjs`, `auditar_integridad.cjs`, `auditar_profundidad.cjs` (ramas Reboot) | APROBADO |
| `validar_profundidad_floyd.cjs` (UBER, CMG) | APROBADO, sin cambios |
| Pruebas de `scripts/tests` | Mismos 22 fallos que antes del cambio (dependen de archivos movidos a `archivo-v1/`); 1 prueba nueva aprobada |
| `validar_no_regresion_20.cjs` | Falla igual que antes (falta un candidato INTU archivado) |
| App (Modelo-JMR): `npm test` | 191/194; fallan 3 pruebas previas ajenas |

## Declarado, no ejecutado
- **R6** auditoría independiente; **QA visual** de la app con el registro AAPL; **CI** del repositorio (por ejecutar en PR).
- Verificación documental FY2017–FY2023.
- Las matrices 5×5 de múltiplos del JSON son **derivadas** de las hojas (precio FY+3 descontado con el Ke Base); las hojas conservan el precio FY+3 sin descontar.
- N1 tiene ~3.600 palabras, menos que las Floyd extensas (CMG 6.800); no se declara investigación extensa definitiva.
- Gobierno corporativo y compensación no analizados.

## Siguiente paso exacto
R6: auditor independiente (otra sesión) revisa supuestos, conciliaciones y la lectura de la app; después, reconfigurar UBER y CMG al modelo Reboot y apuntar Cartera a las nuevas valoraciones.
