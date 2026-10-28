# CELH — Reinicio independiente — control técnico y punto de continuación
Fecha: 2026-10-28. Revisión de preparación: CELH-20261028-R1.
Estado: EN PREPARACIÓN / NO PUBLICADO. No es auditoría económica independiente.

## Identidad de los entregables nuevos
- Fuente contable protegida: https://docs.google.com/spreadsheets/d/1O0tCafCwsCvt8bYnFtKR0SNtjkahEeqm5j192XzkrXs/edit
- Copia nueva de la maestra: https://docs.google.com/spreadsheets/d/1UjNx2Md6-IPRlB-QJQ9w76lu2Q_4q5lt2N1sOAZGmD4/edit
- Maestra vigente consultada: 1OYhz6ulMNNUAs-aW8q9FatOJgmfKAVTBAOmRMhqZzaY. No se alteraron sus fórmulas.

## Conservación y límites contables
Se extrajeron exclusivamente Income Statement, Balance Sheet, Cash Flow Statement y Por acción de cinco hojas anteriores; no se copiaron proyecciones, escenarios, múltiplos de salida ni resultados DCF.
La fuente incluye 2.313 observaciones SEC con unidad, período y accesión; 1.175 registros contables de origen de cuatro hojas antiguas (la hoja vigente se conserva como importación original en las notas de las matrices), y 434 registros contables adicionales de dos libros Excel antiguos.
Las matrices normalizadas cubren 2016-2025 y LTM al 30-jun-2026. Los datos no corroborados se identifican N/D; esto NO equivale a validación contable completa. Las notas conservan los importes importados originales.
Se corrigieron diferencias de precisión y de clasificación contrastables con SEC; no llamar a todas las diferencias errores materiales.
Se comprobaron ausencia de errores de fórmula en las cuatro matrices de datos y siete protecciones de hoja; no se ejecutó la revisión visual nativa completa.
La copia nueva conserva 61 pestañas. Se cargaron 535 entradas históricas numéricas y se omitieron 109 destinos con fórmula durante esa carga; la comparación exhaustiva de fórmulas contra la maestra sigue pendiente.

## Hallazgo técnico que impide certificar los siete múltiplos
La maestra calcula Financials Multiples!E54:H54 (Base; equivalentes E15:H15 y E94:H94) desde EBIT + otros resultados − impuestos. La cadena no incorpora explícitamente dividendos de preferentes ni la asignación de beneficios a preferentes participantes. PE!F20:H20 toma esa utilidad; las fórmulas de precio restan opciones, pero no transforman la utilidad consolidada en utilidad atribuible al común.
Esto es relevante para CELH, no una falta de documentación menor:
- 2025 utilidad consolidada: USD107,999 millones.
- Dividendos de preferentes: USD37,608 millones.
- Resultado asignado a preferentes participantes: USD6,554 millones.
- Utilidad atribuible al común: USD63,837 millones.
Identidad comprobada: 107,999 − 37,608 − 6,554 = 63,837.
La diferencia del denominador es 69,1793% respecto a la utilidad común; NO se afirma que ese sea el impacto en el valor DCF o en el precio por acción.

Otro control imprescindible: la asignación contable de resultados para EPS no equivale a una salida de caja ni debe restarse mecánicamente del patrimonio común. En 1S2026, la conciliación de resultados retenidos es 175,912 + 165,392 − 28,139 = 313,165 millones. Esta identidad también se comprobó.
P/BV debe usar su puente patrimonial y los movimientos de equity disponibles; P/OCF debe conservar su definición y explicar comparabilidad. No convertir automáticamente OCF en FCFE.

### Corrección acotada propuesta, aún NO aplicada
1. Incorporar un puente explícito y trazable entre utilidad consolidada, dividendos de preferentes, asignación participante y utilidad común en las tres historias ordinarias.
2. Hacer que P/E use utilidad común. Separar el tratamiento del FCFE atribuible al común del cálculo FCFF, que permanece operativo.
3. Completar el puente P/BV con dividendos preferentes efectivamente pagados y movimientos de patrimonio, sin descontar una segunda vez la asignación no monetaria.
4. Conciliar preferentes convertibles y opciones con valor de la reclamación, denominador de acciones y WACC: valor contable, valor nominal/redención, valor de mercado estimado y acciones de conversión son conceptos distintos. No aceptar valor contable como mercado sin prueba ni usar acciones convertidas y deducir otra vez el mismo derecho.
5. Mantener fórmulas y resultados idénticos cuando no haya preferentes; probar estos casos antes de mantenimiento de Maestra/IA/Manual y antes de migrar la copia nueva. Conservar intacto el respaldo oficial.
No rediseñar pestañas, eliminar selectores ni implantar un DCF paralelo.

### Pruebas ejecutadas
- Identidad de utilidad común 2025: PASS.
- Conciliación de resultados retenidos 1S2026: PASS.
- Caso aritmético sin preferentes conserva la utilidad: PASS.
Son fixtures contables; NO sustituyen los controles de la hoja ni una auditoría económica.

## Limpieza efectuada
- Drive: 38 archivos eliminados de forma permanente: 16 artículos/informes/HTML de CELH y su alias CELHN; cinco hojas de valoración anteriores; 15 archivos de respaldos, supuestos, resultados y auditorías en el archivo celh_anterior_2026-10-05; una imagen de valoración antigua y un documento vacío de esa carpeta.
- JMR-valuation/main: 60 archivos específicos eliminados (incluidos scripts de supuestos antiguos, respaldos y alias CELHN) y registros compartidos depurados sin retirar las plantillas oficiales.
- Modelo-JMR-datos/main: eliminados valoraciones/CELH-1790595594623.json, analisis/CELH-research-1790597282768-kjm45.json y auditorias/narrativas/CELH.md; retirados del catálogo y de su nota de publicación.
- Modelo-JMR/main: retirada la fila CELH del manifiesto de recuperación, de los múltiplos agrupados y de la bitácora de terceros.
No se reescribió el historial Git. Otras ramas, etiquetas, commits anteriores, posibles referencias de PR/forks/cachés y documentos colectivos pueden conservar copias; no se declara eliminación total.
Permanecen los libros CELH.xlsx y CELH.xlsm y PDFs/documentos de origen por clasificación y conservación contable; no se declaran depurados integralmente. Los archivos locales descargados que mezclan estudios con datos solo se usaron para extraer datos históricos, no como fuente de supuestos.

## Referencias de las modificaciones
- Datos: d18e22ae96b983dd3435d496bed83fab8e49449a; referencia residual retirada en 9e56faa6198dd48865c26f4c44b56e62b8deb859.
- App: 0cf5c63359c5655c8704e246e05b784b228304fc.
- Motor: b5d9e53597445f453c2fa3b03c907fb43fa96bd0; referencia residual de hoja retirada en 636ec858337f5bb04dc97750fac3778b49d24fb6.

## Autorizaciones recibidas y alcance
A. Mantenimiento mínimo de fórmulas oficiales para preferentes participantes y reclamaciones convertibles, con pruebas de regresión y respaldo intacto. La regla vigente exige fórmulas intactas; no se introdujo una excepción silenciosa.
B. Para eliminar las copias anteriores accesibles por Git: preparar una reescritura selectiva de las referencias afectadas en los tres repositorios, preservando contenidos de otras empresas, plantillas y fuentes contables. Cambiarán los SHA de commits afectados y descendientes y requerirá force-with-lease coordinado. La purga de forks y cachés ajenos puede requerir intervención de GitHub. Autorizada expresamente el 28-oct-2026: «Autorizo ambas». Todavía no ejecutada.

## Controles pendientes / publicación
La valoración de cuatro escenarios, los siete múltiplos compatibles, matrices conciliadas, DCF inverso y artículo completo todavía no están terminados. No hay resultados nuevos publicables ni dictamen económico.
La aplicación protegida respondió 401 también mediante la lectura autenticada del conector Vercel; la verificación visual de producción no está resuelta.
El entorno no dispone de credenciales locales del motor Sheets. El conector permite editar la hoja, pero no se declara que controles_todas.sh se ejecutó.
scripts/unificacion_hojas.py no se encontró en main del motor en esta revisión; sí existe audit_master_formulas.py. Resolver el control oficial sin inventar un aprobado ni alterar guardas.

## Evidencia primaria nueva utilizada
- SEC 10-K 2025: https://www.sec.gov/Archives/edgar/data/1341766/000134176626000024/celh-20251231.htm
- SEC 10-Q 30-jun-2026: https://www.sec.gov/Archives/edgar/data/1341766/000134176626000050/celh-20260630.htm
- SEC companyfacts: https://data.sec.gov/api/xbrl/companyfacts/CIK0001341766.json
- 8-K cambio directivo 10-ago-2026: https://www.sec.gov/Archives/edgar/data/1341766/000119312526342430/d135466d8k.htm
- Resultados nuevos del emisor 2T2026: https://ir.celsiusholdingsinc.com/news/news-details/2026/Celsius-Holdings-Reports-Second-Quarter-2026-Financial-Results/default.aspx
- Damodaran prima octubre 2026: https://pages.stern.nyu.edu/adamodar/New_Home_Page/home.htm
- Precio obtenido de nuevo: cierre 27-oct-2026 USD28,00; https://stockanalysis.com/stocks/celh/history/ (confirmación cruzada MarketBeat/Investing).
No se reutilizaron parámetros ni textos de estudios anteriores de CELH.


## Continuación autorizada 28-oct-2026
El usuario autorizó ambas acciones. NO volver a solicitar estas mismas autorizaciones.
PREF-01 aplicado a la copia nueva y a Maestra/IA/Manual: 49 fórmulas existentes ajustadas y 96 celdas nuevas de puente/etiquetas. Se comprobaron 145 celdas en cada plantilla y se preservaron 61 pestañas y dimensiones.
54 aserciones nativas PASS en las tres historias ordinarias (con preferentes, sin preferentes y falta de información). Celdas temporales restauradas; fixtures retirados de la copia. No equivale a controles completos de publicación.
Respaldos nuevos intactos: Maestra 1Mf0UVGV3_xWnXTzOC4qpmXqTPSLtjjaaIcIlostwHBk; IA 1KIVD-elUrABeRS_Vfh0X7eTHhpjl_CWBLbmf98E6Hqw; Manual 1sYLe0ds_AShb0fsjzUxbx4dpx2xlGcL-nTN9kFijU0Q.
Motor commit 0824cee06fdb128e4ed38f0007569d5493aa694a contiene spec/regresión/registro. Reglas v13 en app commit 31f949c9fcad044ada3c63a73e035b6e9285d8d8.
PREF-01 separa NI común, FCFE menos pagos preferentes y puente patrimonial; NO resuelve aún valor de mercado/coste esperado de preferentes convertibles ni WACC.
Validación SEC directa adicional: 41 escrituras en fuente (39 + 2 WC comparativo), y 45 escrituras históricas en copia (39 + 6). Recompras FY2025 corregidas a -45,504 y LTM a -176,874 millones (retenciones + tesorería). Deuda pagada FY2025 -201,750 y LTM -205,250. Intangibles junio 2026 1.379,751; inversiones no cotizadas 17,0. Fuente sigue pendiente de validación completa.
Inventario Git local aislado: app 1.080 commits / 103 ramas / 124 refs PR; datos 1.245 commits / 97 ramas / 180 refs PR. Contenido objetivo detectado en 634 y 944 commits respectivamente. Inventarios NO modifican referencias. PR refs administradas por GitHub no son ramas normales. Clonación local del motor privado falla por falta de autenticación Git; conector sigue funcionando.
Se depuraron referencias colectivas residuales en nueve archivos compartidos de main de datos: siete Markdown/Python y dos JSON. Los recuentos afectados se ajustaron a siete empresas/28 historias; no se reutilizó su contenido para la valoración nueva. Catálogo editorial app main ya limpio; hallazgo adicional solo histórico.
