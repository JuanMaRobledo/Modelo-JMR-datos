**Comprobación adicional independiente (27-oct-2026):** lectura directa de la hoja Google nativa y contraste con el registro **activo**, no con `reference/damodaran/*_resultado.json` histórico. Las cuatro historias DCF (`Escenarios e historias!H5:H8`) son idénticas, sin diferencia numérica, a `valorEsperado.historias` (A=Base, B=Conservadora, C=Disrupción, D=Optimista) del registro publicado. `Valuation output!B35` coincide exactamente con `valorPrincipal`. Se confirmó que `Valuation output!C46` enlaza el margen Base con `Escenarios e historias!D5`. **Los 1 hallazgos consignados frente al motor antiguo son un antecedente, no evidencia de una divergencia DCF vigente; el control integral nuevo aún debe ejecutarse para clasificar cualquier otra anomalía.** No se tocaron supuestos ni resultados.

**Estado de publicación (2026-10-27): PUBLICADO CON SALVEDADES · revisión DUOL-REC-20261027-R1.** Estudio recuperado con corte del 30-sep-2026; sin cambios de supuestos, probabilidades ni pesos. Valoración, análisis fundamental y esta auditoría corresponden a la misma hoja de Google y a la misma revisión.

**Controles ejecutados el 27-oct-2026:** siete múltiplos con fórmula y resultado numérico (`verificar_multiplos_hoja.py`), fórmulas contra la maestra del 22-oct (`audit_master_formulas.py`), consistencia hoja = registro = análisis (`consistencia_migracion.py --hoja`), candados vigentes, probabilidades.

**Salvedades vigentes:**
- Estudio recuperado: precio y corte de información del 30-sep-2026; no incorpora resultados posteriores ni actualiza supuestos.
- Siete múltiplos calculados por las fórmulas originales de la hoja (7/7 con fórmula y resultado numérico; fórmulas de cálculo y múltiplos idénticas a la maestra del 22-oct-2026); P/V y P/BV con peso 0 y estado provisional.
- Candados de la plantilla del 21-oct (Financials Multiples!M34:M36) no aplican a la maestra vigente; se exigen solo los presentes en ella.
- Control de integridad de hojas con 1 hallazgo(s) frente al motor legado, sin diagnóstico económico concluyente.

**Salvedades resueltas (27-oct-2026):** H3: múltiplo de salida EV/FCFF Conservador 16,61x → 14,07x (el actual LTM; `EVFCFF!J8` de la hoja). Efecto: múltiplos Conservador 46,09 → 43,42 y valor presente ponderado Conservador 64,27 → 63,20 (objetivo FY+3 89,18 → 87,70); DCF, Base, Optimista, MOS y pesos sin cambio. S1: márgenes 23/28/32% justificados con evidencia en la base del modelo (margen LTM 24,0%; `reference/damodaran/DUOL.json`, `justificacion_supuestos.S1`); sin cambio de cifras. Versión anterior en `archivo/DUOL-antes-salvedades-20261027/`.

---

# Auditoría económica narrativa — Duolingo, Inc. (DUOL)

**Análisis fundamental vinculado:** [DUOL en la app](https://juanmarobledo.github.io/Modelo-JMR/research.html?ticker=DUOL) · registro `analisis/DUOL-research-20260929-jmr.json` (revisión del 2026-10-26).

## 1. Ficha de auditoría y alcance

| Campo | Contenido |
|---|---|
| Emisor | Duolingo, Inc.; ticker DUOL |
| Mercado, moneda y escala | Nasdaq Global Select Market (EE. UU.); US$ millones salvo por acción |
| Sector | Aprendizaje de idiomas y plataformas digitales de consumo por suscripción (Software (Internet)) (hoja: industria de Damodaran «Software (Internet)») |
| Método intrínseco principal | DCF FCFF de la historia Base (compañía operativa); MOS de 35 % sobre ese valor |
| Estados examinados | 10-K 2025 (27-feb-2026) y 10-Q del 2T26 (6-ago-2026); LTM = FY2025 + 1S26 − 1S25 (cierre 30-jun-2026) |
| Fecha de valoración / de auditoría | Corte de mercado 30-sep-2026 / 2026-10-26 |
| Precio del análisis | US$142,40 al cierre del 30-sep-2026 (corte común de la cartera); no se obtuvo un precio posterior |
| Hoja auditada | [Modelo JMR DUOL](https://docs.google.com/spreadsheets/d/1Pbpv8PYFX6HIPJOQgtoLVDGgtPh08JMxbBkUQWyMVCc/edit), rehecha desde la maestra el 2026-10-26 |
| Artículo y Nivel 2 | `JMR-valuation/data/DUOL_Research_Fundamental_Modelo_JMR_2026-10-26.md` y `DUOL_Nivel2_Datos_Modelo_JMR_2026-10-26.md` |
| Registro en la app | Se publica con la autorización general del usuario; sin certificación previa (el usuario audita después) |
| Visto | Hoja completa por lectura; 10-Q del 2T26 (balance, resultados, flujo y títulos dilutivos); 10-K 2025 (ubicación de los ingresos, impuestos, arrendamientos); carta del 2T26 a los accionistas; 8-K del 18-ago-2026; XBRL de la SEC para I+D semestral |
| Fuera de alcance | 10-K completo (factores de riesgo y litigios); transcripción de la llamada del 2T26; estados de los pares; contrato con Apple y Google; consenso y calificaciones de analistas |
| Estado de verificación | **Con reservas** (no es una auditoría contable). Ver §15 y §17 |

## 2. Resumen ejecutivo y relato económico central

Duolingo ofrece una aplicación gratuita con publicidad que convierte a una fracción de sus usuarios en suscriptores (Super y Max). En el LTM a junio de 2026 ingresó US$1.145 millones (86 % suscripciones) con un EBIT GAAP de US$157 millones (13,7 %) y caja e inversiones de US$1.417 millones sin deuda financiera. El ingreso creció 38,7 % en 2025 pero solo 10,4 % en el LTM; las reservas guiadas para 2026 crecen ~11 % porque la gerencia eligió ganar usuarios antes que monetizar. La valoración Base de US$103,27 por acción queda 27 % por debajo del precio de US$142,40 y se apoya en una recuperación del ingreso por usuario desde 2027 y en un margen GAAP de ~24 %.

**Tesis Base favorable:** La audiencia que creció en 2026 vuelve a pagar desde 2027: ingresos +11 % anual y margen GAAP de ~24 %: US$103,27 por acción. **Interpretación neutral:** Más usuarios que pagan menos: ingresos +6,4 % anual y margen GAAP de ~19 %; la Conservadora (US$76,38, 22,5 %) describe esa ruta. **Contratesis adversa:** Los asistentes de IA generalistas enseñan idiomas gratis y el hábito se rompe: ingresos −2,3 % anual y margen de ~10 % (Disrupción, US$45,74, 15,0 %).

El supuesto que domina el valor es la tasa de descuento (±1 punto de WACC mueve la Base US$93,42 (−9,5 %) / US$115,73 (+12,1 %)), seguido por el margen GAAP de largo plazo (que depende de que la compensación en acciones baje de ~15 % a ~10 % de las ventas) y el crecimiento de las suscripciones desde 2027. El precio (US$142,40) queda por encima de la Base (38 %); ver el DCF inverso en §10. Esta narrativa no se deriva del precio: parte de los estados de la compañía.

## 3. Trazabilidad, integridad y jerarquía de evidencia

Inventario de las celdas de entrada de `Input sheet`, `Cost of capital worksheet`, `R& D converter` y `Option value`, y de los datos que la hoja enlaza desde las pestañas de estados (Income Statement, Balance Sheet, Cash Flow Statement; columna L = LTM). `Financials Multiples` no tiene celdas de entrada propias: son fórmulas.

**Conteo:** la tabla tiene **88 filas** (todas las de `Input sheet` con valor, las entradas clave del costo de capital y el conversor de I+D). Las celdas con fórmula por defecto (`Input sheet!B27:B33`) se incluyen porque el analista puede sustituirlas.

**Cómo se cargaron los estados.** (a) El importador de la SEC (`desde_cero.sh datos`) cargó los ejercicios 2020-2025 y el LTM desde los XBRL; (b) el balance del LTM repetía el cierre de diciembre de 2025 y se reescribió con el 10-Q de junio de 2026 (caja 1.180,9, bonos al vencimiento de corto plazo 132,979 y de largo plazo 102,693); (c) el SG&A del LTM se recalculó (338,1) y los otros gastos operativos quedan como −D&A (15,8), sin cambiar el EBIT; (d) el promedio básico de acciones de 2023-2025 estaba en cero y se completó; (e) el conversor de I+D usa los 12 meses a junio con datos semestrales del 10-Q; (f) las acciones son 46,724 M (A y B) más 2,8 M de RSU = 49,524 M, escritas en Income Statement!L27 porque la restauración de fórmulas pisa Input!B22.

**Diferencias de fuente y ajustes:** (a) acciones: 49,524 M de la hoja frente a 46,724 M del balance (diferencia = RSU sin consolidar, 2,8 M); (b) el EBIT del LTM (157,1) coincide con el 10-Q; (c) la tasa de impuestos del LTM (−103 %) se reemplaza por 24 % en B90; (d) el activo por impuestos diferidos (206,0) queda en el balance y no se suma como valor, solo las pérdidas fiscales federales de 111,2 en B63.

| # | Pestaña | Celda | Rótulo | Valor | Tipo | Documento/fuente (URL en §18) | Quién lo aportó | Verificación |
|---:|---|---|---|---|---|---|---|---|
| 1 | Input sheet | B1 | Duolingo, Inc. (NASDAQ:DUOL) | Duolingo, Inc. (NASDAQ:DUOL) | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 2 | Input sheet | B4 | Date of valuation | sept-26 | Juicio | Corte de mercado 30-sep-2026 (fecha de valoración) | Corte común | [OBSERVADO] |
| 3 | Input sheet | B5 | Company name | Duolingo, Inc. | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 4 | Input sheet | B8 | Country of incorporation | United States | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 5 | Input sheet | B9 | Industry (US) | Software (Internet) | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 6 | Input sheet | B10 | Industry (Global) | Software (Internet) | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 7 | Input sheet | B12 | Revenues | $ 1.145,00 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 8 | Input sheet | B13 | Operating income or EBIT | $ 157,10 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 9 | Input sheet | B14 | Interest expense | $ - | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 10 | Input sheet | B15 | Book value of equity | $ 1.409,74 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 11 | Input sheet | B16 | Book value of debt | $ - | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 12 | Input sheet | B17 | Do you have R&D expenses to capitalize? | Yes | Juicio | Capitalización de I+D según la regla del sector de la empresa | IA | Decisión de método; ver hallazgos |
| 13 | Input sheet | B18 | Do you have operating lease commitments? | Yes | Juicio | Arrendamientos operativos como deuda (conversor de Damodaran) | IA | [MODELO] |
| 14 | Input sheet | B19 | Cash and Marketable Securities | $ 1.313,87 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 15 | Input sheet | B20 | Valor económico validado de participaciones y activos NO ope | $ - | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 16 | Input sheet | B21 | Minority interests | $ - | Dato | Sin participaciones minoritarias relevantes | IA | [NO VERIFICADO] en la nota de patrimonio |
| 17 | Input sheet | B22 | Number of shares outstanding = | 49,52 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 18 | Input sheet | B23 | Current stock price = | $ 142,40 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 19 | Input sheet | B24 | Effective tax rate = | 103,47% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 20 | Input sheet | B25 | Marginal tax rate = | 25,00% | Juicio | Tasa marginal federal más estatal de EE. UU. (25 %) | Plantilla/IA | Convención del modelo [MODELO] |
| 21 | Input sheet | B27 | Revenue growth rate for next year  | 11,07% | Juicio | Crecimiento del año 1 de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 22 | Input sheet | B28 | Operating Margin for next year | 18,54% | Juicio | Margen operativo del año 1 de la Base: 18,5 % en la base del modelo (~9,5 % GAAP, guía de EBITDA ajustado de 26,5 % menos compensación en acciones de ~15 % y depreciación de ~1,5 %) más ~9 pp de I+D capitalizado | IA (ficha de historias) | [HIPÓTESIS]; ver H-02 |
| 23 | Input sheet | B29 | Compounded annual revenue growth rate - years 2-5 = | 10,99% | Juicio | CAGR de los años 2-5 de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 24 | Input sheet | B30 | Referencia de margen objetivo (mediana histórica/sectorial;  | 28,04% | Juicio | Margen objetivo de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 25 | Input sheet | B31 | Year of convergence for margin | 5,00 | Juicio | Año de convergencia del margen: 5 | Plantilla/IA | Coherente con las historias |
| 26 | Input sheet | B32 | Sales to capital ratio  (for years 1-5) | 2,25 | Juicio | Ventas/capital años 1-5 (ficha de historias, ajustado por el conversor de arrendamientos) | IA | [HIPÓTESIS]; ver hallazgos |
| 27 | Input sheet | B33 | Sales to capital ratio (for years 6-10) | 2,00 | Juicio | Ventas/capital años 6-10 (ficha de historias, ajustado por el conversor de arrendamientos) | IA | [HIPÓTESIS]; ver hallazgos |
| 28 | Input sheet | B35 | Riskfree rate | 5,29% | Dato | Treasury a 10 años del corte común (30-sep-2026): 5,29 % | Corte común (datos_mercado.py) | [OBSERVADO] FRED DGS10 |
| 29 | Input sheet | B36 | Initial cost of capital = | 11,70% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 30 | Input sheet | B38 | Do you have employee options outstanding? | Yes | Dato | Opciones: 0,6 M con precio de ejercicio US$21,09, vida 3 años, volatilidad 55 % | IA (carta del 2T26, tabla de títulos dilutivos) | [OBSERVADO] el número y el precio; la vida y la volatilidad son [HIPÓTESIS] |
| 31 | Input sheet | B39 | Number of options outstanding = | 0,60 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 32 | Input sheet | B40 | Average strike price = | $21,09 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 33 | Input sheet | B41 | Average maturity = | 3,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 34 | Input sheet | B42 | Standard deviation on stock price = | 55,00% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 35 | Input sheet | B46 | Do you want to override this assumption = | No | Juicio | No se anula el WACC terminal: converge a la fórmula de la plantilla | Plantilla | [MODELO] |
| 36 | Input sheet | B47 | If yes, enter the cost of capital after year 10 = | 11,70% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 37 | Input sheet | B49 | Do you want to override this assumption = | No | Juicio | Anulación del ROIC terminal (Yes) o ROIC terminal igual al costo de capital (No) | IA | Ver hallazgos de ROIC terminal |
| 38 | Input sheet | B52 | Do you want to override this assumption = | No | Juicio | Sin probabilidad de fracaso en la Base | IA | [INFERENCIA] |
| 39 | Input sheet | B53 | If yes, enter the probability of failure = | 0% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 40 | Input sheet | B54 | What do you want to tie your proceeds in failure to? | V | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 41 | Input sheet | B55 | Enter the distress proceeds as percentage of book or fair va | 50% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 42 | Input sheet | B57 | Do you want override this assumption = | No | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 43 | Input sheet | B58 | If yes, enter a different lag (0 = no lag to 3 = lag of 3 ye | 1 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 44 | Input sheet | B60 | Do you want to override this assumption = | No | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 45 | Input sheet | B62 | Do you want to override this assumption = | Yes | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 46 | Input sheet | B63 | If yes, enter the NOL that you are carrying over into year 1 | $111,20 | Dato | Pérdidas fiscales federales sin vencimiento: US$111,2 M (10-K 2025, nota de impuestos) | IA | [OBSERVADO]; las estatales (72,4) no se suman |
| 47 | Input sheet | B65 | Do you want to override this assumption = | No | Juicio | No se anula la tasa libre después del año 10 | IA | — |
| 48 | Input sheet | B66 | If yes, enter the riskfree rate after year 10 | 5,29% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 49 | Input sheet | B68 | Do you want to override this assumption = | Yes | Juicio | Se anula el crecimiento perpetuo con la regla del modelo | IA | Ver B69 |
| 50 | Input sheet | B69 | If yes, enter the growth rate in perpetuity | 4,00% | Juicio | Crecimiento terminal 4,00 % (≤ tasa libre de 5,29 %) | Regla vigente del modelo | [MODELO] |
| 51 | Input sheet | B71 | Do you want to override this assumption | No | Juicio | Sin efectivo atrapado | IA | [NO VERIFICADO] |
| 52 | Input sheet | B72 | If yes, enter trapped cash (if taxes) or entire balance (if  | $0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 53 | Input sheet | B73 | & Average tax rate of the foreign markets where the cash is  | 0% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 54 | Input sheet | B76 | Valor de acciones preferentes (misma unidad del DCF) | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 55 | Input sheet | B78 | PV del conversor ya incluido en deuda del balance (solapamie | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 56 | Input sheet | B79 | Pasivo de arrendamientos INCREMENTAL no reconocido | $ 105,06 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 57 | Input sheet | B80 | Ajuste de EBIT atribuible a pasivos incrementales | 0,4265234414 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 58 | Input sheet | B81 | Estado de conciliación de arrendamientos | CONCILIADO | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 59 | Input sheet | B82 | Inversiones a largo plazo según balance (dato histórico; NO  | $103 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 60 | Input sheet | B83 | Valor CONTABLE de inversiones excluidas del capital operativ | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 61 | Input sheet | B84 | Valor ECONÓMICO atribuible de participaciones y activos no o | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 62 | Input sheet | B85 | Control de inversiones y doble contabilización | VALIDADO | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 63 | Input sheet | B86 | Revisión: no están incluidas en EBIT/FCFF ni duplicadas | Sin solapamiento | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 64 | Input sheet | B87 | Fuente y conciliación de inversiones no operativas | 10-Q 2T26: las inversiones de largo plazo (bonos al vencimie | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 65 | Input sheet | B89 | Método fiscal de proyección (obligatorio en cada copia) | Normalizada | Juicio | Método fiscal normalizado | IA | — |
| 66 | Input sheet | B90 | Tasa inicial NORMALIZADA (solo si B89=Normalizada) | 0,24 | Juicio | Tasa inicial normalizada de 24 % (guía de 23-25 % para 2026; 24,1 % en el 1S26) | IA | [OBSERVADO] guía; ver H-03 |
| 67 | Input sheet | B91 | Fuente / conciliación de impuesto efectivo vs marginal | Tasa efectiva: 24,1% en el 1S26 y guía de 23-25% para 2026 ( | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 68 | Input sheet | B92 | Control de hipótesis fiscales | VALIDADO | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 69 | Input sheet | B93 | Impuesto inicial para pronóstico (no altera la tasa históric | 0,24 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 70 | Input sheet | B96 | Tasa libre de riesgo nominal de largo plazo · misma moneda d | 5,29% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 71 | Input sheet | B97 | WACC terminal efectivo del modelo (independiente del DCF hab | 8,99% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 72 | Input sheet | B98 | Base | Sin liberación | Juicio | Sin liberación de capital en contracción (reinversión negativa se trunca a cero) | IA | Regla de Damodaran |
| 73 | Input sheet | B99 | Conservadora | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 74 | Input sheet | B100 | Disrupción | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 75 | Input sheet | B101 | Optimista | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 76 | Cost of capital worksheet | B12 | Which approach will you be using? | Detailed | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 77 | Cost of capital worksheet | B22 | Approach for estimating beta | Single Business(Global) | Juicio | Beta bottom-up global de Software (Internet) (desapalancada 1,34) porque 62 % de las ventas está fuera de EE. UU. | IA | [HIPÓTESIS]; la de EE. UU. (1,59) se informa como sensibilidad |
| 78 | Cost of capital worksheet | B26 | What approach do you want to use to input ERP? | Operating regions | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 79 | Cost of capital worksheet | B33 | Average Maturity = | 5 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 80 | Cost of capital worksheet | B34 | Approach for estimating pre-tax cost of debt | Direct Input | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 81 | Cost of capital worksheet | B35 | If direct input, input the pre-tax cost of debt | 5,690% | Juicio | Costo de la deuda antes de impuestos 5,69 % (5,29 % + 0,40 %, calificación sintética AAA): solo afecta a los arrendamientos | IA | [INFERENCIA]; sin deuda financiera |
| 82 | Cost of capital worksheet | B41 | Book Value of Convertible Debt = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 83 | Cost of capital worksheet | B49 | Number of Preferred Shares = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 84 | Cost of capital worksheet | B50 | Current Market Price per Share= | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 85 | Cost of capital worksheet | B51 | Annual Dividend per Share = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 86 | Cost of capital worksheet | H29 | Ingresos H29 | $392 | Dato | Ventas de 2025 en EE. UU.: 392,214 (10-K 2025, ubicación del usuario) | IA | Coincide [OBSERVADO] |
| 87 | Cost of capital worksheet | H32 | Ingresos H32 | $645 | Dato | Resto del mundo: 645,375 (10-K 2025), sin más desglose; prima país de 1,8 % | IA | [INFERENCIA] la prima |
| 88 | R& D converter | F7 | Años de amortización del I+D | 3 | Juicio | Convención de Damodaran para la industria | IA | [MODELO] |

**Jerarquía de evidencia usada:** [OBSERVADO] (documento de la compañía o comprobación directa), [INFERENCIA] (deducción de lo observado), [HIPÓTESIS] (supuesto del analista), [MODELO] (resultado de las fórmulas) y [NO VERIFICADO].

## 4. Historia financiera: diez años y punto de partida

| US$ millones | Dec '20 | Dec '22 | Dec '23 | Dec '24 | Dec '25 | LTM |
|---|---:|---:|---:|---:|---:|---:|
| Ingresos | 162 | 370 | 531 | 748 | 1.038 | 1.145 |
| EBIT | -16 | -65 | -13 | 63 | 136 | 157 |
| Margen operativo | -9,9 % | -17,6 % | -2,5 % | 8,4 % | 13,1 % | 13,7 % |
| Flujo operativo | 18 | 54 | 154 | 286 | 388 | 430 |
| Capex | -3 | -6 | -3 | -12 | -18 | -23 |
| Capex / ventas | 2,1 % | 1,5 % | 0,6 % | 1,6 % | 1,7 % | 2,0 % |

La historia tiene tres fases. De 2019 a 2023 Duolingo perdió dinero o ganó poco mientras crecía 40-55 % anual con una audiencia gratuita y una conversión a suscriptor en alza. En 2024-2025 llegó a margen operativo positivo (8,4 % y 13,1 %) y a un flujo libre de ~35 % de las ventas. En 2026 la gerencia cambió la prioridad a usuarios activos diarios: reservas de ~11 %, funciones de IA regaladas y margen menor. La Base supone que ese sacrificio se revierte desde 2027; la Conservadora que no se revierte del todo; la Disrupción que la IA generalista rompe el hábito.

## 5. Crecimiento de ingresos: de la historia a la proyección

La Base construye el ingreso por cubeta (Suscripciones US$981 millones; Publicidad US$83 millones; Duolingo English Test US$41 millones; Compras en la app y otros US$40 millones). El resultado consolidado es 11,1 %, 12,3 %, 11,5 %, 10,5 %, 9,6 % en los años 1-5 (11,0 % compuesto) y cae a 4,0 % en el año 10: ingresos de 1.930 millones en el año 5 y 2.612 millones en el año 10.

Por qué ese ritmo: [INFERENCIA] el primer año de la Base (11,1 %) sigue el ritmo de las reservas de hoy (+10,9 % en 2026, +8,9 % guiado para el 3T26) y no el +16 % de ingresos de 2026, que viene de reservas del año anterior. Desde el año 2 las suscripciones crecen 13 % y bajan a 10 %, lo que supone que el ingreso por usuario cae menos que en 2026. [OBSERVADO] los usuarios activos diarios crecieron 23 % en el 2T26 y los suscriptores pagos 17 %. La visión externa (Base Rate Book) ubica 11 % anual compuesto en el tercio alto para una empresa de su tamaño (solo ~40 % lo logró). Duda: el crecimiento de la audiencia no se ha traducido aún en reservas.

Alternativas: la Conservadora (6,4 % compuesto, año 1 de 8,2 %); la Optimista (15,0 %, año 1 de 13,5 %); la Disrupción (-2,3 %, con crecimiento terminal de 0 %). Los porcentajes son juicio del analista, no una guía publicada por la compañía.

## 6. Márgenes operativos y normalización de beneficios

La Base lleva el margen de 18,5 % en el año 1 a 28,0 % en el año 5 (ya ajustado por I+D capitalizado y arrendamientos; en base reportada 28,0 %). La Conservadora llega a 23,0 % (23,0 % reportado), la Disrupción a 14,0 % y la Optimista a 32,0 % (32,0 % reportado). Tasa impositiva: 24,0 % al inicio, convergiendo a la marginal de 25 % en el año 10.

Por qué ese margen: [OBSERVADO] el margen GAAP del LTM es 13,7 % y el de 2025 fue 13,1 %; la guía de EBITDA ajustado de 2026 (26,5 %) menos compensación en acciones (~15 %) deja ~9,5 % GAAP. La Base llega a ~24 % GAAP (28 % en la base del modelo) en cinco años, el extremo bajo de Match Group, porque Duolingo gasta el doble en I+D. [HIPÓTESIS] supone que la compensación en acciones baja de ~15 % a ~10 % de las ventas; si se quedara en 15 %, el margen de largo plazo rondaría 19 % y el valor se acercaría al de la Conservadora. Sensibilidad: ±2 puntos de margen dan US$97,50 y US$109,04.

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

La reinversión de la Base es de 70 millones en el año 1 (frente a un NOPAT de 206 millones) y el FCFF del año 1 es de 136 millones. El ventas/capital es 2,25 en los años 1-5 y 2,00 en los 6-10 (base de la hoja, que incluye I+D y arrendamientos cuando la empresa los capitaliza). Con ±20 % en el ancla, el DCF Base va de US$101,24 (−2,0 %) a US$104,62 (+1,3 %). ROIC terminal: Base 9,0 %, Conservadora 9,0 %, Disrupción 9,0 %, Optimista 9,0 %.

Evidencia: el ventas/capital de hoy es 2,38 (con I+D alineado al LTM y sin los impuestos diferidos); el marginal de 7,6 a 14,6 está inflado por los prepagos de los suscriptores. La Base usa 2,25 (años 1-5) y 2,00 (años 6-10), con el capital arrendado y el activo de I+D incluidos. El motor avisa que el capital nuevo rinde 47 % (Base), 39 % (Conservadora) y 54 % (Optimista), más del doble del ROIC terminal (9 %): ver H-01. ±20 % en el ventas/capital mueve la Base de US$101,24 a US$104,62.

## 8. Costo del capital y riesgo

Tasa libre de riesgo 5,29 % (Treasury a 10 años al 30-sep-2026), prima de riesgo de 4,82 % (ponderada por regiones de ingresos), beta desapalancada del sector 1,59 y beta apalancada 1,35 (propuesta bottom-up 1,61). WACC inicial 11,70 %; WACC terminal 8,99 %.

Dudas: (i) la beta global de Software (Internet) (1,35 reapalancada) es la del sector, no la de una app de consumo con retención de 84 %; con la beta de EE. UU. (1,61) el DCF esperado bajaría a US$98,87; (ii) el costo de capital inicial de 11,70 % se apoya en una prima de mercado de 4,82 % ponderada por regiones y en una tasa libre de riesgo de 5,29 %; (iii) la empresa no tiene deuda, así que el costo de la deuda no pesa. ±1 punto de tasa da US$115,73 (+12 %) y US$93,42 (−10 %).

Efecto: ±1 punto de WACC mueve la Base US$93,42 (−9,5 %) / US$115,73 (+12,1 %), el supuesto de mayor peso. La plantilla hace converger el WACC de 11,70 % a 8,99 % en el año 10 (convención de Damodaran).

## 9. Convergencia y valor terminal

El valor terminal es 56,8 % del valor de los activos operativos de la Base (2.262 millones de 3.980 millones). Crecimiento terminal 4,00 % (≤ la tasa libre), ROIC terminal 9,0 % y WACC terminal 8,99 %. Con −0,5 puntos de crecimiento terminal la Base vale US$102,48 (−0,8 %); con +0,5 puntos, US$104,06 (+0,8 %).

Riesgos: (i) las cuatro historias suponen ROIC terminal igual al costo de capital (9 %): Duolingo gana hoy 43 %, así que la hipótesis es conservadora si la marca y el hábito de las rachas resultan una ventaja duradera; (ii) el crecimiento terminal de 4 % es el techo permitido (menor que la tasa libre de riesgo de 5,29 %); (iii) el terminal pesa 56,8 % del valor operativo.

## 10. Validación independiente del valor intrínseco

Comprobación 1 (identidad): la hoja y el motor independiente del repositorio coinciden en las cuatro historias (Base 103,27; Conservadora 76,38; Disrupción 45,74; Optimista 133,35), lo que valida la aritmética, no la economía. Comprobación 2 (puente): activos operativos 3.980 + caja 1.314 − deuda con arrendamientos 105 − opciones 75 − preferentes 0 + no operativos 0 = patrimonio común de 5.114 millones, o US$103,27 por acción con 49,5 millones de acciones. Comprobación 3 (DCF inverso del Nivel 2, margen → crecimiento anual de los años 1-5 que justifica el precio):

| Beta | Margen | Crecimiento anual de los años 1-5 que justifica el precio | Fracción de empresas de este tamaño que lo logra |
|---|---:|---:|---:|
| 1,35 | 24,0% | 22,4% | 9,9% |
| 1,35 | 28,0% | 18,9% | 15,1% |
| 1,35 | 32,0% | 16,0% | 21,7% |
| 1,61 | 24,0% | 23,9% | 8,6% |
| 1,61 | 28,0% | 20,4% | 12,9% |
| 1,61 | 32,0% | 17,4% | 17,4% |

Comprobación 4 (múltiplos propios): el EV/EBITDA de 2025 y del LTM supera 40 veces por el hipercrecimiento de 2023-2025; la regla por ciclo lleva el múltiplo de la Base a 11,6× (EV/EBITDA), 18,2× (EV/FCFF) y 8,7× (P/E), anclados en el múltiplo justificado por crecimiento, riesgo y retorno y en pares (Spotify, Netflix, Reddit; Pinterest se excluye para P/E y EV/EBITDA). El P/E de la propia historia se excluye por el beneficio fiscal único de 2025.

## 11. Cuatro historias y probabilidades

| Historia | Probabilidad | CAGR 1-5 | Margen objetivo (ajustado / reportado) | ROIC terminal | g terminal | DCF por acción |
|---|---:|---:|---:|---:|---:|---:|
| Base · La audiencia que creció en 2026 vuelve a pagar desde 2027 | 40,0 % | 11,0 % | 28,0 % / 28,0 % | 9,0 % | 4,0 % | US$103,27 |
| Conservadora · Más usuarios que pagan menos | 22,5 % | 6,4 % | 23,0 % / 23,0 % | 9,0 % | 4,0 % | US$76,38 |
| Disrupción · Deterioro de los fundamentales | 15,0 % | -2,3 % | 14,0 % / 14,0 % | 9,0 % | 0,0 % | US$45,74 |
| Optimista · Cien millones de usuarios diarios que se monetizan | 22,5 % | 15,0 % | 32,0 % / 32,0 % | 9,0 % | 4,0 % | US$133,35 |

Las probabilidades salen de la regla del ciclo (crecimiento_alto) y no se ajustaron por indicadores: son un juicio condicional, no frecuencias observadas. El DCF esperado de las tres historias activas (pesos renormalizados) es US$104,11; con MOS de 35 % sobre el DCF Base el precio de compra es US$67,12. Cambiar los pesos cambia el esperado, no el DCF Base.

### ¿Qué pasaría si todo fallara?

Si el sacrificio de monetización de 2026 no se revierte (ingresos +6,4 % y margen de 19 %), la acción vale la Conservadora (US$76,38); si además la IA generalista rompe el hábito (ingresos −2,3 % y margen de 10 %), vale la Disrupción (US$45,74). En ambos casos el balance (US$1.417 millones sin deuda) limita la pérdida de valor por quiebra, pero no la de valor por acción.

## 12. Valoración por múltiplos: prueba independiente y secundaria

Siete métodos (EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF, P/V y P/BV; los dos últimos con peso cero). Regla del 18-oct-2026: el múltiplo de cada escenario es el que la empresa tuvo cuando crecía como el escenario espera en FY+3 (Conservador 6,5 %, Base 11,5 %, Optimista 16,4 %), llevado al costo de capital del corte y limitado por el múltiplo justificado por los fundamentos de la misma historia; los comparables solo comprueban.

| Método | Mediana histórica 10a | Actual (LTM) | Ancla de peers (mediana) | Justificado Base | Peso en múltiplos |
|---|---:|---:|---:|---:|---:|
| EV/EBITDA | 48,91× | 33,19× | 32,13× | 11,64× | 33 % |
| EV/FCFF | 49,21× | 14,07× | 25,23× | 21,72× | 17 % |
| P/E | 96,42× | 17,36× | 29,70× | 8,68× | 33 % |
| P/FCFE | 57,13× | 17,29× | 26,19× | 17,22× | 8 % |
| P/OCF | 52,91× | 16,38× | 25,12× | 13,86× | 8 % |

Resultado: múltiplos consolidados de US$43,42 (Conservador), US$52,33 (Base) y US$57,33 (Optimista), frente a DCF de US$76,38, US$103,27 y US$133,35. Lectura del 7-oct-2026 (análisis desde cero, peers al cierre del 30-sep-2026): los múltiplos son precio relativo y salen de tres anclas (etapa actual, peers ajustados −10% y justificado, λ = 0,5); los consolidados Base hoy valen ~8% menos que el DCF Base y no se movió ninguno para acercarlo. El chequeo de crecimiento implícito (paso 6.5) deja tres alertas que se explican y no se corrigen: el EV/EBITDA Base (24,2×, frente a 14,9× que implica el DCF en FY+3) da un valor ~48% mayor que el DCF llevado a FY+3 porque el mercado (cierre de 2025 a 49× y peers de crecimiento alto) paga por una monetización más rápida que la de la Base, y subir λ más lo convertiría en un eco del DCF; P/FCFE (21,1×) y P/OCF (19,9×) dan valores ~25-26% menores que lo que implica el DCF (28,6× y 26,5×) por definición: el flujo de caja suma la compensación en acciones (~13-15% de las ventas), que el DCF trata como costo. P/E y EV/FCFF son coherentes con el DCF. El DCF es el valor intrínseco; P/E y EV/FCFF son los múltiplos más confiables para Duolingo.

La brecha de la Base con los múltiplos (US$52,33 frente a US$103,27 del DCF, −49 %) viene de tres cosas: la regla por ciclo lleva el múltiplo al de una empresa que crece ~11 % y no al de los cierres de hipercrecimiento; el P/E queda anclado en el justificado (8,7×) por la exclusión de la historia; y el DCF supone ROIC terminal igual al costo de capital pero margen de ~24 % GAAP. Los saltos frente al múltiplo actual son bajadas, no subidas, y no requieren justificación de salto. Ver H-05.

## 13. Sensibilidades económicas y escenarios alternativos

| Supuesto cambiado (DCF Base US$103,27) | Valor |
|---|---:|
| WACC +1 pp / −1 pp | US$93,42 (−9,5 %) / US$115,73 (+12,1 %) |
| Crecimiento años 1-5 −2 pp / +2 pp | US$95,89 (−7,1 %) / US$111,41 (+7,9 %) |
| Margen objetivo −2 pp / +2 pp | US$97,50 (−5,6 %) / US$109,04 (+5,6 %) |
| Crecimiento terminal −0,5 pp / +0,5 pp | US$102,48 (−0,8 %) / US$104,06 (+0,8 %) |
| Ventas/capital −20 % / +20 % | US$101,24 (−2,0 %) / US$104,62 (+1,3 %) |

Ordenado por impacto: la tasa de descuento (±1 punto: +12 % / −10 %), el margen objetivo (±2 puntos: ±6 %), la dilución adicional de 5 % (−5 %) y el ventas/capital (±20 %: −2 % / +1 %). El crecimiento de los años 1-5 y el margen concentran el riesgo de la tesis; las matrices del Nivel 2 recogen esas combinaciones.

## 14. Coherencia de hojas, cálculos y presentación

La hoja está unificada con la maestra (61 pestañas en el mismo orden, 21.258 fórmulas intactas, 122 selectores idénticos) y el motor independiente reproduce las cuatro historias. Controles: candados 15/15, inputs completos, estados completos e integridad de hojas (registro en la bitácora de la sesión).

Intervenciones sobre la hoja que el lector debe conocer: (i) se restauraron las fórmulas de la maestra tras cada carga; (ii) el importador traía el balance de diciembre de 2025 en el LTM y se reescribió con el 10-Q de junio de 2026; (iii) las acciones, el EBIT y los impuestos que la restauración pisa se llevaron a celdas que sobreviven (Income Statement!L27, B28 y B90); (iv) la hoja reproduce el motor (DCF Base US$103,27) y quedó UNIFICADA con la maestra (61 pestañas, 21.258 fórmulas y 122 selectores sin pérdidas).

## 15. Hallazgos priorizados y propuestas de corrección

| ID | Severidad | Hallazgo | Impacto | Propuesta |
|---|---|---|---|---|
| H-01 | Alta | Ventas/capital de 2,25 y 2,00 implican que el capital nuevo rinde 39-54 %, más del doble del ROIC terminal (9 %) | Posible sobrevaloración del flujo de los años 1-10 si el crecimiento exige más capital del que suponen los prepagos de los suscriptores; ±20 % mueve la Base solo −2 % / +1 % | Calcular el ventas/capital marginal sin el efecto de los ingresos diferidos y probar 1,5 en los años 1-5 |
| H-02 | Alta | El margen GAAP de ~24 % depende de que la compensación en acciones baje de ~15 % a ~10 % de las ventas | Con 15 % el margen de largo plazo sería ~19 % y la Base se acercaría a la Conservadora (US$76,38) | Revisar la política de compensación en acciones del 10-K y de la carta del 2T26 y calibrar un caso con 15 % sostenido |
| H-03 | Alta | La tasa de impuestos del LTM (−103 %) refleja la liberación de la reserva de valuación de 2025 (US$256,7 M) y la hoja la reemplaza por 24 % | La utilidad y el P/E del LTM no son comparables; el activo por impuestos diferidos (206,0) no se suma como valor y las pérdidas federales (111,2) sí | Conciliar el cronograma de utilización de las pérdidas fiscales y la tasa de efectiva futura con el 10-K completo |
| H-04 | Media | El primer año de la Base (11,1 %) sigue el ritmo de las reservas y no el del ingreso reportado (+16 % en 2026) | Si el ingreso reconocido converge más lento a las reservas, el año 1 sería menor y el valor bajaría poco | Conciliar reservas, ingreso diferido y ingreso reconocido trimestre a trimestre |
| H-05 | Media | Los múltiplos de la Base (US$52,33) quedan 49 % por debajo del DCF Base y dependen de la regla por ciclo y de pares con crecimiento distinto | El consolidado de múltiplos es una lectura conservadora, no el valor intrínseco; el peso del ponderado secundario (40 %) lo arrastra | Revisar las anclas de EV/FCFF y P/E con pares de suscripción de consumo y documentar por qué Pinterest se excluye de dos métodos |
| H-06 | Media | El P/E de la historia propia (2025 y LTM) se excluye por el beneficio fiscal único y queda anclado solo en pares y justificado | El P/E tiene un peso de 12,5 % dentro de los múltiplos con una ancla menos | Calcular el P/E ajustado por el beneficio fiscal (~45×) como referencia adicional |
| H-07 | Media | El conversor de I+D usa los 12 meses a junio con I+D semestral escrito a mano en B12:B14 | Un error de transcripción movería el margen de base ajustada; no se releyeron todos los semestres contra el XBRL | Verificar 1S22-1S25 en los 10-Q correspondientes |
| H-08 | Media | Acciones: 49,524 M (46,724 M de A y B más 2,8 M de RSU); las 0,6 M de unidades del fundador sujetas a precio no se cuentan y las 0,6 M de opciones van a US$21,09 | Una dilución adicional de 5 % bajaría la Base a US$98,35 | Confirmar RSU y opciones con la nota de compensación del 10-K y la tabla de la carta del 2T26 |
| H-09 | Baja | El conversor de arrendamientos usa los compromisos del 10-K 2025 (gasto de 12,1 y calendario de 13,9 a 64,0) | El pasivo de US$93 M del 10-Q puede diferir del VP del calendario; efecto en la Base menor a 1 % | Actualizar el calendario con el 10-Q cuando lo publique |
| H-10 | Media | Las inversiones de largo plazo (US$102,7 M, bonos al vencimiento) se suman como activo no operativo y la caja restringida (2,7) no | Menos de US$2 por acción | Confirmar el vencimiento y valor razonable de los bonos con la nota de inversiones |
| H-11 | Media | La beta global (1,35) y la prima por regiones suponen que 62 % de las ventas fuera de EE. UU. pesa en el riesgo | Con la beta de EE. UU. (1,61) el esperado baja de US$104,11 a US$98,87 | Documentar el desglose real de ingresos por país con el 10-K y comparar con la tabla de Damodaran |
| H-12 | Baja | La probabilidad de la Disrupción (15 %) es un juicio sin tasa base externa | Cada 5 puntos de probabilidad mueven el esperado ~US$3 | Contrastar con casos de plataformas educativas desplazadas por tecnología |
| H-13 | Media | El precio (US$142,40) supera a las tres historias centrales; el DCF inverso exige crecer ~19 % anual con margen de 28 % | La Base queda 27 % por debajo del precio y la Optimista 6 %: el mercado paga una monetización más rápida que la de cualquier historia central | Decidir si la Optimista merece más probabilidad o si el precio descuenta el EBITDA ajustado sin compensación en acciones |

## 16. Catalizadores, señales de refutación y seguimiento

| Indicador | Último dato | Confirma Base u Optimista | Favorece Conservadora o Disrupción |
|---|---|---|---|
| Usuarios activos diarios (crecimiento interanual) | 58,7 M, +23% (2T26); +27,4% el 17-ago-2026 | ≥ +20% | ≤ +12% |
| Reservas totales (crecimiento interanual) | +8% (2T26); guía 2026 +10,9% | ≥ +13% en 2027 | ≤ +8% en 2027 |
| Suscriptores pagos | 12,7 M, +17% (2T26) | ≥ +15% | ≤ +8% |
| Retención de usuarios actuales (CURR) | 84%, récord (2T26) | ≥ 84% | < 82% |
| EBITDA ajustado / ventas | 25,9% (2T26); guía 2026 26,5% | ≥ 28% en 2027 | ≤ 24% en 2027 |
| Compensación en acciones / ventas | ~15% (guía 2026) | ≤ 12% en 2027 | ≥ 15% en 2027 |
| Margen bruto | 72,6% (2T26) | ≥ 72% | ≤ 69% |
| Acciones diluidas totales | 50,7 M (30-jun-2026); recompras de US$71,9M | Estables o en baja | Suben > 2% al año |

Indicadores de actualización de probabilidades: si las reservas del 3T26 quedan por debajo de +8,9 % sube la Conservadora; si los usuarios activos diarios dejan de crecer o las funciones de IA generalistas reducen la retención por debajo de 80 % sube la Disrupción; si las reservas aceleran por encima de +13 % con margen creciente sube la Optimista. Revisar la compensación en acciones cada trimestre.

## 17. Dictamen económico y resumen para escuchar

**Dictamen: con reservas.** La hoja está bien formada, reproduce el motor y quedó UNIFICADA con la maestra; los datos de partida están conciliados con el 10-Q del 2T26 en lo esencial. Los supuestos que dominan el valor (margen GAAP de ~24 % con compensación en acciones a la baja, y crecimiento de suscripciones desde 2027) son hipótesis del analista sin evidencia suficiente todavía; el ventas/capital y la tasa de impuestos son los puntos técnicos a revisar primero.

Resumen para escuchar: Duolingo es un negocio de suscripción liviano en capital y sin deuda, con una audiencia que crece más de 20 % pero reservas de solo 11 %. La Base de 103 dólares por acción queda 27 por ciento bajo el precio y supone que el margen sube a 24 por ciento. Lo que más mueve el valor es la compensación en acciones y la monetización de los nuevos usuarios.

## 18. Fuentes primarias, limitaciones y registro de versión

Fuentes primarias:

- [Duolingo, carta a los accionistas del 2T26 (5-ago-2026)](https://www.sec.gov/Archives/edgar/data/1562088/000162828026053299/q2fy26duolingo6-30x26share.htm)
- [Duolingo, 10-Q del 2T26 (6-ago-2026)](https://www.sec.gov/Archives/edgar/data/1562088/000162828026053603/duol-20260630.htm)
- [Duolingo, carta a los accionistas del 1T26 (4-may-2026)](https://www.sec.gov/Archives/edgar/data/1562088/000162828026029790/q1fy26duolingo3-31x26share.htm)
- [Duolingo, carta a los accionistas del 4T25 y guía 2026 (26-feb-2026)](https://www.sec.gov/Archives/edgar/data/1562088/000162828026012246/q4fy25duolingo12-31x25shar.htm)
- [Duolingo, 10-K 2025 (27-feb-2026)](https://www.sec.gov/Archives/edgar/data/1562088/000162828026012494/duol-20251231.htm)
- [Duolingo, 8-K del programa de recompra de US$400M (26-feb-2026)](https://www.sec.gov/Archives/edgar/data/1562088/000162828026012246/duol-20260226.htm)
- [Duolingo, 8-K del cambio de CFO (12-ene-2026)](https://www.sec.gov/Archives/edgar/data/1562088/000162828026001730/duol-20260108.htm)
- [Duolingo, 8-K de la nueva consejera (10-ago-2026)](https://www.sec.gov/Archives/edgar/data/1562088/000162828026055015/duol-20260810.htm)
- [Duolingo, 8-K (Reg FD) sobre los usuarios de agosto (18-ago-2026)](https://www.sec.gov/Archives/edgar/data/1562088/000162828026057818/duol-20260818.htm)
- [The Motley Fool, transcripción de la llamada del 2T26 (5-ago-2026)](https://www.fool.com/earnings/call-transcripts/2026/08/12/duolingo-duol-q2-2026-earnings-call-transcript/)
- [Yahoo Finance/Reuters, caída tras la guía de 2026 (26-feb-2026)](https://finance.yahoo.com/news/duolingo-prioritizes-user-growth-over-210210779.html)
- [TIKR, mejora de Evercore ISI (29-sep-2026)](https://www.tikr.com/blog/duolingo-duol-stock-evercore-upgrade-survey-data-daus)
- [Damodaran, ERP implícita de octubre de 2026](https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx)
- [Damodaran, betas por industria (enero de 2026)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
- [Mauboussin y Callahan, The Base Rate Book (2016)](https://www.credit-suisse.com/media/assets/corporate/docs/about-us/research/publications/the-base-rate-book-integrating-the-past-to-better-anticipate-the-future.pdf)

Limitaciones: no es una auditoría contable; no se releyeron los factores de riesgo del 10-K ni los contratos con Apple y Google; el desglose geográfico fuera de EE. UU. no está publicado; los datos de la mejora de Evercore y de la pantalla del 8-K del 18-ago-2026 provienen de fuentes secundarias; el consenso no se verificó. Registro de versión: auditoría v1.3 del 2026-10-26, vinculada a la hoja rehecha el mismo día y al artículo `DUOL-2026-10-26`; no sustituye la auditoría posterior del usuario.
