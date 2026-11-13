# AMZN R5 · Método JMR A-1.2 · Fase 3: revisión económica de supuestos

**Fecha del estudio:** 3-nov-2026. **Corte financiero:** 30-sep-2026 (10-Q presentado hasta corte informativo 30-oct-2026). **Precio de referencia al 30-oct-2026:** USD 240,35, conforme a Input R5, NO cotización en tiempo real. **Revisión** `AMZN-20261102-A12-R5`, [hoja candidata](https://docs.google.com/spreadsheets/d/199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I/edit). **Estado:** revisión económica DOCUMENTADA COMO CANDIDATO; **NO certificada**, no autoriza publicación. Conservar F1/F2, notas, fórmulas y cuatro historias. No sustituir R5 por R2/R3/R4.

## 1. Dictamen económico y tesis

Amazon combina tres economías heterogéneas: comercio/marketplace, publicidad y suscripciones sobre infraestructura logística; y AWS, que aporta una parte desproporcionada del EBIT con fuerte consumo de capital en centros de datos/IA. El riesgo principal de la valoración no es la caída aparente del FCF por un error contable: la SEC confirma el FCF neto de incentivos **−42.357 millones USD** LTM, frente a CFO **168.300** y CAPEX neto **210.657**. La pregunta es si los retornos de la capacidad contratada de cómputo compensarán su costo antes de que haya depreciación, obsolescencia o presión en precios. No confundir el flujo reportado con el FCFF proyectado por el método incremental.

**Conclusión condicionada:** mantener por ahora la historia Base de USD **149,19148576/acción**, **NO como precio validado**, mientras se comprueba el puente entre cash CAPEX, crecimiento AWS, desfase de dos años y Sales-to-Capital (S/C) marginal. El precio de mercado usado en la hoja, **240,35**, supera al DCF Base aproximadamente **61,1%**; en este escenario no existe margen de seguridad del 35%. La historia Optimista (241,84) roza ese precio, pero no sustituye el caso Base.

## 2. Diagnóstico de negocio y mezcla operativa (informes SEC)

| 9M hasta 30-sep-2026, USD millones | Ingresos | EBIT operativo | Margen EBIT | Crecimiento ingresos interanual aproximado |
|---|---:|---:|---:|---:|
| Norteamérica | 333.172 | 26.113 | 7,84% | 11% |
| Internacional | 125.094 | 4.721 | 3,77% | 13% |
| AWS | 125.803 | 48.555 | **38,60%** | **35%** |
| **Consolidado** | **584.069** | **79.389** | **13,59%** | **16%** |

AWS representa ~21,5% de ventas 9M pero ~61,2% del EBIT operativo. La publicidad (56.689 millones 9M) y servicios a vendedores (134.850 millones) elevan monetización de la base de clientes; no atribuirles márgenes no desglosados por separado. En Q3 AWS vendió 45.984 millones, +39% interanual, y registró EBIT 17.773 millones. **No extrapolar linealmente 35–39% a diez años**: el crecimiento de cloud es cíclico respecto a capacidad, presupuesto empresarial, deuda, competencia y nuevas arquitecturas.

Fuentes: [10-Q Sep2026, segmentos y producto](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm); [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm).

## 3. Históricos, normalización y ROIC

| Serie, millones USD | FY2024 | FY2025 | LTM Sep2026 |
|---|---:|---:|---:|
| Ventas | 637.959 | 716.924 | 797.455 |
| EBIT GAAP | 68.593 | 79.975 | 104.366 |
| Margen EBIT GAAP | 10,75% | 11,16% | 13,09% |
| CFO | 115.877 | 139.514 | 168.300 |
| CAPEX bruto de caja | 82.999 | 131.819 | 215.192 |
| ROIC histórico de fórmula JMR | 19,24% | 15,94% | **13,07%** |

Crecimiento LTM comparable a LTM anterior **15,350845%**, no LTM/FY2025. La reducción del ROIC de 2024→2026 concuerda con un ciclo de capacidad, aunque el numerador/denominador cambian por ASC842, activos financieros y revalorizaciones contables; **no interpretar ROIC de serie como ROIC marginal puro de AWS**. La nota sobre intangibles no desglosados en balance afecta `Return on Tangible Assets` y la ausencia del desglose de cuentas por cobrar afecta rotación/DSO, **no** los ROIC/ROA/ROE principales que en la hoja usan saldos agregados. Esos indicadores secundarios permanecen N/D, sin inventar cero.

El resultado neto LTM **134.779 millones** contiene plusvalías financieras: la SEC informa **68,4 mil millones** de otros ingresos 9M 2026, ligados principalmente a Anthropic. El impuesto 9M incluye **15,2 mil millones** de cargo discreto por esas plusvalías. Por tanto, **P/E sobre NI GAAP LTM es un indicador engañoso** para la rentabilidad operativa recurrente. No proyectar el beneficio extraordinario dentro del EBIT. Fuente: [10-Q 2026, resultados y nota fiscal](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm).

## 4. Revisión de drivers por historia

| Historia | Probabilidad | CAGR ventas 1–5 | Margen EBIT objetivo | S/C marginal 1–5 | S/C marginal 6–10 | ROIC terminal | g perpetua | Valor hoy USD |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Base | 45% | 9,2947% | 15,8% | **0,72** | 1,65 | 11,5% | 4,0% | **149,19** |
| Conservadora | 22,5% | 6,5965% | 12,0% | 0,52 | 1,25 | 9,5% | 3,2% | 81,01 |
| Disrupción (separada) | 10% | 0,9901% | 8,5% | 0,35 | 1,05 | 7,5% | 2,5% | 62,44 |
| Optimista | 22,5% | 12,0918% | 18,5% | 1,15 | 2,10 | 15,0% | 4,0% | 241,84 |

**Base, cronología:** crecimiento 11% en FY+1 y ~8,8725% anual FY+2–FY+5 (composición genera CAGR ~9,2947%). Margen operativo GAAP LTM 13,0874%, pero margen EBIT ajustado por I+D de la base del DCF **14,4839%**; se proyecta convergencia a 15,8% para Base. La cifra 10,64% histórica/sectorial en Input B30 no es margen de cada historia. El S/C de industria 2,7255 en B32/B33 tampoco reemplaza `Escenarios e historias!E5:F5`.

**Decisiones económicas F3 (sin escritura de drivers a falta de justificación superior):**
- Crecimiento: **MANTENER CON RESERVA** 11% año 1 / ~8,87% años 2–5. AWS crece más, retail mucho menos; la mezcla justifica desaceleración, pero el éxito de IA y competencia son incertidumbres, no nuevas cifras SEC.
- Margen Base: **MANTENER CON RESERVA** 15,8% como aspiración de mezcla AWS + ads; exige demostrar rentabilidad después de depreciación incremental, gasto energético, insumos IA, marketing y SBC.
- S/C marginal **0,72**: **RESERVA MATERIAL**. Dado el CAPEX que aumenta en 2027 y la reinversión FY+1 técnica de 121.712 millones, puede resultar demasiado optimista en intensidad de capital. No reemplazar por 2,7255 de la industria ni por 0,55 arbitrario; valorar el estrés. Mantener desfase de reinversión **2 años** solo como hipótesis testable por utilización de instalaciones.
- S/C 6–10 **1,65**: **RESERVA**; implica fuerte mejora de eficiencia tras despliegue de IA, no extrapolable automáticamente.
- ROIC terminal **11,5% Base**: **RESERVA**; excede WACC terminal ~8,99% en 2,51 pp, reflejando foso competitivo residual, no garantizado. La convergencia hacia la media se conserva por regla JMR.
- Terminal **g=4,0%**, Rf **5,29%**, WACCterminal **8,99%**: **MANTENER condicional** al corte y moneda, con diferencial WACC–g ~4,99 pp. El valor presente terminal es **1.193.803 millones** sobre EV operativo **1.514.824 millones**, aproximadamente **78,8%**; significativo, pero por debajo de alerta 85%. Verificar consistencia de Rf nominal de largo plazo y ERP/terminal al actualizar fecha.
- Impuesto de pronóstico **25% marginal inicial**, en vez de replicar tasa GAAP contaminada por plusvalías: **MANTENER** como juicio económico provisional, no cifra SEC ni exención fiscal estructural.

## 5. Prueba económica crítica: CAPEX, reinversión y desfase

La SEC reporta para el LTM a Sep2026 CFO 168.300, compras de PPE de caja brutas 215.192, incentivos/venta PPE 4.535, CAPEX neto 210.657 y FCF neto **−42.357**. El FCF sin incentivos es −46.892; son definiciones distintas, no error de caja. En 9M2026 las adiciones PPE de AWS **147.236 millones** representan ~74,8% de adiciones consolidadas, pero esas adiciones incluyen actividad no pagada y arrendamientos; **no equivalen a CAPEX cash**. Amazon orientó ~220.000 millones de CAPEX cash en FY2026 y una inversión **mayor** en FY2027, sin cuantía exacta para 2027; no se debe poner una cifra inventada en pronóstico.

En el DCF FCFF se utiliza `reinversión_t = incremento_ventas_(t+desfase) / S/C_t`. No se resta además CAPEX bruto histórico porque se duplicaría inversión económica. El `FCFF FY+1 Base` técnico es **−25.555 millones**, FY+2 −15.679 y FY+3 −6.372; la firma puede tener valor operativo positivo por flujos posteriores. Conciliación tentativamente ilustrativa: si en FY2027 hubiera CAPEX neto 215.465 (referencia FY2026, no guía FY2027), una reinversión 121.712 exigiría D&A menos variación de capital de trabajo ~93.753 millones, mayor que D&A total LTM 79.353. **Diferencia ~14.400 millones no explicada por un supuesto de capital de trabajo nulo y D&A plana.** La conclusión es prudencia en eficiencia de capital, no corrección mecánica del DCF.

| Sensibilidad aislada, S/C años 1–5 | DCF Base USD/acción | FCFF FY+1 USD M | Estado |
|---:|---:|---:|---|
| 0,50 | **128,72** | −79.108 | Estrés severo de capital |
| 0,55 | **134,81** | −63.175 | Estrés relevante |
| **0,72** | **149,19** | −25.555 | Referencia R5 conservada |
| 0,90 | **158,50** | −1.213 | Mayor productividad no probada |

Los cuatro valores anteriores fueron ensayados previamente y devueltos a 0,72, según [anexo CAPEX R5](NORMALIZACION_CAPEX_Y_JUSTIFICACION_DCF.md); no son un cálculo fresco de este documento ni sustituye la prueba de cash CAPEX FY2027. Es una sensibilidad distinta a los centros 5×5 del libro. **Aprobar S/C requerirá presupuesto de capacidad, D&A futuro, energía, contratos de suministro, ΔNWC y rendimiento incremental.**

## 6. Activos no operativos: reconciliación SEC y sensibilidad real

Los activos de Anthropic/OpenAI contabilizados en `Balance Sheet!L14` **288.700 millones USD** provienen, en cifras aproximadas SEC Sep2026, de: Anthropic convertible notes **146.200**, Anthropic nonvoting preferred **92.500**, OpenAI Series C Preferred **50.000**. Suma **288.700**. FY2025: notas Anthropic **45.800** + preferred **14.800** = **60.600**. Esto explica el salto de BS14 entre K y L y reconcilia el saldo informado en el puente; **no son CAPEX, caja libre ni crecimiento operativo**. Los instrumentos privados tienen riesgos de valoración Level 3, descuentos de liquidez, límites de conversión (12% ownership cap relevante en Anthropic) y posible pérdida de valor. La SEC reporta un agregado más amplio de inversiones y warrants por 298.800 millones: no sumar íntegro 298.800 al 288.700. Fuente: [10-Q Sep2026, inversiones no cotizadas, riesgos](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm).

El puente DCF del libro suma 288.700 una sola vez al EV operativo, tras deducir deuda 304.841 y sumar caja/marketables 114.226. En R5, esta cifra representa **26,70 USD por acción**, aproximadamente **17,9%** del valor Base patrimonial. Sensibilidad `manteniendo todo lo demás constante`: desvalorización del 25% → **−6,68 USD/acción**, del 50% → **−13,35 USD/acción**. No incorpora impuestos ni realiza valor justo en transacción; requiere revisar si cartera y capital operativo ya contienen valores de estos activos de otra forma. Riesgo no menor, **no prometer liquidez de Level 3**.

## 7. WACC, deuda, acciones, opciones y capitalización I+D

- **WACC actual 8,179602956%**, enfoque Detailed multinegocio Retail/Computer Services y riesgo AA; Rf USD 5,29%, costo del equity utilizado por múltiplos ~8,44334%, WACC terminal 8,99%. La beta, ponderación regional ERP, precio mercado de deuda, estructura objetivo y fecha de tasas requieren cierre de issue [motor #197](https://github.com/JuanMaRobledo/JMR-valuation/issues/197). Deuda libro **304.841**, sin sumar de nuevo leases ASC842 **114.783** reconocidos en deuda. Esto no es equivalencia automática con valor de mercado.
- **I+D:** fracción capitalizable **25% proxy** sobre tecnología e infraestructura, serie de gastos I+D estimados LTM **31.734,5**, activo de investigación **78.943,15**, amortización **20.597,6**, ajuste EBIT **11.136,9** millones. Fuente de origen SEC no separa todo gasto I+D, por lo que 25% es **juicio**, no factura reportada. Sensibilidades 15/25/40% ya documentadas. No contabilizar incremento de I+D dos veces.
- **RSU/SBC:** SBC LTM **19.873 millones**, acciones comunes **10.811 millones**, RSU sin ejercer ~**223,3 millones** según expediente F1. Las RSU no equivalen a opciones Black–Scholes; la hoja tiene `Input B38=No` para opciones sin warrants sobre acciones propias, `Option value` cero condicional. La dilución de RSUs y la SBC recurrente deben tratarse sin doble descuento. Una sensibilidad de dilución full vest fue calculada como referencia, **no** es nuevo precio oficial.
- **Tasas fiscales:** tipo histórico firmado 2022 beneficio positivo en hoja, gastos negativos en años de ganancias; auditor SEC debe invertir signo solo para comparación. EPS histórica FY2016–19 ajustada por split 20:1; PPE LTM balance al 30-sep-2026 (508.862) no a FY2025 (357.025). Son convenciones verificables, no errores GAAP.
- **NOL:** si se ha elegido B62=No, B63 condicional vacío intencionalmente; no convertirlo en "Amazon jamás tuvo pérdidas fiscales". Sin fuente de liberación fiscal, no reducir arbitrariamente impuesto prospectivo.

## 8. Múltiplos: resultados actuales frente a errores documentales previos

| Método | VP secundario Base observado en hoja actual | Estado |
|---|---:|---|
| EV/EBITDA | **341,10 USD** | Calculado, ancla sensible a operaciones retail/IA y CAPEX, no valor principal |
| P/OCF | **190,40 USD** | Calculado, **no deduce CAPEX**, no equivalente a FCFF |
| EV/FCFF | N/D | FCFF FY+3 Base negativo, múltiplo de denominador negativo no económico |
| P/E | N/D | Normalizar NI financiero extraordinario, impuestos y utilidad operativa antes de habilitar |
| P/FCFE | N/D | Flujo al accionista y endeudamiento extremadamente volátiles; revisar aperturas y leases |

La entrega F1 antigua citaba EV/EBITDA VP3 349,74 y P/OCF VP3 179,15. **No repetirlos como resultados actuales**: el resumen vigente `Resumen de Valoración!D42,D46` muestra 341,10 y 190,40 a valor hoy para Base. La hoja `Resumen de Valoración!D34` del ponderado secundario está **correctamente en blanco** al faltar métodos con peso vigente positivo; no recalcular pesos ni poner N/A=0 para rellenarlo. La valoración DCF **Base 149,19** sigue siendo el valor principal. Revisar el contrato de cinco múltiplos antes de publicar; declarar no aplicabilidad exige fuente, denominador y sensibilidad.
 
## 9. Escenarios, probabilidades y ciclos

Base (45%) refleja AWS creciendo más deprisa que retail mientras el CAPEX se recupera con dos años de demora. Conservadora (22,5%) asume rentabilidad limitada y elevada reinversión. Optimista (22,5%) implica una monetización de AWS/ads, margen 18,5%, S/C 1,15 e incrementos grandes de ROIC; no se convierte en caso central por compararse al precio. Disrupción (10%) mide erosión de precios de cómputo, stranded capacity y crecimiento limitado; no se promedia con las tres historias ordinarias por norma. El promedio renormalizado de las tres ordinarias ronda **155,31 USD/acción**, **secundario**. Las probabilidades son juicios, no frecuencias observadas. El precio histórico de la acción y el sentimiento de mercado no son sustitutos del valor de activos ni del costo de capital.

## 10. Recomendación económica para continuar

**MANTENER provisionalmente drivers Base y los cuatro precios R5, SIN elevarlos a certificados.** La F3 cumple la tarea analítica de contrastar supuestos con historia, estructura de negocio, riesgo de inversión, notas SEC y sensibilidades, pero deja **reservas materiales expresas** sobre S/C con cash CAPEX 2027, deuda a mercado/WACC, riesgos Level 3 y dilución económica. Es preferible un intervalo honesto de escenarios a un valor Base artificialmente estabilizado. En términos de decisión a precio de corte 240,35, la asimetría calculada con R5 no ofrece MOS35% bajo caso Base. La decisión final sobre supuestos y publicación requiere las pruebas de consistencia y puerta integrada.

**Controles necesarios antes de F4 publicada:** revisión auténtica del manifiesto de históricos y SEC signo/split/fecha; coincidencia estricta `ticker + revision_id + sheet_id + corte` entre hoja/JSON/motor/app; múltiplos obligatorios y N/A reconciliados; valoración de deuda y RSU sin duplicar; evidencia de sensibilidad 5×5 y de precios prospectivos; autocrítica del LLM constructor; CI integral sin controles `NO_EJECUTADO`. Hasta entonces solo se pueden redactar F4 Nivel1/Nivel2 como **borrador**. F5 externa queda tras revisión visual e instrucciones del usuario.

### Fuentes primarias principales

- Amazon [10-Q 30-sep-2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm), segmentos, flujos, impuestos, deuda y participaciones Level 3.
- Amazon [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm), comparativos y notas contables.
- Amazon [10-K FY2022 (split)](https://www.sec.gov/Archives/edgar/data/1018724/000101872423000004/amzn-20221231.htm).
- [Hoja candidata R5](https://docs.google.com/spreadsheets/d/199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I/edit), `Input sheet`, `Escenarios e historias`, `Valuation output`, `Resumen de Valoración`, `Financials Multiples`, `R& D converter`.
- [Entregas F1 y F2](FASE_1_ENTREGA.md), [anexo CAPEX](NORMALIZACION_CAPEX_Y_JUSTIFICACION_DCF.md) y [acta técnica](CIERRE_TECNICO_F1_F2_20261103.md).
