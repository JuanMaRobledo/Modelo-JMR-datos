# AMZN R5 — FASE 1 JMR A-1.2 v27 · CERRADA COMO CANDIDATO CON CONTROLES PENDIENTES

**Fecha:** 2026-11-02. **Revisión:** AMZN-20261102-A12-R5. **Método:** JMR A-1.2, DCF Damodaran FCFF, MOS35%. **Herramienta:** GPT-6 / conectores Google Sheets y GitHub, búsqueda/lectura SEC y Damodaran. **Corte mercado:** 30-oct-2026 USD240,35. **Corte financiero:** 30-sep-2026 (FY2025 +9M2026 -9M2025). **Escala:** USD millones, acciones millones, precio USD/acción.
**HOJA AUTORITATIVA R5:** https://docs.google.com/spreadsheets/d/199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I/edit. Copia directa de plantilla IA oficial `1e-lbQmCkObfq74YLpWnMmIidmcdsJQ-6uN4oiHnNTEQ`, ubicada en `Análisis/AMZN`, 46 pestañas. **NO se importó ningún valor, parámetro o precio de R2/R3/R4.** R4 PR #233 cerrado sin fusión.

**Auditoría de datos por celda y fuentes:** [INVENTARIO_ENTRADAS_F1.md](INVENTARIO_ENTRADAS_F1.md), integral y vinculante con el contrato v27: `Modelo-JMR/docs/propuestas/fases/CONTRATO_INSUMOS_FASE_1.md`.

## Resultado DCF por fórmula nativa de la hoja

| Historia | Probabilidad F1 | Margen EBIT objetivo | S/C años 1–5 → 6–10 | ROIC terminal | DCF USD/acción |
|---|---:|---:|---:|---:|---:|
| Base | 45% | 15,8% | 0,72 → 1,65 | 11,5% | **149,1914858** |
| Conservadora | 22,5% | 12,0% | 0,52 → 1,25 | 9,5% | **81,0095172** |
| Optimista | 22,5% | 18,5% | 1,15 → 2,10 | 15,0% | **241,8435161** |
| Disrupción | 10% | 8,5% | 0,35 → 1,05 | 7,5% | **62,4357315** |

**Valor principal: DCF Base USD149,19. Precio MOS 35% = USD96,97.** Promedio renormalizado de las tres historias ordinarias (sin Disrupción) **USD155,3090**; no es valor principal. Precio mercado USD240,35; diferencia Base/mercado ~−37,9%. Las cuatro historias tienen proyecciones individuales de crecimiento diez años y narrativa de demanda/cloud + reinversión CAPEX; NO son predicciones publicadas por SEC. `Escenarios e historias!H5:H8`, `K5:K8=LISTO`, `Valuation output!B35`, tres matrices `Sensibilidad DCF!B12/B23/B34=OK`.

## Inputs económicos verificables y supuestos

- **Resultados:** FY2022–25, comparables 9M2025/9M2026 y LTM. Últimos 12 meses ingresos **797455**, EBIT SEC **104366**, NI GAAP **134779** (incluye ganancias no operativas; NO usar en P/E como recurrente).
- **Flujos:** CFO LTM168300, CAPEX bruto −215192, incentivos +4535; FCF bruto **−46892**, neto de incentivos **−42357**. 2027 CAPEX esperado mayor, reinversión altamente material.
- **Deuda/caja:** BS current/long debt including leases and financing obligations **304841**, cash + marketable **114226**, shares outstanding **10811 M**. Valor no operativo en activos **288700 M** de participaciones Anthropic/OpenAI marcadas como fair value Level3, no cash. Cálculo EV/stock equity usando **deuda BOOK**, no el dato C54 de deuda a mercado.
- **WACC:** `Cost of capital worksheet!B14=Input sheet!B36` **8,179603%** mediante Detailed, beta multibusiness Retail General + Computer Services; Rf5,29%, ERP implícita3,70% de 30-sep-2026, calificación AA S&P. Terminal WACC beta1 **8,99%** por fórmula cofechada; g Base4% parametrizado en Input, otros escenarios con restricciones. **Salvedad:** precio mercado30-oct frente corte tasas30-sep y deuda mercado por bono único ficticio. Motor issue #197 abierto. NO WACC económico certificado.
- **Capitalización I+D:** Amazon NO divulga R&D separada de Technology&Infrastructure. Propuesta económica explícita e independiente 25% de ese agregado; vida5 años, activo de investigación calculado **78943,15 M**, EBIT ajustado +**11136,90 M**, con contrapartida para preservar EBIT SEC. Sensibilidad REAL 15%→Base148,4858 / 25%→149,1915 / 40%→150,2500. Restaurado F119=25%. Este gasto no es cifra publicada ni se certifica.
- **Leases:** ASC842 ya reconoce leases PV114783, sin capitalización incremental; `Input B18=No` no significa no leases. Deuda base book agrupa obligaciones de financiación. **Option value:** sin opciones emitidas de common stock materialmente reportadas (N/A documentada), RSUs **223,3M** outstanding + SBC LTM **19873 M** + unrecognized **22300 M** (SEC 2026Q3). No valorar las RSUs como calls de Black-Scholes; muestra sensibilidad mecánica full vest Base ~USD146,17/acción, NO oficial por potencial doble conteo SBC. NOL de uso consolidado no asumido sin evidencia positiva, pero NOL históricos no necesariamente cero.
- **Ingresos de inversiones:** plusvalías de Anthropic van a otros ingresos, fuera EBIT, no proyectarlas en FCFF ni sumar inversiones dos veces. Una pérdida hipotética del 25% de fair value Level3 impactaría ~US$6,68/acción y 40% ~US$10,68/acción si resto fijo. No son revaloraciones oficiales ni incluyen impuestos de realización.

## Cinco métodos de valoración por múltiplos evaluados

| Método | Evidencia de ancla 2022–25 | Resultado VP3 Base | Dictamen F1 |
|---|---|---:|---|
| **EV/EBITDA** | Cuatro cierres con EBITDA positivo, mediana **18,462x**; 90/100/110% por historia, fórmulas nativas en J8/J19/J30 | **USD349,7436** | Calculado CANDIDATO; EV de libro/lease y reinversión distorsionan comparación con DCF |
| **P/OCF** | Cuatro cierres OCF positivo, mediana **16,833x**, precios año correspondiente y split | **USD179,1477** | Calculado CANDIDATO; OCF omite CAPEX masivo |
| **EV/FCFF** | FY2022–25 histórico positivo, pero FY+3 Base **FCFF −6371,92 M**; 2026 LTM FCFF bruto **−46892 M** | N/A | No aplicar múltiplo positivo a denominador prospectivo negativo |
| **P/E** | FY2022 pérdida neta, solo tres FY positivos; FY2025/26 ganancias extraordinarias en fair value de Anthropic contaminan utilidad | PENDIENTE | Requiere normalizar beneficios no operativos e impuestos antes de calcular P/E FY+3; no usar NI GAAP LTM como recurrente |
| **P/FCFE** | **Solo tres cierres positivos tras revisar apertura 2021**; FY2022 P/FCFE recalculado **−65,429x**, FY2023 193,451x, FY2024 78,476x, FY2025 57,477x | N/A | No fabricar ancla, FCFE/financiamiento volátil; año1 proyectado negativo; bug plantilla issue #199 |

**Perfil en `Resumen de Valoración!G3=Crecimiento` (provisional)**, pesos de norma 60% DCF/10% EBITDA/15% EV-FCFF/5% PE/5% FCFE/5% POCF. **Resumen ponderado global queda en blanco correctamente** porque tres métodos tienen peso >0 sin resultado válido. NO cambiar pesos de tabla maestra o inventar precios para lograr 100%; se revisan por tipo y modelo económico en fase 3. MOS35% sigue referido exclusivamente al DCF Base.

## Controles efectivamente comprobados

| Control | Resultado | Clasificación |
|---|---|---|
| Copia limpia de plantilla IA y aislamiento R5 | 46 pestañas, carpeta Análisis/AMZN, R4 no migrada | CONFIRMADO |
| P&L operativos / EBIT reportado | **7/7** FY2022–25, LTM Sep2026, 9M2025 y 9M2026; diferencias **0** | COMPROBADO por lectura API y cálculo independiente de identidades |
| Cash Flow | **5/5** CFO, **5/5** CFI, **5/5** conciliación CFO+CFI+CFF+FX=cambio caja; diferencias **0** | COMPROBADO |
| Balance | **5/5** FY2022–25 y Sep2026 activos corrientes/total/pasivo corriente/pasivo+equity diferencias **0**, más saldo apertura FY2021 | COMPROBADO |
| Inputs y WACC | `B84`, Tax `B92`, Option/Leases `B108`, R&D `B111`, inversiones `B85` muestran `VALIDADO` | CONTROL ESTRUCTURAL, no auditabilidad económica |
| Escenarios/DCF | `K5:K8=LISTO`, 4 valores DCF y 3 matrices Base 5×5 con centro `OK` | CONTROL DE FÓRMULA, no certificado |
| Múltiplos | 5 evaluados, 2 candidatos calculados y 3 N/A/PENDIENTE con motivo; 5×5 Base EVEBITDA/POCF conectadas con VP3 | CANDIDATO PARCIAL |
| R&D económica | Sensibilidad 15/25/40 realizada en hoja con restauración de 25% | COMPROBADO como proxy, NO como cifra SEC |
| P/FCFE 2022 falsa ancla | La ausencia de BS FY2021 dio falso positivo; tras cargar apertura auténtica recalculó a negativo y dejó ancla en blanco. Issue JMR motor [#199](https://github.com/JuanMaRobledo/JMR-valuation/issues/199) | BUG ABIERTO en plantilla general; **no usado** en salida |
| **Scripts oficiales** `estados_completos.py`, `auditar_estados_sec.py`, `auditar_ceros_materiales.py`, `diff_formulas_plantilla.py`, `inputs_completos.py`, `candados.py`, `controles_todas.sh` | **NO EJECUTADOS** por falta de runtime del motor conectado a la hoja R5 y a la CI del catálogo | **PENDIENTE BLOQUEANTE DE PUBLICACIÓN** |
| JSON, app, CI completa y audit económico | NO EJECUTADOS; no son pasos de publicación en F1 | PENDIENTE, reservado para F3/F4/F5 |

## Dictamen y transferencia

**FASE 1: CERRADA COMO CANDIDATO CON CONTROLES PENDIENTES**. El mapa requerido por la norma v27 se atendió y se produjeron DCF Base/cuatro historias, WACC, I+D, Option value N/A, leases, activos no operativos y cinco métodos evaluados con N/A fundamentados. No es una valoración final ni F1 "certificada": el puente market debt y la normalización P/E son temas económicos materiales, la plantilla contiene bug #199, y las pruebas oficiales NO se ejecutaron. Se permite **F2 datos históricos completos** conservando R5 y fuentes SEC, sin volver a F1 por depender de diez años. F3 juzga economía de márgenes, reinversión y ROIC, resuelve deuda/RSU/P-E/FCFE y recalcula. F4 analiza y publica EN_REVISION **solo con controles oficiales aprobados**. F5 auditoría independiente guiada por usuario.

No fusionar PR de datos [#234](https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/234), ni publicar valores de R5 en app antes del control técnico y aprobación de fase correspondiente. No reutilizar R2/R3/R4.

**Fuentes:** SEC 2026Q3 https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm ; 2025FY https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm ; FY2024 https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/amzn-20241231.htm ; FY2022 https://www.sec.gov/Archives/edgar/data/1018724/000101872423000004/amzn-20221231.htm ; ERP Damodaran https://aswathdamodaran.substack.com/p/earnings-cashflows-and-stock-prices .


## Rectificación posterior a Fase 2 — revisión de Input sheet (2026-11-02)
**Debe leerse junto a [AUDITORIA_POST_F2_INPUT_V27.md](AUDITORIA_POST_F2_INPUT_V27.md).** Se detectaron vacíos B9/B10 y B50 que no fueron tratados en la revisión inicial. Fueron corregidos en R5 y documentados: industria Retail (General) solo benchmark (WACC sigue Multibusiness retail+AWS), ROIC Base referencia B50=N5, y Cost of capital B49 preferentes emitidas=0. Se reactivaron B30 margen referencia10,64%, B32/B33 Sales-to-Capital referencia industria Global2,7255; **son referencias NO ACTIVAS en las cuatro historias** (Base E5=0,72, F5=1,65). El DCF Base y cuatro historias no cambiaron. Persisten peers en Sector sin cargar, normalización de resultados no operativos de múltiplos, puente ERP geográfico y scripts oficiales NO EJECUTADOS. Incidencia de regresión [#200](https://github.com/JuanMaRobledo/JMR-valuation/issues/200). Los controles estructurales LISTO/VALIDADO no prueban que F1 haya llenado todo el Input. **No interpretar el estado CANDIDATO de F1/F2 como captura F1 sin salvedades.**
