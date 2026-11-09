# F3 · Historias a números y DCF · AAPL-FLOYD-FY26-R1
Estado: **CANDIDATO_REVISADO · CALCULADA; AVISOS ECONÓMICOS JUSTIFICADOS (actualizado 9-nov-2026, 2.ª sesión)**.

H2 https://docs.google.com/spreadsheets/d/1gtAc2TclEjszznAC8tfDGiOviq3bagTA7AzOh2r1h0c/edit. Fuente SEC https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm.

## Historias, independientemente calculadas
| Variable | Conservadora | Base | Optimista |
|---|---:|---:|---:|
| Probabilidad | 22,2% | 55,6% | 22,2% |
| CAGR ventas FY+1 a +5 | ~3,30% | ~7,00% | ~10,00% |
| Margen EBIT año10 | 29% | 36% | 39% |
| Sales-to-Capital 1–5 | 1,2 | 1,8 | 2,1 |
| Sales-to-Capital 6–10 | 1,4 | 2,0 | 2,3 |
| g terminal | 2,5% | 3,5% | 4,0% |
| ROIC terminal (hipótesis) | 15% | 15% | 15% |
| DCF USD/acción | 115,7157460 | 179,8060617 | 236,7237544 |

WACC inicial común 10,0120399%, terminal común8,56%; Rf nominal Treasury 10Y 6nov2026 4,86%; ERP de Damodaran estimada a 1oct2026 3,70%; beta bottom-up apalancada1,41489, Apple hardware/software. Impuesto efectivo FY2026 16,995%→marginal21%. Tasa terminal reinversión Base = g/ROIC = 23,3333%.

Precio referencia USD342,37; DCF Base principal USD179,8061; MOS35% = US$116,87394; downside Base −47,48195%. Valor esperado ponderado USD178,2137394.

## Bridge DCF Base
VP flujos años1–10 USDm1.058.811,43; VP terminal USDm1.524.414,11 (59,01% EV); EV operativo USDm2.583.225,54; deuda(−)81.567, cash(+)56.722, inversiones no operativas(+)80.213; equity USDm2.638.593,54 /14.674,664m acciones=179,80606 USD/acción.

## Compuertas nativas y anomalía
H2 'Control de integridad' registra 0/1883 fórmulas alteradas; 3/3 historias LISTO. 'Compuertas económicas' marca 3 escenarios APTO CON AVISOS JUSTIFICADOS: advertencias narrativas en B31,C31,D31.
**AVISO JUSTIFICADO** (antes «riesgo material»): ROIC año 10 Base 74,74 % frente a terminal 15 %. El escalón es mecánico (capital invertido inicial USD 144.517m; S/C marginal 1,8–2,0x frente al 3,31x real) y el 15 % es un supuesto conservador de erosión de la ventaja. Impacto por acción (Base): 15 % → 179,81; 20 % → 187,71; 25 % → 192,45; 30 % → 195,61; 40 % → 199,57; sin escalón → 205,08. Conservadora: 115,72 → 123,94; Optimista: 236,72 → 280,97. Justificación escrita en `Compuertas económicas!B31:D31`. No es auditoría F5.

Las 3 matrices DCF Base 5×5 en 'Sensibilidad DCF' tienen centro US$179,8061 (compuerta OK). Vida de I+D 2/3/5 años (Cons/Base/Opt): 115,10/179,12/235,97 · 115,72/179,81/236,72 · 116,48/180,67/237,67. DCF inverso (réplica externa, error < 0,001 USD/acción): crecimiento años 1-5 ≈ 24,6 %, o margen objetivo ≈ 76,3 %, o WACC −2,49 pp en paralelo. Múltiplos (contraste, peso 0): anclas = mínimo positivo de FY2023-26, ×0,9/×1,1; VP3 Base 253,25 / 213,45 / 244,53 / 230,61 / 204,92; cinco matrices 5×5 con centro = VP3.

**Limitación del motor documentada:** `R& D converter!B12` lee FY2026 como año −1 con LTM = FY2026 (FY2026 entra dos veces, FY2024 no). Re-cablear rompió la `Huella motor` (10 diferencias) y se revirtió; impacto estimado +0,7 % en el Base (USD 181,05). Notas en `Control de integridad!A9:A13`.
