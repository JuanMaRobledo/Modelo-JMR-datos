# DUOL · A-1.2 R4 · FASE 4 — BLOQUEADA PARA PUBLICACIÓN

**Corte de datos:** 30-sep-2026 (Q3 reportado en nov-2026). **Fecha de prueba:** 5-nov-2026. **Estado real:** CANDIDATO_REVISADO, **no** EN_REVISION promovido, **no** publicado. **F5:** no ejecutada, auditoría económica independiente no realizada.

## Arquitectura bajo prueba

- Referencia nativa Damodaran **intacta** (importación del Excel `fcffsimpleginzu (2).xlsx`): https://docs.google.com/spreadsheets/d/1XvRRB0OOOGfRDQh3gMwlQIPgZNvFHWfv4ST2FdTG7Po/edit
- Libro JMR de datos, escenarios y registro de puente: https://docs.google.com/spreadsheets/d/117ZIeaI1NKcSK38XcWtqVwo7JD8qpt6QkDuC3VhOuvY/edit#gid=2051105004
- Base DCF: https://docs.google.com/spreadsheets/d/1Sa7Wplbj-Ef44YinF6XAZnOAMPEoiz9HtSiDLc7x7DM/edit
- Conservador DCF: https://docs.google.com/spreadsheets/d/19mLP96BJqSJDvfdaSfkBod0rMxa37NIwunWRToTdV2w/edit
- Optimista DCF: https://docs.google.com/spreadsheets/d/1OGASsCxkRpUu7vhjddwXs8oqcPUxjezDimCzV6xGDEg/edit
- Disrupción DCF: https://docs.google.com/spreadsheets/d/1A54Rcxwa375nFQn-GNPV0NXQRCDlpaPqvLs4zSb8mHs/edit

Se conserva el motor del Excel: 17 pestañas. Comparación de rango A1:AA260 por pestaña: 1.231 fórmulas en la referencia, 1.224 en las copias operativas porque **solo** se sustituyeron los siete valores predeterminados de entrada de `Input sheet!B27,B28,B29,B31,B32,B46,B62` con autorización explícita del usuario. Las 76 notas y 62 validaciones son iguales a la referencia; **no** se modificaron fórmulas de proyección/salida. Se verificó identidad de salidas entre cada copia y el registro. Esto no acredita paridad integral Excel–Google Sheets ni restauración de metadatos de hilos.

## Resultados de ejecución (solo candidatos)

| Historia | DCF Damodaran USD/acción | DCF auxiliar JMR previo | Brecha |
| --- | ---: | ---: | ---: |
| Base | 111,4426678512 | 111,4426678512 | 0 |
| Conservadora | 83,6628197955 | 83,3091733241 | +0,3536464715 |
| Optimista | 180,4275927836 | 173,8200154917 | +6,6075772919 |
| Disrupción | 58,1380119397 | 56,1497778461 | +1,9882340936 |

MOS 35 % del Base = **USD 72,4377341033**; dato provisional, **no sustituye** el vigente. La diferencia entre proyecciones anuales auxiliares y CAGR uniforme del DCF original está identificada, no conciliada económicamente en historias no Base.

Base: crecimiento año 1 14,1765 %, CAGR años 2–5 13,5035 %, margen EBIT objetivo 28 %, Sales-to-Capital 1–5 1,9, 6–10 1,400643, ROIC marginal terminal 9,7 %, WACC terminal 9,7 %, g terminal 4 %, WACC inicial 12,6833 %. El método de WACC del piloto se alimentó por entrada directa para reproducir candidato; el procedimiento oficial pide `Detailed` y verificación por hoja.

## Salvedades materiales que bloquean F4

1. **ASC 842**: deuda financiera 0 en la entrada no prueba inexistencia de arrendamientos económicos. Faltan conciliar pasivo corriente/no corriente, ROU, EBIT, ROIC, WACC y posible duplicación del conversor para mismo corte Q3 2026.
2. **NOL**: se cargaron USD 111,199 M del candidato y se activó selector; saldo, fecha, utilización y conciliación fiscal aún no certificados con SEC. La Base depende de ello; sensibilidad NOL=0 pendiente.
3. **WACC y riesgo país**: hay prima ROW proxy; WACC cargado directamente; exigir construcción reproducible Detailed, misma fecha Rf/ERP, pesos y deuda consistentes.
4. **Terminal económico**: justificar ritmo de convergencia ROIC marginal vs ROIC existente y reinversión terminal. Falta control económico independiente.
5. **Publicación técnica**: regenerar las tres matrices DCF 5×5 y sensibilidades de múltiplos para las cuatro copias y verificar centros; actualizar múltiplos FY+1/2/3 y análisis Nivel 1/2 al **mismo revision_id**; pruebas `controles_todas.sh`, registro, JSON, CI, despliegue y QA visual. **NO EJECUTADO** en este candidato.

## Aislamiento y decisión de publicación

- **AISLAMIENTO=OK (libros y expedientes):** estos resultados no modifican ni reciclan DUOL R2 en producción. Vigente a 5-nov-2026: `DUOL-20261103-A12-R2` con Base USD 139,10868579.
- No editar `catalogo.json`, `valoraciones/` ni la ficha productiva mientras los gates permanezcan bloqueados. El pedido del usuario de publicar autoriza **intentar** la promoción, **no** constituye aprobación de controles omitidos.
- F4: pasos 1 y 4 ejecutados **parcialmente**; pasos 2,3,3b,5,6 **no completados**. No se afirma PASOS 6/6.
- Próxima acción: cierre contable leases/NOL y WACC; recálculo de supuestos si corresponde; regenerar salidas/matrices/múltiplos/análisis y ejecutar controles completos. Tras pasar F4, sustituir una sola ficha DUOL y comprobar producción.
