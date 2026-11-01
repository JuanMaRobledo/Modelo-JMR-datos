# MODELO JMR — DOCUMENTO DE CONTEXTO Y RELEVO PARA CLAUDE CODE

**Corte de contexto:** 1 de noviembre de 2026 (hora de Colombia).  
**Proyecto:** suite financiera del usuario, especialmente **Modelo JMR — valoración y análisis fundamental**.  
**Estado del documento:** relevo operativo basado en las verificaciones y operaciones relatadas en la sesión anterior. **No sustituye una nueva lectura de GitHub, Google Drive/Sheets, CI y producción.**

> **INSTRUCCIÓN INICIAL A CLAUDE CODE:** Continúa el trabajo existente desde el estado real. Primero verifica lo que está fusionado, lo que está en el catálogo, la ubicación de las hojas y los controles; luego completa ordenadamente la organización de valoraciones, archivos, pestañas y presentación. No comiences desde cero, no rehagas valoraciones correctas, no destruyas históricos, no declares «listo» algo que solo está intentado o en una rama. Trabaja en una sola pasada cuando sea viable, con avances y evidencia comprobable.

---

## 1. Qué estamos haciendo exactamente

Estamos cerrando la **depuración, estandarización y organización del Modelo JMR**, para tener una base técnica estable antes de continuar valorando activos. La prioridad inmediata **no** es rehacer todos los DCF, sino dejar perfectamente identificados:

1. La **única revisión activa por ticker** en el catálogo y la app, con su hoja oficial y sus informes de análisis.
2. El **historial anterior conservado** en `AAA Finanzas / Archivo / TICKER` y fuera del catálogo activo.
3. La **organización del repositorio, los prompts y la app**, sin rutas redundantes ni pantallas que no llevan a ningún lugar.
4. La **integridad de la plantilla/hojas**, con referencia de 46 pestañas para el modelo corporativo estándar y excepciones documentadas para motores especiales (por ejemplo, XP/FCFE).
5. Los **gates de CI y controles financieros**, sin rebajarlos para conseguir verde.
6. La **presentación completa** de valoración, análisis, múltiplos, escenarios, sensibilidades y estados financieros desde la ficha única de la empresa.

Una vez cerrada la organización y recuperadas las validaciones necesarias, continuar sistemáticamente las empresas pendientes con **Método JMR A-1.2** y publicación **`EN_REVISION`**, no como auditadas/certificadas.

## 2. Repositorios, infraestructura y PR relevantes

**Repositorios principales**

- App, navegación, UX, prompts y presentación: https://github.com/JuanMaRobledo/Modelo-JMR
- Datos, catálogo, JSON de valoraciones, informes, evidencia y controles: https://github.com/JuanMaRobledo/Modelo-JMR-datos
- Motor/plantillas/extractor financiero: https://github.com/JuanMaRobledo/JMR-valuation
- Despliegue: Vercel; verificar ambiente, commit desplegado y funcionamiento de producción antes de afirmar publicación efectiva.

**Hitos conocidos que hay que comprobar nuevamente contra GitHub:**

- **PR #151, Modelo-JMR:** reorganización de la app/ficha única y navegación. El usuario aprobó el diseño. Verificar estado de merge y que la producción usa ese commit; no asumir que un preview o diseño antiguo es la versión final. https://github.com/JuanMaRobledo/Modelo-JMR/pull/151
- **PR #181, JMR-valuation:** extractor candidato de matrices; en conversaciones anteriores se reportó fusionado. Verificar presencia real en `main`, integración con datos y app. https://github.com/JuanMaRobledo/JMR-valuation/pull/181
- **PR #211, Modelo-JMR-datos:** diagnóstico del gate de matrices. El 31-oct constaba abierto/en borrador: hojas SHAK/AFYA con matrices nativas, pero un registro activo sin 20 matrices exportadas y gate fallando por ausencia de matrices Base, no por el antiguo requisito erróneo de 21/28. **Este estado es histórico y podría haber cambiado.** https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/211
- **PR #216, Modelo-JMR-datos:** referencia a promoción XP A-1.2; verificar expediente/catálogo. https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/216
- **PR #218, Modelo-JMR-datos — FUSIONADO:** NVDA A-1.2 `NVDA-20261101-A12-R1` a `EN_REVISION`; histórico R4 conservado. https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/218
- **PR #219, Modelo-JMR-datos — FUSIONADO:** META A-1.2 `META-20261101-A12-R1` a `EN_REVISION`; histórico R5 conservado. https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/219
- **PR #220, Modelo-JMR-datos — FUSIONADO (1-nov-2026):** conciliación hoja↔JSON de 23 valoraciones y resolución de pesos/descuentos de **NKE, PYPL, EPAM, ZTS, NVO y ONON**. Merge `6b9252b30656edf99d956e7fcdac60840623a8ff`. https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/220

**Importante sobre el PR #220:** su descripción informa que los **26 pasos de tres workflows pasaron localmente** y que se preservaron DCF, MOS, historias, supuestos y matrices de las seis revisiones. **Eso no prueba por sí mismo que CI remoto, despliegue, app ni auditoría económica estén aprobados.** Revisar las ejecuciones reales. La conciliación encontró 12 registros inicialmente alineados, seis con pesos discordantes —abordados en ese PR—, anclas vinculadas al precio en UBER y GOOGL, pestañas/motores pendientes en INTU y NU, y limitaciones de acceso para revisar XP y CELH. Esas categorías no deben interpretarse como mutuamente excluyentes ni como 23 aprobaciones.

## 3. Inventario funcional: universo de 23 empresas

En el hito descrito por los PR #218–#220 había **23 valoraciones y 23 análisis activos**, sin ticker duplicado según los validadores locales. **Volver a extraer la lista directamente de `catalogo.json`** y contrastar los archivos que efectivamente referencia el catálogo. El universo de trabajo conocido es:

`META, NVDA, XP, SHAK, UBER, MELI, CELH, ADBE, BSX, CMG, NFLX, GOOGL, MSFT, NKE, PYPL, EPAM, ZTS, ONON, NU, NVO, INTU, AFYA, DUOL`.

No crear automáticamente nuevas revisiones ni sustituir archivos por similitud de nombre. Cada empresa debe tener un registro explícito con: ticker, `revisionId`, `version_metodo`, estado, precio/fecha de referencia, `sheet_id`, ruta de JSON, ruta de análisis, historial, controles y URL de consulta en la app.

### Expedientes que requieren atención especial

| Ticker | Estado conocido y asunto que debe preservarse o resolver | Referencia |
|---|---|---|
| **NVDA** | A-1.2 R1 activo `EN_REVISION`. DCF Base **US$205,95**; MOS35 **US$133,87**. Conservador 109,66; optimista 354,62; disrupción 50,08. R4 histórico fuera del catálogo. Cinco múltiplos prioritarios y matrices nativas. Pendientes: contraste guía de ingresos, beta/costo de deuda, AZ Stocks y QA económico/visual. | PR #218 |
| **META** | A-1.2 R1 activo `EN_REVISION`. DCF Base **US$737,51**; MOS35 **US$479,38**. Conservador 457,18; optimista 1.086,77; disrupción 232,18. Pasivo legal de US$19.881 millones deducido una vez; riesgos relevantes de compromisos/capex y diferencia DCF vs múltiplos. AZ Stocks pendiente. | PR #219 |
| **XP** | Modelo **FCFE** para financiera; hoja específica con 71 pestañas, incluidas matrices y soporte XP. No forzar la plantilla corporativa de 46 eliminando el motor FCFE. Verificar catálogo, informes y accesos. | PR #216 y hoja abajo |
| **ADBE** | Revisión A-1.2 A3 activa, hoja con **61 pestañas**, 15 sobre la referencia de 46; separar pestañas de soporte/auditoría del núcleo **solo después** de mapear dependencias. Mantener múltiplos y nivel 1/nivel 2. | Hoja abajo |
| **CELH** | A-1.2 `EN_REVISION`, DCF Base aprox. **US$34,85**, MOS35 aprox. **US$22,65**; hoja de 46 pestañas, históricos parciales. Acceso de cuenta de servicio reportado como insuficiente para auditar. Resolver permisos sin ampliar acceso indiscriminadamente. | Hoja abajo |
| **NKE, PYPL, EPAM, ZTS, NVO, ONON** | El PR #220 corrigió retención de pesos de hoja, descuentos nativos y nivel 2; verificar que la app consuma los JSON fusionados y que no queden etiquetas antiguas como `MULTIPLOS_INCOMPLETOS`. No recalcular DCF sin causa. | PR #220 |
| **UBER, GOOGL** | Revisar los **múltiplos con anclas derivadas del precio de mercado**: no tratarlos como comprobación fundamental independiente ni ponderarlos como si fueran certificados. | PR #220 |
| **GOOGL** | R5, DCF Base **US$287,20**, MOS35 **US$186,68**. Solo Base está homologada en R5; conservador, optimista y disrupción aún son referencias R4. No hacer un promedio mezclando revisiones. Sensibilidad CapEx/ROIC importante; revisar otros escenarios y múltiplos. | `GOOGL-20261029-R5.json` |
| **INTU** | A-1.2 `EN_REVISION`, DCF Base **US$506,85**, MOS35 aprox. **US$329,45**. El DCF se calculó en pestaña independiente; la salida Damodaran estándar no fue alimentada plenamente. Relativos provisionales con peso cero. Faltan grillas nativas completas, I+D y revisión económica. | `INTU-20261029-R1.json` |
| **NU** | Verificar motor y pestañas en `PENDIENTE`; no declarar matriz certificada por la simple existencia de JSON derivado. | PR #220 |
| **SHAK, AFYA** | Las hojas oficiales mostraban matrices Base nativas, pero el pipeline de exportación/gate de datos tuvo fallos. Revisar PR #211, extractor y resultado remoto vigente antes de concluir. | PR #211 |

Cifras expresadas en dólares **por acción** salvo donde se indiquen millones. Todas son **cifras de expedientes con fecha de corte**, NO cotizaciones en vivo ni auditorías económicas.

## 4. Organización de Google Drive y cambios efectuados en la sesión anterior

**Estructura objetivo**

```
AAA Finanzas/
  Análisis/
    <TICKER>/          # hoja o expediente JMR vigente
  Archivo/
    <TICKER>/          # hojas, valoraciones e informes anteriores; sin borrado
  AZ Stocks/           # valoraciones alternativas independientes
  Plantilla Original/  # fuente histórica preservada
  [Plantillas vigentes y otros recursos del proyecto]
```

**Carpetas compartidas de referencia:**

- Análisis: https://drive.google.com/drive/folders/1IVpgm89jA4BmYVc3HKSCQ1iec4fpYE25
- Archivo: https://drive.google.com/drive/folders/1BT0aiVXI4EIqWxhavWEr_a1wDPJcpDzK
- AZ Stocks: https://drive.google.com/drive/folders/1AM_CU-2xvol03G6yQz52W4YmOB9NmoH9

**Operaciones reportadas como exitosas en la sesión anterior:** archivadas **16 hojas históricas** (ADBE 8, NFLX 4, UBER 1, META 1, NVDA 1, NKE 1), y trasladadas **dos hojas alternativas de NKE a AZ Stocks**. Se crearon carpetas de archivo por ticker y se aplicaron movimientos por ID manteniendo los enlaces originales. Hubo reintentos en una operación de ADBE: **volver a consultar los `parent_ids` y comprobar inventario actual, sin contar acciones dos veces**. Se archivó una versión antigua adicional de ADBE dentro de la comprobación final; validar recuentos contra el contenido real y no solo contra los mensajes de ejecución.

**Carpetas de archivo creadas/empleadas:**

- ADBE: https://drive.google.com/drive/folders/1P3sF0SH3fa_uTaOugZ76eoCG7E4-t_IY
- NFLX: https://drive.google.com/drive/folders/12JKout3cj7MCbXkerSTDsESfpIHaQHh5
- UBER: https://drive.google.com/drive/folders/1MHs0TyUQuSm1XRhrU8J4NKfxt0HFIbbf
- META: https://drive.google.com/drive/folders/123mwUchljYfKQZDY3QQljJkIbfOCppsZ
- NVDA: https://drive.google.com/drive/folders/1Mqr_3qBmyv6lOsiMVwWBPjcmAazFBbyN
- NKE: https://drive.google.com/drive/folders/1alKKqDXVMyH_iWUtqD0vZS8PIxfFbAIp

**Hojas oficiales importantes** (corroborar cada una con el `sheet_id` del JSON activo):

- NVDA A-1.2: https://docs.google.com/spreadsheets/d/1gN_WFYyGzdLjgYr_0AEHGDdBIeCiNVnDFy0wkH0vB0Y/edit
- META A-1.2: https://docs.google.com/spreadsheets/d/1lpE-L0Ai2NrWDhzBhtdeOMASwo7XRleUEMEMl3K34ss/edit
- XP FCFE: https://docs.google.com/spreadsheets/d/1C8TU1AJMxy0JmU4KsBNdp1dYzBSoli7CLtnjQI3SsnQ/edit
- ADBE A3: https://docs.google.com/spreadsheets/d/1Di2o1dGk9HMH41oXiEgjvqUk1HI5_yRIogkrBrtjFqw/edit
- CELH A-1.2: https://docs.google.com/spreadsheets/d/1xqXfx9bD8XCGzgWtDnQP_9X0x_Cq94rID4w_w5mPyUo/edit
- NKE A-1.2: https://docs.google.com/spreadsheets/d/1-nmaTwO34GwoqqAE7ROZaO-2icKJKU70oXQAJ5QqFx0/edit
- UBER A-1.2: https://docs.google.com/spreadsheets/d/1T2GB36HCC415XIA0yjP6AITI8kwmfueEZBIFI-ZLdFE/edit

Se renombraron para indicar `EN_REVISION` las hojas **META**, **NVDA**, **XP** y **CELH**; esto cambia el **título en Drive**, **no certifica** que el catálogo, el cálculo, la app ni la producción se hayan actualizado como consecuencia del renombramiento.

### Regla de archivo

- **Mantener una sola revisión activa por ticker** para el usuario final.
- Conservar los históricos en Archivo y/o en Git; no borrarlos ni sobrescribirlos por defecto.
- Guardar el vínculo de versión anterior → versión vigente, fecha, motivo y revisión/commit.
- No mover una hoja oficial sin antes confirmar que la URL en el JSON del catálogo sigue apuntando a ella.
- No crear dos carpetas homónimas en diferentes rutas por confundir `Análisis` con `Archivo`.
- Usar IDs estables de Drive y verificar la carpeta padre **después** de cada lote de movimientos.

## 5. Integridad de las hojas: referencia de 46 pestañas, con excepciones

La plantilla maestra en blanco examinada tiene **46 pestañas**; CELH y NKE tienen 46. Diferencias conocidas:

| Hoja | Número reportado | Observación operativa |
|---|---:|---|
| Plantilla maestra | 46 | Referencia corporativa |
| CELH | 46 | Ya coincide |
| NKE | 46 | Ya coincide |
| META A-1.2 | 47 | Pestaña adicional `Ficha A-1.2 EN_REVISION`; mapear referencias antes de tocar |
| NVDA A-1.2 | 47 | Pestaña adicional de ficha; mapear referencias |
| ADBE A3 | 61 | Pestañas heredadas de Damodaran, controles y notas; preservar información útil |
| XP FCFE A-1.2 | 71 | Motor financiero específico, matrices y soporte XP; **excepción explícita** |

**NO aplicar «eliminar hasta que sean 46» como regla mecánica.** El objetivo es una estructura lógica, consistente y reproducible. Construir un manifiesto por hoja con nombre de pestaña, función, si contiene fórmulas, si otras pestañas la referencian, si la app/extractor la consulta y si pertenece al núcleo, a un anexo, a un motor especializado o a una auditoría. Preferir **ocultar, agrupar o separar en soporte/archivo respaldado** antes que eliminar. Una pestaña dedicada a auditoría económica puede corresponder a documento independiente, pero jamás eliminar su trazabilidad.

## 6. Contrato económico del Método JMR A-1.2

### Método principal y supuestos

- Principal para compañías no financieras: **DCF FCFF** a 10 años, basado en los principios de Aswath Damodaran; para financieras/bancos, emplear **FCFE** cuando sea el método económicamente apropiado (XP y casos pertinentes).
- Cuatro historias: **Base** como valoración central, **Conservadora**, **Optimista** y **Disrupción** separada; no confundir escenarios anteriores con los vigentes ni mezclar metodologías o cortes.
- Examinar explícitamente **crecimiento** (trayectoria anual), **margen EBIT**, **reinv​ersión**, **Sales-to-Capital** marginal, **ROIC** normalizado y terminal, **WACC/Ke**, crecimiento terminal, dilución, arrendamientos, I+D, CapEx y activos no operativos.
- La reinversión por `Δventas / Sales-to-Capital` es un **enfoque** para estimar capital incremental; si se modela inversión física por CapEx−D&A+ΔNWC e I+D capitalizable, **no sumarla otra vez** sobre el enfoque explícito. Caso crítico: GOOGL/IA.
- ROIC de capital histórico, ROIC marginal y ROIC terminal deben definirse y conciliarse; no presuponer que son idénticos.
- Priorizar supuestos razonables y sustentados; evitar conservadurismo excesivo y la calibración artificial para acercarse a cotización de mercado.

### Valoraciones por múltiplos

**Cinco prioritarios:** `EV/EBITDA`, `EV/FCFF`, `P/E`, `P/FCFE`, `P/OCF`.  
`P/S` (o `P/V`) y `P/BV` son **opcionales/no esenciales**: mostrar como referencia cuando tengan sentido, sin ponderarlos por obligación ni fabricar ceros ante datos ausentes.

- Diferenciar múltiplo histórico, forward, de salida y resultado descontado **a valor presente**.
- Mostrar supuestos de ancla y su procedencia. Marcar `PROVISIONAL` o `N/D` si es un proxy o depende del precio de mercado.
- Sensibilidades **5×5 nativas** para los múltiples prioritarios donde corresponda; comprobar valor central frente al valor de la pestaña fuente (y VP FY+3 cuando proceda).
- Sensibilidad DCF incluyendo WACC×g y, según expediente, ROIC, crecimiento, margen, CapEx y Sales-to-Capital. Las matrices deben reproducir el escenario Base.
- El DCF Base es **valor principal**. Si los múltiplos no están auditados, mantenerlos separados o con peso cero según expediente; no cambiar a un promedio arbitrario.

### Presentación del valor y MOS

Al principio de cada ficha, enseñar **precio de referencia con fecha**, **DCF Base por acción**, **precio máximo de compra con MOS 35%** (`Base × 0,65`), escenarios y **potencial** con denominadores consistentes. No etiquetar un cierre histórico como precio «actual» o «en vivo». Explicar si se usa valor presente o precio objetivo futuro, evitando mezclas.

## 7. Contrato de los análisis fundamentales y la app

**Nivel 1: análisis fundamental extenso.** Debe describir negocio, segmentos y economía unitaria, industria, posición competitiva, generación de efectivo, drivers, riesgos, administración y asignación de capital; diagnóstico específico del **ciclo de vida de la empresa según Damodaran** y del **ciclo macroeconómico/monetario/de crédito y sentimiento**, inspirándose analíticamente en Howard Marks; tesis y catalizadores; escenario Base y alternativos; riesgos de disrupción. El usuario prefiere un informe narrativo profundo y un índice lógico, no resúmenes de pocas líneas. Hay expedientes recientes con **14 capítulos de Nivel 1** y **12 apartados de Nivel 2**; preservar ese contenido mientras se estandariza la experiencia, sin reducirlo automáticamente por un número de secciones.

**Nivel 2: sustento técnico reproducible.** Datos históricos y fuente/fecha, normalizaciones, fórmulas **realmente utilizadas**, entradas/supuestos, proyecciones por año, conciliación de DCF, múltiplos y pesos, matrices y centros, escenarios y diferencias JMR vs método alternativo AZ Stocks. Mantenerlo **separado y navegable**, no llenar Nivel 1 de tablas sin explicación.

**App / UX:** una ficha única por ticker, accesible desde el análisis fundamental, con navegación interna real y sin pantallas duplicadas o rutas muertas. Reunir valoración y escenarios, análisis de dos niveles, estados financieros, supuestos/edición, múltiplos, sensibilidad y auditoría/observaciones. Incluir modo **visor** y **edición**; acceso a la hoja fuente para editar datos y estados financieros. Índice único y funcional, pestañas agrupadas, enlaces «ver cálculo» que abran la evidencia correcta, logo, tarjeta inicial de precio/valor/MOS. Respetar el diseño recientemente aprobado, **sin rediseñar otra vez la aplicación desde cero**.

## 8. Secuencia exacta de continuación (priorizada)

### Fase A — Inspección inicial (solo lectura)

1. Leer últimos commits de `main`, PR abiertos/cerrados, releases y ejecuciones CI en los tres repositorios; revisar específicamente #151, #181, #211, #216, #218, #219 y #220. Identificar commit desplegado en Vercel.
2. Validar contenido real de `catalogo.json`, 23 JSON activos y 23 informes correspondientes. Construir tabla `ticker | revisión activa | sheet_id | estado | DCF | MOS | múltiplos | matrices | Nivel 1 | Nivel 2 | URL app | salvedad`.
3. Inventariar **Análisis, Archivo, AZ Stocks**; verificar padre real de cada archivo movido, duplicados, archivos sin clasificar y enlaces rotos. Contrastar con los 16 archivados reportados; contar una sola vez cada ID.
4. Leer nombres y referencias de pestañas de las hojas que no tienen 46 (ADBE, META, NVDA, XP), y registrar dependencias antes de ninguna depuración.
5. Obtener el estado **remoto**, no solo local, del gate de matrices/exportación y del workflow `Control JMR de ponderaciones`; estudiar logs, sin relajar aserciones.

### Fase B — Limpieza y organización de Drive

6. Resolver primero el inventario de las 23 empresas; identificar hoja oficial y archivos anteriores por ID y fecha. Archivar versiones antiguas verificadas en `Archivo/TICKER`. Separar AZ Stocks, plantillas originales y pruebas temporales, sin pérdida de histórico. Aplicar cambios en lotes pequeños e idempotentes; verificar `parent_ids` tras cada lote.
7. Si faltan permisos para auditar XP o CELH mediante cuenta de servicio, reportar la **cuenta concreta, alcance mínimo y acción necesaria**. No publicar documentos con acceso de edición abierto para solucionarlo.
8. Corregir nombres ambiguos (`NO PUBLICAR`, `EN PREPARACION`, etc.) **solo cuando** el estado operativo y de catálogo esté probado. El nombre no reemplaza los controles de publicación.

### Fase C — Estandarización técnica de hojas y datos

9. Definir manifiesto de pestañas: 46 como núcleo empresarial, excepciones documentadas. No borrar módulos XP o fórmulas activas. Priorizar mejoras reversibles y respaldadas.
10. Revisar exportador `JMR-valuation` → JSON en `Modelo-JMR-datos`, en especial matrices Base 5×5, revisiones y SHA/origen. Resolver el cambio mínimo para el gate sin tocar escenarios/cálculos establecidos.
11. Validar que el PR #220 no introdujo regresiones: pesos nativos de las seis empresas, cinco múltiplos, narrativa Nivel 2, no regresión de DCF/MOS, enlaces y compatibilidad de app.
12. Resolver anomalías reales de etiquetas/estados: por ejemplo JSON principal con múltiplos `null` y sección secundaria ya integrada, si la aplicación muestra contradicciones. No inventar cálculos ni homologar proxies como certificados.

### Fase D — App y aceptación

13. Abrir fichas de empresas representativas: **META, NVDA, XP, ADBE, NKE, GOOGL, INTU y SHAK**. Comprobar navegación, estados financieros, editar/visor, Nivel 1, Nivel 2, múltiplos, escenarios, sensibilidades y enlaces a hojas.
14. Comparar los valores mostrados con los JSON activos y las hojas. Verificar de manera explícita **Base, MOS35, fecha de precio, etiquetas `EN_REVISION`, revisiones y matrices**.
15. Ejecutar CI remoto y validar despliegue real en Vercel; distinguir «PR fusionado», «tests locales pasaron», «CI remoto pasó» y «producción verificada» como estados diferentes.

### Fase E — Siguiente ciclo de valoraciones

16. Solo con el flujo estable, priorizar salvedades económicas y análisis incompletos en los 23 expedientes. Continuar A-1.2 sin comenzar de cero, sin ajustar valores que ya estén razonablemente sustentados y con AZ Stocks como contraste **independiente y no mezclado**.
17. Publicar nuevas revisiones como `EN_REVISION` cuando los controles técnicos permitan mostrarlas; mantener auditoría visual y auditoría económica como pasos posteriores separados.

## 9. Criterios de aceptación — cuándo puedes informar «terminado»

- Inventario completo y trazable de los **23 tickers**: revisión única en catálogo, JSON y análisis correspondiente, hoja oficial accesible, enlace válido y archivo anterior preservado.
- Archivos de Drive realmente en las carpetas correctas y contabilizados por ID; sin pérdidas, sin reemplazar ni sobrescribir fórmulas.
- Hojas con estructura coherente; **excepciones técnicas explicadas** y ninguna dependencia eliminada solo para forzar 46 pestañas.
- Los 5 múltiplos prioritarios, sensibilidades y supuestos visibles donde corresponda; faltantes marcados honestamente `PENDIENTE`, `PROVISIONAL` o `N/D`.
- Gate financiero/CI remoto validado con enlaces a ejecución y estado; ningún control relajado para ponerlo verde.
- App probada para fichas representativas en **producción** (no solamente en un preview) con niveles de análisis, pestañas, edición/visor y enlaces funcionales.
- Documento de cambios con **antes/después, IDs/commits/PR/ejecuciones, tests, bloqueos pendientes y siguiente paso**. No declarar auditoría económica sin realizarla.

## 10. Reglas operativas y formato de avances

1. **Continuidad y criterio:** no reiniciar, no duplicar; preferir terminar el trabajo existente. Usar criterio de ingeniería y análisis financiero; evitar preguntas que puedan resolverse investigando.
2. **Cambios mínimos y reversibles:** respaldar, hacer commit/PR claro, correr tests; no cambiar DCF, precio MOS, fórmulas, estados ni metodología sin detectar un error material y documentarlo.
3. **Publicación prudente:** `EN_REVISION` no significa `AUDITADO`. No afirmar publicación en producción sin comprobar desplegado, rutas y contenido.
4. **Trabajo por etapas pero en una sola pasada cuando sea posible.** Informar al usuario cada avance sustantivo: qué encontraste, qué modificaste, qué probaste y qué falta. Evitar «ya está» sin evidencia.
5. **No modificar permisos amplios** ni eliminar históricas por comodidad. Resolver primero acceso mínimo y confirmar contexto propietario.
6. **Para los resúmenes financieros del usuario, separar tres productos**: Valoración — Modelo JMR; Cartera; Presupuesto. Esta tarea se limita al primero salvo que descubras una regresión transversal.

**Formato solicitado de cierre:**

| Bloque | Estado: confirmado / parcial / bloqueado | Evidencia verificable | Pendiente / siguiente acción |
|---|---|---|---|
| GitHub y PR | ... | URL y SHA | ... |
| Catálogo (23) | ... | commit + validadores | ... |
| Google Drive / Archivo | ... | IDs + carpeta padre | ... |
| Hojas y matrices | ... | sheet_id + rangos | ... |
| App / Vercel | ... | URL + despliegue | ... |
| Calidad económica | ... | excepciones por empresa | ... |

## 11. Instrucción de ejecución inmediata para Claude

**Empieza ahora por la Fase A y sigue en el orden indicado.** Prioriza terminar el inventario/archivo y validar las 23 revisiones antes de hacer otra valoración. No te detengas simplemente en el diagnóstico: ejecuta las correcciones de bajo riesgo y verificables que estén dentro de tus permisos, abre PR cuando haya cambios de código o datos, y ejecuta pruebas. Si algún paso exige una autorización o acceso que no tienes, deja un bloqueo explícito con la operación exacta requerida y continúa con lo que no esté bloqueado. No promuevas resultados provisionales a auditados ni modifiques modelos financieros para satisfacer tests. **La meta es dejar el Modelo JMR ordenado, consistente, usable y listo para continuar el trabajo de valoración.**

---

*Documento de traspaso preparado a partir de la sesión anterior del 1-nov-2026. Los links, cifras y conteos indican el último estado conocido, no una certificación independiente del instante en que Claude lo lea.*
