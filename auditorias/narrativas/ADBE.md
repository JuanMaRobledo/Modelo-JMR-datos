**Estado de publicación (2026-10-27): PUBLICADO CON SALVEDADES · revisión ADBE-REC-20261027-R1.** Estudio recuperado con corte del 30-sep-2026; sin cambios de supuestos, probabilidades ni pesos. Valoración, análisis fundamental y esta auditoría corresponden a la misma hoja de Google y a la misma revisión.

**Controles ejecutados el 27-oct-2026:** siete múltiplos con fórmula y resultado numérico (`verificar_multiplos_hoja.py`), fórmulas contra la maestra del 22-oct (`audit_master_formulas.py`), consistencia hoja = registro = análisis (`consistencia_migracion.py --hoja`), candados vigentes, probabilidades.

**Salvedades vigentes:**
- Estudio recuperado: precio y corte de información del 30-sep-2026; no incorpora resultados posteriores ni actualiza supuestos.
- Siete múltiplos calculados por las fórmulas originales de la hoja (7/7 con fórmula y resultado numérico; fórmulas de cálculo y múltiplos idénticas a la maestra del 22-oct-2026); P/V y P/BV con peso 0 y estado provisional.
- Candados de la plantilla del 21-oct (Financials Multiples!M34:M36) no aplican a la maestra vigente; se exigen solo los presentes en ella.
- Control de integridad de hojas con 4 hallazgo(s) frente al motor legado, sin diagnóstico económico concluyente.

---

# Auditoría económica narrativa — Adobe Inc. (ADBE)

**Análisis fundamental vinculado:** [ADBE en la app](https://juanmarobledo.github.io/Modelo-JMR/research.html?ticker=ADBE) · registro `analisis/ADBE-research-1790475622244-a6a92.json` (revisión del 26-oct-2026).

## 1. Ficha de auditoría y alcance

| Campo | Contenido |
|---|---|
| Emisor | Adobe Inc., sociedad de Delaware (EE. UU.); acción ordinaria de clase única; ticker ADBE |
| Mercado, moneda y escala | Nasdaq Global Select Market; US$ millones salvo por acción |
| Sector | Software de creación, documentos y experiencia de cliente (hoja: industria de Damodaran «Software (System & Application)») |
| Método intrínseco principal | DCF FCFF de la historia Base (compañía operativa); MOS de 35 % sobre ese valor |
| Estados examinados | 10-K FY2025 (15-ene-2026) y 10-Q del 3T FY26 (22-sep-2026); LTM = FY2025 + 9M26 − 9M25 (cierre 28-ago-2026) |
| Fecha de valoración / de auditoría | Corte de mercado 30-sep-2026 / 26-oct-2026 |
| Precio del análisis | US$239,94 al cierre del 30-sep-2026 (Alpha Vantage, consultado el 26-oct-2026); no se obtuvo un precio de hoy distinto (el 23-oct cerraba en 263,82) |
| Hoja auditada | [Modelo JMR ADBE](https://docs.google.com/spreadsheets/d/1MhEO0NxlQ7ufHGQODjowcaCBDEyef4PxsC9ANLT2VBo/edit), rehecha desde la maestra el 26-oct-2026 |
| Artículo y Nivel 2 | `JMR-valuation/data/ADBE_Research_Fundamental_Modelo_JMR_2026-10-26.md` y `ADBE_Nivel2_Datos_Modelo_JMR_2026-10-26.md` |
| Registro en la app | Se publica con la autorización general del usuario; sin certificación previa (el usuario audita después) |
| Visto | Hoja completa por lectura; 10-Q del 3T FY26 (páginas R: balance, resultados, flujo, ingresos, compensación en acciones); comunicado del 3T; 8-K del 2-sep y 14-jul-2026; Alpha Vantage |
| Fuera de alcance | 10-K completo (factores de riesgo, vencimientos de la deuda, concentración); transcripción de la llamada; declaración de poderes; estados de pares; calificaciones crediticias; vigilancia posterior al 26-oct-2026 |
| Estado de verificación | **Con reservas** (no es una auditoría contable). Ver §15 y §17 |

## 2. Resumen ejecutivo y relato económico central

Adobe vende suscripciones de software para crear, editar y firmar contenido (Creative Cloud, Acrobat, Express, Firefly) y soluciones de experiencia de cliente. En el LTM a agosto de 2026 ingresó US$25.970 millones (+9,3 % sobre FY2025), con margen operativo GAAP de 35,7 % y flujo operativo de US$10.806 millones; 97 % de los ingresos son suscripciones [OBSERVADO: 10-K FY2025 y 10-Q del 3T FY26].

Lo que cambia: el crecimiento se acelera (10,5 % en FY25; +13 % en el 3T FY26; guía de FY26 elevada a US$26.576-26.626 millones, +12 %), el ARR total llega a US$27.500 millones (+10,2 % previsto al cierre) y el ARR «AI-first» crece más de 150 %. Al mismo tiempo, el costo de ingresos sube de 10,7 % a 11,3 % de las ventas por el cómputo de la IA, la compensación en acciones es 8 % de las ventas, y el liderazgo cambia (nuevo CEO el 1-dic-2026, CFO interino, salida del presidente de Creatividad y Productividad). La acción cayó 32 % en doce meses y cotiza a 14 veces la utilidad.

El motor de crecimiento de la Base es la suma de tres líneas calculadas con la mezcla de los nueve meses de 2026 (el LTM por grupo no se publica): Creative & Marketing Professionals +10 % el primer año y desacelerando a +6 %, Business Professionals & Consumers +14 % a +8 % y otros sin crecimiento, para un crecimiento compuesto de 8,1 % a cinco años (10,8 % el primer año). La ventaja competitiva que sostendría los beneficios son los costos de cambio y el estándar de la industria creativa y documental; el análisis la califica de «ventaja durable» con ROIC terminal de 29,3 % (referencia del sector).

**Tesis Base favorable:** la IA se cobra dentro de la suscripción, el crecimiento desacelera suavemente y el margen reportado llega a 37,5 %: US$399,02 por acción. **Interpretación neutral:** el precio realizado cae por competencia: la Conservadora (US$250,15) describe esa ruta con probabilidad de 20 %. **Contratesis adversa:** la IA generativa comoditiza la creatividad (Disrupción, US$167,70, probabilidad 10 %).

El supuesto que domina el valor es la tasa de descuento (±1 punto de WACC mueve la Base −17,0 % / +25,5 %), seguido del ROIC terminal (igual al costo de capital: −22,9 %) y del crecimiento de los años 1-5 (±2 puntos: −9,6 % / +10,6 %). La contradicción que la empresa debe resolver es cómo sostener 12-13 % de crecimiento y 45 % de margen no-GAAP cuando el cómputo de la IA y la compensación en acciones presionan el margen. Esta narrativa no se deriva del precio: parte de los estados del 10-Q y del comunicado del 3T.

## 3. Trazabilidad, integridad y jerarquía de evidencia

Inventario de las celdas de entrada de `Input sheet`, `Cost of capital worksheet`, `R& D converter` y `Option value`, y de los datos que la hoja enlaza desde las pestañas de estados (Income Statement, Balance Sheet, Cash Flow Statement; columna L = LTM). `Financials Multiples` no tiene celdas de entrada propias: son fórmulas.

**Conteo:** la tabla tiene **87 filas** (todas las de `Input sheet` con valor, las entradas del costo de capital agrupadas por función y las de `R& D converter` y `Option value`); las celdas de rótulo no se cuentan. Las celdas con fórmula por defecto (`Input sheet!B27:B30`) se incluyen porque el analista puede sustituirlas.

**Cómo se cargaron los estados.** (a) El importador de la SEC (`desde_cero.sh datos`) cargó diez ejercicios (2016-2025) y el LTM desde los XBRL; (b) la auditoría de estados contra la SEC corrigió 7 celdas (totales del LTM); (c) el importador deja las partidas del balance LTM con las cifras de noviembre de 2025 y solo corrige los totales, así que se reescribió la columna L del balance con el 10-Q del 3T FY26 (`scripts/adbe_datos_cero.py`); (d) SG&A del LTM = 8.061 + (5.419 + 1.497) − (4.760 + 1.152) = 9.065 y «otros gastos operativos» como diferencia contra el EBIT de 9.271; (e) la variación neta de caja (fila 40 del flujo de caja) se completó con la diferencia del efectivo del balance; (f) el conversor de arrendamientos operativos usó los compromisos del 10-K (VP de US$403 M); (g) ceros explícitos en `Balance Sheet` filas 7 y 21 y `Entradas históricas auxiliares` filas 3 a 5 (la maestra del 22-oct los exige).

**Diferencias de fuente y ajustes:** (a) acciones: 389,2 M de la portada del 10-Q más 11,7 M de RSU esperadas a consolidar = 400,9 M, frente a 391 M en circulación al 28-ago (balance); (b) la agrupación de partidas del balance (otros activos de largo plazo = derecho de uso + impuestos diferidos + otros; otros pasivos corrientes = acumulados + impuestos + arrendamientos operativos) sigue la del ejercicio 2025 de la hoja; (c) los rótulos «Dec '16» y «Dec '21-'23» de las columnas son los del importador: los ejercicios terminan entre fines de noviembre y principios de diciembre.

| # | Pestaña | Celda | Rótulo | Valor | Tipo | Documento/fuente | Quién lo aportó | Verificación |
|---:|---|---|---|---|---|---|---|---|
| 1 | Input sheet | B1 | ADOBE INC. (NASDAQ:ADBE) | ADOBE INC. (NASDAQ:ADBE) | Cálculo | Título de la hoja | Plantilla | Coincide |
| 2 | Input sheet | B4 | Date of valuation | sept-26 | Juicio | Corte de mercado 30-sep-2026 (fecha de valoración) | Corte común | [OBSERVADO] |
| 3 | Input sheet | B5 | Company name | ADOBE INC. | Dato | 10-K FY2025 (SEC, 15-ene-2026), portada | IA | Coincide [OBSERVADO] |
| 4 | Input sheet | B8 | Country of incorporation | United States | Dato | 10-K FY2025 (SEC, 15-ene-2026), portada: Estados Unidos (Delaware) | IA | Coincide [OBSERVADO] |
| 5 | Input sheet | B9 | Industry (US) | Software (System & Application) | Juicio | Damodaran, industrias de EE. UU., enero de 2026: «Software (System & Application)» | IA | Existe en Industry Averages(US) [INFERENCIA] |
| 6 | Input sheet | B10 | Industry (Global) | Software (System & Application) | Juicio | Damodaran, industrias globales, enero de 2026 | IA | Ídem |
| 7 | Input sheet | B12 | Revenues | $ 25.970,00 | Cálculo | 10-K FY2025 (SEC, 15-ene-2026) + 10-Q del 3T FY26 (SEC, 22-sep-2026): 23.769 + 19.776 − 17.575 = 25.970 | Hoja (Income Statement!L3) | Recalculado [OBSERVADO] |
| 8 | Input sheet | B13 | Operating income or EBIT | $ 9.271,00 | Cálculo | 8.706 + 7.010 − 6.445 = 9.271 (EBIT GAAP) | Hoja (Income Statement!L12) | Recalculado [OBSERVADO] |
| 9 | Input sheet | B14 | Interest expense | $ 260,00 | Cálculo | Gasto por intereses LTM: US$260 M | Hoja (Income Statement!L15) | Recalculado [OBSERVADO] |
| 10 | Input sheet | B15 | Book value of equity | $ 11.764,00 | Dato | 10-Q del 3T FY26 (SEC, 22-sep-2026), balance al 28-ago-2026: patrimonio US$11.764 M | Hoja (Balance Sheet!L35) | Coincide [OBSERVADO] |
| 11 | Input sheet | B16 | Book value of debt | $ 6.363,00 | Cálculo | 10-Q del 3T FY26 (SEC, 22-sep-2026): deuda corriente 1.597 + largo plazo 4.766 = 6.363 (los arrendamientos operativos no están en este saldo) | Hoja (Balance Sheet!L20+L21+L25+L26) | Coincide [OBSERVADO] |
| 12 | Input sheet | B17 | Do you have R&D expenses to capitalize? | Yes | Juicio | Se capitaliza el I+D a 3 años (Damodaran, software) | IA | Convención del modelo [MODELO]; ver H-03 |
| 13 | Input sheet | B18 | Do you have operating lease commitments? | Yes | Juicio | US GAAP: arrendamientos operativos fuera de la deuda; se usa el conversor (VP US$403 M) | IA | Procede [OBSERVADO: 10-K FY2025, compromisos] |
| 14 | Input sheet | B19 | Cash and Marketable Securities | $ 5.639,00 | Cálculo | 10-Q del 3T FY26 (SEC, 22-sep-2026): efectivo 4.359 + inversiones a corto plazo 1.280 = 5.639 | Hoja (Balance Sheet!L5) | Coincide [OBSERVADO] |
| 15 | Input sheet | B20 | Valor económico validado de participaciones y activos NO operativos (no duplicados) | $ - | Cálculo | Valor económico de participaciones no operativas: 0 | IA (B84) | [INFERENCIA] |
| 16 | Input sheet | B21 | Minority interests | $ - | Dato | 10-K FY2025 (SEC, 15-ene-2026): sin participaciones minoritarias | IA | [OBSERVADO] |
| 17 | Input sheet | B22 | Number of shares outstanding = | 400,90 | Dato | Portada del 10-Q: 389,2 M de acciones + 11,7 M de RSU esperadas a consolidar (10-Q del 3T FY26 (SEC, 22-sep-2026), nota de compensación) = 400,9 M | Hoja (Income Statement!L27) | Las PSU no se incluyeron [NO VERIFICADO]; ver H-04 |
| 18 | Input sheet | B23 | Current stock price = | $ 239,94 | Dato | Cierre del 30-sep-2026: US$239,94 (Alpha Vantage TIME_SERIES_MONTHLY, consultado el 26-oct-2026) | Corte común (D1) | Contrastado [OBSERVADO] |
| 19 | Input sheet | B24 | Effective tax rate = | 21,52% | Cálculo | Impuesto LTM / utilidad antes de impuestos | Hoja (Income Statement!L29) | 21,5 % [OBSERVADO] |
| 20 | Input sheet | B25 | Marginal tax rate = | 25,00% | Juicio | Tasa marginal federal más estatal de EE. UU. (25 %) | IA | Convención del modelo [MODELO] |
| 21 | Input sheet | B27 | Revenue growth rate for next year  | 9,26% | Cálculo | Predeterminado de la plantilla (crecimiento LTM sobre 2025: 9,26 %) | Plantilla | No gobierna la Base (año 1 de la Base: 10,8 %) |
| 22 | Input sheet | B28 | Operating Margin for next year | 38,84% | Cálculo | Enlace a Valuation output!B6: margen base con I+D capitalizado y arrendamientos (38,84 %) | Hoja | [MODELO]; reportado 35,7 % |
| 23 | Input sheet | B29 | Compounded annual revenue growth rate - years 2-5 = | 9,26% | Cálculo | Predeterminado de la plantilla (=B27) | Plantilla | No gobierna la Base |
| 24 | Input sheet | B30 | Referencia de margen objetivo (mediana histórica/sectorial; NO activa en historias) | 33,08% | Cálculo | Mediana de referencia (no activa) | Plantilla | Informativa |
| 25 | Input sheet | B31 | Year of convergence for margin | 5,00 | Juicio | Año de convergencia del margen: 5 | Plantilla/IA | Coherente con las historias |
| 26 | Input sheet | B32 | Sales to capital ratio  (for years 1-5) | 1,22 | Juicio | Ventas/capital 1-5 = 1,22: nivel actual con I+D capitalizado (25.970 / 21.760 = 1,19); marginal 3 años 3,4; sector 1,54 | IA | [HIPÓTESIS]; ver H-05 |
| 27 | Input sheet | B33 | Sales to capital ratio (for years 6-10) | 1,22 | Juicio | Ventas/capital 6-10 = B32 | IA | Ídem |
| 28 | Input sheet | B35 | Riskfree rate | 5,29% | Dato | FRED DGS10, cierre del 30-sep-2026: 5,29 % | Corte común | Contrastado [OBSERVADO] |
| 29 | Input sheet | B36 | Initial cost of capital = | 10,60% | Cálculo | Enlace a Cost of capital worksheet!B14: 10,59 % | Hoja | [MODELO] |
| 30 | Input sheet | B38 | Do you have employee options outstanding? | No | Dato | 10-Q del 3T FY26 (SEC, 22-sep-2026): compensación con RSU y PSU; sin opciones relevantes en circulación | IA | [NO VERIFICADO] en detalle; las RSU entran en B22 |
| 31 | Input sheet | B39 | Number of options outstanding = | 0,00 | Dato | 0 | IA | Inmaterial |
| 32 | Input sheet | B40 | Average strike price = | $0,00 | Dato | 0 | IA | Inmaterial |
| 33 | Input sheet | B41 | Average maturity = | 0,00 | Dato | 0 | IA | Inmaterial |
| 34 | Input sheet | B42 | Standard deviation on stock price = | 0,00% | Dato | 0 | IA | Inmaterial |
| 35 | Input sheet | B46 | Do you want to override this assumption = | No | Juicio | No se fija el WACC terminal a mano: tasa libre + prima madura | IA | Correcto: 8,99 % terminal |
| 36 | Input sheet | B47 | If yes, enter the cost of capital after year 10 = | 10,60% | Cálculo | Predeterminado (=B36), sin uso | Plantilla | Sin efecto |
| 37 | Input sheet | B49 | Do you want to override this assumption = | Yes | Juicio | Se fija el ROIC terminal a mano | IA | Regla de ventaja durable (referencia sectorial) |
| 38 | Input sheet | B50 | If yes, enter the return on capital you expect after year 10 | 29,32% | Juicio | ROIC terminal 29,32 %: ROIC de Software (System & Application), EE. UU., Damodaran, enero de 2026 (ajustado por arrendamientos e I+D); no supera el ROIC actual de 36,4 % | IA | [HIPÓTESIS]; ver H-01 |
| 39 | Input sheet | B52 | Do you want to override this assumption = | No | Juicio | Sin probabilidad de fracaso | IA | Flujo positivo, deuda neta ≈ 0 [OBSERVADO] |
| 40 | Input sheet | B53 | If yes, enter the probability of failure = | 0% | Juicio | 0 % | IA | Ídem |
| 41 | Input sheet | B54 | What do you want to tie your proceeds in failure to? | V | Juicio | V | Plantilla | No se activa |
| 42 | Input sheet | B55 | Enter the distress proceeds as percentage of book or fair value | 50% | Juicio | 50 % | Plantilla | No se activa |
| 43 | Input sheet | B57 | Do you want override this assumption = | No | Juicio | Rezago de reinversión: predeterminado | Plantilla | Predeterminado |
| 44 | Input sheet | B58 | If yes, enter a different lag (0 = no lag to 3 = lag of 3 years) | 1 | Juicio | Rezago 1 año (no activo) | Plantilla | Predeterminado |
| 45 | Input sheet | B60 | Do you want to override this assumption = | No | Juicio | Sin ajuste de convergencia fiscal adicional (se usa B89) | IA | Coherente |
| 46 | Input sheet | B62 | Do you want to override this assumption = | No | Dato | 10-K FY2025 (SEC, 15-ene-2026): sin pérdidas fiscales acumuladas relevantes | IA | [OBSERVADO] |
| 47 | Input sheet | B63 | If yes, enter the NOL that you are carrying over into year 1 | $0,00 | Dato | 0 | IA | Ídem |
| 48 | Input sheet | B65 | Do you want to override this assumption = | No | Juicio | No se usa tasa libre distinta después del año 10 | IA | Correcto (g ≤ tasa libre) |
| 49 | Input sheet | B66 | If yes, enter the riskfree rate after year 10 | 5,29% | Dato | 5,29 % (no activa) | Plantilla | Sin efecto |
| 50 | Input sheet | B68 | Do you want to override this assumption = | Yes | Juicio | Se fija el crecimiento perpetuo a mano | IA | Regla del corte: 4,0 % |
| 51 | Input sheet | B69 | If yes, enter the growth rate in perpetuity | 4,00% | Juicio | g terminal 4,00 %; techo = tasa libre (5,29 %) | IA/corte | ≤ 5,29 % [MODELO] |
| 52 | Input sheet | B71 | Do you want to override this assumption | No | Juicio | Sin efectivo atrapado adicional | IA | [NO VERIFICADO]: el 10-K detalla efectivo en filiales extranjeras |
| 53 | Input sheet | B72 | If yes, enter trapped cash (if taxes) or entire balance (if mistrust) | $0,00 | Juicio | US$0 | IA | Ídem |
| 54 | Input sheet | B73 | & Average tax rate of the foreign markets where the cash is trapped | 0% | Juicio | 0 % | IA | Ídem |
| 55 | Input sheet | B76 | Valor de acciones preferentes (misma unidad del DCF) | 0 | Dato | 10-K FY2025 (SEC, 15-ene-2026): sin acciones preferentes emitidas | IA | Coincide [OBSERVADO] |
| 56 | Input sheet | B78 | PV del conversor ya incluido en deuda del balance (solapamiento) | 0 | Juicio | PV del conversor ya incluido en la deuda: 0 (B16 no incluye arrendamientos operativos) | IA | Coherente [OBSERVADO] |
| 57 | Input sheet | B79 | Pasivo de arrendamientos INCREMENTAL no reconocido | $ 400,63 | Cálculo | Pasivo de arrendamientos incremental (conversor) | Hoja | — |
| 58 | Input sheet | B80 | Ajuste de EBIT atribuible a pasivos incrementales | 25,22856891 | Cálculo | Ajuste de EBIT por arrendamientos (conversor): +US$24,8 M | Hoja | — |
| 59 | Input sheet | B81 | Estado de conciliación de arrendamientos | CONCILIADO | Cálculo | CONCILIADO | Plantilla | — |
| 60 | Input sheet | B82 | Inversiones a largo plazo según balance (dato histórico; NO valor razonable) | $0 | Cálculo | Inversiones a largo plazo según balance: 0 | Hoja | — |
| 61 | Input sheet | B83 | Valor CONTABLE de inversiones excluidas del capital operativo | 0 | Juicio | 0 | IA | Escrito para validar B85 |
| 62 | Input sheet | B84 | Valor ECONÓMICO atribuible de participaciones y activos no operativos | 0 | Juicio | Valor económico de inversiones estratégicas: 0 (están en otros activos y no tienen valor de mercado reportado) | IA | Criterio conservador [INFERENCIA] |
| 63 | Input sheet | B85 | Control de inversiones y doble contabilización | VALIDADO | Cálculo | VALIDADO | Plantilla | — |
| 64 | Input sheet | B86 | Revisión: no están incluidas en EBIT/FCFF ni duplicadas | Sin solapamiento | Juicio | Sin solapamiento | IA | [INFERENCIA] |
| 65 | Input sheet | B87 | Fuente y conciliación de inversiones no operativas | 10-Q del 3T FY26 (28-ago-2026): las inversiones estratégicas están en otros acti | Juicio | Texto de fuente de B84 | IA | — |
| 66 | Input sheet | B89 | Método fiscal de proyección (obligatorio en cada copia) | Normalizada | Juicio | Método fiscal: normalizada | IA | Política del modelo |
| 67 | Input sheet | B90 | Tasa inicial NORMALIZADA (solo si B89=Normalizada) | 0,225 | Juicio | Tasa inicial 22,5 %: efectiva de 22,6 % en los 9M26, 18,5 % en los 9M25, 21,5 % LTM; objetivo GAAP FY26 de 22,5 % | IA | [OBSERVADO] comunicado del 3T |
| 68 | Input sheet | B91 | Fuente / conciliación de impuesto efectivo vs marginal | Tasa efectiva: 22,6 % en los 9M del FY26 (1.589/7.017), 18,5 % en los 9M del FY2 | Juicio | Texto de conciliación fiscal | IA | — |
| 69 | Input sheet | B92 | Control de hipótesis fiscales | VALIDADO | Cálculo | VALIDADO | Plantilla | — |
| 70 | Input sheet | B93 | Impuesto inicial para pronóstico (no altera la tasa histórica) | 0,225 | Cálculo | 22,5 % | Plantilla | — |
| 71 | Input sheet | B96 | Tasa libre de riesgo nominal de largo plazo · misma moneda del DCF | 5,29% | Cálculo | Tasa libre de largo plazo (=B35) | Plantilla | — |
| 72 | Input sheet | B97 | WACC terminal efectivo del modelo (independiente del DCF habilitado) | 8,99% | Cálculo | WACC terminal 8,99 % | Plantilla | — |
| 73 | Input sheet | B98 | Base | Sin liberación | Juicio | Sin liberación de capital (Base) | IA | Texto de justificación en C98 |
| 74 | Input sheet | B99 | Conservadora | Sin liberación | Juicio | Sin liberación (Conservadora) | IA | Ídem |
| 75 | Input sheet | B100 | Disrupción | Sin liberación | Juicio | Sin liberación (Disrupción) | IA | Ídem |
| 76 | Input sheet | B101 | Optimista | Sin liberación | Juicio | Sin liberación (Optimista) | IA | Ídem |
| 77 | Cost of capital worksheet | B12 | Enfoque de costo de capital | Detailed | Juicio | Detallado: beta, prima y costo de la deuda explícitos | IA | Correcto |
| 78 | Cost of capital worksheet | B22 | Enfoque de beta | Single Business(US) | Juicio | Beta bottom-up de Software (System & Application), EE. UU. (Damodaran, ene-2026): 1,25 desapalancada corregida por caja, reapalancada por la D/E de mercado (~6 %) → 1,31 | IA | [MODELO]; regresión del ADBE (1,39 a 5 años; 0,97 a 2 años) solo de referencia [NO VERIFICADO] |
| 79 | Cost of capital worksheet | B26 | Enfoque de la prima de riesgo | Operating regions | Juicio | Prima ponderada por regiones con ingresos de los 9M26 (Américas 11.601 → Norteamérica; EMEA 5.400; APAC 2.775 → Asia) y prima madura de 3,70 % (Damodaran) | IA | ERP 4,36 % [MODELO]; Américas incluye Latinoamérica y APAC incluye Japón y Australia [HIPÓTESIS] |
| 80 | Cost of capital worksheet | H6, H17 | Ingresos por país (US$ M) | EE. UU. 13.764; resto 12.206 | Dato | Peso de EE. UU. de 53 % tomado de la edición anterior; no se usa con el enfoque de regiones | IA | [NO VERIFICADO] |
| 81 | Cost of capital worksheet | H37, H53 | Ingresos por industria | 25.970 (Software (System & Application)) | Cálculo | Igual a B12 | IA | Coincide |
| 82 | Cost of capital worksheet | B33 | Vencimiento medio de la deuda | 4,2 años | Juicio | Heredado de la hoja anterior; el 10-K detalla los vencimientos de las notas | IA | [NO VERIFICADO] |
| 83 | Cost of capital worksheet | B34 y B36 | Costo de la deuda: calificación real | A1/A+ → 5,80 % antes de impuestos | Dato | Calificaciones de Moody's y S&P citadas en el 10-K; no releídas en esta sesión | IA | [NO VERIFICADO] |
| 84 | Cost of capital worksheet | B41:B44, B49:B51 | Deuda convertible y preferentes | 0 | Dato | 10-K FY2025 (SEC, 15-ene-2026): sin deuda convertible ni preferentes | IA | [OBSERVADO] |
| 85 | Cost of capital worksheet | B13, B23, B27, B35 | Entradas directas (no activas) | 9,00 % / 1,20 / 6,00 % / 4,00 % | Plantilla | Predeterminados; los enfoques elegidos no las usan | Plantilla | Sin efecto |
| 86 | R& D converter | F7 | Vida útil del I+D | 3 años | Juicio | Damodaran: software, 3 años; I+D de diez años en B12:B21 | IA | [MODELO] |
| 87 | Option value | B9 | Rendimiento por dividendo | 0 | Plantilla | Sin opciones (Input!B38 = No) | Plantilla | Sin efecto |


## 4. Historia financiera: diez años y punto de partida

Reconstrucción con diez ejercicios (2016-2025) y LTM, a partir de la hoja (Nivel 2). Ingresos de US$5.854 M (2016) a US$23.769 M (2025), CAGR de 16,7 %, con un quiebre: 24-25 % de crecimiento hasta 2019, 15 % en 2020, 23 % en 2021, 11,5 % en 2022, 10 % en 2023-2025 y 9,3 % del LTM sobre 2025.

| Métrica | Último (2025) | LTM | Promedio 3 años | Promedio 5 años | Rango 2016-2025 |
|---|---:|---:|---:|---:|---|
| Crecimiento de ingresos | 10,5 % | 9,3 % sobre 2025 | 10,5 % | 13,2 % | 10,2 %-24,7 % |
| Margen operativo GAAP | 36,6 % | 35,7 % | 34,1 % | 34,7 % | 25,5 %-36,8 % |
| Margen de flujo libre (operativo − capex) | 41,4 % | 40,8 % | 37,9 % | 39,9 % | 34,1 %-43,6 % |
| ROIC sin I+D (EBIT × (1 − 25 %) / capital) | 58,1 % | 55,7 % | 47,1 % | 42,5 % | 20,8 %-58,1 % |
| ROE | 61,3 % | 61,9 % | 44,5 % | 40,0 % | 15,7 %-61,3 % |
| Acciones en circulación (M) | 413 | 401 | −4,7 % anual | −3,4 % anual | 494 → 401 (−19 %) |
| Deuda neta / EBITDA | −0,04 | 0,07 | −0,30 | −0,29 | −1,58 a 0,28 |

Separación de efectos: (i) ciclo: la demanda de software por suscripción es poco cíclica; (ii) contables: el ejercicio 2020 incluye ganancias de inversiones (utilidad neta de US$5.260 M) y el 2024 el cargo de US$1.000 M por la ruptura del acuerdo con Figma (margen de 31,3 % en lugar de ~36 %); (iii) adquisiciones: Semrush (US$1.560 M netos en 9M26; goodwill +US$1.180 M; deterioro de US$70 M); (iv) anomalías: el ROE y el ROIC contables se inflan porque las recompras (unos US$48.000 M desde 2019) reducen el patrimonio de US$16.518 M (2023) a US$11.764 M. Límites de homogeneidad: el flujo libre, el ROIC y el margen ajustado son definiciones de la hoja; la empresa define el margen no-GAAP sin compensación en acciones ni amortización. Último trimestre: 3T FY26 (cierre 28-ago-2026).

## 5. Crecimiento de ingresos: de la historia a la proyección

**Historia que tendría que ocurrir.** La Base supone que los ingresos pasan de US$25.970 M a US$38.359 M en el año 5 y a US$48.928 M en el año 10. El año 1 crece 10,79 % (US$28.772 M) y los años 2-5, 8,91 %, 7,70 %, 6,75 % y 6,47 %; luego 6,0 %, 5,5 %, 5,0 %, 4,5 % y 4,0 % hasta el terminal de 4 %. Por grupo (estimación con la mezcla de los nueve meses): Creative & Marketing Professionals +10 %, +8 %, +7 %, +6 %, +6 % y Business Professionals & Consumers +14 %, +12 %, +10 %, +9 %, +8 %; otros sin crecimiento. Contra la guía de FY26 (+12 % en ingresos; ARR +10,2 %) y el +13 % del 3T, un año 1 de 10,8 % es ligeramente prudente y supone que el efecto de Semrush y de los créditos de IA se diluye. Se verificó que `Input sheet` (B27 = 9,26 %) no gobierna la proyección: `Valuation output` toma el crecimiento de cada historia, y el CAGR compuesto 38.359 / 25.970 → 8,1 % coincide con el de la ficha.

**Porqué ese valor y no otro.** El 8,1 % se apoya en tres hechos: (1) el crecimiento reciente de 10-13 %; (2) 67 % del RPO (US$22.160 M) se reconoce en doce meses; (3) la mitad de las empresas de US$12.000-25.000 M (en dólares de 2015) logra ~4,5 % real compuesto en cinco años (34 % de ellas logra 8,1 %, según las tasas base de Mauboussin y Callahan): la Base ya está en el cuartil superior. Se rechaza la Optimista (11,0 %) porque exige que la IA agrande el mercado y se rechaza la Conservadora (5,4 %) como central porque el 3T muestra aceleración. Es [HIPÓTESIS] sostenida por [OBSERVADO] de crecimiento y guía.

**Qué haría cambiar el supuesto.** Crecimiento de ingresos ≤ 6 % en FY27 (la Conservadora pasa a central), o ARR «AI-first» sobre 5 % del ARR total y Creative & Marketing Professionals ≥ 8 % (más peso a la Base o a la Optimista).

**Cuánto mueve el valor.** ±2 puntos de crecimiento en los años 1-5 cambian la Base en −9,6 % / +10,6 % (US$360,90 / US$441,29). El DCF inverso muestra que el precio de US$239,94 equivale a un crecimiento de −2,0 % anual en los años 1-5 con el margen de la Base (−0,6 % con el de la Conservadora): el mercado descuenta una caída de ingresos que 87 % de las empresas de este tamaño evita. Límite: la mezcla por grupo es una estimación [HIPÓTESIS] y el crecimiento incluye Semrush sin separar lo orgánico (H-08).

## 6. Márgenes operativos y normalización de beneficios

**Historia que tendría que ocurrir.** La hoja trabaja con el margen operativo con el I+D capitalizado a 3 años y los arrendamientos como deuda: 38,84 % en el año base frente a 35,7 % reportado (+3,0 puntos por el I+D: EBIT +US$790 M = I+D de US$4.694 M menos la amortización del activo; +0,1 punto por arrendamientos). La Base converge a 40,6 % en cinco años (37,5 % reportado), la Conservadora a 37,1 % (34 %), la Disrupción a 31,1 % (28 %) y la Optimista a 43,1 % (40 %). Adobe guía un margen no-GAAP de ~45 % y un GAAP de ~34-36 % (EPS GAAP de US$18,12-18,17 con ~400 M de acciones): la Base supone una mejora reportada de 1,8 puntos por escala, compensada en parte por el cómputo de la IA. El margen de 2024 (31,3 %) incluye el cargo de US$1.000 M por Figma y no se toma como base.

**Porqué ese valor y no otro.** 37,5 % es la combinación de 36,6 % (2025) con una mejora moderada; 34 % (Conservadora) corresponde a descuentos y créditos de IA no cobrados; 28 % (Disrupción) a la pérdida de poder de precio; 40 % (Optimista) iguala la mitad de la brecha con el margen no-GAAP. La compensación en acciones (US$2.071 M) está dentro del EBIT GAAP: el modelo la trata como costo. [HIPÓTESIS] sostenida por [OBSERVADO] de márgenes 2021-2026.

**Qué haría cambiar el supuesto.** Margen GAAP ≤ 33 % (invalida la Base) o ≥ 37 % sostenido. ±2 puntos de margen objetivo mueven la Base ±4,8 % (US$379,94 / US$418,09).

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

**Historia que tendría que ocurrir.** La hoja usa un ventas/capital de 1,22 en los años 1-5 y 6-10 (cada dólar de ventas nuevas exige ~US$0,82 de capital con el I+D capitalizado). Referencias: hoy 1,19 (ventas LTM de US$25.970 M sobre capital invertido de US$21.760 M, que incluye un activo de I+D de US$8.871 M), marginal de tres años 3,4 y del último año 10,4 (Adobe crece sin capital adicional porque recompra más de lo que invierte), y sector 1,54. Con margen de 40,6 % e impuesto de 25 %, el capital nuevo rinde ~37 %, que es menos del doble del ROIC terminal de 29,3 % en la Base y la Optimista, pero **más del doble del costo de capital (9,0 %) en la Conservadora (34 %) y la Disrupción (28 %)**: el motor lo señala como aviso «revisar el ventas/capital» (H-06). [HIPÓTESIS].

**Porqué ese valor y no otro.** Usar el marginal (3,4 o 10,4) inflaría el valor porque ignora el capital que consumen la IA y las adquisiciones; el sector (1,54) es una referencia más holgada. Se elige 1,22, el nivel actual. El valor es poco sensible: ±20 % mueve la Base −1,8 % / +1,2 %.

**ROIC.** ROIC actual del modelo 36,4 % (NOPAT US$7.916 M / capital US$21.760 M); sin capitalizar I+D, 55,7 %; la industria (Damodaran, enero de 2026, ajustada por I+D y arrendamientos) 29,3 %. La Base y la Optimista usan 29,3 % después del año 10 (ventaja durable: la referencia sectorial, sin superar el ROIC actual); la Conservadora y la Disrupción, el costo de capital. Con ROIC terminal = costo de capital la Base valdría US$307,74 (−22,9 %).

**Asignación de capital.** Recompras de US$6.821 M en los nueve meses de 2026 (US$8.807 M un año antes); acciones de 413 M (nov-2025) a 391 M (ago-2026); sin dividendo; adquisiciones de US$1.560 M netos (Semrush); capex de US$214 M en el LTM. Las recompras superaron el flujo libre en 2024 (121 %) y 2025 (115 %), financiadas con caja y deuda [OBSERVADO]. El modelo no proyecta recompras: las acciones son fijas en 400,9 M (+5 % de acciones reduce la Base 4,8 %).

## 8. Costo del capital y riesgo

La hoja usa tasa libre de 5,29 % (FRED DGS10, 30-sep-2026), prima de riesgo ponderada por regiones de operación de 4,36 % (ingresos de los 9M26: Américas 58,7 % → Norteamérica; EMEA 27,3 %; APAC 14,0 % → Asia; prima madura de 3,70 %), beta bottom-up de Software (System & Application) de EE. UU. (1,25 desapalancada, 1,31 reapalancada con la D/E de mercado de ~6 %), costo del patrimonio de ~11,0 %, costo de la deuda de 5,80 % antes de impuestos (calificación A1/A+) y WACC inicial de 10,59 %, que converge a 8,99 % después del año 10. La tabla de EE. UU. se usa porque Adobe vende 53 % allí y 59 % en América. La regresión del ADBE (1,39 a cinco años; 0,97 a dos) es solo referencia [NO VERIFICADO].

**Porqué ese valor y no otro.** El riesgo de Adobe está en los flujos (precio y retención de Creative Cloud), que ya entran en cada historia; subir la tasa además duplicaría el riesgo. Los aproximaciones geográficas (Américas → Norteamérica, APAC → Asia) son [HIPÓTESIS] (H-10). Sensibilidad: +1 punto de tasa lleva la Base a US$331,14 (−17,0 %); −1 punto a US$500,90 (+25,5 %). Es la variable que más mueve el valor.

## 9. Convergencia y valor terminal

El crecimiento perpetuo es 4,00 % (política del corte, por debajo de la tasa libre de 5,29 %); el terminal explica 63,6 % del valor operativo de la Base (US$102.430 M de US$161.090 M), la mayor concentración entre las empresas revisadas. Durante los años 6-10 el crecimiento converge de 6,0 % a 4,0 % y el margen se mantiene en 40,6 %; el impuesto converge de 22,5 % a 25 % y el WACC de 10,59 % a 8,99 %. La Disrupción usa crecimiento terminal 0 %; las demás, 4 %.

**Qué haría cambiar el supuesto.** Un crecimiento perpetuo de 3,5 % reduce la Base −5,7 % y de 4,5 % la aumenta +7,0 %. El supuesto realmente material es el ROIC después del año 10: 29,3 % frente a 9,0 % mueve la Base −22,9 %, porque un negocio con retornos excedentes perpetuos vale más que su flujo del año 10.

## 10. Validación independiente del valor intrínseco

Se validó el DCF de tres maneras: (1) **reproducción:** el motor del Modelo JMR (`docs/jmr_engine.js`), alimentado con las entradas de la hoja, reproduce las cuatro historias con diferencia cero (Base US$399,02, Conservadora US$250,15, Disrupción US$167,70, Optimista US$487,73; DCF esperado US$385,65) — esto verifica la aritmética, no la validez económica; (2) **puente al patrimonio:** valor operativo US$161.090 M + caja US$5.639 M − deuda con arrendamientos US$6.764 M = US$159.966 M; ÷ 400,9 M de acciones = US$399,02 [MODELO]; (3) **coherencia con el mercado:** el EV de mercado (US$96.916 M) equivale a 9,7 veces el EBITDA y 10,5 veces el EBIT; el DCF Base implica un EV/EBIT de 17,4 veces (161.090 / 9.271). El DCF inverso (−2,0 % de crecimiento anual en los años 1-5 con el margen de la Base) indica que el precio descuenta un deterioro mayor que el de la Conservadora (+5,4 %).

## 11. Cuatro historias y probabilidades

| Historia | Probabilidad | CAGR años 1-5 | Margen objetivo (base de la hoja / reportado) | ROIC después del año 10 | DCF por acción |
|---|---:|---:|---:|---:|---:|
| Base · La IA se cobra dentro de la suscripción | 50 % | 8,1 % | 40,6 % / 37,5 % | 29,3 % | US$399,02 |
| Conservadora · Erosión gradual frente a Figma y Canva | 20 % | 5,4 % | 37,1 % / 34 % | 9,0 % (costo de capital) | US$250,15 |
| Optimista · La IA amplía el mercado de Adobe | 20 % | 11,0 % | 43,1 % / 40 % | 29,3 % | US$487,73 |
| Disrupción · La IA generativa comoditiza la creatividad | 10 % | 0,9 % | 31,1 % / 28 % | 9,0 % (costo de capital) | US$167,70 |

Las probabilidades salen de la previa de la etapa madura estable de Damodaran (50/20/20/10) sin ajustes por indicadores, no son frecuencias estadísticas y solo deben moverse cuando un indicador de la ficha cruce su umbral (H-02). El DCF esperado (Conservadora, Base y Optimista con pesos renormalizados) es US$385,65; la Disrupción se calcula aparte.

### ¿Qué pasaría si todo fallara?

La Disrupción (US$167,70) supone que la IA generativa comoditiza la creatividad: Creative & Marketing Professionals crece 5 % el primer año y cae 2-3 % después, el margen reportado baja a 28 % y no recupera. No supone quiebra: la deuda neta de ~0,07 veces el EBITDA y la cobertura de intereses de 36 veces dejan un riesgo de insolvencia muy bajo; el patrimonio sigue valiendo 30 % menos que el precio de hoy.

## 12. Valoración por múltiplos: prueba independiente y secundaria

Los siete métodos se calculan siempre; los pesos en el ponderado (EV/EBITDA 20 %, EV/FCFF 10 %, P/E 20 %, P/FCFE 5 %, P/OCF 5 %, P/V 0 %, P/BV 0 %) los fija `Resumen de Valoración` para una empresa madura y el DCF pesa 40 %. Los múltiplos de salida se fijan con la regla por ciclo: cada escenario usa la mediana de los cierres propios con el crecimiento que el escenario espera en FY+3 (Conservador 4,8 %, Base 7,7 %, Optimista 11,0 %), llevada al costo de capital del corte, con tope en el múltiplo justificado por fundamentales (ancla C).

| Método | Conservador | Base | Optimista | Ancla A (historia propia, mediana 5A) | Ancla B (pares, mediana) | Ancla C (justificado, Base) |
|---|---:|---:|---:|---:|---:|---:|
| EV/EBITDA | 9,1× | 9,4× | 12,7× | 26,0× | 17,3× | 11,8× |
| EV/FCFF | 8,6× | 8,9× | 24,1× | 24,9× | 16,0× | 20,2× |
| P/E | 13,7× | 14,1× | 18,2× | 37,8× | 21,0× | 15,8× |
| P/FCFE | 8,6× | 8,8× | 19,3× | 25,1× | 16,1× | 16,7× |
| P/OCF | 8,4× | 8,6× | 18,8× | 24,2× | 14,9× | 16,2× |
| P/V | 3,60× | 3,70× | 10,41× | — | — | — |
| P/BV | 7,27× | 7,27× | 13,09× | — | — | — |

Valores consolidados hoy: US$204,57 (Conservador), US$222,71 (Base) y US$359,24 (Optimista); ponderado con el DCF, US$222,80 / US$293,23 / US$410,64 (brecha de la Base de múltiplos con el DCF: −44 %). La brecha es la mayor de las empresas revisadas: el mercado cotiza hoy a Adobe a los múltiplos de una empresa de bajo crecimiento (9-14×) y la regla por ciclo le asigna esos mismos a la Base porque su crecimiento de FY+3 (7,7 %) es menor que el de cualquier cierre histórico salvo el LTM. La Optimista salta entre 29 % y 171 % sobre los múltiplos de hoy (todos con tope en el ancla C) y cada salto está justificado en `ADBE_ciclo.json`. Los pares provienen de yfinance al 30-sep-2026 (Autodesk, Intuit, Salesforce, ServiceNow, Workday, PTC) y solo comprueban. P/V y P/BV se calculan y no se ponderan; P/BV no es informativo porque el patrimonio es reducido por recompras. Los múltiplos son precio relativo, no valor intrínseco y comparten crecimiento, margen e impuestos con el DCF.

## 13. Sensibilidades económicas y escenarios alternativos

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp / +2 pp | US$379,94 / US$418,09 | −4,8 % / +4,8 % |
| Crecimiento años 1-5 −2 pp / +2 pp | US$360,90 / US$441,29 | −9,6 % / +10,6 % |
| Ventas/capital −20 % / +20 % | US$392,03 / US$403,67 | −1,8 % / +1,2 % |
| WACC +1 pp / −1 pp | US$331,14 / US$500,90 | −17,0 % / +25,5 % |
| Crecimiento terminal −0,5 pp / +0,5 pp | US$376,22 / US$426,84 | −5,7 % / +7,0 % |
| ROIC terminal = costo de capital | US$307,74 | −22,9 % |
| Acciones +5 % | US$380,02 | −4,8 % |

Escenarios alternativos relevantes: (a) *acciones*: si las 12,8 M de RSU en circulación (y no las 11,7 M esperadas a consolidar) y las PSU se contaran completas, la Base bajaría ~1 %; (b) *ROIC terminal intermedio*: con 20 % (entre el costo de capital y la referencia sectorial), la Base valdría aproximadamente US$350 (interpolación entre las dos sensibilidades; no se calculó en la hoja); (c) *compensación en acciones*: está dentro del EBIT GAAP; si el mercado la excluyera (margen no-GAAP de 45 %), el valor sería mayor, pero se considera un costo económico real.

## 14. Coherencia de hojas, cálculos y presentación

- **Formato unificado:** `unificacion_hojas.py` dio inicialmente una diferencia de dimensión en `Tesis de Inversión y Supuestos` (10 columnas frente a 8 de la maestra); se redimensionó y el informe final queda como UNIFICADA (61 pestañas, ninguna fórmula perdida ni editada).
- **Integridad:** `integridad_hojas.py` sin hallazgos; `estados_completos.py` sin hallazgos tras completar la variación neta de caja; `candados.py` 15/15; `inputs_completos.py` 0 entradas esenciales vacías.
- **Hoja = motor:** Base US$399,02, Conservadora US$250,15, Disrupción US$167,70 y Optimista US$487,73 coinciden entre `Escenarios e historias`, `Valuation output` y el motor de `damodaran_stories.py`.
- **Cambios de entradas durante la preparación:** `Input sheet` (D1, B4, B17/B18, B25, B32:B33, B35, B38:B42, B46, B49:B50, B62:B73, B76, B78, B83:B91, B98:C101), `Cost of capital worksheet` (regiones, calificación, ceros), `R& D converter!F7`, `Balance Sheet!L` (10-Q), `Income Statement!L8, L11, L27`, `Cash Flow Statement!C40:L40`, `Trailing Valuation!L2:L3` y `Entradas históricas auxiliares`. Todos con su script en `JMR-valuation/scripts/adbe_datos_cero.py`.
- **Presentación:** la sección 12 del artículo se generó con `damodaran_stories.py`; la matriz crecimiento × margen y las sensibilidades usan ahora el margen de la Base y la trayectoria explícita de la historia. La pestaña «Crecimiento implícito» que crea la publicación a la app se retira de la hoja después de publicar.

## 15. Hallazgos priorizados y propuestas de corrección

| Id | Prioridad | Hallazgo | Efecto | Propuesta |
|---|---|---|---|---|
| H-01 | Alta | El ROIC terminal de 29,3 % (referencia sectorial de Damodaran, no un ROIC observado de Adobe) pesa 22,9 % del valor y el terminal 63,6 % del valor operativo | ROIC terminal = costo de capital resta 22,9 % | Calcular con las razones de la industria cuando haya datos; documentar la persistencia de la ventaja |
| H-02 | Media | Probabilidades 50/20/20/10 de la previa de la etapa madura sin ajustes por indicadores | Cada 5 puntos entre Base y Conservadora mueven el esperado ~US$8 | Ajustar con evidencia fechada cuando un indicador cruce su umbral |
| H-03 | Media | Vida de I+D de 3 años es convención; el activo (US$8.871 M) y el ajuste de EBIT (+US$790 M) dependen de ella | +3,0 puntos de margen y +US$8.871 M de capital | Contrastar con la duración de los beneficios de los productos |
| H-04 | Media | Acciones: 400,9 M (portada + RSU esperadas); las PSU no se leyeron y las RSU en circulación son 12,8 M | ~1 % en el valor por acción | Incluir las PSU del 10-K |
| H-05 | Media | Ventas/capital de 1,22 es juicio entre referencias muy dispersas (1,19 hoy; 3,4 y 10,4 marginales; 1,54 sector) | ±20 % mueve la Base −1,8 % / +1,2 % | Revisar cuando se publique el 10-K de FY26 |
| H-06 | Media | En la Conservadora y la Disrupción el capital nuevo rinde 34 % y 28 %, más del doble del ROIC terminal de 9 % (aviso del motor) | Sobrevalora esas dos historias | Fijar ventas/capital menores por historia (p. ej. 0,9-1,0) |
| H-07 | Media | No se proyectan recompras ni dilución: las acciones son fijas | +5 % de acciones resta 4,8 % | Modelar recompras y SBC de forma consistente |
| H-08 | Media | La mezcla por grupo del LTM usa la de los nueve meses y el crecimiento incluye Semrush sin separar lo orgánico | Solo la trayectoria por grupo | Pedir el LTM por grupo y el orgánico a la empresa |
| H-09 | Media | Vencimiento medio de la deuda (4,2 años), calificación A1/A+ y peso de EE. UU. (53 %) heredados de la hoja anterior, no verificados | Costo de la deuda 5,80 % (6 % del capital) | Leer el 10-K |
| H-10 | Media | Regiones: Américas → Norteamérica y APAC → Asia son aproximaciones | ERP 4,36 %; ±0,2 puntos mueven la Base ~1 % | Desglosar por país con el 10-K |
| H-11 | Baja | `Forward Valuation` es retrospectivo (importador), `Sector` usa yfinance y el LTM de `Trailing Valuation` toma el precio del corte | Sin efecto en el DCF | Sustituir por estimaciones de consenso con fecha |
| H-12 | Baja | SG&A del LTM y «otros gastos operativos» se recalcularon a mano; variación neta de caja completada desde el balance | Presentación; el EBIT es el del 10-Q | Alinear con el 10-K |
| H-13 | Baja | Referencia de adopción de Figma (59 % frente a 42 %) de prensa financiera | Narrativa | Buscar fuente primaria |

## 16. Catalizadores, señales de refutación y seguimiento

| Variable | Señal favorable | Señal desfavorable | Ventana |
|---|---|---|---|
| Crecimiento de ingresos | ≥ +9 % en FY27 | ≤ +6 % | Resultados del 4T FY26 (dic-2026) y objetivos de FY27 |
| ARR «AI-first» | > 5 % del ARR total | Crece < 60 % antes de llegar a 5 % | Trimestral |
| Creative & Marketing Professionals | ≥ +8 % | ≤ +4 % | Trimestral |
| Margen operativo GAAP | ≥ 37 % | ≤ 33 % | Trimestral |
| Margen bruto | ≥ 88 % | < 87 % | Trimestral |
| Transición de liderazgo | Sin salidas adicionales; CFO permanente | Salida de ejecutivos clave | 1-dic-2026 en adelante |
| Adopción de Figma frente a Adobe | Brecha estable | Brecha creciente | Encuestas |

Posterior al corte: el 23-oct-2026 el ADBE cerraba en US$263,82 (+10 % sobre el 30-sep); no se incorporó en las cifras.

## 17. Dictamen económico y resumen para escuchar

**Dictamen: Plausible con reservas.** Los datos de partida están conciliados con el 10-Q y el comunicado del 3T, y la aritmética del DCF coincide con el motor y con la hoja. Las reservas son tres: (1) el ROIC terminal de 29,3 % y el terminal de 64 % del valor concentran el resultado (H-01); (2) las historias de erosión conservan un ventas/capital que rinde más del doble del ROIC terminal (H-06); (3) las probabilidades de la etapa madura no se ajustaron (H-02). Lo que tiene mejor soporte: ingresos, EBIT, caja, deuda y acciones (conciliados con el 10-Q) y la guía de FY26. Lo más frágil: el ROIC terminal y la duración de la ventaja frente a la IA.

**Resumen para escuchar.** Adobe vale US$399 por acción en la historia Base y US$386 como promedio ponderado de las historias, frente a un precio de US$240. La Base supone ingresos creciendo 8 % compuesto durante cinco años, un margen reportado que sube de 36 % a 37,5 % y un retorno de 29 % sobre el capital nuevo después del año 10; casi dos tercios del valor está en el terminal. El mercado cotiza a Adobe como si los ingresos cayeran 2 % al año. La variable que más mueve el valor es la tasa de descuento; la que más cambiaría la tesis es si la IA se cobra dentro de la suscripción o la sustituye.

## 18. Fuentes primarias, limitaciones y registro de versión

**Fuentes primarias:** [10-K FY2025](https://www.sec.gov/Archives/edgar/data/796343/000079634326000003/adbe-20251128.htm); [10-Q del 3T FY26](https://www.sec.gov/Archives/edgar/data/796343/000079634326000156/adbe-20260828.htm); [comunicado del 3T FY26](https://www.sec.gov/Archives/edgar/data/796343/000079634326000147/adbeex991q326.htm); [8-K del 2-sep-2026](https://www.sec.gov/Archives/edgar/data/796343/000079634326000144/adbe-20260902.htm); [8-K del 14-jul-2026](https://www.sec.gov/Archives/edgar/data/796343/000079634326000120/adbe-20260714.htm); [FRED DGS10](https://fred.stlouisfed.org/series/DGS10); Alpha Vantage (precios); Damodaran (betas, ROIC y prima de riesgo por sector y región, enero de 2026).

**Limitaciones.** No es una auditoría contable; no se leyó el 10-K completo ni la transcripción de la llamada; no se verificaron calificaciones, vencimientos de la deuda ni acciones de desempeño; la adopción de Figma proviene de prensa financiera; los precios y tasas son del corte del 30-sep-2026. Las etiquetas [OBSERVADO], [INFERENCIA], [HIPÓTESIS], [MODELO] y [NO VERIFICADO] distinguen la procedencia de cada afirmación.

**Registro de versión.** v1.3 del 26-oct-2026, hoja rehecha desde la maestra; reemplaza la edición del 19-oct-2026 (hoja anterior, ROIC terminal de 25 %, DCF Base de US$392,96 con precio de US$251,67). Archivos de respaldo: `reference/backups/unificar/…_ADBE_pre.json.gz`, `reference/damodaran/ADBE_ficha_previa_2026-10-26.json`, `reference/multiplos_v3/ADBE_anclas_previa_2026-10-19.json`.
