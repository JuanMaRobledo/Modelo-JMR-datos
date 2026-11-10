# MSFT-REBOOT-3T26-R1 · Fase R1 (corte e identidad)

- **Ticker / revisión:** MSFT (Microsoft Corporation) · `MSFT-REBOOT-3T26-R1` · perfil Floyd R1–R6, contrato `jmr-reboot-3libros-v1`. El «3T26» es el trimestre calendario del corte; para Microsoft es el **primer trimestre del año fiscal 2027**.
- **Fecha:** 2026-11-10 · **Agente:** Claude (Code, nube) · herramientas: Google Drive/Sheets, SEC XBRL (data.sec.gov), Alpha Vantage. Estado **CANDIDATO**.
- **Mercado / moneda / escala:** NASDAQ · USD · millones, por acción en dólares.
- **Corte:** año fiscal que termina el 30 de junio. Último FY: **FY2026 (10-K presentado el 29-jul-2026)**; 10-Q del 1T-FY2027 (30-sep-2026, presentado el 28-oct-2026). LTM = FY2026 + 3M-FY2027 − 3M-FY2026; balance al 30-sep-2026. Las diez columnas anuales son FY2017–FY2026.
- **Precio fechado:** **530,61 USD**, cierre del 6-nov-2026 (Alpha Vantage `TIME_SERIES_DAILY`). Referencias: 9-nov-2026 545,18; cierre de FY2026 (30-jun-2026) 373,02. La acción subió 49 % desde el 29-jul-2026 (390,54) tras el 10-K y 20 % desde el 10-Q.
- **Tasa libre / prima:** 4,86 % (FRED DGS10, 6-nov-2026); prima madura 3,387 % (Damodaran, nov-2026). Iguales a las de las demás revisiones de esta rama.
- **Idoneidad del motor:** empresa operativa de software y nube, cubierta por FCFF Simple Ginzu. Sin excepción FCFE/SOTP. Decisiones de método anticipadas por la evidencia del 10-K/10-Q (se desarrollan en R2–R3 y quedarán en `salvedades`):
  1. **Arrendamientos financieros como deuda** (≈ 66.600 M a junio de 2026; 2.471 M de costo en el trimestre): su amortización está en el EBIT pero su interés no; es financiamiento de centros de datos, no alquiler operativo.
  2. **Arrendamientos operativos no son deuda** (criterio del usuario del 10-nov-2026; el EBIT ya deduce el alquiler).
  3. **Inversión en OpenAI** (método de participación) y demás inversiones: activo no operativo a valor en libros, con la volatilidad de sus resultados fuera del EBIT.
  4. **Gasto de capital extraordinario** (115.948 M en FY2026; +20.000 M en el trimestre): la reinversión de las historias debe reflejar el ciclo de inversión en IA, no el histórico.
- **Antecedentes:** el catálogo no tiene revisión activa de MSFT; la ficha A-1.2 está archivada y **no es insumo**.

## Los seis archivos (carpeta Drive `1qX-M15odmTYkiQtcTLqV0VuyokHnAdLC`)
| Archivo | ID |
|---|---|
| 01 HISTÓRICOS (H) | `1t5ZM7SQF-An3WMJXfdYb0Q_XGHeJuiBY_rervY7eK8E` |
| 02 DCF BASE (D-B) | `19f9zo6xbYTnrjoAZwVf5ViHzVCEnkde9no2cryOBQjA` |
| 02 DCF CONSERVADORA (D-C) | `1TF-_XL14nxdAgNkHzJN3w5plZzOPj54rN2jnFfB33ho` |
| 02 DCF OPTIMISTA (D-O) | `13yJEdR4nTxVwE7b2bspxRGi8Pyk9Q_guwTmQdK36EMg` |
| 03 MÚLTIPLOS (M) | `1m_mbps0ZIVzsDUNyz76UzPGhei5YLuWwnSffk10496o` |
| 04 ANÁLISIS (A) | pendiente (R5) |

Copias directas de las plantillas del contrato. **No se verificó** aún el motor celda a celda (R3/R6).

## Controles
| Control | Estado |
|---|---|
| Seis IDs distintos (cinco creados; A pendiente) | APROBADO (5/6) |
| Fuente primaria y corte (10-K FY2026; 10-Q 1T-FY2027) | APROBADO |
| Precio fechado y tasa libre | APROBADO |
| Integridad del motor en las copias | NO_EJECUTADO |
| `AISLAMIENTO=OK` | Verificado: ningún dato de la ficha A-1.2 archivada se usa |

**PASOS 4/4.** Siguiente paso exacto: R2, cargar H por etiqueta con el XBRL (FY2017–FY2026 + LTM), clasificar arrendamientos financieros, inversiones y efectivo, y conciliar balance, EBIT, caja y LTM.
