# CMG · A-1.2 R4 · FASE 4 — BLOQUEADA PARA PUBLICACIÓN

**Corte contable:** 30-sep-2026. **Fecha de prueba:** 5-nov-2026. **Estado real:** CANDIDATO_REVISADO; **no** EN_REVISION promovido, **no** publicado. Auditoría económica F5 no realizada.

## Arquitectura y pruebas

- Referencia Damodaran intacta: https://docs.google.com/spreadsheets/d/1XvRRB0OOOGfRDQh3gMwlQIPgZNvFHWfv4ST2FdTG7Po/edit
- Libro JMR + `Resultados DCF original`: https://docs.google.com/spreadsheets/d/1hSKPKEUsCtQdpZp30__zCDFCqpMifbco05LsNhG8dX0/edit#gid=2051105004
- Análisis ASC842 de arrendamientos (separado, **no trasladado** a DCF): https://docs.google.com/spreadsheets/d/1hSKPKEUsCtQdpZp30__zCDFCqpMifbco05LsNhG8dX0/edit#gid=2051105005
- Base: https://docs.google.com/spreadsheets/d/1KByj2JtvW3jGVb5oTYtaeR1_tmromC73X5sFehgbxWM/edit
- Conservador: https://docs.google.com/spreadsheets/d/1d0cu9YrImICHvUSbnzh6ZFa9uv6gOj6KMpL8ZHy9TWQ/edit
- Optimista: https://docs.google.com/spreadsheets/d/1hSsfIfUMnURRnUPRSZXvUI1YOkTvQ-zEuERboJsgBek/edit
- Disrupción: https://docs.google.com/spreadsheets/d/1PyRwScNLKpLIxXeeGO_xYztQPQRmIoTNnhiCg-joi7U/edit

Integridad idéntica al piloto DUOL (comparación A1:AA260 en 17 pestañas): 1.224 fórmulas frente a 1.231 de la fuente por **siete sustituciones autorizadas solo en `Input sheet`**; 76 notas y 62 validaciones sin cambio. Circularidad de `Option value` calculada mediante iteraciones 1.000 / umbral 1e-11, sin editar fórmulas. Cada historia reproduce su valor de registro (desviación absoluta menor de 1e-10 USD).

## Valores preliminares

| Historia | DCF Damodaran USD/acción |
| --- | ---: |
| Conservador | 14,6217706126 |
| Base | 24,9573584990 |
| Optimista | 35,8254913060 |
| Disrupción (fuera del promedio) | 4,6506034688 |

MOS del Base 35 % = **USD 16,2222830244**, precio de referencia del libro R4 **USD 35,20** (no cotización viva). Promedio condicionado B/C/O = USD 25,0904947291. Candidato auxiliar R4 Base USD 24,3102680626; brecha de motores no certificada. El primer resultado de prueba Base USD 25,20 cambió a 24,9574 al corregir la diferencia entre CAGR 1–5 y 2–5.

Drivers Base: crecimiento primer año 10,7379 %, CAGR años 2–5 9,55446 %, margen objetivo EBIT 18,5 %, S/C 1–5 1,5 y 6–10 1,4, ROIC terminal 14 %, crecimiento perpetuo 4 %, WACC aplicado en libro DCF 8,2484 % y terminal real 8,91 %.

## Bloqueo económico material: arrendamientos

Datos SEC Q3 2026 recogidos en JMR: obligación de arrendamientos corriente **USD 321,557 M**, no corriente **USD 5.277,474 M**, total **USD 5.599,031 M**; activo ROU **USD 4.928,149 M**. El DCF resta el pasivo lease como deuda y proyecta desde EBIT GAAP con gastos operativos de renta incluidos; **no está demostrado** un recast homogéneo y puede haber doble conteo. `Cost of capital worksheet` trata esos USD 5.599,031 M como deuda con cupón cero/madurez 14,1 y estima valor de mercado de USD 2.462,069 M: peso de deuda 5,24 % vs saldo reconocido 11,17 % del capital de mercado+lease.

La hoja de auditoría separada deriva **interés de leasing implícito proxy de USD 292,491 M** usando saldo medio y tasa 5,48 %; **no** es gasto de leasing reportado como tal. EBIT ajustado proxy USD 2.087,432 M vs EBIT GAAP 1.794,941 M. WACC indicativo con deuda ASC842 íntegra y costo deuda 6 % = **8,184 %** vs 8,248 % antes. **Estas cifras no se han aplicado al DCF**: antes son necesarios tratamiento homogéneo de ROU, EBIT, reinversión, ROIC, beta, Kd y terminal.

## Bloqueos técnicos / publicación

1. Revisar fuentes de recast ASC842 y coherencia FCFF/EV→equity; cuantificar impacto material en Base, escenarios y MOS y criterios de ROIC terminal 14 %.
2. Conciliar WACC del Excel, WACC de JMR y auxiliar (8,1708 % / 9,18 % terminal); las tasas no son intercambiables sin rehacer valoraciones.
3. Recalcular matrices DCF 5×5 y múltiplos/fuentes FY+1/2/3 para la revisión R4; no reutilizar matrices A3 como certificadas. Actualizar Nivel 1 y Nivel 2 con misma revisión y mismo precio/corte.
4. Ejecutar `controles_todas.sh`, `registro_revisiones.py --check`, comparaciones hoja↔JSON↔app y CI/preview/producción; **NO EJECUTADO** para esta revisión R4.

- **AISLAMIENTO=OK:** se mantuvo CMG A3 vigente (`CMG-20261028-A3`, Base USD 25,24649460); se construyó R4 por separado, sin sobrescribir fichas oficiales.
- F4: paso 1 y parte del 4 documentados; análisis/promoción y certificación restantes **no completados**. Publicación denegada por puertas económicas y técnicas conforme a reglas vigentes; usuario solicitó intentarla, no saltarlas.
