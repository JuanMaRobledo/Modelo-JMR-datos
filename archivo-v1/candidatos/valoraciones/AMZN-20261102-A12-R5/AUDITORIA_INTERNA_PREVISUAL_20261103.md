# AMZN R5 — Dictamen de auditoría interna y lista de revisión visual
**Fecha:** 2026-11-03 · **Candidato:** AMZN-20261102-A12-R5 · **Corte mercado:** 2026-10-30 · **Corte financieros:** LTM 2026-09-30 · **No certificado, no publicado**.
Hoja candidata: https://docs.google.com/spreadsheets/d/199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I/edit. Datos PR #234, motor PR #203 y propuesta de proceso PR #172 en borrador.

## Dictamen ejecutivo
**APTO PARA REVISIÓN VISUAL COMO CANDIDATO CON RESERVAS; NO APTO PARA PROMOCIÓN/PUBLICACIÓN.** La aritmética DCF Base reproduce US$149,1914858/acción y MOS35%=US$96,9744657; las tres matrices 5×5 tienen centro OK. Las reservas económicas cuantificadas (CAPEX/S-C, terminal, descuento y Level3) son **materiales**, independientes del hecho de que los controles estructurales den verde. Mantener valor sin retocar supuestos para aproximar cotización.

## 1. Auditoría interna numérica independiente — efectuado en esta revisión
- Lectura efectiva de `Valuation output!C9:L16,B18:B35` y nuevo cálculo externo a sus fórmulas:
  - 10 identidades `NOPAT−reinversión=FCFF`: error máximo **0** a la precisión capturada.
  - 10 `FCFF×factor descontado=VPFCFF_t`: error máximo **0**.
  - VP 10 años **321020,81496489746** M; VP terminal **1193803,3375394288** M; EV **1514824,1525043263** M.
  - Bridge **EV − deuda304841 + caja114226 + nonop288700 − opciones0 = equity1612909,1525043263** M; acciones10811 M; DCF **149,19148575564947**.
  - Participación terminal en EV **78,808%**: concentración de hipótesis relevante.
- Lecturas después de corregir visibilidad: `Valuation output!B35=149,19148575564947` y `Escenarios e historias!H5:H8` = 149,1915 /81,0095/62,4357/241,8435. Estas pruebas son aritméticas; no convierten WACC, I+D, CAPEX o participaciones en precios auditados.

## 2. Resolución de 11 filas señaladas por validador histórico
Se inspeccionaron hojas, fórmulas y notas de celda: los 11 hallazgos no son once cifras que deban rellenarse con ceros.
| Hoja / fila | Situación contable y decisión de auditoría |
|---|---|
| Income Statement!9 G:L D&A | Amazon no separa D&A como gasto dentro del estado de resultados; figura en CF!4. No restar dos veces del EBIT; notas explícitas I:L; verificar G:H en perfil. |
| Balance Sheet!8 G:L Receivables | `Accounts receivable, net and other` agregado está en BS!6. BS!7 sin subdesglose hace que la fórmula de subtotal 8 devuelva blanco. No fabricar 'trade AR'. |
| Balance Sheet!12 G:L Net intangibles | Goodwill y otros activos reportados en distintos epígrafes; sublínea no desglosada. Sin prueba de valor separado; N/D, no cero. |
| Balance Sheet!14 G:I Long-term investments | Valores actuales de Anthropic/OpenAI FY2024→2026 identificados, previos en Other assets sin apertura homogénea. **Pendiente SEC secundario**, no asumir ausencia total. |
| Balance Sheet!23 G:L Other current liabilities | Total y componentes SEC agregados en accrued/otros, ya conciliados; línea residual no informada individualmente. |
| Balance Sheet!28 G:L Total LT liabilities | Subtotal derivable como total liabilities − current liabilities, no impreso por Amazon. **No sustituir dato auditado ni editar con conjeturas**. |
| Cash Flow Statement!29 G:L Issuance common shares | No hay subtítulo cash explícito homogéneo, distinguir SBC de efectivo. **Pendiente secundario** por FY. |
| Cash Flow Statement!30 G,I:L Repurchases | FY2022−6000 M está registrado. Para los demás períodos ausencia de línea no demuestra automáticamente cero. **Pendiente secundario** por año. |
| Cash Flow Statement!31 G:L Net issuance/repurchases | Derivado no computable hasta conciliar emisiones/recompras; no alimenta DCF FCFF. |
| Cash Flow Statement!32 L Dividends paid | Amazon históricamente no distribuye dividendos ordinarios; 2016–25 =0 con fuente, LTM sin fórmula demostrada. Clasificación N/A documentada; **no rellenar sin fuente temporal**. |
| Cash Flow Statement!38 G:L Levered FCF | No es renglón GAAP estándar; no confundir con FCF cash reportado ni FCFE Damodaran. Derivado no presentado. |

El motor PR203 tiene ahora `reference/candidate_profiles/AMZN_R5_HISTORY.json` y `candidate_history_coverage.py`, que exigen lista de renglones materiales numéricos, identidades de ticker/hoja/corte, fuentes SEC, excepciones por columnas y estado `PASS / PASS_CON_SALVEDADES / FAIL`. El perfil separa tres pendientes secundarios: inversiones históricas FY2021-23, emisiones y recompras cash. **Aceptar secundarios como tarea abierta no equivale a aprobar información material faltante**. No cambiar números solo para volver verde un control entre compañías.

## 3. Las 20 diferencias SEC: clasificación y test
- **11 impuestos:** `IncomeTaxExpenseBenefit` XBRL positivo para gasto, mientras `Income Statement!row20` registra gasto con signo negativo/beneficio positivo. El valor económico puede conciliar por inversión de convención; no invertir dos veces en hoja.
- **8 EPS FY2016–19:** SEC muestra EPS pre-split 20:1; la hoja tiene precios y EPS comparables post-split. Hay redondeos; verificar año/fecha, no multiplicar indiscriminadamente FY2020+.
- **1 PPE LTM:** el primer cotejo comparó saldo Sep2026 **508862 M** con Dec2025 **357025 M**, períodos diferentes. SEC 2026Q3 informa explícitamente ambos; no es error de balance.
Motor PR203 incorporó perfil explícito `AMZN_R5_SEC.json` para estas convenciones y salida `_conciliaciones.json` con conciliados/pendientes. **Su adopción queda sujeta a la ejecución autenticada más reciente y a comprobar sus resultados; un script con exit 0 no sustituye inspección del JSON.**

## 4. Fiscalidad y controles de fórmulas después de reparar
Relectura de las fórmulas R5 verificó:
- `POCF!B8` y `PFCFE!B8` usan `+ Income Statement!H20` (impuesto ya firmado), no `−H20`; `EVFCFF!B8` usa `1+H20/(H12+H18)`; `Income Statement!H29` usa `−H20/H19`.
- `Synthetic rating!D14:D17` tiene guardas para rama inactiva, que no deben activar un spread ficticio. Rating efectivo sigue AA.
- `POCF!J19=19,6146907x`, distinto de 16,833x de entrega antigua. El ancla de VP Hoy Base actual P/OCF ~190,40, no reemplazar por la anterior 179,15. Queda control de múltiplos y pertinencia.
La inspección de fórmulas **no certifica** comportamiento para todas las firmas con pérdidas fiscales, por lo que el PR de motor y pruebas de signos sigue como puerta estructural.

## 5. Auditoría de tesis, calidad y materialidad
- **Material económico 1:** CAPEX neto LTM210657 M vs CFO168300 M, FY2026 cash capex guiado ~220000 M y mayor inversión esperada FY2027; S/C Base0,72 puede subestimar capital requerido. Rango de estrés Base128,72–158,50 (S/C0,50–0,90). Material.
- **Material económico 2:** descontar a WACC8,1796% y g4% con 78,808% valor terminal; ±50pb de WACC ⇒ Base133,45–168,51. Material.
- **Material económico 3:** reservas sobre Anthropic92.500+146.200/OpenAI50.000 =288700 M Level3 no operativos; posible descuento 25% baja ~6,68 USD/acción. Material.
- **Material económico 4:** ROIC terminal11,5%, margen objetivo15,8%, distinta sostenibilidad de 3 negocios, deuda mercado y ERP regiones sin sensibilidad conjunta completa. No etiquetar `certificado`.
- P/E no normalizado (NI LTM134779 distorsionado por inversiones); EV/FCFF y P/FCFE pueden permanecer N/A mientras sus bases prospectivas sean negativas. **Los múltiplos secundarios NO sustituyen el DCF principal.**

## 6. Control visual del candidato — trabajo realizado en la hoja, NO en aplicación de producción
1. `Origen de los Supuestos!B23:D24` enlazado de nuevo a `Escenarios e historias!E5:F8`: S/C **Conservador0,52→1,25; Base0,72→1,65; Optimista1,15→2,10**. Antes la vista mostraba los tres **2,7255**, una referencia de sector incorrectamente presentada como driver. El DCF Base quedó inalterado tras la escritura.
2. `Tesis de Inversión y Supuestos!A1:A2,A5:A6,A8:A11,D8:D11,B15:E21,A28,B32:C34,A37` reemplazó placeholders con narrativas y fórmulas ligadas a la hoja viva. Renglones crecimiento **8%/11%/14% año1** y **7%/8,87%/13% años2–5** contrastados contra `Escenarios C53/D53,C101/D101` e Input B27/B29; formatos de porcentaje aplicados y alturas de filas adaptadas.
3. `Tesis!E25:E27` ya no presenta falso **−100%** cuando el ponderado FY+3 está pendiente; fórmula guarda `ISNUMBER(Cn)` y devuelve blanco. El DCF/mercado sí aparece correctamente como Cons **−66,3%**, Base **−37,9%**, Opt **+0,6%**.
4. `Origen!A5` identifica **DCF Base hoy como valor principal** y múltiplos como secundarios. `Supuestos Recomendados!B53` clasifica Amazon como negocio operativo multinegocio (no financiero).
5. Se releyeron resultados y fórmulas tras las escrituras; `Valuation output!B35` **149,19148575564947** persistente. Estructura: **46 pestañas**, sin borrados ni cambios en plantillas maestras.
6. **Límite de QA visual:** revisión de formato y contenido vía API de Sheets, no captura renderizada de navegador. El usuario debe inspeccionar en Google Sheets disposición/recorte en móvil y escritorio, sensibilidad 5×5, indicadores de estado y encabezados. No se declara auditoría visual presencial completada.

## 7. Pruebas técnicas / puerta de publicación
- Evidencia oficial anterior: motor Action `41609454032`, **40/40 regresiones** aprobadas, candados 15/15, insumos obligatorios 0, alertas ceros0; faltaban 11 filas (control genérico), 20 avisos SEC y suite integrada R5.
- Nueva revisión de motor PR203 incluye perfiles de cobertura y convenciones SEC y nuevos tests automáticos. **A la hora de redactar este documento, la corrida autenticada `41638493874` estaba en curso**; actualizar el dictamen con su resultado exacto, no adivinar.
- `controles_todas.sh` sigue sin homologación de identidad candidata en TODOS los consumidores (probabilidades, supuestos, catálogo, JSON, integridad); no ejecutarla contra R2/plantilla para marcar R5 verde.
- Falta snapshot inmutable SHA/hash de fuentes y fórmula (contrato piloto PR172). Hasta instalarlo no se ha demostrado reproducibilidad operativa automática repetida, pese a reproducción numérica puntual.
- **Publicación prohibida** hasta resolver bloqueos materiales económicos, controles técnicos y reconciliación candidato hoja→motor→JSON→app. No fusionar PR #234/203 en estado fallido. El usuario puede revisar el candidato y dejar observaciones sin que se convierta en producción.

## 8. Lista precisa para la revisión visual del usuario
- Abrir `Tesis de Inversión y Supuestos`: ver título Amazon, tesis, cuatro argumentos al alza y cuatro en contra, tabla de tres escenarios, razones y texto de conclusión.
- Abrir `Resumen de Valoración` y `Valuation output`: DCF Base **149,19** debe ser el único valor intrínseco principal; MOS35% **96,97**, precio al corte240,35; secundarios VP HOY no confundir con FY+3. No mostrar 0/−100% ficticios por N/D.
- Abrir `Origen de los Supuestos` y `Supuestos Recomendados`: verificar S/C0,72/1,65 Base, crecimiento11%/8,87%, margen15,8%, ROIC terminal11,5%, WACC8,18%; dependencia de SEC y del escenario.
- Abrir `Sensibilidad DCF`: tres matrices 5×5, centro149,19 identificado en WACC×g, ROIC×g y crecimiento×margen, estados OK; observar rangos y densidad. Abrir `Sensibilidad por múltiplo` con N/A honestos.
- Abrir históricos, CAPEX bridge y `Duración ventaja · FCFF` para revisar la mayor reserva económica; sin perder años ni fórmulas.

**Cierre:** candidata suficientemente preparada para **inspección visual y comentarios del usuario**, no lista para integrar al catálogo. El registro completo de sensibilidad, fuentes y fórmulas se encuentra en `FASE_3_ENTREGA.md`, `FASE_4_BORRADOR_NIVEL_1.md` y `FASE_4_BORRADOR_NIVEL_2.md`.


## Adenda de resultados oficiales posteriores (mismo 3-nov-2026)
**Motor run [41638493874](https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/41638493874) ya terminó.** En lectura autenticada y ejecutada sobre el **mismo sheet_id R5**:
- `inputs_completos`: **exit0**, cero datos materiales esenciales faltantes.
- `auditar_ceros_materiales`: **exit0**, cero alertas.
- `candados`: **exit0**, **15/15**.
- `estados_completos` con perfil explícito de cobertura: **exit0**, `PASS_CON_SALVEDADES`; **0** entradas requeridas vacías, **0** etiquetas erradas, **0** blancos sin explicación, **8** categorías documentadas y **3** pendientes secundarios, **0** pendientes materiales.
- `auditar_estados_sec` con perfil de impuestos, split y corte PPE: **exit0**, **20 normalizaciones, 20 conciliadas, 0 diferencias y 0 cambios propuestos**.
- `diff_formulas_plantilla`: **exit124 TIMEOUT 600s**, por ejecución de lectura secuencial con muchos rangos. El job final **FAILED** por este timeout, no por un error contable acreditado.
- `controles_todas.sh` permaneció **NO EJECUTADO contra candidata** por identidad y contratos JSON integrados no resueltos. El 0 de los controles parciales no autoriza publicación.

En motor PR203 ya se propuso leer fórmulas por **lotes** para reducir las llamadas a Google Sheets sin omitir pestañas ni fallar abierto (nuevo HEAD posterior al timeout). La prueba del nuevo workflow se encuentra pendiente del resultado del [run 41640312601](https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/41640312601), no marcado como aprobado anticipadamente.

**Panel principal de resumen, verificación posterior adicional:** en `Resumen de Valoración!F1:H2` se añadieron los rótulos **DCF BASE HOY · VALOR PRINCIPAL**, fórmula `G1='Valuation output'!B35` que muestra **US$149,19**, y **Precio con MOS35%** con fórmula `G2=G1*(1-G4)` que muestra **US$96,97**. Estado visible **CON RESERVAS / NO PUBLICADO**. La lectura de `Valuation output!B35` tras el cambio permaneció **149,19148575564947**. Este panel es de presentación, no introduce supuesto ni copia un número como constante.

**DICTAMEN actualizado:** pasa cobertura de materialidad histórica y conciliación SEC; la puerta de comparación exhaustiva de fórmulas está pendiente de versión optimizada/repetición; la puerta de promoción integrada y auditoría económica de materialidad siguen pendientes. Disponible **para revisión visual del usuario** exclusivamente como candidata.

## Adenda final de control técnico de candidata — corrida optimizada verificada
[GitHub Actions run 41640312601](https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/41640312601) **SUCCESS**, con job `regression` SUCCESS (**52 passed**) y `live-readonly` SUCCESS. Efectivamente ejecutados con las credenciales oficiales sobre **AMZN R5 sheet-id**: `inputs_completos` exit0 (0 faltantes), `auditar_ceros_materiales` exit0 (0 alertas), `diff_formulas_plantilla` exit0 (**0 sustituciones fórmula→número/vacío**), `candados` exit0 (**15/15**), `estados_completos` exit0 (`PASS_CON_SALVEDADES`, 0 material, 3 secundarias), `auditar_estados_sec` exit0 (**0 discrepancias tras 20/20 normalizaciones**). El comparador de fórmulas pasó en ~7,6 segundos de ejecución según logs en vez de agotar 600 s. Artefactos del run preservan código de salida y detalle. **La observación histórica del timeout del run 41638493874 queda superada, no borrada de la cronología.**

Se congeló un testigo numérico verificable adicional en `SNAPSHOT_NUMERICO_PROVISIONAL_20261103.json`: vectores completos de NOPAT, reinversión, FCFF, factores de descuento, VP por año y bridge, más identidad/ticker/revisión/corte y errores máximos de reproducción. Es una **captura provisional**, NO sustituto de un snapshot automático con hashes de todas las fuentes, fórmulas y repos. Debe formar parte del gate por cada ejecución cuando se implemente el contrato PR172.

**Dictamen actualizado y delimitado:**
- **Controles técnicos F1/F2 de candidata: superados**, con tres salvedades secundarias y la evidencia oficial anterior.
- **Auditoría aritmética interna: superada** para DCF Base y puente, sin recalibración de supuestos.
- **Análisis F3 y F4 Nivel 1/2: redactados como candidatos**, con reservas económicas materiales explícitas.
- **Presentación: preparada para revisión visual directa en la hoja** (no se ha validado renderizado navegador ni desplegado en app).
- **No autoriza merge ni publicación** mientras falten gate integrado de R5 (hoja ↔ motor ↔ JSON ↔ aplicación) y cierre de reservas económicas materialmente relevantes por CAPEX/ROIC/WACC/Level3/RSU/múltiplos.
