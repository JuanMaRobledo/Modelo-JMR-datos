# AMZN R4 · transición al proceso JMR de cinco fases
**Fecha:** 2026-11-02. **Estado:** plan de transición propuesto, sin cambio de cifras ni resultados.
**Hoja oficial de trabajo:** https://docs.google.com/spreadsheets/d/10qfoGrEP1PgdlLWrHvfoHqExKDZbPK75yb_oINlO4a8/edit

## NO equivalencia automática
- El archivo anterior `FASE_1_ENTREGA.md` fue creado bajo el proceso **viejo de cuatro fases** y describía principalmente estados históricos parciales. **No es la nueva Fase 1**, cuyo objetivo ahora es DCF Damodaran + cuatro historias + contraste por múltiplos con los datos conectados a Input sheet.
- Los históricos FY2016–2025 y LTM que están cargados **se conservan** como evidencia disponible para la nueva **Fase 2**, sujetos a auditoría de clasificación, errores detectados y controles oficiales. No recargarlos sin causa.
- **Nueva F1 de AMZN R4 pendiente:** reconstruir inputs materiales de DCF, WACC, impuestos, ajustes I+D/lease/SBC, activos no operativos Anthropic/OpenAI, NCI y cinco múltiplos aplicables; validar la plantilla/fórmulas para calcular cuatro historias provisionales. No reutilizar jamás R2 ni R3.
- **Nueva F2 de AMZN R4:** completar/recertificar históricos, falta de desagregación e indicadores, auditoría de fuente y fórmulas. El bug de impuestos en `Financials Multiples` [JMR-valuation issue #194](https://github.com/JuanMaRobledo/JMR-valuation/issues/194) permanece bloqueante para el P/E correspondiente; no considerar solucionado porque hay fórmulas.
- **Nueva F3:** evaluar crecimiento, EBIT, ROIC terminal, S/C marginal, reinversión y lag, WACC y múltiplos con evidencia de F2, decidir cambios y calcular efecto en DCF Base/MOS.
- **Nueva F4:** análisis fundamental N1/N2 completo y publicación `EN_REVISION` solamente si pasan gates y sincronización hoja–JSON–app.
- **Nueva F5:** auditoría económica independiente guiada por observaciones del usuario.
- `Forward Valuation` se declara obsoleta y sale de favoritos, pero **AMZN R4 conserva 46 pestañas** hasta que la migración de plantillas 45 pase pruebas; no borrarla físicamente ahora.

**Regla de transición:** nuevas entregas deben agregar explícitamente `proceso_version=5f`, `fase`, `estado`, `revision_id=AMZN-20261102-A12-R4`, fuentes, prueba, celdas y bloqueo. El viejo `FASE_1_ENTREGA.md` se conserva por trazabilidad y no debe sobrescribirse para aparentar haber hecho el nuevo proceso.
