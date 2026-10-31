# Depuración y estandarización — 31 de octubre de 2026

## Seguimiento posterior — NI/FCFE NU y anclas UBER/GOOGL

**Cambios efectivos de esta pasada, sin publicación:**
- **NU `NU-20261029-R1`:** se comprobó por conector la matriz nativa FCFE bancario Ke/g (25 valores y 25 fórmulas), ya existente en `sensibilidadDCF`; las 25 coincidencias con JSON y el centro US$18,32707520946464/acción aprobaron en GitHub Actions. Evidencia: `evidencia/nu-fcfe-bancario-20261031/NU-20261029-R1-sensibilidad-25-formulas.json`. NO cuenta como matriz relativa industrial ni completa P/E, P/FCFE y P/BV.
- **Corrección de Nivel 2 NU:** la narración antigua tenía capital retenido Y1 US$1178,754m y FCFE Y1 US$3221,915m, distintos a las fórmulas de `FCFE bancario A`. Se sustituyeron únicamente por **US$1636,799m** y **US$3052,439m**; se añadió la tabla de capital requerido/FCFE y matriz Ke/g con 25 celdas fuente y leyenda metodológica. Respaldos en `evidencia/nu-fcfe-bancario-20261031/NU-20261029-R1-analisis_antes.json`. Solo cambió `html` y `calculationHtml`, no `articleHtml`, el DCF ni los supuestos.
- **Pruebas de NU:** `nu_fcfe_bank_25_formulas.test.cjs` y `nu_n2_reconciliation.test.cjs` pasaron; controles editoriales y no regresión también pasaron en el SHA `01a80bde1efc650aa4f293edba7cf17bf326d848`. El gate general **sigue rojo por UBER**, no por estas correcciones.
- **UBER/GOOGL:** guardada lectura acotada de las celdas de ancla `J19` y dos celdas históricas `D8:E8` por método, sin modificar hojas. En las cinco hojas principales consultadas, las 10 parejas de datos históricos no incluyen valores positivos utilizables. **UBER:** EV/EBITDA y P/E dependen del precio observado; EV/FCFF, P/FCFE y P/OCF dependen de otra ancla. **GOOGL:** EV/EBITDA tiene ancla fija 15,6x; P/E deriva de una fórmula que incorpora precio observado y ajustes; EV/FCFF, P/FCFE y P/OCF dependen de otra ancla. Esto **no demuestra** ausencia de toda la historia contable; sí demuestra que esas celdas y fórmulas no constituyen cinco validaciones independientes. Evidencia `evidencia/diagnostico-anclas-uber-googl-20261031.json`.
- **Matriz financiera global:** continúa **16/20**, pendientes UBER, GOOGL, INTU y NU. Las siete integraciones de descuentos anteriores se mantienen en **1 completa (MSFT)** y seis con divergencias o pesos faltantes (EPAM, NKE, NVO, ONON, PYPL, ZTS). No se alteraron ponderaciones para forzar la conciliación.
- **Sin publicación:** app #151 y datos #211 siguen draft; QA autenticado y visual sin cierre. Se mantiene el paso de revisión visual previo a auditoría económica independiente.

**Próxima acción protegida:** validar anclas independientes y reglas de ponderaciones en UBER/GOOGL; resolver contrato de P/E, P/FCFE y P/BV bancario de NU y el flujo nativo de INTU. Solo importar a la ficha cuando la revisión, fuente y semántica sean idénticas. No rebajar gates.


## Estado vigente — integración protegida SHAK/MELI

- **Matrices Base oficiales en rama de revisión:** **16/20** expedientes Método A-1.2 (14 previos + **SHAK y MELI**). No confundir `INTEGRADO_EN_REVISION` con auditoría económica, aprobación o publicación en producción.
- **SHAK `SHAK-20261029-A12-R2`:** foto de 30 rangos financieros y 125 fórmulas 5×5 contrastadas con Google Sheets, hash SHA256 reproducido por Python y test de integración dry-run aprobado. Cinco métodos con matriz `OK`; EV/FCFF y P/FCFE son `N/A` por flujos FY+3 negativos con peso cero, preservando el `N/D` literal de la hoja. El único campo JSON agregado/modificado fue `sensibilidadMultiples`. DCF Base **US$35,4898699647347**, MOS **US$23,068415477077558** sin cambio. Copia previa exacta: `evidencia/captura-completa-candidata-20261031/SHAK-20261029-A12-R2/registro_antes.json`.
- **MELI `MELI-20261028-A3`:** recuperación de cinco métodos de `Descuento de múltiplos` para Conservador, Base y Optimista, 15 filas con fórmulas originales; foto integral de los 30 rangos, sensibilidades y fórmula fuente validada mediante Python. Cinco matrices `OK`; EV/FCFF y P/FCFE `N/A` justificado por flujos negativos y peso cero. Solo se añadieron/actualizaron `descuentoMultiples` y `sensibilidadMultiples`, con DCF Base **US$2029,8741378091252**, MOS **US$1319,4181895759314**, ponderaciones y escenarios intactos. Copias previas separadas en `evidencia/descuentos-candidatos-20261031` y `evidencia/captura-completa-candidata-20261031/MELI-20261028-A3`.
- **Pruebas:** `validar_no_regresion_20.cjs` verificó los veinte expedientes y al menos 16 respaldos financieros sin cambios fuera de descuentos/matrices. Los tests específicos de SHA, formulación, integración y tres escenarios de SHAK/MELI aprobaron en el commit `2e50c9bdacbc3eba72de9910e697a3d7c1f4393c`. Los dos workflows editoriales aprobaron.
- **Primer bloqueo real del gate global:** ahora `UBER`, con **0 matrices Base verificadas en JSON y anclas nativas faltantes**. No reducir requisitos ni publicar supuestos ficticios. Las otras revisiones con matrices Base ausentes son GOOGL, INTU y NU (banca, tratamiento FCFE específico). Subsisten siete descuentos secundarios incompletos y el QA autenticado de #151.
- **Entornos:** no se han escrito celdas en Sheets ni cambiado producción; #151 y #211 siguen en borrador sin fusionar. El proyecto Vercel Preview READY no acredita QA visual autenticado: último acceso automatizado bloqueado en redirección 401.
- **Nota histórica:** las secciones anteriores de este documento describen estados intermedios en los que SHAK y MELI aún no estaban integrados. Su referencia de bloqueo fue superada en esta rama; no se eliminaron para conservar trazabilidad.


## Cierre editorial de profundidad y prioridad N2

- Se profundizaron sin alterar valoraciones, supuestos ni `calculationHtml` los catorce capítulos del Nivel 1 de SHAK, UBER, AFYA y DUOL. El workflow `Método A · profundidad editorial` del SHA `c3072fc94708a415ad8fa5826677b034d1668b12` terminó **success**: SHAK **8.034**, UBER **8.218**, AFYA **8.146**, DUOL **8.502** palabras. El workflow paralelo de validación editorial también terminó **success**. Los 20 expedientes cumplen así el umbral de longitud, pero aún hay salvedades por investigación y fuentes; no confundir extensión con dictamen de calidad.
- Los 20 expedientes mantienen `calculationHtml` y enlace a su N1 en el HTML integrado. La cobertura es heterogénea: ver [PRIORIZACION_NIVEL2_20261031.md](PRIORIZACION_NIVEL2_20261031.md) con tamaños, tablas y prioridades para conciliación. **No se han certificado todos los N2** solo por la presencia de sus apartados.
- En el Nivel 2 de INTU se corrigió el rótulo engañoso «seis matrices Base validadas» por un aviso de **contrastes exploratorios sin integración en el JSON oficial**. No se modificaron precios, cifras, fórmulas ni escenarios.
- El control financiero `Control JMR de ponderaciones` sigue fallando en SHAK por ausencia de matrices Base 5×5 oficiales; el resultado editorial verde no lo desactiva. La autenticación Preview y su QA visual real siguen pendientes pese a disponer de despliegue READY.

**Próxima secuencia obligatoria:** completar fuentes y métodos faltantes de SHAK, MELI, GOOGL, UBER, INTU y NU; después descuentos/ponderaciones incompletos de siete revisiones; verificar de manera reproducible todos los N2; cerrar acceso y QA de #151. Mantener PR #151 y #211 en borrador hasta superar sus gates; no fusionar ni publicar producción.


## Actualización de ejecución — integridad N/D y acceso de Preview

- En Vercel se registró `APP_PASSWORD` **solo para Preview y para la rama de #151**, como secreto nuevo distinto de producción. Se redesplegó el SHA `a8705030` a `dpl_7PRMENiSueeUXp5QQZEGHWAReGqj`; el estado de build es `READY`. Las peticiones automatizadas a la página protegida terminan en autenticación 401 tras redirección; **no hay todavía QA visual autenticado ni prueba funcional 200**. El problema de acceso no puede considerarse cerrado.
- La app #151 sigue obteniendo `Modelo-JMR-datos/main` para vistas de expediente y lectores heredados, mientras las matrices están en la rama del PR #211. No tratar un Preview que solo carga `main` como prueba de la integración nueva.
- Se contrastó `Sensibilidad por múltiplo!A76:I144` directamente en las hojas originales de SHAK y AFYA: SHAK conserva `N/D` en EV/FCFF y P/FCFE; AFYA mantiene siete bloques `OK`. En SHAK los flujos FY+3 y VP3 correspondientes son negativos y los pesos relativos de ambos métodos son cero en la revisión activa.
- Se fortalecieron `scripts/integrar_matrices_nativas.py` y `scripts/validar_catalogo.cjs`: el valor literal de origen permanece `N/D`; una clasificación económica `N/A` solo puede surgir con evidencia de la misma revisión sobre flujos FY+3 negativos, VP3 negativos, declaración previa y peso cero. No se fabrican grillas, ni se modifica Sheets, DCF, supuestos o precios.
- En CI, las suites Node de matrices y Python del integrador pasaron; el gate global sigue fallando **correctamente** en SHAK (cero matrices importadas en JSON). El control de profundidad sigue fallando en SHAK, UBER, AFYA y DUOL.
- Los cuatro inventarios técnicos con fecha 30-oct se marcaron como fotografías históricas con referencia al informe vigente, para evitar reabrir tareas ya cubiertas. Se preservan fuentes y evidencias originales.

**Sin autorización de cierre:** #151 y #211 continúan en borrador. Siguientes dependencias: foto completa y conciliación hoja→JSON de SHAK/MELI/GOOGL/UBER/INTU/NU, descuentos relativos incompletos de siete empresas, acceso SSO y QA visual real, y profundización editorial. No fusionar ni publicar por esta actualización.


Estado: **avance de revisión, sin cierre ni publicación en producción**.

## Cambios comprobados

- Los 20 análisis A-1.2 tienen 14 capítulos numerados, un índice N1 enlazado y capítulo 5 propio de ciclos. Se conservan los párrafos anteriores y las anclas históricas; se retira el índice textual redundante de UBER. No se reduce la profundidad de los estudios largos.
- SHAK, UBER, AFYA y DUOL reciben explicación específica en sus 14 capítulos sobre negocio, crecimiento, competencia, ciclos, calidad de resultados, reinversión, ROIC, asignación de capital, escenarios y limitaciones. No se modifican sus hipótesis ni probabilidades.
- Esos cuatro N1 aún no superan el mínimo editorial vigente de 7.500 palabras: SHAK 3.714, UBER 4.686, AFYA 4.626 y DUOL 4.612. No se rebaja el umbral para obtener aprobación ni se considera resuelta su profundidad.
- AFYA y DUOL tienen N2 de 12 apartados con estados, ratios de la fotografía, ajustes, supuestos, costo de capital, cuatro proyecciones, puente al patrimonio, escenarios, múltiplos, sensibilidades y fórmulas leídas. Las notas cuantitativas previas se conservan como soporte complementario. El DCF Base se vuelve a leer y sus celdas no vacías coinciden con la fotografía anterior; no se reauditan por ello todos los históricos.
- Se importan tablas nativas FY+1/FY+2/FY+3, VP1/VP2/VP3 y consolidado de cinco métodos en 14 revisiones. En cada empresa los centros Base concilian con las matrices ya integradas. Se conservan fotografías de valores y fórmulas en `evidencia/descuentos-20261031/`.
- En las 20 valoraciones todos los campos ajenos a `descuentoMultiples` permanecen idénticos. Base, precio, MOS, escenarios, hipótesis, catálogo y matrices no cambian.

## Resultado de la importación de descuentos

| Situación | Empresas | Alcance |
|---|---|---|
| Tres escenarios y consolidación nativos conciliados | ADBE, AFYA, BSX, CELH, CMG, DUOL, NFLX | Se incorporan resultados existentes, conservando precisión de resúmenes previos. No certifica anclas económicas. |
| Solo Base disponible; faltan escenarios y/o pesos nativos | EPAM, MSFT, NKE, NVO, ONON, PYPL, ZTS | Conservador y Optimista quedan `null`, sin imputar cero. Se marca consolidación pendiente. |

MSFT tiene ponderaciones, pero carece de resultados relativos conservadores y optimistas. En las otras seis también falta el peso DCF y los pesos de métodos están en cero. El cero que aparece en un consolidado sin alimentación no se presenta como valor económico.

## App y acceso

El preview del commit `a8705030e5a6551d5b8f5e3b93408c092624e7b3`, deployment `dpl_F1qmoSeqrxLaCpHP7nRJPs7zFVqG`, continúa READY pero `/expediente.html?ticker=AFYA` devuelve HTTP 503 y «El acceso privado todavía no está configurado».

Se contrastó `proxy.js`: devuelve ese resultado cuando falta `APP_PASSWORD`. La metadata de configuración confirma que esa variable se aplica solo a producción. No se leyó su valor, no se copió a preview y no se alteraron controles de acceso. La vista previa necesita configuración de acceso propia antes de QA visual autenticado; READY no acredita funcionamiento.

## Pruebas de esta continuación

- 12 pruebas Python de índices, identidad, reproducción, estados pendientes y rechazo de cambios indebidos: aprobadas localmente.
- 5 pruebas Node del contrato de matrices: aprobadas localmente.
- Protección de datos: 20/20 valoraciones idénticas fuera de descuentos; 20/20 nuevos destinos N1/N2 sin duplicados.
- Control editorial: ejecutado sobre las 20 empresas. Falla en las cuatro extensiones insuficientes señaladas arriba; los otros 16 conservan avisos por capítulos que aún requieren investigación.
- Se incorpora la nueva suite Python al workflow antes del gate de catálogo. El primer CI detectó selección accidental de un histórico de AFYA en las pruebas y en el punto de entrada de restauración; se corrigió usando exclusivamente las rutas activas del catálogo y se añadieron dos regresiones de identidad.
- El gate financiero global no se da por recuperado. SHAK, MELI, GOOGL, UBER, INTU y NU conservan sus dependencias previamente identificadas.

## Pendientes concretos

1. Completar investigación específica de los cuatro informes cortos y los apartados pendientes de los otros 16; no inflar texto para satisfacer el contador.
2. Completar resultados relativos conservadores/optimistas y ponderaciones desde sus fuentes en las siete hojas señaladas; no recalibrar supuestos durante la limpieza.
3. Resolver anclas/enlaces de GOOGL, UBER e INTU; justificar y conciliar N/A por flujos negativos de SHAK/MELI; aplicar contrato bancario propio a NU.
4. Configurar acceso de preview y realizar QA real móvil/escritorio de las siete pestañas y sus subpaneles en ADBE, DUOL, UBER, NVO y AFYA.
5. Confirmar identidad y referencias de históricos antes de mover duplicados; META, NVDA y XP siguen como migraciones posteriores. No se borran datos por nombre de archivo.
6. Solo tras controles y QA necesarios: fusión, despliegue y comprobación de producción. La auditoría económica independiente sigue después de la revisión visual del usuario.

No constituye informe final de cierre. Las nuevas evidencias y los scripts se conservan en la rama del PR #211.
