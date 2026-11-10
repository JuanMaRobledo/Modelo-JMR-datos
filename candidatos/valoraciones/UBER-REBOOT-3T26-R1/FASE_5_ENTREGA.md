# UBER-REBOOT-3T26-R1 · Fase R5 (análisis y publicación EN_REVISION)

- **Fecha:** 2026-11-10 · **Agente:** Claude (Code, nube). Reemplaza el R5 parcial de ChatGPT (documento `1O7sHw19zYtntbAaDWErrmkhUX8pN4RdPtBFqLfN6MMA`, que citaba múltiplos distintos): por decisión del usuario se rehízo.
- **Estado:** **EN_REVISION** · auditoría económica independiente (R6) **NO EJECUTADA** · QA visual de la app pendiente.

## Entregables
- **Sexto archivo:** Google Doc `1rTADOh6ToqyWA598V2cCwjnpGxn84-eNZlErMQAKEB8` (Nivel 1: 14 capítulos, 4.469 palabras; Nivel 2: 12 apartados, 3.914 palabras), en la carpeta UBER de Drive.
- **JSON:** `valoraciones/UBER-REBOOT-3T26-R1.json` y `analisis/UBER-research-UBER-REBOOT-3T26-R1.json` (perfil `Floyd`, el nombre oficial vigente del modelo R1–R6; contrato `jmr-reboot-3libros-v1`). Generados con `R5_evidencia/build_json.py` a partir de los motores recalculados (`R3_evidencia/motor/*.xlsx`), `sens_res.json` y las lecturas del libro de Múltiplos (`R5_evidencia/datos.py`).
- **Catálogo:** UBER-REBOOT-3T26-R1 sustituye a UBER-FLOYD-3T26, cuyos JSON pasan a `archivo-v1/`. Registro regenerado.

## Cifras publicadas
DCF 45,29 / **98,74** / 149,67 · esperado 98,11 · MOS 35 % sobre la Base 64,18 · precio 68,59 (6-nov-2026) · múltiplos 40,24 / 70,31 / 104,90 · combinado 75/25: 44,03 / 91,63 / 138,48. Dos matrices DCF 5×5 (centro 98,7383) y cinco matrices 5×5 de múltiplos (centro = VP3 Base) con SHA-256 `5ed8d799…a88f`.

## Controles ejecutados
| Control | Resultado |
|---|---|
| `scripts/validar_reboot.cjs` (registro + análisis de AAPL, CMG y UBER) | PASS |
| `node --test scripts/tests/validar_catalogo.test.cjs` | 7/7 (contadores de archivo 47/72 y regex de MOS actualizados) |
| `scripts/auditar_integridad.cjs`, `validar_profundidad_floyd.cjs`, `registro_revisiones.py --check` | OK |
| Pruebas que ya fallaban antes de este cambio (`capturas_matrices_fuente`, `relativos_revision`, `test_estandarizacion_20261031`, `validar_no_regresion_20` por rutas de INTU) | Mismo conjunto de fallos que en la rama sin los cambios de UBER; no se tocaron |
| CI de GitHub | NO ejecutado desde aquí |
| QA visual de la app | NO ejecutado |
| R6 | NO ejecutada |

## Salvedades (también en el JSON)
Beta 1,20 por decisión del usuario (la bottom-up 0,82 daría Base 108,62); valor terminal 71 % del valor; arrendamientos fuera de la deuda por decisión del usuario; activos no operativos a valor en libros; «otros ajustes» del flujo de caja (6.540 M) sin desglosar; costo de la deuda y volatilidad de opciones supuestos; verificación documental pendiente; EV/FCFF con el valor de FY2025; P/E poco fiable; fórmulas del motor no re-verificadas por mí (ChatGPT dejó un cotejo estructural en `FASE_3_ENTREGA.md` que no repetí).

## Siguiente paso
R6 por un agente independiente; CELH sigue pendiente de reconfigurar; revisar y fusionar PR #193/#215/#263 solo tras CI.
