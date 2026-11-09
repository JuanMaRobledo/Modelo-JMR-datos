# DUOL Atlas R1 · Informe de promoción EN_REVISIÓN · 6-nov-2026

**Corte financiero 2026-09-30 · mercado 2026-11-05.** DUOL Atlas R1 `DUOL-20261105-ATLAS-R1` reemplaza en el catálogo la selección de la revisión R2, **sin eliminar la R2 histórica**. El expediente no se anuncia como certificación económica, sino **EN_REVISION CON RESERVA MATERIAL**. La app debe mostrar la diferencia entre valor intrínseco DCF FCFF Base y precio combinado secundario.

## Valoración calculada y contratos de pesos

| Método | VP Base USD/acción | Peso global |
|---|---:|---:|
| DCF FCFF | 108,2272265 | 60% |
| EV/FCFF | 150,9869857 | 15% |
| EV/EBITDA (GAAP homogéneo con su propio ancla) | 164,2597591 | 10% |
| P/E normalizado | 145,9776543 | 5% |
| P/FCFE de propietario neto SBC | 108,8904186 | 5% |
| P/OCF GAAP | 133,8273213 | 5% |

**Valor múltiplos Base:** US$146,2719837 (40% global). **Valor combinado informativo Base:** US$123,4451294. **MOS35% SOLO DCF Base:** US$70,3476972. Escenarios DCF Conservador US$78,8021, Optimista US$151,3869 y estrés IA (sin ponderar) US$66,6760. Combinados secundarios Conservador US$92,6487, Optimista US$164,1769.

## Pruebas verificadas
1. Cohortes I+D rolling 2023–2026: cuatro conciliaciones SEC con FY+9M−9M. Capitalización I+D 3 años y leasing ASC842 sin doble deuda.
2. Costo capital Damodaran 01-nov-2026: Treasury 5,29%, ERP 4,41%, beta del sector reapalancada1,6026. WACC inicial12,6192% común a las historias, terminal9,70%, g terminal4%. ROIC marginal Base terminal11,5%.
3. Tres matrices DCF Base 5×5 y cinco matrices múltiplos Base 5×5 con centros exactos, sin introducir valores fijos.
4. Anclas de múltiplos propias DUOL FY2025/LTM2026 con ajuste de tasa 2025→2026, evaluación de cambio de ciclo y techo de crecimiento; cuatro pares LRN/PSO/EDU/TAL son únicamente diagnóstico y NO constituyen una mediana falsamente homogénea.
5. `Financials Multiples`: 20 fundamentales de tres historias; `Descuento de múltiplos`: 15 combinaciones método×historia, 45 VP FY+1/2/3; `Sensibilidad por múltiplo`: siete rangos contractuales (5 OK, P/S/P/BV N/A) y 5 centros OK.
6. Nivel 1 JMR 14 capítulos/8.151 palabras y Nivel2 12 controles de reproducibilidad más 18 secciones de explicación, ambas piezas con mismo revisionId y mismas cifras.
7. GitHub CI: registro y drivers; validación de profundidad editorial; Método A profundidad editorial; Control JMR de ponderaciones. Deben pasar en el **SHA final** antes de fusionar.

## Salvedades económicas materiales que permanecen visibles
- Los cinco múltiplos relativos se eligen sobre el ciclo DUOL 2025–2026 y no una mediana certificada de pares homogéneos: el valor relativo es una referencia de mercado con prima de crecimiento potencialmente inestable. La ponderación 60/40 es una síntesis informativa, NO sustituye el valor intrínseco DCF Base.
- SBC LTM156,596m y guía14% ventas; 50,8m acciones plenamente diluidas ya incluyen opciones/RSUs existentes, por lo que no se descuentan dos veces. La dilución futura exige revisión económica de recompras/entrega de títulos.
- NOL e incentivos fiscales FY2025 implican un máximo nominal orientativo ≈US$2,12/acción sin descontar; no añadir dos veces DTA. Provisiones y utilización fiscal FY2026 pendientes de revisión detallada.
- ASC842 lease84,216m ya incluido una sola vez; amortización ROU proxy y sensibilidad ≈US$0,83/acción.
- Riesgo de IA separado: el valor bajo disrupción US$66,6760 no entra en el promedio 25/50/25.
- QA visual de app y revisión económica independiente deben documentarse tras integración; no declarar certificado económico.

## Evidencia
- [Libros y documentos DUOL Atlas](https://drive.google.com/drive/folders/19CKTHWd28ZsaXmm7Yei_T_KKfbh5hkZi)
- [Estados financieros](https://docs.google.com/spreadsheets/d/1f3lPGhv8Lx0DzrA-vwXbLlD5JxzTcjPtj_Nn026mZJA/edit)
- [DCF, historia y sensibilidades](https://docs.google.com/spreadsheets/d/1YPtE7UWhIPCMhiENnRNCe-jX8mzoGEnjpv78P6TdNt4/edit)
- [Múltiplos, pesos y descuento](https://docs.google.com/spreadsheets/d/1K0yBSETJQkWjdAHRy6Os-3iQ5dmHW_bc88LTMXhUxYU/edit)
- [Nivel1 — 14 capítulos](https://docs.google.com/document/d/1ID7E3D-TBBXGFnbMx4WiKcOcI5tyopAJlcXQ4BVJmo0/edit)
- [Nivel2](https://docs.google.com/document/d/1TJ5dDsObHGPD8dTSX_gql6pF1pWJpf9QNWiwa0BrR-Q/edit)
- [Snapshot de 5 matrices con SHA256](https://github.com/JuanMaRobledo/Modelo-JMR-datos/blob/codex/duol-atlas-r1-publicacion-gated-20261106/evidencia/atlas-duol-20261106/multiples_source.json)

**No modificar la plantilla original GINZU ni borrar las revisiones previas.**
