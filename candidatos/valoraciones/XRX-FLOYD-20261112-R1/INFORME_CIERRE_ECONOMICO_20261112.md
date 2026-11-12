# Xerox: correcciones implantadas y cierre económico sometido a pruebas

Revisión **XRX-FLOYD-20261112-R1**. USD millones salvo precio/acciones. Corte contable 30-sep-2026; precio 1,02 USD del 11-nov-2026. FCFF consolidado, contrato `floyd-libro-unico-v1`, Ginsu original. Reglas main `b50fbb431095ed1a3f6ebfc2ab923fd405fcbd30`. Se conserva el libro y el Doc oficiales; PR existente #277. **CANDIDATO; no es un precio intrínseco certificado.** R6 independiente pendiente.

## 1. Hallazgos nuevos y correcciones efectivamente implantadas

**Autorización ejecutada:** tras «Si autorizo», se instalaron los seis S/C, se recalcularon y cargaron las 75 sensibilidades y cuatro inversos para esos mismos inputs, y se implantó la guardia MOS. Firmas de matrices e inversos: VIGENTE. No se adoptó el WACC experimental ni se publicó la revisión.

**Fiscalidad:** se instaló en el candidato una separación entre ETR histórica y tasa prospectiva, después de nueve regresiones reales. `Income Statement!L29` sigue en −6,402164%; `Control económico XRX!B3` la muestra. `B4` activa las hipótesis prospectivas `B5:D5=25%`; los tres `Input sheet!B23` conservan el enlace histórico dentro de un selector reversible. No se modificó ninguna fórmula de `Valuation output`, ni la maestra. El 25% es una hipótesis de impuesto sobre operación desapalancada, sin NOL inicial reconocido; no es una cifra fiscal reportada ni un calendario de caja por jurisdicción ya validado.

**EBITDA:** se corrigió `M · Income Statement!B27:L27`. La fórmula anterior daba prioridad a D&A separada en resultados e ignoraba D&A embebida en costes. LTM: EBIT −653 + D&A total de caja 403 = **−250**, frente al −529 anterior, que sólo añadía 124. Once columnas concilian ahora exactamente con el EBITDA ya calculado en H. No cambia EBIT, PBT ni caja. La normalización mínima de contraste es −250 + goodwill 959 − IEEPA 105 = **604**. La cifra anterior 430 no era una normalización válida del EBITDA consolidado completo.

No se ha confundido estas dos reparaciones con el cierre integral de XRX-07 o XRX-09: quedan fiscalidad realizable y cobertura económica de múltiplos.

## 2. Fuentes primarias recuperadas, sin rehacer los históricos

Se reutilizaron diez FY, LTM, PDF aportados, clasificación H, 22 cuadres de balance/caja con FX y las entregas R2–R5 del PR #277 (`19a7d21`). Las notas se contrastaron con:

- SEC 10-Q sep26, accession `0001770450-26-000051`, notas 8, 11, 12, 14, 15, 16, 19, 20 y 22; MD&A de liquidez/deuda.
- SEC 10-K FY25 `0001770450-26-000009`, notas de leases, pensiones, impuestos y preferentes; 10-Q sep25 `0001770450-25-000037` para leases comparables 74+265.
- Xerox IR 29-oct26, resultados y guía: ingresos ~7600, EBIT ajustado 450–475, CFO145–195, CAPEX95 y FCF50–100; beneficio IEEPA105 y efecto declarado en guía FCF80.
- Presentación de mayo26: 146 de sinergias brutas run-rate y objetivo combinado de ahorros 250–300. Son ahorros brutos; no se suman otra vez a márgenes que ya los recogen.
- Damodaran, *Dealing with Distress in Valuation*, y tabla global dentro de Ginsu. Página de ERP de noviembre: 4,41% con Rf5,29%; el Treasury10Y de10-nov4,98% se conserva como observación diaria distinta.

URLs: https://www.sec.gov/Archives/edgar/data/1770450/000177045026000051/xrx-20260930.htm ; https://www.sec.gov/Archives/edgar/data/1770450/000177045026000009/xrx-20251231.htm ; https://investors.xerox.com/news-releases/news-release-details/xerox-releases-third-quarter-results-2 ; https://investors.xerox.com/static-files/c2a19261-7316-4af4-b49a-9d05df0525ff ; https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm?lfrom=202213444 ; https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/distresspaper.htm .

## 3. Historia económica y supuestos anteriores/nuevos

El crecimiento adquirido de Lexmark desde julio2025 no demuestra crecimiento orgánico. La contracción pro forma, menor originación financiera y menor venta de cartera coexisten con mejora de equipos y sinergias. La recurrencia de servicios depende del parque y del uso. Las reestructuraciones recurrentes, las contribuciones a pensiones y la inversión en equipos/software impiden transformar EBITDA ajustado en caja automáticamente.

| Palanca | Antes de autorización | Oficial vigente / justificación |
|---|---|---|
| Ingresos C/B/O año1 | −8% /−5% /−2% | Se conservan; no se fuerza recuperación adquirida |
| CAGR años2–5 C/B/O | −6% /−3% /+0,5% | Se conserva; estabilización sólo en O |
| Margen año1 C/B/O | −1% /1,5% /3% | Se conserva, sujeto al puente de caja/pensiones |
| Margen objetivo / convergencia | 3% año9 /6% año7 /8,5% año6 | Se conserva como hipótesis; no se vuelve ahorro neto cada anuncio bruto |
| S/C años1–5 C/B/O | 1,1 /1,5 /1,8 | **12 /8 /2,1**, implantado tras autorización; en contracción limita capital recuperable, no mide eficiencia de expansión |
| S/C años6–10 C/B/O | 1,8 /2,1 /2,2 | **8 /4 /2,1**, implantado tras autorización |
| Tipo inicial del motor | **25% ya implantado**; antes −6,4% | 0% y35% como sensibilidad; no reconocer8100 de NOL por omisión |
| WACC común | 10,30%, todavía provisional | Componentes y contraste22,075% en copia; **no definitivo ni instalado** |
| Rf /ERP | Rf4,98% y ERP auxiliar6% | Par mensual5,29%/4,41% sólo en estudio; no mezclar fechas |
| g perpetuo C/B/O | −2,5% /−1% /0% | Se conserva; no se impone4% positivo |

## 4. FCFF Base: de dónde procede y cuánto cambia

La cartera neta baja de1402 a1209 y los equipos para clientes de299 a272 entre diciembre y septiembre. La reducción contable de220 no equivale a caja disponible: CFO9M recoge152 de disminución de cartera; ventas a terceros aportaron122 y los traspasos pueden exigir prepagos de primer lien. No se restan esos prepagos dentro de FCFF y luego otra vez como deuda. Tampoco se consideran los185 de capital financiero asignado un segundo activo.

El CFO9M consume97 en inventarios y52 en AR/cartera facturada; los equipos consumen92 frente a114 de depreciación/obsolescencia. El subtotal parcial152−97−52+114−92=**25** no es FCFF ni una conciliación completa de originaciones. Es una prueba de que extrapolar146 anuales de recuperación neta exige evidencia adicional. Su equivalente anual meramente indicativo es33,33; no se lo presenta como LTM.

| Primer año Base | Original | Antecedente: sólo fiscal25% | Oficial S/C8 con fiscal25% |
|---|---:|---:|---:|
| EBIT |109,212|109,212|109,212|
| NOPAT |116,202|81,909|81,909|
| Reinversión |−145,616|−145,616|**−27,303**|
| FCFF |261,818|227,525|**109,212**|

Todos son resultados de Ginsu, no un DCF manual. La liberación pasa de55,6% del FCFF original a25% en el oficial vigente. El primer efecto fiscal reduce EV Base3195,321→2830,053 (−365,269). El cambio aislado de S/C, manteniendo WACC10,3%, Rf4,98% y el resto, reduce EV2830,053→**2367,260** (−462,793; −3,474 por acción bruta). La reinversión sigue siendo una estimación pendiente de validar, no un saldo reportado.

## 5. Capital invertido, retorno y sostenibilidad

En el oficial Base el capital de Ginsu va de3606 a3367,818 en año10: recuperación acumulada238,182, frente a883,428 con los S/C anteriores. El ROIC año10 es7,83%; la mejora procede en buena medida del margen sobre activos existentes. **RONIC no se infiere** dividiendo una mejora de beneficio por inversión negativa. Los coeficientes8/4 de contracción no equivalen a un ROIC marginal extraordinario.

Ginsu produce FCFF terminal262,201 con g−1% y reinversión terminal0 por su fórmula original para g≤0. Ese resultado presupone que inversión bruta de mantenimiento y depreciación se compensan y que no queda inversión neta adicional; no demuestra que Xerox publique ese CAPEX de mantenimiento. La guía95 de CAPEX excluye los equipos para clientes dentro de CFO. I+D capitalizada: gasto258, activo475, amortización216,667 y EBIT ajustado−611,667; su reinversión no es ahorro gratis. No se impone convergencia efectiva del ROIC a9,70%: para g≤0 el selector terminal no financia nueva expansión.

## 6. Deuda, WACC y fracaso

Se reconcilia **principal4348 = carrying4220 + costes95 + descuento33**. El FV divulgado es2893, no un ingreso del accionista de1327. Damodaran exige valores económicos de los derechos y deuda a mercado para EV→equity; el principal contractual se conserva para vencimientos, reestructuración y el strike de la opción. No se añade de nuevo el fondeo cautivo1296, ya incluido. Vencimientos: Q42620;2027197;2028752;20291137;20301042;2031+1200.

La ABL pasó de0 al30sep a75 dispuestos al5nov; disponibilidad neta225. Es un hecho postcorte consumado y exige puente de caja. El canje174m a nuevos bonos y acciones esperado13nov sigue anunciado. La recompra consumada de200 de principal por101 y los8 de convertibles retirados con warrants no se vuelven a descontar: ya están en los saldos.

En copia, beta operativa bottom-up0,7584 (Office y Computer Services ponderados por EV/ventas), FV deuda2893, capitalización135,873 y preferente hipotética63,326 dan beta apalancada17,260 con beta de deuda0 y sin escudo inmediato; Ke81,41%. Con Kd19,29% (IBR FY25 reportada, **no YTM de bonos al precio**) y rentabilidad preferente supuesta22%, WACC22,075%. Es una **estimación de contraste muy sensible**, no una tasa certificada: beta de deuda0, duración, geografía, deuda convertible y costes por instrumento requieren mejor calibración. Con Kd13,5%, WACC16,658%; con25%,27,417%. No se ha presentado el10,3% anterior ni el22,075% experimental como definitivos.

El riesgo explícito de Ginsu permanece sólo en Conservadora conforme a JMR:20% y recuperación25% de EV; se probaron0/40/60%. No es una probabilidad empírica calibrada ni justifica sumar otra penalización arbitraria al WACC por el mismo incumplimiento. Base0% significa condicionalidad/convención del escenario, no ausencia real de riesgo. Una distribución de reorganización sigue pendiente.

## 7. Fiscalidad y NOL

FY25: NOL6500 que caducan2026–2045 y1600 indefinidos; DTA2242, allowance1933, neto309. El gasto fiscal9M26 de59 no es evidencia de impuestos pagados59. La nota19 explica beneficios gravables en unas jurisdicciones y pérdidas sin beneficio en otras. No se inventó un calendario de NOL por país ni se cargó8100 como escudo realizable.

La reparación técnica elimina el crédito negativo sobre EBIT positivo. Como regresión antecedente, con los supuestos originales restantes, las tres corridas fiscales25% reales dan C−15,728920/B−7,461577/O3,407055 por acción **bruta**, contra−15,450415/−4,719501/8,583045 anteriores. Nueve resultados de regresión coinciden exactamente con la evidencia del #204. La trayectoria fiscal prospectiva es todavía una normalización con sensibilidad, no una auditoría tributaria final.

## 8. Puente al común y derechos

El puente de investigación usa deuda FV2893, caja412 (ya excluye118 restringida), NCI16 una vez, warrants21 cotizados a FV en septiembre y obligación IEEPA81 separada. El crédito arancelario y los17 restringidos asociados deben conciliarse antes de determinar cuánto pasivo está compensado: se probó IEEPA neto0–81, sin certificar ninguno como saldo neto publicado.

Series A:180 de liquidación,214 carrying, dividendo14,4 acumulativo, conversión opcional6,741576m. Hipótesis ilustrativa: reanudar pago tras2años y exigir22% produce PV63,326. **No es valor observado ni valoración completa de su opción de conversión**. Las ramas no-convertida y convertida se comparan por el derecho del titular; no se resta preferente y se añaden acciones simultáneamente. RSU/PSU18,586m son contingentes:0/100% de vesting son sensibilidades, no emisiones ciertas. Warrants81,412m del EPS no se añaden automáticamente; su entrega puede retirar bonos. Las opciones de empleados0,073m no son los warrants21m.

Pensiones:989+146 de pasivos brutos, prepaid578 FY25 y aportes160 guiados. No se resta1135 sin conciliar activos/obligaciones y el coste que ya recogen los márgenes. La hipótesis de caja del margen año1 conserva esa carga; su calendario futuro necesita contraste actuarial. La opción del accionista en reorganización requiere valor/volatilidad de activos y reparto por prelación, no aplicar el modelo de opciones de empleados al total de la empresa.

## 9. Valores: separar salidas definitivas de hipótesis

**Oficial vigente:** tres Ginsu con fiscal25% y S/C autorizados; WACC10,3% todavía provisional y puente al común no certificado. Salidas brutas C−24,2169565532 / B−10,9357673798 / O+3,4852555643USD/acción; EV C598,0894374 / B2367,2600856 / O4288,2665689millones. **No son precios certificados del común**. Un residual negativo no es un precio negativo.

**Estudio de contraste en copia, no implantado**, S/C nuevos, par mensual y WACC experimental22,075%:

| USDm / acción | Conservadora | Base | Optimista |
|---|---:|---:|---:|
| EV tras distress Ginsu |304,664|1314,578|2314,263|
| Residual tras FV deuda y derechos estimados |−2357,662|−1347,748|−348,064|
| Residual común con responsabilidad limitada |0|0|0|
| Valor total incluyendo opción de reorganización |N/D|N/D|N/D|

Los ceros son el piso del residual en esa combinación, no precios certificados de la acción. Con S/C propuesto y WACC10,3%/terminal9,21% se obtiene O10,655 de residual condicionado; con Kd13,5% y el nuevo par mensual O2,186. La sensibilidad es material.

## 10. Esperado, MOS y tesis contraria

No se publica esperado ni MOS como valor certificado. Una ponderación exploratoria C45/B40/O15 (agrupa declive adverso y fracaso en C) no es calibración estadística; el promedio de pisos0 no valora opcionalidad.

**Contraevidencia al cero universal:** combinar coste no apalancado8,635% con S/CBase4/2,1 y25% fiscal produce residual0,0456 por acción. Añadir impuesto inicial0%, IEEPA neto0 y ninguna RSU adicional da **2,9851**. Es un extremo conjunto favorable, no Base; demuestra que las pruebas aisladas no acotan por sí solas el valor total. No se compensan porcentajes de riesgos ni se declara inmaterial con Base0. Si existe una Base común positiva y aprobada, MOS=65% de ella exclusivamente.

## 11. Múltiplos, sensibilidades e inverso

EV/EBITDA: **normalización mínima justificable604**, aún no denominador recurrente definitivo; contraste guía739−105=634, con diferencias de ajustes/licencias/perímetro. P/E reportado: N/M por pérdidas. EV/FCFF y P/FCFE: N/D normalizado hasta capital/financiación/derechos; no inventar flujos positivos. P/OCF: CFO131 positivo, pero cartera impide usarlo sin normalización. No se asignaron pesos para aparentar dos métodos y80% de cobertura. Canon (guía FY26 margen operativo~9,6%) y Ricoh (beneficio operativo FY25 90,7 sobre ventas2608,3) son referencias de economía operativa, no múltiplos intercambiables: mezcla, moneda y financiación difieren; no se inventó una mediana de pares.

Se recalcularon y cargaron **75 sensibilidades con los S/C autorizados y fiscal25%**: tres matrices5×5, tres centros−10,935767379800657, diferencia0. Las75celdas numéricas se releyeron y conciliaron; la copia técnica se restauró a C/B/O vigente. Firmas matrices e inversos VIGENTE; centros coherentes. Las14sensibilidades aisladas y3conjuntas anteriores se conservan como estudios diferenciados, no como matrices vigentes.

Cuatro inversos brutos recalculados y cargados, objetivo1,02: crecimiento **sólo año1**58,9128007% (años2–5 quedan−3%); margen objetivo10,7227304%; crecimiento sólo año1 con margen3%=177,5083545%; WACCinicial1,0271104%, inferior alRf4,98%. Error máximo4,42e−9USD en verificación nativa. B26no cambia los cinco primeros años. No son inversos del común certificado.

## 12. Pruebas e integridad; qué está cerrado realmente

- Nueve regresiones fiscales nativas: diferencias0; ETR histórica intacta.
- Once EBITDA H↔M: diferencias0; EBIT/PBT/caja no alterados.
- Inspección de148302 celdas en51pestañas, A1:AA220, con3736 fórmulas previas: ninguna fórmula de cálculo Damodaran modificada, ningún comentario/formato/validación cambiado en los motores. Se registran por separado los nuevos enlaces de entrada; no se dice que no cambió ningún vínculo.
- 75 corridas y4 raíces vigentes con S/C autorizados cargadas y conciliadas;14stress y3conjuntos. Lag0 y1 comparan diez años y terminal, no sólo el año1.
- Las22 conciliaciones históricas anteriores siguen válidas porque H no se ha reescrito; no se repitieron innecesariamente. La inspección no se presenta como QA visual ni R6.

**Autorización resuelta:** los rechazos automáticos anteriores quedaron superados por la autorización explícita «Si autorizo». Se ejecutaron las tres actuaciones solicitadas: seis S/C,75entradas estáticas y4inversos recién recalculados, guardiaMOS. Los sellos se actualizaron sólo después de conciliar lecturas y restaurar la copia. `Resumen de valoraciones!B17` y Presentación muestran N/M; no se ofrece MOS negativo. La inspección final de148302celdas identifica exactamente6inputsS/C y3enlaces fiscales ya documentados;0fórmulas de cálculo Damodaran alteradas,0cambios de formato/comentarios/validación en motores. El cierre técnico no certifica derechos comunes ni resuelve los asuntos económicos abiertos.

## 13. R2–R5, PR, CI y publicación

R2 **NO CERRADO**:19indicadores derivados de leases propios LTM, no19fuentes independientes. FY25operativos327/financieros8 y sep25operativos339 están verificados; sep26no tiene desglose propio verificado tras revisar PDF/notas y búsqueda XBRL (accesoXML no conseguido). Al tratar rentas como gasto en Ginsu sin conversión, la ausencia no entra por19canales al DCF; aun así los ratios de deuda/EV no admiten la excepción automática §4B-bis. No se imputa0 ni se arrastra327 como histórico2026.

R3 **PARCIAL ECONÓMICO / CORRIDAS TÉCNICAS VIGENTES**: fiscal y S/C implantados;75sensibilidades y4inversos cargados y conciliados. WACC y puente económico siguen pendientes. R4 **PARCIAL**: error EBITDA reparado; normalización y cobertura no aprobadas. R5: análisis y evidencia de esta misma revisión actualizados; **CANDIDATO / NO PUBLICAR**. Se completa el PR existente277 como evidencia candidata; CI técnico no sustituye estos gates. Catálogo y app no se promueven ni se finge una ficha publicada. R6 queda como auditoría económica independiente posterior, no como excusa para impedir el cierre deR5 cuando cumpla sus propios controles.

Siguiente prueba exacta: antes de certificar valor común, contrastar costes/YTM por instrumento y riesgo de refinanciación; conciliar el puente postcorte75ABL/caja y los derechos prioritarios; validar impuestos realizables y mantenimiento/capital cautivo; recuperar el saldo propio de leases o tramitar el mantenimiento contractual admisible sin inventar históricos. Si cambian inputs materiales, invalidar y volver a ejecutar las corridas afectadas. La autorización de estas tres escrituras no adopta22,075% ni publica.
