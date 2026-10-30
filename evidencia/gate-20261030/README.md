# Revisión del gate JMR — 30 de octubre de 2026

Estado: BLOQUEADO para certificación/publicación mediante este gate. Propuesta en rama de revisión, sin modificar catálogo, análisis, valoraciones, hojas o auditorías financieras; sin merge ni despliegue.

## Alcance y evidencia
Repositorio JuanMaRobledo/Modelo-JMR-datos. Base inspeccionada: `0fc2d42ff42d32b876093378261542c10bc161db`.
Ventana 29-oct-2026 America/Bogota: 05:00 UTC del 29 a 04:59:59 UTC del 30.
Se consultaron las 83 ejecuciones de todos los workflows de esa ventana: 70 pertenecen a Control JMR de ponderaciones. Se leyeron los jobs y logs de las 70: todas fallaron en validar_catalogo.cjs, tras checkout y setup-node satisfactorios. Los cuatro pasos posteriores quedaron skipped.
Inventario reproducible: [runs.json](./runs.json), con IDs, SHA, errores y URLs de cada job.

- 61 ejecuciones: deepStrictEqual, actual undefined frente al objeto descuentoMultiples de MELI A3 (DCF Base 2029.8741378091252). Primer fallo observable; no diagnóstico exhaustivo de todas las empresas.
- 9 ejecuciones: Análisis sin valoración. La falta del enlace sourcePath ya impide seguir.
- Ejemplo inicial: https://github.com/JuanMaRobledo/Modelo-JMR-datos/actions/runs/40824554063/job/123284470992
- Ejemplo PR: https://github.com/JuanMaRobledo/Modelo-JMR-datos/actions/runs/40949479904/job/123713476282
- Último del día local: https://github.com/JuanMaRobledo/Modelo-JMR-datos/actions/runs/40993793706/job/123862114331

## Clasificación
**Infraestructura:** no es la causa observada en esas 70 ejecuciones. Runner, checkout y Node completaron. Las advertencias de deprecación no son el error fatal.
**Catálogo/contrato de datos:** causa demostrada. Hay datos serializados y enlaces incompletos respecto al contrato vigente del verificador.
**Fórmulas:** esos logs no las validan ni demuestran que estén mal; los pasos posteriores no corrieron.
**Código de selección:** verificar_cierre_multiplos.py seleccionaba el primer glob por ticker, incluyendo revisiones históricas excluidas del catálogo. Se corrige para seguir exclusivamente la lista activa y rechazar duplicados, enlaces o revisiones discordantes.

## Estado actual en la base inspeccionada
La versión actual añadió otro primer bloqueo: META contiene 13 capítulos y el validador exige 18. No se cambia esa regla silenciosamente.
- Enlaces sourcePath ausentes/no activos: DUOL, CELH, GOOGL y AFYA.
- Snapshot descuentoMultiples ausente en el enlace, presente en la valoración: MELI, ADBE, BSX, CMG, NFLX, MSFT, NKE, PYPL, EPAM, ZTS, ONON y NU.
- 19 análisis tienen 13 h2; DUOL tiene 19; XP, SHAK y UBER tienen 18. Conteo es diagnóstico estructural, no evaluación de calidad.
- 23 valoraciones activas frente a 17 auditorías narrativas declaradas. Faltan CELH, GOOGL, ZTS, NU, INTU y AFYA para el contrato actual. No se fabrican auditorías para completar ese conteo.
- validateRecord, ejecutado por separado para cada registro: pasan META, NVDA, XP, DUOL, SHAK y UBER. Los otros 17 fallan en el contrato de sensibilidad de múltiplos. Esto acredita únicamente ese control técnico, no validación integral, actualidad ni aprobación económica.
- Cierre activo NKE: falta cierreMultiplos.evidencePath; tras corregir selección se informa explícitamente NKE-20261029-R1. No se toma evidencia de una revisión antigua.
- Los tests Node dependen del catálogo de producción y parte de sus casos negativos quedan enmascarados por fallos anteriores. Un test negativo que pasa no certifica el caso positivo.

## Cambio mínimo propuesto
1. Resolver pareja valoración/análisis desde catálogo activo y exigir enlace y revisión coincidentes. Sin fallback a históricos.
2. Agregar contexto de archivo a los dos errores originales del catálogo.
3. Ejecutar los controles independientes aunque falle uno previo, siempre que Node se haya preparado y la ejecución no esté cancelada. Se conserva el job fallido; no se añade continue-on-error ni se omite un requisito.
4. Cinco tests aislados de selección: activo frente a histórico, ausencia, duplicado, enlace incorrecto y revisión discordante.

## Validación realizada
Entorno local Node 24.22.1 y Python 3.12; CI configura Node 22. La réplica local contiene los archivos activos y dependencias de pruebas descargados por SHA, no un checkout completo de históricos.
- Cinco tests nuevos: PASS.
- Cuatro tests existentes del snapshot histórico NFLX 20261025: PASS. Reproducen 63 precios/descuentos y rechazan alteraciones de resultado, hash y revisión. Eso NO valida NFLX A2 activo.
- Suite Python combinada: 9/9 PASS.
- Gate completo: NO verde. Catálogo e integridad siguen fallando justificadamente.
- No se han leído ni escrito hojas en esta revisión. Ninguna valoración o resultado financiero se publica.

## Condiciones para recuperar el gate verde
Reconciliar el contrato editorial vigente y sus validadores; completar enlaces y snapshots de la misma revisión sin recalcular precios; resolver con evidencia el contrato de múltiplos de cada revisión nueva; separar formalmente estados EN_REVISION de certificación económica si la política actual permite publicación preliminar sin auditoría. No eliminar requisitos ni inventar evidencias.
Después ejecutar todos los controles sobre el mismo SHA y verificar resultados CI. Hasta entonces, ni los correos ni este parche habilitan publicación por el gate. El cambio propuesto recupera diagnóstico y selección determinista, no certificación financiera.
