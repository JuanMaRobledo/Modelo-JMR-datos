# META — diagnóstico de matrices de múltiplos, 31-oct-2026

**Estado confirmado:** no exportables todavía / NO APROBAR múltiplos. La hoja A-1.2 conserva 46 pestañas y el expediente candidato separado del catálogo. Este archivo no modifica fórmulas ni supuestos.

## Inspección directa del libro

1. **`Escenarios e historias!K5:K8`: cuatro valores `PENDIENTE`**, incluidos Base, Conservador, Disrupción y Optimista. El DCF calculado en `CALIBRACION_DCF_PROVISIONAL.json` es **independiente** y no habilita automáticamente `Valuation output`.
2. **`Múltiplos históricos!A4:J6`: sin observaciones**; aparece la cabecera solamente. El resumen no contiene mínimo válido, P25, mediana 5A, promedio 5A ni cantidad de cierres positivos. Se requieren cierres fiscales trazables.
3. **`Supuestos de los Múltiplos!A6:M10`:** cinco métodos EV/FCFF, P/OCF, P/E, P/FCFE, EV/EBITDA. Las columnas de múltiplos Base/Conservador/Optimista están vacías, los valores de mínimo/máximo figuran 0 como salida vacía, y `No (automático)` indica ausencia de overrides manuales.
4. **`Descuento de múltiplos`**, historia Base filas 20–25: método y peso relativo 0; valor futuro, valor presente FY+1/Y+2/Y+3 y consolidado no calculados. La tasa Ke del libro sí se calcula (`9,195%`), pero eso **no constituye una valoración relativa**.
5. **`Sensibilidad por múltiplo` filas 76–94:** encabezados de matrices Base EV/EBITDA y EV/FCFF, pero ejes numéricos visibles 0 y celdas `N/D`. El propio libro muestra control de centro `N/D`, no una cuadrícula monetaria con centros 5×5.
6. La regla A-1.2 exige matriz Base 5×5 **para los múltiplos aplicables**, con anclas independientes y distinción FY+3 versus valor presente. Los escenarios Conservador/Optimista/Disrupción no necesitan sus propias matrices de múltiplos, según regla vigente. La ausencia de observaciones no se resuelve trasladando la matriz DCF independiente.

## Secuencia mínima para recuperar el gate sin relajar requisitos

1. Cerrar conciliaciones de acciones diluidas/opciones/RSU, deuda/arrendamientos, participaciones no operativas a valor económico y control `Input sheet!B85`; sustentar impuesto/WACC.
2. Validar casos especiales, `Input sheet!B108`, luego habilitar los cuatro estados `K5:K8=LISTO` **por sus fórmulas**, no mediante escritura manual en las celdas calculadas.
3. Generar estados FY+1..FY+3 coherentes a partir del flujo oficial para EV/EBITDA, EV/FCFF, P/E, P/FCFE y P/OCF (N/A documentado cuando el denominador no sea económico). No reutilizar valor en libros como valor económico de inversiones.
4. Cargar mínimo/mediana de múltiplos de **cierres fiscales reales**, con fuentes y exclusiones; cotejar anclas independientes. Calcular precio futuro al FY+3, pasar a valor presente con Ke coherente y dividendos correctamente descontados, sin duplicación.
5. Generar cuadrículas Base 5×5 de cada método aplicable. Verificar celda (3,3) = VP FY+3 (tolerancia de redondeo), ejes con unidades claras, método no aplicable con razón.
6. Publicar en PR la evidencia por fila y cuadrícula, correr CI completo y QA visual antes de la publicación de la ficha. No promover borradores ni archivar revisiones anteriores hasta cierre.

**No realizado:** modificación de múltiplos oficiales, certificación de anclas, liberación de gates, auditoría económica o publicación de META.
