# Auditoría económica narrativa — PayPal Holdings, Inc. (PYPL)

## 1. Ficha de auditoría y alcance

| Campo | Contenido |
|---|---|
| Emisor | PayPal Holdings, Inc., sociedad de Delaware (EE. UU.); acción ordinaria de clase única, valor nominal US$0,0001; ticker PYPL |
| Mercado, moneda y escala | Nasdaq Global Select Market; US$ millones salvo por acción |
| Sector | Pagos digitales (hoja: industria de Damodaran «Information Services») |
| Método intrínseco principal | DCF FCFF de la historia Base (compañía operativa); MOS de 35 % sobre ese valor |
| Estados examinados | 10-K 2025 (presentado el 3-feb-2026) y 10-Q del 2T26 (presentado el 28-jul-2026); LTM = julio de 2025 a junio de 2026 |
| Fecha de valoración / de auditoría | Corte de mercado 30-sep-2026 / 26-oct-2026 |
| Precio del análisis | US$52,53 al cierre del 30-sep-2026 (contrastado con FMP el 26-oct-2026); no se obtuvo un precio de hoy distinto |
| Hoja auditada | [Modelo JMR PYPL](https://docs.google.com/spreadsheets/d/1LI1LHXYFiCqg5i1_DDzs53Rd4eKv4zhDex2pxSvKuCs/edit), rehecha desde la maestra el 26-oct-2026 |
| Artículo y Nivel 2 | `JMR-valuation/data/PYPL_Research_Fundamental_Modelo_JMR_2026-10-26.md` y `PYPL_Nivel2_Datos_Modelo_JMR_2026-10-26.md` |
| Registro en la app | La versión del 15-oct-2026 (`valoraciones/PYPL-1790205796042.json`, precio 57,16) sigue vigente en la app; **la hoja nueva no está publicada** (requiere autorización expresa) |
| Visto | Hoja completa (61 pestañas) por lectura; 10-K y 10-Q; comunicado del 2T26; 8-K del 3-feb, 30-abr y 15-may-2026; FRED; FMP |
| Fuera de alcance | Transcripción de la llamada del 2T26; declaración de poderes (proxy); estados de pares; calificaciones crediticias; vigilancia posterior al 26-oct-2026 |
| Estado de verificación | **Con reservas** (no es una auditoría contable). Ver §15 y §17 |

## 2. Resumen ejecutivo y relato económico central

PayPal cobra una comisión por cada pago que pasa por una red de dos lados de 439 millones de cuentas (consumidores y comercios en unos 200 mercados), y gana además intereses y comisiones por crédito, reparto de ingresos con un banco socio e intereses sobre saldos de clientes. En 2025 el volumen de pagos fue US$1,79 billones (+7 %), los ingresos US$33.172 millones (+4,3 %) y el margen operativo GAAP 18,3 %. En los doce meses a junio de 2026 los ingresos fueron US$34.128 millones y el margen 17,4 % [OBSERVADO: 10-K 2025 y 10-Q del 2T26].

Lo que cambia: el volumen sigue creciendo (+10 % en el 2T26) pero los ingresos acompañan menos (+5 %; +3 % sin divisas) y el gasto de transacción crece más (+11 %), de modo que el margen operativo del trimestre bajó de 18,1 % a 16,4 %. La explicación de la empresa es mezcla (más procesamiento de Braintree, de menor margen), mezcla de fondeo (más tarjeta), campañas de comarketing con grandes comercios y menores comisiones de divisas. La dirección cambió (Enrique Lores, CEO desde el 1-mar-2026), anunció una reorganización con ahorros brutos de al menos US$1.500 millones anualizados en dos o tres años y dice que el checkout de marca «se ha estabilizado más».

El motor de crecimiento que usa la Base es la suma de cuatro líneas que PayPal no publica (checkout de marca, Braintree, Venmo y otros servicios): 3-4 %, 3-4 %, 10-15 % y 5 %, para un crecimiento compuesto de 4,9 % en cinco años. La ventaja competitiva que sostendría los beneficios es una red de dos lados con marca de veinte años, licencias en unos 200 mercados e identidad verificada; el análisis la califica de «ventaja que se desvanece» porque en el pago en línea compite con billeteras integradas en el teléfono y la plataforma.

**Tesis Base favorable:** el ahorro llega al margen, el checkout se estabiliza y Venmo y el crédito compensan: ingresos +4,9 % y margen 19,2 % valen US$105,13 por acción. **Interpretación neutral:** el volumen crece pero la mezcla absorbe el ahorro: la Conservadora (US$67,06) describe esa ruta con probabilidad de 20 %. **Contratesis adversa:** PayPal se vuelve un procesador de bajo margen (Disrupción, US$47,98, probabilidad 10 %).

El supuesto que domina el valor es el margen operativo objetivo y su combinación con el crecimiento: ±2 puntos de margen mueven la Base ±9,7 % y ±2 puntos de crecimiento ±9,4-10,4 %. La contradicción que la empresa debe resolver es por qué el gasto de transacción crece (+11 %) más que el volumen (+10 %) y los ingresos (+5 %). Esta narrativa no se deriva del precio: parte de los estados y del 10-Q.

## 3. Trazabilidad, integridad y jerarquía de evidencia

Inventario de las celdas de entrada de `Input sheet`, `Cost of capital worksheet` y `Option value`, y de los datos que la hoja enlaza desde las pestañas de estados (Income Statement, Balance Sheet, Cash Flow Statement; columna L = LTM). `Financials Multiples` no tiene celdas de entrada propias: son fórmulas, y 36 valores sobrantes de un uso anterior (`N8:Q10`, `N18:Q20`, `N28:Q30`, sin referencias desde ninguna fórmula) se retiraron durante la preparación, antes de esta auditoría, con respaldo en `JMR-valuation/reference/backups/PYPL_residuos_financials_multiples_2026-10-26.json`.

**Conteo:** la tabla tiene **117 filas** (73 de `Input sheet`, 36 de `Cost of capital worksheet`, incluidas 7 de la calculadora de ERP, y 8 de `Option value`); las celdas de rótulo de la plantilla no se cuentan. Las celdas con fórmula por defecto (`Input sheet!B27:B33` y `B47`) se incluyen porque el analista puede sustituirlas. Los datos crudos de los estados (diez años de la SEC y yfinance/FMP del importador) se contrastaron para las columnas anual de 2025 y LTM con el 10-K y el 10-Q; los demás años provienen del importador y no se contrastaron uno a uno ([NO VERIFICADO] salvo ingresos, EBIT y utilidad neta de 2023-2025, que coinciden con el 10-K).

**Diferencias de fuente y ajustes:** (a) LTM = FY2025 + 6M2026 − 6M2025 para ingresos, EBIT, intereses, D&A (963), compensación en acciones (1.001) y capex (889), todos recalculados; (b) acciones de la portada del 22-jul-2026 (855,46 M) frente a 862 M al 30-jun-2026 del balance; (c) arrendamientos financieros de US$10 M sin actualizar a junio (inmaterial); (d) la caja de la hoja (US$11.256 M) excluye inversiones a largo plazo y fondos de clientes, y la empresa informa US$15.300 M con otra definición.

| # | Pestaña | Celda | Rótulo | Valor | Tipo | Documento/fuente (URL en §18) | Quién lo aportó | Verificación |
|---:|---|---|---|---|---|---|---|---|
| 1 | Input sheet | B5 | Company name | PayPal Holdings, Inc. | Dato | 10-K 2025 (SEC, 3-feb-2026), portada | Importador/IA | Coincide [OBSERVADO] |
| 2 | Input sheet | B8 | Country of incorporation | United States | Dato | 10-K 2025 (SEC, 3-feb-2026), portada: Delaware (EE. UU.) | IA | Coincide [OBSERVADO] |
| 3 | Input sheet | B9 | Industry (US) | Information Services | Juicio | Damodaran, industrias de EE. UU., enero de 2026 («Information Services») | IA (elección de industria) | Existe en Industry Averages(US); elección discutible, ver H-07 [INFERENCIA] |
| 4 | Input sheet | B10 | Industry (Global) | Information Services | Juicio | Damodaran, industrias globales, enero de 2026 | IA | Ídem |
| 5 | Input sheet | B12 | Revenues | $ 34.128,00 | Cálculo | 10-K 2025 (SEC, 3-feb-2026) + 10-Q 2T26 (SEC, 28-jul-2026): 33.172 + 17.035 − 16.079 = 34.128 | Hoja (enlace a Income Statement!L3) | Recalculado: 34.128 [OBSERVADO] |
| 6 | Input sheet | B13 | Operating income or EBIT | $ 5.946,00 | Cálculo | 6.065 + 2.915 − 3.034 = 5.946 | Hoja (Income Statement!L12) | Recalculado [OBSERVADO] |
| 7 | Input sheet | B14 | Interest expense | $ 461,00 | Cálculo | 441 + 237 − 217 = 461 (gasto por intereses) | Hoja (Income Statement!L15) | Recalculado [OBSERVADO] |
| 8 | Input sheet | B15 | Book value of equity | $ 19.820,00 | Dato | 10-Q 2T26 (SEC, 28-jul-2026), balance: patrimonio total 19.820 | Hoja (Balance Sheet!L35) | Coincide [OBSERVADO] |
| 9 | Input sheet | B16 | Book value of debt | $ 13.410,00 | Cálculo | 10-Q 2T26 (SEC, 28-jul-2026): deuda corriente 2.505 + largo plazo 10.895 + arrendamientos financieros 10 (cifra de dic-2025 sin actualizar) | Hoja (Balance Sheet!L20+L21+L25+L26) | Coincide salvo 10 de arrendamientos (<0,1 %) [OBSERVADO] |
| 10 | Input sheet | B17 | Do you have R&D expenses to capitalize? | No | Juicio | No se capitaliza I+D (tecnología y desarrollo se trata como gasto operativo) | IA | Decisión previa distinta; ver H-03 |
| 11 | Input sheet | B18 | Do you have operating lease commitments? | Yes | Juicio | 10-K 2025 (SEC, 3-feb-2026), nota 6 (arrendamientos operativos) | IA | Procede: hay arrendamientos operativos por US$696 M en balance |
| 12 | Input sheet | B19 | Cash and Marketable Securities | $ 11.256,00 | Cálculo | 10-Q 2T26 (SEC, 28-jul-2026): efectivo 8.306 + inversiones a corto plazo 2.950 | Hoja (Balance Sheet!L5) | Coincide [OBSERVADO]; excluye fondos de clientes |
| 13 | Input sheet | B20 | Valor económico validado de participaciones y activos NO operativos (n | $ 3.601,75 | Juicio | 10-Q 2T26 (SEC, 28-jul-2026), inversiones a largo plazo (R59): valor económico = 2.269 + 5 + 106 + 1.629 × (1 − 25 %) | IA (fórmula manual en B84) | Componentes del 10-Q; el descuento fiscal del 25 % es supuesto [INFERENCIA] |
| 14 | Input sheet | B21 | Minority interests | $ - | Dato | 10-Q 2T26 (SEC, 28-jul-2026): sin participaciones minoritarias | IA | No se hallan en el 10-Q [OBSERVADO] |
| 15 | Input sheet | B22 | Number of shares outstanding = | 855,50 | Dato | Portada del 10-Q: 855.460.874 acciones al 22-jul-2026 (clase única) | Hoja (Income Statement!L27) | Coincide; posterior al 22-jul hubo recompras, ver H-04 |
| 16 | Input sheet | B23 | Current stock price = | $ 52,53 | Dato | Precio de cierre del 30-sep-2026: US$52,53 (FMP, consultado el 26-oct-2026) | Corte común de la cartera (D1) | Contrastado con FMP [OBSERVADO] |
| 17 | Input sheet | B24 | Effective tax rate = | 16,39% | Cálculo | Impuesto LTM / utilidad antes de impuestos | Hoja (Income Statement!L29) | Coherente con 10-K y 10-Q [OBSERVADO] |
| 18 | Input sheet | B25 | Marginal tax rate = | 25,00% | Juicio | Tasa marginal federal más estatal de EE. UU. (25 %) | Plantilla/IA | Convención del modelo [MODELO] |
| 19 | Input sheet | B27 | Revenue growth rate for next year  | 2,88% | Cálculo | Predeterminado de la plantilla: crecimiento del último año; la historia Base lo sustituye en `Valuation output` | Plantilla | No gobierna la Base (4,47 % año 1); ver H-05 |
| 20 | Input sheet | B28 | Operating Margin for next year | 17,58% | Cálculo | Enlace a `Valuation output!B6` | Hoja | Coincide con el margen base 17,58 % [MODELO] |
| 21 | Input sheet | B29 | Compounded annual revenue growth rate - years 2-5 = | 2,88% | Cálculo | Predeterminado de la plantilla (igual a B27) | Plantilla | No gobierna la Base |
| 22 | Input sheet | B30 | Referencia de margen objetivo (mediana histórica/sectorial; NO activa  | 17,58% | Cálculo | Referencia de margen (mediana); NO activa | Plantilla | Informativa |
| 23 | Input sheet | B31 | Year of convergence for margin | 5,00 | Juicio | Año de convergencia del margen: 5 | Plantilla/IA | Coherente con las historias |
| 24 | Input sheet | B32 | Sales to capital ratio  (for years 1-5) | 2,71 | Juicio | Ventas/capital 1-5 = 2,71 (K28 de `Valuation output`); marginal 3 años 7,68; sector 2,51 | IA | Ver §7 y H-06 [HIPÓTESIS] |
| 25 | Input sheet | B33 | Sales to capital ratio (for years 6-10) | 2,71 | Juicio | Ventas/capital 6-10 = B32 | Plantilla/IA | Ídem |
| 26 | Input sheet | B35 | Riskfree rate | 5,29% | Dato | FRED DGS10, cierre del 30-sep-2026: 5,29 % (consultado el 26-oct-2026) | Corte común | Contrastado con FRED [OBSERVADO] |
| 27 | Input sheet | B36 | Initial cost of capital = | 8,38% | Cálculo | Enlace a `Cost of capital worksheet!B14` | Hoja | Igual a CoC!B14 y CoC!E63 [MODELO] |
| 28 | Input sheet | B38 | Do you have employee options outstanding? | Yes | Dato | 10-K 2025 (SEC, 3-feb-2026), nota de compensación en acciones (opciones en circulación) | Importador/IA | Existencia confirmada; cifras no trazadas, ver H-02 |
| 29 | Input sheet | B39 | Number of options outstanding = | 0,02 | Dato | Opciones en circulación: 0,017676 millones | Importador/IA | [NO VERIFICADO] contra el 10-K (inmaterial) |
| 30 | Input sheet | B40 | Average strike price = | $20,82 | Dato | Precio de ejercicio promedio: US$20,82 | Importador/IA | [NO VERIFICADO] (inmaterial) |
| 31 | Input sheet | B41 | Average maturity = | 3,00 | Juicio | Vencimiento promedio: 3 años | IA | [HIPÓTESIS] (inmaterial) |
| 32 | Input sheet | B42 | Standard deviation on stock price = | 45,00% | Juicio | Desviación estándar del precio: 45 % | IA | [HIPÓTESIS] (inmaterial) |
| 33 | Input sheet | B46 | Do you want to override this assumption = | No | Juicio | No se fija el WACC terminal por la vía manual: se usa tasa libre + prima país de EE. UU. | IA | Correcto: 8,99 % terminal |
| 34 | Input sheet | B47 | If yes, enter the cost of capital after year 10 = | 8,38% | Cálculo | Predeterminado de la plantilla (=B36), no se usa porque B46 = No | Plantilla | Sin efecto |
| 35 | Input sheet | B49 | Do you want to override this assumption = | Yes | Juicio | Se fija el ROIC terminal manualmente | IA | Regla de ventaja que se desvanece |
| 36 | Input sheet | B50 | If yes, enter the return on capital you expect after year 10 | 15,00% | Juicio | ROIC terminal 15,0 %: punto medio entre costo de capital terminal (8,99 %) y ROIC actual (20,9 %) | IA | Coherente con REGLAS §6 [MODELO] |
| 37 | Input sheet | B52 | Do you want to override this assumption = | No | Juicio | Sin probabilidad de fracaso | IA | Empresa con flujo positivo y deuda con calificación A2/A según la hoja |
| 38 | Input sheet | B53 | If yes, enter the probability of failure = | 0% | Juicio | Probabilidad de fracaso 0 % | IA | Ídem |
| 39 | Input sheet | B54 | What do you want to tie your proceeds in failure to? | V | Juicio | Base de recuperación: valor razonable (V) | Plantilla | No se activa |
| 40 | Input sheet | B55 | Enter the distress proceeds as percentage of book or fair value | 50% | Juicio | Recuperación 50 % | Plantilla | No se activa |
| 41 | Input sheet | B57 | Do you want override this assumption = | No | Juicio | Sin rezago de reinversión distinto del predeterminado | Plantilla | Predeterminado |
| 42 | Input sheet | B58 | If yes, enter a different lag (0 = no lag to 3 = lag of 3 years) | 1 | Juicio | Rezago 1 año (no activo) | Plantilla | Predeterminado |
| 43 | Input sheet | B60 | Do you want to override this assumption = | No | Juicio | Sin ajuste de convergencia fiscal adicional | Plantilla | Predeterminado |
| 44 | Input sheet | B62 | Do you want to override this assumption = | No | Dato | 10-K 2025 (SEC, 3-feb-2026): sin pérdidas fiscales acumuladas relevantes | IA | No se hallan [OBSERVADO] |
| 45 | Input sheet | B65 | Do you want to override this assumption = | No | Juicio | No se usa tasa libre distinta después del año 10 | IA | Correcto (g ≤ tasa libre) |
| 46 | Input sheet | B66 | If yes, enter the riskfree rate after year 10 | 5,29% | Dato | Tasa libre después del año 10 (no activa): 5,29 % | Plantilla | Sin efecto |
| 47 | Input sheet | B68 | Do you want to override this assumption = | Yes | Juicio | Se fija el crecimiento perpetuo manualmente | IA | Regla del corte: 4,0 % |
| 48 | Input sheet | B69 | If yes, enter the growth rate in perpetuity | 4,00% | Juicio | g terminal 4,00 %: inflación esperada ~2,3 % + crecimiento real ~1,7 %; techo = tasa libre (corte vigente) | IA/corte | ≤ 5,29 % [MODELO] |
| 49 | Input sheet | B71 | Do you want to override this assumption | No | Juicio | Sin efectivo atrapado adicional | IA | 58 % del efectivo está en filiales extranjeras pero sujeto a impuesto de EE. UU. (Subpart F, 10-K) |
| 50 | Input sheet | B72 | If yes, enter trapped cash (if taxes) or entire balance (if mistrust) | $0,00 | Juicio | Efectivo atrapado US$0 | IA | Ídem |
| 51 | Input sheet | B73 | & Average tax rate of the foreign markets where the cash is trapped | 0% | Juicio | Tasa adicional 0 % | IA | Ídem |
| 52 | Input sheet | B76 | Valor de acciones preferentes (misma unidad del DCF) | 0 | Dato | 10-Q 2T26 (SEC, 28-jul-2026): sin acciones preferentes emitidas (100 M autorizadas, ninguna emitida) | IA | Coincide [OBSERVADO] |
| 53 | Input sheet | B78 | PV del conversor ya incluido en deuda del balance (solapamiento) | 0 | Juicio | PV del conversor ya incluido en la deuda: 0 (la deuda B16 no incluye arrendamientos operativos) | IA | Coherente: B16 solo suma deuda financiera [OBSERVADO] |
| 54 | Input sheet | B79 | Pasivo de arrendamientos INCREMENTAL no reconocido | $ 651,59 | Cálculo | Conversor de arrendamientos: PV = 651,59 (compromisos de la nota 6 del 10-K 2025 (SEC, 3-feb-2026): 174, 170, 116, 98, 83, 151; Kd 6,39 %) | Hoja | Compromisos coinciden con el 10-K [OBSERVADO]; pasivo contable 696 |
| 55 | Input sheet | B80 | Ajuste de EBIT atribuible a pasivos incrementales | 53,40228625 | Cálculo | Ajuste de EBIT del conversor: 53,40 (gasto 162 − depreciación 108,6) | Hoja | Gasto de arrendamiento 162 coincide con el 10-K [OBSERVADO] |
| 56 | Input sheet | B81 | Estado de conciliación de arrendamientos | CONCILIADO | Cálculo | Estado de conciliación de arrendamientos | Hoja | CONCILIADO |
| 57 | Input sheet | B82 | Inversiones a largo plazo según balance (dato histórico; NO valor razo | $4.009 | Dato | 10-Q 2T26 (SEC, 28-jul-2026): inversiones a largo plazo 4.009 | Hoja (Balance Sheet!L14) | Coincide [OBSERVADO] |
| 58 | Input sheet | B83 | Valor CONTABLE de inversiones excluidas del capital operativo | $4.009 | Cálculo | Valor contable de inversiones excluidas del capital operativo (=B82) | Hoja | Coincide |
| 59 | Input sheet | B84 | Valor ECONÓMICO atribuible de participaciones y activos no operativos | 3601,75 | Juicio | 10-Q 2T26 (SEC, 28-jul-2026): componentes de inversiones; valor económico 3.601,75 | IA | Ver B20 |
| 60 | Input sheet | B85 | Control de inversiones y doble contabilización | VALIDADO | Cálculo | Control de inversiones y doble contabilización | Hoja | VALIDADO (rótulo; no sustituye la comprobación) |
| 61 | Input sheet | B86 | Revisión: no están incluidas en EBIT/FCFF ni duplicadas | Sin solapamiento | Juicio | Sin solapamiento con EBIT/FCFF | IA | Las pérdidas de inversiones van en otros ingresos (fuera del EBIT) [OBSERVADO] |
| 62 | Input sheet | B87 | Fuente y conciliación de inversiones no operativas | 10-Q 30-jun-2026, inversiones a largo pl | Juicio | Texto de fuente y conciliación (URL del 10-Q) | IA | Presente |
| 63 | Input sheet | B89 | Método fiscal de proyección (obligatorio en cada copia) | Normalizada | Juicio | Método fiscal: Normalizada | IA | Ver B90 |
| 64 | Input sheet | B90 | Tasa inicial NORMALIZADA (solo si B89=Normalizada) | 0,19 | Juicio | Tasa inicial 19 %: efectiva LTM 16,4 %, 18 % en 1S26, 16,8 % en 2025 (reestructuración interna) | IA | [HIPÓTESIS]; ver H-09 |
| 65 | Input sheet | B91 | Fuente / conciliación de impuesto efectivo vs marginal | FY2025 16,8 % afectado por una reestruct | Juicio | Fuente/conciliación del impuesto | IA | Presente |
| 66 | Input sheet | B92 | Control de hipótesis fiscales | VALIDADO | Cálculo | Control de hipótesis fiscales | Hoja | VALIDADO (rótulo) |
| 67 | Input sheet | B93 | Impuesto inicial para pronóstico (no altera la tasa histórica) | 0,19 | Cálculo | Impuesto inicial para el pronóstico (=B90) | Hoja | 19 % |
| 68 | Input sheet | B96 | Tasa libre de riesgo nominal de largo plazo · misma moneda del DCF | 5,29% | Cálculo | Tasa libre de largo plazo (=B35) | Hoja | 5,29 % |
| 69 | Input sheet | B97 | WACC terminal efectivo del modelo (independiente del DCF habilitado) | 8,99% | Cálculo | WACC terminal = tasa libre + prima país de EE. UU. (B96 + `Country equity risk premiums!B2`) | Hoja | 8,99 % = costo_capital_terminal del corte [MODELO] |
| 70 | Input sheet | B98 | Base | Sin liberación | Juicio | Sin liberación de capital en la historia Base | IA | Regla: liberación no automática |
| 71 | Input sheet | B99 | Conservadora | Sin liberación | Juicio | Sin liberación (Conservadora) | IA | Ídem |
| 72 | Input sheet | B100 | Disrupción | Sin liberación | Juicio | Sin liberación (Disrupción), con justificación en C100 | IA | Ídem |
| 73 | Input sheet | B101 | Optimista | Sin liberación | Juicio | Sin liberación (Optimista) | IA | Ídem |
| 74 | Cost of capital worksheet | B12 | Which approach will you be using? | Detailed | Juicio | Método Detailed | IA | Exigido por REGLAS [MODELO] |
| 75 | Cost of capital worksheet | B13 | If direct input, enter cost of capital to use | 9,00% | Juicio | Costo de capital directo 9 % (no se usa) | Plantilla | Sin efecto |
| 76 | Cost of capital worksheet | B14 | Cost of capital based upon approach = | 8,38% | Cálculo | WACC inicial 8,38 % = ponderación de Ke 9,35 % y Kd después de impuestos 4,79 % | Hoja | B14 = E63 = Input!B36 [OBSERVADO] |
| 77 | Cost of capital worksheet | B19 | Number of Shares outstanding = | 855,50 | Cálculo | Acciones (=Input!B22) | Hoja | Coincide |
| 78 | Cost of capital worksheet | B20 | Current Market Price per share = | $ 52,53 | Cálculo | Precio (=Input!B23) | Hoja | Coincide |
| 79 | Cost of capital worksheet | B22 | Approach for estimating beta | Single Business(US) | Juicio | Beta por negocio único de EE. UU. (industria Information Services) | IA | Beta desapalancada 0,756 [MODELO]; H-07 |
| 80 | Cost of capital worksheet | B23 | If direct input, enter levered beta (or regression beta) | 1,20 | Dato | Beta de regresión 1,20 (no se usa) | Importador/IA | [NO VERIFICADO]; referencia |
| 81 | Cost of capital worksheet | B24 | Unlevered beta = | 0,76 | Cálculo | Beta desapalancada del sector, reapalancada a 0,91 con D/E de mercado 27 % y t = 25 % | Hoja | Recalculado: 0,7564 × (1 + 0,75 × 0,2701) = 0,9096 [OBSERVADO] |
| 82 | Cost of capital worksheet | B25 | Riskfree Rate = | 5,29% | Cálculo | Tasa libre (=Input!B35) | Hoja | 5,29 % |
| 83 | Cost of capital worksheet | B26 | What approach do you want to use to input ERP? | Operating regions | Juicio | ERP por regiones de operación | IA | Ver H-01 |
| 84 | Cost of capital worksheet | B27 | Direct input for ERP (if you choose "will input" | 6,00% | Juicio | ERP directo 6 % (no se usa) | Plantilla | Sin efecto |
| 85 | Cost of capital worksheet | B28 | Equity Risk Premium used in cost of equity = | 4,46% | Cálculo | ERP ponderado: 57,51 % × 3,70 % + 42,49 % × 5,50 % = 4,46 % | Hoja | Recalculado [OBSERVADO]; 5,50 % es hipótesis, ver H-01 |
| 86 | Cost of capital worksheet | B31 | Book Value of Straight Debt = | $ 13.410,00 | Cálculo | Deuda financiera (=Input!B16) | Hoja | 13.410 |
| 87 | Cost of capital worksheet | B32 | Interest Expense on Debt = | $ 461,00 | Cálculo | Intereses (=Input!B14) | Hoja | 461 |
| 88 | Cost of capital worksheet | B33 | Average Maturity = | 6 | Juicio | Vencimiento promedio de la deuda: 6 años | IA | [HIPÓTESIS]; las notas vencen entre 2026 y 2036 |
| 89 | Cost of capital worksheet | B34 | Approach for estimating pre-tax cost of debt | Direct Input | Juicio | Costo de deuda por entrada directa | IA | Ver B35 |
| 90 | Cost of capital worksheet | B35 | If direct input, input the pre-tax cost of debt | 6,390% | Juicio | Kd = tasa libre + 1,1 % = 6,39 % (calificación A2/A) | IA | Cupones de las notas de mayo de 2026: 4,55 %-5,55 % (8-K del 15-may-2026) [OBSERVADO] |
| 91 | Cost of capital worksheet | B36 | If actual rating, input the rating | A2/A | Dato | Calificación A2/A | IA | [NO VERIFICADO] con la agencia |
| 92 | Cost of capital worksheet | B37 | If synethetic rating, input the type of company | 2 | Juicio | Tipo de empresa para calificación sintética (no se usa) | Plantilla | Sin efecto |
| 93 | Cost of capital worksheet | B38 | Pre-tax Cost of Debt = | 6,39% | Cálculo | Kd antes de impuestos | Hoja | 6,39 % |
| 94 | Cost of capital worksheet | B39 | Tax Rate = | 25% | Cálculo | Tasa marginal (=Input!B25) | Hoja | 25 % |
| 95 | Cost of capital worksheet | B41 | Book Value of Convertible Debt = | 0 | Dato | 10-Q 2T26 (SEC, 28-jul-2026): sin deuda convertible | IA | [OBSERVADO] |
| 96 | Cost of capital worksheet | B42 | Interest Expense on Convertible = | 0 | Dato | Sin intereses de convertibles | IA | [OBSERVADO] |
| 97 | Cost of capital worksheet | B43 | Maturity of Convertible Bond = | 0 | Dato | Sin vencimiento de convertibles | IA | [OBSERVADO] |
| 98 | Cost of capital worksheet | B44 | Market Value of Convertible = | 0 | Dato | Sin valor de mercado de convertibles | IA | [OBSERVADO] |
| 99 | Cost of capital worksheet | B46 | Debt value of operating leases = | $ 651,59 | Cálculo | Deuda por arrendamientos (=Input!B79) | Hoja | 651,59 |
| 100 | Cost of capital worksheet | B49 | Number of Preferred Shares = | 0 | Dato | 10-Q 2T26 (SEC, 28-jul-2026): sin acciones preferentes | IA | [OBSERVADO] |
| 101 | Cost of capital worksheet | B50 | Current Market Price per Share= | 1 | Dato | Precio de preferentes (valor ficticio 1) | Plantilla | Sin efecto |
| 102 | Cost of capital worksheet | B51 | Annual Dividend per Share = | 0 | Dato | Dividendo de preferentes 0 | IA | Sin efecto |
| 103 | Option value | B5 | Enter the current stock price = | $ 52,53 | Cálculo | Precio (=Input!B23) | Hoja | 52,53 |
| 104 | Option value | B6 | Enter the strike price on the option = | $ 20,82 | Cálculo | Precio de ejercicio (=Input!B40) | Hoja | 20,82 |
| 105 | Option value | B7 | Enter the expiration of the option = | 3,00 | Cálculo | Vencimiento (=Input!B41) | Hoja | 3 |
| 106 | Option value | B8 | Enter the standard deviation in stock prices = | 45,00% | Cálculo | Volatilidad (=Input!B42) | Hoja | 45 % |
| 107 | Option value | B9 | Enter the annualized dividend yield on stock = | 0,89% | Juicio | Rendimiento por dividendo 0,89 % (dividendo anualizado US$0,56 / precio daría 1,07 %) | IA | [NO VERIFICADO]; inmaterial (H-02) |
| 108 | Option value | B10 | Enter the treasury bond rate = | 5,29% | Cálculo | Tasa libre (=Input!B35) | Hoja | 5,29 % |
| 109 | Option value | B11 | Enter the number of warrants (options) outstanding = | 0,02 | Cálculo | Opciones (=Input!B39) | Hoja | 0,017676 |
| 110 | Option value | B12 | Enter the number of shares outstanding = | 855,50 | Cálculo | Acciones (=Input!B22) | Hoja | 855,5 |
| 111 | Cost of capital worksheet | H6 | Ingresos EE. UU. (calculadora de países) | 19.626 | Dato | Ingresos de EE. UU. LTM: 18.868 + 9.930 − 9.172 = 19.626 (10-K 2025 (SEC, 3-feb-2026); 10-Q 2T26 (SEC, 28-jul-2026), nota 2) | IA | Recalculado [OBSERVADO] |
| 112 | Cost of capital worksheet | H17 | Ingresos resto del mundo (calculadora de países) | 14.502 | Dato | Resto del mundo LTM: 14.304 + 7.105 − 6.907 = 14.502 | IA | Recalculado [OBSERVADO] |
| 113 | Cost of capital worksheet | H29 | Ingresos América del Norte (calculadora de regiones) | 19.626 | Dato | Ingresos de América del Norte (=EE. UU.) 19.626 | IA | Coincide con H6 |
| 114 | Cost of capital worksheet | H32 | Ingresos fuera de EE. UU. sin desglose (calculadora de regiones) | 14.502 | Dato | Ingresos fuera de EE. UU. sin desglose 14.502 | IA | Coincide con H17 |
| 115 | Cost of capital worksheet | I32 | ERP fuera de EE. UU. sin desglose | 5,50% | Juicio | ERP de «fuera de EE. UU. sin desglose»: 5,50 % | IA | [HIPÓTESIS]; ver H-01 |
| 116 | Cost of capital worksheet | H37 | Ingresos por industria de EE. UU. | 34.128 | Dato | Ingresos por industria (negocio único): 34.128 | Hoja | Coincide con B12 |
| 117 | Cost of capital worksheet | H53 | Ingresos por industria global | 34.128 | Dato | Ingresos por industria global: 34.128 | Hoja | Coincide con B12 |


## 4. Historia financiera: diez años y punto de partida

Reconstrucción con diez ejercicios (2016-2025) y LTM, a partir de la hoja (Nivel 2). Ingresos de US$10.842 M (2016) a US$33.172 M (2025), CAGR de 13,2 %, pero con un quiebre: 15-21 % de crecimiento hasta 2021, 8,5 % en 2022, 8,2 % en 2023, 6,8 % en 2024, 4,3 % en 2025 y 2,9 % LTM sobre 2025.

| Métrica | Último (2025) | LTM | Promedio 3 años | Promedio 5 años | Promedio 9-10 años | Rango |
|---|---:|---:|---:|---:|---:|---|
| Crecimiento de ingresos | 4,3 % | 2,9 % sobre 2025 | 6,4 % | 9,2 % | 13,4 % (2017-2025) | 4,3 %-20,8 % |
| Margen operativo GAAP | 18,3 % | 17,4 % | 17,3 % | 16,5 % | 15,8 % | 13,9 %-18,3 % |
| Margen de flujo libre (operativo − capex) | 16,8 % | 19,3 % | 17,4 % | 18,5 % | 20,5 % | 14,2 %-30,2 % |
| ROIC (pestaña Eficiencia de capital) | 24,7 % | n. d. | 23,1 % | 21,2 % | 20,8 % (2017-2025) | 13,8 %-24,7 % |
| ROE | 25,7 % | n. d. | 22,1 % | n. d. | n. d. | 11,5 %-25,7 % |
| Acciones en circulación (M) | 920 | 856 | −7 % anual | −5 % anual | 1.207 → 856 (−29 %) | — |
| Deuda neta / EBITDA | 0,17 | 0,31 | n. d. | n. d. | negativa hasta 2024 | −2,4 a 0,3 |

Separación de efectos: (i) ciclo: 2022 combinó la caída del consumo y cargos de inversiones (utilidad neta US$2.419 M); (ii) contables: 2020 y 2021 incluyen ganancias de inversiones (utilidad neta de US$4.202 M en 2020) y desde 2025 hay ganancias y pérdidas de inversiones estratégicas fuera del EBIT; (iii) adquisiciones: Honey, Paidy y Xoom en el historial, sin compras grandes recientes; (iv) anomalías: el flujo operativo de 2025 bajó US$1.034 M por originaciones de préstamos mantenidos para la venta. Límites de homogeneidad: el margen bruto es 100 % porque PayPal presenta el gasto de transacción dentro de los gastos operativos; el flujo libre y el ROIC son definiciones de la hoja. Último trimestre: 2T26 (cierre 30-jun-2026).

## 5. Crecimiento de ingresos: de la historia a la proyección

**Historia que tendría que ocurrir.** La Base supone que los ingresos pasan de US$34.128 M a US$43.273 M en el año 5 y a US$53.605 M en el año 10. El año 1 crece 4,47 % (US$35.654 M) y los años 2-5 4,91 %, 5,09 %, 4,90 % y 4,94 %. Por línea (estimación propia, porque PayPal no publica ingresos por producto): checkout de marca 3-4 %, Braintree 3-4 %, Venmo y P2P 15 % a 10 %, otros servicios 5 %. Para llegar a 4,5 % en el año 1 frente a un LTM de +2,9 % sobre 2025 y a +6 % en el primer semestre de 2026 hace falta que el volumen de Braintree y los ingresos de crédito sigan aportando lo que aportaron en el 2T26 (Braintree +US$400 M, Venmo +US$60 M, PayPal −US$130 M). Se verificó que `Input sheet` (B27 = 2,88 %) no gobierna la proyección: `Valuation output` toma el crecimiento de cada historia, y el CAGR compuesto 43.272,8 / 34.128 → 4,87 % coincide con el 4,9 % del texto. Alternativa razonable: crecimiento de 3 % compuesto (entre el LTM y el promedio de 3 años menos un punto), que valdría cerca de US$95 por acción (matriz de sensibilidad: 2,9 % de crecimiento y 19,16 % de margen = US$95,3).

**Porqué ese valor y no otro.** El 4,9 % se apoya en tres hechos: el volumen crece 7-10 %, los ingresos de 2025 fueron +4,3 % y la mitad de las empresas de ese tamaño logra ~5 % compuesto en cinco años (54 % según las tasas base de Mauboussin y Callahan para el tramo de US$12.000-25.000 M en dólares de 2015). Se rechaza 6,8 % (Optimista) porque exige un checkout que crezca ≥5 % y la única evidencia es la declaración de que «se ha estabilizado más», y se rechaza 2-3 % porque ignora el crecimiento de volumen de Braintree. Es [HIPÓTESIS] sostenida por [OBSERVADO] de volumen e [INFERENCIA] de mezcla.

**Seis preguntas.** (a) Año 1: 4,47 %; años 2-5: ~4,9 %; años 6-10 convergen linealmente a 4,0 %; celdas `Escenarios e historias` y `Valuation output!C4:G4`. (b) 3 años 6,4 %, 5 años 9,2 %, 9 años 13,4 %, LTM 2,9 % [OBSERVADO]. (c) Mecanismo: volumen de pagos +7-10 % menos compresión de ingreso por dólar de volumen (5 puntos en el 2T26: ingresos +5 % frente a volumen +10 %). (d) Debe ocurrir: ingresos de transacción crecen ≥3 % con volumen +7 %; Venmo y crédito aportan ≥US$400 M anuales. (e) Lo refutaría: crecimiento sin divisas ≤2 % por dos trimestres con el volumen ya normalizado. (f) ±2 puntos de crecimiento en años 1-5 → −9,4 % / +10,4 % (US$95,27 / US$116,07) [MODELO, matriz de la hoja].

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Crecimiento de ingresos años 1-5 | 6,4 % / 9,2 % / 13,4 % / 2,9 % | 4,47 %, 4,91 %, 5,09 %, 4,90 %, 4,94 %; `Valuation output!C4:G4` | Tasas base: mediana nominal ~5,4 % (Mauboussin y Callahan 2016) | Volumen +7-10 % y estabilización del checkout | El checkout crece poco; el ingreso por transacción sube menos que el volumen | −9,4 % / +10,4 % con ±2 puntos [MODELO] |
| Crecimiento años 6-10 | n. d. | Convergencia lineal a 4,0 % | g del corte 4,0 % | Madurez de la red | Saturación de cuentas (+0,3 %) | Incluido en g terminal |
| Año 1 frente a LTM | LTM +2,9 % sobre 2025; 1S26 +6 % | 4,47 % | Guía no GAAP del año al alza (cifras no incluidas) | Braintree y crédito | 2T26 +3 % sin divisas | Un punto menos en el año 1 ≈ −1 % del valor [INFERENCIA] |

## 6. Márgenes operativos y normalización de beneficios

**Historia.** El margen operativo GAAP sube de 14,6 % (2016) a 18,3 % (2025) por escala, control de gastos de soporte y administración y menor gasto de transacción por dólar de volumen (0,94 % en 2023, 0,93 % en 2024, 0,89 % en 2025). En 2026 se revierte: 17 % en el primer semestre frente a 19 % un año antes, por gasto de transacción +11 %, soporte +12 %, tecnología +10 %. La Base parte de 17,58 % (con arrendamientos como deuda: el EBIT reportado más 53,4 de ajuste, +0,16 puntos) y converge a 19,16 % en el año 5. EBIT GAAP LTM US$5.946 M; el EBIT ajustado de la hoja resulta de sumar el gasto de arrendamiento y restar la depreciación del activo arrendado. Se verificó ingreso × margen = EBIT: 35.654,4 × 17,58 % = 6.267,7 [OBSERVADO en `Valuation output`]. La normalización de beneficios no suma cargos de reestructuración (US$331 M en 2025, US$187 M en el primer semestre de 2026) ni pérdidas de inversiones, que están dentro de «reestructuración y otros» y «otros ingresos»; el margen objetivo es, por tanto, ligeramente prudente si esos cargos no recurren.

**Porqué ese valor.** 19,16 % es el margen de 2025 (18,3 %) más cerca de un punto por el plan de ahorro (US$1.500 M brutos, de los que se reinvierte «una parte significativa»): sin el plan, la Base debería ser cercana a 17,5 %; con la totalidad del ahorro y sin reinversión, el margen subiría más de 4 puntos. 19,2 % supone retener alrededor de una quinta parte del ahorro bruto. Alternativas: 17,5 % (≈ US$96) o 21 % (≈ +10 %).

**Seis preguntas.** (a) 17,58 % año 1 y 19,16 % año 5; `Valuation output!B6:K6`. (b) 3 años 17,3 %, 5 años 16,5 %, 10 años 15,8 %, mejor 18,3 % (2025), peor 13,9 % (2022). (c) Escala y ahorro menos presión de mezcla. (d) Gasto de transacción ≤ crecimiento de ingresos; ahorro realizado. (e) Margen ≤16 % dos trimestres con el ahorro en marcha. (f) ±2 puntos → ±9,7 % [MODELO].

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Margen EBIT año 1 | 17,3 % / 16,5 % / 15,8 % / 17,4 % | 17,58 %; `Input sheet!B28` | Pares sin comparabilidad (Visa, Mastercard 44-66 %) | Continuidad con ahorro inicial | 2T26 en 16,4 % | ±1 punto ≈ ±5 % [MODELO] |
| Margen objetivo (año 5) | Máximo histórico 18,3 % | 19,16 % (19,2 % reportado en la ficha) | N/D | Ahorro y mezcla | Mezcla hacia Braintree | −9,7 % / +9,7 % con ±2 puntos |
| Impuesto | 16,4 % LTM; 18 % en 1S26 | 19 % → 25 % | Tasa marginal 25 % | Normalización | Beneficios fiscales internacionales | ver H-09 |

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

**Historia.** PayPal necesita poco capital físico (capex de US$623-889 M, 2-3 % de los ingresos), pero su capital invertido incluye cartera de crédito, crédito mercantil (US$10.929 M) y caja operativa. La hoja usa ventas/capital de 2,71 en los años 1-10, lo que implica reinversión de US$645 M en el año 1 ((ventas del año 2 − ventas del año 1) / 2,71 = 1.750 / 2,71 = 645) y de unos US$760-790 M en los años 5-10. Se verificó `reinversión = Δventas / ventas-capital` con el rezago de un año. El ventas/capital de 2,71 está por encima del de la empresa hoy (1,55 con capital de la hoja), por encima del sector de Damodaran (2,51) y por debajo del marginal de tres años (7,68) y del último año (3,19); el marginal es volátil por recompras y por la reclasificación de préstamos. El rendimiento implícito del capital nuevo (margen 19,2 % × 0,75 × 2,71) es 39 %, más del doble del ROIC terminal (15 %): la herramienta de control lo marca como aviso. El ROIC actual de la hoja es 24,7 % en 2025 (ROE 25,7 %) con capital que incluye crédito mercantil; no se asume que margen × ventas/capital iguale al ROIC contable.

**Porqué ese valor.** 2,71 equivale a 1,08 veces el ventas/capital del sector y a una reinversión de 11-13 % del NOPAT en los años 1-5. Alternativas: 2,17 (−20 %) da −1,3 % y 3,25 (+20 %) +0,9 % [MODELO]: el valor es poco sensible porque el negocio reinvierte poco. El riesgo está en la dirección opuesta: si la reinversión real incluyera la cartera de crédito que PayPal retiene, el ventas/capital sería menor. La asignación de capital muestra recompras de US$6.052 M (2025) y dividendo de US$0,14 por trimestre desde octubre de 2025; las recompras superaron el flujo operativo menos capex en 2023 y 2025.

**Seis preguntas.** (a) 2,71 años 1-5 y 6-10; `Input sheet!B32:B33`. (b) Empresa hoy 1,55; marginal 3 años 7,68; último año 3,19; sector 2,51. (c) Mecanismo: crecimiento con poco capital físico. (d) Debe ocurrir: el capital de trabajo del crédito se financie con ventas de cartera. (e) Lo refutaría: cartera de crédito retenida que crezca más que los ingresos. (f) ±20 % → −1,3 % / +0,9 %.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Ventas/capital | Hoy 1,55; marginal 3,19 (1 año) y 7,68 (3 años) | 2,71; `Input sheet!B32:B33` | Sector 2,51 (Damodaran, enero de 2026) | Modelo de capital liviano | Rendimiento implícito de 39 % | −1,3 % / +0,9 % con ±20 % |
| ROIC | 23,1 % / 21,2 % / 20,8 % / 2025: 24,7 % | ROIC actual del motor 20,9 % | N/D (Damodaran sin promedio útil) | Ventaja que se desvanece | Marca cede en checkout | Ver §9 |
| Recompras | US$5.002 M, 6.047 M, 6.052 M (2023-2025) | No se modelan: acciones fijas en 855,5 M | N/A | Retorno al accionista | Financiadas en parte con deuda | Acciones +5 % → −4,8 % |

## 8. Costo del capital y riesgo

Rf 5,29 % [OBSERVADO: FRED DGS10, 30-sep-2026]. Beta desapalancada 0,756 de «Information Services» (Damodaran, enero de 2026) reapalancada con D/E de mercado de 27,0 % (deuda 12.138 sobre capitalización de 44.939) y t = 25 %: 0,756 × (1 + 0,75 × 0,2701) = 0,910 [recalculado]. ERP 4,46 % (57,5 % de ingresos en EE. UU. con 3,70 % y 42,5 % fuera con 5,50 %). Ke = 5,29 % + 0,910 × 4,46 % = 9,35 % [recalculado]. Kd antes de impuestos 6,39 % (Rf + 1,10 %); después de impuestos 4,79 %. Pesos de mercado: patrimonio 78,73 %, deuda 21,27 % (incluye arrendamientos de 651,6). WACC = 0,7873 × 9,35 % + 0,2127 × 4,79 % = 8,38 % [recalculado]. El WACC terminal es 8,99 % (tasa libre más prima de EE. UU. de 3,70 %): converge linealmente entre los años 6 y 10 y se verificaron los factores de descuento compuestos (0,9227; 0,8513; 0,7855; 0,7247 en los años 1-4). `Cost of capital worksheet!B14 = E63 = Input sheet!B36` = 8,3817 % [OBSERVADO]. Método Detailed activo.

**Porqué ese valor.** La beta del sector refleja el riesgo operativo de un negocio de pagos con crédito y saldos; la de regresión (1,20) refleja la volatilidad de una acción que cayó con la salida del CEO y se deja como referencia. Con 1,20 el Ke sería 10,64 % y el WACC cerca de 9,4 %: valor cercano a −16 % (WACC +1 punto = −15,7 %) [INFERENCIA]. **Doble conteo:** el riesgo de erosión del checkout está en los flujos de las historias y también en la probabilidad de 20 % de la Conservadora; usar una beta alta lo contaría tres veces. El ERP de 5,50 % para el resto del mundo es el supuesto menos sustentado (H-01): Europa occidental 4,74 %, Asia 5,19 %, Canadá y Australia ≈ 3,70 %.

**Seis preguntas.** (a) Ke 9,35 %, WACC 8,38 % → 8,99 %; `Cost of capital worksheet!B14`. (b) Costo de capital histórico del corte: 2020-2021 con tasas más bajas (factor 0,6 en los múltiplos). (c) Riesgo sistemático moderado. (d) Tasas estables. (e) Tasa libre >5,5 % o beta de mercado persistentemente >1,1. (f) WACC ±1 punto → −15,7 % / +23,5 %.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Beta | Regresión 1,20 | 0,91; `Cost of capital worksheet!B24` | Damodaran, enero de 2026, 0,756 desapalancada | Riesgo operativo de pagos | Volatilidad reciente de la acción | WACC +1 punto = −15,7 % |
| ERP | 3,70 % madura | 4,46 % ponderado; B28 | Damodaran, octubre de 2026 | Exposición geográfica | 5,50 % de resto del mundo sin respaldo | Alternativa 4,9 % → +3,8 % [INFERENCIA] |
| Kd | Cupones 4,55 %-5,55 % (mayo de 2026) | 6,39 %; B35 | Spread de A2/A | Calificación A2/A según la hoja | Cupones por debajo del Kd | Peso de la deuda 21 %: efecto menor |
| WACC terminal | n. d. | 8,99 %; `Input sheet!B97` | Rf + prima EE. UU. | Convergencia | — | Terminal = 58,1 % del valor operativo |

## 9. Convergencia y valor terminal

g perpetuo 4,00 % [`Input sheet!B69`], igual al g del corte y menor que la tasa libre de 5,29 %; WACC terminal − g = 4,99 puntos (> 2 puntos, sin alerta). Margen terminal 19,16 %, impuesto marginal 25 %, reinversión terminal g / ROIC = 4,00 % / 15,00 % = 26,7 % del NOPAT; flujo terminal US$5.873,8 M = 53.605 × 1,04 × 19,16 % × 0,75 × (1 − 26,7 %) [recalculado: 5.875]. Valor terminal US$117.711 M; valor presente US$51.756 M, **58,1 %** del valor operativo (US$89.144 M). Continuidad FY10-FY11: crecimiento 4,0 % en ambos años [OBSERVADO].

ROIC terminal por ventaja: gana por encima del costo de capital desde hace más de tres años (ROIC 20-25 %); tiene ventaja identificable (efectos de red y marca de veinte años); y la ventaja se desvanece de forma visible (checkout). Resultado: punto medio entre 8,99 % y el ROIC actual de 20,9 % = 14,9 %, redondeado a 15,0 %. Sin ventaja la Base valdría US$90,42 (−14,0 %); con ROIC 16 % en lugar de 15 %, US$106,5 (+1,3 %). **Prueba de erosión del moat:** la historia Conservadora y la Disrupción usan ROIC terminal igual al costo de capital y valen US$67,06 y US$47,98.

**Porqué ese valor.** 4,0 % es la inflación esperada (~2,3 %) más crecimiento real (~1,7 %) y no supera la tasa libre; 15 % es un criterio del modelo, no una regla de Damodaran, aplicado igual a todas las empresas con ventaja que se desvanece. Alternativas: g = 3,5 % → −3,8 %; g = 4,5 % → +4,6 %.

**Seis preguntas.** (a) g 4,00 %, ROIC 15,00 %; `Input sheet!B50`, `B69`. (b) ROIC 3/5/10 años: 23,1 %/21,2 %/20,8 %. (c) Red de dos lados y marca. (d) La ventaja sobrevive diez años en pagos entre personas, crédito y transfronterizos. (e) El checkout cae por debajo de 0 % y Venmo se estanca. (f) −14,0 % si el ROIC iguala el costo de capital.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| g terminal | PIB nominal de largo plazo n. d. | 4,00 %; `Input sheet!B69` | Corte vigente (Rf 5,29 %) | Inflación + crecimiento real | Mayor que el crecimiento real de la economía | −3,8 % / +4,6 % con ±0,5 puntos |
| ROIC terminal | 20,8 % medio de 9 años | 15,0 %; `Input sheet!B50` | Industria N/D | Ventaja que se desvanece | Marca y red aún fuertes | −14,0 % si = costo de capital |
| Peso del terminal | — | 58,1 % | — | — | Dependencia alta del terminal | Informativo |

## 10. Validación independiente del valor intrínseco

Reproducción en Python de la Base con los flujos anuales del Nivel 2 (NOPAT y reinversión), descuento compuesto con la tasa de cada año y terminal con g = 4,0 % y ROIC = 15 %: valor presente de los flujos US$37.389 M (hoja: 37.388), valor presente del terminal US$51.765 M (hoja: 51.756), valor operativo US$89.154 M (hoja: 89.144). Puente al patrimonio: + caja 11.256 − deuda con arrendamientos 14.062 (13.410 + 651,6) + activos no operativos 3.601,75 − opciones 0,61 = **89.940** (hoja) frente a 89.950 (reproducción); con 855,5 M de acciones: **US$105,13** frente a US$105,14 [recalculado; diferencia por redondeo de entradas]. `Option value`: Black-Scholes con ajuste por dilución, 0,017676 M de opciones a US$20,82 y 3 años, valor US$34,28 por opción y US$0,61 M en total [OBSERVADO; entradas no trazadas, H-02]. `R& D converter`: sin efecto porque `Input sheet!B17 = No`, aunque la pestaña conserva cifras de ejemplo (1.071, 953, 834) que no son de PayPal (H-03). `Operating lease converter`: compromisos 174, 170, 116, 98, 83, 151 y gasto 162 coinciden con la nota 6 del 10-K; PV 651,6 frente a pasivo contable de 696 (tasa de descuento mayor); hay además un arrendamiento no iniciado de US$284 M [OBSERVADO]. `Cost of capital worksheet`: submétodo Detailed, ERP geográfico y `B14 = E63 = Input!B36`.

Hoy frente a FY+3: el DCF de la hoja es valor de hoy (US$105,13); `Resumen de Valoración` muestra además el «DCF capitalizado FY+3» (US$137,47 en la Base) como línea para combinar con los múltiplos a FY+3; no se confunden. DCF inverso con el precio fechado (US$52,53): crecimiento de los años 1-5 de −4,7 % con margen de 15,2 %, −7,0 % con 17,7 % y −8,5 % con 19,7 %; lo logró entre 92 % y 96 % de las empresas de ese tamaño [MODELO]. Sensibilidad (Base US$105,13): margen ±2 puntos 94,89/115,38; crecimiento ±2 puntos 95,27/116,07; WACC +1/−1 punto 88,58/129,81; g −0,5/+0,5 puntos 101,12/109,96; ROIC terminal = WACC 90,42; acciones +5 % 100,12. Recálculo de las historias y de las matrices: **no ejecutado** más allá de la Base (las otras tres se contrastaron con el motor del Modelo JMR, que coincide con la hoja).

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| DCF Base por acción | — | US$105,13; `Valuation output!B35` | — | Reproducido: US$105,14 | Diferencia de redondeo | Sin ajuste |
| Puente EV→patrimonio | Caja 10.422 → 11.256; deuda 11.593 → 13.410 | +11.256 − 14.062 + 3.602 | 10-Q 2T26 | Neutral | Deuda subió US$1.800 M en el semestre | Cada US$1.000 M = ~US$1,2 por acción |
| Acciones | 920 (dic-2025) → 862 (jun-2026) | 855,5 M fijas | Portada 22-jul | No se proyecta recompra | Recompras de unos US$1.500 M por trimestre | Ver H-04 |

## 11. Cuatro historias y probabilidades

| Historia | Crecimiento | Margen EBIT | Reinversión/ROIC | WACC/Ke | g y retorno terminal | Valor principal por acción | Probabilidad registrada | Qué la confirma/refuta |
|---|---|---|---|---|---|---|---:|---|
| Conservadora: el botón PayPal pierde frente a las billeteras nativas | 1,6 % compuesto (checkout 0 % → −2 %) | 16,2 % | Ventas/capital 2,71; ROIC terminal = 8,99 % | 8,38 % → 8,99 % / 9,35 % | 4,00 % y 8,99 % | US$67,06 | 20 % | Confirma: TPV de marca ≤0 %, margen ≤16 %; refuta: ≥+5 % |
| Base: se estabiliza con márgenes estables | 4,9 % compuesto | 19,2 % | 2,71; ROIC terminal 15,0 % | Ídem | 4,00 % y 15,0 % | US$105,13 | 50 % | Confirma: indicadores cerca de hoy; refuta: umbrales de la ficha |
| Optimista: reactivación con Fastlane, Venmo y publicidad | 6,8 % | 22,2 % | 2,71; ROIC terminal 15,0 % | Ídem | 4,00 % y 15,0 % | US$132,40 | 20 % | Confirma: checkout ≥+5 %, Venmo ≥+15 %, margen ≥19 % |

Promedio de las tres con probabilidades renormalizadas (0,50, 0,20, 0,20 sobre 0,90): (0,50 × 105,13 + 0,20 × 67,06 + 0,20 × 132,40) / 0,90 = **US$102,73** [recalculado: 102,73]. El MOS de 35 % se aplica al DCF Base: 105,13 × 0,65 = **US$68,34** [recalculado], igual a `Resumen de Valoración!B19`. Las probabilidades son la previa de la etapa «madura estable» (50/20/20/10) sin ajustes; se verificó que ningún indicador de la ficha cruzó su umbral (margen operativo 2T26 de 16,4 % frente a umbral ≤16 %; margen de transacción +1 % entre −/+4 %) y por tanto no hay movimientos sin indicador.

### ¿Qué pasaría si todo fallara?

**Disrupción (probabilidad 10 %, fuera del promedio):** PayPal pierde el checkout (−3 % a −5 % anual) y compite por precio; Braintree sin crecimiento; Venmo 5 %; crecimiento compuesto −1,1 %, margen 13,2 %, g terminal 0 % y ROIC igual al costo de capital. Valor **US$47,98** por acción. El esperado de las cuatro historias (con Disrupción al 10 %) sería (0,5 × 105,13 + 0,2 × 67,06 + 0,1 × 47,98 + 0,2 × 132,40) = US$97,3 [recalculado, solo informativo]. Los supuestos son idénticos en WACC e impuestos a las otras historias: el riesgo va en los flujos, no en la tasa.

## 12. Valoración por múltiplos: prueba independiente y secundaria

**Integridad de cálculo.** Los siete métodos están calculados con las fórmulas de la plantilla (el cálculo no se reconstruyó): EV/EBITDA, EV/FCFF, P/E, P/FCFE y P/OCF con los múltiplos de salida de `J8/J19/J30` de cada pestaña; P/V (`PV`) y P/BV (`PBV`) con los de `J8/J19/J30` fijados el 26-oct-2026 con la misma regla (antes estaban en blanco: los ceros o vacíos no se aceptan como evidencia). Cadena verificada: `Financials Multiples` → proyección FY+1..FY+3 → precio por acción → dividendos acumulados (US$0,15/0,30/0,46) → descuento al costo del patrimonio (9,35 %). Para P/BV el patrimonio común del balance es US$19.820 M (conciliado con el 10-Q); P/BV usa el patrimonio proyectado de la hoja. Los pesos del tipo «Madura» (EV/EBITDA 20 %, EV/FCFF 10 %, P/E 20 %, P/FCFE 5 %, P/OCF 5 %, P/V 0 %, P/BV 0 %; 40 % al DCF) se mantienen por una razón específica: el flujo operativo y el FCFE de PayPal se distorsionan por originaciones de préstamos mantenidos para la venta (−US$1.200 M en 2025) y por movimientos de fondos de clientes, de modo que se pesa más EBITDA y utilidad; P/V y P/BV se calculan pero no se ponderan porque las ventas ignoran el gasto de transacción de 48 % de los ingresos y el patrimonio está reducido por recompras (ROE 25,7 %).

| Método | Histórico A (etapa Dec '23-LTM) | Pares B (Visa, Mastercard, GPN, Block, Adyen) | Justificado C (Base) | Elegido Cons / Base / Opt | vs. actual LTM | Peso efectivo | Valor hoy Cons / Base / Opt |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 8,9× | 22,0× | 14,5× | 6,8 / 9,9 / 13,0× | Base +46 % | 20 % | 49,08 / 78,37 / 111,94 |
| EV/FCFF | 11,6× | 28,9× | 23,8× | 7,5 / 10,9 / 13,7× | Base +46 % | 10 % | 35,63 / 52,35 / 68,81 |
| P/E | 13,4× | 31,0× | 17,7× | 9,6 / 15,3 / 19,3× | Base +54 % | 20 % | 48,01 / 85,41 / 119,46 |
| P/FCFE | 11,1× | 28,9× | 20,5× | 6,8 / 10,4 / 14,0× | Base +53 % | 5 % | 33,38 / 52,96 / 76,04 |
| P/OCF | 9,9× | 20,8× | 18,1× | 6,0 / 9,3 / 12,2× | Base +55 % | 5 % | 33,93 / 53,55 / 74,14 |
| P/V | 2,4× (mediana de 4 cierres) | N/D | N/D | 1,32 / 2,03 / 2,63× | Base +54 % | 0 % | 46,09 / 74,57 / 101,26 |
| P/BV | 3,6× (mediana de 4 cierres) | N/D | N/D | 2,27 / 3,21 / 4,08× | Base +41 % | 0 % | 65,89 / 95,74 / 125,24 |

Múltiplos consolidados de los cinco ponderados: Conservador US$43,91, Base US$72,20 y Optimista US$101,12; frente al DCF de las mismas historias (67,06; 105,13; 132,40) la Base queda **31 % por debajo**, fuera de la banda de ±25 % de coherencia (H-10). Los múltiplos históricos se llevaron al costo de capital del corte con el factor (k del cierre − g)/(k del corte − g), acotado a [0,6; 1,4] (por ejemplo 0,6 en 2020-2021 y 1,166 en 2022). Los pares B (márgenes de 44-66 % y crecimiento de 14 %) solo comprueban: PayPal no es comparable. La ancla C comparte hipótesis con el DCF y funciona como techo de cada escenario (el P/E Optimista de 20,4× se recortó a 19,3× por esa razón). Sin descuentos generales adicionales. Justificación específica: EV/EBITDA y P/E miden la rentabilidad operativa y neta estables del negocio de comisiones; EV/FCFF, P/FCFE y P/OCF heredan la volatilidad del capital de trabajo del crédito; los pares puros de pagos de red (Visa, Mastercard) no tienen riesgo de crédito. Las Base de cada método parten de los cierres de 2024-2025 (años de crecimiento 4-7 %), por lo que implican una recuperación del múltiplo de 41-55 % frente al actual: para el Optimista existe justificación escrita por método; **para la Base no** (H-11).

## 13. Sensibilidades económicas y escenarios alternativos

DCF Base × WACC y g (US$ por acción): fila 8,38 % → 97,7 / 101,1 / **105,1** / 110,0 / 115,9 con g de 3,0 a 5,0 %; fila 7,38 % → 116,7 a 151,2; fila 9,38 % → 84,1 a 94,6. ROIC terminal × g: 14 % a 16 % cambia la Base de 103,6 a 106,5 (g = 4 %). Crecimiento de los años 1-5 × margen EBIT objetivo: de 70,4 (0,9 %; 15,16 %) a 154,3 (8,9 %; 23,16 %); el centro (4,9 %; 19,16 %) es 105,13. En las tres matrices el centro concilia con el DCF Base (rótulos «Conciliación central: OK»). DCF inverso frente al precio fechado (US$52,53): ver §10. Familia de múltiplos desplegada: matrices de valor presente por acción con ejes reales (múltiplo en veces × denominador FY+3 en US$ millones) solo para la historia Base y para los siete métodos; los centros concilian con el VP a tres años de cada método: EV/EBITDA 76,61 [`Sensibilidad por múltiplo!G84`, «OK»], EV/FCFF 51,79, P/E 84,08, P/FCFE 52,37, P/OCF 52,80, P/V 71,72, P/BV 105,27. No existen matrices de Conservadora, Optimista ni Disrupción (correcto). La pestaña «Sensibilidad económica múltiplos» de la maestra (ratios de múltiplo justificado) no se usa como matriz editorial. La familia de las dos anclas (JMR y observado) **no está desplegada** en el Nivel 2: [NO VERIFICADO] y fuera de lo exigido por REGLAS §8 salvo cálculo verificable. Todas las cifras de este apartado son simulaciones ejecutadas en la hoja salvo las alternativas con [INFERENCIA], que son direccionales.

## 14. Coherencia de hojas, cálculos y presentación

Artefactos examinados: hoja (61 pestañas); Nivel 1 y Nivel 2 del análisis (nuevos); `reference/damodaran/PYPL.json` y su resultado; anclas de múltiplos; registro de la app del 15-oct-2026 (precio 57,16; **no sincronizado** con la hoja nueva). No se supone sincronización automática.

**Formato unificado (REGLAS §11):** `unificacion_hojas.py` → informe `Modelo-JMR-datos/auditorias/revision-2026-10-26/unificacion/PYPL.json`: **UNIFICADA** (61 de 61 pestañas, mismo orden y dimensiones; 21.265 de 21.265 fórmulas; 122 de 122 selectores con su validación). Tras aplicar los múltiplos se repitió la restauración de fórmulas (0 celdas por restaurar) y `candados.py`: 15 de 15 candados. `controles_todas.sh PYPL`: «sin fallas» (M1-M3 OK).

Coherencia verificada: MOS sobre el principal (Base); promedio condicionado de tres (US$102,73) y Disrupción aislada; precio de la hoja (US$52,53) igual al de `Cost of capital`, `Option value`, `Resumen` y `Input sheet!D1`; costo de capital igual en tres celdas; `Valuation output` Base (35 = 105,13); `Escenarios e historias` con las cuatro historias. Presentación: la pestaña `Country equity risk premiums` conserva el rótulo «Updated January 1, 2026» aunque la prima madura usada (3,70 %) coincide con el corte de octubre de 2026 (H-08); `Resumen de Valoración` filas 6-14 y 22-26 usan el «DCF capitalizado FY+3» y los precios objetivo a FY+3 (US$137,47 en la Base; potencial de 110,6 %), que son una lectura secundaria distinta del valor de hoy de las filas 32-36; el lector no debe confundirlas. Texto del artículo y la sección 12: precio, beta (0,91), ventas/capital (2,71) y acciones (862 M) se alinearon con la hoja en esta revisión; la sección «Múltiplos (lectura secundaria)» del generador usaba los múltiplos del registro del 15-oct y se sustituyó por los de la hoja.

## 15. Hallazgos priorizados y propuestas de corrección

Materialidad (REGLAS §4B). Base de comparación: DCF Base US$105,13.

| ID | Severidad | Tipo | Evidencia | Impacto | Mantener/ajustar/investigar | Propuesta y alternativa | Requiere aprobación | Estado |
|---|---|---|---|---|---|---|---|---|
| H-01 | Medio | Supuesto (B: reserva acotada) | `Cost of capital worksheet!I32`: ERP de 5,50 % para el 42,5 % de ingresos fuera de EE. UU. sin respaldo; Europa occidental 4,74 %, Asia 5,19 %, Canadá/Australia ≈ 3,70 % | Con 4,9 % el ERP ponderado es 4,21 %, Ke −0,23 puntos y el valor sube ≈ +3,8 % [INFERENCIA con matriz WACC] | Investigar | Desglosar ingresos por país (UK, Alemania, Australia, Canadá, India) con la nota del 10-K y ponderar | Sí | Abierto |
| H-02 | Bajo | Dato (C) | `Input sheet!B39:B42` y `Option value!B9`: opciones 0,017676 M, precio de ejercicio 20,82, plazo 3 años, volatilidad 45 %, rendimiento 0,89 % sin trazar al 10-K; el rendimiento real sería ≈1,07 % | Valor total de las opciones US$0,61 M (<0,001 %) | Mantener | Trazar a la nota de compensación en acciones | No | Abierto |
| H-03 | Bajo | Supuesto (C) | `Input sheet!B17 = No`: no se capitaliza tecnología y desarrollo (US$3.103 M en 2025); la versión del 15-oct capitalizaba I+D a 3 años; el `R& D converter` conserva cifras de ejemplo (1.071, 953, 834) | Capitalizar elevaría el EBIT cerca de 0,2 puntos (≈ +1 %) [INFERENCIA con la matriz de margen] | Mantener | Documentar la decisión o limpiar el conversor | No | Abierto |
| H-04 | Bajo | Dato (C) | Acciones de la portada del 22-jul (855,46 M) con precio del 30-sep; recompras de julio-septiembre (≈ US$1.500 M) no reflejadas, ni la caja que financió | ≈ +1,7 % neto [INFERENCIA]; compensado por flujo generado | Mantener | Actualizar con el 10-Q del 3T26 | No | Abierto |
| H-05 | Bajo | Presentación (C) | `Input sheet!B27/B29` (2,88 %) y `B30` son predeterminados de la plantilla y no gobiernan la Base; pueden confundir al lector | Ninguno | Mantener | Añadir nota en la hoja (requiere cambio de plantilla) | Sí | Abierto |
| H-06 | Medio | Supuesto (C) | Ventas/capital 2,71 implica 39 % de rendimiento del capital nuevo (más del doble del ROIC terminal); coincide con el marginal de 3 años (7,68) pero supera el del sector (2,51) | −1,3 % con −20 % [MODELO]; −0,5 % con 2,51 | Mantener | Documentar el porqué (el marginal incluye recompras) | No | Abierto |
| H-07 | Medio | Supuesto (B) | Industria «Information Services» para un negocio de pagos con crédito: ninguna industria de Damodaran lo describe; la ficha anterior usaba «Financial Svcs.» y una beta del patrimonio de 0,97 | Beta 0,97 → Ke +0,27 puntos, WACC +0,21 puntos; valor ≈ −3,6 % [INFERENCIA con la matriz WACC] | Mantener | Dejar documentada la comparación | No | Abierto |
| H-08 | Bajo | Presentación (C) | Rótulo «Updated January 1, 2026» en `Country equity risk premiums` con prima de octubre de 2026 | Ninguno | Mantener | Actualizar el rótulo en la plantilla | Sí | Abierto |
| H-09 | Bajo | Supuesto (C) | Impuesto inicial de 19 % frente a 16,4 % LTM y 18 % en 1S26 | Con 17 % el valor sube ≈ +0,6 % [INFERENCIA] | Mantener | Documentar | No | Abierto |
| H-10 | Medio | Coherencia (D/C) | Múltiplos de la Base 31 % por debajo del DCF (fuera de ±25 %) | No afecta el DCF principal; el MOS usa el DCF | Investigar | Explicar la brecha con la historia de múltiplos (hecho en la sección 12 del artículo) | No | Resuelto en narrativa |
| H-11 | Medio | Supuesto (C) | Falta justificación escrita del salto de +41 % a +55 % del múltiplo Base sobre el actual (solo hay la del Optimista) | Afecta solo al 60 % secundario | Investigar | Escribir `justificacion_salto` para la Base | Sí | Abierto |
| H-12 | Bajo | Dato (C) | `Balance Sheet!L26` (arrendamientos financieros 10) sin actualizar a junio de 2026 | <0,1 % | Mantener | Actualizar | No | Abierto |
| H-13 | Bajo | Presentación (C) | 36 valores residuales en `Financials Multiples` sin referencias | Ninguno | — | Retirados durante la preparación con respaldo | No | Cerrado |
| H-14 | Medio | Dato (C) | El crecimiento del checkout de marca «~2 % sin divisas» de la ficha proviene de comunicaciones de la empresa no revisadas en esta auditoría | Informativo; sustenta la probabilidad de 20 % de la Conservadora | Investigar | Citar la fuente de la cifra en la próxima ficha | No | Abierto |

**Agregado conservador:** suma de valores absolutos de los impactos acotados: H-01 3,8 % + H-03 1,0 % + H-04 1,7 % + H-06 1,3 % + H-07 3,6 % + H-09 0,6 % = **12,0 %**, con direcciones mixtas (el neto es positivo, cercano a +3 %-4 %). **Clasificación:** H-01 y H-07 superan el 2 % individual (reservas materiales acotadas) y el agregado supera 3 %: **no es posible declarar VERIFICADO sin salvedades**; el dictamen es «Con reservas». Efecto en la decisión y el MOS: ninguno en el orden entre precio y valores (el precio de US$52,53 queda por debajo del precio con MOS de US$68,34 y por encima de la Disrupción, US$47,98, en cualquier escenario de los hallazgos). No hay bloqueantes (categoría A) ni datos o fórmulas con error.

## 16. Catalizadores, señales de refutación y seguimiento

| Métrica | Nivel observado con fecha | Señal favorable | Señal adversa | Fuente | Frecuencia |
|---|---|---|---|---|---|
| Margen operativo GAAP | 16,4 % (2T26); 17,4 % LTM | ≥19 % | ≤16 % | 10-Q y comunicado trimestral | Trimestral |
| Gasto de transacción frente a ingresos | +11 % frente a +5 % (2T26) | Crece ≤ ingresos | Crece 5 puntos más que ingresos | 10-Q | Trimestral |
| TPV de checkout de marca sin divisas | No publicado en el 10-Q; ficha ~+2 % | ≥+5 % | ≤0 % | Comunicado y llamada | Trimestral |
| Ahorro de la reorganización | Objetivo ≥US$1.500 M; primera fase ≈US$400 M | ≥US$400 M anualizados al cierre de 2026 | Sin cifra o reinvertidos | 10-Q (nota 1) | Trimestral |
| Pérdidas de crédito | Comercios 7,3 %; consumo 4,0 % (4T25) | ≤5 % y ≤4 % | >7,3 % o >4,5 % | 10-K/10-Q | Trimestral |
| Cuentas activas | 439 M, −0,2 M frente al 1T26 | +2 % anual | Descenso sostenido | Comunicado | Trimestral |
| ROIC y conversión de caja | ROIC 24,7 % (2025); flujo libre/utilidad 134 % LTM | ROIC ≥20 % | ROIC <15 % | Hoja | Anual |
| Resolución de CFPB y demandas | Dos citaciones; litigio consolidado el 21-may-2026 | Cierre sin sanción | Sanción o cambio de producto | 10-Q (contingencias) | Eventual |

Los umbrales son criterios del auditor, no guías oficiales. Próximo informe: resultados del 3T26 (finales de octubre de 2026; fecha por confirmar).

## 17. Dictamen económico y resumen para escuchar

**Calificación de la tesis: Plausible con reservas.** *Consistencia matemática:* alta; la Base se reprodujo con una diferencia de US$0,01, el WACC, la beta, el puente, el promedio de tres y el MOS se recalcularon sin discrepancias. *Trazabilidad documental:* alta para los datos de partida (ingresos, EBIT, intereses, deuda, caja, patrimonio, acciones, arrendamientos, precio y tasa libre, todos contrastados con el 10-K, el 10-Q, FRED y FMP); media para las entradas heredadas de opciones, calificación y beta de regresión. *Razonabilidad económica:* media; el crecimiento es defendible, el margen objetivo depende de un plan de ahorro sin detalle y la brecha de 31 % con los múltiplos no está resuelta del todo. **Supuesto más frágil:** el margen objetivo de 19,2 % y, dentro del costo de capital, el ERP de 5,50 % del resto del mundo. **Más defendible:** los datos de partida y el crecimiento de la Base. **Motor principal del valor:** margen y crecimiento en conjunto, con un terminal de 58,1 %. **Decisión analítica sugerida:** conservar la hipótesis Base con reservas y revisarla al publicar el 3T26. No se modificó la valoración.

**Resumen para escuchar (≈110 palabras):** PayPal cobra una comisión por mover dinero en una red de 439 millones de cuentas. El volumen de pagos crece diez por ciento, pero los ingresos solo cinco, porque el gasto de transacción sube más rápido y el margen operativo bajó a 16 por ciento en el segundo trimestre. La valoración Base supone que la nueva dirección y un plan de ahorro de mil quinientos millones devuelven el margen a 19 por ciento, con un valor de 105 dólares por acción frente a un precio de 52 con 53. La auditoría reprodujo el cálculo sin diferencias relevantes. Sus reservas son el costo del capital fuera de Estados Unidos y la brecha con los múltiplos. Dictamen: plausible con reservas.

## 18. Fuentes primarias, limitaciones y registro de versión

| Fuente | URL | Publicación / período | Consultada | Dato respaldado | Límites |
|---|---|---|---|---|---|
| Form 10-K 2025, PayPal | https://www.sec.gov/Archives/edgar/data/1633917/000163391726000024/pypl-20251231.htm | 3-feb-2026 / FY2025 | 26-oct-2026 | Ingresos, gastos, flujo, balance, arrendamientos (nota 6), segmentos, litigios | Sin proxy |
| Form 10-Q 2T26, PayPal | https://www.sec.gov/Archives/edgar/data/1633917/000163391726000082/pypl-20260630.htm | 28-jul-2026 / 2T26 | 26-oct-2026 | Balance, resultados, flujo, acciones de la portada, reorganización, contingencias | No auditado |
| Comunicado de resultados 2T26 (anexo 99.1) | https://www.sec.gov/Archives/edgar/data/1633917/000163391726000080/pypl2q-26earningsrelease.htm | 28-jul-2026 | 26-oct-2026 | TPV, cuentas activas, efectivo e inversiones, guía (sin cifras), dividendo | Cifras de la guía no leídas |
| Form 8-K (nombramiento del CEO) | https://www.sec.gov/Archives/edgar/data/1633917/000119312526035860/d68718d8k.htm | 3-feb-2026 | 26-oct-2026 | Cambio de CEO y presidente del consejo | — |
| Form 8-K (salida de responsables de unidad) | https://www.sec.gov/Archives/edgar/data/1633917/000119312526197533/d128781d8k.htm | 30-abr-2026 | 26-oct-2026 | Rotación directiva | — |
| Form 8-K (emisión de notas) | https://www.sec.gov/Archives/edgar/data/1633917/000119312526226653/d930458d8k.htm | 15-may-2026 | 26-oct-2026 | Cupones de US$2.000 M en notas | — |
| FRED DGS10 | https://fred.stlouisfed.org/series/DGS10 | 30-sep-2026 | 26-oct-2026 | Tasa libre 5,29 % | — |
| FMP, precios históricos (herramienta del entorno) | https://financialmodelingprep.com | 30-sep-2026 | 26-oct-2026 | Cierre US$52,53 | Fuente secundaria |
| Damodaran, betas por industria y ERP | https://pages.stern.nyu.edu/~adamodar/ | Enero y octubre de 2026 | 26-oct-2026 (por la hoja) | Beta desapalancada, prima de riesgo | No reabiertas en esta auditoría: [NO VERIFICADO] salvo coherencia con la hoja |
| Mauboussin y Callahan, *The Base Rate Book* | — | 2016 | — | Tasas base de crecimiento | Libro, sin enlace |

**No verificado / pruebas no ejecutadas:** transcripción de la llamada del 2T26, proxy, calificación crediticia A2/A, opciones del 10-K, ERP de las regiones por país, tablas históricas de Damodaran, años 2016-2022 de los estados (solo contrastados ingresos, EBIT y utilidad neta de 2023-2025), recálculo independiente de las historias Conservadora, Optimista y Disrupción y de las matrices de múltiplos.

**Registro de versión:** `prompt_version: auditoria-economica-jmr-v1.3`. Hoja auditada `1LI1LHXYFiCqg5i1_DDzs53Rd4eKv4zhDex2pxSvKuCs` (lectura del 26-oct-2026); ficha `JMR-valuation/reference/damodaran/PYPL.json`; corte de mercado 30-sep-2026. Estado de publicación: **no publicada**; ruta prevista si se autoriza: `Modelo-JMR-datos/auditorias/narrativas/PYPL.md`. Historial: versión anterior del 15-oct-2026 en el registro `valoraciones/PYPL-1790205796042.json` (sin auditoría v1.3).
