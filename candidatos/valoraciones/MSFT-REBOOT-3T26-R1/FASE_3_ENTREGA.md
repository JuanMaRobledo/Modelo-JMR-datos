# MSFT-REBOOT-3T26-R1 · Fase R3 (historias y DCF)

- **Fecha:** 2026-11-10 · **Agente:** Claude (Code, nube): Sheets, SEC (10-K FY2026 y 10-Q 1T-FY2027), LibreOffice (recálculo local del motor). Estado **CANDIDATO** (sin R4–R6).
- **Libros:** DCF Base `19f9zo6xbYTnrjoAZwVf5ViHzVCEnkde9no2cryOBQjA` (con hoja nueva `Sensibilidades DCF`) · Conservadora `1TF-_XL14nxdAgNkHzJN3w5plZzOPj54rN2jnFfB33ho` · Optimista `13yJEdR4nTxVwE7b2bspxRGi8Pyk9Q_guwTmQdK36EMg`.
- **Motor:** fcffsimpleginzu original; solo se escribieron celdas de entrada. **Integridad de fórmulas y comentarios no re-verificada** en estas copias.

## Resultado
| | Conservadora | **Base** | Optimista | Esperado (25/50/25) |
|---|---|---|---|---|
| Valor por acción | 232,38 | **496,21** | 676,08 | 475,22 |
| Frente al precio (530,61 · 6-nov-2026) | −56,2 % | **−6,5 %** | +27,4 % | −10,4 % |

**Precio con MOS 35 % = 0,65 × 496,21 = 322,54 USD.** El precio de mercado queda **por encima** del DCF Base (6,5 %) y 64 % por encima del precio con MOS: no hay margen de seguridad. Réplica local = Google Sheets en las tres historias.

## Entradas comunes y decisiones de método
| Entrada | Valor | Fuente / criterio |
|---|---|---|
| Ingresos LTM · EBIT LTM | 346.445 · 163.191 (47,1 %) | H (XBRL): FY2026 + 3M-FY27 − 3M-FY26 |
| Año anterior (FY2026) | 331.839 · 155.237 | 10-K |
| I+D capitalizada | Sí, 3 años | I+D LTM 36.463; FY2026 35.562; FY2025 32.488; FY2024 29.510 → EBIT ajustado 167.134, margen 48,24 % |
| Patrimonio | 470.509 | Balance 30-sep-2026 |
| **Deuda** | **106.454** | Bonos 35.481 (incluye 4.391 corriente) **+ arrendamientos financieros 70.973**. **Decisión mía:** los arrendamientos financieros son financiamiento de centros de datos (su amortización está en el EBIT, su interés no), así que se tratan como deuda; sin ellos la deuda sería 35.481. Efecto: restar 70.973 M baja el valor ≈ 9,5 dólares por acción. Los arrendamientos **operativos** (27.477) no se restan (el EBIT ya deduce el alquiler; criterio del usuario del 10-nov-2026) |
| Caja | 64.509 | Efectivo 20.281 + inversiones de corto plazo 44.228 |
| Activos no operativos | 37.808 | «Inversiones de capital y otras» a valor en libros; incluye la participación en OpenAI (método de participación). **No se valora a mercado** y la volatilidad de esas inversiones (−5.163 M en FY2025; +10.447 M en FY2026) queda fuera del EBIT |
| Minoritarios | 0 | Sin dato |
| Acciones | 7.504,195 M | 7.426,195 (portada del 10-Q, 22-oct-2026) + 78 M de acciones restringidas no devengadas (todas; conservador). Sin opciones |
| Impuesto efectivo / marginal | 19,68 % / 23 % | 34.955 / 177.586 LTM; marginal = federal 21 % + estatal neto (**mi estimación**) |
| Tasa libre · g terminal | 4,86 % · 4,0 % | FRED DGS10 6-nov-2026; regla |
| Beta | **1,28** (bottom-up) | Multinegocio EE. UU. por ingresos del 1T-FY27: «Agents and Infra» 76.795 → Software (System & Application) 1,248; «Devices and Consumer» 15.484 → Computers/Peripherals 1,325 (desapalancadas) → 1,256; apalancada 1,278. **Es alta frente a la beta observada de MSFT (≈1,0)**; con beta directa de 1,00 el costo de capital inicial sería 9,26 % y la Base 533,88 (+7,6 %) |
| ERP | 4,52 % | Regiones por ingresos de FY2026: Estados Unidos 170.794 (Norteamérica) y resto del mundo 161.045 (5,5 %); madura 3,387 % |
| Costo de la deuda | 5,20 % | Entrada directa: tasa libre + 0,34 puntos (**estimación mía**; MSFT tiene calificación AAA, no verificada aquí) |
| Costo de capital | **10,49 % inicial** · 8,25 % estable | Común a las tres historias; la deuda pesa 2,6 % |

## Historias (probabilidades 25 / 50 / 25; sin probabilidad de fracaso)
| Palanca | Conservadora | **Base** | Optimista |
|---|---|---|---|
| Crecimiento año 1 (B26) | 13 % | 18 % | 21 % |
| CAGR años 2–5 (B28) | 7 % | 14 % | 17 % |
| Margen ajustado año 1 → objetivo año 5 | 48,24 % → 40 % | 48,24 % → 46 % | 48,24 % → 49 % |
| Ventas/capital 1–5 · 6–10 | 0,55 · 0,90 | 0,80 · 1,20 | 1,10 · 1,50 |
| ROIC terminal | costo de capital (8,25 %) | 18 % | 26 % |
| Ingresos año 5 · año 10 (M) | 513.154 · 661.083 | 690.456 · 1.012.767 | 785.531 · 1.216.310 |
| Valor por acción | 232,38 | 496,21 | 676,08 |

**Evidencia (10-Q 1T-FY2027 y 10-K FY2026).** Ingresos del trimestre 92.279 M (+19 %); Azure +48 %; Microsoft Cloud 63.900 M (+30 %); obligaciones de desempeño pendientes (RPO) 683.000 M, de los cuales 677.000 M comerciales (+73 %), con duración media de 2,3 años; margen operativo del trimestre 49,8 % (45.915 M); flujo operativo 58.000 M (45.057 M); gasto de capital +20.000 M en el trimestre; plantilla −2 %. Por segmento: «Agents and Infra» 76.795 M (+25 %, margen operativo 52,8 %) y «Devices and Consumer» 15.484 M (−3 %, margen 34,6 %).
- **Tesis de la Base:** el crecimiento se desacelera de 19 % a 18 % y 14 % con el respaldo de la cartera contratada (RPO); el margen baja 2 puntos porque el mix se desplaza a Azure (el margen bruto de Microsoft Cloud ya bajó a 66 %) y porque la depreciación del gasto en IA sube. La reinversión es alta (ventas/capital 0,8): en FY2026 cada dólar nuevo de ingresos requirió ≈ 2 dólares de inversión neta (gasto de capital 115.948 M + 24.608 M en activos por arrendamientos financieros − D&A 39.000 M ≈ 101.600 M para +50.115 M de ingresos). Pasa a 1,2 cuando la capacidad instalada se llena.
- **Contraevidencia que sostiene la Conservadora:** capex sobre ingresos de 39 % (frente a 14 % en FY2023); «ingresos asignados a obligaciones pendientes» dependen de pocos clientes grandes (el 10-K advierte que socios estratégicos, algunos clientes significativos de Azure, pueden cambiar su consumo y que parte de la demanda es de OpenAI); la depreciación aún no ha llegado a su nivel pleno; ventas de Windows y dispositivos −22 %.
- **Optimista:** el RPO se convierte en ingresos al ritmo previsto (30 % en 12 meses), el margen se sostiene en 49 % y la capacidad se llena rápido.

### Pruebas de las tres preguntas
- **Posible:** ingresos del año 5 de 690.456 M (×2,0) y del año 10 de 1,01 billones (×2,9); participación de mercado **N/D**; el RPO de 683.000 M cubre ≈ 2 años de ingresos.
- **Plausible:** margen objetivo de 46 % frente a 47,1 % contable hoy (REVISAR a la baja si la depreciación sube más rápido); reinversión con ventas/capital 0,8 (la historia propia de 5 años dice 0,5–0,6 en FY2025–FY2026 y 1,5–2,5 antes). Juicio: **Con reserva**.
- **Probable:** 15 % anual compuesto a 5 años frente a +18 % en FY2026 y +19 % en el 1T-FY27; valor terminal = 72 % del valor operativo. Juicio: **Con reserva** (alta dependencia de la monetización de la inversión en IA y del valor terminal).

## Puntos críticos para R4–R6
1. **Precio por encima de la Base:** el mercado paga 16,0 % de crecimiento anual (años 1–5), o 49,1 % de margen objetivo, o un costo de capital de 9,37 %, frente a 15 %, 46 % y 10,49 % de la Base. La valoración es sensible sobre todo al costo de capital (beta) y a la reinversión.
2. **Beta bottom-up 1,28** (alta frente a ≈1,0 observada): decisión de método por la regla de beta multinegocio; con 1,00 la Base es 533,88 (sobre el precio). R6 debe decidir cuál es defendible.
3. **Arrendamientos financieros como deuda (70.973 M):** si se ignoran, sube el valor; si se restan pero el capex no los incluye, la reinversión de las historias debe reflejarlos (lo hace por ventas/capital, no por capex).
4. **OpenAI y demás inversiones (37.808 M) a valor en libros** y compromisos con OpenAI no cuantificados.
5. **Concentración del RPO** y dependencia de capacidad (centros de datos, energía, componentes).

## DCF inverso y sensibilidades (hoja `Sensibilidades DCF` del libro Base)
Matriz A (CAGR × margen objetivo): 366,18 a 667,33. Matriz B (costo de capital inicial × g): 413,32 a 600,90. El precio de 530,61 queda dentro de ambos rangos. Centros = DCF Base.

## Controles
| Control | Estado |
|---|---|
| Réplica local vs Google Sheets (tres historias) | APROBADO (496,21 / 232,38 / 676,08) |
| Costo de capital común; probabilidades 100 %; Cons ≤ Base ≤ Opt; costo de capital estable > g | APROBADO |
| Beta bottom-up (juicio de industrias) | APLICADA; sensible |
| Arrendamientos financieros como deuda; inversiones a valor en libros; 78 M acciones restringidas | SUPUESTOS declarados |
| Costo de la deuda y tasa marginal | ESTIMADOS |
| Motor original sin cambios | NO re-verificado |
| Auditoría económica independiente | **NO_EJECUTADA (R6)** |

## Siguiente paso exacto
R4: cargar 03 MÚLTIPLOS (`1m_mbps0ZIVzsDUNyz76UzPGhei5YLuWwnSffk10496o`) con los estados de H y los supuestos de la Base (con los arrendamientos financieros reclasificados a deuda), elegir múltiplos de salida y pesos, y conciliar `Resumen de valoraciones`.
