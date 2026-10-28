**Comprobación adicional independiente (27-oct-2026):** lectura directa de la hoja Google nativa y contraste con el registro **activo**, no con `reference/damodaran/*_resultado.json` histórico. Las cuatro historias DCF (`Escenarios e historias!H5:H8`) son idénticas, sin diferencia numérica, a `valorEsperado.historias` (A=Base, B=Conservadora, C=Disrupción, D=Optimista) del registro publicado. `Valuation output!B35` coincide exactamente con `valorPrincipal`. Se confirmó que `Valuation output!C46` enlaza el margen Base con `Escenarios e historias!D5`. **Los 1 hallazgos consignados frente al motor antiguo son un antecedente, no evidencia de una divergencia DCF vigente; el control integral nuevo aún debe ejecutarse para clasificar cualquier otra anomalía.** No se tocaron supuestos ni resultados.

**Estado de publicación (2026-10-27): PUBLICADO CON SALVEDADES · revisión BSX-REC-20261027-R1.** Estudio recuperado con corte del 30-sep-2026; sin cambios de supuestos, probabilidades ni pesos. Valoración, análisis fundamental y esta auditoría corresponden a la misma hoja de Google y a la misma revisión.

**Controles ejecutados el 27-oct-2026:** siete múltiplos con fórmula y resultado numérico (`verificar_multiplos_hoja.py`), fórmulas contra la maestra del 22-oct (`audit_master_formulas.py`), consistencia hoja = registro = análisis (`consistencia_migracion.py --hoja`), candados vigentes, probabilidades.

**Salvedades vigentes:**
- Estudio recuperado: precio y corte de información del 30-sep-2026; no incorpora resultados posteriores ni actualiza supuestos.
- Siete múltiplos calculados por las fórmulas originales de la hoja (7/7 con fórmula y resultado numérico; fórmulas de cálculo y múltiplos idénticas a la maestra del 22-oct-2026); P/V y P/BV con peso 0 y estado provisional.
- Candados de la plantilla del 21-oct (Financials Multiples!M34:M36) no aplican a la maestra vigente; se exigen solo los presentes en ella.

**Salvedad resuelta (27-oct-2026):** Integridad de hojas: los hallazgos eran la comparación con el motor legado (30-sep) y registros sin `escenariosDCF`; con `escenariosDCF` (historias A-D) tomado de la hoja, `integridad_hojas.py` da 0 hallazgos en las ocho (27-oct-2026).

---

# Auditoría económica narrativa — Boston Scientific Corporation (BSX)

**Análisis fundamental vinculado:** [BSX en la app](https://juanmarobledo.github.io/Modelo-JMR/research.html?ticker=BSX) · registro `analisis/BSX-research-1790597191582-gnvjr.json` (revisión del 2026-10-26).

## 1. Ficha de auditoría y alcance

| Campo | Contenido |
|---|---|
| Emisor | Boston Scientific Corporation; ticker BSX |
| Mercado, moneda y escala | NYSE (EE. UU.); US$ millones salvo por acción |
| Sector | Dispositivos médicos cardiovasculares y MedSurg (Healthcare Products) (hoja: industria de Damodaran «Healthcare Products») |
| Método intrínseco principal | DCF FCFF de la historia Base (compañía operativa); MOS de 35 % sobre ese valor |
| Estados examinados | 10-K 2025 y 10-Q del 2T26 (balance al 30-jun-2026); LTM = FY2025 + 1S26 − 1S25 |
| Fecha de valoración / de auditoría | Corte de mercado 30-sep-2026 / 2026-10-26 |
| Precio del análisis | US$43,65 al cierre del 30-sep-2026 (corte común de la cartera); no se obtuvo un precio posterior |
| Hoja auditada | [Modelo JMR BSX](https://docs.google.com/spreadsheets/d/1LVn63SMyvovWzNjbF5Jdi-v0EFUPXLqp4A6n8gwbKHc/edit), rehecha desde la maestra el 2026-10-26 |
| Artículo y Nivel 2 | `JMR-valuation/data/BSX_Research_Fundamental_Modelo_JMR_2026-10-26.md` y `BSX_Nivel2_Datos_Modelo_JMR_2026-10-26.md` |
| Registro en la app | Se publica con la autorización general del usuario; sin certificación previa (el usuario audita después) |
| Visto | Hoja completa por lectura; 10-Q del 2T26 por XBRL de companyfacts (balance, acciones en circulación, recompra); comunicado del 2T26, 8-K del 27-jul, 26-ago y 8-sep-2026; ficha de historias |
| Fuera de alcance | 10-K completo (factores de riesgo y litigios); transcripción de la llamada del 2T26; detalle de la compra de Penumbra; estados de los pares; consenso y calificaciones |
| Estado de verificación | **Con reservas** (no es una auditoría contable). Ver §15 y §17 |

## 2. Resumen ejecutivo y relato económico central

Boston Scientific vende dispositivos de un solo uso para procedimientos mínimamente invasivos, sobre todo cardiovasculares. En el LTM a junio de 2026 facturó US$20.996 millones con margen bruto de 69,9 % y EBIT GAAP de US$4.152 millones (19,8 %). Tras crecer 12-20 % en 2023-2025 por FARAPULSE, Watchman y compras, el orgánico bajó a 7 % en el 2T26 y un ciberataque en agosto de 2026 llevó a retirar la guía. La Base de US$33,12 por acción supone ~6 % de crecimiento compuesto y un margen GAAP de 24 %, y queda 24 % por debajo del precio de US$43,65.

**Tesis Base favorable:** La cartera diversificada sostiene ~6 % anual y el margen GAAP sube a 24 %: US$33,12 por acción. **Interpretación neutral:** El campo pulsado se vuelve commodity: ingresos +3,7 % anual y margen de 22 %; la Conservadora (US$26,31, 22,5 %) describe esa ruta. **Contratesis adversa:** Pierde participación y precio: ingresos +1,8 % anual y margen de 20 % (Disrupción, US$20,62, 10,0 %).

El supuesto que domina el valor es la tasa de descuento (±1 punto de WACC mueve la Base US$28,00 (−15,4 %) / US$39,60 (+19,6 %)), seguido por el margen GAAP de 24 % y el crecimiento de Electrofisiología y Watchman tras la llegada de competidores. El precio (US$43,65) queda por encima de la Base (32 %); ver el DCF inverso en §10. Esta narrativa no se deriva del precio: parte de los estados de la compañía.

## 3. Trazabilidad, integridad y jerarquía de evidencia

Inventario de las celdas de entrada de `Input sheet`, `Cost of capital worksheet`, `R& D converter` y `Option value`, y de los datos que la hoja enlaza desde las pestañas de estados (Income Statement, Balance Sheet, Cash Flow Statement; columna L = LTM). `Financials Multiples` no tiene celdas de entrada propias: son fórmulas.

**Conteo:** la tabla tiene **86 filas** (todas las de `Input sheet` con valor, las entradas clave del costo de capital y el conversor de I+D). Las celdas con fórmula por defecto (`Input sheet!B27:B33`) se incluyen porque el analista puede sustituirlas.

**Cómo se cargaron los estados.** (a) El importador de la SEC (`desde_cero.sh datos`) cargó diez ejercicios y el LTM; (b) el balance del LTM repetía partidas de diciembre de 2025 y se reescribió con el 10-Q de junio de 2026 (deuda corriente de 1.709, deuda de largo plazo de 10.915, patrimonio de 24.930); (c) las cuentas por cobrar (3.049) se separaron de «otros activos corrientes»; (d) las acciones son 1.449,2 M de la portada del 10-Q, tras la recompra acelerada de US$2.000 M de mayo de 2026, y se escriben en Income Statement!L27; (e) los arrendamientos operativos pasan por el conversor (gasto de 117 y calendario del 10-K 2025).

**Diferencias de fuente y ajustes:** (a) acciones: 1.449,2 M de la portada frente a 1.494,5 M del promedio diluido de 2025; (b) la tasa de impuestos del LTM (5 %) se reemplaza por 17,8 % en B90; (c) el patrimonio de la hoja (24.930) excluye el interés minoritario (242), que va en B21; (d) la hoja no suma como activo no operativo las inversiones por el método de la participación (1.308) ni otras inversiones (2.245).

| # | Pestaña | Celda | Rótulo | Valor | Tipo | Documento/fuente (URL en §18) | Quién lo aportó | Verificación |
|---:|---|---|---|---|---|---|---|---|
| 1 | Input sheet | B1 | BOSTON SCIENTIFIC CORP (NYSE:BSX) | BOSTON SCIENTIFIC CORP (NYSE:BSX) | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 2 | Input sheet | B4 | Date of valuation | sept-26 | Juicio | Corte de mercado 30-sep-2026 (fecha de valoración) | Corte común | [OBSERVADO] |
| 3 | Input sheet | B5 | Company name | BOSTON SCIENTIFIC CORP | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 4 | Input sheet | B8 | Country of incorporation | United States | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 5 | Input sheet | B9 | Industry (US) | Healthcare Products | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 6 | Input sheet | B10 | Industry (Global) | Healthcare Products | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 7 | Input sheet | B12 | Revenues | $ 20.996,00 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 8 | Input sheet | B13 | Operating income or EBIT | $ 4.152,00 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 9 | Input sheet | B14 | Interest expense | $ 363,00 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 10 | Input sheet | B15 | Book value of equity | $ 25.172,00 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 11 | Input sheet | B16 | Book value of debt | $ 12.624,00 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 12 | Input sheet | B17 | Do you have R&D expenses to capitalize? | No | Juicio | Capitalización de I+D según la regla del sector de la empresa | IA | Decisión de método; ver hallazgos |
| 13 | Input sheet | B18 | Do you have operating lease commitments? | Yes | Juicio | Arrendamientos operativos como deuda (conversor de Damodaran) | IA | [MODELO] |
| 14 | Input sheet | B19 | Cash and Marketable Securities | $ 539,00 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 15 | Input sheet | B20 | Valor económico validado de participaciones y activos NO ope | $ - | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 16 | Input sheet | B21 | Minority interests | $ 242,00 | Dato | Interés minoritario de US$242 M (10-Q 2T26) | IA | Coincide [OBSERVADO] |
| 17 | Input sheet | B22 | Number of shares outstanding = | 1449,23 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 18 | Input sheet | B23 | Current stock price = | $ 43,65 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 19 | Input sheet | B24 | Effective tax rate = | 5,00% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 20 | Input sheet | B25 | Marginal tax rate = | 19,00% | Juicio | Tasa marginal federal más estatal de EE. UU. (25 %) | Plantilla/IA | Convención del modelo [MODELO] |
| 21 | Input sheet | B27 | Revenue growth rate for next year  | 3,98% | Juicio | Crecimiento del año 1 de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 22 | Input sheet | B28 | Operating Margin for next year | 20,25% | Juicio | Margen operativo del año 1 de la Base: 20 % más el ajuste de arrendamientos (0,25 pp) | IA (ficha de historias) | [HIPÓTESIS]; ver H-01 |
| 23 | Input sheet | B29 | Compounded annual revenue growth rate - years 2-5 = | 6,62% | Juicio | CAGR de los años 2-5 de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 24 | Input sheet | B30 | Referencia de margen objetivo (mediana histórica/sectorial;  | 24,25% | Juicio | Margen objetivo de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 25 | Input sheet | B31 | Year of convergence for margin | 5,00 | Juicio | Año de convergencia del margen: 5 | Plantilla/IA | Coherente con las historias |
| 26 | Input sheet | B32 | Sales to capital ratio  (for years 1-5) | 1,26 | Juicio | Ventas/capital años 1-5 (ficha de historias, ajustado por el conversor de arrendamientos) | IA | [HIPÓTESIS]; ver hallazgos |
| 27 | Input sheet | B33 | Sales to capital ratio (for years 6-10) | 1,17 | Juicio | Ventas/capital años 6-10 (ficha de historias, ajustado por el conversor de arrendamientos) | IA | [HIPÓTESIS]; ver hallazgos |
| 28 | Input sheet | B35 | Riskfree rate | 5,29% | Dato | Treasury a 10 años del corte común (30-sep-2026): 5,29 % | Corte común (datos_mercado.py) | [OBSERVADO] FRED DGS10 |
| 29 | Input sheet | B36 | Initial cost of capital = | 8,93% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 30 | Input sheet | B38 | Do you have employee options outstanding? | No | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 31 | Input sheet | B39 | Number of options outstanding = | 0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 32 | Input sheet | B40 | Average strike price = | $0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 33 | Input sheet | B41 | Average maturity = | 0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 34 | Input sheet | B42 | Standard deviation on stock price = | 0,00% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 35 | Input sheet | B46 | Do you want to override this assumption = | No | Juicio | No se anula el WACC terminal: converge a la fórmula de la plantilla | Plantilla | [MODELO] |
| 36 | Input sheet | B47 | If yes, enter the cost of capital after year 10 = | 8,93% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
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
| 55 | Input sheet | B79 | Pasivo de arrendamientos INCREMENTAL no reconocido | $ - | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 56 | Input sheet | B80 | Ajuste de EBIT atribuible a pasivos incrementales | 0 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 57 | Input sheet | B81 | Estado de conciliación de arrendamientos | CONCILIADO | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 58 | Input sheet | B82 | Inversiones a largo plazo según balance (dato histórico; NO  | $0 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 59 | Input sheet | B83 | Valor CONTABLE de inversiones excluidas del capital operativ | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 60 | Input sheet | B84 | Valor ECONÓMICO atribuible de participaciones y activos no o | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 61 | Input sheet | B85 | Control de inversiones y doble contabilización | VALIDADO | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 62 | Input sheet | B86 | Revisión: no están incluidas en EBIT/FCFF ni duplicadas | Sin solapamiento | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 63 | Input sheet | B87 | Fuente y conciliación de inversiones no operativas | 10-Q 2T26: inversiones por el método de la participación (1. | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 64 | Input sheet | B89 | Método fiscal de proyección (obligatorio en cada copia) | Normalizada | Juicio | Método fiscal normalizado | IA | — |
| 65 | Input sheet | B90 | Tasa inicial NORMALIZADA (solo si B89=Normalizada) | 0,178 | Juicio | Tasa inicial normalizada de 17,8 % (promedio 2023-2025); el LTM (5 %) incluye beneficios fiscales discretos | IA | [INFERENCIA]; ver H-04 |
| 66 | Input sheet | B91 | Fuente / conciliación de impuesto efectivo vs marginal | Tasa efectiva de 17,8 % (guía y promedio reciente); el LTM ( | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 67 | Input sheet | B92 | Control de hipótesis fiscales | VALIDADO | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 68 | Input sheet | B93 | Impuesto inicial para pronóstico (no altera la tasa históric | 0,178 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 69 | Input sheet | B96 | Tasa libre de riesgo nominal de largo plazo · misma moneda d | 5,29% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 70 | Input sheet | B97 | WACC terminal efectivo del modelo (independiente del DCF hab | 8,99% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 71 | Input sheet | B98 | Base | Sin liberación | Juicio | Sin liberación de capital en contracción (reinversión negativa se trunca a cero) | IA | Regla de Damodaran |
| 72 | Input sheet | B99 | Conservadora | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 73 | Input sheet | B100 | Disrupción | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 74 | Input sheet | B101 | Optimista | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 75 | Cost of capital worksheet | B12 | Which approach will you be using? | Detailed | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 76 | Cost of capital worksheet | B22 | Approach for estimating beta | Direct Input | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 77 | Cost of capital worksheet | B26 | What approach do you want to use to input ERP? | Operating regions | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 78 | Cost of capital worksheet | B33 | Average Maturity = | 8 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 79 | Cost of capital worksheet | B34 | Approach for estimating pre-tax cost of debt | Actual rating | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 80 | Cost of capital worksheet | B36 | If actual rating, input the rating | A3/A- | Dato | Calificación crediticia A3/A- | IA | [NO VERIFICADO] en esta revisión |
| 81 | Cost of capital worksheet | B41 | Book Value of Convertible Debt = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 82 | Cost of capital worksheet | B49 | Number of Preferred Shares = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 83 | Cost of capital worksheet | B50 | Current Market Price per Share= | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 84 | Cost of capital worksheet | B51 | Annual Dividend per Share = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 85 | Cost of capital worksheet | H29 | Ingresos H29 | $12.864 | Dato | Ventas de 2025 en Norteamérica: 12.864 (10-K 2025) | IA | Coincide [OBSERVADO] |
| 86 | R& D converter | F7 | Años de amortización del I+D | 3 | Juicio | Convención de Damodaran para la industria | IA | [MODELO] |

**Jerarquía de evidencia usada:** [OBSERVADO] (documento de la compañía o comprobación directa), [INFERENCIA] (deducción de lo observado), [HIPÓTESIS] (supuesto del analista), [MODELO] (resultado de las fórmulas) y [NO VERIFICADO].

## 4. Historia financiera: diez años y punto de partida

| US$ millones | Dec '20 | Dec '22 | Dec '23 | Dec '24 | Dec '25 | LTM |
|---|---:|---:|---:|---:|---:|---:|
| Ingresos | 9.913 | 12.682 | 14.240 | 16.747 | 20.074 | 20.996 |
| EBIT | -80 | 1.649 | 2.343 | 2.603 | 3.613 | 4.152 |
| Margen operativo | -0,8 % | 13,0 % | 16,5 % | 15,5 % | 18,0 % | 19,8 % |
| Flujo operativo | 1.508 | 1.526 | 2.503 | 3.435 | 4.534 | 4.529 |
| Capex | -376 | -588 | -711 | -790 | -876 | -904 |
| Capex / ventas | 3,8 % | 4,6 % | 5,0 % | 4,7 % | 4,4 % | 4,3 % |

La historia tiene tres fases. De 2016 a 2022 la empresa mejoró su margen operativo de 4,9 % a 13,0 % con compras y crecimiento de un dígito alto. En 2023-2025 un ciclo de producto excepcional (ablación por campo pulsado FARAPULSE y Watchman) llevó el crecimiento a 12-20 % y el margen GAAP a 18 %. En 2026 ambos productos frenaron en EE. UU. (+3 % en el 2T) al llegar Medtronic y Johnson & Johnson, el orgánico bajó a 7 % y un ciberataque obligó a retirar la guía. La Base supone que la cartera amplia sostiene ~6 % compuesto con un margen que sube a 24 %; la Conservadora, que el campo pulsado se vuelve commodity; la Disrupción, un tropiezo clínico.

## 5. Crecimiento de ingresos: de la historia a la proyección

La Base construye el ingreso por cubeta (Electrofisiología US$3.590 millones; Watchman US$2.000 millones; Resto de Cardiovascular US$8.470 millones; MedSurg US$6.936 millones). El resultado consolidado es 4,0 %, 7,6 %, 6,8 %, 6,2 %, 5,9 % en los años 1-5 (6,1 % compuesto) y cae a 4,0 % en el año 10: ingresos de 28.210 millones en el año 5 y 35.567 millones en el año 10.

Por qué ese ritmo: [INFERENCIA] el primer año de la Base (4,0 %) sigue la guía de julio (+3-5 % en el 3T26, ~2-3 % en el segundo semestre) y el efecto del ciberataque; el segundo año rebota a 7,6 % sobre una base deprimida y luego baja a ~6 %. [OBSERVADO] Electrofisiología creció 16 % y Watchman 11,3 % en el 1S26, pero ambos solo +3 % en EE. UU. en el 2T26. Duda: la hoja no incluye Penumbra ni sus ventas; si el ritmo de EE. UU. se repite en el 3T y el 4T la Conservadora debería pesar más que la Base.

Alternativas: la Conservadora (3,7 % compuesto, año 1 de 1,9 %); la Optimista (7,9 %, año 1 de 5,9 %); la Disrupción (1,8 %, con crecimiento terminal de 3 %). Los porcentajes son juicio del analista, no una guía publicada por la compañía.

## 6. Márgenes operativos y normalización de beneficios

La Base lleva el margen de 20,2 % en el año 1 a 24,2 % en el año 5 (ya ajustado por I+D capitalizado y arrendamientos; en base reportada 24,0 %). La Conservadora llega a 22,2 % (22,0 % reportado), la Disrupción a 20,2 % y la Optimista a 26,2 % (26,0 % reportado). Tasa impositiva: 17,8 % al inicio, convergiendo a la marginal de 19 % en el año 10.

Por qué ese margen: [OBSERVADO] el margen GAAP fue 21,6 % en el 2T26 y el ajustado 28,4 %; la amortización de intangibles resta 4,3 pp y compras, reestructuración y litigios ~2,4 pp. La Base llega a 24 % si la amortización de las compras pasadas pesa menos y la reestructuración (US$700-800 millones de costo hasta 2029, ~US$500 millones de ahorro al año) se reinvierte solo en parte. Sensibilidad: ±2 puntos de margen dan US$29,63 y US$36,60 (±10,5 %). Si compra Penumbra y otras, el margen GAAP se queda cerca de 20 %.

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

La reinversión de la Base es de 1.320 millones en el año 1 (frente a un NOPAT de 3.634 millones) y el FCFF del año 1 es de 2.313 millones. El ventas/capital es 1,26 en los años 1-5 y 1,17 en los 6-10 (base de la hoja, que incluye I+D y arrendamientos cuando la empresa los capitaliza). Con ±20 % en el ancla, el DCF Base va de US$31,72 (−4,2 %) a US$34,05 (+2,8 %). ROIC terminal: Base 9,0 %, Conservadora 9,0 %, Disrupción 9,0 %, Optimista 9,0 %.

Evidencia: la hoja usa ventas/capital de 1,26 (años 1-5) y 1,17 (años 6-10), entre el de hoy con crédito mercantil (0,60) y el del sector (1,48). El motor avisa del retorno del capital nuevo frente al ROIC terminal (9 %): ver H-02. ±20 % en el ventas/capital mueve la Base de US$31,72 a US$34,05.

## 8. Costo del capital y riesgo

Tasa libre de riesgo 5,29 % (Treasury a 10 años al 30-sep-2026), prima de riesgo de 4,35 % (ponderada por regiones de ingresos), beta desapalancada del sector 0,86 y beta apalancada 0,98 (propuesta bottom-up 0,97). WACC inicial 8,93 %; WACC terminal 8,99 %.

Dudas: (i) la beta de 0,98 es bottom-up del sector; la regresión queda como referencia; (ii) el costo de capital inicial usa la prima de mercado de 3,70 % de Damodaran de octubre y la tasa libre de riesgo de 5,29 %; (iii) la deuda tiene calificación A3/A- (no verificada). ±1 punto de tasa da US$39,60 (+19,6 %) y US$28,00 (−15,4 %).

Efecto: ±1 punto de WACC mueve la Base US$28,00 (−15,4 %) / US$39,60 (+19,6 %), el supuesto de mayor peso. La plantilla hace converger el WACC de 8,93 % a 8,99 % en el año 10 (convención de Damodaran).

## 9. Convergencia y valor terminal

El valor terminal es 56,9 % del valor de los activos operativos de la Base (34.294 millones de 60.319 millones). Crecimiento terminal 4,00 % (≤ la tasa libre), ROIC terminal 9,0 % y WACC terminal 8,99 %. Con −0,5 puntos de crecimiento terminal la Base vale US$32,80 (−1,0 %); con +0,5 puntos, US$33,44 (+1,0 %).

Riesgos: (i) las cuatro historias suponen ROIC terminal igual al costo de capital (9 %): el ROIC con plusvalía estuvo por debajo del costo de capital hasta 2025, así que la hipótesis es coherente con la evidencia; (ii) el crecimiento terminal de 4 % (2,8 % en la Disrupción) es menor que la tasa libre de riesgo; (iii) la compra pendiente de Penumbra no está en el terminal ni en la deuda.

## 10. Validación independiente del valor intrínseco

Comprobación 1 (identidad): la hoja y el motor independiente del repositorio coinciden en las cuatro historias (Base 33,12; Conservadora 26,31; Disrupción 20,62; Optimista 40,25), lo que valida la aritmética, no la economía. Comprobación 2 (puente): activos operativos 60.319 + caja 539 − deuda con arrendamientos 12.624 − opciones 0 − preferentes 0 + no operativos 0 = patrimonio común de 47.992 millones, o US$33,12 por acción con 1.449,2 millones de acciones. Comprobación 3 (DCF inverso del Nivel 2, margen → crecimiento anual de los años 1-5 que justifica el precio):

| Beta | Margen | Crecimiento anual de los años 1-5 que justifica el precio | Fracción de empresas de este tamaño que lo logra |
|---|---:|---:|---:|
| 0,98 | 22,2% | 13,4% | 13,5% |
| 0,98 | 24,2% | 11,2% | 20,6% |
| 0,98 | 26,2% | 9,2% | 28,9% |
| 0,97 | 22,2% | 13,4% | 13,6% |
| 0,97 | 24,2% | 11,1% | 20,8% |
| 0,97 | 26,2% | 9,2% | 29,0% |

Comprobación 4 (múltiplos propios): los 25-55× el EBITDA de 2019-2024 corresponden a otra etapa; la regla por ciclo lleva la Base a 10,9× (EV/EBITDA), 23,8× (EV/FCFF) y 15,1× (P/E) con pares de medtech (Medtronic, Stryker, Abbott, Edwards, Intuitive, Zimmer Biomet). Tres múltiplos de la Optimista (EV/FCFF, P/FCFE, P/OCF) superan en 26-33 % al actual y se justifican en la hoja.

## 11. Cuatro historias y probabilidades

| Historia | Probabilidad | CAGR 1-5 | Margen objetivo (ajustado / reportado) | ROIC terminal | g terminal | DCF por acción |
|---|---:|---:|---:|---:|---:|---:|
| Base · La cartera diversificada sostiene ~7% | 45,0 % | 6,1 % | 24,2 % / 24,0 % | 9,0 % | 4,0 % | US$33,12 |
| Conservadora · El campo pulsado se vuelve commodity | 22,5 % | 3,7 % | 22,2 % / 22,0 % | 9,0 % | 4,0 % | US$26,31 |
| Disrupción · Deterioro de los fundamentales | 10,0 % | 1,8 % | 20,2 % / 20,0 % | 9,0 % | 2,8 % | US$20,62 |
| Optimista · Electrofisiología y Watchman vuelven a doble dígito | 22,5 % | 7,9 % | 26,2 % / 26,0 % | 9,0 % | 4,0 % | US$40,25 |

Las probabilidades salen de la regla del ciclo (crecimiento_maduro) y no se ajustaron por indicadores: son un juicio condicional, no frecuencias observadas. El DCF esperado de las tres historias activas (pesos renormalizados) es US$33,20; con MOS de 35 % sobre el DCF Base el precio de compra es US$21,53. Cambiar los pesos cambia el esperado, no el DCF Base.

### ¿Qué pasaría si todo fallara?

Si el campo pulsado se vuelve commodity (ingresos +3,7 % y margen de 22 %), la acción vale la Conservadora (US$26,31); si además hay un tropiezo clínico o de producto (ingresos +1,8 % y margen de 20 %), vale la Disrupción (US$20,62). El flujo libre de US$3.625 millones sostiene el servicio de la deuda financiera de US$12.624 millones.

## 12. Valoración por múltiplos: prueba independiente y secundaria

Siete métodos (EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF, P/V y P/BV; los dos últimos con peso cero). Regla del 18-oct-2026: el múltiplo de cada escenario es el que la empresa tuvo cuando crecía como el escenario espera en FY+3 (Conservador 4,2 %, Base 6,8 %, Optimista 8,3 %), llevado al costo de capital del corte y limitado por el múltiplo justificado por los fundamentos de la misma historia; los comparables solo comprueban.

| Método | Mediana histórica 10a | Actual (LTM) | Ancla de peers (mediana) | Justificado Base | Peso en múltiplos |
|---|---:|---:|---:|---:|---:|
| EV/EBITDA | 28,24× | 13,54× | 16,29× | 10,90× | 33 % |
| EV/FCFF | 51,81× | 20,78× | 24,99× | 23,75× | 17 % |
| P/E | 58,51× | 17,78× | 32,64× | 15,12× | 33 % |
| P/FCFE | 46,28× | 17,45× | 22,82× | 20,90× | 8 % |
| P/OCF | 33,77× | 13,97× | 18,59× | 15,93× | 8 % |

Resultado: múltiplos consolidados de US$28,73 (Conservador), US$33,14 (Base) y US$37,49 (Optimista), frente a DCF de US$26,31, US$33,12 y US$40,25. Lectura del 30-sep-2026: el DCF (valor intrínseco) da US$36,39 por acción y los múltiplos, US$38,61 hoy: 6% por encima del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el DCF manda y los múltiplos son precio relativo.

La Base de los múltiplos (US$33,14) coincide con el DCF Base (US$33,12). Los múltiplos del LTM (13,5× EV/EBITDA, 17,8× P/E) ya incorporan la caída de ~50 % de la acción; los saltos de la Optimista frente al actual son +26 % a +33 % en tres métodos y están justificados por el crecimiento a ±2 puntos de los cierres históricos. Ver H-05.

## 13. Sensibilidades económicas y escenarios alternativos

| Supuesto cambiado (DCF Base US$33,12) | Valor |
|---|---:|
| WACC +1 pp / −1 pp | US$28,00 (−15,4 %) / US$39,60 (+19,6 %) |
| Crecimiento años 1-5 −2 pp / +2 pp | US$29,76 (−10,1 %) / US$36,81 (+11,2 %) |
| Margen objetivo −2 pp / +2 pp | US$29,63 (−10,5 %) / US$36,60 (+10,5 %) |
| Crecimiento terminal −0,5 pp / +0,5 pp | US$32,80 (−1,0 %) / US$33,44 (+1,0 %) |
| Ventas/capital −20 % / +20 % | US$31,72 (−4,2 %) / US$34,05 (+2,8 %) |

Ordenado por impacto: la tasa de descuento (±1 punto: +19,6 % / −15,4 %), el margen objetivo (±2 puntos: ±10,5 %), el crecimiento de los años 1-5 (±2 puntos: −10,1 % / +11,2 %), la dilución adicional de 5 % (−4,8 %) y el ventas/capital (±20 %: −4,2 % / +2,8 %). Las matrices del Nivel 2 recogen crecimiento por margen.

## 14. Coherencia de hojas, cálculos y presentación

La hoja está unificada con la maestra (61 pestañas en el mismo orden, 21.258 fórmulas intactas, 122 selectores idénticos) y el motor independiente reproduce las cuatro historias. Controles: candados 15/15, inputs completos, estados completos e integridad de hojas (registro en la bitácora de la sesión).

Intervenciones sobre la hoja que el lector debe conocer: (i) se restauraron las fórmulas de la maestra tras cada carga; (ii) el importador traía partidas de diciembre de 2025 en el LTM y se reescribió con el 10-Q de junio de 2026; (iii) las acciones, la tasa de impuestos y el patrimonio se llevaron a celdas que sobreviven a la restauración; (iv) Penumbra y la financiación asociada no están modeladas.

## 15. Hallazgos priorizados y propuestas de corrección

| ID | Severidad | Hallazgo | Impacto | Propuesta |
|---|---|---|---|---|
| H-01 | Alta | El margen GAAP de 24 % depende de que la amortización de las compras pese menos y la reestructuración se reinvierta solo en parte | ±2 puntos de margen mueven la Base ±10,5 %; con Penumbra y otras compras el margen se queda cerca de 20 % | Calibrar un caso con compras continuas y comparar con la trayectoria de márgenes de Medtronic y Stryker |
| H-02 | Alta | El capital nuevo de la Base (ventas/capital de 1,26 con margen de 24 % e impuesto de 19 %) rinde ~25 %, más del doble del ROIC terminal (9 %) | Posible sobrevaloración del flujo de los años 1-10 si el crecimiento exige más capital por compras | Calcular el ventas/capital marginal con las compras e incluir un caso de reinversión mayor |
| H-03 | Alta | La compra pendiente de Penumbra (~US$14.500 millones) no está en la valoración ni en la deuda | Si se cierra, sube la deuda, el crédito mercantil y cambia la mezcla; el valor por acción cambiaría según el retorno de la compra | Valorar Penumbra por separado y modelar la financiación cuando haya cierre o condiciones públicas |
| H-04 | Media | La tasa de impuestos del LTM (5 %) refleja beneficios fiscales discretos; la hoja usa 17,8 % (promedio 2023-2025) y 19 % marginal | ±3 puntos de tasa mueven el NOPAT ~±3,6 %; la utilidad neta y el P/E del LTM no son comparables | Conciliar la tasa efectiva futura con el desglose de impuestos del 10-Q y la guía de la empresa |
| H-05 | Media | Tres múltiplos de la Optimista (EV/FCFF, P/FCFE, P/OCF) superan en 26-33 % al actual | El consolidado de múltiplos pesa 60 % del ponderado secundario; no afecta al DCF principal | Revisar la mediana de cierres a ±2 pp de crecimiento y el recorte por el ancla C |
| H-06 | Media | La beta de 0,98 es bottom-up reapalancada con D/E de mercado de 0,17; con la caída de la acción la D/E real sube | Con la beta de la regresión el DCF cambia; la tasa de descuento mueve la Base +19,6 % / −15,4 % por punto | Actualizar la D/E con el precio del corte y documentar la elección frente a la regresión |
| H-07 | Media | El balance del LTM se escribió a mano desde el 10-Q (deuda de 1.709 y 10.915, patrimonio de 24.930); el importador repetía diciembre en varias partidas | Un error de transcripción cambia la deuda neta y el valor por acción | Releer el balance del 10-Q y conciliar con la hoja fila por fila |
| H-08 | Media | Las inversiones por el método de la participación (1.308) y otras inversiones (2.245) no se suman como activo no operativo | Hasta ~US$2,4 por acción si se reconocieran a valor contable | Revisar la naturaleza de esas inversiones (participaciones estratégicas) y decidir su tratamiento |
| H-09 | Media | El ciberataque de agosto de 2026 tiene efecto material en 2026 según la empresa, pero la guía nueva llega el 28-oct-2026 | El primer año de la Base (4,0 %) puede resultar alto o bajo según la guía | Actualizar el primer año con la guía del 3T26 |
| H-10 | Baja | La demanda colectiva por la guía de Electrofisiología y los litigios de productos pueden generar provisiones no modeladas | Menor al 1 % del valor salvo fallos adversos | Leer las notas de contingencias del 10-Q |
| H-11 | Media | Acciones de 1.449,2 M tras la recompra acelerada de US$2.000 M; no se suman premios con efecto dilutivo | Una dilución adicional de 5 % baja la Base a US$31,54 (−4,8 %) | Confirmar RSU y opciones con la nota de compensación del 10-K |
| H-12 | Baja | La calificación crediticia A3/A- del costo de la deuda no se verificó | Afecta el costo de la deuda y marginalmente el WACC | Verificar la calificación vigente |
| H-13 | Media | El precio (US$43,65) supera a las tres historias centrales; el DCF inverso pide ~11,2 % anual con margen de 24 % | La Base queda 24 % por debajo del precio y la Optimista 8 %: el mercado paga por una recuperación mayor que cualquier historia central | Decidir si la Optimista merece más probabilidad o si el precio descuenta Penumbra |

## 16. Catalizadores, señales de refutación y seguimiento

| Indicador | Último dato | Confirma Base u Optimista | Favorece Conservadora o Disrupción |
|---|---|---|---|
| Crecimiento orgánico total | 7,0% (2T26) | ≥ 7% | < 5% dos trimestres |
| Recuperación tras el ciberataque | Fabricación y despachos casi normales (8-sep-2026) | Ventas del 4T26 ≥ +5% y guía 2027 sin recortes | Pérdida de clientes o multas |
| Electrofisiología EE.UU. | +3% (2T26) | ≥ +8% en 2027 | ≤ 0% |
| Watchman EE.UU. | +3% (2T26) | ≥ +8% | ≤ 0% |
| Margen operativo GAAP | 19,8% LTM | ≥ 21% en 2027 | ≤ 18% |
| Penumbra (antimonopolio y retorno) | Pendiente | Cierre y crecimiento de trombectomía ≥ 15% | Remedios o deterioro |

Indicadores de actualización de probabilidades: si el crecimiento orgánico baja de 5 % dos trimestres o Electrofisiología y Watchman en EE. UU. quedan en ≤ 3 % en el 3T y el 4T, sube la Conservadora; si hay evidencia clínica comparativa desfavorable o pérdida de clientes tras el ciberataque, sube la Disrupción; si Electrofisiología vuelve a ≥ 8 % en 2027 y el margen GAAP supera 21 %, sube la Optimista. Próximo hito: resultados del 3T26 y guía nueva (28-oct-2026).

## 17. Dictamen económico y resumen para escuchar

**Dictamen: con reservas.** La hoja está bien formada, reproduce el motor y quedó UNIFICADA con la maestra; el balance del LTM se reescribió con el 10-Q del 2T26. Los supuestos que dominan el valor (margen GAAP de 24 % y recuperación del crecimiento de Electrofisiología y Watchman) son hipótesis del analista, y la valoración excluye la compra pendiente de Penumbra. Los saltos de múltiplos y la normalización de impuestos son los puntos técnicos a revisar primero.

Resumen para escuchar: Boston Scientific es una empresa de dispositivos médicos cardiovasculares con flujo libre de más de 3.600 millones de dólares. La Base de 33 dólares por acción queda 24 por ciento bajo el precio y supone un crecimiento de 6 por ciento con margen de 24. Lo que más mueve el valor es el margen y el crecimiento de electrofisiología y Watchman; la compra de Penumbra no está incluida.

## 18. Fuentes primarias, limitaciones y registro de versión

Fuentes primarias:

- [Boston Scientific, comunicado de resultados del 2T 2026 (29-jul-2026)](https://www.sec.gov/Archives/edgar/data/885725/000088572526000051/q22026earningsrelease.htm)
- [Boston Scientific, 8-K del 26-ago-2026 (ciberataque)](https://www.sec.gov/Archives/edgar/data/885725/000088572526000056/bsx-20260826.htm)
- [Boston Scientific, 8-K del 8-sep-2026 (efecto material en 2026)](https://www.sec.gov/Archives/edgar/data/885725/000088572526000059/bsx-20260907.htm)
- [Boston Scientific, 8-K del 27-jul-2026 (plan de reestructuración de 2026)](https://www.sec.gov/Archives/edgar/data/885725/000088572526000049/bsx-20260721.htm)
- [Boston Scientific, Form 10-Q del 2T 2026](https://www.sec.gov/Archives/edgar/data/885725/000088572526000053/bsx-20260630.htm)
- [Boston Scientific, Form 10-Q del 1T 2026](https://www.sec.gov/Archives/edgar/data/885725/000088572526000033/bsx-20260331.htm)
- [Boston Scientific, Form 10-K 2025](https://www.sec.gov/Archives/edgar/data/885725/000088572526000010/bsx-20251231.htm)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)

Limitaciones: no es una auditoría contable; no se releyeron los factores de riesgo del 10-K ni el detalle de la compra de Penumbra; los competidores en campo pulsado se describen con conocimiento general del sector; la calificación crediticia y el consenso no se verificaron. Registro de versión: auditoría v1.3 del 2026-10-26, vinculada a la hoja rehecha el mismo día y al artículo `BSX-2026-10-26`; no sustituye la auditoría posterior del usuario.
