# CELH Floyd R1–R6 · puerta de publicación operativa

Revisión única `CELH-REBOOT-3T26-R1` · Estado **CANDIDATO** · Corte 30/09/2026 · Precio fijo US$33,19 09/11/2026. R6 es independiente y queda fuera de esta fase.

## Correcciones de infraestructura COMPLETADAS Y FUSIONADAS
- `Modelo-JMR` [PR#196](https://github.com/JuanMaRobledo/Modelo-JMR/pull/196): script oficial propuesto `scripts/floyd-r1r6-sync.mjs`, biblioteca de validación `lib/floyd-transfer.js`, manifiesto CELH 650 mapeos y pruebas. **Fusionado** tras suite CI verde. El script solo modifica entradas literales previstas, no fórmulas de 17 hojas, y compara firma SHA-256 antes de aplicar.
- `Modelo-JMR-datos` [PR#266](https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/266): candidatos no publicados ya no se clasifican incorrectamente como «SUSTITUIDA» en `scripts/registro_revisiones.py`. **Fusionado** tras tests específicos verdes; mismo código aprobado incluido en rama PR#265.
- **NO se ha ejecutado** aún ninguna de las 650 transferencias en vivo del nuevo script con credenciales. El manifiesto no convierte en oficiales las salidas pre-preferentes del Ginsu.

## Procedimiento de traspaso autorizado (repetir dry-run+apply por etapa)
Entorno: repositorio `Modelo-JMR` en main, Node22, `GOOGLE_SERVICE_ACCOUNT_JSON_CONTENT` solo como secreto con acceso Editor a H, D-B/D-C/D-O, M, sin exponer en logs.

Primera etapa (no escribe):
```bash
node scripts/floyd-r1r6-sync.mjs --manifest docs/floyd-sync-manifests/CELH-REBOOT-3T26-R1.json --stage H_TO_D
```
Registrar `planSha256` y verificar que la lista de 36 entradas coincida con las celdas históricas de H. Aplicar solo ese plan preciso con:
```bash
FLOYD_SYNC_APPROVED=1 node scripts/floyd-r1r6-sync.mjs --manifest docs/floyd-sync-manifests/CELH-REBOOT-3T26-R1.json --stage H_TO_D --apply --expected-plan <PLAN_SHA256>
```
Si hay conflicto de hash, **no forzar ni saltar el bloqueo**: repetir dry-run. Verificar recibo `reports/floyd-sync/<REV>_H_TO_D.json` y celdas destino. Repetir H_TO_M (586 celdas de estados, con inventario desagregado sin doble suma), D_TO_M (21 celdas de **costos y parámetros**, expresamente NO el valor B33 pre-Pepsi), RESULTS_TO_DB (7 celdas no económicas: Ke/WACC y costo de capital). No dar por completa R4 solo porque el traspaso parcial pasa.

**Precauciones:** el origen calcula y destino sólo recibe snapshot verificado; no IMPORTRANGE; script aplica una etapa por llamada para permitir recálculo; no hay transacción atómica multi-libro, por lo que cada recibo debe guardarse y revisarse si falla después de escribir un libro.

## Puertas económicas aún BLOQUEANTES
1. **Pepsi A/B:** construir puente final de flujo y opciones con derechos completos: 5% preferente, market-share/VWAP, conversión anticipada desde 2031, opción rescate desde 2032, cuotas 2035/2038, pérdida de dividendos tras conversión, valor de tiempo y stock compensation. SEC 10-Q 30/09/26 nota 12. Valor Ginsu B33 **no corresponde** a común; no transferir a celdas oficiales de presentación ni JSON para EN_REVISION hasta cerrar. Diagnóstico BSM (NO certificado) en `PEPSI_PREFERENTES_DIAGNOSTICO_R3.md`: Base estático US$27,07 frente a sensibilidad con opciones/cupons US$25,58 (diferencia US$1,50/acción).
2. **Capital preferente distinto de NCI:** M Balance Sheet 9M26 debe conciliar activos 5152,385 = pasivos2117,042 + mezzanine1759,975 + común1275,368 USD M, sin reclasificar preferred como `intereses no controlantes redimibles`. M no contiene actualmente un canal certificado para este puente; cualquier ajuste estructural de plantilla debe hacerse por **mantenimiento separado con pruebas**, no por IA durante la valoración.
3. **Múltiplos:** EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF con pares y anclas FY+1/FY+2/FY+3, centro y matrices 5×5 de cada método, todos con derechos Pepsi y denominadores comunes conciliados; justificar N/D peso0 cuando sea real. M `Supuestos y control!B60` actual `FALTAN DATOS Y SUPUESTOS`, B63 `PENDIENTE`, B64 `NO PUBLICAR`. No llenar ceros inventados para convertir a EN_REVISION.
4. **Historicos y motor:** cotejo granular SEC FY2016–2025 y LTM; arrendamientos, SBC/RSU, caja restringida, gastos de terminación; evidencia de 1.297 fórmulas/76 comentarios por cada Ginsu copiado intactos, ROIC año10≈17,4% vs terminal11% económicamente explicado.
5. **Resultados finales:** después de puente Pepsi y M listo, completar `Resumen de valoraciones` y `Presentación` D-B por script con SHA; actualizar dos JSON misma revisión, mismo valor Base y MOS35%; peso de múltiplos separado y análisis 14+12 con cifras definitivas. Pruebas de 7 pestañas app y enlazado H, D-B/C/O, M, A; no publicar porque un preview esté READY.
6. **CI:** luego del fix registro #266, su check de CELH pasó. El control global de ponderaciones aún falla por referencias históricas MELI, MSFT, UBER (celh snapshot específico PASÓ). Corregir esos fixtures basándose en revisiones reales de esas empresas mediante mantenimiento separado, nunca modificar valores CELH para forzar verde.

## Estado de publicación
- `Modelo-JMR-datos` [PR#265](https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/265): abierto como draft, misma revisión. `catalogo.json` **sin modificar**. Los JSON/Doc son **CANDIDATO**.
- App: la ficha nueva R1–R6 no se ha publicado ni verificado en producción.
- R6: independiente, no ejecutar en esta fase.

**Regla final:** fusionar/promover `EN_REVISION` solo si las seis puertas de arriba tienen evidencia, la compuerta de M y CI están verdes, el valor ordinario no mezcla preferentes y las salvedades restantes son inmateria. Ante bloqueo mantener CANDIDATO y conservar expediente previo.
