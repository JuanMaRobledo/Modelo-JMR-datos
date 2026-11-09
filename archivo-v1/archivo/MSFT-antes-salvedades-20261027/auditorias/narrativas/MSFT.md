**Estado de publicación (2026-10-27): PUBLICADO CON SALVEDADES · revisión MSFT-REC-20261027-R1.** Estudio recuperado con corte del 30-sep-2026; sin cambios de supuestos, probabilidades ni pesos. Valoración, análisis fundamental y esta auditoría corresponden a la misma hoja de Google y a la misma revisión.

**Controles ejecutados el 27-oct-2026:** siete múltiplos con fórmula y resultado numérico (`verificar_multiplos_hoja.py`), fórmulas contra la maestra del 22-oct (`audit_master_formulas.py`), consistencia hoja = registro = análisis (`consistencia_migracion.py --hoja`), candados vigentes, probabilidades.

**Salvedades vigentes:**
- Estudio recuperado: precio y corte de información del 30-sep-2026; no incorpora resultados posteriores ni actualiza supuestos.
- Siete múltiplos calculados por las fórmulas originales de la hoja (7/7 con fórmula y resultado numérico; fórmulas de cálculo y múltiplos idénticas a la maestra del 22-oct-2026); P/V y P/BV con peso 0 y estado provisional.
- Candados de la plantilla del 21-oct (Financials Multiples!M34:M36) no aplican a la maestra vigente; se exigen solo los presentes en ella.
- Regla H3 incumplida: EV/FCFF Base 30,0x supera 0,78 veces el promedio histórico (26,3x).

---

# Auditoría económica narrativa — Microsoft Corporation (MSFT)

**Análisis fundamental vinculado:** [MSFT en la app](https://juanmarobledo.github.io/Modelo-JMR/research.html?ticker=MSFT) · registro `analisis/MSFT-research-1788905155892-deskj.json` (revisión del 26-oct-2026).

## 1. Ficha de auditoría y alcance

| Campo | Contenido |
|---|---|
| Emisor | Microsoft Corporation, sociedad del estado de Washington (EE. UU.); acción ordinaria de clase única; ticker MSFT |
| Mercado, moneda y escala | Nasdaq Global Select Market; US$ millones salvo por acción |
| Sector | Software y nube (hoja: industria de Damodaran «Software (System & Application)») |
| Método intrínseco principal | DCF FCFF de la historia Base (compañía operativa); MOS de 35 % sobre ese valor |
| Estados examinados | 10-K FY2026 (29-jul-2026, ejercicio cerrado el 30-jun-2026); LTM = FY2026 (aún no hay 10-Q del 1T FY27) y reexpresión de segmentos del 8-K del 2-sep-2026 |
| Fecha de valoración / de auditoría | Corte de mercado 30-sep-2026 / 26-oct-2026 |
| Precio del análisis | US$512,90 al cierre del 30-sep-2026 (corte común de la cartera); no se obtuvo un precio posterior |
| Hoja auditada | [Modelo JMR MSFT](https://docs.google.com/spreadsheets/d/1wIgB2zfjmPk_DdnaFsoJfKHMiIR_p4795ebvbGSOi1E/edit), rehecha desde la maestra el 26-oct-2026 |
| Artículo y Nivel 2 | `JMR-valuation/data/MSFT_Research_Fundamental_Modelo_JMR_2026-10-26.md` y `MSFT_Nivel2_Datos_Modelo_JMR_2026-10-26.md` |
| Registro en la app | Se publica con la autorización general del usuario; sin certificación previa (el usuario audita después) |
| Visto | Hoja completa por lectura; página R6 (flujo de caja) del 10-K FY2026; companyfacts de la SEC; historial de la valoración anterior de MSFT en la app |
| Fuera de alcance | 10-K completo (factores de riesgo, vencimientos de la deuda, concentración de clientes); transcripción de la llamada; estados de pares; calificaciones crediticias; vigilancia posterior al 26-oct-2026 |
| Estado de verificación | **Con reservas** (no es una auditoría contable). Ver §15 y §17 |

## 2. Resumen ejecutivo y relato económico central

Microsoft vende suscripciones y consumo de software y nube: Azure, Microsoft 365, licencias y soluciones sectoriales, y un negocio de consumo. En el ejercicio 2026 ingresó US$331.839 millones (+17,8 %), con margen operativo GAAP de 46,8 % y flujo operativo de US$182.935 millones [OBSERVADO: 10-K FY2026].

Lo que cambia: el crecimiento se reacelera (Azure +40,4 %, Microsoft 365 cloud +18,5 %), el RPO comercial llega a US$678.000 millones (+84 %) y la compañía supera los 30 millones de puestos pagos de Copilot [OBSERVADO según el comunicado de resultados; el detalle del RPO sin OpenAI es de fuente secundaria]. Al mismo tiempo, el capex pagado en efectivo sube a US$115.948 millones (34,9 % de las ventas) y se prevén unos US$175.000 millones en el año calendario 2026, de modo que el flujo libre cae a US$66.987 millones (20,2 % de las ventas, frente a 30 % en FY24).

El motor de crecimiento de la Base es la suma de cuatro cubetas: Azure parte de +40 % y desacelera a +18 % en el año cinco; Microsoft 365 cloud de +18 % a +11 %; licencias y consumo aportan poco; el resultado es 19,4 % el primer año y 16,3 % compuesto a cinco años. La ventaja competitiva que sostendría los beneficios es la distribución (Microsoft 365, identidad, seguridad, datos y desarrolladores) y los costos de cambio, no la tecnología de modelos, que no es exclusiva.

**Tesis Base favorable:** la capacidad construida se vende, el ventas/capital mejora de 0,60 a 1,05 y el margen llega a 47,9 % reportado (50 % ajustado): US$440,73 por acción. **Interpretación neutral:** el crecimiento se mantiene pero la capacidad es más cara de lo previsto; la Conservadora (US$257,57, 22,5 %) describe esa ruta. **Contratesis adversa:** comoditización de modelos y agentes que se cobran por tarea (Disrupción, US$122,84, 10 %).

El supuesto que domina el valor es la tasa de descuento (±1 punto de WACC mueve la Base −18,6 % / +28,1 %), seguido del ROIC terminal (igual al costo de capital: −21,7 %) y del crecimiento de los años 1-5 (±2 puntos: −8,9 % / +9,9 %). La contradicción que la empresa debe resolver es cómo sostener 17 % de crecimiento y 47 % de margen cuando la depreciación de una capacidad que se multiplicó por 2,6 en dos años entra al estado de resultados. El precio (US$512,90) queda entre la Base y la Optimista; el DCF inverso exige 18,6 % de crecimiento anual en los años 1-5 con 50 % de margen, un nivel que solo alcanza 2,8 % de las empresas de este tamaño. Esta narrativa no se deriva del precio: parte de los estados de la compañía.

## 3. Trazabilidad, integridad y jerarquía de evidencia

Inventario de las celdas de entrada de `Input sheet`, `Cost of capital worksheet`, `R& D converter` y `Option value`, y de los datos que la hoja enlaza desde las pestañas de estados (Income Statement, Balance Sheet, Cash Flow Statement; columna L = LTM). `Financials Multiples` no tiene celdas de entrada propias: son fórmulas.

**Conteo:** la tabla tiene **107 filas** (todas las de `Input sheet` con valor, las entradas del costo de capital agrupadas por función y las de `R& D converter` y `Option value`); las celdas de rótulo no se cuentan. Las celdas con fórmula por defecto (`Input sheet!B27:B30`) se incluyen porque el analista puede sustituirlas.

**Cómo se cargaron los estados.** (a) El importador de la SEC (`desde_cero.sh datos`) cargó diez ejercicios (FY17-FY26) y el LTM desde los XBRL; (b) el LTM coincide con FY2026 porque el 10-Q del 1T FY27 se presenta el 28-oct-2026; (c) `scripts/msft_datos_cero.py` agregó la separación de arrendamientos financieros del balance (corriente 4.290 y largo plazo 62.304 en FY26; 3.172 y 43.000 en FY25) y fijó 7.503,5 millones de acciones; (d) el importador trajo la depreciación y amortización redondeada (7.800 … 39.000) de otro tag y se reemplazó por la línea «Depreciation, amortization, and other» del flujo de caja (8.778; 10.261; 11.682; 12.796; 11.686; 14.460; 13.861; 20.958; 29.433; 38.534), con ajuste de «otros gastos operativos» para que las identidades de la plantilla se mantengan; solo FY24-FY26 se verificaron contra el 10-K FY2026 (página R6); (e) la hoja se restauró con las fórmulas de la maestra tras cada carga.

**Diferencias de fuente y ajustes:** (a) acciones: 7.425,5 M de la portada del 10-K más 78 M de premios no consolidados = 7.503,5 M, frente a 7.427 M del balance y 7.453 M promedio diluido; (b) deuda: incluye arrendamientos financieros (US$66.594 M) y excluye los operativos, que el conversor suma una sola vez (VP de US$20.488 M); (c) el EBIT es el reportado (155.237), no una cifra ajustada; (d) los resultados no operativos (US$10.697 M) quedan fuera del EBIT y del FCFF; (e) las inversiones de largo plazo (US$36.348 M) se suman a valor contable.

| # | Pestaña | Celda | Rótulo | Valor | Tipo | Documento/fuente (URL en §18) | Quién lo aportó | Verificación |
|---:|---|---|---|---|---|---|---|---|
| 1 | Input sheet | B1 | MICROSOFT CORP (NASDAQ:MSFT) | MICROSOFT CORP (NASDAQ:MSFT) | Cálculo | Título de la hoja | Plantilla | Coincide |
| 2 | Input sheet | B4 | Date of valuation | sept-26 | Juicio | Corte de mercado 30-sep-2026 (fecha de valoración) | Corte común | [OBSERVADO] |
| 3 | Input sheet | B5 | Company name | MICROSOFT CORP | Dato | 10-K FY2026 (SEC, 29-jul-2026), portada | IA | Coincide [OBSERVADO] |
| 4 | Input sheet | B8 | Country of incorporation | United States | Dato | 10-K FY2026 (SEC, 29-jul-2026), portada: Washington (EE. UU.) | IA | Coincide [OBSERVADO] |
| 5 | Input sheet | B9 | Industry (US) | Software (System & Application) | Juicio | Damodaran, industrias de EE. UU., enero de 2026: «Software (System & Application)» | IA (elección de industria) | Existe en Industry Averages(US) [INFERENCIA]; Microsoft también es nube e infraestructura, ver H-10 |
| 6 | Input sheet | B10 | Industry (Global) | Software (System & Application) | Juicio | Damodaran, industrias globales, enero de 2026 | IA | Ídem |
| 7 | Input sheet | B12 | Revenues | $ 331.839,00 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 8 | Input sheet | B13 | Operating income or EBIT | $ 155.237,00 | Cálculo | 10-K FY2026 (SEC, 29-jul-2026): resultado operativo 155.237 | Hoja (Income Statement!L12) | Coincide [OBSERVADO] |
| 9 | Input sheet | B14 | Interest expense | $ 3.051,00 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 10 | Input sheet | B15 | Book value of equity | $ 442.387,00 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el 10-K FY2026 (SEC, 29-jul-2026) [OBSERVADO] |
| 11 | Input sheet | B16 | Book value of debt | $ 106.888,00 | Cálculo | 10-K FY2026 (SEC, 29-jul-2026): deuda a corto 9.227 + largo plazo 31.067 + arrendamientos financieros 66.594 (corriente 4.290 + no corriente 62.304) | Hoja (Balance Sheet!L20+L21+L25+L26) | Recalculado: 106.888 [OBSERVADO]; arrendamientos financieros solo FY25-FY26 |
| 12 | Input sheet | B17 | Do you have R&D expenses to capitalize? | Yes | Juicio | I+D tratado como inversión a 3 años (Damodaran, software) | IA | Decisión de método; ver H-07 |
| 13 | Input sheet | B18 | Do you have operating lease commitments? | Yes | Juicio | 10-K FY2026 (SEC, 29-jul-2026), nota de arrendamientos: arrendamientos operativos con valor presente de 20.488 | IA | Procede [OBSERVADO] |
| 14 | Input sheet | B19 | Cash and Marketable Securities | $ 76.843,00 | Cálculo | 10-K FY2026 (SEC, 29-jul-2026): efectivo y equivalentes más inversiones a corto plazo (20.935 + 55.908) | Hoja (Balance Sheet!L5) | Coincide [OBSERVADO] |
| 15 | Input sheet | B20 | Valor económico validado de participaciones y activos NO ope | $ 36.348,00 | Juicio | Inversiones de largo plazo a valor contable (B84 = B83) | IA | Valor contable, sin valor de mercado [HIPÓTESIS]; ver H-09 |
| 16 | Input sheet | B21 | Minority interests | $ - | Dato | Sin participaciones minoritarias relevantes | IA | [NO VERIFICADO] en nota de patrimonio |
| 17 | Input sheet | B22 | Number of shares outstanding = | 7503,50 | Dato | Portada del 10-K: 7.425,5 M de acciones (24-jul-2026) más 78 M de premios no consolidados = 7.503,5 M | Hoja (Income Statement!L27) | Coincide con la portada; el 78 M es un supuesto de dilución plena [HIPÓTESIS]; ver H-05 |
| 18 | Input sheet | B23 | Current stock price = | $ 512,90 | Dato | Precio de cierre del 30-sep-2026: US$512,90 | Corte común (D1) | [OBSERVADO] en el registro anterior de la cartera |
| 19 | Input sheet | B24 | Effective tax rate = | 19,40% | Cálculo | Impuesto LTM / utilidad antes de impuestos = 32.185 / 165.934 | Hoja (Income Statement!L29) | Coincide [OBSERVADO] |
| 20 | Input sheet | B25 | Marginal tax rate = | 25,00% | Juicio | Tasa marginal federal más estatal de EE. UU. (25 %) | Plantilla/IA | Convención del modelo [MODELO] |
| 21 | Input sheet | B27 | Revenue growth rate for next year  | 0,00% | Cálculo | Predeterminado de la plantilla; la historia Base lo sustituye en `Valuation output` | Plantilla | No gobierna la Base |
| 22 | Input sheet | B28 | Operating Margin for next year | 48,92% | Cálculo | Enlace a `Valuation output!B6` | Hoja | Coincide con el margen inicial 48,92 % [MODELO] |
| 23 | Input sheet | B29 | Compounded annual revenue growth rate - years 2-5 = | 0,00% | Cálculo | Predeterminado de la plantilla (igual a B27) | Plantilla | No gobierna la Base |
| 24 | Input sheet | B30 | Referencia de margen objetivo (mediana histórica/sectorial;  | 34,20% | Cálculo | Referencia de margen (mediana histórica); NO activa | Plantilla | Informativa |
| 25 | Input sheet | B31 | Year of convergence for margin | 5,00 | Juicio | Año de convergencia del margen: 5 | Plantilla/IA | Coherente con las historias |
| 26 | Input sheet | B32 | Sales to capital ratio  (for years 1-5) | 0,60 | Juicio | Ventas/capital años 1-5 en base reportada: 0,60 (marginal de 3 años: 0,38; rotación FY26: 0,82) | IA (ficha de historias) | [HIPÓTESIS]; ver H-02 |
| 27 | Input sheet | B33 | Sales to capital ratio (for years 6-10) | 1,05 | Juicio | Ventas/capital años 6-10: 1,05 (utilización de la capacidad) | IA | [HIPÓTESIS]; ver H-02 |
| 28 | Input sheet | B35 | Riskfree rate | 5,29% | Dato | Treasury a 10 años del corte común (30-sep-2026): 5,29 % | Corte común (datos_mercado.py) | [OBSERVADO] FRED DGS10 |
| 29 | Input sheet | B36 | Initial cost of capital = | 10,93% | Cálculo | Enlace al costo de capital | Hoja | 10,93 % [MODELO] |
| 30 | Input sheet | B38 | Do you have employee options outstanding? | No | Dato | Sin opciones de empleados en circulación (el 10-K reporta premios en acciones, no opciones) | IA | [NO VERIFICADO] en la nota |
| 31 | Input sheet | B39 | Number of options outstanding = | 0,00 | Dato | Sin opciones | IA | Ídem |
| 32 | Input sheet | B40 | Average strike price = | $0,00 | Dato | Sin opciones | IA | Ídem |
| 33 | Input sheet | B41 | Average maturity = | 0,00 | Dato | Sin opciones | IA | Ídem |
| 34 | Input sheet | B42 | Standard deviation on stock price = | 0,00% | Dato | Sin opciones | IA | Ídem |
| 35 | Input sheet | B46 | Do you want to override this assumption = | No | Juicio | No se anula el WACC terminal: converge a la fórmula de la plantilla | Plantilla | 8,99 % [MODELO] |
| 36 | Input sheet | B47 | If yes, enter the cost of capital after year 10 = | 10,93% | Cálculo | Enlace | Hoja | Sin efecto |
| 37 | Input sheet | B49 | Do you want to override this assumption = | Yes | Juicio | Se anula el ROIC terminal con un valor propio | IA | Ver B50 |
| 38 | Input sheet | B50 | If yes, enter the return on capital you expect after year 10 | 20,00% | Juicio | ROIC terminal Base 20 %: debajo de la referencia de Damodaran (29,3 %; 22,95 % normalizado) | IA | [HIPÓTESIS]; ver H-01 |
| 39 | Input sheet | B52 | Do you want to override this assumption = | No | Juicio | Sin probabilidad de fracaso | IA | Empresa AAA [INFERENCIA] |
| 40 | Input sheet | B53 | If yes, enter the probability of failure = | 0% | Dato | 0 | IA | — |
| 41 | Input sheet | B54 | What do you want to tie your proceeds in failure to? | V | Dato | Sin efecto | Plantilla | — |
| 42 | Input sheet | B55 | Enter the distress proceeds as percentage of book or fair va | 50% | Dato | Sin efecto | Plantilla | — |
| 43 | Input sheet | B57 | Do you want override this assumption = | No | Juicio | Sin rezago de reinversión distinto del predeterminado | IA | — |
| 44 | Input sheet | B58 | If yes, enter a different lag (0 = no lag to 3 = lag of 3 ye | 1 | Dato | 1 | Plantilla | — |
| 45 | Input sheet | B60 | Do you want to override this assumption = | No | Juicio | Sin ajuste | IA | — |
| 46 | Input sheet | B62 | Do you want to override this assumption = | No | Juicio | Sin pérdidas fiscales acumuladas (NOL) | IA | Coincide con el 10-K [INFERENCIA] |
| 47 | Input sheet | B65 | Do you want to override this assumption = | No | Juicio | No se anula la tasa libre después del año 10 | IA | — |
| 48 | Input sheet | B66 | If yes, enter the riskfree rate after year 10 | 5,29% | Dato | 5,29 % | Plantilla | Sin efecto |
| 49 | Input sheet | B68 | Do you want to override this assumption = | Yes | Juicio | Se anula el crecimiento perpetuo | IA | Ver B69 |
| 50 | Input sheet | B69 | If yes, enter the growth rate in perpetuity | 4,00% | Juicio | Crecimiento terminal 4,00 % (≤ tasa libre de 5,29 %) | Regla vigente del modelo | [MODELO]; ver H-06 |
| 51 | Input sheet | B71 | Do you want to override this assumption | No | Juicio | Sin efectivo atrapado ni impuesto extranjero adicional | IA | [NO VERIFICADO] |
| 52 | Input sheet | B72 | If yes, enter trapped cash (if taxes) or entire balance (if  | $0,00 | Dato | 0 | IA | — |
| 53 | Input sheet | B73 | & Average tax rate of the foreign markets where the cash is  | 0% | Dato | 0 | IA | — |
| 54 | Input sheet | B76 | Valor de acciones preferentes (misma unidad del DCF) | 0 | Dato | Sin acciones preferentes | IA | [OBSERVADO] |
| 55 | Input sheet | B78 | PV del conversor ya incluido en deuda del balance (solapamie | 0 | Dato | Sin conversor ya incluido en la deuda | IA | Evita doble conteo |
| 56 | Input sheet | B79 | Pasivo de arrendamientos INCREMENTAL no reconocido | $ 20.488,41 | Cálculo | VP de arrendamientos operativos incrementales (conversor) | Hoja | 20.488 [MODELO] |
| 57 | Input sheet | B80 | Ajuste de EBIT atribuible a pasivos incrementales | 4041,084947 | Cálculo | Ajuste de EBIT por arrendamientos (conversor) | Hoja | 4.041 [MODELO] |
| 58 | Input sheet | B81 | Estado de conciliación de arrendamientos | CONCILIADO | Cálculo | Estado de conciliación | Hoja | CONCILIADO |
| 59 | Input sheet | B82 | Inversiones a largo plazo según balance (dato histórico; NO  | $36.348 | Cálculo | Inversiones de largo plazo según balance: 36.348 | Hoja (Balance Sheet!L14) | Coincide [OBSERVADO] |
| 60 | Input sheet | B83 | Valor CONTABLE de inversiones excluidas del capital operativ | 36348 | Dato | Valor contable de inversiones excluidas del capital operativo: 36.348 | IA | Coincide con B82 [OBSERVADO] |
| 61 | Input sheet | B84 | Valor ECONÓMICO atribuible de participaciones y activos no o | 36348 | Juicio | Valor económico atribuible = valor contable (sin prima ni descuento) | IA | [HIPÓTESIS]; ver H-09 |
| 62 | Input sheet | B85 | Control de inversiones y doble contabilización | VALIDADO | Cálculo | Control de doble contabilización | Hoja | VALIDADO |
| 63 | Input sheet | B86 | Revisión: no están incluidas en EBIT/FCFF ni duplicadas | Sin solapamiento | Juicio | Sin solapamiento con EBIT/FCFF | IA | [INFERENCIA] |
| 64 | Input sheet | B87 | Fuente y conciliación de inversiones no operativas | 10-K FY2026, balance: «Equity and other investments» a valor | Dato | Fuente y conciliación de inversiones no operativas | IA | Texto de la hoja |
| 65 | Input sheet | B89 | Método fiscal de proyección (obligatorio en cada copia) | Normalizada | Juicio | Método fiscal normalizado | IA | — |
| 66 | Input sheet | B90 | Tasa inicial NORMALIZADA (solo si B89=Normalizada) | 0,195 | Juicio | Tasa inicial 19,5 % que converge a la marginal de 25 % | IA | Tasa efectiva 19,4 % FY26, 17,6 % FY25, 18,2 % FY24 [OBSERVADO] |
| 67 | Input sheet | B91 | Fuente / conciliación de impuesto efectivo vs marginal | Tasa efectiva: 19,4 % en FY26 (32.185/165.934), 17,6 % en FY | Dato | Conciliación de impuesto efectivo y marginal | IA | Texto de la hoja |
| 68 | Input sheet | B92 | Control de hipótesis fiscales | VALIDADO | Cálculo | Control | Hoja | VALIDADO |
| 69 | Input sheet | B93 | Impuesto inicial para pronóstico (no altera la tasa históric | 0,195 | Cálculo | Tasa inicial | Hoja | 19,5 % |
| 70 | Input sheet | B96 | Tasa libre de riesgo nominal de largo plazo · misma moneda d | 5,29% | Cálculo | Tasa libre de largo plazo | Hoja | 5,29 % |
| 71 | Input sheet | B97 | WACC terminal efectivo del modelo (independiente del DCF hab | 8,99% | Cálculo | WACC terminal | Hoja | 8,99 % |
| 72 | Input sheet | B98 | Base | Sin liberación | Juicio | Sin liberación de capital en contracción | IA | Regla de truncar reinversión negativa |
| 73 | Input sheet | B99 | Conservadora | Sin liberación | Juicio | Ídem | IA | — |
| 74 | Input sheet | B100 | Disrupción | Sin liberación | Juicio | Ídem | IA | — |
| 75 | Input sheet | B101 | Optimista | Sin liberación | Juicio | Ídem | IA | — |
| 76 | Cost of capital worksheet | B12 | Which approach will you be using? | Detailed | Juicio | Enfoque «Detailed» del costo de capital | IA | — |
| 77 | Cost of capital worksheet | B22 | Approach for estimating beta | Single Business(US) | Juicio | Beta del sector de EE. UU. (negocio único); Damodaran, enero de 2026: 1,25 desapalancada | IA | [HIPÓTESIS]; ver H-10 |
| 78 | Cost of capital worksheet | B26 | What approach do you want to use to input ERP? | Operating regions | Juicio | ERP por regiones de operación | IA | Ver H-08 |
| 79 | Cost of capital worksheet | B33 | Average Maturity = | 6 | Juicio | Vencimiento medio de la deuda: 6 años | IA | [NO VERIFICADO]; vencimientos del 10-K no releídos |
| 80 | Cost of capital worksheet | B34 | Approach for estimating pre-tax cost of debt | Actual rating | Juicio | Calificación real | IA | — |
| 81 | Cost of capital worksheet | B36 | If actual rating, input the rating | Aaa/AAA | Dato | Aaa/AAA (Moody's / S&P) | IA | [NO VERIFICADO] en esta sesión; calificación pública conocida |
| 82 | Cost of capital worksheet | B41 | Book Value of Convertible Debt = | 0 | Dato | Sin deuda convertible | IA | — |
| 83 | Cost of capital worksheet | B42 | Interest Expense on Convertible = | 0 | Dato | Sin deuda convertible | IA | — |
| 84 | Cost of capital worksheet | B43 | Maturity of Convertible Bond = | 0 | Dato | Sin deuda convertible | IA | — |
| 85 | Cost of capital worksheet | B44 | Market Value of Convertible = | 0 | Dato | Sin deuda convertible | IA | — |
| 86 | Cost of capital worksheet | B49 | Number of Preferred Shares = | 0 | Dato | Sin acciones preferentes | IA | — |
| 87 | Cost of capital worksheet | B50 | Current Market Price per Share= | 1 | Dato | Valor ficticio 1 | Plantilla | Sin efecto |
| 88 | Cost of capital worksheet | B51 | Annual Dividend per Share = | 0 | Dato | 0 | IA | Sin efecto |
| 89 | Cost of capital worksheet | H6 | Ingresos H6 | $170.794 | Dato | 10-K FY2026 (SEC, 29-jul-2026): ingresos de EE. UU. 170.794 | IA | Coincide [OBSERVADO] |
| 90 | Cost of capital worksheet | H17 | Ingresos H17 | 161045 | Dato | 10-K FY2026 (SEC, 29-jul-2026): resto del mundo 161.045 | IA | Coincide [OBSERVADO] |
| 91 | Cost of capital worksheet | H29 | Ingresos H29 | $170.794 | Dato | Norteamérica = EE. UU. 170.794 | IA | Coincide con H6 |
| 92 | Cost of capital worksheet | H32 | Ingresos H32 | $161.045 | Dato | Fuera de EE. UU. sin desglose 161.045 | IA | Coincide con H17; ver H-08 |
| 93 | Cost of capital worksheet | H37 | Ingresos H37 |  $ 331.839,00  | Dato | Ingresos por industria (negocio único): 331.839 | Hoja | Coincide con B12 |
| 94 | Cost of capital worksheet | H53 | Ingresos H53 |  $ 331.839,00  | Dato | Ingresos por industria global: 331.839 | Hoja | Coincide con B12 |
| 95 | R& D converter | B12 | Gasto de I+D del año -1 | 35562,00 | Dato | Estado de resultados, ejercicio 2026 (10-K FY2026 (SEC, 29-jul-2026) para FY24-FY26; 10-K anteriores para FY17-FY23) | Hoja (Income Statement!row 10) | Coincide [OBSERVADO] |
| 96 | R& D converter | B13 | Gasto de I+D del año -2 | 32488,00 | Dato | Estado de resultados, ejercicio 2025 (10-K FY2026 (SEC, 29-jul-2026) para FY24-FY26; 10-K anteriores para FY17-FY23) | Hoja (Income Statement!row 10) | Coincide [OBSERVADO] |
| 97 | R& D converter | B14 | Gasto de I+D del año -3 | 29510,00 | Dato | Estado de resultados, ejercicio 2024 (10-K FY2026 (SEC, 29-jul-2026) para FY24-FY26; 10-K anteriores para FY17-FY23) | Hoja (Income Statement!row 10) | Coincide [OBSERVADO] |
| 98 | R& D converter | B15 | Gasto de I+D del año -4 | 27195,00 | Dato | Estado de resultados, ejercicio 2023 (10-K FY2026 (SEC, 29-jul-2026) para FY24-FY26; 10-K anteriores para FY17-FY23) | Hoja (Income Statement!row 10) | Coincide con la hoja; FY17-FY23 no releídos [NO VERIFICADO] |
| 99 | R& D converter | B16 | Gasto de I+D del año -5 | 24512,00 | Dato | Estado de resultados, ejercicio 2022 (10-K FY2026 (SEC, 29-jul-2026) para FY24-FY26; 10-K anteriores para FY17-FY23) | Hoja (Income Statement!row 10) | Coincide con la hoja; FY17-FY23 no releídos [NO VERIFICADO] |
| 100 | R& D converter | B17 | Gasto de I+D del año -6 | 20716,00 | Dato | Estado de resultados, ejercicio 2021 (10-K FY2026 (SEC, 29-jul-2026) para FY24-FY26; 10-K anteriores para FY17-FY23) | Hoja (Income Statement!row 10) | Coincide con la hoja; FY17-FY23 no releídos [NO VERIFICADO] |
| 101 | R& D converter | B18 | Gasto de I+D del año -7 | 19269,00 | Dato | Estado de resultados, ejercicio 2020 (10-K FY2026 (SEC, 29-jul-2026) para FY24-FY26; 10-K anteriores para FY17-FY23) | Hoja (Income Statement!row 10) | Coincide con la hoja; FY17-FY23 no releídos [NO VERIFICADO] |
| 102 | R& D converter | B19 | Gasto de I+D del año -8 | 16876,00 | Dato | Estado de resultados, ejercicio 2019 (10-K FY2026 (SEC, 29-jul-2026) para FY24-FY26; 10-K anteriores para FY17-FY23) | Hoja (Income Statement!row 10) | Coincide con la hoja; FY17-FY23 no releídos [NO VERIFICADO] |
| 103 | R& D converter | B20 | Gasto de I+D del año -9 | 14726,00 | Dato | Estado de resultados, ejercicio 2018 (10-K FY2026 (SEC, 29-jul-2026) para FY24-FY26; 10-K anteriores para FY17-FY23) | Hoja (Income Statement!row 10) | Coincide con la hoja; FY17-FY23 no releídos [NO VERIFICADO] |
| 104 | R& D converter | B21 | Gasto de I+D del año -10 | 13037,00 | Dato | Estado de resultados, ejercicio 2017 (10-K FY2026 (SEC, 29-jul-2026) para FY24-FY26; 10-K anteriores para FY17-FY23) | Hoja (Income Statement!row 10) | Coincide con la hoja; FY17-FY23 no releídos [NO VERIFICADO] |
| 105 | R& D converter | F7 | Años de amortización del I+D | 3 | Juicio | Convención de Damodaran para software | IA | [MODELO]; ver H-07 |
| 106 | R& D converter | F8 | I+D del año actual (LTM) | 35.562 | Dato | 10-K FY2026 (SEC, 29-jul-2026): investigación y desarrollo | Hoja | Coincide [OBSERVADO] |
| 107 | Option value | B9 | Rendimiento por dividendo | 0 | Juicio | Sin opciones: sin efecto | IA | Inmaterial |


**Jerarquía de evidencia usada:** [OBSERVADO] (documento de la compañía o comprobación directa), [INFERENCIA] (deducción de lo observado), [HIPÓTESIS] (supuesto del analista), [MODELO] (resultado de las fórmulas) y [NO VERIFICADO].

## 4. Historia financiera: diez años y punto de partida

| US$ millones | FY17 | FY19 | FY21 | FY23 | FY24 | FY25 | FY26 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Ingresos | 89.950 | 125.843 | 168.088 | 211.915 | 245.122 | 281.724 | 331.839 |
| EBIT | 22.326 | 42.959 | 69.916 | 88.523 | 109.433 | 128.528 | 155.237 |
| Margen operativo | 24,8 % | 34,1 % | 41,6 % | 41,8 % | 44,6 % | 45,6 % | 46,8 % |
| Flujo operativo | 39.507 | 52.185 | 76.740 | 87.582 | 118.548 | 136.162 | 182.935 |
| Capex | −8.129 | −13.925 | −20.622 | −28.107 | −44.477 | −64.551 | −115.948 |
| Flujo libre | 31.378 | 38.260 | 56.118 | 59.475 | 74.071 | 71.611 | 66.987 |
| Capex / ventas | 9,0 % | 11,1 % | 12,3 % | 13,3 % | 18,1 % | 22,9 % | 34,9 % |

La historia tiene dos fases. De FY17 a FY23 el margen operativo subió 17 puntos y el capex se mantuvo en 9-13 % de las ventas: crecimiento con poco capital, de ahí el ROIC contable de 75-104 %. Desde FY24 el capex se multiplica por 2,6 en dos años, el flujo libre se estanca y la rotación del capital cae de 1,03 a 0,82. El punto de partida de la valoración (LTM = FY26) es por tanto el más intensivo en capital de la serie, no un año representativo de la década. Hay un solo año de freno (FY23, +6,9 %) y un salto en el balance: el activo total pasó de US$301.311 millones (FY20) a US$758.376 millones (FY26) y la caja, de US$136.527 millones a US$76.843 millones.

Comparabilidad: el crecimiento de FY18 (22,7 %) compara con el FY17 publicado antes de la norma ASC 606; contra el FY17 reexpresado fue 14,3 %. La utilidad neta de FY18 y FY19 está afectada por la reforma tributaria de EE. UU. [OBSERVADO: 10-K de esos años; no releídos en esta sesión]. La separación de arrendamientos financieros en el balance solo existe desde FY25, así que la deuda de FY17-FY24 en la hoja no incluye arrendamientos financieros (H-11).

## 5. Crecimiento de ingresos: de la historia a la proyección

La Base construye el ingreso por cubeta. Azure (US$101.938 millones, +40,4 %) pasa de +40 % a +33 %, +27 %, +22 % y +18 % en los años 1-5; Microsoft 365 cloud (US$100.299 millones) de +18 % a +17 %, +15 %, +13 % y +11 %; licencias, industria y soporte (US$65.890 millones) de +7 % a +4 %; dispositivos y consumidor (US$63.712 millones) de +1,5 % a +2,5 %. El resultado consolidado es 19,4 %, 18,5 %, 16,6 %, 14,5 % y 12,4 %, que cae a 4 % en el año 10: ingresos de US$705.118 millones en el año 5 y US$1.004.589 millones en el año 10.

Por qué ese ritmo: [HIPÓTESIS] la oferta es la restricción de Azure en los primeros años (así lo supone la ficha de historias; no se contrastó con la llamada) y cada unidad de capacidad nueva se vende; [INFERENCIA] el primer año de la Base (19,4 %) supera el 17,8 % de FY26 porque la mezcla favorece a Azure, que pesa 31 % de las ventas y crece más del doble que el resto. El riesgo es que la Base asume que una empresa de US$332.000 millones de ingresos suma US$370.000 millones en cinco años: más que los ingresos totales de casi todas las empresas del mundo. Las tasas base de Mauboussin y Callahan, que usa el DCF inverso de la hoja, sitúan en 2,8 % la fracción de empresas de este tamaño que sostienen el crecimiento que el precio exige. Esto no invalida la Base, que sostiene 16,3 % por la combinación de nube y suscripción, pero la convierte en una tesis exigente, no en la «central» estadística.

Alternativas: la Conservadora (9,1 % compuesto, año 1 de 12,2 %) supone que Azure desacelera a 9 % en el año 5 y Microsoft 365 a 6 %; la Optimista (20,4 %) mantiene a Azure en +25 % y a Microsoft 365 en +15 % al final de los cinco años; la Disrupción detiene el crecimiento en el año 3. Las adquisiciones previstas son cero y el efecto de moneda es cero [HIPÓTESIS]; el crecimiento de FY26 no se separó entre orgánico y adquirido porque Microsoft no lo publica para el grupo. No se publica una tasa de retención neta.

## 6. Márgenes operativos y normalización de beneficios

El margen operativo GAAP de FY26 fue 46,8 % (EBIT de US$155.237 millones). La Base lo lleva de 48,9 % en el año 1 a 50,0 % en el año 5, ya ajustado por I+D capitalizado (+0,9 puntos) y arrendamientos (+1,2 puntos); en base reportada son 46,8 % → 47,9 %. La Conservadora lo deja en 43,0 % (40,9 % reportado), la Disrupción cae a 30,0 % y la Optimista llega a 54,0 % (51,9 % reportado).

Por qué: [HIPÓTESIS] la escala de las suscripciones y la mejor utilización de la capacidad compensan la depreciación creciente y el costo de inferencia; la guía de Microsoft anticipa una baja de menos de un punto del margen en FY27 [OBSERVADO según la llamada del 29-jul-2026; no releída]. Los cambios de vida útil de los centros de datos (de 15 a 25 años) y la reclasificación de arrendamientos reducen la depreciación contable sin cambiar la caja: por eso el margen GAAP puede sobreestimar la economía. La utilidad neta de FY26 (US$133.749 millones) contiene US$10.697 millones de resultado no operativo, principalmente ganancias de inversiones, que no entran en el FCFF; la Base proyecta cero beneficio por revalorización de OpenAI y otras inversiones.

Normalizaciones: ninguna sobre el EBIT; la tasa impositiva inicial es 19,5 % (efectiva de FY26: 19,4 %) y converge a la marginal de 25 % en el año 10. La compensación en acciones (US$12.405 millones, 3,7 % de las ventas) se mantiene como costo dentro del EBIT. El margen de la Optimista (51,9 % reportado) supera lo que Microsoft ha obtenido en cualquier año y solo es coherente con una utilización muy superior de la capacidad.

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

La reinversión de la Base es de US$122.410 millones en el año 1 (78 % del NOPAT de US$156.025 millones) y se mantiene en US$126.000-132.000 millones hasta el año 5; el FCFF del año 1 es US$33.615 millones, frente a un flujo libre contable de US$66.987 millones. La diferencia es deliberada: el modelo trata el crecimiento de los ingresos como algo que exige capital a razón de 0,60 de ventas por dólar de capital en los años 1-5 (base reportada; 0,72 con I+D y arrendamientos).

Evidencia: el ventas/capital marginal de los últimos tres años es 0,38 a tres años y 0,43 en el último año (peor que el supuesto), la rotación del capital invertido del FY26 es 0,82 y la de FY17 era 5,4 [OBSERVADO en la hoja]. El 1,05 de los años 6-10 supone que la capacidad llega a utilizarse; no hay un dato de utilización publicado. Con ±20 % en el ancla, el DCF Base va de US$421,05 a US$453,85, un rango pequeño porque el valor terminal depende del ROIC terminal y no del ventas/capital.

ROIC: el contable (EBIT × (1 − 25 %) sobre patrimonio más deuda menos caja) cae de 104 % (FY18) a 28,7 % (FY26); el ajustado por I+D y arrendamientos del año base es 24,8 %. El ROIC terminal es 20 % en la Base, 24 % en la Optimista, 14,5 % en la Conservadora (punto medio entre 20 % y el costo de capital terminal) y igual al costo de capital (8,99 %) en la Disrupción. La referencia de Damodaran para software es 29,3 % (22,95 % normalizado): se usa un valor menor porque la escala hace menos creíble un exceso permanente de esa magnitud; es un juicio, no un dato (H-01).

Asignación de capital: recompras de US$22.271 millones en FY26 (US$182.782 millones en FY19-FY26), dividendos de US$0,98 por acción por trimestre y capex dominante; la hoja no proyecta recompras ni dilución adicional, así que mantiene 7.503,5 millones de acciones en las cuatro historias. El ROE de 30,2 % está deprimido por un patrimonio que creció con la utilidad retenida y no con recompras.

## 8. Costo del capital y riesgo

Tasa libre de riesgo 5,29 % (Treasury a 10 años al 30-sep-2026), prima de riesgo de 4,57 % ponderada por regiones (Estados Unidos 51,5 % y resto del mundo 48,5 % de las ventas), beta desapalancada del sector 1,25 y beta apalancada 1,28 (la propuesta bottom-up con corrección por caja es 1,36). Costo del patrimonio 11,12 %; costo de la deuda antes de impuestos 5,69 % (calificación AAA); pesos de 97,2 % patrimonio y 2,8 % deuda con arrendamientos; WACC inicial 10,93 %.

Dudas: (i) 48,5 % de las ventas está fuera de EE. UU. sin desglose por país, de modo que la prima del resto del mundo usa el promedio por regiones de la plantilla y no la exposición real (H-08); (ii) la beta del sector de software de EE. UU. (1,25) puede no reflejar el negocio de infraestructura de Azure, que tiene más capital y menos recurrencia (H-10); (iii) el vencimiento medio de la deuda (6 años) y la calificación AAA no se verificaron en esta sesión; (iv) la tasa libre es la del corte común y la prima es la implícita de Damodaran de octubre de 2026, no un promedio.

Efecto: ±1 punto de WACC mueve la Base −18,6 % / +28,1 %, el supuesto de mayor peso. La plantilla hace converger el WACC de 10,93 % a 8,99 % en el año 10 (aproxima la tasa a la del mercado maduro); esa convergencia es una convención de Damodaran y aporta valor, porque la Base descuenta el terminal con una tasa dos puntos menor que la inicial.

## 9. Convergencia y valor terminal

El valor terminal es 70,7 % del valor de los activos operativos de la Base (US$2.346.962 millones de US$3.321.218 millones). Crecimiento terminal 4,00 % (≤ la tasa libre de 5,29 %), ROIC terminal 20 %, WACC terminal 8,99 % y tasa de reinversión terminal implícita de 20 % (g/ROIC = 4/20).

Riesgos: (i) 4 % de crecimiento nominal perpetuo es exigente para una empresa de US$1 billón de ingresos en el año 10; con −0,5 puntos la Base vale US$416,10 (−5,6 %); (ii) un ROIC terminal de 20 % sobre capital que hoy rinde 24,8 % supone que el exceso de retorno persiste; con ROIC igual al costo de capital la Base vale US$344,97 (−21,7 %); (iii) la Disrupción se estabiliza con crecimiento 0 % y ROIC igual al costo de capital desde el año 5, sin liberar capital (la reinversión es cero), lo cual es una convención y no una predicción.

## 10. Validación independiente del valor intrínseco

Comprobación 1 (identidad): la hoja y el motor independiente del repositorio coinciden en las cuatro historias (Base 440,73; Conservadora 257,57; Disrupción 122,84; Optimista 621,31), lo que valida la aritmética, no la economía. Comprobación 2 (puente): activos operativos 3.321.218 + caja 76.843 + inversiones 36.348 − deuda con arrendamientos 127.376 = patrimonio de US$3.307.033 millones, o US$440,73 por acción con 7.503,5 millones de acciones. Comprobación 3 (DCF inverso): el precio de US$512,90 exige crecimiento de 18,6 % anual en los años 1-5 con margen de 50 % (22,3 % con 43 % y 16,8 % con 54 %); solo 2,8 % de las empresas de este tamaño lo logran.

Comprobación 4 (múltiplos propios): el EV/EBITDA del LTM es 20,0 veces y el P/E 28,6 veces; los múltiplos de salida de la Base (7,8× y 20,2×) quedan por debajo de los históricos por el tope del múltiplo justificado (sección 12 de esta auditoría). Comprobación 5 (retornos): con un NOPAT de US$156.025 millones en el año 1 y un EV de mercado de unos US$3,88 billones, el rendimiento del NOPAT sobre el valor de la empresa es 4,0 %, por debajo del costo de capital de 10,9 %: el mercado ya descuenta un crecimiento sostenido. Esto no demuestra sobrevaloración; indica que el precio exige la Base más una parte de la Optimista.

## 11. Cuatro historias y probabilidades

| Historia | Probabilidad | Crecimiento 1-5 (CAGR) | Margen objetivo (ajustado / reportado) | Ventas/capital 1-5 (reportado) | ROIC terminal | DCF por acción |
|---|---:|---:|---:|---:|---:|---:|
| Base · IA rentable con inversión sostenida | 45,0 % | 16,3 % | 50,0 % / 47,9 % | 0,60 | 20,0 % | US$440,73 |
| Conservadora · adopción más lenta y capacidad cara | 22,5 % | 9,1 % | 43,0 % / 40,9 % | 0,60 | 14,5 % | US$257,57 |
| Disrupción · deterioro de los fundamentales | 10,0 % | 1,8 % | 30,0 % | 0,55 | 9,0 % (= costo de capital) | US$122,84 |
| Optimista · monetización de agentes y utilización superior | 22,5 % | 20,4 % | 54,0 % / 51,9 % | 0,70 | 24,0 % | US$621,31 |

Las probabilidades salen de la regla del ciclo («crecimiento maduro»: 45 / 22,5 / 22,5 / 10) y no se ajustaron por indicadores: son un juicio condicional, no frecuencias observadas. Cada historia es coherente en su mecanismo: la Conservadora no es solo menor crecimiento sino menor retorno (ROIC terminal de 14,5 %); la Disrupción no presupone quiebra, sino ventas planas desde el año 3 y margen de 30 %. El DCF esperado de las tres historias activas (pesos renormalizados) es US$440,09, casi igual a la Base, porque las colas de la Conservadora (−US$183) y de la Optimista (+US$181) casi se compensan. Con MOS de 35 % sobre el DCF Base el precio de compra es US$286,48. Cambiar los pesos cambia el esperado, no el DCF Base.

### ¿Qué pasaría si todo fallara?

Si Azure converge a +9 % en el año 5, el margen cae a 43 % y el ROIC terminal a 14,5 %, la acción vale US$257,57 (−50 % frente al precio). Si además hay comoditización y las ventas se estancan desde el año 3 con margen de 30 %, vale US$122,84 (−76 %); incluso allí el balance (caja de US$76.843 millones, cobertura de intereses de 51 veces, calificación AAA) no está en riesgo: el daño es de valoración, no de solvencia. El camino contrario, hasta la Optimista, vale US$621,31 (+21 %). El precio actual no tiene soporte en las historias a la baja y solo se justifica con un resultado entre Base y Optimista.

## 12. Valoración por múltiplos: prueba independiente y secundaria

Siete métodos (EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF, P/V y P/BV; los dos últimos con peso cero). Regla del 18-oct-2026: el múltiplo de cada escenario es el que Microsoft tuvo cuando crecía como el escenario espera en FY+3 (Conservador 9,2 %, Base 16,7 %, Optimista 20,2 %), llevado al costo de capital del corte y limitado por el múltiplo justificado por los fundamentos de la misma historia; los comparables solo comprueban.

| Método | Peso en múltiplos | Mediana histórica 10a | Actual (LTM) | Cons. | Base | Opt. | Múltiplo justificado Base | Peers (mediana, solo comprobación) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| EV/EBITDA | 33 % | 20,7× | 20,0× | 7,6× | 7,8× | 11,4× | 7,8× | 16,0× |
| EV/FCFF | 17 % | 33,7× | 57,9× | 19,2× | 30,0× | 30,9× | 30,0× | 20,1× |
| P/E | 33 % | 34,4× | 28,6× | 14,2× | 20,2× | 20,8× | 20,2× | 17,3× |
| P/FCFE | 8 % | 35,2× | 57,5× | 16,2× | 23,3× | 24,0× | 23,3× | 19,6× |
| P/OCF | 8 % | 23,5× | 21,0× | 8,1× | 9,4× | 12,9× | 9,4× | 8,9× |

Resultado: múltiplos consolidados de US$210,56 (Conservador), US$279,36 (Base) y US$352,67 (Optimista), frente a DCF de US$257,57, US$440,73 y US$621,31; la brecha de la Base es −37 %. Las tres anclas (historia, peers y justificado) discrepan mucho: la historia propia de Microsoft cotizó a 15-25 veces el EBITDA, los peers (Salesforce, Intuit, Adobe, ServiceNow, Oracle, Alphabet) a unas 16 veces y los fundamentos de la Base, con FCFF de solo 26 % del EBITDA en FY+3 por la reinversión, justifican 7,8 veces. Dado el tope del ancla C, la Base queda igual al múltiplo justificado en los cinco métodos: en la práctica el múltiplo repite el DCF y no lo contrasta (H-13). El orden Cons. < Base < Opt. se rompe de forma leve en EV/FCFF y P/FCFE (Base y Optimista casi iguales) porque el tope de la Optimista es similar al de la Base.

P/V y P/BV (peso 0): Base 9,49× y 8,65×; la Optimista queda por debajo de la Base (5,80× y 6,91×) porque el ciclo elige cierres de crecimiento mayor, que son los de 2022; son informativos. Los múltiplos son precio relativo, no valor intrínseco; no se inventa un resultado de Disrupción.

## 13. Sensibilidades económicas y escenarios alternativos

| Supuesto cambiado (DCF Base US$440,73) | Valor | Variación |
|---|---:|---:|
| WACC +1 pp | US$358,64 | −18,6 % |
| WACC −1 pp | US$564,40 | +28,1 % |
| ROIC terminal = costo de capital | US$344,97 | −21,7 % |
| Crecimiento años 1-5 −2 pp | US$401,36 | −8,9 % |
| Crecimiento años 1-5 +2 pp | US$484,24 | +9,9 % |
| Crecimiento terminal −0,5 pp | US$416,10 | −5,6 % |
| Crecimiento terminal +0,5 pp | US$470,63 | +6,8 % |
| Margen objetivo −2 pp / +2 pp | US$421,62 / US$459,84 | −4,3 % / +4,3 % |
| Ventas/capital −20 % / +20 % | US$421,05 / US$453,85 | −4,5 % / +3,0 % |
| Acciones +5 % | US$419,74 | −4,8 % |

Ordenado por impacto: la tasa de descuento, el ROIC terminal, el crecimiento de los años 1-5 y el crecimiento terminal. El margen y el ventas/capital mueven menos de lo que sugiere la discusión cualitativa, porque la reinversión de los años 1-5 es alta de por sí y el valor terminal pesa 71 %. La matriz de crecimiento por margen del Nivel 2 va de US$348 (12,3 % y 46 %) a US$607 (20,3 % y 54 %); solo las celdas con crecimiento de 18-20 % y margen de 52 % o más superan US$512,90, de acuerdo con el DCF inverso. El DCF inverso con beta 1,36 (propuesta) exige 19,1 % de crecimiento con 50 % de margen.

Escenario alternativo no modelado: que el costo de capital siga en 10,93 % sin converger a 8,99 % (no se cuantificó). No se modelan recompras ni un cambio de la mezcla de arrendamientos.

## 14. Coherencia de hojas, cálculos y presentación

La hoja está unificada con la maestra: 61 pestañas en el mismo orden, 21.258 fórmulas intactas y 122 selectores idénticos; el motor independiente reproduce las cuatro historias al centavo. Controles: candados, inputs completos, estados completos e integridad de hojas (registro en la bitácora de la sesión).

Intervenciones sobre la hoja que el lector debe conocer: (i) se restauraron las fórmulas de la maestra tras cada carga; (ii) la columna L del estado de resultados se ajustó a 7.503,5 millones de acciones, que es una cifra del analista y no del reporte; (iii) el importador trajo la depreciación y amortización redondeada y se reescribió con las cifras del flujo de caja, ajustando «otros gastos operativos» para conservar las identidades de la plantilla; (iv) para unificar se redimensionaron dos pestañas a la medida de la maestra, eliminando columnas sobrantes (Tesis de Inversión y Supuestos, de 10 a 8 columnas; Escenarios e historias, de 21 a 14), cuyas celdas eran notas auxiliares de la carga y no entradas del modelo [la eliminación se hizo sin un respaldo previo de esas celdas]; (v) los sobrescritos de ROIC terminal de las historias (M6:N8 de «Escenarios e historias») se reescriben tras cada reconstrucción de esa pestaña.

Presentación: los rótulos «Jun '17» a «Jun '26» son ejercicios terminados el 30 de junio; el LTM coincide con FY26. Los múltiplos históricos de FY17-FY24 usan una deuda sin arrendamientos financieros (H-11).

## 15. Hallazgos priorizados y propuestas de corrección

| ID | Severidad | Hallazgo | Impacto | Propuesta |
|---|---|---|---|---|
| H-01 | Alta | ROIC terminal de 20 % (Base) y 24 % (Optimista) son juicio; la referencia sectorial es 29,3 % y el costo de capital 9 % | Con ROIC = costo de capital la Base vale US$344,97 (−21,7 %) | Construir una serie homogénea de ROIC incremental de la nube y de la suite; revisar la duración de la ventaja |
| H-02 | Alta | Ventas/capital 0,60 → 1,05 supone que la capacidad llega a utilizarse; el marginal observado es 0,38 a tres años y 0,43 en el último año | ±20 % mueve la Base ±4 %, pero un 0,38 sostenido reduciría el FCFF de años 1-5 | Pedir o estimar utilización y retorno por cohorte; probar 0,38 en los años 1-5 |
| H-03 | Alta | US$329.100 millones de arrendamientos firmados y no iniciados no están en balance ni en deuda | Compromiso fuera de la hoja; solo aparece vía el ventas/capital bajo | Agregar a la tabla de compromisos y medir su calendario |
| H-04 | Media | La depreciación y amortización de FY17-FY23 se tomó de los 10-K anteriores sin releerlos; FY24-FY26 sí se verificaron | El EBITDA histórico y los múltiplos EV/EBITDA pueden moverse ~1-3 % | Releer los 10-K FY17-FY23 y confirmar |
| H-05 | Media | 7.503,5 millones de acciones suponen dilución plena de 78 millones de premios; sin recompras | ±5 % de acciones: ∓4,8 % del valor | Revisar el conteo con el 10-Q del 1T FY27 |
| H-06 | Media | Crecimiento terminal de 4 % y convergencia del WACC de 10,93 % a 8,99 % | −0,5 pp de g: −5,6 %; el efecto de no converger no se modeló | Contrastar con el crecimiento nominal de largo plazo y justificar la convergencia |
| H-07 | Media | I+D capitalizado con vida de 3 años es una convención (activo de US$70.099 millones) | Cambia el EBIT ajustado y el ROIC | Probar vidas de 4-5 años |
| H-08 | Media | 48,5 % de las ventas fuera de EE. UU. sin desglose por país: prima de riesgo por regiones | Efecto menor en WACC, pero no se conoce la exposición real | Leer la nota de segmentos geográficos y rehacer la prima |
| H-09 | Baja | Inversiones de largo plazo (US$36.348 millones) a valor contable | ≈US$4,8 por acción | Revisar valor razonable de participaciones |
| H-10 | Media | Beta del sector de software (1,25) puede subestimar el riesgo de la infraestructura de Azure | +0,1 de beta ≈ +0,5 pp de costo del patrimonio | Beta mixta software + nube (peers: AMZN, GOOGL, ORCL) |
| H-11 | Media | Deuda con arrendamientos financieros separada solo desde FY25: TEV y múltiplos históricos anteriores la subestiman | Series EV/EBITDA y EV/FCFF de FY17-FY24 más bajas de lo real | Cargar la deuda por arrendamientos financieros de FY17-FY24 |
| H-12 | Media | RPO sin OpenAI, puestos de Copilot y guía de FY27 provienen del comunicado y de una fuente secundaria; el 10-K completo no se releyó | Indicadores de la tesis sin verificación primaria | Leer notas de RPO, concentración y la llamada |
| H-13 | Media | El tope del múltiplo justificado hace que los múltiplos repitan el DCF; los múltiplos consolidados (US$279,36) quedan 37 % por debajo del DCF y 45 % por debajo del precio | Los múltiplos aportan poca información independiente | Mostrar también la lectura histórica sin tope (EV/EBITDA 20×) como sensibilidad |
| H-14 | Media | Probabilidades por regla de ciclo, sin ajustar por indicadores | Cambian el esperado, no la Base | Revisar con los resultados del 1T FY27 |
| H-15 | Baja | Se eliminaron columnas sobrantes de dos pestañas sin respaldo previo para unificar | Posible pérdida de notas auxiliares de la carga | Reconstruir las notas si el usuario las necesita |

## 16. Catalizadores, señales de refutación y seguimiento

| Fecha o ventana | Evento | Confirma | Refuta |
|---|---|---|---|
| 28-oct-2026 | Resultados del 1T FY27 | Azure ≥ 33 % y margen ≥ 46 % | Azure < 30 % con capex/ventas creciente |
| Trimestral | RPO sin OpenAI y plazo | Crece con plazo menor | Plazo mayor con crecimiento menor |
| FY27 | Puestos y ARPU de Copilot | Suben con ARPU | Puestos sin ARPU |
| FY27-FY28 | Conversión flujo operativo − capex | Estable o al alza | Cae mientras el margen GAAP sube |
| Continuo | OpenAI y agentes multiplataforma | Consumo de Azure sin pérdida de puestos | Pérdida de puestos de Microsoft 365 |

Indicadores de actualización de probabilidades: si Azure crece menos de 20 % en el año 2 sube la Conservadora; si Copilot y el ARPU suben junto con el crecimiento de Azure, sube la Optimista; si el capex/ventas sube dos años seguidos sin acelerar las ventas, sube la Disrupción.

## 17. Dictamen económico y resumen para escuchar

**Dictamen: con reservas.** La hoja está bien formada y reproduce el motor; los datos de partida están conciliados con el 10-K FY2026 en lo esencial, y los supuestos que dominan el valor (tasa de descuento, ROIC terminal, ventas/capital y crecimiento) son juicios declarados, no datos. La Base de US$440,73 es una tesis exigente (16 % anual durante cinco años a una escala sin precedentes) pero coherente; el precio de US$512,90 queda entre la Base y la Optimista y el margen de seguridad de 35 % exige un precio inferior a US$286,48.

Resumen para escuchar: Microsoft es un negocio excelente que ahora invierte más capital del que nunca ha invertido. El valor de la acción depende de cuánto rinda ese capital: si Azure sigue creciendo cerca de 40 % y la capacidad se llena, la Base vale unos 440 dólares; si la adopción se frena, unos 258; y el precio de 513 ya descuenta algo mejor que la Base. Los supuestos menos respaldados son el ROIC terminal, el ventas/capital de los años 6 a 10 y los US$329.100 millones de arrendamientos que aún no están en el balance.

## 18. Fuentes primarias, limitaciones y registro de versión

Fuentes primarias: [10-K FY2026](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm) (incluida la página R6 del flujo de caja); [8-K de reexpresión de segmentos, 2-sep-2026](https://www.sec.gov/Archives/edgar/data/789019/000119312526380280/d291965dex991.htm); [comunicado de resultados del 4T FY26](https://news.microsoft.com/source/2026/07/29/microsoft-cloud-and-ai-strength-fuels-fourth-quarter-results-4/); [SEC companyfacts](https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json); [Damodaran, ERP implícita de octubre de 2026](https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx); [Damodaran, ROC por industria](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/roc.html); [Damodaran, The Stable Growth Rate](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/stablegrowthrate.htm); [acuerdo Microsoft/OpenAI](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/). Fuente secundaria: TradingKey (RPO sin OpenAI).

Limitaciones: no es una auditoría contable; no se releyeron los factores de riesgo ni las notas de vencimiento de deuda, concentración de clientes ni la declaración de poderes; los estados FY17-FY23 provienen del importador y de los 10-K anteriores; la calificación y el vencimiento medio de la deuda no se verificaron. Registro de versión: auditoría v1.3 del 26-oct-2026, vinculada a la hoja rehecha el mismo día y al artículo `MSFT-2026-10-26`; no sustituye la auditoría posterior del usuario.
