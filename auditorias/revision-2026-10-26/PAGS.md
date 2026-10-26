# Auditoría de registro · PAGS · 26-oct-2026

- Registro: `valoraciones/PAGS-1790596866414.json` (PagSeguro Digital Ltd., Análisis del 30 de sept de 2026)
- Análisis: `analisis/PAGS-research-1790597874865-31w6i.json`
- Valor principal: 12.255330414290382 · precio 11.16 · MOS 0.35 · precio con MOS 7.965964769288749
- **Estado preliminar: SIN ALTAS · fuentes sin verificar**

**Alcance.** Se contrastó el registro y su análisis con `REGLAS_VIGENTES` v10. No se consultó la SEC, ni la hoja de Google, ni precios actuales; por eso ningún estado es VERIFICADO.

| Prioridad | Regla | Hallazgo |
|---|---|---|
| MEDIA | §3 | Conservadora 0.300 ≠ Optimista 0.150: la previa vigente es simétrica salvo en declive. |
| MEDIA | §5 | Comparables sin validar (comparablesValidados = false). |
| MEDIA | §10 | El análisis no enlaza a su valoración (linkedValuation.sourcePath): validar_catalogo.cjs lo rechaza. |
| BAJA | §6 | Verificación visual pendiente. |
| BAJA | §4 | Precio de referencia del 6-oct-2026; el corte vigente es 30-sep-2026 y hoy es 26-oct-2026: hay que fijar un corte común. |
| BAJA | §9 | Falta el recuadro inicial «Valor intrínseco base:». |

**Pendiente de verificación documental:** cuadre con el último 10-Q/10-K, 8-K posteriores al corte, acciones diluidas, deuda y arrendamientos, y recálculo en la hoja con las reglas del 21-oct.
