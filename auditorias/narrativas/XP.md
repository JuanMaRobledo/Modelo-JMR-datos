# Auditoría económica narrativa — XP Inc. (XP)

Revisión **XP-JMR-20261026-R2** · Corte informativo 26-10-2026 · Finanzas 30-06-2026 · BRL millones, salvo acción y porcentajes.

**Estado: PENDIENTE de validación JMR integral.** Cálculo económico provisional completo; auditoría condicionada. Publicación autorizada por el usuario; auditoría condicionada visible.

## 1. Ficha de auditoría y alcance

**Objeto:** valoración y research R2, estados consolidados XP Inc., acción A cotizada NASDAQ y derechos económicos equivalentes supuestos para B. Referencia informativa 26-10-2026; finanzas 30-06-2026. Moneda de proyección BRL millones; salida USD/acción.

**Naturaleza del trabajo:** revisión económica y reproducibilidad numérica realizada por el mismo asistente en fase posterior al modelo. El motor Python y las fórmulas Google Sheets son implementaciones separadas; no hay auditor externo independiente ni opinión de auditoría contable. El término “independiente” en pruebas se refiere a recálculo e identidad alternativa, no independencia profesional. Se leyó el contrato vigente, incluidos los anexos de precisión y matrices.

**Dictamen:** PENDIENTE de validación integral. Hay estimación provisional calculada y tres informes; no se han cerrado controles de capital legal, prima de riesgo, persistencia de retornos y adaptación de plantilla. La publicación fue autorizada posteriormente por el usuario; no modifica este dictamen económico condicionado.

## 2. Resumen ejecutivo y relato económico central

[OBSERVADO] La economía central de XP sigue siendo captar y monetizar patrimonio, combinando distribución con otros servicios financieros. Activos de clientes crecen 12%, clientes 1% y el take rate desciende a 1,20%. La franquicia conserva tracción, pero esa combinación no permite deducir crecimiento proporcional de ingresos o poder de precio ilimitado. [ER26]

[MODELO] La historia Base asume CAGR 8,40% de ingresos en cinco años, margen EBT 31% en año 5 y 29,5% maduro, fiscalidad 20% y ROE 17,77% maduro. Genera USD 13,53 por acción y USD 8,79 con MOS 35%. La historia es posible y económicamente legible, pero depende de que capital y tributación no absorban una fracción del beneficio mayor a la prevista.

[OBSERVADO] Se corrigió un error previo de alineación de años y se recuperó el Pilar 3 regulatorio. El BIS 13,28% no equivale al 20,3% gerencial. [Pilar] [ER26] [INFERENCIA] Esto refuta la idea de distribuir automáticamente todo el exceso aparente frente a una meta gerencial. El modelo no libera ese supuesto exceso inicial.

[NO VERIFICADO] El porcentaje 50% de retención consolidada que se hace llegar a CET1 no es un puente legal. La regla de precisión prohíbe sustituir ese puente por una tasa fija sin respaldo. Tampoco la información de mercados justifica por sí sola los 2 pp adicionales de prima país. Las pruebas cuantificadas muestran que ambas decisiones pueden mover materialmente el resultado; ninguna debe quedar escondida tras un barrido de errores limpio.

[INFERENCIA] El dictamen condicionado se debe a la calidad del soporte de supuestos y a controles estructurales abiertos. No se cuestiona una suma o división que ya concilia, ni se abandona el informe por esas reservas. La salida útil es una valoración trazable y falsable que puede revisarse cuando se cierre el puente de capital y el riesgo contemporáneo.

## 3. Trazabilidad, integridad y jerarquía de evidencia

La jerarquía aplicada es: estados auditados 20-F para series anuales, estados IFRS1H26 y notas para corte, release para métricas gerenciales, Pilar 3 para conglomerado prudencial, mercado/oficiales para FX y referencias de riesgo, y juicio explícito para proyección. Los tres documentos consumen el mismo JSON R2. Las fuentes se enumeran en §18; el Nivel 2 contiene números completos. [20F25] [FS26] [ER26] [Pilar]

|Área|Integridad revisada|Limitación|
|---|---|---|
|IFRS / escala|Miles BRL→millones; año/semestre/LTM separados|Corte financiero envejecido cuatro meses|
|Capital|Perímetro prudencial separado|Fungibilidad futura no probada|
|Precio / FX|Referencias fechadas y congeladas|Intradía no equivale a precio vivo|
|Acciones|Emitidas−tesorería y RSU/PSU|Corte junio; no registro definitivo octubre|
|Hipótesis|Supuestos se conservan separados de datos|No se vuelven datos por entrar en una celda|
|Versiones|R2 reemplaza números históricos erróneos de R1|R1 no es valoración comparable|

Las cifras auditadas pertenecen al emisor; la auditoría de los estados no se extiende a esta proyección. La información no disponible se conserva N/D y no como cero. Los archivos originales completos no se redistribuyen en el paquete: se entregan enlaces, extracciones y cálculos propios.

## 4. Historia financiera: diez años y punto de partida

|FY|Ingresos|EBT|Beneficio controlador|Patrimonio controlador|CFO|ROE promedio anual|
|---|---|---|---|---|---|---|
|2016|1.252,00|374,00|189,00|N/D|N/D|N/D|
|2017|1.906,65|575,51|413,87|N/D|262,37|N/D|
|2018|2.958,45|640,73|461,44|2.084,78|-456,75|N/D|
|2019|5.127,81|1.544,11|1.080,48|7.153,40|-3.813,99|23,39%|
|2020|8.151,60|2.421,41|2.076,43|10.894,61|1.510,73|23,01%|
|2021|12.077,11|3.815,17|3.589,42|14.416,84|-4.020,33|28,36%|
|2022|13.347,39|3.444,66|3.579,05|17.035,74|1.803,88|22,76%|
|2023|14.860,10|3.936,35|3.898,70|19.449,35|8.127,30|21,37%|
|2024|17.030,86|4.985,97|4.513,41|20.043,56|11.178,96|22,86%|
|2025|18.398,60|5.448,56|5.169,79|23.546,70|12.044,83|23,72%|

[OBSERVADO] La historia cubre resultados 2016–2025, pero 2016 es selección redondeada y no diez estados íntegros. CFO 2017–2025 y balances disponibles no justifican marcar cobertura completa a diez años para todas las partidas. La media ROE solo se calcula cuando hay patrimonio de apertura. [20F19] [20F21] [20F23] [20F25]

[MODELO] LTM junio: ingresos 19.122,419; EBT 5.726,543; beneficio grupo 5.313,855 y controlador 5.316,803. El LTM se rehízo como FY25+1H26−1H25. La corrección histórica R2 cierra el desfase de columnas detectado en R1; no cambió el punto LTM que alimentaba el valor, pero sí impide utilizar las comparaciones tempranas sin corrección. Las cifras de balances IR antiguos tienen menor evidencia que el último balance IFRS; se conserva ese límite visible.

|Ratio y definición|FY2025|Media FY23–25|Media FY21–25|Media FY16–25|
|---|---|---|---|---|
|Margen EBT IFRS|29,61%|28,46%|28,56%|28,43%|
|Margen neto controlador|28,10%|26,95%|27,47%|23,63%|
|ROE sobre patrimonio medio|23,72%|22,65%|23,81%|N/D|
|ROIC, deuda neta/EBITDA, S2C industriales|N/A financiero|N/A|N/A|N/A|

## 5. Crecimiento de ingresos: de la historia a la proyección

[MODELO] El crecimiento Base 8/10/9/8/7% se acerca al crecimiento de ingresos reciente, muy por debajo del despegue histórico. El mecanismo supuesto es captación positiva, mayor profundidad por cliente y mezcla suficiente para compensar tarifas. Se exige que el costo de sostener la red y el crédito no se lleve la mejora. Crecer activos con ingreso por activo decreciente es la principal evidencia contraria. [ER26]

[HIPÓTESIS] La convergencia hacia 5% nominal BRL en año 10 no procede de guía de XP. Implica crecimiento real moderado bajoinflación 3%. Una curva suave es convención de modelación, no observación del ciclo; debe revisarse ante captación negativa o cambio estructural de mezcla.

|Métrica y horizonte|Historia 3/5/10 años y LTM|Valor modelo y celda|Industria y fuente|Exigencia causal|Contraevidencia / juicio|Impacto ejecutado|
|---|---|---|---|---|---|---|
|Crecimiento 1–5|Despegue alto; FY2025/LTM en Nivel 2;2016 redondeado|8/10/9/8/7%; XP FCFE C42: G42|Activos+12%, clientes+1%; ER26|Captación y venta cruzada con monetización|Take rate 1,20%; erosión posible|Matriz crecimiento/margen 75 celdas; inversa CAGR 15,36%|
|Convergencia 6–10|Fase madura diferente aldespegue|B42 g=5%; H42: L42|Sin percentil financiero homologado|Crecimiento real~1,94% y retención suficiente|No existe guía oficial 5%|Matriz ROE×g; g 4,5–5,5% explícita en Nivel 2|

## 6. Márgenes operativos y normalización de beneficios

[OBSERVADO] El EBTLTM/ingreso es 29,94675%, mientras el margen gerencial 2Q es 32%. [MODELO] Se proyecta una mejora moderada a 31% y luego 29,5%, sin usar como “dato” una expansión automática por software. El gasto tecnológico no puede capitalizarse en blo que: parte ya está en intangibles y parte presta servicios corrientes. Falta separación para cerrar R&D converter. [20F25] [FS26]

[HIPÓTESIS] La fiscalidad sube de 7,21% LTM a 12% en año 5 y 20% madura. Hay evidencia de tasas bajas y estructura fiscal compleja, pero 20% no es guidance ni un contrato con el fisco. El escenario 34% se aplica como prueba desde año 6, no reescribe retroactivamente años 1–5; reduce valor 2,35% después del ajuste de capital del motor. Efecto moderado no equivale a confirmación fiscal.

|Métrica y horizonte|Historia 3/5/10 años y LTM|Valor modelo y celda|Industria y fuente|Exigencia causal|Contraevidencia / juicio|Impacto ejecutado|
|---|---|---|---|---|---|---|
|EBT margen 5 /10|Medias históricas en §4; LTM 29,95%|B43=31%; N43=29,5%|2Q gerencial 32%, no homólogo; ER26|Escala cubre incentivos, riesgo, cumplimiento|Presión de tarifas / mezcla|Matriz crecimiento×margen con Δmargen±3 pp|
|Impuesto 5 /10|ETRLTM7,21%; histórico bajo y variable|B44=12%; N44=20%|Fiscalidad específica grupo; FS26 notas|Normalización parcial sostenible|Régimen fiscal podría cambiar|ETR terminal 34%:13,21 USD;−2,35%|
|I+D / leases|Software IFRS; lease 427,093 m|Sin segunda capitalización industrial|20F25 / FS26|Separar mantenimiento y creación de activo|Sin vida útil ni serie de I+D aislada|NO VERIFICADO conversor original; impacto I+D no acotado|

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

[MODELO] El crecimiento requiere patrimonio para el beneficio siguiente y reserva para RWA. El motor toma el máximo, no suma dos requerimientos si ambos financian la misma actividad. Año 1 Base: beneficio 5.722,797 menos retención 4.146,769 da FCFE 1.576,028. El libro se reconcilia por clean surplus modelado; OCI, otras emisiones y recompras futuras se fija en cero; es HIPÓTESIS, no dato reportado.

[OBSERVADO] Pilar 3 regulatorio aporta CET1 7.675,252 m, Tier 1 10.630,547 m y total 13.268,802 m frente RWA 99.904,171 m. [NO VERIFICADO] Falta cerrar patrimonio controlador + NCI − deducciones, perímetro seguros y propiedad contra capital prudencial, además de restricciones Tier 1, total, apalancamiento y AT1/Tier 2. Repartir automáticamente 50% de retención a CET1 no resuelve ese puente y contradice el estándar exigido. No se certifica la proxy por el hecho de que produzca ratios positivos. [Pilar] [FS26]

[INFERENCIA] S2C y ROIC industriales no son comparables útiles para deuda operativa de intermediación. ROE ayuda a dimensionar crecimiento, pero no sustituye un piso regulatorio vinculante. La prueba asignación CET1 al 20% reduce valor 24,85%; no se conoce un límite adverso defendible. Es un hallazgo blo queante de validación integral, no una salvedad pequeña.

|Métrica y horizonte|Historia 3/5/10 años y LTM|Valor modelo y celda|Industria y fuente|Exigencia causal|Contraevidencia / juicio|Impacto ejecutado|
|---|---|---|---|---|---|---|
|Retención 1–10|Libro controlador 24.831,073; ROE 25 medio 23,72%|Fila 51 retención; fila 52 libro Base|FS26 /20F25|Rentabilidad prevista exige capital próximo|Capital legal no es libro económico|Retención extra 1.000 m:−2,23%;3.000 m:−6,69%|
|CET1 y RWA|7,68%; RWA 99.904,171 m a junio|B20: B23 y B33=50% asignación|Pilar KM1 p.5|Transferencias, deducciones y propiedad compatibles|Proxy fija prohibida sin puente|Asignación 20%:10,17 USD;−24,85%; RWA×1,5:−3,57%|
|Capital no liberable /retornos|ROE histórico≠capital libre|No liberación de book inicial; ROE efectivo puede caer|Pilar/FS26|Respeta capital retenido improductivo|Pisos Tier 1, total, apalancamiento no integrados|Impacto extremo sin acotar: no VERIFICADO|
|Asignación de capital|Recompras 995,951; dividendos 517,886 en 1H|Proyecciones futuras sin otras recompras/OCI|FS26 flujos|SBC y aportes coherentes por acción|Optimista año 1 requiere 1.646,60 m aporte|PFCFE Optimista año 1 N/A; participación proporcional supuesta|

## 8. Costo del capital y riesgo

[MODELO] Se usó un par coherente de Rf/ERP ajustados de septiembre y moneda BRL para flujos. La beta financiera global 0,98 es una proxy de negocio ya apalancada; no se interpreta toda financiación de clientes como deuda industrial. El país se asocia a la exposición brasileña y no a NASDAQ. El producto anual reproduce descuento variable. [ERP] [Beta] [CRP]

[NO VERIFICADO] La sobretasa 2 pp por repricing no está medida mediante curva soberana contemporánea, ni la exposición lambda 1 contrastada con ganancias y activos por entidad. El anexo de precisión no permite primas arbitrarias. Por ello la prima actual no queda certificada, aunque su hipótesis y sensibilidad estén visibles. El contraste beta 1,03 es diagnóstico de proveedor, no una regresión propia con muestra/índice/frecuencia reproducidos. Detailed original y B14=E63=Input!B36 no están cerrados.

[INFERENCIA] Eliminar 2 pp sube valor 26,67%, más que muchas mejoras operativas cercanas. Esto demuestra que la conclusión depende materialmente del descuento; no demuestra que 0% o 3% sean límites válidos. No se añaden primas diferentes por historia que dupliquen el mismo deterioro ya incorporado en flujos.

|Métrica y horizonte|Historia 3/5/10 años y LTM|Valor modelo y celda|Industria y fuente|Exigencia causal|Contraevidencia / juicio|Impacto ejecutado|
|---|---|---|---|---|---|---|
|Rf /ERP madura|Corte mensual 30-09-2026; no octubre diario|B11=5,07%; B12=3,91748%|ERP Impl premium C44/H44|Moneda y riesgo coherentes|Ancla enero no cotización reciente|Par ajustado usado coherentemente|
|Beta /convergencia|Sector enero 0,98; no cálculo local propio|B13=0,98→1 maduro|Betas Global, brokerage|Mezcla de XP comparable y madura|Crédito creciente puede cambiar beta|Beta 1,03:13,40 USD;−0,96%|
|Riesgo Brasil|CRP enero 3,24%; shock octubre no cuantifica spread|B14=3,24%; B15=2 pp; lambda 1|CRP /Reuters contexto|Prima actual y exposición deben sustentarse|2 pp HIPÓTESIS sin fuente numérica|Extra 0 pp:17,14 USD;+26,67%; extra 3 pp:12,22 USD;−9,66%|
|Moneda / FX|Resultado BRL; cotización USD|B16=3%; B17=2,3%; B18=5,5007|PTAX +anclas analista|Paridad nominal sin doble inflación|Inflación futura distinta|FX 6:12,40 USD;−8,32%|

## 9. Convergencia y valor terminal

[MODELO] La tasa madura supera a g:15,0091% frente 5%. Base ROE 17,77% implica ventaja residual 2,76 pp. El valor terminal pesa 42,95% del equity; es menor que la mitad pero sigue siendo material. El FCFE terminal financia crecimiento del libro existente y no una versión del libro que mágicamente desaparece. El motor admite pérdida de retorno en Disrupción por capital retenido y no impone ROE≥Ke para esconder destrucción.

[NO VERIFICADO] El 17,77% es retorno de industria EEUU, no una media global homologada para XP ni evidencia suficiente de moat eterno. Se requiere rentabilidad incremental, costos de red y eficiencia de capital coherentes con ese estado. [ROE] Quitar el exceso terminal lleva a 11,92 USD,−11,90%; por eso la etiqueta de ventaja moderada del research no resuelve el control de retorno.

[INFERENCIA] La continuidad económica libro 10→flujo 11 está calculada; la continuidad legal capital→dividendo no. La prueba de capital fija no demuestra que todos los requisitos se estabilicen con la misma tasa. No se ejecutó una simulación jurídica entidad por entidad a 20 años; ese trabajo no se declara superado.

|Métrica y horizonte|Historia 3/5/10 años y LTM|Valor modelo y celda|Industria y fuente|Exigencia causal|Contraevidencia / juicio|Impacto ejecutado|
|---|---|---|---|---|---|---|
|g y madurez|Escala reciente mayor que fase inicial; sin percentil sectorial comparable|B42=5%; ingresos 10→11 al 5%|Ancla inflación analista; Base Rates metodología|Crecimiento real y capital sostenible|RWA o márgenes pueden no estabilizar|Matriz KeT×g 5×5; no shock macroeconómico completo|
|ROET /ventaja|ROE 25 medio 23,72%; referencia EEUU17,77%|N45=17,77%; L45 alcanza estado|ROE brokerage EEUU enero 2026|Ventaja de distribución persiste|Tarifas y competencia contradicen permanencia|ROET=Ke:11,92 USD;−11,90%|
|TV y retención 11|Libro 0 de balance verificado; futuro hipotético|B59FCFE11=6.758,281; B60TV=67.521,394 m|Motor financiero R2|NI11−g×book 10 consistente|Puente legal al capital no demostrado|VT42,95% de equity; fórmula reconciliada|
|Disrupción|No hay experiencia comparable certificada|C: ROE efectivo 10,39%<Ke; g 2%|Hipótesis causal propia|No liberar capital improductivo|Liquidación no estimable con evidencia actual|Valor 6,99 USD; separado del promedio|

## 10. Validación independiente del valor intrínseco

[MODELO] El recálculo Python suma BRL 22.263,12 m de flujos y 16.757,35 m de terminal. Equity BRL 39.020,47 m /524,271752 m acciones /5,5007=USD 13,53063065. La hoja nativa obtiene el mismo resultado. La identidad de exceso de retornos parte de libro inicial más VANde beneficios en exceso del cargo a Ke, con corrección terminal de libro; reproduce los cuatro casos con error<1e−8USD.

[INFERENCIA] Son dos pruebas complementarias: implementación separada verifica cálculo y residual income verifica identidad financiera bajo clean surplus. Ambas comparten entradas económicas. No validan por sí solas crecimiento, riesgo ni capital legal. El valor se conserva como estimación provisional y no se ajusta para aproximarlo a mercado o emitir aprobación.

|Métrica y horizonte|Historia 3/5/10 años y LTM|Valor modelo y celda|Industria y fuente|Exigencia causal|Contraevidencia / juicio|Impacto ejecutado|
|---|---|---|---|---|---|---|
|Equity /acción Base|LTM reconstruido y book 0 verificado|B62 equity; B64USD13,53063065|Python vs Google Sheets|Flujos atribuibles y denominador consistentes|Capital/legal y Ke abiertos|Diferencia numérica Base 0 en lectura final|
|Acciones y claims|Junio 507,483079 m básicas;17,672287 m RSU/PSU|B8: B10; B28=524,271752 m|FS26 notas; Cancel agosto|Misma economía A/B, vesting 95%|Registro octubre y condiciones PSU no cerrados|100% vesting−0,1683%; agosto−0,1936%; suma 0,3619%|
|Prueba independiente|Mismos datos; lógica de exceso de retornos|residual_income_value_usd en JSON|Clean surplus modelado|Libro y flujo cierran sin puente industrial|No independencia externa ni control regulatorio|Cuatro historias tolerancia<1e−8|

## 11. Cuatro historias y probabilidades

|Historia|Probabilidad previa|CAGR ingresos 1–5|EBT año 5 / estable|ROE estable efectivo|g BRL|Valor USD|Peso VT|
|---|---|---|---|---|---|---|---|
|Base · expansión con normalización fiscal|45,00%|8,40%|31,00% / 29,50%|17,77%|5,00%|13,53|42,95%|
|Conservadora · presión competitiva y menor retorno|22,50%|4,19%|28,00% / 27,00%|15,01%|5,00%|10,43|37,40%|
|Disrupción · Deterioro de los fundamentales|10,00%|-3,61%|20,00% / 18,00%|10,39%|2,00%|6,99|19,73%|
|Optimista · mayor monetización y escala|22,50%|12,99%|34,00% / 32,00%|17,77%|5,00%|15,38|53,35%|

Las historias combinan ingresos, margen y retornos distintos; no son un multiplicador arbitrario del valor Base. El escenario Optimista requiere financiación inicial y un terminalmás importante 53,35%; el Conservador pierde exceso de retorno. Disrupción mantiene ROE efectivo inferior al costo, sin recuperación obligatoria.

Las probabilidades 45/22,5/10/22,5% son priors de trabajo, no frecuencias estimadas. El promedio ordinario renormaliza Base/Conservadora/Optimista y excluye Disrupción; no debe rotularse “valor esperado total”. No se modificaron pesos por una noticia sin señal predefinida. Se conservael 10% de Disrupción en suhistoria y se excluye de las familias ordinarias de matrices.

## 12. Valoración por múltiplos: prueba independiente y secundaria

|Método|Histórico A FY2025|Factor tasas|Ancla fundamental C Base|Aplicado Base|Peso|Juicio|
|---|---|---|---|---|---|---|
|PE|9,04|0,877|7,18|7,18|70,00%|Menor A ajustada / C; B pares no verificada|
|PS|2,54|0,877|1,70|1,70|0,00%|Menor A ajustada / C; B pares no verificada|
|PBV|1,98|0,877|1,28|1,28|30,00%|Menor A ajustada / C; B pares no verificada|
|PFCFE|N/D|N/A|9,99|9,99|0,00%|Solo C; diagnóstico sin historia homogénea|
|EV/EBITDA|N/A|N/A|N/A|N/A|0% financiero|Financiación operativa: EV industrial no homogéneo|
|EV/FCFF|N/A|N/A|N/A|N/A|0% financiero|No hay FCFF industrial interpretable|
|P/OCF|N/A|N/A|N/A|N/A|0% financiero|Intermediación domina OCF; no se utiliza como FCFE ni se fabrica OCF prospectivo|

[OBSERVADO] Ancla Ase reconstruyó con precio, FX yacciones de FY2025; un solo cierre no cumple una mediana de ciclo. Precio 16,37 vs 16,16 entreproveedores difiere 1,30%. Como Cqueda por debajo deambas Aajustadas, esa discrepancia no cambia la ancla elegida, mientras el ciclo histórico ypar Bsiguenno verificados.

[MODELO] Los ratios fundamentales siguen las fórmulas forward del contrato sin(1+g)extra. El motor anterior tenía ese factor adicional en PE/PFCFE y PV; se corrigió en Python yhojaantes de congelar informes. Noafectó DCFBase. La salida actual Base PE7,17974×, PV1,69536×, PBV1,27584×y PFCFE9,99091×. Las tres lecturas por método sonprecio futuro BRL exdistribuciones, VPUSD del paquete ypesos. Están íntegros en Nivel 2.

[INFERENCIA] PE70% y PBV30% evitan ponderar más deuna vez métricas correlacionadas, pero son criterio analítico, no optimización probada. PBVdepende de clean surplus futuro supuesto. PFCFE es Csin historialhomogéneo ypesocero. El resultado secundario Base 13,32 USD no es una auditoría independiente del DCF: Ccomparte ROE, g, Ke. Se consideraronlas siete familias yse excluyeronlas industriales por el negocio financiero, no porque dieran unprecio incómodo. Falta una prueba relativa conpares y ciclos homologados.

## 13. Sensibilidades económicas y escenarios alternativos

|Prueba ejecutada, una variable salvo indicación|Valor USD|Cambio vs Base|
|---|---|---|
|sin_sobretasa_pais|17,14|26,67%|
|sobretasa_pais_3 pp|12,22|-9,66%|
|sin_moat|11,92|-11,90%|
|impuesto_terminal_34 pct|13,21|-2,35%|
|vesting_100 pct|13,51|-0,17%|
|acciones_emitidas_agosto_sin_ajuste|13,50|-0,19%|
|capital_adicional_1 bn|13,23|-2,23%|
|capital_adicional_3 bn|12,63|-6,69%|
|beta_regresion_1_03|13,40|-0,96%|
|CET1_9 pct|13,35|-1,33%|
|RWA_crece_50 pct_mas|13,05|-3,57%|
|asignacion_CET1_20 pct|10,17|-24,85%|
|FX_6|12,40|-8,32%|

Las pruebas son cambios ejecutados por separado contra Base. No se suman todos los porcentajes ni se presentan como escenarios probables. Capital retenido adicional 1.000/3.000 m es pérdida económica de disponibilidad en año 1, no límite jurídico de lo que pudiera quedar inmovilizado. El agregado conservador 0,362% corresponde solo a las dos salvedades deacciones, no ala reserva global.

Sensibilidad DCFBase: tres 5×5 centros 13,53063065; KeT×g, y ROET×g, ycrecimientoprimeros 5 años×margen. Preciofechado 15,37: inversaΔ6,963658 pp, CAGR 15,3592%. Tabla 2 márgenes×2 betasen Nivel 2. La inversa mantiene capital yrentabilidad fijados; no identifica una previsión única demercado.

Matricespor múltiplos:21 casos ordinarios por familia; doce 5×5 convalor por acción ynueve N/Afinancieros explicados. Eje Yratios reales ×; eje Xfundamental año 3 BRL m; centros concilian con VPpropio delmétodo. La familia deratios económicos se conserva como soporte en hoja/JSON yno se despliega. No se forzó ningún centro al DCF. Son matrices calculadas al corte, no un motor completo de estrés macro; distribuciones intermedias quedan fijas enla prueba local demúltiplos.

## 14. Coherencia de hojas, cálculos y presentación

Se preservó la copia nativa de las 61 pestañas originales y se añadieron módulos financieros. Los resultados principales están en XPFCFEB64/B104/B144/B184; las nuevas matrices yel Nivel 2 identifican unidades y fechas. No se rotularonhojas heredadas como LISTOpara simular una integración. El formato local es_ES requirió separadores y decimales coherentes; elbarridofinal no contieneerrores efectivos enlas hojas nuevas leídas.

Prueba deperturbación: crecimientoaño 3Base 9%→10% mueve el valor 13,53063065→13,56550421 y los tres centros; restaurar 9% recupera 13,53063065. Verregistroadjunto. Los 116 resultados comparados incluyen 4DCF,75 sensibilidades,36 múltiplos/un N/Ayraíz inversa. Las matrices adicionales tienen recálculo ycentros propios documentados. No son prueba de interacción del usuario en la app.

|Control de plantilla / flujo|Estado y evidencia|Consecuencia|
|---|---|---|
|R&D converter|No verificado: desglose/vida útil pendiente|No aplicar ajuste inventado; no cierre integral|
|Operating lease converter|IFRS16 reconocido; sin doblecapitalización|Conversor industrialoriginal no certificado|
|Option value / Black–Scholes|RSU/PSU incluidos; no son opcionesvanilla|BSN/Aalclaimsimple; condiciones PSU pendientes|
|Cost of capital Detailed|Ke externo calculado; segmento/ERP geográfico no homologado|No se confirma B14=E63=Input!B36|
|Hoja→Python|Coincidencias yprueba entrada-salida|Verificación matemática únicamente|
|Auditoría visual|Formato API leído; sin revisión gráfica completa|No se certifica layoutcompleto|
|Importación/visor/publicación app|Publicación autorizada posteriormente; carga comprobada por registros, navegación visual limitada por autenticación|No se afirma flujo de producción correcto|

Flujo defendible ahora: evidencia→valoraciónfinanciera→researchconsumidor→auditoría→paqueterevisable. Laapertura decorrecciones de capital y riesgo es parte del resultado, no un cambio silencioso del valor después de lauditor. El flujo de la app requiere pruebas de contrato financiero/importador/visor y estado condicionado antes decualquier publicación.

## 15. Hallazgos priorizados y propuestas de corrección

|ID|Clase|Fuente / fecha / celda|Base|Alternativa e impacto|Agregado conservador|Decisión / estado|Corrección concreta|
|---|---|---|---|---|---|---|---|
|F1|A blo queante|Pilar/FS26, consulta 26-10; B20: B23/B33|Base CET1 asignación 50%|20%: USD 10,17;−24,85%|Agregado real no acotado|Puede cambiar valor/MOS; puentelegal no demostrado|Reconciliar libro→CET1 y Tier 1/total, seguros, AT1/Tier 2; no certificar proxy|
|F2|A blo queante|CRP/ERP/Reuters,26-10; B14: B15|CRP enero 3,24%+2 pp|Sinextra:17,14;+26,67%; extra 3 pp:12,22;−9,66%|No límites soberanos demostrados|Puede cambiar lecturafrente mercado|Sustituir sobretasa por exposición yprima contemporánea verificable|
|F3|B reserva material|ROE enero 26; N45|ROET17,77% EEUU|Ke: USD 11,92;−11,90%|No sumar con F1/F2|MOS baja a 7,75 enpruebasinmoat|Homologar referentes ydemostrar persistenciade ventaja|
|F4|B reserva material|FS26 tax; N44|ETR madura 20%|34% desde 6:13,21;−2,35%|Pruebaacotada, no peorcasolegal|MOS prueba 8,59; no cambialectura actual|Reconciliar régimenfiscal ysubsanarfechas/entidades|
|F5|A estructural|Contrato JMR yplantilla,26-10|Adaptadorfuera deceldas canónicas|Impactoapp/no equivalenciano acotado|No financiero porcentual|Impide estado VERIFICADO yapp confirmada|Formalizar excepciónfinanciera, conversores, Detailed eimportador|
|F6|C no blo queante|FS26/Cancel,26-10; B8: B10|Accionesjunio; vesting 95%|100%−0,1683%; agosto−0,1936%|Conservador 0,3619% (<3%)|<2% cadauno; MOS sin cambiolectura|Actualizar registro cuandoestédisponible; no restardosveces|
|F7|B reserva de prueba relativa|20F/mercado/pares,26-10; Múltiplos K: L|Uncierre 2025; BN/D|Cmenor que ambas Aprecios; discrepanciavalor 0 al no vinculante|Falta ciclo no acotado por método|No cambia DCF; no certificarval.relativa|Reconstruir ciclo y pares homólogos; mantener diagnóstico|
|F8|C corregido|20-Fyextracción R2,26-10; históricostabla|R1 desfase columnas|R2 realineado yreconciliado|DCFBase cambio 0 por LTM sin error|Cerrado; R1 no reutilizar|Usarúnicamente CSV/JSON histórico R2|
|F9|C corregido|Contrato 21-10; Múltiplos L4: L39|Factor(1+g)duplicadoenprototipo|Retirado; Base ponderada 13,32|DCFBase cambio 0|Cerradoantes de congelar|Conservar fórmula forward ycentros por método|
|F10|B cobertura / evidencia|20F19,26-10; histórico 2016|Selecciónredondeada 2016|Diezestados completos N/D|No cambio LTM; serie no homogénea|No certificarhistorial completo|Declarar cobertura real ypreservar N/D|

Clasificación aplicada según REGLAS§4B: las dos pruebas pequeñas deacciones son individualmente<2% yagregadas<3%, sin alterar identidad estructural ni lectura MOS; no blo quean por sí solas. F1/F2/F5 siguen abiertos porque son estructurales o su efecto material noestá acotado. No se transforma un faltante material en N/A. F3/F4 son reservas ejecutadas a alternativas concretas, sin afirmarque esos valores sean límites extremos. Se cierra la corrección F8/F9 sin reabrir una verificación numéricaque ya pasa.

## 16. Catalizadores, señales de refutación y seguimiento

|Variable|Actual y fuente|Favorece Base/Optimista|Favorece Conservadora/Disrupción|Frecuencia / evidencia|
|---|---|---|---|---|
|Activos clientes|BRL 1.535 bn; +12% interanual|Crecimiento >10% y captación positiva|<5% dos trimestres|ER26; trimestral|
|Take rate|1,20%|≥1,20% con mix rentable|<1,10% dos trimestres|ER26; trimestral|
|Clientes activos|4,772 m; +1%|>3% anual sin mayor subsidio|Cae y sube coste de captación|ER26; trimestral|
|Captación neta|BRL 28 bn trimestral|>20 bn trimestre|Negativa dos trimestres|ER26; trimestral|
|Margen EBT|29,95% LTM IFRS; 32% 2Q gerencial|≥30% IFRS comparable|<27% dos trimestres|FS26; trimestral|
|ROE|23,72% FY25 medio; 22,5% 2Q ajustado|≥20% medio homogéneo|<Ke BRL de forma persistente|20F25 / ER26; trimestral|
|CET1 regulatorio|7,68%; holgura 0,68 pp reportada|Holgura crece sin emisión|<0,5 pp de holgura|Pilar KM1; trimestral|
|Fiscalidad|7,21% ETR LTM|Convergencia ordenada ≤20%|>25% sin compensación|FS26; trimestral|
|Crédito expandido|BRL 77,9 bn; +16%|Rentabilidad neta cubre capital/pérdidas|Pérdidas crecen más que ingresos|ER26 y notas IFRS; trimestral|
|Capital por acción|SBC + recompras + dividendos|Libro y FCFE por acción crecen|Distribuir exige emisión recurrente|FS26 / 20-F; semestral|


|Fracaso posible|Mecanismo que rompe la historia|Señal observable|
|---|---|---|
|Activos crecen sin monetización|Compresión de comisiones neutraliza captación|Take rate <1,10% y clientes estancados|
|Capital queda atrapado|Resultados consolidados no suben a la matriz|CET1 y transferencias divergen de retención|
|Crédito desplaza la plataforma|Crece riesgo y financiación más que comisión|Pérdidas crediticias y RWA/ingresos aumentan|
|ROE se vuelve ordinario|Bancos y digitales erosionan diferenciación|ROE converge a Ke o por debajo|
|Brasil cambia el costo del capital|FX, inflación y riesgo soberano encarecen descuento|Primas y financiación permanecen elevadas|

El próximo reporte oficial debe actualizar la evidencia financiera y prudencial en conjunto. Una tarifa favorable no resuelve capital; un dividendo puntual no prueba libertad de distribución futura; un descensodelspreadno prueba ventaja comercial. Cada señal debe modificar la variable pertinente y mantener registro de probabilidades. Las fechas futuras se dejarán N/Dhasta confirmación del calendario oficial.

## 17. Dictamen económico y resumen para escuchar

**Dictamen económico: PENDIENTE / auditoría condicionada.** El modelo es reproducible ylas historias son interpretables, pero el punto Base no cumple aún la validación integral JMR. No se declara que el negocio esté mal valorado por el mercado ni que el flujo de publicación esté correcto. La reserva principal es demostrar flujos distribuibles bajo todos los requisitos de capital; también se necesita un costo del equity mejor sustentado y confirmar la adaptación estructural.

**Resumen para escuchar:** XP sigue siendo una plataforma rentable que capta patrimonio, pero más activos no garantizan más dinero para el accionista. El modelo financiero estima trece dólares con cincuenta y tres centavos por acción, antes de exigir el margen de seguridad. Los cálculos coinciden entre la hoja y un motor separado. La reserva importante está en otro lugar: todavía falta demostrar cuánto beneficio puede convertirse legalmente en capital y distribución, y sustentar la prima adicional de riesgo de Brasil. Cambiar esas hipótesis mueve materialmente el resultado. También se supone una ventaja de rentabilidad madura que necesita evidencia comparable. Por eso entregamos el valor y sus pruebas como estimación condicionada; no como una certificación ni como una recomendación de inversión.

## 18. Fuentes primarias, limitaciones y registro de versión

|ID|Fuente y alcance|Consulta|Enlace|
|---|---|---|---|
|20F25|XP, 20-F FY2025; publicado 29-04-2026, estados consolidados y notas|26-10-2026|[Abrir](https://www.sec.gov/Archives/edgar/data/1787425/000207097926000182/xp-20251231.htm)|
|FS26|XP, estados IFRS 1H26, publicado 17-08-2026; resultados, balance, flujos y notas|26-10-2026|[Abrir](https://www.sec.gov/Archives/edgar/data/1787425/000095010326012482/dp251887_ex9901.htm)|
|ER26|XP, release 2Q26, publicado 17-08-2026; cifras gerenciales y conciliación|26-10-2026|[Abrir](https://www.sec.gov/Archives/edgar/data/1787425/000095010326012481/dp251884_6k-ex9901.htm)|
|Pilar|XP, Pilar 3 2T26, KM1 página 5, capital prudencial|26-10-2026|[Abrir](https://www.xpi.com.br/documentos/pilar-3-gerenciamento-de-riscos-e-capital-2t26/)|
|20F23|XP, 20-F FY2023; publicado 26-04-2024|26-10-2026|[Abrir](https://www.sec.gov/Archives/edgar/data/1787425/000162828024018424/xp-20231231.htm)|
|20F21|XP, 20-F FY2021; publicado 13-04-2022|26-10-2026|[Abrir](https://www.sec.gov/Archives/edgar/data/1787425/000162828022009080/xp-20211231.htm)|
|20F19|XP, 20-F FY2019; publicado 29-04-2020; selección 2016 redondeada|26-10-2026|[Abrir](https://www.sec.gov/Archives/edgar/data/1787425/000095010320008430/dp126764_20f.htm)|
|Cancel|XP, cancelación de acciones en tesorería, 17-08-2026|26-10-2026|[Abrir](https://www.sec.gov/Archives/edgar/data/1787425/000095010326012480/dp251885_ex9901.htm)|
|Resale|XP, prospecto de reventa, 10-09-2026|26-10-2026|[Abrir](https://www.sec.gov/Archives/edgar/data/1787425/000119312526387869/d142311d424b7.htm)|
|Board|XP, cambio de director, 16-10-2026|26-10-2026|[Abrir](https://www.sec.gov/Archives/edgar/data/1787425/000119312526424071/d79350dex991.htm)|
|ERP|Damodaran, ERPOct26.xlsx; observación mensual 30-09-2026, no tasa diaria de octubre|26-10-2026|[Abrir](https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx)|
|CRP|Damodaran, primas por país, corte enero 2026, Brasil Ba 1|26-10-2026|[Abrir](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html)|
|Beta|Damodaran, betas globales, enero 2026; Investment Banking & Brokerage|26-10-2026|[Abrir](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/BetasGlobal.html)|
|ROE|Damodaran, ROE por industria EEUU, enero 2026; referencia de brokerage, no universo Brasil|26-10-2026|[Abrir](https://pages.stern.nyu.edu/adamodar/New_Home_Page/datafile/roe.html)|
|PTAX|Banco Central do Brasil, PTAX de venta, 26-10-2026 13:09:51 BRT|26-10-2026|[Abrir](https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@data Cotacao=% 2710-26-2026% 27&$format=json)|
|BTG|BTG Pactual, información institucional e inversores, consultada 26-10-2026|26-10-2026|[Abrir](https://institucional.btgpactual.com/en)|
|Itau|Itaú, relaciones con inversores, consultada 26-10-2026|26-10-2026|[Abrir](https://www.itau.com.br/relacoes-com-investidores/en/)|
|Nu|Nu, inversores, consultada 26-10-2026|26-10-2026|[Abrir](https://nu.com/en/investors)|
|Base Rates|Mauboussin, Callahan y Majd, The Base Rate Book, 26-09-2016; original alojado en copia pública|26-10-2026|[Abrir](https://josephnoko.com/wp-content/uploads/2024/04/The-Base-Rate-Book-Michael-Mauboussin.pdf)|
|Price|Stock Analysis, XP; referencia intradía congelada 26-10-2026 13:57 Nueva York, USD 15,37|26-10-2026|[Abrir](https://stockanalysis.com/stocks/xp/)|
|Reuters|Reuters, contexto de volatilidad política de Brasil, 26-10-2026; no fuente de prima de riesgo numérica|26-10-2026|[Abrir](https://www.reuters.com/business/analysts-forecast-brazil-market-falls-after-lula-turnaround-win-2026-10-26/)|
|Rules|JMR, reglas vigentes v 9, 24-10-2026 y prompts vigentes consultados 26-10-2026|26-10-2026|[Abrir](https://github.com/JuanMaRobledo/Modelo-JMR/blob/main/modelo/REGLAS_VIGENTES.md)|

**Registro de versión:** XP-JMR-20261026-R2; tres fases separadas sobre el mismo punto congelado. Prompts: reglasv 9 sha06c95740818a8315f2cbb8a6299b41507ebc61b2; valoraciónsha6b8ad991f8b2ad42858f3f649ce4f7de9e87959b; researchsha6b165d112beeb6c1ee74dd46967aacaf153c6294; auditoríasha0f37f039be30ed425aab56a7d1348d4ccc4ac1e4. Anexosdecontrato yprecisión se conservan con el fichero de origen. Los hashes dearchivos finales están enmanifest_R2.json.

**Límites operativos:** sin auditor externo, sin certificación contable, sin aplicación de los scripts de control canónicos a un repositorio completo, sin evidencia gráfica completa de todas las pestañas, sin prueba end-to-end de app, publicación autorizada con auditoría condicionada. **Límites económicos:** puenteprudencial y transferencias no fungibles abiertos; prima actual y ventaja terminal no verificadas; serie histórica y pares incompletos; supuestos de OCI, PSU, fiscalidad yotros movimientos explícitos. Ninguno se oculta tras N/A o un estado verde. Una consulta fallida de ROE global devolvió 404; se sustituyópor referencia EEUU identificada como tal, no se inventó un promedio global.
[20F25]: https://www.sec.gov/Archives/edgar/data/1787425/000207097926000182/xp-20251231.htm "XP, 20-F FY2025; publicado 29-04-2026, estados consolidados y notas"
[FS26]: https://www.sec.gov/Archives/edgar/data/1787425/000095010326012482/dp251887_ex9901.htm "XP, estados IFRS 1H26, publicado 17-08-2026; resultados, balance, flujos y notas"
[ER26]: https://www.sec.gov/Archives/edgar/data/1787425/000095010326012481/dp251884_6k-ex9901.htm "XP, release 2Q26, publicado 17-08-2026; cifras gerenciales y conciliación"
[Pilar]: https://www.xpi.com.br/documentos/pilar-3-gerenciamento-de-riscos-e-capital-2t26/ "XP, Pilar 3 2T26, KM1 página 5, capital prudencial"
[20F23]: https://www.sec.gov/Archives/edgar/data/1787425/000162828024018424/xp-20231231.htm "XP, 20-F FY2023; publicado 26-04-2024"
[20F21]: https://www.sec.gov/Archives/edgar/data/1787425/000162828022009080/xp-20211231.htm "XP, 20-F FY2021; publicado 13-04-2022"
[20F19]: https://www.sec.gov/Archives/edgar/data/1787425/000095010320008430/dp126764_20f.htm "XP, 20-F FY2019; publicado 29-04-2020; selección 2016 redondeada"
[Cancel]: https://www.sec.gov/Archives/edgar/data/1787425/000095010326012480/dp251885_ex9901.htm "XP, cancelación de acciones en tesorería, 17-08-2026"
[Resale]: https://www.sec.gov/Archives/edgar/data/1787425/000119312526387869/d142311d424b7.htm "XP, prospecto de reventa, 10-09-2026"
[Board]: https://www.sec.gov/Archives/edgar/data/1787425/000119312526424071/d79350dex991.htm "XP, cambio de director, 16-10-2026"
[ERP]: https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx "Damodaran, ERPOct26.xlsx; observación mensual 30-09-2026, no tasa diaria de octubre"
[CRP]: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html "Damodaran, primas por país, corte enero 2026, Brasil Ba 1"
[Beta]: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/BetasGlobal.html "Damodaran, betas globales, enero 2026; Investment Banking & Brokerage"
[ROE]: https://pages.stern.nyu.edu/adamodar/New_Home_Page/datafile/roe.html "Damodaran, ROE por industria EEUU, enero 2026; referencia de brokerage, no universo Brasil"
[PTAX]: https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@data Cotacao=% 2710-26-2026% 27&$format=json "Banco Central do Brasil, PTAX de venta, 26-10-2026 13:09:51 BRT"
[BTG]: https://institucional.btgpactual.com/en "BTG Pactual, información institucional e inversores, consultada 26-10-2026"
[Itau]: https://www.itau.com.br/relacoes-com-investidores/en/ "Itaú, relaciones con inversores, consultada 26-10-2026"
[Nu]: https://nu.com/en/investors "Nu, inversores, consultada 26-10-2026"
[BaseRates]: https://josephnoko.com/wp-content/uploads/2024/04/The-Base-Rate-Book-Michael-Mauboussin.pdf "Mauboussin, Callahan y Majd, The Base Rate Book, 26-09-2016; original alojado en copia pública"
[Price]: https://stockanalysis.com/stocks/xp/ "Stock Analysis, XP; referencia intradía congelada 26-10-2026 13:57 Nueva York, USD 15,37"
[Reuters]: https://www.reuters.com/business/analysts-forecast-brazil-market-falls-after-lula-turnaround-win-2026-10-26/ "Reuters, contexto de volatilidad política de Brasil, 26-10-2026; no fuente de prima de riesgo numérica"
[Rules]: https://github.com/JuanMaRobledo/Modelo-JMR/blob/main/modelo/REGLAS_VIGENTES.md "JMR, reglas vigentes v 9, 24-10-2026 y prompts vigentes consultados 26-10-2026"