# Auditoría de registro · MP · 26-oct-2026

- Registro: `valoraciones/MP-1791720000001.json` (MP Materials Corp., Análisis del 11-oct-2026 · con salvedades · ponderado de métodos incompleto (80%))
- Análisis: `analisis/MP-research-1791720000001-ia26.json`
- Valor principal: 0.26042430245815934 · precio 46.14 · MOS 0.25 · precio con MOS 0.1953182268436195
- **Estado preliminar: PENDIENTE**

**Alcance.** Se contrastó el registro y su análisis con `REGLAS_VIGENTES` v10. No se consultó la SEC, ni la hoja de Google, ni precios actuales; por eso ningún estado es VERIFICADO.

| Prioridad | Regla | Hallazgo |
|---|---|---|
| ALTA | §1 | MOS = 0.25: la regla vigente es 35 % (registro del 19-oct con 25 %). |
| MEDIA | §3 | Conservadora 0.300 ≠ Optimista 0.100: la previa vigente es simétrica salvo en declive. |
| MEDIA | §4 | g terminal de Base = 3.00%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §4 | g terminal de Conservadora = 2.00%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §4 | g terminal de Optimista = 3.50%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §8 | Precio 46.14 frente a Base 0.26 (×177.17): diferencia grande que el informe debe explicar sin tocar la Base. |
| MEDIA | §8 | Estado heredado: «Con salvedades; no certificada». §8: «conciliado con salvedades» no es un estado; hay que cerrarlo como VERIFICADO, CON RESERVA MATERIAL o PENDIENTE. |
| MEDIA | §5 | Comparables sin validar (comparablesValidados = false). |
| MEDIA | §10 | El análisis no enlaza a su valoración (linkedValuation.sourcePath): validar_catalogo.cjs lo rechaza. |
| BAJA | §6 | Verificación visual pendiente. |
| BAJA | §4 | Precio de referencia del 09-oct-2026; el corte vigente es 30-sep-2026 y hoy es 26-oct-2026: hay que fijar un corte común. |
| BAJA | §9 | Falta el recuadro inicial «Valor intrínseco base:». |

**Pendiente de verificación documental:** cuadre con el último 10-Q/10-K, 8-K posteriores al corte, acciones diluidas, deuda y arrendamientos, y recálculo en la hoja con las reglas del 21-oct.
