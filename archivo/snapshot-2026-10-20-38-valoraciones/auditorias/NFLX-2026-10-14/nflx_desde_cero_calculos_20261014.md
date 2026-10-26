NFLX — FUNDAMENTOS Y CÁLCULOS | MODELO JMR | NIVEL 2
Corte: 14 de octubre de 2026 | Cierre financial: 30 de junio de 2026 | Precio fijo: US$70,46 (13-oct-2026)
Hoja de cálculo canónica de esta reconstrucción: https://docs.google.com/spreadsheets/d/1XBj_TtiOqhrdYU0-5JI2iUVrAC7GZHlSvdlTHe3CVds/edit
ESTADO: REGISTRO DE VALORACIÓN Y DOS NIVELES DE ANÁLISIS PUBLICADOS EN GITHUB MODELO-JMR-DATOS; CONTROL CERTIFICADO EN CI SOBRE SNAPSHOT Y 28 FÓRMULAS CRÍTICAS COMPROBADAS. AUDITORÍA ECONÓMICA POSTERIOR DEL INVERSOR PENDIENTE. Visualización final en Vercel no comprobada por restricción de acceso del proyecto.
1. MÉTODO Y CIFRAS CONTABLES (USD MILLONES)
El DCF internacional para compañía no financiera se basa en FCFF = EBIT económico × (1−tasa fiscal) − reinversión. Horizonte 10 años + año11 perpetuo; tasa WACC por año de proyección. Reconstrucción LTM para resultados/caja = 2025 anual + 1S2026 − 1S2025. Balance = saldo 30-jun-2026, nunca 2025 + semestre.
Revenue FY2025 45.183,036, Revenue LTM 48.370,764.
EBIT GAAP FY2025 13.326,603; EBIT LTM 14.354,517, margen 29,68%.
Reexpresión operativa de lease ~+170,789 → EBIT económico inicial 14.525,306 (30,03% LTM). Rentabilidad revisada; no afirmar que el ajuste no GAAP está reportado por Netflix.
CFO LTM 11.970,833; CAPEX PPE LTM 818,808; FCF reportado CFO−PPE ~11.152,025. Se incluyen pagos de contenido dentro de CFO.
Caja e inversiones corto plazo 9.127,900; deuda financiera de balance 14.309,306; número de acciones 4.163,939676 millones; valoración de opciones existentes calculada por Black-Scholes ≈5.026,323. Datos del 10-Q salvo parámetros Black-Scholes explícitamente estimados.
2. INGRESOS / MERCADO / OPERACIÓN
Modelo de motores: crecimiento UCAN, EMEA, LATAM, APAC, efecto de subidas de precio, retención/engagement, ingreso publicidad y directo. Los factores por región son mixtos e interactúan; no tratar tasa de región como causalidad de publicidad exclusiva.
Base tasas años 1–10: 11,50%; 10,50%; 9,50%; 8,60%; 7,80%; 6,90%; 6,00%; 5,10%; 4,30%; 3,50%. Año11 3,50%.
Comprobación: ingresos LTM 48.370,764 → año1 53.933,402 → año10 98.218,601 → año11 101.656,252.
CAGR años1–5 ≈ 9,5721%. Precio al análisis 70,46 no intervino para elegir crecimiento.
3. MÁRGENES
Actual GAAP EBIT 29,68% LTM; reconciliado lease ≈30,03%. Año 1 continúa 30,03%, año5 34,50%, año10/11 34,50%. Es mejora por monetización/escala estimada, sin prueba de EBIT incremental por cada licencia o serie; conservar estado "con salvedades".
Guía Netflix FY2026 EBIT 31,5%; objetivo del analista en año5 34,5% > guía. Cualquier divergencia de flujo la explicaremos con contenido, gastos tecnológicos, marketing y ventas.
4. REINVERSIÓN Y ECONOMÍA DEL CONTENIDO
Ventas/capital incremental Base 1–5=1,18x; 6–10=0,60x. Se conserva lag del motor original entre inversión y crecimiento: no sustituir cash content arbitrariamente sin reexpresar EBIT.
Primer semestre 2026 adiciones a activo contenido 9.774,440; variación pasivo contenido con efecto efectivo −136,578; pago aproximado contenido 9.911,018; amortización 8.529,209. Brecha de pagos vs amortización ~1.381,809. No equivale sin más a capital nuevo neto, por calendarios de deuda de contenido, divisas y activos; no restar pagos adicionales a CFO que ya los incluye.
ROIC marginal sobre nuevas inversiones NO es el ROIC GAAP de toda la empresa y no es directamente observable por cohortes: registrar evidencia/limitación, no calcular circularmente ventas/capital desde el ROIC elegido. Necesidad de backtesting temporal.
5. IMPUESTOS / GASTOS EXTRAORDINARIOS
Tasa efectiva LTM 17,24% de beneficio contable. Hubo cobro no recurrente WBD 2.800 millones 1T2026 registrado por debajo de EBIT, generador de caja incluido CFO. No capitalizarlo. Propuesta IA impuesto inicial normalizado 21%, converge a tasa marginal 25% al año10 y perpetuidad. Es supuesto prudente sujeto a conciliación de créditos FDII, jurisdicciones y tasa de estados.
6. WACC
Rf USD nominal inicios octubre2026 5,29%; prima madura implícita 3,70% según Damodaran, distinta de ERP Netflix por regiones ponderada ≈4,92%. Unlevered beta por sector Entertainment global, estructura market equity vs deuda propia, Ke aprox10,33%. Deuda Kd nominal supuesto 6,14% = Rf 5,29 + spread analista0,85 pp; no afirmar que rating sea oficial.
WACC inicial 10,02277%, converge a WACC terminal 8,99%. ROIC terminal Base 13,50%, 4,51 puntos porcentuales sobre WACC terminal. Necesidad de justificar ventajas de plataforma, retención, ventajas de producción/distribución.
7. PERPETUIDAD
g = 3,50% anual nominal USD; inferior a Rf y WACC. Reinv11 = NOPAT11 × g/ROIC = 26.303,555 × 0,035/0,135 = 6.819,440.
FCFF11 = 26.303,555 − 6.819,440 = 19.484,115.
TV10 = 19.484,115/(0,0899 − 0,035) = 354.901,911.
PV TV = 140.460,752; valor terminal ~62,34% del EV operativo.
ROIC promedio observado año10 puede diferir ROIC *marginal* año11: caída no equivale necesariamente a destrucción del stock existente.
8. CUATRO HISTORIAS (SIMULTÁNEAS, SUMAN 100%)
Base: prob45%; CAGR cinco años9,5721%, margen año5 34,5%, S/C1–5 1,18, 6–10 0,60, ROIC terminal13,5%, g3,5%; DCF 51,1044/acción.
Conservadora: prob25%; CAGR cinco años7,0144%, margen año5 31,5%, S/C1–5 1,02, 6–10 0,55, ROIC terminal10%, g3,5%; DCF 37,3014.
Disrupción: prob10%; CAGR cinco años2,1923%, margen año5 23,5%, S/C1–5 0,85, 6–10 0,55, ROIC terminal9%, g0,7%; DCF 21,9093.
Optimista: prob20%; CAGR cinco años11,6108%, margen año5 38,5%, S/C1–5 1,40, 6–10 0,70, ROIC terminal17,5%, g3,5%; DCF 68,1482.
Promedio historias = suma p×DCF = 48,1429 (informativo). DCF Base=51,1044 único valor intrínseco principal. No usar promedio como justificación del margen Base.
9. PUENTE DCF BASE — RECONSTRUCCIÓN Y CONTROL
PV FCFF años1–10: 84.872,299
PV terminal: 140.460,752
EV operaciones: 225.333,051
Menos deuda incluyendo lease no reconocido como deuda en presentación: 16.638,980
Más caja: 9.127,900
Menos opciones: 5.026,323
Valor de capital común: 212.795,648
Acciones 4.163,939676 M → valor por acción 51,104402.
Comprobaciones: 84.872,299 + 140.460,752 = 225.333,051; 225.333,051 − 16.638,980 + 9.127,900 − 5.026,323 = 212.795,648.
Con precio fijo 70,46: variación valor/precio ~−27,5%. Precio de análisis congelado por fecha; precio actual separado.
10. ARRENDAMIENTOS Y DILUCIÓN
El pasivo reconocido de arrendamientos en el 10-Q es cercano a 2.330,421 M y aparece incluido en otros pasivos, fuera de filas de deuda financiera de esta hoja. El PV de obligaciones según calendarios transcritos y Kd es 2.329,67 M, diferencia aproximada 0,75 M. El motor resta lease como deuda una sola vez y suma ajuste EBIT ~170,789 M. Los calendarios y gasto anual proxy requieren todavía constatación del perímetro y vencimientos.
Opciones: 123,891603 M a strike medio 39,21; vida restante 4,3 años y vol35% son estimaciones de modelo, no certezas. No duplicar compensación basada en acciones en el denominador o en ajustes a flujo. Recompras, RSU futuras y valor temporal son riesgos abiertos.
11. SENSIBILIDADES Y LIMITACIONES
Cambios en margen, productividad del capital y ROIC marginal pueden alterar mucho el patrimonio. El valor terminal ~62% del EV exige probar WACC, g y ROIC juntos y no interpretar dos decimales como precisión económica. En especial S/C 0,60 de años 6–10 necesita contrastarse con inversión en contenido, caja y crecimiento. No usar valoraciones de terceros para conciliar DCF.
Los registros completos 2016–2024 se transfirieron como históricos candidatos desde una hoja JMR anterior, manteniendo períodos, pero NO se recertificó fila por fila contra los 10-K individuales en esta reconstrucción. Los últimos dos cortes y valores LTM críticos se reconstruyeron con SEC. Algunos desgloses históricos de caja son aproximados o incompletos y requieren validación independiente. Sin verificación de múltiples relativos, no publicar métricas de esas metodologías como nuevas.
12. CONTROL Y AUDITORÍA POSTERIOR
Resultado operativo completo en la hoja IA; 28 fórmulas críticas comparadas y cero diferencias, selectores conservados, cuatro historias LISTO, WACC VALIDADO. El validador DCF certificado fue ejecutado en GitHub Actions con snapshot inmutable y manifiesto de fuentes el 14-oct-2026: https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/38645804369 . El control mediante snapshot no equivale a ejecutar todos los scripts frente a Google Sheets en vivo; falta confirmar la interfaz web Vercel. Se mantiene CON SALVEDADES por histórico 2016-17, capital incremental del contenido y múltiplos secundarios sin anclas, con AUDITORÍA POSTERIOR DEL INVERSOR PENDIENTE.
Para revisar tras publicación: crecimiento y márgenes por trimestre/región, gastos de contenido y pagos, deuda/lease, opción/RSU, guidance FY26, cambios en g y coste de deuda. Nuevas cifras no reemplazan retroactivamente el corte inicial.
FUENTES
SEC 10-K FY2025: https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm
SEC 10-Q Q2-2026: https://www.sec.gov/Archives/edgar/data/1065280/000106528026000212/nflx-20260630.htm
Netflix Investor Relations: https://ir.netflix.net/financials/quarterly-earnings/default.aspx
Damodaran octubre 2026: https://aswathdamodaran.substack.com/p/earnings-cashflows-and-stock-prices
Reuters 14-Oct layoffs: https://www.reuters.com/business/world-at-work/netflix-cuts-about-6-jobs-wsj-reports-2026-10-14/
