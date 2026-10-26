# Auditoría de registro · AAPL · 26-oct-2026

- Registro: `valoraciones/AAPL-1791720000000.json` (Apple Inc., Análisis del 11-oct-2026 · con salvedades)
- Análisis: `analisis/AAPL-research-1791720000000-ia26.json`
- Valor principal: 150.13194995008314 · precio 336.64 · MOS 0.25 · precio con MOS 112.59896246256235
- **Estado preliminar: PENDIENTE**

**Alcance.** Se contrastó el registro y su análisis con `REGLAS_VIGENTES` v10. No se consultó la SEC, ni la hoja de Google, ni precios actuales; por eso ningún estado es VERIFICADO.

| Prioridad | Regla | Hallazgo |
|---|---|---|
| ALTA | §1 | MOS = 0.25: la regla vigente es 35 % (registro del 19-oct con 25 %). |
| ALTA | §5A | Vector de pesos (0.4, 0.2, 0.1, 0.2, 0.05, 0.05) idéntico en 14 de las empresas: es un peso universal por defecto, que §5A prohíbe; falta la razón económica por método. |
| MEDIA | §3 | Conservadora 0.250 ≠ Optimista 0.150: la previa vigente es simétrica salvo en declive. |
| MEDIA | §4 | g terminal de Base = 3.00%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §4 | g terminal de Conservadora = 2.00%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §4 | g terminal de Optimista = 3.25%; la regla del 21-oct fija 4% (con techo en la tasa libre). |
| MEDIA | §5 | CAGR implícito negativo en los tres escenarios (conservador -20.7%, base -11.6%, optimista -2.6%): el precio exige más de lo que descuenta cualquiera. |
| MEDIA | §8 | Precio 336.64 frente a Base 150.13 (×2.24): diferencia grande que el informe debe explicar sin tocar la Base. |
| MEDIA | §8 | Estado heredado: «Con salvedades; no certificada». §8: «conciliado con salvedades» no es un estado; hay que cerrarlo como VERIFICADO, CON RESERVA MATERIAL o PENDIENTE. |
| MEDIA | §5 | Comparables sin validar (comparablesValidados = false). |
| MEDIA | §10 | El análisis no enlaza a su valoración (linkedValuation.sourcePath): validar_catalogo.cjs lo rechaza. |
| BAJA | §6 | Verificación visual pendiente. |
| BAJA | §4 | Precio de referencia del 09-oct-2026; el corte vigente es 30-sep-2026 y hoy es 26-oct-2026: hay que fijar un corte común. |
| BAJA | §9 | Falta el recuadro inicial «Valor intrínseco base:». |

**Pendiente de verificación documental:** cuadre con el último 10-Q/10-K, 8-K posteriores al corte, acciones diluidas, deuda y arrendamientos, y recálculo en la hoja con las reglas del 21-oct.
