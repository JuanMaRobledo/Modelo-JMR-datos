# Migración Estilo JMR narrativo v19 — 30 de octubre de 2026

## Alcance

Catálogo vigente: **23** estudios activos. Se aplicó en esta revisión el nuevo índice narrativo de 13 capítulos a **19 expedientes**:

`META, NVDA, MELI, CELH, ADBE, BSX, CMG, NFLX, GOOGL, MSFT, NKE, PYPL, EPAM, ZTS, ONON, NU, NVO, INTU, AFYA`.

Se dejan **4 legados sin migrar**, dado que no se han reconstruido aún en el proceso financiero reciente y el usuario permitió omitirlos:
`XP, DUOL, SHAK, UBER`. Se conservan sus archivos y fuentes.

## Pruebas de preservación

En cada uno de los 19 expedientes se comparó la versión original en `main` con el registro transformado en la rama `editorial/analisis-narrativo-v19-20261030`:
- **13 capítulos principales** `h2` con títulos y orden vigentes.
- **0 párrafos originales perdidos** por empresa (excluyendo únicamente antiguas notas de huecos generadas por una migración previa).
- Sin modificaciones en campos ajenos a `articleHtml`, `html`, `calculationHtml` o la metainformación editorial `jmrNarrative`.
- `calculationHtml` original **sin cambios en 18/19** expedientes. En AFYA, que carecía de anexo autónomo, se añadió aviso explícito de falta de soporte: **no** se crearon fórmulas ni cifras.
- Los títulos anteriores y bloques narrativos quedan como subsecciones de sus capítulos económicos; se preservan datos, fuentes, tablas y referencias existentes.

**Estos controles son documentales, no una auditoría de datos financieros, ni una validación de profundidad.**

## Estado de contenido

Todos los estudios se etiquetan en `jmrNarrative.version=JMR-NARRATIVO-V19` y
`jmrNarrative.structuralOnly=true`. Los capítulos que solo tienen una nota de
pendiente de investigación se listan en `jmrNarrative.sectionsNeedingResearch`.
No se inventan pasajes de industria, management, noticias, supuestos o catalizadores
donde faltaba un desarrollo independiente.

Falta investigación/completitud editorial específica para los capítulos marcados,
incluido contraste de datos primarios, profundidad de dirección/competencia,
coherencia de supuestos y seguimiento. **Ninguno de los 19 debe presentarse como
totalmente terminado solo por la migración.**

La ficha sigue siendo `EN_REVISION` o conserva el estado anterior real.
La auditoría económica permanece separada, solo después de revisión visual.

## Cambios de metodología

Norma editorial: `Modelo-JMR/modelo/REGLAS_VIGENTES.md` §9 versión 19;
`Modelo-JMR/docs/ESTILO_ANALISIS_FUNDAMENTAL_JMR.md`.
No se alteran DCF, FCFF/FCFE, escenarios, MOS35%, múltiplos, Método A/B,
valoraciones ni hojas oficiales.
