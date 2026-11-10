# Netflix: valoración Modelo JMR

Corte: 21 de octubre de 2026. Información financiera hasta 30 de septiembre de 2026. USD millones, excepto valor por acción.

Estado: valoración calculada, reproducida y documentada para revisión. No equivale a auditoría sin salvedades de cada dato o supuesto económico. Publicación autorizada en la app con salvedades visibles.

[Hoja editable](https://docs.google.com/spreadsheets/d/11yN171o8R61n4RhZnmuZuiSyIn_DGkfTmjo7wMKqaZI/edit)

## 1. Resultado

**DCF Base: US$48.34 por acción.** El promedio condicionado de conservadora, base y optimista es US$47.62. Disrupción queda separada.

| Historia | DCF US$/acción | Peso del terminal en EV |
|---|---:|---:|
| Base | 48.34 | 54.56% |
| Conservadora | 33.61 | 48.14% |
| Disrupción | 14.78 | 34.15% |
| Optimista | 68.59 | 60.44% |

Precio de referencia: US$65,04 del cierre 21-oct-2026, Yahoo chart. Investing mostraba US$65,05: diferencia de un centavo documentada, sin combinar ambas cotizaciones. El Base está -25.68% frente a ese precio. El umbral Base con margen de seguridad de 35% es **US$31.42**.

## 2. Estados y normalización

Se reconstruyeron los diez cierres 2016–2025, balance auxiliar 2015, septiembre 2025 y septiembre 2026. Los estados permanecen reportados; el LTM de flujos usa FY2025 + 9M2026 − 9M2025. El balance usa el saldo al cierre, sin sumar balances.

| Partida LTM | USD millones |
|---|---:|
| Ingresos | 49,734.63 |
| EBIT | 15,564.87 |
| Utilidad GAAP | 14,766.65 |
| CFO GAAP | 12,307.94 |
| Capex PPE | 932.88 |
| Adiciones de contenido | 19,991.44 |
| Amortización de contenido | 17,528.90 |

Hay partidas agregadas en los informes que no permiten separar todos los rótulos de una plantilla genérica. Se identifican con N/P, agrupación y nota. N/A identifica ratios sin aplicación económica; N/P no acredita que un activo o pasivo no exista. Los residuos se presentan como agrupaciones aritméticas del total oficial menos componentes, no como nuevas observaciones independientes.

La extracción XBRL inicial mezcló conceptos de tecnología y otros componentes en 2016–2019. Se sustituyeron por las cifras de los estados consolidados de los 10-K2018 y 10-K2020. Se conservan originales, correcciones y fuentes en normalized.json. Las once conciliaciones EBIT revisadas, incluido LTM, y once identidades de balance pasan con tolerancia US$1.000.

Netflix **recibió** US$2.800 millones por la terminación WBD. El ingreso está debajo de EBIT. Se excluye de la utilidad normalizada usando un efecto neto supuesto de US$2.100 millones a impuesto de 25%; no se afirma que ese sea su efecto fiscal real. El ajuste no cambia EBIT ni se vuelve a deducir como capex. La utilidad normalizada indicativa es US$12.666,65 millones.

## 3. Ratios

Las cuatro hojas de ratios abarcan 62 filas por once períodos. En la revisión anterior al cierre final se observaron 584 celdas numéricas y 98 con indisponibilidad/no aplicación explícita. Las correcciones posteriores completan desgloses financieros sin convertir los faltantes en supuestos de inexistencia. Se usan balances iniciales específicos para retornos; inventario tradicional y ciclos que lo requieren no se equiparan al contenido.

El EBIT más D&A PPE no se etiqueta como EBITDA convencional. En la variante convencional se añade la amortización de contenido, incluida la amortización total histórica cuando se publica. Su utilidad económica para comparar Netflix es limitada porque el contenido constituye un costo recurrente.

## 4. Costo de capital

| Entrada | Valor / naturaleza |
|---|---|
| UST diez años, 21-oct-2026 | 5,13%, Treasury |
| Ajuste soberano utilizado | 0,22 puntos, Damodaran |
| Rf nominal USD ajustada | 4,91% |
| ERP madura | 4,42% = adjusted payout 4,20% + 0,22 puntos |
| Prima geográfica adicional | 0,50 puntos, hipótesis |
| Beta global Entertainment ajustada por caja | 0,98, base enero2026 |
| Beta reapalancada | Aproximadamente 1,02 |
| Kd antes de impuestos | 5,85%, estimación anclada en notas USD |
| Impuesto marginal | 25%, hipótesis de valoración |
| Ke | 9.94% |
| WACC inicial y terminal | 9.64% |

El modelo aplica Ke = Rf + beta × (ERP madura + prima geográfica). Por tanto, la exposición a esa prima tiene lambda implícita igual a beta. No se presenta la prima geográfica de 50 puntos básicos como una medición exacta país por país. La tabla sectorial de reinversión usada como ancla es Entertainment de EE.UU.: ventas/capital de 1,39, una referencia de capital total utilizada como hipótesis marginal, no una identidad económica demostrada.

## 5. Cuatro historias independientes

Base: crecimientos 10%, 9%, 8%, 7%, 6%, 5,5%, 5%, 4,5%, 4,2%, 4%. Margen de entrada 32%, convergencia a 34%; ventas/capital 1,39; g4%; ROIC terminal12%. El CAGR inicial de cinco años es 7,99%.

Conservadora: 6%, 5,5%, 5%, 4,5%, 4%, 3,8%, 3,6%, 3,4%, 3,2%, 3%. Margen objetivo30%; ventas/capital1,15; g3%; ROIC terminal igual al WACC.

Optimista: 14%, 13%, 12%, 10%, 9%, 8%, 7%, 6%, 5%, 4,5%. Margen36%; ventas/capital1,8 al inicio y1,6 después; g4,5%; ROIC terminal15%.

Disrupción: −3%, −4%, −3%, −2% y después0%. Margen18%, g0%, sin liberación automática de capital ni recuperación artificial. ROIC estable igual al WACC.

Probabilidades: Base50%, conservadora25%, optimista15%, disrupción10%. El promedio de las primeras tres renormaliza su suma de90%. Estas probabilidades son opiniones del analista.

## 6. DCF y puente

FCFF = EBIT × (1−impuesto) − reinversión. Reinversión explícita por crecimiento/ventas-capital, con desfase seleccionado cero en la corrida Base. En perpetuidad, reinversión = NOPAT × g/ROIC. Impuesto22% al inicio, convergente a25%. WACC puede converger anualmente desde el sexto año si se modifica el terminal.

El puente resta deuda a valor razonable US$15.158 millones y suma caja/inversiones cortas US$8.222,95 millones. Arrendamientos operativos permanecen como gasto y pasivo operativo: no se vuelven a restar como financiación sin convertir coherentemente el EBIT. B18=No significa sin conversión incremental, no ausencia de arrendamientos. Los pasivos operativos de leasing identificados son US$2.252,24 millones.

Acciones al cierre: 4.106,325903 millones; RSU pendientes1,867761 millones. El DCF usa4.108,193664 millones de acciones y resta un derecho de opciones de US$4.290,87 millones. Se observan120,175117 millones de opciones a strike medio US$41,24. Plazo4,5 años es una estimación a partir de4,79 años publicados en diciembre2025; sigma36,96% procede de retornos diarios de un año. Se evita restar un derecho y añadir otra vez las mismas opciones como dilución.

## 7. Siete múltiplos secundarios

Financials Multiples utiliza las mismas ventas, EBIT, impuestos y FCFF de las historias DCF. Presenta FY+1–FY+3 como años de proyección desde el LTM, no como guías oficiales del calendario. Los precios relativos de año3 se descuentan tres años a Ke. No se pronostican dividendos ni recompras; FCFE se retiene como caja y actualiza deuda neta y patrimonio proyectados.

| Método | Base VP US$/acción |
|---|---:|
| EV/EBITDA | 69.16 |
| EV/FCFF | 52.34 |
| P/E | 57.67 |
| P/FCFE | 45.23 |
| P/OCF | 39.69 |
| P/Ventas | 58.37 |
| P/Valor libro | 65.82 |

**Consolidado secundario: US$50.60.** Targets Base: EBITDA8x, FCFF20x, P/E20x, FCFE20x, OCF16x, ventas5x y libro5x. Pesos respectivos0%,25%,25%,25%,15%,10%,0%. Pesos y targets son editables.

EBITDA y libro se calculan con peso cero por la recurrencia del contenido y el efecto de recompras sobre patrimonio. El OCF utilizado es económico normalizado: conserva SBC como costo; no se identifica con CFO GAAP sin ajuste. El FCFF histórico usa el puente explícito CFO−NI+NOPAT marginal−capex−SBC, sujeto a diferencias de impuestos caja/devengo. Las series de deuda históricas usan valores contables cuando no se ha reconstruido el mercado de cada bono.

El contraste de P/E forward citado para DIS14,76x y CMCSA6,26x procede de Reuters del21oct; no se promedia mecánicamente con P/E trailing normalizado. No se completó una certificación de denominadores homogéneos de todos los peers para siete métodos. Los targets no se ajustaron para igualar el DCF.

## 8. Sensibilidad e inverso

Tres matrices DCF de5×5: WACC terminal×g, ROIC terminal×g y margen sostenible×desplazamiento de crecimiento inicial. Se recalculan flujos y descuento. Sus tres centros son US$48,34. Las75 celdas se contrastaron con cálculo independiente.

Hay28 matrices relativas: siete métodos × dos anclas —objetivo e implícito actual— × dos familias. Los ejes son múltiplo en veces y fundamental en dólares, margen, crecimiento o rentabilidad identificada. Cada centro corresponde a su propio método/ancla, no necesariamente al DCF. El centro de las dos familias coincide para cada ancla.

DCF inverso a US$65,04: CAGR inicial **16,12%**, desplazamiento de8,13 puntos en las tasas de los primeros cinco años. Mantiene fijas las demás hipótesis y las tasas de crecimiento de los años6–10; no describe una expectativa directamente observable ni una predicción. Reproduce US$65,04 con residuo inferior a US$0,000001.

## 9. Verificación y límites

124 controles independientes aprobados; cero errores de fórmula almacenados en la exportación revisada, con7.722 celdas de fórmula. Se conservaron24 validaciones originales de Inputs. Pruebas reales: desfase1 elevó Base a48,49480095, y margen inicial33% a48,57004069; ambas coincidieron con el cálculo independiente y se restauraron.

Persisten salvedades documentadas sobre clasificación de desgloses agregados, plazo exacto de opciones a septiembre, impuesto específico de WBD, comparables homogéneos, y justificación de ventajas y retornos terminales. Se recuperó y revisó el prompt v5 vigente del repositorio. La revisión se documenta en la auditoría: no se declara cumplimiento integral de sus controles económicos. El registro de la app y la ficha de esta corrida distinguen datos, cálculos y juicios.

## 10. Fuentes

- SEC10-K2018: https://www.sec.gov/Archives/edgar/data/1065280/000106528019000043/form10k_q418.htm
- SEC10-K2020: https://www.sec.gov/Archives/edgar/data/1065280/000106528021000040/nflx-20201231.htm
- SEC10-K2021: https://www.sec.gov/Archives/edgar/data/1065280/000106528022000036/nflx-20211231.htm
- SEC10-K2024: https://www.sec.gov/Archives/edgar/data/1065280/000106528025000044/nflx-20241231.htm
- SEC10-K2025: https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm
- SEC10-QSep2026: https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm
- CartaQ3: https://www.sec.gov/Archives/edgar/data/1065280/000106528026000290/ex991_q326.htm
- Damodaran ERP: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm
- Damodaran beta global: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/BetasGlobal.html
- Ventas/capital: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/capex.html
- Treasury21oct: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=202610
- Precios: Yahoo chart, URL íntegra en sources/urls.json.
