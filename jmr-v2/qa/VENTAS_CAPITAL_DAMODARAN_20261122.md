# Ventas/capital según Damodaran · 22-nov-2026

Aplicación de la enmienda del contrato V2 «Ventas/capital e industria según Damodaran» (22-nov-2026). Revisión de IA (Claude), no auditoría ni aprobación.

## Qué hace Damodaran (fuentes primarias)

| Fuente | Práctica observada |
| --- | --- |
| `fcffsimpleginzu.xlsx` (plantilla maestra) | `B31 = K27` (promedio global de la industria) y `B32 = B31`; notas: «look at your company's current number» (I27) y el marginal (I28). |
| Amazon 2024 | 2,0× digitado (≈ marginal de entonces). |
| Apple 2024 | 5,0× digitado (actual 6,38×). |
| Google 2024 | 1,2× digitado (≈ actual; industria Advertising). |
| Microsoft 2024 | 3,0× digitado (actual 0,71×). |
| Meta 2024 | 1,5× digitado (marginal 1,30×). |
| NVIDIA 2023 y 2024 | `=M27` (mediana global). NVIDIA sep-2024 y ene-2025: 2,5× digitado. |
| Nike 2024 | `=I27` (número actual, 3,46×). |
| MercadoLibre 2026 | `=N27` (tercer cuartil global, 3,18×). |
| Clases (valspr24, sesión 11) | «the numbers that drive growth are … marginal sales to capital ratios». |

En todos sus libros los años 6–10 son iguales a los años 1–5 (`B32 = B31`).

## Revisiones nuevas (libro con anclas por fórmula en `JMR Escenarios` A33:G48)

| Empresa | Revisión | Ancla Base (ambos tramos) | S/C antes → después | Valor Base antes → después |
| --- | --- | --- | --- | --- |
| MSFT | MSFT-V2-LTM20260930-R6 | Empresa actual (I27) | 0,80×/1,20× → 0,59× | US$462,85 → US$433,35 |
| NVDA | NVDA-V2-FY26Q2FY27-R7 | Tercer cuartil global (N27) | 2,7×/2,2× → 1,64× | US$212,33 → US$206,00 |
| GOOGL | GOOGL-V2-LTM20260930-R2 | Empresa actual (I27) | 1,0×/1,2× → 0,90× | US$286,50 → US$278,74 |
| AMZN | AMZN-V2-LTM20260930-R2 | Empresa actual (I27) | 1,0×/1,6× → 1,05× | US$196,96 → US$190,27 |
| ONON | ONON-V2-LTM20260930-R2 | Empresa actual (I27) | 3,0× → 2,14× | CHF 72,77 → CHF 71,34 |
| EPAM | EPAM-V2-LTM20260930-R7 | Empresa actual (I27) | 2,2×/2,0× → 2,13× | US$197,32 → US$197,36 |

- Conservador y Optimista aplican un factor sobre el ancla que conserva la proporción de cada escenario frente al Base de la revisión anterior.
- MSFT R6 también corrige la industria a Software (System & Application) y usa beta bottom-up de EE. UU. (Single Business): WACC inicial 10,77 % → 10,74 %.
- EPAM R7 corrige la industria a Computer Services. Las dos venían con Food Processing, el valor por defecto de la plantilla.
- GOOGL conserva Software (Internet) en lugar de Software (Entertainment) de indname, con la razón documentada en el libro y el expediente.
- Paridad libro–motor: 0,0000 % en los tres escenarios de las seis empresas. Exportaciones .xlsx con SHA-256 en `scripts/v2_ventas_capital_20261122/xlsx_sha.json`.
- Libros de la revisión anterior: los de EPAM R6 y ONON R1 se restauraron a su estado original. Las revisiones nuevas son copias con su propio ID.
- Se actualizaron análisis (texto, tablas, sensibilidades, estrés y figuras `-rN`), justificaciones y PDF. Las pruebas de estrés que fijan su propio ventas/capital no cambian. Las demás se recalcularon con el Base nuevo.
- Estado declarado sin cambios. Todas siguen con P02 (falta auditoría independiente). Los manifiestos de cierre quedan pendientes de rehacer.

## Resto de la biblioteca

Según la enmienda, los libros existentes se adaptan en su próxima revisión. Correcciones de industria pendientes en los libros, que traen Food Processing por defecto:

| Empresa | Industria correcta |
| --- | --- |
| AAPL | Computers/Peripherals |
| CMG | Restaurant/Dining |
| ORCL | Software (System & Application) |
| UBER | Transportation |

Tabla de anclas y efecto en todas las empresas: `scripts/v2_ventas_capital_20261122/tabla_sc_damodaran.json`.
