# INTU · Método JMR A-1.2 · valoración desde cero · INTU-20261101-A12-R1 (candidata)

**Estado:** candidata a EN_REVISION, **no promovida** (la promoción al catálogo requiere autorización del usuario). Sin auditoría económica.

- **Hoja oficial:** `1jLzrbgQBGS1OPLM0eoiURiRVoSila7ZYH89Lb0XmsFQ` (copia limpia de la plantilla IA vigente en `AAA Finanzas / Análisis / INTU`). La hoja del candidato anterior (`1SkW8M3m…`) queda sin cambios.
- **Corte:** estados al 31-jul-2026 (10-K FY2026, acc. 0000896878-26-000037); guía FY27 (8-K del 25-ago-2026, acc. 0000896878-26-000029); mercado 30-sep-2026 (precio 275,71, Rf 5,29 %, ERP 3,70 %). Hecho posterior: 341,09 el 30-oct-2026.
- **Resultado (Valuation output!B35):** DCF Base **US$402,00**; MOS35 **US$261,30**; Conservadora 295,30; Optimista 506,93; Disrupción 187,79; promedio ordinario 401,56.
- **Múltiplos por ciclo a VP:** 268,72 / 297,54 / 332,30; ponderado DCF 60 % + múltiplos 40 %: 360,22.
- **Controles de la hoja:** 15/15 candados; integridad 0; estados completos 0; entradas esenciales 0 vacías; motor de historias = hoja (diferencia 0,0); 7 matrices de múltiplos con control OK; 3 matrices DCF conciliadas.
- **Correcciones documentadas:** coste de ventas FY24-FY26 y LTM del 10-K (el importador lo dejaba en 0), sin cambio de EBIT; ventas/capital de las historias bajadas a 0,8-1,1 por coherencia con el ROIC terminal (Base 416,91 → 402,00); TurboTax y ProTax agrupados (límite de 4 segmentos de la plantilla).
- **Análisis:** Nivel 1 de 14 capítulos (7.627 palabras según el validador) y Nivel 2 de 12 apartados + referencias, con cifras de esta misma captura.
- **No ejecutado:** control de fórmula única (`apply_canonical_formulas.py` falla al importar `MASTER_ID`, error previo de la herramienta); QA visual autenticado; auditoría económica (prompt 3/3).

Archivos: `candidatos/valoraciones/INTU-20261101-A12-R1/` (valoración y análisis), `evidencia/captura-hoja-20261101/INTU-20261101-A12-R1_resultados_hoja.json`, scripts `construir_valoracion_hoja_20261101.py` y `analisis_intu_20261101_parte{1,2,3}.py`. En JMR-valuation: `scripts/run_intu_cero.py`, `scripts/intu_cero_spec.py`, `reference/multiplos_v3/INTU_*`.
