# Auditoría de paridad 38 hojas nativas frente a JSON — 18-oct-2026

Fuente directa: hojas Google vinculadas por `hojaGoogle` en cada expediente de `Modelo-JMR-datos/valoraciones`; se confirmó la metadata y la pestaña real `Resumen de Valoración` antes de leer `A5:E14` mediante el conector Google Sheets. Se cotejó el peso de los 6 métodos estándar del Resumen (DCF, EV/EBITDA, EV/FCFF, P/E, P/FCFE y P/OCF) contra `metodos` en cada JSON. Se comparó `Precio Objetivo Ponderado` Base de la hoja con `objetivoPonderado.base` de los JSON cuando ambos eran numéricos. Para NFLX se comparó con el JSON actualizado de la **rama del PR**, no con `main`.

**Resultado:** 38 hojas inspeccionadas, 36 con todos los pesos estándar coincidentes y 2 holdings con registros económicos incompletos. El objetivo Base FY+3 coincide en los 34 casos numéricamente verificables. En cuatro casos no se dispone de ambas cifras numéricas para establecer paridad. **La lectura correcta del MOS no se infiere de la columna "MOS vs precio actual" del resumen**, pues ese es un indicador secundario sobre el objetivo combinado: el umbral de compra JMR debe continuar usando `DCF Base × (1 − MOS)`.

| Empresa | Pesos hoja ↔ registro | Objetivo Base FY+3 | Estado |
|---|---|---|---|
| AAPL | 6 pesos coincidentes | Coincide | Mantener |
| ADBE | 6 pesos coincidentes | Coincide | Mantener |
| ADSK | 6 pesos coincidentes | Coincide | Mantener |
| AFYA | 6 pesos coincidentes | Coincide | Mantener |
| AMZN | 6 pesos coincidentes | Coincide | Mantener |
| BSX | 6 pesos coincidentes | Coincide | Mantener |
| CELH | 6 pesos coincidentes | Coincide | Mantener |
| CMG | 6 pesos coincidentes | Coincide | Mantener |
| DPZ | 6 pesos coincidentes | Coincide | Mantener |
| DUOL | 6 pesos coincidentes | Coincide | Mantener |
| EPAM | 6 pesos coincidentes | Coincide | Mantener |
| GOOG | 6 pesos coincidentes | Coincide | Mantener |
| GRUPOARGOS | Incompleto / 6 pesos sin registro comparable | No comparable numéricamente | Completar SOTP y retiro de ponderaciones inoperantes |
| GRUPOSURA | 6 pesos coincidentes | Coincide | Mantener |
| INTU | 6 pesos coincidentes | No comparable numéricamente | Inspeccionar objetivo no numérico de la hoja |
| LULU | 6 pesos coincidentes | Coincide | Mantener |
| MCD | 6 pesos coincidentes | Coincide | Mantener |
| META | 6 pesos coincidentes | Coincide | Mantener |
| MP | 6 pesos coincidentes | No comparable numéricamente | Solo 80% asignado; no renormalizar |
| MSFT | 6 pesos coincidentes | Coincide | Mantener |
| MU | 6 pesos coincidentes | Coincide | Mantener |
| NFLX | 6 pesos coincidentes | Coincide | Conciliado 60/40 en este PR |
| NKE | 6 pesos coincidentes | Coincide | Mantener |
| NU | 6 pesos coincidentes | Coincide | Mantener |
| NVDA | 6 pesos coincidentes | Coincide | Mantener |
| NVO | 6 pesos coincidentes | Coincide | Mantener |
| ONON | 6 pesos coincidentes | Coincide | Mantener |
| P911 | 6 pesos coincidentes | Coincide | Mantener |
| PAGS | 6 pesos coincidentes | Coincide | Mantener |
| PFDAVVNDA | 6 pesos coincidentes | Coincide | Mantener |
| PFE | 6 pesos coincidentes | Coincide | Mantener |
| PFGRUPOARG | Incompleto / 6 pesos sin registro comparable | No comparable numéricamente | Completar SOTP y retiro de ponderaciones inoperantes |
| PFGRUPSURA | 6 pesos coincidentes | Coincide | Mantener |
| PLTR | 6 pesos coincidentes | Coincide | Mantener |
| PYPL | 6 pesos coincidentes | Coincide | Mantener |
| SHAK | 6 pesos coincidentes | Coincide | Mantener |
| UBER | 6 pesos coincidentes | Coincide | Mantener |
| ZTS | 6 pesos coincidentes | Coincide | Mantener |

### Observaciones críticas

- **NFLX:** la hoja vigente 18-oct-2026 utiliza DCF 60%, EV/EBITDA 10%, EV/FCFF 15%, P/E 5%, P/FCFE 10%, P/OCF 0%. El JSON en `main` estaba desfasado: DCF 100% y múltiplos 0%, aunque el HTML exportado de la hoja ya mostraba la distribución 60/40. Esta rama sincroniza estructura y análisis. DCF Base US$71,683834; múltiplos Base VP US$87,604512; mezcla Base VP US$78,052105; objetivo a tres años US$108,327049. MOS 35% × DCF Base → umbral US$46,594492. Quedan cinco matrices N/D y 16 conciliadas; la selección económica de pares sigue pendiente.
- **GRUPOARGOS / PFGRUPOARG:** las hojas conservan ponderaciones indicativas 40% DCF, 30% EV/EBITDA y 30% P/E, pero las fórmulas no producen un valor DCF certificado. Los JSON retiran DCF por falta de cierre, y los selectores históricos muestran 60% de múltiplos inoperantes. No ejecutar publicación financiera; completar SOTP por negocio, deuda neta, participaciones y reconciliaciones contables.
- **MP:** pesos de hoja suman 80%, igual que el registro; no se asignó el 20% restante. Sin datos económicos nuevos no se debe asumir el 20% ni renormalizar sin autorización económica.
- **INTU:** pesos estándar coinciden; el objetivo Base no es numérico en la lectura usada y no se puede afirmar paridad de objetivo.
- **META, MU y P911:** `descuentoMultiples` conserva estructura más corta o sin campo `pesoDcf`, pero la fila ponderada del resumen coincide con el arreglo `metodos`; no confundir ausencia de ese campo con un error de pesos.
- **Métodos P/V y P/BV:** no figuran entre los seis métodos del Resumen tradicional, pero sí constan como anexos de siete múltiplos; validar anclas y sensibilidad por separado.

### Criterio de certificación

Esta es una **verificación de paridad técnica**, no una auditoría completa de la calidad de ganancias, comparables, impuestos, ventajas competitivas, reinversión o magnitud económica de los múltiplos. En particular, **paridad de pesos no demuestra que estén bien seleccionados**. Las decisiones económicas deben quedar por ticker con pares fechados y excluidos justificados. No modificar DCF Base ni MOS para conciliar una discrepancia de valoración relativa.

Lecturas directas verificadas: 38/38. Coincidencia de pesos: 36/38. Paridad Base FY+3 numéricamente comprobable: 34/38.
