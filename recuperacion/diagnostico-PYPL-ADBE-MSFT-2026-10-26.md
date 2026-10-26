# Diagnóstico de recuperación JMR — 26-oct-2026

Este diagnóstico es una lectura puntual de Google Sheets. **No constituye un dictamen financiero ni modifica la hoja**. Las hojas actuales no deben confundirse con las copias del 21 de octubre ni con los JSON históricos del commit 44d546d6b88a7d84d8c24e029b3f03d501a50a55.

## Captura preliminar de hojas actuales

| Ticker | Hoja actual | DCF Base/acción US$ | MOS 35% US$ | DCF esperado de 3 historias US$ | DCF disrupción US$ | Observaciones |
|---|---|---:|---:|---:|---:|---|
| PYPL | https://docs.google.com/spreadsheets/d/1LI1LHXYFiCqg5i1_DDzs53Rd4eKv4zhDex2pxSvKuCs/edit | 105,13 | 68,34 | 102,73 | 47,98 | Hoja etiquetada 15-oct; los precios de mercado visibles se refieren al análisis de 30-sep |
| ADBE | https://docs.google.com/spreadsheets/d/1MhEO0NxlQ7ufHGQODjowcaCBDEyef4PxsC9ANLT2VBo/edit | 399,02 | 259,36 | 385,65 | 167,70 | Título dice ROIC terminal 25%, pero `Escenarios e historias!G5` presenta 29,3%; esclarecer fuente/selector antes de auditar |
| MSFT | https://docs.google.com/spreadsheets/d/1wIgB2zfjmPk_DdnaFsoJfKHMiIR_p4795ebvbGSOi1E/edit | 440,73 | 286,48 | 440,09 | 122,84 | Revisión actual difiere de cifras históricas anteriores; no reutilizarlas como si fueran mismo corte |

Fuentes de las cifras: `Escenarios e historias!H5:H14`, `Valuation output!B35`, `Resumen de Valoración!A1:H47` de cada libro en Google Sheets. Los DCF son de las hojas, no verificación matemática externa de reejecución. Los redondeos se leen como se presentan en cada libro.

## Hallazgos de reconciliación

1. **Los tres libros** muestran `Resumen de Valoración!A2` = `2026-09-30`, aunque los ficheros tuvieron modificaciones el 26-oct. Se debe separar fecha de corte económico, período financiero y fecha de edición antes de publicar.
2. **Los tres libros** conservan marcadores de plantilla en `Tesis de Inversión y Supuestos!A1` (`[TICKER]` / `[Nombre completo de la empresa]`), `A2` (`[$XX,XX]`) y texto ilustrativo en fila 28 (`[XX]%...`). Esa pestaña editorial **no está terminada**. Esto no demuestra que falten necesariamente secciones en los artículos de la app, que requieren revisión independiente.
3. **ADBE**: `Escenarios e historias!G5` obtiene ROIC dinámicamente de `Input sheet!B35/B66/B69/B47` según selectores; la cifra visible es 29,3%, mientras que el **nombre del archivo** afirma 25%. Puede ser un título desactualizado, no se ha demostrado un error de fórmula. Confirmar inputs y fuentes aprobadas antes de tocar el cálculo.
4. `Cost of capital worksheet!B84` en las tres muestra `VALIDADO`, política `Detailed — Damodaran` y `Input sheet!B81/B85/B92` muestran controles satisfactorios. **Son autocomprobaciones de la hoja** y no reemplazan una auditoría económica independiente, especialmente I+D, leases, opciones, reinversión y WACC.
5. El DCF es el valor intrínseco **principal**; los precios objetivo FY+3 y el ponderado relativo de `Resumen de Valoración` son métricas diferentes y no deben copiarse en el campo de DCF ni en el MOS.
6. Las historias Conservadora/Base/Optimista se ponderan por su probabilidad condicionada y Disrupción se expone separadamente; las celdas de escenario muestran referencias de fórmula a los correspondientes `Valuation output`.

## Próximo paso de trabajo, sin alterar aprobaciones

- PYPL: confrontar hoja actual, investigación completa y auditoría previas con diferencias en DCF; contrastar 7 múltiplos y materialidad de opciones/activos no operativos.
- ADBE: resolver discrepancia nominal ROIC 25% vs ROIC calculado 29,3%, fijar revisión/corte, revisar reinversión/ventas-capital y volver a conciliar análisis y auditoría.
- MSFT: comprobar por qué cambió su DCF respecto al estudio anterior, especialmente inversión en IA/capex, margen EBIT, ventas/capital y WACC.
- Emitir valoración, análisis de 18 secciones y auditoría económica independiente de 18 secciones *por la misma revisión* después de verificaciones independientes y controles. No publicar como certificado hasta entonces.

No se modificó ninguna hoja, documento histórico, catálogo ni app al generar este diagnóstico.
