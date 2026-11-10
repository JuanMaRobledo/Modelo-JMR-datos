# AAPL-REBOOT-FY26-R1 · Fase R3 (historias y DCF)

- **Fecha:** 2026-11-09 · **Agente:** Claude (Code, nube): Sheets, SEC XBRL, FMP, FRED, LibreOffice (recálculo local del motor) · esfuerzo: alto.
- **Libros:** DCF Base `1FDKimjBtpWeJO1wjK2-iFbQBhc7fziRWspCqkl41am8` · Conservadora `1z7399gpLt0t0IMTgvXav4u6tEEsCIevd-GSE1U7KMcM` · Optimista `18_DpC1IBerZBKzBpWWkSi-9h4EzXH_fIlesGqmeKffM`. Estado **CANDIDATO** (R4 pendiente; sin auditoría F5).
- **Motor:** fcffsimpleginzu original de Damodaran. Verificado contra el xlsx original: de **1.230 fórmulas y 76 comentarios**, solo cambiaron **5 celdas de entrada** que traían una fórmula por defecto y ahora tienen un valor (`Input sheet` B27, B28, B29, B32 y B62). Ninguna otra fórmula ni comentario difiere.

## Resultado
| | Conservadora | **Base** | Optimista | Esperado (25/50/25) |
|---|---|---|---|---|
| Valor por acción | 106,92 | **209,58** | 260,45 | 196,63 |
| Frente al precio (342,37, 6-nov-2026) | −68,8 % | **−38,8 %** | −23,9 % | −42,6 % |
| Probabilidad | 25 % | 50 % | 25 % | 100 % |

**Precio con MOS 35 % = 0,65 × 209,58 = 136,22 USD** (solo sobre la Base). Hoy el precio cotiza **63 % sobre el DCF Base** y por encima incluso de la Optimista. Conservadora ≤ Base ≤ Optimista: cumple.

## Entradas comunes (mismas en las tres historias)
| Entrada | Valor | Fuente / criterio |
|---|---|---|
| Ingresos LTM, EBIT LTM | 478.834 · 158.063 | 10-K FY2026 (LTM = FY2026) |
| Gasto por intereses | 3.000 | **ESTIMADO**: Apple ya no lo divulga; 3,4 % implícito FY2023 × deuda media FY2025–26 |
| Patrimonio contable | 112.093 | 10-K |
| Deuda | 94.479 | 80.111 financiera + 14.368 arrendamientos ASC 842 (ya en balance → `Operating lease commitments = No`, sin doble conteo) |
| Caja e inversiones | 136.935 | efectivo 36.305 + inversiones CP 20.417 + inversiones LP 80.213 |
| Acciones | 14.590,6 | 14.532,2 en la portada del 10-K (2026-10-23) + 58,4 de dilución incremental de RSU (diluidas − básicas, FY2026). Apple no tiene opciones: `Option value = No` |
| Precio | 342,37 | cierre 2026-11-06 (FMP y Alpha Vantage) |
| Impuesto efectivo / marginal | 17,0 % / 25 % | 27.062 / 159.237; 25 % marginal de EE. UU. (el efectivo converge al marginal en el año 10) |
| I+D capitalizada | Sí, 5 años | I+D FY2017–26 de H. Activo de investigación 109.443; ajuste al EBIT +16.965 → EBIT ajustado 175.028, **margen ajustado 36,55 %** |
| Tasa libre | 4,86 % | FRED DGS10 2026-11-06 |
| Crecimiento terminal | 4,0 % | regla §4 (techo = tasa libre) |
| Valor terminal fase estable | costo de capital 8,25 % (beta 1) | Rf 4,86 % + ERP madura 3,387 % |
| Costo de capital inicial | **10,25 %** | beta desapalancada 1,283 (multinegocio: Computers/Peripherals 319.956; Electronics General 35.577; Software System & Application 123.301, ingresos FY2026 por producto del 10-K) → apalancada 1,30; ERP por regiones 4,23 % (mat. 3,387 % + riesgo país ponderado: Norteamérica 198.083, Europa 127.604, Asia 153.147); Ke 10,35 %; Kd antes de impuestos 5,41 % (calificación «Aa2/AA», la más cercana a AA+/Aaa); pesos de mercado 98,4 % / 1,6 % |
| ERP madura | 3,387 % | decisión del usuario, Damodaran nov-2026 |
| Datos del año anterior (diagnósticos) | ingresos 416.161; EBIT 133.050; patrimonio 73.733; deuda 112.377; caja 132.420 | 10-K FY2025 |

Supuestos que son **estimación o convención mía**, no dato: intereses (3.000), vencimiento medio de la deuda (7 años; vencimientos del 10-K con el tramo posterior a 5 años supuesto en 10), mapeo de segmentos a industrias de Damodaran (Europa del 10-K incluye India, Medio Oriente y África; Japón y Resto de Asia-Pacífico se llevaron a «Asia»), calificación «Aa2/AA», dilución por RSU.

## Historias (Damodaran: historia → números)
**Tipo de historia: crecimiento maduro.** Probabilidades: previa JMR 45 / 22,5 / 22,5 (y 10 de disrupción) → sin la cuarta historia, **50 / 25 / 25**; no hubo cruce de umbral para ajustarlas.

### Base · «Franquicia premium que madura con servicios al alza» (50 %)
Apple vende un ecosistema de dispositivos (iPhone, 53 % de los ingresos) cuyo parque instalado alimenta Servicios (26 % de los ingresos y creciendo +13 %). Tras el ciclo extraordinario de FY2026 (+15 %; iPhone +21 %), el hardware vuelve a crecer a un dígito bajo y Servicios a dos dígitos; el margen sube levemente por mezcla; invierte poco por dólar de ventas (activos ligeros) y devuelve la caja con recompras.
| Palanca | Celda | Valor | Vínculo con la historia |
|---|---|---|---|
| Crecimiento año 1 | B26 | 6,0 % | después de FY2026 normaliza: hardware +3–4 %, Servicios +12 % |
| CAGR años 2–5 | B28 | 5,5 % | Servicios 26 % → 33 % de la mezcla a ~11 %; hardware ~3 % |
| Margen año 1 / objetivo | B27 / B29 | 36,6 % / 37,0 %, año 5 | parte del margen actual ajustado; +0,4 puntos por mezcla de Servicios, compensado por I+D de IA (9,6 % de ventas, +32 % en FY2026) |
| Ventas/capital 1–10 | B31–B32 | 3,0 | actual 2,67 (con I+D); industria 3,62 |
| ROIC terminal | B48–B49 | 44,76 % | ventaja durable: promedio de la industria (regla del moat: gana sobre su costo de capital >3 años, ventaja identificable, sin erosión visible) |
| Fracaso | B51 | No | riesgo en los flujos, no en la probabilidad |
**Evidencia a favor:** ingresos FY2017–26 CAGR 8,5 %; Servicios con margen alto y recurrente; ROIC actual 81 %; recompras 86.390 y dividendos 15.721 en FY2026. **En contra:** FY2026 es un año atípico (iPhone +21 %); regulación de App Store (UE, EE. UU.); pagos de Google por búsqueda (del orden de 20.000 anuales, dato público no verificado en esta revisión; riesgo judicial); aranceles y China (Greater China +28 % en FY2026 tras −4 % en FY2025). **Objeción más fuerte a la Base:** un margen de 37 % a diez años exige que Servicios compense la presión sobre comisiones y el costo de I+D de IA; la historia Conservadora recoge ese riesgo.
**Disparadores:** (1) ruptura: ingresos de Servicios <+8 % dos trimestres seguidos; (2) cambio: margen operativo trimestral <33 %; (3) desplazamiento: caída de la base instalada o de la tasa de renovación de iPhone.

### Conservadora · «Erosión del ecosistema» (25 %)
Regulación y competencia reducen comisiones de App Store y los pagos de búsqueda; China cede cuota; el ciclo de IA en el dispositivo no reaviva la demanda; el hardware se estanca.
| Palanca | Celda | Valor | Vínculo |
|---|---|---|---|
| Crecimiento año 1 / CAGR 2–5 | B26 / B28 | 2,5 % / 2,0 % | hardware plano, Servicios +6 % |
| Margen año 1 / objetivo | B27 / B29 | 35,5 % / 31,0 % año 5 | −5,5 puntos: comisiones, pérdida de pagos de búsqueda (del orden de 20.000 anuales, no verificado), aranceles |
| Ventas/capital | B31–B32 | 2,4 | más capital por dólar de ventas (cómputo para IA) |
| ROIC terminal | B48 | No → costo de capital | la erosión de la ventaja se refleja aquí (regla del moat) |
| Fracaso | B51–B54 | Sí · 5 % · 60 % del valor | desplazamiento de la plataforma; **solo en esta historia** |
**Disparadores:** fallo adverso firme contra comisiones de App Store o acuerdo de búsqueda; ventas de iPhone en Greater China cayendo dos años; margen operativo <32 %.

### Optimista · «Plataforma de IA en el dispositivo y Servicios de dos dígitos» (25 %)
El ciclo de IA genera renovaciones de iPhone más frecuentes y nuevas categorías; Servicios crece 14–15 % y llega a ~38 % de la mezcla.
| Palanca | Celda | Valor | Vínculo |
|---|---|---|---|
| Crecimiento año 1 / CAGR 2–5 | B26 / B28 | 9,0 % / 8,0 % | hardware +5 %, Servicios +14 % |
| Margen año 1 / objetivo | B27 / B29 | 37,0 % / 40,0 % año 5 | mezcla de Servicios y apalancamiento operativo |
| Ventas/capital | B31–B32 | 3,5 | cercano a la industria (3,62) |
| ROIC terminal | B48–B49 | 44,76 % | ventaja durable; no se supera la industria sin evidencia |
**Disparadores:** ingresos de Servicios >+15 % tres trimestres; ciclo de renovación de iPhone <3 años; nuevo producto >20.000 de ventas.

### Pruebas 3P (señales de `Diagnostics`; el juicio es mío)
- **Posible:** participación de mercado **N/D** (no hay TAM homogéneo y confiable para smartphones + servicios digitales; no se inventa). Ventas del año 10: 787.302 (Base) frente a 478.834 hoy.
- **Plausible (Base):** margen año 10 37,0 % frente a 22,5 % de la industria *Computers/Peripherals*: **REVISAR**, sustentado por el ecosistema y el 26 % de Servicios (la propia Apple ya gana 36,5 % ajustado en FY2026 (la historia no exige que lo supere en más de 0,5 puntos)); ventas/capital 3,0 frente a 3,62 de la industria: ok; ROIC terminal 44,76 % = industria: ok; ROIC del año 10 de 80 % frente a 44,76 % terminal: la eficiencia transitoria no se perpetúa. Juicio: **Con reserva** por margen.
- **Probable (Base):** CAGR 5,5–6,0 % frente a 6,7 % de la industria y 8,5 % histórico de Apple; el valor de los 10 años es 36 % del total y el terminal 64 %. Juicio: **Sí**.

## DCF inverso y sensibilidades (hoja `Sensibilidades DCF` del libro Base)
Corridas del motor original recalculado localmente (reproduce 209,5761 / 106,9160 / 260,4456; centro de las matrices = Base).
- Para que el valor sea 342,37 hay que creer, una variable a la vez: **crecimiento de 14,7 % anual los años 1–5** (repetir el +15,1 % de FY2026 durante cinco años), o **margen objetivo de 62,8 %**, o **crecimiento de 13,3 % con margen de 40 %**. El costo de capital inicial **no alcanza**: con 5 % el valor llega a 282,29.
- Matriz A (CAGR 2–5 × margen): rango 172,94 a 252,28. Matriz B (costo de capital inicial × g terminal): rango 173,18 a 256,31. En ninguna celda se alcanza el precio.

## Controles
| Control | Estado |
|---|---|
| Motor original sin cambios (1.230 fórmulas, 76 comentarios) | APROBADO (5 entradas con valor en vez de fórmula) |
| Costo de capital común a las tres historias (10,2520 % inicial, 8,247 % estable, Ke 10,3542 %) | APROBADO |
| Probabilidades = 100 %; Cons ≤ Base ≤ Opt; fracaso solo en Conservadora | APROBADO |
| WACC > g en todas las fases | APROBADO (8,25 % > 4,0 %) |
| Reproducción independiente del motor (LibreOffice sobre el xlsx original) vs Google Sheets | APROBADO (a 6 decimales) |
| MOS 35 % solo sobre la Base | APROBADO |
| Diagnóstico «ventas/capital» y reinversión coherentes con ROIC marginal | PARCIAL: ROIC marginal 70,5 % es alto; la historia lo explica por activos ligeros y recompras, no verificado contra benchmarks externos |
| Auditoría económica independiente | **NO_EJECUTADO (F5/R6)** |
| `AISLAMIENTO=OK` | Sí: nada de `archivo-v1/` ni del libro Floyd previo |

## Siguiente paso exacto
R4: cargar en el LIBRO MÚLTIPLOS los estados de H y los supuestos de la Base (crecimiento, márgenes, tasas, acciones, Ke 10,3542 %), elegir múltiplos de salida y pesos justificados (EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF) y traspasar los resultados al `Resumen de valoraciones`.
