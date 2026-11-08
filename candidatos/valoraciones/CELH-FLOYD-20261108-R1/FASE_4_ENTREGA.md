# F4 · CELH · Modelo JMR Floyd · CELH-FLOYD-20261108-R1 — entrega: EXPEDIENTE EN_REVISION (pendiente de integración en `main` y de F5)

**Fecha:** 2026-11-08 · **Herramienta/modelo:** Claude Code, `claude-sonnet-5-5` (esfuerzo no reportado) · **AISLAMIENTO=OK** · **PASOS: 5/6** (artículo, Nivel 2, JSON valoración/análisis, catálogo y registro, validadores ejecutados; QA visual en navegador NO EJECUTADO).

## Entregables
- `valoraciones/CELH-FLOYD-20261108-R1.json` (perfil Floyd, `contratoLibros=floyd-h1-h2-separados-v1`; libros: Históricos `1MLwY0b7…`, Valoración `1i7KsD5L…`, documento de análisis `16sOYz9JwdIr9-QJoWWOtPTHo0roOt8Nlts9XUIbVggM`) y `analisis/CELH-research-CELH-FLOYD-20261108-R1.json` con Nivel 1 de 14 capítulos (4.282 palabras) y Nivel 2 de 12 apartados más el DCF por FCFE; copias en esta carpeta con `NIVEL_1_14_CAPITULOS.md` y `NIVEL_2_12_APARTADOS.md`.
- Catálogo (`catalogo.json`): CELH pasa de «fuera del catálogo» a activa EN_REVISION (antecedente CELH-20261028-A1, A-1.2, que permanece archivada en `archivoFloyd`, sin borrar). Registro (`registro/`) regenerado con `scripts/registro_revisiones.py`.
- Listas cerradas de validadores ampliadas con CELH (`validar_no_regresion_20.cjs`, dos pruebas); no se relajó ninguna aserción.

## Datos de la publicación
DCF Base **32,55**, valor esperado 33,87, MOS 35 % **21,16**, precio 32,16 (cierre del 6-nov-2026), tres historias 50/25/25, múltiplos como contraste con peso 0.

## Controles ejecutados (resultado real)
| Control | Resultado |
|---|---|
| `node scripts/validar_profundidad_floyd.cjs` | PASS estructural (3 empresas); aviso PENDIENTE_EDITORIAL: Nivel 1 de 4.345 palabras < 7.500 (UBER 1.888, CMG 7.608) |
| `node scripts/validar_catalogo.cjs` | PASS (valoraciones 3, análisis 3); avisos heredados: `PENDIENTE_COBERTURA: CELH no acredita las 25 entradas editoriales vigentes` (igual que UBER y CMG) |
| `python3 scripts/registro_revisiones.py --check` | OK: 30 emisores, 51 sustituidas (registro regenerado con el script) |
| `scripts/validar_no_regresion_20.cjs` | **FALLA igual que en `main`** (aserción de conteo A-1.2: 0 ≠ 16 en `main`, 0 ≠ 15 con esta rama); falla previa a esta revisión |
| pruebas `test_estandarizacion_20261031.py`, `capturas_matrices_fuente.test.cjs` | fallos previos en `main` (0 ≠ 27 análisis A-1.2); sin empeoramiento |
| Visor/app autenticada, CI en GitHub | NO EJECUTADO |

## Reservas
Nivel 1 por debajo del objetivo editorial; auditoría económica independiente F5 PENDIENTE; QA visual PENDIENTE; la publicación en la app exige que este expediente llegue a `main` de `Modelo-JMR-datos`.
