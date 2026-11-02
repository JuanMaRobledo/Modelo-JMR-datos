# Piloto TERPEL · Método JMR A-1.2 Colombia · Inicio 2026-11-01

**Estado:** FUENTES_EN_PREPARACION · NO PUBLICADO · NO EN_REVISION · NO AUDITADO.
**Identidad:** Organización Terpel S.A., acción ordinaria BVC:TERPEL, COP, empresa operativa no financiera.
**Propósito:** abrir expediente candidato independiente mientras NU se trabaja en otro flujo. No tocar `catalogo.json` ni modificar otra valoración.
**Método propuesto:** DCF FCFF (A-1.2) en COP nominal a 10 años, cuatro historias; múltiplos y MOS35. La app debe consumir la ficha única existente de siete pestañas, NO crear pantalla Colombia paralela.

## Evidencia primaria cotejada

Documento: EEFF **consolidados** de Organización Terpel S.A. y subordinadas, ejercicio 2025 y comparativo 2024 **re-presentado**, con opinión de revisor fiscal KPMG. Fuente original: https://www.terpel.com/var/site/storage/original/application/67cb56f49ddb0a24dbf5a602ca8166b5.pdf

- **Importante sobre unidades:** el PDF expresa las partidas en **M$ = miles de COP**. Aquí se convierten a **millones COP dividiendo por 1.000**, nunca copiando sin conversión a un modelo en millones.
- Ingresos 2025: 38.147.135,440 millones COP; 2024: 36.569.100,666 millones COP. Estado de resultados, pág. impresa 7.
- Resultado operacional 2025: 1.292.769,208 millones COP; 2024: 1.275.953,074 millones COP. Estado de resultados, pág. 7. No confundir con «resultado operacional antes de otros ingresos y gastos» (1.397.083,888 / 1.433.531,320).
- Resultado neto 2025: 628.522,922 millones COP; 2024: 530.785,143 millones COP. Estado de resultados, pág. 7.
- Flujo neto de operación 2025: 1.183.693,002 millones COP; 2024: 1.492.912,310 millones COP. Estado de flujos de efectivo **método directo**, pág. 11; no equiparar automáticamente CFO−CapEx con FCFF.
- Compra de propiedades, planta y equipo 2025: 278.857,277 millones COP; 2024: 321.878,232 millones COP (salidas de efectivo); intangibles 2025: 48.187,304; 2024: 45.828,079 millones COP, pág. 11. Evaluar mantenimiento/crecimiento y posibles desembolsos extraordinarios.
- Número de acciones ordinarias en circulación informado: **181.424.505**, considerando 14.574.961 readquiridas sobre 195.999.466 emitidas. Nota 29, pág. 91 (revalidar a fecha de corte bursátil).

### Fuente intermedia localizada, a cotejar con PDF original

- Portal oficial de Terpel con **resultados segundo trimestre 2026**: https://www.terpel.com/accionistas-e-inversionistas/resultados-y-comunicaciones/resultados-trimestrales
- Transcripción accesible del informe intermedio consolidado 30-jun-2026 y comparativo 30-jun-2025 (no usar como fuente primaria hasta cotejar contra PDF de emisor o SIMEV): https://financialfilings.com/filings/organizacion-terpel-sa/interim-quarterly-report/2026/56572613/
- Cifras **solo preextraídas, provisionales**, en millones COP tras dividir M$ por 1.000: ventas H1-2026 19.941.535,071 vs H1-2025 18.829.485,606; EBIT H1-2026 794.515,769 vs 631.982,735; utilidad del período 409.254,194 vs 326.473,895. **NO USAR EN DCF oficial** hasta validar original y ajustes.
- Históricos 2021–2023 existen como contraste externo, pendientes de cotejo con EEFF consolidados originales: https://stockanalysis.com/quote/bvc/TERPEL/financials/ . Este sitio muestra un EBIT 2025 diferente del reporte primario: **prevalece el informe auditado**.

## Contratos y bloqueos antes del cálculo

1. Recuperar EEFF consolidados originales 2021, 2022, 2023; 2024 comparable **re-presentado**. Tratar series separadas y consolidadas como perímetros distintos; nunca ensamblarlas silenciosamente.
2. Verificar 2026 H1 original y calcular LTM por **FY2025 + H1-2026 − H1-2025**, sólo sobre conceptos homogéneos y consistentes con reclasificaciones.
3. Completar CFO, D&A, deuda/arrendamientos, caja restringida, CapEx, capital de trabajo, impuestos, minoritarios, inversiones no operativas y exposición geográfica. Valorar si fuel-price pass-through distorsiona S/C y márgenes.
4. Fijar **precio BVC de cierre 30-oct-2026** con fuente verificable, liquidez/spread y acciones a esa fecha. No sustituirlo por precios del 23-oct u otro día.
5. Calibrar WACC **nominal COP** coherente con TES, ERP/riesgo país, tasas/deuda y moneda de flujos; no combinar tasa USD con flujos COP.
6. Crear **copia** de plantilla oficial en `AAA Finanzas/Análisis/TERPEL`; no cambiar la maestra; mantener motor JMR A-1.2, 4 historias, sensibilidad DCF, múltiplos aplicables e inverso. **La hoja calcula resultados**.
7. Solo después: extracción desde hoja → captura SHA/rangos → JSON de revisión → N1 14 capítulos + N2 12 apartados → validaciones → autorización de publicación `EN_REVISION`.
8. En app: reutilizar `expediente.html?ticker=TERPEL` con las 7 pestañas y filtro Colombia. Probar símbolos COP y no mostrar `US$` en las sensibilidades; móvil/escritorio. No publicar una ficha vacía.

**Estado de puertas:** no ejecutadas para TERPEL. **DCF Base/MOS:** aún no calculados. **Auditoría:** no realizada. **PR y despliegue:** solo preparación aislada, sin promoción.
