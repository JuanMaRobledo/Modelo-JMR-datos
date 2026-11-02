# NU — Revisión económica A-1.2 R3 (2 noviembre 2026)
**Estado:** CANDIDATO / EN_REVISION. **Corte de estados:** 30-jun-2026. **Precio:** 30-oct-2026, US$11,61. **Hoja:** https://docs.google.com/spreadsheets/d/1Wj_LFSEydyflVOBzmhJDWTwuHv_0w_kb-Xe-qDLxzQ0/edit

## Alcance y cambios ejecutados
- Se preserva NU-20261102-A12-R2 y su DCF FCFE Base de US$14,42300446; R3 NO modifica precio ni motor de 10 años ni catálogo activo.
- Nueva pestaña «NU R3 · Control económico» en una copia completa de la hoja: riesgo de márgenes, Ke y reinversión, puente ROE terminal y capital regulatorio por país. Fórmulas nativas verificadas con lectura posterior.
- Análisis R3 Nivel 1: 14 capítulos conservados con adendas en ciclos, calidad de utilidad, drivers, capital/ROE, Ke, valoración y múltiplos.
- Nivel 2: 12 secciones conservadas con trazabilidad de fórmulas, fuentes, cuatro probabilidades y pruebas de sensibilidad.

## Resultados de recálculo en hoja candidata (US$/acción)
| Control | Resultado | Nota |
|---|---:|---|
| DCF R2 Base | 14,42300446 | Intacto |
| MOS35 | 9,374952901 | Intacto |
| Valor esperado con cuatro historias | 12,25271513 | 40 % Base +22,5 % Cons +22,5 % Opt +15 % Disrupción |
| Margen neto −2 pp en años 1-10 | 12,29951104 | Terminal con NI ajustada |
| Ke Base +1 pp | 12,43746385 | Terminal descontado a Ke mayor |
| Deriva APR +3,8 % en cada año 1-10 | 13,19411658 | **Parcial:** terminal Base R2 fijo |
| τ constante en 33,3287 % | 13,80571904 | **Parcial:** terminal Base R2 fijo |

## Hallazgo central: ROE y capital
FCFE = NI − ΔEquity, con Equity = τ×APR (regla R2). El ROE medio del año 10 es 25,83 %, frente al ROE **marginal** terminal elegido de 16 %. La NI11 implícita es US$15.087,88 millones. El terminal con g=4 % requiere US$3.771,97 millones de reinversión, frente a US$2.246,37 millones que arrojaría continuar τ10×APR10×g. Diferencia US$1.525,60 millones. No fusionar estas dos metodologías sin explicar transición.

### Capital prudencial observado (USD millones, 6-K nota 33)
| Jurisdicción | APR de referencia | Capital | Ratio | Mínimo / equivalente |
|---|---:|---:|---:|---:|
| Brasil | 35.710,139 | 5.597,604 | CAR 15,7 % | Requerido 3.749,565 |
| México | 2.869,611 (inferido) | 427,572 | 14,9 % | 10,5 % |
| Colombia | 1.174,778 (inferido) | 179,741 | 15,3 % | 10,5 % |

**No** tratar exceso sobre mínimos como caja distribuible ni usar una tasa consolidada ficticia. Nu Holdings no tiene un único requerimiento regulatorio prudencial; sí sus filiales. El patrimonio consolidado no es igual a la suma de capital prudencial regulatorio.

### Impuestos
1S26: utilidad antes de impuestos US$2.190,619 M; impuesto corriente −US$1.249,145 M; beneficio diferido +US$991,046 M; gasto por impuesto neto −US$258,099 M. La conciliación inicia con tasa brasileña de 42,5 %, pero la tasa efectiva de grupo depende de diferencias permanentes y de cada país. El margen neto Base supone normalización aún pendiente de bridge tributario. Evitar descontar automáticamente 10 % del FCFE global por retención brasileña sin ruta real de distribución.

## Bloqueos antes de promocionar R3
1. Reconstruir capital regulatorio/patrimonio inmovilizado, deducciones, colchones y remesabilidad por jurisdicción.
2. Calibrar cartera × APR y pérdidas por cosecha, excluyendo doble conteo en Ke.
3. Reconciliar impuesto corriente/diferido y tasa fiscal sostenible por jurisdicción.
4. Validar la transición ROE medio del 25,83 % a marginal del 16 % en perpetuidad.
5. Validar fuentes a corte 30-oct-2026 para ERP y prima país y ejecutar QA visual con sesión autenticada.
6. Ejecutar validadores del repo, CI y reconciliar ruta de publicación antes de reemplazar R2. P/E/P/BV siguen contraste peso cero; P/FCFE sin ancla.

## Fuentes primarias
- [Estados intermedios Nu 2T26, 6-K SEC](https://www.sec.gov/Archives/edgar/data/1691493/000129281426004225/nufs2q26_6k.htm), notas 30 (impuestos) y 33 (capital).
- [Resultados Nu 2T26](https://nu.com/es/sala-de-prensa/compania/nu-holdings-ltd-reporta-los-resultados-financieros-del-segundo-trimestre-de-2026).
- [Damodaran ERP y country risk](https://pages.stern.nyu.edu/adamodar/New_Home_Page/home.htm).
