# Control de no regresión — NU, UBER, GOOGL y ponderaciones (31-oct-2026)

**Objetivo:** continuar la depuración técnica sin sustituir decisiones económicas, cambiar supuestos, borrar hojas o atribuir certificaciones financieras inexistentes.

## Evidencia añadida

### NU — sensibilidad bancaria, independiente de los múltiplos
- Se leyó del libro original `NU-20261029-R1` la matriz nativa de **Ke inicial × crecimiento terminal** desde `Sensibilidad FCFE A!A3:F12`, las **25 fórmulas** desde `A6:F10` y los diez FCFE proyectados de `FCFE bancario A!G17:G26`.
- La reproducción independiente del descuento de flujos y valor terminal produce el mismo número en las **25 celdas**. El centro (**Ke 12%, g 4%**) concilia con el DCF FCFE Base **US$18,32707520946464** por acción, diferencia `3.55e-15`.
- Evidencia: `evidencia/banca/NU-20261029-R1-sensibilidad-fcfe-nativa.json`. Guardas: `scripts/tests/nu_fcfe_bancario.test.cjs` y su workflow.
- **Límite:** esta sensibilidad NO es valoración relativa, NO sustituye P/E, P/FCFE o P/BV, NO utiliza EV/EBITDA o EV/FCFF industriales. El JSON de valoración y sus escenarios no se cambiaron.

### UBER y GOOGL — anclas de múltiplos no certificadas
- Se leyeron fórmulas/constantes **J19** de EVEBITDA, EVFCFF, PE, PFCFE y POCF en ambas hojas.
- **UBER:** EVEBITDA y PE se derivan del precio/capitalización; EVFCFF, PFCFE y POCF se derivan de los múltiplos anteriores. La hoja nueva usa 60% DCF / 40% relativos y el JSON conserva 100% DCF / 0% relativos. No reemplazar decisiones.
- **GOOGL:** EVEBITDA está fijado como constante sin serie histórica acreditada; PE incorpora precio de mercado; EVFCFF, PFCFE y POCF se derivan de otro múltiplo. La disponibilidad de cinco matrices numéricas por sí sola no certifica anclas económicas.
- Evidencias: `evidencia/anclas-20261031/UBER-20261030-A1-J19.json` y `GOOGL-20261029-R5-J19.json`. Guarda: `scripts/tests/anclas_uber_googl.test.cjs`.
- **Límite:** ambos JSON conservan cero matrices Base integradas. La reconstrucción de anclas independientes y la conciliación de ponderaciones siguen pendientes.

### Seis revisiones con ponderaciones discordantes
- El inventario existente `evidencia/conciliacion-descuentos-20261031.json` compara EPAM, MSFT, NKE, NVO, ONON, PYPL y ZTS contra sus hojas.
- **MSFT:** los 15 descuentos de Conservador/Base/Optimista se importaron con respaldo y control de fórmulas. Las pruebas concilian pesos y precios sin cambiar el DCF.
- **EPAM, NKE, NVO, ONON, PYPL, ZTS:** guardas `scripts/tests/ponderaciones_no_sobrescribir.test.cjs` comprueban que los pesos y el estado pendiente no se sustituyen silenciosamente por datos de las hojas que divergen. Para NVO, campo ausente y null equivalen únicamente a *dato no disponible*, nunca cero.
- Esta guarda bloquea cambios no autorizados; al resolver la discrepancia deberá actualizarse con una nueva fotografía, justificación y comparación de la revisión anterior.

## Puertas de salida que permanecen
1. Crear/validar anclas independientes para UBER y GOOGL y reconciliar la diferencia de ponderaciones; no adaptar supuestos para forzar un objetivo.
2. INTU debe mantener su DCF independiente y múltiplos N/D hasta contar con soportes; las cuadrículas exploratorias no satisfacen el contrato oficial.
3. NU requiere múltiplos **bancarios** P/E, P/FCFE y P/BV propios, aunque su sensibilidad FCFE ya esté comprobada.
4. Resolver los seis descuentos con ponderaciones discordantes, luego revisar todos los N2.
5. App #151: Preview autenticado con datos coordinados **para todos los visores incrustados**, no solo para la ficha raíz. El visor principal carga `main` en la rama actual; un cambio parcial de fuente produciría resultados mezclados.
6. No cerrar PR #211 mientras el gate financiero falle ni fusionar #151 sin QA visual y autenticación real.

**Norma de seguridad:** conservar PRs en borrador y todas las revisiones `EN_REVISION`; sin cambios a Google Sheets, DCF, MOS, estimaciones de crecimiento, capital invertido, ROIC, reglas de descuentos o ponderaciones por defecto. La validación editorial y las pruebas de no regresión no sustituyen la auditoría económica independiente.

## Contrato bancario estricto añadido

- El validador `scripts/validar_catalogo.cjs` separa ahora los métodos de empresas industriales de NU: el contrato `bank-relative-ke-v1` exige exactamente **P/E, P/FCFE y P/BV** provenientes de las hojas `PE`, `PFCFE` y `PBV`, con anclas históricas verificadas, 5×5 conciliadas, fuente y descuento a Ke. **No hay datos reales falsamente declarados completos para ese contrato.**
- `scripts/tests/validar_matrices_nativas.test.cjs` prueba que una matriz industrial, aunque tenga nombres P/E/P/FCFE/P/BV y centros aritméticos válidos, no puede aprobar NU. Prueba también un esquema sintético positivo del nuevo contrato y seis formas de invalidarlo.
- **Evidencia CI:** los tests de matrices, FCFE NU, conservación de pesos, anclas UBER/GOOGL y no regresión del expediente aprobaron en el commit `412447099e7a88ee0cffd4935d758ddae7fdecc4`. El único fallo del gate financiero global continúa en UBER por no disponer de matrices Base oficialmente justificadas. Ambos workflows editoriales están en verde.
