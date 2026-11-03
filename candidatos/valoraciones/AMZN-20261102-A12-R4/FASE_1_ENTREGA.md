# AMZN · AMZN-20261102-A12-R4 · FASE 1 (NUEVO PROCESO 5F) · CANDIDATO CALCULADO CON CONTROLES PENDIENTES

**Fecha:** 2026-11-02. **Herramienta:** GPT-6/ChatGPT (razonamiento alto), conectores GitHub y Google Sheets, SEC y Damodaran. **Estado:** CANDIDATO, NO AUDITADO, NO PUBLICAR, NO MERGE PR #233. **Proceso v26 / Fase 1 NUEVA:** construir DCF Damodaran y cuatro historias con solo los insumos esenciales de Input + múltiplos. La antigua Fase 1 (históricos) se conserva íntegra en `FASE_1_ENTREGA_4F_HISTORICO.md`. R2/R3 excluidas, sin transferencias de supuestos ni precios.
**Hoja única de trabajo:** https://docs.google.com/spreadsheets/d/10qfoGrEP1PgdlLWrHvfoHqExKDZbPK75yb_oINlO4a8/edit
**Corte mercado:** 30-oct-2026, precio USD240,35; **corte estados:** 30-sep-2026; cifras en USD millones salvo precios/ratio.

## Resultado DCF calculado por fórmulas nativas y verificado por lectura API

| Historia | Probabilidad de trabajo | Crecimiento CAGR 1–5 | Margen EBIT objetivo | Sales/Capital 1–5 / 6–10 | ROIC terminal | g terminal | DCF presente por acción |
|---|---:|---:|---:|---:|---:|---:|---:|
| Base | 45% | 10,9977% | 15,5% | 0,80 / 1,80 | 12% | 4% | **USD163,3495807** |
| Conservadora | 22,5% | 7,5966% | 12,8% | 0,55 / 1,40 | 10% | 3,5% | **USD94,2961842** |
| Optimista | 22,5% | 13,2949% | 17,7% | 1,10 / 2,20 | 15% | 4% | **USD246,1530014** |
| Disrupción | 10% | 2,2943% | 10% | 0,40 / 1,15 | 7% | 2,5% | **USD69,8779391** |

- `Escenarios e historias!H5:H8` muestran valores anteriores, `K5:K8 = LISTO` (control técnico de insumos, NO certificación económica). `Valuation output!B35` **163,3495807** de la misma revisión. Las cuatro historias se calcularon con el motor; Disrupción se excluye del promedio corriente.
- **MOS35%** = 163,3495807 × 0,65 = **USD106,1772275/acción**; `Resumen de Valoración` conserva fórmula propia 0,65× Base.
- **Promedio ordinario** de Conservadora/Base/Optimista con pesos renormalizados = **USD166,7870868/acción** (`Escenarios e historias!H10`). No es el valor principal. Precio de corte USD240,35 > Base: no usar cifras para recomendación definitiva sin F2/F3.
- Años 1–10 de crecimiento están en `Escenarios e historias!C29:L29`, `C53:L53`, `C77:L77`, `C101:L101`; margen/Sales-to-Capital en D:F5:8, ROIC terminal N5:8 y valor presente H5:8. Son **[JUICIOS], no datos SEC ni supuestos heredados**.

## Datos principales y costo de capital

- `Input sheet!B12/B13` ventas/EBIT LTM = **797.455 / 104.366**, B19 caja/marketables **114.226**, B16 deuda/leases/financing obligaciones contables **304.841**, B15 patrimonio contable **613.601**, B21 NCI sin derecho separado reportado = 0, B22 acciones **10.811 millones**; precio D1 240,35. Fuente SEC 2025-10-K y 2026Q3-10-Q; notas por celda.
- `Cost of capital worksheet` método **Detailed**, beta bottom-up mezcla negocios Retail General y Computer Services: 9M2026 North America + International = 458.266 y AWS = 125.803 USD M, ventas consistentes 584.069. F1 beta desapalancada 0,810077 y beta equity 0,852655, usando pesos de negocios por sector de Damodaran; dato/sector proxy justificados.
- Coste capital inicial `Cost of capital worksheet!B14=Input sheet!B36` **8,179603%** (técnicamente `B84=VALIDADO`). Rf y ERP Damodaran fecha **30-sep-2026** 5,29% / 3,70%; B27 prima; rating S&P AA, Kd 5,8406%, impuesto marginal **25% como juicio**, WACC usa deuda a mercado plantilla C54 **180.382 M**, pero DCF resta book debt **304.841 M** en `Valuation output!B27`. **No confundir ambos conceptos.**
- WACC terminal `Input sheet!B46=Yes, B47` **fórmula** = Rf5,29% + ERP madura3,70% = **8,99%**, beta terminal1. Es un override transparente para evitar la prima anual obsoleta en B97 default. Terminal g Base4% < Rf5,29%, WACC terminal>g. Debe verificarse exposición al riesgo país / beta business y precio vs tasas entre 30-sep y 30-oct.

## Reclasificación I+D ESTIMADA — fuente original conservada

Amazon **NO publica una línea I+D separada**; Technology and Infrastructure mezcla I+D, infraestructura, depreciation, mantenimiento y renta. Para la F1 se modeló un **proxy [JUICIO] de 30%** de ese gasto y vida de amortización 5 años, no una cifra SEC. El modelo no puede identificar proporción real con certeza.
- `Input sheet!F119=0,30` factor ajustable; `Input sheet!G120:N120` conserva datos T&I **GAAP originales** de FY2021–FY2025, LTM2026, 9M2025/9M2026; `G122:N122` conserva **Other operating expenses GAAP originales**.
- `Income Statement!G10:N10` = **fórmulas** con proxy 30% desde T&I; `G11:K11` y `M11:N11` = otros gastos GAAP originales MENOS proxy I+D, conservando **cada suma y EBIT reportado**; `L11=K11+N11-M11` se conservó intacta. La reubicación contable **NO cambia el EBIT de origen**; es separación económica pro forma, NO estado SEC original. Se recupera en cualquier momento desde los datos de Input.
- `R& D converter!F7=5`, gasto supuesto LTM **38.081,4 USD M**, activo investigación `D36=94.731,78` M, amortización 24.717,12 y ajuste EBIT 13.364,28 M. `Input sheet!B111=VALIDADO` acredita el cálculo, NO demuestra que el 30% sea una revelación SEC.
- **Sensibilidad ejecutada y restaurada** F119 del 20% → DCF Base **162,6015318** / investigación asset 63.154,52; 30% elegido → **163,3495807** / asset 94.731,78; 45% → **164,4716541** / asset 142.097,67. Rango DCF Base ±1,12 USD/acción (<1% con resto constantes), **pero proporción de I+D exige revisión de documentación en F2/F3**. Se restituyó F119=30%, lectura confirmada.

## Inversiones estratégicas, deuda, SBC y NOL

- `Input sheet!B83/B84` **288.700 USD M**, suma de fair value SEC de Anthropic nonvoting preferred 92.500, Anthropic convertible notes 146.200 y OpenAI preferred 50.000, activos no consolidados en Other assets; valor razonable Level3, susceptible a iliquidez/valoración. `B85=VALIDADO` es control estructural con fuentes, no evidencia de realizabilidad. No añadir plusvalías históricas de Anthropic a FCFF ni volver a sumar esas participaciones. **Un haircut hipotético del 25% al valor económico reduciría equity ~72.175 M, equivalente a ~USD6,68/acción (4,1% del Base) sin alterar otros drivers; material.** Necesita F3.
- `Input sheet!B18=No` significa **sin conversión incremental** porque leases ASC842 **114.783 USD M** ya reconocidos en balance, NO significa ausencia de leases. Cost of capital C56=0, no sumar dos veces.
- **Deuda a mercado:** notas SEC FV145.400, term loan 17.500, leases PV114.783, financing obligations reconocido aprox9.726 → reconstrucción indicativa **287.409 M**, frente a libro304.841 y estimación C54 180.382. La fórmula efectiva DCF en `Valuation output!B27` resta BOOK304.841 (no C54): NO aplicar diferencia ~107.027 de C54 como si fuese corrección directa del equity; el efecto de puente book→mercado ≈USD1,61/acción antes de recalcular WACC. WACC alternativa simplificada 8,1221% vs oficial 8,1796% (−0,0575pp), impacto total exige rehacer el motor y reconciliar pequeñas partidas. Issue oficial del motor [#197](https://github.com/JuanMaRobledo/JMR-valuation/issues/197), corregido en su descripción.
- `Input sheet!B38=No` solo para opción call de empleados no material reportada; **RSUs siguen materiales**: stock awards 222,5M diciembre2025, FY2025 SBC19.467 M, necesidad de proyección de RSU y dilución sin doble conteo en F3.
- `Input sheet!B62=No` se refiere a **escudo NOL utilizable proyectado** en el flujo consolidado, no niega NOL históricos: 10-K reporta 10.600 M extranjeros brutos con allowance sobre sustancialmente todos, restricciones jurisdiccionales y expiración; techo fiscal teórico 25%×10.600 =2.650 M o USD0,25/acción; verificar impuestos en F2/F3.

## Regresión de fórmulas tributarias y múltiples

- **BUG TAX-194 corregido** en las tres plantillas Maestra/IA/Manual (con respaldo previo) y AMZN R4; `Financials Multiples` filas 15/54/94, B:D usan utilidad común reportada o EBT + impuestos signed, no restan gasto negativo. FY2023 **30.425**, FY2024 **59.248**, FY2025 **77.670** M confirmados contra SEC. Proyecciones E:G preservan EBT menos tasas de impuesto positivas. Script y tests integrados por PR del motor [#196](https://github.com/JuanMaRobledo/JMR-valuation/pull/196); CI `JMR materialidad y salvedades` EXIT SUCCESS; issue #194 cerrado. **No se ha certificado la normalización de plusvalías Anthropic en proyecciones P/E, P/FCFE.**
- Cinco contrastes prioritarios (EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF) **aún N/D o incompletos en sus precios FY+1/2/3** porque no se han elegido/marcado anclas de ciclo ni ponderaciones y se requiere normalizar ganancias no operativas. Los 0 visibles en ciertos subpaneles no deben contarse como precios calculados. P/S y P/BV opcionales.

## Riesgo de reinversión detectado y corregido dentro de F1

- En F1 primera pasada `Base E5=1,10` producía FCFF FY+1 de ~2.832 M pese a FCF LTM negativo. SEC indica que CAPEX de caja aumentará significativamente en 2027, por lo que se redujo Sales-to-Capital 1–5 en las cuatro historias (Base **1,10→0,80**, conservadora **0,85→0,55**, optimista **1,40→1,10**, disrupción **0,65→0,40**) y se recalculó la plantilla automáticamente.
- **Prueba sensibilidad manteniendo todo más constante:** S/C Base **0,60** → DCF **145,4550 USD** (FCFF FY+1 −80.156 M); **0,80** → DCF **163,3496 USD** (FCFF FY+1 −34.512 M); **1,10** → DCF **177,9906 USD** (FCFF FY+1 +2.832 M). Se devolvió Base a 0,80. Esta sensibilidad es **material**, no resuelta definitivamente; revisar CAPEX bruto vs incentivos, D&A y NWC durante F3.
- Las tres matrices de sensibilidad DCF Base 5×5 (WACC×g, ROIC terminal×g, crecimiento 1–5×margen EBIT) muestran centro **163,3495807** y estado de conciliación **OK** cada una (`Sensibilidad DCF!D8,D19,D30` y `B12/B23/B34`). No equivale a que los supuestos económicos sean óptimos.
- **Caveat:** `Financials Multiples` anticipa CAPEX FY+1 alrededor de USD120.785 M, mucho menor que CAPEX caja LTM215.192 M pese a anuncio de incremento 2027; el pronóstico por múltiplos no se puede tratar como adecuado hasta revisión, aunque el DCF usa reinversión Sales/Capital separada.

## Controles finales y estado preciso

**OK ejecutados:** integración método v26 main, fuente/ticker/corte, fórmulas 4 historias K5:K8 LISTO, Cost capital B84=VALIDADO (aritmético), Input B85 inversiones=VALIDADO (estructural), B92 política fiscal VALIDADO, B108 opciones/NOL/I+D etc VALIDADO, 3 sensibilidades 5×5 centros OK, 36 fórmulas fiscales en 3 masters + R4 y test GitHub CI success, conciliación EBIT antes/después reclass R&D por agregados publicados, sensibilidad R&D y S/C ensayada y restituida. La hoja oficial de trabajo conserva 46 pestañas; Forward Valuation deprecada pero no borrada aún por issue #195.

**NO CERTIFICADO/NO EJECUTADO:** controles oficiales `estados_completos.py`, `auditar_estados_sec.py`, `auditar_ceros_materiales.py`, `diff_formulas_plantilla.py`, `candados.py`, `controles_todas.sh` con acceso autenticado a la R4; control de cero económico detallado F2, normalización de ganancias no operativas en P/E, financiamiento y CAPEX FY+3 de múltiplos, precio de deuda y leases, resultados de sensibilidad de múltiplos, SBC RSU dilución, límites fiscales inversión, calce geografía del ERP y precios históricos auditados. No se marca ninguno APROBADO por tener los cuatro escenarios calculados.

**Dictamen F1:** el estudio **SÍ TIENE DCF COMPLETO DE CUATRO HISTORIAS COMO CANDIDATO**, pero Fase 1 queda `CERRADA CON CONTROLES PENDIENTES` para continuar investigación de históricos F2 y revisión económica F3. NO pasa a `VERIFICADO`, NO publicar NI fusionar PR datos #233, NO usar DCF como recomendación de compra. F2 aprovecha los históricos ya cargados en el archivo 4F sin recalcular desde cero; F3 resolverá los hallazgos materialmente relevantes y solo F4 promocionará tras todos los gates técnicos. F5 sigue reservada para auditoría independiente guiada por el usuario.

**Fuentes primarias:** https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm ; https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm ; Damodaran implícita https://aswathdamodaran.substack.com/p/earnings-cashflows-and-stock-prices .

## Comprobación posterior de hoja efectiva (2026-11-02)

Nueva lectura de Google Sheets confirmó que **8/8 períodos** FY2021–2025, LTM sep2026 y comparativos 9M2025/9M2026 cumplen `Ingresos − Cost of sales − SG&A − R&D-proxy − Otros gastos reclasificados = EBIT GAAP publicado` con diferencias 0 USD M (error redondeo flotante LTM <3×10^-11). Las cuatro celdas de historia `Escenarios e historias!K5:K8` muestran `LISTO`, con valores 163,34958 / 94,29618 / 69,87794 / 246,15300 USD por acción, en orden Base/Conservadora/Disrupción/Optimista. Las tres conciliaciones centrales `Sensibilidad DCF!B12/B23/B34` muestran **OK**. Se reconfirmó el factor económico I+D `Input sheet!F119=0,30` después de las pruebas. Ninguna de estas pruebas es auditoría económica ni ejecución de los scripts oficiales.
