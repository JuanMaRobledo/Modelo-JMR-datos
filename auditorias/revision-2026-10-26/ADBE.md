# Auditoría de registro · ADBE · 26-oct-2026

- Registro: `valoraciones/ADBE-1789572982820.json` (Adobe Inc., Análisis 15-oct-2026 · estados financieros al 28-ago-2026)
- Análisis: `analisis/ADBE-research-1790475622244-a6a92.json`
- Valor principal: 392.9600099404326 · precio 251.67 · MOS 0.35 · precio con MOS 255.4240064612812
- **Estado preliminar: PENDIENTE**

**Alcance.** Se contrastó el registro y su análisis con `REGLAS_VIGENTES` v10. No se consultó la SEC, ni la hoja de Google, ni precios actuales; por eso ningún estado es VERIFICADO.

| Prioridad | Regla | Hallazgo |
|---|---|---|
| ALTA | §9 | El artículo tiene 19 secciones numeradas; la regla pide 18. |
| MEDIA | §3 | Conservadora 0.300 ≠ Optimista 0.150: la previa vigente es simétrica salvo en declive. |
| MEDIA | §4 | g terminal de Base = 3.50%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §4 | g terminal de Conservadora = 2.50%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §8 | Precio 251.67 frente a Base 392.96 (×0.64): diferencia grande que el informe debe explicar sin tocar la Base. |
| MEDIA | §8 | Estado heredado: «ESTRUCTURA Y ENTRADAS APROBADAS; SALVEDADES ECONÓMICAS EXPLÍCITAS». §8: «conciliado con salvedades» no es un estado; hay que cerrarlo como VERIFICADO, CON RESERVA MATERIAL o PENDIENTE. |
| MEDIA | §5 | Comparables sin validar (comparablesValidados = false). |
| MEDIA | §10 | El análisis no enlaza a su valoración (linkedValuation.sourcePath): validar_catalogo.cjs lo rechaza. |
| BAJA | §6 | Verificación visual pendiente. |
| BAJA | §4 | Precio de referencia del 15-oct-2026; el corte vigente es 30-sep-2026 y hoy es 26-oct-2026: hay que fijar un corte común. |
| BAJA | §9 | Falta el recuadro inicial «Valor intrínseco base:». |

**Pendiente de verificación documental:** cuadre con el último 10-Q/10-K, 8-K posteriores al corte, acciones diluidas, deuda y arrendamientos, y recálculo en la hoja con las reglas del 21-oct.
