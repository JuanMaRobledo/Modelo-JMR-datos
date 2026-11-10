---
schema: "jmr-auditoria-economica-v1.2"
prompt_version: "auditoria-economica-jmr-v1.2"
ticker: "NFLX"
company: "Netflix, Inc."
revision_id: "NFLX-2026-10-25"
audit_date: "2026-10-25"
valuation_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1ZPNMHxc7m3Iv60mdGspgi6-cc2zwf5kZ4ocsuANQUNM/edit"
results_snapshot_sha256: "6afa5b6aba533dcbd28143ba547eb3c98de1b541d5695a9a0e6351a2a06e58d5"
controls_file: "reference/revisiones/NFLX-2026-10-25/auditoria_controles.json"
dictamen: "VERIFICADO con salvedades no bloqueantes"
language: "es"
---

# Auditoría económica narrativa — Netflix, Inc. (NFLX)

> **revision_id `NFLX-2026-10-25`.** Esta auditoría examina la misma hoja, la misma foto de resultados (sha256 `6afa5b6a…58d5`), la valoración `data/NFLX_Valoracion_Modelo_JMR_2026-10-25.md` y el análisis `data/NFLX_Research_Fundamental_Modelo_JMR_2026-10-25.md` de esta revisión. Verifica, contradice y dictamina; **no modificó la valoración**. La única corrección ejecutada en la copia (AUD-01, una fórmula de la plantilla) la hizo el proceso de valoración después de la primera ronda de esta auditoría, con respaldo. La segunda ronda la verificó. No es una auditoría contable.

Etiquetas: **[OBSERVADO]** dato de fuente primaria comprobado; **[MODELO]** valor o fórmula de la hoja; **[INFERENCIA]** deducción del auditor; **[HIPÓTESIS]** supuesto sin prueba; **[NO VERIFICADO]** no comprobado en esta auditoría.

## 1. Ficha de auditoría y alcance

| Campo | Valor |
|---|---|
| Razón social, ticker y mercado | Netflix, Inc. · NFLX · Nasdaq Global Select · acción ordinaria única · CIK 0001065280 |
| Sector | Entertainment (Damodaran, tablas global y de EE. UU., enero de 2026) |
| Moneda y escala | USD; millones salvo valores por acción |
| Método intrínseco principal | DCF FCFF de diez años con perpetuidad (plantilla IA, 'Valuation output'), historia Base |
| Fecha de valoración / de auditoría | 30-sep-2026 (corte común de la cartera) / 25-oct-2026 |
| Corte de estados | 30-sep-2026: 10-Q del 3T26 presentado el 21-oct-2026; LTM = FY2025 + 9M2026 − 9M2025 |
| Precio del análisis | US$69,58, cierre NASDAQ del 30-sep-2026 [OBSERVADO en `Input sheet`!B23 y D1]. El precio de hoy no se usó: el corte de mercado es común a la cartera |
| Hoja examinada | [Copia IA del 25-oct-2026](https://docs.google.com/spreadsheets/d/1ZPNMHxc7m3Iv60mdGspgi6-cc2zwf5kZ4ocsuANQUNM/edit), copiada de la plantilla IA oficial `1e-lbQmCkObfq74YLpWnMmIidmcdsJQ-6uN4oiHnNTEQ` (no modificada) |
| Foto de resultados | `reference/revisiones/NFLX-2026-10-25/resultados_hoja.json`, capturada el 25-oct-2026 a las 14:51 UTC tras la corrección AUD-01 |
| Documentos examinados | Valoración v5, research v5 (18 secciones), Nivel 2, snapshot SEC conciliado, decisiones de materialidad, auditoría de derivaciones, entradas del analista con respaldos, anclas y ciclo de múltiplos, DCF inverso, sensibilidades |
| Fuera de alcance | Proxy de 2026 (incentivos de la alta dirección); app y visor (no publicados); la plantilla oficial |
| Estado de verificación | **Conforme con salvedades no bloqueantes** |

## 2. Resumen ejecutivo y relato económico central

Netflix cobra una suscripción mensual, y cada vez más publicidad, por un catálogo que produce y licencia a escala global [OBSERVADO]. En los doce meses a septiembre de 2026 ingresó US$49.735 millones con un margen operativo GAAP de 31,3%, frente a 17,8% en 2022. El motor del cambio fue que la amortización de contenido creció mucho menos que los ingresos tras el cobro por cuentas compartidas, el plan con anuncios y las alzas de precio [OBSERVADO, 10-K 2025 y 10-Q del 3T26]. Lo que está cambiando ahora es la mezcla del crecimiento. El tiempo de visualización crece ~2% al año, así que el ingreso depende del precio por miembro, de la publicidad y de los mercados fuera de Norteamérica. La meta de publicidad de 2026 ya se rebajó de ~US$3.000 a ~US$2.700 millones [OBSERVADO, carta del 3T26].

**Tesis Base favorable [MODELO].** Ingresos +12% el año 1 y 9,99% compuesto en cinco años, margen GAAP hacia 36% (37,1% ajustado por I+D) y ventas/capital de 1,3 y luego 0,9. ROIC terminal de 20,58% por decisión documentada del usuario. Resultado: US$70,85 por acción.

**Interpretación neutral [INFERENCIA].** El precio de US$69,58 ya descuenta casi exactamente esa historia: el DCF inverso exige 9,63% de crecimiento compuesto.

**Contratesis adversa [INFERENCIA].** Si el uso no crece, las alzas de precio elevan la rotación y el contenido en vivo encarece la parrilla; el margen se estanca en ~32% y el crecimiento cae a ~7% (Conservadora, US$53,22).

El supuesto que domina el valor es el **retorno excedente perpetuo**. El terminal pesa 63,8% del valor operativo, y llevar el ROIC terminal al costo de capital resta 20,8%. La contradicción que la empresa debe resolver es mantener crecimiento de dos dígitos con un uso por miembro plano. La historia no se derivó del precio: el DCF inverso se calculó después y solo como contraste.

## 3. Trazabilidad, integridad y jerarquía de evidencia

| Dato | Valor | Período/perímetro | Tipo | Documento/URL/fecha | Hoja/celda | Verificación |
|---|---:|---|---|---|---|---|
| Ingresos | 49.734,63 | LTM oct-25 a sep-26 | [OBSERVADO] | 10-K 2025, 10-Q 3T26 y 3T25 (SEC, consultados el 25-oct-2026) | Input!B12 | Recalculado: 45.183,04 + 37.683,87 − 33.132,27; dif. 0,00 |
| EBIT | 15.564,87 | LTM | [OBSERVADO] | Ídem | Input!B13 | Recalculado: 13.326,60 + 12.608,21 − 10.369,94; dif. 0,00 |
| Gasto por intereses | 856,86 | LTM | [OBSERVADO] | Ídem | Input!B14 | Dif. 0,00 |
| Tasa efectiva | 16,57% | LTM | [OBSERVADO]/[MODELO] | Impuesto 2.933,7 / UAI 17.700,3 (nota de Input!B91) | Input!B24 | Incluye la comisión de WBD gravada; ver AUD-02 |
| Patrimonio | 29.286,25 | 30-sep-2026 | [OBSERVADO] | 10-Q 3T26 | Input!B15 | Dif. 0,00 |
| Deuda (notas + arrendamientos) | 17.384,63 | 30-sep-2026 | [OBSERVADO] | Notas 2.474,80 + 12.657,60; arrendamientos 2.252,24 (10-Q 3T26) | Input!B16 | Dif. 0,00; B18 = No (sin segunda capitalización) |
| Caja e inversiones | 8.222,95 | 30-sep-2026 | [OBSERVADO] | 10-Q 3T26 | Input!B19 | Dif. 0,00 |
| Acciones en circulación | 4.106,33 M | 30-sep-2026 | [OBSERVADO] | Portada del 10-Q 3T26 | Input!B22 | Dif. 0,00 |
| Opciones | 120,175 M a US$41,24 | 30-sep-2026 | [OBSERVADO] | XBRL del 10-Q 3T26: `OptionsOutstandingNumber` = 120.175.117 y precio medio US$41,24, consultado el 25-oct-2026 | Input!B39:B40 | Conforme |
| Vida y volatilidad de las opciones | 4,04 años; 33,8% | 30-sep-2026 | [MODELO] | Nota de compensación del 10-Q (vida remanente) y volatilidad implícita | Input!B41:B42 | Vida [NO VERIFICADO] contra la nota en esta auditoría; volatilidad comparable con los supuestos de la empresa (40-50% en 2022-2023) |
| Capex | 932,88 | LTM | [OBSERVADO] | Snapshot SEC | Estados | Conforme |
| Tecnología y desarrollo | 3.890,81 | LTM | [OBSERVADO] | Etiqueta propia `nflx:TechnologyandDevelopmentExpense` | R&D converter | Residuo de la cuenta de resultados 0 |
| Precio | US$69,58 | 30-sep-2026 | [OBSERVADO] | Yahoo Finance auto_adjust=False | Input!B23 | Conforme con el corte común |
| Tasa libre | 5,29% | 30-sep-2026 | [OBSERVADO] | FRED DGS10 | Input!B35 | Conforme |
| ERP madura y regiones | 3,70%; ponderada 4,93% | Corte de octubre de 2026 / tabla de enero de 2026 | [MODELO] | Damodaran | CoC G21:K33 | Recalculada: 4,9266% |
| Beta desapalancada | 0,9821 | Ene-2026 | [MODELO] | Damodaran, Entertainment global | CoC B24 | Conforme |
| Pares | DIS, SPOT, ROKU, CMCSA, GOOGL | 30-sep-2026 | [OBSERVADO] | Yahoo Finance | anclas.json | Solo comprobación |

Integridad de la extracción [OBSERVADO en los archivos de la revisión]:
- 28/28 identidades contables.
- LTM independiente PASS.
- Cobertura de once ejercicios más el LTM PASS.
- 20/20 derivaciones verificadas contra la instancia XBRL citada.
- 46 contextos materiales adjudicados, 0 sin revisar.

En esta revisión se corrigieron cuatro errores de mapeo que cambiaban datos:
- Contenido tratado como intangible.
- Pérdidas fiscales mezcladas con créditos.
- Cobros por inversiones incompletos.
- Acciones sin ajustar por el desdoblamiento.

La importación de las 785 celdas está postverificada una a una. No se usaron ceros como sustituto de datos ausentes. Los vacíos se adjudicaron como «no aplica» con URL por período o como «omisión inmaterial» cuantificada.

## 4. Historia financiera: diez años y punto de partida

| Métrica | Último (LTM) | 2025 | Prom. 3 años | Prom. 5 años | Prom. 10 años | Rango 2016-2025 |
|---|---:|---:|---:|---:|---:|---|
| Crecimiento de ingresos | +13,7% (9M26) | 15,85% | 12,72% | 12,69% | 21,28% | 6,46% (2022) – 35,08% (2018) |
| Margen operativo GAAP | 31,30% | 29,49% | 25,61% | 23,10% | 16,84% | 4,30% – 29,49% |
| ROIC después de impuestos (con arrendamientos) | 33,77% | 33,31% | 26,90% | 23,07% | 20,91% (7 obs.) | 12,47% – 33,31% (2019-2025) |
| ROE | 50,42% (con la comisión de WBD) | 41,26% | 34,24% | 31,33% | 25,19% | 6,97% – 41,26% |
| Ventas/capital | 1,29 | 1,31 | 1,20 | 1,13 | 1,13 (7 obs.) | 1,00 – 1,31 (2019-2025) |
| Margen de flujo libre | 22,87% | 20,94% | 19,74% | 12,78% | 0,33% | −18,07% – 20,94% |
| Deuda neta / EBITDA | 0,43 | 0,40 | 0,66 | 0,96 | 2,18 | 0,40 – 4,04 |
| Acciones diluidas promedio (M) | 4.267,91 | 4.343,86 | 4.410,48 | 4.459,61 | 4.472,49 | Máximo 4.553,72 (2021) |

Fuente: `metricas_historicas.json` y el Nivel 2, derivados del snapshot SEC [OBSERVADO].

Hay tres regímenes:
- **2016-2019:** crecimiento financiado con deuda y flujo libre negativo.
- **2020-2022:** transición, con 2022 como año de crisis (+6,5%).
- **2023-LTM:** monetización (cuentas compartidas, anuncios y precio) con apalancamiento operativo.

Para 2016-2018 el pasivo por arrendamientos operativos no está reportado (ASC 842 rige desde 2019), así que el capital invertido, el ROIC y ventas/capital de esos años son n.d. y los promedios de 10 años usan siete observaciones; no se sustituye con cero.

Los límites de homogeneidad son cuatro:
- ASC 842 incorpora los arrendamientos al balance desde 2019.
- Las acciones de 2016-2024 se ajustaron por el desdoblamiento 10:1.
- El LTM incluye la comisión de WBD (US$2.800 millones, fuera del EBIT) y ~US$100 millones de costos de transacción dentro del EBIT.
- El cargo de Brasil (US$619 millones, 3T25) está en 2025 pero ya no en el LTM.

El último trimestre es el 3T26 (julio a septiembre de 2026).

## 5. Crecimiento de ingresos: de la historia a la proyección

**Historia económica.** El crecimiento de 2023-2026 vino de tres palancas:
- El cobro a cuentas compartidas, ya absorbido.
- Alzas de precio en mercados maduros.
- Altas en LATAM y APAC.

La publicidad suma una cuarta palanca que todavía es pequeña (~5% de los ingresos). El tiempo de visualización creció 1,5% en 2025 y 2% en el 1S26 [OBSERVADO]. El crecimiento es de monetización, no de uso. El FX pesa: 56% de los ingresos está fuera del dólar, y en LATAM la diferencia entre lo reportado y la moneda constante fue de 12 puntos en 2025. No hay M&A relevante: la compra de marzo de 2026 fue de ~US$587 millones y la de WBD no se concretó.

**Verificación [MODELO].** 'Valuation output'!C4:L4 contiene exactamente 12, 11, 10, 9 y 8% en los años 1-5 y 7,2, 6,4, 5,6, 4,8 y 4,0% en los años 6-10. Coincide con 'Escenarios e historias'!C29:L29. El CAGR compuesto de los años 1-5 es (80.065,03 / 49.734,63)^(1/5) − 1 = 9,9909%; no es un promedio simple. El año 1 a 12% queda entre el +13,7% de los nueve meses y el ~+11% implícito en la guía del 4T26. Los años 2-5 desaceleran un punto por año.

**Seis preguntas.**
- (a) **Valor:** 12% en el año 1 (oct-26 a sep-27) y 9,99% de CAGR a cinco años en 'Valuation output' fila 4.
- (b) **Histórico:** 3 años 12,7%, 5 años 12,7% y 10 años 21,3%; el LTM a 9M es 13,7%.
- (c) **Mecanismo:** precio de 4-5 pp en UCAN/EMEA, miembros en LATAM/APAC y publicidad.
- (d) **Qué tendría que ocurrir:** alzas anuales sin rotación y publicidad ≥ US$4.500 millones en 2027.
- (e) **Qué lo refutaría:** dos trimestres ≤ +9% a moneda constante o una nueva rebaja de la publicidad.
- (f) **Impacto:** ±2 pp en los años 1-5 da US$63,99 (−9,7%) o US$78,44 (+10,7%) (matriz C de la hoja y réplica).

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Crecimiento años 1-5 | 12,7% / 12,7% / 21,3%; 9M26 13,7% | 12→8%; CAGR 9,99%; VO C4:G4 | Tramo >US$25.000 M de *The Base Rate Book*: mediana real 2,0% (≈4,5% nominal); solo ~23% logra ≥ 9,99% | Precio + publicidad + mercados nuevos | Uso +2%; publicidad rebajada; desaceleración a +11,8% en el 3T26 | ±2 pp: −9,7% / +10,7% |
| Crecimiento años 6-10 | n.a. | Convergencia lineal a 4%; VO H4:L4 | g terminal del corte (4%) | Madurez | Ninguna específica | Incluido en la prueba anterior |

**Juicio [INFERENCIA].** Es exigente frente a la tasa base, pero tiene un mecanismo específico y verificable; el auditor lo considera *plausible*. No hay prudencia duplicada: la Base no recorta además el crecimiento «por si acaso».

## 6. Márgenes operativos y normalización de beneficios

**Historia económica.** El margen bruto pasó de 39,4% (2022) a 50,7% (LTM), porque la amortización de contenido creció ~7% anual frente a ingresos de ~13-16%. Ventas y marketing (7,3%), tecnología y desarrollo (7,8%) y administración (4,3%) son estables en porcentaje. La compensación en acciones es baja (1,1% LTM). La regulación aparece en Brasil.

**Verificación [MODELO].** Las identidades se recalcularon en las 40 celdas por historia, sin diferencias:
- Ingreso × margen = EBIT.
- EBIT × (1 − t) = NOPAT.

El año 1 parte del margen LTM ajustado por I+D: 33,09% (31,30% GAAP + 893,33 / 49.734,63). Converge linealmente al 37,1% del año 5 (Input!B31 = 5). La normalización es correcta: el cargo de Brasil ya salió del LTM y la comisión de WBD está fuera del EBIT. Los ~US$100 millones de costos de WBD dentro del EBIT no se suman de vuelta, porque son inmateriales (0,2% de los ingresos, que mueven el margen del año 1 en 0,2 pp).

**Seis preguntas.**
- (a) **Valor:** 37,1% ajustado (36% GAAP) desde el año 5, en 'Input'/'Escenarios'!D5.
- (b) **Histórico:** GAAP de 25,6% (3 años), 23,1% (5 años) y 16,8% (10 años); el mejor trimestre fue el 3T26 con 34,6% y el peor año reciente, 2022 con 17,8%.
- (c) **Mecanismo:** apalancamiento del contenido y publicidad sobre una base fija de tecnología.
- (d) **Qué tendría que ocurrir:** amortización < ingresos, con el deporte en vivo ≤ ~5-7% del gasto.
- (e) **Qué lo refutaría:** margen de 2027 ≤ 31,5% con ingresos ≥ +10%.
- (f) **Impacto:** ±2 pp dan US$66,86 / US$74,84 (∓5,6%).

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Margen operativo objetivo | 25,6% / 23,1% / 16,8%; LTM 31,3%; 3T26 34,6% | 37,1% ajustado (36% GAAP), año 5 | Discovery 31,7% (2016, XBRL); DIS 19,3%, SPOT 13,7% (30-sep-2026) | Contenido crece menos que los ingresos; la publicidad diluye costos | Guía del 4T26 de 26,0%; costo del vivo | ±2 pp: ∓5,6% |
| Margen año 1 | LTM ajustado 33,09% | VO C6 | — | Punto de partida observable | Ninguna | Implícito |

**Juicio [INFERENCIA].** *Plausible con reservas*: supera a todos los comparables maduros, pero el 3T26 ya mostró 34,6%. No hay doble castigo: el riesgo de margen está en la Conservadora, no en la tasa.

## 7. Reinversión, Sales-to-Capital, ROIC/ROE y asignación de capital

**Historia económica.** La reinversión es contenido, tecnología y algo de capex. Las adiciones de contenido equivalen a 1,14 veces la amortización en el LTM, y el capex es 1,9% de los ingresos. Entre 2022 y el LTM los ingresos subieron US$18.119 millones con US$6.821 millones de capital adicional (2,66 veces sin I+D) [OBSERVADO]. La asignación de capital privilegia las recompras: US$10.782 millones en nueve meses, con 4.222 → 4.106 millones de acciones.

**Verificación [MODELO].** La fórmula de la plantilla es reinversiónₜ = (ventasₜ₊₁ − ventasₜ) / ventas-capitalₜ, recalculada sin diferencias. Base: 1,3 en los años 1-5 y 0,9 en los años 6-10. El rendimiento marginal implícito es margen × (1 − t) × ventas/capital: ≈38% en los años 1-5 (0,355 × 0,83 × 1,3) y ≈26% en los años 6-10 (0,371 × 0,79 × 0,9). Luego queda en 20,58% en la perpetuidad, una caída gradual. Sobre el capital total, el ROIC medio de la hoja pasa de 30,13% (base) a 38,53% (año 5) y 32,43% (año 10). El auditor no asume que margen × ventas/capital sea el ROIC contable: el ROIC de la hoja incluye el activo de I+D.

**Seis preguntas.**
- (a) **Valor:** 1,3 / 0,9 en 'Escenarios e historias'!E5:F5. Input!B32:B33 (1,20) no está activo, porque las historias lo sustituyen.
- (b) **Histórico:** ventas/capital de 1,20 (3 años), 1,13 (5 años) y 1,13 (siete años con dato, 2019-2025); el LTM es 1,29 y el marginal 2022→LTM, 2,66.
- (c) **Mecanismo:** el crecimiento futuro pide contenido local, deporte y tecnología publicitaria.
- (d) **Qué tendría que ocurrir:** que el gasto de contenido en efectivo se mantenga en ~1,1 veces la amortización.
- (e) **Qué lo refutaría:** un gasto de contenido de ≥ 1,2 veces sin crecimiento adicional.
- (f) **Impacto:** ±20% da US$69,01 / US$72,08 (−2,6% / +1,7%).

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| Ventas/capital | 1,20 / 1,13 / 1,13; LTM 1,29; marginal 2,66 | 1,3 (años 1-5), 0,9 (años 6-10) | Entertainment (Damodaran ene-2026): referencia sectorial, menor | Reinvertir en contenido sostiene el crecimiento | Más deporte en vivo | ±20%: −2,6% / +1,7% |
| ROIC del capital nuevo | ROIC medio 27-34% desde 2024 | ≈38% → ≈26% → 20,58% | ROIC de Entertainment 11,04% | Escala de contenido | Competencia por la atención | Ver §9 |

**Juicio [INFERENCIA].** *Razonable y algo prudente*: un 1,3 frente a un marginal de 2,66 incluye reposición de contenido. La corrección desde el borrador de 1,6 (rendimiento ~49% con salto abrupto) mejoró la coherencia.

## 8. Costo del capital y riesgo

**Verificación independiente** (`auditoria_controles.json`, costo_capital: PASS, error 0):

| Componente | Recalculado | Hoja | Fuente y comentario |
|---|---:|---:|---|
| Beta reapalancada | 0,9821 × (1 + 0,75 × 16.686,05 / 285.718,16) = 1,0251 | 1,0251 | Damodaran, Entertainment global; global porque 56% de las ventas está fuera de UCAN [MODELO] |
| ERP ponderada | 4,9266% | 4,927% | North America 3,70% (43,5%), EMEA 5,34% (32,2%), Central y South America 7,93% (12,3%), Asia 5,19% (12,0%) |
| Ke | 5,29% + 1,0251 × 4,927% = 10,340% | 10,340% | Conforme |
| Kd antes / después de impuestos | 6,065% / 4,549% | Ídem | Spread de 0,775% para la clase «A2/A» de la tabla de Damodaran |
| Pesos de mercado | E 94,48% · D 5,52% | Ídem | Deuda a valor de mercado con vencimiento de 4,1 años |
| WACC | 10,0207% | B14 = E63 = Input!B36 = 10,0207% | Conforme; submétodo Detailed, Single Business (Global), Operating regions |
| WACC terminal | 5,29% + 3,70% = 8,99% | Input!B97 | Beta 1 en estabilidad (regla vigente) |

No hay doble conteo. Los riesgos específicos (precio, atención, deporte) no están en la tasa sino en la Conservadora y la Disrupción, y la prima país se pondera por ventas sin añadir otra prima. La beta de regresión (0,93 a 2 años; 1,43 a 5 años) solo sirve de contraste. Los factores de descuento se recalcularon como producto acumulado de (1 + WACCₜ), sin diferencias.

**Prueba de tasa alternativa [MODELO].**
- Con la beta de Entertainment de EE. UU. (0,76 desapalancada, 0,79 reapalancada), el WACC inicial sería 8,94% y el DCF Base US$75,54 (+6,6%).
- Desplazar toda la trayectoria ±1 punto (matriz A) da US$89,77 / US$58,24.

**Seis preguntas.**
- (a) **Valor:** 10,02% en los años 1-5, convergente a 8,99% en los años 6-10.
- (b) **Histórico:** no aplica; la tasa libre era de 3,88% a fines de 2023.
- (c) **Mecanismo:** riesgo de mercado de un negocio de consumo discrecional global.
- (d) **Qué tendría que ocurrir:** que la beta sectorial global represente el riesgo.
- (e) **Qué lo refutaría:** que la beta bottom-up de EE. UU. sea la adecuada; la mezcla de ventas (56% fuera de UCAN) favorece la global [INFERENCIA].
- (f) **Impacto:** −6,6% / +6,6% según la tabla.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| WACC inicial | n.a. | 10,02%; CoC B14 | Histograma de EE. UU., mediana 7,79% (comparador) | Beta global, ERP por regiones | Beta de EE. UU. de 0,79 | Beta de EE. UU.: +6,6% |
| WACC terminal | n.a. | 8,99%; Input!B97 | Rf + ERP madura | Estabilidad con beta 1 | — | Matriz A: 63,97 a 79,26 con ±0,5 pp |

**Observación de presentación (AUD-08).** El texto de la valoración describe la calificación como «S&P "A"; Moody's A3», mientras la hoja usa la clase «A2/A». Con la clase A3/A-, el spread sube ~0,1-0,15 pp [INFERENCIA], el WACC +0,006 pp y el valor cambia en <0,1%. Es inmaterial.

## 9. Convergencia y valor terminal

| Control | Resultado |
|---|---|
| g perpetuo | 4,00% nominal USD = g del corte; ≤ Rf de 5,29% [MODELO, conforme] |
| WACC terminal > g | 8,99% − 4,00% = 4,99 pp [conforme] |
| Impuesto terminal | 25% marginal, con convergencia lineal desde 16,57% en los años 6-10 [conforme] |
| Reinversión terminal | g / ROIC = 4,00% / 20,58% = 19,44% del NOPAT₁₁; recalculada: 5.911,82 [conforme] |
| Continuidad FY10 → FY11 | Ingresos +4%; NOPAT 29.246,44 → 30.416,30; reinversión 16,0% → 19,4% del NOPAT; FCFF 24.574,95 → 24.504,48 |
| Valor terminal | 24.504,48 / 4,99% = 491.071,73; VP 194.378,70 = 63,8% del valor operativo |
| ROIC terminal | 20,58% (Base, Conservadora, Optimista); Disrupción = 8,99% |

**Regla de ventaja.** La regla vigente dice: sin ventaja, costo de capital; ventaja durable, promedio de la industria (11,04%); ventaja que se desvanece, punto medio. El registro `moat_2026-09-30.json` califica a Netflix como «ventaja durable». Aun así, el usuario decidió el 21-oct-2026 («Opción 2») usar el punto medio entre el ROIC actual y la industria. Con el ROIC actual de esta hoja (30,13%) el punto medio es 20,58%.

Es una **decisión metodológica documentada del usuario**, no un error de la valoración. El auditor la clasifica como **supuesto discutible pero razonable**:
- A favor: hay evidencia de retornos de 27-34% desde 2024 y una escala de contenido que la industria no tiene, y evita un salto de 32% a 11% en la perpetuidad.
- En contra: la regla literal llevaría a 11,04%.

Impacto calculado con la plantilla y con la réplica [MODELO]:
- Con 11,04%, el DCF Base sería US$60,98 (−13,9%).
- Con el costo de capital, US$56,13 (−20,8%).
- La propia pestaña 'Auditoría DCF interna' de la plantilla da US$56,13 para el costo de capital, una confirmación independiente.

**Registro desactualizado (AUD-07).** `moat_2026-09-30.json` todavía dice `roic_actual` 0,32 y `roic_terminal` 0,2152 (revisión del 21-oct). Debe actualizarse a 0,3013 / 0,2058 al publicar esta revisión.

**Optimista.** En esta historia el rendimiento del capital nuevo pasa de ≈36% (años 6-10) a 20,58%, el salto más grande de las cuatro. Es coherente con la decisión del usuario de usar el mismo ROIC terminal en las tres historias, y el auditor lo registra como discutible. Prueba en la Base: ROIC terminal de 25,58% da US$73,08 (+3,1%) y de 15,58%, US$67,19 (−5,2%).

**Prueba de erosión del moat.** Que la participación en el tiempo de TV de EE. UU. baje a ≤ 7,0% (hoy 7,9%) con un margen ≤ 31,5% en 2027.

**Seis preguntas.**
- (a) **Valor:** g 4%, ROIC 20,58% y WACC 8,99%, en VO M4, M42 y B19.
- (b) **Histórico:** ROIC 26,9% (3 años) y 23,1% (5 años).
- (c) **Mecanismo:** escala de audiencia, datos y gasto en contenido.
- (d) **Qué tendría que ocurrir:** que la ventaja persista más de diez años.
- (e) **Qué lo refutaría:** la sustitución de la atención (YouTube, IA).
- (f) **Impacto:** −13,9% / −20,8%.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| ROIC terminal | 26,9% / 23,1% / 20,9%; hoja 30,13% | 20,58%; Input!B50 | Entertainment global 11,04% | Ventaja de escala duradera | Atención que migra; la regla literal da 11,04% | 11,04%: −13,9%; WACC: −20,8% |
| g terminal | n.a. | 4,0%; Input!B69 | Inflación ~2,3% + real ~1,7% | Economía nominal en USD | — | ±0,5 pp: −4,5% / +5,5% |

## 10. Validación independiente del valor intrínseco

**Recalculación ejecutada** (`scripts/jmr_audit_checks.py`, que no usa el motor ni la réplica de la valoración). Toma solo las filas capturadas de cada bloque de 'Valuation output' y verifica en las cuatro historias:
- ingresos, EBIT, NOPAT, reinversión y FCFF;
- factor de descuento acumulado y VP del FCFF;
- reinversión terminal, valor terminal y su VP;
- suma de VP, valor operativo, puente y valor por acción.

El error máximo es **0,000000** en todas.

| Historia | VP flujos 1-10 | VP terminal | Valor operativo | − Deuda | + Caja | − Opciones | Acciones | Valor/acción recalculado | Peso del terminal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Base | 110.253,12 | 194.378,70 | 304.631,82 | 17.384,63 | 8.222,95 | 4.526,75 | 4.106,33 | **70,85** | 63,8% |
| Conservadora | 89.972,92 | 142.243,86 | 232.216,78 | Ídem | Ídem | Ídem | Ídem | 53,22 | 61,3% |
| Optimista | 134.501,66 | 245.807,30 | 380.308,97 | Ídem | Ídem | Ídem | Ídem | 89,28 | 64,6% |
| Disrupción | 67.547,91 | 41.034,36 | 108.582,27 | Ídem | Ídem | Ídem | Ídem | 23,11 | 37,8% |

**Otras piezas recalculadas:**
- **Opciones:** Black-Scholes con ajuste por dilución iterativo: S ajustado 68,6726, valor por opción 37,6679 y total US$4.526,75 millones. Coincide con la hoja (dif. < 10⁻⁹). El valor intrínseco simple sería US$3.405,76 millones, así que el valor temporal está incluido. Las opciones se restan una sola vez y las acciones usadas son las en circulación, no las diluidas, así que no hay doble conteo. Las RSU (1,87 millones de acciones, ~US$130 millones) no se valoran: 0,04% del patrimonio, inmaterial.
- **I+D (R& D converter):** vida de 3 años; activo = 3.890,81 + ⅔ × 3.391,39 + ⅓ × 2.925,30 = 7.126,84; amortización 2.997,48; ajuste del EBIT +893,33. Conforme.
- **Arrendamientos (Operating lease converter):** el conversor está desactivado (B18 = No) porque el pasivo ASC 842 ya está en la deuda; no hay doble conteo. Ver AUD-05 sobre el EBIT.
- **Costo de capital:** ver §8.

**Horizontes.** El DCF Base hoy (US$70,85) no se mezcla con los valores FY+3 de los múltiplos (US$83,93 en EV/EBITDA, etc.). El ponderado DCF + múltiplos (US$65,75) se presenta como lectura secundaria.

**Sensibilidad y DCF inverso.** Los centros de las tres matrices de 'Sensibilidad DCF' concilian con B35 (dif. < 10⁻¹¹). El DCF inverso usa la réplica, con error 0 frente a la hoja. Para el precio fechado de US$69,58 el delta es −0,356 pp en los años 1-5, un CAGR implícito de 9,63% frente a 9,99%. El error de reconstrucción es < 10⁻⁷. Los centros de la réplica coinciden además con la matriz C de la hoja, lo que la valida de forma cruzada.

**Seis preguntas sobre el supuesto dominante (retorno excedente perpetuo):** ver §9.

| Métrica y horizonte | Histórico (3/5/10 años, LTM) | Modelo: valor/año/celda | Industria/pares y fuente | Historia causal y requisitos | Evidencia contraria / juicio | Impacto en valor o prueba |
|---|---|---|---|---|---|---|
| DCF Base | n.a. | US$70,85; VO B35 | Precio US$69,58 | Base completa | DCF inverso de 9,63% | Recalculado: error 0 |
| Peso del terminal | n.a. | 63,8% | Alerta de la plantilla > 75% | Crecimiento estable | — | Dentro del rango |

## 11. Cuatro historias y probabilidades

| Historia | Crecimiento | Margen EBIT | Reinversión/ROIC | WACC/Ke | g y retorno terminal | Valor principal por acción | Probabilidad registrada | Qué la confirma/refuta |
|---|---|---|---|---|---|---:|---:|---|
| Base | 12→8%; CAGR 9,99% | 37,1% ajustado / 36% GAAP | S2C 1,3 / 0,9; ROIC 30→38→32% | 10,02% → 8,99% | 4%; 20,58% | 70,85 | 45% | Ingresos ≥ +11% y margen ≥ 34% en 2027 |
| Conservadora | 10→5%; 7,19% | 32,7% / 32% | 1,1 / 0,8 | Igual | 4%; 20,58% | 53,22 | 22,5% | Ingresos ≤ +9%; uso ≤ +1% |
| Optimista | 14→10%; 11,99% | 41,3% / 40% | 1,5 / 1,1 | Igual | 4%; 20,58% | 89,28 | 22,5% | Publicidad ≥ US$6.000 M en 2027 |

**Promedio condicionado de tres historias** = Σpᵢ·Vᵢ / Σpᵢ = (0,45 × 70,8525 + 0,225 × 53,2175 + 0,225 × 89,2819) / 0,90 = **US$71,05**. El denominador está documentado.

**Hallazgo AUD-01 (ronda 1, corregido).** La plantilla IA calculaba H10 como AVERAGE(H5;H6;H8), una media simple de US$71,12, y la columna «Aporte esperado» como H/3. Ignoraba las probabilidades, contra la regla vigente (§2, pesos renormalizados). La valoración lo corrigió en la copia (`scripts/jmr_copy_formula_fix.py`, respaldo `respaldo_formula_promedio.json`) y la ronda 2 verificó H10 = 71,0511. Impacto: −0,09% sobre el complemento; ninguno sobre el DCF Base ni el MOS. **La plantilla oficial conserva el defecto y requiere decisión del usuario.**

**Probabilidades.** Coinciden con la previa «crecimiento maduro» de `probabilidades_prior.json` (45/22,5/22,5/10), con desvío 0 y sin ajustes. Ningún indicador cruzó su umbral escrito: el 3T26 creció +11,8%, entre ≤ 9% y ≥ 11%, y el margen se mide en 2027. Suman 100%. **MOS** = 70,85 × 0,65 = US$46,05, sobre el principal.

### ¿Qué pasaría si todo fallara?

**Disrupción.** El video generado por IA y las plataformas gratuitas comoditizan el contenido:
- crecimiento de 6, 4, 2, 1 y 0% y luego 0%;
- margen de 22%;
- ROIC terminal igual al costo de capital y g = 0.

Resultado: **US$23,11** por acción, con probabilidad registrada de 10%. Está excluida del promedio ordinario. Como dato complementario, el esperado de las cuatro historias sería 0,45 × 70,85 + 0,225 × 53,22 + 0,225 × 89,28 + 0,10 × 23,11 = US$66,26 [INFERENCIA, etiquetado: no es una cifra oficial].

## 12. Valoración por múltiplos: prueba independiente y secundaria

**Integridad (§5A).** Los siete métodos se calcularon con las fórmulas de la plantilla, incluidos P/S (`PV`) y P/BV (`PBV`) con peso 0. La auditoría recalculó para EV/EBITDA, EV/FCFF, P/E, P/FCFE y P/OCF, en las tres historias, la cadena completa: 'Financials Multiples' → precio FY+3 → descuento a Ke. El error máximo es < 10⁻¹¹ [conforme]:
- EV: (múltiplo × fundamental − 13.688,43) / 4.267,91.
- Equity: múltiplo × fundamental / acciones.

La IA solo eligió entradas, múltiplos de salida (J8/J19/J30) y pesos. P/BV concilia el patrimonio común (PBV!M7:O9: otros movimientos = −0,827 × utilidad neta + 0,0084 × ingresos, recompras netas documentadas). No es un cero precargado.

| Método | A: historia (mediana 5 años) | B: pares (mediana) | C: justificado Cons/Base/Opt | Elegido Cons/Base/Opt | LTM | Denominador FY+3 Base (US$ M) | VP Base hoy | Peso efectivo |
|---|---:|---:|---|---|---:|---:|---:|---:|
| EV/EBITDA | 30,17× | 18,75× | 13,03 / 15,06 / 17,51 | Ídem (topado por C) | 18,48× | EBITDA 24.695,23 | 60,37 | 10% |
| EV/FCFF | 49,49× | 27,80× | 19,98 / 24,11 / 27,89 | Ídem | 25,92× | FCFF 15.432,49 | 57,51 | 15% |
| P/E | 40,47× | 21,63× | 16,07 / 18,86 / 21,38 | Ídem | 20,11× | Utilidad 18.822,79 | 60,06 | 5% |
| P/FCFE | 48,46× | 31,26× | 17,44 / 20,53 / 23,23 | Ídem | 25,12× | FCFE 16.275,44 | 57,39 | 5% |
| P/OCF | 51,79× | 22,67× | 18,31 / 22,35 / 25,71 | Ídem | 23,21× | OCF 14.949,33 | 54,04 | 5% |
| P/V | 8,76× | n.d. | 4,12 / 5,22 / 6,34 | Ídem | 5,74× | Ventas 68.013,11 | 61,93 | 0% |
| P/BV | 14,87× | n.d. | 6,73 / 8,99 / 11,29 | Ídem | 9,76× | Patrimonio 39.480,92 | 61,71 | 0% |

Comprobaciones:
- **Ajuste por tasas:** factor (k_cierre − g)/(k_corte − g), acotado a [0,6; 1,4] según `ciclo_resultado.json` [MODELO].
- **Techos:** ningún múltiplo supera su ancla C; en los 21 casos manda C. El Conservador ≤ LTM se cumple en los siete métodos.
- **Descuentos generales:** no hay; los factores de Toro quedan solo como diagnóstico.
- **Independencia de C:** el ancla C comparte flujos con el DCF y no es evidencia independiente. No se calibró al DCF: los múltiplos dan 54-62 frente a 70,85.
- **Denominadores:** EV/FCFF usa FCFF (no FCF genérico) y P/OCF usa OCF (no FCF). Los años con OCF negativo (2016-2019) quedan excluidos.
- **Complementarios:** EV/EBIT (15,41× → US$60,30) y P/FCF (23,67× → US$53,78) se reprodujeron con la misma cadena, sin peso. La puerta de publicación los exige y la plantilla no los tiene.

**Hallazgos de múltiplos.**
- **AUD-04 (acciones):** la plantilla usa 4.267,91 millones de acciones diluidas promedio LTM, constantes, frente a 4.106,33 millones en circulación en el DCF. Subestima los precios por acción de los múltiplos en 3,8%. Con acciones en circulación, el consolidado de múltiplos sería ~US$60,38 y el ponderado ~US$66,66 (+1,4%) [INFERENCIA, cálculo proporcional].
- **AUD-06 (FCFE):** el FCFE proyectado suma endeudamiento neto de US$3.677, 2.142 y 2.161 millones en FY+1 a FY+3, una regla de la plantilla. Implica ~US$8.000 millones más de deuda, frente a una política de deuda bruta estable. Sin ese endeudamiento, el P/FCFE Base bajaría a ~US$46,65, el consolidado de múltiplos −US$1,34 y el ponderado −0,8% [INFERENCIA].

AUD-04 y AUD-06 tienen signos opuestos; ninguno toca el DCF Base ni el MOS.

## 13. Sensibilidades económicas y escenarios alternativos

**DCF Base** (hoja, centros conciliados):
- WACC × g: US$58,24 a US$89,77 con ±1 pp de WACC al g de 4%.
- ROIC terminal × g: US$70,27 a US$71,38 con ±1 pp de ROIC.
- CAGR × margen: US$51,50 a US$96,89.

Pruebas de un solo supuesto (réplica verificada):

| Supuesto | US$/acción | Variación |
|---|---:|---:|
| Margen −2 pp / +2 pp | 66,86 / 74,84 | −5,6% / +5,6% |
| Crecimiento años 1-5 −2 pp / +2 pp | 63,99 / 78,44 | −9,7% / +10,7% |
| Ventas/capital −20% / +20% | 69,01 / 72,08 | −2,6% / +1,7% |
| WACC inicial +1 pp / −1 pp (terminal fijo) | 66,81 / 75,19 | −5,7% / +6,1% |
| g terminal −0,5 pp / +0,5 pp | 67,68 / 74,73 | −4,5% / +5,5% |
| ROIC terminal = WACC terminal | 56,13 | −20,8% |
| ROIC terminal = industria (11,04%) | 60,98 | −13,9% |
| Acciones +5% | 67,48 | −4,8% |

**DCF inverso frente al precio fechado** (US$69,58, 30-sep-2026), crecimiento necesario de los años 1-5:

| Beta | Margen 35,1% | Margen 37,1% | Margen 39,1% |
|---|---:|---:|---:|
| Beta 1,03 | 10,78% | 9,63% | 8,57% |
| Beta 0,79 | 9,51% | 8,39% | 7,34% |

**Múltiplos (familia de valor por acción, solo Base).** La valoración generó 14 matrices: 7 métodos × 2 anclas fechadas al 30-sep-2026 (JMR y observado LTM).
- Eje vertical: múltiplo real en veces (±20%). Eje horizontal: fundamental FY+3 real en US$ millones (±20%).
- Cada celda es el VP hoy por acción.
- Los siete centros JMR concilian con el VP FY+3 de la hoja (EV/EBITDA 62,48; EV/FCFF 62,51; P/E 61,92; P/FCFE 58,28; P/OCF 58,27; P/V 61,92; P/BV 61,91).
- Centros con el múltiplo observado LTM: EV/EBITDA 77,21; EV/FCFF 67,39; P/E 66,02; P/FCFE 71,30; P/OCF 60,53; P/V 68,15; P/BV 67,18.

La familia económica (múltiplo justificado) no se despliega, por regla; sus centros son las anclas C de la tabla de §12. No hay matrices de Conservadora, Optimista ni Disrupción en los documentos.

**AUD-03 (presentación).** La pestaña «Sensibilidad por múltiplo» de la copia proviene de la plantilla: tiene 21 matrices, con ejes rotulados como factores 0,8…1,2 e incluidas Conservadora y Optimista. Sus 21 centros concilian (OK), pero la pestaña no cumple la regla de «solo Base con ejes reales», así que se rechaza como matriz editorial. Las matrices válidas son las del Nivel 2 §7. Regenerar la pestaña exige cambiar el generador común (`multiples_sensitivity_contract.js`), una decisión del usuario que afecta a todas las empresas.

## 14. Coherencia de hojas, cálculos y presentación

| Artefacto | Resultado |
|---|---|
| 'Input sheet' | Candados B84, B85, B92 y B108 en VALIDADO; B109, B110, B113 y B114 en NO APLICA con causa; B111 y B112 en VALIDADO; K5:K8 en LISTO. B32:B33 = 1,20 inactivos (las historias usan E5:F8), sin efecto. B30 (21,8%) es una referencia no activa |
| Estados y LTM | 785 celdas importadas y postverificadas; LTM recalculado con dif. 0 |
| 'Valuation output' (cuatro bloques) | Recalculados con error 0 |
| 'Escenarios e historias' | AUD-01 corregido: H10 = 71,05 |
| 'Option value', 'R& D converter', 'Cost of capital worksheet' | Recalculados, conformes |
| 'Sensibilidad DCF' | Centros OK |
| 'Sensibilidad por múltiplo' | AUD-03 |
| 'Descuento de múltiplos' | Cadena recalculada; rótulo «Promedio 1-3 años · Ke 010%» mal formateado (AUD-09, presentación; el valor usado es 10,34%) |
| 'Trailing Valuation' y pestañas de métodos | Rótulos «Nov '24/'25» y «Columna N» de la plantilla, corregidos solo en la copia (registrado en la valoración) |
| 'Industry Averages(US)' | #DIV/0 de la plantilla, sin uso en el valor |
| CoC enfoque 2 | «Industry average» da 0,71%: comparador roto de la plantilla, no usado (Detailed es el método) |
| 'Auditoría DCF interna' | Identidades OK. Tras este dictamen, B36:B39 = REVISADO y B56 = CONCILIADO (`entradas_auditoria_9.json`, con respaldo). Una captura posterior confirmó que solo cambió esa pestaña (`verificacion_post_auditoria.json`) |
| Valoración v5 | Cifras = foto; promedio 71,05 tras AUD-01; MOS sobre la Base; Disrupción aparte |
| Research v5 | 18 secciones; cifras = foto; ningún número de la revisión anterior (control del ensamblador) |
| Nivel 2 | Estados, ratios, cuatro historias, sensibilidades, DCF inverso y 14 matrices Base |
| JSON y visor | Ficha de la revisión con sha de la foto; `reference/damodaran/NFLX.json` y la app **no** actualizados (publicación pendiente de autorización) |

**Completitud del análisis (REGLAS §9).** Se contrastó con la última versión completa (21-oct-2026, 149 KB): la nueva tiene 159 KB, y ninguna sección quedó más corta en contenido sustantivo. Las secciones 2, 4, 6, 7, 8, 10, 11 y 13 conservan su texto con reemplazos verificados; las 1, 3, 5, 9, 12, 14-18 se reescribieron con el LTM de septiembre. El análisis tiene recuadro de valor base, nivel 1 íntegro, nivel 2 y matriz de cobertura en la sección 18. Hay dos limitaciones de evidencia declaradas: el proxy de 2026 no se revisó, y no hay prueba ácida porque las cuentas por cobrar no se publican por separado. El auditor detectó y el análisis corrigió un defecto heredado: la matriz crecimiento × margen del 21-oct tenía valores incompatibles con su propio DCF.

## 15. Hallazgos priorizados y propuestas de corrección

Materialidad según REGLAS §4B: V_base = US$70,85; impacto = |V_alt − V_base| / V_base.

| ID | Severidad | Tipo | Evidencia | Impacto | Mantener/ajustar/investigar | Propuesta y alternativa | Requiere aprobación | Estado |
|---|---|---|---|---|---|---|---|---|
| AUD-01 | Medio | Fórmula (plantilla) | H10 = AVERAGE; I5:I8 = H/3 | Promedio 71,12 → 71,05 (−0,09%); DCF Base y MOS 0% | Ajustar | Corregido en la copia con respaldo; **corregir la plantilla oficial** | Sí, para la plantilla oficial | Corregido en la copia y verificado |
| AUD-02 | Bajo | Supuesto (dato) | Tasa efectiva LTM de 16,57% incluye la comisión WBD gravada; sin ella ≈15,74% (suponiendo 21% sobre la comisión) [INFERENCIA] | +0,36% (prudente) | Mantener | Opcional: tasa efectiva sin partidas no recurrentes | No | Salvedad no bloqueante |
| AUD-03 | Bajo | Presentación (plantilla) | Pestaña con 21 matrices y ejes en factores | 0% | Ajustar al publicar | Usar las matrices Base del Nivel 2; regenerar la pestaña con un generador «solo Base» | Sí (generador común) | Abierto, no bloqueante |
| AUD-04 | Bajo | Fórmula (convención) | Múltiplos con 4.267,91 M de acciones frente a 4.106,33 M | Múltiplos −3,8%; ponderado −1,4% (prudente); DCF 0% | Investigar | Unificar acciones en la plantilla | Sí | Salvedad |
| AUD-05 | Bajo | Supuesto | Arrendamientos en deuda sin sumar al EBIT el componente financiero (~US$86 M = 2.252 × 3,8%, tasa de descuento del 10-K) | +0,06% a +0,11% (prudente) | Mantener | Opcional: ajustar el EBIT por el interés implícito | No | Salvedad no bloqueante |
| AUD-06 | Bajo | Supuesto (plantilla) | El FCFE proyecta endeudamiento neto de US$8.000 M en tres años | P/FCFE −19%; ponderado −0,8% (agresivo); DCF 0% | Investigar | Endeudamiento neto según la política de deuda | Sí | Salvedad |
| AUD-07 | Bajo | Registro | `moat_2026-09-30.json` con ROIC 0,32 / 0,2152 de la revisión anterior | 0% (la hoja usa 20,58%) | Ajustar al publicar | Actualizar a 0,3013 / 0,2058 | Con la publicación | Abierto |
| AUD-08 | Bajo | Presentación | Rating descrito como Moody's A3; la hoja usa A2/A | < 0,1% | Ajustar texto | Citar la clase usada | No | Corregido en el texto de la valoración |
| AUD-09 | Bajo | Presentación (plantilla) | Rótulo «Ke 010%» | 0% | Ajustar | Formato de porcentaje en la plantilla | Sí (plantilla oficial) | Abierto |
| AUD-10 | Bajo | Supuesto | R& D converter: el año −1 es FY2025 y se solapa un trimestre con el LTM; con FY2024 como año −1 | +0,10% | Mantener | Convención habitual de la plantilla | No | Salvedad |
| D-1 | — | Supuesto discutible documentado | ROIC terminal de 20,58% (decisión del usuario) frente a 11,04% de la regla literal | −13,9% (11,04%); −20,8% (WACC) | Mantener | Revisar en cada actualización con la participación en el tiempo de TV | Decisión ya tomada | Discutible pero razonable |
| D-2 | — | Supuesto discutible | Paso del rendimiento marginal en la Optimista (≈36% → 20,58%) y en la Base (≈26% → 20,58%; reinversión 16,0% → 19,4% del NOPAT) | Base ±5 pp de ROIC: −5,2% / +3,1% | Mantener | — | No | Discutible pero razonable |
| D-3 | — | Supuesto discutible | Margen GAAP de 36% superior a todos los comparables maduros | ±2 pp: ∓5,6% | Mantener | Vigilar el margen de 2027 | No | Discutible pero razonable |

**Materialidad agregada.**
- Ningún hallazgo individual llega a 2% del DCF Base.
- Los hallazgos que mueven el valor intrínseco (AUD-02, AUD-05, AUD-10) son todos prudentes y suman +0,57% en valor absoluto.
- El límite adverso acumulado sobre el DCF Base es 0%.
- Ninguno cruza la decisión: precio/DCF = 0,98, y el precio queda por encima del precio con MOS de US$46,05 en cualquier caso.
- No hay defectos de identidades, unidades, moneda, fechas, deuda, acciones, tasas, escenarios ni doble conteo.

**Clasificación §4B:** (A) bloqueantes: ninguno; (B) reservas materiales: ninguna; (C) salvedades inmateriales: AUD-01 a AUD-10; (D) no aplicables: preferentes, convertibles, minoritarios, NOL material, fracaso empresarial y SOTP.

## 16. Catalizadores, señales de refutación y seguimiento

| Métrica | Nivel observado con fecha | Señal favorable | Señal adversa | Fuente | Frecuencia |
|---|---|---|---|---|---|
| Crecimiento de ingresos a/a | +11,8% (3T26); +13,7% (9M26) | ≥ +11% en 2027 | ≤ +9% dos trimestres | Cartas a accionistas, 10-Q | Trimestral |
| Margen operativo | 34,6% (3T26); guía 2026 31,5% | ≥ 34% en 2027 | ≤ 31,5% | Ídem | Trimestral |
| Ingresos de publicidad | ~US$2.700 M (guía 2026) | ≥ US$4.500 M en 2027 | Nueva rebaja | Cartas | Trimestral |
| Adiciones de contenido / amortización | 1,14 (LTM) | ≤ 1,1 | ≥ 1,2 | 10-Q (flujo de caja) | Trimestral |
| Participación en el tiempo de TV de EE. UU. | 7,9% (jun-2026, Nielsen vía MediaPost) | ≥ 8,3% | ≤ 7,0% | Nielsen The Gauge | Mensual |
| ROIC después de impuestos (con arrendamientos) | 33,8% (LTM) | ≥ 30% | < 25% | Snapshot SEC | Trimestral |
| Acciones en circulación | 4.106,33 M (30-sep-2026) | −2% anual o más | Suben | Portada del 10-Q | Trimestral |

Los umbrales son criterio del auditor y del análisis, no guías oficiales. El próximo informe es el de resultados del 4T26 en enero de 2027; la fecha exacta no está confirmada [NO VERIFICADO].

## 17. Dictamen económico y resumen para escuchar

**Calificación de la tesis: Plausible con reservas.**
- **Consistencia matemática:** conforme. Los cuatro DCF, el WACC, las opciones, el I+D, el LTM, las historias, la cadena de múltiplos y las sensibilidades se recalcularon con error ~0. El único defecto aritmético (AUD-01) se corrigió en la copia.
- **Trazabilidad documental:** conforme. La fuente primaria es la SEC, con hashes, derivaciones verificadas y entradas con respaldo y etiqueta. La vida de las opciones no se verificó contra la nota.
- **Razonabilidad económica:** plausible con reservas. El crecimiento y el margen son exigentes frente a las tasas base y los comparables, pero tienen mecanismo y evidencia trimestral. El ROIC terminal es una decisión documentada del usuario por encima de la regla literal.
- **Supuesto más frágil:** la publicidad como palanca del margen, cuya meta de 2026 ya se rebajó. **Más defendible:** el costo de capital y los datos de partida. **Motor principal del precio:** el retorno excedente perpetuo, con 63,8% del valor en el terminal.
- **Decisión analítica sugerida:** conservar las hipótesis, revisar el ROIC terminal y la publicidad con los resultados del 4T26, y corregir AUD-01 y AUD-03 en la plantilla oficial con autorización.

**Estado de la revisión: VERIFICADO con salvedades no bloqueantes** (§4B). Esta auditoría no se autocertifica para publicar: la publicación exige la autorización explícita del usuario.

**Resumen para escuchar.** Auditamos la valoración de Netflix del 25 de octubre de 2026 con datos al 30 de septiembre. Las cuentas cuadran: recalculamos los cuatro escenarios, la tasa de descuento, las opciones y los múltiplos, y todo coincide con la hoja. Encontramos un error de la plantilla: el promedio de las tres historias no usaba las probabilidades. Ya se corrigió en la copia y el promedio quedó en 71,05 dólares. No cambia el valor principal de 70,85 dólares ni el precio de compra con margen de seguridad, 46,05. El supuesto que más pesa es que Netflix siga ganando por encima de su costo de capital para siempre. Si no fuera así, el valor bajaría alrededor de 21%. El precio de mercado, 69,58, pide casi exactamente la historia base. No se modificó la valoración.

## 18. Fuentes primarias, limitaciones y registro de versión

**Fuentes** (todas consultadas el 25-oct-2026):
- Netflix, [10-K 2025](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm) (23-ene-2026; FY2025; estados, arrendamientos, compromisos).
- Netflix, [10-Q del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm) (21-oct-2026; balance al 30-sep-2026, 9M2026, opciones).
- Netflix, [10-Q del 3T25](https://www.sec.gov/Archives/edgar/data/1065280/000106528025000406/nflx-20250930.htm) (22-oct-2025; 9M2025 para el LTM).
- Netflix, [carta a accionistas del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm) (20-oct-2026; regiones, guía, publicidad, recompras).
- SEC, [companyfacts XBRL de Netflix](https://data.sec.gov/api/xbrl/companyfacts/CIK0001065280.json) (opciones, tasa de descuento de arrendamientos, costo de arrendamientos de 2025: US$503,6 M).
- FRED [DGS10](https://fred.stlouisfed.org/series/DGS10) (30-sep-2026: 5,29%).
- Damodaran: [betas por industria](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html) (enero de 2026), primas por país/región (enero de 2026) y [ERP implícita de octubre de 2026](https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx).
- Mauboussin y Callahan, *The Base Rate Book* (2016).
- Nielsen The Gauge vía [MediaPost](https://www.mediapost.com/publications/article/417308/) (jun-2026).
- Yahoo Finance (precios al 30-sep-2026).

**Archivos auditados:**
- Foto `resultados_hoja.json` (sha256 `6afa5b6aba533dcbd28143ba547eb3c98de1b541d5695a9a0e6351a2a06e58d5`).
- `auditoria_controles.json` (controles independientes, status PASS).
- `snapshot_sec_conciliado.json`, `NFLX_derivation_audit.json`, `NFLX_materiality_adjudication.json`.
- `dcf_inverso.json`, `sensibilidades_un_supuesto.json`, `sensibilidad_multiplos_base.json`.
- `correccion_formula_promedio.json` y su respaldo.
- Rama `fix/jmr-flujo-seguro-20261024` del repositorio JMR-valuation (PR #145, borrador).

**No verificado o no ejecutado:**
- La vida remanente de 4,04 años de las opciones contra la nota del 10-Q.
- La volatilidad de 33,8% como dato de la empresa (se tomó como supuesto del modelo).
- El proxy de 2026.
- La fecha de resultados del 4T26.
- La familia económica de múltiplos desplegada (no exigida).
- La recalculación de Conservadora y Optimista con la beta de EE. UU.
- La app y el visor (no publicados).

**Registro de versión:**
- Auditoría v1 de la revisión `NFLX-2026-10-25`, `prompt_version: auditoria-economica-jmr-v1.2`.
- Ronda 1: AUD-01 detectado. Ronda 2: verificado tras la corrección en la copia y la nueva foto.
- Versiones previas: `data/NFLX_Auditoria_Valoracion_2026-10-01.md` y `data/NFLX_Auditoria_Economica_Narrativa_2026-10-21.md`, que se conservan y se archivarán con la publicación.
- **Publicación:** no publicada. La ruta `Modelo-JMR-datos/auditorias/narrativas/NFLX.md` queda pendiente de la autorización explícita del usuario.
