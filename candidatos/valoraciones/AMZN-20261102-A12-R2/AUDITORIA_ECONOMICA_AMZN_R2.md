# Auditoría económica narrativa — Amazon.com, Inc. (AMZN)

> **Dictamen: PENDIENTE.** Tesis económica: **Plausible con reservas.** Revisión auditada: `AMZN-20261102-A12-R2` (CANDIDATO, no promovida al catálogo). Auditoría independiente: Claude Code, modelo `claude-opus-5-5`, esfuerzo `high` (metadatos de la sesión), en una sesión nueva. Las fases 2 y 3 se hicieron con ChatGPT Work/Codex (GPT-6), así que el auditor es otro LLM y otra sesión. **No se modificó la valoración**: no hubo escrituras en la hoja, en el JSON ni en el análisis. Las propuestas son para una fase 2 posterior con una `<REV>` nueva. **v2.1 (2-nov-2026):** corrige la base fiscal de las preferentes de Anthropic, que incluye las Series G y H (impuesto diferido 54.440, no 56.907). **v2 (2-nov-2026, misma sesión, a pedido del usuario):** se añaden B-06 (impuesto de caja) y C-09 (margen de partida); se resuelven cuantitativamente B-01 (base fiscal), B-03 (beta de regresión), B-04 (I+D capitalizada) y C-02 (causa raíz y anclas de múltiplos), y se deja en §15 un **R3 propuesto** con cambios celda por celda. La valoración sigue sin modificarse.

## 1. Ficha de auditoría y alcance

| Campo | Valor |
|---|---|
| Razón social / ticker | Amazon.com, Inc. · AMZN · acción común (Nasdaq), CIK 0001018724 |
| Sector (Damodaran) | Retail (General); beta multinegocio Retail (General) ×2 + Computer Services (AWS) |
| Moneda / escala | USD; millones (acciones en millones; valores por acción en USD) |
| Método intrínseco principal | DCF FCFF Base (Ginzu), Método A / A-1.2 |
| Corte de estados | LTM al 30-sep-2026 (10-Q presentado el 30-oct-2026) |
| Precio del análisis | 240,35 USD, cierre del 30-oct-2026 [OBSERVADO: Alpha Vantage TIME_SERIES_DAILY, cierre 240,3500] |
| Fecha de valoración / auditoría | 2-nov-2026 / 2-nov-2026 |
| Hoja auditada | [`1h6Xv5cNqwtKPpqI81KiZ_FNpTl4k_uQQS2QJEHphaBI`](https://docs.google.com/spreadsheets/d/1h6Xv5cNqwtKPpqI81KiZ_FNpTl4k_uQQS2QJEHphaBI/edit) (46 pestañas). Captura propia del auditor: valores y fórmulas, SHA-256 `c3fcffec…8c98` |
| JSON / análisis | `candidatos/valoraciones/AMZN-20261102-A12-R2/VALORACION_A12_EN_REVISION.json`, `AMZN_NIVEL_1.md`, `AMZN_NIVEL_2.md`, `AMZN_ANALISIS_A12_R2.html` (commit `b1fb039` de Modelo-JMR-datos) |
| Catálogo | AMZN **no figura** en `catalogo.json` (valoraciones, análisis ni auditorías). La revisión identificable más reciente es R2, en estado CANDIDATO. No existe `auditorias/solicitudes/AMZN/`. |

**Alcance.** Revisé la hoja completa (valores y fórmulas), el JSON y los Niveles 1 y 2. Como fuentes primarias usé el 10-Q del T3 de 2026, los companyfacts XBRL de la SEC (FY2016–9M2026), el 8-K del 29-oct-2026 (guía del T4), la curva diaria del Treasury, los archivos de ERP implícita de Damodaran `ERPOct26.xlsx` y `ERPNov26.xlsx`, y las tablas sectoriales de la propia hoja (Damodaran, enero de 2026). Los scripts oficiales corrieron contra la hoja R2 con el resolvedor de hoja redirigido en memoria, sin tocar el repositorio. Las entregas de las fases 2 y 3 las leí **al final**, solo para contrastar.

**Quedó fuera:** el anexo 99.1 del 8-K, que no leí entero (la guía la tomé del 10-Q, que la reproduce). Tampoco revisé el visor de la app, porque R2 no está publicada, ni verifiqué una por una las notas de las celdas históricas de los estados (verifiqué los agregados contra XBRL). **Estado de verificación: Con reservas.** Esto no es una auditoría contable.

## 2. Resumen ejecutivo y relato económico central

Amazon gana dinero con tres motores de economía muy distinta. El comercio de Norteamérica e Internacional vendió 636.073 M USD en los últimos doce meses con margen operativo bajo: en el T3 de 2026 fue 7,7 % en Norteamérica y 3,7 % en Internacional [OBSERVADO, 10-Q, segmentos]. Ese comercio subsidia y financia un ecosistema donde los servicios a vendedores, la publicidad (19.637 M en el T3, +11 %) y las suscripciones elevan el margen de la mezcla. AWS vendió 161.382 M en doce meses y en el T3 creció 39,3 % con margen operativo de 38,7 % [OBSERVADO]. AWS generó 61 % del EBIT de 9M26 (48.555 de 79.389 M) [OBSERVADO]. Lo que está cambiando es la intensidad de capital: compras de PP&E por 215.192 M LTM frente a una depreciación de 79.353 M, una guía de cerca de 220.000 M de capex en 2026 y un flujo libre reportado negativo (−42.357 M LTM). Todo ello lo respalda un backlog contractual de AWS de 578.000 M, con una vida media de 6,1 años [OBSERVADO], en buena parte asociado a OpenAI y Anthropic. Las dos son, además, inversiones de Amazon que pesan 294.595 M en el balance.

**Tesis Base favorable.** La capacidad de IA se monetiza a lo largo del horizonte. AWS mantiene márgenes cercanos a 30 % sobre una base mucho mayor, el comercio madura hacia un margen de un dígito alto y el margen consolidado sube de 13,1 % a 17 % en diez años. El capital invertido crece fuerte entre los años 1 y 5 (Ventas/Capital 0,75) y su productividad se recupera después (1,4). **Lectura neutral:** el capex adelanta demanda real (el backlog ya existe), pero la competencia de Microsoft y Google, y el poder de negociación de clientes enormes, limitan el ROIC incremental a algo cercano al del capital existente. **Contratesis adversa:** la capacidad entra antes que la demanda pagadora, los clientes de IA concentrados, que además son participadas, renegocian, la depreciación acelerada comprime el margen y el valor de las participaciones privadas, Nivel 3, se corrige.

El supuesto que **domina el valor** es la combinación del margen terminal (17 %) y la tasa terminal (9,49 %). El valor terminal es 85,1 % del VP operativo y, con el crecimiento Base, el precio de mercado exige un margen objetivo de 25,8 % [MODELO, inverso propio]. La contradicción que la empresa debe resolver es convertir 215.000 M anuales de capex en flujo libre positivo antes de que la productividad marginal del capital (Ventas/Capital incremental de 0,65–0,74 en los últimos doce meses, según cómo se defina el capital de trabajo) se consolide como norma.

La aritmética de R2 es **exacta**: reproduje los cuatro DCF con código propio con un error inferior a 1e-13 USD por acción. Pero la tasa de descuento no cumple la regla de fechas y fuente del corte (hallazgo A-01, de +12 % a +20 %) y los arrendamientos operativos se restan como deuda mientras el EBIT ya pagó la renta (A-02, de +6,2 % a +6,6 %). También son prudentes el impuesto contable de 22,5 %, cuando Amazon paga cerca de 6,5 % en caja por la depreciación al 100 % (B-06, +4 %), el ROIC terminal (B-02) y el margen de partida (C-09). En sentido contrario empujan las participaciones de Anthropic sumadas antes de impuestos (B-01, −3,4 %) y, sobre todo, una beta bottom-up de 0,86 frente a una beta de regresión de **1,49** (B-03). Con todo corregido en ambas direcciones, el **R3 central propuesto vale 185,3 USD (+24,6 %)**, en un rango de 169 a 198. La Base actual es más prudente que la mejor sustentada, pero ni corregida explica el precio de 240,35: hacerlo exige un margen terminal de 22,4 %, por encima de la historia Optimista.

## 3. Trazabilidad, integridad y jerarquía de evidencia

**Datos financieros materiales.** Estas celdas se alimentan por fórmula desde los estados de la hoja; las comparé con fuentes primarias.

| Dato | Valor | Período | Tipo | Documento | Celda | Aportó | Verificación |
|---|---|---|---|---|---|---|---|
| Ingresos | 797.455 | LTM sep-26 | Cálculo | XBRL: FY25 716.924 + 9M26 584.069 − 9M25 503.538 | Input!B12 | Fuente primaria | ✓ exacto |
| EBIT | 104.366 | LTM | Cálculo | XBRL 79.975 + 79.389 − 54.998 | Input!B13 | Fuente primaria | ✓ |
| Gasto de intereses | 4.484 | LTM | Cálculo | XBRL 2.274 + 3.805 − 1.595 | Input!B14 | Fuente primaria | ✓ |
| Patrimonio contable | 613.601 | 30-sep-26 | Dato | 10-Q, balance | Input!B15 | Fuente primaria | ✓ |
| Deuda en libros | 304.461 | 30-sep-26 | Cálculo | 10-Q: deuda LP en libros 179.952 (173.125 + 6.827) + arrendamientos 114.783 (100.288 operativos + 14.495 financieros) + obligaciones de financiamiento 9.726 | Input!B16 | Fuente primaria | ✓; excluye 380 de deuda de corto plazo (C-07) |
| Caja y valores | 114.226 | 30-sep-26 | Dato | 55.783 + 58.443 | Input!B19 | Fuente primaria | ✓ |
| No operativos | 294.595 | 30-sep-26 | Cálculo | 10-Q nota 2: notas convertibles de Anthropic 146,2 mM + preferentes de Anthropic 92,5 mM + OpenAI Serie C 50,0 mM + warrants 4,3 mM + método de participación 0,4 mM + otras privadas 1,2 mM (143,7 mM de privadas en el 10-Q − 92,5 − 50,0) | Input!B20/B84 | Fuente primaria + juicio | ✓ importe; **bruto de impuestos diferidos** (B-01) |
| Acciones | 10.811 | 30-sep-26 | Dato | 10-Q, balance (portada: 10.813 al 21-oct) | Input!B22 | Fuente primaria | ✓ (diferencia de 0,02 %) |
| Precio | 240,35 | 30-oct-26 | Dato | Cierre en Nasdaq | Input!B23 | Fuente secundaria | ✓ |
| Tasa libre | 4,94 % | 30-oct-26 | Dato | Treasury, curva diaria, 10 años | Input!B35 | Fuente primaria | ✓ |
| Prima madura | 4,55 % | «rebase» | **Juicio** | Nota: 4,20 % (pago ajustado, 1-oct) + (5,29 − 4,94) | ERP!B2 | IA | ✗ frente a la regla §4 (A-01) |
| Ingresos y EBIT de 10 años | FY2016–FY2025 | FY | Dato | XBRL 10-K | Income Statement B:K | Fuente primaria | ✓ los 20 valores exactos |

**Inventario completo de entradas** (prompt 3/3 §3). Revisé las cuatro pestañas exigidas, `Input sheet`, `Cost of capital worksheet`, `Financials Multiples` y `Option value`. Contra la maestra IA vigente (`1e-lbQ…NTEQ`) hay **207 celdas sin fórmula**. De ellas, **71 se diligenciaron** (valor distinto de la maestra): Input 49, Cost of capital 21, Option value 1 y Financials Multiples **0**. **Las 71 tienen nota de fuente en la celda (100 %)**, y la tabla siguiente tiene exactamente 71 filas, una por entrada. Las otras 136 celdas conservan el valor predeterminado de la plantilla (rótulos, ceros de convertibles y preferentes, textos guía). Los datos financieros brutos de los estados (Income, Balance, Cash Flow) son entradas de otras pestañas y se controlaron con `estados_completos.py` y con los agregados XBRL de arriba. El inventario reproducible está en `auditoria_fase4/inventario_entradas_R2.csv`.

| # | Hoja!celda | Valor | Fuente declarada en nota de la celda (extracto) | Tipo | Verificación del auditor |
|---|---|---|---|---|---|
| 1 | Input sheet!D1 | 240.35 | [DATO PRECIO] cierre sin ajuste de dividendos 2026-10-30 Amazon NASDAQ, USD; https://stockanalysis.com/stocks/amzn/history/?period=daily | Dato | Nota presente; no re-verificada individualmente |
| 2 | Input sheet!B4 | 46,325 | [DATOS FASE1] Precio cierre 30-oct-2026. DATE serial verificado corresponde 30-oct-2026; mercado USD. | Dato | Nota presente; no re-verificada individualmente |
| 3 | Input sheet!B5 | Amazon.com, Inc. | Emisor de clase común Amazon, ticker AMZN; FCFF WACC será Fase2. | Dato | Nota presente; no re-verificada individualmente |
| 4 | Input sheet!B8 | United States | [DATO] Domicilio EE.UU.; portada 10-Q Sep2026. https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm | Dato | Nota presente; no re-verificada individualmente |
| 5 | Input sheet!B9 | Retail (General) | [JUICIO A-1.2] Retail general para referencia consolidada; beta oficial usa tres segmentos y mezcla EV. AWS Computer Services es proxy imperfecto, no  | Juicio | Nota presente; no re-verificada individualmente |
| 6 | Input sheet!B10 | Retail (General) | [JUICIO] Referencia global secundaria para completar diagnóstico legado B32/B33. El DCF NO usa esas celdas: usa E5/F5 por historia. Beta oficial Multi | Juicio | Nota presente; no re-verificada individualmente |
| 7 | Input sheet!B17 | No | [RESERVA MATERIAL] No se inventa I+D pura: tecnología e infraestructura mezcla desarrollo, infraestructura y operación. Base GAAP sin capitalización s | Dato | Nota presente; no re-verificada individualmente |
| 8 | Input sheet!B18 | No | [DATO/CALCULO] No conversión incremental: deuda ASC842 reconocida 15959+98824 incluida en balance. Obligaciones financiación 426+9300 incluidas separa | Cálculo | Nota presente; no re-verificada individualmente |
| 9 | Input sheet!B21 | 0 | [DATO] No intereses no controladores separados en balance consolidado Sep2026; no confundir con inversiones propias en otras entidades. https://www.se | Dato | Nota presente; no re-verificada individualmente |
| 10 | Input sheet!B25 | 0.25 | [JUICIO] Impuesto marginal normalizado federal+estatal e internacional 25%; converge desde 22.5%. No es tasa estatutaria única. https://www.sec.gov/Ar | Juicio | Nota presente; no re-verificada individualmente |
| 11 | Input sheet!B31 | 10 | [JUICIO] Convergencia del margen a diez años por maduración AWS y publicidad, competencia y ampliación de infraestructura. Se preserva interpolación n | Juicio | Nota presente; no re-verificada individualmente |
| 12 | Input sheet!B35 | 0.0494 | [DATO] Treasury 10Y 30-oct-2026 4.94%. https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&t | Dato | Treasury 30-oct 4,94 % ✓ |
| 13 | Input sheet!B38 | Yes | [DATO] RSU a ejercicio cero: 223.3 millones no vestidas, Nota6. Se usa denominador de acciones reales 10811m y SBC permanece en EBIT. Defecto nativo d | Dato | Nota presente; no re-verificada individualmente |
| 14 | Input sheet!B39 | 223.3 | [DATO] Nota6 RSU: 26.1+99.4+62.8+25.2+7.5+2.3 =223.3 millones. No volver a añadir acciones diluidas. https://www.sec.gov/Archives/edgar/data/1018724/0 | Dato | 10-Q RSU 223,3 [no re-verificado en esta auditoría] |
| 15 | Input sheet!B40 | 0 | [DATO] RSU sin precio de ejercicio. Se conserva cero económico; Black-Scholes nativo IFERROR(log(S/0)) tiene error cuantificado. https://www.sec.gov/A | Dato | Nota presente; no re-verificada individualmente |
| 16 | Input sheet!B41 | 1.76741 | [CALCULO/JUICIO] Promedio ponderado desde Sep2026 usando puntos medios de ventanas de vesting Nota6. Después2030 situado a5.25 años; no mide ejercicio | Juicio | Nota presente; no re-verificada individualmente |
| 17 | Input sheet!B42 | 0.35 | [JUICIO] Volatilidad35% solo parámetro técnico; no estimación por regresión. Con strike cero la valoración económica límite no depende de sigma. https | Juicio | Nota presente; no re-verificada individualmente |
| 18 | Input sheet!B46 | No | [JUICIO] Terminal Rf+ERP madura rebasada; beta madura1. No prima específica por riesgo de ejecución. https://www.sec.gov/Archives/edgar/data/1018724/0 | Juicio | Nota presente; no re-verificada individualmente |
| 19 | Input sheet!B49 | Yes | [JUICIO] Ventaja residual de escala/ecosistema AWS y logística; ROIC por historia, calibrado contra sector, no contra precio. https://www.sec.gov/Arch | Juicio | Nota presente; no re-verificada individualmente |
| 20 | Input sheet!B50 | 0.125 | [JUICIO] ROIC terminal Base12.5%, spread3.01pp sobre WACC terminal9.49%. AWS/retail mantienen exceso modesto, no ROIC actual perpetuo. https://www.sec | Juicio | Nota presente; no re-verificada individualmente |
| 21 | Input sheet!B52 | No | [JUICIO] Disrupción ya modela deterioro; no descuento de quiebra adicional sin evidencia específica. https://www.sec.gov/Archives/edgar/data/1018724/0 | Juicio | Nota presente; no re-verificada individualmente |
| 22 | Input sheet!B54 | B | [NO APLICA] No descuento adicional por fracaso; B52=No. https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm | Dato | Nota presente; no re-verificada individualmente |
| 23 | Input sheet!B55 | 0 | [NO APLICA] Recuperación no se usa porque no se activa fracaso; no supone recuperación económica nula. https://www.sec.gov/Archives/edgar/data/1018724 | Dato | Nota presente; no re-verificada individualmente |
| 24 | Input sheet!B57 | No | [JUICIO] Lag1 inversión→ventas por despliegue centros de datos y logística. Se prueba lag0 en cálculo separado, no se elige por valor. https://www.sec | Juicio | Nota presente; no re-verificada individualmente |
| 25 | Input sheet!B60 | No | [JUICIO] No perpetuar tasa inicial; convergencia a25% marginal. https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm | Juicio | Nota presente; no re-verificada individualmente |
| 26 | Input sheet!B62 | No | [JUICIO/RESERVA] EBIT positivo, sin escudo NOL adicional independiente capitalizado; activos fiscales ya en balance. No afirma inexistencia legal de p | Juicio | Nota presente; no re-verificada individualmente |
| 27 | Input sheet!B65 | No | [JUICIO] Rf nominal USD4.94% constante; sensibilidad de tasa separada. https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-2026093 | Juicio | Nota presente; no re-verificada individualmente |
| 28 | Input sheet!B68 | Yes | [REGLA JMR] g estable USD4%, menor que Rf4.94%; Disrupción estabiliza al2% propio. https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/ | Dato | Nota presente; no re-verificada individualmente |
| 29 | Input sheet!B69 | 0.04 | [REGLA JMR] Corte de revisión R2, g USD4%; no modificación de Cartera global. https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn- | Dato | Nota presente; no re-verificada individualmente |
| 30 | Input sheet!B71 | No | [JUICIO/RESERVA] Caja/títulos disponibles sin haircut fiscal adicional no sustentado; no se reduce por prudencia sin evidencia específica. https://www | Juicio | Nota presente; no re-verificada individualmente |
| 31 | Input sheet!B76 | 0 | [DATO] Sin preferentes propias emitidas en balance. Preferentes de participadas son activos no operativos, no reclamaciones sobre Amazon. https://www. | Dato | Nota presente; no re-verificada individualmente |
| 32 | Input sheet!B78 | 0 | [NO APLICA] No conversor incremental activo; pasivo reconocido en balance una sola vez. No representa cero arrendamientos. https://www.sec.gov/Archive | Dato | Nota presente; no re-verificada individualmente |
| 33 | Input sheet!B83 | 294,595 | [CALCULO] Importe contable excluido capital operativo: 146200 convertibles+143700 privadas+4300 warrants+395 equity=294595. Notas2/7. Cifras privadas  | Cálculo | Nota presente; no re-verificada individualmente |
| 34 | Input sheet!B84 | 294,595 | [JUICIO] Proxy económico igual a carrying value reportado; falta verificación de realización/liquidez e impuestos. Stress -20%/-50% y no ganar doble p | Juicio | Nota presente; no re-verificada individualmente |
| 35 | Input sheet!B86 | Sin solapamiento | [CALCULO] Excluidas del capital operativo en B83 y añadidas una vez al equity; ganancias no operativas no están en EBIT. Caja114226 separada. https:// | Cálculo | Nota presente; no re-verificada individualmente |
| 36 | Input sheet!B87 | 10-Q Sep2026 Notas2/7: inversiones conve | [FUENTE/CALCULO/JUICIO] Conciliación no operativos. https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm | Juicio | Nota presente; no re-verificada individualmente |
| 37 | Input sheet!B89 | Normalizada | [JUICIO] NI y tributación afectados por valoraciones privadas; no extrapolar tasa reportada sin normalización. https://www.sec.gov/Archives/edgar/data | Juicio | Nota presente; no re-verificada individualmente |
| 38 | Input sheet!B90 | 0.225 | [JUICIO] Tasa operativa normalizada22.5%; contraste 9M2026 (33939-15200)/(147560-62800)=22.1%, aproximación no asignación fiscal exacta. Convergencia  | Juicio | Nota presente; no re-verificada individualmente |
| 39 | Input sheet!B91 | 10-Q Sep2026: beneficio fiscal y gananci | [FUENTE/JUICIO] No se sobrescribe impuesto histórico. https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm | Juicio | Nota presente; no re-verificada individualmente |
| 40 | Input sheet!B98 | Sin liberación | [JUICIO] Ninguna liberación automática de capital por caída de ventas; preservar capacidad y costos hundidos. | Juicio | Nota presente; no re-verificada individualmente |
| 41 | Input sheet!C98 | La capacidad de centros de datos no se c | [JUICIO] Riesgo expresado en reinversión/flujos. | Juicio | Nota presente; no re-verificada individualmente |
| 42 | Input sheet!B99 | Sin liberación | [JUICIO] Ninguna liberación automática de capital por caída de ventas; preservar capacidad y costos hundidos. | Juicio | Nota presente; no re-verificada individualmente |
| 43 | Input sheet!C99 | La capacidad de centros de datos no se c | [JUICIO] Riesgo expresado en reinversión/flujos. | Juicio | Nota presente; no re-verificada individualmente |
| 44 | Input sheet!B100 | Sin liberación | [JUICIO] Ninguna liberación automática de capital por caída de ventas; preservar capacidad y costos hundidos. | Juicio | Nota presente; no re-verificada individualmente |
| 45 | Input sheet!C100 | La capacidad de centros de datos no se c | [JUICIO] Riesgo expresado en reinversión/flujos. | Juicio | Nota presente; no re-verificada individualmente |
| 46 | Input sheet!B101 | Sin liberación | [JUICIO] Ninguna liberación automática de capital por caída de ventas; preservar capacidad y costos hundidos. | Juicio | Nota presente; no re-verificada individualmente |
| 47 | Input sheet!C101 | La capacidad de centros de datos no se c | [JUICIO] Riesgo expresado en reinversión/flujos. | Juicio | Nota presente; no re-verificada individualmente |
| 48 | Input sheet!B116 | Incluida en balance y gastos | [NO APLICA] No deuda convertible propia identificada; B41WACC=0. Inversiones convertibles Anthropic son activos, no deuda propia. https://www.sec.gov/ | Dato | Nota presente; no re-verificada individualmente |
| 49 | Input sheet!B117 | 10-Q Sep2026 Nota5 emisiones deuda propi | [DATO] Perímetro de convertibles. https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm | Dato | Nota presente; no re-verificada individualmente |
| 50 | Cost of capital worksheet!B12 | Detailed | Método JMR Detailed; segmentación+geografía combinadas. | Dato | Nota presente; no re-verificada individualmente |
| 51 | Cost of capital worksheet!B22 | Multibusiness(US) | Beta bottom-up tres segmentos. Tabla US; 64ComputerServices/23Retail firmas. No cohorte tamaño/ciclo comparable; percentiles N/D. | Dato | Nota presente; no re-verificada individualmente |
| 52 | Cost of capital worksheet!B26 | Will input | ERP geográfica calculada por ingresosFY25, sin sustituir fórmulas. | Dato | Nota presente; no re-verificada individualmente |
| 53 | Cost of capital worksheet!B27 | 0.0490579 | [CALCULO/JUICIO] .0455 +(.0078*43212+.0091*30688+.018*107467)/716924. Resto internacional CRP1.8pp proxy no desglose exacto. FY25 USA489657/Germany459 | Juicio | Juicio rebase; ver A-01 |
| 54 | Cost of capital worksheet!B33 | 10 | [JUICIO] Duración media10años para deuda y leases agregados. Notas de deuda13.9años Q3; leases más cortos. No vencimiento observado del conjunto. | Juicio | Nota presente; no re-verificada individualmente |
| 55 | Cost of capital worksheet!B34 | Direct input | Kd directo calculado de spread sintético: evita sumar spread soberanoUS0.23pp sobre Treasury ya observado. | Dato | Nota presente; no re-verificada individualmente |
| 56 | Cost of capital worksheet!B35 | 0.0534 | [CALCULO] Treasury4.94%+spreadAAA0.40% de tabla sintética local D37, cobertura104366/4484=23.275. No rating emitido por agencia. | Cálculo | Nota presente; no re-verificada individualmente |
| 57 | Cost of capital worksheet!B37 | 1 | [JUICIO] Empresa grande no financiera; tabla sintética de cobertura. | Juicio | Nota presente; no re-verificada individualmente |
| 58 | Cost of capital worksheet!G37 | Retail (General) | [JUICIO] Proxy sectorial para segmento: Norteamérica/Internacional/AWS. Mezcla nativa ponderada EV/Sales de industrias, no beta por ventas simple. | Juicio | Nota presente; no re-verificada individualmente |
| 59 | Cost of capital worksheet!H37 | 460,255 | [DATO/CALCULO] Ingresos LTM Sep2026, segmentosFY25+9M26-9M25. Suma797455. https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com | Cálculo | Nota presente; no re-verificada individualmente |
| 60 | Cost of capital worksheet!G38 | Retail (General) | [JUICIO] Proxy sectorial para segmento: Norteamérica/Internacional/AWS. Mezcla nativa ponderada EV/Sales de industrias, no beta por ventas simple. | Juicio | Nota presente; no re-verificada individualmente |
| 61 | Cost of capital worksheet!H38 | 175,818 | [DATO/CALCULO] Ingresos LTM Sep2026, segmentosFY25+9M26-9M25. Suma797455. https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com | Cálculo | Nota presente; no re-verificada individualmente |
| 62 | Cost of capital worksheet!G39 | Computer Services | [JUICIO] Proxy sectorial para segmento: Norteamérica/Internacional/AWS. Mezcla nativa ponderada EV/Sales de industrias, no beta por ventas simple. | Juicio | Nota presente; no re-verificada individualmente |
| 63 | Cost of capital worksheet!H39 | 161,382 | [DATO/CALCULO] Ingresos LTM Sep2026, segmentosFY25+9M26-9M25. Suma797455. https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com | Cálculo | Nota presente; no re-verificada individualmente |
| 64 | Cost of capital worksheet!B41 | 0 | [DATO] No convertibles propias identificadas; convertibles privadas poseídas son activo. | Dato | Nota presente; no re-verificada individualmente |
| 65 | Cost of capital worksheet!B42 | 0 | [NO APLICA] Sin deuda convertible propia. | Dato | Nota presente; no re-verificada individualmente |
| 66 | Cost of capital worksheet!B43 | 0 | [NO APLICA] Sin deuda convertible propia. | Dato | Nota presente; no re-verificada individualmente |
| 67 | Cost of capital worksheet!B44 | 0 | [NO APLICA] Sin deuda convertible propia. | Dato | Nota presente; no re-verificada individualmente |
| 68 | Cost of capital worksheet!B49 | 0 | [DATO] Sin preferentes propias en balance. | Dato | Nota presente; no re-verificada individualmente |
| 69 | Cost of capital worksheet!B50 | 0 | [NO APLICA] Sin preferentes propias. | Dato | Nota presente; no re-verificada individualmente |
| 70 | Cost of capital worksheet!B51 | 0 | [NO APLICA] Sin preferentes propias. | Dato | Nota presente; no re-verificada individualmente |
| 71 | Option value!B9 | 0 | [DATO] Sin dividendo común anunciado; RSU strike cero. No inventa parámetros para eludir error nativo. | Dato | Nota presente; no re-verificada individualmente |

**Jerarquía de evidencia.** El 10-Q, XBRL y el Treasury son evidencia primaria y verificada. Damodaran es evidencia primaria de mercado, y su uso no se ajusta a la regla (A-01). El precio es una fuente secundaria verificada. Los supuestos son [JUICIO] declarados en las notas. Ninguna entrada carece de origen documentado.

## 4. Historia financiera: diez años y punto de partida

| Métrica | Último (LTM sep-26) | Prom. 3 años (FY23–25) | Prom. 5 años (FY21–25) | Hasta 10 años | Rango |
|---|---|---|---|---|---|
| Crecimiento de ingresos | 11,2 % | 11,7 % | 13,2 % | TACC 9 años FY16→25: 20,3 % | 9,4 % (FY22) – 37,6 % (FY20) |
| Margen EBIT | 13,09 % | 9,44 % | 7,20 % | 5,78 % (FY16–25) | 2,31 % (FY17) – 13,09 % |
| Capex / ventas | 27,0 % | — | — | 5,7 % (FY16) | sube a 18,4 % (FY25) y 27,0 % (LTM) |
| Rotación de activo fijo | — | — | — | 4,56 (FY17) | baja a 2,35 (FY25) |
| Acciones en circulación | 10.811 | — | — | 9.540 (FY16) | +1,4 % anual de dilución neta |
| FCF reportado (OCF − capex neto) | −42.357 | — | — | — | positivo en FY23 y FY24 |

[OBSERVADO: pestañas `Income Statement`, `Eficiencia de capital` y `Valuation output` filas 49–52, verificadas contra XBRL.]

**Lectura.** El margen de 13,1 % es un máximo histórico y no es efecto del ciclo: refleja un cambio estructural de mezcla (AWS, publicidad) visible desde FY23. FY22 (2,4 %) fue una anomalía por exceso de capacidad logística y la marca negativa de Rivian (−16.806 M de resultado no operativo). La utilidad neta LTM (134.779 M) **no es comparable**: incluye 68.359 M de otros ingresos de 9M26, casi todos de la revaluación de Anthropic. Por eso el análisis usa EBIT y no beneficio neto, y por la misma razón P/E queda contaminado (§12). Los límites de homogeneidad son la capitalización de I+D ausente (B-04) y los arrendamientos según ASC 842 (A-02).

## 5. Crecimiento de ingresos: de la historia a la proyección

**Historia económica.** Para crecer 13,9 % en el año 1 (oct-26 a sep-27) se necesita que AWS siga entre 30 % y 35 % (guía implícita: backlog de 578.000 M y nuevos compromisos de OpenAI por 100.000 M a 8 años y de Anthropic por más de 100.000 M a 10 años) y que el comercio crezca entre 6 % y 8 %, con la publicidad en la franja de los «high teens» que la compañía guía para el T4. El crecimiento se desacelera de forma lineal hasta 4 % en el año 10 (TACC de los años 1–5: 11,73 %). Ingresos del año 10: 1,873 billones de USD.

| Métrica y horizonte | Histórico (3/5/10, LTM) | Modelo: valor / año / celda | Industria / pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Crecimiento año 1 | LTM 11,2 %; T3 +12,1 %; guía T4 +12 % a +16 % (8-K del 29-oct) | 13,90 %, `Escenarios e historias!C29` → `Valuation output!C4` | Retail (General) 9,9 % de crecimiento medio a 5 años (Damodaran, ene-26) | AWS +30–35 % sobre 161 mM + comercio +7 % | Norteamérica +6,2 % e Internacional +5,4 % en el T3; con AWS en 25 % el año 1 se queda cerca de 12 % | ±2 pp en los años 1–5: **+3,3 % / −3,1 %** (prueba propia) |
| TACC años 2–5 | Prom. 3 años 11,7 %; prom. 5 años 13,2 % | 12,9 % → 9,4 % | — | AWS converge hacia 15–20 %; comercio entre 5 % y 7 % | Saturación del comercio en EE. UU., aranceles | Incluido arriba |
| Años 6–10 | — | Lineal de 8,4 % a 4,0 % | g del corte 4 % | Madurez | — | Regla JMR |

Seis preguntas. (a) Año 1: 13,90 %; años 1–5: TACC 11,73 %. (b) Supera el LTM y el promedio de 3 años (11,2 % y 11,7 %) y está por debajo del promedio de 5 años (13,2 %). (c) El mecanismo es la mezcla hacia AWS con capacidad ya contratada. (d) Haría falta que AWS mantuviera crecimiento de 30 % o más durante cuatro trimestres y que la utilización fuera alta. (e) Lo refutaría un crecimiento de AWS inferior a 25 % o la renegociación del backlog. (f) ±2 pp mueven el valor ±3 %. **¿Por qué ese valor?** Está en el punto medio de la guía del T4 (14 %) y es coherente con el backlog. **Juicio: defendible, sin sesgo.** Verifiqué que `Valuation output` usa exactamente esa senda. Ojo: `Input sheet!B27/B29` (11,23 %) **no** gobiernan la Base (C-03).

## 6. Márgenes operativos y normalización de beneficios

**Historia económica.** El margen consolidado sube linealmente de 13,09 % (año 1) a 17,0 % (año 10, `Escenarios e historias!D5`). La narrativa de R2 lo descompone como comercio cerca de 8 % y AWS cerca de 30 %. Mi prueba de mezcla: con AWS en 35–40 % de los ingresos del año 10 a un margen de 30–35 %, y el comercio en 8–10 %, el consolidado queda entre 15,7 % y 20,0 %. **17 % es una mediana honesta.** Verifiqué la identidad ingreso × margen = EBIT en los diez años (error 0).

| Métrica y horizonte | Histórico | Modelo | Industria / pares | Historia causal | Evidencia contraria | Impacto |
|---|---|---|---|---|---|---|
| Margen EBIT año 10 | LTM 13,09 %; T3 13,9 %; prom. 3 años 9,4 %; prom. 5 años 7,2 %; 10 años 5,8 % | 17,0 %, `VO!L6`; terminal `M6` | Retail (General) 6,8 %; Software 33,0 % (Damodaran ene-26, en la hoja) | Mezcla AWS + publicidad; escala logística | Depreciación de IA (D&A +28 % LTM), precios de la nube, energía | 16 %: **−7,0 %**; 18 %: **+7,0 %**; 15 %/19 %: ∓14,0 % |
| Impuesto (**B-06**) | Contable 22,3 % LTM (contaminado por no operativos). **En caja: 6.814 M pagados en LTM frente a 104.366 M de EBIT (cerca de 6,5 %)**, con 36.344 M de impuesto diferido en LTM. El 10-K FY2025 dice que la ley tributaria de 2025 (depreciación al 100 % e I+D doméstica deducible de inmediato) «redujo significativamente» los impuestos en caja y prevé un efecto similar en 2026; la Notice 2026-7 los reduce más | 22,5 % en los años 1–5 → 25 % marginal | — | Con capex creciente, el diferimiento se renueva en lugar de revertirse (convención de Damodaran: tasa efectiva que converge a la marginal) | Si el capex se detiene, el diferido revierte; regla fiscal futura | 15 % → 25 %: **+4,2 %**; 10 % → 25 %: +7,1 % |
| Margen de partida (**C-09**) | Trimestres: T4-25 11,7 % → T1-26 13,1 % → T2 13,7 % → T3 13,9 %; guía T4-26 (punto medio) 12,7 %, +1,0 pp interanual | Año 1 = 13,09 % (LTM) | — | Con la mejora interanual de la guía, el año 1 queda en ~14,1 % | Q4 estacional y depreciación | 14,1 % con el mismo 17 % final: **+2,0 %** |

Seis preguntas. (a) 17 %, año 10, D5. (b) Supera todo el historial, pero el T3 ya está en 13,9 %. (c) La mezcla. (d) Que AWS mantenga 30 % o más con el doble de tamaño. (e) Un margen de AWS por debajo de 28 % durante cuatro trimestres. (f) ±1 pp mueve el valor ±7 %. **¿Por qué no más?** El mercado implica 25,8 % (21,4 % tras corregir A-01 y A-02): por encima del Optimista (20 %). Sin evidencia de un margen consolidado superior a 20 %, **17 % se sostiene**. La SBC permanece en el EBIT (19.873 M LTM), lo cual es correcto y evita contarla dos veces.

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

**Historia económica.** Entre los años 1 y 5 la Base reinvierte entre 155.000 y 163.000 M por año (Ventas/Capital 0,75, rezago de 1 año). Eso es coherente con un capex de cerca de 220.000 M (guía 2026), menos una D&A de 80.000 a 100.000 M, más capital de trabajo. Entre los años 6 y 10 la productividad sube a 1,4 y la reinversión cae a la mitad (de 154.744 a 78.118 en el año 6). Eso hace que el FCFF salte de 7.167 a 100.725. El ROIC del modelo va de 18,1 % (año 1) a 14,1 % (año 5) y vuelve a 15,2 % (año 10).

| Métrica | Histórico | Modelo | Industria | Historia causal | Evidencia contraria | Impacto |
|---|---|---|---|---|---|---|
| Ventas/Capital años 1–5 | Promedio del capital existente 1,57 (`Origen!F23`); incremental LTM 0,65–0,74 (prueba propia: ΔVentas 106,1 mM / reinversión de 144 a 164 mM según la definición de capital de trabajo) | 0,75, `VO!C40:G40` | Retail (General) 3,51 | Centros de datos con vida de 15 a 20 años | El capex del T3 (77.259 M) deja un T4 implícito de solo ~44.300 M para cumplir la guía de 220.000 M | 0,65: **−6,0 %**; 0,85: **+4,6 %** |
| Ventas/Capital años 6–10 | — | 1,4, `VO!H40:L40` | — | Normalización del capex | Capacidad por delante de la demanda | 1,0: **−4,1 %**; 1,2: −1,7 %; 1,6: +1,3 % |
| ROIC LTM | 15,9 % (`VO!B42`); 16,8 % con arrendamientos (referencia de foso) | Año 10: 15,2 % | Retail (General) 13,6 %; Software 29,3 % | — | — | ver §9 |
| ROIC LTM con I+D capitalizada (B-04) | I+D estimada 72.980 M (cota prudente: T&I 126.938 − D&A de PP&E 53.958) a 95.787 M (T&I − D&A de AWS); activo de investigación de 136.246 a 178.909 M (vida de 3 años) | — | — | El EBIT ajustado sube a 14,8 %–15,3 % del ingreso, pero el capital crece más | — | **ROIC ajustado 13,7 %–14,6 %** frente a 15,9 % GAAP |

Seis preguntas sobre Ventas/Capital. (a) 0,75 y 1,4. (b) El 0,75 es similar al incremental actual (0,65–0,74) y está por debajo del promedio existente (1,57); el 1,4 está por debajo del promedio existente. (c) Capacidad de larga vida. (d) Que la utilización del backlog avance. (e) Dos años de inversión por encima de 150.000 M sin crecimiento comparable. (f) Ver la tabla. **Juicio: defendible.** El riesgo principal es que el incremental baje a 0,65 y se quede ahí; está acotado en −6 % y la Conservadora (0,6/1,0) lo cubre. No exijo igualar margen × Ventas/Capital al ROIC contable (REGLAS §4C). Arrastre del capex no pagado (+26,8 mM) y arrendamientos aún no iniciados (164,9 mM): son reinversión futura. Los cubre el motor de Ventas/Capital y no se restan por separado, lo cual es correcto.

## 8. Costo del capital y riesgo

**Historia económica.** Amazon es un emisor AA con deuda en expansión: la deuda LP nominal pasó de 68.836 a 180.887 M en 9 meses, con emisiones en USD, EUR, CHF, CAD y GBP y un préstamo a plazo de 17.500 M. Su riesgo sistemático mezcla el de una minorista (beta desapalancada de Retail General 0,78) con el de la infraestructura de software. La hoja usa `Detailed` + `Multibusiness(US)` + ERP geográfica, como exige §4A. Verifiqué la identidad `Cost of capital worksheet!B14 = E63 = Input sheet!B36 = 8,7576 %` y que los pesos suman 100 %.

| Componente | Modelo | Fuente / comprobación del auditor | Juicio |
|---|---|---|---|
| Rf | 4,94 % | Treasury a 10 años del 30-oct-2026 = 4,94 % ✓ | Correcto |
| **Prima madura** | **4,55 %** (`Country equity risk premiums!B2`) | Damodaran **1-nov-2026** (`ERPNov26.xlsx`, T.Bond 4,94 %, el mismo Rf): T12m **3,79 %**, pago sostenible 4,41 %, normalizado 3,39 %. Damodaran 1-oct: T12m 3,70 % (= `corte_vigente.json`), pago sostenible 4,20 %. Maestra oficial: 3,70 % | **✗ A-01**: «rebase» que mezcla la ERP del 1-oct (columna distinta de la convención JMR) con la Rf del 30-oct |
| ERP inicial | 4,906 % = 4,55 % + 0,356 pp de exposición internacional | Ponderación por ingresos FY25 (Reino Unido, Japón, resto 1,8 pp como aproximación) | La mecánica geográfica es correcta |
| Beta desapalancada / reapalancada | 0,8082 / 0,8584 | Retail ×2 (0,781) + Computer Services (0,962) ponderados por EV/Ventas de la industria (2,11 y 1,48) | **B-03**: el mapeo de AWS es discutible |
| Ke | 9,151 % | Rf + 0,8584 × 4,906 % ✓ | — |
| Kd antes / después de impuestos | 5,34 % / 4,005 % | Rf + 40 pb (sintético, cobertura 23,3×); notas negociadas a valor razonable de 145,4 mM | Razonable |
| Pesos de mercado | E 92,36 % / D 7,64 % | D de mercado 215.026 (bono equivalente, duración 10, incluye arrendamientos) | Correcto en mecánica |
| WACC terminal | 9,49 % = Rf + prima madura (beta 1, sin deuda) | REGLAS §4 | Conforme a la regla; hereda A-01 |

Seis preguntas sobre la ERP. (a) 4,55 % (prima madura), 4,906 % (inicial), celda ERP!B2 / CoC!B27. (b) La ERP T12m de Damodaran de 2026 osciló entre 3,70 % y 4,77 %; 4,55 % no aparece en ninguna columna mensual de 2026 (ni en T12m ni en pago sostenible, que va de 4,14 % a 4,67 %). (c) No hay mecanismo de empresa: es un parámetro de mercado. (d) Para sostenerla, la ERP observada del corte tendría que ser 4,55 %. (e) Lo refuta el archivo de noviembre: 3,79 % en T12m (4,41 % en pago sostenible). (f) Recalculé el WACC y los diez factores con código propio (control: el caso base se reproduce con error 0):

| Alternativa (mismo resto Base) | WACC inicial / terminal | Valor por acción | Δ |
|---|---|---|---|
| R2 (rebase 4,55 %) | 8,76 % / 9,49 % | 148,68 | — |
| Damodaran nov-26, T12m 3,79 % (convención del corte JMR) | 8,16 % / 8,73 % | **178,15** | **+19,8 %** |
| Corte oficial vigente del repositorio (30-sep: Rf 5,29 %, ERP 3,70 %) | 8,41 % / 8,99 % | 166,54 | +12,0 % |
| Damodaran nov-26, pago sostenible 4,41 % | 8,65 % / 9,35 % | 153,46 | +3,2 % |
| Beta de AWS con Software (System & Application), βu 1,051 | 9,93 % / 9,49 % | 137,92 | −7,2 % |

**Doble conteo.** No encontré prima específica ni riesgo contado a la vez en la tasa y en los flujos. El riesgo de Disrupción está en su propia historia, no en la tasa. Los factores de descuento son compuestos y anuales, y la convergencia de los años 6–10 es lineal (`VO!H14:L14`), verificada.

**Beta: resolución de B-03 (v2).** La regresión de 60 meses (oct-21 a oct-26, retornos mensuales ajustados de AMZN contra SPY, Alpha Vantage) da **β = 1,491** (error estándar 0,212, R² 0,46, IC 95 % de 1,08 a 1,91; Blume 1,33; desapalancada equivalente 1,40). Bottom-up: R2 0,808 (AWS = Computer Services, pesos por EV/Ventas). Con pesos por EBIT del segmento × EV/EBIT de la industria: 0,863 si AWS es Computer Services y **1,054 si AWS es Software (System & Application)**. La plantilla, cambiando solo el selector `Cost of capital worksheet!G39` a Software, da 1,051. Damodaran prefiere la beta bottom-up, pero todas las mediciones independientes quedan por encima de 0,81; el IC de la regresión excluye 0,86. **Conclusión:** B-03 se confirma como sesgo **favorable al valor** en R2. Propuesta: AWS = Software (βu ≈ 1,05), con la regresión como cota alta. Efecto sobre el R3 central: −6,3 % (de 197,8 a 185,3).

## 9. Convergencia y valor terminal

**Historia económica.** A perpetuidad Amazon crece 4 % nominal en USD (por debajo de la Rf de 4,94 % ✓; WACC 9,49 % > g ✓), con un ROIC terminal de 12,5 % y reinversión g/ROIC = 32,0 % del NOPAT (79.482 de 248.381; verificado). El FCFF terminal (168.899) es **menor** que el del año 10 (185.309), porque el ROIC cae de 15,2 % a 12,5 % y se reinvierte más. El VP terminal es 1.302.283 M, **85,1 %** del VP operativo.

| Métrica | Histórico | Modelo | Referencia | Historia causal | Evidencia contraria | Impacto |
|---|---|---|---|---|---|---|
| ROIC terminal | 15,9 % LTM; 16,8 % con arrendamientos | 12,5 %, `Input!B50` | `reference/moat_2026-09-30.json`: AMZN «**ventaja durable**», industria ponderada 22 %, ROIC terminal registrado **16,5 %**; Retail (General) 13,6 % | Escala, Prime y costos de cambio en AWS | El retorno del capex de IA no está probado | 13,6 % (piso de la industria): **+3,1 %**; 15,2 % (= año 10): +6,8 %; 16,5 %: **+9,2 %**; 11 %: −5,2 % |
| g terminal | — | 4,0 % | Regla JMR (4 %, techo Rf) | — | — | ±0,5 pp: ver la matriz nativa (±5 %) |
| WACC terminal | — | 9,49 % | Regla: Rf + prima madura | — | Hereda A-01 | ±50 pb: **∓7,9 % / +9,5 %** |

Seis preguntas sobre el ROIC terminal. (a) 12,5 %, Input!B50. (b) Está por debajo de todos los ROIC observados desde FY23 (12,8 %–21,0 %) y por debajo del ROIC de la industria más baja aplicable (Retail General, 13,6 %). (c) La nota habla de «exceso modesto». (d) Para sostener 12,5 % la ventaja tendría que estar desvaneciéndose (punto medio entre WACC y la industria). (e) Lo contradice la referencia institucional, que declara ventaja durable. (f) +3 % a +9 %. **¿Por qué 12,5 % y no otro?** R2 no cita `moat_2026-09-30.json` ni justifica apartarse de la regla §4 («ventaja durable = promedio de la industria»). **Hallazgo B-02** (prudencia no sustentada; doble prudencia junto con A-01). Prueba de erosión del foso: con ROIC terminal = WACC el valor es 130,70 (dato de R2 que reproduje: −12,1 %). Esa es la Disrupción económica de la ventaja, y ya está acotada. **Nota v2 (I+D):** sobre capital ajustado por I+D, el 12,5 % GAAP equivale a un ROIC terminal de **11,3 %**, y el ROIC actual ajustado es 13,7 %–14,6 %, no 15,9 %. La referencia de foso (16,5 %, GAAP con arrendamientos) no es comparable con una base ajustada. Por eso el R3 propone **13,6 %** (piso de la industria Retail, GAAP), no 16,5 %.

## 10. Validación independiente del valor intrínseco

Reproduje el DCF por completo con código propio (`auditoria_fase4/scripts/dcf.py`), a partir de las entradas de la captura y no de las salidas:

| Partida (Base) | Hoja | Auditor | Diferencia |
|---|---|---|---|
| VP FCFF años 1–10 | 227.255,95 | 227.255,95 | 0 |
| VP terminal | 1.302.283,17 | 1.302.283,17 | 0 |
| Valor operativo | 1.529.539,13 | 1.529.539,13 | 0 |
| − Deuda + Caja + No operativos | −304.461 + 114.226 + 294.595 | idem | 0 |
| − Opciones / RSU | 26.560,77 | 26.560,77 (K = 0: artefacto, C-01) | 0 |
| Patrimonio / acciones | 1.607.338 / 10.811 | idem | — |
| **Valor por acción** | **148,6762** | **148,6762** | **−2,8e-14** |
| Conservadora / Optimista / Disrupción | 91,93 / 225,33 / 59,98 | idem | < 1e-13 |
| MOS 35 % sobre Base | 96,64 | 148,676 × 0,65 = 96,64 ✓ | — |

**Puente EV→patrimonio.** Hay dos defectos. **A-02:** el pasivo de arrendamientos operativos (100.288) se resta como deuda y entra a la deuda del WACC, pero el EBIT GAAP de EE. UU. ya descuenta el costo completo del arrendamiento operativo (16.070 M en LTM), sin convertidor (`B18 = No`). Con ASC 842, a diferencia de NIIF 16, el gasto operativo de arrendamiento sigue dentro del EBIT, así que restar el pasivo cuenta dos veces la misma obligación. Ajuste de Damodaran con datos del 10-Q (vida remanente 9,9 años, tasa 4,0 %): EBIT + 16.070 − depreciación del derecho de uso (100.288 / 9,9 = 10.130) = **+5.940 M (+0,745 pp de margen)**, manteniendo el pasivo como deuda → **158,56 (+6,6 %)**. Excluir el pasivo de la deuda da 157,95 (+6,2 %). **B-01 (resuelto v2):** los no operativos (294.595) se suman a valor razonable bruto. Impuesto diferido observado de las notas de Anthropic: **34.608 M** (AOCI). Base fiscal de las notas restantes: 146,2 − 140,3 (ganancia no realizada) = **5,9 mM**; por tanto, la base de las preferentes es 8,0 − 5,9 = 2,1 mM de notas convertidas más 5,0 mM de la Serie G y 5,0 mM de la Serie H compradas en efectivo en el T2-26, es decir **12,1 mM** [CÁLCULO a partir del 10-Q nota 2; corregido en v2.1]. A la tasa implícita de 24,67 % (34.608 / 140.300), el impuesto diferido de las preferentes es 19.832 M y el **total 54.440 M → 143,64 (−3,4 %)**. Los warrants (4,3 mM, base no publicada) quedan como límite adicional menor a 1,1 mM.

**I+D: resolución de B-04 (v2).** Amazon no publica la I+D, pero sí «Technology and infrastructure» (10-K FY2015–FY2025: 12.540 … 108.521; LTM 126.938) y la D&A de PP&E por segmento (FY2018–9M26). Estimé la I+D como T&I − D&A de PP&E (cota prudente, 72.980 M en LTM) o T&I − D&A de AWS (cota alta, 95.787 M), sin restar arriendos ni energía [INFERENCIA]. Con vida de 2 a 3 años, el activo de investigación va de 106.310 a 178.909 M y el ROIC ajustado de 13,7 % a 14,6 %. **Prueba de neutralidad:** si se capitaliza de forma consistente (EBIT + I+D − amortización, y la reinversión sube en el mismo neto), el FCFF de los diez años y el terminal **no cambian**: 168.899 en ambos casos, verificado. El valor solo cambia si, además, se reinterpreta el ROIC terminal sobre la base ajustada: aplicar 12,5 % sobre ella sumaría +4,6 %, pero eso es otro supuesto económico, no un efecto del método. **Conclusión:** B-04 queda **acotado e inmaterial para el valor** si se hace de forma consistente, y se reclasifica como C-10. Su efecto real es informativo: el ROIC GAAP de 15,9 % sobrestima el retorno económico, lo que modera B-02.

**Horizontes.** El DCF de hoy (148,68) no se confunde con el valor llevado al año 3 (193,34 = valor × (1 + Ke)³ en `Origen de los Supuestos`, que es solo la referencia del ponderado). El ponderado es 100 % DCF porque los múltiplos tienen peso 0.

**DCF inverso.** Para justificar 240,35 con el resto de la Base, el TACC a 5 años implícito es 28,4 % (JSON de R2; lo reproduje). Por margen, el inverso propio da un margen objetivo implícito de **25,8 %** (21,4 % tras corregir A-01 y A-02). Ninguna de las cuatro historias de R2 llega a ese nivel.

## 11. Cuatro historias y probabilidades

| Historia | Crecimiento (TACC 1–5) | Margen EBIT año 10 | Ventas/Capital 1–5 / 6–10 · ROIC terminal | WACC / Ke | g · retorno terminal | Valor por acción | Probabilidad | Qué la confirma / refuta |
|---|---|---|---|---|---|---|---|---|
| Base | 11,73 % | 17 % | 0,75 / 1,4 · 12,5 % | 8,76 % → 9,49 % | 4 % · 12,5 % | 148,68 | 45 % | AWS entre 25 % y 35 %, margen de AWS ≥ 30 % |
| Conservadora | 7,11 % | 14 % | 0,6 / 1,0 · 10,5 % | idem | 4 % · 10,5 % | 91,93 | 22,5 % | AWS < 25 %, margen estancado en 14 % |
| Optimista | 14,27 % | 20 % | 0,95 / 1,7 · 15 % | idem | 4 % · 15 % | 225,33 | 22,5 % | AWS ≥ 35 % durante 4 trimestres |
| **Promedio de 3** (denominador 0,90) | — | — | — | — | — | **153,65** ✓ | — | — |

Las probabilidades son la previa de «crecimiento maduro» (45/22,5/22,5/10), sin ajustes (`ajustes_prob = []`). `probabilidades.py`: 0 fallos. La etapa es razonable: crecimiento de dos dígitos bajos, ROIC por encima del WACC y reinversión alta. El orden de márgenes y crecimientos es Conservadora ≤ Base ≤ Optimista ✓, y el Optimista no supera la Base en más de 10 pp ✓. La Conservadora y la Optimista son casi simétricas en margen (±3 pp) y en ROIC (±2–2,5 pp), lo que cumple la calibración honesta.

### «¿Qué pasaría si todo fallara?»

**Disrupción (10 %, 59,98 USD):** capacidad ociosa y comercialización de la nube. Crecimiento de 5 % a 2 %, margen de 10 %, Ventas/Capital 0,45/0,65, ROIC terminal = WACC (9,49 %) y g = 2 %. Queda fuera del promedio, como corresponde. Como referencia, el valor esperado de las cuatro historias (con Disrupción incluida, etiquetado aparte) es 0,45 × 148,68 + 0,225 × 91,93 + 0,225 × 225,33 + 0,1 × 59,98 = **144,28**. R2 reconoce que su motor no impone gasto contractual fijo: el estrés con reinversión mínima de 160.000 M por año en los años 1–3 da 40,76 según su propio diagnóstico, que no reproduje.

## 12. Valoración por múltiplos: prueba independiente y secundaria

**Integridad de cálculo (§5A).** `diff_formulas_plantilla.py` da 0 fórmulas sustituidas, de modo que la mecánica original se conserva. Pero **ningún método tiene ancla**: la fila 19 de las cinco pestañas (múltiplo histórico por cierre fiscal) vale 0 en los cuatro cierres. Esos son **ceros precargados, no evidencia**: las capitalizaciones y EV de cada cierre no se diligenciaron, y `Financials Multiples` tiene 0 entradas. El resultado son **15 celdas `#NUM!`** (B39:B41 de las cinco pestañas, según `integridad_hojas.py`) y la sección 5 de `Origen de los Supuestos` con `#NUM!`. Las métricas FY+1/2/3 sí se calculan con las fórmulas de la plantilla.

| Método | Denominador FY+3 Base (hoja) | A histórico | B pares | C fundamental | Observado al corte [CÁLCULO del auditor] | Estado R2 | Juicio del auditor |
|---|---|---|---|---|---|---|---|
| EV/EBITDA | 265.178 | N/D (ceros) | N/D | N/D | EV operativo 2.494.064 / EBITDA LTM 183.719 = **13,6×** | PENDIENTE_ANCLA, peso 0 | Aplicable; falta ancla; **sin matriz 5×5** |
| EV/FCFF | −34.076 | — | — | — | FCFF LTM negativo | N/A | ✓ N/A justificado (denominador negativo) |
| P/E | 136.889 | N/D | N/D | N/D | 19,3× LTM, distorsionado por 68 mM de ganancias de Anthropic | PENDIENTE_ANCLA y normalización | Aplicable con utilidad normalizada; sin matriz |
| P/FCFE | −7.201 | — | — | — | — | N/A | ✓ N/A (denominador negativo en la Base) |
| P/OCF | 131.185 | N/D | N/D | N/D | 2.598.424 / 168.300 = 15,4× | PENDIENTE_ANCLA y capital de trabajo | Aplicable; sin matriz |
| P/S (PV) | — | — | — | — | 3,3× | Complementario, no usado | ✓ No bloquea (§5A) |
| P/BV (PBV) | — | — | — | — | 4,2× | Complementario, no usado | ✓ No bloquea |

**Contraste útil.** El valor operativo de la Base DCF (1.529.539) equivale a **8,3×** el EBITDA LTM, frente a 13,6× observado en el mercado. Es otra forma de ver la brecha. No calibro nada para cerrarla: el ancla C no debe ajustarse al DCF ni al precio. El repositorio tiene una serie de múltiplos históricos de una revisión anterior (`JMR-valuation/reference/historical_multiples/AMZN.json`, 12-oct-2026, otra hoja). R2 no puede heredarla sin verificar, pero eso desmiente que «faltan series»: el dato existe y debe reverificarse contra los cierres de la SEC. **Hallazgo C-02:** el valor principal no cambia (peso 0), pero el entregable mínimo §8 y la puerta de publicación siguen pendientes. Faltan las matrices de EV/EBITDA, P/E y P/OCF. No hay ajuste por tasas ni descuentos generales que auditar, porque no hay múltiplos.

**Resolución de C-02 (v2).** La **causa raíz** es que `Trailing Valuation!B3:K3` (precio de la acción en cada cierre fiscal) está vacía; de esa fila dependen la capitalización, el EV y todos los múltiplos históricos (`Trailing Valuation!5–24` → fila 19 de cada pestaña → B39:B41). Es un dato crudo de fase 1 que falta, no un problema de método. Lo reconstruí con los cierres de diciembre (Alpha Vantage, ajustados por el split 20:1), las acciones de `Income Statement!27`, y la deuda, la caja y las inversiones de `Balance Sheet`. El EV excluye los no operativos y el P/E usa utilidad operativa normalizada, sin Anthropic ni Rivian. Ajuste por tasas con `costo_capital_historico.json` y k del corte de nov-26 (8,73 %):

| Método | Cierres FY22 / FY23 / FY24 / FY25 (sin ajuste) | Ancla A ajustada: mediana / mínimo | Observado hoy | Ancla C (justificado DCF): R2 / R3 | VP por acción con A (mediana / mínimo) | Lectura |
|---|---|---|---|---|---|---|
| EV/EBITDA | 17,2 / 19,0 / 19,4 / 16,9 | 19,1 / 15,8 | 13,6 | **8,1 / 10,6** | 371,9 / 308,7 | A muy por encima de C → **tope en C** (= DCF); el EBITDA futuro está inflado por la D&A del capex de IA |
| P/OCF | 18,4 / 18,6 / 20,1 / 17,8 | 19,2 / 16,6 | 15,4 | 16,9 / **21,5** | **180,5 / 155,3** | Con R3, A < C: método aplicable (en R2, A ≈ C) |
| P/E operativo | 100,2 / 54,5 / 41,5 / 38,2 | 47,4 / 35,6 | 31,4 | 16,2 / 20,6 | 467,7 / 351,1 | A muy por encima de C → **tope en C** |

Con las tasas de R2 (k 9,49 %), las medianas ajustadas son 16,4 / 16,6 / 40,8 y P/OCF da 152,5. Las matrices 5×5 (múltiplo real × denominador FY+3 real; centro en la mediana ajustada; VP por acción descontado con Ke) están en `auditoria_fase4/resolucion_R3.json`. **Son una propuesta del auditor, no salidas nativas:** la hoja debe calcularlas tras diligenciar `Trailing Valuation!B3:K3` y `Entradas históricas auxiliares!B4:K5` (= 0). La plantilla **no resta** las inversiones de largo plazo en el EV histórico; en FY25 eso infla el EV/EBITDA cerca de 0,45×, y debe declararse. Conclusión: aplicando el tope C de REGLAS §5, los múltiplos no contradicen el DCF; solo P/OCF aporta una lectura independiente (155–181 con tasas del corte).

## 13. Sensibilidades económicas y escenarios alternativos

**Matrices DCF Base nativas** (`Sensibilidad DCF`; las 75 celdas reproducidas con código propio, error máximo 8,5e-14):

| Matriz | Eje filas × columnas | Centro | Rango |
|---|---|---|---|
| A | WACC inicial **en paralelo con el terminal** (7,76 %–9,76 %) × g (3 %–5 %) | 148,68 ✓ | 114,43–219,00 |
| B | ROIC terminal (11,5 %–13,5 %) × g | 148,68 ✓ | 136,68–167,95 |
| C | TACC 1–5 (7,7 %–15,7 %) × margen objetivo (13 %–21 %) | 148,68 ✓ | 103,31–216,94 |

La matriz A es un desplazamiento paralelo y no «WACC terminal × g» como pide §8. R2 corrigió el rótulo y añadió en el JSON una matriz diagnóstica de WACC terminal ±1 pp (C-05, menor). La **DCF inversa** frente al precio fechado del 30-oct da un TACC implícito de 28,4 % o un margen implícito de 25,8 %. **Familia de múltiplos:** **no desplegada** (C-02). La pestaña `Sensibilidad por múltiplo` solo tiene encabezados, de modo que no hay matriz editorial que aceptar ni rechazar.

**Pruebas propias ejecutadas** (todas recalculan diez años más el terminal; mismo corte):

| Prueba | Valor | Δ |
|---|---|---|
| ERP nov-26 T12m (A-01) | 178,15 | +19,8 % |
| Corte oficial vigente (A-01) | 166,54 | +12,0 % |
| Arrendamientos fuera de deuda / EBIT ajustado (A-02) | 157,95 / 157,59 | +6,2 % / +6,0 % |
| Impuesto diferido observado / estimado (B-01) | 145,48 / 143,37 | −2,2 % / −3,6 % |
| No operativos −20 % / −50 % (B-05) | 143,23 / 135,05 | −3,7 % / −9,2 % |
| ROIC terminal 13,6 % / 16,5 % (B-02) | 153,22 / 162,42 | +3,1 % / +9,2 % |
| Beta de AWS = Software (B-03) | 137,92 | −7,2 % |
| RSU por método del tesoro / a precio de mercado (C-01) | 148,07 / 146,17 | −0,4 % / −1,7 % |
| **Favorable conjunto** A-01 (T12m) + A-02 | 187,43 | +26,1 % |
| **Neto** A-01 (T12m) + A-02 + B-01 máximo + RSU a mercado | **179,61** | **+20,8 %** |
| Neto con ERP de pago sostenible de nov (4,41 %) | 154,92 | +4,2 % |
| **Adverso conjunto** B-01 máximo + RSU a mercado + B-03 | 130,10 | −12,5 % |

**Pruebas añadidas en v2** (`auditoria_fase4/resolucion_R3.json`; RSU a precio de mercado en los paquetes):

| Prueba | Valor | Δ |
|---|---|---|
| Arrendamientos con ajuste de Damodaran (vida 9,9 años) | 158,56 | +6,6 % |
| Impuesto diferido total resuelto (54.440) | 143,64 | −3,4 % |
| Impuesto de caja 15 % → 25 % / 10 % → 25 % (B-06) | 154,98 / 159,18 | +4,2 % / +7,1 % |
| Margen de partida 14,1 % (C-09) | 151,60 | +2,0 % |
| Ventas/Capital 1,0 en los años 4–5 | 153,67 | +3,4 % |
| I+D capitalizada de forma consistente (B-04) | 148,68 | 0,0 % |
| Paquete 1: errores (A-01 T12m, A-02 Damodaran, B-01, RSU a mercado) | 181,86 | +22,3 % |
| Paquete 2: + B-06 (15 %) + C-09 | 191,90 | +29,1 % |
| Paquete 3: + ROIC terminal 13,6 % (B-02) | 197,79 | +33,0 % |
| **R3 central propuesto: paquete 3 + beta AWS = Software (βu 1,054)** | **185,32** | **+24,6 %** (MOS 120,5) |
| R3 central con beta de regresión (βu 1,40) | 169,03 | +13,7 % |
| R3 central con ERP de pago sostenible (4,41 %) | 170,84 | +14,9 % |

Margen terminal que exige el precio de 240,35 con el R3 central: **22,4 %**.

Son simulaciones realmente ejecutadas (`auditoria_fase4/alternativas*.json`, `resolucion_R3.json`), no impactos direccionales.

## 14. Coherencia de hojas, cálculos y presentación

| Control | Resultado real | Lectura |
|---|---|---|
| `diff_formulas_plantilla.py --sheet-id R2` (oficial) | **0 reemplazos** declarados y no declarados; 0 pestañas añadidas o faltantes | ✓ Formato unificado (46 pestañas) |
| `candados.py` (oficial, hoja redirigida a R2) | **15/15 candados listos** | ✓ |
| `inputs_completos.py` (oficial, redirigido) | **0** entradas esenciales vacías | ✓ |
| `estados_completos.py` (oficial, redirigido) | **2 hallazgos**: `Cash Flow Statement!38–39` (FCF apalancado y no apalancado) vacías G:L | C-06, filas de memoria |
| `integridad_hojas.py` (oficial, redirigido) | **19 hallazgos**: 15 `#NUM!` en múltiplos (C-02) + 4 «pestaña frente a motor legado» (H5–H8 frente a 233,85/159,45/66,16/299,13 de la ficha legada `reference/damodaran/AMZN.json`) | Los 4 últimos son falsos positivos para un candidato no promovido (D-01) |
| `controles_supuestos.py` | Oficial (ficha legada): 2 alertas S1. Con los datos de R2 (prueba equivalente): **1 alerta S1** (Optimista 20 % > 2,5 × 6,8 %) | **Falso positivo**: el script busca el foso con `tk.rstrip("N")` → «AMZ» y no encuentra la «ventaja durable» de AMZN (D-01) |
| `probabilidades.py` (oficial) | **0 fallos** (45/22,5/22,5/10) | ✓ |
| Valores JSON ↔ hoja | Valor principal, MOS, promedio y cuatro historias idénticos | ✓ |
| `Origen de los Supuestos` ↔ supuestos efectivos | El texto dice que la Base sale de `Input!B27–B33` (11,23 %, Ventas/Capital 2,73, referencia de margen 9,94 %); el DCF usa `Escenarios e historias` (13,9 %, 0,75/1,4, 17 %) | C-03, presentación |
| Ubicación de la hoja | En `Revisiones sustituidas — archivo histórico hasta 24-oct-2026/AMZN`; no existe `Análisis/AMZN` | C-04, contra REGLAS §10–§11 |
| MOS / promedio / Disrupción | MOS sobre la Base ✓; promedio de 3 ✓; Disrupción aislada ✓ | ✓ |
| Nivel 1 / Nivel 2 | N1: 14 capítulos en orden canónico, 8.798 palabras, mínimo 546 por capítulo (≥ 330) ✓; capítulo 5 de ciclos con Damodaran y Marks ✓. N2: 12 apartados ✓ | Estructura conforme |
| Completitud semántica N1 | **No nombra a Anthropic ni a OpenAI**, que son 294,6 mM (cerca de 27 USD por acción, 18 % del valor Base), fuente principal del resultado neto y contrapartes de más de 200 mM de compromisos con AWS. Tampoco cuantifica su impuesto diferido | C-08 (editorial, Medio) |

Artefactos examinados: hoja (captura completa), JSON, N1, N2, CONTROLES_FASE3.json y metadatos del HTML. No examiné el visor de la app porque R2 no está publicada.

## 15. Hallazgos priorizados y propuestas de corrección

`V_base` = 148,68 USD. Impacto según REGLAS §4B: `100 × |V_alt − V_base| / V_base`.

| ID | Severidad | Tipo | Evidencia | Impacto | Mantener / ajustar / investigar | Propuesta y alternativa | Requiere aprobación | Estado |
|---|---|---|---|---|---|---|---|---|
| **A-01** | **Crítico** | Dato / tasa | `ERP!B2 = 4,55 %` «[JUICIO REBASE]»: ERP de pago ajustado del 1-oct + Δ Rf; `ERPNov26.xlsx` (Rf 4,94 %) da T12m 3,79 %; el corte oficial usa la columna T12m (oct 3,70 %) | **+12,0 % a +19,8 %** (+3,2 % si se elige pago sostenible de nov); cruza §4B; no cambia la relación precio/valor | Ajustar | Usar Rf y prima madura de la **misma fecha y la misma columna** que el corte JMR: Damodaran 1-nov-26 (3,79 %) con Rf 4,94 %, o el corte oficial 30-sep (5,29 % / 3,70 %). Si se prefiere otra columna (pago sostenible), cambiarla en REGLAS para todas las empresas, no por revisión | Sí (usuario) | Abierto · **bloqueante** |
| **A-02** | **Alto** | Fórmula / puente (doble conteo) | Arrendamientos operativos 100.288 en `Input!B16` y en la deuda del WACC; EBIT GAAP de EE. UU. después de la renta; `B18 = No`; convertidor vacío | **+6,2 % a +6,6 %** | Ajustar | Una de dos: (a) `B18 = Yes` con el convertidor (EBIT + gasto de arrendamiento − depreciación del derecho de uso), manteniendo el pasivo como deuda; o (b) excluir de la deuda los 100.288 operativos (y de la deuda de mercado del WACC), conservando financieros y obligaciones de financiamiento | Sí | Abierto · **bloqueante** |
| **B-01** | Alto | Puente / impuestos | Impuesto diferido AFS 34.608 (10-Q, AOCI); base de las preferentes 12,1 mM (= 8,0 − 5,9 + 5,0 Serie G + 5,0 Serie H) → impuesto diferido 19.832; total 54.440 | **−3,4 %** (resuelto) | Ajustar | `Input!B84` (valor económico) = 294.595 − 54.440 = **240.155**; `B83` (contable) sin cambio | Sí | Reserva resuelta con cifra |
| **B-02** | Alto | Supuesto | ROIC terminal 12,5 % frente a «ventaja durable» con referencia 16,5 % (`moat_2026-09-30.json`) y piso de la industria Retail 13,6 % | **+3,1 % a +9,2 %** | Investigar / justificar | Justificar el desvanecimiento de la ventaja con evidencia, o subir a 13,6 %–16,5 % según la regla §4 | Sí | Reserva material |
| **B-03** | **Alto** | Supuesto (beta) | Regresión de 60 meses β = 1,49 (EE 0,21; IC 1,08–1,91) frente a bottom-up 0,86; con AWS = Software, βu 1,05 | **−6,3 %** sobre el R3 central (−7,2 % sobre R2); −14,6 % con la regresión | Ajustar | `Cost of capital worksheet!G39` = «Software (System & Application)»; documentar la regresión como contraste | Sí | Reserva material, sesgo favorable al valor |
| C-10 (antes B-04) | Bajo | Método | I+D estimada 73–96 mM; activo 106–179 mM; ROIC ajustado 13,7 %–14,6 % | **0 %** con capitalización consistente (FCFF idéntico, verificado) | Mantener `B17 = No` o capitalizar de forma consistente | Si se capitaliza: R& D converter con la serie T&I − D&A de PP&E (`auditoria_fase4/resolucion_R3.json`) **y** reinversión ajustada; no reexpresar márgenes sin reinversión | No | Resuelto (no bloqueante) |
| **B-06** | Medio | Supuesto (impuestos) | Caja 6.814 M frente a EBIT 104.366 (≈ 6,5 %); diferido LTM 36.344; 10-K: la ley de 2025 reduce el impuesto en caja en 2025–2026 | **+4,2 %** (15 %) a +7,1 % (10 %) | Ajustar | `Input!B90` = 0,15 (normalizada de caja), convergiendo a 25 % en el año 10 (mecánica nativa) | Sí | Reserva material, sesgo prudente |
| **B-05** | Medio | Dato (Nivel 3) | Valor razonable de participaciones privadas por transacciones observables y descuento por falta de liquidez; no cotizadas | −3,7 % (−20 %) / −9,2 % (−50 %); efecto también al alza no acotado | Mantener con sensibilidad | Conservar el importe reportado; registrar fecha de la última ronda; sensibilidad simétrica | No | Reserva cuantificada |
| C-01 | Bajo | Fórmula de plantilla | `Option value`: K = 0 → `ln(S/0)` → IFERROR → d1 = 0, N(d1) = 0,5 → 118,95 por RSU en lugar de ~237,9 | −0,4 % (tesoro) / −1,7 % (mercado) | Ajustar por vía de mantenimiento | Corregir la plantilla (rama K = 0 → valor = S ajustado), con respaldo y regresión; sin editar R2 | Sí (mantenimiento) | No bloqueante |
| C-02 | Medio | Dato faltante (fase 1) | Causa raíz: `Trailing Valuation!B3:K3` vacía → EV histórico vacío → ceros en la fila 19 y 15 `#NUM!` | 0 % en el valor principal (peso 0) | Completar | Diligenciar B3:K3 = 37,49; 58,47; 75,10; 92,39; 162,85; 166,72; 84,00; 151,94; 219,39; 230,82 (cierres de dic-16 a dic-25, base post-split) y `Entradas históricas auxiliares!B4:K5` = 0; generar matrices nativas; declarar que el EV no resta inversiones de largo plazo | No | Resuelto en propuesta; matrices nativas pendientes |
| C-09 | Bajo | Supuesto | Año 1 = margen LTM 13,09 %, contra una tendencia trimestral de ~14,1 % | +2,0 % | Ajustar | `Input!B28` = 0,141 (+0,745 pp si se aplica el convertidor de arrendamientos) | Sí | No bloqueante (≈ 2 %) |
| C-03 | Bajo | Presentación | `Origen de los Supuestos` e `Input!B27–B33` no reflejan la Base efectiva | 0 % | Ajustar texto | Aclarar en la nota que la Base la gobierna `Escenarios e historias` | No | No bloqueante |
| C-04 | Medio | Gobierno | Hoja en una carpeta de archivo histórico | 0 % | Ajustar | Crear `Análisis/AMZN` y mover la hoja conservando su ID (REGLAS §11) | Sí (usuario) | Previo a promover |
| C-05 | Bajo | Presentación | Matriz A en paralelo, no «WACC terminal × g» | 0 % | Mantener | Promover a nativa la matriz diagnóstica de WACC terminal del JSON | No | No bloqueante |
| C-06 | Bajo | Dato | `CFS!38–39` vacías | 0 % | Completar | Rellenar o declarar una excepción | No | No bloqueante |
| C-07 | Bajo | Dato | Deuda CP 380 omitida; duración de 10 años agregada | 0,02 % | Mantener | Documentar | No | No bloqueante |
| C-08 | Medio | Editorial (§9) | N1 sin Anthropic ni OpenAI; sin cuantificar el impuesto diferido ni la concentración del backlog | 0 % en el valor | Completar | Añadir un subcapítulo de participadas de IA, doble relación cliente-participada y riesgo de concentración | No | **Atendido en fase 3 (2-nov-2026, misma sesión): N1 2B/8/11/12/13/14 y tabla N2.4.** No auditado: requiere revisión independiente |
| D-01 | — | Herramienta | `controles_supuestos.py`: `rstrip("N")` convertía AMZN en «AMZ»; `integridad_hojas.py` compara con la ficha legada | No aplica a la valoración | **Corregido** | Función `foso()`: ticker exacto primero; pruebas nuevas (3/3). Repo JMR-valuation, commit `667de1c`. AMZN da 0 hallazgos. `integridad_hojas` para candidatos queda pendiente | No | **Resuelto** (script) |
| D-02 | — | Observación | WACC terminal = Ke con beta 1 sin deuda (9,49 %), conforme a REGLAS §4 | — | Mantener | Si se quisiera un WACC maduro con deuda, sería un cambio de regla global | — | No aplica |

**Separación.** Datos o fórmulas con error: A-01 (fuente y fecha de la tasa), A-02 (doble conteo), B-01 (puente fiscal, ya cuantificado) y C-02 (dato faltante). Hipótesis discutibles: B-02, B-03, B-05, B-06 y C-09. B-04 queda resuelto como C-10. **No se modificó R2.**

### Resolución cuantificada: R3 propuesto, celda por celda (v2)

Son propuestas para una fase 2 nueva en **copia limpia** (`AMZN-<fecha>-A12-R3`). Las cifras salen del replicador del auditor y no son oficiales hasta que las calcule la hoja.

| # | Celda (R3) | R2 | Propuesto | Hallazgo | Efecto incremental |
|---|---|---|---|---|---|
| 1 | `Country equity risk premiums!B2` / `Cost of capital worksheet!B27` | 4,55 % / 4,906 % | **3,79 % / 4,146 %** (Damodaran 1-nov-26 T12m + 0,356 pp geográficos) | A-01 | +19,8 % |
| 2 | `Input!B18` + `Operating lease converter` + `Input!B78` | No / vacío / 0 | Yes; gasto actual 16.070; compromisos del 10-Q nota 4 (T4-26 5.320; 2027 15.889; 2028 14.938; 2029 13.760; 2030 12.213; después 59.372); B78 = PV del convertidor (solapamiento con B16) | A-02 | +6,6 % |
| 3 | `Input!B84` (y B20) | 294.595 | **240.155** (neto de impuesto diferido) | B-01 | −3,4 % |
| 4 | `Option value!B6` | 0 (artefacto de K = 0) | Corregir la rama K = 0 en la maestra (mantenimiento), o strike técnico 0,01 USD declarado como excepción | C-01 | −1,7 % |
| 5 | `Input!B90` | 22,5 % | **15 %** (convergencia nativa a 25 %) | B-06 | +4,2 % |
| 6 | `Input!B28` | 13,09 % | **14,1 %** (+0,745 pp si se aplica la fila 2; idem en `Escenarios e historias!D5:D8`) | C-09 | +2,0 % |
| 7 | `Input!B50` / `Escenarios e historias!G5` | 12,5 % | **13,6 %** | B-02 | +3,1 % |
| 8 | `Cost of capital worksheet!G39` | Computer Services | **Software (System & Application)** | B-03 | −6,3 % |
| 9 | `Trailing Valuation!B3:K3`, `Entradas históricas auxiliares!B4:K5` | vacías | Cierres de diciembre y ceros (ver C-02) | C-02 | 0 % (múltiplos) |
| | **R3 central** | **148,68** | **185,32** (MOS 120,46) · rango 169,0 (beta de regresión) – 197,8 (beta de R2) | | **+24,6 %** |

Fuera del alcance del auditor (requieren al usuario o permisos): mover la hoja a `Análisis/AMZN` (C-04), crear la hoja de auditoría en Drive (REGLAS §11), el mantenimiento de la rama K = 0 de la maestra (C-01) y el texto de Anthropic/OpenAI en el Nivel 1 (C-08; lo redacta la fase 3, no la auditoría).

## 16. Catalizadores, señales de refutación y seguimiento

| Métrica | Nivel observado (fecha) | Señal favorable | Señal adversa | Fuente | Frecuencia |
|---|---|---|---|---|---|
| Crecimiento de AWS | +39,3 % interanual (T3-26) | ≥ 30 % durante 4 trimestres | < 25 % durante 2 trimestres | 10-Q, segmentos | Trimestral |
| Margen operativo de AWS | 38,7 % (T3-26) | ≥ 32 % con D&A creciente | < 28 % | 10-Q | Trimestral |
| Margen EBIT consolidado | 13,09 % LTM; 13,9 % T3 | Camino ≥ 14,5 % LTM en FY27 | Estancado < 13 % | 10-Q | Trimestral |
| Capex frente a guía | 9M26: 175.670 M; guía FY26 ~220.000 M | FY27 sin aumento mayor al de las ventas de AWS | Capex FY27 > 1,4 × el incremental de ventas | 8-K / 10-K | Trimestral |
| FCF reportado | −42.357 M LTM | Vuelve a ser positivo en FY27 | Negativo con AWS < 25 % | Flujo de caja | Trimestral |
| Backlog de AWS | 578 mM, vida media 6,1 años (sep-26) | Crece más rápido que los ingresos de AWS | Cae, o hay renegociaciones de OpenAI o Anthropic | 10-Q, obligaciones de desempeño | Trimestral |
| Participaciones privadas | 294,6 mM brutos; impuesto diferido 34,6 mM | Rondas o IPO a precios superiores | Deterioro o falta de liquidez | 10-Q nota 2 | Trimestral |
| ERP de Damodaran | 1-nov-26: T12m 3,79 % / pago sostenible 4,41 % | — | — | `ERPNov26.xlsx` | Mensual |

Los umbrales son criterios del auditor, no guías oficiales. La fecha de los resultados del T4 2026 **no está confirmada** y no se cita.

## 17. Dictamen económico y resumen para escuchar

**Tesis: Plausible con reservas.**

- **Consistencia matemática: conforme.** Los cuatro DCF, el puente, el MOS, el promedio y las tres matrices nativas se reproducen con error inferior a 1e-13. Las fórmulas están intactas (0 sustituciones) y hay 15/15 candados.
- **Trazabilidad documental: conforme con reservas.** Hay 71/71 entradas con nota de fuente, y el LTM, el balance y la serie de diez años están verificados contra la SEC. Pero la prima madura no corresponde al corte (A-01) y el impuesto diferido de las participaciones está omitido (B-01).
- **Razonabilidad económica: con reservas materiales.** El crecimiento (13,9 % → 4 %) y el margen (17 %) son medianas defendibles. La tasa (A-01), el doble conteo de arrendamientos (A-02) y el ROIC terminal (B-02) acumulan prudencia no sustentada. El beta (B-03) y las participaciones brutas (B-01) empujan en sentido contrario.

**Dictamen: PENDIENTE** (sin cambio en v2). A-01 es un defecto de fuente crítica en la tasa (REGLAS §4 y §4B) y A-02 un doble conteo en el puente de deuda; los dos son errores de R2 que solo se corrigen en una revisión nueva. B-04 quedó resuelto (C-10, inmaterial con tratamiento consistente). B-03 y B-06 son reservas materiales de signo opuesto. **R3 central propuesto: 185,3 USD** (rango 169–198), +24,6 % sobre la Base R2. No cruza la relación precio/valor: 240,35 sigue por encima de todos los casos y exige un margen terminal de 22,4 %. Supuesto más frágil: el margen terminal combinado con la tasa. Más defendible: el crecimiento del año 1. Motor principal del precio: el margen de la mezcla AWS/publicidad. **Decisión analítica sugerida:** fase 2 nueva (`AMZN-…-R3`) con la tabla celda por celda de §15, y luego fase 3 y una auditoría en otra sesión. **No se modificó la valoración.**

**Resumen oral:** Auditamos la valoración candidata de Amazon, revisión R2. La aritmética es impecable: reproducimos el valor Base de ciento cuarenta y ocho dólares sin diferencias. El crecimiento y el margen son razonables. Pero la tasa de descuento usa una prima de riesgo que no es la del corte, los arrendamientos se cuentan dos veces y el impuesto supuesto es muy superior al que Amazon paga en caja. En sentido contrario, la beta es demasiado baja frente a la de mercado y las participaciones en Anthropic se suman sin su impuesto diferido. La investigación y desarrollo, capitalizada de forma consistente, no cambia el valor. Corregido todo, proponemos una Base cercana a ciento ochenta y cinco dólares, todavía por debajo del precio de doscientos cuarenta. Dictamen: pendiente, con revisión R3 recomendada.

## 18. Fuentes primarias, limitaciones y registro de versión

**Fuentes** (consultadas el 2-nov-2026):

1. Amazon.com, Inc., Form 10-Q, trimestre al 30-sep-2026, presentado el 30-oct-2026. https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm. Respalda balance, segmentos, notas 2 (inversiones en Anthropic y OpenAI, impuesto diferido AFS), 3 (arrendamientos), 4 (compromisos), 5 (deuda), obligaciones de desempeño y guía del T4. SHA-256 `4860db2d…`.
2. SEC XBRL companyfacts CIK 0001018724. https://data.sec.gov/api/xbrl/companyfacts/CIK0001018724.json. Respalda ingresos, EBIT, capex, D&A, SBC, arrendamientos y acciones FY2016–9M2026. SHA-256 `acddb7c0…`.
3. Amazon, Form 8-K del 29-oct-2026 (2.02/9.01). https://www.sec.gov/Archives/edgar/data/1018724/000101872426000038/amzn-20261029.htm. Respalda los resultados del T3 y la guía (vía el 10-Q). El anexo 99.1 no se leyó entero.
4. U.S. Treasury, Daily Treasury Par Yield Curve 2026. https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve. 10 años, 30-oct-2026 = 4,94 %. SHA-256 `12905220…`.
5. Damodaran, A., Implied ERP, 1-nov-2026. https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPNov26.xlsx. T12m 3,79 %, pago sostenible 4,41 %, T.Bond 4,94 %. SHA-256 `919b7cc8…`.
6. Damodaran, A., Implied ERP, 1-oct-2026. https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx. T12m 3,70 %, pago sostenible 4,20 %, T.Bond 5,29 %. SHA-256 `54c311b7…`.
7. Damodaran, tablas de industria de EE. UU., ene-2026 (copia en la pestaña `Industry Averages(US)` de la hoja). Respalda betas, EV/Ventas, ROIC y márgenes sectoriales.
8. Precio: Alpha Vantage TIME_SERIES_DAILY AMZN, cierre del 30-oct-2026 de 240,35.
9. JMR: `JMR-valuation/reference/corte_vigente.json` (corte 30-sep-2026), `moat_2026-09-30.json` (AMZN), `plantillas.json` (maestra IA `1e-lbQ…`).
10. Amazon, 10-K FY2025, FY2022, FY2020, FY2017 y FY2015 (https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001018724&type=10-K). Respaldan la serie «Technology and infrastructure/content», la D&A de PP&E por segmento y la descripción de la ley tributaria de 2025.
11. Alpha Vantage TIME_SERIES_MONTHLY_ADJUSTED para AMZN y SPY (consulta del 2-nov-2026). Respalda la beta de regresión y los cierres fiscales.

**No verificado / no ejecutado.** Base fiscal de las preferentes: derivada (12,1 mM), no publicada directamente [CÁLCULO]. I+D pura: estimada por diferencia con cotas [INFERENCIA]. Anclas B de pares: N/D. Los múltiplos A y C y las matrices son del auditor, no nativos. Visor de la app (R2 no publicada). `unificacion_hojas.py` no existe en el repositorio: lo sustituí por `diff_formulas_plantilla.py` más la comprobación de 46 pestañas (APROBADO POR PRUEBA EQUIVALENTE en fórmulas y orden; los **selectores y validaciones de datos no se compararon** uno por uno, así que esa parte queda NO EJECUTADA). `controles_supuestos.py` sobre R2: prueba equivalente con la ficha construida en memoria. **Hoja de auditoría independiente en Google Sheets (REGLAS §11): NO CREADA.** El permiso para crear archivos en Drive fue denegado en esta sesión; el inventario está listo para importar (`inventario_entradas_R2.csv`).

**Registro de versión.**

| Campo | Valor |
|---|---|
| Versión de la auditoría | AMZN-20261102-A12-R2 · auditoría fase 4 · **v2.1** · 2-nov-2026 (v1: commit `08b9d4a`) |
| prompt_version | `auditoria-economica-jmr-v1.3` |
| Hoja / captura | `1h6Xv5cNqwtKPpqI81KiZ_FNpTl4k_uQQS2QJEHphaBI` · captura SHA-256 `c3fcffec122fbd20a5f42e084c44d71397c4d70b4e69c878f62a8fc801118c98` |
| JSON / commit | `VALORACION_A12_EN_REVISION.json` · Modelo-JMR-datos `b1fb039` |
| Fecha de corte | Estados LTM al 30-sep-2026; mercado 30-oct-2026 |
| Publicación | **No publicada.** `auditorias/narrativas/AMZN.md` requiere autorización expresa del usuario |
| Versiones previas | No hay auditorías previas de AMZN en `auditorias/` |
