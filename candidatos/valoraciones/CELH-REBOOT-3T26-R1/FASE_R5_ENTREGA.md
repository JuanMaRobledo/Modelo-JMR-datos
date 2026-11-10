# CELH Floyd R1–R6 · R5 análisis y publicación

- Estado **CANDIDATO, NO PUBLICADO**; PASOS **1/6**. Google Doc A contiene 14 capítulos Nivel 1 y 12 apartados Nivel 2, pero es un diagnóstico con resultados faltantes; no es el análisis final.
- Documento A: https://docs.google.com/document/d/1KguK_xZWgWr7a5j92O-Ye7_mmN7up5kWN8QlxBeb8c0/edit. Las cifras históricas son las cargadas en H; valores FCFF escenarios, matrices, ROIC terminal y múltiplos son N/D.
- JSON candidato de misma revisión escritos en la rama `floyd/celh-reboot-3t26-r1`, no en main: `valoraciones/CELH-REBOOT-3T26-R1.json` y `analisis/CELH-research-CELH-REBOOT-3T26-R1.json`.
- **NO_EJECUTADO** GitHub Actions de esa revisión, validadores, coherencia económica de tres DCF, huellas de traspaso, prueba de siete pestañas de aplicación y QA de producción.
- No se modifica `catalogo.json` ni revisión A-1.2 anterior. La existencia de PR o Docs no permite declarar EN_REVISION.
- R6: RESERVADA a otro agente, NO EJECUTADA.

## CI del PR #265 · comprobación 2026-11-10
- URL: https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/265 — **borrador abierto, sin fusión**.
- Commit examinado `bab106d175eb004b5f0544d76e9ce260129ae0b2`.
- `Método A · profundidad editorial`: **success** (run 42875444049).
- `Validación de profundidad editorial`: **success** (run 42875444698).
- `Control JMR de ponderaciones`: **success** (run 42875444061).
- `Registro de revisiones y drivers`: **failure** (run 42875443823, job 130037391890). Paso `python3 scripts/registro_revisiones.py --check` denuncia diferencias en `registro/revisiones.json`, `registro/REVISIONES.md`, `registro/drivers.json`, `registro/DRIVERS.md`. El registro derivado generado añade `CELH-REBOOT-3T26-R1` con estado `SUSTITUIDA` y drivers N/D; requiere decidir la forma correcta de registrar una valoración CANDIDATO sin promoverla. **NO se han modificado automáticamente registros oficiales ni catálogos para superar un control**.
- Resultado: 3 workflows success, 1 failure. Ningún control del DCF H→D/M, de la app ni R6 puede darse por aprobado; **no publicar**.
