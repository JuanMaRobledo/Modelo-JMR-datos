# Amazon R5 — Nivel 2 · Datos, fórmula, supuestos y reproducción
**Corte financiero:** 2026-09-30 (LTM), **mercado:** 2026-10-30, **unidad:** millones USD salvo por acción. **Revisión:** AMZN-20261102-A12-R5. **Estado:** borrador reproducible, materialidad económica pendiente, publicación bloqueada. Fuente única de cálculos: [hoja candidata de 46 pestañas](https://docs.google.com/spreadsheets/d/199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I/edit).

## 1. Identidad y jerarquía de fuentes
Método `A-1.2` según `Modelo-JMR/modelo/REGLAS_VIGENTES.md` v27 y `METODO_A_JMR.md`; motor `JMR-valuation` con pruebas del PR203; rama datos PR234. No se importaron cifras R2/R3/R4. Las fuentes primarias son SEC 10-K FY2016–25, 10-Q 2026-09-30, reporte de resultados 29-oct-2026. Toda cifra en Input separa dato SEC, fórmula y juicio. Cualquier corrida futura debe retener SHA de los tres repos, hoja_ID, revision_ID, corte financiero/mercado, versiones de plantilla y hashes de inputs/escenarios.

## 2. Histórico consolidado y puntos de control
| FY | Ventas | EBIT GAAP | CFO | CAPEX cash bruto | ROIC GAAP calculado |
|---|---:|---:|---:|---:|---:|
| 2016 | 135987 | 4186 | 17203 | 7804 | 21,37% |
| 2017 | 177866 | 4106 | 18365 | 11955 | 12,00% |
| 2018 | 232887 | 12421 | 30723 | 13427 | 24,01% |
| 2019 | 280522 | 14541 | 38514 | 16861 | 17,73% |
| 2020 | 386064 | 22899 | 66064 | 40140 | 20,80% |
| 2021 | 469822 | 24879 | 46327 | 61053 | 14,97% |
| 2022 | 513983 | 12248 | 46752 | 63645 | 8,99% |
| 2023 | 574785 | 36852 | 84946 | 52729 | 11,58% |
| 2024 | 637959 | 68593 | 115877 | 82999 | 19,24% |
| 2025 | 716924 | 79975 | 139514 | 131819 | 15,94% |
| LTM sep-26 | 797455 | 104366 | 168300 | 215192 | 13,0740% |
Fuente: `FASE_2_ENTREGA.md` y valores/fórmulas de `Income Statement`, `Balance Sheet`, `Cash Flow Statement`, `Eficiencia de capital`. Total 88/88 conciliaciones aritméticas históricas reportadas F2. Control independiente R5 replicó NOPAT−reinversión y descuentos de los 10 años Base (desvío cero). No significa que todas las 11 filas señaladas por `estados_completos` sean errores.

## 3. Cadena de dependencias (sin volver a capturar manualmente)
- `Income Statement!L3=K3+N3−M3` → `Input sheet!B12` → `Valuation output!B5` → `Valuation output!C5:L5`; crecimiento LTM vs LTM histórico = `797455/691330−1=15,350845%`.
- `Income Statement!L12=K12+N12−M12` → `Input!B13` → EBIT normalizado en `Valuation output!B7` por `R& D converter`, no un EBIT GAAP inventado.
- `Balance Sheet!L35` → `Input!B15`; `Balance Sheet!L20+L21+L25+L26` → `Input!B16` deuda book 304841, incluye arrendamientos y financiación.
- `Cash Flow Statement!L13/L15/L16` → `Input sheet!B160:B164` CFO 168300/CAPEX 215192/incentivos4535/FCF−42357, sin alimentar CAPEX dos veces al FCFF pronosticado.
- `Cost of capital worksheet!B14=E63=Input!B36` por método Detailed/Multibusiness; `Valuation output!C14:L14` interpola tasa hasta 8,99% terminal.
- `Escenarios e historias!C5:G8,N5:N8` y proyección `Valuation output` → cuatro DCF; `Resumen de Valoración` los muestra como DCF HOY, separado de salida FY+3.
- `Sector` alimenta `Crecimiento y Márgenes` y referencias secundarias. Los ratios sectoriales **2,7255** de `Input!B32:B33` son referencias, NO el S/C marginal aplicado: Base **0,72→1,65**. Debe corregirse el panel `Origen de los Supuestos` si visualmente dice lo contrario.
- Cinco múltiplos: `EVEBITDA`, `EVFCFF`, `PE`, `PFCFE`, `POCF`, `Descuento de múltiplos`, `Sensibilidad por múltiplo`, `Resumen`. N/A justificado ≠ cero; la salida FY+3 difiere del VP hoy.

## 4. Supuestos activos Base y cuatro historias
| Parámetro | Conservadora | Base (principal) | Optimista | Disrupción |
|---|---:|---:|---:|---:|
| Crecimiento año1 | 8% | **11%** | 14% | consultar Escenarios C77 |
| Objetivo margen EBIT | 12% | **15,8%** | 18,5% | 8,5% |
| S/C marginal años1–5 | 0,52 | **0,72** | 1,15 | 0,35 |
| S/C marginal años6–10 | 1,25 | **1,65** | 2,10 | 1,05 |
| ROIC terminal | 9,5% | **11,5%** | 15% | 7,5% |
| Valor por acción | 81,0095 | **149,1915** | 241,8435 | 62,4357 |
Los 10 crecimientos y proyecciones de cada historia están en sus filas de `Escenarios e historias` y `Valuation output`; esta tabla no reescribe esos cálculos. Las probabilidades iniciales Base45%, Cons22,5%, Opt22,5%, Disrupción10% se someten a control de ciclo. La disrupción es escenario separado y no entra en promedio ordinario.

## 5. Ecuaciones económicas utilizadas y reconciliaciones explícitas
1. `NOPAT_t = EBIT_ajustado_t × (1−tasa_t)`. FY+1: EBIT128208,219 y tasa25%, NOPAT96156,16425 M.
2. `Reinversión_t = f(Δingresos/S-C marginal, desfase 2 años)` según fórmula nativa, sin añadir sobre ello otro CAPEX histórico. FY+1:121711,569375 M.
3. `FCFF_t=NOPAT_t−reinversión_t`. FY+1 **−25555,405125**; FY+2 **−15679,203406**; FY+3 **−6371,915436**; FY+4 **+4635,98553**; se preserva negatividad durante expansión.
4. `VP(FCFF_1..10)=sum(FCFF_t × DF_t)` con descuentos de `Valuation output!C15:L15`: **321020,81496489746 M** (comprobado segunda vez fuera de fórmulas).
5. `FCFF_terminal = NOPAT_terminal×(1−g/ROIC_terminal)`. Salida reportada **133727,4768103316 M**; `Vterminal=FCFF_terminal/(WACC_terminal−g)=2679909,3549164645 M`.
6. `VPterminal=2679909,3549×DF10=1193803,3375394288 M`; **78,808% EV**.
7. `EV=VPflujos+VPterminal=1514824,1525043263 M`. `Equity=EV−deuda304841−minorías0+caja114226+no_operativos288700−opciones0=1612909,1525043263 M`.
8. `Vprincipal=equity/10811M acciones=149,19148575564947 USD`. `MOS35%=149,19148575564947×0,65=96,97446574117216 USD`. El promedio de historias ≠ valor principal.
9. Chequeos de ROIC: GAAP LTM13,0740%, adjusted LTM15,0919%, año10 13,9267%, terminal11,5%; terminal reinversión/NOPAT 34,7826%.

## 6. Reconciliación temporal y fiscal
El LTM sep2026 usa FY2025 + 9M2026 − 9M2025 para **flujos**; para balance es foto sep2026, apertura sep2025 y deuda/leases al mismo corte. Precios FY históricos están ajustados por split20:1; no confundir EPS original 2016–19 con EPS recalculada. Los impuestos de `Income Statement!H20` y demás están **firmados como gasto negativo/beneficio positivo**; el cotejo SEC inverso sin normalización genera once avisos falsos. No cambiar ambas convenciones ni doblar signos. Faltan pruebas oficiales del cotejo de impuestos, split y fecha de PPE; el auditor SEC mostró 20 avisos (11 impuestos, 8 EPS, 1 PPE). La fórmula fiscal R5 cambió respecto de plantilla, y debe homologarse con test en pérdidas/beneficios antes de adoptarla como estándar.

## 7. Sensibilidades reproducibles con valores del centro
| Shock | DCF Base alternativo US$/acción | Δ vs 149,1915 | Interpretación |
|---|---:|---:|---|
| S/C 0,50 vs 0,72 años1-5 | 128,7214 | −13,72% | Mayor capital para el mismo crecimiento |
| S/C 0,55 | 134,8117 | −9,64% | Contraste CAPEX |
| S/C 0,90 | 158,4961 | +6,24% | Productividad superior |
| WACC +50pb, g4% | 133,4533 | −10,55% | Duración y tasa |
| WACC −50pb, g4% | 168,5132 | +12,95% | Duración y tasa |
| g3,5%, WACC inicial inalterado | 144,9978 | −2,81% | Terminal |
| g4,5% | 154,2876 | +3,42% | Terminal |
| Margen objetivo13,8% | 126,4483 | −15,24% | Composición/escala |
| Margen objetivo17,8% | 171,9347 | +15,24% | Composición/escala |
| ROIC terminal10,5%, g4% | 143,5826 | −3,76% | Foso decreciente |
| ROIC terminal12,5%, g4% | 153,9029 | +3,16% | Foso más durable |
| Nonop participaciones −25% | 142,5149 aproximadamente | −4,48% | Level3, sin impuestos |
| Ventaja desaparece tras 10Y | 132,7485 | −11,02% | Fade ROIC (hoja de duración) |
Las tres matrices nativas `Sensibilidad DCF!A4:G12,A15:G23,A26:G34` tienen centro conciliado en 149,1915. Las pruebas S/C provienen de `NORMALIZACION_CAPEX_Y_JUSTIFICACION_DCF.md`, con restauración de 0,72 confirmada; no se sustituyen supuestos finales con el stress. No sumar estos deltas como si fueran independientes.

## 8. Múltiplos, anclas y estado
- **EV/EBITDA:** cálculo candidato nativo vigente VP Base hoy **341,1023**; diferencia con F1 FY+3 **349,7436** proviene de convención de horizonte/descuento y actualizaciones: comparar campos específicos, no mezclar.
- **P/OCF:** cálculo candidato vigente VP Base hoy **190,4043**; antigua F1 179,1477 y 16,833x no coincide con ancla de 19,6147x de `Supuestos de los Múltiplos`. Reconciliar y versionar documentación; OCF no deduce expansión de CAPEX.
- **EV/FCFF:** FY+3 Base FCFF **−6371,915 M**; no multiplicar flujos negativos por un múltiplo positivo para crear precio.
- **P/FCFE:** flujos negativos o financiación poco comparable impiden usar ancla positiva de forma defendible.
- **P/E:** NI GAAP LTM **134779 M** incluye ganancias Level3 extraordinarias; no disponible earnings normalizado IFRS/GAAP reconciliado; `N/D` pendiente, no rellenar cero.
- **P/S y P/BV:** opcionales, no bloquean.
- **Salida integral secundaria:** `Resumen de Valoración` tiene celdas en blanco para P/E, EV/FCFF y P/FCFE; el ponderado combinado no se debe mostrar como certificado ni equipararse con DCF. Revisar interpretación de `Descuento de múltiplos`: FY+3 no es VP hoy.

## 9. Observaciones de calidad visual antes de lectura del usuario
- `Origen de los Supuestos` enseña S/C sectorial 2,7255 en las tres columnas de escenarios; **no coincide** con `Escenarios e historias` (Cons0,52/1,25, Base0,72/1,65, Optimista1,15/2,10). Debe referenciar las historias activas, manteniendo la referencia sectorial como contraste.
- `Tesis de Inversión y Supuestos` conserva título genérico, campos `[$XX,XX]` y textos de plantilla. No presentarlo como análisis completo hasta actualizarlo o remitir al Nivel1.
- `Supuestos Recomendados` marca tipo de negocio POR CLASIFICAR y el marginal histórico N/D. Es un diagnóstico pendiente, no error de DCF por sí solo.
- `Resumen de Valoración` muestra algunas celdas secundarias FY+3 sin ajustar y otras VP; **resaltar DCF Base** y MOS, precio al corte, y distinguir estado `CANDIDATO`.

## 10. Validaciones y limitaciones declaradas
Pruebas verificadas previamente por GitHub Actions 41609454032: regresión **40/40**; scripts `inputs_completos` (0 faltantes), `auditar_ceros_materiales` (0), `candados` (15/15), `diff_formulas` (no reemplazos por constantes, sí cambios fórmula→fórmula). Persisten **11 filas señaladas** por `estados_completos`, **20 diferencias** sin normalización contable de SEC y falta suite integrada R5. **Ninguna de estas cifras se declara aprobada solo porque el cálculo matemático reproduzca el precio.**

Los controles de publicación y JSON para R5 no están listos: no ejecutar `controles_todas.sh` dirigido al catálogo viejo ni promocionar el PR234. La tarea de análisis F4 **se entrega como borrador** y se debe pasar por revisión visual; F5 económica posterior a indicaciones del usuario, y una auditoría interna preliminar aquí separada. Las operaciones no afectadas pueden continuar sin reextraer estados correctos.

## 11. Referencias y reproducibilidad de lectura
Celdas y scripts: R5 `Valuation output!C4:L16,B18:B35`, `Cost of capital worksheet`, `Input`, `Escenarios`, `Eficiencia de capital`, `Duración ventaja · FCFF`, `Sensibilidad DCF`, `Descuento de múltiplos`. Documentos fuente R5 `FASE_1_ENTREGA.md`, `FASE_2_ENTREGA.md`, `INVENTARIO_ENTRADAS_F1.md`, `NORMALIZACION_CAPEX_Y_JUSTIFICACION_DCF.md`, `CIERRE_TECNICO_F1_F2_20261103.md`, `FASE_3_ENTREGA.md`.

Fuente primaria: [Amazon 10-Q 2026Q3](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm), [release 29-oct-2026](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx). Fuente histórica por tramo en `FASE_2_ENTREGA.md`.
