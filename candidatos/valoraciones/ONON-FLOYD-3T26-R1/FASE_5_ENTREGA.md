# ONON Floyd libro único · R1–R4 · candidato (no publicado) · 12-nov-2026

**Estado:** CANDIDATO fuera de `catalogo.json`; NO PUBLICAR. R2 no cerrado; R6 NO REALIZADA; sin PR, integración, despliegue ni verificación en la app.
**Contrato:** `floyd-libro-unico-v1` (CONTRATO_FLOYD_LIBRO_UNICO v1.5). **Moneda de valoración:** USD (estados en CHF convertidos; respaldo en CHF).

## Artefactos
- Libro único (85 pestañas): https://docs.google.com/spreadsheets/d/1yWRxhEtXldpVU415VDpcz3hehf33xLVlL6BiF3IhR98/edit
- Análisis N1 (14 capítulos) y N2 (12 apartados): https://docs.google.com/document/d/1mG6Sl51M3j-rRT65s61ql_fNIi_Lk_-TtORbTq8j_PY/edit
- Respaldo en CHF: https://docs.google.com/spreadsheets/d/1SKoPFQ2B7Wh5XEcsIpledTz1o83nAHKHKlVkVzdgccI/edit
- Copia temporal de corridas (NO USAR): https://docs.google.com/spreadsheets/d/19_NjUTHZeocSBLECyhv2leZmaOpQkNjWmJr6E8HImt8/edit
- JSON: `ONON-FLOYD-3T26-R1.json` y `ONON-research-ONON-FLOYD-3T26-R1.json` (esta carpeta).

## Resultados (USD por acción; precio 33,10 al 12-nov-2026, fuente secundaria)
Conservadora 20,1065 (25 %) · Base 34,8104 (50 %) · Optimista 56,8061 (25 %) · esperado 36,6333 · MOS35 sobre el Base 22,6267.
WACC inicial 9,894 %, terminal 9,11 %, Ke 10,141 %, Rf 4,88 %, g 4,88 %, ROIC terminal 11 %.
Múltiplos Base (secundarios): EV/EBITDA 25,95; EV/FCFF 16,68; P/E 24,74; P/FCFE 20,18; P/OCF 30,85; ponderado 21,46; combinado 75/25 = 31,47.
DCF inverso (precio 33,10): crecimiento 1–5 10,80 %; margen 14,73 %; crecimiento con margen Conservadora 17,0 %; WACC inicial 10,83 %.

## Verificación ejecutada
- `node scripts/preflight_floyd.cjs` sobre los dos JSON: ESTRUCTURA_OK (sin catálogo).
- 96 corridas del motor original sobre copia (75 de matrices y 21 del inverso); centros conciliados; firmas `Control de revisión!B5:B31` copiadas a C y D; B2/B3 VIGENTE.
- Las cinco matrices de múltiplos son paneles nativos del libro (fórmulas vivas).

## Incidentes
- `Input sheet!B24` (tasa marginal) estaba vacía: Base 41,45 → 34,81 tras fijar 21 %; se rehicieron matrices e inverso.
- Defecto de plantilla (deuda sin arrendamientos, `Input sheet!B14`): arrendamientos IFRS 16 clasificados como deuda; sin tocar fórmulas.
- Se sobrescribió y restauró la fórmula `Guía y empresa!B13` y una fila de estados de `M · Income Statement`.

## Pendiente (ver pestaña «Asuntos por revisar» y `asuntosPorRevisar` del JSON)
R2 (siete ejercicios; el control exige 11 columnas), contraste de precios y tipos de cambio con fuentes primarias, comparables Adidas/ASICS/Brooks, auditoría R6, catalogación, PR, CI, despliegue y verificación de las siete pestañas de la app.
