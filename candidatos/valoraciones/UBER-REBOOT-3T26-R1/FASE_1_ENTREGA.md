# UBER-REBOOT-3T26-R1 · Fase R1 (corte e identidad)

- **Ticker:** UBER · Uber Technologies, Inc. (CIK 0001543151) · USD, millones · NYSE
- **Revisión:** UBER-REBOOT-3T26-R1 · `perfil_valoracion=Reboot` · `contratoLibros=jmr-reboot-3libros-v1`. Reemplaza a la revisión Floyd vigente (UBER-FLOYD-3T26), que sigue activa en el catálogo hasta que esta pase sus puertas.
- **Corte contable:** 2026-09-30 (10-Q del 3T-2026, acc. 0001543151-26-000041, presentado el 2026-11-04). LTM = 4T-2025 + 9M-2026 (el 10-K FY2025 y los trimestres de 2026 se leen de SEC XBRL).
- **Precio fechado:** 68,59 USD, cierre del 2026-11-06 (Alpha Vantage TIME_SERIES_DAILY).
- **Fecha:** 2026-11-09 · **Agente:** Claude (Code, nube): Drive, Sheets, SEC companyfacts, Alpha Vantage.

## Archivos (carpeta Drive de UBER bajo `Modelo JMR/Análisis`)
| Archivo | ID | Plantilla |
|---|---|---|
| 01 HISTÓRICOS | `176tcVAz_RzHluf4kyjEEsMjDcDosldPdB5FBifO9YQA` | `1DWY01fy7Zikb-MTY8ycoCTAVEncqKdjJefQEPWh6n08` |
| 02 DCF BASE | `14QlydMFli2pxdG4agUYOAXL8QIE99P-3UDE7vwK8CaM` | `1w51-vAGJS2_2CHuGv24124wiQixB8a9D62Pt3NWloxE` (02b) |
| 02 DCF CONSERVADORA | `1TUDP8WvRpjtm5AbCpGkKkfyAlItRuufIAAEkFp95aHA` | `1nh7V0GW-ZWZMRdIbGW_fGtlcAb5qQd6uuNXEUKQ8iOA` (02) |
| 02 DCF OPTIMISTA | `1f7Fzs7TBezRNa4E0lwHoh8fcPXTGn0d09HTatCaDLRU` | `1nh7V0GW-ZWZMRdIbGW_fGtlcAb5qQd6uuNXEUKQ8iOA` (02) |
| 03 MÚLTIPLOS | `19fe8FcQ32d3yf169i-XA7F-c4IGhWTCNl_QO4WgCwA4` | `1J1wpGYvTpMozhCy3YSM-IO3BbXM7B5c0lZtRj6dyZWU` (con la corrección de `POCF!B56`) |
| 04 ANÁLISIS | pendiente: se crea en R5 desde HTML (en AAPL la copia de la plantilla Floyd se descartó) | — |

Copias directas de Drive de plantillas verificadas (motor Ginzu original sin cambios; la 02b ya trae el control `IF(ISNUMBER…)` de la Presentación). **No se re-verificó cada copia.** Los archivos Floyd de la misma carpeta no se tocan ni se usan como insumo.

## Mercado y tasas (las de la entrega R1 de AAPL, misma fecha de precio)
- **Tasa libre:** 4,86 % (FRED DGS10, 2026-11-06). **Prima madura:** 3,387 % (Damodaran, nov-2026), confirmada por el usuario para AAPL el 2026-11-09 y vigente para el mismo corte.
- **Idoneidad del motor:** empresa operativa con FCFF positivo; sin banco ni holding. Simple Ginzu FCFF: sí (a confirmar en R3 por el peso de las inversiones en participadas, que irían como activos no operativos).

## Controles
| Control | Estado |
|---|---|
| Copias creadas, aisladas y con ID registrado | APROBADO |
| 10-Q presente en SEC XBRL (`companyfacts`) | APROBADO |
| Precio del 2026-11-06 reconfirmado | APROBADO |
| Integridad del motor en cada copia | NO re-verificada (herencia de la plantilla) |
| Análisis con plantilla Reboot | NO_EJECUTADO (R5) |

## Siguiente paso exacto
R2: cargar en 01 HISTÓRICOS los estados FY2016–FY2025 (10-K) más 9M-2025 y 9M-2026 (10-Q) para construir el LTM, con fuente por partida, y conciliar balance, EBIT y caja.
