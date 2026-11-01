# Conciliación hoja ↔ JSON de las 23 valoraciones activas · 1-nov-2026

**Lectura de solo lectura** de cada hoja Google con la cuenta de servicio del proyecto, contra el JSON activo de `main` (commit `dfaedae`). No se escribió en ninguna hoja ni valoración. Datos por empresa en `evidencia/reconciliacion-hoja-json-20261101/<TICKER>.json`; script `scripts/reconciliar_hoja_json_20261101.py`. **No es auditoría económica**: comprueba que lo publicado coincide con lo que calcula la hoja, no que los supuestos sean correctos.

## Resultado

| Ticker | Revisión | DCF Base hoja / JSON | K5:K8 | Peso DCF hoja / JSON | Consolidados que coinciden | Matrices OK hoja/JSON | Clasificación |
|---|---|---|---|---|---|---|---|
| META | META-20261101-A12-R1 | 737,51 / 737,51 | LLLL | 0,60 / 0,60 | 5/5 | 5/5 | **CONCILIADA** |
| NVDA | NVDA-20261101-A12-R1 | 205,95 / 205,95 | LLLL | 0,60 / 0,60 | 5/5 | 5/5 | **CONCILIADA** |
| XP | XP-20261031-A12-R1 | no abre | — | — | — | — | **NO AUDITABLE** |
| SHAK | SHAK-20261029-A12-R2 | 35,49 / 35,49 | LLLL | 0,80 / 0,80 | 5/5 | 5/5 | **CONCILIADA** |
| UBER | UBER-20261030-A1 | 91,14 / 91,14 | LLLL | 0,60 / 1,00 | 0/5 | 5/5 | **DIVERGENCIA** |
| MELI | MELI-20261028-A3 | 2.029,87 / 2.029,87 | LLLL | 0,60 / 0,60 | 5/5 | 5/5 | **CONCILIADA** |
| CELH | CELH-20261028-A1 | no abre | — | — | — | — | **NO AUDITABLE** |
| ADBE | ADBE-20261028-A3 | 432,29 / 432,29 | LLLL | 0,60 / 0,60 | 5/5 | 7/7 | **CONCILIADA** |
| BSX | BSX-20261028-A4 | 41,76 / 41,76 | LLLL | 0,50 / 0,50 | 5/5 | 7/7 | **CONCILIADA** |
| CMG | CMG-20261028-A3 | 23,21 / 23,21 | LLLL | 0,40 / 0,40 | 5/5 | 7/7 | **CONCILIADA** |
| NFLX | NFLX-20261028-A2 | 74,08 / 74,08 | LLLL | 0,60 / 0,60 | 5/5 | 7/7 | **CONCILIADA** |
| GOOGL | GOOGL-20261029-R5 | 287,20 / 287,20 | LLLL | 0,60 / 1,00 | 5/6 | 6/6 | **DIVERGENCIA** |
| MSFT | MSFT-20261028-R1 | 480,84 / 480,84 | LLLL | 0,60 / 0,60 | 5/5 | 7/7 | **CONCILIADA** |
| NKE | NKE-20261029-R1 | 37,73 / 37,73 | LLLL | 0,40 / 0,60 | 5/5 | 7/7 | **DIVERGENCIA DE PESOS** |
| PYPL | PYPL-20261029-R1 | 137,81 / 137,81 | LLLL | 0,40 / 0,60 | 5/5 | 7/7 | **DIVERGENCIA DE PESOS** |
| EPAM | EPAM-20261029-R1 | 184,41 / 184,41 | LLLL | 0,50 / 0,60 | 5/5 | 7/7 | **DIVERGENCIA DE PESOS** |
| ZTS | ZTS-20261029-R1 | 98,32 / 98,32 | LLLL | 0,30 / 0,60 | 5/5 | 7/7 | **DIVERGENCIA DE PESOS** |
| ONON | ONON-20261029-R1 | 40,81 / 40,81 | LLLL | 0,60 / 0,60 | 5/5 | 7/7 | **CONCILIADA** |
| NU | NU-20261029-R1 | — / 18,33 | PPPP | — / 1,00 | 0/3 | 0/3 | **BLOQUEO MATERIAL** |
| NVO | NVO-20261029-R1 | 63,43 / 63,43 | LLLL | 0,55 / — | 5/5 | 6/6 | **DIVERGENCIA DE PESOS** |
| INTU | INTU-20261029-R1 | — / 506,85 | PPPP | 1,00 / 1,00 | 0/6 | 0/6 | **BLOQUEO MATERIAL** |
| AFYA | AFYA-20261029-R1 | 20,92 / 20,92 | LLLL | 0,40 / 0,40 | 5/5 | 7/7 | **CONCILIADA** |
| DUOL | DUOL-20261029-A1 | 136,68 / 136,68 | LLLL | 0,60 / 0,60 | 5/5 | 7/7 | **CONCILIADA** |

`K5:K8`: L = LISTO, P = PENDIENTE. «Consolidados que coinciden»: métodos cuyo valor consolidado a hoy de la hoja (historia Base) iguala al del JSON.

## Detalle
- **META** — CONCILIADA: DCF, pesos, consolidados por método y matrices coinciden con la hoja.
- **NVDA** — CONCILIADA: DCF, pesos, consolidados por método y matrices coinciden con la hoja.
- **XP** — NO AUDITABLE: la cuenta de servicio no puede abrir la hoja (no compartida).
- **SHAK** — CONCILIADA: DCF, pesos, consolidados por método y matrices coinciden con la hoja.
- **UBER** — DIVERGENCIA: pesos 60/40 en la hoja frente a 100/0 en el JSON; consolidados por método distintos; anclas derivadas del precio.
- **MELI** — CONCILIADA: DCF, pesos, consolidados por método y matrices coinciden con la hoja.
- **CELH** — NO AUDITABLE: la cuenta de servicio no puede abrir la hoja (no compartida).
- **ADBE** — CONCILIADA: DCF, pesos, consolidados por método y matrices coinciden con la hoja.
- **BSX** — CONCILIADA: DCF, pesos, consolidados por método y matrices coinciden con la hoja.
- **CMG** — CONCILIADA: DCF, pesos, consolidados por método y matrices coinciden con la hoja.
- **NFLX** — CONCILIADA: DCF, pesos, consolidados por método y matrices coinciden con la hoja.
- **GOOGL** — DIVERGENCIA: pesos 60/40 en la hoja frente a 100/0 en el JSON; P/V sin conciliar; anclas no independientes.
- **MSFT** — CONCILIADA: DCF, pesos, consolidados por método y matrices coinciden con la hoja.
- **NKE** — DIVERGENCIA DE PESOS: DCF y consolidados coinciden; los pesos de la hoja difieren del JSON (retención guardada por prueba).
- **PYPL** — DIVERGENCIA DE PESOS: DCF y consolidados coinciden; los pesos de la hoja difieren del JSON (retención guardada por prueba).
- **EPAM** — DIVERGENCIA DE PESOS: DCF y consolidados coinciden; los pesos de la hoja difieren del JSON (retención guardada por prueba).
- **ZTS** — DIVERGENCIA DE PESOS: DCF y consolidados coinciden; los pesos de la hoja difieren del JSON (retención guardada por prueba).
- **ONON** — CONCILIADA: DCF, pesos, consolidados por método y matrices coinciden con la hoja.
- **NU** — BLOQUEO MATERIAL: hoja en PENDIENTE: el DCF publicado no sale de una salida nativa de la hoja.
- **NVO** — DIVERGENCIA DE PESOS: DCF y consolidados coinciden; los pesos de la hoja difieren del JSON (retención guardada por prueba).
- **INTU** — BLOQUEO MATERIAL: hoja en PENDIENTE: el DCF publicado no sale de una salida nativa de la hoja.
- **AFYA** — CONCILIADA: DCF, pesos, consolidados por método y matrices coinciden con la hoja.
- **DUOL** — CONCILIADA: DCF, pesos, consolidados por método y matrices coinciden con la hoja.

## Lo que esto significa
1. **12 expedientes conciliados** (META, NVDA, SHAK, MELI, ADBE, BSX, CMG, NFLX, MSFT, ONON, AFYA, DUOL): lo publicado coincide con la hoja. Eso no certifica que sus anclas de múltiplos sean independientes ni sus supuestos.
2. **NKE, PYPL, EPAM, ZTS y NVO** coinciden en DCF, consolidados y matrices, pero los pesos de la hoja (DCF 0,40 / 0,40 / 0,50 / 0,30 / 0,55) difieren del 0,60 genérico del JSON (NVO no tiene `pesoDcf`). Una prueba (`ponderaciones_no_sobrescribir`) retiene esos valores a propósito hasta contar con fotografía nueva, justificación y comparación. **Resolverlo exige además regenerar el estado «ponderaciones pendientes» que el Nivel 2 de EPAM, ZTS y NVO incluye como texto**; cambiar solo el JSON dejaría los documentos contradiciéndose. Los pesos de la hoja salen de la categoría de empresa (`Resumen de Valoración!G3`) y son juicio del analista, no evidencia: hay que justificarlos antes de publicarlos.
3. **UBER y GOOGL**: el JSON mantiene 100/0 y la hoja 60/40. El estado del JSON es el **correcto según la regla vigente** mientras las anclas sigan derivadas del precio (evidencia en `evidencia/anclas-20261031/`): una ancla ligada al precio observado debe quedar con peso cero. Para pasar a 60/40 hay que reconstruir anclas independientes (historia propia más pares, como se hizo en NVDA y META) y justificar cada peso.
4. **INTU y NU**: sus hojas están en `PENDIENTE` y no producen `B35`; el DCF publicado (506,85 y 18,33) proviene de un cálculo independiente y no de una salida nativa de la hoja. La regla de aceptación dice que un valor así «puede conservarse únicamente como candidato, no valor vigente oficial». Hoy ambos figuran como EN_REVISION en el catálogo con esa salvedad documentada. **Es una decisión de política que corresponde al propietario**: o se completan sus hojas (INTU: motor Damodaran sin alimentar; NU: contrato bancario P/E, P/FCFE y P/BV) o se pasan a candidato.
5. **XP y CELH**: la cuenta de servicio no puede abrir sus hojas. Para auditarlas hay que compartirlas con `jmr-valuation-bot@jmr-valuation-508617.iam.gserviceaccount.com` (lectura basta).

## Aplicación
`modelo-jmr.vercel.app` responde 401 sin sesión (SSO) y lee el catálogo de `main` del repositorio de datos. Con las herramientas disponibles **no se puede comprobar** visor, editor, pestañas, estados financieros completos ni móvil: esa prueba sigue sin ejecutarse y no debe darse por aprobada.

## Adenda — XP y CELH (tras mover las hojas a Análisis)

- **CELH:** DCF hoja 34,8526 = JSON; K5:K8 LISTO; B85/B108/B84 VALIDADO; pesos y 5 consolidados coinciden; 7 controles de sensibilidad OK.
- **XP:** la hoja abre (71 pestañas). Valor FCFE en `XP FCFE!B64` = 14,4756 (`B65` = 9,41 es el precio con MOS) USD/acción = JSON. Las compuertas de la plantilla estándar (Escenarios K5:K8, Input B85/B108) están en PENDIENTE porque XP usa el motor FCFE propio; no se forzaron. Los consolidados de múltiplos y las matrices estándar no son comparables con el JSON. Queda pendiente decidir si se completa la plantilla estándar para XP.
