# Dictamen económico · Modelo JMR · 18-oct-2026

Este dictamen sigue a la comparación directa de 38 Google Sheets con sus JSON: 36 registran paridad de pesos, dos holdings tienen registros económicos incompletos. La paridad técnica no certifica la selección de los múltiplos. Los DCF Base y el MOS no se cambiaron.

## Once brechas VP3 superiores al 30% en valor absoluto

| Ticker | Brecha centro VP3 vs DCF Base | Ponderación existente (provisional) | Evidencia y prueba necesaria |
|---|---:|---|---|
| SHAK | +310,0% | DCF 60%, EV/EBITDA 20%, P/E 10%, P/OCF 10% | FCFF/FCFE no sostenibles; ROIC propio cercano a 5% frente a peers de 20–40%; revisar leases, ROIC y aperturas |
| PLTR | +152,0% | DCF 60% y cinco múltiplos 40% | FY+3 no debe utilizar el crecimiento inmediato de hipercrecimiento; revisar utilidad vs EBITDA, SBC y comparables rentables |
| CELH | +128,8% | DCF 40% y múltiplos 60% | Depurar cargos/pagos de distribución extraordinarios; historia normalizada corta y pares de bebidas con distinto ROIC |
| PFE | +87,1% | DCF 55% y múltiplos 45% | Falta expediente v3 de comparables; revisar expiración patentes, márgenes y flujo libre después de adquisiciones |
| MCD | +57,3% | DCF 40% y múltiplos 60% | P/BV N/D; expediente anterior DCF US$224,12 frente a US$159,94 vigente; reexaminar historia de franquicias |
| NVO | +52,6% | DCF 55% y múltiplos 45% | DCF anterior US$41,96 vs vigente US$33,17; actualizar precios, cuota, presión genéricos y pipeline |
| AAPL | +49,2% | DCF 40%, EV/EBITDA 30%, P/E 30% | EV/FCFF N/D; sin dictamen v3 específico, revisar recompras, servicios y normalización de FCFF |
| NVDA | +43,4% | DCF 60% y múltiplos 40% | DCF anterior US$259,29 vs vigente US$219,03; comprobar splits, memoria y márgenes IA |
| AMZN | +34,2% | DCF 40%, EV/EBITDA 30%, P/E 30% | Peers mezclan comercio/nube/publicidad; CapEx IA puede distorsionar EBITDA y FCFF |
| AFYA | −32,4% | DCF 40% y múltiplos 60% | Comparables brasileños con menores márgenes; dictamen histórico sin enlaces completos de fuentes |
| EPAM | −40,7% | DCF 40% y múltiplos 60% | DCF anterior US$168,22 vs vigente US$185,56; revisar riesgo IA estructural, crecimiento y márgenes |

**Decisión:** preservar ponderaciones actuales sin promoverlas a estado certificado. Los dictámenes antiguos comparan cortes y versiones DCF distintos, como se documenta en MCD, NVO, NVDA y EPAM. No rebajar ni elevar un múltiplo solo para aproximarlo al DCF; recalibrar el ancla exige datos de pares al corte, normalización de ROIC, margen y riesgo.

## Casos especiales

- **NFLX:** hoja vigente DCF 60%, múltiplos 40%; se corrigió en rama el JSON y análisis para sincronizarlos. DCF Base US$71,68, múltiplos Base VP US$87,60, mezcla secundaria US$78,05, objetivo FY+3 US$108,33. MOS 35% solo del DCF Base, umbral US$46,59. Sus comparables precisan certificación económica.
- **GRUPOARGOS y PFGRUPOARG:** DCF y SOTP por negocios inconclusos, 21 N/D por expediente. No aplicar el 40% DCF y 60% de relativos históricos como combinación válida. Completar participaciones, deuda corporativa, deuda de filiales y FCFF por negocio.
- **MP:** suma de pesos 80%. El 20% sin asignar no debe rellenarse artificialmente. Revisar FCFF, inversiones, opciones, P/V y P/BV antes de decidir DCF 100% u otra ponderación explícita.
- **META, MU, P911:** objetivos y pesos del Resumen sí coinciden con los métodos JSON, pero el apartado de descuento tiene estructura antigua. Migrar solo tras conciliación de los siete métodos, valor presente y comparables.

## Veinte expedientes sin brecha material

ADBE, ADSK, BSX, CMG, DPZ, DUOL, GOOG, GRUPOSURA, INTU, LULU, MSFT, NKE, NU, ONON, PAGS, PFDAVVNDA, PFGRUPSURA, PYPL, UBER, ZTS. Conservar sin republicar hasta que haya una corrección económica o editorial demostrable. Holdings financieras requieren SOTP y P/E secundario; un EV operativo consolidado no sustituye SOTP.

## Regla de publicación

La selección debe expresar método principal, secundario o no elegible por empresa, con régimen histórico y pares fechados, ajustes por ROIC, crecimiento, márgenes, reinversión, deuda, SBC y riesgo. Corroborar siete múltiplos × tres escenarios y explicar N/D sin inventar resultados. Disrupción es una historia separada; no participa en el promedio ordinario. El DCF Base es intrínseco principal y referencia exclusiva del MOS, aun cuando la mezcla secundaria tenga otro valor.

**Publicación autorizable tras esta revisión:** sincronización técnica NFLX, con salvedad explícita sobre la falta de certificación contemporánea de pares. **No autorizable aún:** recalibración financiera de las otras 37 sin evidencia adicional, en particular Grupo Argos, PF Grupo Argos y MP.

Fuentes de metodología: Damodaran, Investment Valuation y factores de los múltiplos (https://pages.stern.nyu.edu/~adamodar/pdfiles/uValue/uValuebook.pdf); tablas históricas sectoriales (https://pages.stern.nyu.edu/adamodar/New_Home_Page/datafile/data.html). Evidencia interna: dictámenes previos en JuanMaRobledo/JMR-valuation/reference/multiplos_v3 y lectura de hojas nativas 18-oct-2026.
