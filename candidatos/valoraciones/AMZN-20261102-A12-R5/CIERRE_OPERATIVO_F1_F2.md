# AMZN R5 · Puerta de cierre de fases 1 y 2 — sin confundir completitud con auditoría

**Fecha:** 2026-11-03. **Proyecto:** AMZN-20261102-A12-R5, hoja https://docs.google.com/spreadsheets/d/199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I/edit, PR datos #234. **DICTAMEN:** `F1_CANDIDATO_CON_RESERVAS` y `F2_HISTORICOS_COMPLETOS_CANDIDATO`. Se **cierran los trabajos de extracción y conciliación directa**, pero no se marca `CERTIFICADO`, ni se publica, ni se fusiona PR.

## Cierre ejecutado y contrastado en hoja (fuentes y fórmulas)
| Puerta | Prueba concreta | Resultado |
|---|---|---|
| Estados F2 | 10FY 2016–25 Income Statement, BS, CF, LTM Sep26 y aperturas FY2015/Sep2025 | **CARGADOS**; conciliaciones históricas de EBIT/CFO/CFI/balance 10/10 reportadas en F2_ENTREGA |
| Crecimiento | `Input!I26` LTM interanual comparable; B27/B29 proyección y CAGR Base; tabla Input137:152 | CORREGIDO según `CORRECCION_CRECIMIENTO_INPUT.md`, con referencias nativas |
| CAPEX | `Cash Flow Statement!L13,L15,L16` y puente `Input!A159:B207` | **CERRADA CAPTURA**: CFO 168300, capex bruto215192, incentivos4535 y FCF −42357; 9M PPE AWS y expansión identificados |
| DCF F1 | `Escenarios e historias!H5:H8`, `Valuation output!B35` | 4 historias calculadas, Base149,1915; sin cambio tras puente/sensibilidad; MOS35%=96,9745 |
| Sector fuera del modelo | `Sector!A3:X7` | **5 comparables fuentes publicadas** (3 cloud/IA: MSFT, GOOGL, ORCL; 2 retail: WMT, COST), márgenes y CAGR 3Y/5Y con fórmulas; referencias FY y URL por celda. No se inventan valor de mercado/PE/múltiplos faltantes, no forzar como similares puros AWS |
| Ratios de pares | `Crecimiento y Márgenes!C15:E20` | Antes N/D, ahora estadísticas min/Q1/mediana/Q3/max/media calculadas; mediana 3Y crecimiento **10,48%**, 5Y **10,72%**, margen EBIT **30,59%**. **La mediana consolidada de 5 empresas mixtas NO es margen objetivo de Amazon**, contiene software de alta rentabilidad |
| WACC auxiliar | `Cost of capital worksheet!B84` | VALIDADO **ESTRUCTURAL** 8,1796%, no deuda FV sectorizada ni ERP geográfica auditada |
| Capitalización I+D | `R& D converter` / Input F119 | Proxy no divulgada 25% Tech&Infrastructure + vida 5 años, fuentes agregadas; sensibilidad previa 15/25/40 ejecutada |
| Option value/RSU | `Option value`, Input B38, stock award note | Ninguna emisión de call propia relevante y RSU reconocidas 223,3 M, SBC19.873 M LTM, no tratar RSU como calls |
| Múltiplos | EV/EBITDA, EV/FCFF, PE, PFCFE, POCF | 5 evaluados; **2 con precios prospectivos candidatos**, EV/FCFF N/A por FCFF negativo, PE/FCFE N/D o ancla insuficiente. Ponderado general N/D correcto |
| Sensibilidades | 3 tablas `Sensibilidad DCF` y reinversión Base | 3 centros **OK**; S/C .50/.55/.72/.90 probado en hoja, 0,72 restaurado |
| Candados en hoja | 15 definidos por `JMR-valuation/reference/candados_plantilla.json` | Lectura puntual: Input B81 NO APLICA; B85/B92/B108/B111 VALIDADOS; B109/B110/B112/B113/B114 NO APLICA; COC B84 VALIDADO; cuatro K5:K8 LISTO. **15/15 estados admitidos**, esto no sustituye script `candados.py` |
| F1 inputs obligatorios | Input B9/B10 industrias, B50 ROIC, COC B49 preferred 0 | Completados y verificados; condicionales (opciones, preferentes) no se fuerzan con ceros. El script `inputs_completos.py` **NO EJECUTADO** |
| Controles oficiales | `estados_completos.py`, `auditar_estados_sec.py`, `auditar_ceros_materiales.py`, `diff_formulas_plantilla.py`, `inputs_completos.py`, `candados.py`, `controles_todas.sh` sobre revisión R5 | **NO EJECUTADOS** por falta de acceso al runtime autenticado del motor conectado a ID de hoja R5. No simular ni reportar exit code 0 |
| CI del PR #234 | GitHub commit de rama | 0 workflows / 0 status checks observados en último head consultado; **NO CONFIRMADA CI** |

## Bloqueos y clasificación (no ocultar)
1. **Material económico F3:** CAPEX guía FY2026~US$220bn y FY2027 superior, aún no conciliado con reinversión proyectada FY+1 S/C0,72/lag2. A mayor CAPEX, el DCF podría ser inferior a Base149,19. Documento [NORMALIZACION_CAPEX_Y_JUSTIFICACION_DCF.md](NORMALIZACION_CAPEX_Y_JUSTIFICACION_DCF.md).
2. **Material económico F3:** deuda de mercado y pasivos ASC842 tratados como un bono único de valor ~180382 M frente deuda libro304841 M; EV-equity resta book304841, no market180382. Corregir valor deuda y sensibilidad WACC/bridge, motor [#197](https://github.com/JuanMaRobledo/JMR-valuation/issues/197).
3. **Material económico F3:** inversiones Level3 Anthropic/OpenAI no operativas288700 M (restricciones/realizabilidad/impuestos/contratos AWS), RSU/SBC, normalización P/E, P/FCFE insuficiente y EV/FCFF negativo. Bug plantilla primer saldo apertura [#199](https://github.com/JuanMaRobledo/JMR-valuation/issues/199) pendiente propagación.
4. **Integridad técnica F1/F2 pendiente:** candados completos leídos 15/15 por API, pero **scripts oficiales/no regresión de fórmulas** no ejecutados; issue [#200](https://github.com/JuanMaRobledo/JMR-valuation/issues/200) pendiente. Ausencia de pruebas CI no es prueba de éxito. Peers cubren histórico margen/CAGR, **no precios comparables ni todos los 5 múltiplos actuales**, correctamente N/D en celdas sin fuente; faltan fuentes/criterios de ERP país.
5. **De fuente irreductible:** Amazon no desglosa mantenimiento versus crecimiento CAPEX y R&D exacta separada de Tech&Infrastructure; se usan proxies explicitados y no se rellenan con ceros ficticios. Pre 2019 ASC842 hace algunas razones históricas no estrictamente comparables.

## Decisión
- **Cerrar F1/F2 en el sentido de trabajo de captura y prueba equivalente disponible**, y preservar expediente (sin reabrir toda la extracción de diez FY).
- **NO marcar «completo certificado», «gates aprobados», «DCF económico definitivo» ni «publicable»** hasta ejecutar suites oficiales de motor, resolver inconsistencias materiales y comprobar CI. PR #234 permanecerá DRAFT, sin publicaciones.
- La fase 3, cuando la solicite el usuario, se dedica a racionalidad de CAPEX y reinversión, márgenes, ROIC, crecimiento, mercado de deuda, participaciones y valor intrínseco final.
- La fase 4 incorpora pruebas de publicación y análisis Nivel1/2; fase5 auditoría guiada. No se hizo F3/F4/F5 ni se reemplazó el catálogo de producción.

**Resumen:** No se han perdido los avances de los prompts viejos. La valoración Base sigue **149,1915 US$/acción, provisoria**. Los datos financieros históricos 10FY + LTM y el puente CAPEX quedan documentados y comprobados. El cierre de controles **formales** es bloqueado y debe decirse así hasta ejecución real.

## Actualización de cierre técnico 3-nov-2026 — pruebas y correcciones confirmadas

1. `Resumen de Valoración!G4` estaba vacío (MOS). **Se cargó 0,35 y se leyó de vuelta**, completando la entrada de seguridad estándar sin alterar ninguna proyección ni ratio.
2. `Input sheet!A210:B226` contiene prueba de conciliación 2027: cash CAPEX FY2026 guidance 220000, 9M2026 175670, cash neto ilustrativo 215465 y D&A menos ΔNWC requerido 93753 vs LTM D&A79353. Discrepancia hipotética 14400 USD M; **no** ajuste a DCF. Fuente SEC e informe de ganancias referenciados en [NORMALIZACION_CAPEX_Y_JUSTIFICACION_DCF.md](NORMALIZACION_CAPEX_Y_JUSTIFICACION_DCF.md).
3. Se hizo **réplica literal de selección de campos** de `inputs_completos.py` mediante lectura actual de `Input A1:C120`, COC y Resumen: con MOS corregido, quedan **4 alertas, todas `Input sheet!B39:B42`**. Son campos de opciones propias desactivadas porque `Input B38=No`; no sería correcto completarlas con ceros arbitrarios. Se mantiene evidencia separada de RSU/SBC. Esta prueba replica condiciones del script, **NO es ejecución del script oficial con credenciales**.
4. En [PR del motor #202](https://github.com/JuanMaRobledo/JMR-valuation/pull/202) se propuso corrección mínima de las cuatro condiciones, flag `--sheet-id` para que el control use el candidato correcto, y pruebas de regresión de Yes/No. **Solo rama de revisión, sin merge**. El [issue #200](https://github.com/JuanMaRobledo/JMR-valuation/issues/200) sigue abierto hasta que pase la CI relevante y se ejecute el control contra R5.
5. El PR R5 datos #234 sigue en borrador. Datos 10FY+LTM, puentes y controles nativos satisfactorios; los scripts SEC/no-regresión y normalización económica WACC/múltiplos **siguen pendientes**. **El gate formal de F1/F2 todavía no es PASS**. No publicar ni promover la valoración por un cálculo ilustrativo.


### CI real del motor · nueva evidencia 2026-11-03

- [PR #202 JMR-valuation](https://github.com/JuanMaRobledo/JMR-valuation/pull/202) **DRAFT**, sin merge. En el commit `8788398007fea0f1bd0df98e2c94d9093067da32`, workflows de GitHub Actions:
  - **JMR F1 Input candidate regression** run **41591400571**, `SUCCESS`, test explícito `tests/test_inputs_completos_amzn_condicionales.py`: **2 passed**; sintaxis `inputs_completos.py` compilada correctamente.
  - **JMR materialidad y salvedades** run **41591400515**, `SUCCESS`: **28 passed**, sintaxis del script probada.
- Este resultado valida la **propuesta de reparación del gate para opciones B39:B42**, no su integración a `main`. En lectura literal anterior, los únicos cuatro avisos del script de cobertura eran B39:B42 condicionalmente no aplicables si B38=No. **Aún no se ha ejecutado el nuevo script contra la hoja real con `--sheet-id`**.
- **No asumir éxito del resto**: `estados_completos.py`, `auditar_estados_sec.py`, `auditar_ceros_materiales.py`, `diff_formulas_plantilla.py`, `candados.py` con lectura real y CI de datos R5 **pendientes**. Los estados K5:K8 y matrices 5×5 acreditan cálculo, no auditoría de las hipótesis económicas.
- Datos F1 y F2 **cerrados operativamente como candidatos con salvedades**, no valoración publicada. No fusionar PR #202 ni #234 por ahora.
