# AMZN · AMZN-20261102-A12-R3 · Fase 2 · CERRADA

2026-11-02 · Claude Code, modelo y esfuerzo según los metadatos de la sesión · hoja [`1yzSqSP3Qopz3lPBNKsyXCsNSgioxZkoWOrZ6eaTjBvA`](https://docs.google.com/spreadsheets/d/1yzSqSP3Qopz3lPBNKsyXCsNSgioxZkoWOrZ6eaTjBvA/edit) en `AAA Finanzas / Análisis / AMZN/` · Método A / A-1.2 · Estado **CANDIDATO** · **AISLAMIENTO=OK** (solo datos de Amazon, de sus documentos SEC y de fuentes de mercado declaradas; los pares solo como comprobación declarada).

**Operación:** *actualizar*. R3 es una copia de la hoja R2 (mismos estados y datos crudos, verificados contra la SEC en la auditoría fase 4) con: (1) las correcciones de la auditoría que la regla admite, (2) los cinco múltiplos completados y (3) los datos crudos de mercado que faltaban desde la fase 1. **Independencia:** esta sesión auditó R2; por eso la **fase 4 de R3 debe hacerla otra sesión u otro LLM**.

## Hecho y verificado (con evidencia)

**Resultado (hoja, `Valuation output!B35` y `Escenarios e historias!H5:H10`):**

| Historia | Probabilidad | Valor por acción | Precio con MOS 35 % |
|---|---|---|---|
| **Base** (valor principal) | 45 % | **175,48** | **114,06** |
| Conservadora | 22,5 % | 102,92 | — |
| Optimista | 22,5 % | 263,45 | — |
| Promedio de tres (sin Disrupción) | 90 % renormalizado | 179,33 | — |
| Disrupción (aparte) | 10 % | 54,93 | — |

Precio del análisis: 240,35 USD (cierre del 30-oct-2026). Base R2: 148,68 → R3: 175,48 (+18,0 %).

**Recálculo independiente** (replicador propio desde las entradas de la captura): Base, Conservadora, Optimista y Disrupción iguales a la hoja con error ≤ 6e-14 USD por acción. Valor terminal = 88,2 % del VP operativo.

**Puente:** VP operativo 1.900.820 − deuda 304.461 + caja 114.226 + no operativos netos 240.155 = patrimonio 1.950.740; − RSU 53.668; ÷ 10.811 M acciones = 175,48.

**Cambios de entrada frente a R2 (todas con nota en la celda):**

| Celda | R2 | R3 | Motivo (hallazgo de auditoría) |
|---|---|---|---|
| `Country equity risk premiums!B2` | 4,55 % (rebase) | 3,79 % | A-01: prima madura Damodaran 1-nov-2026 (T12m), misma fecha que Rf 4,94 % |
| `Cost of capital worksheet!B27` | 4,906 % | 4,146 % | A-01: 3,79 % + CRP ponderada por ingresos (sin cambio) |
| `Cost of capital worksheet!G39` | Computer Services | Software (System & Application) | B-03: AWS = infraestructura y plataforma de nube; beta de regresión 1,49 (EE 0,21) como contraste |
| `Input sheet!B84` | 294.595 | 240.155 | B-01: neto del impuesto diferido estimado 54.440 |
| `Input sheet!B40` | 0 | 0,01 | C-01: con 0 la fórmula valoraba cada RSU a la mitad (excepción técnica declarada) |
| `Input sheet!B50`, `Escenarios!N5:N8` | 12,5 / 10,5 / 9,49 / 15 % | 16,5 / 12,62 / 8,73 / 20 % | B-02: regla de foso (REGLAS §4, `moat_2026-09-30.json`) |
| `Trailing Valuation!B2:L3` | vacío | periodos y cierres dic-16…dic-25 + LTM | Dato crudo de fase 1 que faltaba (C-02) |
| `Entradas históricas auxiliares!B4:L5` | vacío | 0 | Sin minoritarios ni preferentes (10-K/10-Q) |
| `Cash Flow Statement!G38:L39` | vacío | FCF apalancado/no apalancado | Filas de memoria (construcción del importador) |
| Múltiplos `J8/J19/J30` (cinco pestañas) | vacío | regla por ciclo (ver abajo) | C-02 |
| `Escenarios!M5:M8`, `Tesis!A1` | textos R2 | textos R3 | Coherencia editorial |

**Correcciones de la auditoría NO aplicadas, con motivo:**
- **A-02 (arrendamientos):** REGLAS §4A trata los pasivos ASC 842 reconocidos igual que NIIF 16 (en la deuda, sin conversión) y la plantilla prorratea el ajuste de EBIT solo a pasivos no reconocidos. R2 cumple la regla; la objeción económica (+6 %) se eleva al usuario como posible cambio de regla para todas las empresas de EE.UU.
- **B-06 (impuesto de caja):** REGLAS §4 fija la tasa efectiva al inicio; se mantiene 22,5 % → 25 % y el impuesto de caja (~6,5 % del EBIT) queda como sensibilidad (+4 %).
- **C-09 (margen del año 1):** `Input sheet!B28` es una fórmula de la plantilla (= margen base); cambiarla sería reemplazar una fórmula.
- **C-10 (I+D):** capitalización consistente neutral para el valor; `B17 = No`.

## Tabla de supuestos (revisada en ambas direcciones)

| Supuesto | Valor R3 | Historia 3/5 años y LTM | Pares / consenso (fecha) | Mecanismo | Qué lo refuta | Efecto en valor |
|---|---|---|---|---|---|---|
| Crecimiento año 1 | 13,9 % | LTM 11,2 %; T3-26 +12,1 %; prom. 3a 11,7 %, 5a 13,2 % | Guía T4-26 +12–16 % (8-K 29-oct) | AWS +30–35 % (backlog 578.000 M) + comercio ~7 % | AWS < 25 % dos trimestres | ±2 pp años 1–5: ±3 % |
| Margen EBIT año 10 | 17 % | LTM 13,1 %; T3 13,9 %; 5a 7,2 % | Retail 6,8 %; Software 33 % (Damodaran ene-26) | Mezcla AWS ~30 % / comercio ~8 % | Margen AWS < 28 % | ±1 pp: ±7 % |
| Ventas/Capital 1–5 / 6–10 | 0,75 / 1,4 | Incremental LTM 0,65–0,74; promedio 1,57 | Retail 3,51 | Capex de IA (guía 2026 ~220.000 M) | Inversión > 150.000 M dos años sin crecimiento | 0,65: −6 %; 1,0 en 6–10: −4 % |
| Beta desapalancada | 1,05 | Regresión 60m 1,49 (EE 0,21) | Retail 0,78; Software 1,25; Computer Services 0,96 | Pesos EV/Ventas de la plantilla | Regresión < 1,0 sostenida | Computer Services: +6 % |
| WACC inicial / terminal | 9,14 % / 8,73 % | — | Damodaran 1-nov-26 | Rf 4,94 % + prima 3,79 % (+CRP); terminal beta 1 | ERP de pago sostenible 4,41 %: −13 % | ±0,5 pp terminal: ver matriz |
| g terminal | 4 % | — | Regla JMR (techo Rf 4,94 %) | Inflación + crecimiento real | — | ±0,5 pp: matriz nativa |
| ROIC terminal Base | 16,5 % | GAAP LTM 15,9 %; con I+D 13,7–14,6 % | Retail 13,6 %; ref. foso 16,5 % | Ventaja durable (escala, Prime, AWS) | Erosión del foso (ROIC = WACC): ver Disrupción | 13,6 %: ~−4 % |
| No operativos | 240.155 | 294.595 bruto | — | Notas/preferentes Anthropic, OpenAI a costo | Rondas a la baja; liquidez | −20 %: −2,5 % |
| Impuesto | 22,5 % → 25 % | Efectivo operativo ~22 %; caja ~6,5 % | — | Normalizado (REGLAS §4) | — | 15 % → 25 %: +4 % (no aplicado) |
| RSU | 53.668 M | 223,3 M RSU | — | Black-Scholes con ejercicio técnico 0,01 | — | vs R2: −2,5 USD |

**Probabilidades:** previa de crecimiento maduro 45/22,5/22,5/10 sin ajustes (`probabilidades.py`: 0 fallos). **Sesgo:** se retiraron dos prudencias duplicadas de R2 (prima rebasada y ROIC terminal bajo la industria) y un sesgo favorable (beta y no operativos brutos). Ningún supuesto se ajustó para acercarse al precio.

## Múltiplos (cinco prioritarios, hoja nativa)

Regla por ciclo (`multiples_by_cycle.py` + `apply_multiples_v3.py`, JMR-valuation): cierres FY2022–FY2025 y LTM con crecimiento a ±2 pp del FY+3 de cada historia (7,1 / 11,9 / 14,7 %), ajuste por tasas `(k cierre − g)/(k corte − g)`, Conservador ≤ múltiplo LTM, Optimista ≥ 1,03× Base. Pares (WMT, COST, MSFT, GOOGL, yfinance 30-oct) solo comprueban.

| Método | Cons / Base / Opt (×) | VP3 Base | Matriz 5×5 | Estado |
|---|---|---|---|---|
| EV/EBITDA | 15,2 / 16,2 / 16,7 | 302,19 | nativa, centro OK | Calculado, peso 0 |
| EV/FCFF | ancla C 23,6 / 31,7 / 38,8 | -76,20 | N/A | FCFF FY+3 negativo |
| P/E | 15,6 / 20,1 / 24,0 (tope C) | 189,32 | nativa, centro OK | Calculado, peso 0 |
| P/FCFE | ancla C 20,8 / 26,8 / 31,8 | -17,36 | N/A | FCFE FY+3 negativo |
| P/OCF | 14,9 / 16,2 / 16,7 | 145,48 | nativa, centro OK | Calculado, peso 0 |

**Juicio documentado:** la C de EV/EBITDA y P/OCF (conversión FCFF/EBITDA y FCFE/OCF de FY+3) no se calcula porque FY+3 sigue en la rampa de capex (FCFF −1.733 / −34.076 / −26.170); el script ya no topa con C ≤ 0 y el criterio se aplica igual a las tres historias. **Pesos:** DCF 100 %, múltiplos 0 (contraste secundario): las métricas FY+3 están distorsionadas por la transición de inversión y el EV histórico de la plantilla incluye las inversiones no operativas.

## Sensibilidad y DCF inverso

Tres matrices DCF nativas 5×5 (`Sensibilidad DCF`), centro = Base. **DCF inverso** (contrato del prompt: delta común a los años 1–5, años 6–10 convergen a g): delta **+8,86 pp**, TACC 5 años implícito 20,6 % frente a 11,7 % Base; raíz única, error 5.7e-14.

## Controles de cierre (resultado real)

| Control | Resultado |
|---|---|
| Recálculo independiente = hoja (4 historias) | **APROBADO** (≤ 6e-14) |
| `diff_formulas_plantilla.py --sheet-id R3` | **0** reemplazos; 46 pestañas |
| `candados.py` / `inputs_completos.py` | **15/15** / **0** vacías |
| `estados_completos.py` | **0** hallazgos |
| `integridad_hojas.py` | 4 hallazgos «pestaña vs motor legado» (compara con `reference/damodaran/AMZN_resultado.json` de oct-2026 mientras R3 no está en el catálogo); se repite tras la promoción |
| `controles_supuestos.py` / `probabilidades.py` | **0** / **0** |
| `ubicacion_hoja.py` / `precios_historicos.py` | **OK** / **completo** |
| `verificar_multiplos_hoja.py` | **APTO_FUENTE** (5 fórmulas, 2 N/A justificados) |
| `validar_matrices_candidato.cjs` (regla del CI) | **APTA** |
| `auditar_integridad.validateRecord` | **OK** |
| Centros de matrices = Base/VP3; probabilidades = 1; MOS = Base × 0,65 | **OK** |

**PASOS: 7/7 ejecutados** (1 supuestos, 1b ciclo/probabilidades, 2 historias, 3 entradas/DCF/matrices, 3b múltiplos por ciclo, 4 recálculo, 5 captura/JSON).

## Decisiones y juicios
- Operación *actualizar* sobre copia de R2 (no desde cero): los estados y datos crudos de R2 están verificados contra XBRL; repetirlos no agrega evidencia.
- A-02 y B-06 no se aplican por regla (ver arriba); se elevan al usuario.
- ROIC terminal por regla de foso aunque la auditoría proponía 13,6 % como central: la regla prevalece; la sensibilidad queda declarada.

## Pendiente o bloqueado
- **Fase 4 de R3** en otra sesión u otro LLM (esta sesión auditó R2).
- Decisión de regla sobre arrendamientos ASC 842 (A-02) para todas las empresas de EE.UU.
- `integridad_hojas` contra el registro publicado tras la promoción.

## Para la fase siguiente
Leer este archivo, `VALORACION_A12_EN_REVISION.json`, `dcf_inverso_r3.json`, la captura `evidencia/captura-hoja-20261102/AMZN-20261102-A12-R3_resultados_hoja.json` (SHA-256 `8ca4d58c18896c21b8c7baa4bb4db194154e2870a68e51a227c12b0a946575f4`) y el análisis de R2 (N1/N2) para actualizarlo con las cifras de R3.
