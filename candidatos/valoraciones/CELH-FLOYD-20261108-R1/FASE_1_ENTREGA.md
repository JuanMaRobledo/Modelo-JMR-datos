# F1 · CELH · Modelo JMR Floyd · CELH-FLOYD-20261108-R1 — entrega: CERRADA

**Fecha:** 2026-11-08 · **Perfil:** `perfil_valoracion=Floyd`, `version_metodo=Floyd` (motor Simple Ginzu FCFF, tres historias) · **Estado:** CANDIDATO
**Corte contable:** 30-sep-2026 (10-Q 3T-26, acc. 0001341766-26-000062, presentado 5-nov-2026) · último FY: 31-dic-2025 (10-K, presentado 2-mar-2026) · **LTM = FY2025 + 9M-26 − 9M-25.**
**Corte de mercado:** cierre del 6-nov-2026 = US$32,16 (Alpha Vantage, NASDAQ). **Supuestos financieros:** Damodaran ERPNov26 (1-nov-2026): T-bond 4,94 %, ERP madura implícita 3,387 %.
**Herramienta/modelo/esfuerzo:** Claude Code en la nube, modelo configurado `claude-sonnet-5-5`; el entorno no reporta el esfuerzo de razonamiento. **PASOS: 3/3 ejecutados.** `AISLAMIENTO=OK`.

## Hechos ejecutados
1. **Identidad y motor.** CELH, NASDAQ, USD millones, CIK 1341766, una clase de acción ordinaria (split 3:1 de nov-2023 aplicado a las series previas). Operativa FCFF; un solo segmento reportable (10-Q nota 14), sin utilidad por marca → **Segmentos = NO USADO**. Hay dos series de preferentes convertibles de PepsiCo (mezzanine) que se tratan como derecho híbrido en WACC y en el puente patrimonial; no obligan a otro motor. No hay bloqueo.
2. **Revisión y copia limpia.** Se creó `CELH-FLOYD-20261108-R1` en *Modelo JMR Floyd / Análisis / CELH* (carpeta `159n8fISRbeUAp4TWNxL0R0HbF0KJ5ls-`) copiando la Maestra Floyd `157EabbntPVoydBgBZNjp90BBjoliGDOts2E0MxNVKSc` (54 pestañas). **Valoración:** `1i7KsD5LJ98XOVjVPrS355weuaSuNo_ISuMVSHS_4MhU`. **Históricos:** `1MLwY0b7u4pKUgu5hDzj0hN2S73yu_Ng323zAcUCY8qg`. La plantilla y los archivos A-1.2 no se modificaron.
3. **Aislamiento.** `CELH-20261028-A1` (A-1.2, ahora en `archivoFloyd`) se conserva intacta y solo se usa como referencia de comparación en F4; ninguna cifra de esa revisión es insumo. Los datos salen del XBRL de la SEC, del 10-Q 3T-26, de Alpha Vantage y de Damodaran.

## Mapa de insumos materiales (hoja → celda → valor → fuente → estado)
| Dato | Celda (valoración) | Valor | Fuente | Estado |
|---|---|---|---|---|
| Ingresos LTM | Income Statement!L3 → Input B12 | 3.169,4 | XBRL FY25 + 10-Q 3T-26 | reportado/derivado LTM |
| EBIT LTM | Income Statement!L12 → B13 | 412,4 (13,0 %) | XBRL OperatingIncomeLoss | reportado; incluye 169,5 de comisiones por terminación de distribuidores (no recurrentes) |
| Gasto por intereses | Income Statement!L15 → B14 | 47,3 | XBRL InterestExpenseNonoperating | reportado/derivado |
| Patrimonio contable | Balance Sheet!L35 → B15 | 3.035,3 | 10-Q: patrimonio 1.275,4 + mezzanine 1.760,0 | reportado |
| Deuda financiera | Balance Sheet!L20,L25 → B16 | 674,7 | 10-Q nota 10: principal 693,0 menos descuento 18,3 | reportado (valor contable) |
| Caja | Balance Sheet!L5 → B19 | 700,6 | 10-Q balance (sin caja restringida a 30-sep) | reportado |
| Inversiones no operativas | B82:B87 | 0 | 10-Q: sin asociadas ni valores | NO APLICABLE |
| Interés minoritario | B21 | 0 | sin NCI | NO APLICABLE |
| Acciones | Income Statement!L27 + B122 → B22 | 251,725 + 2,078 RSU/PSU = 253,803 | 10-Q balance y nota 13 | reportado |
| Opciones | B38:B42 / Option value | 2,313 M; strike 6,28; 2,5 años; σ 50 % | 10-K FY25 (último dato; el 10-Q no lo actualiza); σ y plazo | reportado / **HIPÓTESIS** (valor 61,5 M = 0,7 % del patrimonio) |
| Preferentes Serie A y B | B76; CoC B49:B51, B97:B109 | 1.550,1 | 10-Q nota 12: 1,467 M × $375 + 0,390 M × $1.500; 5 % en efectivo; conv. $25,00 y $51,75; ago-2032 | componente financiero 981,8 (8 %) + opciones de conversión 568,3 (Black-Scholes, σ 50 %, 5,8 años) = **HIPÓTESIS** documentada |
| Precio | D1 | 32,16 | 6-nov-2026 | mercado fechado |
| Rf / ERP | B35; Country ERP!B2; CoC B27 | 4,94 % / 3,387 % (ERP con CRP de ingresos no EE. UU.: 3,42 %) | Damodaran ERPNov26 | tasa |
| Beta | CoC B24 | 0,58 desapalancada Beverage (Soft) → 0,61 | Damodaran (ene-2026, de la plantilla) | **HIPÓTESIS**; sin beta propia de CELH |
| Costo de deuda | CoC B35 | 6,5 % antes de impuestos | intereses 9M-26 / deuda media | **HIPÓTESIS** |
| Impuesto | B24 / B25 | 19,3 % LTM / 25 % | XBRL / 21 % federal + ~4 % estatal | reportado / supuesto |
| Arrendamientos ASC 842 | B18 = No; B123/B124 | 0 (LTM) / 18,2 (FY25) | 10-K FY25; el 10-Q no los desglosa | inmaterial (0,4 % del EV): NO APLICA conversor |
| I+D | B17 = No | — | no reportada | NO APLICABLE |
| NOL | B62 = No | — | sin pérdidas a trasladar | NO APLICABLE |
| Fracaso | B52 = No | — | CFO LTM 331 M; deuda neta ≈ 0 | NO APLICABLE |

## Controles
- Integridad: `Huella motor` = 0 diferencias frente a la Maestra (calculado por la hoja). APROBADO.
- Cobertura de dependencias del grafo de `Input sheet`, WACC y opciones: todo con fuente y estado; las no aplicables, justificadas. APROBADO por inspección manual de fórmulas (no existe script). PARCIAL como equivalente manual de `CONTRATO_INSUMOS_FASE_1.md`.
- `Cost of capital worksheet`: Detailed = VALIDADO; control de preferentes B113 = VALIDADO.

## Salvedades
Beta, costo de deuda, σ de opciones y la valoración híbrida de los preferentes son hipótesis; se prueban en F3 (sensibilidad). El valor de deuda es contable (693,0 de principal): la diferencia de 18,3 es inferior al 0,1 % del EV.

## Siguiente: F2 (Históricos y H2) → F3 (supuestos y valoración).
