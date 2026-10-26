# Auditoría de registro · ONON · 26-oct-2026

- Registro: `valoraciones/ONON-1790595640519.json` (On Holding AG, Análisis del 01 de oct de 2026)
- Análisis: `analisis/ONON-research-1790597785576-4ggnz.json`
- Valor principal: 32.37033013053928 · precio 35.09 · MOS 0.35 · precio con MOS 21.040714584850534
- **Estado preliminar: PENDIENTE**

**Alcance.** Se contrastó el registro y su análisis con `REGLAS_VIGENTES` v10. No se consultó la SEC, ni la hoja de Google, ni precios actuales; por eso ningún estado es VERIFICADO.

| Prioridad | Regla | Hallazgo |
|---|---|---|
| ALTA | §5A | Vector de pesos (0.6, 0.1, 0.15, 0.05, 0.05, 0.05) idéntico en 5 de las empresas: es un peso universal por defecto, que §5A prohíbe; falta la razón económica por método. |
| MEDIA | §3 | Conservadora 0.250 ≠ Optimista 0.200: la previa vigente es simétrica salvo en declive. |
| MEDIA | §4 | g terminal de Base = 5.29%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §4 | g terminal de Conservadora = 5.29%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §4 | g terminal de Optimista = 5.29%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §5 | Comparables sin validar (comparablesValidados = false). |
| MEDIA | §10 | El análisis no enlaza a su valoración (linkedValuation.sourcePath): validar_catalogo.cjs lo rechaza. |
| BAJA | §6 | Verificación visual pendiente. |
| BAJA | §4 | Precio de referencia del 6-oct-2026; el corte vigente es 30-sep-2026 y hoy es 26-oct-2026: hay que fijar un corte común. |
| BAJA | §9 | Falta el recuadro inicial «Valor intrínseco base:». |

**Pendiente de verificación documental:** cuadre con el último 10-Q/10-K, 8-K posteriores al corte, acciones diluidas, deuda y arrendamientos, y recálculo en la hoja con las reglas del 21-oct.
