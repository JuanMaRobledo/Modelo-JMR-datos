# Auditoría de registro · DPZ · 26-oct-2026

- Registro: `valoraciones/DPZ-1790595610921.json` (DOMINO'S PIZZA INC, Análisis del 30 de sept de 2026)
- Análisis: `analisis/DPZ-research-1790597462756-7k8ad.json`
- Valor principal: 409.25068981182955 · precio 296.1 · MOS 0.35 · precio con MOS 266.0129483776892
- **Estado preliminar: PENDIENTE**

**Alcance.** Se contrastó el registro y su análisis con `REGLAS_VIGENTES` v10. No se consultó la SEC, ni la hoja de Google, ni precios actuales; por eso ningún estado es VERIFICADO.

| Prioridad | Regla | Hallazgo |
|---|---|---|
| ALTA | §5A | Vector de pesos (0.4, 0.2, 0.1, 0.2, 0.05, 0.05) idéntico en 14 de las empresas: es un peso universal por defecto, que §5A prohíbe; falta la razón económica por método. |
| MEDIA | §3 | Conservadora 0.250 ≠ Optimista 0.200: la previa vigente es simétrica salvo en declive. |
| MEDIA | §4 | g terminal de Conservadora = 1.80%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §5A | Método P/BV / conservador: chequeo = N/D. |
| MEDIA | §5A | Método P/BV / base: chequeo = N/D. |
| MEDIA | §5A | Método P/BV / optimista: chequeo = N/D. |
| MEDIA | §8 | Estado heredado: «CORREGIDO CON SALVEDADES». §8: «conciliado con salvedades» no es un estado; hay que cerrarlo como VERIFICADO, CON RESERVA MATERIAL o PENDIENTE. |
| MEDIA | §5 | Comparables sin validar (comparablesValidados = false). |
| MEDIA | §10 | El análisis no enlaza a su valoración (linkedValuation.sourcePath): validar_catalogo.cjs lo rechaza. |
| BAJA | §6 | Verificación visual pendiente. |
| BAJA | §4 | Precio de referencia del 12-oct-2026; el corte vigente es 30-sep-2026 y hoy es 26-oct-2026: hay que fijar un corte común. |
| BAJA | §9 | Falta el recuadro inicial «Valor intrínseco base:». |

**Pendiente de verificación documental:** cuadre con el último 10-Q/10-K, 8-K posteriores al corte, acciones diluidas, deuda y arrendamientos, y recálculo en la hoja con las reglas del 21-oct.
