# AMZN R4 · PRUEBA REAL del proceso JMR de cinco fases · Fase 1 (valoración inicial)

**Fecha:** 2026-11-02. **Proceso:** versión 26, cinco fases, ahora INTEGRADO en main de Modelo-JMR PR #166 y JMR-valuation PR #193. **Estado de este ensayo:** `FASE_1_INICIADA_CON_BLOQUEOS_MATERIALES` — CANDIDATO, NO VALORADO, NO PUBLICADO. No sustituye la anterior `FASE_1_ENTREGA.md`, que documenta la fase 1 histórica del sistema de cuatro fases. **Hoja R4 exclusiva:** https://docs.google.com/spreadsheets/d/10qfoGrEP1PgdlLWrHvfoHqExKDZbPK75yb_oINlO4a8/edit. Se prohíbe consultar R2/R3 como fuente de valoración.

## Qué se hizo en esta ejecución, comprobado por API nativa de Sheets

1. **Integración del proceso.** Se comprobaron en main la regla `modelo/REGLAS_VIGENTES.md` versión 26, `docs/propuestas/fases/README.md`, `FASE_1_VALORACION_INICIAL.md` y la habilidad Claude Code para 5 fases; son referencias oficiales de ahora. CI del PR #166: 7/7 workflows OK antes de merge. CI PR #193: control materialidad OK. El PR de Amazon #233 continúa en DRAFT y NO fue fusionado, para no publicar candidato.
2. **Origen principal del DCF:** `Input sheet!B12` ventas LTM 797.455 USD M, `B13` EBIT LTM 104.366 USD M, `B14` interés LTM 4.484 USD M, `B15` equity contable septiembre 613.601 USD M, `B16` deuda + leases/financing contables 304.841 USD M, `B19` caja/marketables 114.226 USD M, `B22` acciones 10.811 millones, `B23` precio 240,35 USD al 30-oct, `B24` tasa efectiva calculada 22,33%, `B27/B29` crecimiento histórico extrapolado 11,23% y `B28` margen EBIT LTM 13,09%. Son fórmulas de la hoja, NO valores objetivo calibrados. Fuente SEC Q3 2026 y 10-K FY2025; precio de cierre 30-oct-2026. En `Input sheet!B82` el agregado de inversiones de largo plazo contables es 294.595 USD M, NO valor económico disponible.
3. **Tasa/ERP:** `Input sheet!B35` 5,29% (US Treasury 30-sep-2026), `Cost of capital worksheet!B27` añadida PRIMA DE MERCADO 3,70% (Damodaran corte 30-sep-2026), y nota de B35 corregida; el autor reporta retorno implícito 8,99%, Treasury 5,29%, ERP 3,70%. Fuente original: https://aswathdamodaran.substack.com/p/earnings-cashflows-and-stock-prices . **NO equivale a tasa spot 30-oct-2026 de 4,94%** (https://ploveranalytics.com/us-treasury.html y datos Treasury). Se conserva la pareja del mismo corte para coherencia, con desfase mercado/costo capital identificado y sensibilidad pendiente.
4. **No hubo fraude de WACC.** `Cost of capital worksheet!B12` Detailed/Industry/Distribution todavía sin selector, `B22` beta business sin decisión, `B26` prima país por regiones sin decisión, `B34` costo de deuda sin decisión, `B39` impuesto marginal sin completar. El diagnóstico `E63 = 5,29%` procede artificialmente de Ke = Rf y deuda mercado = 0 por insumos vacíos, **NO ES WACC válido**. `B14` (WACC oficial) y `Input sheet!B36` permanecen sin valor; no escribir tasa arbitraria para forzar DCF.
5. **Controles de riesgo por valor de activos:** `Input sheet!B20` valor económico de activos NO operativos en blanco, `B21` minority interests sin verificar, `B81` arrendamientos PENDIENTE, `B85` inversiones NO operativas PENDIENTE. La SEC 2026 10-Q registra Anthropic preferentes 92.500, notas convertibles 146.200 y OpenAI preferentes 50.000 USD M (valores contables/fair value, con restricciones). No sumarlos mecánicamente al EV–equity ni descontarlos por duplicado: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm (p. 11–12). En `B82` hay 294.595 USD M de inversiones históricas, NO valor de equity con prima de liquidez; chequear inclusión en Other assets y participación en AWS.
6. **Problema de múltiplos encontrado y aún abierto:** `Financials Multiples!B54:D54` usa `EBT - Taxes` mientras la SEC trae gastos fiscales negativos, inflando NI normalizada (FY2023 44.677 vs utilidad reportada 30.425 USD M). Issue técnico https://github.com/JuanMaRobledo/JMR-valuation/issues/194 . P/E y métodos que hereden NI **N/D bloqueados**, aunque existan sus fórmulas; EV/EBITDA y EV/FCFF requieren cerrar EV–equity y distinguir flujo libre negativo tras CAPEX.
7. **DCF:** `Valuation output!B35` y `Escenarios e historias!H5:H8` no contienen resultados. No existe valor intrínseco Base ni MOS verificables de R4. **No se escribió crecimiento ni WACC inventados para hacer aparecer un resultado.** La valoración temprana de F1 permite plantear hipótesis pero no puede forzar precio con insumos críticos ausentes.

## Historias de trabajo preliminares (candidatas de juicio; NO son entradas aprobadas ni cifras de valoración)

| Historia | Probabilidad PREVIA condicional a etapa «crecimiento maduro» | Hipótesis de ventas 1–5 años | Margen EBIT hacia año 5 | Motor económico / invalidación |
|---|---:|---|---|---|
| Base | 45% | +10% a +12% inicial, desacelerando hacia +8–9% | 14,5–16% | AWS y publicidad sostienen mix de ganancias; retorno de CAPEX IA llega con retraso; invalidar si el FCFF no recupera pese a crecimiento. |
| Conservadora | 22,5% | +6% a +9%, desacelerando | 11–13% | CAPEX hiperescala tarda, menor AWS incremental y consumo; presión costos. |
| Optimista | 22,5% | +12% a +15%, desacelerando | 16,5–18,5% | Mejora de utilización IA/capacidad, AWS mayor participación y mayor monetización publicitaria; exigir S/C y ROIC marginal congruentes. |
| Disrupción | 10% | 0% a +5% con deterioro | 8–11% | Ruptura del moat cloud, sobreinversión/obsolescencia y guerra de precios. Fuera del promedio ordinario. |

**Advertencia:** son RANGOS de hipótesis para ensayar la fase 1, **NO entradas escritas en Escenarios e historias**, **NO trayectorias anualizadas finales**, **NO WACC ni ROIC terminal**. Requieren contraste con historial/segmentos/consenso, S/C marginal y coste de capital; el estudio monetario e incertidumbre de inversiones no operativas puede cambiar mucho el DCF. Baseline comprobado: ventas 9M2026 584.069 (+16% Y/Y) y AWS 125.803 (+35% Y/Y), EBIT 79.389 9M, fuente SEC 10-Q; LTM ventas 797.455, EBIT 104.366. Las previas solo se usan si la clasificación por ciclo es finalmente «crecimiento maduro», no imponerla por defecto.

## Checklist real Fase 1 (proceso nuevo)

| Paso | Estado | Por qué |
|---|---|---|
| 1 Aislamiento, identidad, moneda, corte | APROBADO DIRECTO | R4, SEC, hoja/corte USD, sin R2/R3 |
| 2 Input y mapa de dependencias | PARCIAL | Datos GAAP sí; NCI, valor económico de inversiones, lease e I+D requieren validación |
| 3 WACC fechado y pesos de mercado | **BLOQUEO MATERIAL** | Beta, segmentos, exposición país, costo deuda y conversor de deuda sin aprobar |
| 4 Historias Damodaran e inputs DCF | PARCIAL, solo hipótesis | Baseline y propuesta escritos aquí; no hay DCF válido aún |
| 5 Cinco múltiplos prioritarios | **BLOQUEO MATERIAL** | Bug fiscal #194 y bridge EV incompleto |
| 6 DCF inverso, 5×5, JSON | NO EJECUTADO por dependencia | No inventar matrices, valores, ni centros sin DCF Base |
| 7 Gates / prueba de fórmula oficial | PARCIAL | Hoja 46 módulos, fórmulas observadas; `candados.py`, `diff_formulas_plantilla.py`, etc NO EJECUTADOS contra R4 con el motor autenticado |

## Próximas acciones precisas para completar de verdad la Fase 1
1. Seleccionar sector/betas bottom-up (Commerce/Cloud) y geografías verificadas; estimar costo de deuda, rating, maturity y deuda a mercado; tasa marginal; activar **Detailed** solo después de insumos o mantener trazabilidad sin WACC ficticio.
2. Resolver valoración económica de inversiones Anthropic/OpenAI (otros valores financieros/participaciones, restricciones, impuestos, compromisos, doble conteo), NCI, arrendamientos e I+D; cuantificar impacto del agregado 294.595 USD M.
3. Resolver bug de signo tributario #194 mediante mantenimiento en plantilla respaldada, regresión, propagación controlada a R4; revalidar P/E/FCFE y las demás dependencias.
4. Construir trayectorias anuales completas de cuatro historias, márgenes, ROIC, S/C, lag, impuestos, g y sensibilidades, comprobar contra versión de motor JMR A-1.2 sin sustituir fórmulas.
5. Ejecutar controles oficiales y cotejo fuente/hoja, dejar nueva `FASE_1_ENTREGA.md` **solo cuando el expediente antiguo se archive con nombre inequívoco** y la F1 nueva tenga un resultado verificable. No publicar hasta F4.

**Resultado del ensayo:** el proceso actualizado funciona como puerta de entrada y **detuvo correctamente** una valoración que parecía calculable con WACC ficticio y NI inflado. **NO certifica cumplimiento integral de Fase 1 y NO pasa a Fase 2 por defecto**; se mantiene en F1 hasta resolver bloqueos materiales para las operaciones dependientes. La captura histórica existente no debe perderse; en F2 se terminará su conciliación.
