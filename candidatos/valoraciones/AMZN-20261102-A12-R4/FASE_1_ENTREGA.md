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