# META · Nivel 2 — calibración reproducible A-1.2 (NO oficial)

**Versión:** META-20261031-A12-R1 · **Corte:** 30-sep-2026 · **Precio referencia:** US$614,99 (30-oct-2026).  
**Unidad fija:** USD millones salvo valor por acción y porcentajes.  
**Estado:** simulación externa de contraste. La hoja oficial conserva `Escenarios e historias!K5:K8 = PENDIENTE`; no actualizar el catálogo, ni publicar precio intrínseco, ni clasificar como auditoría económica.

## 1. Fuentes e históricos
De la hoja financiera 2016–2025 y LTM 2026-09-30: ingresos FY2025 200.966; 9M2026 181.712; 9M2025 141.073; **ingresos LTM 241.605**. EBIT FY2025 83.276 + 9M2026 54.635 − 9M2025 58.531 = **79.380** GAAP. El conversor I+D a tres años calcula ajuste positivo al EBIT 32.422,67 y activo I+D no amortizado 125.558,67. **Margen EBIT inicial analítico**: `(79380 + 32422,6667) / 241605 = 46,27%`.

El reporte trimestral incluye un cargo extraordinario jurídico de 9.890. **No sumamos automáticamente 9.890 al EBIT inicial ya capitalizado**, pero usamos el gasto jurídico excepcional para explicar diferencias y evitar doble deducción. La simulación descuenta como **hipótesis máximamente precautoria** 18.590 de pasivo/reclamación jurídica en el puente de EV a equity; importe y tratamiento exactos deben conciliarse con el pasivo real y calendario de pagos.

## 2. Política de monedas y acciones
Todos los flujos, WACC y valor terminal están en USD nominales. El número de acciones `2.556,241253` millones proviene de la hoja histórica. No está ajustado todavía por la distribución futura de Clase C (efecto 2:1 cuando sea efectiva en 2027); tampoco se cambia el número de acciones por esa noticia en una valoración con corte 31-oct-2026. Dilución/RSU y valor de opciones requieren recaptura específica.

## 3. Ajustes y capital no operativo
El modelo puente provisional utiliza **deuda 116.026**, efectivo 82.449, participaciones no cotizadas **32.624 como proxy de valor contable**, reclamaciones hasta 18.590, y opción heredada 574,65. **Este proxy NO es «valor económico validado»**: en la hoja oficial `Input sheet!B20` se dejó vacío para evitar que apruebe un dato económico no certificado. Sigue faltando revisar el coste de opciones y la clasificación de leases.

## 4. WACC explicado
Coste de capital **detallado** en hoja: Treasury USD 10 años al 30-oct **4,94%** (frente a 5,29% al cierre de septiembre); ERP Damodaran octubre **3,70%**, beta apalancada **1,15** como supuesto analítico, coste de deuda antes de impuestos **6,0%** preliminar, tasa marginal **25,37%** y deuda valor de mercado modelado 75.394,22 vs patrimonio de mercado 1.572.062,81. WACC resultante de la fórmula de la hoja: **8,98%**. WACC de madurez **8,80%**, sometido a sensibilidad. El gate WACC de cálculo llegó a `VALIDADO` en Sheets, **sin que beta, coste de deuda o valoración final se consideren auditados económicamente**.

## 5. Impuestos y trayectoria
La tasa histórica LTM de 4,58% está distorsionada; para proyección se eligió **17% inicial**, coherente con guía de 4T26 de 15–17%, convergiendo linealmente a **25,37%** años 6–10. Este es un supuesto de normalización a discutir. Los años 1–5 tienen tasa de 17%; años 6–10 aumentan 1,674 puntos porcentuales por año hasta 25,37%.

## 6. Método de reinversión
Fórmulas explícitas: 
- `Ingresos[t] = Ingresos[t−1] × (1+g[t])`.
- `EBIT[t] = Ingresos[t] × margenEBIT[t]`.
- `NOPAT[t] = EBIT[t] × (1−tax[t])`.
- `Reinversión[t] = (Ingresos[t+1]−Ingresos[t]) / SalesToCapital[t]`, con un año de desfase como en el motor de la hoja.
- `FCFF[t] = NOPAT[t] − Reinversión[t]`.
- `DF[t] = producto_{i=1..t} 1/(1+WACC[i])`; `PV_FCFF[t] = FCFF[t] × DF[t]`.
- Terminal: `FCFF[t+1] = NOPAT[t+1] × (1−gTerminal/ROICterminal)`, `TV = FCFFterminal/(WACCterminal−gTerminal)`.

**Atención**: sales-to-capital es un método *sustitutivo* para proyectar la reinversión neta, no un cargo de CapEx que se pueda sumar después. La guía CapEx 2026 de 135–145 mil millones (incluye pagos principales de finance leases) será contraste externo de magnitud, no input automático duplicado.

## 7. Escenarios y probabilidad

| Historia | Prob. | CAGR 5 años | Margen terminal | S/C años 1–5 | S/C años 6–10 | ROIC terminal | g terminal | Valor/acc. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Base | 45,00% | 14,65% | 44,00% | 0,52 | 0,55 | 18,69% | 3,50% | US$780,63 |
| Conservadora | 22,50% | 9,16% | 38,50% | 0,43 | 0,50 | 14,80% | 3,00% | US$482,77 |
| Disrupción | 10,00% | 2,35% | 25,50% | 0,35 | 0,48 | 9,27% | 1,50% | US$244,06 |
| Optimista | 22,50% | 18,83% | 47,00% | 0,68 | 0,60 | 21,89% | 4,00% | US$1.152,39 |

La historia Disrupción se presenta separada y no entra en el promedio ponderado de las tres restantes. El promedio de Base/Conservador/Optimista es **US$799,11** por acción (ponderaciones 45%/22,5%/22,5% normalizadas por el 90% de tres historias). El DCF **Base principal** es US$780,63, con MOS35% US$507,41.

## 8. Proyección anual Base de diez años

| Año | Ventas | Crec. | Margen | NOPAT | Reinversión | FCFF | WACC | VP FCFF |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 289.926 | 20,00% | 46,27% | 111.355 | 94.783 | 16.572 | 8,98% | 15.207 |
| 2 | 339.213 | 17,00% | 45,36% | 127.724 | 94.588 | 33.135 | 8,98% | 27.900 |
| 3 | 388.399 | 14,50% | 44,91% | 144.777 | 89.631 | 55.146 | 8,98% | 42.608 |
| 4 | 435.007 | 12,00% | 44,45% | 160.507 | 83.655 | 76.852 | 8,98% | 54.486 |
| 5 | 478.508 | 10,00% | 44,00% | 174.751 | 78.218 | 96.533 | 8,98% | 62.800 |
| 6 | 519.181 | 8,50% | 44,00% | 185.781 | 70.797 | 114.983 | 8,94% | 68.662 |
| 7 | 558.120 | 7,50% | 44,00% | 195.604 | 65.960 | 129.644 | 8,91% | 71.085 |
| 8 | 594.398 | 6,50% | 44,00% | 203.940 | 59.440 | 144.500 | 8,87% | 72.774 |
| 9 | 627.089 | 5,50% | 44,00% | 210.538 | 51.307 | 159.230 | 8,84% | 73.682 |
| 10 | 655.308 | 4,50% | 44,00% | 215.185 | 41.701 | 173.484 | 8,80% | 73.785 |

## 9. Conciliación de valor Base
- VP FCFF años 1–10: **US$562.989 millones**.
- VP terminal: **US$1.452.608 millones**; proporción del EV operativo: **72,07%**.
- EV operativo: **US$2.015.597 millones**.
- Equity candidato: EV − deuda − reclamación − opciones + caja + participaciones contables = **US$1.995.479 millones**.
- Per share / MOS35: **US$780,63 / US$507,41**.

## 10. Sensibilidad intrínseca (no anclas de múltiplos)
Se guardaron dos matrices 5×5 calculadas de forma independiente: **WACC inicial+terminal × g terminal** y **WACC inicial+terminal × ROIC terminal**. La celda central (fila 3, columna 3) es **US$780,63** y concilia con el DCF Base. Cambiar el WACC a la vez en la etapa explícita y terminal conserva la forma del descuento y es más honesto que cambiar solo el denominador de perpetuidad.

## 11. Múltiplos y AZ Stocks
No se extrajeron ni certificaron aún precios FY+3 ni valores presentes por EV/EBITDA, EV/FCFF, P/E, P/FCFE y P/OCF. P/S y P/BV permanecen secundarios con justificación o N/A. **Las matrices 5×5 anteriores son DCF, no sensitividades de múltiplos**. Se realizará una valoración AZ Stocks separada; no sustituye el DCF principal.

## 12. Salvedades y gates por cerrar
1. **Deuda/leases:** valor libro 116.026 y deuda a mercado calculada 75.394 requieren prueba de consolidación entre Notes y obligaciones de arrendamiento.
2. **Litigio:** cuánto del compromiso total 18.590 está provisionado, calendario y tratamiento del gasto 9.890 ya reconocido.
3. **Participaciones:** 32.624 es valor contable, no valor económico validado. El campo oficial B20 está vacío, control de inversiones pendiente.
4. **Opciones/dilución:** existe SBC y futura Clase C; falta cotejo de premios y opciones, precio de ejercicio, plazo, volatilidad y doble cuenta.
5. **Ciclo de CapEx:** conciliar reinversión calculada con guía CapEx 2026 y compromisos futuros sin contabilizar dos veces obligaciones aún no iniciadas.
6. **Pruebas:** la hoja oficial no ha habilitado historias con `LISTO`, el DCF es independiente y no certifica el exportador ni las matrices de múltiplos; el gate de datos global PR #211 permanece bloqueado.

**Fuentes:** [Resultados 3T 2026 Meta](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/); [10-Q](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930_htm.xml); [10Y Treasury](https://ploveranalytics.com/us-treasury.html); [Damodaran](https://aswathdamodaran.blogspot.com/2026/10); [hoja de trabajo](https://docs.google.com/spreadsheets/d/1lpE-L0Ai2NrWDhzBhtdeOMASwo7XRleUEMEMl3K34ss/edit).
