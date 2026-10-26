# Auditoría de registro · NFLX · 26-oct-2026

- Registro: `valoraciones/NFLX-1792548021734.json` (Netflix, Inc., 2026-09-30)
- Análisis: `analisis/NFLX-research-1792549859632-adttn.json`
- Valor principal: 70.85248520211614 · precio 69.58 · MOS 0.35 · precio con MOS 46.054115381375496
- **Estado preliminar: PENDIENTE**

**Alcance.** Se contrastó el registro y su análisis con `REGLAS_VIGENTES` v10. No se consultó la SEC, ni la hoja de Google, ni precios actuales; por eso ningún estado es VERIFICADO.

| Prioridad | Regla | Hallazgo |
|---|---|---|
| ALTA | §5A | Vector de pesos (0.6, 0.1, 0.15, 0.05, 0.05, 0.05) idéntico en 5 de las empresas: es un peso universal por defecto, que §5A prohíbe; falta la razón económica por método. |
| MEDIA | §8 | Estado heredado: «VERIFICADO_CON_SALVEDADES_NO_BLOQUEANTES». §8: «conciliado con salvedades» no es un estado; hay que cerrarlo como VERIFICADO, CON RESERVA MATERIAL o PENDIENTE. |
| BAJA | §4 | Precio de referencia del 30-sep-2026; el corte vigente es 30-sep-2026 y hoy es 26-oct-2026: hay que fijar un corte común. |

**Pendiente de verificación documental:** cuadre con el último 10-Q/10-K, 8-K posteriores al corte, acciones diluidas, deuda y arrendamientos, y recálculo en la hoja con las reglas del 21-oct.
