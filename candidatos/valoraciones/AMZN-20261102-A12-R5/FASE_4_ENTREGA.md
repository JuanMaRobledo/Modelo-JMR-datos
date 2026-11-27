# Amazon (AMZN) · Entrega integrada de valoración y análisis A-1.2 · R5

**3-nov-2026 · Ticker:** `AMZN` · **Revisión:** `AMZN-20261102-A12-R5` · **Corte contable:** 2026-09-30 · **Precio de referencia fechado:** USD 240,35 (2026-10-30) · **Estado del expediente:** **CANDIDATO ANALIZADO, CONTROLES PARCIALES APROBADOS, PUBLICACIÓN PENDIENTE DE GATE INTEGRADO**.

## Resultado y prioridad visual

| Concepto (USD/acción) | Valor y estado |
|---|---:|
| **Valor intrínseco DCF Base, principal** | **149,19 — CANDIDATO** |
| **MOS 35% sobre Base** | **96,97 — CANDIDATO** |
| Conservadora | 81,01 |
| Optimista | 241,84 |
| Disrupción — separada | 62,44 |
| Precio al corte | 240,35 |
| Múltiplo EV/EBITDA Base, media VP1–3 | 341,10 — secundario |
| P/OCF Base, media VP1–3 | 190,40 — secundario |
| EV/FCFF / P/E / P/FCFE | N/D, no fuerza peso ni número |

**Presentación candidata en hoja:** [AMZN R5 / Resumen de Valoración](https://docs.google.com/spreadsheets/d/199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I/edit#gid=0) (abrir pestaña «Resumen de Valoración» por nombre; el enlace de gid no garantiza foco). En `Resumen de Valoración!F1:H2` se observa panel de **DCF Base 149,19 / MOS96,97** y estado **CON RESERVAS / NO PUBLICADO**; las sensibilidades están en `Sensibilidad DCF` y `Sensibilidad por múltiplo`. La hoja no se llama producción, la ficha de app no se presume desplegada.

## Entregables de investigación canónicos

- **F1:** [FASE_1_ENTREGA](FASE_1_ENTREGA.md); insumos y fuentes primarias mantenidos.
- **F2:** [FASE_2_ENTREGA](FASE_2_ENTREGA.md), 10 FY+LTM e identidades 88/88.
- **F3:** [FASE_3_REVISION_ECONOMICA_20261103](FASE_3_REVISION_ECONOMICA_20261103.md); contrastes de crecimiento, CAPEX, S/C, ROIC, WACC, I+D, deuda y Level3 con decisión MANTENER/RESERVA y pruebas de sensibilidad.
- **F4 · Nivel 1:** [ANALISIS_NIVEL_1_20261103](ANALISIS_NIVEL_1_20261103.md), artículo **14 capítulos** según prompt maestro 2/3 v23 vigente; incluye ciclos corporativo, macro/monetario/crédito y Marks.
- **F4 · Nivel 2:** [ANALISIS_NIVEL_2_20261103](ANALISIS_NIVEL_2_20261103.md), **12 secciones**, 10 FY+LTM, 40 filas de DCF anual, los cuatro puentes equity, tres matrices DCF 5×5 y matrices Base por múltiplo; centros comparados contra valor presente FY+3, sin confundir promedio 1–3.
- **Primera auditoría del constructor, no independiente:** [AUDITORIA_INTERNA_LLM_20261103](AUDITORIA_INTERNA_LLM_20261103.md), juicio técnico y económico con riesgos no resueltos.

Los archivos anteriores `FASE_4_BORRADOR_NIVEL_1.md`, `FASE_4_BORRADOR_NIVEL_2.md` y `AUDITORIA_INTERNA_PREVISUAL_20261103.md` se conservan como borradores de trabajo/soporte, pero no son el texto canónico de la entrega. **No borrar avances**; cualquier discrepancia con el análisis final debe resolverse por evidencia de la revisión R5, no copiando números legados.

## Evidencia técnica positiva (sobre el ID R5 y sin escribir)

El [PR de motor #203](https://github.com/JuanMaRobledo/JMR-valuation/pull/203) implementó modo candidato y mejoras de ejecución. La [corrida autenticada #41640359117](https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/41640359117) finalizó con **ambos jobs verdes**:

| Control | Resultado efectivo y alcance |
|---|---|
| Suite de regresión | ÉXITO, pipeline software local |
| `inputs_completos` | 0 faltantes esenciales |
| `auditar_ceros_materiales` | 0 alertas |
| `diff_formulas_plantilla` | Código 0; 0 fórmulas→constante/vacío; diferencias fórmula→fórmula informativas requieren homologación económica |
| `candados` | 15/15 LISTO |
| `estados_completos --coverage-manifest` | **PASS_CON_SALVEDADES**: 0 filas materiales faltantes, 0 vacíos sin clasificar, 8 agregados/derivados y 3 secundarios aún pendientes |
| `auditar_estados_sec --audit-profile` | 20/20 convenciones de signo/split/fecha conciliadas; **0 diferencias restantes**, 0 cambios propuestos. Se usa fuente SEC directa con override explícito PPE, no un cotejo ciego de XBRL. |

Se conservó un [artefacto de ejecución](https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/41640359117/artifacts/13231734392), y `CIERRE_TECNICO_F1_F2_20261103.md` registra versiones anteriores, incluido fallo por tiempo de fórmula corregido mediante consultas por lotes. Los 4 DCF se reprodujeron independientemente desde proyecciones en un control previo; se añadió captura congelada específica de los cuatro escenarios y de las matrices al PR del motor para probar el mismo snapshot de punta a punta.

## Reservas y puerta que sigue pendiente

- **Económicas M1:** realismo del S/C marginal0,72 y desfase 2 años con expansión de cash CAPEX 2027; beta/regiones/deuda a mercado; riesgo material Level 3 Anthropic/OpenAI, RSUs y costo económico de SBC, capitalización de I+D proxy. Las alternativas están cuantificadas en F3 e internal audit; no cambiar hipótesis por precio o rellenar con cifras no publicadas.
- **Métodos con N/D:** EV/FCFF, P/E y P/FCFE no se presentan como precios calculados con denominadores negativos o extraordinarios. Su evaluación se documenta; no aprobar ponderado total artificial.
- **Gate de publicación NO EJECUTADO:** falta adaptar `probabilidades.py`, `controles_supuestos.py`, `consistencia_migracion.py`, `integridad_hojas.py` para validar `ticker+revision_id+sheet_id` de R5 y cotejar el **JSON candidato** con los mismos datos de hoja y app. `controles_todas.sh` en su estado actual no sirve como prueba R5 y no se ha ejecutado contra ella.
- **Producción y revisión visual:** no existe evidencia aquí de ficha Amazon R5 validada y desplegada en la aplicación; por tanto **NO publicar ni decir que ya puede inspeccionarse en app**. El usuario puede inspeccionar el candidato en la hoja y documentos mientras se cierra la puerta.
- **Auditoría independiente:** deliberadamente NO ejecutada. La hará **otro LLM después** de que el usuario revise visualmente y deje instrucciones. Nunca sustituirlo por el LLM constructor.

**Dictamen de etapa:** F3 + F4 editorial + autoauditoría **REALIZADOS como candidatos**; pruebas técnicas F1/F2 **APROBADAS CON SALVEDADES SECUNDARIAS**; publicación `EN_REVISION` **BLOQUEADA POR GATE INTEGRADO NO EJECUTADO y reservas de materialidad**. Mismo expediente, sin reiniciar Amazon, mantener las 46 pestañas. No elevar de candidato a `EN_REVISION` por simple existencia de archivos.

## Operación siguiente para cerrar sin abrir otra revisión

1. Tomar snapshot reproducible R5 con `jmr_candidate_snapshot_audit.py`, incluyendo 4 historias y anclas, y conservar hash/artefacto.
2. Ejecutar contratos de probabilidades, supuestos y consistencia usando exclusivamente JSON/hoja R5, no referencia publicada; crear JSON de valoración y análisis de la **misma** revisión.
3. Completar prueba app/preview y CI, cerrar reservas materiales de CAPEX/ROIC/WACC y no doble conteo, conciliar múltiplos N/D por aplicabilidad.
4. Si todos los controles de publicación aprobaran, publicar solo `EN_REVISION` tras autorización aplicable, presentar la ficha al usuario para **revisión visual** y recoger instrucciones. F5 auditor externo **después** de esa revisión.
