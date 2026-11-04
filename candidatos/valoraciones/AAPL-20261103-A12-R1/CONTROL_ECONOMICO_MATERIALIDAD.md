# AAPL-20261103-A12-R1 · Control económico de materialidad (NO auditoría F5)

**Fecha y corte:** 3-nov-2026, datos FY2026 SEC 10-K; precio AAPL **US$331,90**, cierre 3-nov posterior al filing, [Yahoo histórico](https://finance.yahoo.com/quote/AAPL/history/). Modelo JMR A-1.2 FCFF, [hoja 46 pestañas](https://docs.google.com/spreadsheets/d/1dEycisHE5Ai34Z50ELOByAiZxub87dPG2TwOmYjS2tA/edit), **CANDIDATO_REVISADO, NO PUBLICADO**. Los resultados aquí son **stress puntuales**, no sustituyen la auditoría independiente (F5).

## Nuevos valores nativos vs documentación antigua
- Antes, en foto previa del PR (cuadro del 3-nov): Base US$150,042339, WACC inicial12,483%, WACC terminal9,32%, referencia US$338,32 2-nov. **SUPERSEDIDOS** por recalibración de tasa Damodaran mensual.
- **Ahora:** Base 141.008516469, MOS35% 91.655535705, Conservadora102,820990, Optimista172,892801, Disrupción71,266176; ponderado secundario hoy166,77140659 y múltiplos secundarios183,94666668; cierre AAPL 3-nov **331,90**. WACC inicial12,86221066%, Ke12,99450599%, Kd5,69%, terminal9,70%; deuda mercado76.262,208M y peso1,5565%, RF5,29%/ERP operativa5,4384%. **Confirmar que el archivo JSON y los textos usen solo esta foto; están pendientes.**
- Fuente Damodaran https://pages.stern.nyu.edu/adamodar/New_Home_Page/home.htm: prima implícita **4,41%** de la actualización mensual indicada 1-nov-2026, referencia de tasa libre **5,29%** del mismo dataset; esta combinación implica Ke terminal9,70%. Treasury cierre 2-nov 10Y4,91% (https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/textview?type=daily_treasury_yield_curve&field_tdr_date_value=2026) es un corte diario distinto; no mezclar RF4,91 con ERP4,41 sin recalcular la prima implícita. Se requiere análisis temporal si se renormaliza la curva.

## Stress puntual — R&D capitalización
| Vida útil de I+D | DCF nativo en misma hoja |
|---|---:|
| 2 años | 140,78800169 |
| **3 años (se restauró)** | **141.00851647** |
| 5 años | 141,69178640 |

- Diferencia 2→3 años -0,1564%, 5→3 años +0,4846%; menor2% individual. I+D SEC FY2026 US$45.765M; 3 años es juicio de ciclo tecnológico, reversiones confirmadas en `R& D converter!F7=3` y `Valuation output!B35`.
- Ajuste EBIT FY26 con vida3: +13.820M, EBIT ajustado171.883M; vida2 +12.805M, vida5 +16.965M; no extrapolar como crecimiento orgánico.

## Stress puntual — RSU/SBC
- [Apple 10-K FY2026, Nota acciones](https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm): **142,405 millones de RSU no consolidadas**, grants75,538M, vested73,529M, forfeited11,178M, saldo a 26-sep; SBC FY2026 US$13.789M y coste de RSU no reconocido US$24.100M a lo largo de 2,6 años.
- Denominador formal de la plantilla: 14.532,259M acciones emitidas, opcional contractual N/A. **Cota conservadora de dilución** si el saldo RSU entero se convirtiera en nuevas acciones de inmediato sin compras de compensación ni fallos de vesting: valor por acción **US$139.640150** vs **141.008516**, impacto **-0.970%** (<2%). No es pronóstico del recuento futuro.
- La SBC ya está en EBIT GAAP/I+D y, por tanto, en flujos ajustados; no descontar los US$24.100M no reconocidos **adicionalmente** y además diluir todas las RSU sin demostrar que no haya doble cargo. Las RSUs todavía no vestidas no son 'opciones' para Black-Scholes. Documentar en F5 si la dilución debe estimarse explícitamente.

## Stress puntual — deuda FV vs libros
- `Valuation output!B27` usa deuda **libro** US$94.479M, incluyendo leasing ASC842; `Cost of capital worksheet!C61` descuenta deuda a mercado **US$76.262,208M** estimada con notas, interés proxy2.937M, plazo10 años y Kd5,69%.
- Si únicamente se reemplazara el monto restado al equity por el mercado estimado (sin cambiar WACC ni FCFF), valor accionista `(2.049.172,283+94.479−76.262,208)/14.532,259` = **US$142.262058**, impacto **+0.889%** (<2%). **No editar la fórmula**, porque mercado deuda calculada debe verificar qué leases se incluyeron y qué componente es financiado. Ese proxy no es cotización pública del bono.
- La incertidumbre agregada debe reevaluarse al cerrar fuentes y fiscalidad; los umbrales JMR son <2% individual y <3% acumulado, sin cambio de decisión.

## Riesgo económico material aún abierto: costo de capital
- Centro matriz nativa `Sensibilidad DCF!D8=US$141.008516`; WACC −0,50pp → aprox **US$153,171427** (g4%); WACC +0,50pp → **US$130,762989**. Estas variaciones ~+8,63%/−7,27% son **MATERIALES**. No son error de fórmula; reflejan riesgo de estimación de Rf/ERP/beta y compresión del valor terminal.
- `Valuation output`: PVterminal US$1.058.697,220M y PV flujos10a US$947.946,824M; terminal ~52,76% EV. Riesgo de perpetuidad no se disimula por pasar matriz5×5.
- Necesario confirmar prima de riesgo por geografías, beta business mix y momento de RF; Fuente primaria [Apple 10-K FY2026](https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm) y [Damodaran](https://pages.stern.nyu.edu/adamodar/New_Home_Page/home.htm).

## Resultado y gate
- **Clasificaciones numéricas:** vida I+D y RSU <2%, deuda libros/mercado <2% individual, pero no acumular sin probar dependencia y posible doble conteo.
- **Sin acción de publicación:** faltan serie/contrato JSON y editorial Nivel1 >=7500 palabras, conciliación financiera automática, CI del catálogo y verificación visual de app. Esta evidencia no certifica F4, pero acota 3 diferencias que parecían indeterminadas.
