# AAPL-20261103-A12-R1 · FASE 3 · CANDIDATO_REVISADO · NO PUBLICADO

- **Fecha**: 3-nov-2026. **Método**: JMR A-1.2 / DCF FCFF USD nominal. **Hoja de 46 pestañas**: https://docs.google.com/spreadsheets/d/1dEycisHE5Ai34Z50ELOByAiZxub87dPG2TwOmYjS2tA/edit. **AISLAMIENTO=OK**. Herramientas: ChatGPT GPT-6, conectores GitHub/Sheets y SEC web, esfuerzo de configuración no verificable.
- **PASOS**: 9/9 abordados, 6 parciales y 3 no cerrados. Se verificaron fórmulas nativas y matrices puntuales; los tests oficiales de promoción **NO EJECUTADOS**.

## DCF nativo
| Historia | Probabilidad | Valor presente USD/acción | g terminal | ROIC terminal |
|---|---:|---:|---:|---:|
| Base | 50 % | **150,04233928** | 4 % | 15 % |
| Conservadora | 20 % | 108,78883113 | 4 % | 12 % |
| Disrupción (separada) | 10 % | 73,75534342 | 1 % | 9,5 % |
| Optimista | 20 % | 184,75711617 | 4 % | 18 % |

- Promedio renormalizado tres historias principales **US$148,58928789**. MOS35% sobre Base **US$97,52752053**; **no** sobre múltiplos ni ponderado.
- Precio referencial US$338,32 al cierre 2-nov-2026 **anterior** a presentación FY2026 10-K 3-nov. Precio/valor 2,25483; prima de mercado sobre DCF 125,48%; retorno desde mercado a Base −55,65%. No es un pronóstico de rentabilidad a plazo determinado.
- `Valuation output`: PV flujos10a 964.440,233M; PV valor terminal 1.173.557,902M; EV operativa 2.137.998,135M; valor terminal representa 54,89% de EV. Puente: deuda libros −94.479M; caja +56.722M; securities no corrientes +80.213M; equity 2.180.454,135M/14.532,259M acciones = US$150,042339. Opciones $0 solo como opción contractual no identificada; dilución RSUs **sin cerrar**.

## Drivers y cambios F1 → F3
| Driver | F1 contraste independiente, NO homologado | F3 motor nativo | Decisión y dónde |
|---|---|---|---|
| Crecimiento años 1–5 | 7 % | 7 % | MANTENER, `Escenarios e historias!C29:G29`; desacelera FY2026 +15,06 % |
| Margen EBIT horizonte | 35,5 % propuesto term externo | 36 % años10/terminal del motor | CAMBIAR, `Escenarios e historias!D5`; I+D capitalizada FY26 EBIT adj171.883M |
| Sales-to-Capital 1–5 | 1,80× | 1,80× | MANTENER `E5`, juicio marginal, no promedio industria |
| Sales-to-Capital 6–10 | 2,00× | 2,00× | MANTENER `F5`, juicio de eficiencia industrial |
| WACC inicial | 9,45 % externo inválido | **12,483033% nativo** | CAMBIAR `Cost of capital worksheet!E63`, deuda positiva y prima riesgo |
| WACC terminal | 9,32 % externo | 9,32 % motor | MANTENER valor calculado, beta terminal converge |
| g terminal | 4 % | 4 % | MANTENER `M29`; Rf USA 4,91 %, g menor |
| ROIC terminal | 15 % | 15 % | MANTENER `N5` por ecosistema, reinversión terminal g/ROIC26,67 % |

**NO atribuir** cambio DCF externo inicial US$174,52 → DCF motor US$150,04 exclusivamente al WACC: no tienen mismos supuestos ni puente equity. `Cost of capital worksheet!B84=VALIDADO` certifica consistencia aritmética de entradas, NO el costo económico de capital. Ke12,615632%, Kd5,31%, deuda mercado78658,118M/peso1,57467%; intereses brutos FY26 en `Income Statement!L15=2937M` **PROXY no reportado por Apple como partida separada**; rating Moody Aaa, maturity sintética10años y prima ERP requieren contraste, no son observaciones SEC.

## Múltiplos nativos: valor HOY, no precio FY+3
| Método | Ancla de salida Base FY+3 (juicio, no mediana automática) | VP Base hoy | Peso total |
|---|---:|---:|---:|
| EV/EBITDA | 17× | 200,3212553 | 20 % |
| EV/FCFF | 19× | 150,8562879 | 10 % |
| P/E | 22× | 197,6324132 | 20 % |
| P/FCFE | 20× | 157,1212616 | 5 % |
| P/OCF | 20× | 171,2912398 | 5 % |
| DCF | N/A | 150,0423393 | 40 % |

Múltiplos secundarios combinados US$185,161646; ponderado hoy US$171,113923; objetivo FY+3 ponderado US$236,905390. La principal sigue siendo DCF Base. `Múltiplos históricos` excluye FY2026 para mediana FY2021–25: EV/EBITDA 21,6555×, P/E27,9114×, P/OCF24,0841×, y actuales FY2026 29,1235×/37,9849×/34,1600×. EV/FCFF y P/FCFE histórico NO derivan de CFO-CAPEX: N/D, juicio de múltiplos salida no certificado. `Financials Multiples!D26` OCF proyectivo normalizado ≈134.296M no equivale al CFO SEC FY26 145.097M: revisar SBC, capital de trabajo, influencia sobre P/OCF.

## Sensibilidades y análisis de supuestos
- Cuatro historias `Escenarios e historias!K5:K8=LISTO`; 3 sensibilidad DCF 5×5 WACC/g, ROIC/g, crecimiento/margen con centros exactamente DCF Base (filas 12,23,34 `OK`).
- Cinco sensibilidad de múltiplos 5×5 independientes con centros exactamente las proyecciones FY+3 por método (filas84,94,104,114,124 `OK`).
- 138 referencias históricas de `Financials Multiples!B3:D123` se desplazaron una columna para FY2026 en **copia AAPL**, pendiente `diff_formulas_plantilla.py` y regresión. La plantilla maestra no se tocó.
- Reinversión: S/C no es ROIC ni CAPEX anual; ROIC contable inicial95,82% distorsionado por recompras y activos internos; a10años15% requiere prueba económica. Terminal alto54,89% EV hace sensibilidad sustancial. Tax efectiva FY26≈17%, marginal21%, convergencia como hipótesis.
- FY26 RSUs no consolidadas142,405 millones (≈0,98% acciones) y SBC 13.789M requieren dilución y coste económico reconciliados; `Option value` de opciones ordinarias N/A no significa RSU N/A. Deuda capitalizada leasing ASC842 sin recapitalizar.

## Gates pendientes para promover F4
1. **NO EJECUTADOS** `controles_todas.sh`, 18 candados, `auditar_ceros_materiales.py`, `diff_formulas_plantilla.py`, reconciliación hoja↔motor↔JSON, stress WACC/ROIC terminal y DCF inverso nativo con WACC actual.
2. No hay auditoría formal de fuentes/precios posteriores al filing, comparables externos ni prueba económica del OCF prospectivo/SBC/fiscalidad.
3. Aprobación de rango material de proxies y regresión de fórmulas necesaria; no basta con que centros 5×5 indiquen OK.

**Estado F3:** CANDIDATO_REVISADO con DCF y cinco múltiplos efectivamente calculados y reproducibles, sin validación integral ni certificación económica. Fuente central: https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm.
