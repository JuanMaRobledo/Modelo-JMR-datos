# Auditoría de registro · SHAK · 26-oct-2026

- Registro: `valoraciones/SHAK-1790595627129.json` (Shake Shack Inc., Análisis del 30 de sept de 2026)
- Análisis: `analisis/SHAK-research-1790597619437-xvczr.json`
- Valor principal: 24.678204563820863 · precio 66.9 · MOS 0.35 · precio con MOS 16.04083296648356
- **Estado preliminar: SIN ALTAS · fuentes sin verificar**

**Alcance.** Se contrastó el registro y su análisis con `REGLAS_VIGENTES` v10. No se consultó la SEC, ni la hoja de Google, ni precios actuales; por eso ningún estado es VERIFICADO.

| Prioridad | Regla | Hallazgo |
|---|---|---|
| MEDIA | §3 | Conservadora 0.300 ≠ Optimista 0.150: la previa vigente es simétrica salvo en declive. |
| MEDIA | §4 | g terminal de Base = 5.29%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §4 | g terminal de Conservadora = 5.29%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §4 | g terminal de Optimista = 5.29%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §5A | Método EV/FCFF / base: chequeo = n/a (≤ 0). |
| MEDIA | §5A | Método EV/FCFF / optimista: chequeo = n/a (≤ 0). |
| MEDIA | §8 | Precio 66.90 frente a Base 24.68 (×2.71): diferencia grande que el informe debe explicar sin tocar la Base. |
| MEDIA | §5 | Comparables sin validar (comparablesValidados = false). |
| MEDIA | §10 | El análisis no enlaza a su valoración (linkedValuation.sourcePath): validar_catalogo.cjs lo rechaza. |
| BAJA | §6 | Verificación visual pendiente. |
| BAJA | §4 | Precio de referencia del 30-sep-2026; el corte vigente es 30-sep-2026 y hoy es 26-oct-2026: hay que fijar un corte común. |
| BAJA | §9 | Falta el recuadro inicial «Valor intrínseco base:». |

**Pendiente de verificación documental:** cuadre con el último 10-Q/10-K, 8-K posteriores al corte, acciones diluidas, deuda y arrendamientos, y recálculo en la hoja con las reglas del 21-oct.
