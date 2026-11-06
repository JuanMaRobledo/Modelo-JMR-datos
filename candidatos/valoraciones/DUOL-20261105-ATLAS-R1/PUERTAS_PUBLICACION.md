# DUOL Atlas R1 · Auditoría de publicación — 6 noviembre 2026

**Estado actual:** CANDIDATO / PUBLICACIÓN BLOQUEADA por datos materiales sin verificar. La orden del usuario para completar y publicar está autorizada; no autoriza sustituir valores N/D por otros de una versión distinta. La ficha activa DUOL R2 y el catálogo de producción continúan intactos.

## Entregables reproducibles de la revisión
- Estados y cohortes SEC: https://docs.google.com/spreadsheets/d/1f3lPGhv8Lx0DzrA-vwXbLlD5JxzTcjPtj_Nn026mZJA/edit
- DCF, tres sensibilidades 5×5, WACC y materialidad: https://docs.google.com/spreadsheets/d/1YPtE7UWhIPCMhiENnRNCe-jX8mzoGEnjpv78P6TdNt4/edit
- Múltiplos y pesos, con valores faltantes identificados: https://docs.google.com/spreadsheets/d/1K0yBSETJQkWjdAHRy6Os-3iQ5dmHW_bc88LTMXhUxYU/edit
- Nivel 1 (historia → números): https://docs.google.com/document/d/1vJtGag0P7q8QRmHpz4WyNxfQDihK5KlEm9jtjIUAvZI/edit
- Nivel 2 (supuestos, fórmulas y pruebas): https://docs.google.com/document/d/1TJ5dDsObHGPD8dTSX_gql6pF1pWJpf9QNWiwa0BrR-Q/edit

## Resultado DCF, desde la hoja y NO CERTIFICADO ECONÓMICAMENTE
Corte financiero **2026-09-30**, mercado **2026-11-05**. Base DCF FCFF **US$108,2272265**; MOS35% **US$70,3476972**. Conservador **US$78,8020985**, Optimista **US$151,3868611**, promedio condicional C/B/O 25/50/25 **US$111,6608532**. Stress IA independiente **US$66,6760002**. No ajustar al precio US$157,02. Caja + activos no operativos − lease = equity bridge sin doble conteo. WACC inicial12,6192%, terminal9,7%, g nominal terminal4%, ROIC marginal terminal11,5%.

## Puertas que sí cerraron en esta revisión
1. **I+D SEC, 4/4 cohortes TTM septiembre conciliadas:** 188,566 (2023), 219,159 (2024), 293,162 (2025), 362,473 (2026), fórmulas FY+9M−9M; hoja de estados tab `12 Cohortes ID SEC` y export `05 Export Atlas` B37:B39; vinculado a converter.
2. **WACC con tasa y ERP del mismo corte Damodaran 01-nov-2026:** Treasury10Y 5,29%, ERP4,41%, beta cash-corrected unlevered1,59, reapalancada1,60259 con leasing reconocido84,216M y equity7.976,616M; CRP 0,35pp es **juicio de analista**, stress CRP0–1pp mueve valoración de US$109,2533 a US$106,3628 (−1,72% máximo individual). Hoja DCF tab `20 WACC Damodaran 01Nov2026`.
3. **WACC común a cuatro historias, g terminal USD4%**, WACC de 12,6192% a9,7%; ROC terminal ajustado por historia, disrupción no promediada.
4. **Tres matrices DCF Base 5×5 con centro exactamente coincidente** con US$108,2272265: WACC/g `10 Sens WACC g`!E11, ROIC/g `11 Sens ROIC g`!E11, crecimiento explícito/margen EBIT `21 Sens crecimiento EBIT 5x5`!D11. Tercera matriz ejecuta **25 DCF completos**, recalcando ventas, reinversión, FCFF y VP diez años.
5. **Dos niveles narrativos**: Nivel 1 extenso y Nivel 2 reproducible en dos Google Docs. Requieren adaptación final al contrato de app (14 capítulos) antes de publicar.

## Puertas aún ABIERTAS / no acreditar
1. **VALOR RELATIVO 40% GLOBAL — BLOQUEO MATERIAL.** Múltiplos EV/FCFF15%, EV/EBITDA10%, P/E5%, P/FCFE5%, P/OCF5%. Dentro del bloque 37,5/25/12,5/12,5/12,5%. Pesos suman 100%, pero los **cinco precios FY+3, valor presente y sus sensibilidades de Atlas permanecen N/D** por falta de anclas independientes de histórico FY+3, normalización consistente, peers y controles. P/S y P/BV tienen peso cero opcional. El libro de múltiplos tabs `12 POCF y comparables`, `13 Sens POCF`, `14 Ponderacion DCF y multiples`, `15 Históricos propios DUOL` contiene fórmulas y diagnósticos históricos; **los históricos no equivalen a comparables externos** ni permiten formar un valor combinado. No transportar cifras de R2/R4 porque el Google Sheet de R2 diverge materialmente de su JSON publicado.
2. **SBC/dilución:** SEC Q3 reporta 50,8m acciones ya fully diluted y 156,596M SBC LTM. Guía SBC FY2026 ≈14% de ingresos y dilución bruta 3,5–4% antes de recompras. No volver a deducir RSU/opciones existentes; verificar emisión futura y recompras sin duplicar SBC modelada en EBIT. Stress 1% dilución neta diez años sería ~−9,47%/acción, pero NO se aplica sin comprobar doble conteo. Tab `22 Materialidad NOL lease SBC`.
3. **Créditos fiscales/NOL 2026:** NOL federal111,199M, estatal72,425M, créditos76,419M (FY2025), DTA neto203,605M (Sep2026). Límite nominal superior no descontado de tres atributos ~US$107,84M ≈US$2,12/acción (1,96%). No sumar DTA a los mismos atributos. Falta transición de impuestos en efectivo y uso FY2026; no inyectar beneficio ficticio al DCF.
4. **Arrendamientos ASC842:** pasivo84,216M reconocido, sin doble deuda; amortización ROU proxy7,279M sobre lease cost FY2025 12,071M. Estimación ±gasto total equivale aproximación ±US$0,835/acción (<0,8% individual), **no** prueba contabilidad completa.
5. **Materialidad conjunta y fuentes:** NOL nominal 1,96% + máxima CRP ~1,72% + lease ~0,77% puede superar **3%** sin compensar signos, encima incertidumbre SBC; dictamen económico sigue PENDIENTE.
6. **Integración técnica Atlas→app:** libros modulares Atlas no cuentan con las hojas nativas obligatorias `Financials Multiples`, `Descuento de múltiplos`, `Sensibilidad por múltiplo` de una misma revisión. Hace falta adaptador/evidencia de fórmula y contrato JSON. No crear una ficha aparentemente COMPLETA con N/D ponderado. No se ejecutó `bash scripts/controles_todas.sh`, QA autenticado Vercel móvil/escritorio ni regresión global.

## Contratos y destino
- Método JMR A-1.2: `modelo/REGLAS_VIGENTES.md` §§0A, 0B, 4A, 4B, 5A, 6 y 8A.
- **Valor intrínseco principal** es DCF FCFF Base, MOS35% únicamente sobre el Base, **no** sobre el promedio de métodos ni de escenarios.
- La valoración relativa y el combinado 60% DCF / 40% múltiplos deben publicarse separados **solo cuando sus fórmulas de la MISMA revisión den resultados válidos**.
- La historia Disrupción es **separada y no ponderada**.
- La app continúa usando `valoraciones/DUOL-20261103-A12-R2.json` y `analisis/DUOL-research-20261103-A12-R2.json`. La solicitud de publicar R1 está registrada; esta PR solo almacena avances candidatos.

**Decisión verificada 2026-11-06:** No fusionar/publicar la valoración incompleta de DUOL Atlas hasta controlar múltiples y las dependencias estructurales anteriores. No afirmar certificación, publicación ni app QA no ejecutadas.
