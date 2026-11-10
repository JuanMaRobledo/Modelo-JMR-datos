# CMG-REBOOT-3T26-R1 · Fase R3 (historias y DCF)

- **Fecha:** 2026-11-10 · **Agente:** Claude (Code, nube): Sheets, SEC (10-K FY2025 y 10-Q 3T-2026), LibreOffice (recálculo local del motor).
- **Libros:** DCF Base `1asO4BR42MypptINAooJ3hP6joY5fFUYDB5IM2NSDo7U` · Conservadora `1i5Sc_uoJX6cnvq9wDjr4jP0XtMIE5c1vtlDDEBfz_qU` · Optimista `1hSctlkSB4-mUMZPxwtnGpKLWaH8Bn_Ymzhdowh6mpzQ`. Estado **CANDIDATO** (R4 pendiente; sin R6).
- **Motor:** fcffsimpleginzu original. Se cargaron entradas en `Input sheet`, `Cost of capital worksheet` y `Country equity risk premiums!B1` (3,387 %). Para activar las opciones se habilitó el cálculo iterativo en los tres libros y se aplicó el arreglo de Damodaran a `Option value!B17` (escribir un número y restaurar la fórmula). **No se re-verificaron una a una las 1.230 fórmulas y 76 comentarios** (en AAPL sí se hizo; aquí queda pendiente para R6).

## Resultado
| | Conservadora | **Base** | Optimista | Esperado (25/50/25) |
|---|---|---|---|---|
| Valor por acción | 17,69 | **32,28** | 40,47 | 30,68 |
| Frente al precio (34,43, 6-nov-2026) | −48,6 % | **−6,2 %** | +17,5 % | −10,9 % |

**Precio con MOS 35 % = 0,65 × 32,28 = 20,98 USD** (solo sobre la Base). El precio está 6,7 % por encima del DCF Base y por debajo de la Optimista. Conservadora ≤ Base ≤ Optimista: cumple. Réplica local (LibreOffice sobre el xlsx original) = Google Sheets: 17,6858 / 32,2837 / 40,4675 (diferencia < 1e-4).

## Entradas comunes
| Entrada | Valor | Fuente / criterio |
|---|---|---|
| Ingresos LTM · EBIT LTM | 12.713,5 · 1.794,9 | H (XBRL): FY2025 + 9M-2026 − 9M-2025 |
| Año anterior (10-K FY2025) | 11.925,6 · 1.935,8 | H |
| Patrimonio · deuda | 2.455,1 · **0** | Los arrendamientos (5.599) **no se restan como deuda**: decisión del usuario, el EBIT ya deduce el alquiler |
| Caja e inversiones CP | 902,6 | Efectivo 634,2 + inversiones CP 268,4 |
| Activos no operativos | 100,4 | Inversiones LP |
| Acciones | 1.270,149 | 1.264,975 de la portada del 10-Q + 4,138 RSU + 1,036 PSU esperadas |
| Opciones (SOSARs) | 12,268 M a 39,51 · vencimiento 4,2 años · volatilidad 35 % | 10-Q 3T-2026 Nota 7; **volatilidad supuesto mío (35 %)**, no medida |
| Valor de las opciones | 126,7 M (Black-Scholes con dilución) | `Option value` |
| Precio | 34,43 | cierre 2026-11-06 |
| Impuesto efectivo / marginal | 24,74 % / 25 % | 452,7 / 1.829,8 LTM |
| Tasa libre · crecimiento terminal | 4,86 % · 4,0 % | FRED DGS10; regla (techo = Rf) |
| ERP | 3,603 % inicial (Norteamérica) · 3,387 % madura | Damodaran nov-2026; 100 % de los ingresos en EE. UU. |
| Beta | 0,783 (industria Restaurant/Dining; sin deuda) | tabla de Damodaran del motor (enero 2026) |
| Costo de capital | **7,68 % inicial** · 8,25 % estable | Ke = WACC; el inicial queda **por debajo** del estable porque la beta es < 1 |
| Costo de la deuda | 5,86 % (entrada directa) | Irrelevante: el peso de la deuda es 0 |

## Historias (punto de partida: la revisión Floyd; modificaciones declaradas)
**Tipo: crecimiento maduro**; probabilidades 50 / 25 / 25. Sin fracaso en ninguna historia: no hay deuda ni riesgo financiero (la desventaja está en los márgenes y no en la solvencia).
| Palanca | Conservadora | **Base** | Optimista |
|---|---|---|---|
| Crecimiento año 1 (B26) | 6,4 % | 9,5 % | 11,0 % |
| CAGR años 2–5 (B28) | 6,4 % | 8,8 % | 10,9 % |
| Margen año 1 (B27) | 14,12 % (actual) | 14,12 % | 14,12 % |
| Margen objetivo año 5 (B29) | 13,0 % | 16,0 % | 18,0 % |
| Ventas/capital 1–5 · 6–10 | 2,2 · 2,4 | 2,7 · 2,9 | 2,9 · 3,2 |
| ROIC terminal (B48–B49) | costo de capital (8,25 %) | 18,36 % | 18,36 % |
| Valor por acción | 17,69 | 32,28 | 40,47 |

Los parámetros de crecimiento, margen y ventas/capital son los de la historia Floyd (CAGR 6,4 / 8,9 / 10,9 %; márgenes 13 / 16 / 18 %; s2c 2,2–2,4 / 2,7–2,9 / 2,9–3,2). **Cambios frente a Floyd:** (1) el crecimiento del año 1 y el CAGR 2–5 se separan en dos entradas porque el motor original no admite trayectoria anual libre (Floyd usaba una trayectoria por unidades); (2) **ROIC terminal por la regla del contrato**: ventaja durable = promedio de la industria (Restaurant/Dining, 18,36 %) en Base y Optimista, y costo de capital en la Conservadora, en lugar de 22 / 28 / 15 % de Floyd; (3) tasa libre 4,86 % (Floyd 4,94 %) y prima regional 3,603 %; (4) sin deuda por arrendamientos (igual que Floyd). Efecto neto en la Base: 32,28 frente a 33,04 de Floyd.

### Pruebas de las tres preguntas (señales de `Diagnostics`; el juicio es mío)
- **Posible:** ingresos del año 10 de 25.996 M frente a 12.713 M hoy (×2,0). El TAM de comida rápida informal no está verificado con fuente primaria: **N/D**. La expansión se apoya en unidades (≈ 4.300 restaurantes propios), dato del 10-Q no verificado aquí.
- **Plausible:** margen objetivo Base 16,0 % frente a 15,8 % de la industria y 16,9 % de CMG en FY2024; margen LTM 14,1 % (baja de 2,8 puntos desde FY2024). ROIC del año base 87 % (capital invertido sin arrendamientos: 1.553 M) frente a 52,9 % en el año 10 y 18,36 % terminal: la eficiencia transitoria no se perpetúa. Ventas/capital 2,7 frente a 8,2 actual: la Base asume reinvertir mucho más capital por dólar de ventas que hoy. Juicio: **Con reserva** (margen y capital invertido).
- **Probable:** CAGR 8,8–9,5 % frente a 13,9 % de la industria a cinco años, 14,6 % de CMG en FY2024 y 6,6 % LTM. Valor de los 10 años: 30 % del total; terminal 70 %. Juicio: **Sí**, con la caída del 2026 como alerta.

## DCF inverso y sensibilidades (hoja `Sensibilidades DCF` del libro Base)
Corridas del motor original recalculado localmente (centro de las matrices = Base).
- Para que el valor sea 34,43 hace falta, una variable a la vez: **crecimiento de 10,19 %** en los años 1–5 (frente a 8,8–9,5 %), o **margen objetivo de 17,08 %** (frente a 16,0 %), o **7,93 % de crecimiento con 18 % de margen**, o **costo de capital inicial de 6,58 %** (frente a 7,68 %).
- Matriz A (CAGR × margen): 26,12 a 39,51. Matriz B (costo de capital inicial × g terminal): 27,08 a 38,87. El precio queda dentro de ambos rangos: **CMG cotiza cerca del DCF Base**, a diferencia de AAPL.

## Controles
| Control | Estado |
|---|---|
| Réplica local vs Google Sheets (tres historias) | APROBADO (< 1e-4) |
| Costo de capital común (7,68 % inicial; 8,25 % estable) | APROBADO |
| Probabilidades = 100 %; Cons ≤ Base ≤ Opt; WACC estable > g | APROBADO |
| MOS 35 % solo sobre la Base | APROBADO |
| Motor original sin cambios (1.230 fórmulas, 76 comentarios) | **NO re-verificado** |
| Opciones: cálculo iterativo habilitado y `Option value!B17` restaurado como fórmula | APROBADO (valor 126,68 = réplica) |
| Volatilidad de las opciones 35 % | SUPUESTO (no medida) |
| Beta de la industria con datos de enero 2026 (0,783); Floyd usó 0,86 | PARCIAL: sensibilidad alta (un punto menos de costo de capital llega al precio) |
| «Otros ajustes» del flujo LTM (804 M) heredado de R2 | PENDIENTE (no afecta el DCF) |
| Auditoría económica independiente | **NO_EJECUTADA (R6)** |

## Siguiente paso exacto
R4: cargar en 03 MÚLTIPLOS (`1jdUkjDwPG79FmSGLbZfQd-xTXMVBC8xJ9wG2imACeK0`) los estados de H y los supuestos de la Base, elegir múltiplos de salida y pesos (tipo «Madura»), conciliar con los tres DCF por script con SHA-256 y completar `Presentación` y `Resumen de valoraciones` del libro Base.
