# AAPL-REBOOT-FY26-R1 · Fase R1 (corte e identidad)

- **Ticker:** AAPL · Apple Inc. (CIK 0000320193) · USD, millones · NASDAQ
- **Revisión:** AAPL-REBOOT-FY26-R1 · `perfil_valoracion=Reboot` · `contratoLibros=jmr-reboot-3libros-v1`
- **Corte contable:** 2026-09-26 (FY2026, 10-K presentado el 2026-11-03) · LTM = FY2026
- **Precio fechado:** 342,37 USD, cierre del 2026-11-06 (Alpha Vantage TIME_SERIES_DAILY). Cierre del 2026-11-09: 350,69 USD (solo referencia).
- **Fecha de la entrega:** 2026-11-09 · **Agente:** Claude (Code, en la nube), herramientas: Drive, Sheets, FMP, Alpha Vantage. Esfuerzo: bajo.

## Archivos (carpeta Drive `Modelo JMR/Análisis/AAPL`)
| Archivo | ID | Plantilla origen |
|---|---|---|
| 01 HISTÓRICOS | `1b1G1RciCJYH-J-RLXZhQX90RBlEZ-GY4qi13vSOdxEs` | `1DWY01fy7Zikb-MTY8ycoCTAVEncqKdjJefQEPWh6n08` |
| 02 DCF BASE | `1FDKimjBtpWeJO1wjK2-iFbQBhc7fziRWspCqkl41am8` | `1w51-vAGJS2_2CHuGv24124wiQixB8a9D62Pt3NWloxE` (02b) |
| 02 DCF CONSERVADORA | `1z7399gpLt0t0IMTgvXav4u6tEEsCIevd-GSE1U7KMcM` | `1nh7V0GW-ZWZMRdIbGW_fGtlcAb5qQd6uuNXEUKQ8iOA` (02) |
| 02 DCF OPTIMISTA | `18_DpC1IBerZBKzBpWWkSi-9h4EzXH_fIlesGqmeKffM` | `1nh7V0GW-ZWZMRdIbGW_fGtlcAb5qQd6uuNXEUKQ8iOA` (02) |
| 03 MÚLTIPLOS | `1SJn1NC6zGAWvMPOS6yK-0TxheNlZ0oabBPX8yaqpXmg` | `1J1wpGYvTpMozhCy3YSM-IO3BbXM7B5c0lZtRj6dyZWU` |
| 04 ANÁLISIS | `1GR89kYVx8XwfJUEmKFqiYQjq5aGTjYGTcvYlDOh3MmU` | `13TJsT-I5bieP-tgvYYo6N_QG5O-seUHUxYC7KzGEF6A` (Floyd, **provisional**) |

Los cinco libros son copias directas de Drive de plantillas ya verificadas (motor Ginzu original sin cambios; 0 errores en H y M). La carpeta ya contenía tres archivos Floyd de un intento previo (`AAPL-FLOYD-FY26-R1`); **no se usan como insumo** y no se modificaron.

## Mercado y tasas (verificadas el 2026-11-09)
- **Tasa libre (Treasury 10 años, FRED DGS10):** 4,86 % el 2026-11-06, la fecha del precio. Coincide exactamente con FMP `treasury-rates`. FRED aún no publica el 9-nov; FMP da 4,88 % ese día (referencia). Se usa **4,86 %**, alineada con el precio.
- **Corrección a la versión anterior de esta entrega:** `JMR-valuation/reference/corte_vigente.json` (Rf 5,29 % al 2026-09-30) **es correcto**: FRED DGS10 de ese día es 5,29 %. La sospecha de que fuera el Treasury a 20 años era un error de comparación. No hay nada que corregir.
- **Prima de riesgo de Damodaran (archivos oficiales descargados de `pages.stern.nyu.edu/~adamodar/pc/implprem/`):**
  | Dato | Oct-2026 | **Nov-2026** |
  |---|---|---|
  | S&P 500 al inicio del mes | 7.651,54 | **7.580,07** |
  | Treasury 10 años usado | 5,29 % | **4,94 %** |
  | ERP implícita con Treasury como tasa libre (calculadora C45) | 3,70 % | **3,387 %** |
  | ERP implícita con tasa libre ajustada por riesgo de default (C44) | 3,917 % | 3,607 % (tasa libre ajustada 4,72 %) |
  | Rendimiento esperado implícito del S&P 500 | 8,99 % | 8,33 % |
  El 3,70 % del repositorio (`erp_madura`) es el C45 de octubre, así que el repositorio sigue la práctica «ERP implícita del mes con el Treasury como tasa libre».
  Otras variantes de la serie mensual de noviembre: T12m 3,79 %; con pago sostenible 4,41 %; suavizada 5,81 %; normalizada 3,39 %; rendimiento neto de caja 3,43 %.
- **ERP propuesta para R3: 3,387 %** (nov-2026, C45), con Treasury 4,86 %. Es una entrada de `Country equity risk premiums!B1`, que en el original de Damodaran dice 4,23 % «actualizado el 1-ene-2026»; el propio original indica que cambiar B1 actualiza todas las primas por país. **Pendiente de confirmación del usuario** antes de escribirla en los libros DCF. Las primas por país de esa hoja (enero 2026) no se tocan.
- Nota: Moody's rebajó a EE. UU. a Aa1 en 2025; Damodaran reporta también una versión con tasa libre ajustada (4,72 % y ERP 3,607 %). La suma tasa libre + ERP queda casi igual (8,25 % frente a 8,33 % implícito).

## Idoneidad del motor
AAPL es una empresa operativa con FCFF positivo, sin banco ni holding. Idoneidad Simple Ginzu FCFF: **sí**.

## Datos primarios identificados (para R2)
- 10-K FY2026 (CIK 0000320193, presentado 2026-11-03). Cifras de control FY2026 (FMP, a verificar contra el 10-K en R2): ingresos 478.834; utilidad operativa 158.063; utilidad neta 132.175; acciones diluidas promedio 14.720,3 millones.
- Series históricas hasta diez FY: FMP `statements` y Alpha Vantage como contraste; el 10-K manda ante cualquier diferencia.

## Controles
| Control | Estado |
|---|---|
| Copias creadas y aisladas | APROBADO (IDs verificados en Drive) |
| Guía y empresa del libro H cargada | APROBADO |
| Integridad del motor DCF en las copias | APROBADO por herencia de la plantilla verificada; **no se re-verificó cada copia** |
| Rf verificada | APROBADO (FRED DGS10 y FMP coinciden: 4,86 % al 2026-11-06) |
| ERP definida | PARCIAL (propuesta 3,387 %, nov-2026, Damodaran C45; falta confirmación y no se ha escrito en los libros) |
| Análisis con plantilla Reboot | NO_EJECUTADO (plantilla Floyd provisional) |
| `PASOS` | 6/6 de R1 · `AISLAMIENTO=OK` solo para los cinco libros |

## Siguiente paso exacto
R2: cargar en el libro 01 HISTÓRICOS (`Income Statement`, `Balance Sheet`, `Cash Flow Statement` y `Entradas históricas auxiliares`) las cifras FY2017–FY2026 del 10-K y los 10-K anteriores, con fuente por partida en `Fuentes y clasificación`, y conciliar balance, EBIT y caja.
