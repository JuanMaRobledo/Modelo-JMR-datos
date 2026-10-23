# NFLX · cierre cuantitativo de los cinco hallazgos JMR v6 (23-oct-2026)

**Estado de esta revisión:** DOCUMENTO DE EVIDENCIA Y COPIA DE VALORACIÓN ACTUALIZADA; **NO PUBLICACIÓN OFICIAL NUEVA**. Valor anterior publicado US$69,94. Valor revisado de la [copia Google Sheets](https://docs.google.com/spreadsheets/d/15QDfNDg_2TG90sFFFvUyeYvI6rL9-AwfwUHI7XmHgPQ/edit), DCF Base US$61,115425. La copia modifica solamente 11 entradas/ajustes de la calculadora de costo de capital y anotaciones de 3 conceptos, con todas las historias y sensibilidades recalculadas por fórmulas nativas. La copia sigue siendo un expediente candidato: no sustituye por sí misma registro JSON, HTML del análisis ni auditoría publicada en app.

## Identidad y fuentes

- Corte contable 30-sep-2026; precio histórico US$65,04 del 21-oct-2026; moneda USD, todas las cifras de estado financiero en millones de USD, acciones en millones; beta bottom-up global Entertainment de tabla de referencia y costo de deuda heredado US$/deuda de bonos. No se actualiza la cotización al 23-oct sin fuente homogénea.
- [Netflix SEC 10-Q 30-sep-2026](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm) notas 2 (ventas/regiones), 5 (leases), 10 (opciones/RSU), MD&A tecnología.
- [Netflix SEC 10-K 2025](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm) notas 2 y 10; plazo de opciones 4,79 años al 31-dic-2025.
- [Damodaran, publicación del 8-oct-2026, ERP a septiembre 30](https://aswathdamodaran.blogspot.com/2026/10/stock-prices-earnings-and-cashflows-ai.html?m=0): ERP **3,70% respecto a Treasury10Y 5,29%**, o **3,92% respecto al Rf USD 5,07% descontando spread USA 0,22 pp**. La hoja usa Rf USD 4,91%, obtenido al 21-oct-2026 descontando el mismo spread 0,22 pp del Treasury 5,13%; por coherencia la prima madura usada es **3,92%**, nunca 3,70%. El corte de tasa libre, la cotización y las ventas deben mantenerse fechados por separado.

## 1. Geografía / prima de riesgo / WACC — MATERIAL, CORREGIDO EN COPIA

**Ventas LTM septiembre 2026 = FY2025 + 9M2026 − 9M2025**. [Cifras primarias 10-Q y 10-K](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm).

| Región SEC | FY2025 | 9M2025 | 9M2026 | LTM | Peso |
|---|---:|---:|---:|---:|---:|
| UCAN | 19.957,152 | 14.617,882 | 16.305,180 | 21.644,450 | 43,52% |
| EMEA | 14.514,646 | 10.641,903 | 12.138,506 | 16.011,249 | 32,19% |
| LATAM | 5.357,521 | 3.939,582 | 4.683,951 | 6.101,890 | 12,27% |
| APAC | 5.353,717 | 3.932,907 | 4.556,234 | 5.977,044 | 12,02% |
| **Total** | 45.183,036 | 33.132,274 | 37.683,871 | **49.734,633** | 100% |

Los cuatro LTM suman exactamente 49.734,633 millones de USD, el total LTM del estado de resultados; las pequeñas variaciones de las tasas están por debajo del redondeo mostrado. La copia introduce APAC `H23`, LATAM `H26`, UCAN `H29`, EMEA `H31`; usa `B26 = Operating regions`. Las primas `I23/I26/I29/I31` se reexpresan como `3,92% + CRP por región` obtenida por diferencia contra el ERP maduro de la tabla anual, evitando mezclar maduro de octubre y enero. Los CRP de enero son un **proxy por región, no por país** (EMEA 1,64 pp); sus límites deberán considerarse en sensibilidad cuando se obtenga desglose país.

**Resultado directamente re-leído de la copia:**
- ERP geográfica total `K33=B28` = **5,1466404%** = madura ajustada 3,92% + CRP LTM 1,2266404 pp. El dato anterior B27=4,42% incluía una CRP arbitraria de solo 0,50 pp.
- Beta desapalancada 0,98207732; beta apalancada 1,02386203, modelo beta `Single Business(Global)` (Netflix reporta **un solo segmento operativo**); Ke **10,17945%**; deuda pre-tax 5,85%, tasa marginal 25%, pesos mercado patrimonio 94,63158% y deuda 5,36842% (suman 100%).
- `Cost of capital worksheet!B12=Detailed`; `B14=E63=Input sheet!B36` = **WACC 9,8685135%**. Con Rf B35 4,91% la prima de 3,92% sobre Rf ajustada evita descontar dos veces riesgo soberano.
- DCF Base anterior **US$69,94197**, nuevo **US$61,11543**, `ΔV=-US$8,82654 (-12,62%)`. La sensibilidad preliminar con ERP madura 3,70% y Rf ya ajustada fue DESCARTADA por incompatibilidad; no es el valor corregido.

| Historia | Valor por acción actualizado (USD) |
|---|---:|
| Conservadora | 40,116805 |
| Base | **61,115425** |
| Optimista | 80,280502 |
| Disrupción | 14,389163 |
| Promedio condicionado tres ordinarias | 58,425723 |
| Precio mecánico con MOS 35% (solo Base) | 39,725027 |

La copia regeneró automáticamente la sensibilidad de WACC × g (centro US$61,115425), y sus cuatro historias están LISTO. La revisión de 2026-10-22 sigue publicada; **no declarar el nuevo valor oficial** hasta integrar la copia, publicar JSON+análisis+auditoría de la misma revisión y correr el gate total.

## 2. Opciones y RSU — NO BLOQUEANTE PARA PLAZO ESTIMADO, SIN CAMBIAR EL VALOR EN LA COPIA

El 10-Q confirma 120.175.117 opciones; strike ponderado US$41,24; la vida restante de **4,50 años es hipótesis**, el plazo de 4,79 corresponde a diciembre 2025, no a septiembre 2026. Desviación de retornos 36,95909% tomada de la hoja. `Option value` se titula «dilution-adjusted», pero su fórmula visible `B18=B5` produce Black–Scholes **sin ajuste efectivo por dilución** y descuenta US$4.290,87 millones de `Valuation output!B32`, una sola vez. Acciones `B34=4.108,193664`M incluyen 1,867761M RSU/PSU no consolidadas, sumadas a 4.106,325903M emitidas y en circulación, sin multiplicar otra vez por opciones. La compensación SBC figura en EBIT GAAP.

Prueba independiente Black–Scholes con S=65,04, K=41,24, r=4,91%, σ=36,95909%, q=0, N=120,175117M, con otras entradas sin cambios:
- T=3,5: reclamación BS convencional US$4.019,85M; valor DCF **61,18140**.
- T=4,5: US$4.290,87M; valor DCF **61,11543**.
- T=4,79: US$4.364,13M; valor DCF **61,09759**.
- T=5,5: US$4.534,56M; valor DCF **61,05611**.
- Black–Scholes iterativo con dilución al T=4,5 aproxima reclamación US$4.199,00M (US$0,0224/acción menos que la convencional); peor variación absoluta entre combinaciones 3,5–5,5 y ajuste iterativo <**US$0,091/acción (0,15%)**.

Mantener convencional por ahora es prudente (reclamación mayor) y **su diferencia no es material**. Registrar el rótulo incorrecto como defecto de presentación a corregir en plantilla, sin afirmar que ya se corrigió; si cambia el pool real o el gasto SBC futuro, revisar.

## 3. Arrendamientos — TRATAMIENTO CONTABLE CONCILIADO, SIN CONVERSIÓN DUPLICADA

El 10-Q, nota 5, registra pasivos operativos US$2.252,237M (435,730 corrientes + 1.816,507 no corrientes) en «Accrued expenses» / «Other non-current liabilities», con activo ROU US$1.969,057M. El total de compromisos brutos en MD&A US$2.618,583M incluye pagos futuros con intereses imputados y posibles compromisos no reconocidos. Diferencia **US$366,346M**, cota bruta agregada de la porción adicional potencial; como piso los pagos no descontados que corresponden a pasivos ya reconocidos superan su VP, el VP de contratos no reconocidos no puede superar esa diferencia si no hay componentes netos atípicos. `366,346 / 4.108,193664 = US$0,0892/acción (0,146%)`, una **prueba de cota del puente de deuda**, no la diferencia exacta de un FCFF íntegramente reestructurado.

En el DCF actual `Input sheet!B18=No` significa **sin conversión incremental**: las rentas ya están en gastos GAAP y no se suma ni resta una segunda vez la deuda de arrendamientos. Esa política operativo/financiera es internamente consistente mientras el margen proyectado incluya las rentas; no afirma que Netflix no tenga leases. No aplicar mecánicamente `B18=Yes` a los US$2.252,237M sin revertir previamente las rentas en EBIT, reinversión y estructura de capital.

## 4. Tecnología e I+D — SENSIBILIDAD INMATERIAL PARA CONVENCIÓN DE 2–5 AÑOS, SIN INVENTAR I+D PURO

La cuenta SEC «Technology and development» es un agregado que incluye personal de mantenimiento, pruebas, interfaz, recomendaciones, infraestructura, instalaciones, equipos y software general. No acredita gasto íntegramente capitalizable. `Input sheet!B17=No` se mantiene por prudencia. `R& D converter!F7=3` de la copia está **solo habilitado para prueba 100% tecnología** (sin activar B17); arroja activo hipotético US$7.126,838M, amortización corriente US$2.997,481M y EBIT corregido US$893,332M en LTM. Es incorrecto presentar el activo como I+D puro reconocido.

Prueba de sensibilidad independiente, *no reproducida automáticamente como DCF secundario nativo de la hoja*, aplicando a cada uno de los diez FCFF los ajustes simultáneos `EBIT_adj=EBIT+I+D_nueva−amortización` y `reinversión_adj=reinversión+I+D_nueva−amortización`, con impuesto anual de cada año, I+D hipotética 100% de la partida actual como proporción de ventas, amortización lineal, año terminal calculado con igual regla, mismo WACC/g y puente. Por tanto `ΔFCFF_t = −tasa_impuesto_t × (I+D_nueva_t − amortización_t)` dentro de **esta convención de normalización**, NO cambio real de caja comprobado ni certificación del valor económico de tecnología.
- Vida 3 años, 100% capitalizada: `ΔV ≈ −US$0,539/acción (−0,88%)`.
- Vida 5 años, 100% capitalizada: `ΔV ≈ −US$0,808/acción (−1,32%)`.
- Menor fracción capitalizable reduce proporcionalmente ambos efectos, manteniendo ceteris paribus. Vida 10 años y cambios simultáneos en inversiones, márgenes o duración de la ventaja **no quedan acotados por esta prueba**.

La capitalización mecánica por sí sola no supera 2% bajo vidas plausibles (2–5 años) aun con supuesto extremo del 100% de tecnología. Debe **revisarse si el nuevo análisis modifica las historias, ROIC y Sales-to-Capital**: no usar la sensibilidad contable como certificación de los supuestos económicos.

## 5. Materialidad y dictamen de uso

| Tipo | Prueba/impacto | Resultado |
|---|---|---|
| ERP país/mercado | −US$8,82654/acción; −12,62% | **MATERIAL y corregida solo en copia** |
| Opciones: vida y fórmula | <US$0,091/acción (<0,15%) | Salvedad menor cuantificada |
| Compromisos de lease adicionales | <US$0,0892/acción (<0,15%) como puente de deuda | Salvedad menor condicionada |
| Capitalización I+D 100% tech a 3–5 años | −US$0,539 a −US$0,808 (<1,33%) | Sensibilidad limitada de presentación contable |
| **Suma conservadora de las tres últimas cotas** | **<US$0,989/acción, <1,62%** | Menor al umbral JMR3%; NO borra la salvedad económica sobre ROIC/reinversión |

**No confundir cierre de cinco partidas con certificación integral.** El ROIC terminal Base del 21,52% supera industria 11,04% y WACC revisado 9,87%, y los supuestos de Sales-to-Capital/contenido y múltiples siguen requiriendo la auditoría económica habitual. Antes de publicar: (1) ejecutar el validador DCF con la nueva copia, (2) regenerar todas las cifras JSON, descuentos de múltiplos/Ke y matrices de sensibilidad que dependan del WACC, (3) alinear artículo Nivel1+Nivel2 y auditoría a la misma nueva revisión, (4) ejecutar `controles_todas.sh NFLX` y comprobar el despliegue. Sin prueba verde no rotular `VERIFICADO` ni cambiar el registro oficial.

**Fuente única de la revisión propuesta:** copia https://docs.google.com/spreadsheets/d/15QDfNDg_2TG90sFFFvUyeYvI6rL9-AwfwUHI7XmHgPQ/edit · candidata JMR v6 del 23-oct-2026. El registro publicado y el artículo aún apuntan a la hoja anterior y a US$69,94, por diseño mientras el gate final esté pendiente.
