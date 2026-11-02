# AMZN · AMZN-20261102-A12-R4 · reinicio desde cero e aislamiento

**Fecha:** 2026-11-02. **Estado:** CANDIDATO, Fase 1 EN CURSO. Este documento NO equivale a FASE_1_ENTREGA ni acredita auditoría o valoración.
**Instrucción expresa del usuario:** reconstruir Amazon completamente y de manera verificable; retirar R2 y R3 del circuito para que no influyan en la nueva.

## Fuente única de la nueva hoja
- **Hoja nueva R4:** https://docs.google.com/spreadsheets/d/10qfoGrEP1PgdlLWrHvfoHqExKDZbPK75yb_oINlO4a8/edit
- **sheet_id:** `10qfoGrEP1PgdlLWrHvfoHqExKDZbPK75yb_oINlO4a8`.
- **Origen:** copia directa de `reference/plantillas.json -> vigente.ia` (`1e-lbQmCkObfq74YLpWnMmIidmcdsJQ-6uN4oiHnNTEQ`).
- **Verificación nativa inicial:** 46 hojas; entradas de `Income Statement` vacías; `Valuation output!B35` conserva fórmula nativa y no muestra valor sin datos. La carpeta `AAA Finanzas / Análisis / AMZN` contiene únicamente esta R4 tras el traslado de candidatos descartados.
- **Moneda prevista:** USD, cifras financieras en USD millones; corte financiero y de mercado pendientes de confirmación con fuentes primarias.

## Exclusión expresa de versiones anteriores
Prohibido importar, copiar, trasplantar o usar como ancla datos, supuestos, historia, tasas, ROIC, DCF, múltiplos, comentarios, auditorías o resultados de **R2, R3 y otras valoraciones previas**. No comparar valores antiguos hasta cerrar de manera independiente la nueva valoración. Fuentes admitidas: SEC (10-K/10-Q/8-K), informes originales, Treasury, Damodaran (corte fechado) y otras referencias externas identificadas y verificables. La plantilla IA vigente aporta **fórmulas**, no cifras de empresa.

- R2: `1h6Xv5cNqwtKPpqI81KiZ_FNpTl4k_uQQS2QJEHphaBI` → archivada fuera de `Análisis/AMZN`, rotulada DESCARTADA NO USAR.
- R3: `1yzSqSP3Qopz3lPBNKsyXCsNSgioxZkoWOrZ6eaTjBvA` → archivada fuera de `Análisis/AMZN`, rotulada DESCARTADA NO USAR.
- Auditoría R2 y dos entregas R2: igualmente archivadas y excluidas.
- PR antiguo R2 #232: https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/232 — cerrado sin fusionar.
- Los archivos se conservan en área histórica aislada por trazabilidad, **no fueron eliminados permanentemente**.
- `catalogo.json` consultado en main: no contenía entrada AMZN, por tanto no se cambió registro vigente ni se sustituyó una ficha publicada.

## Requisitos reales antes de acreditar Fase 1
1. Reconstruir estados hasta diez años + LTM si están disponibles con documentos SEC y notas por celda, sin usar revisiones previas; auditoría de identidad, calendario fiscal, fechas, escala y saldos.
2. Justificar ceros y categorías agrupadas (I+D frente a technology and content; D&A, COGS, pasivos y arrendamientos) mediante clasificación y fuentes; nunca usar cero como dato desconocido. Comprobar conciliaciones y fórmula del LTM.
3. Ejecutar o documentar resultados reales de `estados_completos.py`, `auditar_estados_sec.py`, `auditar_ceros_materiales.py` si integrado, `diff_formulas_plantilla.py`, `inputs_completos.py` y `candados.py`; no poner APPROVED a verificaciones no realizadas.
4. Dejar inventario reproducible `dato | valor | año/LTM | unidad | URL/página | celda | naturaleza (dato/agrupación/fórmula/juicio)`, evidencia de cortes SEC, precio/Treasury/ERP con fechas, y `FASE_1_ENTREGA.md` con cada control aprobado/pendiente.
5. Mantener fases 2/3/4 separadas y método A-1.2; no publicar ni reemplazar una versión vigente hasta superar puertas aplicables y autorización.

**Regla de aislamiento para ChatGPT y Claude:** solo `AMZN-20261102-A12-R4` está habilitada como hoja de trabajo para esta reconstrucción. Toda revisión anterior es evidencia histórica excluida del motor.
