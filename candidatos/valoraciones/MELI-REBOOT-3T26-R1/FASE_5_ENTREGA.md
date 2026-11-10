# MELI-REBOOT-3T26-R1 · Fase R5 (análisis y publicación EN_REVISION)

- **Fecha:** 2026-11-10 · **Agente:** Claude (Code, nube). Estado: **EN_REVISION** · auditoría económica independiente (R6) **NO EJECUTADA** · QA visual de la app pendiente.

## Entregables
- **Sexto archivo:** Google Doc `1LslHW-GKMNM1W_LOa3FUKMvnVDlz7MsSX9qwfGNK33o` (Nivel 1: 14 capítulos, 4.418 palabras; Nivel 2: 12 apartados, 3.897 palabras), en la carpeta de la revisión.
- **JSON:** `valoraciones/MELI-REBOOT-3T26-R1.json` y `analisis/MELI-research-MELI-REBOOT-3T26-R1.json` (perfil `Floyd`; contrato `jmr-reboot-3libros-v1`), generados con `R5_evidencia/build_json.py` desde los motores recalculados (`R3_evidencia/motor/*.xlsx`), `sens_res.json` y las lecturas del libro de Múltiplos.
- **Catálogo:** MELI-REBOOT-3T26-R1 entra como revisión activa de MELI (no había una activa; las fichas A-1.2 y la reconstrucción Floyd F1–F5 siguen archivadas). Registro regenerado.

## Cifras publicadas
DCF 908,33 / **2.536,95** / 4.120,94 · esperado 2.525,79 · MOS 35 % sobre la Base 1.649,02 · precio 1.510,00 (6-nov-2026) · múltiplos 1.116,16 / 1.782,61 / 2.486,03 · combinado 75/25: 960,29 / 2.348,37 / 3.712,21. Dos matrices DCF 5×5 (centro 2.536,95) y cinco matrices 5×5 de múltiplos (centro = VP3 Base) con SHA-256 `8b937700…359b`.

## Controles ejecutados
| Control | Resultado |
|---|---|
| `scripts/validar_reboot.cjs` (registro + análisis de AAPL, CMG, UBER y MELI) | PASS |
| `scripts/validar_profundidad_floyd.cjs`, `auditar_integridad.cjs`, `registro_revisiones.py --check` | OK |
| `node --test scripts/tests/validar_catalogo.test.cjs` | pasa (lista de vigentes actualizada con MELI) |
| CI de GitHub | NO ejecutado desde aquí |
| QA visual de la app | NO ejecutado |
| R6 | NO ejecutada |

## Salvedades materiales (también en el JSON)
1. **Fondeo del crédito como pasivo operativo** (deuda del puente 2.369 en vez de 13.190): decisión mía que cambia lo acordado en R1 porque el EBIT ya descuenta el costo de fondeo; excepción al FCFF industrial.
2. **El precio queda por debajo de todas las celdas de las matrices** (se necesitarían 9,6 % de crecimiento o 8,4 % de margen): los supuestos de margen y de ventas/capital de la Base no se prueban con el historial y son la primera línea de ataque para R6.
3. Beta bottom-up 0,93 con mapeo de industrias propio (con beta 1,30, Base 2.289,61).
4. EV/FCFF sin ancla histórica; P/FCFE y P/OCF con flujo distorsionado por fondos de clientes (pesos mínimos).
5. Caja de 8.126 según la definición de MELI; arrendamientos no restados; verificación documental, calidad de la cartera y gobierno pendientes.

## Siguiente paso
R6 por otro agente. Antes de publicar, el usuario debería decidir si acepta el tratamiento del fondeo (salvedad 1).
