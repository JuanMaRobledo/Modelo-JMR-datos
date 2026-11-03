# Corrección de crecimiento visible en Input sheet · AMZN R5 · 2026-11-02

Hoja única: https://docs.google.com/spreadsheets/d/199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I/edit
Revisión: `AMZN-20261102-A12-R5`, Método JMR A-1.2. No se reutilizó R2/R3/R4. Afecta referencias informativas y enlazado de tasas, NO drivers ni resultados DCF.

## Error identificado
- `Input sheet!I26`, crecimiento histórico de la empresa junto a las comparaciones sectoriales, estaba EN BLANCO: su fórmula asumía abreviaturas de meses inglesas y año de dos cifras, mientras `Income Statement!K2=2025` y `L2=LTM 2026-09-30`.
- `Input sheet!B27` (crecimiento proyectado año1) se enlazaba a `Income Statement!L4=11,23285%`, que comparaba LTM Sep2026 contra FY2025: son períodos solapados de distinta base, NO un pronóstico ni auténtico crecimiento interanual LTM.
- `Input sheet!B29` (CAGR proyectado años2–5) copiaba el mismo B27 histórico en vez de calcular los cuatro crecimientos anuales del escenario Base.
- `Valuation output!B4` (crecimiento del año base) traía el antiguo B27 no comparable. Ninguna de estas celdas alimentaba las proyecciones anuales Base C4:M4, que nacen directamente de `Escenarios e historias!C29:L29`; el DCF era calculable, pero Input era equívoca.

## Datos SEC y reparación con referencias (no importes de otra revisión)
- Fuente primaria 2025 Q3 10-Q: https://www.sec.gov/Archives/edgar/data/1018724/000101872425000123/amzn-20250930.htm, ingresos 9M2024 **450167 M USD**, 9M2025 **503538 M USD**.
- Fuente primaria 2026 Q3 10-Q: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm, ingresos 9M2026 **584069 M USD**.
- `Entradas históricas auxiliares!J6=450167` con URL SEC en nota; `J7='Income Statement'!J3+'Income Statement'!M3-J6` = LTM Sep2025 **691330 M**, `J8='Income Statement'!L3` = LTM Sep2026 **797455 M**, `J9=J8/J7−1` = crecimiento LTM YoY **15,350845%**.
- `Input sheet!I26` enlazó al cociente de J8/J7 con control de existencia numérica; **15,35 %**, correctamente comparable año contra año, no anualización de LTM frente a un 10-K.
- `Input sheet!D12` ahora calcula **0,75 años** desde FY2025 hasta el LTM Sep2026 interpretando etiquetas ISO (el blanco por formato quedó resuelto). Esta celda describe tiempo transcurrido; **NO** sustituye el verdadero LTM YoY.
- `Input sheet!B27` ahora enlaza a `Escenarios e historias!C29` = **11,00 %** (proyección Base año1). `Input sheet!B29` usa la media geométrica de `Escenarios e historias!D29:G29` = **8,872493%** (CAGR Base años2–5). Los valores de las historias no fueron editados.
- `Valuation output!B4` ahora enlaza crecimiento histórico LTM YoY `Input sheet!I26=15,35%`, distinto del crecimiento proyectado año1 de `Valuation output!C4=11,00%`.
- `Input sheet!A137:B152` contiene resumen con **FY2025 YoY12,38%, LTM YoY15,35%, 9M YoY15,99%, CAGR 3Y11,73%, CAGR 5Y13,18%, CAGR 9Y20,29%, Base año1 11,00%, Base CAGR años2–5 8,87%, Base años6–10 5,99%, terminal efectivo 4,00%, años1 Conservador8%, Optimista14%, Disrupción3%**; todas las tasas son fórmulas a datos SEC o drivers R5. El rótulo terminal distingue J5 efectivo de M29, que no es el driver terminal con override B68=Yes.

## Verificación POST-ESCRITURA
- Fuente J6/J7/J8/J9: **450167 / 691330 / 797455 / 0,1535084547** confirmados por lectura efectiva de Sheets.
- `Input sheet D12=0,75`, `I26=15,35%`, `B27=11,00%`, `B29=8,87%`, `Valuation output B4=15,35%`, `C4=11,00%`.
- DCF Base **US$149,19148575564947** y otros escenarios Conservador **US$81,0095172**, Disrupción **US$62,4357315**, Optimista **US$241,8435161**: **SIN CAMBIOS**.
- Los cuatro `Escenarios e historias!K5:K8=LISTO`, `Cost of capital worksheet!B84=VALIDADO`, las tres matrices `Sensibilidad DCF!B12/B23/B34=OK`, inspección sin errores de fórmula en rangos actualizados.

## Prevención de regresiones
En la plantilla IA universal, corregir la extracción de etiquetas de período ISO, separar **crecimiento histórico comparable** de **driver Base año 1 y CAGR 2–5**, y exigir `Input I26` no vacío cuando se dispone de 9M comparables SEC. Proponer test por copia limpia antes de cambiar plantilla maestra, porque el proceso JMR A-1.2 requiere preservar drivers y fórmulas. Esto es una corrección de R5, NO propagación automática a todas las plantillas o empresas.

**Estado:** corrección aplicada en AMZN R5 y documentada; scripts oficiales del motor NO EJECUTADOS, F3 económica y publicación pendientes; PR #234 permanece draft.