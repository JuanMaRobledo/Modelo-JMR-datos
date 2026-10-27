**Corrección técnica de precios (27-oct-2026):** la valoración activa ya usa `precio` y `precioAnalisis` = USD 29,61 (corte 30-sep-2026) y conserva USD 30,20 en `precioAnalisisHistorico.valor`, con su fuente anterior. La mención inferior a la diferencia de precios describe el estado previo a la corrección. El DCF, múltiplos, escenarios y pesos no cambiaron.

**Comprobación adicional independiente (27-oct-2026):** lectura directa de la hoja Google nativa y contraste con el registro **activo**, no con `reference/damodaran/*_resultado.json` histórico. Las cuatro historias DCF (`Escenarios e historias!H5:H8`) son idénticas, sin diferencia numérica, a `valorEsperado.historias` (A=Base, B=Conservadora, C=Disrupción, D=Optimista) del registro publicado. `Valuation output!B35` coincide exactamente con `valorPrincipal`. Se confirmó que `Valuation output!C46` enlaza el margen Base con `Escenarios e historias!D5`. **Los 12 hallazgos consignados frente al motor antiguo son un antecedente, no evidencia de una divergencia DCF vigente; el control integral nuevo aún debe ejecutarse para clasificar cualquier otra anomalía.** No se tocaron supuestos ni resultados.

**Conciliación de fecha y precio:** el corte del DCF y el precio usado por la hoja son **30-sep-2026 / USD 29.61** (`Input sheet!D1` y `Resumen de Valoración!C25`). El `precioAnalisis` heredado de USD 30.20 pertenece a una referencia anterior de otra fecha y **no debe compararse con el DCF de este corte ni mostrarse como precio de hoy**. El detalle trazable se conserva en `recuperacion/conciliacion-integridad-precios-20261027.json`.

**Estado de publicación (2026-10-27): PUBLICADO CON SALVEDADES · revisión ONON-REC-20261027-R1.** Estudio recuperado con corte del 30-sep-2026; sin cambios de supuestos, probabilidades ni pesos. Valoración, análisis fundamental y esta auditoría corresponden a la misma hoja de Google y a la misma revisión.

**Controles ejecutados el 27-oct-2026:** siete múltiplos con fórmula y resultado numérico (`verificar_multiplos_hoja.py`), fórmulas contra la maestra del 22-oct (`audit_master_formulas.py`), consistencia hoja = registro = análisis (`consistencia_migracion.py --hoja`), candados vigentes, probabilidades.

**Salvedades vigentes:**
- Estudio recuperado: precio y corte de información del 30-sep-2026; no incorpora resultados posteriores ni actualiza supuestos.
- Siete múltiplos calculados por las fórmulas originales de la hoja (7/7 con fórmula y resultado numérico; fórmulas de cálculo y múltiplos idénticas a la maestra del 22-oct-2026); P/V y P/BV con peso 0 y estado provisional.
- Candados de la plantilla del 21-oct (Financials Multiples!M34:M36) no aplican a la maestra vigente; se exigen solo los presentes en ella.

**Salvedad resuelta (27-oct-2026):** Integridad de hojas: los hallazgos eran la comparación con el motor legado (30-sep) y registros sin `escenariosDCF`; con `escenariosDCF` (historias A-D) tomado de la hoja, `integridad_hojas.py` da 0 hallazgos en las ocho (27-oct-2026).

---

# Auditoría económica narrativa — On Holding AG (ONON)

**Análisis fundamental vinculado:** [ONON en la app](https://juanmarobledo.github.io/Modelo-JMR/research.html?ticker=ONON) · registro `analisis/ONON-research-1790597785576-4ggnz.json` (revisión del 2026-10-26).

## 1. Ficha de auditoría y alcance

| Campo | Contenido |
|---|---|
| Emisor | On Holding AG; ticker ONON |
| Mercado, moneda y escala | NYSE (EE. UU.); emisor suizo (NIIF, francos suizos); US$ millones salvo por acción |
| Sector | Calzado y ropa deportivos premium (Shoe) (hoja: industria de Damodaran «Shoe») |
| Método intrínseco principal | DCF FCFF de la historia Base (compañía operativa); MOS de 35 % sobre ese valor |
| Estados examinados | 20-F 2025 (3-mar-2026) y 6-K del 1S26 (11-ago-2026); LTM = FY2025 + 1S26 − 1S25 (cierre 30-jun-2026); CHF convertidos a US$ al tipo de cada período |
| Fecha de valoración / de auditoría | Corte de mercado 30-sep-2026 / 2026-10-26 |
| Precio del análisis | US$29,61 al cierre del 30-sep-2026 (corte común de la cartera); no se obtuvo un precio posterior |
| Hoja auditada | [Modelo JMR ONON](https://docs.google.com/spreadsheets/d/1nlN8qDy9BipM5IWwGE5Fgf6VKpyYQScLXIPvqtAE9Oo/edit), rehecha desde la maestra el 2026-10-26 |
| Artículo y Nivel 2 | `JMR-valuation/data/ONON_Research_Fundamental_Modelo_JMR_2026-10-26.md` y `ONON_Nivel2_Datos_Modelo_JMR_2026-10-26.md` |
| Registro en la app | Se publica con la autorización general del usuario; sin certificación previa (el usuario audita después) |
| Visto | Hoja completa por lectura; 6-K del 1S26 (balance, resultados, flujo, notas de acciones); 20-F 2025 vía XBRL IFRS de companyfacts; Investor Day del 22-sep-2026; comunicado del 2T26 |
| Fuera de alcance | 20-F completo (factores de riesgo y litigios); transcripción de la llamada; contratos con fabricantes y mayoristas; estados de los pares; consenso y calificaciones |
| Estado de verificación | **Con reservas** (no es una auditoría contable). Ver §15 y §17 |

## 2. Resumen ejecutivo y relato económico central

On vende calzado, ropa y accesorios deportivos premium, con venta directa de 45,7 % de las ventas del 2T26. En el LTM a junio de 2026 ingresó US$4.060 millones con margen bruto de 65 % y EBIT de US$560 millones (13,8 %); tiene caja de US$1.493 millones y solo deuda por arrendamientos NIIF 16 (US$697 millones). El 2T26 creció 13,5 % en francos y 21,6 % en moneda constante. La valoración Base de US$34,18 por acción supone ~15 % de crecimiento anual compuesto y margen operativo de 16,5 %, y queda 13 % por encima del precio de US$29,61.

**Tesis Base favorable:** Marca premium global que crece ~15 % con margen de 16,5 %: US$34,18 por acción. **Interpretación neutral:** El ciclo de moda se enfría: ingresos +8,1 % anual y margen de 13 %; la Conservadora (US$21,37, 22,5 %) describe esa ruta. **Contratesis adversa:** Pasa la moda y las ventas caen como en Under Armour: ingresos ~0 % anual y margen de 9 % (Disrupción, US$12,59, 15,0 %).

El supuesto que domina el valor es la tasa de descuento (±1 punto de WACC mueve la Base US$29,99 (−12,3 %) / US$39,51 (+15,6 %)), seguido por el crecimiento de la venta directa (30 % a 14 %) y el margen operativo de 16,5 % sin ventaja competitiva probada. El precio (US$29,61) queda por debajo de la Base (-13 %); ver el DCF inverso en §10. Esta narrativa no se deriva del precio: parte de los estados de la compañía.

## 3. Trazabilidad, integridad y jerarquía de evidencia

Inventario de las celdas de entrada de `Input sheet`, `Cost of capital worksheet`, `R& D converter` y `Option value`, y de los datos que la hoja enlaza desde las pestañas de estados (Income Statement, Balance Sheet, Cash Flow Statement; columna L = LTM). `Financials Multiples` no tiene celdas de entrada propias: son fórmulas.

**Conteo:** la tabla tiene **85 filas** (todas las de `Input sheet` con valor, las entradas clave del costo de capital y el conversor de I+D). Las celdas con fórmula por defecto (`Input sheet!B27:B33`) se incluyen porque el analista puede sustituirlas.

**Cómo se cargaron los estados.** (a) La serie anual 2021-2025 se armó desde `ifrs-full` de companyfacts (el importador de la SEC solo lee us-gaap) con `scripts/run_onon_cero.py --step refresh`; (b) el LTM y el balance de junio de 2026 salen del 6-K del 1S26 escritos a mano en el script (H-08); (c) cada año se convierte a su tipo de cambio (promedio para flujos, cierre para saldos; constantes del script, no verificadas contra una fuente independiente en esta revisión); (d) el pasivo de arrendamiento de largo plazo (fila 26 del balance) se escribió año por año porque un ajuste genérico lo había puesto en cero y subía el valor en US$1,3 por acción; (e) las acciones económicas son 301,7 M de la Clase A más 325,0 M de la Clase B / 10 más 1,9 M de premios dilutivos = 336,1 M, escritas en Income Statement!L27.

**Diferencias de fuente y ajustes:** (a) acciones: 336,1 M de la hoja frente a 301,7 M de la Clase A del balance (la Clase B tiene 1/10 de los derechos económicos); (b) el EBIT LTM es la suma de FY2025, 1S26 y 1S25 en CHF convertida a un solo tipo de cambio promedio, no la suma de períodos convertidos por separado; (c) la tasa de impuestos del LTM (7,9 %) se reemplaza por 20 % en B90.

| # | Pestaña | Celda | Rótulo | Valor | Tipo | Documento/fuente (URL en §18) | Quién lo aportó | Verificación |
|---:|---|---|---|---|---|---|---|---|
| 1 | Input sheet | B1 | On Holding AG (NYSE:ONON) | On Holding AG (NYSE:ONON) | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 2 | Input sheet | B4 | Date of valuation | sept-26 | Juicio | Corte de mercado 30-sep-2026 (fecha de valoración) | Corte común | [OBSERVADO] |
| 3 | Input sheet | B5 | Company name | On Holding AG | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 4 | Input sheet | B8 | Country of incorporation | Switzerland | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 5 | Input sheet | B9 | Industry (US) | Shoe | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 6 | Input sheet | B10 | Industry (Global) | Shoe | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 7 | Input sheet | B12 | Revenues | $ 4.060,30 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 8 | Input sheet | B13 | Operating income or EBIT | $ 559,90 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 9 | Input sheet | B14 | Interest expense | $ 40,70 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 10 | Input sheet | B15 | Book value of equity | $ 2.366,70 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 11 | Input sheet | B16 | Book value of debt | $ 696,40 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 12 | Input sheet | B17 | Do you have R&D expenses to capitalize? | No | Juicio | Capitalización de I+D según la regla del sector de la empresa | IA | Decisión de método; ver hallazgos |
| 13 | Input sheet | B18 | Do you have operating lease commitments? | No | Juicio | Arrendamientos operativos como deuda (conversor de Damodaran) | IA | [MODELO] |
| 14 | Input sheet | B19 | Cash and Marketable Securities | $ 1.492,80 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 15 | Input sheet | B20 | Valor económico validado de participaciones y activos NO ope | $ - | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 16 | Input sheet | B21 | Minority interests | $ - | Dato | Sin participaciones minoritarias relevantes | IA | [NO VERIFICADO] en la nota de patrimonio |
| 17 | Input sheet | B22 | Number of shares outstanding = | 336,11 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 18 | Input sheet | B23 | Current stock price = | $ 29,61 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 19 | Input sheet | B24 | Effective tax rate = | 7,94% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 20 | Input sheet | B25 | Marginal tax rate = | 23,00% | Juicio | Tasa marginal de 23 %: mezcla de Suiza, EE. UU. (55 % de las ventas) y resto | IA | [HIPÓTESIS] |
| 21 | Input sheet | B27 | Revenue growth rate for next year  | 17,50% | Juicio | Crecimiento del año 1 de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 22 | Input sheet | B28 | Operating Margin for next year | 14,00% | Juicio | Margen operativo del año 1 de la Base: 14,0 % (margen NIIF del 1S26 de 14,1 %); sube a 16,5 % en 5 años | IA (ficha de historias) | [HIPÓTESIS]; ver H-09 |
| 23 | Input sheet | B29 | Compounded annual revenue growth rate - years 2-5 = | 14,00% | Juicio | CAGR de los años 2-5 de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 24 | Input sheet | B30 | Referencia de margen objetivo (mediana histórica/sectorial;  | 16,50% | Juicio | Margen objetivo de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 25 | Input sheet | B31 | Year of convergence for margin | 5,00 | Juicio | Año de convergencia del margen: 5 | Plantilla/IA | Coherente con las historias |
| 26 | Input sheet | B32 | Sales to capital ratio  (for years 1-5) | 2,30 | Juicio | Ventas/capital años 1-5 (ficha de historias, ajustado por el conversor de arrendamientos) | IA | [HIPÓTESIS]; ver hallazgos |
| 27 | Input sheet | B33 | Sales to capital ratio (for years 6-10) | 2,00 | Juicio | Ventas/capital años 6-10 (ficha de historias, ajustado por el conversor de arrendamientos) | IA | [HIPÓTESIS]; ver hallazgos |
| 28 | Input sheet | B35 | Riskfree rate | 5,29% | Dato | Treasury a 10 años del corte común (30-sep-2026): 5,29 % | Corte común (datos_mercado.py) | [OBSERVADO] FRED DGS10 |
| 29 | Input sheet | B36 | Initial cost of capital = | 9,74% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 30 | Input sheet | B38 | Do you have employee options outstanding? | No | Dato | Sin opciones de empleados; los premios con efecto dilutivo (1,9 M) van en las acciones | IA (6-K, nota 4.5) | [OBSERVADO] el número de premios |
| 31 | Input sheet | B39 | Number of options outstanding = | 0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 32 | Input sheet | B40 | Average strike price = | $0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 33 | Input sheet | B41 | Average maturity = | 0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 34 | Input sheet | B42 | Standard deviation on stock price = | 0,00% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 35 | Input sheet | B46 | Do you want to override this assumption = | No | Juicio | No se anula el WACC terminal: converge a la fórmula de la plantilla | Plantilla | [MODELO] |
| 36 | Input sheet | B47 | If yes, enter the cost of capital after year 10 = | 9,74% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
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
| 55 | Input sheet | B79 | Pasivo de arrendamientos INCREMENTAL no reconocido | 0 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 56 | Input sheet | B80 | Ajuste de EBIT atribuible a pasivos incrementales | 0 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 57 | Input sheet | B81 | Estado de conciliación de arrendamientos | NO APLICA | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 58 | Input sheet | B82 | Inversiones a largo plazo según balance (dato histórico; NO  | $0 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 59 | Input sheet | B83 | Valor CONTABLE de inversiones excluidas del capital operativ | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 60 | Input sheet | B84 | Valor ECONÓMICO atribuible de participaciones y activos no o | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 61 | Input sheet | B85 | Control de inversiones y doble contabilización | VALIDADO | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 62 | Input sheet | B86 | Revisión: no están incluidas en EBIT/FCFF ni duplicadas | Sin solapamiento | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 63 | Input sheet | B87 | Fuente y conciliación de inversiones no operativas | 6-K del 1S26: sin participaciones relevantes por método de l | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 64 | Input sheet | B89 | Método fiscal de proyección (obligatorio en cada copia) | Normalizada | Juicio | Método fiscal normalizado | IA | — |
| 65 | Input sheet | B90 | Tasa inicial NORMALIZADA (solo si B89=Normalizada) | 0,2 | Juicio | Tasa inicial normalizada de 20 %: el LTM (7,9 %) incluye el reconocimiento de impuestos diferidos; Suiza ~19,6 % | IA | [INFERENCIA]; ver H-05 |
| 66 | Input sheet | B91 | Fuente / conciliación de impuesto efectivo vs marginal | Tasa efectiva normalizada de 20 %: el LTM (7,9 %) incluye el | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 67 | Input sheet | B92 | Control de hipótesis fiscales | VALIDADO | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 68 | Input sheet | B93 | Impuesto inicial para pronóstico (no altera la tasa históric | 0,2 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 69 | Input sheet | B96 | Tasa libre de riesgo nominal de largo plazo · misma moneda d | 5,29% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 70 | Input sheet | B97 | WACC terminal efectivo del modelo (independiente del DCF hab | 8,99% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 71 | Input sheet | B98 | Base | Sin liberación | Juicio | Sin liberación de capital en contracción (reinversión negativa se trunca a cero) | IA | Regla de Damodaran |
| 72 | Input sheet | B99 | Conservadora | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 73 | Input sheet | B100 | Disrupción | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 74 | Input sheet | B101 | Optimista | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 75 | Cost of capital worksheet | B12 | Which approach will you be using? | Detailed | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 76 | Cost of capital worksheet | B22 | Approach for estimating beta | Direct Input | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 77 | Cost of capital worksheet | B26 | What approach do you want to use to input ERP? | Will Input | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 78 | Cost of capital worksheet | B33 | Average Maturity = | 5 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 79 | Cost of capital worksheet | B34 | Approach for estimating pre-tax cost of debt | Direct Input | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 80 | Cost of capital worksheet | B35 | If direct input, input the pre-tax cost of debt | 6,000% | Juicio | Costo de la deuda de 6,0 %: tasa de los arrendamientos en US$ ≈ UST + ~0,8 pp | IA | [INFERENCIA]; sin deuda bancaria |
| 81 | Cost of capital worksheet | B41 | Book Value of Convertible Debt = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 82 | Cost of capital worksheet | B49 | Number of Preferred Shares = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 83 | Cost of capital worksheet | B50 | Current Market Price per Share= | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 84 | Cost of capital worksheet | B51 | Annual Dividend per Share = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 85 | R& D converter | F7 | Años de amortización del I+D | 3 | Juicio | Convención de Damodaran para la industria | IA | [MODELO] |

**Jerarquía de evidencia usada:** [OBSERVADO] (documento de la compañía o comprobación directa), [INFERENCIA] (deducción de lo observado), [HIPÓTESIS] (supuesto del analista), [MODELO] (resultado de las fórmulas) y [NO VERIFICADO].

## 4. Historia financiera: diez años y punto de partida

| US$ millones | — | Dec '22 | Dec '23 | Dec '24 | Dec '25 | LTM |
|---|---:|---:|---:|---:|---:|---:|
| Ingresos | N/D | 1.281 | 1.995 | 2.635 | 3.636 | 4.060 |
| EBIT | N/D | 89 | 201 | 240 | 455 | 560 |
| Margen operativo | N/D | 7,0 % | 10,1 % | 9,1 % | 12,5 % | 13,8 % |
| Flujo operativo | N/D | -243 | 251 | 563 | 408 | 632 |
| Capex | N/D | -87 | -53 | -74 | -95 | -121 |
| Capex / ventas | N/D | 6,8 % | 2,6 % | 2,8 % | 2,6 % | 3,0 % |

La historia tiene tres fases. En 2021-2022 On salió a bolsa con márgenes negativos o bajos mientras crecía 60 %. En 2023-2025 el crecimiento bajó de 56 % a 32-38 % y el margen operativo llegó a 9-13 % con margen bruto de 60 %+. En 2026 las ventas crecen 13,5 % en francos y 21,6 % en moneda constante, con la venta directa al triple de ritmo que los mayoristas. La Base supone una desaceleración gradual a ~11 % en el año 5 con margen que sube a 16,5 % por escala; la Conservadora, que el ciclo de moda se enfría; la Disrupción, una caída como la de Under Armour.

## 5. Crecimiento de ingresos: de la historia a la proyección

La Base construye el ingreso por cubeta (Mayoristas US$2.313 millones; Directo al consumidor US$1.748 millones). El resultado consolidado es 17,5 %, 16,7 %, 15,1 %, 13,2 %, 11,3 % en los años 1-5 (14,7 % compuesto) y cae a 4,0 % en el año 10: ingresos de 8.067 millones en el año 5 y 11.256 millones en el año 10.

Por qué ese ritmo: [INFERENCIA] el primer año de la Base (17,5 %) está por debajo de la guía de 2026 (~20 % en moneda constante) por la contención de los mayoristas; el venta directa crece 30 % el primer año y 14 % el quinto, los mayoristas 8-10 %. La visión externa ubica 15 % compuesto en cinco años en el tercio alto (~18 % de las empresas de su tamaño lo logró). Duda: el franco fuerte resta ~8 puntos al crecimiento reportado en dólares y la hoja convierte con tipos históricos.

Alternativas: la Conservadora (8,1 % compuesto, año 1 de 10,9 %); la Optimista (18,1 %, año 1 de 21,5 %); la Disrupción (0,1 %, con crecimiento terminal de 2 %). Los porcentajes son juicio del analista, no una guía publicada por la compañía.

## 6. Márgenes operativos y normalización de beneficios

La Base lleva el margen de 14,0 % en el año 1 a 16,5 % en el año 5 (ya ajustado por I+D capitalizado y arrendamientos; en base reportada 16,5 %). La Conservadora llega a 13,0 % (13,0 % reportado), la Disrupción a 9,0 % y la Optimista a 20,0 % (20,0 % reportado). Tasa impositiva: 20,0 % al inicio, convergiendo a la marginal de 23 % en el año 10.

Por qué ese margen: [OBSERVADO] el margen operativo NIIF del 1S26 fue 14,1 % y el del LTM 13,8 %; la meta de EBITDA ajustado ≥ 22 % en 2029 equivale a ~15,5 % operativo. La Base llega a 16,5 % por escala en gastos, sin acercarse al 23-29 % de Deckers o Birkenstock. Sensibilidad: ±2 puntos de margen dan US$29,98 y US$38,37 (−12 % / +12 %). Los arrendamientos ya están en el balance (NIIF 16) y el EBIT excluye su interés.

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

La reinversión de la Base es de 346 millones en el año 1 (frente a un NOPAT de 534 millones) y el FCFF del año 1 es de 189 millones. El ventas/capital es 2,30 en los años 1-5 y 2,00 en los 6-10 (base de la hoja, que incluye I+D y arrendamientos cuando la empresa los capitaliza). Con ±20 % en el ancla, el DCF Base va de US$32,64 (−4,5 %) a US$35,20 (+3,0 %). ROIC terminal: Base 9,0 %, Conservadora 9,0 %, Disrupción 9,0 %, Optimista 9,0 %.

Evidencia: On rota su capital ~2,6 veces con arrendamientos; la Base usa 2,30 en los años 1-5 y 2,00 en los años 6-10. El motor avisa que el capital nuevo rinde 29 % (Base), 23 % (Conservadora) y 35 % (Optimista), más del doble del ROIC terminal (9 %): ver H-01. ±20 % en el ventas/capital mueve la Base de US$32,64 a US$35,20.

## 8. Costo del capital y riesgo

Tasa libre de riesgo 5,29 % (Treasury a 10 años al 30-sep-2026), prima de riesgo de 3,70 % (ponderada por regiones de ingresos), beta desapalancada del sector 1,00 y beta apalancada 1,30 (propuesta bottom-up 1,05). WACC inicial 9,74 %; WACC terminal 8,99 %.

Dudas: (i) la beta de 1,30 es una entrada directa entre la bottom-up (~0,95) y las regresiones (1,58-1,80), y la que propone el motor es 1,05, con la que el esperado sube a US$36,04; (ii) el costo de capital inicial de 9,74 % usa la prima de mercado de 3,70 % de Damodaran de octubre y una tasa libre de riesgo de 5,29 %; (iii) los arrendamientos pesan ~6 % del capital. ±1 punto de tasa da US$39,51 (+16 %) y US$29,99 (−12 %).

Efecto: ±1 punto de WACC mueve la Base US$29,99 (−12,3 %) / US$39,51 (+15,6 %), el supuesto de mayor peso. La plantilla hace converger el WACC de 9,74 % a 8,99 % en el año 10 (convención de Damodaran).

## 9. Convergencia y valor terminal

El valor terminal es 62,3 % del valor de los activos operativos de la Base (6.665 millones de 10.690 millones). Crecimiento terminal 4,00 % (≤ la tasa libre), ROIC terminal 9,0 % y WACC terminal 8,99 %. Con −0,5 puntos de crecimiento terminal la Base vale US$33,90 (−0,8 %); con +0,5 puntos, US$34,46 (+0,8 %).

Riesgos: (i) las cuatro historias suponen ROIC terminal igual al costo de capital (9 %): On gana hoy muy por encima, así que la hipótesis es conservadora si la marca resulta duradera; (ii) el crecimiento terminal de 4 % (2,5 % en la Disrupción) es menor que la tasa libre de riesgo; (iii) el terminal pesa 62,3 % del valor operativo.

## 10. Validación independiente del valor intrínseco

Comprobación 1 (identidad): la hoja y el motor independiente del repositorio coinciden en las cuatro historias (Base 34,18; Conservadora 21,37; Disrupción 12,59; Optimista 47,85), lo que valida la aritmética, no la economía. Comprobación 2 (puente): activos operativos 10.690 + caja 1.493 − deuda con arrendamientos 696 − opciones 0 − preferentes 0 + no operativos 0 = patrimonio común de 11.487 millones, o US$34,18 por acción con 336,1 millones de acciones. Comprobación 3 (DCF inverso del Nivel 2, margen → crecimiento anual de los años 1-5 que justifica el precio):

| Beta | Margen | Crecimiento anual de los años 1-5 que justifica el precio | Fracción de empresas de este tamaño que lo logra |
|---|---:|---:|---:|
| 1,30 | 13,0% | 16,8% | 13,5% |
| 1,30 | 16,5% | 10,7% | 33,7% |
| 1,30 | 20,0% | 6,3% | 58,2% |
| 1,05 | 13,0% | 15,6% | 16,4% |
| 1,05 | 16,5% | 9,6% | 39,6% |
| 1,05 | 20,0% | 5,3% | 64,6% |

Comprobación 4 (múltiplos propios): el cierre de 2025 cotizó a 26,6× el EBITDA y 63× la utilidad por el hipercrecimiento de 2022-2025; la regla por ciclo lleva la Base a 10,8× (EV/EBITDA), 7,0× (EV/FCFF) y 20,6× (P/E), con pares de calzado (Deckers, Nike, Lululemon, Birkenstock, Adidas, Crocs). El EV/FCFF de 7× se apoya en un flujo libre del LTM deprimido por inventario y tiendas.

## 11. Cuatro historias y probabilidades

| Historia | Probabilidad | CAGR 1-5 | Margen objetivo (ajustado / reportado) | ROIC terminal | g terminal | DCF por acción |
|---|---:|---:|---:|---:|---:|---:|
| Base · Marca premium global que crece ~15% con margen de 16,5% | 40,0 % | 14,7 % | 16,5 % / 16,5 % | 9,0 % | 4,0 % | US$34,18 |
| Conservadora · El ciclo de moda se enfría | 22,5 % | 8,1 % | 13,0 % / 13,0 % | 9,0 % | 4,0 % | US$21,37 |
| Disrupción · Deterioro de los fundamentales | 15,0 % | 0,1 % | 9,0 % / 9,0 % | 9,0 % | 2,5 % | US$12,59 |
| Optimista · On se vuelve una marca deportiva global de primera línea | 22,5 % | 18,1 % | 20,0 % / 20,0 % | 9,0 % | 4,0 % | US$47,85 |

Las probabilidades salen de la regla del ciclo (crecimiento_alto) y no se ajustaron por indicadores: son un juicio condicional, no frecuencias observadas. El DCF esperado de las tres historias activas (pesos renormalizados) es US$34,40; con MOS de 35 % sobre el DCF Base el precio de compra es US$22,21. Cambiar los pesos cambia el esperado, no el DCF Base.

### ¿Qué pasaría si todo fallara?

Si el ciclo de moda se enfría (ingresos +8,1 % y margen de 13 %), la acción vale la Conservadora (US$21,37); si pasa la moda y las ventas caen como en Under Armour (margen de 9 %), vale la Disrupción (US$12,63). El balance (caja de US$1.493 millones frente a arrendamientos de US$697 millones) sostiene el piso de valor del patrimonio, no el valor por acción.

## 12. Valoración por múltiplos: prueba independiente y secundaria

Siete métodos (EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF, P/V y P/BV; los dos últimos con peso cero). Regla del 18-oct-2026: el múltiplo de cada escenario es el que la empresa tuvo cuando crecía como el escenario espera en FY+3 (Conservador 7,9 %, Base 15,1 %, Optimista 18,5 %), llevado al costo de capital del corte y limitado por el múltiplo justificado por los fundamentos de la misma historia; los comparables solo comprueban.

| Método | Mediana histórica 10a | Actual (LTM) | Ancla de peers (mediana) | Justificado Base | Peso en múltiplos |
|---|---:|---:|---:|---:|---:|
| EV/EBITDA | 34,22× | 12,46× | 9,27× | 11,19× | 33 % |
| EV/FCFF | 41,93× | 17,93× | 13,50× | 33,16× | 17 % |
| P/E | 71,10× | 19,90× | 12,78× | 20,59× | 33 % |
| P/FCFE | 43,28× | 19,49× | 12,59× | 27,36× | 8 % |
| P/OCF | 34,22× | 15,75× | 10,67× | 17,23× | 8 % |

Resultado: múltiplos consolidados de US$13,43 (Conservador), US$15,99 (Base) y US$19,27 (Optimista), frente a DCF de US$21,37, US$34,18 y US$47,85. Lectura del 2-oct-2026: el DCF Base de las historias da ~US$33,2 por acción y los múltiplos consolidados ~US$47 hoy, ~40% más, fuera del ±25%. Los múltiplos no se movieron para acercarlos. La diferencia es la ventaja competitiva: el justificado (C) supone que el ROE de FY+3 (~22%) dura para siempre y la historia de On (P/E de 60-96×) refleja la etapa de hipercrecimiento, mientras el DCF lleva el ROIC al costo de capital después del año 10 porque la marca tiene 16 años y no está probada. El DCF es el valor intrínseco; los múltiplos dicen cuánto pagaría el mercado si On sostuviera retornos excedentes como una marca consolidada.

La brecha de la Base con los múltiplos (US$15,99 frente a US$34,18 del DCF, −53 %) viene de tres cosas: la regla por ciclo lleva el múltiplo al de una empresa que crece ~15 % y no al de los cierres de hipercrecimiento; el EV/FCFF de 7× refleja un flujo libre LTM deprimido; y el DCF supone ROIC terminal igual al costo de capital pero margen de 16,5 %. El único salto sobre el múltiplo actual es el P/E Optimista (+34 %), justificado en la hoja. Ver H-02.

## 13. Sensibilidades económicas y escenarios alternativos

| Supuesto cambiado (DCF Base US$34,18) | Valor |
|---|---:|
| WACC +1 pp / −1 pp | US$29,99 (−12,3 %) / US$39,51 (+15,6 %) |
| Crecimiento años 1-5 −2 pp / +2 pp | US$31,49 (−7,9 %) / US$37,13 (+8,6 %) |
| Margen objetivo −2 pp / +2 pp | US$29,98 (−12,3 %) / US$38,37 (+12,3 %) |
| Crecimiento terminal −0,5 pp / +0,5 pp | US$33,90 (−0,8 %) / US$34,46 (+0,8 %) |
| Ventas/capital −20 % / +20 % | US$32,64 (−4,5 %) / US$35,20 (+3,0 %) |

Ordenado por impacto: la tasa de descuento (±1 punto: +16 % / −12 %), el margen objetivo (±2 puntos: ±12 %), el crecimiento de los años 1-5 (±2 puntos: −8 % / +9 %), la dilución adicional de 5 % (−5 %) y el ventas/capital (±20 %: −4 % / +3 %). Las matrices del Nivel 2 recogen crecimiento por margen.

## 14. Coherencia de hojas, cálculos y presentación

La hoja está unificada con la maestra (61 pestañas en el mismo orden, 21.258 fórmulas intactas, 122 selectores idénticos) y el motor independiente reproduce las cuatro historias. Controles: candados 15/15, inputs completos, estados completos e integridad de hojas (registro en la bitácora de la sesión).

Intervenciones sobre la hoja que el lector debe conocer: (i) se restauraron las fórmulas de la maestra tras cada carga; (ii) la serie anual viene de IFRS en CHF y se convierte con tipos escritos en el script; (iii) las acciones, la tasa de impuestos y el balance LTM se llevaron a celdas que sobreviven a la restauración; (iv) un ajuste genérico puso en cero el pasivo de arrendamiento de largo plazo y se corrigió (el DCF Base bajó de US$35,52 a US$34,18).

## 15. Hallazgos priorizados y propuestas de corrección

| ID | Severidad | Hallazgo | Impacto | Propuesta |
|---|---|---|---|---|
| H-01 | Alta | Ventas/capital de 2,30 y 2,00 implican que el capital nuevo rinde 23-35 %, más del doble del ROIC terminal (9 %) | Posible sobrevaloración del flujo de los años 1-10; ±20 % mueve la Base −4 % / +3 % | Calcular el ventas/capital marginal con inventario y tiendas y probar 1,8 en los años 1-5 |
| H-02 | Alta | Los múltiplos de la Base (US$15,99) quedan 53 % por debajo del DCF Base y el EV/FCFF de 7× se apoya en un flujo libre LTM deprimido | El consolidado de múltiplos pesa 40 % del ponderado secundario y lo arrastra; no afecta al DCF principal | Normalizar el flujo libre (inventario y capex de tiendas) antes de aplicar el múltiplo y revisar el ancla C de EV/FCFF (31,9×) |
| H-03 | Media | Los arrendamientos NIIF 16 (US$697 millones) están en la deuda del DCF y el EBIT excluye su interés; el conversor de arrendamientos no se usa | Un error de signo o de columna cambia la Base en ~US$1,3 por acción (ya ocurrió y se corrigió) | Conciliar el pasivo con la nota de arrendamientos del 6-K y comprobar que B16 suma las filas 21 y 26 |
| H-04 | Media | Las cifras en CHF se convierten a US$ con tipos promedio y de cierre escritos en el script | Un tipo equivocado distorsiona crecimiento y márgenes históricos; el LTM usa un solo promedio | Verificar los tipos con una fuente oficial (SNB) y recalcular el LTM por períodos |
| H-05 | Media | La tasa de impuestos inicial normalizada es 20 % (LTM 7,9 %, Suiza ~19,6 %, marginal 23 %) | ±3 puntos de tasa mueven el NOPAT ~±3,5 % | Conciliar con el desglose de impuestos del 6-K y la mezcla geográfica de utilidades |
| H-06 | Media | Acciones económicas: 301,7 M de Clase A + 325,0 M de Clase B / 10 + 1,9 M de premios = 336,1 M | Una dilución adicional de 5 % baja la Base a US$32,55 | Confirmar la relación 1/10 de la Clase B y los premios con la nota 4.5 del 6-K |
| H-07 | Media | La beta de 1,30 es una entrada directa entre la bottom-up (~0,95) y la regresión (1,58-1,80) | Con la beta de 1,05 que propone el motor el esperado sube a US$36,04 | Documentar la elección y comparar con la beta bottom-up de Damodaran de calzado y ropa |
| H-08 | Media | El LTM y el balance de junio de 2026 se escribieron a mano desde el 6-K; los emisores extranjeros no tienen XBRL trimestral | Sin contraste automático; un error de transcripción pasa inadvertido | Releer las cifras del 1S26 y 1S25 contra el 6-K y reconciliar el flujo operativo |
| H-09 | Alta | El margen de 16,5 % y el crecimiento de la venta directa (30 % a 14 %) dominan el valor sin ventaja competitiva probada | ±2 puntos de margen mueven la Base ±12 %; con 13 % de margen el valor se acerca a la Conservadora | Contrastar con la trayectoria de márgenes de Deckers, Hoka y Nike en etapa comparable |
| H-10 | Baja | Los pagos en acciones (~2 % de las ventas) se tratan como costo dentro del EBIT NIIF | Si el EBIT los excluyera, el margen estaría sobrestimado en ~2 puntos | Verificar la línea de pagos basados en acciones en el estado de resultados |
| H-11 | Media | El P/E Optimista (26,6×) supera en 34 % al actual (19,9×) y la historia propia (63×) se excluye como ancla | El P/E pesa 12,5 % dentro de los múltiplos | Revisar los pares de calzado y el ajuste por tasas de la regla por ciclo |
| H-12 | Baja | La probabilidad de la Disrupción (15 %) y su crecimiento terminal de 2,5 % son juicio sin tasa base externa | Cada 5 puntos de probabilidad mueven el esperado ~US$1,1 | Contrastar con casos de marcas deportivas que perdieron favor (Under Armour, Fila) |
| H-13 | Media | El precio (US$29,61) queda 13 % por debajo del DCF Base y 14 % del esperado; el DCF inverso pide ~10,7 % anual frente a 14,7 % de la Base | El mercado descuenta una desaceleración mayor que la de la tesis central o un margen menor | Decidir si la Conservadora merece más probabilidad dado el enfriamiento del sector |

## 16. Catalizadores, señales de refutación y seguimiento

| Indicador | Último dato | Confirma Base u Optimista | Favorece Conservadora o Disrupción |
|---|---|---|---|
| Crecimiento en moneda constante | +21,6% (2T26) | ≥ 18% | ≤ 10% |
| Mayoristas (moneda constante) | +12,7% (2T26) | ≥ +10% | ≤ 0% |
| Directo al consumidor (participación) | 45,7% de las ventas (2T26) | ≥ 48% | Cae |
| Margen bruto | 65,4% (2T26) | ≥ 65% | ≤ 62% |
| EBITDA ajustado | 19,8% (2T26) | ≥ 21% | ≤ 17% |
| Inventario / ventas | ~15% (jun-26) | Estable | Crece más que las ventas |
| Asia-Pacífico | +54,7% (2T26) | ≥ +30% | ≤ +10% |
| Recompras (programa de US$1.000M) | Aprobado en sep-2026 | Ejecución gradual | Suspendido |

Indicadores de actualización de probabilidades: si el crecimiento de los mayoristas pasa a negativo o el inventario sube más que las ventas dos trimestres sube la Conservadora; si el margen bruto cae por debajo de 62 % con rebajas sube la Disrupción; si la venta directa sostiene más de 25 % y el margen operativo supera 15 % en 2027 sube la Optimista. Próximo informe: resultados del 3T26.

## 17. Dictamen económico y resumen para escuchar

**Dictamen: con reservas.** La hoja está bien formada, reproduce el motor y quedó UNIFICADA con la maestra salvo la verificación final; los datos de partida se apoyan en el 6-K del 1S26 y en IFRS del 20-F, pero las conversiones de moneda y las cifras del LTM se escribieron a mano y requieren contraste. Los supuestos que dominan el valor (margen de 16,5 % y crecimiento de la venta directa) son hipótesis del analista; los múltiplos son una lectura secundaria conservadora.

Resumen para escuchar: On es una marca de calzado deportivo premium con caja neta y margen bruto de 65 por ciento. La Base de 34 dólares por acción queda 15 por ciento sobre el precio y supone un crecimiento de 15 por ciento anual con margen de 16,5. Lo que más mueve el valor es el margen y el ritmo de la venta directa.

## 18. Fuentes primarias, limitaciones y registro de versión

Fuentes primarias:

- [On, comunicado del 2T26 (11-ago-2026)](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm)
- [On, estados intermedios del 1S26 (6-K, 11-ago-2026)](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/onholdingag-20260630_d2.htm)
- [On, 20-F 2025 (3-mar-2026)](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000008/onholdingag-20251231.htm)
- [On, Investor Day 2026 (22-sep-2026)](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000021/exhibit991oninvestorday202.htm)
- [On, cofundadores como co-CEO (25-mar-2026)](https://www.sec.gov/Archives/edgar/data/1858985/000095010326004606/dp244091_ex9901.htm)
- [Damodaran, ERP implícita de octubre de 2026 (con la tasa y los precios del 30-sep)](https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx)
- [Damodaran, Betas by Sector (global), enero de 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
- [Mauboussin y Callahan, The Base Rate Book (2016)](https://www.credit-suisse.com/media/assets/corporate/docs/about-us/research/publications/the-base-rate-book-integrating-the-past-to-better-anticipate-the-future.pdf)

Limitaciones: no es una auditoría contable; no se releyeron los factores de riesgo del 20-F ni los contratos con mayoristas y fabricantes; los tipos de cambio y las cifras del LTM se escribieron a mano; el consenso y las calificaciones no se verificaron. Registro de versión: auditoría v1.3 del 2026-10-26, vinculada a la hoja rehecha el mismo día y al artículo `ONON-2026-10-26`; no sustituye la auditoría posterior del usuario.
