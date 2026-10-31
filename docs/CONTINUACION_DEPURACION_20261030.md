# Continuación técnica del Modelo JMR — 30-oct-2026 Colombia

> **Registro histórico (corte 30-oct-2026).** Este inventario conserva la evidencia de origen, pero ya no describe el estado vigente: el 31-oct se organizaron 20 análisis en 14 capítulos y se integraron matrices nativas Base de 14 revisiones en el PR #211. Para decisiones actuales y pendientes, consultar [AVANCE_ESTANDARIZACION_20261031.md](AVANCE_ESTANDARIZACION_20261031.md). No convertir los pendientes históricos de 13 capítulos o cero matrices en tareas nuevas sin reconciliar con el informe vigente.


Estado: **avance en ramas de revisión, sin cierre ni publicación**.

## Cambios de esta ejecución

- 20 identidades de hojas oficiales comprobadas con metadata de Google Sheets; lecturas nuevas de A76:I144 con fórmulas y valores.
- 19 fotografías de los rangos del extractor #181, SHA256 recalculado y puente candidato ejecutado. NU usa hojas bancarias específicas y queda fuera del extractor industrial.
- 14 registros de valoración reciben únicamente `sensibilidadMultiples`: CELH, ADBE, BSX, CMG, NFLX, MSFT, NKE, PYPL, EPAM, ZTS, ONON, NVO, AFYA, DUOL. Estado técnico `INTEGRADO_EN_REVISION`, certificado económico falso. No se cambiaron Base, escenarios, MOS, precios, descuentos, supuestos, fórmulas ni catálogo.
- Integrador reproducible `scripts/integrar_matrices_nativas.py`: coteja identidad, SHA256, matriz, ejes, control FY+3, origen, 25 fórmulas y todas las celdas del rango fuente. Rechaza candidatos que alteren otros campos. Bloquea N/D prioritarios y banca. La salida debe ser distinta de las entradas.
- Evidencia por revisión bajo `evidencia/integracion-nativa-20261030/`: registro anterior, fotografía de rangos del motor, fórmulas nativas y matrices candidatas del motor. Los archivos candidatos no se incluyen en catálogo ni sustituyen por sí solos una valoración.
- Validador endurecido: exige el rango fuente exacto de cada método. Inventario corregido: banca requiere P/E, P/FCFE y P/BV, no los cinco industriales.

## Bloqueos identificados individualmente

| Empresa | Evidencia actual | Acción pendiente |
|---|---|---|
| SHAK | EV/FCFF FY+3 −36,4662 y FCFE −65,7664 en unidades de hoja; matrices N/D | Resolver aplicabilidad y documentar exclusiones económicas cuando corresponda. No cambiar flujos para aprobar. |
| MELI | FCFF FY+3 −941,3741 y FCFE −984,8153; otros tres métodos calculados | Revisar tratamiento del negocio mixto y exclusiones justificadas; no imponer FCFF a cartera crediticia. |
| GOOGL | P/E: ancla y NI proyectado vacíos; P/FCFE: ancla y flujo vacíos; P/OCF: flujo existe y ancla vacía | Completar trazabilidad de datos/enlaces y anclas en una revisión financiera; no es N/A económico demostrado. |
| UBER | Fundamentales FY+1/2/3 positivos en cinco métodos, anclas objetivo vacías | Completar comparables/anclas justificadas. No faltan los cinco fundamentales. |
| INTU | Proyecciones y anclas vacías en los cinco métodos; bloque relativo sin alimentación | Conectar datos oficiales y modelo relativo. El DCF independiente existente no debe borrarse. |
| NU | FCFE bancario y sensibilidad Ke/g existentes; tres relativos bancarios pendientes | Completar P/E, P/FCFE y P/BV con capital/ROE y comparables adecuados. |

Las 14 integraciones de matrices **no completan por sí solas** los bloques de `descuentoMultiples` ausentes de varios JSON, los análisis ni la validación visual. Esas dependencias permanecen abiertas.

## Verificación ejecutada

- Datos: 30 pruebas Node aprobadas (capturas, matrices, inventario).
- Integrador: 7 pruebas Python aprobadas; cubren cambio económico indebido, hash alterado, foto parcial, fuente/ejes incorrectos, constantes y datos desactualizados, banca y matrices preexistentes.
- Motor fusionado #181: 13 pruebas relevantes aprobadas localmente, incluido pipeline opt-in.
- Puerta individual de las 14 matrices integradas: aprobada.
- Gate global: mantiene bloqueo en SHAK por matrices prioritarias pendientes. No se omite ni se modifica la puerta para obtener verde.
- Profundidad editorial: 16 estudios pasan control estructural con aviso explícito de 13 capítulos; prueba de prosa: 23/23. Ninguna acredita por ello el Nivel 1 de 14 capítulos ni completitud económica.
- App #151: ocho workflows aprobados en SHA anterior `69a1a855f091b36394f80e3680e77740643bc251`. El despliegue de ese SHA está READY; lectura autenticada Vercel de `/expediente.html?ticker=AFYA` devuelve 503 «El acceso privado todavía no está configurado». No se modificó autenticación.

## Estado de cierre y dependencias

1. Confirmar CI de los nuevos commits de #151 y #211; no fusionar #211 mientras el gate global falle.
2. Exportar y conciliar los resultados de `Descuento de múltiplos` existentes en las 14 hojas cuando falten en JSON; no recalcularlos fuera de Sheets.
3. Separar el contenido de ciclos en capítulo 5 y actualizar índices a 14, preservando narrativa y sin acreditar contenido genérico. Validar los 12 apartados de Nivel 2: presencia no equivale a completitud.
4. Resolver GOOGL, UBER, INTU, SHAK, MELI y NU según la tabla; distinguir defectos de datos de cambios de supuestos. Estos últimos quedan fuera de esta limpieza.
5. Habilitar acceso de preview mediante configuración autorizada existente, sin desactivar controles; verificar ficha única en móvil y escritorio en ADBE, DUOL, UBER, NVO y AFYA.
6. Solo con controles necesarios aprobados: fusión, despliegue y QA real. La auditoría económica sigue reservada para después de la revisión visual del usuario.

No hay informe final de cierre. El inventario detallado acompaña esta ejecución y conserva separados catálogo activo, hojas históricas encontradas y empresas listadas sin expediente vinculado.
