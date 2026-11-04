# KO · KO-20261103-A12-R1 · F4 (cierre de controles) · CERRADA CON CONTROLES PENDIENTES
Fecha 04-nov-2026 · método A-1.2 · AISLAMIENTO=OK · corte 03-nov-2026 · hoja `17bX2bK0z1LSxO02GGv7HDFpAU6f8hkxIH4rUMdfnyEE` · constructor Claude Code (Sonnet 5.5; esfuerzo no expuesto) · no es F5: **no se emite dictamen independiente**.
Alcance (decisión del usuario): completar la R1 existente sin rehacer cifras. DCF Base US$59,49298288, MOS US$38,67043887, Conservador 40,20535617, Optimista 71,71935197 y Disrupción 30,86592400: **sin cambio** (comprobado en la hoja antes y después de cada escritura).

## Hecho y comprobado
| Control | Resultado antes → después | Evidencia |
|---|---|---|
| `auditar_ceros_materiales.py` | 8 alertas (D&A e I+D, columnas I:L, vacías sin nota) → **0**. Se clasificaron con notas de celda con fuente: D&A no desglosada en el estado de resultados (gastos por función), importe en el flujo de caja del 10-K FY2025 (accession 0001628280-26-010047): FY2023 USD 1.128 M, FY2024 1.075 M, FY2025 1.050 M; 9M-2026 USD 783 M (10-Q 2-oct-2026, 0001628280-26-067844). I+D: KO no la presenta como línea ni la etiqueta en XBRL; `Input sheet!B17` = No. No se escribió ningún valor. | `evidencia_cierre_20261104/auditar_ceros_materiales_KO.json` |
| `inputs_completos.py` | 1 entrada esencial vacía (`Input sheet!B101`, política de reinversión negativa de Optimista) → **0**. Se fijó «Sin liberación», igual que las otras tres historias; la fórmula de control pasa de «SIN REDUCCIÓN DETECTADA» a «CAP 0 si reinversión negativa» y el DCF Optimista no cambia (71,71935197). | hoja `Input sheet!B101:D101` |
| `auditar_estados_sec.py` (SEC XBRL) | **0 diferencias, 0 cambios propuestos** frente a las filas con etiqueta XBRL equivalente. | `auditar_estados_sec_KO_diagnostico.json` |
| `diff_formulas_plantilla.py` | 10 fórmulas reemplazadas por número (`Entradas históricas auxiliares!B2:K2`, encabezados de período) y 1 por texto (`L2`) → restauradas a `='Income Statement'!B2…L2` (mismos valores). Ahora **0 reemplazos no declarados**. Quedan 2 avisos: 8 fórmulas reescritas en `POCF` y 8 en `PFCFE` (F2 documentó la corrección del POCF histórico a CFO SEC; la de PFCFE no tiene nota en F2 y debe confirmarse). | `diff_formulas_plantilla_KO.txt/.json` |
| `candados.py`, `integridad_hojas.py` | 15/15 candados; 0 hallazgos de integridad. | corrida del 04-nov |
| DCF por FCFE (REGLAS v28/v29) | Pestaña `DCF FCFE` añadida a la hoja (0 diferencias de fórmula con la maestra); `dcfFCFE` en registro y análisis (FCFE Base US$59,64 frente a FCFF 59,49; informativo, sin MOS). | PR #247 |

## Controles NO cerrados (pendientes, con motivo)
1. **`estados_completos.py`: 9 hallazgos, PARCIAL.** Filas vacías en G:L: `Income Statement` D&A e I+D (ya documentadas por nota; la herramienta no lee notas); `Balance Sheet` Unearned Revenue, Other Current Liabilities, Total Long-Term Liabilities y Total Liabilities (KO no presenta ni etiqueta en XBRL `Liabilities` ni `LiabilitiesNoncurrent`); `Cash Flow Statement` Changes in Trade Receivables y Other Financing Activities (**sí están en XBRL** y faltan: p. ej. otras financiaciones 2021–2025 −353, −1.095, −465, −31, −279 USD M; no cargadas porque el signo de la plantilla y el LTM exigen cotejo con el estado de flujos del 10-K/10-Q) y Net Issuance of Long-Term Debt (G, L). Los indicadores derivados no tienen errores; solo `Quick Ratio` queda parcialmente vacío. **Tarea:** cargar esas dos filas del flujo con fuente y clasificar las cuatro del balance con nota («no presentada por la empresa»), y volver a correr el control.
2. **`controles_supuestos.py`: NO EJECUTADO.** Requiere `reference/damodaran/KO.json` del flujo anterior, que no existe para una revisión A-1.2.
3. **Perímetro CCBA/Asia, participaciones y contingencia fiscal (IRS):** sin revisión adicional; siguen las aproximaciones explícitas de la entrega F4 original.
4. **Cotejo SEC de notas y subpartidas:** no se amplió más allá de `auditar_estados_sec.py` (filas con etiqueta XBRL) ni del cotejo de 297 comprobaciones de F4.
5. **Verificación visual de la ficha en producción:** NO EJECUTADA (producción exige sesión; sin credenciales). En la app local con los datos de `main` la ficha carga, muestra el DCF por FCFE y su ponderación 50 % / 50 % y no desborda en móvil.
6. **Aviso `PFCFE`:** confirmar la reescritura de 8 fórmulas.

Estado: la R1 sigue `EN_REVISION`; no se marca AUDITADO. Insumos para la siguiente: tareas 1, 2 y 6; F5 en otra sesión/modelo.
