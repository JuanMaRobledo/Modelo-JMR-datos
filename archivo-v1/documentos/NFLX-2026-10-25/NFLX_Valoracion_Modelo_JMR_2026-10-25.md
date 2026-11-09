---
schema: "jmr-valuation-v5"
title: "Valoración de Netflix, Inc. (NFLX) · Modelo JMR"
ticker: "NFLX"
revision_id: "NFLX-2026-10-25"
valuation_date: "2026-09-30"
financial_cutoff: "2026-09-30 (10-Q del 3T26 presentado el 21-oct-2026; extracción SEC as_of 2026-10-24)"
market_cutoff: "2026-09-30 (precio, Treasury y prima de Damodaran del corte común de la cartera)"
sheet: "https://docs.google.com/spreadsheets/d/1ZPNMHxc7m3Iv60mdGspgi6-cc2zwf5kZ4ocsuANQUNM/edit"
results_snapshot_sha256: "6afa5b6aba533dcbd28143ba547eb3c98de1b541d5695a9a0e6351a2a06e58d5"
status: "VERIFICADO con salvedades no bloqueantes (auditoría NFLX-2026-10-25) · publicación autorizada el 25-oct-2026"
currency: "USD"
---

# Valoración de Netflix, Inc. (NFLX) · revisión NFLX-2026-10-25

> **Valor intrínseco base: US$70,85 por acción** · DCF FCFF Base (criterio Damodaran) · corte 30-sep-2026 · revisión `NFLX-2026-10-25`.
> Todas las cifras salen de la copia de trabajo de la plantilla IA ([hoja](https://docs.google.com/spreadsheets/d/1ZPNMHxc7m3Iv60mdGspgi6-cc2zwf5kZ4ocsuANQUNM/edit)) y de la foto `reference/revisiones/NFLX-2026-10-25/resultados_hoja.json` (sha256 `6afa5b…58d5`). Ninguna se recalcula fuera del motor salvo EV/EBIT y P/FCF complementarios, señalados como tales. Precisión interna completa; presentación a dos decimales. No es una recomendación de inversión.

Convención de etiquetas: **[Dato]** reportado con fuente; **[Cálculo]** fórmula reproducible; **[Juicio]** supuesto del analista con evidencia a favor y en contra.

## 1. Resumen

| Concepto | Valor | Etiqueta |
|---|---:|---|
| **DCF Base hoy (valor intrínseco principal)** | **US$70,85** | [Cálculo] Valuation output!B35 |
| Promedio de tres historias (condicionado a que no ocurra la disrupción) | US$71,05 | [Cálculo] Σpᵢ·Vᵢ / Σpᵢ, Escenarios e historias!H10 (fórmula corregida en la copia: la plantilla promediaba sin pesos; hallazgo AUD-01 de la auditoría) |
| Rango Conservadora – Optimista | US$53,22 – US$89,28 | [Cálculo] |
| ¿Qué pasaría si todo fallara? Disrupción (10 %) | US$23,11 | [Cálculo], fuera del promedio |
| Precio con MOS 35 % sobre el DCF Base | US$46,05 | [Cálculo] 70,85 × (1 − 0,35) |
| Precio al corte (30-sep-2026) | US$69,58 | [Dato] cierre NASDAQ |
| Precio / DCF Base | 0,98 | [Cálculo] |
| DCF inverso | El precio implica un CAGR de ingresos años 1-5 de 9,63 % frente a 9,99 % de la Base (delta −0,36 pp) | [Cálculo] `dcf_inverso.json` |

Múltiplos como precio relativo (Base, valor hoy, secundario): EV/EBITDA US$60,37 · EV/FCFF US$57,51 · P/E US$60,06 · P/FCFE US$57,39 · P/OCF US$54,04 · P/S US$61,93 · P/BV US$61,71; complementarios EV/EBIT US$60,30 y P/FCF US$53,78. Consolidado de múltiplos ponderados US$58,09; ponderado DCF + múltiplos US$65,75 (lectura secundaria, nunca valor intrínseco).

## 2. Historia y visión externa

**La historia en un párrafo [Juicio].** Netflix es el servicio de entretenimiento por suscripción y publicidad con mayor audiencia del mundo y el mayor comprador individual de series, películas y eventos en vivo. En los próximos cinco años los ingresos crecen ~10 % anual compuesto (12 % el primer año, 8 % el quinto) porque tres palancas siguen activas: precio por miembro en mercados maduros (alzas de 2026 absorbidas «como las anteriores», [carta del 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm)), miembros nuevos en LATAM y APAC y una publicidad que parte de ~US$2.700 millones en 2026. El margen operativo GAAP sube de 31,3 % (LTM) a ~36 % porque la amortización de contenido crece menos que los ingresos y la publicidad se apoya en una base fija de tecnología; no sube más porque contenido, deporte en vivo y la competencia por la atención (YouTube, video corto, IA generativa) obligan a seguir gastando. La reinversión es sobre todo contenido y tecnología: el gasto de contenido en efectivo es ~1,1 veces la amortización. El riesgo principal no es de caja sino de uso: si el tiempo de visualización no crece, el precio deja de ser palanca.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Ingresos +12 % el año 1 y ~10 % compuesto a cinco años | Sí | Sí: 9M2026 +13,7 % y guía 2026 de US$51.100 M (+13 %) [Dato] | Probable con desaceleración: 3T26 +11,8 %; el uso por miembro casi no crece |
| Margen GAAP ~36 % en cinco años | Sí | Sí: 17,8 % (2022) → 29,5 % (2025) → 34,6 % en el 3T26; guía 2026 31,5 % [Dato] | Plausible: exige que contenido y deporte crezcan menos que los ingresos |
| Publicidad duplica su peso | Sí | Sí: plan con anuncios en 15 países nuevos en 2027 [Dato] | Menos probable: la meta de 2026 se rebajó de ~US$3.000 M a ~US$2.700 M |
| Reinversión moderada (ventas/capital 1,3 en años 1-5) | Sí | Sí: ventas/capital incremental 2022→LTM de 2,66 sin I+D [Cálculo] | Probable |

**Visión externa [Cálculo].** Con ingresos LTM de US$49.735 M, Netflix está en el tramo de mayor tamaño de *The Base Rate Book* (Mauboussin y Callahan, 2016), donde la mediana real de crecimiento a cinco años ronda 2 % (≈4,5 % nominal). La Base (9,99 % nominal) se aparta de esa mediana por razones específicas y verificables: crecimiento actual de dos dígitos, publicidad que partió de cero en 2022 y penetración baja fuera de Norteamérica. Aun así, la Base ya incorpora la regresión a la media: de 12 % a 8 % en cinco años y convergencia lineal a 4 % en el año 10.

**Descomposición del crecimiento [Dato].** LTM por región ([10-K 2025](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm) + [10-Q 3T26](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm) − 9M2025): UCAN US$21.644 M (43,5 %), EMEA US$16.011 M (32,2 %), LATAM US$6.102 M (12,3 %), APAC US$5.977 M (12,0 %). Crecimiento 3T26: UCAN +11 %, EMEA +11 % (+9 % a moneda constante), LATAM +17 % (+12 %), APAC +12 % (+15 %). Orgánico: la única compra relevante (~US$587 M, marzo de 2026) se trata como reinversión en el flujo de inversión.

## 3. Datos y conciliación

- **Fuente primaria:** SEC companyfacts e instancias XBRL de los 10-K 2016-2025 y de los 10-Q 3T25 y 3T26 (31.213 hechos), con hash por archivo. Snapshot conciliado `snapshot_sec_conciliado.json`: 28/28 identidades contables, LTM independiente PASS (7 magnitudes), cobertura de 11 ejercicios + LTM PASS, 20/20 derivaciones verificadas contra XBRL, 46 vacíos materiales adjudicados y 0 sin revisar ([docs/NFLX_CIERRE_SEC_2026-10-25.md](../docs/NFLX_CIERRE_SEC_2026-10-25.md)).
- **Importación:** 785 celdas de los tres estados y de entradas auxiliares, postverificadas una a una; respaldo previo `respaldo_antes_importacion.json`.
- **Correcciones de extracción que cambian el valor si se omiten:** contenido no tratado como intangible genérico (34.605 M USD); cobros por inversiones = ventas + vencimientos; acciones de 2016-2023 ajustadas por el split 10:1; tecnología y desarrollo con el tag de Netflix (`TechnologyandDevelopmentExpense`), que deja en cero el residuo de la cuenta de resultados.
- **LTM a 30-sep-2026 [Cálculo]:** ingresos 45.183,04 + 37.683,87 − 33.132,27 = US$49.734,63 M; EBIT 13.326,60 + 12.608,21 − 10.369,94 = US$15.564,87 M (31,30 %).
- **Balance al 30-sep-2026 [Dato]:** caja e inversiones US$8.222,95 M; notas US$15.132,39 M (2.474,80 corrientes + 12.657,60 no corrientes); arrendamiento operativo US$2.252,24 M; patrimonio US$29.286,25 M; acciones en circulación 4.106,33 M.
- **Partida no recurrente:** comisión de terminación del acuerdo WBD de US$2.800 M cobrada en el 1T26, registrada en «Interest and other income» (fuera del EBIT). Infla la utilidad neta LTM (US$14.766,65 M) y la caja; no entra en el valor operativo.
- **Hecho posterior:** carta del 3T26 del 20-oct-2026 con guía del 4T26 (ingresos US$13.400 M, margen 26,0 % con ~120 pb de reducción de personal) y flujo libre 2026 de ~US$12.000 M.

## 4. Costo de capital

| Componente | Valor | Etiqueta y fuente |
|---|---:|---|
| Método | Detailed, VALIDADO | [Juicio] Cost of capital worksheet!B12/B84 |
| Tasa libre | 5,29 % | [Dato] Treasury 10 años 30-sep-2026 (FRED) |
| Beta desapalancada | 0,98 | [Dato] Damodaran, Entertainment global (ene-2026); tabla global porque 56 % de las ventas está fuera de UCAN |
| Beta reapalancada (D/E de mercado 5,8 %) | 1,03 | [Cálculo] C58 |
| Beta de regresión semanal vs S&P 500 | 0,93 (2 años) · 1,43 (5 años) | [Cálculo] solo referencia; la de 5 años incluye la caída de 2022 |
| Prima de riesgo por regiones | 4,93 % | [Cálculo] ERP madura 3,70 % + primas regionales ponderadas por ingresos LTM (North America 3,70 %, EMEA 5,34 %, Central and South America 7,93 %, Asia 5,19 %) |
| Costo del patrimonio | 10,34 % | [Cálculo] 5,29 % + 1,03 × 4,93 % |
| Costo de la deuda antes de impuestos | 6,07 % | [Cálculo] Rf + spread de la clase «A2/A» de la tabla de Damodaran (S&P «A»; Moody's A3 según fuentes secundarias de 2025) |
| Tasa marginal | 25 % | [Dato] Damodaran EE. UU. |
| Pesos de mercado | 94,48 % patrimonio · 5,52 % deuda (incluye arrendamientos) | [Cálculo] E 285.718 M; D 16.686 M a valor de mercado |
| **WACC inicial** | **10,02 %** | [Cálculo] B14 = E63 = Input!B36 |
| WACC terminal | 8,99 % | [Cálculo] Rf + ERP madura (beta 1) |
| Controles externos | Rating sintético (cobertura 18,2×) y histograma US mediana | Comparadores, no WACC |

Los riesgos diversificables (dependencia del precio, competencia por la atención, costo de derechos deportivos) no están en la tasa: van en las historias.

## 5. Historias

| Historia | Prob. | Crecimiento años 1-10 | CAGR 1-5 | Margen objetivo (base ajustada / GAAP) | Ventas/capital 1-5 · 6-10 | ROIC terminal | g terminal | DCF/acción |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| **Base** · líder global con precio, publicidad y miembros | 45 % | 12, 11, 10, 9, 8, 7,2, 6,4, 5,6, 4,8, 4,0 % | 9,99 % | 37,1 % / 36 % | 1,3 · 0,9 | 20,58 % | 4,00 % | **US$70,85** |
| Conservadora · saturación y competencia por la pantalla | 22,5 % | 10, 8, 7, 6, 5, 4,8, 4,6, 4,4, 4,2, 4,0 % | 7,19 % | 32,7 % / 32 % | 1,1 · 0,8 | 20,58 % | 4,00 % | US$53,22 |
| Optimista · publicidad y deporte en vivo amplían el mercado | 22,5 % | 14, 13, 12, 11, 10, 8,8, 7,6, 6,4, 5,2, 4,0 % | 11,99 % | 41,3 % / 40 % | 1,5 · 1,1 | 20,58 % | 4,00 % | US$89,28 |
| Disrupción · el video gratuito y generado por IA comoditiza el contenido | 10 % | 6, 4, 2, 1, 0, 0… % | 2,58 % | 22,0 % / 22 % | 1,0 · 0,9 | 8,99 % | 0,00 % | US$23,11 |

**Base ajustada [Cálculo].** La hoja capitaliza tecnología y desarrollo (vida de 3 años; activo US$7.126,84 M; EBIT +US$893,33 M). El margen del año 1 es el LTM ajustado, 33,09 %, frente a 31,30 % GAAP. Por eso los márgenes objetivo se escriben en base ajustada: GAAP + ajuste de I+D en estado estable al crecimiento del año 5 (+1,1 pp en la Base, +0,7 pp en la Conservadora, +1,3 pp en la Optimista y 0 pp en la Disrupción).

**ROIC terminal [Juicio documentado].** Se aplica la decisión del usuario del 21-oct-2026 (`reference/moat_2026-09-30.json`, «Opción 2»): punto medio entre el ROIC actual de la hoja (30,13 %, con I+D y arrendamientos) y el promedio de Entertainment global de Damodaran (11,04 %) = 20,58 %, igual en Base, Conservadora y Optimista. La Disrupción usa el costo de capital (8,99 %). La transición es gradual: el rendimiento marginal del capital nuevo es ≈38 % en los años 1-5 (0,355 × 0,83 × 1,3) y ≈26 % en los años 6-10 (0,371 × 0,79 × 0,9) antes del 20,58 % perpetuo. La reinversión pasa de 16,0 % del NOPAT en el año 10 a 19,4 % en el terminal (4,0 % / 20,58 %).

**Coherencia de la reinversión [Cálculo].** ROIC medio de la Base: 30,1 % (base) → 38,5 % (año 5) → 32,4 % (año 10). Queda dentro del doble del ROIC terminal hacia el año 10 y por encima de él antes, por la ventaja de escala sostenida en el horizonte explícito.

**Probabilidades [Juicio].** Previa «crecimiento maduro» 45/22,5/22,5/10. Ningún indicador cruzó su umbral al corte: el crecimiento del 3T26 fue +11,8 %, entre los umbrales de ≥11 % y ≤9 %, y el margen del 3T26 fue de 34,6 %.

| Indicador | Valor actual (fuente) | Favorece Base/Optimista | Favorece Conservadora/Disrupción |
|---|---|---|---|
| Crecimiento de ingresos a/a | +11,8 % 3T26; +13,7 % 9M26 | ≥ +11 % en 2027 | ≤ +9 % |
| Margen operativo | 34,6 % 3T26; guía 2026 31,5 % | ≥ 34 % en 2027 | ≤ 31,5 % |
| Ingresos por publicidad | ~US$2.700 M 2026 (rebajado) | ≥ US$4.500 M en 2027 | Nueva rebaja |
| Gasto de contenido en efectivo / amortización | ~1,1× (guía) | ≤ 1,1× | ≥ 1,2× |
| Participación en tiempo de TV EE. UU. (Nielsen) | 7,9 % jun-2026 | ≥ 8,3 % | ≤ 7,0 % |
| Flujo libre | ~US$12.000 M 2026 (guía) | Creciente | Cae con ingresos al alza |
| Acciones en circulación | 4.106,33 M (−2,7 % en 9 meses) | Bajan ≥2 %/año | Suben |

**Pre-mortem (si en 2029 la tesis falló):**
1. El uso por miembro se estancó y las alzas de precio elevaron la rotación.
2. La publicidad no escaló (otra rebaja de meta) y el margen incremental fue menor.
3. El costo de contenido y de derechos deportivos absorbió el apalancamiento operativo.
4. Un dólar fuerte recortó el crecimiento reportado: 56 % de los ingresos está fuera de UCAN.
5. Una compra grande, del tipo del intento con WBD, cambió el perfil de riesgo y frenó las recompras.

**Puente Base [Cálculo]:** (110.253,12 + 194.378,70) VP operativo = 304.631,82; − deuda 17.384,63 + caja 8.222,95 − opciones 4.526,75 = 290.943,40; ÷ 4.106,33 M acciones = **US$70,85**. El terminal pesa 63,8 % del valor operativo; WACC terminal − g = 4,99 pp.

## 6. Múltiplos (precio relativo, secundarios)

Se calcularon los siete métodos de la plantilla con sus fórmulas: historia propia por ciclo (±2 pp de crecimiento), ajuste por tasas `(k_cierre − g)/(k_corte − g)` acotado a [0,6; 1,4], tope del ancla C justificada por los fundamentales FY+3 de cada historia y comprobación con pares (DIS, SPOT, ROKU, CMCSA, GOOGL al 30-sep-2026). En todos los métodos manda el ancla C, porque la historia de Netflix (30-50×) se pagó con tasas de 1-4 %.

| Método | Historia (mediana 5 años) | LTM | Pares (mediana) | Ancla C (Cons/Base/Opt) | Elegido Cons/Base/Opt | Precio FY+3 Base | Valor hoy Base | Peso |
|---|---:|---:|---:|---|---|---:|---:|---:|
| EV/EBITDA | 30,17× | 18,48× | 18,75× | 13,03 / 15,06 / 17,51 | 13,03 / 15,06 / 17,51 | US$83,93 | US$60,37 | 10 % |
| EV/FCFF | 49,49× | 25,92× | 27,80× | 19,98 / 24,11 / 27,89 | 19,98 / 24,11 / 27,89 | US$83,97 | US$57,51 | 15 % |
| P/E | 40,47× | 20,11× | 21,63× | 16,07 / 18,86 / 21,38 | 16,07 / 18,86 / 21,38 | US$83,18 | US$60,06 | 5 % |
| P/FCFE | 48,46× | 25,12× | 31,26× | 17,44 / 20,53 / 23,23 | 17,44 / 20,53 / 23,23 | US$78,29 | US$57,39 | 5 % |
| P/OCF | 51,79× | 23,21× | 22,67× | 18,31 / 22,35 / 25,71 | 18,31 / 22,35 / 25,71 | US$78,29 | US$54,04 | 5 % |
| P/S (PV) | 8,76× | 5,74× | n.d. | 4,12 / 5,22 / 6,34 | 4,12 / 5,22 / 6,34 | — | US$61,93 | 0 % |
| P/BV (PBV) | 14,87× | 9,76× | n.d. | 6,73 / 8,99 / 11,29 | 6,73 / 8,99 / 11,29 | — | US$61,71 | 0 % |
| EV/EBIT (complementario) | — | 18,95× | — | 13,35 / 15,41 / 17,89 | 13,35 / 15,41 / 17,89 | — | US$60,30 | — |
| P/FCF (complementario) | — | 25,12× | — | 19,42 / 23,67 / 27,13 | 19,42 / 23,67 / 27,13 | — | US$53,78 | — |

Notas:
- Pesos según el tipo «Crecimiento» de la plantilla: DCF 60 % y múltiplos 40 %, repartidos en EV/FCFF 37,5 %, EV/EBITDA 25 %, P/E, P/FCFE y P/OCF 12,5 % cada uno.
- P/S y P/BV se calculan con peso 0. P/S es redundante con EV/EBITDA mientras el margen se expande. En P/BV el patrimonio está reducido por recompras netas del 82,7 % de la utilidad, que se concilian en PBV!M7:O9.
- EV/EBIT y P/FCF no existen en la plantilla y se reproducen con su misma cadena (`scripts/jmr_complementary_multiples.py`).
- Ningún múltiplo supera su ancla C ni se calibra al DCF.
- El Conservador queda por debajo del LTM en todos los métodos.
- Excepciones: con la mediana de 5 años, P/OCF y P/FCF de 2016-2019 quedan excluidos por flujo operativo negativo.

## 7. Sensibilidad y DCF inverso (solo sobre la Base)

Las tres matrices son de la hoja (`Sensibilidad DCF`). Cada celda recalcula el DCF completo y el centro concilia con el Base (OK).

**A · WACC terminal × g:**

| WACC \ g | 3,00 % | 3,50 % | 4,00 % | 4,50 % | 5,00 % |
|---|---:|---:|---:|---:|---:|
| 9,02 % | 78,16 | 83,33 | 89,77 | 98,05 | 109,06 |
| 9,52 % | 70,47 | 74,43 | 79,26 | 85,29 | 93,02 |
| **10,02 %** | 64,06 | 67,15 | **70,85** | 75,36 | 80,99 |
| 10,52 % | 58,65 | 61,09 | 63,97 | 67,42 | 71,62 |
| 11,02 % | 54,01 | 55,97 | 58,24 | 60,93 | 64,13 |

**B · ROIC terminal × g:**

| ROIC \ g | 3,00 % | 3,50 % | 4,00 % | 4,50 % | 5,00 % |
|---|---:|---:|---:|---:|---:|
| 19,58 % | 63,71 | 66,70 | 70,27 | 74,62 | 80,04 |
| 20,08 % | 63,89 | 66,93 | 70,57 | 75,00 | 80,52 |
| **20,58 %** | 64,06 | 67,15 | **70,85** | 75,36 | 80,99 |
| 21,08 % | 64,22 | 67,36 | 71,12 | 75,71 | 81,43 |
| 21,58 % | 64,38 | 67,57 | 71,38 | 76,04 | 81,84 |

**C · Crecimiento años 1-5 (CAGR) × margen objetivo:**

| CAGR \ margen | 33,10 % | 35,10 % | 37,10 % | 39,10 % | 41,10 % |
|---|---:|---:|---:|---:|---:|
| 5,99 % | 51,50 | 54,64 | 57,78 | 60,92 | 64,06 |
| 7,99 % | 56,90 | 60,45 | 63,99 | 67,53 | 71,07 |
| **9,99 %** | 62,87 | 66,86 | **70,85** | 74,84 | 78,83 |
| 11,99 % | 69,46 | 73,95 | 78,44 | 82,93 | 87,41 |
| 13,99 % | 76,73 | 81,77 | 86,81 | 91,85 | 96,89 |

**DCF inverso [Cálculo]** (`scripts/jmr_dcf_inverse.py`). Réplica independiente del bloque Base: 70,852485 frente a 70,852485 de la hoja, error 0,000000. El método es un delta aditivo común a las tasas de los años 1-5, que se desvanece linealmente en los años 6-10 para conservar la convergencia al g fijo, con los demás supuestos fijos. Para el precio fechado de US$69,58 (30-sep-2026) el delta es **−0,36 pp**: CAGR implícito de 9,63 % frente a 9,99 % del Base. El error de reconstrucción del precio es menor que 0,001. Lectura: el mercado paga casi exactamente la historia Base.

Sensibilidades de múltiplos (solo Base, regla vigente): 14 matrices con ejes reales, múltiplo de salida en veces × fundamental FY+3 en US$ millones, para dos anclas fechadas al 30-sep-2026: el múltiplo elegido por JMR y el observado LTM. Están en el Nivel 2 (§7, `sensibilidad_multiplos_base.json`) y los siete centros JMR concilian con el VP FY+3 de la hoja. La pestaña «Sensibilidad por múltiplo» de la copia conserva las 21 matrices que trae la plantilla, con ejes en factores 0,8…1,2 e incluidas Conservadora y Optimista; no se publican (hallazgo AUD-03 de la auditoría).

## 8. Controles (prompt v5 §7) y precio

| # | Control | Resultado |
|---:|---|---|
| 0 | Entradas completas; I+D, arrendamientos y opciones tratados; candados VALIDADO/LISTO | Sí: B84 WACC VALIDADO, B85 VALIDADO, B92 VALIDADO, B108-B114 VALIDADO/NO APLICA, K5:K8 LISTO |
| 1 | Regiones suman el total; CAGR geométrico; caja, deuda y acciones del último informe | Sí: 21.644 + 16.011 + 6.102 + 5.977 = 49.735; balance al 30-sep-2026 |
| 2 | g ≤ tasa libre; g < costo de capital terminal; peso terminal informado | Sí: 4,00 % ≤ 5,29 %; 8,99 % − 4,00 % = 4,99 pp; terminal 63,8 % del VO |
| 3 | ROIC terminal según la regla de ventaja | Sí, con la decisión documentada del usuario (punto medio) |
| 4 | Márgenes: ninguno > 2,5× el del sector sin ventaja demostrada; Optimista ≤ Base + 10 pp | Sí: margen ya demostrado de 34,6 % en el 3T26; la Optimista queda 4,2 pp sobre la Base |
| 5 | Probabilidades = previa + ajustes; suman 100 % | Sí: 45 + 22,5 + 22,5 + 10 |
| 6 | Siete múltiplos con fórmulas de la plantilla; ninguno sobre su ancla C | Sí; P/S y P/BV con peso 0 justificado |
| 7 | MOS sobre la Base | Sí: US$46,05 |
| 8 | Etiquetas [Dato]/[Cálculo]/[Juicio] | Sí |
| 9 | AISLAMIENTO = OK | Ninguna cifra ni texto de otra empresa ni de la valoración NFLX anterior. Pares solo como comparables declarados. La regla de ROIC terminal es una decisión metodológica del usuario, no un dato |

**El precio, al final.** El precio de US$69,58 está 1,8 % por debajo del DCF Base (US$70,85), 2,1 % por debajo del promedio de tres historias (US$71,05) y muy por encima de la Disrupción (US$23,11). El DCF inverso muestra que el mercado descuenta un crecimiento apenas inferior al de la Base.

¿Qué sabe el mercado que yo no? Que la meta de publicidad ya se rebajó y que el uso por miembro casi no crece. Ambos riesgos están en la Conservadora, pero el mercado podría estar dándoles más peso que el 22,5 %. En sentido contrario, el crecimiento del 3T26 (+11,8 %) y el margen (34,6 %) se cumplieron.

Con el MOS de 35 %, el precio de compra según la regla de la cartera es US$46,05.

## 9. Fuentes

- Netflix, [10-K 2025 (23-ene-2026)](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm); [10-Q 3T26 (21-oct-2026)](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm); [10-Q 3T25 (22-oct-2025)](https://www.sec.gov/Archives/edgar/data/1065280/000106528025000406/nflx-20250930.htm); [carta a accionistas del 3T26 (8-K, 20-oct-2026)](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm); [companyfacts XBRL](https://data.sec.gov/api/xbrl/companyfacts/CIK0001065280.json); consultados el 25-oct-2026.
- Damodaran: betas y medias por industria (enero de 2026) y primas por país/región, en la plantilla; ERP implícita de octubre de 2026 en `reference/corte_vigente.json`.
- FRED DGS10 al 30-sep-2026 (5,29 %). Precios de Yahoo Finance (auto_adjust=False, ajustados por split) de NFLX y de los pares al 30-sep-2026.
- Mauboussin y Callahan, *The Base Rate Book* (2016).
- Calificaciones: S&P «A» / Moody's «A3» (fuentes secundarias de 2025; sin acción posterior a la terminación del acuerdo WBD).

## 10. Ficha JSON para el modelo

La ficha de esta revisión está en `reference/revisiones/NFLX-2026-10-25/ficha_damodaran_NFLX.json`. No reemplaza a `reference/damodaran/NFLX.json` hasta que la revisión se certifique y se autorice su publicación.
