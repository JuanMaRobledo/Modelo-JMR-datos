# Davivienda · revisión Damodaran r2 (11-oct-2026)

Expedientes: `PFDAVVNDA.CL-pfdavvnda-20261009-jmr-r1.json` (Banco) y `PFDAVIGRP.CL-pfdavigrp-20261009-jmr-r3.json` (Group).
Hojas: [Banco](https://docs.google.com/spreadsheets/d/16smCZh7JIB3om_UabhiFymPElK6zyq_6Z8iY-P4Kgrs/edit) · [Group](https://docs.google.com/spreadsheets/d/1ogP8LfxEBxslOeC6Avgk2BAClJ_0cfzpgJ06icvVSys/edit).

## Resultado

| COP/acción | Antes | r2 | Precio 9-oct | Base/precio |
| --- | --- | --- | --- | --- |
| PFDAVVNDA Base | 17.387 | **19.474** | 31.460 | −38% |
| PFDAVVNDA esperado | 13.416 | 15.584 | | |
| PFDAVVNDA combinado 80/20 | 19.255 | 20.924 | | |
| PFDAVIGRP Base | 28.213 | **21.969** | 40.620 | −46% |
| PFDAVIGRP esperado | 25.238 | 19.662 | | |
| PFDAVIGRP combinado 80/20 | 28.431 | 21.884 | | |

## Cambios en las hojas

Banco (16smCZh…):
- `Datos!B26:C27`: precio 31.460, cierre BVC 9-oct-2026 (Yahoo Finance); antes 30.800 del 8-oct.
- `'Motor Operativo'!I6`: crecimiento de gastos Conservador 4,5% → 4%. ROE terminal Conservador 4,9% → 6,2%; valor 2.234 → 3.923.
- `'Ke sustentado'!C8`: rótulo ERP (4,20% = base julio; implícita oct 3,70% como sensibilidad).
- `'Cesión Davibank'!A31:C46`: puente Damodaran. Intercambio a valor justo (B31 = B32, VPN 0) + sinergias del Group 1,05 billones/año × 70% Banco × 50% realización × (1 − 35%) a perpetuidad desde 2028 con Ke terminal 18,92% y g 4% (VP 1,289 billones) − costos de integración 0,65 billones × 70% × (1 − 35%) (0,271 billones) = VPN 1,018 billones. Sensibilidad de sobreprecio 10% (−0,259 billones). Realización 25%/75%/0% en Conservadora/Optimista/Disrupción.
- `'Cesión Davibank'!B7:B11` alimentan el puente existente (B12 "PUENTE COMPLETO", B15 = 19.473,6).
- `'Cesión Davibank'!A48:C56`: lectura de minoría controlada y desliste (98,9% Group; canje 2025 a 1,39× libro; P/B 0,91×). No se pondera.
- `'Cesión Davibank'!A58:E65`: valor por historia con cesión y esperado 15.583,9.
- Textos: `Resumen!A1:A2`, `Supuestos!E7`, `'Valoración JMR'!A32,A37,A41,A57,A59` (`escritura_textos_hojas.py`).

Group (1ogP8L…):
- `'Entradas cierre'!B12:B13`: Rf COP 11,467% (`=0,13217-0,0174988122`) y ERP 4,20%, en lugar de Rf USD 5,07% + ERP 4,42%.
- `'Entradas cierre'!B19:B20`: Ke = Rf + β·ERP + CRP con β 0,70 → 1,0: 17,62% → 18,88%. Antes el terminal era 14,36% por conversión USD→COP con inflaciones supuestas, inconsistente con el inicial y con el Banco.
- Textos `'Valoración actual'!A1,A6`.

## Criterios

- Banco = equity-only (RE/FCFE con capital regulatorio); Ke con el mismo corte que SURA y Argos.
- Una adquisición a valor justo tiene VPN cero; solo sinergias y costos cuentan, con escepticismo sobre su realización.
- La cesión no se suma en el Group: es intragrupo y las sinergias están dentro del ROE terminal 14% (guía 14–16% 2028-29).
- La opción de OPA/desliste del controlante explica parte de la brecha con el precio, pero no se pondera sin oferta.

## Fuentes

- DAVIbank, información relevante 6-oct-2026: https://cdn.aglty.io/scotiabank-colombia/davibank/Info_Relevante_0610_DAVIbank.pdf
- Acciones & Valores, libro de resultados Davivienda Group 2T26 (sinergias, costos, CET1, desliste, canje 1,39×): https://www.accivalores.com/wp-content/uploads/Libro-de-resultados-Davivienda-Group-2T26-13.08.2026.pdf
- Banco Davivienda, presentación corporativa 1T26: https://ir.davivienda.com/wp-content/uploads/2026/05/Presentacion-Corporativa-Banco-Davivienda-1T26.pdf
- Precio: https://finance.yahoo.com/quote/PFDAVVNDA.CL/history/
- Damodaran, primas país julio 2026: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html

## Scripts

- `escritura_textos_hojas.py`: textos de las hojas.
- `build_davivienda_r2.py`: lee las hojas (valores sin formato) y escribe los expedientes, incluidos `valuationOutput` y `dcfFcffIntrinsicScenarios` que usa el visor. Idempotente.
- `gs.py`: cliente de Google Sheets (credencial en `GOOGLE_SERVICE_ACCOUNT_JSON_CONTENT`).
