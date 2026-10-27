**Estado de publicación (2026-10-27): PUBLICADO CON SALVEDADES · revisión CELH-REC-20261027-R1.** Estudio recuperado con corte del 30-sep-2026; sin cambios de supuestos, probabilidades ni pesos. Valoración, análisis fundamental y esta auditoría corresponden a la misma hoja de Google y a la misma revisión.

**Controles ejecutados el 27-oct-2026:** siete múltiplos con fórmula y resultado numérico (`verificar_multiplos_hoja.py`), fórmulas contra la maestra del 22-oct (`audit_master_formulas.py`), consistencia hoja = registro = análisis (`consistencia_migracion.py --hoja`), candados vigentes, probabilidades.

**Salvedades vigentes:**
- Estudio recuperado: precio y corte de información del 30-sep-2026; no incorpora resultados posteriores ni actualiza supuestos.
- Siete múltiplos calculados por las fórmulas originales de la hoja (7/7 con fórmula y resultado numérico; fórmulas de cálculo y múltiplos idénticas a la maestra del 22-oct-2026); P/V y P/BV con peso 0 y estado provisional.
- Candados de la plantilla del 21-oct (Financials Multiples!M34:M36) no aplican a la maestra vigente; se exigen solo los presentes en ella.

---

# Auditoría económica narrativa — Celsius Holdings, Inc. (CELH)

**Análisis fundamental vinculado:** [CELH en la app](https://juanmarobledo.github.io/Modelo-JMR/research.html?ticker=CELH) · registro `analisis/CELH-research-1790597282768-kjm45.json` (revisión del 2026-10-26).

## 1. Ficha de auditoría y alcance

| Campo | Contenido |
|---|---|
| Emisor | Celsius Holdings, Inc.; ticker CELH |
| Mercado, moneda y escala | Nasdaq Global Select Market (EE. UU.); US$ millones salvo por acción |
| Sector | Bebidas energéticas listas para beber (hoja: industria de Damodaran «Beverage (Soft)») |
| Método intrínseco principal | DCF FCFF de la historia Base (compañía operativa); MOS de 35 % sobre ese valor |
| Estados examinados | 10-K 2025 (2-mar-2026) y 10-Q del 2T FY26 (6-ago-2026); LTM = FY2025 + 1S26 − 1S25 (cierre 30-jun-2026) |
| Fecha de valoración / de auditoría | Corte de mercado 30-sep-2026 / 2026-10-26 |
| Precio del análisis | US$27,35 al cierre del 30-sep-2026 (corte común de la cartera); no se obtuvo un precio posterior |
| Hoja auditada | [Modelo JMR CELH](https://docs.google.com/spreadsheets/d/1tHDLsh4yBF9NQkRLNqfTU6GPM5trOWsB5xIjpALLOIw/edit), rehecha desde la maestra el 2026-10-26 |
| Artículo y Nivel 2 | `JMR-valuation/data/CELH_Research_Fundamental_Modelo_JMR_2026-10-26.md` y `CELH_Nivel2_Datos_Modelo_JMR_2026-10-26.md` |
| Registro en la app | Se publica con la autorización general del usuario; sin certificación previa (el usuario audita después) |
| Visto | Hoja completa por lectura; 10-Q del 2T FY26 (páginas R: balance, resultados, flujo, deuda, mezzanine, ingresos y EPS); XBRL companyfacts (variación neta de caja); comunicados del 4T25 y 2T26; Alpha Vantage (precios) |
| Fuera de alcance | 10-K completo (factores de riesgo, litigios, vencimientos); transcripción de la llamada; contrato con PepsiCo; estados de pares; calificaciones crediticias; vigilancia posterior al 26-oct-2026 |
| Estado de verificación | **Con reservas** (no es una auditoría contable). Ver §15 y §17 |

## 2. Resumen ejecutivo y relato económico central

Celsius vende bebidas energéticas con tres marcas (CELSIUS, Alani Nu y Rockstar) distribuidas sobre todo por PepsiCo. En el LTM a junio de 2026 ingresó US$3.047 millones (+21 % sobre el ejercicio 2025; +85,5 % en FY25 por las compras de Alani Nu y Rockstar), con EBIT GAAP de US$160 millones (5,3 %) y EBIT normalizado de ~US$602 millones (19,7 %) tras US$441,6 millones de partidas de una vez, sobre todo la terminación de distribuidores [OBSERVADO: 10-Q del 2T FY26 y comunicados del 4T25 y 2T26].

Lo que cambia: el crecimiento orgánico se agota (2T26: +10,6 % total, CELSIUS −11,7 %, Alani Nu +21 %), el margen bruto baja a 48,1 % por promociones y el balance se carga de capital comprado (marcas US$1.280 millones, plusvalía US$920 millones, costos diferidos de PepsiCo US$747 millones y preferentes de PepsiCo con valor contable de US$1.760 millones y valor de liquidación de US$1.135 millones).

El motor de crecimiento de la Base es la suma de tres cubetas calculadas con la mezcla estimada del LTM: CELSIUS cae 3 % el primer año y luego crece 2-3 %; Alani Nu crece 12 % y se modera a 5 %; Rockstar suma un año completo de ventas y luego declina. El resultado es 5,9 % el primer año y 4,8 % compuesto a cinco años. La ventaja competitiva que sostendría los beneficios es la distribución contratada con PepsiCo (~17 años desde 2025) y la escala de ~20 % de la categoría, no una marca con ciclo completo superado.

**Tesis Base favorable:** Alani Nu sostiene el portafolio, CELSIUS se estabiliza en 2027 y el margen normalizado se mantiene cerca de 20 %: US$24,20 por acción. **Interpretación neutral:** CELSIUS sigue cediendo y las promociones se quedan, con margen de 17 %; la Conservadora (US$16,58, 22,5 %) describe esa ruta. **Contratesis adversa:** la regulación de la cafeína y el fin de la moda de Alani Nu golpean la marca que sostiene el crecimiento (Disrupción, US$5,85, 10,0 %).

El supuesto que domina el valor es la tasa de descuento (±1 punto de WACC mueve la Base US$20,81 (−14,0 %) / US$28,49 (+17,7 %)), seguido por el ROIC terminal igual al costo de capital (sin ventaja competitiva) y el crecimiento de los años 1-5. El precio (US$27,35) queda por encima de la Base (13 %); ver el DCF inverso en §10. Esta narrativa no se deriva del precio: parte de los estados de la compañía.

## 3. Trazabilidad, integridad y jerarquía de evidencia

Inventario de las celdas de entrada de `Input sheet`, `Cost of capital worksheet`, `R& D converter` y `Option value`, y de los datos que la hoja enlaza desde las pestañas de estados (Income Statement, Balance Sheet, Cash Flow Statement; columna L = LTM). `Financials Multiples` no tiene celdas de entrada propias: son fórmulas.

**Conteo:** la tabla tiene **92 filas** (todas las de `Input sheet` con valor, las entradas clave del costo de capital y el conversor de I+D). Las celdas con fórmula por defecto (`Input sheet!B27:B33`) se incluyen porque el analista puede sustituirlas.

**Cómo se cargaron los estados.** (a) El importador de la SEC (`desde_cero.sh datos`) cargó diez ejercicios (2016-2025) y el LTM desde los XBRL; (b) la auditoría de estados contra la SEC corrigió 8 celdas (totales del LTM); (c) `scripts/celh_datos_cero.py` reescribió el balance LTM y el de diciembre de 2025 con el 10-Q (marcas e intangibles, costos diferidos, otros pasivos), agregó las preferentes de PepsiCo al patrimonio total de 2022 en adelante (US$824,5 millones hasta 2024 y US$1.759,975 millones desde 2025), aplicó el split 3 por 1 de nov-2023 a las acciones de 2016-2022, fijó 255,184 millones de acciones, cargó los compromisos de arrendamientos del 10-K y las entradas del costo de capital; (d) la variación neta de caja de 2021-2025 se tomó del XBRL y la del LTM se calculó (−350,203 + 93,142 + 274,957 = 17,896); (e) las preferentes entran al TEV histórico a valor de liquidación; (f) la hoja se restauró con las fórmulas de la maestra tras cada carga.

**Diferencias de fuente y ajustes:** (a) acciones: 253,035 M de la portada del 10-Q más 2,149 M de RSU/PSU sin consolidar = 255,184 M, frente a 253,341 M en el balance; (b) deuda: valor en libros neto de descuento (US$674,9 M) más arrendamientos (US$17,4 M) frente a US$694,75 M nominales; (c) el EBIT base es el GAAP (160,3) y la normalización de US$441,6 M se aplica al margen del año 1 (`Input sheet!B28` = 19,6 %), porque la plantilla unificada no permite editar `B13`; (d) la tasa efectiva usada es 20,1 % (1S26), no el 8,8 % del LTM; (e) el patrimonio de la hoja incluye las preferentes (el balance publicado las muestra fuera del patrimonio).

| # | Pestaña | Celda | Rótulo | Valor | Tipo | Documento/fuente (URL en §18) | Quién lo aportó | Verificación |
|---:|---|---|---|---|---|---|---|---|
| 1 | Input sheet | B1 | Celsius Holdings, Inc. (NASDAQ:CELH) | Celsius Holdings, Inc. (NASDAQ:CELH) | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 2 | Input sheet | B4 | Date of valuation | sept-26 | Juicio | Corte de mercado 30-sep-2026 (fecha de valoración) | Corte común | [OBSERVADO] |
| 3 | Input sheet | B5 | Company name | Celsius Holdings, Inc. | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 4 | Input sheet | B8 | Country of incorporation | United States | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 5 | Input sheet | B9 | Industry (US) | Beverage (Soft) | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 6 | Input sheet | B10 | Industry (Global) | Beverage (Soft) | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 7 | Input sheet | B12 | Revenues | $ 3.047,30 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 8 | Input sheet | B13 | Operating income or EBIT | $ 160,30 | Cálculo | Enlace a Income Statement!L12 (EBIT GAAP 160,3); la normalización de 441,6 va en B28 | Hoja | Coincide con el 10-Q [OBSERVADO] |
| 9 | Input sheet | B14 | Interest expense | $ 54,30 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 10 | Input sheet | B15 | Book value of equity | $ 2.959,56 | Cálculo | Patrimonio total del balance (incluye las preferentes en mezzanine: 1.759,975) | Hoja (Balance Sheet!L35) | Recalculado [OBSERVADO] |
| 11 | Input sheet | B16 | Book value of debt | $ 674,85 | Cálculo | Deuda corriente 7,0 + largo plazo neto 667,85 (10-Q 2T26, nota de deuda); nominal 694,75 | Hoja | Diferencia de 19,9 por descuento; ver H-06 |
| 12 | Input sheet | B17 | Do you have R&D expenses to capitalize? | No | Juicio | Capitalización de I+D según la regla del sector de la empresa | IA | Decisión de método; ver hallazgos |
| 13 | Input sheet | B18 | Do you have operating lease commitments? | Yes | Juicio | Arrendamientos operativos como deuda (conversor de Damodaran) | IA | [MODELO] |
| 14 | Input sheet | B19 | Cash and Marketable Securities | $ 631,23 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 15 | Input sheet | B20 | Valor económico validado de participaciones y activos NO ope | $ - | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 16 | Input sheet | B21 | Minority interests | $ - | Dato | Sin participaciones minoritarias relevantes | IA | [NO VERIFICADO] en la nota de patrimonio |
| 17 | Input sheet | B22 | Number of shares outstanding = | 255,18 | Cálculo | Acciones de la hoja: 253,035 M de la portada + 2,149 M de RSU/PSU | Hoja (Income Statement!L27) | Coincide con el 10-Q [OBSERVADO] |
| 18 | Input sheet | B23 | Current stock price = | $ 27,35 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 19 | Input sheet | B24 | Effective tax rate = | 8,83% | Cálculo | Tasa efectiva LTM de la hoja; la proyección usa B90 (20,1 %) | Hoja | Distorsionada por partidas de una vez; ver B90 |
| 20 | Input sheet | B25 | Marginal tax rate = | 25,00% | Juicio | Tasa marginal federal más estatal de EE. UU. (25 %) | Plantilla/IA | Convención del modelo [MODELO] |
| 21 | Input sheet | B27 | Revenue growth rate for next year  | 5,90% | Juicio | Crecimiento del año 1 de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 22 | Input sheet | B28 | Operating Margin for next year | 19,60% | Juicio | Margen operativo del año 1 de la Base: 19,6 % (EBIT normalizado US$601,9 M + ajuste de arrendamientos / ventas) | IA (ficha de historias) | [HIPÓTESIS]; ver H-01 |
| 23 | Input sheet | B29 | Compounded annual revenue growth rate - years 2-5 = | 4,50% | Juicio | CAGR de los años 2-5 de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 24 | Input sheet | B30 | Referencia de margen objetivo (mediana histórica/sectorial;  | 20,10% | Juicio | Margen objetivo de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 25 | Input sheet | B31 | Year of convergence for margin | 5,00 | Juicio | Año de convergencia del margen: 5 | Plantilla/IA | Coherente con las historias |
| 26 | Input sheet | B32 | Sales to capital ratio  (for years 1-5) | 1,78 | Juicio | Ventas/capital años 1-5 (ficha de historias, ajustado por el conversor de arrendamientos) | IA | [HIPÓTESIS]; ver hallazgos |
| 27 | Input sheet | B33 | Sales to capital ratio (for years 6-10) | 1,59 | Juicio | Ventas/capital años 6-10 (ficha de historias, ajustado por el conversor de arrendamientos) | IA | [HIPÓTESIS]; ver hallazgos |
| 28 | Input sheet | B35 | Riskfree rate | 5,29% | Dato | Treasury a 10 años del corte común (30-sep-2026): 5,29 % | Corte común (datos_mercado.py) | [OBSERVADO] FRED DGS10 |
| 29 | Input sheet | B36 | Initial cost of capital = | 7,05% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 30 | Input sheet | B38 | Do you have employee options outstanding? | Yes | Dato | Opciones de empleados: 2,313 M con precio de ejercicio US$6,28, vida 3,96 años, volatilidad 60 % | IA (10-Q 2T26, nota de compensación) | Valor de las opciones US$52 M; [NO VERIFICADO] en la nota |
| 31 | Input sheet | B39 | Number of options outstanding = | 2,31 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 32 | Input sheet | B40 | Average strike price = | $6,28 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 33 | Input sheet | B41 | Average maturity = | 3,96 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 34 | Input sheet | B42 | Standard deviation on stock price = | 60,00% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 35 | Input sheet | B46 | Do you want to override this assumption = | No | Juicio | No se anula el WACC terminal: converge a la fórmula de la plantilla | Plantilla | [MODELO] |
| 36 | Input sheet | B47 | If yes, enter the cost of capital after year 10 = | 7,05% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 37 | Input sheet | B49 | Do you want to override this assumption = | No | Juicio | Anulación del ROIC terminal (Yes) o ROIC terminal igual al costo de capital (No) | IA | Ver hallazgos de ROIC terminal |
| 38 | Input sheet | B50 | If yes, enter the return on capital you expect after year 10 | 15,00% | Juicio | ROIC terminal de la historia Base si B49 = Yes | IA | [HIPÓTESIS] |
| 39 | Input sheet | B52 | Do you want to override this assumption = | No | Juicio | Sin probabilidad de fracaso en la Base | IA | [INFERENCIA] |
| 40 | Input sheet | B53 | If yes, enter the probability of failure = | 0% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 41 | Input sheet | B54 | What do you want to tie your proceeds in failure to? | V | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 42 | Input sheet | B55 | Enter the distress proceeds as percentage of book or fair va | 50% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 43 | Input sheet | B57 | Do you want override this assumption = | No | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 44 | Input sheet | B58 | If yes, enter a different lag (0 = no lag to 3 = lag of 3 ye | 1 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 45 | Input sheet | B60 | Do you want to override this assumption = | No | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 46 | Input sheet | B62 | Do you want to override this assumption = | No | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 47 | Input sheet | B65 | Do you want to override this assumption = | No | Juicio | No se anula la tasa libre después del año 10 | IA | — |
| 48 | Input sheet | B66 | If yes, enter the riskfree rate after year 10 | 5,29% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 49 | Input sheet | B68 | Do you want to override this assumption = | Yes | Juicio | Se anula el crecimiento perpetuo con la regla del modelo | IA | Ver B69 |
| 50 | Input sheet | B69 | If yes, enter the growth rate in perpetuity | 4,00% | Juicio | Crecimiento terminal 4,00 % (≤ tasa libre de 5,29 %) | Regla vigente del modelo | [MODELO] |
| 51 | Input sheet | B71 | Do you want to override this assumption | No | Juicio | Sin efectivo atrapado | IA | [NO VERIFICADO] |
| 52 | Input sheet | B72 | If yes, enter trapped cash (if taxes) or entire balance (if  | $0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 53 | Input sheet | B73 | & Average tax rate of the foreign markets where the cash is  | 0% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 54 | Input sheet | B76 | Valor de acciones preferentes (misma unidad del DCF) | 1135 | Dato | Preferentes de PepsiCo a valor de liquidación: Serie A US$550 M + Serie B US$585 M (10-Q 2T26) | IA | Coincide con el 10-Q [OBSERVADO]; ver H-02 |
| 55 | Input sheet | B78 | PV del conversor ya incluido en deuda del balance (solapamie | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 56 | Input sheet | B79 | Pasivo de arrendamientos INCREMENTAL no reconocido | $ 17,35 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 57 | Input sheet | B80 | Ajuste de EBIT atribuible a pasivos incrementales | 2,8077177 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 58 | Input sheet | B81 | Estado de conciliación de arrendamientos | CONCILIADO | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 59 | Input sheet | B82 | Inversiones a largo plazo según balance (dato histórico; NO  | $0 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 60 | Input sheet | B83 | Valor CONTABLE de inversiones excluidas del capital operativ | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 61 | Input sheet | B84 | Valor ECONÓMICO atribuible de participaciones y activos no o | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 62 | Input sheet | B85 | Control de inversiones y doble contabilización | VALIDADO | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 63 | Input sheet | B86 | Revisión: no están incluidas en EBIT/FCFF ni duplicadas | Sin solapamiento | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 64 | Input sheet | B87 | Fuente y conciliación de inversiones no operativas | 10-Q 2T FY26: sin inversiones financieras relevantes; se com | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 65 | Input sheet | B89 | Método fiscal de proyección (obligatorio en cada copia) | Normalizada | Juicio | Método fiscal normalizado | IA | — |
| 66 | Input sheet | B90 | Tasa inicial NORMALIZADA (solo si B89=Normalizada) | 0,201 | Juicio | Tasa efectiva del 1S26 (41,674/207,066 = 20,1 %), que converge a la marginal de 25 % | IA | [OBSERVADO] 10-Q |
| 67 | Input sheet | B91 | Fuente / conciliación de impuesto efectivo vs marginal | Tasa efectiva: 20,1 % en el 1S26 (41,674/207,066), 13,6 % en | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 68 | Input sheet | B92 | Control de hipótesis fiscales | VALIDADO | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 69 | Input sheet | B93 | Impuesto inicial para pronóstico (no altera la tasa históric | 0,201 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 70 | Input sheet | B96 | Tasa libre de riesgo nominal de largo plazo · misma moneda d | 5,29% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 71 | Input sheet | B97 | WACC terminal efectivo del modelo (independiente del DCF hab | 8,99% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 72 | Input sheet | B98 | Base | Sin liberación | Juicio | Sin liberación de capital en contracción (reinversión negativa se trunca a cero) | IA | Regla de Damodaran |
| 73 | Input sheet | B99 | Conservadora | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 74 | Input sheet | B100 | Disrupción | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 75 | Input sheet | B101 | Optimista | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 76 | Cost of capital worksheet | B12 | Which approach will you be using? | Detailed | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 77 | Cost of capital worksheet | B22 | Approach for estimating beta | Single Business(US) | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 78 | Cost of capital worksheet | B26 | What approach do you want to use to input ERP? | Operating regions | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 79 | Cost of capital worksheet | B33 | Average Maturity = | 5,75 | Juicio | Vencimiento medio de la deuda: 5,75 años (préstamo a plazo con vencimiento en 2032) | IA | [OBSERVADO] 10-Q |
| 80 | Cost of capital worksheet | B34 | Approach for estimating pre-tax cost of debt | Direct input | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 81 | Cost of capital worksheet | B35 | If direct input, input the pre-tax cost of debt | 6,500% | Juicio | Costo de la deuda 6,5 %: SOFR + 2,25 % tras la enmienda del 15-jul-2026; intereses del 2T26 anualizados ≈ 6,7 % | IA | [OBSERVADO] 8-K del 15-jul-2026 |
| 82 | Cost of capital worksheet | B41 | Book Value of Convertible Debt = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 83 | Cost of capital worksheet | B49 | Number of Preferred Shares = | 1,856666 | Dato | 1,856666 M de acciones preferentes (1.466.666 + 390.000) | IA (10-Q 2T26) | Coincide [OBSERVADO] |
| 84 | Cost of capital worksheet | B50 | Current Market Price per Share= | 611,31 | Dato | Precio por acción preferente = valor de liquidación (US$1.135 M / 1,857 M) | IA | Coincide con Input B76 |
| 85 | Cost of capital worksheet | B51 | Annual Dividend per Share = | 30,32 | Dato | Dividendo en efectivo anual por acción preferente: US$56,3 M / 1,857 M | IA (10-Q 2T26) | [OBSERVADO] |
| 86 | Cost of capital worksheet | H6 | Ingresos H6 | $2.423 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 87 | Cost of capital worksheet | H17 | Ingresos H17 | 92,8 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 88 | Cost of capital worksheet | H29 | Ingresos H29 | $2.423 | Dato | Ventas de 2025 en Norteamérica: 2.422,5 (10-K 2025) | IA | Coincide [OBSERVADO] |
| 89 | Cost of capital worksheet | H30 | Ingresos H30 | 72,5 | Dato | Ventas de 2025 en Europa: 72,5 (10-K 2025) | IA | Coincide [OBSERVADO] |
| 90 | Cost of capital worksheet | H32 | Ingresos H32 | $7 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 91 | Cost of capital worksheet | H37 | Ingresos H37 |  $ 3.047,30  | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 92 | R& D converter | F7 | Años de amortización del I+D | 3 | Juicio | Convención de Damodaran para la industria | IA | [MODELO] |

**Jerarquía de evidencia usada:** [OBSERVADO] (documento de la compañía o comprobación directa), [INFERENCIA] (deducción de lo observado), [HIPÓTESIS] (supuesto del analista), [MODELO] (resultado de las fórmulas) y [NO VERIFICADO].

## 4. Historia financiera: diez años y punto de partida

| US$ millones | Dec '20 | Dec '22 | Dec '23 | Dec '24 | Dec '25 | LTM |
|---|---:|---:|---:|---:|---:|---:|
| Ingresos | 131 | 654 | 1.318 | 1.356 | 2.515 | 3.047 |
| EBIT | 8 | -158 | 266 | 156 | 141 | 160 |
| Margen operativo | 6,0 % | -24,1 % | 20,2 % | 11,5 % | 5,6 % | 5,3 % |
| Flujo operativo | 3 | 108 | 141 | 263 | 359 | 509 |
| Capex | -1 | -8 | -17 | -23 | -36 | -46 |
| Capex / ventas | 0,5 % | 1,3 % | 1,3 % | 1,7 % | 1,4 % | 1,5 % |

La historia tiene tres fases. De 2016 a 2022 Celsius perdió dinero o ganó poco mientras escalaba con un distribuidor nuevo (PepsiCo desde 2022). En 2023-2024 llegó a un margen operativo de 11-20 % con capex mínimo. En 2025-2026 las compras de Alani Nu (abr-2025) y Rockstar (ago-2025) multiplicaron el balance (activo de US$1.767 millones a US$5.120 millones) y llenaron la utilidad de cargos de una vez. El punto de partida de la valoración (LTM a junio de 2026) no es un año representativo: el EBIT GAAP de US$160 millones esconde ~US$442 millones de partidas no recurrentes, y el flujo operativo de US$509 millones está inflado por ingresos diferidos de PepsiCo (+US$330 millones).

Comparabilidad: el crecimiento de 2025 (+85,5 %) y del LTM incluye adquisiciones y no es orgánico; la marca CELSIUS creció 7,5 % en 2025. Las acciones de 2016-2022 se ajustaron por el split de 3 por 1 (nov-2023); el XBRL las trae sin ajustar.

## 5. Crecimiento de ingresos: de la historia a la proyección

La Base construye el ingreso por cubeta (Celsius US$1.425 millones; Alani Nu US$1.433 millones; Rockstar US$189 millones). El resultado consolidado es 5,9 %, 5,2 %, 5,0 %, 4,1 %, 3,7 % en los años 1-5 (4,8 % compuesto) y cae a 4,0 % en el año 10: ingresos de 3.852 millones en el año 5 y 4.662 millones en el año 10.

Por qué ese ritmo: [INFERENCIA] el primer año de la Base (5,9 %) supone un año completo de Rockstar (+27 % anualizado) y un CELSIUS en −3 % (el 3T26 parecido al 2T26 y recuperación al cierre de 2026, como espera la gerencia según un resumen de la llamada del 6-ago-2026); [HIPÓTESIS] Alani Nu factura +12 % en el año 1, por debajo del consumo (+55,7 % en el 2T26) por el cambio de canal y la base alta del 4T25. La categoría vendió US$28.100 millones en 52 semanas a abril de 2026 (+15 %), pero Monster reporta una desaceleración a +7 % en 13 semanas a julio de 2026. La distribución por marca del LTM (CELSIUS 1.425, Alani Nu 1.433, Rockstar 189) es una estimación con el 1S26 y el 4T25 (H-05). No se proyectan compras nuevas.

Alternativas: la Conservadora (0,7 % compuesto, año 1 de 2,3 %); la Optimista (9,2 %, año 1 de 13,1 %); la Disrupción (-7,1 %, con crecimiento terminal de 0 %). Los porcentajes son juicio del analista, no una guía publicada por la compañía.

## 6. Márgenes operativos y normalización de beneficios

La Base lleva el margen de 19,6 % en el año 1 a 20,1 % en el año 5 (ya ajustado por I+D capitalizado y arrendamientos; en base reportada 20,0 %). La Conservadora llega a 17,1 % (17,0 % reportado), la Disrupción a 12,1 % y la Optimista a 23,6 % (23,5 % reportado). Tasa impositiva: 20,1 % al inicio, convergiendo a la marginal de 25 % en el año 10.

Por qué ese margen: [OBSERVADO] el margen normalizado del 2T26 fue 19,6 % (EBIT sin terminación de distribuidores, compras e integración) y el EBITDA ajustado que reporta la compañía es 22,5 %, pero este último excluye la compensación en acciones (1,3 % de las ventas), que aquí se trata como costo. [HIPÓTESIS] la Base lo mantiene cerca de 20 % porque la escala en gastos generales compensa promociones más altas; la Conservadora lo deja en 17 % (promociones permanentes), la Disrupción cae a 12 % y la Optimista llega a 23,5 %. El acuerdo legal de US$24,6 millones del 1T26 NO se suma: Celsius registró US$54,0 millones en 2024 y tiene litigios abiertos. Riesgo: el margen bruto bajó de 51,5 % a 48,1 % en un año, mientras Monster subió precios (H-01).

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

La reinversión de la Base es de 95 millones en el año 1 (frente a un NOPAT de 505 millones) y el FCFF del año 1 es de 411 millones. El ventas/capital es 1,78 en los años 1-5 y 1,59 en los 6-10 (base de la hoja, que incluye I+D y arrendamientos cuando la empresa los capitaliza). Con ±20 % en el ancla, el DCF Base va de US$23,56 (−2,7 %) a US$24,63 (+1,8 %). ROIC terminal: Base 9,0 %, Conservadora 9,0 %, Disrupción 9,0 %, Optimista 9,0 %.

Evidencia: la rotación del capital invertido pasó de 4,1 veces (2024) a 1,0 vez (LTM) por las compras; el ventas/capital marginal histórico es poco informativo porque el capital creció por adquisiciones. La Base usa 1,78 y 1,59 (base ajustada de la hoja): el capital nuevo rinde 23-32 % después de impuestos según la hoja, más del doble del ROIC terminal de 9 % (H-03). Con ±20 % en el ancla de ventas/capital el valor se mueve poco porque el valor terminal depende del ROIC terminal.

Asignación de capital: Alani Nu costó US$2.055,6 millones (~10 % de retorno después de impuestos sobre lo pagado), Rockstar y la capitanía US$935,8 millones en preferentes; en el 1S26 se recompraron 4,0 millones de acciones por US$125,5 millones (a US$31,38) y se pagaron US$28,1 millones de dividendos preferentes.

## 8. Costo del capital y riesgo

Tasa libre de riesgo 5,29 % (Treasury a 10 años al 30-sep-2026), prima de riesgo de 3,74 % (ponderada por regiones de ingresos), beta desapalancada del sector 0,58 y beta apalancada 0,62 (propuesta bottom-up 0,63). WACC inicial 7,05 %; WACC terminal 8,99 %.

Dudas: (i) la beta del sector de bebidas no alcohólicas (0,58 desapalancada) es baja para una empresa de una categoría, un distribuidor y una marca dominante; los riesgos propios están en las historias Conservadora y Disrupción, no en la tasa; (ii) 96 % de las ventas en EE. UU., así que la prima por regiones (3,74 %) es casi la de EE. UU.; (iii) las preferentes (US$1.135 millones, 12,9 % del capital) entran al WACC con su costo en efectivo de 5,0 %, bajo el costo de capital propio; (iv) el costo de la deuda (6,5 %) es el del préstamo, sin calificación pública verificada.

Efecto: ±1 punto de WACC mueve la Base US$20,81 (−14,0 %) / US$28,49 (+17,7 %), el supuesto de mayor peso. La plantilla hace converger el WACC de 7,05 % a 8,99 % en el año 10 (convención de Damodaran).

## 9. Convergencia y valor terminal

El valor terminal es 52,5 % del valor de los activos operativos de la Base (3.897 millones de 7.424 millones). Crecimiento terminal 4,00 % (≤ la tasa libre), ROIC terminal 9,0 % y WACC terminal 8,99 %. Con −0,5 puntos de crecimiento terminal la Base vale US$23,99 (−0,9 %); con +0,5 puntos, US$24,42 (+0,9 %).

Riesgos: (i) las cuatro historias suponen ROIC terminal igual al costo de capital (9 %), es decir, ninguna ventaja competitiva duradera; si Celsius conservara retornos excedentes (la hoja calcula un ROIC del año base de ~15 %), la Base valdría más; (ii) 4 % de crecimiento nominal perpetuo es exigente para una marca de moda; (iii) la Disrupción se estabiliza en 0 % de crecimiento sin liberar capital, una convención y no una predicción. El valor del terminal es el 52 % del valor de los activos operativos, menos que en empresas con ROIC terminal alto.

## 10. Validación independiente del valor intrínseco

Comprobación 1 (identidad): la hoja y el motor independiente del repositorio coinciden en las cuatro historias (Base 24,20; Conservadora 16,58; Disrupción 5,85; Optimista 35,95), lo que valida la aritmética, no la economía. Comprobación 2 (puente): activos operativos 7.424 + caja 631 − deuda con arrendamientos 692 − opciones 52 − preferentes 1.135 + no operativos 0 = patrimonio común de 6.176 millones, o US$24,20 por acción con 255,2 millones de acciones. Comprobación 3 (DCF inverso del Nivel 2, margen → crecimiento anual de los años 1-5 que justifica el precio):

| Beta | Margen | Crecimiento anual de los años 1-5 que justifica el precio | Fracción de empresas de este tamaño que lo logra |
|---|---:|---:|---:|
| 0,62 | 17,1% | 10,9% | 32,2% |
| 0,62 | 20,1% | 7,1% | 53,6% |
| 0,62 | 23,6% | 3,6% | 75,9% |
| 0,63 | 17,1% | 11,0% | 32,1% |
| 0,63 | 20,1% | 7,1% | 53,4% |
| 0,63 | 23,6% | 3,6% | 75,8% |

Comprobación 4 (múltiplos propios): el P/E del LTM es 54 veces y el EV/EBITDA 35 veces, inflados por el EBIT GAAP deprimido; los múltiplos de salida de la Base (17,3× EV/EBITDA y 22,9× P/E) se apoyan en el cierre de 2024, el único con crecimiento de un dígito. Comprobación 5 (retornos): el EBIT normalizado de US$602 millones sobre un valor de empresa de ~US$8.200 millones (con preferentes) da un rendimiento de 7,4 %, algo por encima del WACC de 7,05 %: el mercado descuenta una Base moderada, sin crecimiento extraordinario.

## 11. Cuatro historias y probabilidades

| Historia | Probabilidad | CAGR 1-5 | Margen objetivo (ajustado / reportado) | ROIC terminal | g terminal | DCF por acción |
|---|---:|---:|---:|---:|---:|---:|
| Base · Alani Nu sostiene un portafolio que crece algo menos que la categoría | 45,0 % | 4,8 % | 20,1 % / 20,0 % | 9,0 % | 4,0 % | US$24,20 |
| Conservadora · CELSIUS sigue cediendo y las promociones se quedan | 22,5 % | 0,7 % | 17,1 % / 17,0 % | 9,0 % | 4,0 % | US$16,58 |
| Disrupción · Deterioro de los fundamentales | 10,0 % | -7,1 % | 12,1 % / 12,0 % | 9,0 % | 0,0 % | US$5,85 |
| Optimista · Plataforma multimarca con PepsiCo y exterior | 22,5 % | 9,2 % | 23,6 % / 23,5 % | 9,0 % | 4,0 % | US$35,95 |

Las probabilidades salen de la regla del ciclo (crecimiento_maduro) y no se ajustaron por indicadores: son un juicio condicional, no frecuencias observadas. El DCF esperado de las tres historias activas (pesos renormalizados) es US$25,23; con MOS de 35 % sobre el DCF Base el precio de compra es US$15,73. Cambiar los pesos cambia el esperado, no el DCF Base.

### ¿Qué pasaría si todo fallara?

Si CELSIUS sigue cediendo y Alani Nu madura antes (margen de 17 %), la acción vale la Conservadora; si además la regulación y el fin de la moda frenan a Alani Nu (ventas −7 % anual y margen de 12 %), vale la Disrupción. En ambos casos el balance (caja de US$631 millones, deuda neta casi nula) no está en riesgo inmediato, pero las preferentes (US$1.135 millones) y el préstamo (US$695 millones) absorben una parte creciente del valor de la empresa. El camino contrario, hasta la Optimista, vale US$35,95. El precio de US$27,35 queda entre la Base y la Optimista.

## 12. Valoración por múltiplos: prueba independiente y secundaria

Siete métodos (EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF, P/V y P/BV; los dos últimos con peso cero). Regla del 18-oct-2026: el múltiplo de cada escenario es el que la empresa tuvo cuando crecía como el escenario espera en FY+3 (Conservador 0,2 %, Base 5,0 %, Optimista 9,2 %), llevado al costo de capital del corte y limitado por el múltiplo justificado por los fundamentos de la misma historia; los comparables solo comprueban.

| Método | Mediana histórica 10a | Actual (LTM) | Ancla de peers (mediana) | Justificado Base | Peso en múltiplos |
|---|---:|---:|---:|---:|---:|
| EV/EBITDA | 46,11× | 41,35× | 19,56× | 17,29× | 33 % |
| EV/FCFF | 59,82× | 17,63× | 23,90× | 26,45× | 17 % |
| P/E | 50,03× | 54,00× | 27,38× | 22,93× | 33 % |
| P/FCFE | 57,96× | 15,08× | 21,85× | 28,35× | 8 % |
| P/OCF | 53,08× | 13,72× | 19,20× | 26,11× | 8 % |

Resultado: múltiplos consolidados de US$27,35 (Conservador), US$38,42 (Base) y US$45,28 (Optimista), frente a DCF de US$16,58, US$24,20 y US$35,95. Decisión del 26-oct-2026: se mantiene el DCF Base con MOS de 35 %. Los múltiplos del ciclo se apoyan en un solo cierre comparable (2024); el TEV de la hoja no suma las preferentes de PepsiCo (US$1.135 M).

La brecha entre los múltiplos de la Base y el DCF (+59 %) viene de tres cosas: el margen normalizado se aplica a las razones de 2024, el DCF supone ROIC terminal igual al costo de capital y el ciclo se apoya en un solo cierre comparable. Los saltos frente al múltiplo actual de EV/FCFF, P/FCFE y P/OCF se justifican porque el flujo del LTM está inflado por capital de trabajo (H-08). El TEV de la hoja incluye las preferentes a valor de liquidación desde agosto de 2022. Los peers (Monster, Keurig Dr Pepper, Coca-Cola, PepsiCo, Coca-Cola Consolidated y National Beverage) solo comprueban.

## 13. Sensibilidades económicas y escenarios alternativos

| Supuesto cambiado (DCF Base US$24,20) | Valor |
|---|---:|
| WACC +1 pp / −1 pp | US$20,81 (−14,0 %) / US$28,49 (+17,7 %) |
| Crecimiento años 1-5 −2 pp / +2 pp | US$21,82 (−9,8 %) / US$26,82 (+10,8 %) |
| Margen objetivo −2 pp / +2 pp | US$21,45 (−11,4 %) / US$26,96 (+11,4 %) |
| Crecimiento terminal −0,5 pp / +0,5 pp | US$23,99 (−0,9 %) / US$24,42 (+0,9 %) |
| Ventas/capital −20 % / +20 % | US$23,56 (−2,7 %) / US$24,63 (+1,8 %) |

Ordenado por impacto, la tasa de descuento (±1 punto: −14 % / +18 %), el crecimiento de los años 1-5 y el margen objetivo (±2 puntos: ~±10-11 %) pesan más que el ventas/capital y el crecimiento terminal. La matriz de crecimiento por margen del Nivel 2 recoge el rango completo.

## 14. Coherencia de hojas, cálculos y presentación

La hoja está unificada con la maestra (61 pestañas en el mismo orden, 21.258 fórmulas intactas, 122 selectores idénticos) y el motor independiente reproduce las cuatro historias. Controles: candados 15/15, inputs completos, estados completos e integridad de hojas (registro en la bitácora de la sesión).

Intervenciones sobre la hoja que el lector debe conocer: (i) se restauraron las fórmulas de la maestra tras cada carga; (ii) el importador traía el balance de diciembre de 2025 en parte del LTM y se reescribió con el 10-Q de junio de 2026; (iii) los totales de patrimonio de 2022-2025 incluyen las preferentes para que el balance cuadre; (iv) para unificar se redujo la pestaña «Tesis de Inversión y Supuestos» a 120 × 8 columnas, eliminando el texto de la regla por ciclo que `apply_multiples_v3.py` escribe en las columnas I:J (el texto está en `reference/multiplos_v3/CELH_decision.json`); (v) los márgenes y crecimientos del año 1 se cargan en `Input sheet!B27:B30`, las entradas con defecto de la plantilla.

## 15. Hallazgos priorizados y propuestas de corrección

| ID | Severidad | Hallazgo | Impacto | Propuesta |
|---|---|---|---|---|
| H-01 | Alta | El margen del año 1 parte de 19,6 % (EBIT normalizado) y no del 5,3 % GAAP; la normalización de US$441,6 M depende de aceptar que los cargos no se repiten | Sin ella el DCF Base sería mucho menor; los litigios sí se repiten (US$54,0 M en 2024, US$24,6 M en 2026) | Confirmar con el 10-K completo qué parte de la terminación de distribuidores es reembolsada por PepsiCo y reconciliar el EBIT normalizado |
| H-02 | Media | Las preferentes de PepsiCo se deducen a valor de liquidación (US$1.135 M) y no a valor contable (US$1.760 M) | A valor contable la Base bajaría ~US$2,5 por acción | Leer los términos de conversión y redención del 10-K y valorarlas como deuda híbrida con la opción de conversión |
| H-03 | Alta | Ventas/capital de 1,78 y 1,59 implican que el capital nuevo rinde 23-32 %, más del doble del ROIC terminal (9 %) | Posible sobrevaloración del flujo de los años 1-10 si el crecimiento exige más capital | Calcular el ventas/capital marginal orgánico (sin compras) y probar valores menores en los años 1-5 |
| H-04 | Alta | ROIC terminal igual al costo de capital en las cuatro historias (sin ventaja competitiva) | Si se conservara un ROIC excedente la Base valdría más; con la hipótesis actual es conservadora | Revisar la persistencia de márgenes de Monster y Celsius para justificar o no un ROIC terminal mayor |
| H-05 | Media | La distribución por marca del LTM (CELSIUS 1.425, Alani Nu 1.433, Rockstar 189) es una estimación | Cambia el peso de cada cubeta en el primer año | Obtener los ingresos por marca del 3T25 y 4T25 de los comunicados |
| H-06 | Baja | La hoja usa la deuda en libros (US$674,9 M) y no el nominal (US$694,75 M) | US$0,08 por acción | Sumar el descuento de emisión si el usuario lo prefiere |
| H-07 | Media | Las acciones (255,184 M) suponen 2,149 M de RSU/PSU y 2,313 M de opciones valoradas aparte (US$52 M); no se proyectan recompras | ±5 % de acciones: ∓4,8 % del valor | Revisar el conteo con el 10-Q del 3T26 |
| H-08 | Media | El flujo libre del LTM (US$463 M) está inflado por ingresos diferidos de PepsiCo (+US$330 M) y promociones devengadas; los múltiplos de flujo del LTM son bajos por eso | Los saltos del múltiplo Base frente al actual en EV/FCFF, P/FCFE y P/OCF dependen de esta lectura | Normalizar el flujo con capital de trabajo estable |
| H-09 | Media | PepsiCo es cliente (~60 % de las ventas), distribuidor, tenedor de preferentes y parte relacionada; el contrato no se releyó | Riesgo de renegociación o de prioridad de otras marcas | Leer el acuerdo de distribución y el de la capitanía |
| H-10 | Media | Beta del sector (0,58) y prima por regiones casi de EE. UU. (3,74 %) para una empresa de categoría única | +0,1 de beta ≈ +0,4 pp de costo del patrimonio | Probar una beta mayor como sensibilidad |
| H-11 | Media | Investigación del fiscal de Texas y demandas colectivas sobre Alani Nu sin cuantificar | Riesgo de la marca que sostiene el crecimiento (Disrupción) | Seguir el avance y ajustar la probabilidad de la Disrupción |
| H-12 | Baja | Se eliminó el texto de la regla por ciclo de la pestaña «Tesis de Inversión y Supuestos» (columnas I:J) para unificar la hoja | Pérdida de una nota de presentación; la regla está en el JSON de decisión | Mantener la regla en el artículo (sección 12) |
| H-13 | Baja | La variación neta de caja de 2021-2025 proviene del XBRL y la del LTM es calculada; las acciones de 2016-2022 se ajustaron por el split de 3 por 1 | Presentación de estados históricos | Verificar contra los 10-K de 2021-2023 si se necesitan ratios históricos finos |

## 16. Catalizadores, señales de refutación y seguimiento

| Indicador | Último dato | Confirma Base u Optimista | Favorece Conservadora o Disrupción |
|---|---|---|---|
| Ventas al consumidor de CELSIUS (Circana/Nielsen) | −2% (2T26); −7,2% en conveniencia (jul-26) | ≥ 0% desde el 1T27 | ≤ −8% |
| Ventas al consumidor de Alani Nu | +55,7% (2T26); +74,2% en conveniencia (jul-26) | ≥ +15% | ≤ 0% |
| Crecimiento de la categoría en EE.UU. | +7,1% (13 semanas al 25-jul-26) | ≥ +7% | ≤ +3% |
| Participación del portafolio en EE.UU. | 20,1% (2T26) | ≥ 21% | ≤ 18% |
| Margen bruto | 48,1% (2T26) | ≥ 50% | ≤ 46% |
| EBITDA ajustado / ventas | 22,5% (2T26) | ≥ 24% | ≤ 19% |
| Regulación de la cafeína (Texas, otros estados) | Investigación abierta (jun-2026) | Cierre sin restricciones | Restricción por edad o etiquetado obligatorio |
| Acciones en circulación | 253,0 M (31-jul-2026); recompras de US$125,5M en el 1S26 | Bajan | Emisión para compras |

Indicadores de actualización de probabilidades: si el consumo de CELSIUS sigue negativo dos trimestres sube la Conservadora; si Alani Nu desacelera por debajo de +15 % o llega una restricción regulatoria sube la Disrupción; si CELSIUS se estabiliza y el margen bruto se mantiene sobre 47 % sube la Optimista.

## 17. Dictamen económico y resumen para escuchar

**Dictamen: con reservas.** La hoja está bien formada y reproduce el motor; los datos de partida están conciliados con el 10-Q del 2T FY26 en lo esencial, y los supuestos que dominan el valor (normalización del margen, ROIC terminal igual al costo de capital, ventas/capital y crecimiento de Alani Nu) son juicios declarados, no datos. La Base de US$24,20 es una tesis coherente pero frágil ante la regulación y la dependencia de PepsiCo; el precio de US$27,35 queda entre la Base y la Optimista y el margen de seguridad de 35 % exige un precio inferior a US$15,73.

Resumen para escuchar: Celsius es un negocio de bebidas rentable y liviano en capital, pero sin una marca con ciclo completo y con un único distribuidor. Si Alani Nu mantiene su ritmo y CELSIUS se estabiliza, la Base vale unos 24 dólares; si no, entre 17 y 6; y el precio de 27 ya descuenta algo mejor que la Base. Los supuestos menos respaldados son la normalización del margen de 19,6 por ciento, la deuda con PepsiCo en preferentes y el ventas sobre capital.

## 18. Fuentes primarias, limitaciones y registro de versión

Fuentes primarias:

- [Celsius, comunicado del 2T26 (6-ago-2026)](https://www.sec.gov/Archives/edgar/data/1341766/000134176626000047/ex9912q2026.htm)
- [Celsius, 10-Q del 2T26 (6-ago-2026)](https://www.sec.gov/Archives/edgar/data/1341766/000134176626000050/celh-20260630.htm)
- [Celsius, comunicado del 4T25 (26-feb-2026)](https://www.sec.gov/Archives/edgar/data/1341766/000134176626000017/ex9914q20251.htm)
- [Celsius, 10-K 2025 (2-mar-2026)](https://www.sec.gov/Archives/edgar/data/1341766/000134176626000024/celh-20251231.htm)
- [Celsius, 8-K de la segunda enmienda del crédito (15-jul-2026)](https://www.sec.gov/Archives/edgar/data/1341766/000119312526304791/d64754d8k.htm)
- [Celsius, 8-K de cambios en la gerencia (10-ago-2026)](https://www.sec.gov/Archives/edgar/data/1341766/000119312526342430/d135466dex991.htm)
- [Celsius, Form 4 del CEO (10-sep-2026)](https://www.sec.gov/Archives/edgar/data/1341766/000162828026061406/)
- [Monster Beverage, comunicado del 2T26 (6-ago-2026)](https://www.sec.gov/Archives/edgar/data/865752/000110465926092046/tm2622396d1_ex99-1.htm)
- [Monster Beverage, datos NielsenIQ al 25-jul-2026 (6-ago-2026)](https://www.sec.gov/Archives/edgar/data/865752/000110465926092046/tm2622396d1_ex99-2.htm)
- [Yahoo Finance, resumen de la llamada del 2T26 (6-ago-2026)](https://uk.finance.yahoo.com/news/celsius-holdings-inc-celh-q2-190423226.html)
- [14 News, investigación del fiscal de Texas (4-jun-2026)](https://www.14news.com/2026/06/04/state-opens-investigation-into-celsius-over-caffeine-levels-alani-nu-energy-drinks-marketed-teens/)
- [Robbins LLP vía GlobeNewswire, demanda colectiva (10-sep-2026)](https://www.globenewswire.com/news-release/2026/09/10/3360012/32719/en/celh-class-action-notice-robbins-llp-reminds-investors-of-the-lead-plaintiff-deadline-in-the-celsius-holdings-inc-class-action-lawsuit.html)
- [Damodaran, ERP implícita de octubre de 2026 (con la tasa y los precios del 30-sep)](https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx)
- [Damodaran, betas por industria (enero de 2026)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
- [Mauboussin y Callahan, The Base Rate Book (2016)](https://www.credit-suisse.com/media/assets/corporate/docs/about-us/research/publications/the-base-rate-book-integrating-the-past-to-better-anticipate-the-future.pdf)

Limitaciones: no es una auditoría contable; no se releyeron los factores de riesgo del 10-K ni el contrato con PepsiCo; la distribución del LTM por marca es una estimación; los datos de escáner provienen de comunicados de Monster y de resúmenes de prensa; la calificación crediticia no se verificó. Registro de versión: auditoría v1.3 del 2026-10-26, vinculada a la hoja rehecha el mismo día y al artículo `CELH-2026-10-26`; no sustituye la auditoría posterior del usuario.
