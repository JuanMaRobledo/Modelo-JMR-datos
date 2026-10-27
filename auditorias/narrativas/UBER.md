**Estado de publicación (2026-10-27): PUBLICADO CON SALVEDADES · revisión UBER-REC-20261027-R1.** Estudio recuperado con corte del 30-sep-2026; sin cambios de supuestos, probabilidades ni pesos. Valoración, análisis fundamental y esta auditoría corresponden a la misma hoja de Google y a la misma revisión.

**Controles ejecutados el 27-oct-2026:** siete múltiplos con fórmula y resultado numérico (`verificar_multiplos_hoja.py`), fórmulas contra la maestra del 22-oct (`audit_master_formulas.py`), consistencia hoja = registro = análisis (`consistencia_migracion.py --hoja`), candados vigentes, probabilidades.

**Salvedades vigentes:**
- Estudio recuperado: precio y corte de información del 30-sep-2026; no incorpora resultados posteriores ni actualiza supuestos.
- Siete múltiplos calculados por las fórmulas originales de la hoja (7/7 con fórmula y resultado numérico; fórmulas de cálculo y múltiplos idénticas a la maestra del 22-oct-2026); P/V y P/BV con peso 0 y estado provisional.
- Candados de la plantilla del 21-oct (Financials Multiples!M34:M36) no aplican a la maestra vigente; se exigen solo los presentes en ella.
- Regla H3 pendiente: P/E Base 15,16x y Optimista 15,61x, P/FCFE Optimista 23,10x y P/OCF Optimista 22,96x superan el límite de la regla; corregirlos exige cambiar celdas de salida de la hoja y requiere autorización.
- S1: márgenes Base 22% y Optimista 26% sostenidos con evidencia escrita (margen consolidado 13,4% en el 2T26; Movilidad 30,1%, Delivery 20,1%); hipótesis del analista, no hecho demostrado.
- Errores informativos #NUM! en EVEBITDA!B39:B41 y EVFCFF!B39:B41 (MEDIAN de múltiplos históricos sin datos numéricos); fórmulas idénticas a la maestra, no alimentan ningún precio.

---

# Auditoría económica narrativa — Uber Technologies, Inc. (UBER)

**Análisis fundamental vinculado:** [UBER en la app](https://juanmarobledo.github.io/Modelo-JMR/research.html?ticker=UBER) · registro `analisis/UBER-research-1789655244618-k9n7u.json` (revisión del 2026-10-26).

## 1. Ficha de auditoría y alcance

| Campo | Contenido |
|---|---|
| Emisor | Uber Technologies, Inc.; ticker UBER |
| Mercado, moneda y escala | NYSE (EE. UU.); US$ millones salvo por acción |
| Sector | Plataformas de movilidad y entrega (Transportation) (hoja: industria de Damodaran «Transportation») |
| Método intrínseco principal | DCF FCFF de la historia Base (compañía operativa); MOS de 35 % sobre ese valor |
| Estados examinados | 10-K 2025 y 10-Q del 2T26 (balance al 30-jun-2026, filing 0001543151-26-000032); LTM = FY2025 + 1S26 − 1S25 |
| Fecha de valoración / de auditoría | Corte de mercado 30-sep-2026 / 2026-10-26 |
| Precio del análisis | US$68,51 al cierre del 30-sep-2026 (corte común de la cartera); no se obtuvo un precio posterior |
| Hoja auditada | [Modelo JMR UBER](https://docs.google.com/spreadsheets/d/1R3V8gISxXCYIujVFSITu0svVBC3AsN4GF_pQHHLs5dw/edit), rehecha desde la maestra el 2026-10-26 |
| Artículo y Nivel 2 | `JMR-valuation/data/UBER_Research_Fundamental_Modelo_JMR_2026-10-26.md` y `UBER_Nivel2_Datos_Modelo_JMR_2026-10-26.md` |
| Registro en la app | Se publica con la autorización general del usuario; sin certificación previa (el usuario audita después) |
| Visto | Hoja completa por lectura; 10-Q del 2T26 (R2: balance) y XBRL de companyfacts; resultados del 2T26; comunicados de Delivery Hero y Rivian; ficha de historias |
| Fuera de alcance | 10-K completo (factores de riesgo, seguros, litigios); notas de inversiones y de impuestos del 10-Q; transcripción de la llamada; estados de los pares; consenso y calificaciones |
| Estado de verificación | **Con reservas** (no es una auditoría contable). Ver §15 y §17 |

## 2. Resumen ejecutivo y relato económico central

Uber coordina oferta y demanda local de viajes, entregas y carga. En el LTM a junio de 2026 facturó US$55.227 millones con EBIT GAAP de US$6.700 millones (12,1 %) y flujo libre de US$10.116 millones; Movilidad ganó 30,1 % y Delivery 20,1 % sobre sus ingresos en el 2T26. Tiene deuda financiera de US$12.723 millones e inversiones y participaciones por US$12.532 millones. La Base de US$73,27 por acción supone ~11 % de crecimiento compuesto y margen operativo de 22 % con ROIC terminal igual al costo de capital, y queda 7 % por encima del precio de US$68,51.

**Tesis Base favorable:** Plataforma madura que crece ~11 % con margen de 22 %: US$73,27 por acción. **Interpretación neutral:** Los robotaxis y la competencia recortan crecimiento y margen: ingresos +6,2 % anual y margen de 16 %; la Conservadora (US$42,62, 22,5 %) describe esa ruta. **Contratesis adversa:** Los robotaxis desintermedian los viajes más rentables: ingresos ~0 % anual y margen de 10 % (Disrupción, US$21,52, 15,0 %).

El supuesto que domina el valor es la tasa de descuento (±1 punto de WACC mueve la Base US$63,46 (−13,4 %) / US$85,72 (+17,0 %)), seguido por el margen operativo GAAP de 12 % a 22 % y el crecimiento de Movilidad y Delivery frente a los vehículos autónomos. El precio (US$68,51) queda por debajo de la Base (-7 %); ver el DCF inverso en §10. Esta narrativa no se deriva del precio: parte de los estados de la compañía.

## 3. Trazabilidad, integridad y jerarquía de evidencia

Inventario de las celdas de entrada de `Input sheet`, `Cost of capital worksheet`, `R& D converter` y `Option value`, y de los datos que la hoja enlaza desde las pestañas de estados (Income Statement, Balance Sheet, Cash Flow Statement; columna L = LTM). `Financials Multiples` no tiene celdas de entrada propias: son fórmulas.

**Conteo:** la tabla tiene **87 filas** (todas las de `Input sheet` con valor, las entradas clave del costo de capital y el conversor de I+D). Las celdas con fórmula por defecto (`Input sheet!B27:B33`) se incluyen porque el analista puede sustituirlas.

**Cómo se cargaron los estados.** (a) El importador de la SEC (`desde_cero.sh datos`) cargó diez ejercicios y el LTM; (b) el balance del LTM se reescribió con el 10-Q de junio de 2026 (caja 4.870 y 521 de inversiones corrientes, deuda de 1.997 y 10.726, patrimonio de 27.316); (c) la caja y las inversiones restringidas (11.132) quedan fuera de la caja; (d) las inversiones (8.759) y el método de la participación (3.773) van a la fila 14 como activo no operativo, con la historia de la hoja anterior; (e) las acciones son 2.042,56 M de la portada del 10-Q (31-jul-2026), escritas en Income Statement!L27; (f) las entradas de conversores (I+D, arrendamientos), NOL y regiones se heredaron de la hoja anterior.

**Diferencias de fuente y ajustes:** (a) acciones: 2.042,6 M de la portada frente a 2.067,9 M en el balance; (b) la tasa de impuestos del LTM (beneficio) se reemplaza por 25 % en B90; (c) el patrimonio de la hoja incluye las participaciones no controladoras redimibles (180), y B21 suma 903 + 180; (d) el costo de la deuda es una entrada directa de 6,4 % (la calificación sintética dejaba el cálculo vacío por la circularidad con el conversor).

| # | Pestaña | Celda | Rótulo | Valor | Tipo | Documento/fuente (URL en §18) | Quién lo aportó | Verificación |
|---:|---|---|---|---|---|---|---|---|
| 1 | Input sheet | B1 | Uber Technologies, Inc (NYSE:UBER) | Uber Technologies, Inc (NYSE:UBER) | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 2 | Input sheet | B4 | Date of valuation | 2026-09-30 | Juicio | Corte de mercado 30-sep-2026 (fecha de valoración) | Corte común | [OBSERVADO] |
| 3 | Input sheet | B5 | Company name | Uber Technologies, Inc | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 4 | Input sheet | B8 | Country of incorporation | United States | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 5 | Input sheet | B9 | Industry (US) | Transportation | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 6 | Input sheet | B10 | Industry (Global) | Transportation | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 7 | Input sheet | B12 | Revenues | $ 55.227,00 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 8 | Input sheet | B13 | Operating income or EBIT | $ 6.700,00 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 9 | Input sheet | B14 | Interest expense | $ 462,00 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 10 | Input sheet | B15 | Book value of equity | $ 28.399,00 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 11 | Input sheet | B16 | Book value of debt | $ 12.723,00 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 12 | Input sheet | B17 | Do you have R&D expenses to capitalize? | Yes | Juicio | Capitalización de I+D según la regla del sector de la empresa | IA | Decisión de método; ver hallazgos |
| 13 | Input sheet | B18 | Do you have operating lease commitments? | Yes | Juicio | Arrendamientos operativos como deuda (conversor de Damodaran) | IA | [MODELO] |
| 14 | Input sheet | B19 | Cash and Marketable Securities | $ 5.391,00 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 15 | Input sheet | B20 | Valor económico validado de participaciones y activos NO ope | $ - | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 16 | Input sheet | B21 | Minority interests | $ 1.083,00 | Dato | Participaciones no controladoras: 903 no redimibles + 180 redimibles | IA (10-Q 2T26) | Coincide [OBSERVADO] |
| 17 | Input sheet | B22 | Number of shares outstanding = | 2042,56 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 18 | Input sheet | B23 | Current stock price = | $68,51 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 19 | Input sheet | B24 | Effective tax rate = | 45,66% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 20 | Input sheet | B25 | Marginal tax rate = | 25,00% | Juicio | Tasa marginal federal más estatal de EE. UU. (25 %) | Plantilla/IA | Convención del modelo [MODELO] |
| 21 | Input sheet | B27 | Revenue growth rate for next year  | 12,90% | Juicio | Crecimiento del año 1 de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 22 | Input sheet | B28 | Operating Margin for next year | 14,29% | Juicio | Margen operativo del año 1 de la Base: 14 % más el ajuste de arrendamientos (0,29 pp) | IA (ficha de historias) | [HIPÓTESIS]; ver H-01 |
| 23 | Input sheet | B29 | Compounded annual revenue growth rate - years 2-5 = | 10,46% | Juicio | CAGR de los años 2-5 de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 24 | Input sheet | B30 | Referencia de margen objetivo (mediana histórica/sectorial;  | 22,29% | Juicio | Margen objetivo de la historia Base (entrada con defecto) | IA (ficha de historias) | Coincide con la ficha [MODELO] |
| 25 | Input sheet | B31 | Year of convergence for margin | 5,00 | Juicio | Año de convergencia del margen: 5 | Plantilla/IA | Coherente con las historias |
| 26 | Input sheet | B32 | Sales to capital ratio  (for years 1-5) | 2,20 | Juicio | Ventas/capital años 1-5 (ficha de historias, ajustado por el conversor de arrendamientos) | IA | [HIPÓTESIS]; ver hallazgos |
| 27 | Input sheet | B33 | Sales to capital ratio (for years 6-10) | 2,00 | Juicio | Ventas/capital años 6-10 (ficha de historias, ajustado por el conversor de arrendamientos) | IA | [HIPÓTESIS]; ver hallazgos |
| 28 | Input sheet | B35 | Riskfree rate | 5,29% | Dato | Treasury a 10 años del corte común (30-sep-2026): 5,29 % | Corte común (datos_mercado.py) | [OBSERVADO] FRED DGS10 |
| 29 | Input sheet | B36 | Initial cost of capital = | 10,31% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 30 | Input sheet | B38 | Do you have employee options outstanding? | No | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 31 | Input sheet | B39 | Number of options outstanding = | 0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 32 | Input sheet | B40 | Average strike price = | $0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 33 | Input sheet | B41 | Average maturity = | 0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 34 | Input sheet | B42 | Standard deviation on stock price = | 0,00% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 35 | Input sheet | B46 | Do you want to override this assumption = | No | Juicio | No se anula el WACC terminal: converge a la fórmula de la plantilla | Plantilla | [MODELO] |
| 36 | Input sheet | B47 | If yes, enter the cost of capital after year 10 = | 10,31% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 37 | Input sheet | B49 | Do you want to override this assumption = | No | Juicio | Anulación del ROIC terminal (Yes) o ROIC terminal igual al costo de capital (No) | IA | Ver hallazgos de ROIC terminal |
| 38 | Input sheet | B52 | Do you want to override this assumption = | No | Juicio | Sin probabilidad de fracaso en la Base | IA | [INFERENCIA] |
| 39 | Input sheet | B53 | If yes, enter the probability of failure = | 0% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 40 | Input sheet | B54 | What do you want to tie your proceeds in failure to? | V | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 41 | Input sheet | B55 | Enter the distress proceeds as percentage of book or fair va | 50% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 42 | Input sheet | B57 | Do you want override this assumption = | No | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 43 | Input sheet | B58 | If yes, enter a different lag (0 = no lag to 3 = lag of 3 ye | 1 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 44 | Input sheet | B60 | Do you want to override this assumption = | No | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 45 | Input sheet | B62 | Do you want to override this assumption = | Yes | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 46 | Input sheet | B63 | If yes, enter the NOL that you are carrying over into year 1 | $14.024,00 | Dato | NOL = (3.177 + 1.641 − 1.312) / 0,25, heredado de la hoja anterior | IA (hoja anterior) | [NO VERIFICADO] contra la nota de impuestos |
| 47 | Input sheet | B65 | Do you want to override this assumption = | No | Juicio | No se anula la tasa libre después del año 10 | IA | — |
| 48 | Input sheet | B66 | If yes, enter the riskfree rate after year 10 | 5,29% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 49 | Input sheet | B68 | Do you want to override this assumption = | Yes | Juicio | Se anula el crecimiento perpetuo con la regla del modelo | IA | Ver B69 |
| 50 | Input sheet | B69 | If yes, enter the growth rate in perpetuity | 4,00% | Juicio | Crecimiento terminal 4,00 % (≤ tasa libre de 5,29 %) | Regla vigente del modelo | [MODELO] |
| 51 | Input sheet | B71 | Do you want to override this assumption | No | Juicio | Sin efectivo atrapado | IA | [NO VERIFICADO] |
| 52 | Input sheet | B72 | If yes, enter trapped cash (if taxes) or entire balance (if  | $0,00 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 53 | Input sheet | B73 | & Average tax rate of the foreign markets where the cash is  | 0% | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 54 | Input sheet | B76 | Valor de acciones preferentes (misma unidad del DCF) | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 55 | Input sheet | B78 | PV del conversor ya incluido en deuda del balance (solapamie | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 56 | Input sheet | B79 | Pasivo de arrendamientos INCREMENTAL no reconocido | $ 2.459,59 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 57 | Input sheet | B80 | Ajuste de EBIT atribuible a pasivos incrementales | 165,9790176 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 58 | Input sheet | B81 | Estado de conciliación de arrendamientos | CONCILIADO | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 59 | Input sheet | B82 | Inversiones a largo plazo según balance (dato histórico; NO  | $12.532 | Cálculo | Enlace a pestaña de estados (col. L = LTM) | Hoja | Coincide con el último reporte [OBSERVADO] |
| 60 | Input sheet | B83 | Valor CONTABLE de inversiones excluidas del capital operativ | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 61 | Input sheet | B84 | Valor ECONÓMICO atribuible de participaciones y activos no o | 0 | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 62 | Input sheet | B85 | Control de inversiones y doble contabilización | VALIDADO | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 63 | Input sheet | B86 | Revisión: no están incluidas en EBIT/FCFF ni duplicadas | Sin solapamiento | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 64 | Input sheet | B87 | Fuente y conciliación de inversiones no operativas | Inversiones (8.759) y método de la participación (3.773) en  | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 65 | Input sheet | B89 | Método fiscal de proyección (obligatorio en cada copia) | Normalizada | Juicio | Método fiscal normalizado | IA | — |
| 66 | Input sheet | B90 | Tasa inicial NORMALIZADA (solo si B89=Normalizada) | 0,25 | Juicio | Tasa inicial normalizada de 25 %: el LTM tiene beneficios fiscales por liberación de reservas de valuación | IA | [INFERENCIA]; ver H-05 |
| 67 | Input sheet | B91 | Fuente / conciliación de impuesto efectivo vs marginal | El LTM tiene beneficio fiscal (liberaciones de la reserva de | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 68 | Input sheet | B92 | Control de hipótesis fiscales | VALIDADO | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 69 | Input sheet | B93 | Impuesto inicial para pronóstico (no altera la tasa históric | 0,25 | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 70 | Input sheet | B96 | Tasa libre de riesgo nominal de largo plazo · misma moneda d | 5,29% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 71 | Input sheet | B97 | WACC terminal efectivo del modelo (independiente del DCF hab | 8,99% | Cálculo | Fórmula de la plantilla | Plantilla | [MODELO] |
| 72 | Input sheet | B98 | Base | Sin liberación | Juicio | Sin liberación de capital en contracción (reinversión negativa se trunca a cero) | IA | Regla de Damodaran |
| 73 | Input sheet | B99 | Conservadora | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 74 | Input sheet | B100 | Disrupción | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 75 | Input sheet | B101 | Optimista | Sin liberación | Dato | Entrada de la hoja; fuente en la nota de la celda y en la sección 3 | IA | [NO VERIFICADO] |
| 76 | Cost of capital worksheet | B12 | Which approach will you be using? | Detailed | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 77 | Cost of capital worksheet | B22 | Approach for estimating beta | Direct Input | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 78 | Cost of capital worksheet | B26 | What approach do you want to use to input ERP? | Operating regions | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 79 | Cost of capital worksheet | B33 | Average Maturity = | 3 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 80 | Cost of capital worksheet | B34 | Approach for estimating pre-tax cost of debt | Direct Input | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 81 | Cost of capital worksheet | B35 | If direct input, input the pre-tax cost of debt | 6,400% | Juicio | Costo de la deuda antes de impuestos de 6,4 % (Treasury 5,29 % + ~1,1 pp); grado de inversión | IA | [NO VERIFICADO] la calificación; ver H-09 |
| 82 | Cost of capital worksheet | B41 | Book Value of Convertible Debt = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 83 | Cost of capital worksheet | B49 | Number of Preferred Shares = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 84 | Cost of capital worksheet | B50 | Current Market Price per Share= | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 85 | Cost of capital worksheet | B51 | Annual Dividend per Share = | 0 | Juicio | Costo de capital según la ficha de la empresa y las tasas comunes del corte | IA | [HIPÓTESIS]; ver §8 |
| 86 | Cost of capital worksheet | H29 | Ingresos H29 | $26.469 | Dato | Ventas de 2025 en Norteamérica: 26.469 (10-K 2025) | IA | Coincide [OBSERVADO] |
| 87 | R& D converter | F7 | Años de amortización del I+D | 3 | Juicio | Convención de Damodaran para la industria | IA | [MODELO] |

**Jerarquía de evidencia usada:** [OBSERVADO] (documento de la compañía o comprobación directa), [INFERENCIA] (deducción de lo observado), [HIPÓTESIS] (supuesto del analista), [MODELO] (resultado de las fórmulas) y [NO VERIFICADO].

## 4. Historia financiera: diez años y punto de partida

| US$ millones | Dec '20 | Dec '22 | Dec '23 | Dec '24 | Dec '25 | LTM |
|---|---:|---:|---:|---:|---:|---:|
| Ingresos | 11.139 | 31.877 | 37.281 | 43.978 | 52.017 | 55.227 |
| EBIT | -4.863 | -1.832 | 1.110 | 2.799 | 5.565 | 6.700 |
| Margen operativo | -43,7 % | -5,7 % | 3,0 % | 6,4 % | 10,7 % | 12,1 % |
| Flujo operativo | -2.745 | 642 | 3.585 | 7.137 | 10.099 | 10.424 |
| Capex | -616 | -252 | -223 | -242 | -336 | -308 |
| Capex / ventas | 5,5 % | 0,8 % | 0,6 % | 0,6 % | 0,6 % | 0,6 % |

La historia tiene tres fases. De 2019 a 2022 Uber perdió dinero mientras escalaba (margen operativo de −61 % a −6 %). En 2023-2025 el margen GAAP subió de 3,0 % a 10,7 % con ingresos creciendo ~18 % al año y el flujo libre pasó de US$3.362 a US$9.763 millones. En 2026 las reservas crecen ~20 %, el ingreso en dólares +6,2 % en el LTM, y la empresa anunció una oferta por Delivery Hero y acuerdos de robotaxis. La Base supone que la red sigue creciendo ~11 % con margen de 22 %; la Conservadora, que robotaxis y competencia recortan crecimiento y margen; la Disrupción, que los autónomos desintermedian los viajes más rentables.

## 5. Crecimiento de ingresos: de la historia a la proyección

La Base construye el ingreso por cubeta (Movilidad US$29.500 millones; Delivery US$21.000 millones; Freight US$4.727 millones). El resultado consolidado es 12,9 %, 12,1 %, 10,8 %, 9,9 %, 9,0 % en los años 1-5 (10,9 % compuesto) y cae a 4,0 % en el año 10: ingresos de 92.818 millones en el año 5 y 124.219 millones en el año 10.

Por qué ese ritmo: [INFERENCIA] el primer año de la Base (12,9 %) sigue las reservas de ~+20 % con captura menor, y baja a ~9 % en el año 5; la visión externa ubica ~11 % compuesto en el quintil superior (~19 % de las empresas de más de US$25.000 millones lo logró). Duda: el LTM en dólares crece solo 6,2 % y la hoja no incluye Delivery Hero.

Alternativas: la Conservadora (6,7 % compuesto, año 1 de 9,9 %); la Optimista (13,8 %, año 1 de 15,4 %); la Disrupción (2,0 %, con crecimiento terminal de 1 %). Los porcentajes son juicio del analista, no una guía publicada por la compañía.

## 6. Márgenes operativos y normalización de beneficios

La Base lleva el margen de 14,3 % en el año 1 a 22,3 % en el año 5 (ya ajustado por I+D capitalizado y arrendamientos; en base reportada 22,0 %). La Conservadora llega a 16,3 % (16,0 % reportado), la Disrupción a 10,3 % y la Optimista a 26,3 % (26,0 % reportado). Tasa impositiva: 25,0 % al inicio, convergiendo a la marginal de 25 % en el año 10.

Por qué ese margen: [OBSERVADO] el margen GAAP fue 12,1 % en el LTM, y los segmentos de Movilidad y Delivery ganan 30,1 % y 20,1 %. La Base supone 14 % el primer año y 22 % de objetivo, tras absorber costos corporativos y de seguros. Sensibilidad: ±2 puntos de margen dan US$66,08 y US$80,47 (±9,8 %). Fuerzas en contra: incentivos a conductores, regulación laboral, seguros y flotas autónomas propias.

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

La reinversión de la Base es de 3.421 millones en el año 1 (frente a un NOPAT de 8.910 millones) y el FCFF del año 1 es de 5.489 millones. El ventas/capital es 2,20 en los años 1-5 y 2,00 en los 6-10 (base de la hoja, que incluye I+D y arrendamientos cuando la empresa los capitaliza). Con ±20 % en el ancla, el DCF Base va de US$70,85 (−3,3 %) a US$74,89 (+2,2 %). ROIC terminal: Base 9,0 %, Conservadora 9,0 %, Disrupción 9,0 %, Optimista 9,0 %.

Evidencia: capex de apenas US$308 millones; el negocio es liviano en capital, pero la hoja usa ventas/capital de 2,2 (años 1-5) y 2,0 (años 6-10) heredados. El motor avisa que el capital nuevo rinde 27 % (Conservadora) y 43 % (Optimista), más del doble del ROIC terminal (9 %): ver H-07. ±20 % en el ventas/capital mueve la Base de US$70,85 a US$74,89.

## 8. Costo del capital y riesgo

Tasa libre de riesgo 5,29 % (Treasury a 10 años al 30-sep-2026), prima de riesgo de 4,65 % (ponderada por regiones de ingresos), beta desapalancada del sector 0,71 y beta apalancada 1,20 (propuesta bottom-up 1,20). WACC inicial 10,31 %; WACC terminal 8,99 %.

Dudas: (i) la beta de 1,20 es de regresión; la bottom-up de logística (0,71-0,80) queda muy por debajo y los comparables puros dan más (Lyft ~1,8, DoorDash ~1,75); (ii) el costo de la deuda es una entrada directa; (iii) la prima de mercado se pondera por regiones. ±1 punto de tasa da US$85,72 (+17,0 %) y US$63,46 (−13,4 %).

Efecto: ±1 punto de WACC mueve la Base US$63,46 (−13,4 %) / US$85,72 (+17,0 %), el supuesto de mayor peso. La plantilla hace converger el WACC de 10,31 % a 8,99 % en el año 10 (convención de Damodaran).

## 9. Convergencia y valor terminal

El valor terminal es 58,1 % del valor de los activos operativos de la Base (93.323 millones de 160.542 millones). Crecimiento terminal 4,00 % (≤ la tasa libre), ROIC terminal 9,0 % y WACC terminal 8,99 %. Con −0,5 puntos de crecimiento terminal la Base vale US$72,54 (−1,0 %); con +0,5 puntos, US$74,02 (+1,0 %).

Riesgos: (i) las cuatro historias suponen ROIC terminal igual al costo de capital (9 %): Uber gana hoy ~18 %, así que la hipótesis es conservadora si la red resiste a los robotaxis; (ii) el crecimiento terminal de 4 % (2,8 % en la Disrupción) es menor que la tasa libre de riesgo; (iii) Delivery Hero y las flotas autónomas no están en el terminal ni en la deuda.

## 10. Validación independiente del valor intrínseco

Comprobación 1 (identidad): la hoja y el motor independiente del repositorio coinciden en las cuatro historias (Base 73,27; Conservadora 42,62; Disrupción 21,52; Optimista 101,02), lo que valida la aritmética, no la economía. Comprobación 2 (puente): activos operativos 160.542 + caja 5.391 − deuda con arrendamientos 15.183 − opciones 0 − preferentes 0 + no operativos 0 = patrimonio común de 149.667 millones, o US$73,27 por acción con 2.042,6 millones de acciones. Comprobación 3 (DCF inverso del Nivel 2, margen → crecimiento anual de los años 1-5 que justifica el precio):

| Beta | Margen | Crecimiento anual de los años 1-5 que justifica el precio | Fracción de empresas de este tamaño que lo logra |
|---|---:|---:|---:|
| 1,20 | 16,3% | 16,7% | 6,5% |
| 1,20 | 22,3% | 9,3% | 25,4% |
| 1,20 | 26,3% | 5,8% | 42,9% |
| 1,20 | 16,3% | 16,7% | 6,5% |
| 1,20 | 22,3% | 9,3% | 25,4% |
| 1,20 | 26,3% | 5,8% | 42,9% |

Comprobación 4 (múltiplos propios): los múltiplos de 2019-2022 corresponden a una empresa con pérdidas; la regla por ciclo lleva la Base a 11,8× (EV/EBITDA), 14,7× (EV/FCFF) y 15,2× (P/E) con pares de plataformas (Lyft, DoorDash, Airbnb, Booking, Grab, Expedia). Dos múltiplos de la Optimista (P/FCFE y P/OCF) saltan 67-71 % sobre el actual y se justifican en la hoja.

## 11. Cuatro historias y probabilidades

| Historia | Probabilidad | CAGR 1-5 | Margen objetivo (ajustado / reportado) | ROIC terminal | g terminal | DCF por acción |
|---|---:|---:|---:|---:|---:|---:|
| Base · Plataforma madura que escala márgenes | 40,0 % | 10,9 % | 22,3 % / 22,0 % | 9,0 % | 4,0 % | US$73,27 |
| Conservadora · Robotaxis y regulación presionan la movilidad | 22,5 % | 6,7 % | 16,3 % / 16,0 % | 9,0 % | 4,0 % | US$42,62 |
| Disrupción · Deterioro de los fundamentales | 15,0 % | 2,0 % | 10,3 % / 10,0 % | 9,0 % | 0,9 % | US$21,52 |
| Optimista · Uber es la red de los vehículos autónomos | 22,5 % | 13,8 % | 26,3 % / 26,0 % | 9,0 % | 4,0 % | US$101,02 |

Las probabilidades salen de la regla del ciclo (crecimiento_alto) y no se ajustaron por indicadores: son un juicio condicional, no frecuencias observadas. El DCF esperado de las tres historias activas (pesos renormalizados) es US$72,50; con MOS de 35 % sobre el DCF Base el precio de compra es US$47,63. Cambiar los pesos cambia el esperado, no el DCF Base.

### ¿Qué pasaría si todo fallara?

Si los robotaxis y la competencia recortan el crecimiento y el margen (ingresos +6,2 % y margen de 16 %), la acción vale la Conservadora (US$42,62), 38 % por debajo del precio; si además los autónomos desintermedian los viajes (margen de 10 %), vale la Disrupción (US$21,52). El flujo libre de US$10.116 millones sostiene el servicio de la deuda de US$12.723 millones.

## 12. Valoración por múltiplos: prueba independiente y secundaria

Siete métodos (EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF, P/V y P/BV; los dos últimos con peso cero). Regla del 18-oct-2026: el múltiplo de cada escenario es el que la empresa tuvo cuando crecía como el escenario espera en FY+3 (Conservador 6,2 %, Base 10,8 %, Optimista 13,9 %), llevado al costo de capital del corte y limitado por el múltiplo justificado por los fundamentos de la misma historia; los comparables solo comprueban.

| Método | Mediana histórica 10a | Actual (LTM) | Ancla de peers (mediana) | Justificado Base | Peso en múltiplos |
|---|---:|---:|---:|---:|---:|
| EV/EBITDA | N/D× | 19,93× | 27,98× | 11,79× | 33 % |
| EV/FCFF | N/D× | 14,66× | 9,37× | 24,85× | 17 % |
| P/E | 15,20× | 15,16× | 23,17× | 17,83× | 33 % |
| P/FCFE | 18,44× | 13,83× | 9,96× | 19,63× | 8 % |
| P/OCF | 17,82× | 13,42× | 9,24× | 19,39× | 8 % |

Resultado: múltiplos consolidados de US$46,55 (Conservador), US$55,58 (Base) y US$76,29 (Optimista), frente a DCF de US$42,62, US$73,27 y US$101,02. Lectura del 30-sep-2026: el DCF (valor intrínseco) da US$88,85 por acción y los múltiplos, US$83,89 hoy: 6% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el DCF manda y los múltiplos son precio relativo.

La Base de los múltiplos (US$55,58) queda 24 % por debajo del DCF Base (US$73,27): la regla por ciclo lleva los múltiplos al nivel actual y el DCF supone que el margen sube de 12 % a 22 %. Los saltos de la Optimista en P/FCFE y P/OCF (+67 % y +71 %) superan además el tope diagnóstico del caso toro. Ver H-10.

## 13. Sensibilidades económicas y escenarios alternativos

| Supuesto cambiado (DCF Base US$73,27) | Valor |
|---|---:|
| WACC +1 pp / −1 pp | US$63,46 (−13,4 %) / US$85,72 (+17,0 %) |
| Crecimiento años 1-5 −2 pp / +2 pp | US$66,36 (−9,4 %) / US$80,91 (+10,4 %) |
| Margen objetivo −2 pp / +2 pp | US$66,08 (−9,8 %) / US$80,47 (+9,8 %) |
| Crecimiento terminal −0,5 pp / +0,5 pp | US$72,54 (−1,0 %) / US$74,02 (+1,0 %) |
| Ventas/capital −20 % / +20 % | US$70,85 (−3,3 %) / US$74,89 (+2,2 %) |

Ordenado por impacto: la tasa de descuento (±1 punto: +17,0 % / −13,4 %), el crecimiento de los años 1-5 (±2 puntos: −9,4 % / +10,4 %), el margen objetivo (±2 puntos: ±9,8 %), la dilución adicional de 5 % (−4,8 %) y el ventas/capital (±20 %: −3,3 % / +2,2 %). Las matrices del Nivel 2 recogen crecimiento por margen.

## 14. Coherencia de hojas, cálculos y presentación

La hoja está unificada con la maestra (61 pestañas en el mismo orden, 21.258 fórmulas intactas, 122 selectores idénticos) y el motor independiente reproduce las cuatro historias. Controles: candados 15/15, inputs completos, estados completos e integridad de hojas (registro en la bitácora de la sesión).

Intervenciones sobre la hoja que el lector debe conocer: (i) se restauraron las fórmulas de la maestra tras cada carga; (ii) el importador traía partidas de diciembre de 2025 en el LTM y se reescribió con el 10-Q de junio de 2026; (iii) las acciones, la tasa de impuestos y el patrimonio se llevaron a celdas que sobreviven a la restauración; (iv) el costo de la deuda se fijó como entrada directa porque la calificación sintética dejaba la celda vacía; (v) Delivery Hero y las flotas autónomas no están modelados.

## 15. Hallazgos priorizados y propuestas de corrección

| ID | Severidad | Hallazgo | Impacto | Propuesta |
|---|---|---|---|---|
| H-01 | Alta | El margen GAAP de 12,1 % sube a 22 % en la Base, por encima de lo que muestran los costos corporativos actuales | ±2 puntos de margen mueven la Base ±9,8 %; con 16 % de margen el valor se acerca a la Conservadora | Conciliar el margen de segmento (30 % y 20 %) con los costos corporativos y de seguros y proyectar el puente |
| H-02 | Alta | La oferta por Delivery Hero (~US$13.700 millones) y las flotas autónomas no están en la valoración ni en la deuda | Si se concretan, cambian la deuda, el crecimiento y el retorno del capital; el valor por acción cambiaría según el precio pagado | Valorar Delivery Hero por separado y modelar la financiación cuando haya condiciones públicas |
| H-03 | Alta | Las inversiones y participaciones (US$12.532 millones) se suman como activo no operativo a valor contable; el método de la participación pasó de US$287 a US$3.773 millones en el semestre | Equivale a ~US$6 por acción (9 % del precio); el valor razonable puede diferir mucho del contable | Valorar cada participación (cotizadas y no cotizadas) con la nota de inversiones del 10-Q |
| H-04 | Media | Las reservas de seguros (US$13.286 millones) están respaldadas por caja e inversiones restringidas (US$11.132 millones) que quedan fuera de la caja; la diferencia no se trata como deuda | Una brecha de ~US$2.200 millones equivale a ~US$1,1 por acción si fuera una obligación neta | Revisar la nota de seguros y decidir el tratamiento de la brecha |
| H-05 | Media | El NOL (≈ US$14.024 millones de ingresos) se heredó de la hoja anterior y el activo por impuestos diferidos (US$10.162 millones) sigue en el balance; el LTM tiene beneficios fiscales | Un NOL sobreestimado sube el valor; la tasa de 25 % desde el año 1 puede ser alta si el uso del NOL reduce impuestos en efectivo | Conciliar el NOL con la nota de impuestos del 10-K y 10-Q |
| H-06 | Media | El conversor de I+D usa I+D semestral escrito a mano (1S22 a 1S25) para alinear a 12 meses a junio | Un error de transcripción cambia el margen de la base ajustada | Verificar los semestres contra los 10-Q |
| H-07 | Media | Ventas/capital de 2,2 y 2,0 heredados implican que el capital nuevo rinde 27-43 % en la Conservadora y la Optimista, más del doble del ROIC terminal (9 %) | Posible sobrevaloración del flujo; ±20 % mueve la Base −3,3 % / +2,2 % | Recalcular el ventas/capital marginal con las compras y las flotas |
| H-08 | Media | La beta de 1,20 es de regresión (1,21 a dos años, error 0,20); la bottom-up de Transportation (0,71-0,80) describe otro negocio | ±1 punto de tasa mueve la Base +17,0 % / −13,4 % | Documentar la elección y comparar con comparables puros (Lyft, DoorDash, Instacart) |
| H-09 | Media | El costo de la deuda de 6,4 % es una entrada directa; la calificación sintética dejó la celda vacía por la circularidad con el conversor de arrendamientos | Afecta el WACC marginalmente (la deuda pesa ~8 % del capital) | Verificar la calificación vigente y el costo de la deuda con el 10-Q |
| H-10 | Media | P/FCFE y P/OCF de la Optimista (~23×) saltan 67-71 % sobre el actual y superan el tope diagnóstico del caso toro | El consolidado de múltiplos pesa 40 % del ponderado secundario; no afecta al DCF principal | Revisar el cierre de 2023 como ancla y el flujo libre normalizado |
| H-11 | Media | Las acciones (2.042,6 M) no incluyen premios sin consolidar; los pagos en acciones son US$1.939 millones al año | Una dilución adicional de 5 % baja la Base a US$69,78 (−4,8 %) | Confirmar RSU y opciones con la nota de compensación del 10-K |
| H-12 | Baja | El conversor de arrendamientos usa los compromisos del 10-Q anterior heredados (gasto de 370,9 y calendario de 341,3 a 2.050,5) | Efecto menor a 1 % en la Base | Actualizar el calendario con el 10-Q del 2T26 |
| H-13 | Media | El precio (US$68,51) queda 7 % por debajo del DCF Base y entre la Conservadora y el esperado; el DCF inverso pide ~9,3 % anual con margen de 22 % | El mercado paga por una expansión de margen parcial, no por la Optimista | Decidir si la Conservadora merece más probabilidad que 22,5 % |
| H-14 | Baja | La composición de los competidores y de la dirección, el resultado de Freight y los 8-K posteriores al 10-Q no se revisaron | Afecta las secciones 7 y 8 del análisis | Verificar con el 10-K y los informes de las compañías |

## 16. Catalizadores, señales de refutación y seguimiento

| Indicador | Último dato | Confirma Base u Optimista | Favorece Conservadora o Disrupción |
|---|---|---|---|
| Reservas brutas (interanual, sin divisas) | ~+20% | ≥ +15% | ≤ +10% |
| Margen de segmento de Movilidad | 30,1% (2T26) | ≥ 30% | ≤ 26% |
| Margen de segmento de Delivery | 20,1% (2T26) | ≥ 20% | ≤ 16% |
| Participación de viajes autónomos en la red de Uber | Inicial | Socios crecen dentro de Uber | Robotaxis crecen fuera de Uber |
| Delivery Hero | Oferta anunciada | Cierre con precio disciplinado | Precio más alto o integración difícil |

Indicadores de actualización de probabilidades: si las reservas crecen ≤ 10 % o el margen de Movilidad baja de 26 % sube la Conservadora; si los robotaxis crecen fuera de la red de Uber o hay reclasificación laboral, sube la Disrupción; si los socios autónomos crecen dentro de Uber y los márgenes de segmento suben, sube la Optimista. Próximo hito: resultados del 3T26 (nov-2026).

## 17. Dictamen económico y resumen para escuchar

**Dictamen: con reservas.** La hoja está bien formada, reproduce el motor en las cuatro historias y quedó UNIFICADA con la maestra; el balance del LTM se reescribió con el 10-Q del 2T26. Los supuestos que dominan el valor (margen de 12 % a 22 % y la respuesta de la red a los robotaxis) son hipótesis del analista, y la valoración excluye Delivery Hero. El valor de las participaciones, el tratamiento de las reservas de seguros y el NOL heredado son los puntos técnicos a revisar primero.

Resumen para escuchar: Uber es una plataforma de viajes y entregas con flujo libre de más de 10 mil millones de dólares. La Base de 73 dólares por acción queda 7 por ciento sobre el precio y supone que el margen sube de 12 a 22 por ciento. Lo que más mueve el valor es el margen y la amenaza de los robotaxis; la compra de Delivery Hero no está incluida.

## 18. Fuentes primarias, limitaciones y registro de versión

Fuentes primarias:

- [Uber, resultados del 2T 2026](https://investor.uber.com/news-events/news/press-release-details/2026/Uber-Announces-Results-for-Second-Quarter-2026/default.aspx)
- [Uber, oferta de compra de Delivery Hero](https://investor.uber.com/news-events/news/press-release-details/2026/Uber-Announces-Acquisition-Offer-for-Delivery-Hero/default.aspx)
- [Uber y Rivian, hasta 50.000 robotaxis](https://investor.uber.com/news-events/news/press-release-details/2026/Uber-and-Rivian-Partner-to-Deploy-up-to-50000-Fully-Autonomous-Robotaxis-2026-TViR4R05gi/default.aspx)
- [Waymo, datos de seguridad (jun-2026)](https://waymo.com/blog/shorts/safetydata-june26/)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)

Limitaciones: no es una auditoría contable; no se revisaron el 10-K completo, las notas de inversiones, impuestos y seguros, ni los 8-K posteriores al 10-Q; los competidores y la dirección se describen con conocimiento general; la calificación crediticia y el consenso no se verificaron. Registro de versión: auditoría v1.3 del 2026-10-26, vinculada a la hoja rehecha el mismo día y al artículo `UBER-2026-10-26`; no sustituye la auditoría posterior del usuario.
