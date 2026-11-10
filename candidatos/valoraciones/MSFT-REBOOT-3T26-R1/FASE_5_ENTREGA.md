# MSFT-REBOOT-3T26-R1 · Fase R5 (análisis y publicación EN_REVISION)

- **Fecha:** 2026-11-10 · **Agente:** Claude (Code, nube). Estado: **EN_REVISION** · auditoría económica independiente (R6) **NO EJECUTADA** · QA visual de la app pendiente.

## Entregables
- **Sexto archivo:** Google Doc `1UH8C1KdvAlGCoCOLYGy20HP2GIjrQx_vZ63fHgOVoEY` (Nivel 1: 14 capítulos, 4.077 palabras; Nivel 2: 12 apartados, 3.787 palabras), en la carpeta de la revisión.
- **JSON:** `valoraciones/MSFT-REBOOT-3T26-R1.json` y `analisis/MSFT-research-MSFT-REBOOT-3T26-R1.json` (perfil `Floyd`; contrato `jmr-reboot-3libros-v1`), generados con `R5_evidencia/build_json.py` desde los motores recalculados (`R3_evidencia/motor/*.xlsx`), `sens_res.json` y las lecturas del libro de Múltiplos.
- **Catálogo:** MSFT-REBOOT-3T26-R1 entra como revisión activa de MSFT (la ficha A-1.2 sigue archivada). Registro regenerado; lista de vigentes del test del catálogo actualizada.

## Cifras publicadas
DCF 232,38 / **496,21** / 676,08 · esperado 475,22 · MOS 35 % sobre la Base 322,54 · precio 530,61 (6-nov-2026) · múltiplos 366,43 / 503,13 / 657,02 · combinado 65/35: 279,30 / 498,63 / 669,41. Dos matrices DCF 5×5 (centro 496,21) y cinco matrices 5×5 de múltiplos (centro = VP3 Base) con SHA-256 `20c3a583…f415`.

## Controles ejecutados
| Control | Resultado |
|---|---|
| `scripts/validar_reboot.cjs` (registro + análisis de cinco empresas) | PASS |
| `scripts/validar_profundidad_floyd.cjs`, `auditar_integridad.cjs`, `registro_revisiones.py --check` | OK (PENDIENTE_EDITORIAL de profundidad: aviso, como en las demás) |
| `node --test scripts/tests/validar_catalogo.test.cjs` | pasa |
| CI de GitHub | NO ejecutado desde aquí |
| QA visual de la app | NO ejecutado |
| R6 | NO ejecutada |

## Salvedades materiales (también en el JSON)
1. **Precio sobre el DCF Base (−6,9 %) y sin margen de seguridad**: el precio implica 16,0 % de crecimiento, 49,1 % de margen o 9,37 % de costo de capital. Orden de magnitud de la decisión: la beta.
2. **Beta bottom-up 1,28 frente a ≈ 1,0 observada**: con 1,00 la Base sería 533,88. R6 debe decidir cuál es defendible.
3. **Arrendamientos financieros (70.973) como deuda** (≈ −9,5 por acción); operativos no; capex en efectivo excluye 24.608 de activos por arrendamientos financieros.
4. Inversiones no operativas (37.808, OpenAI) a valor en libros; concentración del RPO no cuantificada.
5. EV/FCFF y P/FCFE con medianas de 5 años; tasa marginal, costo de la deuda y 78 M de acciones restringidas como supuestos; verificación documental y gobierno pendientes.

## Siguiente paso
R6 por otro agente.
