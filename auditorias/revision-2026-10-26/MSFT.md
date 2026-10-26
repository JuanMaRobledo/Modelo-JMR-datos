# Auditoría de registro · MSFT · 26-oct-2026

- Registro: `valoraciones/MSFT-1789582778217.json` (MICROSOFT CORP, Análisis del 30 de sept de 2026)
- Análisis: `analisis/MSFT-research-1788905155892-deskj.json`
- Valor principal: 570.7312305188628 · precio 535.07 · MOS 0.35 · precio con MOS 370.9752998372609
- **Estado preliminar: PENDIENTE**

**Alcance.** Se contrastó el registro y su análisis con `REGLAS_VIGENTES` v10. No se consultó la SEC, ni la hoja de Google, ni precios actuales; por eso ningún estado es VERIFICADO.

| Prioridad | Regla | Hallazgo |
|---|---|---|
| ALTA | §5A | Vector de pesos (0.6, 0.1, 0.15, 0.05, 0.05, 0.05) idéntico en 5 de las empresas: es un peso universal por defecto, que §5A prohíbe; falta la razón económica por método. |
| MEDIA | §3 | Conservadora 0.250 ≠ Optimista 0.150: la previa vigente es simétrica salvo en declive. |
| MEDIA | §4 | g terminal de Base = 5.29%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §4 | g terminal de Conservadora = 5.29%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §4 | g terminal de Optimista = 5.29%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §8 | Estado heredado: «corregido con salvedades». §8: «conciliado con salvedades» no es un estado; hay que cerrarlo como VERIFICADO, CON RESERVA MATERIAL o PENDIENTE. |
| MEDIA | §5 | Comparables sin validar (comparablesValidados = false). |
| MEDIA | §10 | El análisis no enlaza a su valoración (linkedValuation.sourcePath): validar_catalogo.cjs lo rechaza. |
| BAJA | §6 | Verificación visual pendiente. |
| BAJA | §4 | Precio de referencia del 30-sep-2026; el corte vigente es 30-sep-2026 y hoy es 26-oct-2026: hay que fijar un corte común. |
| BAJA | §9 | Falta el recuadro inicial «Valor intrínseco base:». |

**Pendiente de verificación documental:** cuadre con el último 10-Q/10-K, 8-K posteriores al corte, acciones diluidas, deuda y arrendamientos, y recálculo en la hoja con las reglas del 21-oct.
