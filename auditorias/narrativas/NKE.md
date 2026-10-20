# Auditoría económica narrativa — NIKE, Inc. (NKE)

> **Estado global: Auditoría condicionada.** Varios controles no pudieron completarse con evidencia primaria directa (Input sheet no accesible por valores, contrato `contrato-historias-multiplos-20261017.md` no localizado, comparables sin certificar, estados del 10-K no leídos directamente). Cada limitación se indica en su sección con N/D, motivo e implicación. **No se modificó la valoración.**
> Convenciones: [OBSERVADO] [MODELO] [INFERENCIA] [HIPÓTESIS] [NO VERIFICADO]. Cifras en US$ millones salvo por acción. Idioma: español de Colombia.

## 1. Ficha de auditoría y alcance

| Campo | Contenido |
|---|---|
| Emisor legal / ticker | NIKE, Inc. · NKE · NYSE · acción clase B (Class B Common Stock) [OBSERVADO en hoja y 10-K]. ISIN: N/D (no consultado) |
| Sector / tipo de empresa | Calzado y ropa deportiva; "Madura" según la hoja [MODELO] |
| Moneda y escala | USD; millones, salvo valores por acción. Ejercicio fiscal termina el 31 de mayo |
| Método intrínseco principal | DCF Damodaran FCFF/WACC, historia **Base** (compañía operativa) [MODELO]. FCFE/SOTP: «No aplica» |
| Valoración auditada | `valoraciones/NKE-1790205121370.json`, guardada 2026-10-19T17:10:43Z; la hoja de valoración tiene fecha 15-oct-2026 («Anexo Work 15 oct 2026») y publicación 19-oct-2026 |
| Fecha de la auditoría | 20-oct-2026 |
| Corte de estados en la valoración | FY2026 (31-may-2026) + LTM al 31-ago-2026 (Q1 FY27) [OBSERVADO en hoja; verificado contra 10-Q y comunicado] |
| Precio del análisis | **US$35,15**, cierre del 1-oct-2026 [OBSERVADO en hoja] |
| Precio más reciente obtenido | **US$37,21**, cierre del 19-oct-2026 (Alpha Vantage, consultado 20-oct-2026). Se usa solo como referencia; no sustituye el precio del análisis |
| Versión efectiva | JSON 19-oct-2026 (HEAD del repositorio `10ce1316e0f2578085e5f67d838fb754d21bbd3f`); hoja Google Sheets `1OITWNynG7R3PKC1sITOOazW9jzXgFWFda6qNbbOnYZI` (solo estructura accesible) |
| Estado de verificación | **Con reservas** (no es una auditoría contable). Aritmética reproducida; evidencia primaria parcial; comparables y Input sheet no verificables |

**Documentos examinados.** JSON de valoración (hojas `financieros`, `valoracion`, `analisis` en HTML; `valorEsperado`, `escenariosDCF`, `descuentoMultiples`, `seleccionMultiples`, `sensibilidadMultiples`, `contratoHistoriasMultiplos`, `controlPublicacion`); `analisis/NKE-research-1789598316641-7lxuk.json`; `auditorias/cuatro-activos-2026-10-16/NKE-preflight.json` (estado PENDIENTE, 9 incumplimientos) y `NKE-numerical.json` (ARITHMETIC_PASS, 150/150); `auditorias/cierre-valoraciones-2026-10-19.json`; auditoría previa `auditorias/narrativas/PYPL.md` (solo como referencia de formato). Fuentes primarias: 10-K FY2026, 10-Q Q1 FY27, comunicados de resultados FY26 y Q1 FY27 (ver sección 18).

**Fuera del alcance o no accesible.** (i) *Input sheet* de la hoja de cálculo: el conector de Drive devolvió solo nombres y rangos, sin valores → **N/D** (se auditó la copia JSON). (ii) Contrato `contrato-historias-multiplos-20261017.md`: no está en el repositorio → se usaron los metadatos del bloque `contratoHistoriasMultiplos` del JSON y las descripciones de las hojas; **N/D**. (iii) Financial Datasets sin créditos. (iv) Tablas del 10-K (estados) no leídas directamente por truncamiento; las cifras FY26 se contrastaron con el comunicado y la hoja. (v) Damodaran (datasets de beta/ERP/spreads) no consultado directamente. (vi) Comparables: sin verificación independiente.

## 2. Resumen ejecutivo y relato económico central

Nike diseña, comercializa y vende calzado, ropa y equipamiento deportivo a través de mayoristas y de canales propios (Nike Direct: tiendas y comercio digital), con Converse como marca adicional. Gana dinero combinando una marca de escala global, un margen bruto cercano al 43 % [OBSERVADO: 43,07 % LTM] y una estructura de costos fijos de marketing y distribución que se diluye cuando crecen las ventas. El modelo es poco intensivo en capital (capex de apenas 1,5 % de las ventas, LTM) y generó retornos sobre capital invertido de 20–50 % durante la década pasada [OBSERVADO en hoja: ROIC 19,8 %–51,4 % entre FY18 y FY24; 17,1 % LTM].

Lo que está cambiando es el punto de partida. Tras el máximo de FY2023–FY2024 (ingresos de US$51.200–51.400 millones, margen EBIT de 11,6–12,3 %), Nike entró en una reestructuración: ingresos −9,8 % en FY2025, +0,2 % en FY2026 y −1,1 % en el LTM, con margen EBIT de ~8 % (7,99 % FY25; 8,18 % FY26; 8,19 % LTM) [OBSERVADO en hoja]. Además, el resultado de FY2026 incluye un reembolso de aranceles IEEPA de ~US$986 millones [OBSERVADO en la nota de la hoja; el efecto no se verificó línea por línea en el 10-K]; excluido, el margen EBIT LTM sería ≈ 6,0 % [INFERENCIA del auditor: (3.758 − 986)/45.891]. La dirección ha señalado que los ingresos de FY2027 caerían de forma notable (la hoja cita «caída de un dígito alto»).

**Motor de crecimiento del modelo.** La historia Base [MODELO] supone ingresos −7,0 % en el año 1 (US$42.679 millones), +1 %, +3 %, +4 % y +4,5 % en los años 2–5, y una aceleración gradual hasta 5,24 % en el año 10 y en perpetuidad. El margen EBIT cae a 6,0 % en el año 1 y se recupera linealmente hasta 11,62 % en el año 6, donde se queda. Ese margen coincide casi exactamente con el promedio de diez años (11,65 %), que incluye el régimen anterior a la crisis y el pico de 15,6 % de FY2021. La reinversión sigue un Sales-to-Capital de 2,6 que decrece hasta 1,39 en el año 10; el ROIC terminal es 12,1 % frente a un WACC terminal de 8,94 %.

**Tres lecturas.**
- *Tesis Base favorable.* Una marca con ventaja competitiva duradera, con inventario sano y menor exposición a descuentos, recupera poder de fijación de precios y apalancamiento operativo; el margen vuelve a su media de diez años y el crecimiento a un dígito bajo-medio. El DCF Base es US$33,59 y el promedio ponderado de tres historias US$32,06.
- *Interpretación neutral.* El precio de US$35,15 (104,6 % del DCF Base) ya descuenta más o menos esa recuperación: el DCF inverso exige solo ~0,93 puntos porcentuales más de crecimiento anual en los años 1–5 (CAGR 1,94 % frente a 1,01 % en la Base). El mercado no está pagando una recuperación espectacular, pero tampoco ofrece margen de seguridad: el umbral con MOS 35 % es US$21,83.
- *Contratesis adversa.* La pérdida de relevancia frente a On, Hoka y Adidas es estructural (no cíclica); el margen no regresa a 11–12 % porque el mayor costo de cadena, aranceles y promociones se convierte en permanente. Con margen objetivo de 9,49 % (promedio de 3 años) el DCF cae a US$27,31 (−18,7 %); con 8,64 %, US$24,53 (−27,0 %).

**Supuesto que domina el valor.** El valor terminal pesa 68,3 % del valor operativo [MODELO: PV(TV) 35.992,86/52.735,23], y dentro de él dominan tres supuestos acoplados: g = 5,24 % (igual al Rf spot del 1-oct), ROIC terminal 12,1 % > WACC y margen terminal 11,62 %. La contradicción que Nike debe resolver es que la historia necesita simultáneamente recuperar crecimiento y margen mientras el LTM combina ingresos a la baja con un margen operativo que, sin el reembolso arancelario, está ~5,6 puntos porcentuales por debajo del objetivo. La narrativa no se deriva del precio: se contrasta con histórico, pares y economía del negocio (secciones 5–9).

**Dictamen en una línea.** Tesis **Exigente**: matemáticamente consistente y razonablemente trazable, pero apoyada en un margen y un valor terminal que exigen evidencia que hoy no existe.

## 3. Trazabilidad, integridad y jerarquía de evidencia

| Dato | Valor | Período/perímetro | Tipo | Documento/URL/fecha de consulta | Hoja/celda | Verificación |
|---|---|---|---|---|---|---|
| Ingresos | 46.398 (FY26); 45.891 (LTM) | FY al 31-may-2026; LTM al 31-ago-2026 | [OBSERVADO] | Comunicado FY26 y 10-Q Q1 FY27 (about.nike.com / sec.gov), 20-oct-2026 | `financieros` · Income Statement | FY26 conforme con comunicado; LTM reconciliado (FY26 + Q1 FY27 − Q1 FY26) |
| EBIT (Operating Profit) | 3.797 (FY26); 3.758 (LTM) = 8,18 % / 8,19 % | ídem | [OBSERVADO] | ídem | Income Statement | Conforme. Incluye reembolso IEEPA ~986 (nota de la hoja) → N/D su verificación en el 10-K |
| EBIT del año base del modelo | 3.440,2 (7,50 %) | Base year | [MODELO] | JSON `valoracion` | Valuation output, fila 6 | N/D origen exacto del 7,50 % (Input sheet no accesible) |
| Impuestos | 25 % modelo; efectiva 20,31 % FY26, 20,67 % LTM | — | [MODELO] / [OBSERVADO] | Hoja | Valuation output fila 7; Income Statement fila 28 | Tasa marginal razonable; prueba en sección 6 |
| Flujo FCFF año 1 / terminal | 1.756,4 / 3.192,9 | Años 1–10 y terminal | [MODELO] | JSON | Valuation output filas 10 | Reproducido (dif. 0,013 % en PV) |
| Capex / reinversión | Capex 1,47 % de ventas LTM; reinversión modelo según ΔVentas/S2C | LTM | [OBSERVADO] / [MODELO] | Hoja | Eficiencia de capital fila 19; Valuation output fila 9 | Conforme |
| Deuda financiera | 7.893 | 31-ago-2026 | [OBSERVADO] | 10-Q Q1 FY27 | Cost of capital worksheet B30 | Conforme con 10-Q |
| Arrendamientos (deuda) | 2.868,58 (modelo) vs ≈3.179 (10-Q) | 31-ago-2026 | [MODELO] vs [OBSERVADO] | 10-Q | Cost of capital worksheet fila 45 | **Diferencia de +310** (H-07) |
| Caja | 8.368 | 31-ago-2026 | [OBSERVADO] | 10-Q | Valuation output fila 26 | Conforme con 10-Q |
| Acciones (valoración) | 1.496,0 | Input | [MODELO] | Hoja | Valuation output fila 31 | 10-Q: 1.485,31 al 28-sep-2026 (H-06) |
| Acciones (múltiplos) | 1.484,2 | Diluidas promedio LTM | [OBSERVADO] | Hoja | Income Statement fila 25 | Distinto del DCF (H-06) |
| Opciones | 90,68 | Black-Scholes | [MODELO] | Hoja | Option value | Reproducible; parámetros no auditados línea por línea |
| Precio | 35,15 (1-oct-2026); 37,21 (19-oct-2026) | Cierre | [OBSERVADO] | Alpha Vantage `TIME_SERIES_DAILY`, 20-oct-2026 | Resumen de Valoración | Conforme |
| Rf | 5,24 % | 1-oct-2026 | [OBSERVADO] | UST 10 años, Alpha Vantage `TREASURY_YIELD` | Cost of capital worksheet | Conforme con el dato del 1-oct |
| ERP | 4,77 % (ponderado por regiones de ingresos) | — | [MODELO] | Tabla de ERP por región (Damodaran, versión no verificada) | Cost of capital worksheet fila 27 | Fuente Damodaran N/D |
| Beta | Desapalancada 0,89; apalancada 1,0093 (hoja) / 1,129 (propuesta no adoptada) | — | [MODELO] | Hoja / JSON `betaPropuesta` | Cost of capital worksheet; `valorEsperado` | Diferencia sin resolver (H-04) |
| Costo de deuda | 6,02 % antes de impuestos (rating A2/A) | — | [MODELO] | Hoja | Cost of capital worksheet fila 37 | Spread no verificado |
| Peers | Adidas, Deckers, On, Lululemon, Crocs, Birkenstock (Under Armour excluida) | Precios al 30-sep-2026 (otra nota dice 2-oct) | [NO VERIFICADO] | yfinance, citado por la hoja | Selección económica NKE | Sin certificar (H-11) |

**Diferencias de fuentes y ajustes.** (1) LTM no coincide con el último año calendario: se reconcilió como FY26 + Q1 FY27 − Q1 FY26 (período 1-jun-2025 a 31-ago-2025 como comparable). (2) El año base del modelo (EBIT 7,50 %) no es ni el FY26 (8,18 %) ni el LTM (8,19 %) ni el LTM sin reembolso (6,04 %): su construcción es **N/D**. (3) Versiones previas: el valor DCF Base «técnico anterior» fue US$28,39 y el vigente es US$33,59 (+18,3 %); el motivo del cambio es **N/D** en el JSON (H-19).

## 4. Historia financiera: diez años y punto de partida

Fuente: hoja `financieros` y `analisis` del JSON [OBSERVADO], contrastada con los comunicados para FY26 y LTM. El último trimestre es Q1 FY27 (terminado el 31-ago-2026).

| Métrica | FY17 | FY18 | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 | LTM |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ingresos | 34.350 | 36.397 | 39.117 | 37.403 | 44.538 | 46.710 | 51.217 | 51.362 | 46.309 | 46.398 | 45.891 |
| Crecimiento | — | 5,96 % | 7,47 % | −4,38 % | 19,08 % | 4,88 % | 9,65 % | 0,28 % | −9,84 % | 0,19 % | −1,09 % |
| Margen bruto | 44,58 % | 43,84 % | 44,67 % | 43,42 % | 44,82 % | 45,98 % | 43,52 % | 44,56 % | 42,73 % | 42,91 % | 43,07 % |
| EBIT | 4.749 | 4.445 | 4.772 | 3.115 | 6.937 | 6.675 | 5.915 | 6.311 | 3.702 | 3.797 | 3.758 |
| Margen EBIT | 13,83 % | 12,21 % | 12,20 % | 8,33 % | 15,58 % | 14,29 % | 11,55 % | 12,29 % | 7,99 % | 8,18 % | 8,19 % |
| EBITDA | 5.455 | 5.192 | 5.477 | 3.836 | 7.681 | 7.392 | 6.618 | 7.107 | 4.477 | 4.544 | 4.505 |
| Utilidad neta | 4.240 | 1.933 | 4.029 | 2.539 | 5.727 | 6.046 | 5.070 | 5.700 | 3.219 | 3.108 | 3.093 |
| Tasa efectiva | 13,22 % | 55,31 % | 16,08 % | 12,05 % | 14,02 % | 9,10 % | 18,24 % | 14,93 % | 17,14 % | 20,31 % | 20,67 % |
| Acciones diluidas (prom.) | 1.692,0 | 1.659,1 | 1.618,4 | 1.591,6 | 1.609,4 | 1.610,8 | 1.569,8 | 1.529,7 | 1.487,6 | 1.481,0 | 1.484,2 |
| ROIC (hoja) | — | 19,75 % | 50,41 % | 28,19 % | 51,36 % | 46,47 % | 32,76 % | 36,58 % | 20,87 % | 18,94 % | 17,14 % |
| Capex/ventas | 3,22 % | 2,82 % | 2,86 % | 2,90 % | 1,56 % | 1,62 % | 1,89 % | 1,58 % | 0,93 % | 1,47 % | 1,47 % |

**Comparación de regímenes.**

| Indicador | Último (LTM) | Prom./CAGR 3 años | 5 años | 9–10 años | Rango (10 años) |
|---|---|---|---|---|---|
| CAGR de ingresos | −1,09 % | −3,24 % | 0,82 % | 3,40 % (9 años, FY17–FY26) | −9,84 % a 19,08 % |
| Margen EBIT | 8,19 % | 9,49 % | 10,86 % | 11,65 % | 7,99 % a 15,58 % |
| ROIC (hoja, prom. simple) | 17,14 % | 25,5 % (FY24–26) | 31,1 % (FY22–26) | 33,9 % (FY18–26) | 18,9 % a 51,4 % |
| Capex/ventas | 1,47 % | 1,33 % | 1,49 % | 2,09 % | 0,93 % a 3,22 % |
| Acciones diluidas (variación anual, FY26 vs. inicio) | 1.484,2 | −1,9 % | −1,6 % | −1,5 % (FY17–FY26) | — |

[OBSERVADO] salvo promedios de ROIC y capex/ventas, calculados por el auditor a partir de las series mostradas. El margen EBIT medio de peers es 13,62 % (mediana de la industria) y el primer cuartil 9,69 % [OBSERVADO en la hoja `Crecimiento y Márgenes`; fuente del panel de industria N/D].

**Lectura.**
- *Ciclo y regímenes.* Hay dos regímenes de margen: 12–16 % (FY17–FY24, con la excepción de FY20 por COVID, 8,3 %) y ~8 % (FY25–LTM). Los ingresos se estancaron en US$46.000–46.400 millones tres años seguidos después del pico de US$51.400 millones.
- *Anomalías.* FY18 tuvo una tasa efectiva de 55,3 % por la reforma tributaria estadounidense (impacto único). FY26 incluye el reembolso IEEPA (~US$986 millones; N/D línea exacta en el 10-K); al excluirlo, el LTM sería ≈ US$2.772 millones de EBIT (6,04 %) [INFERENCIA]. Esta cifra es crítica para evaluar el punto de partida del margen.
- *Cambios contables y perímetro.* No se identificó ninguna adquisición o desinversión relevante; I+D se presenta en cero porque Nike lo incluye en SG&A (la fila «Other operating expenses» negativa es un ajuste de presentación de la hoja [INFERENCIA]).
- *Calidad de capital.* El ROIC cayó de 36,6 % (FY24) a 17,1 % (LTM) porque cayó el NOPAT y el capital invertido se mantuvo; los días de cuentas por cobrar subieron de 30 a 44 y los de cuentas por pagar de 37 a 49 [OBSERVADO], señal de presión de capital de trabajo.
- *Límites de homogeneidad.* Los ratios provienen de una plataforma de datos (hoja) y no se reconstruyeron desde el 10-K; las diferencias de definición (leases, cash) pueden afectar el ROIC.
- *Recompras.* El número de acciones diluidas pasó de 1.692 a 1.484 millones (−12,3 % en nueve años), con una tendencia de contracción más lenta desde FY25 (−0,4 % de FY25 a FY26).

## 5. Crecimiento de ingresos: de la historia a la proyección

**Historia económica.** Nike creció a un ritmo medio de 3,4 % anual entre FY17 y FY26 (CAGR de 9 años), pero con dos tramos muy distintos: expansión con venta directa y digital hasta FY23 (CAGR FY17–FY23 de 6,9 % [INFERENCIA: (51.217/34.350)^(1/6)−1]) y estancamiento desde entonces (FY23→FY26: −3,2 % anual). La proyección Base asume un año 1 de −7,0 %, un rebote moderado en los años 2–5 (CAGR 3,11 %) y una aceleración gradual hasta 5,24 % en el año 10, de modo que los ingresos del año 10 (US$61.419 millones) superan en 19,6 % el máximo histórico de FY24 (US$51.362 millones) y en 33,8 % el LTM. Para que eso ocurra se necesita que la reestructuración devuelva participación en calzado deportivo (especialmente en running y en Norteamérica), que Gran China se estabilice y que Converse deje de restar. El año 1 está apoyado en el LTM: el puente LTM muestra que Q1 FY27 quedó ≈US$507 millones por debajo de Q1 FY26 (≈ −4 %) [INFERENCIA a partir de la conciliación LTM], lo que hace más probable un FY27 de −4 % a −8 % que de −10 %.

**Desglose por grupo en la hoja** [MODELO, JSON `crecimientoPorGrupo`, años 1–5]: Norteamérica −2,8 %, +1,0 %, +2,4 %, +4,3 %, +5,8 %; EMEA y APLA −7,0 %, +2,3 %, +3,8 %, +3,8 %, +3,3 %; Gran China −20 %, −3 %, +3 %, +4 %, +4 %; Converse y otros −20 %, −5 %, 0 %, +1 %, +1 %. **N/D**: no pude verificar los pesos por grupo para reconciliar el agregado de −7,0 % del año 1 (no se leyó la nota de segmentos del 10-K); se informa como limitación. Noto que Norteamérica llega a +5,8 % en el año 5, por encima del agregado (+4,5 %), así que el agregado es una elección top-down.

**Verificación Input sheet ↔ Valuation output.** Los crecimientos de la fila 3 de *Valuation output* (−7,00 %, 1,00 %, 3,00 %, 4,00 %, 4,50 %, 4,65 %, 4,80 %, 4,94 %, 5,09 %, 5,24 %) multiplican correctamente la base de US$45.891 millones (42.678,63 → 61.418,96 → terminal 64.637,31). El Input sheet no pudo leerse (N/D); la coincidencia se verificó contra la hoja de salida. El CAGR compuesto años 1–5 desde el LTM es 1,01 %; años 6–10, 4,95 %; años 1–10, 2,95 %.

**Las seis preguntas.**
- **(a) Valor:** −7,00 % año 1; +1 %, +3 %, +4 %, +4,5 % años 2–5; 4,65 %→5,24 % años 6–10; g terminal 5,24 %. Hoja `Valuation output`, fila 3 (columnas 1–10 y terminal).
- **(b) Histórico:** LTM −1,09 %; 3 años −3,24 %; 5 años +0,82 %; 9 años +3,40 %; mínimo −9,84 % (FY25), máximo +19,08 % (FY21). Pares: mediana de CAGR 3 años 7,70 %, 5 años 18,43 % [hoja, fuente del panel N/D]; Nike está por debajo del primer cuartil a 3 años (3,56 %).
- **(c) Mecanismo causal:** mejora del producto (innovación en running y lifestyle), menor dependencia de promociones en mayoristas, recuperación de la relación con minoristas, normalización del inventario y reapertura del crecimiento en Gran China. El crecimiento por precio/mezcla puede dominar en los primeros años; el volumen en los posteriores.
- **(d) Hechos necesarios:** ingresos que dejan de caer a partir de FY28; crecimiento orgánico positivo en Norteamérica en FY28 (+1 %), +4–5 % de FY30 en adelante; Gran China estabilizada en FY28; sin nuevas pérdidas de participación frente a On, Hoka, Adidas.
- **(e) Hechos que lo refutarían:** un segundo año consecutivo con ingresos −5 % o peor en FY28; participación decreciente en calzado de running; inventario que requiera descuentos; crecimiento de peers a un dígito alto mientras Nike sigue plano.
- **(f) Efecto si es erróneo:** año 1 en −9 %: US$32,84 (−2,3 %); año 1 en −4 %: US$34,73 (+3,4 %) [simulación ejecutada por el auditor]. DCF inverso: el precio de US$35,15 implica +0,93 pp por año en años 1–5 (CAGR 1,94 %); el de US$37,21 implica +2,10 pp (CAGR 3,11 %) [ejecutado].

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Crecimiento de ingresos, año 1 | LTM −1,09 %; FY26 +0,19 %; Q1 FY27 ≈ −4 % | −7,00 % · año 1 · Valuation output fila 3 | N/D (guías de la dirección no leídas del 10-K) | FY27 con caída por reestructuración | Q1 FY27 sugiere −4 %; el Base podría ser prudente en el año 1 | Año 1 −9 % → 32,84; −4 % → 34,73 [ejecutado] |
| CAGR años 2–5 | 3 años −3,24 %; 5 años +0,82 %; 9 años +3,40 % | 3,11 % (1 %, 3 %, 4 %, 4,5 %) | Mediana de industria 3 años 7,70 % (hoja; definición y fuente N/D) | Recuperación gradual de participación | Nike no ha crecido >1 % en 3 años seguidos | DCF inverso: +0,93 pp anual en años 1–5 (con fade) vale +US$1,56; orden de magnitud ≈ US$1,7 por pp (extrapolación lineal; no ejecutada con exactitud) |
| CAGR años 6–10 | 9 años +3,40 % | 4,95 % (4,65 %→5,24 %) | Pares: N/D | Crecimiento nominal convergiendo a g terminal | Supera el 3,4 % histórico y el crecimiento nominal de largo plazo del PIB de EE. UU. (N/D, fuente no consultada) | Fade a g=4,0 % años 6–10: −9,9 % (US$30,28) [ejecutado] |
| g terminal | Rf spot 5,24 % | 5,24 % · terminal · fila 3 | Rf = UST 10 años 1-oct-2026 | Crecimiento nominal igual a Rf | No hay evidencia de que la economía crezca a 5,24 % nominal; se iguló g a Rf (ver sección 9) | g 4,0 %: US$30,71 (−8,6 %) [ejecutado] |

**Alternativa razonable.** Año 1 entre −5 % y −8 %, años 2–5 de 2–3 % y años 6–10 convergiendo a 4,0 %. Solo se ejecutó el componente de convergencia (fade a g = 4,0 %: US$30,28); la combinación completa es N/D (no ejecutada).

## 6. Márgenes operativos y normalización de beneficios

**Historia económica.** El margen EBIT no cayó por el margen bruto: éste pasó de 44,6 % (FY17) a 43,1 % (LTM), solo −1,5 pp. La caída viene del SG&A, que subió de 30,8 % de las ventas (FY17) a 34,9 % (LTM): +4,1 pp. SG&A en dólares creció de US$10.563 a US$16.008 millones (+51,5 %), mientras los ingresos crecieron 33,6 % [OBSERVADO, cálculo del auditor sobre la hoja; margen bruto − SG&A% = EBIT% verifica en FY26 (42,91 − 34,73 = 8,18) y LTM (43,07 − 34,88 = 8,19)]. En otras palabras, Nike construyó una base de costos (Nike Direct, tecnología, marketing) para un nivel de ventas superior al actual y no se ha ajustado a los ingresos reales.

**Camino modelado.** Año base 7,50 % (EBIT US$3.440 millones; origen N/D); año 1 6,00 %; recuperación lineal de ≈0,94 pp por año hasta 11,62 % en el año 6, que se mantiene hasta el año 10 y la perpetuidad. Comprobación *ingreso × margen = EBIT*: año 1, 42.678,63 × 6,00 % = 2.560,72 ✓; año 10, 61.418,96 × 11,617 % = 7.135,11 ✓.

**Qué implica 11,62 %.** Desde el LTM (8,19 %) son +3,43 pp; desde el LTM ex-reembolso (6,04 %), +5,58 pp. Con un margen bruto ilustrativo de ~44 % [HIPÓTESIS del auditor, similar a FY24], el SG&A tendría que bajar a ~32,4 % de las ventas del año 6 (US$50.495 millones), es decir, ≈ US$16.350 millones: solo +2,1 % en cinco años frente a los US$16.008 millones del LTM. Con inflación de costos de 2–3 % anual, eso significa recortes reales de costo por unidad vendida. A los ingresos del año 5 (US$48.252 millones), el EBIT adicional frente al LTM ex-reembolso sería ≈ US$2.700 millones [INFERENCIA].

**Dispersión de impuestos.** El modelo usa 25 % [MODELO]; la tasa efectiva fue 20,3 % (FY26) y 20,7 % (LTM), y el promedio de cinco años 15,9 % [OBSERVADO/cálculo]. La tasa de 25 % es una tasa marginal prudente: con 22 % el DCF es US$35,17 (+4,7 %); con 27 %, US$32,54 (−3,1 %) [ejecutado].

**Las seis preguntas.**
- **(a) Valor:** 6,00 % año 1; 7,87 %, 8,81 %, 9,74 %, 10,68 % años 2–5; 11,62 % años 6–10 y terminal. Valuation output, fila 5.
- **(b) Histórico:** LTM 8,19 % (6,04 % ex-IEEPA); media 3 años 9,49 %; 5 años 10,86 %; 10 años 11,65 %; mínimo 7,99 %; máximo 15,58 %. Mediana de la industria 13,62 %; primer cuartil 9,69 % [hoja; fuente N/D].
- **(c) Mecanismo causal:** apalancamiento operativo sobre una base de SG&A estable, menor liquidación de inventario (mejora de margen bruto), mix hacia canales propios y eficiencias de la reestructuración.
- **(d) Hechos necesarios:** margen bruto ≥ 43,5–44 % sostenido; SG&A creciendo ≤ 1 % anual hasta FY31; aranceles con efecto neutro o trasladado a precios; sin necesidad de reinvertir en marketing para frenar la pérdida de participación.
- **(e) Hechos que lo refutarían:** margen EBIT ex-extraordinarios por debajo de 8 % en dos trimestres consecutivos de FY28; SG&A creciendo más rápido que las ventas; nuevos gastos de reestructuración; aranceles permanentes sin traslado.
- **(f) Efecto si es erróneo:** margen objetivo 10,86 % (media 5 años) → US$31,78 (−5,4 %); 9,49 % (media 3 años) → US$27,31 (−18,7 %); 8,64 % → US$24,53 (−27,0 %); 14,0 % → US$42,02 (+25,1 %) [ejecutado]. Cada punto de margen terminal vale ≈ US$2,4–3,3 por acción.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Margen EBIT objetivo (años 6–10) | 3a 9,49 %; 5a 10,86 %; 10a 11,65 %; LTM 8,19 % (6,04 % ex-IEEPA) | 11,62 % · años 6–10 · Valuation output fila 5 | Mediana 13,62 %; Q1 9,69 % (hoja `Crecimiento y Márgenes`; fuente del panel N/D) | Recuperar estructura de FY24: margen bruto ~44 %, SG&A ~32 % | Es el promedio de 10 años que incluye el pico de FY21 (15,6 %); requiere recortar SG&A en términos reales | 9,49 % → 27,31; 10,86 % → 31,78; 14 % → 42,02 [ejecutado] |
| Margen EBIT, año 1 | FY26 8,18 %; LTM ex-IEEPA 6,04 % | 6,00 % · año 1 · fila 5 | N/D | Costos de reestructuración y aranceles | Q1 FY27 con margen ≈ 7,9 % (10-Q; cálculo del auditor) parece menos severo que 6,00 % | Poco material en valor (año 1) |
| Tasa de impuestos | Efectiva 20,3 % FY26; 5a 15,9 % | 25 % · todos los años · fila 7 | N/D | Tasa marginal consolidada | Prudente frente a la efectiva reciente | 22 % → 35,17; 27 % → 32,54 [ejecutado] |
| EBIT normalizado del año base | LTM 3.758 (3.440 en modelo; 2.772 ex-IEEPA) | 3.440,2 · año base · fila 6 | — | Normalización del año base | Origen del 7,50 % N/D | Impacto no calculable sin Input sheet |

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

**Historia económica.** Nike requiere poco capital: capex de 1,5 % de las ventas (LTM), por debajo de la depreciación (CapEx/depreciación 90 %), y un capital de trabajo que se financia en buena parte con proveedores (ciclo de conversión de efectivo de −4,6 días). Esto explica ROIC históricos de 30–50 %. El modelo trabaja con una relación ventas/capital invertido de 2,6 en los años 1–5 (consistente con 45.891/17.614 = 2,61 en el año base) que cae a 2,21; 1,93; 1,71; 1,53 y 1,39 en los años 6–10 [MODELO, Valuation output fila 36], de modo que la reinversión crece más rápido que las ventas: suma 11.428,6 en 10 años (capital invertido de 17.614 a 29.042, +64,9 %) frente a ventas +33,8 %. Fórmula verificada: reinversión año *t* = (Ventas *t*+1 − Ventas *t*)/S2C *t* con convención forward (por ejemplo, año 1: (43.105,42 − 42.678,63)/2,6 = 164,15 ✓; en la historia Conservadora el año 1 libera capital, −129,24).

**Retornos.** ROIC del modelo: año base 14,65 %; año 1, 10,90 %; sube a 21,34 % en el año 6 y se mantiene en 20,0–21,3 % hasta el año 10; en el terminal baja a 12,10 % [MODELO, fila 38]. Es un ROIC de año 10 inferior al promedio histórico (hoja: 33,9 % de 9 años; 17,1 % LTM) y consistente con una recuperación parcial. El **ROIC incremental** implícito entre el año base y el año 10 es ΔNOPAT/ΔCapital = (5.351,3 − 2.580,2)/(29.042 − 17.614) = **24,2 %** [INFERENCIA]: es alto porque casi todo el aumento de NOPAT viene de recuperar margen sobre el capital ya instalado, no de productividad de capital nuevo. El ROIC terminal (12,1 %) supone que las inversiones posteriores al año 10 ganan 3,2 pp sobre el WACC terminal (8,94 %); la reinversión terminal es g/ROIC = 5,24/12,1 = 43,3 % del NOPAT (US$2.438,9 millones) ✓.

**Asignación de capital.** Las acciones diluidas bajaron de 1.692 a 1.484 millones en nueve años; la recompra es relevante pero se ralentizó (−0,4 % de FY25 a FY26). El análisis de múltiplos proyecta dividendos y recompras sin que la hoja documente los movimientos de patrimonio («hipótesis provisionales», según la hoja de selección) y el payout proyectado supera el 100 % del beneficio en algún tramo [INFERENCIA; detalle numérico N/D, ver H-13]. No se identificó capital destinado a adquisiciones. ROE (hoja): 20,6 % LTM frente a 55,0 % en FY20 y 42,7 % en FY18.

**Las seis preguntas.**
- **(a) Valor:** S2C 2,6 (años 1–5), 2,21→1,39 (años 6–10); ROIC terminal 12,1 %; reinversión terminal 2.438,9. Valuation output filas 9, 36–38.
- **(b) Histórico:** ROIC (hoja) LTM 17,14 %; prom. 3 años 25,5 %; 5 años 31,1 %; 9 años 33,9 %. Capex/ventas 1,47 % (LTM) frente a 2,09 % (10 años).
- **(c) Mecanismo causal:** marca con poder de precio y modelo de subcontratación de manufactura (activos ligeros); crecer exige inventario y tiendas, pero a una intensidad de capital baja.
- **(d) Hechos necesarios:** capex de ~1,5–2,5 % de las ventas; capital de trabajo estable (los días por cobrar de 44 y por pagar de 49 son una desviación frente a 30/37 en FY24); retorno marginal ≥ 12 % sobre inversiones nuevas.
- **(e) Hechos que lo refutarían:** necesidades de capex de 3 %+ por remodelación de tiendas y tecnología; inventario creciente más rápido que ventas; adquisiciones destructoras de valor; ROIC LTM ex-IEEPA por debajo del WACC.
- **(f) Efecto si es erróneo:** ROIC terminal = WACC (8,94 %): US$27,10 (−19,3 %); 10 %: US$29,74 (−11,5 %); 15 %: US$37,15 con g=5,24 % (+10,6 %) [ejecutado].

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Sales-to-Capital (años 1–10) | LTM 2,61 (45.891/17.614) | 2,6 (años 1–5) → 1,39 (año 10) · fila 36 | N/D | Capital liviano; más capital por venta a medida que crece | Descenso a 1,39 es conservador frente al ratio actual | S2C constante en 2,6: efecto no ejecutado (N/D) |
| ROIC (año 5–10) | LTM 17,14 %; 3a 25,5 %; 9a 33,9 % | 19,56 %→20,02 % · fila 38 | N/D | Marca + palanca operativa | ROIC incremental 24 % sale del margen, no del capital | Ligado al margen (sección 6) |
| ROIC terminal | — | 12,10 % · terminal · fila 38 | Rf 5,24 % y WACC 8,94 % | Ventaja competitiva parcial sobrevive | Sin evidencia independiente de ventaja duradera a 10 años | =WACC: 27,10 (−19,3 %); 10 %: 29,74 [ejecutado] |
| Reinversión terminal | — | 2.438,9 (43,3 % del NOPAT) · terminal | — | g/ROIC | Alta por g=5,24 % | Con g=4 %: reinversión 33 % del NOPAT; valor 30,71 [ejecutado] |
| Recompra y payout | Acciones −1,5 % anual (9 años) | 1.496 acciones constantes en DCF; 1.484,2 en múltiplos | N/D | Retorno al accionista | Payout >100 % proyectado [INFERENCIA]; hipótesis provisional | Acciones 1.485,31: +0,7 % [ejecutado] |

## 8. Costo del capital y riesgo

**Historia económica.** Nike es una compañía grande, con calificación A2/A+, caja de US$8.368 millones frente a deuda financiera de US$7.893 millones y ventas distribuidas en el mundo: ≈44 % Norteamérica, ≈27 % EMEA, ≈19 % Asia (incluye Gran China) y ≈7 % Latinoamérica [INFERENCIA a partir de los pesos de la tabla de ERP por regiones de la hoja]. Su riesgo no está en la deuda sino en el negocio: dependencia de unos pocos canales, cadena de suministro asiática, aranceles, ciclo de moda y la competencia de marcas más pequeñas. La hoja estima un WACC de 9,22 % para los años 1–5 que se reduce linealmente a 8,94 % en el año 10 y en el terminal.

**Componentes** [MODELO, Cost of capital worksheet]:
- Rf = 5,24 %, igual al rendimiento del UST a 10 años del 1-oct-2026 [verificado con Alpha Vantage].
- ERP = 4,77 %, ponderada por regiones de ingresos; la parte estadounidense usa la prima madura de 3,70 % (entrada directa) y las demás regiones usan las primas de la tabla (Asia 5,19 %, EMEA 5,34 %, Latinoamérica 7,93 %, resto 5,50 %). La versión de Damodaran de la que proviene queda N/D. Con los pesos mostrados reproduzco 4,77 % [INFERENCIA].
- Beta desapalancada 0,89 (negocio único global); apalancada 1,0093 según la hoja. La celda «Direct input beta = 1,20» no se utiliza (H-16). Una beta alternativa de 1,129 figura en el JSON como `betaPropuesta`, **no adoptada** en la valoración vigente.
- Ke = 10,08 % (hoja «Descuento de múltiplos»); recalculado con la beta 1,0093: 5,24 % + 1,0093 × 4,77 % = 10,05 % (diferencia de 0,03 pp, por redondeos [INFERENCIA]).
- Costo de deuda antes de impuestos 6,02 % (rating A2/A; spread N/D), impuesto 25 %, costo de deuda después de impuestos 4,52 %. Pesos 84,6 % / 15,4 %. WACC = 0,846 × 10,08 % + 0,154 × 4,52 % = 9,22 % ✓.
- WACC terminal = 8,94 % = 5,24 % + 3,70 % [INFERENCIA]: coincide exactamente con Rf + prima madura, es decir, un costo de patrimonio con beta 1,0 sin beneficio de deuda. Es una convención de Damodaran razonable y ligeramente prudente.
- Factores de descuento compuestos verificados: 1/1,0922 = 0,9156; × 1/1,0922 = 0,8382; … año 6 = 0,6433/1,0917 = 0,5893 ✓ (Valuation output fila 13).

**Doble conteo y coherencia.** La prima por regiones ya contiene el riesgo país; los flujos tienen recortes explícitos para Gran China (−20 % en el año 1). No encontré doble conteo evidente de ese riesgo, pero tampoco hay una prima adicional por el riesgo de aranceles: el modelo lo trata dentro de los márgenes. **Arrendamientos:** la hoja incluye US$2.868,58 millones de arrendamientos en la deuda de la ponderación y los resta en el puente EV→equity. Si el EBIT/FCFF sigue deduciendo el costo completo del arrendamiento operativo (tratamiento ASC 842) y además se resta la deuda por arrendamientos, parte de esa carga se cuenta dos veces (hasta US$1,92 por acción, el 5,7 % del valor, en el caso extremo) [HIPÓTESIS; no pude verificar si el EBIT fue ajustado en el Input sheet, N/D] (H-07).

**Las seis preguntas.**
- **(a) Valor:** WACC 9,22 % (años 1–5), 9,17 %→8,94 % (años 6–10) y 8,94 % terminal; Ke 10,08 %. Valuation output fila 12; Cost of capital worksheet.
- **(b) Histórico:** no hay serie histórica de WACC en la hoja (N/D). La beta apalancada de 1,01 se compara con 1,20 de la celda de entrada directa y 1,129 propuesta. Pares: beta de industria desapalancada 0,89 [hoja, fuente Damodaran N/D].
- **(c) Mecanismo causal:** Nike tiene exposición cíclica al consumo discrecional, riesgo de cadena y de fuerte competencia, compensado por escala, balance sólido y diversificación geográfica; una beta cercana a 1 es consistente.
- **(d) Hechos necesarios:** Rf cercano a 5,2 %; prima de mercado estable en 4,8 %; spread de crédito A estable; sin deterioro del rating.
- **(e) Hechos que lo refutarían:** beta de regresión sostenidamente > 1,2 (la celda de entrada directa usa 1,20); caída del rating a BBB; ERP implícita de mercado superior a 5 %.
- **(f) Efecto si es erróneo:** WACC +0,5 pp: US$29,52 (−12,1 %); +1,0 pp: US$26,30 (−21,7 %); −0,5 pp: US$38,94 (+15,9 %); −1,0 pp: US$46,25 (+37,7 %). Con la beta propuesta (1,129), el DCF Base pasa a US$27,59 (−17,9 %) y, según el JSON, el promedio de tres historias a US$25,51 (−20,4 %) [valores del JSON `valorBetaPropuesta`; no los repliqué]. Aviso: con los valores por historia del propio JSON (Base 27,59; Conservadora 18,18; Optimista 36,65) y los pesos 0,5/0,278/0,222, el promedio de tres sería 26,99 (−15,8 %), no 25,51: inconsistencia interna sin explicación (H-04). Rf 5,09 % con g = 5,09 %: US$34,24 (+1,9 %) [ejecutado].

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Rf | UST 10 años 5,24 % el 1-oct-2026 | 5,24 % · Cost of capital worksheet | Alpha Vantage `TREASURY_YIELD`, 20-oct-2026 | Tasa libre de riesgo en USD nominal | Se usa spot, no promedio; ya coincide con g | Rf 5,09 % (g y WACC ajustados): 34,24 [ejecutado] |
| ERP | N/D | 4,77 % (3,70 % EE. UU.) | Tabla regional (Damodaran, versión N/D) | Prima ponderada por ingresos | La ERP madura de 3,70 % parece baja frente al Rf de 5,24 %; N/D evidencia | ERP +0,5 pp ≈ Ke +0,5 pp y WACC +0,4 pp; efecto ≈ −10 % por interpolación del cuadro de WACC (no ejecutado) |
| Beta | N/D (regresión no revisada) | 0,89 des.; 1,0093 apal. | Industria Damodaran (fecha N/D) | Negocio cíclico de consumo | Celda de 1,20 sin uso; propuesta 1,129 sin adoptar | Beta 1,129 → 27,59 (Base) [JSON] |
| WACC (años 1–5 → terminal) | N/D | 9,22 % → 8,94 % | N/D | Estructura 84,6/15,4 | Peso de deuda 15,4 % no reconciliado con celdas (14,7 %) (H-17) | ±0,5 pp: 29,52 / 38,94 [ejecutado] |
| Costo de deuda | Interés/deuda LTM: 228/7.893 = 2,9 % | 6,02 % antes de impuestos | N/D | Rating A2/A | Spread N/D | Efecto pequeño (<0,1 pp de WACC) |

**Prueba de tasa alternativa.** Con WACC 10,22 % (años 1–5) y 9,94 % (terminal) el DCF vale US$26,30; con 8,22 %/7,94 %, US$46,25. La asimetría (+37,7 % frente a −21,7 %) muestra que el valor es mucho más sensible a la baja del WACC que a su alza, por la proximidad entre g y WACC terminal.

## 9. Convergencia y valor terminal

**Historia económica.** El año 11 (terminal) hereda sin cambios las condiciones del año 10: crecimiento de 5,24 %, margen EBIT de 11,62 %, impuesto de 25 % y una tasa de reinversión de 43,3 % (g/ROIC = 5,24/12,1). La continuidad entre años 10 y 11 es consistente: en el año 10 la reinversión es 2.317,4 (43,3 % del NOPAT de 5.351,3) y en el terminal 2.438,9 (43,3 % de 5.631,7) ✓. El S2C de 1,39 del año 10 está calibrado para que margen × S2C × (1 − t) = 11,62 % × 1,39 × 0,75 = 12,1 % = ROIC terminal [INFERENCIA]; el ROIC terminal no se supone, resulta de esa calibración. El flujo terminal es 5.631,7 − 2.438,9 = 3.192,9, el valor terminal 3.192,9/(8,94 % − 5,24 %) = US$86.293,9 millones ✓, y su valor presente US$35.992,9 millones (factor 0,4171), es decir, **68,3 %** del valor operativo (57,9 % en la Conservadora, 69,8 % en la Optimista y 41,5 % en la Disrupción [cálculo del auditor]).

**Múltiplo implícito.** El valor terminal equivale a 12,1× el EBIT del año 10 (7.135,1), 16,1× el NOPAT del año 10 y 1,40× los ingresos del año 10 [INFERENCIA]. Con el EV de mercado actual (35,15 × 1.496 + 10.761,6 − 8.368 = US$54.978 millones) Nike cotiza a 14,6× el EBIT LTM de 3.758 y a 12,2× el EBITDA LTM (hoja: 12,18×); el múltiplo terminal es, por tanto, moderado frente al de hoy sobre beneficios deprimidos, pero depende de que el EBIT del año 10 sea 90 % mayor que el LTM.

**Sobre g = Rf.** En la convención de Damodaran, la tasa de crecimiento perpetuo se limita al Rf; aquí g toma exactamente ese tope (5,24 %), que además es el UST a 10 años del día de la valoración, no una media de largo plazo. Nike no ha crecido a 5,24 % en términos nominales de forma sostenida: CAGR de 9 años 3,40 %. Un crecimiento perpetuo de 5,24 % nominal significa que Nike crecería sistemáticamente más que la economía nominal de largo plazo (que no verifiqué: N/D); eso implica ganar participación de manera permanente. Es el supuesto más discutible del terminal (H-01). Con ROIC terminal constante en 12,1 %, bajar g reduce el valor así: 4,5 % → 31,68; 4,0 % → 30,71; 3,5 % → 29,92; 3,0 % → 29,27 [ejecutado, solo terminal]; con un fade de los años 6–10 hacia g, el rango es 31,40; 30,28; 29,36; 28,58 respectivamente.

**Ventaja competitiva a diez años.** Una marca global con décadas de historia, una red global de distribución y capacidad de inversión en marketing que los competidores pequeños no alcanzan. No obstante, el estancamiento FY23–FY26, la pérdida de participación en running y el éxito de On y Hoka muestran que el foso no es automático. El ROIC de la hoja bajó de 36,6 % a 17,1 % en tres años.

**Las seis preguntas.**
- **(a) Valor:** g = 5,24 %; WACC terminal 8,94 %; ROIC terminal 12,1 %; margen 11,62 %; impuesto 25 %; valor terminal 86.293,9; PV 35.992,9. Valuation output filas 15–18.
- **(b) Histórico:** crecimiento a 3, 5 y 9 años: −3,24 %, 0,82 %, 3,40 %; ROIC LTM 17,14 %; margen medio 10 años 11,65 %.
- **(c) Mecanismo causal:** la marca y la escala sostienen un retorno de capital invertido por encima del costo del capital y permiten fijar precios; la reinversión del 43 % del NOPAT sostiene un crecimiento nominal perpetuo.
- **(d) Hechos necesarios:** cuota de mercado estable o creciente; ROIC sobre inversiones nuevas ≥ 12 % durante décadas; crecimiento nominal del sector ≥ 5 %.
- **(e) Hechos que lo refutarían:** ROIC LTM convergiendo a 10 % en los próximos años; caída persistente de cuota; márgenes brutos erosionados por promociones; crecimiento del sector < 4 % nominal.
- **(f) Efecto si es erróneo:** ROIC terminal = WACC: US$27,10 (−19,3 %); g = 4,0 % más ROIC terminal = WACC con fade: US$26,74 (−20,4 %); g = 3,5 % igual: US$26,59 (−20,8 %). Con ROIC = WACC el valor casi no depende de g (27,00–27,10), como predice la teoría [ejecutado].

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| g perpetuo (USD nominal) | Ingresos 3a −3,24 %; 5a 0,82 %; 9a 3,40 % | 5,24 % · terminal · fila 3 | Tope Rf 5,24 % (UST 10a, 1-oct-2026); crecimiento nominal PIB largo plazo N/D | Participación creciente y precios | Crece sistemáticamente sobre el PIB nominal; Rf no es una estimación del crecimiento sostenible | 4,0 %: 30,71; 3,0 %: 29,27 [ejecutado] |
| ROIC terminal | LTM 17,14 %; 3a 25,5 % | 12,10 % · terminal · fila 38 | N/D | Foso parcial que sobrevive | Sin prueba independiente | =WACC: 27,10 (−19,3 %) [ejecutado] |
| WACC terminal | — | 8,94 % · terminal · fila 16 | Rf + ERP madura | Convergencia a empresa madura | Spread g–WACC de solo 3,70 pp | ±1 pp: 26,30 / 46,25 (sección 8) |
| Peso del valor terminal | — | 68,3 % del EV · fila 18/20 | N/D | — | Concentración alta | Cualquier cambio en g/ROIC/WACC terminal tiene efecto amplificado |
| Margen terminal | 10a 11,65 % | 11,62 % | Mediana 13,62 % | Ver sección 6 | Ver sección 6 | Ver sección 6 |

## 10. Validación independiente del valor intrínseco

**Reproducción del DCF Base.** Con los inputs de la hoja (ingresos, márgenes, impuestos, S2C, WACC por año, g, ROIC terminal) reconstruí el DCF en Python: valor por acción US$33,595 frente a los US$33,590 de la hoja (diferencia en PV de 0,013 %, por redondeo) [EJECUTADO]. Puente EV→equity [OBSERVADO en la hoja y verificado contra el 10-Q para deuda y caja]:

| Concepto | Hoja | Verificación |
|---|---|---|
| PV de los flujos años 1–10 | 16.742,36 | Reproducido |
| PV del valor terminal | 35.992,86 | Reproducido |
| Valor de los activos operativos | 52.735,23 | ✓ suma |
| − Deuda (7.893 + arrendamientos 2.868,58) | 10.761,58 | Deuda ✓ 10-Q; arrendamientos: 10-Q ≈ 3.179 (H-07) |
| − Participaciones minoritarias | 0 | N/D (no se hallaron en el 10-Q) |
| + Caja | 8.368,00 | ✓ 10-Q |
| + Activos no operativos | 0 | Sin verificar (preflight: `activos_no_operativos` B85 pendiente) |
| Valor del patrimonio | 50.341,64 | ✓ |
| − Opciones | 90,68 | Parámetros no auditados |
| Valor del patrimonio común | 50.250,96 | ✓ |
| Acciones | 1.496,00 | 10-Q: 1.485,31 (+0,7 % en valor) |
| **Valor por acción** | **33,59** | ✓ |

**Reconciliación de horizontes.** DCF hoy 33,59 × (1 + Ke 10,08 %)³ = 44,80 ≈ «DCF capitalizado FY+3» de 44,81 ✓. Precio objetivo ponderado FY+3 (Base): 0,40 × 44,81 + 0,20 × 42,59 + 0,10 × 39,69 + 0,20 × 39,82 + 0,05 × 41,44 + 0,05 × 41,11 = 42,50 ✓. Valor ponderado hoy (Base): 0,40 × 33,59 + 0,60 × 27,74 = 30,08 ✓. Promedio de tres historias con probabilidades renormalizadas: (0,45 × 33,59 + 0,25 × 19,04 + 0,20 × 44,89)/0,90 = 32,06 ✓. El umbral de MOS (35 %) sobre el DCF Base es 33,59 × 0,65 = **US$21,83** ✓. El precio del análisis (35,15) es 104,6 % del DCF Base; el de hoy (37,21), 110,8 %.

**DCF inverso.** Con el precio del 1-oct (35,15) hay que añadir +0,933 pp a cada tasa de crecimiento de los años 1–5 (con desvanecimiento 80/60/40/20/0 % en los años 6–10): CAGR años 1–5 de 1,94 % frente a 1,01 % de la Base; reproduje el cálculo de la hoja con exactitud [EJECUTADO]. Con 37,21 se requiere +2,098 pp (CAGR 3,11 %). El crecimiento perpetuo implícito en los múltiplos Base de FY+3 es 4,5–5,3 % (EV/EBITDA 4,9 %, EV/FCFF 4,5 %, P/E 5,3 %, P/FCFE 4,8 %, P/OCF 4,7 %), 0,6–0,9 pp sobre el crecimiento del DCF de cada método (4,0–4,6 %); la hoja lo califica «coherente», pero es alto frente al 3,4 % histórico. Las filas 7–11 de esa hoja son, según ella misma, «referencias históricas pendientes de refrescar».

**Sensibilidad DCF Base (US$ por acción; g solo en el terminal, ROIC terminal 12,1 %)** [EJECUTADO]:

| Δ WACC (todos los años y terminal) | g = 3,0 % | g = 4,0 % | g = 4,5 % | g = 5,24 % (Base) |
|---|---|---|---|---|
| −1,0 pp | 36,05 | 39,17 | 41,41 | 46,25 |
| −0,5 pp | 32,35 | 34,47 | 35,93 | 38,94 |
| 0 (Base) | 29,27 | 30,71 | 31,68 | **33,59** |
| +0,5 pp | 26,68 | 27,65 | 28,29 | 29,52 |
| +1,0 pp | 24,46 | 25,11 | 25,52 | 26,30 |

**Sensibilidad ROIC terminal × g** [EJECUTADO]:

| ROIC terminal | g = 3,0 % | g = 4,0 % | g = 4,5 % | g = 5,24 % |
|---|---|---|---|---|
| 8,94 % (=WACC) | 27,00 | 27,04 | 27,07 | 27,10 |
| 10,0 % | 27,92 | 28,53 | 28,94 | 29,74 |
| 12,1 % (Base) | 29,27 | 30,71 | 31,68 | **33,59** |
| 15,0 % | 30,51 | 32,72 | 34,21 | 37,15 |

**Combinaciones adversas ejecutadas.** g = 4,0 % + ROIC terminal = WACC + margen 10,86 % + acciones y arrendamientos del 10-Q: US$25,38 (−24,5 %). Moderada (g = 4,0 %, ROIC = 10 %, margen 10,86 %): US$26,75 (−20,4 %). Acciones 1.485,31: US$33,84 (+0,7 %); arrendamientos +310: US$33,39 (−0,6 %).

**Las seis preguntas** (supuestos dominantes: WACC/terminal, g, margen; véanse además secciones 5–9):
- **(a) Valor:** US$33,59 por acción; PV terminal 35.992,9 de 52.735,2; 1.496 acciones. Valuation output filas 18–32.
- **(b) Histórico:** precio de mercado: 35,15 (1-oct), 37,21 (19-oct). Valor DCF anterior: 28,39.
- **(c) Mecanismo causal:** el valor surge de flujos que crecen de US$1,76 mil millones (año 1) a US$3,19 mil millones (terminal), con 68 % en el terminal.
- **(d) Hechos necesarios:** los de las secciones 5–9 (margen 11,6 %, g 5,24 %, ROIC 12,1 %).
- **(e) Hechos que lo refutarían:** los de las secciones 5–9; en especial EBIT por debajo de US$4.500 millones en FY30 (año 4).
- **(f) Efecto si es erróneo:** tablas anteriores; escenario adverso combinado: US$25,38.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Valor por acción DCF Base | Precio 35,15 / 37,21; DCF anterior 28,39 | 33,59 · Valuation output fila 32 | Peers: N/D | Ver secciones 5–9 | Precio 4,6 % sobre el valor; MOS 35 % exige 21,83 | Reproducido (33,595) |
| Puente EV→equity | Caja y deuda del 10-Q | −10.761,6 + 8.368 | — | Arrendamientos como deuda | Posible doble conteo con EBIT; diferencia de +310 | −0,6 % (arrendamientos); doble conteo hasta −5,7 % si aplica (no ejecutado) |
| Acciones | 1.484,2 (diluidas LTM); 1.485,31 (10-Q) | 1.496 · fila 31 | — | Dilución por opciones | 1.496 es mayor que el observado | +0,7 % [ejecutado] |
| DCF inverso | CAGR 1–5: 1,94 % a 35,15; 3,11 % a 37,21 | Base 1,01 % | — | Mercado exige +0,93 a +2,10 pp | Precio ya descuenta casi toda la recuperación | Ejecutado y reproducido |

## 11. Cuatro historias y probabilidades

Las probabilidades y valores son los **vigentes en la hoja y el JSON**; la auditoría no los modifica ni inventa pesos. Todas las historias comparten WACC (9,22 % → 8,94 %), Ke (10,08 %), tasa de impuestos (25 %) y S2C (2,6 en los años 1–5), según el contrato `supuestosCompartidosPorHistoria: true` [OBSERVADO].

| Historia | Crecimiento | Margen EBIT | Reinversión/ROIC | WACC/Ke | g y retorno terminal | Valor principal por acción | Probabilidad registrada | Qué la confirma / refuta |
|---|---|---|---|---|---|---|---|---|
| **Conservador** · «Recuperación a medias, la marca pierde participación» | Año 1 −9,07 %; años 2–5: −0,81 %, +1,62 %, +2,08 %, +2,21 %; CAGR 1–5 −0,89 % | 6,00 % año 1 → 9,12 % (año 6) | S2C 2,6→…; ROIC terminal 8,94 % (= WACC) | 9,22 %→8,94 % / 10,08 % | g 5,24 %; ROIC = WACC | **19,04** (DCF) | 25 % (peso en promedio 0,278) | Confirma: ventas planas, margen LTM ex-IEEPA ≤ 7 % en FY28. Refuta: crecimiento > 3 % en FY28 con margen > 9 % |
| **Base** · «Reestructuración que devuelve a Nike a crecer poco con margen de 11 %» | Año 1 −7,00 %; +1 %, +3 %, +4 %, +4,5 %; CAGR 1–5 +1,01 % | 6,00 % → 11,62 % (año 6) | S2C 2,6→1,39; ROIC terminal 12,1 % | 9,22 %→8,94 % / 10,08 % | g 5,24 %; ROIC 12,1 % | **33,59** (DCF) | 45 % (peso 0,500) | Confirma: ingresos FY28 > FY27 y margen EBIT ≥ 9 % en FY29. Refuta: segundo año de caída o margen < 8 % ex-extraordinarios |
| **Optimista** · «Vuelve la Nike de márgenes históricos» | Año 1 −3,92 %; +5,15 %, +5,66 %, +4,98 %, +4,44 %; CAGR 1–5 +3,20 % | Año 1 N/D → 14,12 % objetivo | S2C 2,6→…; ROIC terminal 12,1 % | ídem | g 5,24 %; ROIC 12,1 % | **44,89** (DCF) | 20 % (peso 0,222) | Confirma: crecimiento orgánico ≥ 5 % en FY28–FY29 y margen EBIT ≥ 12 %. Refuta: crecimiento < 3 % |
| **Promedio condicionado de tres** (Conservador, Base, Optimista) | — | — | — | — | — | **32,06** | Denominador 0,45 + 0,25 + 0,20 = **0,90** | Fórmula: (0,25 × 19,04 + 0,45 × 33,59 + 0,20 × 44,89)/0,90 = 32,06 ✓ |
| **Disrupción** (aparte) | Año 1 −11,62 %; −5,07 %, −2,04 %, −0,40 %, +0,30 %; CAGR 1–5 −3,87 % | 6,62 % | ROIC terminal 8,94 % (= WACC) | ídem | g terminal 0,30 % | **12,65** | 10 % (peso 0 en el promedio) | Ver subsección siguiente |
| *Esperado de las cuatro (etiqueta del auditor, no usado por la hoja)* | — | — | — | — | — | *30,12* | 100 % | 0,45 × 33,59 + 0,25 × 19,04 + 0,20 × 44,89 + 0,10 × 12,65 [calculado por el auditor] |

Los umbrales de confirmación y refutación de la última columna son criterios del auditor, no guías oficiales ni de la compañía.

**Verificaciones.**
- Probabilidades: 45 + 25 + 20 + 10 = 100 %; la normalización de las tres historias ordinarias usa 0,90 (0,50 / 0,278 / 0,222) ✓.
- Reproduje los valores de las historias Conservadora (19,05), Optimista (44,90) y Disrupción (12,65) con mi propio cálculo, con diferencias ≤ 0,02 [EJECUTADO].
- **MOS sobre el principal:** umbral = 33,59 × (1 − 35 %) = **US$21,83**. Con el precio del análisis (35,15) el margen de seguridad real es **−4,6 %** (precio 4,6 % sobre el DCF Base) y frente al promedio de tres es −9,6 %; con el precio del 19-oct (37,21) es −10,8 %. La hoja ofrece «Value 21,83–23,51» y «Deep Value 18,47–20,15» como zonas de compra [OBSERVADO].
- **Observación de diseño.** Los márgenes objetivo de las historias se separan mecánicamente de la Base en ±2,5 pp (9,12 % y 14,12 %) y −5,0 pp (6,62 %): 11,617 − 2,5 = 9,117; 11,617 + 2,5 = 14,117; 11,617 − 5,0 = 6,617 [INFERENCIA]. La dispersión de márgenes no se deriva de causas distintas; es un abanico simétrico. Y las cuatro historias comparten el mismo WACC, así que ninguna incorpora un mayor riesgo en el escenario adverso. Por otra parte, el margen de Disrupción (6,62 %) está solo 0,58 pp por encima del margen LTM ex-IEEPA (6,04 %): la historia «todo falla» en margen es, en realidad, la rentabilidad subyacente actual.
- **Beta propuesta (no adoptada):** valores por historia con beta 1,129: Base 27,59; Conservadora 18,18; Optimista 36,65; Disrupción 12,22 (JSON) [no replicados].

### ¿Qué pasaría si todo fallara?

*Explicación operativa.* Nike deja de ser relevante en calzado de rendimiento y lifestyle como le ocurrió a Adidas en 2015–2016, pero sin la recuperación posterior. Los ingresos del año 1 caen 11,6 % (a ≈US$40.558 millones), siguen cayendo ~5 %, ~2 % y ~0,4 % en los años 2–4 y se estabilizan en el año 5 (+0,3 %), con crecimiento perpetuo de 0,30 %. El margen EBIT baja a 6,62 %; el ROIC marginal terminal cae al WACC (8,94 %), de modo que el crecimiento deja de crear valor. La compañía no quiebra: probabilidad de fallo 0 % y caja de US$8.368 millones frente a deuda financiera de US$7.893 millones.

*Estimación.* **US$12,65 por acción** (64 % por debajo del precio del análisis), con valor terminal de solo 41,5 % del valor operativo [cálculo del auditor]. Con un piso de cero en la reinversión (sin liberar capital cuando los ingresos caen), el valor sería US$11,97 [EJECUTADO]. *Probabilidad vigente:* 10 % [OBSERVADO; no modificada]. Su razonabilidad es un juicio del propietario de la valoración: el auditor no encuentra evidencia para sustituirla. Disrupción queda **fuera** del promedio de tres, como exige el contrato.

## 12. Valoración por múltiplos: prueba independiente y secundaria

Los múltiplos son secundarios: el ponderado hoy es 40 % DCF + 60 % múltiplos (Base: 0,40 × 33,59 + 0,60 × 27,74 = 30,08). **No son una prueba independiente en sentido estricto:** los denominadores FY+1…FY+3 (EBITDA 4.629,0; FCFF 2.250,1; utilidad neta 3.068,3; FCFE 2.607,6; OCF 2.974,8; ventas 44.398,6; patrimonio 14.153,3) salen del mismo modelo operativo que el DCF (por ejemplo, el FCFF de FY+3 es exactamente el del año 3 del DCF), y el múltiplo C comparte hipótesis con él. Fórmula del Base: **múltiplo = (1 − λ) × promedio(A, B) + λ × C, con λ = 0,5**; verificada: EV/EBITDA 0,5 × (15,51 + 8,81)/2 + 0,5 × 12,42 = 12,29 ✓; EV/FCFF 23,37 ✓; P/E 16,39 ✓; P/FCFE 20,21 ✓; P/OCF 17,55 ✓ [EJECUTADO].

| Método (peso) | A · historia de la etapa: mediana (P25–P75) | B · peers: mediana → ajustada (−5 %) | C · justificado FY+3 (en la fórmula) / centro estable de la matriz | Múltiplo elegido Base (Cons. – Opt.) | Actual LTM | Denominador FY+3 (Base) | Valor FY+3 (precio + div.) | VP a 3 años / consolidado hoy | Justificación económica |
|---|---|---|---|---|---|---|---|---|---|
| EV/EBITDA (20 %) | 15,51× (13,84–18,03) | 9,28× → 8,81× | 12,42× / 9,71× | 12,29× (10,74–14,25) | 12,18× | EBITDA 4.629,0 | 42,59 | 32,36 / 28,93 | Margen y escala; el Base queda +0,9 % sobre el actual |
| EV/FCFF (10 %) | 29,49× (28,39–31,64) | 13,56× → 12,88× | 25,55× / 27,03× | 23,37× (19,21–27,12) | 26,06× | FCFF 2.250,1 | 39,69 | 30,19 / 27,97 | Conversión de caja; justificado = 1/(WACC − g) |
| P/E (20 %) | 22,01× (19,41–25,03) | 13,13× → 12,48× | 15,53× / 15,67× | 16,39× (13,89–19,30) | 16,82× | Utilidad neta 3.068,3 | 39,82 | 30,28 / 26,53 | Retorno al accionista; poco apalancamiento |
| P/FCFE (5 %) | 27,58× (26,17–29,46) | 12,59× → 11,96× | 20,64× / 20,66× | 20,21× (16,92–23,48) | 24,77× | FCFE 2.607,6 | 41,44 | 31,50 / 25,48 | Flujo al accionista; FCFE FY+1 deprimido (1.205) |
| P/OCF (5 %) | 23,87× (21,31–24,12) | 10,67× → 10,14× | 18,09× / 18,11× | 17,55× (14,42–19,48) | 18,75× | OCF 2.974,8 | 41,11 | 31,25 / 29,59 | OCF no es FCF: no descuenta capex |
| P/V (0 %) | 2,39× (1,83–2,93; 4 cierres) | N/D | N/D / 1,08× | 2,39× (1,83–2,93) | N/D | Ventas 44.398,6 | 77,39 | 58,45 / 60,99 | Peso cero; el ancla histórica no es consistente con el centro justificado |
| P/BV (0 %) | 8,45× (6,27–10,51; 4 cierres) | N/D | N/D / 3,40× | 8,45× (6,27–10,51) | N/D | Patrimonio común 14.153,3 | 86,50 | 65,28 / 70,89 | Peso cero; patrimonio contable deprimido por recompras |

**Hallazgos de la prueba.**
- **A reproducible solo en parte.** La etapa de A se define como May '25, May '26 y LTM. Con las observaciones visibles reproduzco EV/EBITDA (15,51×: 20,55×, 15,51×, 12,18×) y P/E (22,0×: 28,00×, 22,03×, 16,82×). **No** reproduzco EV/FCFF (mediana visible 26,49× frente a 29,49×), P/FCFE (34,35× frente a 27,58×) ni P/OCF (22,23× frente a 23,87×) [INFERENCIA; puede haber observaciones adicionales o ajustes por IEEPA no visibles] (H-12).
- **El múltiplo se comprime.** EV/EBITDA: 25,1× (FY23), 20,4×, 20,6×, 15,5× (FY26), 12,2× (LTM). El A es una mediana de tres puntos con tendencia a la baja; la media a 10 años (22,6×) está lejos del actual.
- **B (peers).** Seis comparables (Adidas, Deckers, On, Lululemon, Crocs, Birkenstock; Under Armour excluida por margen negativo). Medianas reproducidas: EV/EBITDA 9,28× y P/E 13,13× ✓ [cálculo con los 6 valores de la hoja]. Datos de yfinance al 30-sep-2026 (la nota textual dice 2-oct): **sin certificar** (`comparablesValidados: false`). Los ajustes (crecimiento −10 %, margen −5 %, riesgo +10 % → −5 %) son juicios del analista [HIPÓTESIS], y el +10 % por «menor riesgo» es discutible con un ROIC que cayó de 36,6 % a 17,1 %. No figuran, por ejemplo, Asics ni Puma [observación del auditor; sin verificar disponibilidad].
- **C comparte hipótesis con el DCF** (g, ROIC, WACC, márgenes); no es evidencia independiente y la hoja correctamente advierte que no debe calibrarse. Para EV/FCFF y P/FCFE el justificado es 1/(WACC − g) = 27,03× (y 20,66× para P/FCFE), por construcción **idéntico** en las tres historias; no discrimina.
- **Denominadores positivos y definiciones.** Todos son positivos en los tres horizontes. P/V = capitalización/ventas (no EV/ventas) ✓; P/BV usa patrimonio común ✓; EV/FCFF usa el FCFF del DCF ✓; P/OCF se rotula como OCF y no como FCF ✓.
- **Dividendos.** DPS acumulado: 1,80 (FY+1), 3,77 (FY+2), 5,93 (FY+3), idéntico en las tres historias. Frente a la utilidad por acción Base (1.484,2 acciones) el payout implícito es 133 % (FY+1), 110 % (FY+2) y 104 % (FY+3); el LTM real fue 78 % (US$2.426 millones sobre US$3.093 millones, hoja `Dividendos`) y DPS LTM US$1,64 [cálculo del auditor] (H-13). Los dividendos se descuentan una vez en su fecha, sin doble conteo con el precio ✓.
- **P/V y P/BV** devuelven valores de US$58–87 por acción frente a un precio de US$35: son anclas históricas iniciales de cuatro cierres (FY23–FY26, incluyendo el régimen anterior) y no de la etapa; se mantienen en peso cero y no contaminan el ponderado (H-09).

## 13. Sensibilidades económicas y escenarios alternativos

**Familia 1: valor por acción («Sensibilidad por múltiplo»).** Contrato: *valor presente FY+3 = múltiplo × fundamental ±20 %*, matrices de 5 × 5 con ejes 0,8–1,2, centro igual al VP3 original, solo Conservador, Base y Optimista (Disrupción fuera), 21 matrices (3 historias × 7 métodos), 0 N/D, controles OK [OBSERVADO, JSON `sensibilidadMultiples`]. Centros verificados contra la hoja «Descuento de múltiplos» (VP3):

| Método | Conservador | Base | Optimista |
|---|---|---|---|
| EV/EBITDA | 24,57 | 32,36 | 44,79 |
| EV/FCFF | 23,50 | 30,19 | 41,39 |
| P/E | 22,38 | 30,28 | 42,57 |
| P/FCFE | 24,31 | 31,50 | 44,94 |
| P/OCF | 24,67 | 31,25 | 40,08 |
| P/V (peso 0) | 43,74 | 58,45 | 77,37 |
| P/BV (peso 0) | 46,54 | 65,28 | 87,26 |

Ejemplo (Conservador · EV/EBITDA; filas = múltiplo, columnas = fundamental, 0,8→1,2): fila 0,8: 17,03 · 18,70 · 20,38 · 22,05 · 23,73; fila 1,0: 20,38 · 22,47 · **24,57** · 26,66 · 28,75; fila 1,2: 23,73 · 26,24 · 28,75 · 31,27 · 33,78. Las esquinas valen 17,03 (−30,7 %) y 33,78 (+37,5 %) respecto al centro; el valor no es proporcional porque la deuda neta se resta del EV. **Fecha/unidad:** USD por acción, VP a 3 años descontado con Ke 10,08 %; precio de referencia 35,15 (1-oct-2026).

**Familia 2: múltiplo justificado («Sensibilidad económica múltiplos»).** Régimen de crecimiento estable; cada celda es un múltiplo (×), **no** un precio. Centros [OBSERVADO]: 

| Método | Conservador | Base | Optimista | Fórmula |
|---|---|---|---|---|
| EV/EBITDA | 6,91× | 9,71× | 9,90× | (1 − g/ROIC) × (EBIT/EBITDA) × (1 − t)/(WACC − g) |
| EV/FCFF | 27,03× | 27,03× | 27,03× | 1/(WACC − g) |
| P/E | 14,95× | 15,67× | 16,31× | N/D en el volcado (usa ROE y retención) |
| P/FCFE | 20,66× | 20,66× | 20,66× | N/D en el volcado |
| P/OCF | 17,29× | 18,11× | 19,51× | N/D |
| P/V | 0,89× | 1,08× | 1,29× | N/D |
| P/BV | 2,83× | 3,40× | 4,06× | N/D |

Reproduje los centros de EV/EBITDA: Conservador (1 − 0,0524/0,0894) × 0,8237 × 0,75/0,0370 = 6,91× ✓; Base (1 − 0,0524/0,121) × 0,8449 × 0,75/0,0370 = 9,71× ✓ [EJECUTADO]. Con ROIC = WACC (Conservador) el múltiplo no depende de g (fila central 6,91× en todas las columnas), tal como predice la teoría. Los centros de estas matrices **no** se calibran para coincidir con el DCF ni con los múltiplos elegidos: por ejemplo, el EV/EBITDA justificado (9,71×) está 21 % por debajo del elegido (12,29×) y 20 % por debajo del actual (12,18×). Los ejes exportados aparecen redondeados (0,04…0,06) en la hoja; el centro económico de las filas es g = 5,24 %.

**Sensibilidades del DCF y escenarios alternativos.** Matrices WACC × g y ROIC terminal × g: sección 10. Resumen de pruebas **realmente ejecutadas** por el auditor (reconstrucción propia del DCF Base; ninguna altera la valoración):

| Prueba | Valor/acción | Δ vs 33,59 |
|---|---|---|
| g terminal 4,5 % / 4,0 % / 3,5 % / 3,0 % (solo terminal) | 31,68 / 30,71 / 29,92 / 29,27 | −5,7 % / −8,6 % / −10,9 % / −12,9 % |
| Igual con fade de los años 6–10 hacia g | 31,40 / 30,28 / 29,36 / 28,58 | −6,5 % / −9,9 % / −12,6 % / −14,9 % |
| ROIC terminal = WACC / 10 % | 27,10 / 29,74 | −19,3 % / −11,5 % |
| g 4,0 % + ROIC = WACC (fade) / g 3,5 % + ROIC = WACC | 26,74 / 26,59 | −20,4 % / −20,8 % |
| WACC +0,5 / +1,0 / −0,5 / −1,0 pp | 29,52 / 26,30 / 38,94 / 46,25 | −12,1 % / −21,7 % / +15,9 % / +37,7 % |
| Margen objetivo 14,0 % / 10,86 % / 9,49 % / 8,64 % | 42,02 / 31,78 / 27,31 / 24,53 | +25,1 % / −5,4 % / −18,7 % / −27,0 % |
| Año 1: −9 % / −4 % | 32,84 / 34,73 | −2,3 % / +3,4 % |
| Impuestos 22 % / 27 % | 35,17 / 32,54 | +4,7 % / −3,1 % |
| Acciones 1.485,31 · arrendamientos +310 · ambos | 33,84 · 33,39 · 33,63 | +0,7 % · −0,6 % · +0,1 % |
| Rf 5,09 % (WACC −0,127 pp, g 5,09 %) | 34,24 | +1,9 % |
| Combinado moderado (g 4 %, ROIC 10 %, margen 10,86 %) | 26,75 | −20,4 % |
| Combinado adverso (g 4 %, ROIC = WACC, margen 10,86 %, acciones y arrendamientos) | 25,38 | −24,5 % |

*Impacto solo direccional (no ejecutado):* beta propuesta 1,129 (el JSON informa 27,59, no replicado); posible doble conteo de arrendamientos (hasta −5,7 % si aplica); ERP +0,5 pp (≈ −10 % por interpolación).

## 14. Coherencia de hojas, cálculos y presentación

**Artefactos examinados:** JSON de valoración (todas las hojas exportadas), preflight (PENDIENTE), prueba numérica (ARITHMETIC_PASS, 150/150), cierre de valoraciones del 19-oct-2026. **No examinados:** celdas del Input sheet y fórmulas de la hoja de Google (solo estructura), visor/app de publicación (`verificacionVisual: PENDIENTE`), enlaces externos. No se supone sincronización automática entre hoja, JSON y visor.

**Preflight pendiente (9 incumplimientos):** `wacc_estado` (B84), arrendamientos (B81), `activos_no_operativos` (B85), fiscal (B92), `casos_especiales` (B108), subcontroles, campos de `cuatro_historias`, probabilidades y evidencia [OBSERVADO en `NKE-preflight.json`]. La propia hoja de selección indica «Auditoría económica CONDICIONAL: comparables por certificar», y `controlPublicacion` registra `comparablesValidados: false`.

**Chequeos que pasan.** Ingreso × margen = EBIT (años 1 y 10 ✓); factores de descuento compuestos ✓; suma de PV y puente EV→equity ✓; valor por acción ✓; MOS 21,83 ✓; probabilidades normalizadas ✓; promedio de tres solo con C/B/O y Disrupción aislada (`incluidaEnPromedio: false`) ✓; 21 + 21 matrices sin N/D ✓; centros de matrices = VP3 ✓; VP3 < FY+3 en todos los métodos ✓; fórmula del Base de la selección (λ = 0,5) ✓; Rf = UST 1-oct ✓; caja y deuda financiera = 10-Q ✓.

**Inconsistencias y rarezas** (detalle y severidad en la sección 15):
1. *Etiquetas:* la tabla de las filas 39–43 de *Valuation output* rotula «Crecimiento años 2-5» pero muestra el crecimiento del año 1 (−7,00 % Base; −9,07 %; −3,92 %; −11,62 %); el CAGR real años 2–5 de la Base es 3,11 %. También rotula como «Promedio 3Y/5Y» lo que son CAGR de ingresos.
2. *Celdas sin etiqueta:* la fila 6 contiene un valor adicional 4.068,79 tras el EBIT terminal; la fila 9 termina con 13.867,48, que equivale a la reinversión acumulada años 1–10 más la terminal (11.428,6 + 2.438,9) [INFERENCIA].
3. *Precios mezclados:* «Precio de hoy» en el resumen es el cierre del 1-oct (35,15); el 19-oct cotiza 37,21. La hoja de P/E muestra «Price today: 35,2» (redondeo).
4. *Acciones:* DCF 1.496; múltiplos 1.484,2; 10-Q 1.485,31.
5. *Arrendamientos:* 2.868,58 en la hoja frente a ≈3.179 en el 10-Q; posible doble conteo.
6. *Beta:* celda de entrada directa 1,20 no usada; beta propuesta 1,129 no adoptada; promedio con beta propuesta (25,51) no reconcilia con las historias (26,99).
7. *Peso de deuda:* 15,4 % en la hoja; con deuda de mercado 6.215,64 + arrendamientos 2.868,58 y capitalización 52.584 resulta 14,7 % [INFERENCIA]. Efecto en WACC < 0,05 pp.
8. *Dividendos:* DPS de la hoja de múltiplos (1,80/1,97/2,16) > DPS LTM (1,64); payout 104–133 %.
9. *Etiqueta «Promedio 1-3 años · Ke 010%»* en la fila 47 del resumen: formato de Ke ausente (10,08 %).
10. *Fecha de comparables:* 30-sep (tabla) frente a 2-oct (texto).
11. *Dos «C»* distintos por método en la hoja de selección (p. ej., EV/EBITDA 12,42× en la fórmula frente a 9,71× en el centro de la matriz), correctamente descritos, pero fácil de confundir.
12. *Versión previa:* DCF Base técnico anterior US$28,39 → vigente US$33,59 sin motivo documentado en el JSON.

## 15. Hallazgos priorizados y propuestas de corrección

Separo los **datos o fórmulas erróneos** (H-06, H-07, H-10, H-15, H-17) de las **hipótesis discutibles** (H-01 a H-05, H-11, H-21). Ningún hallazgo se aplicó: son recomendaciones para la revisión del usuario. No se encontró un error aritmético que invalide el valor (severidad «Crítico»: ninguna). Los impactos son simulaciones del auditor sobre una reconstrucción propia del DCF Base, salvo indicación.

| ID | Severidad | Tipo | Evidencia | Impacto | Mantener / ajustar / investigar | Propuesta y alternativa | Requiere aprobación | Estado |
|---|---|---|---|---|---|---|---|---|
| H-01 | Alto | Supuesto | g terminal 5,24 % = Rf spot del 1-oct (Valuation output fila 3; Cost of capital worksheet) | g 4,0 %: 30,71 (−8,6 %); 3,0 %: 29,27 (−12,9 %) | Investigar / ajustar | Documentar por qué Nike crecería a un ritmo nominal superior al de largo plazo de la economía; alternativa: g entre 3,5 % y 4,5 % (rango 29,9–31,7) | Sí | Abierto |
| H-02 | Medio | Supuesto | ROIC terminal 12,1 % > WACC 8,94 %; resulta de S2C 1,39 × 11,62 % × 0,75 | =WACC: 27,10 (−19,3 %); 10 %: 29,74 (−11,5 %) | Investigar | Aportar evidencia de ventaja duradera (ROIC incremental histórico, participación); alternativa: ROIC terminal 10 % | Sí | Abierto |
| H-03 | Alto | Supuesto | Margen 11,62 % vs LTM 8,19 % (6,04 % ex-IEEPA); requiere SG&A ≈ +2 % en 5 años (secc. 6) | 9,49 %: 27,31 (−18,7 %); 10,86 %: 31,78 (−5,4 %) | Investigar / ajustar | Explicitar el plan de SG&A y margen bruto; alternativa: objetivo 10,86 % (media 5 años) o rampa más lenta | Sí | Abierto |
| H-04 | Alto | Supuesto / dato | Beta de la hoja 1,0093 frente a beta propuesta 1,129 no adoptada; celda directa 1,20 sin uso; JSON informa 25,51 para el promedio de tres con beta propuesta, que no reconcilia con las historias (26,99) | Base con beta propuesta 27,59 (−17,9 %) [JSON, no replicado] | Investigar | Decidir cuál beta rige y documentar fuente y fecha (Damodaran / regresión); corregir la inconsistencia del promedio | Sí | Abierto |
| H-05 | Medio | Dato / supuesto | Año base EBIT 3.440 (7,50 %) sin origen; LTM 3.758 incluye reembolso IEEPA (~986) | Año base: no calculable (Input sheet N/D); poco efecto en valor si el año 1 es 6,00 % | Investigar | Documentar la normalización del año base y verificar el reembolso en el 10-K (nota y página) | No (documental) | Abierto |
| H-06 | Bajo | Dato | Acciones: DCF 1.496; múltiplos 1.484,2; 10-Q 1.485,31 (28-sep-2026) | +0,7 % (33,84) | Ajustar | Unificar en un solo conteo con fecha y fuente | Sí | Abierto |
| H-07 | Medio | Dato / fórmula | Arrendamientos 2.868,58 (hoja) vs ≈3.179 (10-Q); posible doble conteo si el EBIT no se ajusta | −0,6 % por la diferencia; hasta −5,7 % por doble conteo (hipótesis) | Investigar | Confirmar tratamiento del arrendamiento en EBIT/FCFF y en el puente; actualizar a 31-ago-2026 | Sí | Abierto |
| H-08 | Alto | Presentación / gobierno | Preflight PENDIENTE, 9 incumplimientos (B81, B84, B85, B92, B108…) | Sin efecto numérico directo | Investigar | Completar los controles pendientes antes de dar la valoración por conforme | No | Abierto |
| H-09 | Medio | Supuesto / fórmula | P/V (2,39×) y P/BV (8,45×) usan 4 cierres FY23–FY26 y no la etapa; centros justificados 1,08× y 3,40×; valores FY+3 de 77,39 y 86,50 | Ninguno hoy (peso 0) | Mantener peso 0 | Si algún día se ponderan, alinear A con la etapa y con el justificado | Sí | Abierto |
| H-10 | Bajo | Presentación | Rótulo «Crecimiento años 2-5» con valores del año 1; «Promedio 3Y/5Y» que son CAGR; fila 47 «Ke 010%» | Ninguno | Ajustar | Corregir rótulos | No | Abierto |
| H-11 | Medio | Dato | Seis peers de yfinance, 30-sep (nota 2-oct), `comparablesValidados: false`; ajuste −5 % por juicio | Afecta B (25 % del Base por λ y promedio A/B): no cuantificado | Investigar | Certificar peers y fechas; ampliar muestra; probar ajustes −10 %/0 % | Sí | Abierto |
| H-12 | Medio | Fórmula / dato | A no reproducible en EV/FCFF (26,49× vs 29,49×), P/FCFE (34,35× vs 27,58×), P/OCF (22,23× vs 23,87×) | No cuantificado (afecta el Base de tres métodos con peso total 20 %) | Investigar | Documentar las observaciones y los ajustes de A | No (documental) | Abierto |
| H-13 | Medio | Supuesto | DPS acumulado 1,80/3,77/5,93 → payout 133 %/110 %/104 % frente a 78 % LTM; igual para las tres historias | Dividendos por encima de la utilidad en los tres años; efecto en el VP no cuantificado (N/D) | Ajustar | Ligar el DPS a la utilidad por historia con un payout ≤ 100 % | Sí | Abierto |
| H-14 | Medio | Documental | Falta `contrato-historias-multiplos-20261017.md` en el repositorio | Ninguno directo | Investigar | Publicar el contrato o corregir la referencia | No | Abierto |
| H-15 | Bajo | Presentación | «Precio de hoy» = cierre 1-oct (35,15); el 19-oct fue 37,21 | Precio +5,9 % → MOS −10,8 % | Ajustar | Rotular «precio del análisis» y mostrar el precio vigente aparte | No | Abierto |
| H-16 | Bajo | Presentación | Celdas sin etiqueta (4.068,79; 13.867,48) y beta directa 1,20 sin efecto | Ninguno | Ajustar | Etiquetar o eliminar | No | Abierto |
| H-17 | Bajo | Dato | Peso de deuda 15,4 % no reconciliado (14,7 % con celdas visibles) | < 0,05 pp en WACC | Investigar | Mostrar la fórmula del peso | No | Abierto |
| H-18 | Medio | Documental | Input sheet no accesible por valores (solo estructura) | Limita la verificación de supuestos de entrada | Investigar | Exportar el Input sheet al JSON o dar acceso de lectura | No | Abierto |
| H-19 | Medio | Documental | DCF Base técnico anterior 28,39 → 33,59 (+18,3 %) sin motivo registrado | Variación de valor significativa | Investigar | Registrar el motivo del cambio en el historial de versiones | No | Abierto |
| H-20 | Bajo | Fórmula | EV/FCFF y P/FCFE justificados idénticos en las tres historias (27,03× y 20,66×) por usar 1/(WACC − g) | Las matrices económicas no discriminan entre historias | Ajustar | Incorporar ROIC o conversión de caja de cada historia | Sí | Abierto |
| H-21 | Medio | Supuesto | Márgenes de las historias separados mecánicamente ±2,5 pp / −5,0 pp; mismo WACC en las cuatro | Sin efecto numérico; afecta la credibilidad del abanico | Investigar | Derivar cada historia de mecanismos causales y considerar un mayor riesgo en el escenario adverso | Sí | Abierto |

## 16. Catalizadores, señales de refutación y seguimiento

Los umbrales son **criterios del auditor**, no guías oficiales ni de la compañía. Las fechas de los próximos reportes no están confirmadas en las fuentes consultadas (N/D).

| Métrica | Nivel observado (fecha) | Señal favorable | Señal adversa | Fuente | Frecuencia |
|---|---|---|---|---|---|
| Crecimiento de ingresos (reportado y a moneda constante) | LTM −1,09 % (31-ago-2026); Q1 FY27 ≈ −4 % interanual [derivado del puente LTM] | FY27 cerrando no peor que −7 % y crecimiento interanual ≥ 0 en dos trimestres consecutivos durante FY28 | FY27 peor que −9 % (peor que la Conservadora) o FY28 negativo | 10-Q / 10-K / comunicados de Nike | Trimestral |
| Margen EBIT sin extraordinarios (excluye reembolso IEEPA y reestructuración) | 8,19 % LTM; 6,04 % ex-IEEPA; Q1 FY27 ≈ 7,9 % (31-ago-2026) | ≥ 9 % en FY28 y ≥ 10 % en FY29 | < 8 % ex-extraordinarios en FY28 | 10-Q / 10-K (cálculo propio) | Trimestral |
| Margen bruto | 43,07 % LTM (31-ago-2026) | ≥ 44 % | ≤ 42 % | 10-Q / 10-K | Trimestral |
| SG&A / ventas | 34,88 % LTM (31-ago-2026) | ≤ 33,5 % en FY29 con SG&A creciendo ≤ 1 % anual | > 35 % o SG&A creciendo más que las ventas | 10-Q / 10-K | Trimestral |
| ROIC (definición de la hoja) | 17,14 % LTM (31-ago-2026) | ≥ 20 % en FY29 | < 12 % (cerca de WACC) | Hoja / estados | Semestral |
| Conversión de caja: FCFF | FCFF FY26 1.729 [hoja]; modelo: 1.756 (FY+1), 2.048 (FY+2), 2.250 (FY+3) | FCFF ≥ lo modelado en FY+2 | FCFF < 1.500 dos años seguidos | 10-K (flujo de caja) | Anual |
| Capital de trabajo: días por cobrar | 44,4 días LTM frente a 30,4 en FY23 [hoja] | ≤ 38 días | ≥ 46 días | Estados financieros | Trimestral |
| Aranceles y regulación | Reembolso IEEPA ~986 en FY26; efecto posterior N/D | Aranceles trasladados a precios sin pérdida de margen | Nuevos aranceles sin traslado; devolución no recurrente | 10-Q / notas | Trimestral |
| Competencia y cuota (calzado de rendimiento) | N/D (no se obtuvo una serie verificable) | Crecimiento de Nike en running ≥ al de On y Hoka | Peers de calzado creciendo a dos dígitos mientras Nike cae | Resultados de peers y de Nike | Trimestral |
| Asignación de capital | Acciones 1.485,31 (28-sep-2026); payout LTM 78 % | Recompras compatibles con FCF, payout ≤ 100 % | Payout > 100 % financiado con caja o deuda | 10-Q / hoja de dividendos | Trimestral |

## 17. Dictamen económico y resumen para escuchar

**Calificación de la tesis: Exigente.**

- **Consistencia matemática: alta.** Reproduje el DCF Base con una diferencia del 0,013 % en el valor presente (33,595 frente a 33,590), el DCF inverso, el puente EV→equity, los factores de descuento compuestos, las probabilidades normalizadas y el umbral de MOS; el control numérico previo pasó 150 de 150. Los defectos son de rotulado y de coherencia entre hojas, no de aritmética.
- **Trazabilidad documental: con reservas.** Verifiqué ingresos, caja, deuda y precio contra fuentes primarias o de mercado, pero el Input sheet, el contrato de historias y múltiplos y las tablas del 10-K no se leyeron directamente; los comparables no están certificados y el preflight sigue pendiente.
- **Razonabilidad económica: exigente.** La Base necesita una recuperación del margen EBIT de 6–8 % a 11,6 %, una expansión del crecimiento hasta 5,24 % y un ROIC terminal superior al WACC. Ninguno está contradicho por los hechos, pero ninguno cuenta hoy con evidencia que lo respalde, y varios riesgos del lado adverso están a una distancia de 5–20 % de valor.

**Supuesto más frágil:** el margen EBIT objetivo de 11,62 % (sin el reembolso arancelario, el punto de partida está ~5,6 pp por debajo). **Más arbitrario:** g terminal = Rf. **Más defendible:** el Sales-to-Capital de 2,6 (observado: 2,61), la tasa de impuestos de 25 % y el puente de caja y deuda financiera. **Motor principal del precio:** el valor terminal (68,3 % del valor operativo), gobernado por margen, g, ROIC terminal y la diferencia WACC − g. **Decisión analítica sugerida: revisar la hipótesis** (resolver H-01 a H-04 y H-07 antes de usarla como base de decisión); no basta conservarla tal cual. Con el precio del análisis (35,15) no hay margen de seguridad sobre el DCF Base (−4,6 %), y el umbral de compra con MOS 35 % es US$21,83.

**No se modificó la valoración.**

**Resumen para escuchar (125 palabras).** Auditamos la valoración de Nike del diecinueve de octubre. El flujo de caja descontado da treinta y tres dólares con sesenta centavos por acción, y lo reproducimos con una diferencia mínima. El precio del primero de octubre, treinta y cinco con quince, queda cuatro por ciento por encima de ese valor, así que no hay margen de seguridad. La historia exige que los ingresos caigan siete por ciento este año, se recuperen despacio y que el margen operativo suba de ocho a casi doce por ciento. Sin el reembolso de aranceles, el margen actual ronda seis por ciento. Además, el crecimiento perpetuo iguala la tasa del bono a diez años. Calificamos la tesis como exigente y recomendamos revisar esos supuestos. No se modificó la valoración.

## 18. Fuentes primarias, limitaciones y registro de versión

| Fuente | URL | Publicación / período | Consultada | Dato respaldado | Límites |
|---|---|---|---|---|---|
| Nike, Form 10-K FY2026 | https://www.sec.gov/Archives/edgar/data/0000320187/000032018726000088/nke-20260531.htm | Ejercicio terminado el 31-may-2026; fecha de presentación N/D | 20-oct-2026 | Datos de portada (acciones) y Parte I | No se leyeron los estados financieros ni las notas (truncamiento) |
| Nike, Form 10-Q Q1 FY27 | https://www.sec.gov/Archives/edgar/data/0000320187/000032018726000193/nke-20260831.htm | Trimestre terminado el 31-ago-2026 | 20-oct-2026 | Caja 8.368; deuda 7.893; arrendamientos ≈3.179; acciones 1.485,31 (28-sep-2026) | Lectura parcial; página y nota exactas N/D |
| Nike, resultados Q1 FY27 | https://about.nike.com/newsroom/releases/nike-inc-reports-fiscal-2027-first-quarter-results | Q1 FY27 | 20-oct-2026 | Puente del LTM | Cifras no GAAP no revisadas |
| Nike, resultados 4T y año FY26 | https://about.nike.com/en-GB/newsroom/releases/nike-inc-reports-fiscal-2026-fourth-quarter-and-full-year-results | FY26 | 20-oct-2026 | Ingresos FY26, EBIT | Reembolso IEEPA no verificado línea por línea |
| Alpha Vantage `TIME_SERIES_DAILY` NKE | API (sin URL pública) | Cierres hasta 19-oct-2026 | 20-oct-2026 | Precios 35,15 (1-oct) y 37,21 (19-oct) | Datos de proveedor secundario |
| Alpha Vantage `TREASURY_YIELD` 10 años | API | 1-oct-2026 | 20-oct-2026 | Rf 5,24 % | Proveedor secundario |
| Hoja Google de la valoración | https://docs.google.com/spreadsheets/d/1OITWNynG7R3PKC1sITOOazW9jzXgFWFda6qNbbOnYZI/edit | Versión del 15–19-oct-2026 | 20-oct-2026 | Estructura de hojas y rangos | Valores no accesibles; Input sheet N/D |
| Repositorio `JuanMaRobledo/Modelo-JMR-datos` | https://github.com/JuanMaRobledo/Modelo-JMR-datos | HEAD `10ce1316e0f2578085e5f67d838fb754d21bbd3f` | 20-oct-2026 | JSON `valoraciones/NKE-1790205121370.json`; análisis; preflight; prueba numérica; cierre | Contrato de historias y múltiplos no encontrado |
| yfinance (citado por la hoja) | N/D | Precios 30-sep / 2-oct-2026 | No consultada por el auditor | Múltiplos de peers | **No verificado** |
| Damodaran (ERP, betas, spreads) | N/D | Versión usada por la hoja N/D | No consultada directamente | Prima por regiones, beta de industria | **No verificado** |

**No verificado / pruebas no ejecutadas.** Input sheet; origen del EBIT del año base (7,50 %); estados del 10-K (nota y página del reembolso IEEPA y de los arrendamientos); segmentos y pesos por grupo; comparables y ajustes; fuente de la ERP y de la beta; spread de crédito; valor con beta propuesta (solo leído del JSON); A en EV/FCFF, P/FCFE y P/OCF; reproducción celda a celda de las 42 matrices (solo centros y una muestra); tratamiento de arrendamientos en EBIT; fechas de próximos reportes; verificación visual del visor; Financial Datasets (sin créditos).

**Registro de versión.** `prompt_version: auditoria-economica-jmr-v1.0` · versión de la auditoría: NKE-auditoria-narrativa-2026-10-20 v1.0 · hoja/JSON auditados: `NKE-1790205121370.json` (guardado 2026-10-19T17:10:43Z), hoja `1OITWNynG7R3PKC1sITOOazW9jzXgFWFda6qNbbOnYZI` · commit auditado del repositorio: `10ce1316e0f2578085e5f67d838fb754d21bbd3f` · fecha de corte de la valoración: 19-oct-2026 (precio del análisis 1-oct-2026) · fecha de la auditoría: 20-oct-2026 · versiones previas de esta auditoría: ninguna para NKE (la auditoría `PYPL.md` es de otra empresa y se conserva sin cambios).

**Publicación.** Ruta: `Modelo-JMR-datos/auditorias/narrativas/NKE.md`. Commit de publicación: `fe5fd952daba1011adf07a44cbb0d625c0a14007` (rama `main`, 20-oct-2026). Verificación: tras el push, `git ls-remote` devolvió ese commit y la lectura de `origin/main:auditorias/narrativas/NKE.md` mostró 18 títulos H2; el único cambio frente al commit anterior es este archivo, y `PYPL.md` quedó intacto. Acceso desde la app/visor: **no verificado** (sin acceso al visor).

### Control de entrega

| Control | Estado |
|---|---|
| H1 único y 18 títulos H2 exactos, en orden | Cumple (verificado con script) |
| Seis preguntas y tabla fija en secciones 5–10 | Cumple (sección 10 consolida los supuestos dominantes) |
| Fuentes, períodos, crecimiento, margen, reinversión, retornos, tasas, terminal, DCF, múltiplos | Cumple, con N/D señalados |
| Cuatro historias, promedio de tres, Disrupción aparte | Cumple |
| MOS sobre el principal (DCF Base) | Cumple (21,83; −4,6 % al precio del análisis) |
| Siete múltiplos con A/B/C | Cumple (A reproducido solo en dos de cinco ponderados) |
| Dos familias de matrices | Cumple (centros verificados; matrices completas no recalculadas) |
| Sensibilidad DCF e inverso | Cumple (ejecutadas) |
| Hallazgos, señales, dictamen y resumen hablado (125 palabras) | Cumple |
| Markdown editable | Cumple |
| Ninguna modificación de la valoración | Cumple |
| **Declaración** | **Auditoría condicionada:** Input sheet, contrato, estados del 10-K, comparables y publicación sin verificar |
