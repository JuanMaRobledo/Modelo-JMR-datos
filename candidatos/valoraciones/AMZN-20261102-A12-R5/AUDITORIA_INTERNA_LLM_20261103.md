# Auditoría interna del constructor — Amazon AMZN R5 · Método JMR A-1.2

**Fecha:** 3-nov-2026 · **Revisión:** `AMZN-20261102-A12-R5` · **Alcance:** valoración, conciliaciones, supuestos y borradores Nivel 1/2 del mismo expediente. **Naturaleza: revisión crítica del mismo LLM constructor, NO AUDITORÍA INDEPENDIENTE.** La auditoría económica por segundo LLM queda **EXPRESAMENTE PENDIENTE** hasta la revisión visual del usuario y sus instrucciones.

## Dictamen

**CANDIDATO CON SALVEDADES MATERIALES — NO CERTIFICAR NI PUBLICAR EN_REVISION TODAVÍA.** Los cuatro DCF actuales y las principales entradas permanecen consistentes con sus fórmulas; los controles de historia y cotejo SEC tienen una ruta reproducible, pero faltan validación integrada sobre el mismo candidato y contraste económico suficiente sobre CAPEX FY2027, valoración privada y deuda. No es aceptable llamar «valor definitivo» a USD149,19 o «recomendación de compra» a un múltiplo más alto.

## 1. Controles críticos de independencia aritmética

| Objeto | Observado en hoja R5 | Prueba/limitación |
|---|---:|---|
| DCF Base | **149,19148575564947** | 1.612.909,1525 M de equity /10.811M acciones |
| Conservadora | **81,00951720766344** | Recalculada previamente desde la tabla de DCF; salvedad económica abierta |
| Optimista | **241,84351613972044** | Recalculada previamente; no elevar a Base por coincidir con mercado |
| Disrupción | **62,43573154339526** | Separada del promedio ordinario |
| WACC actual | **8,179602956%** | Fórmula activa; beta/ERP/deuda mercado requieren contraste separado |
| MOS35% Base | **96,97446574** | `0,65 × 149,19148576`, única base de margen de seguridad |
| FCF neto LTM | **−42.357 M** | `CFO 168300 - CAPEX bruto215192 + incentivos4535` |
| Reinversión FY+1 Base | **121.711,569 M** | Incremento de ventas/Sales-to-Capital con lag; no cash CAPEX |
| Capital de activos privados incluido | **288.700 M** | Exactamente una vez en EV→equity, no FCF operativo |

**A favor:** se comprobó que histórico→Input→DCF sigue vinculado por fórmulas y que las correcciones fiscales de 2022 no alteraron los cuatro DCF. El centro de las tres matrices DCF Base reproduce149,1915. En una lectura independiente del detalle, el centro 5×5 EV/EBITDA =349,7436 y P/OCF=208,7479 es `VP3` del método, mientras que el resumen Base341,1023 y190,4043 es `promedio VP1/2/3`; esa diferencia de métrica **no es un error** y no debe ser «reparada» sustituyendo fórmulas. Las tablas de Nivel 2 usan ambas etiquetas.

**En contra:** las pruebas de reproducibilidad de cuatro DCF y 88 identidades son aritméticas. No confirman por sí solas impuestos, clasificación, valoración económica de cuentas o representatividad de probabilidades. Un `LISTO` de escenario solo demuestra que se llenan las celdas necesarias de esa fórmula.

## 2. Datos y clasificación contable: avances y reservas

El antiguo validador de `estados_completos.py` detectaba once renglones con vacíos porque sus pares sí publican esas líneas. El nuevo perfil `AMZN_R5_HISTORY.json` separa datos indispensables numéricos de partidas agregadas en rubros mayores y de derivaciones no publicadas. **No se ha escrito cero inventado ni duplicado una cuenta en el balance.**

Clasificación y riesgo residual:
- IS9 amortización/D&A: gasto no separado por P&L, CF4 da D&A para reconstruir EBITDA; vigilar doble descuento.
- BS8 cuentas por cobrar: la línea BS6 agrega `receivables and other`; rotación y DSO N/D, no DCF.
- BS12 intangibles no desglosados: ROIC/ROA/ROE vigentes no consultan BS12, pero rentabilidad sobre activos tangibles queda N/D; no normalizar a cero.
- BS14 inversiones largo plazo histórico FY2021–23 parcialmente embebidas en otros activos; afecta series de indicadores, exige seguimiento.
- BS23 pasivo corriente: agregado de accrued y deuda/arrendamientos; no sumar la misma línea dos veces.
- BS28 subtotal de pasivo largo plazo no reportado: derivable por diferencia, no precisa sobreescritura.
- CF29/30/31 emisiones/recompras no desglosadas homogéneamente por fecha; no inferir ausencia del 0 económico. FY2022 −6.000 M sí está capturado.
- CF32 dividendos comunes LTM: nulo conforme a política oficial IR; no inventar pagos.
- CF38 `Levered Free Cash Flow`: métrica derivada no GAAP, no debe contaminar FCFF.
Quedan subpartidas **secundarias pendientes** de completar fuente histórica; la puerta de integridad económica nunca se convierte en verde si una discrepancia resulta material y no está acotada.

El auditor SEC en PR motor #203 ahora documenta firmado fiscal, split20:1 FY2016–19 y PPE LTM con fecha2026-09-30. **La contabilización del 2022 beneficio fiscal** en Excel positivo requiere comparar invertido a la etiqueta SEC, no tratar el beneficio como gasto. El cotejo está instrumentado y testado, pero es importante no llamar «cero diferencias SEC auténticas» a un informe que utiliza un override secundario documentado del 10-Q: es **conciliación reproducible con fuente primaria y fecha**, no una validación ciega de un único XBRL tag.

## 3. Supuestos que pueden cambiar materialmente el valor

### M0 económico: 2027 CAPEX y S/C 0,72

La guía 2026 cash CAPEX ~220.000 M y 2027 **mayor**, sin cuantía, hace dudoso que reinversión FY+1 técnica 121.712 M capture íntegramente costo de capacidad y reemplazo de chips. No es una refutación matemática porque `Reinvestment = cash CAPEX − D&A + ΔNWC` en puente simplificado y pueden existir leases/activos no cash; sí es un **riesgo económico material no cerrado**. Referencia FY2026 CAPEX cash neto215.465 menos reinversión121.712 ⇒ requiere D&A−ΔNWC ~93.753, superior a D&A LTM79.353 por ~14.400, bajo supuestos ilustrativos. La simulación S/C0,50 y0,55 reduce precio Base a128,72 y134,81; no usarlo como `verdadero valor` sin evidencia, pero no ocultar la sensibilidad.

### M1: activos privados y ganancias

El puente añade Anthropic/OpenAI 288.700 M, ~26,70 USD por acción del Base. Diferencia precio valor enorme; descuento 25% reduce Base ~6,68 por acción. La marca contable Level 3 es distinta de realización en efectivo. NI de 2025/26 con plusvalías no operativas no valida P/E forward GAAP. **Independencia** requiere considerar en el futuro escenarios de amortización/ilíquidez o pérdidas de participaciones y doble conteo en capital económico.

### M1: deuda de mercado/arrendamientos/WACC

Deuda **book**304.841 y leasing operativo/financiero reconocido ASC842; no capitalizar de nuevo el PV114.783. La deuda a valor de mercado puede diferir, y WACC8,18% podría infravalorar prima regional y exposición a riesgo de centros de datos. La beta multinegocio y tasa de deuda requieren corte homogéneo. La terminal g4% y WACC8,99% satisfacen desigualdad numérica, no garantizan rentabilidad competitiva de largo plazo.

### M1: RSU/SBC e I+D

Gasto SBC LTM19.873 y RSUs ~223,3 M: tratarlos como warrants Black-Scholes es metodológicamente inapropiado, pero ignorar su dilución también. La proxy capitalizable25% de gasto tecnológico y activo investigación78.943 M es hipótesis, no etiqueta R&D íntegra de Amazon. Revisar vida útil económica y amortización de inversión IA, coherencia de terminal ROIC y NOPAT, sin descontar SBC dos veces.

### M2: márgenes, competencia y ciclos

AWS alcanza margen9M ~38,6%, pero el EBIT consolidado LTM GAAP13,09%; el Base ajustado espera15,8%. Mezcla nube/ads ofrece racional, aunque la depreciación futura puede erosionar rentabilidad incremental. La caída histórica de ROIC de19,24% a13,07% respalda prudencia. Retail Norteamérica e Internacional están mucho más expuestos a salarios, combustible, demanda y presión comercial. El escenario Optimista18,5% y S/C1,15 exige hipótesis combinadas fuertes y no se acepta por resultado bursátil.

## 4. Múltiplos y consistencia temporal

EV/EBITDA y P/OCF calculados en VP tres años y promedio actual son **métodos secundarios**, sometidos a riesgo de un denominador que excluye inversiones de capital. La brecha EV/EBITDA VP promedio341,10 vs DCF149,19 se explica en parte por intensidad del CAPEX; **no prueba** que el DCF sea erróneo. EV/FCFF FY+3 negativo no admite múltiplo positivo; P/E está contaminado por ganancias financieras y P/FCFE requiere ajuste de deuda y flujo; ambos N/D con motivo. No cambiar pesos o forzar cero a métodos invalidables para fabricar precio ponderado.

**Potencial precisión de matriz:** comprobar diferencia entre `Descuento de múltiplos!I20/I24` (centro VP3) y `J20/J24` (media VP1–3). Debe rotularse en la app y tabla del Nivel 2 para no confundir al usuario. Las tres matrices DCF Base tienen centro149,1914858 ejes WACC/g, ROIC/g, crecimiento/margen; opcionales P/V y P/BV no se presentan como métodos JMR principales.

## 5. Calidad del informe y temas que faltan

Nivel 1 redactado con índice normativo **14 capítulos** y Nivel 2 con **12 apartados**, tablas de diez ejercicios + LTM, diez años proyectados de cuatro historias y matrices 5×5 leídas de R5. Los informes citan fuentes SEC, fechas, identificadores y salvedades; su existencia no prueba que los datos que aparecen hayan pasado todos los gates. **No se presentó un cálculo independiente del DCF inverso nuevo** ni una comparación cerrada con AZ Stocks/InvestingPro. El capítulo de mercado reconoce incertidumbre sobre ciclo de sentimiento Marks por falta de indicador con base temporal. No se reemplazaron los cinco múltiplos; se explican N/D y causas.

## 6. Resultado de auditoría interna y controles de cierre

| Componente | Estado | Condición de avance |
|---|---|---|
| Historia 10Y+LTM y DCF cuatro historias | REPRODUCIBLE COMO CANDIDATO | Verificar runtime de cada nueva revisión |
| Fórmulas tax2022, rating inactivo | CORREGIDO EN HOJA R5 | Regresión de fórmulas/prueba crítica con último snapshot |
| Control histórico 11 filas | PERFIL CANDIDATO IMPLEMENTADO | Fuente y saldo de excepciones secundarias mantenidos |
| Cotejo SEC 20 diferencias | PERFIL DE CONVENCIÓN IMPLEMENTADO | Corrida real y resultado final por guardar |
| CAPEX FY2027 y reinversión | **SALVEDAD ECONÓMICA MATERIAL** | Validar guía, D&A 2027, ΔNWC y S/C marginal |
| Deuda a mercado, RSUs, Level3 | **SALVEDAD ECONÓMICA MATERIAL** | Análisis de impacto y tratamiento sin doble conteo |
| Cinco múltiplos | DOS CALCULADOS + TRES N/D | Concluir normalizaciones o dejar N/D aplicabilidad documentada |
| Puerta integrada candidata hoja ↔ motor ↔ JSON ↔ app | **NO EJECUTADA** | Requiere adaptación de runner a R5 |
| Auditoría por LLM diferente | **NO EJECUTADA** | Solo después de revisión visual e instrucciones del usuario |

**Decisión:** entregar F3 y N1/N2 para revisión técnica interna, no promocionar ni publicar hasta gate estricto. No iniciar F5 independiente ahora. El constructor reconoce que su misma auditoría puede compartir sesgos con el análisis y por definición no emite dictamen independiente. Los próximos hallazgos deben dirigirse a una celda/hipótesis concreta con evidencia, sin reiniciar Amazon.

### Referencias

[SEC Amazon 10-Q 2026Q3](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm), [10-K 2025](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm), [hoja R5](https://docs.google.com/spreadsheets/d/199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I/edit), [F3](FASE_3_REVISION_ECONOMICA_20261103.md), [Nivel 1](ANALISIS_NIVEL_1_20261103.md), [Nivel 2](ANALISIS_NIVEL_2_20261103.md), [PR motor #203](https://github.com/JuanMaRobledo/JMR-valuation/pull/203) y [PR datos #234](https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/234).
