> **ESTADO VIGENTE 03-nov-2026 · R1 tras Work**: el cálculo nativo actualizado y listo para integrar es **DCF Base US$141,0085164686**, MOS35% **US$91,6555357046**, Conservador102,820990, Optimista172,892801, Disrupción71,268253. Precio de referencia **US$331,90 cierre 3-nov-2026** posterior a presentación SEC. WACC Detailed inicial**12,86221066%**, terminal**9,70%**, Ke12,994506%, ROICterminal15%. Múltiplos secundarios Base hoy**US$183,946667**, combinado secundario hoy**US$166,771407**. **Fuente única de estos números:** [hoja JMR](https://docs.google.com/spreadsheets/d/1dEycisHE5Ai34Z50ELOByAiZxub87dPG2TwOmYjS2tA/edit) y `SNAPSHOT_FINANCIERO_NATIVO.json` / `valoraciones/AAPL-20261103-A12-R1.json` en el PR. El texto posterior registra estado de fases ANTERIOR y sus cifras Base 150,04 / WACC12,48 / precio338,32 están **SUPERSEDIDAS**; no usar como valores activos de AAPL. El artículo completo actualizado consta de **14 capítulos y 9.668 palabras**, 12 apartados Nivel2, en `ANALISIS_N1_N2_CANDIDATO.json` / `analisis/AAPL-research-AAPL-20261103-A12-R1.json`. El catálogo está preparado en rama; sólo se publica tras CI aprobado y fusión del PR. Auditoría F5 independiente pendiente.

# Apple (AAPL) · JMR A-1.2 R1 · Análisis fundamental Nivel 1 y 2 · CANDIDATO_REVISADO / NO PUBLICADO
**Fecha:** 2026-11-03 · **Revisión:** AAPL-20261103-A12-R1 · **Hoja:** [Google Sheets 46 pestañas](https://docs.google.com/spreadsheets/d/1dEycisHE5Ai34Z50ELOByAiZxub87dPG2TwOmYjS2tA/edit) · **Método:** A-1.2, FCFF · **Estado:** CANDIDATO, NO AUDITADO, NO PUBLICADO.

Documento narrativo (14 capítulos) y técnico (12 apartados), versión actualizada con **DCF y cinco múltiplos NATIVOS** de la hoja, FY2026 (cierre contable 26-sep-2026; Apple publicó el 10-K 3-nov-2026). Datos SEC señalados [Dato], derivaciones de Sheets [Cálculo], entradas sensibles [Juicio]; modelos externos anteriores quedan supersedidos. Estado candidato porque faltan candados oficiales, auditorías de fórmulas y reconciliación JSON/app, no porque el DCF sea N/D. Fuente [SEC FY2026](https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm).

## NIVEL 1 — Historia económica y análisis fundamental (14 capítulos; BORRADOR)

### 1. Empresa, tesis y contraste esencial
Apple combina hardware premium, sistema operativo, distribución, servicios y ecosistema de desarrolladores con costos de cambio relevantes. [Dato] FY2026 ventas US$478.834M (+15,06%), NI US$132.175M (+18,0%), EBIT GAAP US$158.063M. [Juicio] no extrapolar +15% indefinido: ciclo de renovación y servicios, IA, regulatory takerates y poder adquisitivo global. [Cálculo nativo] DCF FCFF Base **US$150,04/acción**, MOS35% **US$97,53**, cotización fechada US$338,32 al cierre 2-nov-2026 (ANterior a presentación 10-K 3-nov; precio no actualizable por suposición). La cotización excede en 125,48% el valor estimado; no hay margen de seguridad según esta hipótesis ni predicción de caída en horizonte fijo.

### 2. Modelo de negocios
La integración de chips, software, diseño y retail permite vender dispositivos con precio premium y una relación recurrente vía servicios. Hardware exige renovación, componentes y manufactura tercerizada; servicios generan mayor margen bruto y rentas por uso del ecosistema. [Dato] Productos **US$355.533 M**, servicios **US$123.301 M**. Servicios son **25,75%** de ingresos, no de EBIT, y no se deben proyectar con el margen consolidado.

### 3. Segmentación y motores de monetización
[Dato] iPhone **US$254.098 M**, Services **US$123.301 M**; Mac, iPad y wearables complementan entrada/uso del ecosistema. Crecimiento iPhone requiere distinguir reemplazo de unidades, ASP, modelos, FX y China; servicios requiere base activa, monetización, tarifas regulatorias y retención. [Juicio] Una tasa de crecimiento agregado 7% durante años1–5 se propone como hipótesis externa, y exige un puente por líneas para validarse. El FY2026 +15% no basta para demostrarlo.

### 4. Ventajas competitivas y límites
Fortalezas: marca, integración hardware/software, desarrolladores, complementariedad de hardware/servicios, fidelidad. Los costes de cambio no son barreras absolutas: IA multimodal, distribución, regulación y competencia pueden erosionarlos. El ROIC terminal Base 15% frente al WACC terminal calculado **9,32%** implica 5,68 puntos porcentuales de renta económica persistente; el WACC inicial **12,4830%** es distinto del terminal, por beta que converge. No perpetuar el ROIC contable actual inflado por recompras y tratamientos de I+D.

### 5. Ciclos: compañía, macro, crédito, monetario y sentimiento
Apple es negocio grande y maduro con crecimiento ligado a renovación de equipos y consumo discrecional; servicios suavizan volatilidad pero no la eliminan. Tasa libre, tipo de cambio USD, crédito de hogares, aranceles y costo de componentes alteran consumo y valor presente. Las recompras a precios elevados pueden reducir retorno al accionista aun elevando EPS. Diferenciar ciclo operativo (unidades, precio, mix), ciclo de crédito (demanda), monetario (WACC) y de sentimiento (P/E) y evitar contar el mismo riesgo a la vez en flujos y tasa. No se deriva valoración de movimientos diarios de la acción.

### 6. Crecimiento 1–5 y 6–10
[Dato] ventas FY2024 391.035; FY25 416.161; FY26 478.834; tasas FY25 **6,43%**, FY26 **15,06%**. [Juicio de contraste] Base 7% anual 1–5, luego 6,0/5,5/5,0/4,5/4,0% 6–10. Sensibilidad: 4% conservador, 9,5% optimista, 1% disrupción. Pendiente: cohortes outside-view por tamaño y subsector, estimación del aporte real de servicios y capacidad de suministro/IA; no multiplicar ingresos sin reinversión.

### 7. Márgenes
[Dato] FY26 margen bruto **48,79%**; EBIT GAAP 158.063 / 478.834 = **33,01%**; margen operativo ajustado por I+D capitalizada **35,90%**, sujeto a vida útil y amortización. Márgenes brutos Productos **39,28%** (139.659/355.533) y Servicios **76,19%** (93.943/123.301), sin equivalencia directa con EBIT por segmento. [Juicio] Margen EBIT ajustado Base 36,3% año5, 36% año10, 35,5% terminal; si servicios pesan más pueden elevar el margen, pero IA computacional y política App Store pueden contrarrestar.

### 8. Reinversión económica y Sales-to-Capital
[Dato] FY26 CFO145.097, capex físico9.041, D&A13.423, I+D45.765, SBC13.789 (USD M). Inversiones de innovación y cadena de suministros no se agotan en PP&E, y el FCF de caja **136.056** no es el FCFF económico de Damodaran. [Juicio] S/C marginal Base1,80 años1–5 y2,00 años6–10; sensibilidad a menor productividad, desfasaje y reinversión en infraestructura IA. Diagnóstico 1 año: Δventas FY25→FY26 =62.673 y Δcapital operativo ajustado proxy ≈29.767 => S/C histórico ≈2,106; **no** usar como evidencia suficiente de retorno incremental ni promediar sin ajustes.

### 9. ROIC, retorno incremental y terminal
La combinación de elevada rentabilidad y bajo capital contable genera ROIC extraordinarios, distorsionados por recompras, activos creados internamente e I+D previamente gastada. [Juicio] ROIC terminal **15%** y no perpetuar el ROIC reportado actual; implica reinversión de perpetuidad `g/ROIC=4/15=26,67% de NOPAT`. Verificar ROIC año10→terminal, tasa de capital y convergencia. Pendiente analizar RONIC de inversiones en software, chips e IA.

### 10. Estructura financiera, capital y accionista
[Dato] 2026 caja+valores negociables **136.935**, deuda financiera+arrendamientos en libros **94.479**, patrimonio contable112.093, acciones ordinarias outstanding **14.532,259M**, recompra FY26 **US$86.390M**, dividendos pagados **15.721M**. El puente bruto a equity de +42.456M es **proxy** y depende de caja operativa, valores no corrientes y valor mercado de deuda. Las recompras futuras reducen acciones pero consumen capital; modelar RSU/SBC sin duplicar denominador y no sumar compras como creación automática de valor.

### 11. Gestión, asignación de capital y ejecución
El valor proviene de sostener rentabilidad, no de gastar el máximo. Criterios observables: tasa de I+D que produce servicios/productos escalables, uso de cash vs financiación, precio de recompra y resiliencia de cadena. No asignar un retorno sobre inversiones en IA antes de que haya ingresos/márgenes verificables. Exigir estrategia y desempeño por categorías/mercados de forma contrastable.

### 12. Riesgos materiales y disrupción
[Dato SEC] concentración de ensamblaje y componentes en Asia, litigios/regulación App Store, privacidad y confianza en sistemas IA, limitaciones de capacidad computacional, riesgos tributarios entre jurisdicciones. Riesgos económicos: estancamiento iPhone, nuevas interfaces que reduzcan switching costs, sustitución de búsquedas y pagos, importaciones y FX, variación de gasto computacional y capex. Escenario Disrupción separa pérdida de crecimiento y márgenes; no sumar otra vez al WACC por el mismo riesgo.

### 13. Escenarios y valoración
**Cuatro DCF nativos calculados en la nueva hoja JMR A-1.2**, en US$/acción hoy: Conservadora **108,79** (20%); Base **150,04** (50%); Optimista **184,76** (20%); Disrupción **73,76** (10%, separada de promedio). MOS35% Base US$97,53. Media tres historias renormalizada **148,59**; valor de múltiplos combinados secundario **185,16** y ponderado general hoy **171,11**; horizonte FY+3 del ponderado **236,91** no es valor presente. WACC inicial12,483%, Ke12,616%, WACC terminal9,32%, g4%, ROIC terminal15%, PV terminal54,89% EV. DCF externo anterior (Base US$174,52) queda supersedido y no se usa como valor principal. Falta auditoría económica y pruebas de promoción; no publicar.

### 14. Qué invalidaría la tesis, seguimiento y estado de decisión
Monitorear: crecimiento por categoría y región; márgenes productos/servicios; retención y distribución; I+D ajustada, reinversión y ROIC incremental; evolución de cash/marketables, recompra y RSU; Treasury, ERP y beta; evolución jurídica pagos/App Store. El margen de seguridad se calcula 35% sobre DCF Base **cuando** el DCF nativo esté aprobado. Al 3-nov-2026 estado **CANDIDATO**, no emitir recomendación operativa ni etiqueta auditada. El último precio de cierre de 2-nov es previo a publicación 10-K del 3-nov y debe actualizarse para paridad informativa.

---

## NIVEL 2 — Anexo cuantitativo y reproducibilidad (12 apartados; BORRADOR)

### 1. Identidad, universo y corte
AAPL único ticker, acciones comunes, USD millones, 10-K FY2026 emitido 3-nov, precio cierre 2-nov338,32 (no mismo instante). `revision_id=AAPL-20261103-A12-R1`; `sheet_id=1dEycisHE5Ai34Z50ELOByAiZxub87dPG2TwOmYjS2tA`, 46 tabs.

### 2. Fuentes y clasificación de insumos
Fuente auditada primaria https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm, estados p32/34/36, leases/p47–48, tax/p45, shares/p49; treasury https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/textview?type=daily_treasury_yield_curve&field_tdr_date_value=2026; mercado https://investor.apple.com/stock-price/default.aspx; historia I+D FY2023 https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/aapl-20230930.htm. Todos los datos no confirmados pendientes, nunca 0 por silencio.

### 3. Serie financiera verificada parcial
| USD millones, salvo acciones | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|
| Ingresos | 391.035 | 416.161 | 478.834 |
| EBIT GAAP | 123.216 | 133.050 | 158.063 |
| I+D | 31.370 | 34.550 | 45.765 |
| NI ordinaria | 93.736 | 112.010 | 132.175 |
| CFO | 118.254 | 111.482 | 145.097 |
| Capex físico | 9.447 | 12.715 | 9.041 |
| D&A | 11.445 | 11.698 | 13.423 |
| Acciones (fin de año; M) | 15.116,786 | 14.773,260 | 14.532,259 |
Celdas J/K/L en `Income Statement` y `Cash Flow Statement`. Balance disponible sólo K2025/L2026, F2 completará hasta10FY.

### 4. Conciliación del balance y activos no operativos
[Dato] FY2026 activos404.548=pasivos292.455+equity112.093. Deuda y leasing reconocidos libros94.479, caja actual56.722 y investments no corrientes80.213; valores no corrientes no se duplican. [Cálculo nativo] `Valuation output` EV2.137.998,135M − deuda94.479 + caja56.722 + inversiones80.213 = equity2.180.454,135M /14.532,259M acciones = US$150,042339; `Input!B85=VALIDADO` solo control estructural de no doble conteo. Market value debt78658,118M en WACC, en el puente se descuenta deuda en libros como plantilla: diferencia FV vs contable requiere prueba de materialidad.

### 5. Operación, fiscalidad y FCFF inicial
EBIT/ventas33,00998%, NI margin27,602%; tasa efectiva FY26 27062/159237=16,995%. Tasa marginal federal21% como proxy, no tasa global definitiva. CFO−CAPEX136.056 = flujo accionista previo a estructura de capital, **no** FCFF. FCFF ex ante `EBITaj*(1-T)-[Capex-D&A+ΔNWC+intangibles/I&D+acquisitions]`, no derivado de CFO−CAPEX sin tasas y pagos financieros.

### 6. Capitalización de I+D (fórmula nativa)
`Input!B17=Yes`, `R& D converter!F7=3`. Gasto 2026 45.765, 2025 34.550, 2024 31.370, 2023 29.915; activo investigación `D36=79255`, amort `E36=31945`, ajuste EBIT `D40=13820`, fiscal al21%=2902,2. EBIT ajustado171.883 =35,896% de ventas. Vida2–5 años y efecto ROIC no validados.

### 7. Leases/RSU/Option value
ASC842 lease liabilities14.368 ya en balance. `Input B18=No` para no reconvertir; verificar compromisos todavía no iniciados (SEC644M). SBC FY26 13.789, RSUs futura remuneración24.100 (2,6 años); no imputar stock options inexistentes ni declararlos cero: faltan cantidades y strikes.

### 8. Costo de capital y terminal
`Cost of capital worksheet!B12=Detailed` y `B84=VALIDADO` con costo patrimonio Ke12,615632%, Kd antes impuestos5,31%, deuda mercado78.658M (1,5747% del total), WACC inicial **12,483033%** calculado en `E63` y heredado por `Input B36` y `B14`; WACC terminal9,32%, g4%, ROIC terminal15%. Rf US Treasury4,91% referencial 2-nov-2026 y ERP operativo5,4384%, proxy de interés bruto **2.937M FY2026, NO SEC** en Income Statement L15, plazo deuda10años supuesto y rating Moody Aaa. Kd y riesgo dependen del corte/supuestos; VALIDADO en celda no es 18 candados económicos. No pegar cálculo externo sobre fórmulas.

### 9. Cuatro DCF y puente EV-equity
Para ilustración externa **no oficial** leer `DCF_CONTRASTE_INDEPENDIENTE.md`: Conservadora125,73, Base174,52, Optimista215,80, Disrupción82,46; Base EV2.493.755 M; net cash externo42456 M; acciones14532,259 M; precio MOS113,44. **Hoja JMR nativa sigue N/D** hasta F3.

### 10. Múltiplos FY2026 y objetivos FY+1/2/3
A US$338,32 cierre 2-nov los múltiplos de pantalla del corte difieren de los cierres FY. Históricos al cierre fiscal FY2026 $341,07: P/E**37,98×**, P/OCF**34,16×**, EV/EBITDA**29,12×**; mediana FY2021–25 P/E27,91×, P/OCF24,08×, EV/EBITDA21,66×, calculados por fórmulas. Cinco VP Base hoy de la hoja: EV/EBITDA**200,32**, EV/FCFF**150,86**, P/E**197,63**, P/FCFE**157,12**, P/OCF**171,29**; anclas FY+3 17×/19×/22×/20×/20× son **hipótesis no consenso de pares**. `Financials Multiples` OCF normalizado (≈134.296M) no equivale CFO GAAP FY26 145.097M y requiere conciliación SBC; EV/FCFF y P/FCFE históricos N/D. Cinco matrices de salida5×5 concilian. P/S/P/BV opcionales sin peso.

### 11. Sensibilidades / DCF inverso
Matriz EXTERNA de contraste WACC×ROIC 5×5 centrada174,52 documentada, pero no sustituye las tres 5×5 JMR Base (WACC×g, ROIC×g, crecimiento×margen). A precio338,32, bajo supuestos externos constantes, WACC terminal implícita aprox.6,64% (solo prueba inversa). Evaluar lag0 vs lag1, S/C, tasa tributaria, RSU, caja excedente y duración ventaja antes de declararlas aprobadas.

### 12. Pruebas, divergencias y gates
- Confirmado: copia sin fórmulas reemplazadas en rangos revisados, 46 pestañas, identidad, balance2026, NI/ventas/EBIT FY2026, CFO−CAPEX, R&D converter.
- No demostrado: diez años completos, SEC classifications todas partidas, `inputs_completos.py`, auditorías SEC/ceros, WACC Detailed y puente, `candados.py` 18, `controles_todas.sh`, cuatro DCF de hoja, matrices 5×5 centros, cinco múltiplos, CI, preview y ficha Vercel.
- **Puerta F4 aún cerrada:** 18 candados, controles SEC/cero, `diff_formulas_plantilla.py` y regresión de 138 referencias reancladas, costo de deuda proxy, RSU/SBC, puente económico de OCF/múltiplos, reconciliación hoja↔JSON↔app, preview/CI de publicación: **NO EJECUTADOS O NO CERRADOS**. Cuatro historias nativas, 3 matrices DCF y 5 de múltiplos ya concilian pero eso NO reemplaza los gates. El estado correcto es **CANDIDATO_REVISADO NO PUBLICADO**. F5 auditoría por otra sesión/agente una vez cumplida la publicación EN_REVISION y revisión visual usuario. Consultar `FASE_2_ENTREGA.md`, `FASE_3_ENTREGA.md`, `FASE_4_ENTREGA.md`.
