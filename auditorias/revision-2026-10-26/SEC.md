# Contraste con la SEC · 33 empresas · 26-oct-2026

Generado por `scripts/contrastar_sec.py` (XBRL `companyfacts` y `submissions` de data.sec.gov). Para el último período con ingresos en XBRL calcula ingresos LTM, activos, patrimonio y deuda, y busca esas cifras en el análisis y el registro guardados.

**Cómo leerlo.** «Conciliado» = el registro reproduce el ingreso LTM del último período publicado (exacto o a ≤1 %). Que no se encuentre una cifra **no prueba un error**: puede estar en otra moneda, otra unidad o con otra definición. Activos, patrimonio y deuda son indicios; la deuda usa el tag `LongTermDebt` y puede diferir de la definición del registro (con papel comercial, arrendamientos, etc.).

| Empresa | Resultado | Último informe SEC | Período que reproduce el registro | Ingresos LTM SEC (M) | Activos | Patrimonio | Deuda | 8-K/6-K posteriores al registro |
|---|---|---|---|---:|:-:|:-:|:-:|---|
| AAPL | CONCILIADO | 2026-06-27 (10-Q) | 2026-06-27 | 466,823.0 | ✓ | ✓ | ✗ | 0 |
| ADBE | CONCILIADO | 2026-08-28 (10-Q) | 2026-08-28 | 25,970.0 | ✓ | ✓ | ✓ | 0 |
| ADSK | CONCILIADO | 2026-07-31 (10-Q) | 2026-07-31 | 7,790.0 | ✓ | ✓ | ✓ | 0 |
| AFYA | CONCILIADO (solo 20-F anual) | 2025-12-31 (20-F) | 2025-12-31 | 3,697.3 | ✗ | ✗ | — | 0 |
| AMZN | CONCILIADO | 2026-06-30 (10-Q) | 2026-06-30 | 775,680.0 | ✓ | ✓ | ✓ | 0 |
| BSX | CONCILIADO | 2026-06-30 (10-Q) | 2026-06-30 | 20,996.0 | ✓ | ✓ | ✓ | 1: 2026-10-07 8-K |
| CELH | CONCILIADO | 2026-06-30 (10-Q) | 2026-06-30 | 3,047.3 | ✓ | ✓ | ✗ | 0 |
| CMG | CONCILIADO | 2026-06-30 (10-Q) | 2026-06-30 | 12,423.8 | ✓ | ✓ | — | 0 |
| DPZ | CONCILIADO | 2026-09-06 (10-Q) | 2026-09-06 | 5,066.4 | ✓ | ✓ | ✓ | 1: 2026-10-13 8-K |
| DUOL | CONCILIADO | 2026-06-30 (10-Q) | 2026-06-30 | 1,145.0 | ✓ | ✓ | — | 0 |
| EPAM | CONCILIADO | 2026-06-30 (10-Q) | 2026-06-30 | 5,616.7 | ✓ | ✓ | ✗ | 0 |
| GOOG | CONCILIADO | 2026-06-30 (10-Q) | 2026-06-30 | 445,866.0 | ✓ | ✓ | ✓ | 0 |
| INTU | CONCILIADO | 2026-07-31 (10-K) | 2026-07-31 | 21,448.0 | ✓ | ✓ | ✓ | 0 |
| LULU | CONCILIADO | 2026-08-02 (10-Q) | 2026-08-02 | 11,094.0 | ✓ | ✓ | — | 2: 2026-10-22 8-K, 2026-10-07 8-K |
| MCD | CONCILIADO | 2026-06-30 (10-Q) | 2026-06-30 | 27,702.0 | ✓ | ✓ | ✓ | 0 |
| META | CONCILIADO | 2026-09-30 (10-Q) | 2026-09-30 | 241,605.0 | ✓ | ✓ | ✗ | 0 |
| MP | CONCILIADO ≤1 % | 2026-06-30 (10-Q) | 2026-06-30 | 305.4 | ✓ | ✓ | ✗ | 0 |
| MSFT | CONCILIADO | 2026-06-30 (10-K) | 2026-06-30 | 331,839.0 | ✓ | ✓ | ✓ | 0 |
| MU | CONCILIADO | 2026-09-03 (10-K) | 2026-09-03 | 133,188.0 | ✓ | ✓ | ✓ | 0 |
| NFLX | CONCILIADO | 2026-09-30 (10-Q) | 2026-09-30 | 49,734.6 | ✓ | ✓ | ✓ | 1: 2026-10-20 8-K |
| NKE | CONCILIADO | 2026-08-31 (10-Q) | 2026-08-31 | 45,891.0 | ✓ | ✓ | ✓ | 0 |
| NU | XBRL SIN EL ÚLTIMO INFORME | 2025-12-31 (20-F) | 2024-12-31 | 11,517.1 | ✓ | ✓ | — | 1: 2026-10-23 6-K |
| NVDA | CONCILIADO | 2026-07-26 (10-Q) | 2026-07-26 | 302,970.0 | ✓ | ✓ | ✓ | 0 |
| NVO | CONCILIADO (solo 20-F anual) | 2025-12-31 (20-F) | 2025-12-31 | 309,064.0 | ✗ | ✗ | — | 2: 2026-10-19 6-K, 2026-10-13 6-K |
| ONON | SIN XBRL | — | — | — | — | — | — | Sin ingresos en XBRL (20-F/6-K sin datos estructurados o tags no estándar). |
| P911 | SIN SEC | — | — | — | — | — | — | No figura en company_tickers.json de la SEC (no presenta ante la SEC como emisor de EE.UU. |
| PAGS | XBRL SIN EL ÚLTIMO INFORME | 2025-12-31 (20-F) | 2024-12-31 | 18,809.6 | ✗ | ✗ | — | 0 |
| PFE | CONCILIADO | 2026-06-28 (10-Q) | 2026-06-28 | 63,696.0 | ✓ | ✓ | ✗ | 0 |
| PLTR | CONCILIADO | 2026-06-30 (10-Q) | 2026-06-30 | 6,155.9 | ✓ | ✓ | — | 0 |
| PYPL | XBRL SIN EL ÚLTIMO INFORME | 2026-06-30 (10-Q) | 2026-03-31 | 33,734.0 | ✗ | ✗ | ✗ | 0 |
| SHAK | CONCILIADO | 2026-07-01 (10-Q) | 2026-07-01 | 1,552.3 | ✓ | ✗ | ✗ | 0 |
| UBER | CONCILIADO | 2026-06-30 (10-Q) | 2026-06-30 | 55,227.0 | ✓ | ✓ | ✓ | 0 |
| ZTS | CONCILIADO ≤1 % | 2026-06-30 (10-Q) | 2026-06-30 | 9,525.0 | ✓ | ✓ | ✓ | 2: 2026-10-13 8-K, 2026-10-08 8-K |

## Resumen

- CONCILIADO: 24
- XBRL SIN EL ÚLTIMO INFORME: 3
- CONCILIADO (solo 20-F anual): 2
- CONCILIADO ≤1 %: 2
- SIN XBRL: 1
- SIN SEC: 1

## Casos que requieren revisión a mano

- **PYPL:** la SEC tiene el 10-Q de 2T26 pero `companyfacts` solo trae hasta 1T26. El análisis usa **FY2025 (33.172 M)** como ingreso base y cita los resultados de 2T26 (8.682 M); conviene fijar la base en LTM a 2T26.
- **NU y PAGS:** el último 20-F con XBRL llega a 2024 en `companyfacts`; el registro usa cifras posteriores en dólares (NU) o convertidas (PAGS). No se pudo contrastar con la SEC.
- **AFYA y NVO:** solo hay datos estructurados del 20-F anual (2025); los trimestres de 2026 están en 6-K sin XBRL. El registro reproduce el ingreso FY2025, pero no se contrastó el trimestre más reciente.
- **ONON:** sin ingresos en XBRL. **P911 (Porsche AG):** no presenta ante la SEC; hay que contrastarla con su informe de Frankfurt.
- **ZTS y MP:** reproducen el LTM a ≤1 % (ZTS 9.517 frente a 9.525 M; MP 305 frente a 305,4 M), dentro de la materialidad de `REGLAS` §4B, pero no coinciden al decimal.
- **Empresas con 8-K/6-K posteriores a la fecha del registro:** revisar su contenido antes de publicar (columna final).
