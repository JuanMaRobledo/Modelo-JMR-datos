# Depuración y estandarización — 31 de octubre de 2026

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
