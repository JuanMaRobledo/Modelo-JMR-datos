# DUOL · Método JMR A-1.2 R4 · revisión económica conforme a Damodaran
**Corte:** 30-sep-2026 · **Fecha de revisión:** 5-nov-2026 · **Estado:** CANDIDATO_REVISADO / NO PUBLICAR · **Alcance:** DUOL exclusivamente.

**Objeto.** Revisar crecimiento, margen, reinversión presupuestada/Sales-to-Capital, ROIC medio/marginal/terminal, prima de mercado y riesgo geográfico, WACC y reconciliaciones contables, **sin reconstruir el motor original de Damodaran ni recalibrar al precio de mercado**. Esta es una revisión económica F3 y una lista de controles para la continuación F4; **no** es auditoría independiente F5, ni recálculo certificado de una nueva Base. El candidato R4 reproducible sigue en USD 111,4426678512, MOS 35% USD 72,4377341033; la revisión vigente en catálogo sigue siendo DUOL R2.

## 1. Fuentes primarias, períodos y escala

- 10-Q SEC del 30-sep-2026, presentado 4-nov: https://www.sec.gov/Archives/edgar/data/1562088/000162828026069692/duol-20260930.htm
- Carta Q3 y guía de 4T26, SEC: https://www.sec.gov/Archives/edgar/data/1562088/000162828026069474/q3fy26duolingo9-30x26share.htm
- 10-K FY2025: https://www.sec.gov/Archives/edgar/data/1562088/000162828026012494/duol-20251231.htm
- Datos NYU Damodaran (ERP implícita 1-nov-2026): https://pages.stern.nyu.edu/adamodar/New_Home_Page/home.htm
- Damodaran, crecimiento fundamental: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/growth.htm
- Damodaran, capitalización de I+D: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/R%26D.htm
- Damodaran, ROIC y capital operativo: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/definitions.html
- Hoja piloto JMR: https://docs.google.com/spreadsheets/d/117ZIeaI1NKcSK38XcWtqVwo7JD8qpt6QkDuC3VhOuvY/edit
- Motor original Base: https://docs.google.com/spreadsheets/d/1Sa7Wplbj-Ef44YinF6XAZnOAMPEoiz9HtSiDLc7x7DM/edit

Valores económicos en **USD millones**, salvo USD por acción, porcentajes y multiplicadores. LTM = FY2025 + 9M26 - 9M25.

## 2. Diagnóstico: qué muestran los estados y qué presenta la hoja

| Partida | Valor | Cálculo/referencia |
| --- | ---: | --- |
| Ventas LTM | 1.182,296 | 1.037,589 + 899,428 − 754,721 |
| EBIT GAAP LTM | 146,122 | 135,570 + 102,668 − 92,116 |
| Margen EBIT GAAP LTM | 12,3592 % | 146,122 / 1.182,296 |
| I+D expensada LTM | 362,473 | 306,323 + 282,917 − 226,767 |
| Amortización del activo I+D (3 años) | 233,629 | `R& D converter` |
| Ajuste EBIT por I+D | +128,844 | 362,473 − 233,629 |
| EBIT económico R&D-adjusted | 274,966 | 146,122 + 128,844 |
| Margen EBIT R&D-adjusted | 23,25695 % | 274,966 / 1.182,296 |
| Activo I+D no amortizado | 630,967 | `R& D converter!D36` |
| Efectivo y equivalentes/inversiones cortas | 1.373,901 | 1.239,607 + 134,294 |
| Inversión largo plazo no operativa | 110,120 | 10-Q; no sumar dos veces |
| Capital invertido ajustado Base | 628,543 | Equity 1.481,597 − caja 1.373,901 − activos no op 110,120 + activo I+D 630,967 |
| NOPAT ajustado sobre tasa efectiva | 209,820 | 274,966 × (1 − 23,6923%) |
| ROIC inicial calculado | 33,3820 % | 209,820 / 628,543 |

**Interpretación:** 33,38% no es un ROIC marginal proyectable. Depende del capital empleado **sin caja y con el ajuste de I+D**. La proporción elevada de caja respecto del patrimonio hace el cociente particularmente sensible al denominador; el activo I+D reduce la artificial inflación del ROIC que aparecería ignorándolo. Confirmar consistencia de capital operativo con el tratamiento elegido de leasing, activos fiscales y costo de ingresos diferidos. Los intereses recibidos por caja no son EBIT operativo.

El incremento de R&D ajustado exige también incluirlo como **reinversión económica**; no basta subir EBIT manteniendo la inversión medida solo por CAPEX de infraestructura. La inversión en software que ya aparece como CAPEX contable no debe volver a capitalizarse como si fuera I+D expensada. En 9M26 se registraron US$282,917 M de I+D en resultados, US$8,718 M de software/intangibles capitalizados y US$18,001 M de PP&E comprada; no son categorías idénticas.

## 3. Crecimiento y narrativa: MANTENER CON RESERVAS

- Q3 2026: ventas US$309,007 M, +13,7% interanual; bookings US$316,1 M, +12%; DAU 64,9 M, +29%; suscriptores pagados 13,1 M, +14%. 9M26 ventas US$899,428 M frente a US$754,721 M: +19,17%. La tasa LTM y las tasas trimestrales NO deben promediarse indiscriminadamente.
- Base R4: +14,1765% año 1; CAGR +13,5035% años 2–5; transición al 4% nominal terminal. Año5 ingresos US$2.240,471 M; año10 US$3.256,760 M. El motor Damodaran aplica un CAGR uniforme 2–5; la hoja `Puente Base Damodaran` normaliza el mix por productos y verifica identidad matemática de los FCFF, **no prueba que las cohortes de usuarios sigan exactamente esa curva**.
- Hipótesis de penetración +1% relativa y precio/mezcla +2% en Base son **supuestos** sustentados parcialmente por Q3, no conversiones/ARPU de cohortes observadas. La prueba sin esos aumentos de monetización da US$101,1301/acción en la misma hoja (−9,25%): material. Presentar casos sin y con mejora; no imputar el riesgo de IA otra vez a la tasa si ya se recoge en participación, conversión y márgenes.
- Propuesta F3: conservar crecimiento como **candidato**, NO elevarlo, probar contra TAM₁₀ × participación sostenible, composición de suscripciones/publicidad/DET/IAP, demanda impulsada por IA y contraevidencia de maduración y competencia.

## 4. Márgenes: RESERVA MATERIAL

- R4 parte de **23,25695% EBIT ajustado**, no de 23% GAAP. El EBIT GAAP es **12,3592% LTM** y **7,83% en Q3** (US$24,196 M / US$309,007 M). El margen ajustado por capitalización de I+D es una conversión económica según Damodaran, no EBITDA ajustado anunciado por la empresa.
- R4 propone **28% de EBIT ajustado** en año 5 y posteriores. El conjunto sectorial guardado en `Crecimiento y Márgenes` da mediana EBIT ~21,15% y cuartil 3 ~28,78% bajo su propia definición; la comparabilidad de ajustes I+D sectoriales aún debe verificarse. Llegar al tramo alto del sector es una hipótesis relevante y exige productividad y disciplina de gastos, pese a desaceleración y costes de producto/IA.
- Sensibilidad nativa `Sensibilidad DCF!C30:D30` al crecimiento central fijo: bajar **margen objetivo 28% → 26%** reduce valor **111,4427 → 105,3020 USD/acción** (−5,51%). **No se sustituye Base con este estrés univariado.** Falta escoger margen Base por evidencia causal de mezcla, gastos I+D, coste IA, marketing y escala, no por cercanía a la cotización.
- Q3 gross margin 72,9%; 9M26 gasto I+D US$282,917 M (31,45% de ventas), y SBC 9M US$120,334 M. Los ingresos diferidos y el bonus trimestral afectan comparaciones. Evitar reconstruir el margen sacando SBC de EBITDA y después también descontar opciones: doble conteo a controlar.

## 5. Reinversión y presupuesto de crecimiento: RESERVA MATERIAL

Modelo Damodaran: reinversión proyectada = incremento futuro de ventas / **Sales-to-Capital marginal**, sujeto a lag. El input `Input sheet!B57` NO cambia el supuesto estándar de **un año de rezago**. Por ello, la reinversión registrada en año 1 de **US$95,9389 M** es el aumento esperado de **ventas año 2 vs año 1 (US$182,2838 M) / S/C 1,9**, no ventas año 1 vs año 0.

| Elemento | R4 Base | Interpretación |
| --- | ---: | --- |
| S/C marginal años 1–5 | 1,9× | US$1 de capital nuevo soporta US$1,9 de ventas adicionales; exige prueba sectorial y por cohortes |
| S/C marginal años 6–10 | 1,400643× | Más capital requerido por dólar adicional de ventas |
| Reinversión año1 | US$95,939 M | Financiamiento de crecimiento año2 con lag1 |
| Reinversión año10 | US$93,008 M | Menor crecimiento incremental explícito |
| Reinversión terminal | **US$293,310 M** | Reinversión necesaria = NOPAT11 × g/ROIC terminal = 711,276 × 4%/9,7% |

La **reinvención terminal triplica aproximadamente la del año10**; no es por sí misma una fórmula incorrecta. Es el efecto de asumir que el retorno de **nuevos** proyectos cae al costo de capital, haciendo mucho más intensivo mantener g=4%. Ese salto es una decisión económica decisiva: **FCFF pasa de US$590,912 M (año10) a US$417,966 M (año11)** mientras sube NOPAT. Debe presentarse en Nivel 1 y Nivel 2, no ocultarse como un artefacto.

Conciliar inversión económica con R&D capitalizada (flujo neto de activo), PP&E/capitalización de software, adquisiciones y NWC operativo **incluyendo ingresos diferidos**. No usar CFO/FCF reportados como FCFF sin reconocer SBC, pagos anticipados de suscripción y ajuste contable I+D. SEC 9M26: CFO US$328,475 M, CAPEX US$26,719 M (8,718 + 18,001) y FCF US$301,756 M. La SBC de US$120,334 M representa ~13,38% de ingresos 9M y no es gratuita para el accionista.

## 6. ROIC: TRES magnitudes y una hipótesis terminal defendible, no certificada

- ROIC sobre **capital existente**: 33,38% inicial y **38,55%** en año10 según `Valuation output!L42`.
- ROIC **marginal indicativo** en año10: 26,85%, calculado como ΔNOPAT/reinversión rezagada. Contiene cambio de rentabilidad/mezcla de activos existentes: **no es prueba directa del retorno de una cohorte de proyectos**.
- ROIC **marginal terminal** año11+: 9,70% = WACC terminal 9,70%, supuesto de competencia que erosiona rentas para inversión incremental. Es coherente conceptualmente con ausencia de foso perpetuo defendible. **No significa que todo el capital acumulado caiga a 9,7% en un año.** Tampoco significa que el 38,55% sea perpetuo.
- Lo que requiere justificación adicional es el paso de retorno marginal indicativo 26,85% de año10 al retorno marginal 9,70% de inversión perpetua, y la tasa de reinversión resultante. `F3 ROIC marginal y fade` ya cuantificó ventajas **temporales** después del año10: frente a Base 111,44, retorno inicial marginal 12% con fade5/10 +0,98/+1,65 por acción y 15% con fade5/10 +1,89/+3,22. Son sensibilidades, no nuevas Bases.
- En `Auditoría DCF interna!B38` había una nota obsoleta que mencionaba retorno terminal **15%**; se corrigió con los valores reales **38,55% / 26,85% / 9,70%**.

## 7. Rf, ERP de mercado, beta y WACC: MANTENER PAREJA; RESERVA EN CRP

- Fuente Damodaran NYU **1-nov-2026**: Rf USD 10Y empleado por NYU **5,29%**, ERP implícita de mercado maduro **4,41%**. Mantener la pareja coherente; no mezclar Rf de otro día con una ERP de esa fecha sin recalcular.
- Beta bottom-up global seleccionada en la hoja: **1,3370400** (sector Software Internet). Duolingo no tiene deuda financiera tradicional en el input, por lo que el costo de patrimonio coincide inicialmente con WACC.
- Ventas geográficas FY2025: EEUU US$392,214 M (37,8005%), resto US$645,375 M (62,1995%), sin desglose suficiente por cada país. La hoja aplica **+1,80 puntos porcentuales al resto del mundo**, **no observable** de Duolingo ni una CRP por país certificada. ERP = 4,41% + 62,1995% × 1,80pp = **5,5295907%**; WACC = 5,29% + 1,33704 × 5,5295907% = **12,683284%**. `Cost of capital worksheet!B12=Detailed` y `B14=Input sheet!B36`.
- Sensibilidad fuente en `F3 País y monetización`: CRP ROW +1,80pp ⇒ **US$111,44**; +1,20pp ⇒ **US$113,73** (+2,05%); +0,90pp ⇒ **US$114,90** (+3,11%); +0pp ⇒ US$118,54. Son variaciones en el mismo motor, no nuevas cifras aprobadas. Por materialidad **no es lícito elegir una prima puntual sin fuentes geográficas o sin declarar su naturaleza proxy**.
- Los riesgos particulares de competencia e IA se reflejan principalmente en flujos/márgenes/historias; no se debe duplicar castigo con una CRP sin conexión geográfica. En `Auditoría DCF interna!B39` se corrigió una nota stale que decía Rf 4,91%: los parámetros usados son 5,29%/4,41%.

## 8. Arrendamientos, remuneración en acciones y NOL: NO CERRADOS

**Arrendamientos (ASC842).** Al 30-sep el balance registra activo ROU US$73,359 M y **obligación a largo plazo US$84,216 M**, con porción corriente incluida en `Accrued expenses and other current liabilities` (US$70,536 M total, no todo es leasing). `Operating lease converter` produce PV US$105,061 M de compromisos, que **no debe añadirse automáticamente** a deuda ASC842 ya reconocida. El input DCF considera `B18=No`, `B16=0`, por tanto usa contratos como coste operativo y no capitaliza nuevamente; sin embargo, la deuda lease reconocida no es literalmente cero y hay que elegir/trazar criterio único en EBIT/ROU, capital invertido, reinversión, WACC y EV–equity. La porción corriente no identificada separadamente permanece N/D, NO 0. No certificar ROIC ni EV-equity final hasta cerrar tratamiento. Esto no autoriza inventar un ajuste de interés o de ROU.

**RSU/stock options.** SEC 30-sep: ~47,1 M acciones ordinarias, 0,6 M de founder awards, 0,4 M efecto dilutivo de opciones (482 mil opciones brutas a strike US$20,36), 2,6 M RSUs, **50,8 M totalmente diluidas** en la carta. La plantilla usa 50,8 M y `Do you have employee options outstanding? No`; **no** descontar también el valor bruto de esas opciones sin demostrar que no está incluido en el denominador. Reconciliar SBC futuro de forma consistente y no sumar de vuelta el gasto como si fuera gratis.

**NOL.** El saldo de US$111,199 M no cuenta con conciliación fiscal suficiente en 10-Q. Sensibilidad ejecutada con selector activo vs inactivo: US$111,4427 vs US$110,9824 por acción, +0,413% individual. No bloquea en solitario bajo el umbral JMR de 2%, pero documentar fiscalidad agregada y no confundir con activo por impuesto diferido de US$203,605 M.

## 9. Matriz de materialidad y decisiones F3

| Palanca | Veredicto F3 | ¿Por qué? |
| --- | --- | --- |
| Datos LTM / I+D | **MANTENER / verificados** | Identidades GAAP y R&D ajustada reproducidas en hoja |
| Crecimiento 14,18% / 13,50% | **MANTENER CON RESERVA** | Q3 y drivers sostenibles, penetración y mix futuros no observados |
| Margen ajustado objetivo 28% | **RESERVA MATERIAL** | Estrés a 26% mueve Base −5,51%; debe defenderse contra sector y gastos |
| S/C 1,9 → 1,400643 | **RESERVA MATERIAL** | Falta puente inversión I+D+PP&E+NWC/deferred revenue y retornos incrementales |
| ROIC marginal terminal 9,70% | **MANTENER CON RESERVA** | Consistente con no-moft; paso año10→año11 y magnitud de inversión por justificar |
| Rf 5,29% + ERP madura 4,41% | **MANTENER** | Pareja NYU de misma fecha |
| Beta global 1,337 | **MANTENER CON RESERVA** | Sector bottom-up, comprobar comparables/región |
| +1,8pp CRP ROW | **RESERVA MATERIAL** | Proxy no observable; alternativa +1,2pp mueve Base +2,05% |
| Leasing ASC842 | **PENDIENTE** | Falta porción corriente y política homogénea |
| NOL US$111,199 M | **PENDIENTE NO MATERIAL AISLADO** | +0,413%, no certificado en fuente |
| SBC/denominador | **PENDIENTE** | Validar 50,8M diluidas y costo de futuras RSU |

**No cambiar inputs para aproximar al precio**. La coincidencia entre Stories y Damodaran Base no valida independientemente la causalidad de los supuestos. No elevar a `EN_REVISION` ni publicar DUOL R4 todavía.

## 10. Cambios efectivamente realizados y controles

1. **Hoja piloto JMR, `Auditoría DCF interna!B38:B39`:** corregidas las afirmaciones incongruentes sobre ROIC marginal terminal 15% y tasa libre de riesgo 4,91%.
2. **Hoja piloto JMR, `Auditoría DCF interna!A60:E75`:** añadido cuadro dinámico con enlaces a fórmulas **sin alterar** `Input sheet`, `Valuation output`, `R& D converter`, `Operating lease converter` ni los 4 motores DCF. Readback de 16 filas verificó ROIC 33,382%, 38,551%, 26,849%, reinversión 95,939/293,310 y sensibilidad US$105,302.
3. El estado sigue `CANDIDATO_REVISADO / NO PUBLICAR`. La Base US$111,4427 y MOS US$72,4377 están **sin cambios**, al igual que la R2 del catálogo y los demás emisores.
4. **Control completo de publicación, 18 candados, 75 sensibilidades R4 por las cuatro historias, múltiplos FY+1/2/3, N1/N2 R4 y QA app:** NO EJECUTADOS en esta revisión. No se declara aprobado. **F5**: NO REALIZADA.
5. **AISLAMIENTO=OK**: únicamente estudio y hoja piloto DUOL R4; ningún archivo de CMG o catálogo vigente modificado.

## 11. Siguiente secuencia técnica exacta

1. Conciliar **Q3 ASC842** desde footnote FY2025 y cambios 9M26, clasificar deuda corriente/N/D, escoger tratamiento homogéneo sin conversor duplicado. Documentar impacto Base + agregación con CRP/NOL.
2. Reconciliar **presupuesto real de reinversión** (I+D y amortización 3 años, software capitalizado, PP&E, NWC y deferred revenue, SBC), estimar S/C marginal y evolución de ROIC incremental con año de rezago; dejar puente de US$ por año y no solo múltiplo.
3. Revisar **historia de monetización y margen 28%** contra trimestres y sector comparable ajustado a I+D; seleccionar Base fundamentada y rango para Conservador/Optimista/Disrupción; considerar un 26% solo si evidencia lo respalda, no como ajuste automático.
4. Sustituir **CRP ROW +1,8pp** por promedio regional documentado o mantener explícitamente proxy con intervalo y salvedad material; validar beta y Ke con misma pareja Rf/ERP.
5. Solo después **recalcular cuatro historias** en las copias intactas de Damodaran, matriz de márgenes y ROIC, tres 5×5 y múltiplos propios R4; sincronizar hoja–JSON–N1/N2, ejecutar `controles_todas.sh`, CI, QA y entonces promover una sola ficha DUOL si los gates aprueban.

**PASOS:** revisión de estados, identidad R&D/ROIC, crecimiento, margen, S/C, riesgo/WACC y sensibilidad **ejecutadas como diagnóstico**; **no ejecutados** recast ASC842 completo, conciliación NWC/I+D y múltiplos, recálculo certificado de 4 historias, gates CI y publicación. Sin dictamen de auditoría independiente.
