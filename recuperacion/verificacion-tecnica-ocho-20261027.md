# Verificación técnica de ocho recuperaciones — 27-oct-2026

**APROBADA en el alcance comprobado.** La ejecución real de `scripts/integridad_hojas.py` sobre Google Sheets terminó con **0 hallazgos** en ADBE, BSX, DUOL, MSFT, NVO, ONON y PYPL. Evidencia: https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/40534493438

La conciliación directa fue 8/8 valores DCF Base exactos, 32/32 historias idénticas, 36.559 celdas y 23.679 fórmulas inspeccionadas sin errores de celda en 13 pestañas clave de cada hoja. Se mantienen siete múltiplos por empresa (P/V y P/BV provisionales con peso cero).

ADBE y ONON: `precioAnalisis` coincide ahora con `precio` del corte 30-sep-2026 (239,94 y 29,61 USD); legado histórico preservado. NVO: ficha de crecimiento 6-10 conciliada con los valores que ya estaban en la hoja publicada; historial preservado. Sin modificar DCF ni supuestos efectivos.

La web pública respondió HTTP 200 y contenido actualizado: https://github.com/JuanMaRobledo/Modelo-JMR/actions/runs/40534288888. Se comprobaron seis renderizados de Chromium en escritorio/móvil: https://github.com/JuanMaRobledo/Modelo-JMR/actions/runs/40534898947. Se visualizó la pantalla de acceso; **no** se comprobó la aplicación después de autenticarse.

**Límites:** el control de integridad abarca 13 pestañas principales, no 61; no verifica exhaustivamente fuentes contables históricas ni pronostica la exactitud de supuestos. Las ocho continúan publicadas con salvedades, sin declarar validación integral de cada fuente documental.
