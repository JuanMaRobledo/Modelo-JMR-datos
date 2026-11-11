# CELH Floyd · Tratamiento económico de las preferentes Pepsi A/B

**Revisión:** `CELH-REBOOT-3T26-R1` · **Corte contable:** 30/09/2026 · **precio de referencia:** US$33,19 (09/11/2026) · **fecha del ejercicio:** 10/11/2026 · **estado:** CANDIDATO / valoración económica cuantificada **no certificada**.

## 1. Evidencia primaria y regla de Damodaran

Fuente principal SEC, Nota 12 del 10-Q 3T2026: https://www.sec.gov/Archives/edgar/data/1341766/000134176626000062/celh-20260930.htm (páginas 29–34). La negociación de distribuidores/capital preferente se refleja también en notas 4, 5 y 11; no se duplica ni se resta a la vez el gasto comercial del valor operativo.

Damodaran (restar valor de mercado estimado de preferred de los reclamos totales del equity, en lugar del valor contable): https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/debttosubtract.htm y https://pages.stern.nyu.edu/adamodar/New_Home_Page/lectures/eqshare.htm .

**Secuencia que preserva el motor original:**

```text
EV operativo Ginsu DCF FCFF (Base)                         = 7.969,516 M
+ caja no restringida                                          +700,617 M
- deuda financiera                                            -674,703 M
= equity antes de preferentes (Ginsu Valuation output!B29)   7.995,430 M
- fair value estimado Pepsi A (no carrying)                    -926,064 M
- fair value estimado Pepsi B (no carrying)                    -647,173 M
= equity ordinario implícito                                  6.422,192 M
/ 251,725 M de acciones ordinarias efectivamente en circulación
= 25,5127 USD/acción común
```

No restar adicionalmente mezzanine de US$1.759,975 M, ni sumar las 33,3 M acciones as-converted a las 251,725 M actuales: eso duplicaría el efecto ya valorado en la opción.

## 2. Derechos SEC: clasificación y flujos

| Derecho | Serie A | Serie B |
|---|---:|---:|
| *Carrying* mezzanine, 30/09/26 | US$852,355 M | US$907,620 M |
| Preferencia de liquidación (*stated value*) | US$550 M | US$585 M |
| Tasa dividendos acumulativos | 5% | 5% |
| Dividendo anual aproximado en efectivo | US$27,50 M | US$29,25 M |
| Acciones posibles al corte | 22,0 M | 11,3 M |
| Strike de conversión | US$25,00 | US$51,75 |
| Automática condicionada desde | 28-ago-2031 | 28-ago-2031 |
| Conversión a opción emisor desde | 28-ago-2032 | 28-ago-2032 |
| Solicitud rescate titular | 2032 / 2035 / 2038 | 2032 / 2035 / 2038 |

En 9M2026 se pagaron US$20,6 M (A) y US$21,9 M (B) en dividendos preferentes; no había dividendos acumulados sin declarar al 30/09/2026. La compañía puede pagar dividendos futuros en efectivo o PIK; aquí se elige cash-only mientras no haya evidencia de cambio. Si un titular pide rescate, el calendario de tres cuotas comienza en la fecha elegida, luego 15 y 30 meses; mientras las participaciones no se redimen continúan dividendos. Demoras legales disparan 8%, 10%, 12%: no se activa este estrés por defecto. El cambio de control concede al titular el mayor entre el efectivo de rescate y el equivalente si se hubiera convertido. El posible evento automático requiere VWAP diez días superior al strike y cuota de mercado contractual; también puede activarse al terminar distribución. La SEC considera conversión el desenlace más probable bajo su criterio empresarial, no un evento incondicional al corte.

## 3. Método de valoración de los derechos (modelo de investigación, no valor justo oficial)

Se valora cada serie por **flujos dividendos + valor contingente de acciones al convertirse + valor presente de rescates si no convierte**, aplicando una cuadratura normal determinista con 8.192 nodos, 2031 y 2032 como dos puntos de decisión (precio VWAP diez días aproximado por precio al punto), y expectativa condicional analítica entre ambos puntos. Todos los dividendos cash y rescates se descuentan al 9% nominal anual *supuesto* para preferred junior a deuda; valor de acciones al convertir se descuenta a tasa libre 4,88%, con proceso lognormal neutral al riesgo y sin dividendos ordinarios (actualmente no pagados). La condición de cuota de mercado 2031 se aproxima con probabilidad analítica75%, independiente del precio; **no es un dato SEC**.

Inputs mercado: precio común US$33,19 del 09/11/2026 (https://www.alphaquery.com/stock/CELH/volatility-option-statistics/90-day/iv-mean); volatilidad histórica 1 año **54,2%** de la fecha (https://marketchameleon.com/Overview/CELH/IV/), redondeada a **54%**; IV opciones 90 días **48,09%** como contraste; la SEC usó 60% de volatilidad y 90% de probabilidad de condición de mercado para una medición de **2025**, no como información futura de 2026. Tasa 10 años USD 4,88% a 09/11/2026. Volatilidad a cinco/seis años y riesgo crediticio no son directamente observables, y el método es una aproximación, no un Monte Carlo con contrato continuo completo.

### Descomposición del valor de derechos

| VP (millones USD) | A | B | Total |
|---|---:|---:|---:|
| Dividendos preferentes hasta el evento | 116,477 | 126,837 | 243,313 |
| Acciones en conversión esperadas | 646,049 | 274,550 | 920,599 |
| Rescate esperado en 3 cuotas cuando aplique | 163,539 | 245,786 | 409,325 |
| **Valor híbrido estimado** | **926,064** | **647,173** | **1.573,238** |

Las probabilidades integradas de eventos son **neutrales al riesgo**, no pronósticos físicos: A ~32,9% convierte en checkpoint2031, ~14,6% en2032, ~52,5% rescata; B ~16,6% / ~9,2% / ~74,2% respectivamente. Por su naturaleza **no se comparan directamente** con la manifestación directiva de que la conversión es más probable.

### Por qué usamos precio de mercado y no la cifra del DCF como subyacente principal

Damodaran indica restar el *valor de mercado o valor de mercado estimado* del capital preferente para obtener el valor de la acción común. Por ello valoramos el instrumento no cotizado A/B usando el precio bursátil observable de la acción común en la misma fecha (US$33,19) y sustraemos ese reclamo constante de los tres equity Ginsu. Como prueba de método alternativa, también resolvimos una **ecuación autofijada** usando como spot el valor intrínseco de la propia acción. Este enfoque alternativo cambia el Base a **US$26,27**. Se documenta, pero no se mezcla con el seleccionado para los escenarios principales.

## 4. Resultado DCF ordinario tras el puente

| Historia | Equity Ginsu pre-pref (millones USD) | Común post-Pepsi (USD/acción) |
|---|---:|---:|
| Conservadora | 4.442,907 | 11,4000 |
| **Base** | **7.995,430** | **25,5127** |
| Optimista | 12.584,920 | 43,7449 |

Esperado ponderado C25%/B50%/O25% = **US$26,5426**. MOS 35% solo DCF Base = **US$16,5833**. Diferencia Base frente al viejo waterfall estático US$27,0725: **−US$1,5598 por acción**. Comparación con precio mercado US$33,19: valor Base **23,13% por debajo** del precio observado, sin que ese descuento mida el potencial de precio futuro.

### Sensibilidades imprescindibles

Al 9% descuento preferente y probabilidad cuota75%, el precio ordinario Base varía de US$25,84 (volatilidad40%) a US$24,98 (volatilidad80%). Con volatilidad54%, q50/75/90% produce US$25,50/25,51/25,52; la variabilidad mayor viene de volatilidad y descuento.

Con vol54% y q75%, descuento de la pata preferente7/9/11/12,5% produce Base **25,22 /25,51 /25,77 /25,95**. Si la primera solicitud de rescate en vez de 2032 fuera en2035/2038, manteniendo los demás supuestos del módulo, Base 25,63/25,73 (escenario no contractual base, no trayectorias de conversión continua).

Tres matrices DCF 5×5 de crecimiento+EBIT, WACC+g y ROIC terminal+g están en `SENSIBILIDADES_PEPSI_R3_V2.json`, con **75 valores derivados algebraicamente** de las corridas Ginsu anteriores (no se atribuyen otras 75 corridas a esta operación). Centro de las tres US$25,51273.

### DCF inverso reejecutado y restaurado

El patrimonio Ginsu **pre-preferente requerido** para justificar US$33,19 del mercado con el claim híbrido del mercado es **US$9.927,990 M**. Con EBIT sostenible Base505 M, ventas/capital1,9, tasa WACC original y demás variables constantes, Input Sheet!B26 del Ginsu Base reejecutado con crecimiento **15,987225%** produjo B29 US$9.928,005 M y acción post-Pepsi US$33,19006. **Se restauró el input B26 al 11%** y su salida original B29 US$7.995,430 M, verificado tras la prueba. La tasa inversa antigua15,386% del puente estático NO es vigente.

## 5. Controles, salvedades materiales y criterio de publicación

**Cinco pruebas locales del modelo numérico pasaron**: suma de probabilidades por serie, reconciliación de VP componentes, precio residual, consistencia de shocks y convergencia 8.192→32.768 nodos. Código de investigación: `PEPSI_WATERFALL_R3.py` (Python stdlib, reproduce bridge mercado) y descarga de ejecución completa `celh_pepsi_waterfall.py`; parámetros y salida en `PEPSI_ECONOMICO_R3_V2.json`. El motor 17 hojas de Damodaran no cambió.

**Este puente es una estimación económica condicionada, no una auditoría independiente ni valor justo contractual certificado**, por razones explícitas:

1. No hay dato público para probabilidad real de cuota de mercado y camino completo de VWAP 10 días; 75% y una observación en 2031 son aproximaciones, al igual que el precio de conversión bursátil bajo riesgo neutral. La distribución y el cambio de control pueden precipitar conversión/rescate.
2. Se aproximan 5% dividendos cash y pagos puntuales, pero PIK, dividendos comunes as-converted y penalizaciones de mora requieren escenarios adicionales si se consideran probables; el modelo usa la primera ventana de rescate 2032 y 2035/38 como sensibilidad.
3. La volatilidad54% y descuento9% son supuestos con evidencia histórica/contraste, no cotizaciones a 5–6 años. La conversión esperada según management no constituye probabilidad de valoración objetiva.
4. El WACC original Ginsu 7,398% incluye deuda y comunes, pero **no integra en forma coherente el costo de financiación del componente convertible preferente**, y la fórmula habitual costo preferente=dividendo/valor mercado no captura opción; se requiere estudiar una sensibilidad o adaptación de inputs aprobada, sin modificar fórmula.
5. Este trabajo SOLO cierra el módulo Pepsi como estudio cuantificado; sigue faltando reconciliación R4 de cinco múltiplos, acciones por SBC/RSU, cotejo SEC granular de H, ROIC año10→terminal y propagación sincronizada SHA256 a M/Presentación, además de CI global y QA app. Por ello el expediente **permanece CANDIDATO** y el [PR#265](https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/265) no debe fusionarse para publicar.

**Archivos y referencias dentro de la revisión:** `PEPSI_ECONOMICO_R3_V2.json`, `PEPSI_WATERFALL_R3.py`, `SENSIBILIDADES_PEPSI_R3_V2.json`, `SENSIBILIDADES_R3_CELH.json` (legado estático), `FASE_R3_ENTREGA.md` y documento A. Se conserva la historia de cálculo sin duplicar expedientes.
