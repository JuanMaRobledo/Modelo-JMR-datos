# F4 · UBER-FLOYD-3T26 · CANDIDATO

- Corte contable 30-sep-2026. Cierre de mercado US$68,59, 6-nov-2026.
- Valoración: https://docs.google.com/spreadsheets/d/1jMzDqRnTiBdbeFJmB0UH4aLdthBtC1JtiRhl8PEQBcg/edit
- Análisis: https://docs.google.com/document/d/1KGzxUKOCrpyqG0cgo84eTC9lFMPN_D_1VZS87QMK2mE/edit
- Históricos: https://docs.google.com/spreadsheets/d/1m19UGgqKLS5dhkBjABTxh8fyzD3vrxXAqsefq9OXn24/edit
- AISLAMIENTO=OK para esta exportación: mismo ticker, revisión y sheet_id en los dos JSON. El catálogo principal conserva la revisión activa anterior.

## Controles comprobados

1. Paridad DCF inverso con B35: 100,19381867706664 USD/acción. Las tres soluciones reproducen 68,59 a precisión numérica.
2. Escenarios: Conservadora 48,64133539, Base 100,19381868, Optimista 145,0858766. Probabilidades 25 %, 50 %, 25 %. Promedio 98,52871233. MOS 35 %: 65,12598214.
3. Tres matrices DCF de 5 × 5 con centro igual al Base. Cinco matrices de múltiplos de 5 × 5 con centro igual al VP3 de cada método. Normalización DCF probada usando la función vigente de `docs/expediente.js` en Node. Esta prueba no sustituye la ficha completa en el visor.
4. Huella nativa reportada: 0 diferencias de 1.883 fórmulas. El JSON y el análisis coinciden en revisión, hoja, Base y MOS.
5. SHA-256 de las exportaciones:
- `162e5c9fcdd0843dc790e03528e27b37fd3b33609a393dfe2f8706f58a5ff1c2  valoracion.json`
- `7fc2d5c871daa53992205bdb3cab940c2108172c8799e6fa3e79d581475f2514  analisis.json`

## Puertas pendientes o fallidas

- FALLA reproducida al ejecutar `offline` de `JMR-valuation/scripts/consistencia_migracion.py` sobre los dos JSON: `{'M1': False, 'M2': False, 'M3': False}`. M1 y M3 aún exigen Disrupción separada y métodos opcionales P/V y P/BV. M2 usa identificadores A/B/D para el promedio y no reconoce el tercer escenario Floyd (C). El promedio y el MOS sí pasan la comprobación numérica independiente.
- NO EJECUTADO como gate aprobatorio: batería completa con ruta Floyd para probabilidades, historia a números e integridad, conciliación completa en visor/preview y CI de promoción. El módulo de múltiplos del visor oculta candidatos sin validación de publicación. No habilitarlo con indicadores ficticios.
- PARCIAL: actualización del artículo y anexo. El análisis conserva apartados pendientes en industria/TAM, macro/mercado y gobierno. Revisión económica independiente F5 pendiente.
- Conclusión: CANDIDATO. Adaptar y probar el contrato de publicación Floyd, completar el cierre editorial y verificar la ficha en preview antes de reemplazar el catálogo.

PASOS F4: 3/5 de esta entrega ejecutados (reconciliación de valores, actualización parcial del análisis, exportación y prueba local). Integración de producción y publicación pendientes. Herramientas: conector Sheets/Docs, Node 24 y Python 3.12, ChatGPT Work.

## Continuidad verificada · 8-nov-2026 · implementación Floyd

**Aplicación:** `JuanMaRobledo/Modelo-JMR#188` fue fusionado (commit `190d25f`). Corrige la interpretación de escenarios: Floyd C=Optimista; las revisiones A-1.2 conservan C=Disrupción/D=Optimista. Las pruebas de la app reportaron 8 workflows exitosos y Vercel mostró despliegue de producción READY con el commit fusionado. Esto **solo actualiza el visor**, no el registro oficial de UBER.

**Motor:** `JuanMaRobledo/JMR-valuation#212` es un borrador sin fusionar. Incorpora ruta Floyd en `consistencia_migracion.py` (M1 para tres historias y 3+5 matrices, M2 para promedio y MOS, M3 para conciliación editorial), además de pruebas de regresión. La última ejecución oficial documentada de M1/M2/M3 fue la anterior al cambio de motor, con los tres resultados FALSE. **No se ha ejecutado ni certificado el nuevo validador contra este expediente**; por tanto M1 y M2 siguen en estado NO CERTIFICADO y M3 sigue BLOQUEADO por pendientes editoriales, aunque las cifras de M2 tienen conciliación independiente.

**Fuentes y análisis:** se incorporó `INVESTIGACION_EDITORIAL_F4_20261108.md` con fuentes primarias de resultados 3T26, competencia, autonomía/vehículos autónomos, contexto monetario, gobierno, recompras y Delivery Hero. Es material para cerrar capítulos, no una nueva valoración ni sustituto del artículo. Se mantiene **PENDIENTE** el TAM verificable y cuota objetivo, además de la revisión conjunta de beta/ERP/Rf y el flujo/reinversión frente a supuestos.

**Coherencia de cortes:** el análisis candidato menciona un Treasury nominal 10 años de 4,94 % (30-oct-2026); la curva Treasury da 4,86 % el 6-nov-2026, fecha del precio de referencia. Identificar si el modelo adoptó deliberadamente el corte de factores del 30-oct y documentarlo o recalcular la sensibilidad de WACC si no; **no modificar automáticamente las cifras**.

**Pendientes para reemplazar la ficha anterior:**
1. Ejecutar y aprobar el nuevo gate Floyd de `JMR-valuation#212`, sus regresiones, los controles de hoja y la paridad JSON; fusionar solo con evidencia.
2. Cerrar el artículo Nivel 1 y anexo Nivel 2 con fuentes, límites y comprobaciones de supuestos; resolver M3, TAM, fechas macro y puente Delivery Hero/SBC.
3. Prueba end-to-end de candidato en preview y auditoría económica F5 independiente; no marcar artificialmente `controlesTecnicosAprobados`.
4. Tras validar gates, fusionar el expediente `Modelo-JMR-datos#254`, promover la revisión Floyd como única ficha visible y comprobar enlace, catálogo y app con lectura posterior.

**Estado:** CANDIDATO / NO PUBLICADO en el catálogo. El informe anterior es una instantánea válida de las comprobaciones de su fecha; esta sección distingue los cambios posteriores de los gates todavía no certificados.
