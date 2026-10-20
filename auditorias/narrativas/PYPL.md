---
title: "Modelo JMR | Auditoría económica narrativa 01: PayPal (PYPL)"
author: "Auditoría independiente de supuestos — uso privado"
date: "20 de octubre de 2026"
lang: es-CO
geometry: margin=22mm
fontsize: 10pt
colorlinks: true
linkcolor: blue
---

# Auditoría económica narrativa — PayPal Holdings (PYPL)

**Informe 01 | Versión narrativa ampliada — 20 de octubre de 2026**  
**Condición:** documento narrativo editable en la app. La auditoría no modifica la valoración, sus supuestos ni su publicación.  
**Documento fuente:** [PYPL — Valoración JMR vigente — 15-oct-2026 — Option value revisado](https://docs.google.com/spreadsheets/d/1LI1LHXYFiCqg5i1_DDzs53Rd4eKv4zhDex2pxSvKuCs/edit).  
**Datos de la compañía:** estados al **30-jun-2026** (10-Q), contrastados con FY2025 (10-K). Precio del análisis **US$57,16 (15-oct-2026)**: no es una cotización actual.  
**Estado de auditoría:** **condicional**, con consistencia matemática parcial confirmada y justificación económica todavía no certificada.

## Guía de lectura: una cifra debe tener una historia

En adelante, las auditorías de todas las empresas internacionales seguirán la misma secuencia: **crecimiento → margen operativo → reinversión y ROIC → costo de capital y valor terminal → múltiplos**, y terminarán con conclusiones y posibles pruebas. Cada supuesto se documentará respondiendo **seis preguntas**: (1) ¿cuánto es y dónde está en la hoja?, (2) ¿qué pasó históricamente?, (3) ¿qué está pasando hoy en el negocio?, (4) ¿qué tendría que suceder para que el número proyectado se cumpla?, (5) ¿qué evidencia lo refutaría? y (6) ¿qué efecto tiene en la valoración si no se cumple? La **historia** no sustituye las fuentes; sirve para formular y evaluar una hipótesis causal.

**Convenciones:** *observado* = dato del reporte o de la serie interna expresamente indicada; *modelo* = valor calculado por la hoja vigente; *hipótesis* = supuesto del analista pendiente de corroborar; *inferencia* = interpretación de los datos, no afirmación de la empresa; *prueba* = sensibilidad que no cambia el archivo original. No se confunden EBIT GAAP, EBIT ajustado del DCF, margen no GAAP, FCFF y flujo de caja reportado.

## Resumen ejecutivo: la tesis que intentan contar los números

PayPal no está siendo valorada como una empresa que vuelve al crecimiento explosivo de su pasado, sino como una **plataforma de pagos madura, rentable y con una recuperación operativa gradual**. El escenario Base supone que la empresa logra mantener las transacciones, estabilizar el pago identificado con la marca PayPal, monetizar Venmo, mejorar la mezcla de clientes y absorber mejor sus costos fijos. Eso podría justificar ingresos que crecen cerca de **4,9 %** anual, un margen EBIT que vuelve a subir hasta **19,64 %** y una eficiencia de reinversión de **2,37 veces**.

Hay, sin embargo, un problema que debe enfrentarse: en el **2T 2026** el volumen procesado creció **~10 %**, los ingresos **~5 %**, pero el margen operativo **GAAP bajó a 16,4 % desde 18,1 %** y el beneficio operativo se contrajo. El negocio está moviendo más pagos sin capturar proporcionalmente más ingresos ni beneficios. Esa evidencia no invalida de forma automática la historia de recuperación, pero **mueve la carga de la prueba** al margen, al mix de productos y a los costos transaccionales.

**Tesis provisional favorable:** PayPal convierte la escala de Braintree en rentabilidad, estabiliza checkout con marca, aprovecha Venmo y disciplina gastos; el margen se recupera progresivamente y se sostiene un exceso de rentabilidad sobre el costo de capital.

**Tesis alternativa adversa:** PayPal gana volumen en servicios de bajo margen, su producto de marca pierde poder de monetización y las inversiones para competir absorben el ahorro; el crecimiento existe, pero la rentabilidad y la ventaja terminal quedan por debajo de lo modelado. **Ambas historias caben en los datos actuales; ninguna está probada.**

### Las cifras que tenemos que defender

| Variable | Supuesto / resultado Base | Ancla, pregunta o alerta |
|:--|:--|:--|
| Ingresos | **4,90 % CAGR años 1–5** | FY2025 **4,32 %**; 1S26 **5,95 %** interanual; el *Input sheet* dice **5,00 %**, el motor usa **4,90 %** |
| Margen EBIT | **19,64 % año 5** | FY2025 serie JMR **17,42 %**; máximo 10 años JMR **18,28 %**; 2T26 GAAP **16,44 %** |
| Sales-to-Capital | **2,3663×** | Referencia propia mostrada **1,82×**; sector Damodaran **2,51×**; confirmar homogeneidad |
| ROIC terminal | **15,58 %** | WACC terminal **8,99 %**; ventaja de **6,59 puntos porcentuales** mantenida indefinidamente |
| Crecimiento perpetuo | **3,0 %** | Inferior al Rf del modelo **5,09 %**; el *override* está activado |
| DCF Base hoy | **US$97,25/acción** | Precio histórico de análisis US$57,16; resultado condicionado a los supuestos |
| Precio ponderado FY+3 | **US$104,15/acción** | Mezcla de DCF capitalizado y múltiplos de salida; **no** equivale al DCF de hoy |

# 1. Crecimiento: ¿de dónde sale el 4,9 %?

### 1.1. El número y su procedencia

El *Input sheet* B27/B29 contiene **5,0 %**, pero las fórmulas efectivas de la fila de ingresos del *Valuation output* enlazan a **«Escenarios e historias»**. Allí, la historia Base supone aproximadamente **5 % anual para ingresos por transacciones** y **4 % para servicios de valor añadido**. El resultado agregado es **~4,90 % anual** en años 1 a 5. En el año 6 empieza la convergencia al crecimiento perpetuo de **3 %** en el año 10. Por eso debemos auditar **4,9 %**, no tomar acríticamente el **5,0 %** de una celda de entrada.

| Período | Dato / supuesto | Naturaleza |
|:--|--:|:--|
| 2023 ingresos netos | US$29.771 millones | 10-K 2025 |
| 2024 ingresos netos | US$31.797 millones | 10-K 2025; +**6,8 %** anual |
| 2025 ingresos netos | US$33.172 millones | 10-K 2025; +**4,32 %** anual |
| 1S25 ingresos netos | US$16.079 millones | 10-Q comparativo |
| 1S26 ingresos netos | US$17.035 millones | 10-Q; +**5,95 %** |
| LTM usado por DCF | **US$34.128 millones** | Fuente interna JMR |
| Año 1 modelo | US$35.799,86 millones | +~**4,90 %** sobre LTM |
| Año 5 modelo | US$43.350,98 millones | +~**27 % acumulado** sobre LTM |
| Crecimiento perpetuo | **3,00 %** | Hipótesis de madurez, no dato histórico |

Las tasas más largas de la serie interna (CAGR 3 años **6,43 %**, 5 años **9,11 %**, 9 años **13,23 %**) muestran **desaceleración estructural** frente a la época de rápida adopción de pagos digitales. Elegir 4,9 % es contar una historia de **normalización**, no de regreso al crecimiento de dos dígitos. El hecho de que 2026 crezca ~6 % semestralmente le da algún respaldo, pero un semestre no valida cinco años.

### 1.2. La historia de negocio detrás del número

El ingreso por pagos depende, de forma simplificada, de **cuánto dinero se procesa** y **cuánto se monetiza cada unidad de volumen**, más ingresos por otros servicios. En el 2T26 PayPal informó TPV de **US$486.448 millones** frente a **US$443.547 millones**, cerca de **+9,7 %**; ingresos por transacciones de **US$7.832 millones** frente a **US$7.441 millones**, cerca de **+5,3 %**. El cociente simple *ingresos por transacciones/TPV* cayó de **~1,68 % a ~1,61 %**: es un indicador descriptivo calculado aquí, **no una take rate oficial homogénea ni prueba de deterioro de precios por sí sola**.

El 10-Q explica parte de la diferencia: mayor peso de Braintree, campañas de co-marketing que reducen el ingreso reconocido y menor ingreso por conversión de divisas. En el trimestre reporta aportes aproximados de **+US$400 millones de Braintree** y **+US$60 millones de Venmo**, con **−US$130 millones de productos PayPal**, entre otros efectos, incluyendo cobertura cambiaria. No debemos sumar esas partidas como si fueran todos los cambios del trimestre: son explicaciones parciales y aproximadas del emisor.

La reorganización anunciada en abril de 2026 busca agrupar Checkout Solutions & PayPal, Consumer Financial Services & Venmo y Payment Services & Crypto. Es razonable plantear que una operación más focalizada podría mejorar producto y ejecución; **sería incorrecto dar por logrado ese beneficio solo porque se anunció una reorganización**.

**Lectura económica:** 4,9 % parece **posible** si el crecimiento de procesamiento y Venmo compensa un checkout de marca modesto, sin nuevas pérdidas pronunciadas de monetización. Se vuelve **optimista** si requiere simultáneamente mayor participación de mercado, recuperación de comisiones y fuerte aceleración de checkout, sin evidencia en resultados trimestrales.

**Qué vigilar:** crecimiento de ingresos transaccionales versus TPV; branded checkout TPV; cambio de mezcla Braintree/PayPal/Venmo; ingresos por servicios añadidos sin contar efectos transitorios de intereses; ingresos por usuario activo y tasa de crecimiento orgánica comparable.

**Dictamen sobre crecimiento:** **plausible con evidencia parcial, no certificado para cinco años**. Mantener el supuesto en observación, sin cambiarlo.

# 2. Margen operativo: ¿por qué habría de llegar al 19,64 %?

### 2.1. Trayectoria observada y proyecto

| Variable | Margen | Fuente / definición |
|:--|--:|:--|
| Media 10 años | **15,84 %** | Serie JMR, «Crecimiento y Márgenes» |
| Media 5 años | **16,53 %** | Serie JMR |
| Media 3 años | **17,31 %** | Serie JMR |
| FY2025 | **17,42 %** | Serie JMR, no intercambiar sin puente con GAAP |
| Máximo 10 años | **18,28 %** | Serie JMR |
| 1S25 | **18,87 %** | GAAP 10-Q comparativo, período semestral |
| 1S26 | **17,11 %** | GAAP 10-Q, período semestral |
| 2T25 | **18,15 %** | GAAP 10-Q |
| 2T26 | **16,44 %** | GAAP 10-Q |
| Año 0 DCF | **17,56 %** | EBIT ajustado en «Valuation output» |
| Año 1 DCF | **17,14 %** | «Input sheet» B28 |
| Año 5 y terminal DCF | **19,64 %** | «Input sheet» B30, hipótesis |

El margen Base **supera por 1,36 puntos** el máximo de los 10 años de la serie JMR. La comparación sirve como alerta, no como refutación, porque el EBIT en el DCF incorpora ajustes posibles por I+D y arrendamientos; hay que **conciliar exactamente las definiciones**. El margen sectorial mediano de los *peers* de la plantilla es **19,01 %**, pero su composición es heterogénea; que una mediana se acerque al supuesto **no convierte** a ese supuesto en razonable automáticamente.

### 2.2. ¿Qué tendría que ocurrir en la economía real?

Los ingresos crecerían de **US$34.128 millones** a **US$43.351 millones** en cinco años, mientras el EBIT modelado subiría de **US$5.992 millones** a **US$8.512 millones**. Es una expansión de EBIT de aproximadamente **42 %** frente a ventas que crecerían aproximadamente **27 %**. La historia está suponiendo, por tanto, **apalancamiento operativo positivo**: cada dólar adicional de ventas tendría que aportar más beneficio operativo del que aportan las ventas actuales, neto de los ajustes del modelo.

Esa tesis requiere alguno de estos mecanismos, preferiblemente documentados por separado: **(i)** recuperación de checkout de mayor contribución; **(ii)** mejor monetización en Venmo; **(iii)** mejora contractual y mezcla de clientes en Braintree; **(iv)** automatización y control de gastos generales; **(v)** menor costo de transacciones y pérdidas, sin sacrificar seguridad ni la experiencia de pago. Hay oposición entre ellos: aumentar incentivos comerciales puede sostener volumen, pero presionar precio y margen.

La evidencia reciente es adversa a una recuperación **ya materializada**. En 2T26 los gastos transaccionales aumentaron **~11 %** frente a ingresos que aumentaron **~5 %**; tecnología y desarrollo subieron **~11 %**, aunque las pérdidas transaccionales y crediticias bajaron **~17 %**. Además, el margen de transacción en dólares (TM$, medida no GAAP) aumentó solo **1 %**, frente a una expansión del TPV de ~10 %. Esto explica por qué **más volumen no equivale a más rentabilidad**.

**Prueba cuantitativa:** las sensibilidades conservadas en la auditoría anterior mostraban que, dejando los demás supuestos iguales, un margen objetivo de **17,636 %** daba un DCF de **US$88,14**; el **19,636 %** Base daba **US$97,25**; el **21,636 %** daba **US$106,37**. Se trata de escenarios contrafactuales documentados, **no** corridas actualizadas o precios confirmados.

**Dictamen sobre margen:** **exigente y no demostrado por la tendencia reciente**. Este es uno de los puntos que más conviene reevaluar cuando se disponga de una secuencia de trimestres con mejor monetización y menores costos transaccionales relativos.

# 3. Reinversión y retorno del capital: ¿cómo crecería sin invertir demasiado?

### 3.1. Diferenciar inversión contable de reinversión económica

En la metodología FCFF, la reinversión operativa relevante no es solo el gasto de capital (*capex*). Abarca, según los ajustes de la plantilla, inversión neta, capital de trabajo incremental y ciertos efectos de capitalización de gasto económico. La identidad del modelo es:

> **Reinversión aproximada = incremento de ingresos / Sales-to-Capital.** Cuanto más alta es la razón ventas/capital, menor reinversión necesita cada dólar adicional de ingresos.

El *Input sheet* fija **2,3663×** para los diez años explícitos. La hoja «Origen de los Supuestos» muestra **1,82×** como referencia reciente de la compañía y **2,51×** como referencia Damodaran de industria. **2,37× es ~30 % mayor que 1,82×**; con el mismo crecimiento necesita alrededor de **23 % menos reinversión** que 1,82×. La hipótesis es una **mejora de eficiencia respecto de la referencia propia**, más que una tasa evidente por sí misma. La comparación solo es válida si definiciones, años y ajustes de capital son homogéneos; esa conciliación aún falta.

**Ejemplo reproducible:** el motor calcula US$741,26 millones de reinversión en año 1 como **(US$37.553,93 M de ingresos del año 2 − US$35.799,86 M del año 1) / 2,3663**. Utiliza el crecimiento del año siguiente porque la plantilla supone **un año de rezago** entre invertir y generar ingresos (*Input sheet* B57 = No). Con un Sales-to-Capital de **1,82×** y el mismo incremento de ingresos, serían alrededor de **US$963,8 millones**: **~US$222,5 millones más** para ese tramo. Esto es **una ilustración parcial**, no una nueva valoración ni un impacto directo por acción.

El 10-Q reporta **US$439 millones** de compras de propiedades y equipos en el primer semestre de 2026, frente a **US$402 millones** un año antes; equivale aproximadamente al **2,6 % de los ingresos semestrales**. El dato ayuda a entender por qué se habla de un negocio relativamente ligero en capital físico, pero **no debe reemplazar** el cálculo de reinversión de FCFF ni ignorar software capitalizado, crédito, gastos de plataforma o cambios operativos de capital circulante.

### 3.2. ¿Qué cuenta la historia?

Una red de pagos madura podría aprovechar una infraestructura tecnológica ya desplegada para procesar más operaciones sin replicar proporcionalmente el gasto de infraestructura. Eso permitiría cierta mejora de ventas/capital. Pero el crecimiento de Braintree, las obligaciones de cumplimiento, las pérdidas crediticias, la necesidad de innovar y las campañas para atraer comercio pueden frenar esa mejora. La **recompra de acciones** es asignación de caja a accionistas, **no** reinversión productiva; no debe utilizarse como prueba de eficiencia operacional.

La hoja presenta un **ROIC aproximado del 22,9 % LTM**, frente a **29,9 % implícito para el año 10** en el escenario Base y **15,58 % terminal**. Es importante distinguir tres conceptos: el ROIC contable calculado de toda la empresa, el retorno incremental que justificaría el crecimiento y el ROIC de perpetuidad. Estos no son intercambiables. El salto implícito del año 10 necesita explicación o reconciliación adicional del capital empleado.

**Dictamen sobre reinversión:** hay una historia económica **posible, pero incompleta**: escala de tecnología y menor intensidad de capital. La superioridad de 2,37× frente al referente propio 1,82× **todavía no está acreditada** por una serie comparable de reinversión y retorno incremental.

# 4. Valor terminal y costo de capital: ¿por qué durarían las ventajas?

### 4.1. Los valores del modelo

| Componente | Modelo | Interpretación |
|:--|--:|:--|
| Rf (Treasury 10 años según hoja) | **5,09 %** | Ancla de descuento en USD al corte del análisis |
| Beta apalancada | **0,90** | Derivada de proxy sectorial; revisar adecuación a fintech |
| ERP geográfica | **~4,46 %** | Proxy de prima de renta variable |
| Costo patrimonio Ke | **9,11 %** | Aproximadamente Rf + beta × ERP |
| WACC inicial | **8,20 %** | Modelo de ponderación inicial |
| WACC terminal | **8,99 %** | Mayor costo de capital en madurez |
| g terminal | **3,00 %** | Hipótesis de crecimiento nominal perpetuo |
| ROIC terminal | **15,58 %** | Hipótesis de ventaja persistente |

Un crecimiento perpetuo de **3 %** es consistente con la restricción de crecimiento estable y menor que el **Rf de 5,09 %** vigente en la hoja. **No es igual al Rf**, pese a que el texto de «Origen de los Supuestos» todavía lo describa así: hay un *override* activado. El spread **WACC − g = 5,99 puntos** es positivo y matemáticamente permite capitalizar flujos, pero la coherencia económica depende de la rentabilidad y reinversión terminales.

### 4.2. ¿Qué justifica un ROIC terminal de 15,58 %?

Si el WACC de largo plazo fuera **8,99 %** y PayPal siguiera produciendo ROIC de **15,58 %**, conservaría un exceso de retorno de **6,59 puntos porcentuales** después del décimo año. Esto cuenta una historia de **barrera de entrada y ventaja persistente**: marca, confianza, datos, integración comercial, escala de pagos, reconocimiento de la billetera, relaciones con comerciantes y costos de cambio. Es una historia **compatible con ciertas características de su plataforma**, pero competidores con redes de pagos, billeteras y servicios de adquirencia pueden erosionar dicha ventaja.

No bastaría con argumentar que PayPal «es grande». Hay que demostrar la capacidad de cobrar una contribución económica atractiva después de gastos de transacción, inversión tecnológica, prevención de fraude y competencia. Lo que separa una franquicia valiosa de una procesadora de alto volumen es su capacidad de **retener rentabilidad incremental**, no simplemente TPV.

### 4.3. Dependencia real del valor terminal

| Bloque del DCF | Valor actual de activos operativos |
|:--|--:|
| PV de FCFF de años 1–10 | **US$37.849 millones** |
| PV del valor terminal | **US$47.412 millones** |
| Total de activos operativos | **US$85.261 millones** |
| Porcentaje atribuido al valor terminal | **55,6 %** |

El modelo usa FCFF terminal de aproximadamente **US$6.386 millones** y un valor terminal nominal del año diez cercano a **US$106.608 millones**. El 55,6 % es la **fracción del valor presente de los activos operativos**, no del precio por acción: evita confundir puentes de deuda, caja, inversiones y acciones diluidas.

En el terminal, el modelo reinvierte aproximadamente **US$1.523 millones** de un EBIT después de impuestos próximo a **US$7.908 millones**, consistente con **g/ROIC, aproximadamente 3 %/15,58 % = 19,3 %**. Esa relación permite pagar un FCFF estable, pero presupone retornos sobre el capital superiores al descuento durante toda la perpetuidad.

**Sensibilidades históricas registradas en el trabajo previo (no recalculadas hoy):** si el ROIC converge inmediatamente a WACC tras año diez, el DCF desciende desde **US$97,25** a aproximadamente **US$87,86**; con convergencia en cinco años, aproximadamente **US$89,50**. Cambiar g de **3 % a 2 %** dio **US$91,56**; llevar g a **4 %**, **US$104,99**. Estas cifras solo describen **experimentos condicionales**, no otras versiones de valoración vigentes.

**Dictamen terminal:** g y WACC parecen **internamente compatibles**, pero la ventaja competitiva **perpetua** es un **supuesto económico crítico** que necesita evidencia y escenarios de erosión, no una aceptación automática de la hoja Damodaran.

# 5. Múltiplos: la última prueba, no un atajo para confirmar el DCF

La selección económica más reciente del archivo es la pestaña **«Selección económica PYPL» del 19-oct-2026**. Su mecanismo descrito combina una **ancla histórica del régimen reciente** (A), **peers ajustados** (B) y un **múltiplo justificado** (C), con aproximadamente 25 % de peso para C. Esto es diferente de la regla antigua del «menor múltiplo positivo de cuatro cierres» que aún aparece en la pestaña narrativa de origen. El objetivo es preguntar **qué está pagando el mercado por beneficios y flujos comparables y por qué debería seguir haciéndolo dentro de tres años**.

| Método | Actual LTM (hoja selección) | Base FY+3 elegido | Variación vs. múltiplo actual | Estado |
|:--|--:|--:|--:|:--|
| EV/EBITDA | **6,82×** | **9,12×** | **+34 %** | Requiere recuperación de precio relativo |
| EV/FCFF | **7,15×** | **13,31×** | **+86 %** | Brecha notable; revisar definiciones y calidad del FCFF |
| P/E | **9,91×** | **16,91×** | **+71 %** | Implica rerating además de EPS proyectado |
| P/FCFE | **6,82×** | **10,78×** | **+58 %** | Revisar recompras, estructura financiera y base FCFE |
| P/OCF | **6,01×** | **9,74×** | **+62 %** | Revisar generación de caja normalizada |
| P/V | s/d certificado | **2,44×** | n/d | Calculado, **peso 0 %** |
| P/BV | s/d certificado | **3,56×** | n/d | Calculado, **peso 0 %** |

**Precaución de comparabilidad temporal:** «actual LTM» y «Base FY+3» son *múltiplos* calculados para métricas correspondientes, pero sus saltos no representan por sí solos rendimiento accionarial; el precio de salida usa además proyecciones de beneficios, deuda neta, acciones y dividendos. Se debe verificar que cada múltiplo histórico sea realmente observable con corte preciso, definiciones coherentes y denominadores positivos. Una hoja complementaria marca ciertos múltiplos de mercado LTM como **N/D**, por falta de fuente conciliada. Por eso los «actuales» de la tabla **no son todavía cotizaciones certificadas**.

**Historia económica de los múltiplos:** un mercado podría aumentar lo que paga por PayPal si la compañía deja de ser percibida como procesadora de alto volumen y bajo margen y vuelve a demostrar una franquicia de checkout rentable, con crecimiento estable y conversión de beneficios en caja. Pero se estaría **sumando una segunda apuesta**, el *rerating*, a la primera apuesta de recuperación operativa. Especialmente EV/FCFF **13,31× versus 7,15×**, la magnitud exige más que una narrativa genérica de «valor infravalorado».

**Peers:** Visa y Mastercard tienen modelos económicos y márgenes radicalmente distintos; Stripe/Adyen, Block, Global Payments y otras compañías poseen perímetros, geografía y exposición al procesamiento diferentes. Ningún promedio mecánico crea un verdadero comparable. Debe exigirse en cada empresa: periodos exactos, fuente del precio y deuda, denominadores homogéneos, justificación de inclusión y ajuste documentado por márgenes, crecimiento y riesgo.

**Control adicional detectado:** en la hoja, el **«justificado estable (centro de la matriz)»** no coincide necesariamente con el **«C — justificado FY+3 (usado en la fórmula del Base)»**. Ejemplos: **EV/EBITDA 8,67× vs 12,20×** y **EV/FCFF 16,69× vs 20,40×**. Pueden ser medidas diferentes legítimamente, pero el informe debe reconstruir el puente entre ellas antes de afirmar que el centro de la matriz justifica el múltiplo elegido. **Control de trazabilidad no superado aún.**

**Ponderación vigente en «Resumen de Valoración»:** DCF FY+3 **40 %**, EV/EBITDA **20 %**, EV/FCFF **10 %**, P/E **20 %**, P/FCFE **5 %** y P/OCF **5 %**. El resultado Base ponderado FY+3 es **US$104,15**; el valor intrínseco DCF Base **hoy** es **US$97,25**. El *Panel JMR unificado* ensaya ponderaciones alternativas **no certificadas**; no confundir sus US$105,09 u otros valores con el resumen seleccionado.

**Dictamen de múltiplos:** **sin certificación económica todavía**. Debemos distinguir una elección argumentada de un múltiplo, su procedencia verificable y su sensibilidad; no elevarlo a «correcto» porque el valor final se acerque al DCF.

# 6. Integridad del modelo y pequeñas discrepancias importantes

1. **Fuente de crecimiento:** 5,00 % en «Input sheet» frente a **~4,90 % efectivo** en «Escenarios e historias»/«Valuation output». Documentar cuál gobierna; no modificarlo dentro de la auditoría.
2. **Margen comparable:** el año 0 **17,56 %** tiene ajustes; series históricas y GAAP no se equiparan sin conciliación de conceptos.
3. **Sales-to-Capital:** la referencia interna **1,82×** y el supuesto **2,37×** deben normalizarse bajo idéntico cálculo.
4. **Reinversión temporal:** la fórmula usa el crecimiento del **año siguiente** por el rezago activado; no reemplazarla por una identidad del mismo año sin identificar la convención.
5. **Perpetuidad:** «Origen de los Supuestos» dice g = Rf, pero hoy **g 3 %** y **Rf 5,09 %**. Es un texto obsoleto.
6. **Múltiplos:** método de selección vigente de 19-oct no coincide con la descripción antigua ni con ciertos centros de las matrices de sensibilidad. Conciliar antes de certificarlos.
7. **Promedio de historias:** **US$94,16** es el promedio condicionado **sin disrupción** (45 % / 25 % / 15 % renormalizados a 85 %); incluyendo la probabilidad de disrupción 15 %, el esperado informativo es **~US$85,61**. El valor principal por política JMR sigue siendo **DCF Base US$97,25**, no ninguno de los promedios.
8. **Dilución, caja y deuda:** el puente de DCF registra **US$14.248 M** de deuda ajustada, **US$13.530 M** de caja/inversiones propias, **US$1.328 M** de activos no operativos, **~883 M acciones** en el denominador, e impacto residual de opciones. La selección de RSU de FY2025 es un **proxy**, no un saldo confirmado al 15-oct-2026; evitar doble contar awards. No equivale a certificación completa de instrumentos.
9. **Publicación:** el control de la hoja marca publicación **E2E pendiente**. Este documento **no verifica** que JSON, PDF, visor y bitácora estén sincronizados y **no publica nada**.
10. **Historial:** se usó únicamente la hoja vigente de 15-oct y los selectores de múltiplos actualizados en ella a 19-oct. Los materiales de 18-oct con DCF diferente permanecen como **antecedente**, no se incorporaron a las cifras del presente análisis. No se trasladaron ni eliminaron archivos originales.

# 7. Qué confirmaría o refutaría la historia en una nueva revisión

| Pregunta a verificar | Evidencia que fortalecería el supuesto | Señal que exigiría revisarlo |
|:--|:--|:--|
| ¿Puede crecer ~4,9 %? | Ventas y TM$ consistentes, branded checkout estable/mejorando, Venmo monetizando | TPV sube, pero ingresos / TPV y TM$ se desaceleran de forma persistente |
| ¿Se recuperará a 19,64 % EBIT? | Trimestres con menor peso de costos transaccionales relativos y expansión GAAP comparable | Margen GAAP permanece ~16–17 % sin puente creíble de recuperación |
| ¿Es defendible 2,37× Sales-to-Capital? | Series de inversión neta y ventas incrementales normalizadas que demuestran eficiencia | Se necesita más capital, producto, co-marketing y cumplimiento que el modelado |
| ¿Persistirá el ROIC terminal > WACC? | Retornos incrementales consistentes, poder de monetización, retención comercial | Competencia erosiona márgenes, aumentan incentivos y costes de integración |
| ¿Es justificado el rerating de múltiplos? | Historial y comparables auditables con denominadores homogéneos y puente a FY+3 | Comparables de negocios distintos, métricas no certificadas o rerating como única explicación |

**La siguiente evidencia crítica será una actualización de resultados posterior al 30-jun-2026**, usando cifras SEC comparables por trimestre y sin sustituir el conjunto congelado de datos de esta auditoría. Evitar considerar noticias de mercado o opiniones de analistas como pruebas suficientes de la tesis.

# 8. Conclusión independiente

**Crecimiento 4,9 %: defendible, con verificación pendiente.** Los ingresos recientes no lo contradicen; la calidad del crecimiento sí es una preocupación al observar volumen versus monetización.

**Margen 19,64 %: exige evidencia adicional.** La evolución reciente GAAP va en sentido opuesto; es uno de los supuestos con mayor peso económico que debe defenderse con costos, mix y márgenes normales.

**Reinversión 2,37×: posible, pero no justificada todavía.** La empresa tiene rasgos de escala y bajo capital físico, pero no se ha confirmado que eso autorice la mejora proyectada frente a 1,82× comparable.

**ROIC terminal 15,58 %: principal pregunta de permanencia.** La rentabilidad perpetua excede mucho el costo de capital; aproximadamente **55,6 % del valor operativo del DCF** depende de flujos posteriores al año diez.

**Múltiplos: auditar al final y por separado.** No son mecanismo para arreglar o confirmar un DCF; las brechas frente a múltiplos actuales merecen fuentes y razones específicas.

**Decisión propuesta:** **mantener intacta la valoración**. Clasificar esta auditoría como **«observaciones significativas / pendiente de validación económica»**, sin aprobar ni desaprobar automáticamente el precio objetivo. Si más adelante se deciden cambios, abrir un análisis de sensibilidad o nueva versión aprobada por el usuario; nunca hacerlo desde el módulo de auditoría.

## Resumen narrado breve (para escuchar)

«La historia de la valoración de PayPal es la de una empresa madura que intenta recuperar el poder de generar utilidades con los pagos que procesa. Su crecimiento proyectado, cercano al cinco por ciento, es razonable si miramos los ingresos recientes; sin embargo, procesar más pagos no le está dando todavía un crecimiento equivalente de rentabilidad. El supuesto más difícil de justificar es el margen operativo del diecinueve coma sesenta y cuatro por ciento, que supera el máximo de la serie histórica usada en la valoración. Además, el modelo supone que para crecer la empresa necesitará relativamente poca reinversión y que conservará ventajas competitivas durante muchos años. Como más de la mitad del valor operativo calculado proviene de flujos después del décimo año, esa ventaja es clave. Por último, los múltiplos elegidos suponen que el mercado volverá a pagar bastante más por las utilidades y el flujo de caja. Mi conclusión es que debemos conservar la valoración, pero exigir evidencia especialmente del margen, la reinversión y el retorno sobre el capital antes de considerarlos suficientemente justificados».

# 9. Fuentes y límites de certificación

**Fuentes externas primarias:**

- [PayPal 10-K 2025, SEC (ingresos FY2023–FY2025, negocio, estrategia, riesgos)](https://www.sec.gov/Archives/edgar/data/1633917/000163391726000024/pypl-20251231.htm).
- [PayPal 10-Q 2T26, SEC (estados al 30-jun-2026, ingresos, gastos, TPV, capex, intereses)](https://www.sec.gov/Archives/edgar/data/1633917/000163391726000082/pypl-20260630.htm).
- [PayPal, resultados 2T26, SEC (GAAP y non-GAAP, TM$, guidance)](https://www.sec.gov/Archives/edgar/data/1633917/000163391726000080/pypl2q-26earningsrelease.htm).
- [PayPal, anuncio de reorganización de 29-abr-2026](https://about.pypl.com/news-details/2026/PayPal-Announces-Strategic-Reorganization-to-Accelerate-Growth/default.aspx).

**Fuente del modelo auditado:** [Hoja Google Sheets PYPL vigente](https://docs.google.com/spreadsheets/d/1LI1LHXYFiCqg5i1_DDzs53Rd4eKv4zhDex2pxSvKuCs/edit): «Input sheet», «Valuation output», «Escenarios e historias», «Crecimiento y Márgenes», «Eficiencia de capital», «Origen de los Supuestos», «Selección económica PYPL», «Sensibilidad económica múltiplos», «Auditoría económica PYPL», «Resumen de Valoración», «Panel JMR unificado». Las sensibilidades condicionadas proceden del informe previo de auditoría y no fueron reejecutadas con un motor independiente en esta ampliación.

**Límites:** No certificamos aquí que la serie histórica interna o los pares tengan proveedores, cortes y normalizaciones perfectos; no cotejamos cada enlace de fórmula contra un motor de valoración independiente; no recalcamos todas las sensibilidades; el juicio es económico, no una opinión de auditoría contable formal. Las predicciones describen escenarios del analista, no guidance de PayPal. No constituye recomendación personal de inversión.