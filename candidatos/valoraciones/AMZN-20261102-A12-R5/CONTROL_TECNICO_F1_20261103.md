# AMZN R5 — Cierre técnico del gate de entradas F1 · 2026-11-03

**Alcance:** control de completitud condicional de entradas (`inputs_completos.py`) y evaluación independiente de los estados de candados en la hoja **R5**. **No es auditoría económica de CAPEX, ROIC, FCFF, WACC/valor de deuda, ni autorización de publicación.**

## Implementación efectivamente cerrada en el motor

- PR [JMR-valuation #202](https://github.com/JuanMaRobledo/JMR-valuation/pull/202) **fusionado en `main`** mediante squash commit `836ae6827df152a79c699d1629af3470f9417734`.
- `scripts/inputs_completos.py` no exige `Input sheet!B39:B42` cuando `Input sheet!B38=No` (ausencia de stock options; RSU/SBC se tratan separadamente). Las cuatro entradas siguen siendo obligatorias cuando B38=Yes. No se rellenaron con 0.
- Acepta `AMZN --sheet-id 199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I` para evaluar **la hoja candidata** sin resolver la hoja previa del ticker. La apertura usa `open_target_sheet`, **con protección de plantillas**. Las salvedades solo coinciden con el ID real del candidato, no con otro ID del ticker.
- GitHub Actions confirmados sobre HEAD original del PR `f88f00eec1712bdf0582bad38733449149e68486`: run `41605990868` **4 tests aprobados** (gate condicional y CLI candidato); run `41605990934` **28 tests aprobados** (materialidad y controles financieros), ambos `success`, cero pasos fallidos. Código final inspeccionado también en `main`.

## Comprobación independiente del estado actual de la hoja R5 (API Google Drive)

- Se leyeron `Input sheet!A1:C120`, `Cost of capital worksheet!A1:B60`, `Option value!A5:B12`, `Resumen de Valoración!F3:G4`.
- Se reprodujo **el algoritmo de `vacias()`** del motor con los mismos filtros de rótulos, condicionales, selección de método, COC, opciones, empresa y MOS. **0 entradas exigibles sin valor**. R5 muestra `Input sheet!B38=No`, `Input sheet!B9=Retail (General)`, `Input sheet!B50=0,115`, `Cost of capital worksheet!B49=0` (preferentes verificadas), `Resumen de Valoración!G4=0,35`.
- Los **15 estados** de `reference/candados_plantilla.json` se leyeron individualmente en R5 y **15/15** pertenecen a `{LISTO, VALIDADO, CONCILIADO, NO APLICA}`; 0 bloqueos de estados. Incluye WACC B84, escenarios K5:K8, inversiones, R&D e impuestos.
- Esta reproducción independiente **NO ES ejecución del comando Python oficial**, ni sustituye una prueba contra el servicio Google Sheets a través de la cuenta de servicio del motor; no se informó `exit=0` de un proceso que no se pudo ejecutar.

## Falta para certificar la suite técnica COMPLETA de R5

```bash
PYTHONPATH=.:scripts python scripts/inputs_completos.py AMZN --sheet-id 199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I
```
La sesión actual no tiene credenciales de cuenta de servicio del motor para correr esa CLI directamente. Confirmar la ejecución real dentro del runtime autenticado y guardar stdout/exit code. Deberá extenderse un `--sheet-id` seguro también a controles que actualmente resuelven `model_steps.hoja_de('AMZN')`, **sin probar por accidente la hoja vieja**. Ejecutar y guardar la evidencia de:
- `candados.py` y `inputs_completos.py` (originales, sobre candidato)
- `estados_completos.py`, `auditar_estados_sec.py`, `auditar_ceros_materiales.py`
- `diff_formulas_plantilla.py`, `controles_todas.sh`, gate de publicación del catálogo contra revisión R5
- PR datos [#234](https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/234) sin workflows por commit: estado `DRAFT` no es suite aprobada

**No mezclar estos controles técnicos con los hallazgos económicos del CAPEX 2027 [#201](https://github.com/JuanMaRobledo/JMR-valuation/issues/201), deuda/ASC842 [#197](https://github.com/JuanMaRobledo/JMR-valuation/issues/197), P/FCFE saldo apertura [#199](https://github.com/JuanMaRobledo/JMR-valuation/issues/199).**

## Dictamen preciso
**Corregido e integrado el código del gate F1 #202. Cobertura de entradas y candados de la hoja R5: sin faltantes detectados mediante consulta API y reproducción independiente. Certificación de la ejecución oficial del motor sobre R5: PENDIENTE.** F1/F2 permanecen capturadas y conciliadas con reservas, DCF Base aún candidato US$149,19, PR #234 no fusionado ni publicado. Issue [#200](https://github.com/JuanMaRobledo/JMR-valuation/issues/200) no debe cerrarse totalmente mientras falten las ejecuciones oficiales.
