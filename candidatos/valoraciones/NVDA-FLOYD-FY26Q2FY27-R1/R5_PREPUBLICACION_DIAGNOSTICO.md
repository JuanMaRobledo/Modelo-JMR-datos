# NVDA Floyd libro único · R2–R5 · Informe de cierre y publicación EN_REVISION
**Corte de esta ejecución:** 12-nov-2026 · **Edición:** NVDA-FLOYD-FY26Q2FY27-R1 · **agente:** ChatGPT GPT-6
**Fuente normativa:** `Modelo-JMR/modelo/REGLAS_VIGENTES.md` v41 y `docs/CONTRATO_FLOYD_LIBRO_UNICO.md` v1.5. **R6 independiente:** NO REALIZADA.
**Estado:** R5 estructural completado en PR #276; `EN_REVISION` (no AUDITADO); la comprobación visual en producción requiere navegación autenticada tras integrar.

## Artefactos oficiales reutilizados, sin duplicar
- Libro único H + DCF Base/C/O + M + presentación (85 pestañas): https://docs.google.com/spreadsheets/d/1XLRmnAEGenqe1YCTYdGmdbeKyfvmEDQs8v8Bmnc3mRs/edit
- Análisis nivel 1 (14 capítulos) y nivel 2 (12 apartados), mismo Doc: https://docs.google.com/document/d/1myWWDZoFiIewj1qSoQ6KjHBEoc5Fdg_lPH8DLiidBcQ/edit
- Copia aislada usada exclusivamente para 75 corridas R3 y cuatro inversos (restaurada, no activa): https://docs.google.com/spreadsheets/d/1Z2no-hz8_hnW1ojMsLUzldS2pzMVC92zpBLcMEAeils/edit
- JSON oficial de valoración: `valoraciones/NVDA-FLOYD-FY26Q2FY27-R1.json`.
- JSON oficial de análisis: `analisis/NVDA-research-NVDA-FLOYD-FY26Q2FY27-R1.json`.
- Catálogo: `catalogo.json` incluye el par y `controlModeloA.empresas.NVDA.rutaValoracion` exacta; antiguo NVDA A-1.2 conservado en `archivoFloyd/archivo-v1`.

## Cambios verificados en el libro (no en fórmulas)
Se corrigieron solo **36 entradas históricas primarias** en LTM Income Statement, Balance Sheet y Cash Flow Statement, comparándolas con SEC, sin editar salidas calculadas. Fuentes:
- https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
- https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

| Rubro | Antes | Después SEC | Resultado |
|---|---:|---:|---|
| Ingresos LTM | 302.970 | 302.970 | CONCILIADO |
| Coste de ventas LTM | 83.963 | 76.729 | CORREGIDO |
| EBIT LTM | 195.976 | 197.579 | CORREGIDO |
| Activos totales | 333.760 | 320.272 | CORREGIDO |
| Pasivos totales | 104.776 | 91.288 | CORREGIDO |
| Patrimonio total | 228.984 | 228.984 | CONCILIADO |
| Efectivo e inversiones negociables | 99.369 | 99.369 | CONCILIADO |
| Arrendamientos corrientes + no corrientes | 5.384 | 5.494 | CORREGIDO |

Unidades: USD millones, datos contables al 26-jul-2026. El renglón fuente de cada período se amplió en `Fuentes y clasificación!A4:H21` (18 registros; seguimiento de trazabilidad por partida histórica en R6). El DCF se recalculó por **fórmulas vivas**.

## Resultados oficiales vigentes (USD/acción)
- Conservadora: **93,0159353897486** · 25%.
- Base: **176,48445877356448** · 50%.
- Optimista: **270,22596065024203** · 25%.
- Valor esperado: **179,05270339677992**; **MOS35 = 114,71489820281691**.
- Precio de referencia en la hoja **198,69**, fechado 11-nov-2026; cotización externa no contrastada por este agente.
- Múltiplos Base (secundarios): EV/EBITDA 153,3232, EV/FCFF 257,6936, P/E 125,5495, P/FCFE 119,8512, P/OCF 175,1669; promedio relativo 187,784 y combinado 75/25 = 179,309.
- WACC inicial 11,3025%; terminal 8,56%; terminal g=3,5%; ROIC terminal Base 20%; sales-to-capital 1–5 =1,45 y 6–10 =1,21.

## Corridas originales R3 y firmas
1. 25 corridas `Input sheet!B28` CAGR 2–5 × `B29` margen 44%–60%.
2. 25 corridas WACC inicial `Cost of capital worksheet!B11/B12` × `Input sheet!B68` g 2,5%–4,33%.
3. 25 corridas ROIC terminal `Input sheet!B49` × `B68` g.
4. Cuatro DCF inversos numéricos: crecimiento años 1–5 uniforme **20,38696%**; margen objetivo **58,93824%**; crecimiento uniforme con margen Conservadora 42% **24,76788%**; WACC inicial **9,16287%**. Las cuatro reconstruyeron US$198,69 dentro de US$0,001.
5. Se restauró la copia a WACC detallado, g 3,5%, CAGR 16%, margen 52%, ROIC terminal 20%. `Valuation output!B33` devolvió exactamente 176,48445877356448.
6. Se compararon **27/27 firmas posicionales** `Control de revisión!B5:B31` entre el scratch restaurado y el oficial: idénticas.
7. Se transfirieron al libro oficial **75 valores** (tres matrices 5×5) y cuatro inversos; se sellaron `Control de revisión!C5:D31` solo después de las corridas. Verificación posterior: `B2/B3=VIGENTE`; diferencias de centro `Sensibilidades DCF!B28/B29/B42=0` y `B32=CENTROS COHERENTES · AUDITORÍA PENDIENTE`.
8. Comparación de integridad de **773 posiciones de fórmulas** de Presentación, Ginsu Base/C/O (Input + Valuation output) y M · Income Statement con maestra oficial: **769 idénticas**, 4 diferencias por elección de hipótesis en entradas autorizadas del `Input sheet` Base. **No se alteraron las fórmulas de cálculo de Ginsu.**

## Análisis y publicación
El documento H3 previo contenía solo instrucciones genéricas. Se sustituyó *en el mismo ID* por tesis propia y análisis narrativo (14 capítulos, **3.631 palabras** nivel 1) + soporte cuantitativo (12 apartados, **3.093 palabras** nivel 2), actualizados tras recaptura. Los JSON están emparejados por `revisionId`, modelo `floyd-libro-unico-v1`, enlace a libro y Doc, tres escenarios, tres matrices DCF, cinco matrices de múltiplos extraídas de paneles nativos y transformadas a VP3 real; `sensibilidadMultiples.resultadosSha256` = SHA256 UTF8 de `JSON.stringify(matrices)`. Los cinco centros relativos reproducen los valores `Descuento de múltiplos!I20:I24`.

**CI confirmada en PR #276 (commit 2ffe7c1b, previo a actualizaciones documentales):**
- Registro de revisiones y drivers — PASS, luego de regenerar los cuatro archivos de registro.
- Validación de profundidad editorial — PASS.
- Método A profundidad editorial — PASS.
- Control JMR de ponderaciones — PASS.
Las pruebas deben volver a terminar en verde con el último commit tras integrar este informe.

**Materialidad:** `Asuntos por revisar!B3` muestra `PUBLICABLE · 4 asunto(s) por revisar`, **0 críticos**. Abiertos: fuentes antiguas por partida, acciones/dilución, QA visual y valor económico de inversiones no cotizadas. Revisiones futuras/independientes R6 deben verificar materialidad, supuestos terminales, precio real y coherencia de activos estratégicos. Diferencias económicas pequeñas se documentan y no bloquean si su efecto es <~2% sobre valor y tesis; nunca se ocultan.

**Lo que no certifica:** este expediente no equivale a auditoría económica R6 ni a un QA autenticado del portal. Un PR fusionado no demuestra por sí solo que Vercel sirva los nuevos datos; verificar pantalla NVDA y siete pestañas después del merge.
