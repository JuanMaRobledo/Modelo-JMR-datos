# Revisión transversal de las valoraciones activas — Modelo JMR A-1.2

**Corte del inventario:** 31 de octubre de 2026. **Rama examinada:** `main` de `JuanMaRobledo/Modelo-JMR-datos`, SHA `144285bb31075f511489bdaca0ee13e274e79f29`. Se leyeron individualmente los **23 JSON de valoración y sus 23 análisis asociados** del `catalogo.json`; se contrastaron expedientes de candidatos y CI de los PR #215 y #216. Esta revisión es **documental/estructural**, no una auditoría económica, no relee las 23 hojas de cálculo celda a celda ni verifica visualmente la app autenticada.

## Resumen verificable

- **23 revisiones activas únicas** en catálogo (una por ticker), **23 análisis**; 20 nuevas `A-1.2` `EN_REVISION` y 3 revisiones históricas activas (META R5, NVDA R4, XP R2). Los candidatos A-1.2 de esos últimos tres están en `candidatos/valoraciones/*-20261031-A12-R1/`, incorporados por PR #215 sin activarlos.
- **20/20 análisis A-1.2 vigentes** contienen `articleHtml` y `calculationHtml` y un vínculo a su valoración; el índice Nivel 1 es de 14 títulos H2 salvo DUOL (15 H2 por sección adicional). Los conteos de palabras estructurales de los 20 superan el mínimo editorial de 7.500; **no certifican semántica ni fuentes**. Nivel 2 existe pero requiere contrastar fórmulas, 12 apartados y sensibilidades en cada uno.
- **Múltiplos:** la existencia de cinco entradas `descuentoMultiples.metodos` o de siete matrices en `sensibilidadMultiples.matrices` **no prueba** cinco anclas independientes, pesos conciliados, ni una captura económicamente válida. El control global de la integración #211 identifica **16/20 matrices Base integradas** y cuatro expedientes críticos (UBER, GOOGL, INTU, NU), con salvedades; el control de descuento fue completo en MSFT y dejó seis con divergencias. Todas las `certificado:false` observadas **evitan afirmar auditoría económica**, no indican por sí mismas ausencia de la grilla.
- **CI rama principal**: Control JMR de ponderaciones en `main` aprobado, ejecución 41252935168. El PR #216 de promoción XP sigue en borrador; los tres workflows de su último SHA auditado fallaron por pruebas ligadas al catálogo y por longitud editorial. Correcciones de fixture/tests posteriores requieren nueva ejecución; no consta aprobación final.
- **App**: PR #151 y #152 fusionados y despliegue Vercel `READY` en commit `a0e555ba057c8576b6b270b9ee19415dd58cf054`. No equivale a comprobación SSO real de visor, editor y pestañas.

## Inventario individual del catálogo (sin recalcular cifras)

**Leyenda de controles:** `Rel.` = número de entradas de métodos relativos en el JSON; `5×5` = número de objetos bajo `sensibilidadMultiples.matrices`, **sin atribuirles validez económica automáticamente**; `N1` = palabras aproximadas del `articleHtml` y títulos H2, no palabras del Nivel 2. `EN_REVISION` no significa auditoría terminada. Valores por acción en USD según archivo, sin actualización de cotización.

| Ticker | Revisión activa | Base USD | MOS35 USD | Rel. | 5×5 | N1 palabras/H2 | Hallazgo/acción |
|---|---|---:|---:|---:|---:|---:|---|
| META | R5, legado | 726,65 | 472,32 | 7 | 0 | 12.077 / 13 | Candidato A12 Base 780,63; completar DCF y sensibilidades fuente antes de promover |
| NVDA | R4, legado | 381,79 | 248,16 | 7 | 28 | 8.470 / 13 | Candidato A12 Base 201,45; diferencia -47% exige puente de supuestos, hoja y matrices nuevas |
| XP | R2, legado | 13,53 | 8,79 | 7 | 0 | 6.180 / 18 | Candidato A12 FCFE Base 14,48; PR #216 bloqueado por reporte corto y anclas bancarias provisionales |
| SHAK | A12-R2 | 35,49 | 23,07 | 5 | 7 | 8.034 / 14 | EV/FCFF y P/FCFE N/D por denominadores: resolver aplicabilidad sin forzar números |
| UBER | A1 | 91,14 | 59,24 | 5 | 5 | 8.218 / 14 | Anclas dependientes de cotización/u otros métodos; pesos hoja vs JSON divergentes |
| MELI | A3 | 2.029,87 | 1.319,42 | 5 | 7 | 10.160 / 14 | FCFF/FCFE negativos: verificar denominadores, reinversión y N/A justificado |
| CELH | A1 | 34,85 | 22,65* | 5 | 7 | 11.004 / 14 | Verificar anclas y descuentos desde hoja, no solo presencia de grillas |
| ADBE | A3 | 432,29 | 280,99 | 5 | 7 | 10.515 / 14 | Contraste integral de sensibilidad por múltiplos y Nivel 2 |
| BSX | A4 | 41,76 | 27,14 | 5 | 7 | 10.262 / 14 | Contrastar captura e hipótesis sectoriales; no confundir estructura con calidad |
| CMG | A3 | 23,21 | 15,09 | 5 | 7 | 10.019 / 14 | Revisar serie histórica/anclas y coherencia Nivel 2 |
| NFLX | A2 | 74,08 | 48,15 | 5 | 7 | 10.234 / 14 | Verificar denominadores FY+3 y conciliaciones |
| GOOGL | R5 | 287,20 | 186,68 | 6 | 6 | 9.306 / 14 | Anclas no independientes y con precio observado; matrices no bastan |
| MSFT | R1 | 480,84 | 312,54 | 5 | 7 | 10.160 / 14 | Descuentos reconciliados estructuralmente; verificar QA visual y fuentes económicas |
| NKE | R1 | 37,73 | 24,52 | 5 | 7 | 10.153 / 14 | Pendiente conciliar descuentos, pesos y escenarios desde hoja |
| PYPL | R1 | 137,81 | 89,58 | 5 | 7 | 9.990 / 14 | Pendiente conciliar descuentos, pesos y escenarios desde hoja |
| EPAM | R1 | 184,41 | 119,87 | 5 | 7 | 9.846 / 14 | Pendiente conciliar descuentos, pesos y escenarios desde hoja |
| ZTS | R1 | 98,32 | 63,91 | 5 | 7 | 10.046 / 14 | Pendiente conciliar descuentos, pesos y escenarios desde hoja |
| ONON | R1 | 40,81 | 26,53 | 5 | 7 | 9.976 / 14 | Pendiente conciliar descuentos, pesos y escenarios desde hoja |
| NU | R1 | 18,33 | 11,91 | 3 | 3 | 10.065 / 14 | FCFE bancario: capital, perímetro RWA/CET1 y P/E/P/FCFE/P/BV sin anclas independientes |
| NVO | R1 | 63,43 | 41,23 | 5 | 7 | 10.135 / 14 | Descuentos incompletos, P/BV N/D opcional |
| INTU | R1 | 506,85 | 329,45 | 6 | 6 | 10.018 / 14 | Nivel 2 de DCF ampliado; seis matrices exploratorias, no exportadas como oficiales |
| AFYA | R1 | 20,92 | 13,59 | 5 | 7 | 8.146 / 14 | Nivel 2 extenso; revalidar estados, fiscalidad, fuentes y cifras publicadas |
| DUOL | A1 | 136,68 | 88,84 | 5 | 7 | 8.502 / 15 | Revisar título H2 adicional, sin inferir índice de 15 capítulos canónicos; SBC y reinversión |

\* CELH: `precioMOS` publicado 22,65 es redondeado; no reescribirlo sin comprobar salida original.

## Cierre de las tres candidaturas A-1.2

| Ticker | Base candidato | MOS35 candidato | Causas de no promoción | Cierre mínimo |
|---|---:|---:|---|---|
| META | 780,6303 | 507,4097 | DCF `Valuation output` sin salida nativa conciliada y matrices relativas nuevas faltantes; candidato 18 capítulos frente a contrato canónico 14 | Verificar la hoja o generar desde inputs oficiales, capturar fuentes, rehacer editorial 14+12, CI y QA |
| NVDA | 201,4460 | 130,9399 | Cambio Base vs R4 material (-47,2%); hojas nuevas sin output nativo y grillas; nivel narrativo candidato 6.339 palabras de prosa en gate separado | Reconstruir puente económico R4→A12, corregir hoja/DCF/relativos, completar profundidad y CI |
| XP | 14,4756 | 9,4091 | Hoja `XP FCFE!B64/B65` coincide con candidato, cuatro grillas bancarias de carácter provisional; capítulo N1 candidato 1.441 palabras; PR #216 no verde | Completar informe financiero extenso y los 14 capítulos canónicos; separar anclas no independientes con peso 0, resolver CI, promover EN_REVISION **sin certificar economía** |

**Precios de mercado de los candidatos**: META 614,99; NVDA 204,64; XP 14,29 USD al cierre del 30-oct-2026. No son cotizaciones en tiempo real y no deben transferirse a otros cortes.

## Regla de aceptación de una valoración nueva

1. Copia o actualización de la hoja oficial con fuentes, revisión, moneda/corte y escenarios. Solo la hoja determina el valor principal; no escribir a mano un DCF candidato sobre salida vacía.
2. Captura verificable y exportación a JSON de escenarios, denominadores, múltiples aplicables, fuentes/centros 5×5; `N/D` y `PENDIENTE_ANCLA` no son números. Cuando hay método no aplicable, `N/A` justificado y `peso=0`.
3. Informe de Nivel 1 de **14 capítulos canónicos**, sin reiteraciones artificiales, y Nivel 2 de **12 apartados de cálculos reproducibles** vinculados a igual `revisionId`, incluyendo sensibilidades relativas y DCF.
4. Un solo registro activo por ticker y copia histórica completa; `EN_REVISION` tras CI financiero y editorial verde y chequeo funcional; auditoría económica posterior, nunca presunta.
5. No ejecutar promociones en cadena si la primera empresa no supera la conciliación hoja→registro→app: la estructura común está lista, las salvedades por ticker no desaparecen con un cambio de formato.

## Evidencia y siguientes acciones

- `Modelo-JMR-datos` PR #211: recuperación de controles y captura 20 expedientes; PR #215: integración **solo de candidatos**; PR #216: propuesta XP no fusionada.
- `Modelo-JMR` PR #151: ficha única; #152: vista de candidatos; #153: procedimientos y prompts armonizados.
- Fuentes complementarias en este repositorio: `docs/AVANCE_ESTANDARIZACION_20261031.md`, `docs/PRIORIZACION_NIVEL2_20261031.md`, `docs/DIAGNOSTICO_MULTIPLOS_MODELO_A_20261030.md`.
- Orden: **(P0)** concluir XP, META, NVDA mediante evidencia nativa, reporte y CI; **(P1)** UBER, GOOGL, INTU, NU por anclas bancarias/relativas; **(P2)** seis descuentos y pesos EPAM/NKE/NVO/ONON/PYPL/ZTS; **(P3)** revisar en hojas el resto de 20 y QA visual autenticado. No recalcular DCF ya válidos solo por depuración.

**No se cambian** catálogo activo, valoraciones, hojas, fórmulas, análisis o pesos con este inventario.
