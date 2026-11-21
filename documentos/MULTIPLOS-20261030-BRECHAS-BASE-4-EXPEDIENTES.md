# Sensibilidad de múltiplos — diagnóstico real del archivo activo (30-oct-2026)

**No confundir centros numéricos con matrices 5x5 verificadas.** Esta extracción lee exclusivamente el JSON publicado en el catálogo, sin simulaciones arbitrarias, sin modificación de resultados y sin nueva validación del motor.

## Inventario de contratos disponibles

| Expediente | Cobertura guardada | 5x5 económicas independientes | Estado |
|---|---|---:|---|
| META | matrices array 0 | 0 | FALTAN matrices de múltiplos |
| UBER | 7 centros Base verificables | 0 | Centros sin 5x5 completas |
| XP | 4 centros Base verificables | 0 | Centros sin 5x5 completas |
| NVDA | 28 matrices 5x5 | 0 | 28 matrices nativas (2 anclas × 2 familias × 7 métodos) |

## Centros por método en Base: US$/acción, valores presentes FY+3

| Método | UBER | META | NVDA JMR | XP |
|---|---:|---:|---:|---:|
| EV/EBITDA | 63.83 | N/D* | 296.84 | N/D |
| EV/FCFF | 36.07 | N/D* | 296.84 | N/D |
| P/E | 72.53 | N/D* | 295.00 | 13.74 |
| P/FCFE | 68.66 | N/D* | 276.29 | 13.11 |
| P/OCF | 67.45 | N/D* | 295.00 | N/D |
| P/V | 70.37 | N/D* | 295.00 | 12.16 |
| P/BV | 131.15 | N/D* | 295.00 | 12.33 |

\* **META:** el JSON sí contiene `descuentoMultiples.metodos` para siete métodos con FY+3 VP, pero `sensibilidadMultiples=[]`. Los valores presentes individuales de salida NO son la matriz de sensibilidad. Se debe preservar la distinción.

### Ejemplo de matriz nativa NVIDIA, EV/EBITDA, ancla JMR, familia tradicional

Eje horizontal: múltiplo (veces); vertical: EBITDA FY+3 en USD millones; celdas: precio por acción a valor presente. Fuente `sensibilidadMultiples.matrices`, no nueva simulación.

| EBITDA / múltiplo | 12.98 | 14.60 | 16.22 | 17.84 | 19.46 |
|---|---:|---:|---:|---:|---:|
| 483,483.93 | 191.91 | 215.23 | 238.55 | 261.86 | 285.18 |
| 543,919.42 | 215.23 | 241.46 | 267.69 | 293.92 | 320.15 |
| 604,354.92 | 238.55 | 267.69 | 296.84 | 325.98 | 355.12 |
| 664,790.41 | 261.86 | 293.92 | 325.98 | 358.04 | 390.10 |
| 725,225.90 | 285.18 | 320.15 | 355.12 | 390.10 | 425.07 |

Centro: US$296.84. Verificar antes de considerar validada la matriz económica: los dos ejes mezclan múltiplos y niveles de resultados, y cualquier valor observado debe ser una referencia sectorial fechada comparable.

## Brechas precisas para el cierre A-1.2

1. **UBER:** hay 7 centros de múltiplos FY+3 y `controlesOK=7`, pero 5x5 económicas independientes = **0**. Estimar trayectoria y dos anclas sin interpolar arbitrariamente.
2. **META:** no hay `sensibilidadMultiples` poblada; 7 métodos existentes requieren ancla y matriz nueva. Múltiplos son secundarios, peso 0; el DCF sigue principal.
3. **NVDA:** las 28 matrices se preservan y sirven de patrón técnico, pero el estudio es anterior a Método A-1.2; después de recalibrar fundamentos hay que regenerar las 28, no copiar precios antiguos a una nueva valoración.
4. **XP:** los centros P/E, P/FCFE, P/V y P/BV existentes tienen estado OK pero sin matriz completa. EV/EBITDA/EV/FCFF y P/OCF son N/D **económicamente justificados** para actividad de intermediación. El FCFE principal no se pondera con múltiplos.
5. Para cerrar el gate: vincular cada análisis a la revisión exacta y fuente, tener snapshot reproducible y comprobar centro 3×3 vs método FY+3, cambios de denom./WACC/Ke y no sustituir errores por `N/D` sin justificación.

**Estado:** nota cuantitativa para los cuatro expedientes pendientes, NO modificación de las fichas activas. 
