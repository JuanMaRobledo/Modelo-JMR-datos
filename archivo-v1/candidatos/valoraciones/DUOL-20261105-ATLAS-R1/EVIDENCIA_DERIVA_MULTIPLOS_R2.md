# DUOL R2 — conciliación en vivo entre JSON publicado y hoja, 6-nov-2026

El repositorio main selecciona valoraciones/DUOL-20261103-A12-R2.json y su hoja 1_-Rxwq04iuXvS1FNpYuwlaAkGEeBxUsuyblIZAx_Oqc. Al leer Descuento de múltiplos!J20:J24 y comparar con metodos[].base del JSON:

| Método | VP Base JSON oficial US$/acción | VP Base Google Sheet actual US$/acción | Brecha actual |
|---|---:|---:|---:|
| EV/EBITDA | 99,173965 | 99,173965 | 0,00 |
| EV/FCFF | 75,708373 | 62,089972 | −13,618401 |
| P/E | 23,419287 | 23,419287 | 0,00 |
| P/FCFE | 12,443671 | −0,434356 | −12,878026 |
| P/OCF | 14,650143 | 4,284903 | −10,365241 |

**Conclusión:** tres de cinco valores de la fuente activa difieren hoy materialmente. Se desconoce si la hoja se recalculó después de la fotografía JSON o si la discrepancia existía originalmente. La prueba de hoy demuestra deriva actual, NO un dictamen retroactivo de que R2 fuera inválida en la fecha de publicación.

**Acciones antes de promover Atlas:** identificar fórmula/inputs que variaron en cada método de R2; no copiar cifras de R2/R4 al Atlas R1; trabajar con Financials Multiples, Descuento de múltiplos, Sensibilidad por múltiplo de la MISMA revisión final, extraer un JSON con checks. El libro Atlas todavía deja todos los precios relativos FY+3 como N/D y el bloque combinado 60/40 vacío.

- Hoja activa R2: https://docs.google.com/spreadsheets/d/1_-Rxwq04iuXvS1FNpYuwlaAkGEeBxUsuyblIZAx_Oqc/edit
- JSON activo R2: https://github.com/JuanMaRobledo/Modelo-JMR-datos/blob/main/valoraciones/DUOL-20261103-A12-R2.json
- Libro Atlas relativo: https://docs.google.com/spreadsheets/d/1K0yBSETJQkWjdAHRy6Os-3iQ5dmHW_bc88LTMXhUxYU/edit

**Estado:** HALLAZGO MATERIAL, no modificar R2 en este PR. NO_PUBLICAR.
