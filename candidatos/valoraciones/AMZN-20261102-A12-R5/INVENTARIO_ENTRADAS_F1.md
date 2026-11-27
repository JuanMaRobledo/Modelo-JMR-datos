# AMZN R5 — INVENTARIO Y CONCILIACIÓN DE INSUMOS FASE 1 (v27)
**Corte financiero:** 30-sep-2026. **Mercado:** 30-oct-2026. **Moneda:** USD millones (salvo múltiplos, porcentajes y valores/acción). **Revisión:** AMZN-20261102-A12-R5. Hoja: https://docs.google.com/spreadsheets/d/199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I/edit.
**Fuente prioritaria (no R4):** SEC 2026Q3 https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm ; 2025 10-K https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm ; 2024 10-K https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/amzn-20241231.htm ; 2022 10-K https://www.sec.gov/Archives/edgar/data/1018724/000101872423000004/amzn-20221231.htm. Fuentes de tasas: https://aswathdamodaran.substack.com/p/earnings-cashflows-and-stock-prices . Todos los inputs principales tienen nota de celda con procedencia y estatus.
La tabla señala los bloques críticos, no sustituye las notas individuales de cada celda.

| Bloque | Entrada / enlace y tipo | Valor o alcance | Fuente / clasificación / límite |
|---|---|---|---|
| Identidad | `Input sheet!A1,B4,B5,B8,D1` | AMZN, 30-oct-2026, Amazon.com Inc., United States, USD240,35 | Mercado de cierre y SEC, fuente primaria / histórica, no precio actual |
| Resultados | `Income Statement!H3:K22` | FY2022–25, ingresos/gastos/NI y fiscal firmado; cuentas 9M2025=M y 9M2026=N | SEC auditado y Q3; 2022 cargado para cuarto cierre anual |
| LTM | `Income Statement!L3:L22` | ventas797455, EBIT104366, NI134779 | Fórmulas `=FY2025+9M2026−9M2025`; NI incluye ganancias de inversiones NO operativas |
| Capitalización I+D | `Input sheet!F119=25%`, `G120:N122`, `Income Statement!G10:N11`, `R& D converter!F7=5` | Gasto I+D PROXY 25% del SEC technology&infrastructure; activo R&D78943,15 y EBIT ajustado +11136,90 | **JUICIO_PROXY NO DIVULGADO**; 2021/22 dato Tech SEC; corrección simétrica de Other op preserva EBIT SEC. Vida5 años, rango 3–7 |
| CAPEX/FCF | `Cash Flow Statement!H3:L40` | CFO LTM168300, CAPEX bruto −215192, incentivos +4535; FCF bruto −46892, neto incentivos −42357 | SEC; no usar FCFF LTM negativo como múltiplo positivo |
| Balance y apertura | `Balance Sheet!G3:L36` | FY2021 saldo apertura para FY2022, FY2022–25, Sep2026 | SEC. Activos=pasivos+patrimonio, separaciones de deuda corriente, lease, financing obligations reconocidos; no duplicación |
| Deuda contable | `Balance Sheet!L20,L21,L25,L26`, `Input sheet!B16` | **304841 M** deuda y arrendamientos/financing obligations a sep2026 | PUBLICADO+RECLASIFICADO desde SEC; deuda a mercado por tipo NO resuelta |
| Cash/caja | `Balance Sheet!L3:L5`, `Input sheet!B19` | **114226 M** cash+marketable; restricted cash excluida de esas líneas | SEC, distinto de caja utilizada con restricciones |
| NCI/preferentes | `Entradas históricas auxiliares!G4:L5`, `Input sheet!B21,B76` | 0 dentro del puente presentado | Preferentes none issued explícito; NCI sin línea independiente en patrimonio consolidado; juicio de bridge, no demuestra inexistencia de derechos contractuales en inversiones |
| No operativos | `Balance Sheet!L14`, `Input sheet!B82:B87` | **288700 M** Anthropic preferentes92500 + convertibles held146200 + OpenAI pref50000 | VALOR RAZONABLE LEVEL3 estimado SEC (no cash ni activos consolidados); sensibilidad económica. No agregar a FCFF ingresos extraordinarios |
| WACC | `Cost of capital worksheet!B12:B14,B22:B28,B33:B39,G37:H38`, `Input sheet!B35:B36` | Detailed, multibusiness Retail General+Computer Services, beta bottom-up y deuda con rating AA; WACC fórmula **8,1796%** | Damodaran Sept30 Rf5,29%+ERP3,70%, precio Oct30; sector proxy y geografía pendientes auditoría |
| Terminal | `Input sheet!B46:B49, B65:B69`, `Escenarios e historias!N5:N8,M29/M53/M77/M101` | WACC beta1 =8,99% por fórmula; g, ROIC por historia | HIPÓTESIS, WACC>g, g≤Rf |
| Leases | `Input sheet!B18=No`, BS `L21,L26`, `Operating lease converter` | No conversión INCREMENTAL; pasivos ASC842 ya en BS, PV ~114783 M | SEC nota 3, no significa leases cero |
| Rating | `Cost of capital worksheet!B34,B36`, `Synthetic rating` | Rating S&P AA, Damodaran lookup Aa2/AA | Deuda mercado C54 trata libro como un solo bono; diferencia material; issue motor #197 |
| Opciones propias | `Input sheet!B38=No`, `Option value!B9=0` | N/A opciones sobre acción Amazon; 0 dividendo | SEC Stock Award Plans centrado en RSUs, NO significa RSUs=0; warrants sobre terceros son activos, no opciones sobre acciones propias |
| RSU/SBC | `Input sheet!F126:F132` | RSU223,3M, acciones10811M, exposición máxima 11034,3M; SBC LTM19873M; no reconocido22300M; vest2027 99,4M | SEC 2026 Q3 Note Stock Awards. Dilución mecánica total ~146,17 vs DCF Base149,19; NO oficial por doble conteo potencial |
| NOL/impuestos | `Input sheet!B25,B62,B89:B92` | marginal 25% juicio (21% federal + supuesto estados/extranjero); NOL utilizable consolidado no modelado | NO significa NOL históricos inexistentes; fiscal 2026 GAAP distorsionado inversiones |
| Proyección | `Escenarios e historias!B5:N8,C29:M101` | 4 historias probabilidades 45/22,5/22,5/10 y crecimientos anuales explícitos | JUICIO; deben contrastarse con F2/F3, no sacados de R2/R3 |
| EV/EBITDA | `EVEBITDA!J8,J19,J30` | 16,62x/18,46x/20,31x; VP FY+3 Base **349,74** | MEDIANA 4 cierres FY2022–25 ×9/10,1,11/10; no etiqueta valor definitivo por deuda/lease y CAPEX |
| P/OCF | `POCF!J8,J19,J30` | 15,15x/16,83x/18,52x; VP FY+3 Base **179,15** | MEDIANA 4 cierres 2022–25; OCF no incluye reinversión y puede sobrestimar en Amazon |
| EV/FCFF | `EVFCFF!J8/J19/J30` | **N/A Base y Conservadora** | FCFF proyectado FY+3 Base **−6371,92 M**, no valorar flujo NEGATIVO usando múltiplo positivo. Optimista FY+3 positivo, todavía sin ancla aprobada |
| P/E | `PE!J8/J19/J30` | **PENDIENTE** | FY2022 NI negativo, 3 cierres positivos; 2025/26 ganancias fair value Anthropic NO recurrentes contaminan NI y proyecciones; corregir normalización económica en F3 |
| P/FCFE | `PFCFE!J8/J19/J30` | **N/A / PENDIENTE** | Con apertura correcta 2021, FY2022 P/FCFE **−65,43x**, FY2023 193,45x, FY2024 78,48x, FY2025 57,48x: solo tres positivas y alta varianza; no forzar ancla. Bug transversal issue #199 |
| Sensibilidad DCF | `Sensibilidad DCF!B12,B23,B34` | 3 centros **OK** | Fórmulas 5×5 Base, no prueba independiente de supuestos |
| Sensibilidad múltiplos | `Sensibilidad por múltiplo` | EVEBITDA y POCF Base 5×5 generan centros VP3 | No presentar matrices inválidas de denominadores negativos como completadas |
| Pesos | `Resumen de Valoración!G3=Crecimiento`, `B6:B11` | Perfil normativo: 60% DCF, 10% EVEBITDA, 15% EVFCFF, 5% PE, 5% PFCFE, 5% POCF | **NO calcular precio objetivo global ponderado**: métodos con peso >0 carecen de salida válida; `Resumen!D12` en blanco como gate correcto |
| Fuente de valores | `Valuation output!B35`, `Escenarios e historias!H5:H8` | Base149,1915; cons81,0095; disrup62,4357; optim241,8435; MOS35%=96,9745 | Fórmulas nativas, no precios pegados |
| Test oficial | `estados_completos.py`, `auditar_estados_sec.py`, `auditar_ceros_materiales.py`, `diff_formulas_plantilla.py`, `candados.py`, `controles_todas.sh` | **NO EJECUTADOS** con entorno motor autenticado | Direct check Sheets por API es equivalente parcial, no afirmar CI integral |

## Validaciones directas (no confundir con gates)
- 7/7 resultados FY2022–25 + LTM + 9M2025/26: `Ventas−COGS−SG&A−I+D económica−otros gastos=EBIT`, diferencia 0 USD M.
- 5/5 CFO, 5/5 CFI y 5/5 caja de FY2022–25 + LTM al introducir cambio FX, diferencia 0 USD M.
- 5/5 balance FY2022–25 + sep2026: activos corrientes, totales, pasivo corriente, activos=pasivos+patrimonio todos diferencia 0 USD M. FY2021 balance apertura también concilia 0.
- Copia desde plantilla oficial IA (46 pestañas), ningún dato heredado de R4, 4 historias K5:K8 LISTO, controles Input/WACC/Tax/R&D/RSU y tres matrices DCF OK. Fórmula fiscal TAX-194 estaba corregida en plantilla IA, fuente GI.
- La auditoría de dependencias detectó ancla inicialmente falsa de P/FCFE por balance apertura en blanco (sheets convertía vacío en 0). Se cargó FY2021 desde SEC y ratio FY2022 cambió a **−65,43x**; se descartó ancla PFCFE y abrió bug motor https://github.com/JuanMaRobledo/JMR-valuation/issues/199, prueba de que «fórmula calculada» no implica dato verificable.
- `R& D converter` sensibilidad REAL ejecutada con F119=15%→DCF Base148,4858 y asset47365,89; 25%→149,1915 y asset78943,15; 40%→150,2500 y asset126309,04. **Restaurado al 25%**. Efecto ≈US$1,76 por acción, pero proxy no se certifica como I+D real.
- Ilustración analítica de inversiones no operativas: haircut 25% en US$288700M = −US$6,68 por acción, haircut40%=−US$10,68 por acción, ceteris paribus, **sin recalcular** WACC ni impuestos. No es un escenario oficial.
- Dilución mecánica full RSU (sin doble conteo de SBC) a 11034,3M acciones ~US$146,17 frente a149,19 Base; no es valoración principal.

## Salvedades para continuar
1. **Deuda mercado y WACC:** C54 usa bono único para deuda contable304841, estima mercado≈180382. SEC notas tienen FV145400, term loan17500, leases114783, financing obligations9726, más partidas menores; estimación alternativa287409 antes de conciliar. DCF usa libro304841 para bridge, NO C54. No atribuir error directo de USD107027M al equity (issue #197).
2. **I+D:** Amazon no divulga como partida independiente; 25% de tecnología es PROXY discutible y no se puede certificar en F1. Revisar inversión económica y vida útil F3, sin hacer pasar hipótesis por dato.
3. **No operativos:** participaciones Level3 ilíquidas Anthropic/OpenAI 288700M, derechos, valor y fiscalidad inciertos, doble conteo potencial con relaciones comerciales AWS. F3 sensibilidad obligatoria.
4. **FCFF/capex:** CFO168300 y capex bruto215192, FCF bruto−46892, neto incentivos−42357. Forecast FY+3 FCFF negativo Base, EV/FCFF N/A. S/C marginal del DCF requiere F3 revisión de CAPEX 2027 anunciado.
5. **P/E y FCFE:** signos históricos fiscales correctos pero net income FY2025/26 distorsionado por revalorización de inversiones, proyecciones no depuradas. P/FCFE requiere tratamiento histórico/apertura y riesgo de doble contar préstamos/leases; bug #199.
6. **RSUs:** 223,3M outstanding, emisiones futuras, unrecognized SBC, riesgo de doble conteo con FCFF y denominador. Modelar uso anual y márgenes por método F3.
7. **Cobertura F2:** completar FY2016–2020 estados, varios auxiliares, precios FY y revisión NIIF/SEC, sin reemplazar validaciones F1 ni reciclar R4.

**Estado:** F1 tiene DCF candidato calculado + evaluación de los cinco múltiplos, pero **no está económicamente auditada ni publicable**. Pasar a F2 como CANDIDATO con estas reservas y cerrar los controles técnicos/materiales antes de F4; F5 auditoría guiada por usuario.


## Cierre operativo post F2 (03-nov-2026): CAPEX y cohorte sectorial

**Documentos nuevos de referencia:** [NORMALIZACION_CAPEX_Y_JUSTIFICACION_DCF.md](NORMALIZACION_CAPEX_Y_JUSTIFICACION_DCF.md) y [CIERRE_OPERATIVO_F1_F2.md](CIERRE_OPERATIVO_F1_F2.md). Estas comprobaciones actualizan las RESERVAS de la primera entrega, no sustituyen ni falsean la fuente contable.

- Incorporado en la misma hoja R5 `Input sheet!A159:B207`: puente de CFO168300, CAPEX bruto215192, proceeds/incentivos4535, CAPEX neto210657 y FCF Amazon **−42357 millones USD LTM**, con AWS 147236/196910 millones de adiciones PPE 9M (~74,77%) y DA PPE 41845 (datos de cortes distintos, no sumar). No existe desglose reportado mantenimiento/crecimiento: el uso de DA PPE como proxy NO autoriza reescribir FCFF ni añadir CAPEX sobre reinversión Sales-to-Capital.
- En S/C Base `Escenarios e historias!E5` probados **0,50→DCF128,7214**, **0,55→134,8117**, **0,72→149,1915**, **0,90→158,4961** con primer FCFF **−79108/−63175/−25555/−1213** M. Se **RESTAURÓ 0,72** y tres centros 5×5 quedaron OK. Guía de CAPEX 2027 mayor que FY2026~220000 M hace prudente no normalizar crecimiento para maximizar precio.
- Se completó `Sector!A3:X7` con **cinco referentes**: Microsoft, Alphabet, Oracle para nube/tecnología y Walmart, Costco para retail; fuente 10-K, ingresos recientes, EBIT, 3Y/5Y, EBITDA/operating margin sin inventar cotizaciones ni múltiplos; `Crecimiento y Márgenes!C15:E20` ahora calcula los cuartiles y medias. Cohorte mixta orientativa, no comparables económicos exactos AWS ni precio por múltiplos autorizado. Mediana margen EBIT 30,59% no es margen objetivo Amazon; márgenes por historia se mantienen.
- Lectura de **15/15 estados de candados** de la plantilla en niveles aceptados (LISTO/VALIDADO/NO APLICA). Es lectura de valores por API, **NO es ejecución de `candados.py`**. Los scripts oficiales (including `inputs_completos.py`, `auditar_estados_sec.py`, `auditar_ceros_materiales.py`, `diff_formulas_plantilla.py`) **NO EJECUTADOS**, GitHub PR #234 sin CI detectado en head consultado.
- **Dictamen actualizado:** cierre de CAPTURA y conciliación directa F1/F2 como **CANDIDATO CON RESERVAS**, NO `CERTIFICADO`, NO cierre de gate técnico ni valoración económica final. Pendientes deuda mercado/ASC842 #197, FCFE primera apertura plantilla #199, control full F1 #200, PE/EVFCFF/SBC/no operativos, riesgo de S/C2027 y suite oficial. Estas reservas deben quedar explícitas en la promoción F4; no se fusionó ni publicó.
