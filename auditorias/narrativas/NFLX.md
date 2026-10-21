# Auditoría económica narrativa — Netflix, Inc. (NFLX)

> Auditoría de la valoración JMR vigente de NFLX (precio de análisis del 30-sep-2026, estados al 30-jun-2026), emitida el 21-oct-2026. Verifica, contradice y emite dictamen; **no se modificó la valoración**. Las cifras nuevas son propuestas que requieren un ciclo posterior de Valoración. Etiquetas: [OBSERVADO] hecho en documento fechado; [MODELO] salida de la hoja; [INFERENCIA] cálculo del auditor a partir de lo anterior; [HIPÓTESIS] juicio o supuesto; [NO VERIFICADO] sin fuente primaria accesible.

## 1. Ficha de auditoría y alcance

| Campo | Valor |
|---|---|
| Emisor / ticker | Netflix, Inc. · NFLX · acciones ordinarias (una clase) [OBSERVADO] |
| Sector / mercado | Entretenimiento por streaming · NASDAQ (EE.UU.) · ingresos por cuatro regiones (UCAN, EMEA, LATAM, APAC) |
| Moneda y escala | US$; millones salvo indicación; acciones en millones |
| Método intrínseco principal | DCF Base de FCFF (compañía operativa): **US$61,04 por acción** [MODELO] |
| Valoración auditada | Hoja «Modelo JMR - NFLX (desde cero 2026-10-21)», ID `1Qx8jFSxX5LzkKzhWsPgHfeKy9c33eNygVtN4_O-Ze3E`; registro `Modelo-JMR-datos/valoraciones/NFLX-1792548021734.json`; informe de valoración `NFLX_Valoracion_Modelo_JMR_2026-09-30.md`; análisis fundamental `NFLX_Research_Fundamental_Modelo_JMR_2026-10-21.md` y Nivel 2 `NFLX_Nivel2_Datos_Modelo_JMR_2026-10-21.md` |
| Fecha de valoración / auditoría | Valoración con precio del 30-sep-2026; auditoría el 21-oct-2026 |
| Corte de estados | 10-K 2025 (23-ene-2026) y 10-Q del 2T26 (balance al 30-jun-2026); LTM jul-2025 a jun-2026 |
| Precio del análisis | US$69,58, cierre del 30-sep-2026 (Yahoo Finance, sin ajustar) [OBSERVADO en `reference/corte_vigente.json`] |
| Precio de hoy | **N/D**: no se obtuvo una cotización del 21-oct-2026 con fuente verificable. Los resultados del 3T26 (20-oct-2026) pueden haber movido el precio; esta auditoría no lo asume |
| Estado de verificación | **Con reservas** (no es una auditoría contable) |

**Documentos que se examinaron:** la hoja (estados, `Input sheet`, `Valuation output`, escenarios, costo de capital, múltiplos y pestaña «Sensibilidad DCF»), el JSON de valoración, el informe de valoración, el análisis fundamental, el Nivel 2, el 10-K 2025, el 10-Q del 2T26 y las cartas a accionistas del 2T26 y del 3T26. **Quedaron fuera:** conciliación celda por celda de todas las fórmulas de múltiplos y de «Relativa v2 · Sensibilidad», series históricas de múltiplos de peers (no se recuperaron de nuevo), calificación crediticia vigente y cualquier dato posterior al 21-oct-2026.

**Limitación de independencia (declarada):** el mismo equipo y la misma sesión de trabajo produjeron la valoración y esta auditoría. Eso reduce su independencia organizativa; para compensarlo se recalculó el DCF con un script propio que no lee la hoja (sección 10) y se buscaron activamente argumentos contrarios. Un tercero debería repetir las pruebas antes de tratar el dictamen como externo.

## 2. Resumen ejecutivo y relato económico central

Netflix cobra una suscripción mensual (cada vez más con plan con anuncios) por un catálogo de series, películas, eventos en vivo y juegos que produce, licencia y distribuye con su propia red de entrega. En 2025 ingresó US$45.183 M (+15,9%) con margen operativo GAAP de 29,5%; en el LTM a junio de 2026 ingresó US$48.371 M con margen de 29,7% [OBSERVADO]. El negocio es de costo fijo alto (el contenido se amortiza de forma acelerada) y costo marginal bajo por miembro adicional, y de ahí sale el apalancamiento operativo: el margen pasó de 17,8% en 2022 a 29,5% en 2025.

Qué está cambiando: el crecimiento depende cada vez más del precio por miembro, de la publicidad y de las regiones fuera de Norteamérica (UCAN creció +10% en el 2T26 frente a +21% de LATAM y +16% de APAC), mientras que el tiempo de visualización crece alrededor de 2% [OBSERVADO en cartas del 2T26 y análisis]. El 20-oct-2026 la compañía reportó ingresos del 3T26 de US$12.874 M (+11,8%), margen operativo de 34,6% (adelantado por el momento de los gastos), guió el 4T26 con margen de 26,0% y mantuvo el año 2026 en ingresos de US$51,1 mil millones (+13%) y margen de 31,5% [OBSERVADO en la carta del 3T26]; esos hechos son posteriores al corte de la hoja y no están en los números.

**Tesis Base favorable.** La escala de audiencia reparte el costo de cada título entre más miembros, el precio sigue subiendo sin pérdida de retención, la publicidad se vuelve una segunda línea y el margen EBIT converge de 31,9% en el año 1 a 36,4% en el año 5. Eso da crecimiento de 11,1% en el año 1 que se desacelera a 6,8% en el año 5 y DCF Base de US$61,04. **Interpretación neutral.** El precio del 30-sep (US$69,58) es 14,0% superior a ese valor: el mercado paga por un crecimiento de los años 1–5 cercano a 11% (DCF inverso del informe: 11,4%) frente al 8,9% de la Base. **Contratesis adversa.** Si la atención se reparte con YouTube, el video corto y los juegos, el precio por miembro deja de compensar un uso plano, el contenido absorbe el margen (Conservadora: margen 32,9%, valor US$49,29) y, en el extremo, los fundamentales se deterioran (Disrupción: US$22,91).

**Supuesto que domina el valor.** La combinación crecimiento de los años 1–5 y margen objetivo: ±2 puntos de crecimiento anual mueven el valor entre US$54,95 y US$67,78 y el margen entre 32,35% y 40,35% lo mueve entre US$54,25 y US$67,83 [MODELO, pestaña «Sensibilidad DCF»]. Detrás de ellos el valor terminal pesa 59,1% del valor operativo. **Contradicción que la empresa debe resolver:** el margen objetivo de 36,4% está por encima de cualquier régimen histórico (mejor año: 29,5%; mejor trimestre: 34,6% por el momento de gastos), mientras el uso por miembro casi no crece; la historia del margen depende de que el precio y la publicidad sigan compensando.

## 3. Trazabilidad, integridad y jerarquía de evidencia

| Dato | Valor | Período/perímetro | Tipo | Documento/URL/fecha | Hoja/celda | Verificación |
|---|---|---|---|---|---|---|
| Ingresos LTM | US$48.370,8 M | jul-2025 a jun-2026 | [OBSERVADO] derivado | 10-K 2025 y 10-Q 2T26: 45.183,0 + 24.809,7 − 21.622,0 | `Input sheet`!B12 | Reconciliado: coincide |
| EBIT GAAP LTM | US$14.354,5 M | LTM | [OBSERVADO] | 10-Q 2T26 (https://www.sec.gov/Archives/edgar/data/1065280/000106528026000212/nflx-20260630.htm) | `Income Statement` | Coincide con Nivel 2 |
| EBIT base de valoración | US$14.973,5 M | LTM + 619 | [MODELO] ajuste | Cargo no recurrente de Brasil (impuestos no sobre la renta) | `Input sheet`!B13 | Ajuste explicado; el monto del cargo se acepta del análisis, [NO VERIFICADO] contra nota del 10-Q por esta auditoría |
| Impuestos | 17% (efectivo) → 25% (marginal) | años 1–5 / año 10 | [MODELO] | Análisis fundamental, sección 17 | `Input sheet`!B24, B25 | Reproducido |
| Capex / flujo libre LTM | −US$819 M / US$11.152 M | LTM | [OBSERVADO] | 10-Q 2T26 | `Cash Flow` | Coincide |
| Caja e inversiones | US$9.127,9 M | 30-jun-2026 | [OBSERVADO] | 10-Q 2T26 | `Balance Sheet` | Incluye la comisión de WBD de US$2.800 M |
| Deuda financiera | US$14.309,3 M (notas senior) + arrendamientos ~US$2.327 M = US$16.636 M | 30-jun-2026 | [OBSERVADO]/[MODELO] | 10-Q 2T26 | `Input sheet`, bloque arrendamientos | Suma reproducida |
| Acciones | 4.165,9 M (4.163,9 + 2,0 de RSU) | 30-jun-2026 | [OBSERVADO] | Portada 10-Q 2T26 | `Input sheet`!B22 | Coincide. La carta del 3T26 reporta 4.195 M diluidas promedio (incluye opciones) [OBSERVADO] |
| Opciones | 123,9 M a US$39,21, 4,6 años, vol. 33,8% | 30-jun-2026 | [OBSERVADO]/[MODELO] | 10-K/10-Q | `Option value` | Valor total US$4.973 M; ver H13 |
| Precio de análisis | US$69,58 | 30-sep-2026 | [OBSERVADO] | Yahoo Finance, cierre sin ajustar | `Input sheet`!D1 | Fecha consistente |
| Tasa libre de riesgo | 5,29% | 30-sep-2026 | [OBSERVADO] | Tesoro de EE.UU. a 10 años (serie DGS10) | `Cost of capital worksheet` | Coincide con el archivo de corte |
| Prima de mercado | 4,92% (ponderada por regiones) | oct-2026 | [OBSERVADO] | Damodaran, https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx | `Cost of capital worksheet`!H23–H31 | Ponderación reproducida sobre las ventas regionales del LTM |
| Beta desapalancada del sector | 0,98 (Entertainment global) → 1,02 apalancada | enero 2026 | [OBSERVADO]/[MODELO] | Damodaran, https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html | `Cost of capital worksheet`!B14 | Reapalancamiento reproducido |
| Peers (DIS, SPOT, ROKU) | múltiplos y márgenes | 30-sep-2026 | [OBSERVADO] secundario | Yahoo Finance vía yfinance (https://finance.yahoo.com/quote/DIS/ y análogas) | `Financials Multiples` | Fuente secundaria; no se contrastó con estados de cada par |
| Hechos posteriores | 3T26: ingresos US$12.874 M, margen 34,6%, FCF 2026 guiado ~US$12.000 M, publicidad 2026 ~US$2.700 M | 20-oct-2026 | [OBSERVADO] | Carta del 3T26 (https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm) | No incorporado | Pendiente de ciclo de valoración |

**Diferencias de fuente, ajustes y versiones.** (i) Se usan dos EBIT: el GAAP de 14.354,5 y el base de 14.973,5 (más 619 de Brasil); sólo el segundo alimenta ROIC y márgenes de referencia, no el flujo proyectado. (ii) El LTM no es el último año calendario: se reconcilia como 45.183,0 + acumulado de seis meses de 2026 (24.809,7) − acumulado comparable de 2025 (21.622,0). (iii) El informe de valoración conserva la fecha del 30-sep-2026 mientras que la hoja se titula «2026-10-21»; la fecha de la hoja es la de construcción y la de los datos de mercado, la del 30-sep. (iv) No se encontraron versiones contradictorias del registro tras la migración del 21-oct (consistencia M1–M3, H1–H3 e I1 en OK al cierre de esta auditoría).

**Hallazgo de proceso.** Durante la construcción, un paso no idempotente de corrección de la hoja multiplicó una vez por 100 el número de acciones; se detectó al comparar valor por acción contra equity ÷ acciones, se reescribió con valores absolutos y se regeneró todo antes de publicar. El valor final (4.165,9 M) coincide con la portada del 10-Q. Queda como H12 para que el paso tenga una prueba de idempotencia.

## 4. Historia financiera: diez años y punto de partida

Todas las cifras en US$ M, ejercicios cerrados en diciembre; fuente: hoja, pestañas de estados (Nivel 2) [OBSERVADO]. El LTM llega a junio de 2026.

| Métrica | 2016 | 2018 | 2020 | 2022 | 2023 | 2024 | 2025 | LTM |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Ingresos | 8.831 | 15.794 | 24.996 | 31.616 | 33.723 | 39.001 | 45.183 | 48.371 |
| Crecimiento | n/d | 35,1% | 24,0% | 6,5% | 6,7% | 15,7% | 15,9% | n/d (3T26: +11,8%) |
| Margen operativo | 4,3% | 10,2% | 18,3% | 17,8% | 20,6% | 26,7% | 29,5% | 29,7% |
| Margen de flujo libre | −17,9% | −18,1% | 7,7% | 5,1% | 20,5% | 17,7% | 20,9% | 23,1% |
| ROIC (EBIT×(1−17%)/capital invertido) | 6,9% | 11,3% | 19,9% | 16,1% | 20,6% | 28,1% | 34,5% | 33,7% |
| Deuda neta / EBITDA | 4,34x | 3,89x | 1,72x | 1,39x | 1,01x | 0,56x | 0,40x | 0,35x |
| Acciones diluidas promedio (M) | 4.387 | 4.512 | 4.542 | 4.513 | 4.495 | 4.393 | 4.344 | 4.292 |

| Comparación | Último | Prom. 3 años (2023–25) | Prom. 5 años (2021–25) | Prom. 10 años | Rango 10 años |
|---|---:|---:|---:|---:|---|
| Crecimiento de ingresos | 15,9% (2025) | 12,8% | 12,7% | 20,3% (CAGR 20,4%) | 6,5% a 35,1% |
| Margen operativo | 29,5% | 25,6% | 23,1% | 16,8% | 4,3% a 29,5% (LTM 29,7%) |
| ROIC | 34,5% | 27,7% | 23,9% | 18,0% | 6,9% a 34,5% |
| Margen de flujo libre | 20,9% | 19,7% | 12,8% | 0,3% | −18,1% a 23,1% |

*Los promedios son del auditor [INFERENCIA] sobre las filas anuales de la hoja; el de 3, 5 y 10 años de margen operativo y de flujo libre coincide con el análisis fundamental.*

**Lectura.** (a) Ciclo: 2016–2019 es una fase de crecimiento financiado con deuda (flujo operativo negativo hasta −US$2.887 M en 2019); 2022–2023 es una pausa de crecimiento (6,5% y 6,7%) con saturación en Norteamérica y competencia; 2024–2025 es la reaceleración por precio, control de cuentas compartidas y publicidad. (b) Cambios contables: los activos de contenido netos (US$33.838 M en el LTM, 58% del activo) figuran con valor cero en la hoja hasta 2023 y con saldo desde 2024, de modo que la serie de balance 2016–2023 no es homogénea con la posterior [OBSERVADO en Nivel 2]. (c) Anomalías: el LTM incluye la comisión de terminación de WBD (US$2.800 M antes de impuestos, ~US$0,40 de BPA) y el cargo de Brasil de 2025 (US$619 M); por eso el margen neto LTM (28,2%) y el P/E LTM (21,9x) no son comparables sin ajuste. (d) Último trimestre: 3T26, ingresos US$12.874 M, margen 34,6% frente a 28,2% en el 3T25 [OBSERVADO]. (e) Límite de homogeneidad: el ROIC de la hoja usa una tasa fija de 17% y el capital contable más deuda menos caja, sin arrendamientos ni contenido en producción, por lo que no es comparable con el ROIC terminal de Damodaran (11,04%) sin esa advertencia.

## 5. Crecimiento de ingresos: de la historia a la proyección

**La historia que tendría que ocurrir.** La Base supone que los ingresos pasan de US$48.371 M (LTM) a US$98.556 M en el año 10: crecimiento de 11,1% en el año 1 (jul-2026 a jun-2027), CAGR de 8,3% en los años 2–5 y de aproximadamente 5,9% en los años 6–10 [MODELO, `Valuation output` fila de crecimiento], hasta un crecimiento terminal de 5,29%. El motor es el precio por miembro, la publicidad y el crecimiento de APAC/LATAM/EMEA; UCAN (44% de los ingresos) se desacelera por base alta. La verificación contra la hoja: el año 1 coincide con `Input sheet` B27 (11,1%) y el CAGR de los años 1–5 recalculado por el auditor es 8,9% ((74.013/48.371)^(1/5) − 1), igual al 8,9% que usa el informe.

**Prueba de coherencia con los hechos más recientes** [INFERENCIA]. Con el 3T26 (US$12.874 M) y el 4T26 guiado (US$13.442 M), el segundo semestre de 2026 suma US$26.316 M, +11,7% frente al mismo período de 2025 (US$23.561 M). Para alcanzar US$53.742 M en el año 1, el primer semestre de 2027 debe ingresar unos US$27.426 M, +10,5% sobre el primer semestre de 2026 (US$24.810 M). Con +11,5% guiado para el 4T26, el año 1 exige una desaceleración de aproximadamente un punto: es alcanzable pero ya no tiene colchón si el 1T27 repite el ritmo del 3T26 (+11,8%) menos un efecto cambiario favorable que la compañía no promete.

**Seis preguntas (crecimiento, años 1–5).**
- (a) Valor exacto: 11,1% (año 1), 9,9%, 8,8%, 7,8%, 6,8% (años 2–5); `Input sheet`!B27 y B29; `Valuation output` fila 4; unidad: crecimiento anual de ingresos totales en US$.
- (b) Histórico: último 15,9%; 3 años 12,8%; 5 años 12,7%; 10 años 20,3% (CAGR 20,4%); trimestres recientes +13,4% (2T26) y +11,8% (3T26). La Base queda por debajo del promedio de 3 y 5 años y por encima del peor régimen (6,5%–6,7%).
- (c) Mecanismo: cada año los miembros pagan más (precio), la publicidad añade ingresos por usuario y APAC/LATAM crecen a dos dígitos; la oferta de eventos en vivo y deporte sostiene la audiencia.
- (d) Hechos que deben ocurrir: retención estable tras las alzas de precio de 2026 (la compañía dice que la respuesta fue la esperada), publicidad que escale (la guía de 2026 bajó de ~US$3.000 M a ~US$2.700 M), y crecimiento fuera de Norteamérica que compense a UCAN (+10%).
- (e) Hechos que la refutan: crecimiento de ingresos por debajo de 9% en el primer semestre de 2027; publicidad 2027 por debajo de ~US$3.500 M [HIPÓTESIS del auditor]; horas vistas por miembro en caída; churn por encima del reportado.
- (f) Impacto: −2 pp anuales en los años 1–5 deja la Base en US$54,95 (−10,0%); +2 pp en US$67,78 (+11,0%); −4 pp en US$49,45 con margen de la Base. Reproducido por el auditor: −2 pp US$54,81, +2 pp US$67,63 [INFERENCIA].

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Crecimiento de ingresos, años 1–5 | 12,8% / 12,7% / 20,3%; 2T26 +13,4%, 3T26 +11,8% | 11,1% → 6,8% (CAGR 8,9%); `Input sheet`!B27, B29 | Streaming: SPOT y ROKU 14%–22% a FY+3 según el informe; DIS y CMCSA bajos; fuente yfinance 30-sep-2026 | Precio + publicidad + mercados nuevos; requiere retención estable y publicidad escalando | Horas vistas +2%; UCAN +10%; guía de publicidad recortada | −2 pp: US$54,95; +2 pp: US$67,78 (matriz 3) |
| Crecimiento años 6–10 | n/a (10 años: 20,3% pero etapa distinta) | 6,5% → 5,3%; `Valuation output` años 6–10 | Sin referencia comparable; Damodaran no publica crecimiento de la industria por año | Convergencia lineal hacia 5,29% | La convergencia a Rf no se apoya en un benchmark; ver sección 9 | N/D (la hoja no varía los años 6–10 por separado) |
| Crecimiento terminal | n/a | 5,29% = Rf; `Input sheet` (tg) | Rf a 10 años: 5,29% (30-sep-2026) | Crecimiento nominal de la economía no puede superarse a perpetuidad | Un 5,29% nominal es alto frente a los 4%–4,5% habituales para el PIB nominal de largo plazo [HIPÓTESIS] | g = 4,29%: US$56,97 (−6,7%) |

**Alternativa razonable.** Un año 1 de 10,5%–11,0% (más cercano al 3T26 y al 4T26 guiado), años 2–5 de 7%–8% y sin cambios en el margen. No se cuantificó con el motor de la hoja; con la matriz 3 una resta de 1 pp anual daría aproximadamente US$57,6 [INFERENCIA por interpolación; no ejecutada].

## 6. Márgenes operativos y normalización de beneficios

**La historia que tendría que ocurrir.** El margen EBIT de valoración (ajustado por arrendamientos, +0,35 pp) pasa de 31,85% en el año 1 a 36,35% en el año 5 y se mantiene [MODELO, `Input sheet` B28 y B30; `Valuation output` fila de margen]. La guía de 2026 es 31,5% [OBSERVADO en la carta del 2T26 y reiterada en la del 3T26], de modo que el año 1 está anclado a la guía. El tramo adicional de 4,5 puntos en cuatro años depende de que la amortización de contenido crezca menos que los ingresos (en 2025 creció 7% frente a 16% de ingresos) y de que la publicidad escale sobre costo casi fijo.

**Verificación de ingreso × margen = EBIT** [INFERENCIA]: año 1, 53.742 × 31,85% = 17.116 y, con 17% de impuesto, NOPAT = 14.207 (el valor de la hoja); año 10, 98.556 × 36,35% × (1 − 25%) = 26.870 frente a 26.872 en la hoja. Sin diferencias materiales.

**Normalización.** El EBIT GAAP LTM (14.354,5) más el cargo de Brasil (619) da 14.973,5 (31,0% normalizado); la comisión de WBD no está en el EBIT sino en otros ingresos, y por eso afecta al P/E y al flujo, no al margen operativo. El 3T26 (34,6%) debe leerse con cautela: la compañía dice que se adelantó por el momento de gastos y guía 26,0% para el 4T26 (incluye ~120 pb de reducciones de personal), de modo que el promedio del segundo semestre de 2026 es ~30,2% [INFERENCIA: (4.459 + 3.500) / 26.316].

**Seis preguntas (margen objetivo de 36,35%).**
- (a) 36,35% en el año 5 y siguientes (36,4% en el informe); `Input sheet`!B30; ajustado por arrendamientos.
- (b) Margen operativo: último 29,5% (LTM 29,7%; 31,0% normalizado); 3 años 25,6%; 5 años 23,1%; 10 años 16,8%; mejor año 29,5%; peor régimen 4,3%–10,2% (2016–2018).
- (c) Mecanismo: la audiencia global reparte el costo de cada título; el precio sube más que el costo de contenido; la publicidad añade margen de contribución alto; el costo de revisión de personal reduce gastos generales.
- (d) Hechos requeridos: amortización de contenido creciendo por debajo de los ingresos durante cuatro años más; costo de derechos de deportes en vivo contenido (hoy ~5% del gasto de contenido y ~1% de las horas según el análisis); sin nuevo ciclo de inflación de costos de producción.
- (e) Hechos refutadores: margen operativo anual por debajo de 31% en 2027; amortización de contenido por encima de 50% de los ingresos; aumento del gasto en contenido para defender horas vistas; regulación fiscal tipo Brasil recurrente.
- (f) Impacto: el eje de margen de la matriz 3 va de 32,35% (−4 pp) a 40,35% (+4 pp) y mueve el valor entre US$54,25 y US$67,83 con el crecimiento de la Base; un punto de margen vale ~US$1,7 por acción [INFERENCIA de la matriz]; el auditor reprodujo +2 pp en US$64,23 (hoja: US$64,43).

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Margen EBIT objetivo (año 5 en adelante) | 25,6% / 23,1% / 16,8%; LTM 29,7%; mejor año 29,5% | 36,35%; `Input sheet`!B30, año de convergencia 5 (B31) | Mediana de peers ~14% (yfinance, 30-sep-2026); Entertainment de Damodaran: N/D en la hoja como cifra citada | Operating leverage + publicidad + precio; requiere amortización de contenido < ingresos | Ningún año histórico supera 29,5%; el 3T26 de 34,6% es de calendario de gastos; 4T26 guiado 26,0% | −4 pp: US$54,25; +4 pp: US$67,83 (matriz 3, fila de crecimiento 0) |
| Margen año 1 | 29,7% LTM; 31,0% normalizado | 31,85% (guía 2026 31,5% + 0,35 pp de arrendamientos); `Input sheet`!B28 | Guía de la compañía (carta del 2T26, reiterada en el 3T26) | Guía realizada hasta el 3T26 | Cada trimestre puede variar ±4 pp por momento de gastos | Bajo: dentro de la guía |
| Tasa de impuesto | Efectiva 17% (ROIC histórico) | 17% → 25% al año 10; `Input sheet`!B24, B25 | Marginal de EE.UU. 25% | Convergencia a la tasa marginal | Netflix tiene exposición internacional y créditos; el 17% efectivo puede ser alto o bajo según mix | Tasa +2 pp en toda la proyección: N/D, no ejecutada |

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

**La historia que tendría que ocurrir.** La reinversión del modelo se calcula como cambio de ingresos del año siguiente dividido entre ventas/capital: 1,824 en los años 1–5 y 1,486 en los años 6–10 [MODELO, `Input sheet` B32 y B33]. El auditor verificó la convención de Damodaran: la reinversión del año 1 (US$2.916 M) es igual a (59.061 − 53.742) / 1,824 y la del año 10 (US$3.508 M) es igual a 5,29% × 98.556 / 1,486. Esto significa que el capital se invierte con un año de anticipación respecto de los ingresos que lo usan.

**Retornos.** El retorno incremental implícito en los años 1–5 es margen × (1 − t) × ventas/capital = 31,9%–36,4% × 83% × 1,824 ≈ 48%–55%; en los años 6–10 ≈ 40%–45% (36,35% × ~80% × 1,486). Son superiores al ROIC contable LTM de 33,7% y muy superiores al ROIC terminal de 11,04%. La evidencia histórica favorece la cifra alta: entre 2022 y el LTM a junio de 2026 Netflix sumó US$16.755 M de ingresos con US$6.261 M de capital invertido adicional y subió el EBIT de US$5.633 M a US$14.354 M [OBSERVADO según el análisis; cálculo reproducido con las filas de balance]. Un cociente de ventas/capital incremental de 2,7 (16.755 / 6.261) está por encima de los 1,82 y 1,49 del modelo: el modelo reinvierte más de lo que la historia reciente pedía, y eso es prudente.

**Asignación de capital.** Recompras de US$9.921 M en el LTM (US$9.127 M en 2025, US$6.264 M en 2024) frente a flujo libre de US$11.152 M: la compañía devuelve ~89% del flujo libre vía recompras, sin dividendo; el conteo diluido pasó de 4.542 M en 2020 a 4.292 M en el LTM [OBSERVADO]. La deuda neta es 0,35x EBITDA. La compañía intentó comprar negocios de Warner Bros. Discovery y terminó recibiendo una comisión de US$2.800 M tras ser desplazada por Paramount Skydance (feb-2026) [OBSERVADO según el análisis]: la adquisición, de haberse hecho, habría cambiado el perímetro y la reinversión; la valoración no la incluye, y es correcto.

**Seis preguntas (ventas/capital y ROIC terminal).**
- (a) 1,824 (años 1–5) y 1,486 (años 6–10); ROIC terminal 11,04%; `Input sheet`!B32, B33, B49, B50.
- (b) ROIC contable 34,5% (2025), 33,7% (LTM); 3 años 27,7%; 5 años 23,9%; 10 años 18,0%; rotación del capital invertido 1,37x en el LTM, 1,09x–1,93x en diez años.
- (c) Mecanismo: el contenido original se produce una vez y se monetiza en todos los mercados; las nuevas inversiones (publicidad, vivo, juegos) piden menos capital por dólar de ingreso que el contenido original.
- (d) Hechos requeridos: el gasto en contenido sigue una trayectoria de ingresos/capital ≥ 1,5 durante la década; capex bajo (US$819 M LTM, 1,7% de ingresos).
- (e) Hechos refutadores: aumento del gasto en deportes y vivo con retornos menores; adquisiciones; inflación del costo de producción; ROIC incremental por debajo del costo de capital.
- (f) Impacto: ROIC terminal igual al costo de capital (8,99%) → US$53,10 (−13,0%), reproducido US$52,96; 13% → US$66,29 (+8,6%); 15% → US$70,23 (+15,1%).

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Ventas/capital años 1–5 | Rotación 1,2–1,4x (3 años); incremental 2022–LTM: 2,7x | 1,824; `Input sheet`!B32 | Rango empresa/marginal/sector de la hoja; fuente Damodaran enero 2026: N/D en cifra | Cada dólar de ingreso nuevo requiere ~US$0,55 de capital | Los pipelines de contenido y las alzas de capex pueden cambiar la relación | N/D (no hay matriz propia); el ROIC=WACC prueba el extremo |
| Ventas/capital años 6–10 | n/a | 1,486; `Input sheet`!B33 | Igual | Disminución por madurez | Salto del retorno incremental de ~40% a 11% en el año 11 (ver sección 9) | N/D |
| ROIC terminal | 33,7% LTM; 18,0% promedio 10 años | 11,04% (promedio de Entertainment); `Input sheet`!B49 = Yes, B50 | Damodaran global, enero 2026 [OBSERVADO en el análisis] | Regla de ventaja durable: converge al promedio de la industria | La ventaja medida es 3x el promedio de industria desde hace tres años | =costo de capital: US$53,10; 13%: US$66,29; 15%: US$70,23 |

## 8. Costo del capital y riesgo

**Reproducción.** Ke = 5,29% + 1,02 × 4,92% = 10,31% frente a 10,33% de la hoja (diferencia de 0,02 pp por redondeo de la beta). Costo de la deuda antes de impuestos 6,18% (calificación A3/A−) y 4,63% después de impuestos con el 25% marginal; peso del patrimonio 94,6% [MODELO]. WACC inicial = 0,946 × 10,33% + 0,054 × 4,63% = 10,02%, igual a la hoja. La tasa de descuento baja de 10,02% (años 1–5) a 8,99% (año 10) de forma lineal en los años 6–10, y los factores compuestos que reproduce el auditor dan un EV de US$266.161 M frente a US$266.763 M de la hoja (−0,23%) [INFERENCIA, sección 10].

**Riesgos y doble conteo.** La prima por regiones (4,92%) pondera los ERP de Damodaran de octubre de 2026 por ventas regionales (UCAN 44%, EMEA 32%, LATAM 12%, APAC 12%); no hay prima específica de compañía; la beta es la del sector global (0,98) reapalancada y no la regresión propia de Netflix. El riesgo del contenido, de la competencia y de la regulación entra en los flujos de las historias (Conservadora, Disrupción), no en la tasa, lo que evita el doble conteo.

**Cómo cambia el riesgo.** La tasa terminal de 8,99% es inferior a la tasa del patrimonio de un negocio con beta 1 (5,29% + 4,92% = 10,21%) porque combina una estructura de capital objetivo con deuda y un costo de deuda de ~4,6% después de impuestos. No pude verificar en las celdas la composición exacta de esa tasa terminal (peso de deuda y beta terminal): **N/D**. El estructural 94,6% patrimonio / 5,4% deuda de hoy no explica ese descenso por sí solo, de modo que la hoja asume una estructura de capital más apalancada a perpetuidad. Esto es una hipótesis del modelo, no un hecho de Netflix (deuda neta/EBITDA 0,35x).

**Seis preguntas (WACC inicial y terminal).**
- (a) WACC inicial 10,02% (años 1–5), terminal 8,99% (año 10 en adelante); Ke 10,33%; `Cost of capital worksheet`!B14, B63.
- (b) Sin serie histórica de WACC en la hoja; N/D. Frente a la tasa libre de riesgo, el prima de Ke sobre Rf es 5,04 pp.
- (c) Mecanismo: flujo en dólares de negocio con exposición global; beta del sector de entretenimiento global.
- (d) Hechos requeridos: Rf cercana a 5,29%; ERP ponderado estable.
- (e) Hechos refutadores: caída de Rf (aumenta el valor por menor descuento pero también baja g terminal en el mismo modelo, g = Rf) o beta propia de Netflix muy distinta de 1,02 (la referencia de EE.UU. de 0,79 da US$64,01 de valor esperado según la hoja frente a US$60,12).
- (f) Impacto: WACC ±1 pp en inicial y terminal → US$81,35 (−1 pp) y US$49,17 (+1 pp); reproducido US$81,19 y US$49,03. **Prueba de tasa alternativa del auditor:** subir sólo la tasa terminal a 9,99% → US$51,89 (−14,9%); a 10,21% (equivalente a beta 1 sin deuda) → US$50,40 (−17,4%) [INFERENCIA con el script independiente; no ejecutada en la hoja].

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| WACC inicial / Ke | N/D | 10,02% / 10,33%; `Cost of capital worksheet`!B14, B63 | Damodaran (beta global, ERP octubre 2026); Rf 5,29% | Beta 0,98 → 1,02; ERP regional 4,92% | Beta bottom-up de EE.UU. 0,79 (referencia) reduciría Ke | ±1 pp: US$81,35 / US$49,17 |
| WACC terminal | N/D | 8,99% (año 10) | Damodaran: converge al costo de capital de largo plazo | Estructura objetivo de deuda y costo de deuda | Supera por 3,7 pp a g = 5,29%; sin beta terminal visible | Terminal 9,99%: US$51,89; 10,21%: US$50,40 |
| Rf y ERP | Rf 10 años, 30-sep-2026 | 5,29% y 4,92% | FRED DGS10; Damodaran ERPOct26 | Fecha común del corte | El Tesoro y la ERP cambian cada mes | N/D (no hay matriz de Rf aislada) |

## 9. Convergencia y valor terminal

**Comprobaciones.** (i) g perpetuo en US$ nominales: 5,29% = Rf, regla de la hoja; (ii) WACC terminal 8,99% > g (diferencial de 3,70 pp); (iii) margen terminal igual al del año 10 (36,35%); (iv) impuesto 25%; (v) reinversión terminal = g / ROIC = 5,29% / 11,04% = 47,9% del NOPAT; (vi) ROIC terminal 11,04% > WACC terminal 8,99% con una ventaja durable declarada (regla de `moat_2026-09-30.json`: ventaja durable → promedio de industria). El valor terminal descontado es US$157.621 M de un valor operativo de US$266.763 M: **59,1%** [MODELO]; el recálculo independiente da 59,2%.

**Continuidad FY10–FY11.** En el año 10 el FCFF es US$23.363 M con reinversión de 13,1% del NOPAT (US$3.508 M sobre US$26.872 M). En el año 11, con NOPAT de US$28.293 M y reinversión de 47,9%, el FCFF cae a ~US$14.741 M, **−36,9%** [INFERENCIA]. El retorno incremental baja de ~40% a 11,04% en un solo año. No es un error de fórmula (la regla de Damodaran lleva el ROIC terminal al promedio de la industria), pero sí una discontinuidad: el valor terminal asume que los US$3.500 M de reinversión del año 10 pasan a US$13.600 M al año siguiente. Es conservadora (mantener ROIC marginal alto durante más años subiría el valor) y es la razón por la que ROIC terminal igual a WACC resta sólo 13%.

**Qué ventaja sobreviviría diez años.** La escala de audiencia y de distribución, el catálogo propio de contenido y la red Open Connect son ventajas identificables; los efectos de red son débiles salvo en publicidad. Prueba de erosión del moat: ROIC terminal igual al costo de capital → US$53,10 (−13,0%); ROIC de 10% → US$57,42 (−5,9%).

**Seis preguntas (crecimiento terminal y ROIC terminal).**
- (a) g 5,29%, ROIC 11,04%, WACC 8,99%; `Input sheet`!B49 y B50, tg en `Valuation output`.
- (b) No hay histórico de g; el crecimiento de ingresos de 2023–2025 fue 12,8% anual; el ROIC LTM es 33,7%.
- (c) Mecanismo: Netflix sigue siendo el mayor agregador de suscripciones de video, con inflación de precios; el retorno marginal cae hacia el del sector.
- (d) Hechos requeridos: g nominal sostenible; ventaja durable sin descontar más de un tercio.
- (e) Hechos refutadores: crecimiento de ingresos que converge en menos de 4% antes del año 10; o ROIC marginal que no se desploma sino que se mantiene sobre 20% (el modelo sería entonces conservador).
- (f) Impacto: g ±1 pp → US$56,97 / US$67,57 (−6,7% / +10,7%); reproducido US$56,83 / US$67,42; ROIC 10%–15%: US$57,42–US$70,23; tasa terminal 9,99%: US$51,89.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| g terminal | n/a | 5,29%; `Valuation output`, tg | Rf 5,29% | Igualar g a Rf es la regla de la hoja | El prompt pide no imponerlo sin evidencia; 5,29% es alto para el PIB nominal de largo plazo [HIPÓTESIS] | 4,29%: US$56,97; 6,29%: US$67,57 |
| ROIC terminal | 33,7% LTM; 18,0% (10 años) | 11,04% | Entertainment, Damodaran enero 2026 | Ventaja durable se disipa al promedio | Retorno incremental 2022–LTM muy superior | 8,99%: US$53,10; 13%: US$66,29 |
| Proporción del terminal | n/a | 59,1% del valor operativo | n/a | n/a | Alta dependencia de supuestos de la perpetuidad | Independiente: 59,2% |

## 10. Validación independiente del valor intrínseco

**Reproducción con un script propio** (no lee la hoja; toma de ella los insumos y la trayectoria de crecimiento de la fila 4 de `Valuation output`) [INFERENCIA, ejecutada]: EV = US$266.161 M frente a US$266.763 M de la hoja (−0,23%); puente EV → equity con caja US$9.128 M, deuda con arrendamientos US$16.636 M y opciones US$4.973 M; valor por acción **US$60,89** frente a **US$61,04** (−0,25%). La diferencia viene del redondeo de los crecimientos anuales que tomé de la fila de la hoja (cuatro decimales) y no de una diferencia de método.

**Puente de la hoja** [MODELO]: PV de los flujos años 1–10 US$109.142 M + PV del terminal US$157.621 M = valor de activos operativos US$266.763 M; + caja US$9.128 M − deuda con arrendamientos US$16.636 M − opciones US$4.973 M = patrimonio US$254.282 M; ÷ 4.165,9 M de acciones = US$61,04 (reproducido: 266.763 + 9.128 − 16.636 − 4.973 = 254.282).

**Horizontes.** El DCF Base de hoy es US$61,04; el DCF capitalizado a FY+3 (valor de hoy × (1 + Ke)^3, riqueza antes de distribuciones) es US$81,98; el ponderado hoy con múltiplos es US$86,11 y a FY+3 US$118,37 [MODELO]. No se mezclan horizontes en este informe: el valor de comparación con el precio es el DCF de hoy.

**Sensibilidad DCF reproducida (US$ por acción, Base):**

| Prueba | Hoja (pestaña «Sensibilidad DCF») | Auditor | Diferencia |
|---|---:|---:|---:|
| Centro | 61,04 | 60,89 | −0,25% |
| WACC +1,0 pp / −1,0 pp | 49,17 / 81,35 | 49,03 / 81,19 | −0,3% / −0,2% |
| g 4,29% / 6,29% | 56,97 / 67,57 | 56,83 / 67,42 | −0,2% |
| ROIC terminal = WACC | 53,10 | 52,96 | −0,3% |
| Crecimiento −2 pp / +2 pp | 54,95 / 67,78 | 54,81 / 67,63 | −0,3% / −0,2% |
| Margen +2 pp | 64,43 | 64,23 | −0,3% |

**DCF inverso.** Con el precio de US$69,58, el informe estima que los ingresos de los años 1–5 deberían crecer 11,4% anual frente a 8,9% de la Base (+2,5 pp). La tabla del Nivel 2 da, con beta 1,02 y margen de 36,4%, un crecimiento de 11,0% (fracción de empresas de este tamaño que lo logra: 19,2%); con margen de 40,4% basta 9,0% (26,5%) y con 32,9% se necesita 13,0% (12,8%). No logré conciliar 11,4% con 11,0% (misma beta, mismo margen y mismo precio) con los documentos examinados: **N/D**, ver H10. Contra la comparación de ecuaciones reales, el precio de US$69,58 está dentro del rango de los cuatro escenarios (US$22,91 a US$75,12) y por encima del esperado de US$60,12 (+15,7%).

**Opciones y dilución.** Valor de cada opción US$40,14 (123,9 M a US$39,21, 4,6 años, volatilidad 33,8%) → US$4.973 M. El valor se calcula con el precio de mercado de US$69,58 como subyacente; con el valor intrínseco de US$61,04 el valor Black-Scholes por opción baja de ~US$40,9 a ~US$33,1 (sin ajuste de dilución) y el valor por acción sube aproximadamente US$0,2 [INFERENCIA]. Es inmaterial y se registra como H13.

**Seis preguntas (supuesto dominante: crecimiento y margen en conjunto).** Resueltas en las secciones 5 y 6; la sensibilidad conjunta se muestra en la sección 13. **Valor que descuenta el precio:** para igualar US$69,58 con la Base se necesitan, por ejemplo, +2 pp de crecimiento anual en los años 1–5 y un margen de 38,35% (US$71,60) o +4 pp con el margen de la Base (US$75,23) [matriz 3].

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| DCF Base hoy | n/a | US$61,04; `Valuation output`!B35 | Precio US$69,58 (+14,0%) | Suma de supuestos de secciones 5–9 | Mercado paga por 11,0%–11,4% de crecimiento | Reproducido US$60,89 |
| Puente EV → equity | Caja 9.128 M; deuda 14.309 M + arrendamientos 2.327 M | −US$7.508 M de caja neta más opciones −US$4.973 M | 10-Q 2T26 | Deuda neta baja (0,35x EBITDA) | La comisión de WBD (US$2.800 M) ya está en caja | Opciones: ±US$0,2 por acción según subyacente |
| Acciones | 4.165,9 M (30-jun-2026) | `Input sheet`!B22 | Carta 3T26: 4.195 M diluidas promedio | Recompras reducen el conteo | Recompras post-corte bajan la cifra, lo que favorece el valor por acción | Una dilución de 5% daría US$58,13 (−5%, según el análisis) |

## 11. Cuatro historias y probabilidades

| Historia | Crecimiento | Margen EBIT | Reinversión/ROIC | WACC/Ke | g y retorno terminal | Valor principal por acción | Probabilidad registrada | Qué la confirma / refuta |
|---|---|---|---|---|---|---:|---:|---|
| Conservadora: la atención se estanca y el contenido absorbe el margen | 9,5% → 4,7% (años 1–5); 4,8% → 5,3% (6–10) | 32,9% | Reinversión US$2.257 M → US$3.044 M; ROIC terminal 11,04% | 10,02% → 8,99% / Ke 10,33% | 5,29% / 11,04% | **US$49,29** | 25% | Confirma: crecimiento < 8% y margen estancado en ~32%; refuta: crecimiento > 10% sostenido |
| **Base**: precio, publicidad y mercados nuevos con margen hacia 36% | 11,1% → 6,8%; 6,5% → 5,3% | 36,4% | Reinversión US$2.916 M → US$3.508 M; ROIC terminal 11,04% | igual | 5,29% / 11,04% | **US$61,04** (principal) | 50% | Confirma: ingresos +10%/+11% con margen ≥ 33%; refuta: margen < 31% o crecimiento < 9% |
| Optimista: la publicidad y el vivo escalan y el margen llega a 40% | 12,7% → 8,8%; 8,1% → 5,3% | 40,4% | Reinversión US$3.557 M → US$3.974 M; ROIC terminal 11,04% | igual | 5,29% / 11,04% | **US$75,12** | 15% | Confirma: publicidad > US$4.500 M y margen ≥ 38%; refuta: guía de publicidad recortada de nuevo |

**Promedio condicionado de las tres historias ordinarias.** Pesos 50%, 25% y 15% sobre 90% (la Disrupción, 10%, se excluye y los pesos se normalizan: 55,6%, 27,8%, 16,7%): 0,556 × 61,04 + 0,278 × 49,29 + 0,167 × 75,12 = **US$60,12** [MODELO; reproducido por el auditor]. El MOS de 35% aplicado a ese esperado da US$39,08; aplicado al valor principal (DCF Base, regla de este prompt) da **US$39,68**. Ver H6.

### ¿Qué pasaría si todo fallara?

**Disrupción (probabilidad vigente 10%): US$22,91 por acción.** Operativamente: la atención migra a plataformas abiertas y a contenido generado por IA, el precio deja de subir, el crecimiento cae de 7,4% (año 1) a 0,3% (años 4–10), el margen retrocede de 31,9% a 22,4% y el crecimiento terminal es 0,25% con ROIC terminal igual al costo de capital (la hoja lo muestra como 0,00%; ver H11). El valor de activos operativos es US$107.918 M frente a US$266.763 M de la Base (−60%). **Esta historia no entra en el promedio de las tres.** Como dato etiquetado, el esperado de las cuatro historias con los pesos registrados (50/25/10/15) es 0,50 × 61,04 + 0,25 × 49,29 + 0,10 × 22,91 + 0,15 × 75,12 = **US$56,40**; la columna «aporte al esperado» del informe de valoración suma esa cifra (30,52 + 12,32 + 2,29 + 11,27) pero su fila total muestra US$60,12, y por eso la verificación `valor_esperado_igual_suma` figura como falsa en el registro (H7). La probabilidad de 10% no se puede contrastar: no hay una base de frecuencia publicada para el evento «deterioro de los fundamentales»; el 10% es un juicio [HIPÓTESIS].

## 12. Valoración por múltiplos: prueba independiente y secundaria

**Reglas.** Los múltiplos son secundarios, se calculan después del DCF y no se calibran para coincidir con él (la hoja lo declara y el auditor no encontró un múltiplo que dependa del DCF). La ancla **C** (múltiplo fundamental sostenible) comparte hipótesis de crecimiento, ROE y costo de capital con el DCF: no es evidencia independiente. Pesos del panel: tipo «Madura» (DCF 40%, múltiplos 60%): EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%, P/V 0%, P/BV 0%. Las cifras de peers (DIS, SPOT, ROKU; se excluye CMCSA) son de yfinance al 30-sep-2026 [OBSERVADO, fuente secundaria].

| Método | A: historia de la etapa (2022–LTM) | B: peers ajustados (×1,10) | C: justificado | Múltiplo elegido Cons / **Base** / Opt | Denominador FY+3 | Valor FY+3 Base (US$) | Descuento al presente (VP 3 años / consolidado hoy, Base) | Peso efectivo |
|---|---:|---:|---:|---|---|---:|---|---:|
| EV/EBITDA | 29,4x | 38,4x | 19,3x | 20,0x / **29,8x** / 30,7x | EBITDA FY+3: N/D en esta auditoría | 155,15 | 115,52 / 112,54 | 20% (33% de los múltiplos) |
| EV/FCFF | 42,4x | 31,3x | 27,9x | 26,4x / **31,5x** / 32,5x | FCFF FY+3: N/D | 112,23 | 83,57 / 78,61 | 10% (17%) |
| P/E | 37,1x | 30,8x | 21,0x | 21,9x / **38,5x** / 40,6x | BPA FY+3 ≈ US$4,16 [INFERENCIA: 160,20 / 38,5] | 160,20 | 119,28 / 116,12 | 20% (33%) |
| P/FCFE | 41,8x | 33,7x | 23,3x | 26,0x / **30,4x** / 31,3x | ≈ US$3,89 por acción [INFERENCIA] | 118,27 | 88,06 / 86,45 | 5% (8%) |
| P/OCF | 39,0x | 33,0x | 24,4x | 24,2x / **29,0x** / 29,8x | ≈ US$3,71 por acción [INFERENCIA] | 107,49 | 80,03 / 75,65 | 5% (8%) |
| P/V | N/D (ancla inicial pendiente de justificación) | N/D | N/D | 5,7x / **7,5x** / 9,0x | Ventas por acción FY+3 ≈ US$14,99 [INFERENCIA: 112,41 / 7,5] | 112,41 | 83,70 / 84,57 | 0% |
| P/BV | N/D («provisional: conciliar equity por historia») | N/D | N/D | 9,3x / **12,6x** / 15,0x | Patrimonio por acción FY+3 ≈ US$18,05 [INFERENCIA: 227,40 / 12,6] | 227,40 | 169,32 / 143,15 | 0% |

**Resultado consolidado.** Múltiplos solos al presente: Conservador US$65,45, Base US$102,83, Optimista US$114,01. DCF + múltiplos al presente: US$58,99 / US$86,11 / US$98,45. El Base de múltiplos es **+68% sobre el DCF Base**; la propia valoración lo marca y explica: sin cierres anuales a ±2 pp de crecimiento, la Base toma el cierre de 2023 (crecimiento de 6,7%), cuyo precio descontaba una reaceleración a ~15% con tasa libre de riesgo cercana a 4%, frente a 5,29% hoy.

**Justificación económica por método y críticas.**
- *EV/EBITDA (29,8x).* Es 2x el 15,7x que implica el DCF Base y 1,5x el ancla C (19,3x). Peers: DIS 10,9x, SPOT 34,9x, ROKU 35,4x; la mediana de tres incluye dos pares de crecimiento mucho más alto. Conserva 20% del peso total del panel.
- *EV/FCFF (31,5x)* y *P/FCFE (30,4x)*, *P/OCF (29,0x).* Las anclas históricas parten de 2022, porque el flujo libre de 2016–2021 es negativo o cercano a cero; los pares tienen n=3. P/OCF no es FCF: el flujo operativo LTM incluye la comisión de WBD neta de impuestos (~US$2.200 M) y los otros métodos de flujo también la arrastran.
- *P/E (38,5x).* El múltiplo Base **está fuera de su propio rango de anclas** (21,0x–37,1x) y es 1,76x el P/E LTM de 21,9x (~25x ajustado por WBD). El texto del informe describe la fórmula Base = 0,65 × promedio(A, B) + 0,35 × C, que daría ~29,4x, y no la regla por ciclo que realmente se aplicó (H4). El Conservador (21,9x) coincide con el múltiplo actual (la regla exige que el Conservador no lo supere) y el Optimista (40,6x) está +85% sobre el actual, lo que la regla exige justificar con evidencia; la justificación documentada es sólo el cierre de 2023.
- *P/V y P/BV.* Sin anclas justificadas; con peso 0 no afectan el resultado. Para P/BV el patrimonio por acción pasa de ~US$7,24 hoy (30.152 / 4.164) a ~US$18,05 en FY+3, un aumento de 2,5x que sólo se explicaría si se retuviera toda la utilidad: el modelo no resta las recompras (~US$9.900 M al año) en la proyección del patrimonio (H8). Con recompras equivalentes, el patrimonio por acción de FY+3 sería del orden de US$11–12 y el valor de P/BV a 12,6x bajaría proporcionalmente [INFERENCIA, no ejecutada].
- *Denominadores no positivos:* no hay en los siete métodos; los múltiplos históricos negativos de 2016–2021 se excluyen correctamente. Doble conteo de dividendos: Netflix no paga dividendo, no aplica. EV/FCFF ≠ EV/FCF genérico: la hoja usa FCFF.

**Independencia de las anclas.** B (peers) es independiente de las hipótesis de Netflix pero con n=3 y heterogéneo (Disney con parques, Spotify con música, Roku con plataforma). A (historia) es de un solo emisor. C comparte hipótesis con el DCF. Ninguna se calibró contra el DCF ni contra el consenso de terceros (el registro de fuentes sustituyó una fuente de consenso por otra sin cambio de cifras).

## 13. Sensibilidades económicas y escenarios alternativos

### 13.1 DCF Base × WACC y g terminal (US$ por acción; simulación ejecutada en la hoja, fecha 21-oct-2026)

| WACC (± pp) \ g terminal | 4,29% | 4,79% | 5,29% | 5,79% | 6,29% |
|---|---:|---:|---:|---:|---:|
| −1,0 | 71,50 | 75,72 | 81,35 | 89,35 | 101,82 |
| −0,5 | 63,39 | 66,15 | 69,64 | 74,29 | 80,88 |
| 0,0 | 56,97 | 58,81 | **61,04** | 63,85 | 67,57 |
| +0,5 | 51,75 | 52,98 | 54,43 | 56,16 | 58,33 |
| +1,0 | 47,42 | 48,24 | 49,17 | 50,24 | 51,51 |

*Eje: WACC inicial y terminal ± puntos porcentuales; centro = DCF Base vigente. Impacto direccional extra del auditor (script propio): sólo tasa terminal a 9,99% → US$51,89.*

### 13.2 ROIC terminal × g terminal

| ROIC terminal \ g | 4,29% | 4,79% | 5,29% | 5,79% | 6,29% |
|---|---:|---:|---:|---:|---:|
| 8,99% (= costo de capital) | 52,09 | 52,59 | 53,10 | 53,62 | 54,14 |
| 10,00% | 54,75 | 55,97 | 57,42 | 59,18 | 61,44 |
| 11,04% (hoja) | 56,97 | 58,81 | **61,04** | 63,85 | 67,57 |
| 13,00% | 60,20 | 62,91 | 66,29 | 70,62 | 76,45 |
| 15,00% | 62,62 | 66,00 | 70,23 | 75,70 | 83,12 |

### 13.3 Crecimiento años 1–5 × margen EBIT objetivo

| Crecimiento \ margen | 32,35% | 34,35% | 36,35% | 38,35% | 40,35% |
|---|---:|---:|---:|---:|---:|
| −4 pp | 44,11 | 46,78 | 49,45 | 52,12 | 54,79 |
| −2 pp | 48,92 | 51,94 | 54,95 | 57,96 | 60,97 |
| 0 pp | 54,25 | 57,65 | **61,04** | 64,43 | 67,83 |
| +2 pp | 60,14 | 63,96 | 67,78 | 71,60 | 75,41 |
| +4 pp | 66,66 | 70,94 | 75,23 | 79,52 | 83,81 |

**Lectura.** En 19 de 25 celdas de la matriz 13.3 el valor está por debajo del precio de US$69,58; el valor lo supera sólo con +2 pp de crecimiento y margen de ~38% o más, o con +4 pp de crecimiento y margen de ~34% o más. El DCF inverso (sección 10) es consistente con esto.

### 13.4 Múltiplos: primera familia, valor por acción (múltiplo real × denominador FY+3 real, ±20%)

Las matrices de la hoja están pobladas para los siete métodos con la rejilla 0,8–1,2 sobre el múltiplo y sobre el fundamental, valor presente de FY+3 por acción, Base [MODELO, Nivel 2]. Valores centrales (múltiplo y fundamental en 1,0): EV/EBITDA US$115,52; EV/FCFF US$83,57; P/E US$119,28; P/FCFE US$88,06; P/OCF US$80,03; P/V US$83,70; P/BV US$169,32. Extremos de cada rejilla: EV/EBITDA US$73,15 a US$167,30; EV/FCFF US$52,70 a US$121,29; P/E US$76,34 a US$171,76; P/FCFE US$56,36 a US$126,81; P/OCF US$51,22 a US$115,25; P/V US$53,57 a US$120,52; P/BV US$108,37 a US$243,82. Fecha: 21-oct-2026.

### 13.5 Múltiplos: segunda familia, múltiplo justificado (ejes propios del método)

**N/D.** La pestaña «Relativa v2 · Sensibilidad» no contiene esta familia poblada (el Nivel 2 lo declara). Implicación: no es posible mostrar cuánto cambia el múltiplo justificado ante variaciones de crecimiento, ROE y costo de capital propios de cada método. Evidencia necesaria: poblar la pestaña con la formulación del contrato `contrato-historias-multiplos-20261017.md`. Efecto sobre el dictamen: **Auditoría condicionada**.

*Diferencia entre simulado y direccional:* las matrices 13.1–13.4 son simulaciones realmente ejecutadas en la hoja; la prueba de tasa terminal del auditor y la interpolación de la sección 5 son direccionales con script propio.

## 14. Coherencia de hojas, cálculos y presentación

Artefactos examinados: hoja (`Input sheet`, estados, LTM, `Valuation output`, `Escenarios e historias`, `Cost of capital worksheet`, `Option value`, múltiplos, «Sensibilidad DCF»), JSON de valoración, informe de valoración, análisis (Nivel 1 y Nivel 2) y los controles de consistencia, integridad y estados completos que ejecuta el flujo (al cierre: consistencia M1–M3/H1–H3/I1 en OK; la integridad de hojas dio 0 hallazgos para NFLX en la ejecución anterior y la última falló por una hoja ajena, NKE, con error 404: **no reejecutada con éxito**). No se verificó el visor de la app más allá de que el registro está en la rama principal.

- **Fórmulas y overrides.** Los pasos de construcción dejaron sobreescritos a mano, con nota, entradas de la plantilla («LISTO» gates) y un parche del cálculo de g terminal para evitar una referencia circular entre `Input sheet`!J5 y `Valuation output`!M4; el parche es correcto pero es una divergencia con la plantilla maestra. La fórmula del cambio de caja (fila 40 de `Cash Flow`) se escribe a mano.
- **Etiquetas y unidades.** La tabla de Nivel 2 «Opciones y dilución» mostraba «Opciones en circulación (M): N/D» mientras la hoja trae 123,9 M (H14). La Disrupción muestra «ROIC terminal 0,00%» cuando la regla es «igual al costo de capital».
- **Precios mezclados.** Sólo hay un precio (US$69,58, 30-sep-2026) en la hoja y en el registro; el 3T26 es posterior.
- **Supuestos desactualizados.** Guía de publicidad 2026 de US$3.000 M (en el modelo, vía análisis) frente a ~US$2.700 M del 20-oct; guía de FCF 2026 de ~US$12.500 M frente a ~US$12.000 M; margen de 2026 de 31,5% reiterado.
- **MOS y promedios.** MOS sobre el esperado (US$39,08) en el resumen y sobre el principal (US$39,68) en la tabla; promedio de tres historias = US$60,12 correcto; Disrupción aislada; la suma de aportes por historia no cuadra con el total (H6, H7).
- **Panel de métodos.** Los pesos del tipo «Madura» (DCF 40%/múltiplos 60%) producen un «ponderado hoy» de US$86,11, +41% sobre el DCF principal; el panel y el valor intrínseco principal pueden confundir al lector (H5).
- **Cálculo del ciclo de vida.** La clasificación «Madura» para una empresa cuyo crecimiento Base es 11,1% y cuyo margen se expande no está argumentada en los documentos examinados (H15).

## 15. Hallazgos priorizados y propuestas de corrección

| ID | Severidad | Tipo | Evidencia | Impacto | Mantener/ajustar/investigar | Propuesta y alternativa | Requiere aprobación | Estado |
|---|---|---|---|---|---|---|---|---|
| H1 | Alto | Supuesto | WACC terminal 8,99% vs 10,21% (Rf + ERP, beta 1); composición no visible en celdas (N/D) | Terminal 9,99% → US$51,89 (−14,9%); 10,21% → US$50,40 (−17,4%) | Investigar | Documentar peso de deuda, beta terminal y costo de deuda terminal; alternativa: mostrar en el informe el DCF con terminal 9,99% como lectura conservadora | Sí (nuevo ciclo de Valoración) | Abierto |
| H2 | Alto | Supuesto | Terminal: salto del ROIC marginal de ~40% (año 10) a 11,04% (año 11); FCFF del año 11 −36,9% frente al año 10 | ROIC terminal 13%: US$66,29 (+8,6%); 15%: US$70,23 (+15,1%); =WACC: US$53,10 (−13,0%) | Investigar | Declarar la discontinuidad en la tesis y evaluar una convergencia gradual de ventas/capital en los años 8–10; alternativa: mantener (es la regla de Damodaran y conservadora) | Sí | Abierto |
| H3 | Medio | Supuesto | g terminal = Rf = 5,29% | g = 4,29%: US$56,97 (−6,7%) | Investigar | Justificar con inflación y crecimiento real sostenible; alternativa: g = 4,5% con el mismo ROIC | Sí | Abierto |
| H4 | Alto | Dato/presentación | P/E Base 38,5x fuera de sus anclas (21,0x–37,1x); descripción de fórmula (65%/35%) no coincide con la regla por ciclo; Base +76% sobre el P/E LTM y +68% de los múltiplos sobre el DCF | El ponderado hoy de US$86,11 (+41% sobre el DCF) depende de este múltiplo | Investigar | Documentar la regla por ciclo aplicada y alinear el texto; evaluar el límite de anclas; alternativa: reducir el peso de múltiplos mientras la brecha supere ±25% | Sí | Abierto |
| H5 | Medio | Presentación | Panel «Madura» 40/60 vs valor principal DCF Base; ponderado hoy US$86,11 | Lectura engañosa del valor | Ajustar | Presentar el ponderado como lectura secundaria y etiquetarlo en la app | No (presentación) | Abierto |
| H6 | Medio | Dato | MOS 35% da US$39,08 (sobre esperado) y US$39,68 (sobre DCF Base) en el mismo informe | US$0,60 por acción | Ajustar | Declarar una base única; este prompt exige el principal (DCF Base) | Sí | Abierto |
| H7 | Medio | Fórmula | Aportes por historia suman US$56,40; la fila total dice US$60,12; `valor_esperado_igual_suma` = falso en el registro | Etiquetado | Ajustar | Mostrar el esperado de tres (US$60,12) y el de cuatro (US$56,40) por separado | No | Abierto |
| H8 | Medio | Supuesto | P/BV: patrimonio por acción FY+3 ≈ US$18,05 vs ~US$7,24 hoy; no resta recompras; anclas provisionales | Peso 0 hoy; sobrestimaría si se activara | Investigar | Conciliar equity por historia con recompras, SBC y OCI antes de dar peso | Sí | Abierto |
| H9 | Medio | Dato | Segunda familia de matrices (múltiplo justificado) no poblada | Auditoría condicionada | Investigar | Poblar «Relativa v2 · Sensibilidad» con el contrato 17-oct-2026 | No | Abierto |
| H10 | Bajo | Dato | DCF inverso: 11,4% (informe) frente a 11,0% (Nivel 2) con el mismo precio, beta y margen | Presentación | Investigar | Unificar la definición (tasa uniforme vs trayectoria) | No | Abierto |
| H11 | Medio | Supuesto | Avisos del flujo: capital nuevo rinde 31% en Disrupción (ROIC terminal = WACC 9%) y 55% en Optimista (ROIC terminal 11%): más del doble | Disrupción y Optimista con ventas/capital posiblemente altos | Investigar | Revisar ventas/capital de las historias C y D y mostrar «= costo de capital» en vez de 0,00% | Sí | Abierto |
| H12 | Alto (histórico) | Fórmula/proceso | Paso de corrección no idempotente multiplicó acciones ×100; detectado antes de publicar | Habría reducido el valor ~100x | Mantener (corregido) | Añadir prueba de idempotencia al paso | No | Cerrado, verificar |
| H13 | Bajo | Fórmula | Opciones valoradas con el precio de mercado (US$69,58) en vez del valor intrínseco | ~+US$0,2 por acción | Mantener | Alternativa: iterar con el valor intrínseco como lo hace la plantilla de Damodaran | No | Abierto |
| H14 | Bajo | Presentación | Nivel 2 con «Opciones en circulación: N/D» pese a 123,9 M en la hoja | Etiqueta | Ajustar | Leer el dato de la hoja en el generador | No | Abierto |
| H15 | Medio | Supuesto | Tipo «Madura» (60% múltiplos) no argumentado | Cambia el ponderado hoy | Investigar | Documentar por qué no «Crecimiento»/«Maduración» según `ciclo_de_vida` | Sí | Abierto |
| H16 | Medio | Dato | Hechos del 3T26 (20-oct): guía de publicidad ~US$2.700 M (antes ~US$3.000 M), FCF 2026 ~US$12.000 M (antes ~US$12.500 M), margen 4T26 26,0% | No incorporado; el año 1 sigue alcanzable pero con menos colchón | Investigar | Incorporar en el próximo ciclo de valoración y revisar el supuesto de publicidad | Sí | Abierto |
| H17 | Bajo | Dato | Fuente de consenso secundaria (cobertura de mercado) para movimientos de precio y expectativas; no se contrastó con fuente primaria | Contexto, no cifras del modelo | Mantener | Marcar [NO VERIFICADO] las citas de consenso | No | Abierto |

*Separación:* H4, H6, H7, H14 y H10 son errores de dato o de presentación; H1, H2, H3, H8, H11, H15 son hipótesis discutibles; H12 es un error de proceso ya corregido. Las alternativas con efecto numérico (H1 y H3) son direccionales del auditor y no se aplicaron a la hoja.

## 16. Catalizadores, señales de refutación y seguimiento

Los umbrales son criterios del auditor [HIPÓTESIS], no guías oficiales, salvo cita.

| Métrica | Nivel observado con fecha | Señal favorable | Señal adversa | Fuente | Frecuencia |
|---|---|---|---|---|---|
| Crecimiento de ingresos | 3T26 +11,8% (20-oct-2026); 4T26 guiado +11,5% | ≥ 11% en 1T27 y 2T27 | < 9% en el primer semestre de 2027 | Carta a accionistas | Trimestral |
| Margen operativo | 3T26 34,6%; 4T26 guiado 26,0%; guía 2026 31,5% | ≥ 31,5% en 2026 y ≥ 33% guiado para 2027 | < 31% en 2027 | Carta a accionistas | Trimestral |
| Ingresos por publicidad | Guía 2026 ~US$2.700 M (bajó de ~US$3.000 M) | Guía 2027 ≥ US$3.500 M | Nuevo recorte de guía | Carta y 10-K | Trimestral/anual |
| Conversión de caja | FCF LTM US$11.152 M; guía 2026 ~US$12.000 M | FCF/utilidad operativa ≥ 75% | FCF por debajo de la guía | 10-Q/10-K | Trimestral |
| ROIC incremental / relación contenido-ingresos | ROIC LTM 33,7%; amortización de contenido 52% de los ingresos en 2025 | Costo de ingresos < 50% de los ingresos | > 52% por dos años | 10-K | Anual |
| Uso por miembro | Horas vistas +2% en el primer semestre de 2026 | ≥ 3% | Caída | Informe de compromiso (What We Watched) | Semestral |
| Crecimiento de UCAN | 2T26 +10% | ≥ 10% | < 8% | Carta a accionistas | Trimestral |

Próximos reportes: la fecha del resultado del 4T26 y del 10-K 2026 no está confirmada en los documentos examinados: **N/D**.

## 17. Dictamen económico y resumen para escuchar

**Dictamen: Plausible con reservas** (no es «Sostenible» por las razones de H1, H2, H4 y la segunda familia de matrices no poblada).

- **Consistencia matemática: conforme.** El DCF Base se reproduce con un script independiente: US$60,89 frente a US$61,04 (−0,25%); las sensibilidades quedan dentro de 0,3%. Las diferencias de presentación (H6, H7) no cambian el valor.
- **Trazabilidad documental: con reservas.** Las cifras de estados, tasas y acciones se concilian con fuentes primarias; los peers y el consenso son fuentes secundarias, y el cargo de Brasil, la composición del WACC terminal y los denominadores FY+3 de los métodos no se verificaron celda por celda.
- **Razonabilidad económica: plausible con reservas.** El año 1 está anclado a la guía de 2026 y es consistente con los resultados del 3T26; el margen de 36,4% supera todo registro anual, y el valor terminal (59,1%) descansa en g = Rf y en un descenso brusco del retorno marginal.
- **Supuesto más frágil:** el margen objetivo de 36,35% sostenido durante diez años con un uso por miembro casi plano. **Más defendible:** el año 1 (ingresos +11,1%, margen 31,85%), alineado con la guía de 2026. **Motor principal del precio:** crecimiento de los años 1–5 y margen, con un tercer factor en el terminal.
- **Precio frente al valor:** US$69,58 es 14,0% sobre el DCF Base (US$61,04) y 15,7% sobre el esperado (US$60,12): no hay margen de seguridad frente al principal; la compra con MOS de 35% estaría cerca de US$39,68.
- **Decisión analítica sugerida:** conservar la hipótesis Base, revisar la tasa terminal, el salto del ROIC y los múltiplos (H1, H2, H4) y volver a valorar con los hechos del 3T26 (H16).
- **Auditoría condicionada:** por la segunda familia de matrices (N/D), la independencia limitada, los denominadores FY+3 no re-verificados y la falta de precio de hoy.

**Resumen oral (≈120 palabras).** Netflix vale hoy, según el modelo, unos sesenta y un dólares por acción, y el precio de cierre de septiembre fue sesenta y nueve con cincuenta y ocho: catorce por ciento por encima. Recalculamos el valor por otro camino y llegamos a sesenta con ochenta y nueve, así que las matemáticas cuadran. La historia que sostiene el valor es que los ingresos crezcan once por ciento este año y el margen suba hasta treinta y seis por ciento; ningún año anterior pasó de treinta. Las reservas son la tasa de descuento de largo plazo, la caída brusca del retorno después del año diez y unos múltiplos muy generosos. Dictamen: plausible con reservas. No se modificó la valoración.

## 18. Fuentes primarias, limitaciones y registro de versión

**Fuentes.**

| Fuente | URL | Publicación / período | Consultada | Respalda | Límites |
|---|---|---|---|---|---|
| Netflix, 10-K 2025 | https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm | 23-ene-2026; ejercicio 2025 | 21-oct-2026 | Estados anuales, segmentos, contenido, compromisos | No se releyó íntegro; cifras vía la hoja y el análisis |
| Netflix, 10-Q 2T26 | https://www.sec.gov/Archives/edgar/data/1065280/000106528026000212/nflx-20260630.htm | 30-jun-2026 | 21-oct-2026 | Balance, acciones, opciones, deuda, LTM | Idem |
| Netflix, carta a accionistas 2T26 | https://www.sec.gov/Archives/edgar/data/1065280/000106528026000211/ex991_q226.htm | 16-jul-2026 | 21-oct-2026 | Guía de 2026, regiones, 2T26 | La guía es del emisor, no un hecho realizado |
| Netflix, carta a accionistas 3T26 (hecho posterior) | https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm | 20-oct-2026; 3T26 | 21-oct-2026 | Ingresos, margen, FCF y publicidad 2026, acciones diluidas | Posterior al corte; no incorporada |
| Damodaran, prima implícita (ERP) | https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx | oct-2026 | N/D en esta auditoría (cifra tomada de la hoja) | ERP por región | No re-descargada |
| Damodaran, betas por industria | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html | enero 2026 | idem | Beta 0,98, ROIC y márgenes de Entertainment | idem |
| Yahoo Finance (yfinance) | https://finance.yahoo.com/quote/DIS/ (y SPOT, ROKU) | 30-sep-2026 | 21-oct-2026 | Múltiplos de peers, precio del 30-sep | Fuente secundaria; no reconciliada con estados de cada par |
| Serie DGS10 (Tesoro EE.UU.) | `reference/corte_vigente.json` del repositorio | 30-sep-2026 | 21-oct-2026 | Rf 5,29% | Archivo local, no consultado de nuevo |

**Lo no verificado y pruebas no ejecutadas.** Composición de la tasa terminal (peso de deuda, beta terminal): N/D. Cargo de Brasil (US$619 M) contra la nota del 10-Q: [NO VERIFICADO] por esta auditoría. Denominadores FY+3 de EV/EBITDA y EV/FCFF: N/D. Segunda familia de matrices: N/D. Precio de hoy: N/D. Pruebas direccionales no ejecutadas en la hoja: tasa terminal alternativa, tasa de impuesto +2 pp, año 1 en 10,5%, patrimonio de P/BV con recompras. Cotizaciones y expectativas de terceros mencionadas en el análisis: [NO VERIFICADO] contra fuente primaria.

**Registro de versión.**
- `prompt_version: auditoria-economica-jmr-v1.0` (el archivo del prompt lleva la etiqueta v1.1 del 20-oct-2026; el campo de versión de salida es el exigido por la plantilla).
- Versión de la auditoría: 1 · fecha de corte de la auditoría: 21-oct-2026 · hoja auditada: `1Qx8jFSxX5LzkKzhWsPgHfeKy9c33eNygVtN4_O-Ze3E` · JSON auditado: `valoraciones/NFLX-1792548021734.json` (valor esperado US$60,12, DCF Base US$61,04) · commit auditado de `Modelo-JMR-datos` y `JMR-valuation`: se registra al publicar.
- Ruta de publicación prevista: `Modelo-JMR-datos/auditorias/narrativas/NFLX.md`; **estado de publicación: pendiente de verificar la escritura y el acceso en la app; no declarado publicado en este texto.**
- Historial: esta es la primera auditoría de NFLX; no hay versiones previas. Las versiones anteriores de la valoración de NFLX (15-oct-2026) están archivadas en `respaldos/NFLX_valoracion_2026-10-15/` y no se usaron.

**No se modificó la valoración.**
