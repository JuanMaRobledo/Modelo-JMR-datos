# F1 · CMG · Modelo JMR Floyd · CMG-FLOYD-20261108-R1 — entrega: CERRADA

**Fecha:** 2026-11-08 · **Perfil:** `perfil_valoracion=Floyd`, `version_metodo=Floyd` (motor Simple Ginzu FCFF, tres historias) · **Estado:** CANDIDATO
**Corte contable:** 30-sep-2026 (10-Q 3T-26, acc. 0001058090-26-000104) · último FY: 31-dic-2025 (10-K, acc. 0001058090-26-000009) · **LTM = FY2025 + 9M-26 − 9M-25.**
**Corte de mercado:** cierre del 6-nov-2026 = US$34,43 (Alpha Vantage, NYSE). **Corte de supuestos financieros:** Damodaran ERPNov26 (1-nov-2026): T-bond 4,94 %, ERP maduro implícito 3,387 %; Treasury a 10 años del 6-nov-2026 = 4,86 % (home.treasury.gov), diferencia de 8 pb sin efecto material (se mantiene el par Rf/ERP del mismo archivo).
**Herramienta/modelo/esfuerzo:** Claude Code en la nube, modelo configurado `claude-sonnet-5-5`; el entorno no reporta el esfuerzo de razonamiento. **PASOS: 3/3 ejecutados.** `AISLAMIENTO=OK` (ver abajo).

## Hechos ejecutados
1. **Identidad y motor.** CMG, NYSE, USD millones, CIK 1058090, una acción ordinaria (split 50:1 del 26-jun-2024 aplicado). Operativa FCFF, sin segmentos separables (un solo segmento reportable), sin deuda financiera: Simple Ginzu FCFF es idóneo; no hay bloqueo de motor.
2. **Revisión y copia limpia.** Se creó `CMG-FLOYD-20261108-R1` en *Modelo JMR Floyd / Análisis / CMG* (carpeta `15Hlb2LQ4RgauCY31L2zyRLeMdgZ_0YSD`) copiando la Maestra Floyd `157EabbntPVoydBgBZNjp90BBjoliGDOts2E0MxNVKSc` ("Plantilla Maestra (3 escenarios) · 2026-11-08", 54 pestañas). **Valoración:** `1f7BMt0ynbvjFUT84ftUmkPfxyJvmPvcqQ-7GW7EWtAY`. La plantilla y los archivos A-1.2 no se modificaron.
3. **Aislamiento.** CMG-20261028-A3 y CMG-A3-LTMSEP2026-REV20261103 (A-1.2) se leyeron solo como referencia de comparación en F4: ninguna cifra de esas revisiones es insumo. Los datos salen del XBRL de la SEC, del 10-K/10-Q, de Alpha Vantage y de Damodaran.

## Mapa de insumos materiales (hoja → celda → valor → fuente → estado)
| Dato | Celda (valoración) | Valor | Fuente | Estado |
|---|---|---|---|---|
| Ingresos LTM | Income Statement!L3 → Input B12 | 12.713,5 | 10-K FY25 + 10-Q 3T-26 (XBRL Revenues) | reportado/derivado LTM |
| EBIT LTM | Income Statement!L12 → Input B13 | 1.794,9 (14,12 %) | XBRL OperatingIncomeLoss | reportado/derivado |
| Gasto por intereses | Income Statement!L15 → Input B14 | no desglosado | sin deuda; revolver de 500 M sin dispuesto | NO APLICABLE |
| Patrimonio contable | Balance Sheet!L35 → B15 | 2.455,1 | 10-Q balance | reportado |
| Deuda financiera | Balance Sheet!L20,L25 → B16 | 0 | 10-Q: sin préstamos | NO APLICABLE (cero sustentado) |
| Caja + inversiones CP | Balance Sheet!L5 → B19 | 902,6 (634,2 + 268,4) | 10-Q balance | reportado |
| Inversiones no operativas | B83/B84 | 100,4 | 10-Q: inversiones LP | reportado; sin solapamiento |
| Interés minoritario / preferentes | B21 / B76 | 0 / 0 | sin NCI ni preferentes | NO APLICABLE |
| Acciones | Income Statement!L27 → B22 | 1.264,975 + 5,174 RSU/PSU = 1.270,149 | portada 10-Q (26-oct-26); RSU 4,138 + PSU esperadas 1,036 | reportado |
| Opciones (SOSARs) | B38:B42 | 12,268 M; strike 39,51; 4,2 años; σ 35 % | 10-Q nota 7; σ propia (diaria 49 % con saltos de resultados; mensual 33 %) | reportado / **HIPÓTESIS σ** (valor 10,37/opción = 127 M, 0,3 % del patrimonio) |
| Precio | D1 | 34,43 | 6-nov-2026 | mercado fechado |
| Rf / ERP | B35; Country ERP!B2; CoC B27 | 4,94 % / 3,387 % | Damodaran ERPNov26 | tasa |
| Beta | CoC B23 | 0,8585 | 0,783 desapalancada Restaurantes/Dining (Damodaran ene-2026) re-apalancada con arrendamientos 5.599 / capitalización 43.553 | **HIPÓTESIS** documentada |
| Costo de deuda | CoC B35 | 5,6 % | inactivo (peso 0 %) | HIPÓTESIS sin efecto |
| Impuesto | B24 / B25 | 24,74 % / 25 % | 10-Q nota 8; 10-K tasa estatal ~3,9 % | reportado / supuesto |
| Arrendamientos ASC 842 | B18=No; B123/B124 | 5.599,0 (LTM) / 5.075,8 (FY) | 10-Q balance | reportado (tratamiento en F3) |
| I+D | B17 = No | — | no reportada | NO APLICABLE |
| NOL | B62 = No | — | sin pérdidas fiscales a trasladar | NO APLICABLE |
| Fracaso | B52 = No | — | sin deuda; FCF positivo | NO APLICABLE |

Pestañas auxiliares revisadas: `Option value` (validada), `R& D converter` y `Operating lease converter` (no activadas), `Synthetic rating` (no aplica: sin deuda), `Cost of capital worksheet` (Detailed validado, WACC 7,85 %), `Failure Rate worksheet` (no aplica), `Financials Multiples`/5 hojas de múltiplos (F3).

## Controles
- Integridad: `Huella motor` = 0 diferencias (APROBADO, calculado por la propia hoja).
- Cobertura: todas las entradas materiales del grafo de fórmulas de `Input sheet`, costo de capital y opciones tienen fuente y estado; las no aplicables se justifican arriba. APROBADO.
- `CONTRATO_INSUMOS_FASE_1.md` como algoritmo de cobertura: ejecutado manualmente sobre las fórmulas reales; no existe script. PARCIAL (equivalente manual).

## Salvedades
Beta y σ de opciones son hipótesis (impacto inferior al 0,5 % del valor por σ; beta se somete a sensibilidad en F3). No hay DCF definitivo en esta fase.

## Siguiente: F2 (Históricos y H2) → F3 (supuestos y valoración).
