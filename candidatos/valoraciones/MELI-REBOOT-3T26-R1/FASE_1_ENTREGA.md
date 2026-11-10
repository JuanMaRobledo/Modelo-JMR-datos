# MELI-REBOOT-3T26-R1 · Fase R1 (corte e identidad)

- **Ticker / revisión:** MELI (MercadoLibre, Inc.) · `MELI-REBOOT-3T26-R1` · perfil Floyd R1–R6 (antes Reboot), contrato `jmr-reboot-3libros-v1`.
- **Fecha:** 2026-11-10 · **Agente:** Claude (Code, nube) · herramientas: Google Drive/Sheets, SEC XBRL (data.sec.gov), Alpha Vantage. Estado **CANDIDATO**.
- **Mercado / moneda / escala:** NASDAQ · USD (reporta en USD) · millones, por acción en dólares.
- **Corte:** FY2025 (10-K) + 10-Q del 3T-2026 (30-sep-2026). LTM = FY2025 + 9M-2026 − 9M-2025; balance al 30-sep-2026.
- **Precio fechado:** **1.510,00 USD**, cierre del 6-nov-2026 (Alpha Vantage `TIME_SERIES_DAILY`). La acción cayó 12 % el 5-nov-2026 (de 1.739,88 a 1.530,28), el día siguiente a los resultados del 3T; el cierre del 9-nov fue 1.532,68.
- **Tasa libre / prima:** 4,86 % (FRED DGS10, 6-nov-2026); prima madura 3,387 % (Damodaran, nov-2026). Sin cambios frente a AAPL, CMG y UBER de esta rama.
- **Idoneidad del motor (excepción declarada):** MELI mezcla comercio electrónico y logística con Mercado Pago (pagos, cuentas y una gran cartera de crédito). Por decisión del usuario (10-nov-2026) se valora con **un solo FCFF consolidado** (formato de seis archivos): la cartera de crédito queda dentro de los activos operativos y su financiamiento (préstamos y otras obligaciones financieras, notas) se resta como deuda; los fondos por pagar a clientes y su caja asociada quedan fuera del puente. No se ejecuta SOTP ni FCFE. Es un riesgo para R6, porque el FCFF de un negocio de crédito depende del tratamiento de la reinversión en cartera.
- **Antecedentes:** el catálogo no tiene revisión activa de MELI; las fichas A-1.2 y la reconstrucción Floyd F1–F5 del 9-nov están archivadas y **no son insumo**. Los archivos de la carpeta `MELI` de Drive anteriores a hoy no se usan.

## Los seis archivos (carpeta Drive `1asACoeaTypXHPkGu52jSH8wgqavdmwpZ`)
| Archivo | ID |
|---|---|
| 01 HISTÓRICOS (H) | `15Z4mnTqLAm05V0svSMbKS1jZB9VEMKRwCO6z4GwvyPI` |
| 02 DCF BASE (D-B, con Presentación y Resumen) | `174iyMLVgEsIw8sAWHNF3_SAvcbOoZbb1dB94gUF5yLc` |
| 02 DCF CONSERVADORA (D-C) | `1RYE2kFcPstfBAH2eTRkyiMwvw64XuOcgnofD9Jq8jPM` |
| 02 DCF OPTIMISTA (D-O) | `1fdZBeu5c4Agd54piuip2jnLL8HxM2yUbGOkGUKjgjd4` |
| 03 MÚLTIPLOS (M) | `19jUYjQ-KXnLUjvQBXzTJhIRHJgxN79BdOfoqdB7REJk` |
| 04 ANÁLISIS (A) | pendiente (R5) |

Copias hechas desde las plantillas del contrato (H `1DWY01fy…`, D-B `1w51-vAG…`, D-C/D-O `1nh7V0GW…`, M `1J1wpGYv…`). **No se verificó** aún que los tres D conserven el motor idéntico a la plantilla (se hizo copia directa de Drive, sin edición); la verificación celda a celda queda para R3/R6.

## Controles
| Control | Estado |
|---|---|
| Seis IDs distintos (cinco creados; A pendiente) | APROBADO (5/6) |
| Fuente primaria y corte (10-K FY2025; 10-Q 3T-2026 en XBRL) | APROBADO (datos accesibles) |
| Precio fechado y tasa libre | APROBADO |
| Integridad del motor en las copias | NO_EJECUTADO (copia directa de plantilla) |
| `AISLAMIENTO=OK` | Verificado: ningún dato de revisiones anteriores de MELI se usa como insumo |

**PASOS 4/4.** Siguiente paso exacto: R2, llenar H por etiqueta con el XBRL de la SEC (diez FY + LTM), clasificar la cartera de crédito, la deuda de financiamiento, los fondos de clientes y la caja restringida, y conciliar balance, EBIT y LTM.
