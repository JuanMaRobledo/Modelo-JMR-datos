**Estado de publicación (2026-10-27): PUBLICADO CON SALVEDADES · revisión EPAM-REC-20261027-R1.** Estudio recuperado con corte del 30-sep-2026; sin cambios de supuestos, probabilidades ni pesos. Valoración, análisis fundamental y esta auditoría corresponden a la misma hoja de Google y a la misma revisión.

**Controles ejecutados el 27-oct-2026:** siete múltiplos con fórmula y resultado numérico (`verificar_multiplos_hoja.py`), fórmulas contra la maestra del 22-oct (`audit_master_formulas.py`), consistencia hoja = registro = análisis (`consistencia_migracion.py --hoja`), candados vigentes, probabilidades.

**Salvedades vigentes:**
- Estudio recuperado: precio y corte de información del 30-sep-2026; no incorpora resultados posteriores ni actualiza supuestos.
- Siete múltiplos calculados por las fórmulas originales de la hoja (7/7 con fórmula y resultado numérico; fórmulas de cálculo y múltiplos idénticas a la maestra del 22-oct-2026); P/V y P/BV con peso 0 y estado provisional.
- Candados de la plantilla del 21-oct (Financials Multiples!M34:M36) no aplican a la maestra vigente; se exigen solo los presentes en ella.

---

# Auditoría económica narrativa — EPAM Systems, Inc. (EPAM)

**Análisis fundamental vinculado:** [EPAM en la app](https://juanmarobledo.github.io/Modelo-JMR/research.html?ticker=EPAM) · registro `analisis/EPAM-research-1790597542389-2lrkz.json` (revisión del 2026-10-26).

## 1. Ficha de auditoría y alcance

| Campo | Contenido |
|---|---|
| Emisor | EPAM Systems, Inc.; ticker EPAM |
| Mercado, moneda y escala | NYSE (EE. UU.); US$ millones salvo por acción |
| Sector | Servicios de ingeniería de software y TI (Computer Services) (hoja: industria de Damodaran «Computer Services») |
| Método intrínseco principal | DCF FCFF de la historia Base (compañía operativa); MOS de 35 % sobre ese valor |
| Estados examinados | 10-K 2025 y 10-Q del 2T26 (balance al 30-jun-2026); LTM = FY2025 + 1S26 − 1S25 |
| Fecha de valoración / de auditoría | Corte de mercado 30-sep-2026 / 2026-10-26 |
| Precio del análisis | US$108,36 al cierre del 30-sep-2026 (corte común de la cartera); no se obtuvo un precio posterior |
| Hoja auditada | [Modelo JMR EPAM](https://docs.google.com/spreadsheets/d/1txQTjdUuzsnCem_4O1szofY7uAp5xLc3uda3l_iIcR0/edit), rehecha desde la maestra el 2026-10-26 |
| Artículo y Nivel 2 | `JMR-valuation/data/EPAM_Research_Fundamental_Modelo_JMR_2026-10-26.md` y `EPAM_Nivel2_Datos_Modelo_JMR_2026-10-26.md` |
| Registro en la app | Se publica con la autorización general del usuario; sin certificación previa (el usuario audita después) |
| Visto | Hoja completa por lectura; 10-Q del 2T26 por XBRL de companyfacts (balance, acciones en circulación); ficha de historias |
| Fuera de alcance | 10-K completo (factores de riesgo, concentración de clientes, litigios); transcripción de la llamada; 8-K posteriores al 10-Q; estados de los pares; consenso y calificaciones |
| Estado de verificación | **Con reservas** (no es una auditoría contable). Ver §15 y §17 |

## 2. Resumen ejecutivo y relato económico central

EPAM presta servicios de ingeniería de software, datos, nube e IA y cobra casi todo por tiempo y materiales. En el LTM a junio de 2026 facturó US$5.617 millones con margen bruto de 29,4 % y EBIT GAAP de US$563 millones (10,0 %); tiene caja de US$789 millones y deuda financiera de US$25 millones. El margen cayó de ~14 % en 2021 a 10 % y el crecimiento orgánico es de un dígito bajo. La Base de US$157,05 por acción supone ~5,5 % de crecimiento compuesto y recuperación del margen a 12 %, con ROIC terminal igual al costo de capital, y queda 45 % por encima del precio de US$108,36.

**Tesis Base favorable:** La IA compensa lo que quita: crecimiento moderado de ~5,5 % y margen que se recupera a 12 %: US$157,05 por acción. **Interpretación neutral:** Deflación de horas por IA: ingresos +2,1 % anual y margen de 10 %; la Conservadora (US$118,64, 20,0 %) describe esa ruta. **Contratesis adversa:** Los servicios se comoditizan: ingresos −1,1 % anual y margen de 8 % (Disrupción, US$87,49, 10,0 %).

El supuesto que domina el valor es la tasa de descuento (±1 punto de WACC mueve la Base US$139,82 (−11,0 %) / US$178,87 (+13,9 %)), seguido por la recuperación del margen operativo de 10 % a 12 % frente a la deflación de horas por IA. El precio (US$108,36) queda por debajo de la Base (-31 %); ver el DCF inverso en §10. Esta narrativa no se deriva del precio: parte de los estados de la compañía.

## 3. Trazabilidad, integridad y jerarquía de evidencia

Inventario de las celdas de entrada de `Input sheet`, `Cost of capital worksheet`, `R& D converter` y `Option value`, y de los datos que la hoja enlaza desde las pestañas de estados (Income Statement, Balance Sheet, Cash Flow Statement; columna L = LTM). `Financials Multiples` no tiene celdas de entrada propias: son fórmulas.

**Conteo:** la tabla tiene **85 filas** (todas las de `Input sheet` con valor, las entradas clave del costo de capital y el conversor de I+D). Las celdas con fórmula por defecto (`Input sheet!B27:B33`) se incluyen porque el analista puede sustituirlas.

**Cómo se cargaron los estados.** (a) El importador de la SEC (`desde_cero.sh datos`) cargó diez ejercicios y el LTM; (b) el balance del LTM repetía partidas de diciembre de 2025 y se reescribió con el 10-Q de junio de 2026 (caja 789,4, intangibles 373,0, crédito mercantil 1.203,0, patrimonio 3.519,3); (c) las cuentas por cobrar quedan dentro de «otros activos corrientes» como en la serie histórica; (d) las acciones son 51,587 M de la portada del 10-Q (31-jul-2026), escritas en Income Statement!L27; (e) los arrendamientos operativos pasan por el conversor con los compromisos del 10-K 2025; (f) ROIC terminal igual al costo de capital (B49 = No): la hoja anterior usaba 12,1 %.

**Diferencias de fuente y ajustes:** (a) acciones: 51,587 M de la portada frente a 56,2 M del promedio diluido de 2025; (b) el conversor usa compromisos del 10-K 2025 (gasto de 55,9) mientras la ficha cita compromisos al 30-jun-2026 (VP 120,8); (c) el interés minoritario (0,6) va en B21; (d) la hoja no suma como activo no operativo las inversiones sin precio de mercado (36,6).

| # | Pestaña | Celda | Rótulo | Valor | Tipo | Documento/fuente (URL en §18) | Quién lo aportó | Verificación |
|---:|---|---|---|---|---|---|---|---|
| 1 | Input sheet | B1 | EPAM Systems, Inc. (NYSE:EPAM) | EPAM Systems, Inc. (NYSE:EPAM) | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 2 | Input sheet | B4 | Date of valuation | sept-26 | Juicio | Corte de mercado 30-sep-2026 (fecha de valoración) | Corte común | [OBSERVADO] |
| 3 | Input sheet | B5 | Company name | EPAM Systems, Inc. | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 4 | Input sheet | B8 | Country of incorporation | United States | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 5 | Input sheet | B9 | Industry (US) | Computer Services | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 6 | Input sheet | B10 | Industry (Global) | Computer Services | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 7 | Input sheet | B12 | Revenues | $ 5.616,70 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 8 | Input sheet | B13 | Operating income or EBIT | $ 563,20 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 9 | Input sheet | B14 | Interest expense | $ - | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 10 | Input sheet | B15 | Book value of equity | $ 3.519,30 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 11 | Input sheet | B16 | Book value of debt | $ 25,00 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 12 | Input sheet | B17 | Do you have R&D expenses to capitalize? | No | Juicio | Capitalización de I+D según la regla del sector de la empresa | IA | Decisión de método; ver hallazgos |
| 13 | Input sheet | B18 | Do you have operating lease commitments? | Yes | Juicio | Arrendamientos operativos como deuda (conversor de Damodaran) | IA | [MODELO] |
| 14 | Input sheet | B19 | Cash and Marketable Securities | $ 789,40 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 15 | Input sheet | B20 | Valor económico validado de participaciones y activos NO ope | $ - | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 16 | Input sheet | B21 | Minority interests | $ 0,60 | Dato | Interés minoritario de US$0,6 M (10-Q 2T26) | IA | Coincide [OBSERVADO] |
| 17 | Input sheet | B22 | Number of shares outstanding = | 51,59 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 18 | Input sheet | B23 | Current stock price = | $ 108,36 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 19 | Input sheet | B24 | Effective tax rate = | 26,80% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 20 | Input sheet | B25 | Marginal tax rate = | 24,00% | Juicio | Tasa marginal federal más estatal de EE. UU. (25 %) | Plantilla/IA | Convención del modelo [MODELO] |
| 21 | Input sheet | B27 | Revenue growth rate for next year  | 5,63% | Juicio | Crecimiento del año 1 de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 22 | Input sheet | B28 | Operating Margin for next year | 11,07% | Juicio | Margen operativo del año 1 de la Base: 10,5 % más el ajuste de arrendamientos (0,57 pp) | IA (ficha de historias) | [HIPÓTESIS]; ver H-01 |
| 23 | Input sheet | B29 | Compounded annual revenue growth rate - years 2-5 = | 5,52% | Juicio | CAGR de los años 2-5 de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 24 | Input sheet | B30 | Referencia de margen objetivo (mediana histórica/sectorial;  | 12,57% | Juicio | Margen objetivo de la Base: 12,0 % más el ajuste de arrendamientos; el texto de la ficha cita 12,5 % | IA | [HIPÓTESIS]; ver H-01 |
| 25 | Input sheet | B31 | Year of convergence for margin | 5,00 | Juicio | Año de convergencia del margen: 5 | Plantilla/IA | Coherente con las historias |
| 26 | Input sheet | B32 | Sales to capital ratio  (for years 1-5) | 3,27 | Juicio | Ventas/capital años 1-5 (ficha de historias, ajustado por el conversor de arrendamientos) | IA | [HIPÓTESIS]; ver hallazgos |
| 27 | Input sheet | B33 | Sales to capital ratio (for years 6-10) | 2,83 | Juicio | Ventas/capital años 6-10 (ficha de historias, ajustado por el conversor de arrendamientos) | IA | [HIPÓTESIS]; ver hallazgos |
| 28 | Input sheet | B35 | Riskfree rate | 5,29% | Dato | Treasury a 10 años del corte común (30-sep-2026): 5,29 % | Corte común (datos_mercado.py) | [OBSERVADO] FRED DGS10 |
| 29 | Input sheet | B36 | Initial cost of capital = | 9,73% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 30 | Input sheet | B38 | Do you have employee options outstanding? | No | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 31 | Input sheet | B39 | Number of options outstanding = | 0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 32 | Input sheet | B40 | Average strike price = | $0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 33 | Input sheet | B41 | Average maturity = | 0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 34 | Input sheet | B42 | Standard deviation on stock price = | 0,00% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 35 | Input sheet | B46 | Do you want to override this assumption = | No | Juicio | No se anula el WACC terminal: converge a la fórmula de la plantilla | Plantilla | [MODELO] |
| 36 | Input sheet | B47 | If yes, enter the cost of capital after year 10 = | 9,73% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 37 | Input sheet | B49 | Do you want to override this assumption = | No | Juicio | ROIC terminal igual al costo de capital (regla vigente); la hoja anterior aplicaba 12,1 % | IA | [HIPÓTESIS]; ver H-02 |
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
| 55 | Input sheet | B79 | Pasivo de arrendamientos INCREMENTAL no reconocido | $ 119,96 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 56 | Input sheet | B80 | Ajuste de EBIT atribuible a pasivos incrementales | 31,9438791 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 57 | Input sheet | B81 | Estado de conciliación de arrendamientos | CONCILIADO | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 58 | Input sheet | B82 | Inversiones a largo plazo según balance (dato histórico; NO  | $0 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 59 | Input sheet | B83 | Valor CONTABLE de inversiones excluidas del capital operativ | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 60 | Input sheet | B84 | Valor ECONÓMICO atribuible de participaciones y activos no o | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 61 | Input sheet | B85 | Control de inversiones y doble contabilización | VALIDADO | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 62 | Input sheet | B86 | Revisión: no están incluidas en EBIT/FCFF ni duplicadas | Sin solapamiento | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 63 | Input sheet | B87 | Fuente y conciliación de inversiones no operativas | 10-Q 2T26: inversiones en valores sin precio de mercado fáci | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 64 | Input sheet | B89 | Método fiscal de proyección (obligatorio en cada copia) | Convergencia Damodaran | Juicio | Convergencia Damodaran: tasa efectiva del LTM que converge a la marginal de 24 % | IA | [INFERENCIA] |
| 65 | Input sheet | B91 | Fuente / conciliación de impuesto efectivo vs marginal | Tasa efectiva del LTM de la hoja (L29) que converge a la mar | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 66 | Input sheet | B92 | Control de hipótesis fiscales | VALIDADO | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 67 | Input sheet | B93 | Impuesto inicial para pronóstico (no altera la tasa históric | 26,80% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 68 | Input sheet | B96 | Tasa libre de riesgo nominal de largo plazo · misma moneda d | 5,29% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 69 | Input sheet | B97 | WACC terminal efectivo del modelo (independiente del DCF hab | 8,99% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 70 | Input sheet | B98 | Base | Sin liberación | Juicio | Sin liberación de capital en contracción (reinversión negativa se trunca a cero) | IA | Regla de Damodaran |
| 71 | Input sheet | B99 | Conservadora | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 72 | Input sheet | B100 | Disrupción | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 73 | Input sheet | B101 | Optimista | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 74 | Cost of capital worksheet | B12 | Which approach will you be using? | Detailed | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 75 | Cost of capital worksheet | B22 | Approach for estimating beta | Direct Input | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 76 | Cost of capital worksheet | B26 | What approach do you want to use to input ERP? | Operating regions | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 77 | Cost of capital worksheet | B33 | Average Maturity = | 5 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 78 | Cost of capital worksheet | B34 | Approach for estimating pre-tax cost of debt | Actual rating | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 79 | Cost of capital worksheet | B36 | If actual rating, input the rating | A2/A | Dato | Calificación crediticia A2/A | IA | [NO VERIFICADO] en esta revisión |
| 80 | Cost of capital worksheet | B41 | Book Value of Convertible Debt = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 81 | Cost of capital worksheet | B49 | Number of Preferred Shares = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 82 | Cost of capital worksheet | B50 | Current Market Price per Share= | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 83 | Cost of capital worksheet | B51 | Annual Dividend per Share = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 84 | Cost of capital worksheet | H29 | Ingresos H29 | $2.834 | Dato | Ventas de 2025 en Norteamérica: 2.834,3 (10-K 2025) | IA | Coincide [OBSERVADO] |
| 85 | R& D converter | F7 | Años de amortización del I+D | 3 | Juicio | Convención de Damodaran para la industria | IA | [MODELO] |

**Jerarquía de evidencia usada:** [OBSERVADO] (documento de la compañía o comprobación directa), [INFERENCIA] (deducción de lo observado), [HIPÓTESIS] (supuesto del analista), [MODELO] (resultado de las fórmulas) y [NO VERIFICADO].

## 4. Historia financiera: diez años y punto de partida

| US$ millones | Dec '20 | Dec '22 | Dec '23 | Dec '24 | Dec '25 | LTM |
|---|---:|---:|---:|---:|---:|---:|
| Ingresos | 2.660 | 4.825 | 4.690 | 4.728 | 5.457 | 5.617 |
| EBIT | 379 | 573 | 501 | 545 | 520 | 563 |
| Margen operativo | 14,3 % | 11,9 % | 10,7 % | 11,5 % | 9,5 % | 10,0 % |
| Flujo operativo | 544 | 464 | 563 | 559 | 655 | 539 |
| Capex | -69 | -82 | -28 | -32 | -42 | -56 |
| Capex / ventas | 2,6 % | 1,7 % | 0,6 % | 0,7 % | 0,8 % | 1,0 % |

La historia tiene tres fases. Entre 2016 y 2021 EPAM creció 16-41 % al año con margen operativo de 12-14 % y la acción llegó a US$668. En 2022-2024 la guerra en Ucrania obligó a reubicar ingenieros, el gasto discrecional cayó y los ingresos se estancaron (−2,8 % en 2023, +0,8 % en 2024). En 2025 el crecimiento volvió a +15,4 % por compras y en el 2T26 fue +4,5 % con Europa +10 %. La Base supone que la IA compensa lo que quita (crecimiento de ~5,5 % y margen que sube a 12 %); la Conservadora, deflación de horas; la Disrupción, comoditización.

## 5. Crecimiento de ingresos: de la historia a la proyección

La Base construye el ingreso por cubeta (Norteamérica US$3.200 millones; Europa US$2.250 millones; Otros mercados US$167 millones). El resultado consolidado es 5,6 %, 5,8 %, 5,4 %, 5,4 %, 5,4 % en los años 1-5 (5,5 % compuesto) y cae a 4,0 % en el año 10: ingresos de 7.355 millones en el año 5 y 9.195 millones en el año 10.

Por qué ese ritmo: [INFERENCIA] el primer año de la Base (5,6 %) sigue el +6 % del 1S26 con Norteamérica de 4 % a 5 % y Europa de 8 % bajando a 6 %; no extrapola el +15,4 % de 2025, comprado. La visión externa ubica 5,5 % compuesto en el tramo donde ~60 % de las empresas de su tamaño lo logró. Dos trimestres de crecimiento orgánico negativo invalidarían la Base. Duda: el 1S26 puede incluir efectos de compras y divisas.

Alternativas: la Conservadora (2,1 % compuesto, año 1 de 1,6 %); la Optimista (8,6 %, año 1 de 8,8 %); la Disrupción (-1,1 %, con crecimiento terminal de 1 %). Los porcentajes son juicio del analista, no una guía publicada por la compañía.

## 6. Márgenes operativos y normalización de beneficios

La Base lleva el margen de 11,1 % en el año 1 a 12,6 % en el año 5 (ya ajustado por I+D capitalizado y arrendamientos; en base reportada 12,0 %). La Conservadora llega a 10,6 % (10,0 % reportado), la Disrupción a 8,6 % y la Optimista a 14,6 % (14,0 % reportado). Tasa impositiva: 26,8 % al inicio, convergiendo a la marginal de 24 % en el año 10.

Por qué ese margen: [OBSERVADO] el margen GAAP pasó de ~14 % en 2021 a 9,5 % en 2025 y 10,0 % en el LTM. La Base lo recupera a 12 %, la apuesta más frágil: si la IA reduce las horas, el margen difícilmente sube salvo que suban las tarifas. Sensibilidad: ±2 puntos de margen dan US$134,66 y US$179,44 (±14,3 %), más que ±2 puntos de crecimiento (−7,8 % / +8,6 %).

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

La reinversión de la Base es de 106 millones en el año 1 (frente a un NOPAT de 481 millones) y el FCFF del año 1 es de 375 millones. El ventas/capital es 3,27 en los años 1-5 y 2,83 en los 6-10 (base de la hoja, que incluye I+D y arrendamientos cuando la empresa los capitaliza). Con ±20 % en el ancla, el DCF Base va de US$153,51 (−2,3 %) a US$159,41 (+1,5 %). ROIC terminal: Base 9,0 %, Conservadora 9,0 %, Disrupción 9,0 %, Optimista 9,0 %.

Evidencia: capex de ~US$40-56 millones al año y ventas/capital de 3,27 (años 1-5) y 2,83 (años 6-10), valores heredados de la hoja anterior. El motor avisa que el capital nuevo rinde más del doble del ROIC terminal (9 %) en la Conservadora y la Optimista: ver H-03. ±20 % en el ventas/capital mueve la Base de US$153,51 a US$159,41.

## 8. Costo del capital y riesgo

Tasa libre de riesgo 5,29 % (Treasury a 10 años al 30-sep-2026), prima de riesgo de 4,66 % (ponderada por regiones de ingresos), beta desapalancada del sector 0,96 y beta apalancada 0,98 (propuesta bottom-up 0,98). WACC inicial 9,73 %; WACC terminal 8,99 %.

Dudas: (i) la beta de 0,98 es bottom-up del sector y no recoge el riesgo de entrega desde Europa del Este, que va en la prima de mercado ponderada por regiones; (ii) la prima ponderada usa los ingresos de 2025 por región; (iii) la deuda tiene calificación A2/A (no verificada). ±1 punto de tasa da US$178,87 (+13,9 %) y US$139,82 (−11,0 %).

Efecto: ±1 punto de WACC mueve la Base US$139,82 (−11,0 %) / US$178,87 (+13,9 %), el supuesto de mayor peso. La plantilla hace converger el WACC de 9,73 % a 8,99 % en el año 10 (convención de Damodaran).

## 9. Convergencia y valor terminal

El valor terminal es 54,9 % del valor de los activos operativos de la Base (4.096 millones de 7.458 millones). Crecimiento terminal 4,00 % (≤ la tasa libre), ROIC terminal 9,0 % y WACC terminal 8,99 %. Con −0,5 puntos de crecimiento terminal la Base vale US$155,88 (−0,7 %); con +0,5 puntos, US$158,24 (+0,8 %).

Riesgos: (i) las cuatro historias usan ROIC terminal igual al costo de capital (9 %); con 12,1 % (hoja anterior) la Base valdría ~US$173, +10 %; (ii) el crecimiento terminal de 4 % (1 % en la Disrupción) es menor que la tasa libre de riesgo; (iii) el terminal pesa más de la mitad del valor operativo.

## 10. Validación independiente del valor intrínseco

Comprobación 1 (identidad): la hoja y el motor independiente del repositorio coinciden en las cuatro historias (Base 157,05; Conservadora 118,64; Disrupción 87,49; Optimista 204,43), lo que valida la aritmética, no la economía. Comprobación 2 (puente): activos operativos 7.458 + caja 789 − deuda con arrendamientos 145 − opciones 0 − preferentes 0 + no operativos 0 = patrimonio común de 8.102 millones, o US$157,05 por acción con 51,6 millones de acciones. Comprobación 3 (DCF inverso del Nivel 2, margen → crecimiento anual de los años 1-5 que justifica el precio):

| Beta | Margen | Crecimiento anual de los años 1-5 que justifica el precio | Fracción de empresas de este tamaño que lo logra |
|---|---:|---:|---:|
| 0,98 | 9,6% | 1,8% | 81,3% |
| 0,98 | 11,1% | -1,1% | 89,7% |
| 0,98 | 13,1% | -3,8% | 94,5% |
| 0,98 | 9,6% | 1,8% | 81,3% |
| 0,98 | 11,1% | -1,1% | 89,7% |
| 0,98 | 13,1% | -3,8% | 94,6% |

Comprobación 4 (múltiplos propios): los 25-40× el EBITDA de 2019-2021 corresponden al hipercrecimiento; la regla por ciclo lleva la Base a 7,0× (EV/EBITDA), 9,8× (EV/FCFF) y 14,2× (P/E), iguales o cercanos a los actuales, con pares de servicios de TI (Accenture, Globant, Cognizant, Infosys, EXL, Wipro). Ningún múltiplo salta más de 25 % sobre el actual.

## 11. Cuatro historias y probabilidades

| Historia | Probabilidad | CAGR 1-5 | Margen objetivo (ajustado / reportado) | ROIC terminal | g terminal | DCF por acción |
|---|---:|---:|---:|---:|---:|---:|
| Base · La IA compensa lo que quita: crecimiento moderado | 50,0 % | 5,5 % | 12,6 % / 12,0 % | 9,0 % | 4,0 % | US$157,05 |
| Conservadora · Deflación de horas por IA | 20,0 % | 2,1 % | 10,6 % / 10,0 % | 9,0 % | 4,0 % | US$118,64 |
| Disrupción · Deterioro de los fundamentales | 10,0 % | -1,1 % | 8,6 % / 8,0 % | 9,0 % | 1,0 % | US$87,49 |
| Optimista · La IA crea demanda de ingeniería | 20,0 % | 8,6 % | 14,6 % / 14,0 % | 9,0 % | 4,0 % | US$204,43 |

Las probabilidades salen de la regla del ciclo (madura_estable) y no se ajustaron por indicadores: son un juicio condicional, no frecuencias observadas. El DCF esperado de las tres historias activas (pesos renormalizados) es US$159,04; con MOS de 35 % sobre el DCF Base el precio de compra es US$102,08. Cambiar los pesos cambia el esperado, no el DCF Base.

### ¿Qué pasaría si todo fallara?

Si la deflación de horas se materializa (ingresos +2,1 % y margen de 10 %), la acción vale la Conservadora (US$118,64), por encima del precio; si además los servicios se comoditizan (ingresos −1,1 % y margen de 8 %), vale la Disrupción (US$87,49), 19 % por debajo. El balance (caja de US$789 millones frente a deuda de US$25 millones) limita el riesgo financiero.

## 12. Valoración por múltiplos: prueba independiente y secundaria

Siete métodos (EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF, P/V y P/BV; los dos últimos con peso cero). Regla del 18-oct-2026: el múltiplo de cada escenario es el que la empresa tuvo cuando crecía como el escenario espera en FY+3 (Conservador 2,4 %, Base 5,4 %, Optimista 9,0 %), llevado al costo de capital del corte y limitado por el múltiplo justificado por los fundamentos de la misma historia; los comparables solo comprueban.

| Método | Mediana histórica 10a | Actual (LTM) | Ancla de peers (mediana) | Justificado Base | Peso en múltiplos |
|---|---:|---:|---:|---:|---:|
| EV/EBITDA | 25,49× | 7,00× | 8,14× | 10,50× | 33 % |
| EV/FCFF | 28,30× | 10,00× | 10,25× | 20,85× | 17 % |
| P/E | 44,20× | 15,16× | 13,40× | 14,22× | 33 % |
| P/FCFE | 32,17× | 11,58× | 9,81× | 19,15× | 8 % |
| P/OCF | 29,84× | 10,37× | 8,97× | 17,55× | 8 % |

Resultado: múltiplos consolidados de US$88,39 (Conservador), US$104,03 (Base) y US$123,15 (Optimista), frente a DCF de US$118,64, US$157,05 y US$204,43. Lectura del 30-sep-2026: el DCF (valor intrínseco) da US$168,22 por acción y los múltiplos, US$109,37 hoy: 35% por debajo del DCF, fuera del rango de ±25%. Los múltiplos reflejan lo que el mercado paga hoy por los servicios de TI bajo el temor a la IA (~7-9x EBITDA); el DCF supone que EPAM vuelve a crecer y a recuperar margen. Si la presión de los asistentes de código resulta estructural, los múltiplos son la referencia más prudente.

La Base de los múltiplos (US$104,03) queda 34 % por debajo del DCF Base (US$157,05) y cerca del precio: la regla por ciclo lleva el múltiplo al actual y el DCF supone que el margen se recupera. Ningún múltiplo salta más de 25 % sobre el actual. Ver H-05.

## 13. Sensibilidades económicas y escenarios alternativos

| Supuesto cambiado (DCF Base US$157,05) | Valor |
|---|---:|
| WACC +1 pp / −1 pp | US$139,82 (−11,0 %) / US$178,87 (+13,9 %) |
| Crecimiento años 1-5 −2 pp / +2 pp | US$144,86 (−7,8 %) / US$170,51 (+8,6 %) |
| Margen objetivo −2 pp / +2 pp | US$134,66 (−14,3 %) / US$179,44 (+14,3 %) |
| Crecimiento terminal −0,5 pp / +0,5 pp | US$155,88 (−0,7 %) / US$158,24 (+0,8 %) |
| Ventas/capital −20 % / +20 % | US$153,51 (−2,3 %) / US$159,41 (+1,5 %) |

Ordenado por impacto: la tasa de descuento (±1 punto: +13,9 % / −11,0 %), el margen objetivo (±2 puntos: ±14,3 %), el crecimiento de los años 1-5 (±2 puntos: −7,8 % / +8,6 %), la dilución adicional de 5 % (−4,8 %) y el ventas/capital (±20 %: −2,3 % / +1,5 %). Las matrices del Nivel 2 recogen crecimiento por margen.

## 14. Coherencia de hojas, cálculos y presentación

La hoja está unificada con la maestra (61 pestañas en el mismo orden, 21.258 fórmulas intactas, 122 selectores idénticos) y el motor independiente reproduce las cuatro historias. Controles: candados 15/15, inputs completos, estados completos e integridad de hojas (registro en la bitácora de la sesión).

Intervenciones sobre la hoja que el lector debe conocer: (i) se restauraron las fórmulas de la maestra tras cada carga; (ii) el importador traía partidas de diciembre de 2025 en el LTM y se reescribió con el 10-Q de junio de 2026; (iii) las acciones y el patrimonio se llevaron a celdas que sobreviven a la restauración; (iv) se revirtió el ROIC terminal de 12,1 % a la regla vigente y la hoja ahora coincide con el motor en las cuatro historias.

## 15. Hallazgos priorizados y propuestas de corrección

| ID | Severidad | Hallazgo | Impacto | Propuesta |
|---|---|---|---|---|
| H-01 | Alta | La recuperación del margen de 10 % a 12 % es la apuesta más frágil de la Base (el texto de la ficha cita 12,5 %, la hoja usa 12,0 %) | ±2 puntos de margen mueven la Base ±14,3 %; con la IA reduciendo horas el margen difícilmente sube | Contrastar con la trayectoria de márgenes de pares de TI en periodos de presión de tarifas y alinear el texto de la ficha |
| H-02 | Alta | La hoja anterior aplicaba ROIC terminal de 12,1 % (punto medio entre costo de capital y ROIC actual); esta edición lo revierte al costo de capital | Con 12,1 % la Base valdría ~US$173 (+10 %) y la Optimista ~US$227 | Decidir si EPAM tiene una ventaja que justifique retornos excedentes después del año 10 |
| H-03 | Media | Ventas/capital de 3,27 y 2,83, heredados de la hoja anterior, hacen que el capital nuevo rinda más del doble del ROIC terminal en la Conservadora (21 %) y la Optimista (36 %) | Posible sobrevaloración del flujo; ±20 % mueve la Base −2,3 % / +1,5 % | Recalcular el ventas/capital marginal con el crédito mercantil de las compras |
| H-04 | Media | El balance del LTM se escribió a mano desde el 10-Q; las cuentas por cobrar quedan dentro de otros activos corrientes | Un error de transcripción cambia la caja neta y el valor por acción | Releer el balance del 10-Q y conciliar fila por fila |
| H-05 | Media | Los múltiplos de la Base (US$104,03) quedan 34 % por debajo del DCF Base y el 60 % del ponderado secundario depende de ellos | El ponderado secundario (US$125,24) queda por debajo del DCF principal | Revisar las anclas de pares y de la historia propia en etapa de crecimiento de un dígito |
| H-06 | Media | La caja bajó de US$2.097 a US$789 millones y las acciones de 57,8 a 51,6 millones entre 2023 y julio de 2026 por compras y recompras | Si las recompras se hicieron a precios altos, destruyeron valor; la hoja no las modela | Conciliar usos de caja con el flujo de financiación del 10-Q |
| H-07 | Media | La beta de 0,98 es bottom-up del sector y el riesgo de entrega desde Europa del Este solo entra en la prima de mercado | ±1 punto de tasa mueve la Base +13,9 % / −11,0 % | Documentar la ponderación regional y comparar con la beta de regresión |
| H-08 | Baja | El conversor de arrendamientos usa los compromisos del 10-K 2025 y la ficha cita los del 10-Q (VP de 120,8) | Efecto menor a 1 % en la Base | Actualizar el calendario con el 10-Q |
| H-09 | Baja | Las inversiones sin precio de mercado (US$36,6 millones) no se suman como activo no operativo | Menos de US$1 por acción | Revisar su naturaleza y valor razonable |
| H-10 | Media | La composición de los competidores y de la dirección proviene de conocimiento general y no se contrastó con documentos | Afecta las secciones 7 y 8 del análisis | Verificar con el 10-K y los informes de las compañías |
| H-11 | Media | La concentración de clientes y los 8-K posteriores al 10-Q no se revisaron | Puede ocultar riesgos de pérdida de un cliente grande | Leer la nota de concentración del 10-K y los 8-K de agosto a octubre de 2026 |
| H-12 | Baja | Los pagos en acciones (US$186 millones, 3,3 % de las ventas) se tratan como costo dentro del EBIT | Si se excluyeran, el margen se sobrestimaría ~3 puntos | Verificar la línea en el estado de resultados |
| H-13 | Media | El precio (US$108,36) queda 31 % por debajo del DCF Base y 9 % por debajo de la Conservadora; el DCF inverso solo exige ~1,8 % anual con margen de 10 % | El mercado descuenta que el margen no se recupera o que la IA reduce los ingresos | Decidir si la Conservadora merece más probabilidad que 20 % |

## 16. Catalizadores, señales de refutación y seguimiento

| Indicador | Último dato | Confirma Base u Optimista | Favorece Conservadora o Disrupción |
|---|---|---|---|
| Crecimiento de ingresos (orgánico, sin divisas) | +4,5% (2T26) | ≥ +6% | Negativo dos trimestres |
| Margen operativo GAAP | 10,0% LTM | ≥ 11% | < 9% |
| Norteamérica (interanual) | Bajo un dígito | ≥ +5% | Negativo |
| Utilización de ingenieros | Estable | En alza | En baja |
| Ingresos de proyectos de IA y datos | En aumento | Más de 20% de los ingresos | Estancados |

Indicadores de actualización de probabilidades: si el crecimiento orgánico es negativo dos trimestres o el margen baja de 9 % sube la Conservadora (y la Disrupción); si Norteamérica crece ≥ 5 % y el margen supera 11 % en 2027 sube la Base; si los ingresos de proyectos de IA y datos superan 20 % sube la Optimista. Próximo hito: resultados del 3T26 (nov-2026).

## 17. Dictamen económico y resumen para escuchar

**Dictamen: con reservas.** La hoja está bien formada, reproduce el motor en las cuatro historias y quedó UNIFICADA con la maestra; el balance del LTM se reescribió con el 10-Q del 2T26. Los supuestos que dominan el valor (recuperación del margen a 12 % y ROIC terminal) son hipótesis del analista, y el precio descuenta un escenario peor que la Base. El ventas/capital heredado y la elección del ROIC terminal son los puntos técnicos a revisar primero.

Resumen para escuchar: EPAM es una empresa de ingeniería de software con balance sin deuda y flujo libre de casi 500 millones de dólares. La Base de 157 dólares por acción queda 31 por ciento sobre el precio y supone que el margen se recupera de 10 a 12 por ciento. Lo que más mueve el valor es el margen y la amenaza de la inteligencia artificial sobre las horas facturables.

## 18. Fuentes primarias, limitaciones y registro de versión

Fuentes primarias:

- [EPAM, Form 10-Q del 2T 2026](https://www.sec.gov/Archives/edgar/data/1352010/000135201026000046/epam-20260630.htm)
- [EPAM, Form 10-Q del 1T 2026](https://www.sec.gov/Archives/edgar/data/1352010/000135201026000029/epam-20260331.htm)
- [EPAM, Form 10-K 2025](https://www.sec.gov/Archives/edgar/data/1352010/000135201026000015/epam-20251231.htm)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)

Limitaciones: no es una auditoría contable; no se revisaron el 10-K completo, la concentración de clientes ni los 8-K posteriores al 10-Q; los competidores y la dirección se describen con conocimiento general; el consenso y las calificaciones no se verificaron. Registro de versión: auditoría v1.3 del 2026-10-26, vinculada a la hoja rehecha el mismo día y al artículo `EPAM-2026-10-26`; no sustituye la auditoría posterior del usuario.
