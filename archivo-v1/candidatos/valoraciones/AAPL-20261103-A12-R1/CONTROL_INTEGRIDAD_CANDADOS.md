# AAPL R1 · Evidencia de controles equivalentes de candados + integridad · 2026-11-03

**CANDIDATO_REVISADO · NO PUBLICADO · NO FUSIONADO.** Este archivo documenta verificaciones de solo lectura por conectores sobre la nueva hoja IA de 46 pestañas y la plantilla oficial IA, sin suplantar la ejecución de los scripts del motor.

## A. Candados vigentes: 15/15 listos (no 18)
- Fuente del contrato: [JMR-valuation/reference/candados_plantilla.json](https://github.com/JuanMaRobledo/JMR-valuation/blob/main/reference/candados_plantilla.json) y [scripts/candados.py](https://github.com/JuanMaRobledo/JMR-valuation/blob/main/scripts/candados.py). Desde 27-oct-2026 la maestra vigente registra **15**, excluidas las tres celdas Financials Multiples!M34:M36 retiradas del maestro.
- Se leyeron directamente en [hoja AAPL 46 pestañas](https://docs.google.com/spreadsheets/d/1dEycisHE5Ai34Z50ELOByAiZxub87dPG2TwOmYjS2tA/edit) y se aplicó el conjunto autorizado por script: LISTO, VALIDADO, CONCILIADO, NO APLICA.

| Pestaña | Celda | Valor observado |
|---|---|---|
| Input sheet | B81 | NO APLICA |
| Input sheet | B85 | VALIDADO |
| Input sheet | B92 | VALIDADO |
| Input sheet | B108 | VALIDADO |
| Input sheet | B109 | NO APLICA |
| Input sheet | B110 | NO APLICA |
| Input sheet | B111 | VALIDADO |
| Input sheet | B112 | NO APLICA |
| Input sheet | B113 | NO APLICA |
| Input sheet | B114 | NO APLICA |
| Cost of capital worksheet | B84 | VALIDADO |
| Escenarios e historias | K5 | LISTO |
| Escenarios e historias | K6 | LISTO |
| Escenarios e historias | K7 | LISTO |
| Escenarios e historias | K8 | LISTO |

**Resultado observable**: 15/15 estados cumplen el predicado de candados. **No** se ejecutó literalmente `python scripts/candados.py AAPL` con Google auth/registro oficial de hoja; faltan evidencia firmada de ejecución y `controles_todas.sh`.

## B. Comparación exhaustiva en rango de auditoría (46/46 pestañas)
- Origen plantilla IA: `1e-lbQmCkObfq74YLpWnMmIidmcdsJQ-6uN4oiHnNTEQ`; destino AAPL: `1dEycisHE5Ai34Z50ELOByAiZxub87dPG2TwOmYjS2tA`.
- Se compararon las **46 pestañas**, rangos **A1:CB400** en cada una, exactamente los límites de `scripts/diff_formulas_plantilla.py` (máximo 80 columnas y 400 filas). Se clasificó cada fórmula de plantilla según fórmula intacta, otra fórmula, número, texto, vacío.

| Categoría | Celdas |
|---|---:|
| Fórmulas originales de plantilla | **7.882** |
| Fórmulas idénticas | 7.744 |
| Fórmula → otra fórmula | **138** |
| Fórmula → número | **0** |
| Fórmula → texto | **0** |
| Fórmula → vacío | **0** |
| Pestañas añadidas / faltantes | 0 / 0 |

- **Los 138 cambios están todos y solo en `Financials Multiples`**. Cada cambio desplaza fuente histórica una columna para usar FY2024/25/26 en las columnas B/C/D del submodelo, en lugar de FY2023/24/25 que traía la plantilla al desplazar la ventana contable a FY2026. Las notas de las celdas documentan motivo y SEC. El programa oficial clasifica `fórmula→otra fórmula` como AVISO, no FALLA automática; se deben documentar regresiones de equivalencia aritmética.
- Una fórmula nueva en un lugar originalmente vacío (p.ej. `Múltiplos históricos`) no reemplaza fórmula preexistente, pero requiere auditoría editorial adicional.
- Prueba equivalente de lectura directa, **no se ejecutó literalmente** `python scripts/diff_formulas_plantilla.py --sheet-id ...`, ni se generó reporte JSON de ese script con auth oficial.

## C. Balance histórico independiente 11/11
- Para FY2016–FY2026 se releyeron `Balance Sheet!B16:L35` y se computaron cuatro diferencias **por columna**, todas cero USD millones: activos (row16) − pasivos (row29) − equity (row35); suma de pasivos corrientes [rows18:23] − total row24; suma LT [rows25:27] − total row28; row24+row28−row29.
- **44/44 identidades aritméticas =0** después de separar arrendamientos FY2021–2024 y reclasificar su valor dentro de otros pasivos. Es una prueba reproducible independiente de formulas del sheet; sin certificación contable de cada entrada SEC.

## D. Lo que sigue NO aprobado por esta evidencia
- La emisión de `controles_todas.sh` y la suite oficial completa incluye probabilidad, supuestos, consistencia entre repos, integridad de entradas y estados financieros, materialidad de salvedades. **NO EJECUTADA**.
- Interés financiero FY26 `2937M` es proxy no publicado como bruto; fiscalidad/discount rate, valoraciones de RSU/SBC y flujos normalizados de FCFE/FCFF/OCF requieren revisión económica independiente.
- F4 no tiene JSON activo ni comparación `hoja↔motor↔datos↔app`; no se verificó Vercel preview/producción. F5 independiente no realizada.
- Decisión metodológica: mantener el PR #241 como **draft**, sin fusionar ni publicar hasta pasar F4. Esta evidencia sí elimina la hipótesis de que hay **fórmulas originales borradas** o **candados de plantilla pendientes**.