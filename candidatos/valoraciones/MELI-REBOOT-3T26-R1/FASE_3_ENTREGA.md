# MELI-REBOOT-3T26-R1 · Fase R3 (historias y DCF)

- **Fecha:** 2026-11-10 · **Agente:** Claude (Code, nube): Sheets, SEC (10-K FY2025 y 10-Q 3T-2026), LibreOffice (recálculo local del motor). Estado **CANDIDATO** (sin R4–R6).
- **Libros:** DCF Base `174iyMLVgEsIw8sAWHNF3_SAvcbOoZbb1dB94gUF5yLc` (con hoja nueva `Sensibilidades DCF`) · Conservadora `1RYE2kFcPstfBAH2eTRkyiMwvw64XuOcgnofD9Jq8jPM` · Optimista `1fdZBeu5c4Agd54piuip2jnLL8HxM2yUbGOkGUKjgjd4`.
- **Motor:** fcffsimpleginzu original; solo se escribieron celdas de entrada (`Input sheet`, `Cost of capital worksheet`, `R& D converter`, `Country equity risk premiums!B1`). **Integridad de fórmulas y comentarios no re-verificada** en estas copias (copia directa de plantilla).

## Resultado
| | Conservadora | **Base** | Optimista | Esperado (25/50/25) |
|---|---|---|---|---|
| Valor por acción | 908,33 | **2.536,95** | 4.120,94 | 2.525,79 |
| Frente al precio (1.510,00 · 6-nov-2026) | −39,8 % | **+68,0 %** | +172,9 % | +67,3 % |

**Precio con MOS 35 % = 0,65 × 2.536,95 = 1.649,02 USD**: el precio de mercado queda **por debajo** del precio con MOS (en zona de compra según la regla). Réplica local = Google Sheets en las tres historias (2.536,95 / 908,33 / 4.120,94). **Advertencia:** el rango es muy amplio y el resultado depende de supuestos que el historial no prueba (ver «Puntos críticos»).

## Entradas comunes
| Entrada | Valor | Fuente / criterio |
|---|---|---|
| Ingresos LTM · EBIT LTM | 38.523 · 2.859 (7,4 %) | H (XBRL): FY2025 + 9M-2026 − 9M-2025; verificado con el 10-Q |
| Año anterior (FY2025) | 28.893 · 3.201 | 10-K |
| I+D capitalizada | Sí, 3 años | «Desarrollo de producto y tecnología» LTM 2.757; FY2025 2.269; FY2024 1.934; FY2023 1.831 → EBIT ajustado 3.605, margen 9,36 % |
| Patrimonio | 8.200 | Balance 30-sep-2026 |
| **Deuda** | **2.369** | **Solo deuda corporativa y de comercio**: notas 2031 / 2033 / 2036 (537 + 742 + 974) y arrendamientos financieros 116. Los demás «préstamos y obligaciones financieras» (≈10.800: bancos, bills y certificados de depósito, deuda colateralizada, notas comerciales) **fondean la cartera de crédito y su costo ya está en el EBIT**, de modo que se tratan como capital de trabajo operativo (lo mismo hace MELI en su «flujo libre ajustado»). **Cambia lo acordado en R1 (restarlos como deuda): se evita contar dos veces el costo de fondeo.** Estimación mía para R6: el XBRL no separa con certeza el fondeo corporativo del fintech |
| Caja | 8.126 | «Efectivo, inversiones y activos digitales disponibles» según MELI (10-Q, MD&A); excluye efectivo restringido (14.559) y los fondos de clientes (17.400 por pagar), que no son caja corporativa |
| Activos no operativos · minoritarios | 0 · 0 | Sin dato separable (incluidos en la caja disponible); MELI no tiene participaciones no controladoras |
| Acciones · opciones | 50,696802 M · No | Portada del 10-Q. El plan de retención LTRP se liquida en efectivo (ya está en el gasto); sin opciones ni RSU en acciones |
| Impuesto efectivo / marginal | 26,46 % / 32 % | LTM (680 / 2.570); marginal = promedio por país (Brasil 34 %, México 30 %, Argentina 35 %, otros ≈ 25–27 %) |
| Tasa libre · g terminal | 4,86 % · 4,0 % | FRED DGS10 6-nov-2026; regla |
| Beta | **0,93** (bottom-up) | Multinegocio global por ingresos de 9M-2026: comercio 16.771 → Retail (General) 0,937; fintech 12.993 → Information Services 0,874. **El mapeo de industrias es juicio mío**: Damodaran no tiene una industria para fintech de crédito; «Financial Svcs. (Non-bank)» (0,295) no es comparable por su apalancamiento |
| ERP | 7,56 % | Por país (ingresos 9M-2026): Brasil 16.305 (6,63 %), México 6.742 (5,85 %), Argentina 5.355 (13,10 %), otros 1.362 repartidos entre Chile, Colombia, Uruguay y Perú (**reparto supuesto, inmaterial**); madura 3,387 % |
| Costo de la deuda | 6,90 % | Entrada directa: tasa libre + ≈2,0 puntos (**estimación mía**; no verifiqué la calificación) |
| Costo de capital | **11,67 % inicial** (Ke = 11,67 %; la deuda pesa 3 %) · 8,25 % estable | Común a las tres historias |

## Historias
Probabilidades **25 / 50 / 25**; sin probabilidad de fracaso (cobertura de intereses alta y sin deuda corporativa significativa; el riesgo de crédito está en el margen, no en la supervivencia).
| Palanca | Conservadora | **Base** | Optimista |
|---|---|---|---|
| Crecimiento año 1 (B26) | 22 % | 30 % | 36 % |
| CAGR años 2–5 (B28) | 11 % | 19 % | 23 % |
| CAGR 5 años resultante | ≈13 % | ≈21 % | ≈25 % |
| Margen año 1 → objetivo año 5 (ajustado por I+D) | 9,36 % → 9,0 % | 9,36 % → 13,5 % | 9,36 % → 16,5 % |
| Ventas/capital 1–5 · 6–10 | 2,5 · 2,3 | 3,2 · 3,0 | 3,8 · 3,4 |
| ROIC terminal | costo de capital (8,25 %) | 14,0 % | 16,4 % |
| Ingresos año 5 · año 10 (M) | 71.346 · 99.050 | 100.427 · 161.138 | 119.917 · 206.385 |
| Valor por acción | 908,33 | 2.536,95 | 4.120,94 |

**Mecanismo y evidencia (10-Q 3T-2026).** Los ingresos crecen +48 % en nueve meses (+45 % en el trimestre) con volumen de pagos +53 % (296.939 M en nueve meses), mercancía bruta +38 %, compradores únicos +22 % (94 M en el trimestre) y usuarios activos de fintech +29 % (93 M). El crédito crece por encima de ambos (préstamos netos 12.451 + 589; tarjetas 9.055 + 145). El motor del valor es la monetización de Mercado Pago (pagos, cuentas, tarjetas y préstamos) sobre una base de compradores en Brasil, México y Argentina.
- **Contraevidencia que sostiene la Conservadora:** el EBIT cayó 15 % en nueve meses (1.970 frente a 2.312) con ingresos +48 %: la provisión para incobrables pasó de 2.108 a 3.862 (de 10,5 % a 13,0 % de los ingresos), el costo de ingresos subió de 54,9 % a 58,3 % (envíos, costo de mercancía propia, costos de fondeo y comisiones) y el margen del trimestre es 6,3 % (frente a 9,8 %). La NIMAL (margen de interés neto después de pérdidas) baja de 22,0 % a 19,7 %. Hay umbral de envío gratis reducido en Brasil, más ventas de primera mano (menor margen) y competencia de Shopee, Amazon y Temu (no verificada con fuente primaria). Argentina (18 % de los ingresos) vive con inflación y devaluación.
- **Base:** crecimiento que se desacelera de +48 % a 30 % y 19 % anual; margen ajustado que se recupera de 9,4 % a 13,5 % (≈ margen operativo contable de 11,6 %, el nivel de FY2025; FY2023 fue 14,6 %) porque la provisión se estabiliza y el apalancamiento de logística y publicidad compensa el costo de fondeo. ROIC terminal 14 % (punto medio entre el costo de capital y el promedio ponderado de las industrias de comercio y servicios de información ≈ 16,4 %): ventaja que se desvanece.
- **Optimista:** margen ajustado de 16,5 %, por encima del máximo histórico (FY2023: 14,6 % contable), con crecimiento sostenido de 23 % y ROIC terminal de industria (16,4 %).
- **Conservadora:** el margen no se recupera (9 %), el crecimiento cae a un dígito alto y no hay ventaja en el terminal.

### Pruebas de las tres preguntas
- **Posible:** ingresos del año 5 de 100.427 M en la Base (×2,6 en cinco años) frente a ×7,3 entre FY2020 y FY2025 (3.974 → 28.893 M); participación de mercado **N/D** (sin TAM verificado).
- **Plausible:** margen objetivo ajustado de 13,5 % frente a 9,4 % hoy y 11,1 % contable en FY2025: **REVISAR**. La reinversión de la Base (ventas/capital 3,2) implica ≈ 37 centavos de capital por dólar nuevo de ventas, con un capital invertido del año base de solo ≈6.100 (el fondeo del crédito es pasivo operativo), y un ROIC contable de 36 % → 43 %: **alto y frágil**. Juicio: **Con reserva**.
- **Probable:** 21 % anual a cinco años frente a +48 % LTM y +39 % en FY2025; valor terminal = 77 % del valor operativo. Juicio: **Con reserva**.

## Puntos críticos para R4–R6
1. **El precio queda por debajo de todas las celdas de las dos matrices** (mínimo 1.673,69, con 15 % de crecimiento y 10,5 % de margen). Para igualar 1.510 harían falta 9,6 % de crecimiento anual, o un margen ajustado de 8,4 %, o un costo de capital inicial de 21,2 %. Es una lectura de que el mercado descuenta un deterioro del crédito mayor que el de nuestras tres historias. **No lo tomo como prueba de que la acción esté barata: lo más probable es que mis supuestos de margen y reinversión sean favorables** (el margen cayó en los dos últimos años y la provisión no ha tocado techo). R6 debe cuestionar sobre todo margen, ventas/capital y beta.
2. **Tratamiento del fondeo del crédito.** Es la decisión que más mueve el valor y cambió frente a R1 (ver «Deuda»). Si en cambio se restara todo como deuda (≈ 13.200 frente a 2.369), el valor del patrimonio bajaría ≈ 10.800 M (≈ 213 por acción) **sin** devolver el costo de fondeo al EBIT: sería una doble cuenta, no una alternativa válida.
3. **Beta y mapeo de industrias.** Con beta directa de 1,30 el costo de capital inicial sube a 14,39 % y el DCF Base baja a 2.289,61. Con 1,20 (como UBER) el costo de capital inicial sería 13,66 % y el DCF Base 2.263,92.
4. **Costo de capital moderado para una empresa con 18 % de ingresos en Argentina y 55 % en Brasil**; la ERP ponderada (7,56 %) ya lo recoge, pero sin riesgo de convertibilidad ni de crédito soberano adicional.
5. **Moneda:** todo en dólares con tasa libre de dólares; las cifras de Argentina se convierten a un tipo de cambio que se devalúa. Sin ajuste adicional.

## DCF inverso y sensibilidades (hoja `Sensibilidades DCF` del libro Base)
Matriz A (CAGR × margen objetivo): 1.673,69 a 3.698,19. Matriz B (costo de capital inicial × g): 2.155,93 a 3.012,43. Centros = DCF Base (diferencia 0,01 por redondeo del texto del control).

## Controles
| Control | Estado |
|---|---|
| Réplica local vs Google Sheets (tres historias) | APROBADO |
| Costo de capital común; probabilidades 100 %; Cons ≤ Base ≤ Opt; costo de capital estable > g | APROBADO |
| Beta bottom-up (juicio de industrias) | APLICADA; **sensible** |
| Deuda corporativa 2.369 y fondeo del crédito como pasivo operativo | SUPUESTO declarado (cambia lo acordado en R1) |
| Caja disponible 8.126 (definición de MELI) y exclusión de fondos de clientes | SUPUESTO declarado |
| Costo de la deuda y reparto de «otros países» | ESTIMADOS |
| Motor original sin cambios | NO re-verificado |
| Auditoría económica independiente | **NO_EJECUTADA (R6)** |

## Siguiente paso exacto
R4: cargar 03 MÚLTIPLOS (`19jUYjQ-KXnLUjvQBXzTJhIRHJgxN79BdOfoqdB7REJk`) con los estados de H y los supuestos de la Base, elegir múltiplos de salida y pesos (la fintech de crédito vuelve poco fiables P/OCF y P/FCFE), y conciliar `Resumen de valoraciones`.
