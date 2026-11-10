# UBER-REBOOT-3T26-R1 · R5 — investigación creada, integración pendiente
**Fecha:** 2026-11-10. **Agente:** GPT-6, ChatGPT. **Estado:** CANDIDATO — NO PUBLICAR; R6 auditoría independiente NO_EJECUTADA. **PASOS R5: 1/4** (A creada; JSON, validadores y publicación pendientes).

## Evidencia del sexto documento
Documento nativo Google Docs creado **en la misma carpeta UBER de Drive**, sin usar como insumo ni copiar el análisis Floyd anterior:
- A: https://docs.google.com/document/d/1O7sHw19zYtntbAaDWErrmkhUX8pN4RdPtBFqLfN6MMA/edit
- 14 capítulos narrativos de Nivel 1 y 12 apartados cuantitativos de Nivel 2, títulos Google Docs para navegación, históricos, puente GAAP→económico, beta aprobada, escenarios, 10 años de DCF por historia, puente hasta acción, múltiplos FY+1/2/3 y VP, DCF inverso y sensibilidad.
- Cinco libros operativos: H `176tcVAz_RzHluf4kyjEEsMjDcDosldPdB5FBifO9YQA`, D-B `14QlydMFli2pxdG4agUYOAXL8QIE99P-3UDE7vwK8CaM`, D-C `1TUDP8WvRpjtm5AbCpGkKkfyAlItRuufIAAEkFp95aHA`, D-O `1f7Fzs7TBezRNa4E0lwHoh8fcPXTGn0d09HTatCaDLRU`, M `19fe8FcQ32d3yf169i-XA7F-c4IGhWTCNl_QO4WgCwA4`.

## Reconciliación económica sin nuevo ajuste
Beta apalancada usuario **1,20** en los tres libros; ERP geográfica 4,6896%; Ke 10,4875%; WACC inicial 9,9997%; estable 8,247%; g 4%.
DCF (Cons/Base/Opt) **45,29115176 / 98,73828566 / 149,66887071 USD/acción**. Esperado (25/50/25) **98,10914844**. MOS 35% Base **64,17988568** frente a precio fechado **68,59 (2026-11-06)**; no alcanza MOS35%.
Múltiplos totales combinados (Cons/Base/Opt) 49,27756 / 94,44358 / 136,81749; EV/FCFF **N/D** con peso 0 por ancla insuficiente, no sustituir con cero.
**Matrices DCF**: A crecimiento×margen, B WACC×g, C ROIC terminal×g; 25 corridas cada una = 75. Centros **98,7382856555** y controles de diferencia 0 contra DCF Base. Matriz C en D-B `Sensibilidades DCF!A35:F42`, rangos ROIC9%–17%, g3%–4,8%, extremos **81,4284–119,5899**. Entradas restauradas `Input sheet!B49=0.1323` y `B68=0.04`.
Matriz 5×5 por múltiplo activo EV/EBITDA, PE, PFCFE, POCF: controles centrales FY+3 = OK, no equivalen a VP3; anclas históricas y ajuste CFO residual siguen bajo reserva.
**Motor**: cotejo por exportación XLSX de plantillas y DCF: 1.225 fórmulas del motor iguales en cada copia más 5 sustituciones deliberadas en entradas de `Input sheet` (B27/B28/B29/B32/B62); 76 notas originales iguales por copia, cero diferencias de contenido/dirección. No se editaron las 17 hojas originales salvo entradas.
**SEC/IR**: se contrastó el 10-Q 3T26, 10-K FY2025 y resultados de 4-nov-2026: ingresos 9M2026 42.160 USDm, caja septiembre 9.558 USDm, inversiones CP 510, viajes 3T2026 4.061 millones, Gross Bookings 59.819 USDm. Ver el análisis A para URLs primarias y límites.
**Fuente de datos vs juicio:** históricos SEC; R&D capitalizada 3 años, beta1.20, márgenes18% Base, ventas/capital2,8→2,5, ROIC terminal13,23%, costo deuda6,10% son elecciones analíticas. Ninguna de estas decisiones constituye un hecho auditado.

## Comp puerta R5
| Control | Resultado |
|---|---|
| Sexto documento A creado con índice 14+12 y magnitudes de revisión | **HECHO**, requiere revisión visual/económica de contenido |
| H / tres D / M y matemáticas R3–R4 | **APROBADO** técnicamente, con salvedades descritas |
| Anclas históricas de los cuatro múltiplos y ajuste CFO residual | **PARCIAL**, R4 pendiente de dictamen |
| Fuente primaria por toda línea y valor económico participadas/caja/minoritarios | **PARCIAL** |
| `M!Supuestos y control!B63` AUDITADO | **NO** (permanece PENDIENTE) |
| `M!Supuestos y control!B64` estado para publicar | **NO PUBLICAR** |
| JSON revisión par (valoración/análisis) y validadores, catálogo, app | **NO_EJECUTADO** |
| Integración de PR app #193, motor #215, datos #263 | **NO_EJECUTADO** |
| Auditoría externa R6 | **NO_EJECUTADO** |

## Siguiente paso exacto
Completar fuentes y anclas económicas de M (EV/FCFF justificar N/D o cuantificar con serie normalizada; CFO residual, minoritarios y reservas, fiscalidad, deuda y acciones), registrar si hay salvedades materiales; crear par JSON en branch sin modificar catálogo principal, ejecutar validadores y prueba del contrato Reboot de PR #193/#215/#263; solo entonces publicar EN_REVISION si puerta completa. R6 debe quedar en otra sesión/agente.
