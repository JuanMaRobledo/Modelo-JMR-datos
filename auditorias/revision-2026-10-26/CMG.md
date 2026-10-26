# Auditoría de registro · CMG · 26-oct-2026

- Registro: `valoraciones/CMG-1790595601973.json` (CHIPOTLE MEXICAN GRILL INC, Revisión Modelo JMR 15-oct-2026 · información financiera 30-jun-2026)
- Análisis: `analisis/CMG-research-1790597372260-oos55.json`
- Valor principal: 23.991434067319343 · precio 30.81 · MOS 0.35 · precio con MOS 15.594432143757574
- **Estado preliminar: PENDIENTE**

**Alcance.** Se contrastó el registro y su análisis con `REGLAS_VIGENTES` v10. No se consultó la SEC, ni la hoja de Google, ni precios actuales; por eso ningún estado es VERIFICADO.

| Prioridad | Regla | Hallazgo |
|---|---|---|
| ALTA | §5A | Vector de pesos (0.4, 0.2, 0.1, 0.2, 0.05, 0.05) idéntico en 14 de las empresas: es un peso universal por defecto, que §5A prohíbe; falta la razón económica por método. |
| ALTA | §9 | El artículo tiene 0 secciones numeradas; la regla pide 18. |
| MEDIA | §3 | Conservadora 0.350 ≠ Optimista 0.200: la previa vigente es simétrica salvo en declive. |
| MEDIA | §4 | g terminal de Base = 4.25%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §4 | g terminal de Conservadora = 4.25%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §4 | g terminal de Optimista = 4.25%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §5 | Comparables sin validar (comparablesValidados = false). |
| MEDIA | §10 | El análisis no enlaza a su valoración (linkedValuation.sourcePath): validar_catalogo.cjs lo rechaza. |
| BAJA | §6 | Verificación visual pendiente. |
| BAJA | §4 | Precio de referencia del 15-oct-2026; el corte vigente es 30-sep-2026 y hoy es 26-oct-2026: hay que fijar un corte común. |
| BAJA | §9 | Falta el recuadro inicial «Valor intrínseco base:». |

**Pendiente de verificación documental:** cuadre con el último 10-Q/10-K, 8-K posteriores al corte, acciones diluidas, deuda y arrendamientos, y recálculo en la hoja con las reglas del 21-oct.
