# DUOL · DUOL-20261104-A12-R3 · FASE_3 · BLOQUEADA PARA PROMOCIÓN

Actualización: 5-nov-2026 UTC / 4-nov Colombia. Método A-1.2, reglas v33. Información hasta 4-nov-2026; contabilidad 30-sep-2026. Ejecutor Codex / ChatGPT Work; esfuerzo exacto no expuesto. AISLAMIENTO=OK. No es auditoría independiente.

**Estado actual: CANDIDATO, publication_ready=false.** La revisión económica y las reparaciones descritas están aplicadas en la copia R3. La publicación solicitada no se ejecutó porque el puente de arrendamientos no está conciliado. Se retiró el cero no soportado de Input sheet!B78; la fórmula canónica B81 devuelve REVISAR y el DCF queda en blanco automáticamente. No se modificó esa fórmula para obtener el bloqueo.

[Copia R3](https://docs.google.com/spreadsheets/d/1TdXRa1f1HL5JusQV3LDgEnb4GWKYXEbVd6lhQjGSqQA/edit) · [Respaldo anterior a reparaciones](https://docs.google.com/spreadsheets/d/1FGr0uQFMTBzfS_QJF3mDAqx7FDOiX0RkBtaZ1k245Rw/edit?usp=drivesdk) · [PR250](https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/250).

R2 continúa como única versión publicada. Se confirmó que Valuation output!B35 de R2 sigue en139,1086857874. No se cambió catálogo, análisis publicado, registro de vigencia, plantillas oficiales ni el motor global.

**PASOS F3: 8/10 completos, 2/10 parciales (múltiplos y cadena integral). F4: publicación intentada por preparación y controles; no promovida.** No se presenta esta entrega como cierre completo de valoración ni como análisis Nivel1/2 actualizado publicado.

## Cálculo condicional preservado, no salida aprobada actual

| Medida USD/acción | R2 publicada | R3 provisional anterior | Diagnóstico corregido antes del bloqueo |
|---|---:|---:|---:|
| DCF Base FCFF |139,1087|134,8958|106,9762|
| Precio Base×0,65 |90,4206|87,6823|69,5345|

El diagnóstico es una fotografía anterior a retirar B78=0. La salida vigente de la hoja R3 está bloqueada/en blanco. **106,9762 no es valor final aprobado ni una nueva cotización.** El precio128 usado por el expediente es histórico del3-nov, no precio actual.

## Cambios aplicados y su causa

| Palanca | Antes de este cierre | Después | Causa / soporte nativo |
|---|---|---|---|
| Crecimiento1–5 |13,6378%CAGR|Mismos motores explícitos; pequeño cambio de redondeo|Audiencia, conversión y ARPU permanecen como hipótesis; ingresos LTM exactos1182,296m. No extrapola DAU ni Max premium.|
| Margen EBIT año1 |23% fijado|22,3024% por fórmula|Se restaura InputB28 enlazada al EBIT económico LTM. Objetivo28% se mantiene con reserva de cohortes I+D y escala.|
| S/C marginal1–5 |1,9|1,9|Juicio conservado, no cociente promedio: TesisC66→InputB32. No se declara calibración histórica terminada.|
| S/C6–10 |2,3|1,400643|Convergencia a SoftwareInternetGlobal, InputK28→TesisC73→InputB33; no sostener mejora de eficiencia sin barrera demostrada.|
| Rf/ERP madura |4,91%/4,20% mezclados|5,29%/4,41%|Pareja mensualNYU1-nov, conforme§4. CountryequityB2 actualizado; fórmulas de ponderación conservadas.|
| ERP inicial |4,20% directa|5,5295907%|K33 por geografíaFY2025: EEUU37,8005%, ROW62,1995%; ROW añade proxy1,80pp. Es estimación, no distribución observada por país.|
| WACC inicial/terminal |10,4930%/9,50%|12,6376368%/9,70%|Detailed, beta global1,3370 reapalancada, pesos de mercado; terminal beta1=Rf+ERP madura. Igual para cuatro historias.|
| ROIC nuevo terminal Base/C/D |15%/11,5%/12%|9,70% en las tres|Registro moatDUOL previo: sin ventaja defendible. Marca/hábito con bajos costes de cambio no acreditan exceso perpetuo. Override nativoN5:N7, fórmulaG preservada. Optimista19% sigue condicionada a ventaja futura, no es Base.|
| Capital operativo |Incluía inversionesLP no operativas|InputB83=B82=110,120m|Excluir valor en libros del capital; sumar su valor económico una sola vez al patrimonio. No altera por sí solo los flujos proyectados.|

No se ha probado una descomposición aditiva del cambio de precio: los supuestos interactúan. Se conserva respaldo nativo para repetir comparaciones aisladas. La clasificación competitiva es un juicio del analista, no una conclusión atribuida a Damodaran sobre DUOL.

## Reparación de fuentes y fórmulas

1. Comparación contra plantillaIA vigente:8687 fórmulas inspeccionadas,98 ausentes/reemplazadas y37 distintas inicialmente. Se restauraron134 expresiones canónicas; B47 se mantiene como fórmula explícita de tasa madura. El panel de reinversión se recuperó, ampliando únicamente Supuestos Recomendados a60filas. No se eliminaron las62pestañas heredadas.
2. Se restauraron fórmulas tributarias y puentes de preferentes de múltiplos. Los valores relativos no se certifican por coincidir sus centros.
3. Sensibilidad v2 en copiaR3: en la primera matriz años1–10 mantienen curva original y solo cambia WACC terminal. Se agregan restricciones g≤Rf y WACC>g en los75bloques; no se cambió el motor DCF principal.
4. Se reconstruyeron FY2025 y LTM de resultados/flujo de caja en Entradas históricas auxiliares!A32:H76, con tres entradas primarias y LTM=FY+9Mactual−9Mprevio. Las salidas en Income Statement y Cash Flow Statement son referencias/fórmulas nativas.
5. CFO LTM435,753m; PPE28,728m más software11,537m; FCF395,488m. El anterior406,994m omitía software y mezclaba redondeos. Los componentes de CFO, CFI y CFF ahora concilian con sus totales y el movimiento de caja para FY2025,9M2025 y9M2026. FCF menosSBC238,892m es diagnóstico, no FCFE económico certificado.
6. Intereses y otros no operativos se separaron; utilidad LTM145,737m, EBIT146,122m e I+D362,473m. El10-Q fue publicado4-nov: no se atribuye disponibilidad al3-nov.

## Controles y evidencia

| Control | Resultado y alcance |
|---|---|
| node verificar_cierre.mjs |APROBADO: DCF condicional reproduce106,9761673399;75celdas de las tres matrices reproducidas, incluidaterminal-only; identidades primarias CFO/CFI/CFF/caja y resultados pasan.|
| diff_formulas_plantilla.py |APROBADO en captura previa a últimos ajustes de fuentes, por adaptador explícito de SOLOLECTURA:0 fórmulas→número/vacío sin declarar. Código original sin modificación. Alcance oficial primeras400filas por pestaña; no equivale a revisar las3600del motor de sensibilidad.|
| R2 y catálogo |R2 B35 intacto139,1086857874; no promoción ni cambio de referencia.|
| Control nativo de promoción |REVISAR enB81; cuatro historias PENDIENTE;B35 vacío tras retirar B78no soportado. Ver CONTROL_FINAL_NATIVO.json.|
| Gates CLI completos |NOEJECUTADOS: no hay autenticación CLI/serviceaccount disponible; no se simula una consulta viva. El adaptador de captura solo se usó para el diff indicado.|
| Render nativo / auditoría independiente |NOEJECUTADOS. No se emite dictamen VERIFICADO ni se afirma calidad visual completa.|

## Bloqueos precisos que quedan

- **Leases, puente estructural:** InputB78 decía0 ya reconocido, pero10-Qp6 tiene84,216mLP y corriente agrupada en70,536m de accruedliabilities; el conversor descuenta el cronogramaFY2025. Hace falta conciliar mismo corte/perímetro, porción corriente y deuda reconocida contra balance, sin sumar otra vez pasivosASC842. No reemplazar el total por84,216LP. B78 queda pendiente yB81 bloquea.
- **NOL:** origen111,199mFY2025 verificado; no hay saldo fiscalQ3 conciliado. No sumar72,425mestatales,76,419mcréditos ni todoDTA203,605m al mismo NOL; tienen otra naturaleza/límites. No afirmar que un estrésNOL0 acota todo el riesgo fiscal.
- **CohortesI+D y reinversión:** el conversor usa gastoLTM y cohortesFY, con solapamiento de ventanas; reconstruir cohortesLTM homogéneas y reconciliar inversión marginal/prepagos. S/C1,9 y margen28% siguen siendo hipótesis, no datos auditados.
- **Múltiplos:** FCFF histórico312,8m permanece como entrada heredada sin fórmula reproducible; las anclas por ciclo, P/E fiscalmente normalizado, tratamientoSBC y denominadores deben reconstruirse antes de certificar. Restaurar una fórmula canónica no convierte una utilidad reportada con beneficio fiscal en utilidad normalizada.
- Ejecutar controles integrales sobreIDR3, con registro candidato explícito, y verificar app/preview solo después de resolverlos. No modificar el mapeo oficialR2 para hacer pasar una prueba de candidato.

## Archivos y fuentes

CIERRE_REVISION.json y LECTURA_CONDICIONAL_NATIVA.json preservan el cálculo condicionado; CONTROL_FINAL_NATIVO.json demuestra el bloqueo vigente. verificar_cierre.mjs reproduce el alcance declarado. REVISION_SUPUESTOS.json, verificar_revision.mjs y FASE_3_ENTREGA_ANTES_CIERRE.md son fotografías históricas anteriores a este cierre: **no representan la salida actual**.

Fuentes: [10-K2025](https://www.sec.gov/Archives/edgar/data/1562088/000162828026012494/duol-20251231.htm), [10-Q4-nov2026 originaldel emisor](https://duolingo.gcs-web.com/static-files/f27581cd-cf47-4058-a316-2dcca04cfb00), [NYU ERP mensual](https://pages.stern.nyu.edu/adamodar/New_Home_Page/home.htm), registro moat y plantilla del repositorio JMR-valuation consultados enmain. Datos monetarios enUSDmillones salvo precios poracción. Juicios de crecimiento, margen y riesgo diferenciados de hechos reportados.
