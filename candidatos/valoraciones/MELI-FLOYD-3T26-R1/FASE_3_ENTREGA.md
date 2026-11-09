# F3 · MELI-FLOYD-3T26-R1 · CANDIDATO

**MercadoLibre, MELI · acción ordinaria Nasdaq · USD nominal · perfil Floyd.** Corte contable 30-sep-2026, cierre US$1.510 al 6-nov-2026. Trabajo del 8-nov-2026 (Colombia). OpenAI Codex en ChatGPT Work, familia GPT-6, variante y esfuerzo de razonamiento no expuestos a esta sesión. Google Sheets/Docs y GitHub conectados, Git local y Node/Python para controles, SEC/NYU Stern para fuentes.

[H1](https://docs.google.com/spreadsheets/d/1TF8KaMkn-Wc3csoCK1z9-IierhPhOBZwwdX7fiBYN6Q/edit) · [H2](https://docs.google.com/spreadsheets/d/1wkFwjzufTR8KqrLSc7gxmxuB_qepFjEDc-LMuFi5oR0/edit) · [Google Docs](https://docs.google.com/document/d/1bv2hPD1XvgVM2Vz3WjQdX8Sh1bLo0FXEhqPc3GZCxVk/edit) · [PR #260](https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/260). Rama `meli-floyd-3t26-r1`, punto de partida remoto comprobado `451d84ba675f42998c2488d5f617acd9c19d2f57`. [Revisión crítica](https://github.com/JuanMaRobledo/Modelo-JMR-datos/blob/ccr-d8664753-j2j79d/candidatos/valoraciones/MELI-FLOYD-3T26-R1/REVISION_CLAUDE_20261108.md). H1, H2 y Maestra tienen IDs distintos. No se declara aislamiento integral.

**PASOS F3 1/5 completos.** Selección del método cerrada. Bloques de costo de capital, reinversión e historias parciales. Cierre del cálculo pendiente.

| Control | Estado | Evidencia |
|---|---|---|
| Método §4C | APROBADO | SOTP. Commerce y corporativo con FCFF Floyd. Mercado Pago, incluidos crédito y pagos/adquirencia que comparten fondeo y capital, con FCFE/ROE. El detalle de ingresos por vertical y la contribución por geografía del 10-Q (nota 7) no identifican el EBIT por negocio. |
| Identidades observables del puente | APROBADO | H2 `Tesis de Inversión y Supuestos!B43:C57`. Cartera bruta US$17.884m, residuo de caja restringida cero, deuda bruta/netas del emisor US$16.154m/US$8.028m. Deuda colateralizada incluida, leases ASC 842 reconocidos una vez. |
| Perímetro y materialidad | PARCIAL | H2 `B53:C66` del puente. US$6.773m de pasivos financieros pendientes de asignación tras identificar bonos senior y deuda colateralizada. Faltan utilidad Fintech, EBIT de Commerce/corporativo, patrimonio requerido, buffer, recursos transferibles y caja excedentaria por unidad. `B68` da US$19,73 por acción por cada US$1.000m, con EV fijo. Falta Base válida para calcular impacto §4B o acotar la incertidumbre. |
| Costo de capital | PARCIAL | `Cost of capital worksheet!B12` Detailed. `L83:N91` registra Rf 5,29 %, ERP madura 4,41 %, ambas del 1-nov-2026, y beta terminal 1. Referencia terminal USD 9,70 % antes del ajuste Brasil. `Input sheet!B35/B68/B69` reflejan Rf y g estándar 4,0 %. Ke Fintech, WACC Commerce y tasas terminales definitivas N/D. Faltan beta por bloque, exposiciones país, deuda, Kd y pesos de mercado. `B14/E63/Input sheet!B36` sin cálculo autorizado. |
| Retención y retornos | PARCIAL | H2 `Tesis de Inversión y Supuestos!A78:H118` prepara las tres trayectorias FCFE con cartera bruta, provisión, fondeo, otros activos netos, capital objetivo y utilidad. Resta el aumento positivo de patrimonio requerido, sujeto a validar distribución por entidad. `H82/H94/H106` devuelven N/D. `B71/B72` verifican ROE grupo 26,22 % promedio y 23,05 % de cierre. ROE incremental Fintech y S/C Commerce siguen pendientes. |
| Tres historias y previa | PARCIAL | `Escenarios e historias!B5/B6/B8`, previa de alto crecimiento normalizada 47,06 %/26,47 %/26,47 %, suma 100 % en el control nativo del candidato en `Tesis de Inversión y Supuestos!B77`. Narrativa, mecanismos, celdas y disparadores en filas 117–201. Rangos numéricos y 3P cuantitativas pendientes. El fracaso queda reservado a Conservadora. Probabilidad y recuperación sin estimar. |
| Orden y valor esperado, DCF, MOS, inverso | NO_EJECUTADO | `Escenarios e historias!H5/H6/H8/H10/H11` vacías y `K5/K6/K8` PENDIENTE. H2 se mantiene en modo plantilla por el perímetro. Inverso único definido como margen EBIT maduro Commerce con demás supuestos Base y FCFE Fintech fijos para llegar a US$1.510. |
| Cinco múltiplos y matrices 5×5 | NO_EJECUTADO | EVEBITDA, EVFCFF, PE, PFCFE y POCF pendientes de anclas y VP FY+3 coherentes. Los múltiplos de contraste LTM en H1 `Resumen!B16:B17` no constituyen anclas. Los centros DCF/múltiplos oficiales siguen pendientes. |
| Huella registrada | APROBADO | Relectura H2 `Huella motor!F2:F3`: 0 diferencias de 1.883. Comparación de `A2:D1884` con la Maestra `157EabbntPVoydBgBZNjp90BBjoliGDOts2E0MxNVKSc`: 0 diferencias en el registro de referencia, 1.883 comprobaciones TRUE en H2. Alcance limitado a las fórmulas incluidas. |
| Controles de carga, compuertas y casos especiales | PARCIAL | H2 `Control de integridad!B2:C6`: PLANTILLA, 0/3 LISTO, sin empresa en las compuertas. El cotejo ASC 842 consolidado se realizó. Continúan I+D separable, RSU/opciones, NOL, inversiones no operativas y traspaso integral. |
| Réplica histórica y comparación A3 | PARCIAL | `python3 -B diagnostico_flujo_accionista.py` y `python3 -B revision_supuestos.py` completaron las aserciones del diagnóstico. Análisis N2 §11 documenta la reconciliación de tasa terminal, el puente de palancas de A3 y la discrepancia entre `valorPrincipal` y `metodos[0].base`. Atribución monetaria A3 → Floyd pendiente de Base válida. |

**Foto H2.** Base oficial, esperado, MOS y sensibilidades N/D. El rango US$1.281,88–1.320,59 pertenece exclusivamente a la réplica histórica con cambio de denominador terminal. Aproximadamente +25,5 % y +28,4 % al comparar cada variante con su base de igual g, por encima de §4B dentro de esa réplica. El efecto oficial en Floyd es N/D. Se conserva la fuente nativa como requisito para toda cifra de valoración.

**Primer siguiente paso exacto.** Completar las aperturas en H2 `Tesis de Inversión y Supuestos!B81:F81`, `B93:F93` y `B105:F105` a partir de una conciliación de Mercado Pago al 30-sep-2026 por entidad: cartera, provisión, fondeo, otros activos/pasivos netos y capital objetivo. Adjuntar utilidad de Mercado Pago y EBIT Commerce/corporativo, eliminar saldos internos y conciliar con el 10-Q antes de activar los bloques de valoración.

[10-Q 3T26](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000029/meli-20260930.htm) · [Carta 3T26](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000027/meli-20260930xex991.htm) · [Damodaran, corte 1-nov](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm) · [A3, JSON histórico](../../../valoraciones/MELI-20261028-A3.json).


## Verificación incremental · 8-nov-2026 · GPT-6 (ChatGPT)

Modelo/herramienta real: GPT-6 en ChatGPT; conectores GitHub y Google Drive/Sheets/Docs y cotejo público SEC. Esfuerzo interno de razonamiento no expuesto. No se utilizó Work, terminal Git, Python ni Node en esta ejecución. Se preservan rama y PR #260, sin libros ni revisiones nuevos. PASOS F3: el método permanece decidido y el cálculo no se cierra (1/5).

| Control | Resultado de esta sesión | Evidencia y límite |
|---|---|---|
| Exclusión de fondos de clientes | APROBADO para clasificación, NO para SOTP | SEC 10-Q MD&A: no se emplean fondos de clientes en el negocio crediticio. H2 Tesis de Inversión y Supuestos!B44=17.400 US$m; nota D44 corregida. No incluir como fondeo de cartera ni caja libre. |
| Diferencia de definiciones de liquidez | APROBADO para clasificación, NO para disponibilidad por negocio | H2 B56=8.126 US$m: definición del puente de deuda neta que incluye inversiones de largo plazo. SEC MD&A también describe 6.902 US$m de liquidez principal (caja e inversiones cortas ajustadas). H2 D56 actualizado; B62/C62 siguen N/D. |
| Fondeo por unidad y doble conteo | PARCIAL | H2 B50=13.190 US$m; B51=4.164 US$m deuda colateralizada ya incluida; B52=2.253 US$m bonos senior; B53=6.773 US$m aún sin asignación, calculado por fórmula. D61 actualizado. El residuo no se asignó arbitrariamente. ASC842 B54=2.964 US$m ya reconocido y no agregado otra vez. |
| Resultados separados | PARCIAL | Nota 7 del 10-Q presenta utilidad operativa por geografía, no EBIT Commerce/corporativo y utilidad neta Mercado Pago. El grupo emisor y garantes de Reg. S-X 13-01 tampoco representa un negocio individual. H2 D66 corregido, B66/C66=N/D. |
| Capital distribuible y reinversión Fintech | PARCIAL | H2 B61:C66=N/D; aperturas B81:F81, B93:F93 y B105:F105 vacías. La fuente no separa patrimonio exigible, colchones, eliminaciones ni resultado Fintech. ROE consolidado B71=26,22 % promedio y B72=23,05 % cierre, no ROE incremental crediticio. |
| Ke/WACC y terminal | PARCIAL | Cost of capital worksheet!B12=Detailed, pero B22/B26 sin selección documentada y B14 sin WACC oficial. Panel L83:N91: Rf 5,29 %, ERP madura 4,41 % (fecha indicada 1-nov-2026), beta normativa terminal 1, referencia 9,70 % antes de prima país. Faltan beta, exposición Brasil, Kd, ponderación de mercado y Ke por unidad; g estándar 4,0 % es referencia, no valoración activada. La Ke 12,5 % no se usa. La pareja 5,29 % y 4,41 % fue contrastada además con la página oficial de Damodaran, https://pages.stern.nyu.edu/adamodar/New_Home_Page/home.htm (consulta 8-nov-2026); no acredita beta o WACC por negocio. |
| Huella observada tras editar notas | APROBADO dentro de huella, no integral | Lectura Google Sheets: Huella motor!F2=0 diferencias y F3=1.883 fórmulas registradas. En esta sesión solo se editaron cuatro celdas de texto D44/D56/D61/D66, sin tocar fórmulas/selectores. No se ejecutó comparación externa integral contra maestra. |
| Valores centrales y sensibilidades | NO_EJECUTADO | Escenarios e historias!H5/H6/H8/H10/H11 vacíos; K5/K6/K8=PENDIENTE; Control de integridad!B2=PLANTILLA y B4=0/3 LISTO. DCF SOTP, Base/esperado/MOS, inverso único, cinco múltiplos aplicables y matrices 5×5 = N/D. Probabilidades Base/Conservadora/Optimista 47,06/26,47/26,47 % suman 100 %, pero los escenarios no están calculados. |
| Scripts diagnósticos y gates | NO_EJECUTADO en esta sesión | Sin ejecución nueva de Python, controles financieros, catálogo o profundidad. Ejecuciones previas no son controles de esta revisión actualizada. Las cifras replicadas en Python no son resultados oficiales. |

Materialidad §4B: la falta de fondeo, resultado y patrimonio distribuible por entidad impide calcular el SOTP Base o acotar el impacto; por ello no puede denominarse salvedad inmaterial. La A-1.2 MELI-20261028-A3 conserva su Base histórica US$2.029,87, mientras que su metodos[0].base registra US$2.817,58: inconsistencia histórica a explicar, no transferir al candidato. Comparación de efectos monetarios antes→después = N/D hasta que H2 calcule el valor. Estado CANDIDATO.

Primer siguiente paso exacto: obtener y conciliar la apertura de Mercado Pago al 30-sep-2026 por entidad (cartera bruta, provisiones, fondeo, otros activos/pasivos, capital requerido, liquidez, colchones, eliminaciones y capacidad de distribución), resultado neto Fintech y EBIT Commerce/corporativo, y cargar solo sus entradas justificadas en H2 Tesis de Inversión y Supuestos!B81:F81, B93:F93 y B105:F105. Luego se podrán terminar costos por bloque y activar SOTP, escenarios y matrices.


## Avance F3 tras cierre físico H1/H2 · 8-nov-2026 · GPT-6 (ChatGPT)

**Método SOTP §4C sigue siendo obligatorio y aún NO calculable con los datos públicos disponibles.** La carga del expediente MELI-FLOYD-3T26-R1 mejora sin cambiar sus valores centrales N/D:

- Ingresos LTM por línea, con identidad SEC: Commerce **US$21.749m**, Fintech **US$16.774m**, total **US$38.523m** y residuo cero. Detalle auditable: H1 `Resumen!B26:E29`; H2 `Segmentos!A10:D11` y `Presentación!A32:J35`. `Segmentos!B4=No` deliberadamente: no usar un DCF industrial consolidado como sustituto del SOTP.
- Clasificación de I+D: H1 `Income Statement!B10:L10` enlaza Product and Technology Development como **proxy**, con nota explícita: no equivale necesariamente a I+D puro; el residuo de gastos operativos de la fila 11 se recalcula para evitar duplicación y deja EBIT reconciliado en todas las columnas de 2016–2025/LTM. H2 `Input sheet!B17=Yes`; `R& D converter!F7=4` años como hipótesis de vida económica de software, **no dato SEC ni valor SOTP activado**; sensibilidad 3–5 años pendiente.
- Arrendamientos: H2 `Input sheet!B18=No`, `B123=US GAAP`, `B124=2.964`, `C124=2.199` (USDm de obligaciones operativas de arrendamiento). El gasto está en EBIT; evitar capitalizar dos veces ASC842. La deuda financiera H2 `Input sheet!B16=US$13.190m` vs anterior bruto 16.154 cuando se sumaban leases operativos; esto sigue siendo **consolidado**, no debt Finance vs Commerce asignado.
- `Input sheet!B5` nombre verificado, `D1=US$1.510` fechado 6-nov-2026, `B4` fecha; **A1 permanece vacío temporalmente**: al activarlo con historias SOTP y costo de capital ausentes se observaron `#DIV/0!` en `Escenarios e historias` y `Control de integridad`. Se restauró A1 en blanco y los controles vuelven a `PLANTILLA`. No ocultar esta limitación.
- Tres historias con probabilidades 47,06/26,47/26,47%, pero Commerce EBIT/Fintech earnings, ROE de Mercado Pago, capital requerido y libertad de fondos siguen N/D. `Tesis de Inversión y Supuestos!B61:C66`, `B81:F81/B93:F93/B105:F105` sin apertura confiable; `Cost of capital worksheet!B14` sin tasa final aprobada; `Escenarios e historias!K5/K6/K8=PENDIENTE`; DCF Base/esperado/MOS, DCF inverso y matrices 5×5 permanecen N/D.

**Pruebas:** traspaso H1/H2 (12.155 comparaciones, 1.554 valores, 0 discrepancias), huella registrada 0/1.883 con actualización identificada de 31 fórmulas por referencias. No hay resultado de F3 aprobado. No se ejecutó una corrida válida de SOTP del motor ni gates de publicación de MELI. No sustituir por DCF industrial, A-1.2 o scripts aislados.

**Materialidad:** ingresos Commerce vs Fintech no determinan ganancias, capital regulatorio transferible ni fondeo; US$6.773m de pasivos financieros sin asignación económica documentada. La incertidumbre puede mover considerablemente el precio/acción y no está cuantificada; no calificarla como inmaterial. Estado CANDIDATO.


## Control de frontera F2→F3 tras actualizar H2 · 8-nov-2026

H2 ahora recibe los 2.687 valores fuente de H1 (11 bloques) por `Traspaso H1`, con comparación 12.155/12.155 y cero discrepancias. Las fórmulas de Input sheet y módulos históricos están vinculadas a esa fotografía; la captura es estática, no sincroniza nuevas modificaciones de H1 por sí sola. Se verificaron saldos de ventas LTM 38.523, EBIT 2.859, interés 235, equity 8.200 y deuda financiera 13.190 US$m en `Input sheet`.

**El estado de F3 sigue PENDIENTE:** NO existe cierre documentado de las utilidades atribuibles Commerce/Fintech, capital regulatorio excedentario/distribuible Fintech, fondeo atribuible, reinversión por unidad ni Ke/WACC validado. `Input sheet!A1` no se activó porque el motor muestra resultados no válidos antes de completar historias. `Tesis de Inversión y Supuestos!B61:C66` sigue N/D y `Escenarios e historias!K5/K6/K8` siguen PENDIENTE. No calcular ni presentar SOTP, MOS 35 %, matriz 5×5, DCF inverso o valor esperado a partir de cifras no verificadas. **No publicación ni fusión.**


## F3 · SOTP condicional reproducible — hipótesis no validadas (8-nov-2026)

Se ejecutó **una valoración numérica de contraste exclusivamente hipotética** *en el H2 ya existente* mediante ampliación de `Tesis de Inversión y Supuestos` de 120 a 310 filas (`A121:H309`). Se preservaron **H1, H2, nombres de libros, las 45 pestañas y las 1.883 huellas originales**; no se creó otro libro/revisión ni se cambió `Valuation output`, `Input sheet!A1`, `Tesis!B61:C66/B69` ni las celdas oficiales de escenarios, SOTP, MOS o app. Es una prueba de la materialidad de los datos ausentes, **NO una propuesta oficial que supere el gate de §4C**.

### Resultado del ejercicio, cierre 30-sep-2026, precio US$1.510 (06-nov-2026)

| Historia | EV Commerce FCFF (US$m) | Equity Fintech + residual FCFE (US$m) | Bonos corporativos supuestos deducidos (US$m) | Equity condicionado (US$m) | US$/acción | 35% MOS condicional |
|---|---:|---:|---:|---:|---:|---:|
| Conservadora | 12.817,38 | 8.419,39 | 2.253 | 18.224,42 | **359,48** | 233,66 |
| Base | 33.408,69 | 14.921,67 | 2.253 | 46.077,36 | **908,88** | **590,77** |
| Optimista | 67.769,16 | 21.515,19 | 2.253 | 87.031,35 | **1.716,70** | 1.115,86 |

Probabilidades originales Floyd: Conservadora 26,4706%, Base 47,0588%, Optimista 26,4706%; **esperado condicional US$977,29/acción**. Base −39,8% respecto al precio US$1.510; **NO hay Base oficial ni MOS oficial**. Los valores y el cuadro se enlazan nativamente en `Presentación!A46:L55` como **HIPOTÉTICOS**, manteniendo `Presentación!D6,G6,J6=N/D` en los resultados oficiales.

**Datos observados SEC:** Commerce ingresos LTM US$21.749m, Fintech ingresos LTM US$16.774m, EBIT consolidado US$2.859m, utilidad neta US$1.890m, acciones aprox 50,697m, bonos senior matriz US$2.253m, otros pasivos financieros por asignar US$6.773m, clientes US$17.400m y liquidez restringida US$14.559m. Fuentes: [SEC 10-Q 3T26](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000029/meli-20260930.htm), [carta 3T26](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000027/meli-20260930xex991.htm), H1 verificado. En 3T26 el grupo creció 45% en ingresos USD pero margen operativo de solo 6,3% por inversión en envíos/marketing; la historia no presume expansión inmediata.

**Hipótesis materiales no reveladas (todas rotuladas en H2, NO SEC):** 7% de margen EBIT actual de Commerce ⇒ EBIT Commerce supuesto US$1.522,43m, NOPAT US$1.096,15m tras impuestos normalizados 28%; el **residuo analítico** US$793,85m = NI consolidada US$1.890m − NOPAT Commerce estimado. Ese residuo **contiene Mercado Pago + corporativo + financiación + diferencias fiscales** y **NO es utilidad neta publicada de Fintech**; prolongarlo como utilidad Fintech es solo *hipótesis de cierre contable con riesgo material*. No se llenaron artificialmente las filas de capital y utilidad desagregada pendientes.

La Base condicional: Commerce ingreso +28% año 1, +21% a/a años 2–5, convergencia a +4,5% año 10; EBIT 7%→12% año10; S/C marginal 2,2 (1–5)→2,0 (6–10); ROIC terminal 14%, g 4%, WACC 11,2%. Fintech +residual utilidad +30% año1, +25% años2–5, +5,5% año10; ROE **marginal supuesto** 25%, ROE estable 16%, g 4%, Ke 13,8%. **Tasas iguales en las tres historias:** no se cargan tasas menores para Optimista ni mayores para Conservadora para fabricar spread. En Conservadora se aplica además una hipótesis de fracaso del 4%, sin aval empírico, solo al valor condicionado de esa historia. Cero caja adicional **presunta para puente**, no afirmación de caja libre real igual a cero.

Método explícito, años 1–10 con fórmulas Sheets (no números pegados): `Commerce FCFF_t=Revenue_t×Margin_t×(1−Tax)−ΔRevenue_t/SalesToCapital_t`, terminal `NOPAT_10(1+g)(1−g/ROIC_terminal)/(WACC−g)`; `Fintech residual FCFE_t=NI_t−ΔNI_t/ROE_incremental`, terminal `NI_10(1+g)(1−g/ROE_terminal)/(Ke−g)`. `Equity condicional=PV Commerce FCFF+PV residual FCFE−bonos holdco + caja libre hipotética cero`; evita descontar otra vez fondeo incluido ya en beneficio financiero. Esta fórmula **no certifica** RWA ni patrimonio económico inicial.

### Sensibilidad e impacto de incógnitas materiales

`Tesis!B277:F281` matriz **5×5** WACC Commerce (9,2–13,2%) × margen EBIT año10 (8–16%), equiv. por acción **US$453,09–1.793,94**; su centro `D279=908,88`. `Tesis!B288:F292` matriz **5×5** Ke Fintech (11,8–15,8%) × ROE marginal (18–32%), equiv. **US$782,09–1.059,36**; su centro `D290=908,88`. Ambas conservan demás supuestos y finanzas constantes. Si se asigna al holding 50% de US$6.773m sin atribuir, Base condicional baja **US$908,88→842,08**; con 100%, **US$775,28** (−US$133,60 por acción). Esta es una hipótesis adversa, NO decisión real de asignación.

Inverso **parcial**, no oficial: mantener hipótesis resto y resolver por sensibilidad lineal el margen Commerce año 10 que igualaría precio US$1.510: **19,6%**, vs 12% en Base; brecha de equity ≈US$30.474,81m. No subir márgenes para llegar a cotización. La incertidumbre individual supera los umbrales §4B; **no se puede declarar salvedad inmaterial**.

### QA técnico real de esta simulación

- Google Sheets devolvió **0 errores en los rangos de hipótesis y matrices** tras corregir dos errores de sintaxis de construcción de escenario y separadores decimales. En `Tesis!C302=0` conciliación de EBIT por puente analítico; `C303=7,2%` spread WACC−g; `C304=9,8%` spread Ke−g; `C305=100%` probabilidades; `C306=OK` orden de escenarios.
- Los centros de **ambas** matrices 5×5 reconciliaron con la Base condicional a una precisión numérica de Google Sheets.
- Huella registrada permanece 0/1.883; Control de integridad muestra `PLANTILLA`, `0/3 LISTO` y ninguna compuerta económica aprobada, **por diseño**: falta SOTP verificable. No se ejecutó validador externo del motor sobre esta simulación, ni JSON, pruebas end-to-end o publicación.
- **F3 oficial queda PENDIENTE.** Para convertir la simulación en una valoración SOTP oficial es obligatoria una separación con fuentes por entidad de EBIT Commerce, utilidad y patrimonio Fintech, capital regulatorio/distribuible, deuda y saldos internos, costo de capital auditable, historias y múltiplos aplicables. No se cambia `valorPrincipal` ni `baseMOS` del catálogo.

Identidad del ejecutor: GPT-6 en ChatGPT, herramientas Google Sheets, GitHub y consulta SEC. No se usó Claude, Work, Node/Python de repositorio, Vercel ni app para publicar. La cifra es ilustrativa, no recomendación de inversión.


## F3 · conciliación cruzada AZ Stocks/SEC y corrección del proxy Fintech (8-nov-2026)

**Este cierre actualiza y prevalece sobre el contraste condicional previo**, sin borrar las cifras antiguas ni cambiar el motor oficial. Se trabajó exclusivamente en la misma H1 de 19 pestañas, H2 de 45 y este PR #260; no se crearon libros/revisiones. Origen: [H1](https://docs.google.com/spreadsheets/d/1TF8KaMkn-Wc3csoCK1z9-IierhPhOBZwwdX7fiBYN6Q/edit); [H2](https://docs.google.com/spreadsheets/d/1wkFwjzufTR8KqrLSc7gxmxuB_qepFjEDc-LMuFi5oR0/edit). Datos SEC Q3 2026 y FY2025, consultas 8-nov-2026. En H2 las fórmulas del análisis viven en `Tesis de Inversión y Supuestos!A121:H430`; el SOTP official `B69`, `Input sheet!A1`, `Valuation output`, `Escenarios e historias` y las compuertas financieras no se activaron.

### 1. Actualización de la tesis AZ Stocks: problemas de fecha/método

[AZ Stocks, 12-jul-2026](https://azstocks.substack.com/p/mercadolibre-english-version) publica una **Base US$2.339/acción**, 40% DCF de perpetuidad (g 2,5%) y 60% DCF terminal a 13× EV/EBITDA; WACC 11,6%; deuda neta US$6.712m a corte anterior. Ventas FY2026 +37%, EBIT FY2026 8%, EBIT terminal **15,8% del CONSOLIDADO**; CAPEX/ventas 5,2% FY26 descendiendo. No equivale a un SOTP FCFF Commerce + FCFE Mercado Pago y NO es precio actualizado a 3T26.

Datos SEC: FY25 ingresos 28.893m, 9M25 20.134m, 9M26 29.764m, Q4'25 8.759m; ingresos 3T26 10.750m (+45,1% interanual), EBIT 676m (6,3%); EBIT 9M26 1.970m. El escenario AZ FY26 +37% implica ventas 39.583,41m, Q4'26 9.819,41m, **+12,1% interanual**. Su FY26 EBIT 8% exige Q4 EBIT 1.196,67m y **margen Q4 12,2%**, muy distinto a 6,3% en Q3. **No es imposible**, pero sin evidencia del rebote no es una Base contemporánea. La comprobación alternativa Q4 ventas +40%/EBIT Q4 7,5% implica FY26 ventas 42.026,6m (+45,5%) y margen EBIT FY26 6,88%; ambos son SUPUESTOS ilustrativos, no guía SEC. Todo queda por fórmula en `Tesis!B314:B336`.

### 2. Conciliación obligatoria de caja: 4 de 4 períodos a cero

SEC FY25 y [carta Q3 2026](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000027/meli-20260930xex991.htm): en 9M26 (US$m) **8.687 CFO + 38 ajuste − 3.574 fondos restringidos − 1.215 CAPEX − 6.212 nueva cartera + 2.719 fondeo Fintech = 443 ajustado**. FY25=1.481, 9M25=718, LTM=1.206, todos con residuo 0 en `Tesis!B341:E349` y en H1 `Mercado Pago!B3:G11`. En cambio CFO−CAPEX GAAP 9M26=7.472 y LTM=12.254, un factor LTM **10,16×** sobre el ajustado (brecha **US$11.048m**). El FCF simple/OCF de varios modelos (y ratios P/FCF) es **no distribuible** si incluye flujos de clientes/crédito, independientemente de que la provisión haya sido no monetaria al devengo.

La SEC también presenta 9M26 fondeo neto de Fintech **+2.719** y de Commerce+corporativo **+974**. GAAP neto de emisión/amortización de préstamos **+3.860**; diferencia de perímetro de caja **167** (FY25 57, 9M25 40, LTM 184). Eso ayuda a CLASIFICAR el flujo histórico, **no prueba el stock de pasivos atribuible por entidad al 30-sep-2026 ni el capital distribuible**. `Tesis!A350:F355` contiene los residuos. Sigue sin asignar US$6.773m en pasivos financieros del balance, que NO se imputan sin soporte.

### 3. Corrección de normalización por intereses/FX/impuestos (no doble contar bonos)

**Error demostrado del ejercicio previo:** se usaba "Fintech utilidad" = NI grupo (1.890) − Commerce NOPAT supuesto (1.096,15) = **793,85 US$m**. Esa NI incluía intereses/gastos corporativos y FX mientras los bonos de matriz US$2.253m se deducían por separado del EV Commerce; la interpretación mezclaba FCFF y FCFE.

**Corrección ejecutada en `Tesis!B134:D134`:** NOPAT operativo residual = (EBIT grupo 2.859 − Commerce EBIT supuesto 1.522,43) × (1−28%) = **962,33 US$m**. El puente de US$168,48m se atribuye exactamente a ingreso financiero LTM +120, gasto −235, FX −174, y diferencia entre impuesto GAAP 680 y tributación normalizada a 28%; resultado antes de impuestos 2.570 y neto 1.890, ambos conciliados; `Tesis!B375=0`. **Importante**: 962,33 es un proxy operativo mixto **Fintech+corporativo**, NO utilidad Fintech revelada, no FCFE distribuible ni ROE por entidad. Se conserva un solo cargo por bonos dentro de las hipótesis y el riesgo de atribución de deuda no se resuelve por la sola normalización.

Resultados condicionales después de la corrección (US$/acción):

| Historia | Antes | Después | MOS hipotético al 35% |
|---|---:|---:|---:|
| Conservadora | 359,48 | 393,31 | 255,65 |
| Base | **908,88** | **971,35** | **631,38** |
| Optimista | 1.716,70 | 1.806,77 | 1.174,40 |
| Esperado ponderado | 977,29 | **1.039,48** | NO corresponde |

La Base sube US$62,47/acción solo por normalización; el supuesto central 7% EBIT Commerce, ROE/Ke Fintech, 11,2% WACC Commerce y 14% ROIC terminal permanecen hipótesis, sin separación fuente. Respecto a cotización de corte US$1.510, la Base es ~−35,7%. Base/MOS oficiales permanecen N/D y sin publicación. Historial antes→después en `Tesis!A360:C384`. Huella del motor oficial no alterada.

### 4. Atribución verificable de la diferencia con AZ: terminal

Sin tocar el crecimiento ni reinversión de JMR, `Tesis!A408:F421` aplica el **13× EBITDA de AZ al terminal de Commerce exclusivamente** (NO al consolidado de AZ). Commerce año 10 ventas 100.563,95m, EBIT 12.067,67m; D&A/ventas proxy 2,81% de LTM consolidado (no SEC segmentado) ⇒ EBITDA 14.892,23m. VP terminal Commerce por perpetuidad **31.008,52m**, a 13× EBITDA **66.966,11m**, **delta +35.957,60m = +US$709,27 por acción**; con el peso 60% de AZ aplicado SOLO a esta palanca, Base condicional alterna aprox **US$1.396,91**, frente a 971,35; **31,1% de la brecha** contra 2.339 se explica por terminal/método bajo este experimento. No atribuir el 68,9% restante a margen, tasa o ROE sin calcular cada contrafactual de perímetro homogéneo. La aplicación de 13× **no convierte** la cifra JMR en Base válida.

### 5. Contraste de otros modelos y sesgos de caja

- [Alpha Spread](https://www.alphaspread.com/security/nasdaq/meli/summary) muestra una cifra online aprox US$3.184,08 y un [modelo FCFE](https://www.alphaspread.com/security/nasdaq/meli/dcf-valuation) con descuento 8,6%, crecimiento 21,6%, net margin 4,9→7,6%, siete años y salida 1,7× ventas. No equivale a tasas ni flujos Floyd; la cifra publicada previamente como 3.306 no es la página consultada ahora.
- [Manfredi Investment](https://manfredinvestment.com/informes/meli) (corte 2T26) DCF Base ~US$1.957,44 con WACC 12%, g 3%, FCF ≈ ventas × (margen OCF − CAPEX/ventas). La metodología que proyecta CFO temprano **no resuelve el financiamiento de cartera ni fondos clientes**; ancla CFO LTM junio ~13.905m y presupone margen OCF año 1 32%, distinto de flujo ajustado LTM Sep de solo 1.206m. No trasladar su cash flow a FCFE.
- [Faircurve](https://faircurve.io/research/MELI) 7-nov-2026 US$1.755,07: múltiplos forward EV/EBITDA, 2.000 simulaciones, pares mayormente retail, no son financieros latinoamericanos. Reporta FCF/net income 6,21× como calidad; por las notas SEC ese dato requiere ajustar depósitos/clientes/crédito antes de interpretarse como caja del accionista.
- [SweetValueLab](https://sweetvaluelab.com/stocks/meli) modelo 5 años perpetuo ≈US$1.523,33 vs 10 años ≈US$2.213,69; gran sensibilidad a horizonte/salida, mismo riesgo de ratios de FCF sin limpieza crediticia. Datos de página dinámica, snapshot consulta 8-nov-2026.

Las cifras externas se registraron como comparables **diagnósticos sin peso oficial** en `Tesis!A387:F430`.

### 6. Estado, pruebas y salvedades

- QA nativo Sheets: EBIT→NI según SEC 2.859 + 120 −235 −174 −680 = 1.890; impuestos y NOPAT residuo 0; ajustes CFO 4/4 = 0; centros de matrices 5×5 tras recalcular = Base condicional; tasas terminales WACC Commerce − g=7,2pts; Ke Fintech − g=9,8pts. Huella registrada 0/1.883; compuertas `0/3 LISTO`, `PLANTILLA` por `Input sheet!A1` deliberadamente vacío.
- **Materialidad** §4B: efectos separados superiores al 2% (normalización +US$62,47, valor terminal +US$709,27, deuda no atribuida hasta −US$133,60/acción). Ninguno es inmaterial; no son recomendaciones de ajustes sin atribución financiera.
- **Bloqueos F3**: resultados netos por negocio, costos corporativos y eliminaciones, capital elegible/RWA por institución Mercado Pago, caja excedentaria Commerce, deuda completa por perímetro, valoración de I+D (proxy), beta/ERP/riesgo país y Ke/WACC verificados, RSU y tres escenarios OFICIALES + múltiplos. Ausencia de los datos impide acotar SOTP Base con calidad publicable. **CANDIDATO; sin publicación, sin nueva revisión; F5 independiente posterior**.

Identidad y herramientas: GPT-6 en ChatGPT; web SEC, AZ y pares, conectores Google Sheets/Docs, GitHub; cálculos independientes de verificación. No Work ni validadores Python/Node del repositorio, ni despliegue. Cambios por Sheets en H2 y por Google Docs en el documento N1/N2; no se alteró el modelo Damodaran ni se certificó un guardrail no ejecutado.
