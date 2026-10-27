**Estado de publicación (2026-10-27): PUBLICADO CON SALVEDADES · revisión SHAK-REC-20261027-R1.** Estudio recuperado con corte del 30-sep-2026; sin cambios de supuestos, probabilidades ni pesos. Valoración, análisis fundamental y esta auditoría corresponden a la misma hoja de Google y a la misma revisión.

**Controles ejecutados el 27-oct-2026:** siete múltiplos con fórmula y resultado numérico (`verificar_multiplos_hoja.py`), fórmulas contra la maestra del 22-oct (`audit_master_formulas.py`), consistencia hoja = registro = análisis (`consistencia_migracion.py --hoja`), candados vigentes, probabilidades.

**Salvedades vigentes:**
- Estudio recuperado: precio y corte de información del 30-sep-2026; no incorpora resultados posteriores ni actualiza supuestos.
- Siete múltiplos calculados por las fórmulas originales de la hoja (7/7 con fórmula; 5 con resultado y 2 N/A del paso 6.1; fórmulas de cálculo y múltiplos idénticas a la maestra del 22-oct-2026); P/V y P/BV con peso 0 y estado provisional.
- Candados de la plantilla del 21-oct (Financials Multiples!M34:M36) no aplican a la maestra vigente; se exigen solo los presentes en ella.
- EV/FCFF y P/FCFE no aplican (paso 6.1, marcados «No» en Resumen de Valoración!F8 y F10): FCFF negativo en FY+1 y FY+2 de Conservador y Base y múltiplo histórico de P/FCFE de 282x por FCFE casi nulo; peso 0, sin precio y sin valor inventado.
- Regla H3 pendiente: P/OCF Optimista 20,34x supera 0,92 veces el promedio histórico (19,82x); corregirlo exige cambiar `POCF!J30` y requiere autorización.
- Errores informativos #NUM! en EVEBITDA!B39:B41 y EVFCFF!B39:B41 (MEDIAN de múltiplos históricos sin datos numéricos); fórmulas idénticas a la maestra, no alimentan ningún precio.

---

# Auditoría económica narrativa — Shake Shack Inc. (SHAK)

**Análisis fundamental vinculado:** [SHAK en la app](https://juanmarobledo.github.io/Modelo-JMR/research.html?ticker=SHAK) · registro `analisis/SHAK-research-1790597619437-xvczr.json` (revisión del 2026-10-26).

## 1. Ficha de auditoría y alcance

| Campo | Contenido |
|---|---|
| Emisor | Shake Shack Inc.; ticker SHAK |
| Mercado, moneda y escala | NYSE (EE. UU.); US$ millones salvo por acción |
| Sector | Restaurantes de servicio rápido «fine casual» (Restaurant/Dining) (hoja: industria de Damodaran «Restaurant/Dining») |
| Método intrínseco principal | DCF FCFF de la historia Base (compañía operativa); MOS de 35 % sobre ese valor |
| Estados examinados | 10-K 2025 y 10-Q del 2T26 (balance al 1-jul-2026); LTM = FY2025 + 1S26 − 1S25 |
| Fecha de valoración / de auditoría | Corte de mercado 30-sep-2026 / 2026-10-26 |
| Precio del análisis | US$58,68 al cierre del 30-sep-2026 (corte común de la cartera); no se obtuvo un precio posterior |
| Hoja auditada | [Modelo JMR SHAK](https://docs.google.com/spreadsheets/d/1j6U5KtzbnRDyI6mQDgJD4pNq15flN9k8RvdXGfUrG1o/edit), rehecha desde la maestra el 2026-10-26 |
| Artículo y Nivel 2 | `JMR-valuation/data/SHAK_Research_Fundamental_Modelo_JMR_2026-10-26.md` y `SHAK_Nivel2_Datos_Modelo_JMR_2026-10-26.md` |
| Registro en la app | Se publica con la autorización general del usuario; sin certificación previa (el usuario audita después) |
| Visto | Hoja completa por lectura; 10-Q del 2T26 por XBRL de companyfacts (balance, arrendamientos, convertibles); carta del 2T26; ficha de historias |
| Fuera de alcance | 10-K completo (factores de riesgo, litigios, margen a nivel Shack); transcripción de la llamada; 8-K posteriores al 10-Q; estados de los pares; consenso y calificaciones |
| Estado de verificación | **Con reservas** (no es una auditoría contable). Ver §15 y §17 |

## 2. Resumen ejecutivo y relato económico central

Shake Shack opera 703 Shacks (406 propios y 297 licenciados). En el LTM a julio de 2026 facturó US$1.552 millones con EBIT GAAP de US$55 millones (3,6 %); el capex de US$203 millones consumió todo el flujo operativo y el flujo libre fue ligeramente negativo. La gerencia redujo la guía de 2026. La Base de US$24,13 por acción supone ~11 % de crecimiento compuesto y margen operativo de 8 % con ROIC terminal igual al costo de capital, y queda 59 % por debajo del precio de US$58,68.

**Tesis Base favorable:** Crece por aperturas ~11 % anual y el margen operativo llega a 8 %: US$24,13 por acción. **Interpretación neutral:** Crece sin rentabilidad: ingresos +7 % anual y margen de 5 %; la Conservadora (US$7,29, 22,5 %) describe esa ruta. **Contratesis adversa:** Los Shacks nuevos no rinden y el crecimiento se frena: ingresos +3 % anual y margen de 3 % (Disrupción, US$0,00, 15,0 %).

El supuesto que domina el valor es la tasa de descuento (±1 punto de WACC mueve la Base US$18,05 (−25,2 %) / US$31,96 (+32,5 %)), seguido por el margen operativo GAAP de 3,6 % a 8 % y el retorno de los Shacks nuevos. El precio (US$58,68) queda por encima de la Base (143 %); ver el DCF inverso en §10. Esta narrativa no se deriva del precio: parte de los estados de la compañía.

## 3. Trazabilidad, integridad y jerarquía de evidencia

Inventario de las celdas de entrada de `Input sheet`, `Cost of capital worksheet`, `R& D converter` y `Option value`, y de los datos que la hoja enlaza desde las pestañas de estados (Income Statement, Balance Sheet, Cash Flow Statement; columna L = LTM). `Financials Multiples` no tiene celdas de entrada propias: son fórmulas.

**Conteo:** la tabla tiene **84 filas** (todas las de `Input sheet` con valor, las entradas clave del costo de capital y el conversor de I+D). Las celdas con fórmula por defecto (`Input sheet!B27:B33`) se incluyen porque el analista puede sustituirlas.

**Cómo se cargaron los estados.** (a) El importador de la SEC (`desde_cero.sh datos`) cargó diez ejercicios y el LTM; (b) el balance del LTM repetía partidas de diciembre de 2025 y se reescribió con el 10-Q de julio de 2026 (caja 308,0, convertibles 248,3, patrimonio 571,6); (c) las acciones son 42,8 M (Clase A y Clase B canjeable) de la hoja anterior, escritas en Income Statement!L27, y las participaciones no controladoras (27,2) no se restan porque son unidades de la LLC ya contadas; (d) los arrendamientos operativos pasan por el conversor con los compromisos del 10-Q anterior; (e) EV/FCFF y P/FCFE se marcan «No» en 'Resumen de Valoración'!F8 y F10 (paso 6.1).

**Diferencias de fuente y ajustes:** (a) acciones: 42,8 M frente a 41,8 M del promedio diluido; (b) la tasa del LTM (33 %) converge a la marginal de 25 % por el método Convergencia Damodaran; (c) el ancla C de EV/EBITDA (0,26×) no es calculable por el FCFF negativo y no se usa como tope (decisión del 3-oct-2026); (d) la hoja suma los convertibles (248,3) como deuda y no estima su opción de conversión.

| # | Pestaña | Celda | Rótulo | Valor | Tipo | Documento/fuente (URL en §18) | Quién lo aportó | Verificación |
|---:|---|---|---|---|---|---|---|---|
| 1 | Input sheet | B1 | Shake Shack Inc. (NYSE:SHAK) | Shake Shack Inc. (NYSE:SHAK) | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 2 | Input sheet | B4 | Date of valuation | sept-26 | Juicio | Corte de mercado 30-sep-2026 (fecha de valoración) | Corte común | [OBSERVADO] |
| 3 | Input sheet | B5 | Company name | Shake Shack Inc. | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 4 | Input sheet | B8 | Country of incorporation | United States | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 5 | Input sheet | B9 | Industry (US) | Restaurant/Dining | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 6 | Input sheet | B10 | Industry (Global) | Restaurant/Dining | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 7 | Input sheet | B12 | Revenues | $ 1.552,30 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 8 | Input sheet | B13 | Operating income or EBIT | $ 55,40 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 9 | Input sheet | B14 | Interest expense | $ 2,10 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 10 | Input sheet | B15 | Book value of equity | $ 571,60 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 11 | Input sheet | B16 | Book value of debt | $ 256,60 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 12 | Input sheet | B17 | Do you have R&D expenses to capitalize? | No | Juicio | Capitalización de I+D según la regla del sector de la empresa | IA | Decisión de método; ver hallazgos |
| 13 | Input sheet | B18 | Do you have operating lease commitments? | Yes | Juicio | Arrendamientos operativos como deuda (conversor de Damodaran) | IA | [MODELO] |
| 14 | Input sheet | B19 | Cash and Marketable Securities | $ 308,00 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 15 | Input sheet | B20 | Valor económico validado de participaciones y activos NO ope | $ - | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 16 | Input sheet | B21 | Minority interests | $ - | Dato | Sin participaciones minoritarias relevantes | IA | [NO VERIFICADO] en la nota de patrimonio |
| 17 | Input sheet | B22 | Number of shares outstanding = | 42,80 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 18 | Input sheet | B23 | Current stock price = | $ 58,68 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 19 | Input sheet | B24 | Effective tax rate = | 33,38% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 20 | Input sheet | B25 | Marginal tax rate = | 25,00% | Juicio | Tasa marginal federal más estatal de EE. UU. (25 %) | Plantilla/IA | Convención del modelo [MODELO] |
| 21 | Input sheet | B27 | Revenue growth rate for next year  | 12,97% | Juicio | Crecimiento del año 1 de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 22 | Input sheet | B28 | Operating Margin for next year | 6,02% | Juicio | Margen operativo del año 1 de la Base: 4,5 % más el ajuste de arrendamientos (1,5 pp) | IA (ficha de historias) | [HIPÓTESIS]; ver H-01 |
| 23 | Input sheet | B29 | Compounded annual revenue growth rate - years 2-5 = | 10,55% | Juicio | CAGR de los años 2-5 de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 24 | Input sheet | B30 | Referencia de margen objetivo (mediana histórica/sectorial;  | 9,52% | Juicio | Margen objetivo de la Base: 8 % más el ajuste de arrendamientos | IA | [HIPÓTESIS]; ver H-01 |
| 25 | Input sheet | B31 | Year of convergence for margin | 5,00 | Juicio | Año de convergencia del margen: 5 | Plantilla/IA | Coherente con las historias |
| 26 | Input sheet | B32 | Sales to capital ratio  (for years 1-5) | 1,90 | Juicio | Ventas/capital años 1-5 (ficha de historias, ajustado por el conversor de arrendamientos) | IA | [HIPÓTESIS]; ver hallazgos |
| 27 | Input sheet | B33 | Sales to capital ratio (for years 6-10) | 1,70 | Juicio | Ventas/capital años 6-10 (ficha de historias, ajustado por el conversor de arrendamientos) | IA | [HIPÓTESIS]; ver hallazgos |
| 28 | Input sheet | B35 | Riskfree rate | 5,29% | Dato | Treasury a 10 años del corte común (30-sep-2026): 5,29 % | Corte común (datos_mercado.py) | [OBSERVADO] FRED DGS10 |
| 29 | Input sheet | B36 | Initial cost of capital = | 7,92% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 30 | Input sheet | B38 | Do you have employee options outstanding? | No | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 31 | Input sheet | B39 | Number of options outstanding = | 0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 32 | Input sheet | B40 | Average strike price = | $0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 33 | Input sheet | B41 | Average maturity = | 0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 34 | Input sheet | B42 | Standard deviation on stock price = | 0,00% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 35 | Input sheet | B46 | Do you want to override this assumption = | No | Juicio | No se anula el WACC terminal: converge a la fórmula de la plantilla | Plantilla | [MODELO] |
| 36 | Input sheet | B47 | If yes, enter the cost of capital after year 10 = | 7,92% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 37 | Input sheet | B49 | Do you want to override this assumption = | No | Juicio | Anulación del ROIC terminal (Yes) o ROIC terminal igual al costo de capital (No) | IA | Ver hallazgos de ROIC terminal |
| 38 | Input sheet | B52 | Do you want to override this assumption = | No | Juicio | Sin probabilidad de fracaso en la Base | IA | [INFERENCIA] |
| 39 | Input sheet | B53 | If yes, enter the probability of failure = | 0% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 40 | Input sheet | B54 | What do you want to tie your proceeds in failure to? | V | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 41 | Input sheet | B55 | Enter the distress proceeds as percentage of book or fair va | 50% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 42 | Input sheet | B57 | Do you want override this assumption = | No | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 43 | Input sheet | B58 | If yes, enter a different lag (0 = no lag to 3 = lag of 3 ye | 1 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 44 | Input sheet | B60 | Do you want to override this assumption = | No | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 45 | Input sheet | B62 | Do you want to override this assumption = | No | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 46 | Input sheet | B65 | Do you want to override this assumption = | No | Juicio | No se anula la tasa libre después del año 10 | IA | — |
| 47 | Input sheet | B66 | If yes, enter the riskfree rate after year 10 | 5,29% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 48 | Input sheet | B68 | Do you want to override this assumption = | Yes | Juicio | Se anula el crecimiento perpetuo con la regla del modelo | IA | Ver B69 |
| 49 | Input sheet | B69 | If yes, enter the growth rate in perpetuity | 4,00% | Juicio | Crecimiento terminal 4,00 % (≤ tasa libre de 5,29 %) | Regla vigente del modelo | [MODELO] |
| 50 | Input sheet | B71 | Do you want to override this assumption | No | Juicio | Sin efectivo atrapado | IA | [NO VERIFICADO] |
| 51 | Input sheet | B72 | If yes, enter trapped cash (if taxes) or entire balance (if  | $0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 52 | Input sheet | B73 | & Average tax rate of the foreign markets where the cash is  | 0% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 53 | Input sheet | B76 | Valor de acciones preferentes (misma unidad del DCF) | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 54 | Input sheet | B78 | PV del conversor ya incluido en deuda del balance (solapamie | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 55 | Input sheet | B79 | Pasivo de arrendamientos INCREMENTAL no reconocido | $ 654,44 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 56 | Input sheet | B80 | Ajuste de EBIT atribuible a pasivos incrementales | 24,50735771 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 57 | Input sheet | B81 | Estado de conciliación de arrendamientos | CONCILIADO | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 58 | Input sheet | B82 | Inversiones a largo plazo según balance (dato histórico; NO  | $0 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 59 | Input sheet | B83 | Valor CONTABLE de inversiones excluidas del capital operativ | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 60 | Input sheet | B84 | Valor ECONÓMICO atribuible de participaciones y activos no o | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 61 | Input sheet | B85 | Control de inversiones y doble contabilización | VALIDADO | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 62 | Input sheet | B86 | Revisión: no están incluidas en EBIT/FCFF ni duplicadas | Sin solapamiento | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 63 | Input sheet | B87 | Fuente y conciliación de inversiones no operativas | 10-Q 2T26: sin inversiones relevantes; las participaciones n | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 64 | Input sheet | B89 | Método fiscal de proyección (obligatorio en cada copia) | Convergencia Damodaran | Juicio | Convergencia Damodaran: la tasa efectiva del LTM (~33 %) converge a la marginal de 25 % | IA | [INFERENCIA] |
| 65 | Input sheet | B91 | Fuente / conciliación de impuesto efectivo vs marginal | Tasa efectiva del LTM de la hoja (L29, ~33 %) que converge a | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 66 | Input sheet | B92 | Control de hipótesis fiscales | VALIDADO | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 67 | Input sheet | B93 | Impuesto inicial para pronóstico (no altera la tasa históric | 33,38% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 68 | Input sheet | B96 | Tasa libre de riesgo nominal de largo plazo · misma moneda d | 5,29% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 69 | Input sheet | B97 | WACC terminal efectivo del modelo (independiente del DCF hab | 8,99% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 70 | Input sheet | B98 | Base | Sin liberación | Juicio | Sin liberación de capital en contracción (reinversión negativa se trunca a cero) | IA | Regla de Damodaran |
| 71 | Input sheet | B99 | Conservadora | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 72 | Input sheet | B100 | Disrupción | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 73 | Input sheet | B101 | Optimista | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 74 | Cost of capital worksheet | B12 | Which approach will you be using? | Detailed | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 75 | Cost of capital worksheet | B22 | Approach for estimating beta | Single Business(US) | Juicio | Beta bottom-up de Restaurant/Dining para un negocio único de EE. UU. | IA | [HIPÓTESIS]; ver H-06 |
| 76 | Cost of capital worksheet | B26 | What approach do you want to use to input ERP? | Will Input | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 77 | Cost of capital worksheet | B33 | Average Maturity = | 2 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 78 | Cost of capital worksheet | B34 | Approach for estimating pre-tax cost of debt | Actual rating | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 79 | Cost of capital worksheet | B36 | If actual rating, input the rating | Ba1/BB+ | Dato | Calificación crediticia Ba1/BB+ | IA (hoja anterior) | [NO VERIFICADO] en esta revisión |
| 80 | Cost of capital worksheet | B41 | Book Value of Convertible Debt = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 81 | Cost of capital worksheet | B49 | Number of Preferred Shares = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 82 | Cost of capital worksheet | B50 | Current Market Price per Share= | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 83 | Cost of capital worksheet | B51 | Annual Dividend per Share = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 84 | R& D converter | F7 | Años de amortización del I+D | 3 | Juicio | Convención de Damodaran para la industria | IA | [MODELO] |

**Jerarquía de evidencia usada:** [OBSERVADO] (documento de la compañía o comprobación directa), [INFERENCIA] (deducción de lo observado), [HIPÓTESIS] (supuesto del analista), [MODELO] (resultado de las fórmulas) y [NO VERIFICADO].

## 4. Historia financiera: diez años y punto de partida

| US$ millones | Dec '20 | Dec '22 | Dec '23 | Dec '24 | Dec '25 | LTM |
|---|---:|---:|---:|---:|---:|---:|
| Ingresos | 523 | 900 | 1.088 | 1.253 | 1.445 | 1.552 |
| EBIT | -44 | -27 | 6 | 3 | 62 | 55 |
| Margen operativo | -8,4 % | -3,0 % | 0,5 % | 0,2 % | 4,3 % | 3,6 % |
| Flujo operativo | 37 | 77 | 132 | 171 | 222 | 192 |
| Capex | -69 | -143 | -146 | -136 | -166 | -203 |
| Capex / ventas | 13,2 % | 15,8 % | 13,4 % | 10,8 % | 11,5 % | 13,1 % |

La historia tiene tres fases. De 2016 a 2019 Shake Shack creció 28-34 % con aperturas y margen operativo de 10 % a 4 %. En 2020-2024 la pandemia y la inflación llevaron el margen a −8 % en 2020 y a ~0 % en 2023-2024 con crecimiento de 15-21 %. En 2025-2026 el margen subió a 4,3 % y el LTM está en 3,6 %, con ingresos +17,2 % en el 2T26 y same-Shack +3,5 %. La Base supone que el crecimiento se sostiene (~11 %) y el margen llega a 8 %; la Conservadora, que crece sin rentabilidad; la Disrupción, que los Shacks nuevos no rinden.

## 5. Crecimiento de ingresos: de la historia a la proyección

La Base construye el ingreso por cubeta (Shacks propios US$1.500 millones; Licencias US$52 millones). El resultado consolidado es 13,0 %, 12,0 %, 11,0 %, 10,1 %, 9,1 % en los años 1-5 (11,0 % compuesto) y cae a 4,0 % en el año 10: ingresos de 2.619 millones en el año 5 y 3.510 millones en el año 10.

Por qué ese ritmo: [INFERENCIA] el primer año de la Base (13 %) sigue las aperturas (61 Shacks propios en doce meses) y same-Shack de +3,5 %, y baja a ~9 % en el año 5; la visión externa ubica ~11 % compuesto en el tramo donde ~40 % de las empresas de su tamaño lo logró. Duda: el LTM de la hoja muestra +7,4 % y la guía de 2026 se redujo.

Alternativas: la Conservadora (7,4 % compuesto, año 1 de 9,9 %); la Optimista (13,1 %, año 1 de 15,0 %); la Disrupción (2,8 %, con crecimiento terminal de 2 %). Los porcentajes son juicio del analista, no una guía publicada por la compañía.

## 6. Márgenes operativos y normalización de beneficios

La Base lleva el margen de 6,0 % en el año 1 a 9,5 % en el año 5 (ya ajustado por I+D capitalizado y arrendamientos; en base reportada 8,0 %). La Conservadora llega a 6,5 % (5,0 % reportado), la Disrupción a 4,5 % y la Optimista a 12,5 % (11,0 % reportado). Tasa impositiva: 33,4 % al inicio, convergiendo a la marginal de 25 % en el año 10.

Por qué ese margen: [OBSERVADO] el margen GAAP pasó de 0,5 % (2023) a 4,3 % (2025) y 3,6 % en el LTM. La Base lo lleva a 8 % con eficiencia en costos y gastos generales que crecen menos que las ventas. Sensibilidad: ±2 puntos de margen dan US$13,30 y US$34,96 (±44,9 %): es la variable que más mueve el valor. La Optimista (11 %) exige márgenes de cadenas mucho más grandes.

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

La reinversión de la Base es de 111 millones en el año 1 (frente a un NOPAT de 70 millones) y el FCFF del año 1 es de -40 millones. El ventas/capital es 1,90 en los años 1-5 y 1,70 en los 6-10 (base de la hoja, que incluye I+D y arrendamientos cuando la empresa los capitaliza). Con ±20 % en el ancla, el DCF Base va de US$19,93 (−17,4 %) a US$26,92 (+11,6 %). ROIC terminal: Base 9,0 %, Conservadora 9,0 %, Disrupción 9,0 %, Optimista 9,0 %.

Evidencia: capex de US$135-203 millones al año; la hoja usa ventas/capital de 1,9 (años 1-5) y 1,7 (años 6-10), con los arrendamientos incluidos (promedio de Restaurant/Dining 1,51). El motor avisa del retorno del capital nuevo frente al ROIC terminal (9 %). ±20 % en el ventas/capital mueve la Base de US$19,93 a US$26,92.

## 8. Costo del capital y riesgo

Tasa libre de riesgo 5,29 % (Treasury a 10 años al 30-sep-2026), prima de riesgo de 3,70 % (ponderada por regiones de ingresos), beta desapalancada del sector 0,78 y beta apalancada 0,99 (propuesta bottom-up 0,99). WACC inicial 7,92 %; WACC terminal 8,99 %.

Dudas: (i) la beta bottom-up de Restaurant/Dining (0,99) no recoge el riesgo de ejecución de una cadena de crecimiento con márgenes bajos; (ii) el costo de capital inicial es ~9 % con prima de mercado de 3,7 % y tasa libre de 5,29 %; (iii) la calificación Ba1/BB+ no se verificó. ±1 punto de tasa da US$31,96 (+32,5 %) y US$18,05 (−25,2 %).

Efecto: ±1 punto de WACC mueve la Base US$18,05 (−25,2 %) / US$31,96 (+32,5 %), el supuesto de mayor peso. La plantilla hace converger el WACC de 7,92 % a 8,99 % en el año 10 (convención de Damodaran).

## 9. Convergencia y valor terminal

El valor terminal es 80,3 % del valor de los activos operativos de la Base (1.313 millones de 1.636 millones). Crecimiento terminal 4,00 % (≤ la tasa libre), ROIC terminal 9,0 % y WACC terminal 8,99 %. Con −0,5 puntos de crecimiento terminal la Base vale US$23,95 (−0,7 %); con +0,5 puntos, US$24,31 (+0,7 %).

Riesgos: (i) las cuatro historias suponen ROIC terminal igual al costo de capital (9 %), coherente con un ROIC con arrendamientos de ~5 %; (ii) el crecimiento terminal de 4 % es menor que la tasa libre de riesgo; (iii) los convertibles de 2028 pueden refinanciarse con dilución.

## 10. Validación independiente del valor intrínseco

Comprobación 1 (identidad): la hoja y el motor independiente del repositorio coinciden en las cuatro historias (Base 24,13; Conservadora 7,29; Disrupción 0,00; Optimista 44,84), lo que valida la aritmética, no la economía. Comprobación 2 (puente): activos operativos 1.636 + caja 308 − deuda con arrendamientos 911 − opciones 0 − preferentes 0 + no operativos 0 = patrimonio común de 1.033 millones, o US$24,13 por acción con 42,8 millones de acciones. Comprobación 3 (DCF inverso del Nivel 2, margen → crecimiento anual de los años 1-5 que justifica el precio):

| Beta | Margen | Crecimiento anual de los años 1-5 que justifica el precio | Fracción de empresas de este tamaño que lo logra |
|---|---:|---:|---:|
| 0,99 | 9,5% | 30,2% | 4,3% |
| 0,99 | 12,5% | 18,1% | 16,3% |
| 0,99 | 15,5% | 11,4% | 38,3% |
| 0,99 | 9,5% | 30,2% | 4,4% |
| 0,99 | 12,5% | 18,0% | 16,3% |
| 0,99 | 15,5% | 11,4% | 38,4% |

Comprobación 4 (múltiplos propios): los cierres hasta noviembre de 2024 (EV/EBITDA de 20 a 675×) reflejan la etapa de expansión; la regla por ciclo lleva la Base a 14,6× (EV/EBITDA), 28,0× (P/E) y 13,1× (P/OCF) con pares de restaurantes en expansión (Chipotle, Wingstop, Texas Roadhouse, Dutch Bros). EV/FCFF y P/FCFE no aplican.

## 11. Cuatro historias y probabilidades

| Historia | Probabilidad | CAGR 1-5 | Margen objetivo (ajustado / reportado) | ROIC terminal | g terminal | DCF por acción |
|---|---:|---:|---:|---:|---:|---:|
| Base · Crece por aperturas y el margen mejora | 40,0 % | 11,0 % | 9,5 % / 8,0 % | 9,0 % | 4,0 % | US$24,13 |
| Conservadora · Crece, pero el margen no despega | 22,5 % | 7,4 % | 6,5 % / 5,0 % | 9,0 % | 4,0 % | US$7,29 |
| Disrupción · Deterioro de los fundamentales | 15,0 % | 2,8 % | 4,5 % / 3,0 % | 9,0 % | 2,0 % | US$0,00 |
| Optimista · Economía unitaria de primer nivel | 22,5 % | 13,1 % | 12,5 % / 11,0 % | 9,0 % | 4,0 % | US$44,84 |

Las probabilidades salen de la regla del ciclo (crecimiento_alto) y no se ajustaron por indicadores: son un juicio condicional, no frecuencias observadas. El DCF esperado de las tres historias activas (pesos renormalizados) es US$25,15; con MOS de 35 % sobre el DCF Base el precio de compra es US$15,68. Cambiar los pesos cambia el esperado, no el DCF Base.

### ¿Qué pasaría si todo fallara?

Si crece sin rentabilidad (ingresos +7 % y margen de 5 %), la acción vale la Conservadora (US$7,29); si los Shacks nuevos no rinden y el crecimiento se frena (margen de 3 %), el DCF da cero. El balance (caja de US$308 millones frente a convertibles de US$250 millones) limita el riesgo de liquidez a corto plazo, no el de valor por acción.

## 12. Valoración por múltiplos: prueba independiente y secundaria

Siete métodos (EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF, P/V y P/BV; los dos últimos con peso cero). Regla del 18-oct-2026: el múltiplo de cada escenario es el que la empresa tuvo cuando crecía como el escenario espera en FY+3 (Conservador 7,0 %, Base 11,0 %, Optimista 13,1 %), llevado al costo de capital del corte y limitado por el múltiplo justificado por los fundamentos de la misma historia; los comparables solo comprueban.

| Método | Mediana histórica 10a | Actual (LTM) | Ancla de peers (mediana) | Justificado Base | Peso en múltiplos |
|---|---:|---:|---:|---:|---:|
| EV/EBITDA | N/D× | 14,58× | 18,37× | 0,26× | 33 % |
| EV/FCFF | N/D× | N/D× | 40,79× | 36,97× | 17 % |
| P/E | 83,01× | 61,78× | 53,56× | 27,99× | 33 % |
| P/FCFE | 122,17× | N/D× | 48,40× | 30,81× | 8 % |
| P/OCF | 21,54× | 13,11× | 16,82× | 15,13× | 8 % |

Resultado: múltiplos consolidados de US$72,94 (Conservador), US$99,69 (Base) y US$140,48 (Optimista), frente a DCF de US$7,29, US$24,13 y US$44,84. Lectura del 3-oct-2026: EV/FCFF y P/FCFE no aplican (FCFF proyectado negativo en FY+1-FY+2; el FCFE solo es positivo por deuda nueva; revisado el 5-oct-2026) y su peso pasa a EV/EBITDA, P/E y P/OCF. Los múltiplos aplicables quedan muy por encima del DCF y la brecha no es un error de cálculo: A es el múltiplo de la propia acción desde 2025 (historia corta, casi el precio de mercado) y B son peers con ROIC de 20-40%, mientras el ROIC de Shake Shack con arrendamientos es ~5% y en el DCF el crecimiento apenas crea valor (ROIC terminal = costo de capital). El DCF es el método más confiable para esta empresa; los múltiplos dicen cuánto paga hoy el mercado por restaurantes en expansión. Pendiente del analista (paso 6.5): ajustar la mediana de peers por margen y ROIC (hoy solo se ajusta +10% por crecimiento) o subir λ; no se movió para acercarlo al DCF.

La Base de los múltiplos (US$99,69) queda 313 % por encima del DCF Base (US$24,13): los múltiplos (EV/EBITDA de ~14,5×) describen lo que el mercado paga por restaurantes en expansión y no el retorno del capital, y el EV/EBITDA ignora el capex de expansión. Es una brecha de método, no un error de cálculo. Ver H-03.

## 13. Sensibilidades económicas y escenarios alternativos

| Supuesto cambiado (DCF Base US$24,13) | Valor |
|---|---:|
| WACC +1 pp / −1 pp | US$18,05 (−25,2 %) / US$31,96 (+32,5 %) |
| Crecimiento años 1-5 −2 pp / +2 pp | US$21,94 (−9,1 %) / US$26,51 (+9,9 %) |
| Margen objetivo −2 pp / +2 pp | US$13,30 (−44,9 %) / US$34,96 (+44,9 %) |
| Crecimiento terminal −0,5 pp / +0,5 pp | US$23,95 (−0,7 %) / US$24,31 (+0,7 %) |
| Ventas/capital −20 % / +20 % | US$19,93 (−17,4 %) / US$26,92 (+11,6 %) |

Ordenado por impacto: el margen objetivo (±2 puntos: ±44,9 %), la tasa de descuento (±1 punto: +32,5 % / −25,2 %), el ventas/capital (±20 %: −17,4 % / +11,6 %), el crecimiento de los años 1-5 (±2 puntos: −9,1 % / +9,9 %) y la dilución adicional de 5 % (−4,8 %). Las matrices del Nivel 2 recogen crecimiento por margen.

## 14. Coherencia de hojas, cálculos y presentación

La hoja está unificada con la maestra (61 pestañas en el mismo orden, 21.258 fórmulas intactas, 122 selectores idénticos) y el motor independiente reproduce las cuatro historias. Controles: candados 15/15, inputs completos, estados completos e integridad de hojas (registro en la bitácora de la sesión).

Intervenciones sobre la hoja que el lector debe conocer: (i) se restauraron las fórmulas de la maestra tras cada carga; (ii) el importador traía partidas de diciembre de 2025 en el LTM y se reescribió con el 10-Q de julio de 2026; (iii) las acciones, el patrimonio y la tasa fiscal se llevaron a celdas que sobreviven a la restauración; (iv) se corrigió multiples_by_cycle.py para métodos «no aplica» y se excluyó el ancla C de EV/EBITDA; (v) EV/FCFF y P/FCFE se marcaron «No» en el Resumen.

## 15. Hallazgos priorizados y propuestas de corrección

| ID | Severidad | Hallazgo | Impacto | Propuesta |
|---|---|---|---|---|
| H-01 | Alta | El valor depende casi por completo del margen operativo: de 3,6 % a 8 % en la Base | ±2 puntos de margen mueven la Base ±44,9 %; con 5 % el valor es US$7,29 | Construir el puente de margen por Shack (margen a nivel Shack, gastos generales) y contrastar con cadenas comparables |
| H-02 | Alta | El precio (US$58,68) supera a las tres historias centrales, incluida la Optimista (US$44,84); el DCF inverso pide un margen de 16 % con crecimiento de ~11 % | El mercado supone un margen que la empresa no demostró; la Base queda 59 % por debajo del precio | Decidir si el precio descuenta una ventaja duradera o una expansión de márgenes no incluida |
| H-03 | Alta | Los múltiplos aplicables dan US$99,69 en la Base frente al DCF de US$24,13 (+313 %) | El consolidado de múltiplos pesa 40 % del ponderado secundario (US$54,35) y lo aleja del DCF principal | Ajustar la mediana de peers por margen y ROIC (paso 6.5) o subir λ |
| H-04 | Media | EV/FCFF y P/FCFE no aplican (FCFF negativo, FCFE financiado con deuda) y su peso pasa a EV/EBITDA, P/E y P/OCF | EV/EBITDA pesa 50 % dentro de los múltiplos aunque ignora el capex de expansión | Revisar el reparto de pesos y considerar EV/ventas como referencia |
| H-05 | Media | El ancla C de EV/EBITDA (0,26×) no es calculable por el FCFF negativo y se excluyó como tope | Sin tope, la Base de EV/EBITDA es 14,6× | Revisar si un EV/EBITDA justificado puede calcularse con un FCFF normalizado |
| H-06 | Media | La beta de 0,99 es bottom-up de restaurantes y el costo de capital es ~9 % | ±1 punto de tasa mueve la Base +32,5 % / −25,2 % | Documentar la elección y comparar con la beta de regresión |
| H-07 | Media | Los convertibles de US$250 millones al 0 % vencen en 2028 y se tratan solo como deuda | Refinanciar a tasas altas o con dilución reduciría el valor por acción | Modelar el refinanciamiento y la opción de conversión |
| H-08 | Media | Las acciones (42,8 M) incluyen la Clase B canjeable y no restan las participaciones no controladoras (27,2) | Si no son canjeables en la práctica, la deducción bajaría la Base ~US$0,6 | Confirmar el canje de las unidades de la LLC con el 10-K |
| H-09 | Media | El balance del LTM se escribió a mano desde el 10-Q (caja, convertibles, patrimonio) | Un error de transcripción cambia la deuda neta y el valor por acción | Releer el balance del 10-Q y conciliar fila por fila |
| H-10 | Baja | El conversor de arrendamientos usa los compromisos del 10-Q anterior heredados (gasto de 97,2 y calendario de 89,2 a 383,6) | Efecto menor en la Base | Actualizar el calendario con el 10-Q del 2T26 |
| H-11 | Media | La composición de los competidores y de la dirección, el desglose geográfico y el margen a nivel Shack no se revisaron | Afecta las secciones 3, 7 y 8 del análisis | Verificar con el 10-K y la carta del 2T26 |
| H-12 | Baja | La probabilidad de la Disrupción (15 %) y el DCF de cero de esa historia son juicio sin tasa base externa | Cada 5 puntos de probabilidad mueven el esperado ~US$1,2 | Contrastar con casos de cadenas de restaurantes que frenaron su expansión |

## 16. Catalizadores, señales de refutación y seguimiento

| Indicador | Último dato | Confirma Base u Optimista | Favorece Conservadora o Disrupción |
|---|---|---|---|
| Ventas same-Shack | +3,5% (2T26) | ≥ +3% | Negativas |
| Margen a nivel Shack | En alza | ≥ 22% | ≤ 19% |
| Margen operativo GAAP | 3,6% LTM | ≥ 6% en 2027 | ≤ 3% |
| Aperturas de Shacks propios | 61 en 12 meses | 55-70 al año con buen volumen | Recortes o volúmenes bajos |
| Flujo libre | ~0 | Positivo y creciente | Negativo |

Indicadores de actualización de probabilidades: si same-Shack es negativo o el margen a nivel Shack baja de 19 % sube la Conservadora (y la Disrupción); si el margen operativo supera 6 % en 2027 con aperturas de 55-70 al año sube la Base; si el margen se acerca a 11 % sube la Optimista. Próximo hito: resultados del 3T26 (oct-2026).

## 17. Dictamen económico y resumen para escuchar

**Dictamen: con reservas.** La hoja está bien formada, reproduce el motor en las cuatro historias y quedó UNIFICADA con la maestra; el balance del LTM se reescribió con el 10-Q del 2T26. El valor depende del margen operativo y el precio supera todas las historias centrales; los múltiplos aplicables quedan muy por encima del DCF y no son comparables con él. La brecha entre métodos, el reparto de pesos y los convertibles de 2028 son los puntos técnicos a revisar primero.

Resumen para escuchar: Shake Shack es una cadena de hamburguesas premium que crece 15 por ciento al año pero gana solo 3,6 por ciento de margen operativo. La Base de 24 dólares por acción queda muy por debajo del precio de casi 59 dólares. Lo que más mueve el valor es el margen; los múltiplos dan mucho más que el flujo descontado.

## 18. Fuentes primarias, limitaciones y registro de versión

Fuentes primarias:

- [Shake Shack, Form 10-Q del 2T 2026](https://www.sec.gov/Archives/edgar/data/1620533/000162053326000034/shak-20260701.htm)
- [Shake Shack, Form 10-Q del 1T 2026](https://www.sec.gov/Archives/edgar/data/1620533/000162053326000026/shak-20260401.htm)
- [Shake Shack, Form 10-K 2025](https://www.sec.gov/Archives/edgar/data/1620533/000162053326000018/shak-20251231.htm)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)

Limitaciones: no es una auditoría contable; no se revisaron el 10-K completo, el margen a nivel Shack ni los 8-K posteriores al 10-Q; los competidores y la dirección se describen con conocimiento general; la calificación crediticia y el consenso no se verificaron. Registro de versión: auditoría v1.3 del 2026-10-26, vinculada a la hoja rehecha el mismo día y al artículo `SHAK-2026-10-26`; no sustituye la auditoría posterior del usuario.
