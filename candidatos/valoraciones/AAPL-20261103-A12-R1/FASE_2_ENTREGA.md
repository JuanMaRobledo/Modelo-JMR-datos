> **ADENDA F2 03-nov-2026 — precios y leases resueltos.** Se rellenaron `Trailing Valuation!C3:L3` con diez cierres fiscales 2017–2026, ajustados solo por splits y documentados por fuente/fecha en cada nota: 38,53; 56,44; 54,71; 112,28; 146,92; 150,43; 171,21; 227,79; 255,46; 341,07 USD, respectivamente. La ausencia de precio FY2016 se mantiene N/D. En `Balance Sheet` se desglosaron leases reconocidos FY2021–24 y se restaron exactamente de pasivos corrientes/no corrientes residuales, sin doble conteo; totales permanecen. FY2021/22 leases current 1.528/1.663M y LT10.275/10.748M [SEC FY2022](https://d18rn0p25nwr6d.cloudfront.net/CIK-0000320193/2095e158-2009-40a8-985a-c821f0020341.html). FY2023/24 leases current1.575/1.632M y LT11.267/10.798M [SEC FY2024](https://www.sec.gov/Archives/edgar/data/320193/000032019324000123/aapl-20240928.htm). `Múltiplos históricos` ahora genera por fórmulas FY2026 EV/EBITDA29,1235× vs medianaFY2021–25 21,6555×; PE37,9849× vs27,9114×; P/OCF34,1600× vs24,0841×. EV/FCFF y P/FCFE históricos declarados N/D por no existir FCFF/FCFE normalizados conciliados, no se sustituyen por FCF GAAP. **La F2 sigue abierta a scripts oficiales y revisión SEC rubro a rubro**; los párrafos de abajo que digan 'precios faltan', 'leases FY2021–24 no están' o 'DCF aún no calculado' describen la foto ANTERIOR, reemplazada por esta adenda y `FASE_3_ENTREGA.md`.

# AAPL-20261103-A12-R1 · FASE_2 · CERRADA CON CONTROLES PENDIENTES

- Fecha: **3-nov-2026**. Modelo JMR A-1.2, FCFF, **CANDIDATO_HISTORICOS_COMPLETOS / NO PUBLICADO**.
- Hoja nueva 46 pestañas `sheet_id=1dEycisHE5Ai34Z50ELOByAiZxub87dPG2TwOmYjS2tA`, `AAA Finanzas/Análisis/AAPL`. **AISLAMIENTO=OK.**
- ChatGPT GPT-6 y conector de Sheets + informes SEC HTML, sin motor local GitHub Actions ni terminal con credenciales Sheets; esfuerzo de configuración no verificable.
- **PASOS: 6/6 examinados, 3/6 con evidencia parcial aprobatoria, 3/6 pendientes**. No certificar F2 hasta fuente por cada rubro y pruebas oficiales.

## Historia obtenida e introducida en fórmulas nativas

`Income Statement!B:L`, `Balance Sheet!B:L`, `Cash Flow Statement!B:L` cubren **2016–2026**: 10 FY históricos **2016–2025** y LTM coincidente con FY2026 en columna L por diseño del conversor. FY2026 10-K presentado 3-nov-2026; último precio de cierre de referencia 2-nov-2026.

**Fuentes primarias por bloques (períodos no extrapolados, USD millones)**:

- FY2016–17: [SEC Form 10-K FY2017](https://www.sec.gov/Archives/edgar/data/320193/000032019317000070/a10-k20179302017.htm), p39 operaciones, p41 balance, p43 efectivo.
- FY2018–20: [SEC Form 10-K FY2020](https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/aapl-20200926.htm), p31 resultados, p33 balance (FY19–20); FY18 BS desde [SEC Form 10-K FY2019](https://www.sec.gov/Archives/edgar/data/320193/000032019319000119/a10-k20199282019.htm) p31, p35 flujos.
- FY2021: [SEC Form 10-K FY2021](https://www.sec.gov/Archives/edgar/data/320193/000032019321000105/aapl-20210925.htm), p31 balance; flujos del 10-K FY2023.
- FY2022–23: [SEC Form 10-K FY2023](https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/aapl-20230930.htm), p28 resultado, p30 balance, p32 flujos.
- FY2024 BS: [SEC Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm), FY2024 como comparativo; FY2024 resultados y flujos en FY2026 10-K.
- FY2025–26 balance y FY2024–26 resultados/CF: [SEC Form 10-K FY2026](https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm), p32/p34/p36.

La fecha y documento oficial están en las **notas de cada celda**. A cada fila se le asignó la empresa AAPL; no se importó de otra ficha ni se alteró la fórmula de un ratio. No se completaron antiguas cifras históricas por suponer ceros: partidas no segregadas siguen vacías.

## Tabla base (US$ millones)

| Año | Ingresos | EBIT GAAP | CFO | CAPEX físico | D&A |
|---|---:|---:|---:|---:|---:|
| 2016 | 215.639 | 60.024 | 65.824 | 12.734 | 10.505 |
| 2017 | 229.234 | 61.344 | 63.598 | 12.451 | 10.157 |
| 2018 | 265.595 | 70.898 | 77.434 | 13.313 | 10.903 |
| 2019 | 260.174 | 63.930 | 69.391 | 10.495 | 12.547 |
| 2020 | 274.515 | 66.288 | 80.674 | 7.309 | 11.056 |
| 2021 | 365.817 | 108.949 | 104.038 | 11.085 | 11.284 |
| 2022 | 394.328 | 119.437 | 122.151 | 10.708 | 11.104 |
| 2023 | 383.285 | 114.301 | 110.543 | 10.959 | 11.519 |
| 2024 | 391.035 | 123.216 | 118.254 | 9.447 | 11.445 |
| 2025 | 416.161 | 133.050 | 111.482 | 12.715 | 11.698 |
| 2026 | 478.834 | 158.063 | 145.097 | 9.041 | 13.423 |

En `Cash Flow Statement!B:L`, CAPEX aparece con signo negativo y el FCF por fórmula `row36=CFO+Capex`; arriba se reporta CAPEX absoluto por legibilidad. I+D, SBC, basic/diluted weighted shares, gastos SG&A y balances documentados por filas. No usar FY2024/2025 ingresos de fecha previa como FY26 por error de columnas.

## Cotejos ejecutados contra cifras SEC

1. **11/11 balances anuales:** `Balance Sheet!row16 activos − row29 pasivos − row35 patrimonio = 0` para FY2016–2026. Ecuaciones independientes del conector, todos los años diferencia **USD 0 M**.
2. **11/11 CFO anuales:** el total oficial `Cash Flow Statement!row13` coincide con NI, D&A, SBC, otros y variaciones separadas o agregadas, diferencia **USD 0 M** (2016–26). Desgloses agregados explícitos fila6 y fila12, no ceros falsos.
3. **11/11 CFI anuales:** inversiones financieras compradas/vendidas, CAPEX, adquisiciones cuando desglosadas y otros reconciliados con `row22`, diferencia **USD 0 M**.
4. **11/11 CFF anuales:** `row34` coincide con net commercial paper, emisiones/pagos de bonos, recompra, dividendo, financiación y otros, **USD 0 M**.
5. **Ejercicios de cotejo independiente:** EBIT FY25/ventas = 133050/416161 = 31,9708%, FY26 = 158063/478834 = 33,00998%; margen bruto FY25 = (416161−220960)/416161 = 46,9052%, FY26 = (478834−245232)/478834 = 48,7856%, igual a las celdas de fórmula de la hoja.
6. `R& D converter` (3 años) con I+D FY23–26: activo79.255, amort31.945, ajuste EBIT13.820, DCF nativo aún no calculado.
7. `Input!B83:B87`: cartera negociable no corriente80.213M separada de caja+negociables corrientes56.722M, control nativo `B85=VALIDADO`. Este es un **control de no duplicidad puntual**, NO certifica liquidez neta total ni condiciones impositivas.

### Reclasificaciones registradas, no ocultas
- `Balance Sheet!row9` = inventarios + otros activos corrientes, pues el formato no tiene columna de inventario separada. `row7` = receivables de proveedores; `row20` = commercial paper + term debt corriente. Lo mismo para `row27` otros pasivos no corrientes.
- `Cash Flow Statement!row12` agrupa partidas SEC no representadas en el formato: vendor receivables, inventarios, otros activos y pasivos; conservando CFO exacto. `row6` agrupa otros ajustes no monetarios. `row18` combina vencimientos y ventas de bonos.
- **2017 y 2023 tuvieron 53 semanas** frente a 52 en otros ejercicios; no comparar CAGR ajustado por semana sin señalarlo.
- En **FY2020**, Apple adoptó ASC842 arrendamientos, registrando activos ROU7,5bn y pasivos8,1bn, sin restatement de 2019; no comparar capital/ROIC y deuda históricas antes/después sin ajuste. FY2026 pasivos por leasing14.368M están reconocidos. `Input!B18=No` significa **no capitalizar de nuevo**, NO ausencia de arrendamientos.
- FY2016/17 basic y diluted weighted shares retroajustados por split 4:1 de ago2020; FY2018–26 denominador en millones, no miles. `Input!B22` usa acciones **en circulación** FY26 (14.532,259M) y no weighted avg diluidas.

## Bloqueos y clasificación material

**Materiales:** opciones/RSU aún sin dilución/valor opción reconciliados, financiación al valor de mercado (bonos 64bn de FV vs libros78,1bn) y WACC Detailed; cambio fiscal e impuestos normalizados, capital económico/ROIC ajustado y series de precios split-ajustados por cierre FY, S/C marginal y lags; múltiplos FY+1/2/3 e industria. El caso no está READY para F3/F4 sin resolver drivers sensibles.

**Documentales/no resueltos:** BS FY2018–FY2024 no muestra todos los arrendamientos en partidas autónomas, `Balance Sheet!row21, row26` permanece sin cifra si no fue capturada nota de leases. NI/EBIT se representan con SEC GAAP, no se han normalizado cargos extraordinarios FY2024 ni impuestos territoriales. Tipo `NO DESGLOSADO` no reemplazado con cero.

**Controles oficiales NO EJECUTADOS:** `estados_completos.py`, `auditar_estados_sec.py`, `auditar_ceros_materiales.py`, `diff_formulas_plantilla.py`, audit de 18 candados, fuentes AAPL actuales vs plantilla limpia, pruebas de ratios ROIC/ROE/ROA/P/E/EV-EBITDA en dos períodos, historial de precios y cohortes. Solo se ejecutaron **pruebas equivalentes de sumas primarias** arriba.

## Drivers Base anterior → nuevo

No existe todavía DCF Base de salida nativa (Estado **N/D**). Se conserva exclusivamente el contraste externo de F1; F2 **no cambia** hipótesis ni precio por reflejo. `Fase3` deberá justificar `CAGR1-5: 7% candidato, margen term35,5%, S/C 1–5 1,80, S/C6–10 2,00, WACC candidato9,45%, g4%, ROIC terminal15%` **contra históricos y fuente Damodaran del corte, no contra precio**; no se han inyectado estos drivers al motor.

## Traspaso operativo a F3 y F4
1. Cotejar cohortes, mediana/p10–p90 de comparables, dividir productos/servicios, precio/unidades, reinversión y ROIC ajustados a 10 años; resolver ASC842 y FV inversiones/deuda, opciones/RSU.
2. Ejecutar hojas y scripts oficiales, incluidos costos capital nativos, fiscalidad, cinco múltiplos, DCF 4 historias y sensibilidad 3 matrices 5×5, 18 candados; registrar estado real.
3. Redactar Nivel 1 y 2 desde esta revisión (borrador ya existe), **publicar solo si** F4 tiene gates completos y verificable en app y CI. Auditoría F5 aparte tras revisión visual usuario.

**Conclusión:** captura económica ampliada y conciliaciones de sumas completadas **parcialmente**, sigue CANDIDATO; no hacer merge ni activar `catalogo.json` por simples sumas que cuadran.
