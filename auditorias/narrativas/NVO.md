**Estado de publicación (2026-10-27): PUBLICADO CON SALVEDADES · revisión NVO-REC-20261027-R1.** Estudio recuperado con corte del 30-sep-2026; sin cambios de supuestos, probabilidades ni pesos. Valoración, análisis fundamental y esta auditoría corresponden a la misma hoja de Google y a la misma revisión.

**Controles ejecutados el 27-oct-2026:** siete múltiplos con fórmula y resultado numérico (`verificar_multiplos_hoja.py`), fórmulas contra la maestra del 22-oct (`audit_master_formulas.py`), consistencia hoja = registro = análisis (`consistencia_migracion.py --hoja`), candados vigentes, probabilidades.

**Salvedades vigentes:**
- Estudio recuperado: precio y corte de información del 30-sep-2026; no incorpora resultados posteriores ni actualiza supuestos.
- Siete múltiplos calculados por las fórmulas originales de la hoja (7/7 con fórmula y resultado numérico; fórmulas de cálculo y múltiplos idénticas a la maestra del 22-oct-2026); P/V y P/BV con peso 0 y estado provisional.
- Candados de la plantilla del 21-oct (Financials Multiples!M34:M36) no aplican a la maestra vigente; se exigen solo los presentes en ella.

---

# Auditoría económica narrativa — Novo Nordisk A/S (NVO)

**Análisis fundamental vinculado:** [NVO en la app](https://juanmarobledo.github.io/Modelo-JMR/research.html?ticker=NVO) · registro `analisis/NVO-research-1790596929135-a90uu.json` (revisión del 26-oct-2026).

## 1. Ficha de auditoría y alcance

| Campo | Contenido |
|---|---|
| Emisor | Novo Nordisk A/S, sociedad danesa; acciones A (control) y B (cotizadas en Copenhague); ADR en la NYSE (1 ADR = 1 acción B); ticker NVO |
| Mercado, moneda y escala | NYSE (ADR); la empresa reporta en coronas danesas (DKK) con NIIF; la hoja convierte a US$ millones salvo por acción |
| Sector | Farmacéutica (hoja: industria de Damodaran «Drugs (Pharmaceutical)») |
| Método intrínseco principal | DCF FCFF de la historia Base (compañía operativa); MOS de 35 % sobre ese valor |
| Estados examinados | Form 20-F 2025 (4-feb-2026), 6-K de resultados 2025 (3-feb-2026) y 6-K del 1S2026 (4-ago-2026); LTM = julio de 2025 a junio de 2026, ajustado (sin la reversión de la 340B ni el deterioro del 2T26) |
| Fecha de valoración / de auditoría | Corte de mercado 30-sep-2026 / 26-oct-2026 |
| Precio del análisis | US$37,91 al cierre del 30-sep-2026 (Alpha Vantage, consultado el 26-oct-2026); no se obtuvo un precio de hoy distinto |
| Hoja auditada | [Modelo JMR NVO](https://docs.google.com/spreadsheets/d/1_w85o-Cv_4GzFB4nq5fGqrMSVoYf-Ltafuol3ir5TMw/edit), rehecha desde la maestra el 26-oct-2026 (61 pestañas, estado UNIFICADA) |
| Artículo y Nivel 2 | `JMR-valuation/data/NVO_Research_Fundamental_Modelo_JMR_2026-10-26.md` y `NVO_Nivel2_Datos_Modelo_JMR_2026-10-26.md` |
| Registro en la app | Se publica con la autorización general del usuario del 26-oct-2026; sin certificación previa (el usuario audita después) |
| Visto | Hoja completa por lectura; 20-F 2025 (páginas R 2021-2025 y companyfacts); 6-K del 1S2026 (texto completo); FRED (DEXDNUS); Alpha Vantage |
| Fuera de alcance | Transcripción de la llamada del 1S2026; informe anual (vencimientos de la deuda, concentración de clientes); estados de pares; calificación vigente de Moody's; vigilancia posterior al 26-oct-2026 |
| Estado de verificación | **Con reservas** (no es una auditoría contable). Ver §15 y §17 |

## 2. Resumen ejecutivo y relato económico central

Novo Nordisk vende terapias crónicas para diabetes y obesidad —sobre todo semaglutida (Ozempic, Wegovy, Rybelsus)— más insulinas y medicamentos para enfermedades raras, y cobra por receta a través de PBM, aseguradoras y gobiernos. En el LTM ajustado a junio de 2026 ingresó US$47.235 millones con un margen operativo de 40,4 % y un flujo operativo de US$20.954 millones; en 2025 ingresó US$46.731 millones (+11 % en dólares; +6,4 % en coronas) con margen de 41,3 % [OBSERVADO: 20-F 2025 y 6-K del 1S2026, conversión de la hoja].

Lo que cambia: el volumen de GLP-1 crece con fuerza (más de 265.000 recetas semanales de Wegovy en pastilla en julio de 2026; obesidad +19 % a tipo constante en el 1S26), pero el precio realizado cae más rápido (Wegovy inyectable −17 % en EE. UU., acuerdo MFN, autopago de US$149-299 al mes, recorte del precio de lista desde el 1-ene-2027) y Lilly tiene 61 % de las recetas de incretinas en EE. UU. El resultado: ventas ajustadas +2 % a tipo constante (−2 % en coronas) en el 1S26 y guía de 2026 de 0 % a −6 %, con margen bruto ajustado de 79,3 % frente a 83,1 % un año antes. La semaglutida perdió la exclusividad en Canadá, China, Brasil e India en 2026 y la perderá en Europa (marzo de 2031) y EE. UU. (diciembre de 2031 a octubre de 2032).

El motor de crecimiento de la Base es la suma de cuatro líneas calculadas con la mezcla del 1S26 (el LTM por línea no se publica): obesidad +16 % el primer año y desacelerando a +6 %, GLP-1 para diabetes −7 % a −1 %, insulinas −6 % a −3 % y enfermedades raras +2 % a +3 %, para un crecimiento compuesto de 1,9 % en cinco años, seguido de una caída de 3 %, 5 % y 2 % en los años 6-8 por los genéricos y una recuperación de 2-3 % en los años 9-10. La ventaja competitiva que sostendría los beneficios es la patente, la escala de fabricación de péptidos y los datos clínicos; el análisis la califica de «ventaja que se desvanece», con ROIC después del año 10 de 11,1 % en la Base.

**Tesis Base favorable:** el volumen compensa la caída de precios, el margen reportado baja de 40 % a 38 % y la nueva generación compensa parcialmente la caída de 2031-2033: US$45,43 por acción. **Interpretación neutral:** el precio sigue cayendo más de lo que crece el volumen: la Conservadora (US$31,61) describe esa ruta con probabilidad de 25 %. **Contratesis adversa:** Novo pierde relevancia frente a Lilly y los genéricos (Disrupción, US$20,17, probabilidad 20 %).

El supuesto que domina el valor es la tasa de descuento (±1 punto de WACC mueve la Base −14,8 % / +21,8 %), seguido del crecimiento de los años 1-5 (±2 puntos mueven la Base −5,8 % / +6,2 %) y el margen (±2 puntos, ±3,8 %). La contradicción que la empresa debe resolver es cómo convertir un volumen que crece 15-20 % en obesidad en ingresos cuando el precio neto cae dos dígitos. Esta narrativa no se deriva del precio: parte de los estados de 2019-2025, del LTM y del 6-K del 1S2026.

## 3. Trazabilidad, integridad y jerarquía de evidencia

Inventario de las celdas de entrada de `Input sheet`, `Cost of capital worksheet` y `Option value`, y de los datos que la hoja enlaza desde las pestañas de estados (Income Statement, Balance Sheet, Cash Flow Statement; columna L = LTM). `Financials Multiples` no tiene celdas de entrada propias: son fórmulas.

**Conteo:** la tabla tiene **87 filas** (todas las de `Input sheet` con valor, las entradas del costo de capital agrupadas por función y la de `Option value`); las celdas de rótulo no se cuentan. Las celdas con fórmula por defecto (`Input sheet!B27:B30`) se incluyen porque el analista puede sustituirlas.

**Cómo se cargaron los estados.** Emisor extranjero con NIIF: no hay 10-K/10-Q. La hoja se cargó con scripts propios (`scripts/nvo_datos_cero.py` y `scripts/run_nvo_cero.py`): (a) estados anuales 2019-2025 de las páginas R (XBRL) de los 20-F 2021-2025 y de companyfacts IFRS (para 2019-2020, donde faltan páginas R); (b) 1S2026 y 1S2025 de los 6-K, con los flujos de efectivo llevados a la presentación anterior (intereses pagados en operaciones); (c) LTM = 2025 + 1S26 − 1S25, ajustado: se resta la reversión de la provisión 340B (DKK 26.760 millones) y se suma el deterioro del 2T26 (DKK 6.328 millones) para llegar a las cifras ajustadas de la empresa; (d) conversión a dólares con FRED DEXDNUS: tipo medio anual para resultados y flujos, tipo de cierre (6,5458 DKK/US$ al 30-jun-2026) para el balance; (e) I+D 2016-2018 de los 6-K en DKK (14.563 / 14.014 / 14.805 millones) a los tipos medios de cada año (6,7276 / 6,5957 / 6,3131), único dato anterior a 2019; (f) precios del ADR de fin de año de Alpha Vantage, ajustados por la división 2:1 de septiembre de 2023 (÷2 hasta 2022). Los estados de 2016-2018 no están en formato estructurado y quedan en blanco.

**Diferencias de fuente y ajustes:** (a) el flujo de caja de la hoja parte de la utilidad neta reportada (LTM US$18.214 M, con la 340B), mientras el estado de resultados usa la ajustada (US$15.726 M); el flujo operativo ya está ajustado y es el que usa el modelo; (b) las acciones (4.425 M) son equivalentes de acciones B tras el desdoblamiento; (c) el balance del 30-jun-2026 se convierte al tipo de cierre y los saldos de años anteriores al de cierre de cada año; (d) la caja de la hoja (US$6.872 M) suma efectivo y valores negociables.

| # | Pestaña | Celda | Rótulo | Valor | Tipo | Documento/fuente | Quién lo aportó | Verificación |
|---:|---|---|---|---|---|---|---|---|
| 1 | Input sheet | B1 | Novo Nordisk A/S (NYSE:NVO) | Novo Nordisk A/S (NYSE:NVO) | Cálculo | Título de la hoja | Plantilla | Coincide |
| 2 | Input sheet | B4 | Date of valuation | sept-26 | Juicio | Corte de mercado 30-sep-2026 (fecha de valoración) | Corte común | [OBSERVADO] corte vigente de la cartera |
| 3 | Input sheet | B5 | Company name | Novo Nordisk A/S | Dato | 20-F 2025 (SEC, 4-feb-2026), portada | IA | Coincide [OBSERVADO] |
| 4 | Input sheet | B8 | Country of incorporation | Denmark | Dato | 20-F 2025 (SEC, 4-feb-2026), portada: Dinamarca | IA | Coincide [OBSERVADO] |
| 5 | Input sheet | B9 | Industry (US) | Drugs (Pharmaceutical) | Juicio | Damodaran, industrias de EE. UU., enero de 2026: «Drugs (Pharmaceutical)» | IA | Existe en Industry Averages(US); 51 % de las ventas en EE. UU. [INFERENCIA] |
| 6 | Input sheet | B10 | Industry (Global) | Drugs (Pharmaceutical) | Juicio | Damodaran, industrias globales, enero de 2026 | IA | Ídem |
| 7 | Input sheet | B12 | Revenues | $ 47.235,00 | Cálculo | 20-F 2025 (SEC, 4-feb-2026) + 6-K del 1S2026 (SEC, 4-ago-2026): LTM ajustado = 2025 + 1S26 − 1S25, en DKK convertido a US$ (medios FRED): US$47.235 M; excluye la reversión de la 340B (US$4.178 M) | Hoja (Income Statement!L3) | Recalculado [OBSERVADO]; el LTM ajustado de la empresa es DKK 148.551 M en el 1S26 |
| 8 | Input sheet | B13 | Operating income or EBIT | $ 19.066,80 | Cálculo | EBIT ajustado LTM: 19.067 (sin 340B ni deterioro del 2T26) | Hoja (Income Statement!L12) | Recalculado [OBSERVADO]; incluye ~DKK 8.000 M de reestructuración de 2025 (H-03) |
| 9 | Input sheet | B14 | Interest expense | $ 781,00 | Cálculo | Gasto por intereses LTM: US$781 M (20-F 2025 (SEC, 4-feb-2026), 6-K del 1S2026 (SEC, 4-ago-2026)) | Hoja (Income Statement!L15) | Recalculado [OBSERVADO] |
| 10 | Input sheet | B15 | Book value of equity | $ 33.804,40 | Dato | 6-K del 1S2026 (SEC, 4-ago-2026), balance al 30-jun-2026: patrimonio DKK 221.277 M a 6,5458 = US$33.804 M | Hoja (Balance Sheet!L35) | Coincide [OBSERVADO] |
| 11 | Input sheet | B16 | Book value of debt | $ 21.407,10 | Cálculo | 6-K del 1S2026 (SEC, 4-ago-2026): deuda corriente 2.801 + largo plazo 18.606 (incluye arrendamientos NIIF 16) a 6,5458 | Hoja (Balance Sheet!L20+L21+L25+L26) | Coincide con DKK 140.127 M [OBSERVADO] |
| 12 | Input sheet | B17 | Do you have R&D expenses to capitalize? | Yes | Juicio | Se capitaliza el I+D a 10 años (Damodaran, farmacéuticas) | IA | Convención del modelo [MODELO]; ver H-02 |
| 13 | Input sheet | B18 | Do you have operating lease commitments? | No | Juicio | NIIF 16: los arrendamientos ya están en la deuda; no se usa el conversor | IA | Procede [OBSERVADO] |
| 14 | Input sheet | B19 | Cash and Marketable Securities | $ 6.871,90 | Cálculo | 6-K del 1S2026 (SEC, 4-ago-2026): caja DKK 44.482 M + valores negociables 500 M = US$6.872 M | Hoja (Balance Sheet!L5) | Coincide [OBSERVADO] |
| 15 | Input sheet | B20 | Valor económico validado de participaciones y activos NO operativos (no duplicados) | $ 356,00 | Juicio | 6-K del 1S2026 (SEC, 4-ago-2026), apéndice 3: asociadas DKK 207 M + otros activos financieros DKK 2.123 M a 6,5458; valor contable | IA (B84) | [INFERENCIA]: sin valor de mercado |
| 16 | Input sheet | B21 | Minority interests | $ - | Dato | 20-F 2025 (SEC, 4-feb-2026): sin participaciones minoritarias | IA | No se hallan [OBSERVADO] |
| 17 | Input sheet | B22 | Number of shares outstanding = | 4425,00 | Dato | 6-K del 1S2026 (SEC, 4-ago-2026): 4.425 M de acciones en circulación (≈ A + B tras el desdoblamiento 2:1), equivalentes ADR | Hoja (Income Statement!L27) | Coincide con 4.420,75 M al 3-ago-2026 salvo recompras posteriores [OBSERVADO] |
| 18 | Input sheet | B23 | Current stock price = | $ 37,91 | Dato | Cierre del ADR del 30-sep-2026: US$37,91 (Alpha Vantage TIME_SERIES_MONTHLY, consultado el 26-oct-2026) | Corte común (D1) | Contrastado [OBSERVADO] |
| 19 | Input sheet | B24 | Effective tax rate = | 21,68% | Cálculo | Impuesto LTM / utilidad antes de impuestos | Hoja (Income Statement!L29) | 21,7 %; coherente con 21,5 % (2025) [OBSERVADO] |
| 20 | Input sheet | B25 | Marginal tax rate = | 22,00% | Juicio | Tasa estatutaria danesa 22 % | IA | 20-F 2025 (SEC, 4-feb-2026): 22 % [OBSERVADO] |
| 21 | Input sheet | B27 | Revenue growth rate for next year  | 1,08% | Cálculo | Predeterminado de la plantilla (crecimiento LTM sobre 2025: 1,08 %) | Plantilla | No gobierna la Base (la historia Base fija año 1 en 0,55 %) |
| 22 | Input sheet | B28 | Operating Margin for next year | 51,67% | Cálculo | Enlace a Valuation output!B6: margen base con I+D capitalizado (51,67 %) | Hoja | [MODELO]; reportado 40,4 % |
| 23 | Input sheet | B29 | Compounded annual revenue growth rate - years 2-5 = | 1,08% | Cálculo | Predeterminado de la plantilla (=B27) | Plantilla | No gobierna la Base |
| 24 | Input sheet | B30 | Referencia de margen objetivo (mediana histórica/sectorial; NO activa en historias) | 29,54% | Cálculo | Mediana de referencia (no activa) | Plantilla | Informativa |
| 25 | Input sheet | B31 | Year of convergence for margin | 5,00 | Juicio | Año de convergencia del margen: 5 | Plantilla/IA | Coherente con las historias |
| 26 | Input sheet | B32 | Sales to capital ratio  (for years 1-5) | 0,50 | Juicio | Ventas/capital 1-5 = 0,50: entre el marginal de 3 años (0,46) y el actual (0,60); marginal del último año 0,22; sector 1,11 | IA | [HIPÓTESIS]; ver H-05 |
| 27 | Input sheet | B33 | Sales to capital ratio (for years 6-10) | 0,50 | Juicio | Ventas/capital 6-10 = B32 | IA | Ídem |
| 28 | Input sheet | B35 | Riskfree rate | 5,29% | Dato | FRED DGS10, cierre del 30-sep-2026: 5,29 % (consultado el 26-oct-2026) | Corte común | Contrastado [OBSERVADO] |
| 29 | Input sheet | B36 | Initial cost of capital = | 9,34% | Cálculo | Enlace a Cost of capital worksheet!B14: 9,34 % | Hoja | [MODELO] |
| 30 | Input sheet | B38 | Do you have employee options outstanding? | No | Dato | 20-F 2025 (SEC, 4-feb-2026): Novo remunera con acciones restringidas y de desempeño, sin opciones sobre acciones relevantes | IA | [NO VERIFICADO] en detalle (inmaterial: compensación en acciones US$217 M) |
| 31 | Input sheet | B39 | Number of options outstanding = | 0,00 | Dato | 0 | IA | Inmaterial |
| 32 | Input sheet | B40 | Average strike price = | $0,00 | Dato | 0 | IA | Inmaterial |
| 33 | Input sheet | B41 | Average maturity = | 0,00 | Dato | 0 | IA | Inmaterial |
| 34 | Input sheet | B42 | Standard deviation on stock price = | 0,00% | Dato | 0 | IA | Inmaterial |
| 35 | Input sheet | B46 | Do you want to override this assumption = | No | Juicio | No se fija el WACC terminal a mano: tasa libre + prima madura de EE. UU. | IA | Correcto: 8,99 % |
| 36 | Input sheet | B47 | If yes, enter the cost of capital after year 10 = | 9,34% | Cálculo | Predeterminado (=B36), sin uso porque B46 = No | Plantilla | Sin efecto |
| 37 | Input sheet | B49 | Do you want to override this assumption = | Yes | Juicio | Se fija el ROIC terminal a mano | IA | Regla de ventaja que se desvanece |
| 38 | Input sheet | B50 | If yes, enter the return on capital you expect after year 10 | 11,10% | Juicio | ROIC terminal 11,1 %: punto medio entre el costo de capital terminal (8,99 %) y el ROIC de la industria llevado a la base del modelo (13,3 %) | IA | [HIPÓTESIS]; ver H-01 y H-06 |
| 39 | Input sheet | B52 | Do you want to override this assumption = | No | Juicio | Sin probabilidad de fracaso (flujo positivo, calificación Aa2/AA) | IA | [OBSERVADO] |
| 40 | Input sheet | B53 | If yes, enter the probability of failure = | 0% | Juicio | Probabilidad de fracaso 0 % | IA | Ídem |
| 41 | Input sheet | B54 | What do you want to tie your proceeds in failure to? | V | Juicio | Base de recuperación: valor razonable (V) | Plantilla | No se activa |
| 42 | Input sheet | B55 | Enter the distress proceeds as percentage of book or fair value | 50% | Juicio | Recuperación 50 % | Plantilla | No se activa |
| 43 | Input sheet | B57 | Do you want override this assumption = | No | Juicio | Rezago de reinversión: el predeterminado | Plantilla | Predeterminado |
| 44 | Input sheet | B58 | If yes, enter a different lag (0 = no lag to 3 = lag of 3 years) | 1 | Juicio | Rezago 1 año (no activo) | Plantilla | Predeterminado |
| 45 | Input sheet | B60 | Do you want to override this assumption = | No | Juicio | Sin ajuste de convergencia fiscal adicional (se usa la política normalizada B89) | IA | Coherente |
| 46 | Input sheet | B62 | Do you want to override this assumption = | No | Dato | 20-F 2025 (SEC, 4-feb-2026): sin pérdidas fiscales acumuladas relevantes | IA | No se hallan [OBSERVADO] |
| 47 | Input sheet | B65 | Do you want to override this assumption = | No | Juicio | No se usa tasa libre distinta después del año 10 | IA | Correcto (g ≤ tasa libre) |
| 48 | Input sheet | B66 | If yes, enter the riskfree rate after year 10 | 5,29% | Dato | Tasa libre después del año 10 (no activa): 5,29 % | Plantilla | Sin efecto |
| 49 | Input sheet | B68 | Do you want to override this assumption = | Yes | Juicio | Se fija el crecimiento perpetuo a mano | IA | Regla del corte: 4,0 % |
| 50 | Input sheet | B69 | If yes, enter the growth rate in perpetuity | 4,00% | Juicio | g terminal 4,00 %; techo = tasa libre (5,29 %) | IA/corte | ≤ 5,29 % [MODELO] |
| 51 | Input sheet | B71 | Do you want to override this assumption | No | Juicio | Sin efectivo atrapado adicional | IA | Novo no reporta efectivo atrapado material [NO VERIFICADO] |
| 52 | Input sheet | B72 | If yes, enter trapped cash (if taxes) or entire balance (if mistrust) | $0,00 | Juicio | Efectivo atrapado US$0 | IA | Ídem |
| 53 | Input sheet | B73 | & Average tax rate of the foreign markets where the cash is trapped | 0% | Juicio | Tasa adicional 0 % | IA | Ídem |
| 54 | Input sheet | B76 | Valor de acciones preferentes (misma unidad del DCF) | 0 | Dato | 20-F 2025 (SEC, 4-feb-2026): sin acciones preferentes | IA | Coincide [OBSERVADO] |
| 55 | Input sheet | B78 | PV del conversor ya incluido en deuda del balance (solapamiento) | 0 | Juicio | PV del conversor ya incluido en la deuda: 0 (B18 = No) | IA | Coherente |
| 56 | Input sheet | B79 | Pasivo de arrendamientos INCREMENTAL no reconocido | 0 | Cálculo | Pasivo de arrendamientos incremental: 0 | Plantilla | NIIF 16 |
| 57 | Input sheet | B80 | Ajuste de EBIT atribuible a pasivos incrementales | 0 | Cálculo | Ajuste de EBIT por pasivos incrementales: 0 | Plantilla | NIIF 16 |
| 58 | Input sheet | B81 | Estado de conciliación de arrendamientos | NO APLICA | Cálculo | NO APLICA | Plantilla | — |
| 59 | Input sheet | B82 | Inversiones a largo plazo según balance (dato histórico; NO valor razonable) | $356 | Cálculo | Inversiones a largo plazo según balance (Balance Sheet!L14) | Hoja | 356 [OBSERVADO] |
| 60 | Input sheet | B83 | Valor CONTABLE de inversiones excluidas del capital operativo | 356 | Juicio | Valor contable de inversiones excluidas del capital operativo: 356 | IA | Escrito el 26-oct-2026 para validar B85 |
| 61 | Input sheet | B84 | Valor ECONÓMICO atribuible de participaciones y activos no operativos | 356 | Juicio | 6-K del 1S2026 (SEC, 4-ago-2026), apéndice 3: (207 + 2.123) / 6,5458 = US$356 M, valor contable | IA | [INFERENCIA] sin valor de mercado |
| 62 | Input sheet | B85 | Control de inversiones y doble contabilización | VALIDADO | Cálculo | Control: VALIDADO | Plantilla | — |
| 63 | Input sheet | B86 | Revisión: no están incluidas en EBIT/FCFF ni duplicadas | Sin solapamiento | Juicio | Sin solapamiento con EBIT/FCFF | IA | [INFERENCIA] |
| 64 | Input sheet | B87 | Fuente y conciliación de inversiones no operativas | Informe financiero del 1S2026 (6-K del 4-ago-2026), apéndice 3: inversiones en asociadas (DKK 207 M) y otros activos financieros (DKK 2.123 M) a 30-jun-2026, a 6,5458 DKK/USD; sin valor de mercado, se toma el contable. No están en el EBIT. | Juicio | Texto de fuente de B84 | IA | — |
| 65 | Input sheet | B89 | Método fiscal de proyección (obligatorio en cada copia) | Normalizada | Juicio | Método fiscal: normalizada | IA | Política del modelo |
| 66 | Input sheet | B90 | Tasa inicial NORMALIZADA (solo si B89=Normalizada) | 0,218 | Juicio | Tasa inicial 21,8 %: efectiva 21,5 % (2025), 21,6 % (1S25), 21,9 % (1S26); guía 2026 de 21-23 % | IA | 20-F 2025 (SEC, 4-feb-2026); 6-K del 1S2026 (SEC, 4-ago-2026) [OBSERVADO] |
| 67 | Input sheet | B91 | Fuente / conciliación de impuesto efectivo vs marginal | Tasa efectiva: 21,5 % en 2025 (20-F), 21,6 % en 1S25 y 21,9 % en 1S26 (informe del 1S); tasa estatutaria danesa 22 %. Se usa 21,8 % al inicio y converge a la marginal de 22 %. | Juicio | Texto de conciliación fiscal | IA | — |
| 68 | Input sheet | B92 | Control de hipótesis fiscales | VALIDADO | Cálculo | Control fiscal: VALIDADO | Plantilla | — |
| 69 | Input sheet | B93 | Impuesto inicial para pronóstico (no altera la tasa histórica) | 0,218 | Cálculo | 21,8 % | Plantilla | — |
| 70 | Input sheet | B96 | Tasa libre de riesgo nominal de largo plazo · misma moneda del DCF | 5,29% | Cálculo | Tasa libre de largo plazo (=B35) | Plantilla | — |
| 71 | Input sheet | B97 | WACC terminal efectivo del modelo (independiente del DCF habilitado) | 8,99% | Cálculo | WACC terminal 8,99 % | Plantilla | — |
| 72 | Input sheet | B98 | Base | Sin liberación | Juicio | Sin liberación de capital en la Base (hay caída de ventas en los años 6-8) | IA | Texto de justificación en C98 |
| 73 | Input sheet | B99 | Conservadora | Sin liberación | Juicio | Sin liberación (Conservadora) | IA | Ídem |
| 74 | Input sheet | B100 | Disrupción | Sin liberación | Juicio | Sin liberación (Disrupción) | IA | Ídem |
| 75 | Input sheet | B101 | Optimista | Sin liberación | Juicio | Sin liberación (Optimista) | IA | Ídem |
| 76 | Cost of capital worksheet | B12 | Enfoque de costo de capital | Detailed | Juicio | Detallado: beta, prima y costo de la deuda explícitos | IA | Correcto |
| 77 | Cost of capital worksheet | B22 | Enfoque de beta | Single Business(US) | Juicio | Beta bottom-up de Drugs (Pharmaceutical), EE. UU. (Damodaran, ene-2026): 0,92 desapalancada, reapalancada por la D/E de mercado → 1,00 | IA | [MODELO]; regresión del ADR 1,12 (2 años) y 0,78 (5 años) solo de referencia [NO VERIFICADO] |
| 78 | Cost of capital worksheet | B26 | Enfoque de la prima de riesgo | Operating regions | Juicio | Prima ponderada por regiones de operación (ingresos ajustados del 1S26) con Damodaran, ene-2026 | IA | ERP 4,60 % [MODELO] |
| 79 | Cost of capital worksheet | H22:H32 | Ingresos por región (DKK M, 1S26) | EE. UU. 76.254; EUCAN 37.124; Asia-Pacífico + China 19.899; emergentes 15.274 repartidos en África, Centro/Sudamérica, Europa del Este y Medio Oriente | Dato | 6-K del 1S2026 (SEC, 4-ago-2026), cuadro «Adjusted sales split per geographical area» | IA | Coincide con el total 148.551 [OBSERVADO]; el reparto de emergentes en cuatro regiones es una convención [HIPÓTESIS] |
| 80 | Cost of capital worksheet | H6, H17 | Ingresos por país (US$ M) | EE. UU. 24.247; resto 22.988 | Cálculo | Ingresos LTM × peso del 1S26 | IA | [INFERENCIA] |
| 81 | Cost of capital worksheet | H37, H53 | Ingresos por industria | 47.235 (Drugs (Pharmaceutical)) | Cálculo | Igual a B12 | IA | Coincide |
| 82 | Cost of capital worksheet | B33 | Vencimiento medio de la deuda | 7 años | Juicio | Convención del modelo; el 20-F remite los vencimientos al informe anual | IA | [NO VERIFICADO] |
| 83 | Cost of capital worksheet | B34 y B36 | Costo de la deuda: calificación real | Aa2/AA → 5,84 % antes de impuestos | Dato | S&P AA (mayo de 2025, resumen del buscador); Moody's Aa2 no verificado en este informe | IA | [NO VERIFICADO] para Moody's |
| 84 | Cost of capital worksheet | B41:B44 | Deuda convertible | 0 | Dato | 20-F 2025 (SEC, 4-feb-2026): sin deuda convertible | IA | [OBSERVADO] |
| 85 | Cost of capital worksheet | B49:B51 | Acciones preferentes | 0 / 1 / 0 | Dato | 20-F 2025 (SEC, 4-feb-2026): sin preferentes | IA | [OBSERVADO] |
| 86 | Cost of capital worksheet | B13, B23, B27, B35 | Entradas directas (no activas) | 9,00 % / 1,20 / 6,00 % / 4,00 % | Plantilla | Predeterminados de la plantilla; los enfoques elegidos no las usan | Plantilla | Sin efecto |
| 87 | Option value | B9 | Rendimiento por dividendo | 0 | Plantilla | Sin opciones (Input!B38 = No) | Plantilla | Sin efecto |


## 4. Historia financiera: siete años y punto de partida

Reconstrucción con siete ejercicios (2019-2025) y LTM a partir de la hoja (Nivel 2). Ingresos de US$18.293 M (2019) a US$46.731 M (2025), CAGR de 17,2 %, con un quiebre: 6 % en 2020, 15 % en 2021, 12 % en 2022, 35 % en 2023, 25 % en 2024, 11 % en 2025 y 1,1 % del LTM sobre 2025.

| Métrica | Último (2025) | LTM | Promedio 3 años | Rango 2019-2025 |
|---|---:|---:|---:|---|
| Crecimiento de ingresos | 11,0 % | 1,1 % sobre 2025 | 23,6 % | 6,1 %-34,8 % |
| Margen operativo GAAP | 41,3 % | 40,4 % | 43,2 % | 41,3 %-44,2 % |
| Margen de flujo libre (operativo − capex) | 10,0 % | 16,9 % | 21,1 % | 10,0 %-36,2 % |
| ROIC sin I+D (EBIT × (1 − 22 %) / capital) | 32,1 % | 30,8 % | 51,8 % | 32,1 %-75,7 % |
| ROE | 50,8 % | 46,5 % | 67,0 % | 50,8 %-76,8 % |
| Acciones en circulación (M) | 4.444 | 4.425 | −0,3 % anual | 4.800 → 4.425 (−7,8 %) |
| Deuda neta / EBITDA | 0,72 | 0,62 | 0,40 | −0,04 a 0,72 |

Separación de efectos: (i) ciclo: la demanda de terapias crónicas es poco cíclica; el quiebre es de precio y competencia; (ii) contables: la 340B (reversión de DKK 26.760 M en el 1T26), los deterioros (ocedurenone DKK 5.700 M en 2024, DKK 6.328 M en el 2T26) y ~DKK 8.000 M de reestructuración en el 3T25; (iii) adquisiciones: Catalent (plantas de llenado, US$11.700 M, 2024) y Akero (US$4.700 M, 2025) explican el salto de la deuda y del capital; (iv) cambiario: el crecimiento en dólares (+11 % en 2025) difiere del de coronas (+6,4 %). Límites de homogeneidad: el margen bruto, el flujo libre y el ROIC son definiciones de la hoja; la empresa define el flujo libre sin intereses desde 2026. Último trimestre: 2T26 (cierre 30-jun-2026).

## 5. Crecimiento de ingresos: de la historia a la proyección

**Historia que tendría que ocurrir.** La Base supone que los ingresos pasan de US$47.235 M a US$52.023 M en el año 5 y caen a US$46.980 M en el año 8 antes de recuperarse a US$49.357 M en el año 10. El año 1 crece 0,55 % (US$47.494 M) y los años 2-5, 2,16 %, 2,72 %, 2,30 % y 2,03 %. Por línea (estimación con la mezcla del 1S26): obesidad +16 %, +14 %, +11 %, +8 %, +6 %; GLP-1 para diabetes −7 %, −5 %, −3 %, −2 %, −1 %; insulinas y otros −6 %, −4 %, −3 %, −3 %, −3 %; enfermedades raras +2 % a +3 %. Años 6-10 explícitos: −3 %, −5 %, −2 %, +2 %, +3 %. Contra la guía de 2026 (0 % a −6 % a tipo constante) y el +2 % del 1S26, un año 1 de +0,55 % exige que el segundo semestre y el primero de 2027 mejoren por el volumen de la pastilla antes del recorte de precio de 2027. Se verificó que `Input sheet` (B27 = 1,08 %) no gobierna la proyección: `Valuation output` toma el crecimiento de cada historia, y el CAGR compuesto 52.023 / 47.235 → 1,9 % coincide con el de la ficha.

**Porqué ese valor y no otro.** El 1,9 % se apoya en tres hechos: (1) el volumen del mercado de obesidad crece más de 80 %, pero el precio realizado de Novo cae (Wegovy inyectable −17 % en EE. UU.); (2) la guía de la empresa sitúa 2026 entre 0 % y −6 %; (3) la mitad de las empresas de más de US$25.000 M logra ~4,5 % nominal en cinco años (67 % de ellas alcanza 1,9 %, según las tasas base de Mauboussin y Callahan). Se rechaza la Optimista (5,2 %) porque exige que CagriSema, amicretina y la pastilla recuperen participación frente a una Lilly con 61 % de las recetas y mayor eficacia, y se rechaza la Conservadora (−1,7 %) como central porque el volumen internacional (obesidad +40 %) y Wegovy en pastilla muestran demanda. Es [HIPÓTESIS] sostenida por [OBSERVADO] de volumen y guía e [INFERENCIA] de precio.

**Qué haría cambiar el supuesto.** Ventas ajustadas a tipo constante negativas en 2027 (la Conservadora pasa a central); recetas de la pastilla por encima de 350.000 por semana y precio realizado cayendo menos de 10 % anual (más peso a la Base o a la Optimista); aprobación de CagriSema en el 4T26 con etiqueta competitiva.

**Cuánto mueve el valor.** ±2 puntos de crecimiento en los años 1-5 (conservando la trayectoria de los años 6-10) cambian la Base en −5,8 % / +6,2 %; la matriz crecimiento × margen del Nivel 2 va de US$36,47 (−2 %, 45,3 %) a US$55,74 (6 %, 53,3 %). El DCF inverso muestra que el precio de US$37,91 equivale a un crecimiento de −4,0 % anual en los años 1-5 con el margen de la Base (−2,3 % con el de la Conservadora): el mercado descuenta una trayectoria cercana a la Conservadora, que 85-90 % de las empresas de este tamaño supera. Límite: la mezcla por línea del LTM es una estimación [HIPÓTESIS] (H-07).

## 6. Márgenes operativos y normalización de beneficios

**Historia que tendría que ocurrir.** La hoja trabaja con el margen operativo con el I+D capitalizado a 10 años (Damodaran, farmacéuticas): 51,7 % en el año base frente a 40,4 % reportado (+11,3 puntos: EBIT +US$5.340 M = I+D de US$9.030 M menos la amortización del activo de US$30.701 M). La Base converge a 49,3 % en cinco años (38 % reportado), la Conservadora a 44,3 % (33 %), la Disrupción a 36,3 % (25 %) y la Optimista a 53,3 % (42 %). Hasta 2024 el margen reportado fue 41,7-44,2 %: la Base supone una compresión de 2 puntos por el recorte del precio de lista de 2027, el MFN y la competencia, parcialmente compensada por la escala. Los costos únicos (~DKK 8.000 M de reestructuración del 3T25, ≈2,6 puntos en 2025) siguen dentro del EBIT base del LTM porque la definición ajustada de la empresa no los excluye [OBSERVADO]: la normalización los dejaría fuera, pero el margen objetivo de cada historia se fija explícitamente y no depende del punto de partida (H-03).

**Porqué ese valor y no otro.** 38 % reportado es el punto medio entre el 40-41 % actual y un 36 % que invalidaría la Base; 33 % (Conservadora) corresponde a una caída de precios neta de ~15 % sin ahorro de costos; 25 % (Disrupción) es el margen de una farmacéutica diversificada sin franquicia dominante; 42 % (Optimista) mantiene el nivel actual con apalancamiento operativo de la pastilla. La I+D subió de 11,7 % a 16,8 % de las ventas, así que mantener el margen exige que el crecimiento de volumen absorba ese gasto. [HIPÓTESIS] sostenida por [OBSERVADO] de márgenes 2019-2025 y de la guía de 2026.

**Qué haría cambiar el supuesto.** Margen reportado ≤ 36 % (invalida la Base) o ≥ 40 % sostenido tras el recorte del WAC. ±2 puntos de margen objetivo mueven la Base ±3,8 % (US$43,69 / US$47,17).

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

**Historia que tendría que ocurrir.** La hoja usa un ventas/capital de 0,50 en los años 1-5 y 6-10 (cada dólar de ventas nuevas exige ~US$2,00 de capital con el I+D capitalizado). Referencias: hoy 0,60 (ventas LTM de US$47.235 M sobre capital invertido de US$78.684 M, que incluye el activo de I+D de US$30.701 M), marginal de tres años 0,46, marginal del último año 0,22 (el capex de capacidad se adelantó a las ventas) y sector 1,11. Con margen de 49,3 % e impuesto de 22 %, el capital nuevo rinde ~19 %, menos del doble del ROIC terminal (11,1 %), sin alerta de coherencia. Capex de DKK 60.140 M en 2025 y ~DKK 55.000 M previstos en 2026, con el compromiso de que baje. [HIPÓTESIS] (H-05).

**Porqué ese valor y no otro.** 0,60 sería el nivel actual pero haría que el capital nuevo rindiera ~23 % (más del doble del ROIC terminal); 0,46 y 0,22 son marginales volátiles por el calendario del capex; 1,11 del sector no aplica a péptidos inyectables con plantas propias. Se elige 0,50 como punto intermedio. El valor es poco sensible: ±20 % mueve la Base −1,4 % / +0,9 %.

**ROIC.** ROIC actual del modelo 24,3 % (NOPAT US$19.116 M / capital US$78.684 M); sin capitalizar I+D, 30,8 %; la industria (Damodaran, enero de 2026) 17,0 % en EE. UU. y 14,7 % global sin ajuste de I+D, que llevado a la base del modelo es 13,3 % (aproximación, H-01). La Base y la Optimista usan 11,1 % después del año 10 (punto medio entre el costo de capital terminal de 8,99 % y esa referencia); la Conservadora y la Disrupción, el costo de capital. Con ROIC terminal = costo de capital la Base valdría US$42,30 (−6,9 %).

**Asignación de capital.** Las recompras cayeron de DKK 29.924 M (2023) a DKK 1.388 M (2025) (programa 2026 de hasta DKK 15.000 M); los dividendos fueron DKK 35.300 M en el 1S26; las acciones bajaron 7,8 % desde 2019. Las recompras de 2021-2023 se hicieron a 34-39 veces la utilidad frente a 10,7 hoy [OBSERVADO]. El modelo no proyecta recompras: el número de acciones es fijo en 4.425 M (+5 % de acciones reduce la Base 4,8 %).

## 8. Costo del capital y riesgo

La hoja usa tasa libre de 5,29 % (FRED DGS10, 30-sep-2026), prima de riesgo ponderada por regiones de operación de 4,60 % (ingresos ajustados del 1S26: EE. UU. 76.254, Europa y Canadá 37.124, Asia-Pacífico y China 19.899, emergentes 15.274 en DKK M; prima madura del corte), beta bottom-up de Drugs (Pharmaceutical) de EE. UU. (0,92 desapalancada, 1,00 reapalancada con la D/E de mercado: capital 89,9 % / deuda 10,1 %), costo del patrimonio de 9,87 %, costo de la deuda de 5,84 % antes de impuestos (calificación Aa2/AA; tasa libre más diferencial) y WACC inicial de 9,34 %, que converge a 8,99 % después del año 10. La tabla de EE. UU. se usa porque 51 % de las ventas ajustadas se hacen allí; la tabla global daría una beta ligeramente mayor (1,09 en la edición anterior). La regresión del ADR contra el S&P 500 (1,12 a dos años; 0,78 a cinco) es solo referencia [NO VERIFICADO].

**Porqué ese valor y no otro.** El riesgo de Novo está en el precio de los GLP-1, que ya entra en los flujos de cada historia; subir la tasa además duplicaría el riesgo. La tasa libre de dólares es coherente con una hoja en dólares aunque los flujos de Novo se generen en parte en coronas, y la prima por regiones refleja que 49 % de las ventas están fuera de EE. UU. [MODELO]. Sensibilidad: +1 punto de tasa lleva la Base a US$38,72 (−14,8 %); −1 punto a US$55,33 (+21,8 %). Es la variable que más mueve el valor.

## 9. Convergencia y valor terminal

El crecimiento perpetuo es 4,00 % (política del corte, por debajo de la tasa libre de 5,29 %); el terminal explica 49 % del valor operativo de la Base (US$104.641 M de US$215.206 M). Antes del terminal, la Base atraviesa la caída de ventas de 2031-2034 (años 6-8) con reinversión truncada a cero («sin liberación de capital», C98), porque la caída proviene de genéricos y no de decisiones de desinversión: sin truncar, la reinversión negativa sumaría caja que la empresa no recuperaría. El margen se mantiene en 49,3 % desde el año 5 hasta el terminal, el impuesto converge de 21,8 % a 22,0 % y el WACC de 9,34 % a 8,99 %. La Disrupción usa crecimiento terminal 0 % (estabilización sin recuperación); las demás, 4 %.

**Qué haría cambiar el supuesto.** Un crecimiento perpetuo de 3,5 % reduce la Base −1,6 % y de 4,5 % la aumenta +1,9 %: el terminal pesa menos que en empresas de alto crecimiento porque el valor se concentra en los años 1-10. El supuesto realmente material es el ROIC después del año 10 (11,1 % frente a 8,99 %: −6,9 %).

## 10. Validación independiente del valor intrínseco

Se validó el DCF de tres maneras: (1) **reproducción:** el motor del Modelo JMR (`docs/jmr_engine.js`), alimentado con las entradas de la hoja, reproduce las cuatro historias con diferencia cero (Base US$45,43, Conservadora US$31,61, Disrupción US$20,17, Optimista US$57,57; DCF esperado US$43,39) — esto verifica la aritmética, no la validez económica; (2) **puente al patrimonio:** valor operativo US$215.206 M + caja US$6.872 M + activos no operativos US$356 M − deuda US$21.407 M = US$201.027 M; ÷ 4.425 M de acciones = US$45,43 [MODELO]; (3) **coherencia con el mercado:** el EV de mercado (US$182.287 M = capitalización de US$167.752 M + deuda − caja) equivale a 7,8 veces el EBITDA y 9,6 veces el EBIT ajustado, y el DCF Base implica un EV/EBIT de 11,3 veces. El DCF inverso (−4,0 % de crecimiento anual en los años 1-5 con el margen de la Base) indica que el precio descuenta un deterioro mayor que la Conservadora (−1,7 %). Valor de patrimonio: un 4,8 % de dilución adicional (+5 % de acciones) llevaría la Base a US$43,27.

## 11. Cuatro historias y probabilidades

| Historia | Probabilidad | CAGR años 1-5 | Margen objetivo (base de la hoja / reportado) | ROIC después del año 10 | DCF por acción |
|---|---:|---:|---:|---:|---:|
| Base · El volumen de obesidad compensa la caída de precios y el vencimiento de patentes | 40 % | 1,9 % | 49,3 % / 38 % | 11,1 % | US$45,43 |
| Conservadora · Guerra de precios con Lilly y genéricos de semaglutida | 25 % | −1,7 % | 44,3 % / 33 % | 9,0 % (costo de capital) | US$31,61 |
| Optimista · La nueva generación recupera el liderazgo | 15 % | 5,2 % | 53,3 % / 42 % | 11,1 % | US$57,57 |
| Disrupción · Deterioro de los fundamentales | 20 % | −5,8 % | 36,3 % / 25 % | 9,0 % (costo de capital) | US$20,17 |

Las probabilidades salen de la previa de la etapa de declive de Damodaran (40/25/15/20) sin ajustes por indicadores, no son frecuencias estadísticas y solo deben moverse cuando un indicador de la ficha cruce su umbral (H-06). El DCF esperado (Conservadora, Base y Optimista con pesos renormalizados) es US$43,39; la Disrupción se calcula aparte.

### ¿Qué pasaría si todo fallara?

La Disrupción (US$20,17) supone que Novo pierde relevancia frente a Lilly y los genéricos: la obesidad cae en vez de crecer, los GLP-1 para diabetes pierden 16 % el primer año, el margen cae a 25 % reportado y no recupera. No supone quiebra: la calificación Aa2/AA, la deuda neta de 0,6 veces el EBITDA y la cobertura de intereses de 24 veces dejan un riesgo de insolvencia muy bajo; el patrimonio sigue valiendo US$20 por acción, 47 % por debajo del precio.

## 12. Valoración por múltiplos: prueba independiente y secundaria

Los siete métodos se calculan siempre; los pesos en el ponderado (EV/EBITDA 20 %, EV/FCFF 10 %, P/E 20 %, P/FCFE 5 %, P/OCF 5 %, P/V 0 %, P/BV 0 %) los fija `Resumen de Valoración` para una empresa madura y el DCF pesa 40 %. Los múltiplos de salida se fijan con la regla por ciclo: cada escenario usa la mediana de los cierres propios con el crecimiento que el escenario espera en FY+3 (Conservador −0,9 %, Base 2,7 %, Optimista 6,3 %), llevada al costo de capital del corte, con tope en el múltiplo justificado por fundamentales (ancla C).

| Método | Conservador | Base | Optimista | Ancla A (historia propia, mediana 5A) | Ancla B (pares, mediana) | Ancla C (justificado, Base) |
|---|---:|---:|---:|---:|---:|---:|
| EV/EBITDA | 7,8× | 7,8× | 8,5× | 25,3× | 13,3× | 8,6× |
| EV/FCFF | 11,9× | 14,1× | 16,8× | 39,6× | 21,4× | 14,1× |
| P/E | 10,7× | 10,7× | 14,4× | 34,0× | 24,1× | 12,4× |
| P/FCFE | 11,0× | 12,9× | 15,1× | 38,5× | 20,2× | 12,9× |
| P/OCF | 7,0× | 8,0× | 9,3× | 27,3× | 16,3× | 8,2× |
| P/V | 3,55× | 3,55× | 5,08× | — | — | — |
| P/BV | 4,96× | 4,96× | 9,46× | — | — | — |

Valores consolidados hoy: US$37,92 (Conservador), US$43,83 (Base) y US$53,53 (Optimista); ponderado con el DCF, US$35,40 / US$44,47 / US$55,15. La brecha de la Base de múltiplos con el DCF Base es −3,5 %: el mercado cotiza hoy a Novo a los múltiplos de una empresa sin crecimiento y la Base supone justo eso para FY+3. Las anclas A (historia propia: 25-39×) y B (pares: Lilly con 54 % de margen y +48 % de crecimiento distorsiona la mediana) son solo comprobación. Los pares provienen de yfinance al 30-sep-2026 (Lilly, AstraZeneca, Novartis, Sanofi, Merck, Pfizer); Sanofi no devolvió flujo de caja. P/V y P/BV se calculan y no se ponderan. Los múltiplos son precio relativo, no valor intrínseco, y comparten crecimiento, margen e impuestos con el DCF; no se corrigen sesgos cambiarios de los cierres históricos más allá de usar el tipo medio de cada año (H-04). El tratamiento de la 340B y los deterioros hace que el P/E del LTM (10,7×) use utilidad ajustada: con la reportada (US$18.214 M) sería 9,2×.

## 13. Sensibilidades económicas y escenarios alternativos

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp / +2 pp | US$43,69 / US$47,17 | −3,8 % / +3,8 % |
| Crecimiento años 1-5 −2 pp / +2 pp | US$42,80 / US$48,22 | −5,8 % / +6,2 % |
| Ventas/capital −20 % / +20 % | US$44,80 / US$45,85 | −1,4 % / +0,9 % |
| WACC +1 pp / −1 pp | US$38,72 / US$55,33 | −14,8 % / +21,8 % |
| Crecimiento terminal −0,5 pp / +0,5 pp | US$44,73 / US$46,28 | −1,6 % / +1,9 % |
| ROIC terminal = costo de capital | US$42,30 | −6,9 % |
| Acciones +5 % | US$43,27 | −4,8 % |

Escenarios alternativos relevantes: (a) *sin caída de 2031-2034*: si los años 6-8 crecieran 0 % en vez de −3 %, −5 % y −2 %, la Base subiría varios dólares (no se calculó en la hoja; la matriz del Nivel 2 la cubre solo parcialmente) — es el supuesto con mayor incertidumbre fuera del descuento; (b) *precio de lista*: el recorte de enero de 2027 no está separado en la Base, que lo absorbe en el crecimiento de GLP-1 (−7 %) y el margen (−2 puntos); (c) *tipo de cambio*: una corona 10 % más fuerte reduciría en el mismo porcentaje las ventas en dólares en el corto plazo sin cambiar el valor en coronas; la hoja no modela el efecto.

## 14. Coherencia de hojas, cálculos y presentación

- **Formato unificado:** `unificacion_hojas.py` da estado UNIFICADA (61 pestañas, 21.258 fórmulas, 122 selectores, ninguna fórmula perdida ni editada). Para lograrlo hubo que redimensionar la pestaña `Tesis de Inversión y Supuestos` de 10 a 8 columnas (columnas sin datos).
- **Integridad:** `integridad_hojas.py` sin hallazgos; `estados_completos.py` sin hallazgos; `candados.py` 15/15; `inputs_completos.py` 0 entradas esenciales vacías.
- **Hoja = motor:** Base US$45,43, Conservadora US$31,61, Disrupción US$20,17 y Optimista US$57,57 coinciden entre `Escenarios e historias`, `Valuation output` y el motor de `damodaran_stories.py`.
- **Cambios de entradas durante la preparación:** `Input sheet!B32:B33` = 0,50 y `B50` = 11,1 % (juicio, documentado), `B83` = 356 y `B39:B42` = 0 (para validar los controles), `C98:C101` (texto de «sin liberación»), `Trailing Valuation!L2:L3` (encabezado LTM y precio), `Forward Valuation` (múltiplos retrospectivos calculados con los estados de la hoja), `Sector` (pares de yfinance; la fila de Novo se reemplazó por los datos de la hoja porque yfinance mezcla coronas y dólares) y `Income Statement!B10:D10` y `R& D converter!B19:B21` (I+D de 2016-2018). Todos con su script en `JMR-valuation/scripts/run_nvo_cero.py`.
- **Presentación:** la sección 12 del artículo se generó con `damodaran_stories.py` desde la hoja y el motor; se corrigió en el generador la matriz crecimiento × margen (se centraba en la mediana de referencia de 29,5 % y no en el margen de la Base) y las sensibilidades de crecimiento (no conservaban la trayectoria explícita de los años 6-10). La pestaña «Crecimiento implícito» que crea la publicación a la app se retira de la hoja después de publicar.

## 15. Hallazgos priorizados y propuestas de corrección

| Id | Prioridad | Hallazgo | Efecto | Propuesta |
|---|---|---|---|---|
| H-01 | Media | El ROIC de la industria llevado a la base del modelo (13,3 %) es una aproximación con la razón de márgenes (51,7/40,4) y de capital (0,612) de Novo, no de la industria; fija el ROIC terminal (11,1 %) | ROIC terminal = costo de capital resta 6,9 % | Calcular con las razones de la industria cuando Damodaran publique el ROIC con I+D capitalizado |
| H-02 | Media | El I+D de 2016-2018 viene de los 6-K en DKK convertido a los tipos medios; el activo de I+D (US$30.701 M) depende de una vida de 10 años que es convención | Ajuste de EBIT +US$5.340 M; margen +11,3 puntos | Contrastar la vida útil con la duración de los beneficios de los productos |
| H-03 | Media | El EBIT base incluye ~DKK 8.000 M de reestructuración del 3T25 (≈US$1.200 M, 2,6 puntos) | Margen del año 1 subestimado 2,6 puntos; el objetivo de cada historia no depende de él | Documentar o normalizar en la próxima actualización |
| H-04 | Media | La conversión DKK→US$ usa tipos medios anuales; el crecimiento en dólares no es el de coronas y los múltiplos históricos mezclan precio del ADR y estados convertidos | Crecimiento 2025 de +11 % en dólares frente a +6,4 % en coronas | Valorar en coronas y convertir al spot como contraste |
| H-05 | Media | Ventas/capital de 0,50 es juicio del analista entre referencias muy dispersas (0,22 a 1,11) | ±20 % mueve la Base −1,4 % / +0,9 % | Revisar cuando el capex de 2027 confirme la normalización |
| H-06 | Media | Probabilidades 40/25/20/15 de la etapa de declive sin ajustes por indicadores | Cada 5 puntos entre Base y Conservadora mueven el esperado ~US$0,9 | Ajustar con evidencia fechada cuando un indicador cruce su umbral |
| H-07 | Media | La mezcla por línea del LTM usa la del 1S26 | Solo cambia la trayectoria del crecimiento agregado | Reemplazar con el LTM por línea cuando se publique |
| H-08 | Media | Las fechas de vencimiento de patentes (2031-2032) y las cifras del Capital Markets Day se tomaron de la edición anterior del análisis y de reportes secundarios, no se releyeron en el 20-F en esta sesión | Calendario de los años 6-8 de la Base | Leer la sección de propiedad intelectual del 20-F |
| H-09 | Baja | `Forward Valuation` es retrospectivo (precio dividido por el resultado real del año siguiente), `Sector` usa yfinance para los pares y la columna EV/FCF queda vacía | Sin efecto en el DCF; el ancla B de pares es solo comprobación | Sustituir por estimaciones de consenso con fecha cuando haya fuente |
| H-10 | Baja | La calificación de Moody's (Aa2) y las betas de regresión (1,12 / 0,78) no se verificaron | Costo de la deuda 5,84 % y beta de referencia | Verificar en el informe anual y en Bloomberg/yfinance |
| H-11 | Baja | El estado de flujo de caja de la hoja parte de la utilidad neta reportada (LTM US$18.214 M) y el de resultados de la ajustada (US$15.726 M) | Presentación; el modelo usa el flujo operativo ajustado | Alinear la presentación |
| H-12 | Baja | Estados de 2016-2018 sin datos estructurados | Los múltiplos de ciclo usan 7 cierres, no 10 | Cargar de los 20-F antiguos si se requiere |

## 16. Catalizadores, señales de refutación y seguimiento

| Variable | Señal favorable | Señal desfavorable | Ventana |
|---|---|---|---|
| Ventas ajustadas a tipo constante | ≥ +3 % en 2027 | Negativas en 2027 | 9M26 (nov-2026) y guía 2027 (feb-2027) |
| Recetas semanales de Wegovy en pastilla | ≥ 350.000 | < 200.000 | Trimestral |
| Decisión de la FDA sobre CagriSema | Aprobación con etiqueta competitiva | Rechazo o retraso | 4T26 |
| Precio realizado de Wegovy/Ozempic en EE. UU. | Baja < 10 % anual | Baja > 15 % anual | 2027 |
| Margen operativo reportado | ≥ 40 % | ≤ 36 % | Trimestral |
| Capex y flujo libre | Capex 2027 claramente inferior | Sin bajar con ventas planas | Guía de febrero de 2027 |
| Litigios de patente (Cipla, Sandoz) | Patente válida hasta 2031-2032 | Revocación temprana | Sin fecha |

Posterior al corte: el 2-oct-2026 Novo informó una revisión extendida de la FDA para denecimig (lanzamiento previsto en el 1S27); no se incorporó en las cifras.

## 17. Dictamen económico y resumen para escuchar

**Dictamen: Plausible con reservas.** Los datos de partida están conciliados con fuentes primarias y la aritmética del DCF coincide con el motor y con la hoja. Las reservas son tres: (1) el ROIC terminal descansa en una aproximación de la industria (H-01); (2) el calendario de patentes de los años 6-8 no se releyó en el 20-F en esta sesión (H-08); (3) las probabilidades de la etapa de declive no se ajustaron con evidencia fechada (H-06). Lo que tiene mejor soporte: ingresos, EBIT, caja, deuda, acciones e impuestos (conciliados con el 20-F y el 6-K del 1S2026) y la guía de 2026. Lo más frágil: el crecimiento de los años 2-8 y el margen objetivo, que dependen del precio de los GLP-1 y del pipeline.

**Resumen para escuchar.** Novo Nordisk vale US$45,43 por acción en la historia Base y US$43,39 como promedio ponderado de las historias, frente a un precio de US$37,91. La Base supone ventas casi planas durante cinco años, un margen reportado que baja de 40 % a 38 %, una caída de ventas en 2031-2034 por los genéricos y un retorno de 11 % sobre el capital nuevo después del año 10. El mercado paga como si la historia Conservadora fuera la más probable. La variable que más mueve el valor es la tasa de descuento; la que más cambiaría la tesis es el precio neto por paciente en EE. UU. después del recorte de enero de 2027.

## 18. Fuentes primarias, limitaciones y registro de versión

**Fuentes primarias:** [Form 20-F 2025](https://www.sec.gov/Archives/edgar/data/353278/000035327826000012/nvo-20251231.htm); [6-K de resultados 2025](https://www.sec.gov/Archives/edgar/data/353278/000035327826000006/caq42025.htm); [6-K del 1S2026](https://www.sec.gov/Archives/edgar/data/0000353278/000035327826000023/caq22026.htm); [companyfacts IFRS](https://data.sec.gov/api/xbrl/companyfacts/CIK0000353278.json); [FRED DEXDNUS](https://fred.stlouisfed.org/series/DEXDNUS); [FRED DGS10](https://fred.stlouisfed.org/series/DGS10); Alpha Vantage (precios del ADR); [8-K de Lilly del 2T26](https://www.sec.gov/Archives/edgar/data/0000059478/000005947826000077/q226lillysalesandearningsp.htm); Damodaran (betas, ROIC y prima de riesgo por sector y región, enero de 2026).

**Limitaciones.** No es una auditoría contable; no se examinó el informe anual completo, la transcripción de la llamada ni los estados de los pares; no se verificó la calificación vigente de Moody's; las cifras de participación de mercado de Lilly provienen de un resumen del buscador; los precios y tasas son del corte del 30-sep-2026. Las etiquetas [OBSERVADO], [INFERENCIA], [HIPÓTESIS], [MODELO] y [NO VERIFICADO] distinguen la procedencia de cada afirmación.

**Registro de versión.** v1.3 del 26-oct-2026, hoja rehecha desde la maestra; reemplaza la auditoría del 26-oct-2026 del registro anterior (estado preliminar: sin altas, fuentes sin verificar). Archivos de respaldo: `reference/backups/unificar/…_NVO_pre.json.gz`, `reference/damodaran/NVO_ficha_previa_2026-10-26.json`, `reference/multiplos_v3/NVO_anclas_previa_2026-10-19.json`.
