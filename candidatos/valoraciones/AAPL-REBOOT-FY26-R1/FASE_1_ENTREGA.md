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

## Mercado y tasas
- **Tasa libre (Treasury 10 años), 2026-11-06:** 4,86 % (FMP `treasury-rates`).
- **Alerta:** `JMR-valuation/reference/corte_vigente.json` registra Rf = 5,29 % al 2026-09-30 como «FRED DGS10»; ese valor coincide con el Treasury a 20 años de FMP (5,29 %), no con el de 10 años. Verificar contra FRED antes de usar esa referencia en otras empresas.
- **Prima de riesgo (ERP): decisión pendiente para R3.** El repositorio registra 3,70 % como ERP de mercado maduro (Damodaran, oct-2026); la búsqueda web da 4,14 % de ERP implícita del S&P 500 al 1-sep-2026, y no se localizó el dato de nov-2026. En el libro DCF la hoja `Country equity risk premiums` usa un ERP maduro en B1.

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
| Rf verificada | PARCIAL (una sola fuente: FMP) |
| ERP definida | NO_EJECUTADO (pendiente de decisión) |
| Análisis con plantilla Reboot | NO_EJECUTADO (plantilla Floyd provisional) |
| `PASOS` | 6/6 de R1 · `AISLAMIENTO=OK` solo para los cinco libros |

## Siguiente paso exacto
R2: cargar en el libro 01 HISTÓRICOS (`Income Statement`, `Balance Sheet`, `Cash Flow Statement` y `Entradas históricas auxiliares`) las cifras FY2017–FY2026 del 10-K y los 10-K anteriores, con fuente por partida en `Fuentes y clasificación`, y conciliar balance, EBIT y caja.
