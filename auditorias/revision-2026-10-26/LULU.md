# Auditoría de registro · LULU · 26-oct-2026

- Registro: `valoraciones/LULU-1789603628153.json` (lululemon athletica inc., Análisis del 01 de oct de 2026)
- Análisis: `analisis/LULU-research-1789871389884-xj509.json`
- Valor principal: 158.4332135916115 · precio 94.5 · MOS 0.35 · precio con MOS 102.98158883454747
- **Estado preliminar: PENDIENTE**

**Alcance.** Se contrastó el registro y su análisis con `REGLAS_VIGENTES` v10. No se consultó la SEC, ni la hoja de Google, ni precios actuales; por eso ningún estado es VERIFICADO.

| Prioridad | Regla | Hallazgo |
|---|---|---|
| ALTA | §5A | Vector de pesos (0.4, 0.2, 0.1, 0.2, 0.05, 0.05) idéntico en 14 de las empresas: es un peso universal por defecto, que §5A prohíbe; falta la razón económica por método. |
| MEDIA | §3 | Conservadora 0.300 ≠ Optimista 0.150: la previa vigente es simétrica salvo en declive. |
| MEDIA | §4 | g terminal de Base = 3.00%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §4 | g terminal de Conservadora = 3.00%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §4 | g terminal de Optimista = 3.00%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §8 | Precio 94.50 frente a Base 158.43 (×0.60): diferencia grande que el informe debe explicar sin tocar la Base. |
| MEDIA | §5 | Comparables sin validar (comparablesValidados = false). |
| MEDIA | §10 | El análisis no enlaza a su valoración (linkedValuation.sourcePath): validar_catalogo.cjs lo rechaza. |
| BAJA | §6 | Verificación visual pendiente. |
| BAJA | §4 | Precio de referencia del 6-oct-2026; el corte vigente es 30-sep-2026 y hoy es 26-oct-2026: hay que fijar un corte común. |
| BAJA | §9 | Falta el recuadro inicial «Valor intrínseco base:». |

**Pendiente de verificación documental:** cuadre con el último 10-Q/10-K, 8-K posteriores al corte, acciones diluidas, deuda y arrendamientos, y recálculo en la hoja con las reglas del 21-oct.
