# Gemini CLI · biblioteca de producción JMR V2

Este directorio **no** tiene motor independiente ni contrato distinto. Aplicar el `GEMINI.md`, `AGENTS.md`, `CONTRATO_UNICO_LLM.md` y `contrato-v2.json` **vigentes** en `JuanMaRobledo/Modelo-JMR-V2` (contrato v1.5.5 de 21-nov-2026, o sucesor autorizado).

## Alcance

- Dentro de este repositorio, escribir únicamente en `jmr-v2/` y en scripts necesarios **exclusivamente para V2** que el PR identifique expresamente. El directorio `jmr-multiplos/` y los datos Floyd quedan fuera de alcance.
- `biblioteca.json` es manifiesto de la **biblioteca completa**, no de una sola empresa; no reemplazarlo por un fichero con una sola valoración ni editar su hash manualmente.
- Para actualizar, seguir `Modelo-JMR-V2/CONTENIDOS.md`: preparar expediente y análisis de misma revisión, ejecutar exportador oficial, preservar todas las empresas, generar o regenerar PDF, revisar fuentes, gráficas, unidades, tres escenarios y matrices, crear manifiesto comprimido consistente y probar integridad.
- Cada cambio debe preservar toda la información correcta de las demás empresas y no aprobar una auditoría personal inexistente. Un informe preliminar publicado puede seguir `EN_REVISION` económica.
- El informe PDF sigue **NVIDIA R6** y para MELI el diseño exacto **MELI R8**, según el contrato V2 v1.5.5. No introducir portadas alternativas ni resumir los 14 capítulos.
- No mezclar fecha de cotización con fecha contable y no copiar cifras R8 en valoraciones R10.
- Antes de publicar: probar `npm test`, `npm run catalogo:check`, cierre editorial del ticker cuando aplique, integridad del archivo comprimido y paridad app/PDF. Registrar evidencias, commit y PR.
- Por defecto trabajar en rama de revisión y PR, **sin escrituras directas a `main`**; no atribuir aprobación del usuario, no exponer credenciales o documentos personales.

Si Gemini no puede acceder a `Modelo-JMR-V2` o al expediente oficial, detener **solo la escritura**, describir la falta de acceso y no improvisar un motor ni reconstruir la biblioteca a partir de memoria.
