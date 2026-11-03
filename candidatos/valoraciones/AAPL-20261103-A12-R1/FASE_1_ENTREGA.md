> **ACTUALIZACIÓN 03-nov-2026 — DCF y WACC resueltos aritméticamente después de F1.** Este archivo preserva la foto original de Fase 1, cuando los nativos aún eran PENDIENTE y el escenario externo ilustrativo daba US$174,52. La revisión actual calculada en la hoja 46 pestañas es **DCF Base US$150,042339, MOS35% US$97,527521, WACC Detailed inicial12,483033% y cinco múltiplos nativos calculados**. Referencia oficial al estado ACTUAL: `FASE_3_ENTREGA.md`; controles integrales aún NO EJECUTADOS. No publicar ni usar contraste externo como valoración oficial.

# AAPL · AAPL-20261103-A12-R1 · FASE_1 · CERRADA CON CONTROLES PENDIENTES

- Fecha de ejecución: 3-nov-2026 · Método **A / A-1.2** · Emisor Apple Inc. (NASDAQ: AAPL), USD millones y millones de acciones.
- Estado **CANDIDATO_VALORACION_INICIAL**, **NO PUBLICADO, NO CERTIFICADO**. Esta entrega documenta avance y reservas; **no** constituye valor oficial JMR.
- Ejercicio FY2026 terminado **26-sep-2026**; formulario 10-K **presentado 3-nov-2026**; precio de contraste **US$338,32, cierre 2-nov-2026**, deliberadamente ANTERIOR al documento 10-K, útil solo como último cierre confirmado; se debe sincronizar corte de precio con el informe antes de promover.
- `sheet_id`: `1dEycisHE5Ai34Z50ELOByAiZxub87dPG2TwOmYjS2tA` · [Hoja candidata](https://docs.google.com/spreadsheets/d/1dEycisHE5Ai34Z50ELOByAiZxub87dPG2TwOmYjS2tA/edit) · ruta Google Drive `AAA Finanzas/Análisis/AAPL/`.
- Plantilla IA canónica del 22-oct-2026: **46 pestañas**, fórmula/estructura copiada; hoja AAPL histórica **61 pestañas**, preservada, no reutilizada.
- Ejecutor: ChatGPT **GPT-6**, razonamiento; conectores GitHub/Google Drive, Python para contraste aritmético. Esfuerzo de configuración no observable, **NO DETERMINABLE**.
- **PASOS: 7/7 examinados, 1/7 íntegramente comprobado, 6/7 parciales o pendientes**. AISLAMIENTO=OK (copia nueva; cero valores transplantados de otra empresa; historia antigua conservada).
- Fuente principal: [Apple SEC 2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm) (p.32 estados de resultado, p.34 balance, p.36 flujos, p.45 impuestos, p.47–48 arrendamientos, p.49 acciones y RSU). Es obligatorio cotejar cada clasificación fina con esta fuente antes de declaración de fase completa.

## Hecho y comprobado

1. **Identidad, estructura y aislamiento APROBADO**: carpeta AAPL creada; copia nueva separada, 46 hojas; `Input sheet!A1=AAPL`. Ninguna alteración de fórmulas/plantilla compartida.
2. **Resultados SEC PARCIAL**: `Income Statement!J:L` permite FY2024–2026: ingresos 391.035/416.161/478.834; EBIT GAAP 123.216/133.050/158.063; gastos I+D 31.370/34.550/45.765; SG&A 26.097/27.601/29.774; utilidad neta 93.736/112.010/132.175. Se utiliza L como LTM=FY2026 y K como año comparativo FY2025; **no** atribuir a K el FY2026 ni duplicar la I+D FY2026. `Input sheet!B12=478834`, `B13=158063`; margen EBIT GAAP FY26 = 33,00998%. Fuente 10-K SEC. FY2023 I+D 29.915 en `Income Statement!I10` de 10-K 2023: https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/aapl-20230930.htm.
3. **Balance SEC PARCIAL**: `Balance Sheet!K:L` FY25–26: efectivo y valores corrientes 56.722 (2026), valores no corrientes 80.213, patrimonio 112.093, pasivos por deuda y leasing 94.479, activos 404.548 = pasivos 292.455 + patrimonio 112.093. `Input sheet!B16=94479`, `B19=56722`, `B22=14532.259` millones de acciones al cierre FY2026. **Importante**: activo NO operativo a valor razonable no ha pasado la puerta `Input!B83:B87`; no sumar 80.213 al equity nativo sin conciliación.
4. **Flujos SEC PARCIAL**: `Cash Flow Statement!J:L` FY24–FY26, CFO 118.254/111.482/145.097; capex -9.447/-12.715/-9.041, D&A 11.445/11.698/13.423; SBC 11.688/12.863/13.789; recompras de capital 94.949/90.711/86.390. `L36=136056` millones = CFO − CAPEX **no es FCFF Damodaran**.
5. **I+D material**: se activó `Input sheet!B17=Yes` y `R& D converter!F7=3` años de amortización como **JUICIO PROVISIONAL** (tecnología de consumo); 2023–2026 I+D separado. Fórmulas nativas `R& D converter!D36=79255` activo investigación; `E36=31945` amortización; `D40=+13820` ajuste EBIT, `D41=2902,2` ajuste fiscal al 21% federal provisional; EBIT ajustado 171.883, margen 35,896%. Sensibilizar vida 2–5 años y ROIC ajustado.
6. **Arrendamientos**: `Input sheet!B18=No` (no convierte obligaciones ya capitalizadas) por pasivos total 14.368 en SEC FY26 bajo ASC 842; incluidos en `Balance Sheet!L21+L26` y deuda de `Input sheet!B16`. Falta cotejo de 644M de contratos no iniciados y la deuda de mercado; no duplicar.
7. **Tasa y precio**: `Input sheet!B25=21%` estatutaria federal como juicio de entrada sujeto a ajuste por perfil internacional; efectiva FY26 17,0%. `B89=Convergencia Damodaran`. `B35=4,91%` Treasury 10 años, 2-nov-2026; `D1=338,32` cierre 2-nov. Source https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/textview?type=daily_treasury_yield_curve&field_tdr_date_value=2026 y https://investor.apple.com/stock-price/default.aspx.
8. **WACC nativo** `Cost of capital worksheet!B12=Detailed`; no se ha completado beta bottom-up, ERP por regiones/fecha, rating, costo de deuda ni `E63/B14/Input!B36`. **CONTROL NO EJECUTADO/INCOMPLETO**. Los supuestos 9,45% inicial y 9,32% terminal en el archivo `DCF_CONTRASTE_INDEPENDIENTE.md` **son juicios para una comparación externa, no la salida de esta hoja**.
9. **Opciones/RSU**: el 10-K informa SBC 13.789, RSU no reconocidas 24.100 a reconocer 2,6 años; falta stock options cuantificadas (si hay), las opciones se restan una sola vez en `Option value` y RSU/SBC se modelan separadamente. `Input!B38:B42` N/D por falta de recuento/strikes, **NO se pusieron en cero**.
10. **Reinversión**: CAPEX físico, D&A y Δcapital trabajo no equivalen a reinversión económica ajustada. `S/C incremental` no es `Ventas/Capital` promedio. A modo de diagnóstico con inversión R&D, patrimonio, deuda y efectivo, FY25 capital ajustado aprox.119.125, FY26 148.892; Δventas 62.673/Δcapital 29.767 ≈ **2,106**; este cociente es sensible al puente contable, no suficiente para aprobar el supuesto Base. No se alteró `Supuestos Recomendados` sin anclas verificadas.

## Insumos por celda: tipo, control y fuente

| Hoja/celda | Tipo | Dato/unidad/fuente | Estado |
|---|---|---|---|
| Income Statement!L3 | PUBLICADO | 478.834 USD M, SEC 10-K p32 FY26 | APROBADO puntual |
| Income Statement!L12 | PUBLICADO | EBIT 158.063 USD M, SEC p32 | APROBADO puntual |
| Income Statement!L10 | PUBLICADO | I+D 45.765 USD M, SEC p32 | APROBADO puntual |
| Income Statement!L22 | PUBLICADO | NI ordinaria 132.175 USD M, SEC p32 | APROBADO puntual |
| Income Statement!L27 | PUBLICADO | Acciones en circulación FY26 14.532,259 M, SEC notas equity | APROBADO puntual |
| Balance Sheet!L20:L26 | PUBLICADO/RECLASIFICADO | Deuda & leases, SEC p34, p47 | PARCIAL: puente a FV |
| Cash Flow Statement!L13,L15,L4,L5 | PUBLICADO | CFO, CAPEX, D&A, SBC, SEC p36 | APROBADO puntual |
| Input sheet!D1 | PRECIO MERCADO | 338,32 USD 2-nov, anterior a filing 3-nov | PARCIAL corte |
| Input sheet!B35 | TASA | Treasury US10Y 4,91% 2-nov | PARCIAL ERP/beta |
| Input sheet!B25 | JUICIO_PROXY | 21% federal marginal, perfil mundial a conciliar | RESERVA MATERIAL |
| Input sheet!B17; R& D converter!F7 | JUICIO_PROXY | Yes; 3 años, tasa amortización | PARCIAL vida útil |
| Input sheet!B18 | NO_APLICA (incremental) | No: ASC842 reconocidos, SEC leasing | PARCIAL contratos no iniciados |
| Input sheet!B38:B42 | PENDIENTE | Opciones con strikes/plazos; RSU separado | BLOQUEANTE si material |
| Input sheet!B82:B87 | PENDIENTE | Valores negociables fuera de operaciones, FV/solape | BLOQUEANTE puente equity |
| Cost of capital worksheet!B22:B38, E63 | PENDIENTE | Beta bottom-up, ERP, Kd/rating, geografía | BLOQUEANTE WACC nativo |
| Financials Multiples; PFCFE; POCF; EVEBITDA; EVFCFF; PE | PENDIENTE | FY+1/2/3, anclas/VP y comparables | BLOQUEANTE cinco métodos |
| Escenarios e historias; Sensibilidad DCF | PENDIENTE | Cuatro DCF nativos y matrices 5×5 de centro exacto | BLOQUEANTE promoción |

## Drivers Base: anterior → propuesta de CONTRASTE externo (NO pegada en hoja)

No existe revisión oficial previa AAPL en `registro/DRIVERS.md` ni `catalogo.json`. **Anterior N/D**, no reutilizar hoja histórica de 61 pestañas.

| Driver | Anterior | Juicio externo provisional | Fundamento y reserva |
|---|---:|---:|---|
| CAGR ventas 1–5 | N/D | 7,0% | FY26 +15,1% no perpetuo; servicios +12,96%, hardware maduro; validar drivers sector/volumen |
| Margen EBIT terminal ajustado | N/D | 35,5% | 35,90% EBIT ajustado FY26; mix servicios y escala vs costos AI |
| S/C marginal 1–5 | N/D | 1,80× | contrasta con estimación histórica corta ~2,106×, no ancla definitiva |
| S/C marginal 6–10 | N/D | 2,00× | productividad incremental sostenible: reserva por inversiones IA |
| WACC inicial | N/D | 9,45% | **solo contraste**, no certificado como WACC Detailed |
| WACC terminal | N/D | 9,32% | **solo contraste**, pendiente coherencia Rf/ERP/beta y ponderaciones |
| g terminal | N/D | 4,0% | techo 4,91% Treasury; reserva corte actualizado |
| ROIC terminal | N/D | 15,0% | exceso ~5,7 pp sobre costo, ventaja durable hardware+servicios, prueba independiente pendiente |

## Estados de controles

- APROBADO: aislamiento, copia 46 pestañas y fórmulas presentes en rangos inspeccionados; igualdad libro FY26 404.548=292.455+112.093; cálculo EBIT FY26; CFO−capex; R&D converter.
- PARCIAL: clasificación de CFO/SBC/arrendamientos; comparación FY24–FY26; evidencia de vida útil; puente deuda/caja; coherencia del precio de corte.
- NO EJECUTADO: `scripts/inputs_completos.py`, `scripts/estados_completos.py`, `scripts/auditar_estados_sec.py`, `scripts/auditar_ceros_materiales.py`, `scripts/diff_formulas_plantilla.py`, `scripts/controles_todas.sh`, `scripts/candados.py` (18), gates del JSON/CI y comparaciones 5×5 nativas; **no afirmar resultados**.
- **No se han completado cinco múltiplos, cuatro escenarios en hoja, ni WACC de fórmula. DCF de contraste no es salida oficial ni apto para publicación.**

## Bloqueos materiales

1. Normalizar tasas Damodaran y beta bottom-up por negocios/geografías, rating/Kd/financiación, obtener WACC nativo con `B14=E63=Input!B36` y WACC terminal > g.
2. Completar auditoría de tasas fiscales, métodos ASC842 y deuda FV, inversiones no operativas a FV sin doble conteo.
3. Dilución opciones/RSU, capital & activos operativos, S/C marginal 0/1 lag, ROIC/RONIC, impuesto y superposición de cash flows.
4. Cargar histórico comparativo 10 años (F2) y anclas FY+1/2/3 para cinco múltiplos.
5. Escribir supuestos como entradas en la copia, comprobar escenarios/terminal nativos, DCF inverso y tres matrices DCF 5×5+matrices múltiplos, 18 candados y tests CI antes de F4.
6. Datos y precio no comparten exactamente el instante (cierre previo vs 10-K presentado al día siguiente); normalizar corte.

## Insumos para siguiente fase

- Hoja viva y registros SEC en cada celda; el archivo de contraste `DCF_CONTRASTE_INDEPENDIENTE.md`, con valores provisionales, no sustituye cálculos.
- F2: SEC FY2017–2023 completos; deuda/leases/NI/CFO/capex por ejercicio, precios fechados y splits, tests contables; conservar la copia limpia.
- F3: supuestos recalibrados con cohortes y tasas, documentación `antes→después→celda→impacto`; hasta entonces estado **CANDIDATO**.
- F4: análisis narrativo y cuantitativo y publicación **solo con gates verdes**, reconciliación hoja↔JSON↔app y prueba real en Vercel. No publicar mientras las salvedades anteriores sigan materiales.
