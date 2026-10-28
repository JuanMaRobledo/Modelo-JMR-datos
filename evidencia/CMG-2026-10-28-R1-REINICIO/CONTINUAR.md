# CMG · reinicio: avance técnico parcial

Revisión prevista: `CMG-2026-10-28-R1-REINICIO`. Registro de trabajo: 27-oct-2026. Rama: `ccr-e19723cb-q1m72p`.

**Estado: PENDIENTE. La auditoría económica está PENDIENTE. Este archivo no es un dictamen ni certificación.**

Hoja de trabajo: https://docs.google.com/spreadsheets/d/1SF3cYhIe01LazAiW4klGgYd6QrYG_uC-X-A8N5yYETc/edit

Se restauraron 1.062 fórmulas. Comparación posterior: 1.312 fórmulas de la maestra en los rangos de 12 pestañas, cero diferencias, excepto la exclusión expresa de Resumen de Valoración!C25. No es una certificación del libro completo. Se añadieron 22 fórmulas de FCF en Cash Flow Statement!B38:L39, donde la maestra no tenía fórmulas, con notas de definición.

Código: split 50:1 mediante dataclasses.replace, sin mutar AnnualSeries; carga de estados y refresco parcial conservan fórmulas existentes. Pruebas aisladas aprobadas. El refresco completo contra Sheets no se ha ejecutado.

Bloqueo de ejecución: gspread ya se instaló, pero no hay cuenta de servicio configurada. get_gspread_client() falla al resolver una ruta de credenciales vacía como '.'. El conector de Sheets sí funcionó para restauración y lectura de comprobación. El script unificacion_hojas.py citado en las reglas no está en esta rama (404).

No se ha aplicado el corte: el C25 aún es 27,98 y debe fijarse en 31,95 al continuar. No hay DCF Base oficial nuevo, historias, siete múltiplos, artículo, registro EN_REVISION ni prueba local de app completados. No se ejecutó audit_report.py ni se generó manifiesto de auditoría.

No hubo eliminaciones en esta sesión; no se consultaron valoraciones antiguas. La carpeta personal CMG de Drive se conserva. No se puede afirmar eliminación definitiva de los archivos retirados previamente: pueden permanecer en historial de Git, papelera de Drive y referencias de terceros.

Evidencia detallada y cambios anteriores de las celdas en `evidencia/CMG-2026-10-28-R1-REINICIO/restauracion-formulas-parcial.json`.
