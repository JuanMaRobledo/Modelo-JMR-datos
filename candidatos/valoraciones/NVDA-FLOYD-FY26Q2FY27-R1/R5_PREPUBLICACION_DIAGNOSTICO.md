# NVDA Floyd libro único · R5 · Prepublicación BLOQUEADA

**Fecha de verificación:** 2026-11-12 (America/Bogota)  
**Agente:** ChatGPT GPT-6 (lectura mediante conectores Google Drive / GitHub; sin auditoría R6)  
**Revisión:** `NVDA-FLOYD-FY26Q2FY27-R1`  
**Contrato:** `floyd-libro-unico-v1` — `Modelo-JMR/docs/CONTRATO_FLOYD_LIBRO_UNICO.md` v1.5 y `modelo/REGLAS_VIGENTES.md` v41.  
**Estado efectivo:** `CANDIDATO / NO PUBLICAR`. El título de los documentos pone `EN_REVISION`, pero el contenido no cumple el gate R5. No se ha modificado la app ni el catálogo.

## Artefactos existentes (reutilizar IDs, no crear copias)
- **Libro único** (85 pestañas): https://docs.google.com/spreadsheets/d/1XLRmnAEGenqe1YCTYdGmdbeKyfvmEDQs8v8Bmnc3mRs/edit
- **Doc de análisis**: https://docs.google.com/document/d/1myWWDZoFiIewj1qSoQ6KjHBEoc5Fdg_lPH8DLiidBcQ/edit
- Corte: 2026-07-26 (Q2 FY2027); FY final: FY2026; moneda USD, cifras en millones; precio de referencia 198,69 USD a 2026-11-11 (valor de la hoja, cotización independiente no verificada aquí).

## Resultados leídos del motor (no auditados económicamente)
| Comprobación | Hoja/celdas | Lectura |
|---|---|---|
| DCF Base | `Valuation output!B33` | USD 176,40/acción |
| Conservadora | `Valuation output · C!B33` | USD 92,96/acción |
| Optimista | `Valuation output · O!B33` | USD 270,11/acción |
| Probabilidades | `Resumen de valoraciones!C9:E9` | 25 %, 50 %, 25 % |
| Esperado | `Presentación!B15` / Resumen | USD 178,97/acción |
| MOS 35 % | `Presentación!E7` / Resumen | USD 114,66/acción |
| Sensibilidades DCF | `Sensibilidades DCF` | Tres matrices 5×5; tres centros ~176,3974, vigencia declarada en `Control de revisión!B2:B3` |
| Cinco múltiplos | `Presentación!A37:G42` | Números presentes; anclas y calidad económica **no** verificadas |
| R2 | `Entradas históricas auxiliares!B67` | CONCILIADO · PENDIENTE AUDITORÍA MATERIAL |
| Portada | `Presentación!G47` | NO CERRADO |
| Preparación | `Supuestos y control!B64` | EN_REVISION · FALTA AUDITORÍA ECONÓMICA |

## Bloqueos de publicación (evidencia del 12-nov)
1. **Análisis A no escrito.** Lectura íntegra del Google Doc: es la plantilla H3 legada con campos `[EMPRESA]`, `[TICKER]`, `[Tesis propia, ...]`, `[Tabla: ...]` y las indicaciones redactadas entre corchetes para los 14 capítulos de Nivel 1 y los 12 apartados de Nivel 2. Su título no acredita investigación cumplida. **Material**.
2. **Fuente primaria no rastreable en el registro.** Búsqueda de `http` en toda la matriz `'Fuentes y clasificación'!A1:H350`: **0 coincidencias** (350 filas, 8 columnas, consulta no truncada). Inspección adicional A15:H40, A200:H230 y A330:H350: sin registros de detalle visibles. El selector `Supuestos y control!B63 = AUDITADO` no constituye auditoría externa y entra en conflicto con registro vacío. **Material**.
3. **R2 no cerrado / salvedades pendientes.** La hoja declara `CONCILIADO · PENDIENTE AUDITORÍA MATERIAL` y la portada `NO CERRADO`. Validar deuda, caja, activos no operativos, dilución, fuentes de ingresos por intereses y puentes postcorte antes de promoción; no corregir salidas manualmente.
4. **Aún no existen par JSON ni entrada activa de esta revisión en `valoraciones/`, `analisis/`, `catalogo.json` para NVDA Floyd.** La entrada vigente que figura actualmente en `controlModeloA.empresas.NVDA` es `valoraciones/NVDA-20261101-A12-R1.json`. No sustituirla hasta aprobar R5 y preservar archivo histórico.
5. **Sin controles de integración/QA autenticado.** No se ejecutaron `scripts/preflight_floyd.cjs`, `validar_catalogo.cjs`, CI ni prueba en producción: todavía no hay JSON de esta revisión para validación. **NO_EJECUTADO**.

## Secuencia mínima de recuperación (sin reconstruir valoración ni modificar motores)
1. Completar y documentar la trazabilidad de los diez FY + LTM en `Fuentes y clasificación`, con URLs/nota SEC oficiales, celdas, clasificación, precio y comprobaciones; conciliar el estado R2 y todos los asuntos materiales sin declaraciones genéricas.
2. Redactar **en el Doc existente** el análisis específico de NVIDIA: 14 capítulos N1 + 12 secciones N2, reconciliado con las salidas vivas del libro, supuestos y fuentes primarias; retirar todos los placeholders.
3. Validar integridad de fórmulas frente a maestra (`verificar.py`), tres motores, matrices e inverso con evidencia de corridas, múltiplos y anclas, y los estados de `Control de revisión`. No fabricar sellos ni aprobar por estado textual.
4. Crear los **dos JSON de la misma revisión**, con `contratoLibros=floyd-libro-unico-v1`, `libros.unico`, `libros.analisis`, `hojaGoogle`, `sheet_id`, resultados reales y fuentes. Ejecutar preflight y validadores.
5. Solo si pasan los gates, promover `NVDA-FLOYD-FY26Q2FY27-R1` en catálogo y `controlModeloA.empresas.NVDA`, preservar revisión A-1.2 en archivo, fusionar tras CI y probar ficha de siete pestañas en producción. Mantener R6 independiente.

**No modificar:** motores Ginsu, fórmulas, selectores, pestañas, matrices sin corridas, o los documentos históricos. Esta entrega es *diagnóstico reproducible*, NO autorización de producción ni certificación económica.