> **REVISIÓN DE CALIDAD POSTERIOR — 2 NOV 2026.** La etiqueta anterior «CERRADA CON CONTROLES PENDIENTES / apta para fase 2» se limitaba a la posibilidad de continuar la investigación como CANDIDATO, **no acreditó datos completos**. Ante la revisión directa de los 46 módulos y estados, se identificaron vacíos de desagregación, un puente EV–equity no resuelto y un **bug material de signo en impuestos de Financials Multiples**. Ver [AUDITORIA_COBERTURA_DATOS.md](AUDITORIA_COBERTURA_DATOS.md) e [issue JMR-valuation #194](https://github.com/JuanMaRobledo/JMR-valuation/issues/194). **Fase 1 NO RECERTIFICADA; los múltiplos P/E, P/FCFE y EV no deben marcarse verificados; PR sigue en borrador.**

# AMZN · AMZN-20261102-A12-R4 · FASE 1 — CERRADA CON CONTROLES PENDIENTES
**Actualización final de esta fase: 2026-11-02. Estado: APTO PARA EMPEZAR FASE 2 EN CANDIDATO, no certificada ni publicable.**
**Herramienta:** ChatGPT GPT-6 (esfuerzo alto), Google Sheets / GitHub, SEC web; identificador de hoja: `10qfoGrEP1PgdlLWrHvfoHqExKDZbPK75yb_oINlO4a8`.
**Aislamiento:** R4 exclusiva. R2/R3 archivadas y no utilizadas como fuentes.
**Corte:** 30-oct-2026 precio US$240,35, Treasury 10Y 4,94%; últimos estados al 30-sep-2026. Datos en USD millones, acciones millones post-split 20:1.

## Dictamen operativo y puerta exacta
**HABILITADA a Fase 2 (valoración como CANDIDATO), con obligaciones de corregir/corroborar antes de usar cada salida y antes de Fase 3.** Las cifras materiales de ventas, resultados, EBITDA, CFO, capex, deuda reconocida y balance son reproducibles con fuentes primarias y fórmulas. No se generó ni publicó DCF, MOS, múltiples EV ni JSON certificado. Las tareas de modelización (I+D, inversiones Anthropic/OpenAI, WACC, reinversión, NCI y SBC) son propias de Fase 2, NO se han declarado resueltas.

## Matriz de controles efectivamente realizados
| Requisito | Resultado comprobado | Estado |
|---|---|---|
| Emisor/CIK/fiscal/moneda | Amazon.com Inc, Nasdaq AMZN, CIK 0001018724, FY 31 diciembre, USD | OK |
| Aislamiento y plantilla | R4 copia de plantilla IA, **46 pestañas**; sin fuentes de R2/R3 | OK |
| Estados históricos | 2016–2025, diez ejercicios de P&L, balance y CF, con notas en celdas; apertura 2015 | OK CON RESERVAS DE CLASIFICACIÓN |
| LTM 30-sep-2026 | P&L LTM con **15 fórmulas añadidas** (FY2025 + 9M2026 - 9M2025; acciones ponderadas pro rata 9/12), flujos LTM publicados directamente, balance spot sep2026, apertura sep2025 | OK |
| Verificación contable directa | 10/10 EBIT FY2016–25 conciliados; 11/11 CFO y CFI (incl. LTM) conciliados; 11/11 balances 2016–25+sep2026: activos corrientes, activos totales, pasivos corrientes y pasivo+patrimonio = 0 de diferencia en USD M | APROBADO EQUIVALENTE PARCIAL |
| Conservación de fórmulas | Comparación programática **5.357 fórmulas coincidentes**, 0 desaparecidas, 0 modificadas, en 46 pestañas: 14 pestañas A1:L80 y las otras 32 A1:L120. Excepciones: exactamente 15 fórmulas NUEVAS (Income Statement columna L). No es `diff_formulas_plantilla.py` de todo el libro | APROBADO EQUIVALENTE ACOTADO |
| Precios de cierre por año | Trailing Valuation!B3:K3, cierre FY2016–25, USD split-adjusted; 2026 L3 cierre 30-oct-2026 | OK FUENTE EXTERNA FECHADA |
| ROIC/ROE/ROA/trading | Fórmulas originales preservadas. Tras desagregar obligaciones 2023/24, ROIC FY2024 19,70%, FY2025 16,26%, LTM 13,26% observados en la hoja; ROA LTM 13,67%, ROE LTM 27,42% **GAAP** afectados por ingresos no operativos | OK TÉCNICO; INTERPRETACIÓN F2 |
| Ceros/reclasificación | I+D no separada (dentro de tecnología/infrastructure); D&A CF no expensa separada en EBIT; deuda/leases 2023–26 desagregados desde notas 10-K/10-Q, con recorte equivalente de accrued. Preferentes **0** por balance que dice no emitidas. En otros años, sin soporte de desglose no se inventaron ceros | PARCIAL EVIDENCIADO |
| Corte de tasas | Treasury 30-oct-2026 4,94% en Input B35. Damodaran ERP 1-oct-2026 4,20% (Rf original al 30-sep 5,29%): no trasladar 4,20 y 4,94 a un WACC como si fueran medidas simultáneas sin tratamiento temporal y sensibilidad | F2 PENDIENTE DE CIERRE |
| 8-K / actualizaciones | Inventario de 15 formularios 8-K en 2026 hasta 30-oct, entre ellos 29-oct resultados, emisiones de deuda y contratos; varios materiales contrastados con 10-Q y SEC 8-K, no se afirma auditoría completa de los 15 cuerpos | INVENTARIO OK; LECTURA EXHAUSTIVA PENDIENTE |
| Controles oficiales del motor | `estados_completos.py`, `auditar_estados_sec.py`, `auditar_ceros_materiales.py`, `diff_formulas_plantilla.py`, `inputs_completos.py`, `candados.py` | **NO EJECUTADO**: no hay sesión con credenciales/runtime del motor para correrlos contra la hoja; la revisión directa no reemplaza gates |
| Entrega a siguiente agente | Hoja R4 y esta documentación con datos originales, advertencias de normalización y fuentes fechadas | OK |

## Datos verificables clave y excepciones económicas
- **FY2025:** ventas 716.924, EBIT 79.975, CFO 139.514, capex en caja 131.819 (USD M).
- **LTM sep2026:** ingresos **797.455**, EBIT **104.366**, CFO **168.300**, capex de caja **215.192**, FCF fórmula CFO − capex **−46.892**, ajuste por incentivos de propiedad y equipo **4.535**, FCF neto incentivos **−42.357** (USD M). LTM net income contable **134.779** incluye beneficios financieros extraordinarios y NO debe usarse como utilidad recurrente.
- **Deuda y arrendamientos a sep2026:** LT debt 173.125, corriente debt 6.827, leases largo 98.824 y corriente 15.959 (USD M), total reconocido de 294.735. Finanzas de infraestructura de corto/largo plazo y otros pasivos de financiamiento deben evaluarse en Fase 2 sin doble conteo.
- **Mercado:** precio 240,35 USD; acciones 10.811 M (balance sep2026); market cap fórmula **2.598.423,85 USD M**. No se calculó EV oficial porque NCI e inversiones no operativas requieren comprobación.
- **P/E LTM visible de 19,43x es DISTORSIONADO** por Anthropic y otras partidas a valor razonable; EV/FCFF LTM puede no ser económico por FCFF negativo. Es obligación de Fase 2 normalizar y decidir N/A o escenarios, no calcular mecánicamente.
- **Capital I+D:** Technology and Infrastructure mezcla investigación, gastos operativos y otros; no se usaron ceros como sustituto de I+D. Separar o justificar proxy con sensibilidad en fase 2.
- **Inversiones Anthropic/OpenAI:** activos financieros valorados a valor razonable y aportes 2026 son potencialmente materiales; estimar no-operativo con derechos/restricciones/posible no liquidez, no sumar toda cifra de Other assets ni duplicar ganancias no realizadas en DCF.

## Documentos nuevos contrastados
- SEC 2026 10-Q (estados, notas de leases, deuda, inversiones y guía): https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm
- SEC 2025 Q3 10-Q (saldos de apertura LTM): https://www.sec.gov/Archives/edgar/data/1018724/000101872425000123/amzn-20250930.htm
- SEC 2016 10-K (saldos de apertura 2015, recalculados desde último comparativo 2016): https://www.sec.gov/Archives/edgar/data/1018724/000101872417000011/amzn-20161231x10k.htm
- 2024 10-K (obligaciones current FY2023/2024): https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/amzn-20241231.htm
- 2025 10-K: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
- Cierre anual ajustado por split: https://www.macrotrends.net/stocks/charts/AMZN/amazon/stock-price-history
- 8-K resultados 29-oct-2026: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000038/amzn-20261029.htm
- Catálogo de 8-K: https://biz.datenus.com/companies/amazon-com-inc/filings (fechas: 02/05, 02/27, 03/13, 03/16, 04/09, 04/14, 04/29, 05/22, 06/10, 06/12, 07/09, 07/30, 09/09, 09/14, 10/29 de 2026; fuentes subyacentes SEC).
- Rf 30-oct: https://treasuryratewatch.com/daily/treasury-yield-curve (replica U.S. Treasury). ERP 1-oct: https://pages.stern.nyu.edu/adamodar/New_Home_Page/home.htm ; blog 08-oct: https://aswathdamodaran.substack.com/p/earnings-cashflows-and-stock-prices

## Fase 2 habilitada con dependencias materiales explícitas
**Orden de continuación:** (1) ejecutar scripts reales desde entorno de JMR con credenciales Google Sheets antes de certificar; (2) verificar todo cero/rubro agrupado y 8-K faltantes; (3) Fase 2 calcula tasas/fuentes homogéneas, beta y WACC, ajuste I+D/leases, RSU, no operativos y capital de reinversión; (4) cuatro historias, controles DCF y múltiplos + sensibilidades 5×5, recálculo independiente, captura+SHA y JSON candidato; (5) no promover a EN_REVISION hasta gates y autorización. Esta autorización de avance es **metodológica y de trabajo CANDIDATO**, NO certificado de auditoría.

**Pasos de Fase 1 (0/1/2/3/4/5/5b/6/7/8):** 10/10 abordados, algunos con resultados PARCIALES y control oficial NO EJECUTADO justificado por acceso a scripts y entorno. No se oculta la pendiente ni se desbloquea la publicación. **La fase se declara CERRADA CON CONTROLES PENDIENTES porque hay insumos materiales suficientemente reconciliados para iniciar la investigación y construcción de Fase 2, no para entregar una valoración final.**

---

## Registro anterior de trabajo (historial; el dictamen anterior de PENDIENTE quedó reemplazado por el cierre CON CONTROLES PENDIENTES de arriba)

# AMZN · AMZN-20261102-A12-R4 · Fase 1 · ENTREGA PARCIAL, cierre NO acreditado

**Fecha:** 2026-11-02. **Herramienta:** ChatGPT GPT-6 / conectores Google Drive, GitHub y SEC (web), esfuerzo de razonamiento alto. **Método:** JMR A-1.2. **Estado:** CANDIDATO — fase 1 en curso, NO promover a EN_REVISION. **Hoja única de trabajo:** https://docs.google.com/spreadsheets/d/10qfoGrEP1PgdlLWrHvfoHqExKDZbPK75yb_oINlO4a8/edit. **PR:** https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/233 (borrador).

## Hecho y verificado

1. Hoja R4 limpia (46 pestañas), sin trasplante de R2/R3. R2/R3 archivadas, prohibido usar sus valores. El 2-nov-2026 se aplicaron **650 operaciones de escritura confirmadas** con Google Sheets API en la R4, exclusivamente en entradas y notas de origen: 202 para FY 2023–25 y Q3-2026, 112 de resultados FY 2016–22, 135 de flujos FY 2016–22, 197 de balances FY 2016–23, más 4 de identidad/corte/precio. No equivalen a 650 celdas únicas necesariamente, pues se actualizaron algunos encabezados.
2. **Income Statement:** diez FY completos 2016–2025 en B:K (ventas, COGS, SG&A agrupado, otros gastos operativos agrupados, EBIT, intereses, otros ingresos, impuestos, net income y acciones ponderadas). Fuentes SEC 10-K 2018 p.37 (2016–18), 2021 p.37 (2019), 2022 p.37 (2020–22) y 2025 p.37 (2023–25).
3. **Cash Flow Statement:** FY 2016–2025 en B:K y doce meses cerrados a 2026-09-30 en L, con CFO, D&A, SBC, capital expenditures, proceeds/incentives, inversiones, CFI/CFF. La SEC reporta directamente el flujo LTM 2026 en 10-Q p.3; no se usó la cifra de nueve meses como si fuera LTM.
4. **Balance Sheet:** FY 2016–2025 B:K y 2026-09-30 L con balances primarios SEC; inventarios en `Entradas históricas auxiliares!B3:L3`. Antes de 2019, los operating leases no estaban reconocidos por ASC 842: NO se colocó cero en long-term leases. De 2019 en adelante se registraron los pasivos de operating leases de largo plazo tal como se presentan.
5. **Corte de mercado:** 2026-10-30, cierre AMZN **USD 240,35** (histórico Yahoo/ChartExchange; `Trailing Valuation!L3`, fecha y procedencia en nota). `Input sheet!B4`, `B5` y `B8` contienen fecha, emisor y país, no supuestos especulativos.
6. **Reclasificación operativa:** `Income Statement!B8:K8` = Marketing/Sales + General administrative; `B11:K11` = Fulfillment + Technology/content or infrastructure + Other operating (expense) income. `I+D` no se publica de forma separada: incluido en Technology/content; NO implica que sea cero. Anotaciones de fuentes SEC por celda. Los 10 cálculos de ingresos − COGS − SG&A − otros gastos = EBIT publicado conciliaron a diferencia **0 USD M**.
7. **CFO y CFI:** las 10 conciliaciones construidas con partidas SEC y agregaciones anotadas dieron diferencia **0 USD M** en comprobación directa; FY2026 LTM CFO 168.300 y CAPEX bruto (215.192) USD M. `Cash Flow Statement!L36` calculó con su **fórmula original** CFO+CAPEX bruto = **−46.892 USD M**; la medida FCF reportada neta de incentivos agrega +4.535 y equivale a **−42.357 USD M**. Son DEFINICIONES DIFERENTES; no sobrescribir la fórmula existente.
8. **Identidades de balances:** agregaciones de activos, activos corrientes y pasivo + patrimonio FY2016–2026 conciliadas directamente a los totales SEC con diferencia **0 USD M** en las operaciones revisadas. Precios históricos de FY2016–25 no se inventaron.
9. **Fórmulas:** lecturas posteriores confirmaron que las celdas derivadas revisadas permanecieron como fórmulas: margen, crecimiento, EPS, EBITDA, FCF, ROE/ROIC/ROA y Trailing Valuation. Verificación directa parcial, NO es `diff_formulas_plantilla.py`.

## Fuentes primarias

- SEC 2017 10-K FY2016/17: https://www.sec.gov/Archives/edgar/data/1018724/000101872418000005/amzn-20171231x10k.htm
- SEC 2018 10-K FY2016–18: https://www.sec.gov/Archives/edgar/data/1018724/000101872419000004/amzn-20181231x10k.htm
- SEC 2020 10-K FY2019/20: https://www.sec.gov/Archives/edgar/data/1018724/000101872421000004/amzn-20201231.htm
- SEC 2021 10-K FY2019–21: https://www.sec.gov/Archives/edgar/data/1018724/000101872422000005/amzn-20211231.htm
- SEC 2022 10-K FY2020–22: https://www.sec.gov/Archives/edgar/data/1018724/000101872423000004/amzn-20221231.htm
- SEC 2024 10-K FY2023/24: https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/amzn-20241231.htm
- SEC 2025 10-K FY2023–25: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
- SEC 2026-Q3 10-Q, resultados 9M y CF 12M: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm
- Yahoo Finance 2026-10-30 cierre de mercado: https://finance.yahoo.com/quote/AMZN/history/?p=AMZN

## Juicios, restricciones y pendientes REALES

- **No existe todavía un valor intrínseco oficial A-1.2 para R4.** El DCF, WACC, cuatro historias, múltiplos, matrices 5x5, niveles narrativos y JSON de R4 no se publicaron ni se certificaron.
- **LTM Income Statement pendiente:** Q3-2026 publica nueve meses, no doce de la cuenta de resultados. Incorporar a la hoja un cálculo **con fórmula y referencias auditables** para LTM = FY2025 + 9M2026 − 9M2025, sin pegar el resultado manual ni ocupar o cambiar las 46 pestañas contractuales. Comprobación externa ilustrativa (NO salida oficial): ventas 797.455, EBIT 104.366, net income 134.779 USD M. No escribir automáticamente dichas comprobaciones sobre fórmulas.
- **Precios anuales:** se requieren cierres FY2016–25 ajustados por split 20:1, con fecha y acciones para `Trailing Valuation` y calibración por ciclo. Precio del 30-oct-2026 NO sustituye precios históricos.
- **Deuda y leases corrientes:** SEC incluye conceptos dentro de `Accrued expenses and other`; desagregar deuda y lease corriente desde notas/etiquetas XBRL cuando sea posible, documentar lo no separable; no poner ceros ficticios. Revisar reconciliación de activos y pasivos por arrendamiento ya reconocidos bajo ASC 842 (sin doble capitalización). Minoritarios y preferentes para EV: preferentes sin emisiones según SEC; minoritarios no separados, verificación pendiente, no inferir cero.
- **D&A y SBC:** el D&A del estado de CF abarca depreciación, contenido capitalizado y amortización de ROU assets. No atribuir todo al gasto SG&A ni deducir dos veces. I+D contenida en Technology/content requiere evaluación económica de capitalización, con desglose honesto y vida útil del activo. Acciones previas al split se normalizaron x20; shares reportadas originalmente redondeadas y deben validarse para múltiplos.
- **Extraordinarios:** altas plusvalías no operativas 2026 asociadas a inversiones, y un fuerte aumento de `Other assets` y `Long-term debt`. No usar el beneficio neto LTM sin normalizar inversiones ni mezclar activo no operativo con FCFF/EV.
- **Saldo previo FY2015 y Sep2025** para ROE/ROA/ROIC de primer año y LTM pendiente; inventario de entradas 2016/2026 y clasificaciones específicas por rubro sujeto a cotejo material y revisión de reconciliación.
- **Fase 1, controles oficiales NO EJECUTADOS:** `estados_completos.py`, `auditar_ceros_materiales.py`, `auditar_estados_sec.py`, `diff_formulas_plantilla.py`, `inputs_completos.py`, `candados.py`. La comparación de ciertas fórmulas fue directa/parcial; no sustituye gates y no se declara aprobación de CI ni publicación.
- En `Income Statement` utilidad común = utilidad neta bajo hipótesis sin derechos preferentes; antes de usar P/E y P/FCFE, validar patrimonio común y derechos atribuibles. FY2022 pérdida con beneficio fiscal: la tasa efectiva de la plantilla puede verse negativa; NO confundir con una anomalía económica sin análisis.
- El control de fecha/precios/inputs aún no es una fase 2. Si faltara desagregación material, continuar documentación y preparar supuestos como CANDIDATO; detener solo cálculos afectados y mantener el PR en borrador.

## Próximos pasos exactos

1. Conciliar 9M2025/9M2026 contra FY2025 y construir LTM por fórmulas sin cambiar plantillas o pestañas; cargar los saldos a 30-sep-2025 para balances iniciales de ratios.
2. Desagregar current leases/debt e inversiones no operativas, fuentes de I+D, SBC/dilución y precios anuales FY2016–25, sin inventar ceros ni valores.
3. Ejecutar scripts de integridad, fórmulas y anticeros. Guardar auditoría por ticker/revisión/sheet_id. Revisar el resultado en hoja.
4. Entregar Fase 1 cerrada o con controles pendientes según evidencias, iniciar Fase 2 solo con insumos materiales verificados y continuar Fase 3 sin publicar antes de gates y autorización.

**PASOS:** trabajo significativo de carga y controles directos ejecutado; el procedimiento completo de Fase 1 NO está acreditado. Estado de cierre: **PENDIENTE**, no CERRADA.
## ACTUALIZACIÓN DE COMPROBACIÓN DE CELDAS — 2026-11-02, posterior a la primera entrega

- **Se completó fórmula LTM de ingresos y EBIT en la misma hoja** sin pegar números: `Entradas históricas auxiliares!K6:L7` guarda ingresos y EBIT 9M 2025/2026 de SEC Q3, `Income Statement!L3` y `L12` calculan FY2025+9M2026−9M2025. Salidas de la hoja confirmadas: ventas LTM **797.455** y EBIT LTM **104.366** (USD M), margen **13,09 %**. `Income Statement!L21:L22` enlaza beneficio neto directamente del LTM reportado en Cash Flow, **134.779 USD M**, extraordinarios Anthropic incluidos; no se presenta como beneficio operativo normalizado.
- **Se introdujo fecha real tipo DATE 30-oct-2026 en `Input sheet!B4` y precio 240,35 USD en la celda fuente `Input sheet!D1`**, conectada por fórmula original a `B23`. Acciones en `Income Statement!L27` **10.811 millones**, fuente 10-Q. `Trailing Valuation!L5` calculó market cap **2.598.423,85 USD M**; el EV permanece no disponible porque quedan reconciliaciones de intereses minoritarios/activos y otros inputs, NO se inventa cero.
- **Deuda y leases corrientes 2025/2026 aclaradas con notas SEC:** FY2025 debt corriente **2.748** y leases corriente **14.199**, sep-2026 debt corriente **6.827** y leases corriente **15.959** (USD M). Se restaron íntegramente de `Accrued expenses and other` agregados, de modo que `Balance Sheet!K/L19+K/L20+K/L21` sigue igual a la fuente SEC; no se duplicaron pasivos. `Input sheet!B16` calcula deuda financiera y leases contables **294.735 USD M**. Las cifras por deuda a valor de MERCADO aún requieren WACC.
- **Cero de preferentes expresamente permitido** solo en `Entradas históricas auxiliares!K5:L5` porque el balance SEC informa none issued/outstanding. **Minoritarios NO se pusieron en cero** hasta confirmar su ausencia. La deuda y leases anteriores a 2025 siguen sujetos a desagregación documentada para valoraciones históricas.
- **Detección y corrección:** durante un lote de carga, ocho `Balance Sheet!B27:I27` habían recibido accidentalmente acciones comunes en vez de otros pasivos no corrientes. Se restauraron los ocho valores de los 10-K SEC y se escribieron las acciones en su ubicación correcta `Income Statement!B27:I27`. Se ejecutó comprobación directa nueva sobre datos efectivos B:L.
- **11/11 balances reconciliados** (FY2016–2025 y 2026Q3) en activo corriente, activo total, pasivo corriente y activos=pasivos+patrimonio, todas diferencias **0 USD M**. **10/10 EBIT anuales** y **11/11 CFO/CFI** (incluido LTM de caja 2026) con diferencias **0 USD M**. Es una prueba equivalente PARCIAL, no reemplaza `estados_completos.py`, `auditar_ceros_materiales.py` ni `diff_formulas_plantilla.py`.
- **Inversiones extraordinarias 2026:** 10-Q p.11–12 indica Anthropic preferentes **92.500**, notas convertibles **146.200** y OpenAI preferentes **50.000** (USD M, valores contables/fair value). Deben evaluarse individualmente como activos no operativos, sujetos a restricciones, caps/lockup, posibles participaciones en ingresos de AWS y doble conteo. Plusvalías no realizadas en utilidad LTM NO son FCFF. Las obligaciones contractuales de IA y aumento de CAPEX en 2027 son un riesgo de reinversión material.
- **Estado:** CANDIDATO; histórica primaria ampliamente cargada, paso de Fase 2 permitido solo en componentes con datos verificados. **Fase 1 NO CERRADA**: faltan cotejo total de fuentes/celdas, programas oficiales de integridad/anticeros, ajustes de I+D, datos de WACC/corte Damodaran, historial de precios y anclas, balances de apertura 2015 y Sep-2025 y varios desgloses/acciones LTM. No abrir publicación ni fusionar PR por esta entrega.

**Fuente para lease/debt:** SEC https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm (Nota 3 p.14 y Nota 5 p.19).
