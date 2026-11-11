# Etapas 5 y 6 · Flujo compartido, CI, pruebas y prueba integral — ENTREGA

**Etapa 5: PARCIAL** (diagnóstico + validador mecánico nuevo; sin cambios al contrato). **Etapa 6: PARCIAL / prueba integral UBER R1–R5 y ChatGPT↔Claude: NO_EJECUTADO.** 2026‑11‑11.

## Etapa 5 · Punto de entrada único y pasos reanudables
Comprobado en los tres repos:
| Hallazgo | Evidencia | Severidad |
|---|---|---|
| `AGENTS.md` dice «mismo texto obligatorio en los tres repos», pero **`Modelo-JMR-datos/AGENTS.md` difiere** (tiene un punto 8 «Criterio propio y decisiones de método» ausente en los otros dos; md5 distinto). `CLAUDE.md` sí es idéntico en los tres. | `diff` | Media: ChatGPT y Claude pueden recibir reglas distintas según el repo que lean |
| Se nombra a Gemini, pero **no existe archivo de entrada para Gemini** (`GEMINI.md`) en ningún repo | listado de raíz | Baja |
| `AGENTS.md`/`CLAUDE.md` ordenan usar la rama `claude/jmr-model-reboot-rnj087` «mientras los PR no se fusionen». La rama sigue existiendo y `main` ya contiene contrato y reglas §0R. Instrucción **obsoleta/ambigua**; hay que fijar un solo ref | `git branch -r` | Media |
| **Las entregas no cumplen el formato de reanudación del contrato:** de 25 `FASE_*_ENTREGA.md` de las 5 revisiones REBOOT, 19 carecen de `PASOS n/n` y 18 de `AISLAMIENTO=…` (UBER 11 campos ausentes; CMG 10; MELI 7; MSFT 7; AAPL 6) | nuevo `scripts/validar_entregas_floyd.py` | Alta para «reanudar sin recrear» |
| Nombres técnicos heredados (`CONTRATO_REBOOT_JMR.md`, `ordenes-reboot.md`, `jmr-reboot-3libros-v1`) | contrato | Informativo: documentado como histórico; no se renombra sin migración |

**Hecho (mecánico, sin tocar el contrato):** `Modelo-JMR-datos/scripts/validar_entregas_floyd.py` — comprueba en cada entrega: revisión, fecha, agente/modelo, IDs, `PASOS n/n`, `AISLAMIENTO`, estado de controles y siguiente paso; informa por defecto y falla con `--estricto`. Ejecutado sobre las 5 revisiones (tabla anterior).
**Propuesta (no aplicada; requiere aprobación porque toca el contrato):** (1) unificar los tres `AGENTS.md` (decidir si el punto 8 es regla vigente) y añadir un test que compare los tres; (2) fijar `main` como único ref y retirar la mención de la rama; (3) añadir `GEMINI.md` que remita a `AGENTS.md`; (4) hacer `--estricto` obligatorio en CI para entregas de nuevas fases (las existentes quedarían con excepción registrada); (5) cada fase escribe además un `FASE_<N>_ESTADO.json` {revisión, paso, SHA de entradas, estado de vínculos del manifiesto de sincronización} para que ChatGPT y Claude reanuden con el mismo dato.

## Etapa 6 · CI y pruebas
| Suite | Resultado medido (local, 2026‑11‑11) |
|---|---|
| `Modelo-JMR`: `node --test tests/**` | **210/210 pasan** (la primera corrida dio 198/201 por falta de `npm ci`; `linkedom` está declarado en `package.json`) |
| `Modelo-JMR` CI en GitHub, `main` (`676dced`) | `suite-completa`, `prompts-triad`, `separacion-editorial-calculadora`, `nav-multiplos`, `expediente`, `vista-hojas`, `pages` en **success** |
| `Modelo-JMR-datos`: `scripts/validar_catalogo.cjs` | 5 valoraciones, 5 análisis; **`PENDIENTE_COBERTURA: MSFT no acredita las 25 entradas editoriales vigentes`** (aviso, no error) |
| `JMR-valuation`: `pytest` | **707 pasan, 29 fallan, 1 omitida** (tras instalar dependencias). Incluye las 7 pruebas nuevas de sincronización |
| `JMR-valuation` CI en GitHub, `main` | `JMR certified DCF preflight tests` #479–#503 y `materialidad`, `puerta de múltiplos` en **success** |

**Los 29 fallos de `JMR-valuation` no los detecta el CI porque los workflows solo ejecutan subconjuntos** (preflight, materialidad, puerta de múltiplos), no `pytest` completo. Causas raíz (no se desactivó ni se modificó ningún control):
1. **25 fallos** `tests/test_analisis_registros.py::test_all_reports_equal_current_record_render`: el manifiesto `reference/analisis_desde_registros.json` usa rutas Windows (`valoraciones\ADSK-17913….json`), apunta a registros que el 9‑nov se movieron a `Modelo-JMR-datos/archivo-v1/valoraciones/`, y los informes de comparación (`data/*_Analisis_Damodaran_*.md`) **no están en el repositorio**. No se arregla con un cambio de ruta: requiere restaurar o regenerar esos informes. Es una prueba de legado A‑1.2/Manual v5 que solo era ejecutable en el equipo del autor.
2. `test_sync_pypl_research_registro` (2) → `StopIteration`: busca el registro PYPL en `valoraciones/` (archivado).
3. `test_valuation_report` (2): espera `P/V` y `P/BV` entre los métodos; el contrato Floyd los excluye (cinco múltiplos sin P/S ni P/BV). Conflicto legado A‑1.2 vs. Floyd.
4. `test_audit_fix_model::test_reset_from_master_apunta_a_la_plantilla_auditada`: espera el ID de plantilla maestra `19PRUFiY…`; el código apunta a `1OYhz6ul…` (plantilla distinta). Hay que decidir cuál es la vigente (¿Atlas/A‑1.2 o Floyd?).
**Reparación propuesta:** mover estas pruebas a un marcador `legado` ejecutado con los datos de `archivo-v1` y añadir `pytest` completo (con ese marcador separado) al CI; **no se ha hecho** porque implica decidir qué legado se mantiene.

## Pruebas exigidas por el prompt que **no existen** o no se ejecutaron
Existen (CI verde): contrato/paridad de agentes (`floyd-agent-parity`, `reboot-libros`, `prompts-triad`), expediente y múltiplos. **No hay prueba automática de:** estructura de plantillas (17 hojas, fórmulas), celdas de entrada permitidas, diez FY, DCF/escenarios/MOS contra el libro, matrices 5×5 contra el libro, JSON↔catálogo↔hoja con lectura autenticada. Se añadió solo la de sincronización (7 pruebas) y el validador de entregas.

## Prueba integral UBER R1–R5 / agentes
- **UBER R1–R5 en copias:** **NO_EJECUTADO.** Reproducir R2 (SEC XBRL), R3 (corridas del motor) y R4 en copias requiere los scripts por revisión (`R2_evidencia`…), credenciales de Sheets y fuentes SEC; lo que sí se hizo es la prueba de propagación de la Etapa 4 y la reconciliación de cifras de `Presentación` frente al JSON (98,74 / 64,18 / 98,11 / 70,31 / 71,44 idénticos).
- **Conciliación con `UBER-REBOOT-3T26-R1`:** cifras de D‑B, Resumen y JSON coinciden; diferencia pendiente de explicar: múltiplos Base −28,8 % frente al DCF Base (declarada en `FASE_4`).
- **ChatGPT y Claude:** **NO_EJECUTADO** (solo hay sesión de Claude; no se inventa resultado de ChatGPT).
- **Ficha de la app (siete pestañas, móvil):** **NO_EJECUTADO** (acceso con contraseña).
