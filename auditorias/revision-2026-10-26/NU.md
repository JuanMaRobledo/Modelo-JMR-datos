# Auditoría de registro · NU · 26-oct-2026

- Registro: `valoraciones/NU-1791687886500.json` (Nu Holdings Ltd., Análisis del 30 de sept de 2026)
- Análisis: `analisis/NU-research-1791690919747-wcpoa.json`
- Valor principal: 18.270733146432395 · precio 16.12 · MOS 0.35 · precio con MOS 11.875976545181057
- **Estado preliminar: SIN ALTAS · fuentes sin verificar**

**Alcance.** Se contrastó el registro y su análisis con `REGLAS_VIGENTES` v10. No se consultó la SEC, ni la hoja de Google, ni precios actuales; por eso ningún estado es VERIFICADO.

| Prioridad | Regla | Hallazgo |
|---|---|---|
| MEDIA | §3 | Conservadora 0.250 ≠ Optimista 0.200: la previa vigente es simétrica salvo en declive. |
| MEDIA | §4 | g terminal de Base = 5.29%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §4 | g terminal de Conservadora = 5.29%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §4 | g terminal de Optimista = 5.29%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §5 | Comparables sin validar (comparablesValidados = false). |
| MEDIA | §10 | El análisis no enlaza a su valoración (linkedValuation.sourcePath): validar_catalogo.cjs lo rechaza. |
| BAJA | §6 | Verificación visual pendiente. |
| BAJA | §9 | Falta el recuadro inicial «Valor intrínseco base:». |

**Pendiente de verificación documental:** cuadre con el último 10-Q/10-K, 8-K posteriores al corte, acciones diluidas, deuda y arrendamientos, y recálculo en la hoja con las reglas del 21-oct.
