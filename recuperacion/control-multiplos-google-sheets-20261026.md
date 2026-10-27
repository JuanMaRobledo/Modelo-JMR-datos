# JMR · Conciliación de siete múltiplos desde Google Sheets · 26-oct-2026

**Alcance:** verificación **solo lectura**, sin recalcular ni cambiar valores, fórmulas, supuestos, pesos, hojas, catálogo o dictámenes. Se compararon las **siete fórmulas de salida del escenario Base** de cada uno de los 16 archivos de `valoraciones/` contra esas mismas celdas en la **Maestra vigente** del registro `JMR-valuation/reference/plantillas.json` (maestra del 22-oct-2026). Se extrajeron `userEnteredValue.formulaValue` y `effectiveValue` directamente de Google Sheets.

**Celdas cotejadas (idénticas en las 16 hojas):** EV/EBITDA = `Descuento de múltiplos!J20`; EV/FCFF = `J21`; P/E = `J22`; P/FCFE = `J23`; P/OCF = `J24`; P/S (P/V) = `PV!E42`; P/BV = `PBV!E42`. Todos los métodos se comprueban aunque tengan peso cero.

| Empresa | Fórmulas iguales a maestra | Salidas numéricas | Diferencias vs JSON de valor presente Base |
|---|---:|---:|---|
| ADBE | 7/7 | 7/7 | No detectadas (>0,01) |
| BSX | 7/7 | 7/7 | No detectadas |
| CELH | 7/7 | 7/7 | **P/V y P/BV: hoja − JSON = −0,1777 por acción** |
| DUOL | 7/7 | 7/7 | **P/V y P/BV: hoja − JSON = −1,2109 por acción** |
| EPAM | 7/7 | 7/7 | No detectadas |
| META | 7/7 | 7/7 | No detectadas |
| MSFT | 7/7 | 7/7 | No detectadas |
| NFLX | 7/7 | 7/7 | No detectadas |
| NKE | 7/7 | 7/7 | No detectadas |
| NVDA | 7/7 | 7/7 | No detectadas |
| NVO | 7/7 | 7/7 | No detectadas |
| ONON | 7/7 | 7/7 | No detectadas |
| PYPL | 7/7 | 7/7 | No detectadas |
| SHAK | 7/7 | **5/7** | `EV/FCFF` y `P/FCFE` sin salida numérica; ambos tienen peso cero en el JSON. Verificar si la métrica es negativa/no aplicable, documentar salvedad o resolver la entrada. |
| UBER | 7/7 | 7/7 | No detectadas |
| XP | 7/7 | **0/7** | `Input sheet!A1` está vacío: las fórmulas tienen guarda de empresa vacía. El registro financiero FCFE conserva P/E, P/FCFE, P/S, P/BV procedentes de otro cálculo, pero **no están reproducidos en las celdas originales aquí verificadas**. Se requiere decidir el puente de modelo financiero sin inventar salidas ni activar una plantilla incompleta. |

**Total:** 112/112 fórmulas de salida equivalentes a la maestra; 103/112 resultados numéricos; 14 empresas con siete salidas numéricas; cuatro empresas con alguna revisión pendiente (DUOL, CELH, SHAK y XP).

## Cómo interpretar el control

- Se comparó `descuentoMultiples.metodos[].base.consolidado` (valor presente) del JSON contra la celda `J20:J24` / `E42`, **no** `metodos[].base`, que para algunas empresas expresa **FY+3 + dividendos** y por diseño difiere del valor presente. Confundir ambos daría falsos errores.
- La concordancia de siete fórmulas no prueba que todos los parámetros, columnas, fórmulas intermedias, historia Base, datos ni supuestos coincidan con la maestra. Para ello existe `JMR-valuation/scripts/audit_master_formulas.py` y el control de publicación integral.
- Ver fórmulas sin valor no equivale a calcular un múltiplo. **No publicar como 7/7** cuando no se obtienen siete precios numéricos, salvo excepciones N/A/N/D financieramente justificadas con evidencia, conforme a `Modelo-JMR/modelo/REGLAS_VIGENTES.md` §5A. Una ponderación cero no reemplaza la justificación.
- En **SHAK**, no escribir un cero en lugar del método faltante; estudiar primero el denominador económico y los supuestos. En **XP** no escribir simplemente el nombre en `Input sheet!A1` para forzar el cálculo: analizar el carácter financiero FCFE y la aplicabilidad del bloque de múltiplos.
- DUOL/CELH: conservar las hojas; inspeccionar si cambió alguna entrada o si el registro usó un ajuste adicional, documentar la causa y **recapturar solo los valores afectados** más el análisis/auditoría vinculados si hubo cambio económico. No crear otra valoración desde cero por este desajuste.

## Estado de publicación

Este reporte **NO** modifica `catalogo.json`, no certifica ninguno de los 16 estudios ni cambia el dictamen de auditoría publicado. La herramienta nueva `JMR-valuation/scripts/verificar_multiplos_hoja.py` ejecuta una puerta de fórmulas y valores directamente sobre Sheets; debe usarse en futuros cierres sin sustituir los controles anteriores.

**Siguiente paso operativo único:** resolver los cuatro casos señalados, empezando por DUOL y CELH como conciliaciones de un único precio relativo, luego SHAK (aplicabilidad) y XP (método financiero). Conservar todo el resto sin repetir auditorías ya aprobadas.
