# Inventario de sensibilidad por múltiplos — 20 revisiones Método A-1.2

**Inspección de solo lectura — 30 de octubre de 2026, hora Colombia.**
Objetivo: separar la existencia de celdas nativas en Google Sheets de su
**exportación, auditoría y publicación**. No se modificaron hojas, fórmulas,
proyecciones ni valoraciones. Los expedientes oficiales siguen en `EN_REVISION`.

## Criterios de la inspección

- Fuente: ID `sheet_id` registrado en cada una de las 20 valoraciones del
  `catalogo.json` del PR #211; pestaña `Sensibilidad por múltiplo`,
  rango `A76:I144`; salida numérica `UNFORMATTED_VALUE`.
- Para `OK`: encabezado de historia Base, 25 valores numéricos de la grilla
  5×5, centro numérico y coincidencia con `VP3 original` de la propia hoja.
- `N/D`: estado real de la hoja, **no es sinónimo de no aplicable** ni de
  método incorrecto. Requiere análisis de signo, denominador, ponderación y
  fuente. `—` significa celdas vacías o sin control reportado.
- Este inventario verifica valores y conciliación de centros **en las
  celdas consultadas**, no todas las fórmulas, las anclas económicas,
  las fuentes contables ni el resultado completo de valoración. Tampoco
  acredita que las matrices ya existan en el JSON público.

## Matrices de la hoja verificadas por método

| Ticker | EV/EBITDA | EV/FCFF | P/E | P/FCFE | P/OCF | P/V (opcional) | P/BV (opcional, salvo bancos) | Prioritarios OK |
|---|---|---|---|---|---|---|---|---|
| SHAK | OK | N/D | OK | N/D | OK | OK | OK | 3/5 |
| UBER | N/D | N/D | N/D | N/D | N/D | N/D | N/D | 0/5 |
| MELI | OK | N/D | OK | N/D | OK | OK | OK | 3/5 |
| CELH | OK | OK | OK | OK | OK | OK | OK | 5/5 |
| ADBE | OK | OK | OK | OK | OK | OK | OK | 5/5 |
| BSX | OK | OK | OK | OK | OK | OK | OK | 5/5 |
| CMG | OK | OK | OK | OK | OK | OK | OK | 5/5 |
| NFLX | OK | OK | OK | OK | OK | OK | OK | 5/5 |
| GOOGL | OK | OK | N/D | N/D | N/D | OK | N/D | 2/5 |
| MSFT | OK | OK | OK | OK | OK | OK | OK | 5/5 |
| NKE | OK | OK | OK | OK | OK | OK | OK | 5/5 |
| PYPL | OK | OK | OK | OK | OK | OK | OK | 5/5 |
| EPAM | OK | OK | OK | OK | OK | OK | OK | 5/5 |
| ZTS | OK | OK | OK | OK | OK | OK | OK | 5/5 |
| ONON | OK | OK | OK | OK | OK | OK | OK | 5/5 |
| NU | — | — | — | — | — | — | — | 0/3 bancarios |
| NVO | OK | OK | OK | OK | OK | OK | N/D | 5/5 |
| INTU | N/D | N/D | N/D | N/D | N/D | N/D | N/D | 0/5 |
| AFYA | OK | OK | OK | OK | OK | OK | OK | 5/5 |
| DUOL | OK | OK | OK | OK | OK | OK | OK | 5/5 |

**Resultado:** 14 empresas operativas con cinco métodos prioritarios
presentes y centros conciliados en las celdas de Sheets; tres con
métodos pendientes de definir (SHAK, MELI, GOOGL); dos con siete métodos
N/D (UBER, INTU); y una financiera (NU) cuya hoja tiene estructura
industrial vacía, no un contrato bancario completado.

## Excepción sectorial NU

NU utiliza **DCF FCFE bancario regulatorio** como valor Base; los depósitos
no son deuda industrial. Su valoración activa ya indica explícitamente
P/E, P/FCFE y P/BV como *pendientes de anclas, fiscalidad, regulación y
comparables*. La pestaña `Sensibilidad por múltiplo` existe, pero las
grillas industriales `A76:I144` están vacías; hay pestañas separadas
`FCFE bancario A` y `Sensibilidad FCFE A`. **No declarar 0/5
industriales como error económico de NU ni aprobar sus tres múltiplos
bancarios por omisión.** El gate exige P/E, P/FCFE y P/BV verificables
antes de cerrar la parte relativa de NU.

## Ruta de salida sin inventar cifras

1. Para las 14 con celdas 5/5 OK: capturar la misma hoja y revisión,
   comprobar SHA256 de la foto, generar el candidato de matrices 5×5 con
   `JMR-valuation/scripts/jmr_native_sens_candidate.py`, conciliar con
   `VP3` del JSON y preparar versión candidata con
   `jmr_native_record_candidate.py` **sin sustituir el registro activo**.
2. Para SHAK y MELI: investigar EV/FCFF y P/FCFE negativos. Para GOOGL:
   revisar P/E, P/FCFE y P/OCF N/D; documentar N/A con razón económica
   solo cuando realmente corresponda.
3. Para UBER e INTU: revisar insumos `Financials Multiples`, anclas y
   `Descuento de múltiplos` desde Sheets. No convertir N/D en cero,
   ni asumir que los siete métodos carecen de sentido económico.
4. Para NU: aplicar contrato bancario FCFE y completar comparables,
   anclas y sensibilidad P/E, P/FCFE, P/BV. No imponer EV/EBITDA ni FCFF.
5. Solo después: hacer QA de la ficha única y validar cadena
   **hoja → snapshot → candidato → JSON oficial → app**, sin publicar un
   candidato con `CANDIDATO_NO_PUBLICADO` como resultado certificado.

**No es auditoría económica ni informe de valoración.** El PR #211
permanece en revisión y su gate financiero **debe continuar bloqueando**
toda afirmación de completitud hasta resolver lo anterior.
