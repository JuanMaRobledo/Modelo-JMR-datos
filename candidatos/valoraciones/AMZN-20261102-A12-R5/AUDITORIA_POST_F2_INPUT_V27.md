# AMZN R5 — Auditoría de integridad de Input sheet y continuidad de prompts (posterior a F2)
Fecha: 2-nov-2026. Estado: CONTROLES F1 ABIERTOS; la F2 de históricos no sustituye la calidad de captura de F1.
Hoja oficial https://docs.google.com/spreadsheets/d/199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I/edit
Regla activa JMR v27 https://github.com/JuanMaRobledo/Modelo-JMR/blob/main/docs/propuestas/fases/CONTRATO_INSUMOS_FASE_1.md
Prompt maestro anterior conservado https://github.com/JuanMaRobledo/Modelo-JMR/blob/main/docs/prompts/valoracion-modelo-jmr-v5.md

## Hallazgo y reparación concreta
| Celda | Estado antes de esta revisión | Corrección / interpretación actual | Efecto |
|---|---|---|---|
| Input B9 / B10, industria US/Global | VACÍAS pese a existir tarifas sectoriales | Referencia Retail (General) US/Global; **no** se usa como beta única ni sustituye modelo Multibusiness de Retail + AWS | Activa comparativos J/K de industria, sin cambios DCF |
| Input B30 margen objetivo de referencia | FÓRMULA SIN RESULTADO por B9 vacío y cohorte Sector N/D | Fórmula original preservada; ahora 10,64%, mediana de benchmark y margen primer año. **NO es el margen objetivo de cada escenario** | Comparativo informativo, no nuevo supuesto |
| Input B32/B33 Sales-to-Capital referencia | FÓRMULAS EN BLANCO por B10 vacío | Fórmulas conservadas B32=K28, B33=B32, hoy ~2,7255 INDUSTRIA Global. **No confundir** con Sales-to-Capital Base marginal 0,72 años1–5 y 1,65 años6–10 de Escenarios!E5/F5 | No impacta cuatro DCF; etiquetas antiguas pueden confundir: issue de regresión |
| Input B49=Yes con B50 sin ROIC de referencia | Referencia CONDICIONAL FALTANTE | B50 = fórmula a 'Escenarios e historias'!N5 (Base 11,5%); cada escenario conserva su ROIC propio N5:N8 | No cambia valores ni historias |
| Cost of capital worksheet B49 (preferentes) | VACÍA con ausencia SEC demostrada | B49=0 acciones preferentes emitidas; B50/B51 precio/dividendo dependientes N/A | WACC y DCF inalterados |

## Blancos que sí son condicionales (no llenar con 0 inventado)
- Input B39:B42 opciones sobre acciones propias si B38=No (no equivale a ausencia de RSU/SBC).
- Input B53 probabilidad de fracaso con B52=No; B63 NOL utilizable con B62=No; B66 Rf alterna con B65=No; B72:B73 cash atrapada con B71=No.
- Input B78 valor de solapamiento converter solo obligatorio cuando B18=Yes; B79:B81 calculan NO APLICA para conversión incremental por ASC842 ya reconocido.
- Input B94 solo cuando B89=Excepción, no B89=Normalizada; Cost of capital B50/B51 solo si B49>0 preferentes, y resto campos de métodos no seleccionados.
Los valores condicionales están vacíos intencionalmente; las notas y control de casos especiales explican N/A. Se recomienda UI con etiquetas de estado en vez de celdas sin descripción.

## Elementos obligatorios del PROMPT MAESTRO v5 que NO se han demostrado plenamente
1. Cohorte 5–10 pares comparables (retail y AWS por separado), márgenes y outside-view con datos de igual corte: 'Sector!A3:N11' vacía, 'Crecimiento y Márgenes!E15:E20' = N/D. B9 y B10 son solo benchmark, NO reemplazan peers.
2. Prima riesgo país por regiones de ventas: Cost of capital worksheet B26=Will input 3,70% prima madura sin puente detallado de ponderación geográfica; revisar materialidad. WACC Detailed Multibusiness sí usa Retail+Computer Services.
3. Normalización de extraordinarios en PE/FCFE, anclas FY+1/2/3 y sensibilidad cinco múltiplos. EV/EBITDA y P/OCF siguen candidatos; PE, EV/FCFF, P/FCFE N/D o N/A. Proyección 'Interest / Other' en Financials Multiples arrastra base histórica con plusvalías financieras; no convertirlo a recurrencia.
4. Verificación de 8-K y comunicados entre últimos reportes y corte: no hay constancia de cotejo exhaustivo. DCF inverso y 18 candados oficiales: no hay evidencia de ejecución formal con runtime. inputs_completos.py NO EJECUTADO.
5. Auditoría económica final de deuda market/leases (motor #197), RSU vs SBC, opción valor, I+D proxy y participaciones Level3. Quedan para verificación, NO validadas por K5:K8=LISTO.

## Revisión posterior a las escrituras
- DCF Base permaneció USD149,19148575564947/acción; Conservadora81,0095172, Disrupción62,4357315, Optimista241,8435161. Costo capital B84=VALIDADO estructural.
- Verificado 'Input sheet' B9/B10 selectores, B30=0,1064313649, B32/B33=2,7255166819, B50=0,115; Cost of capital B49=0. Solo celdas de referencia e índice, ningún driver de historias alterado.
- No se tocó plantilla IA maestra, app, JSON ni valoración publicada. PR #234 permanece draft.
- Issue transversal de no regresión: https://github.com/JuanMaRobledo/JMR-valuation/issues/200. Requiere ejecutar inputs_completos.py y matriz por entrada ANTES de declarar F1 cerrada, con exclusión condicional legítima. Issues #197 y #199 siguen abiertos.

**Dictamen:** la Fase 2 de diez años está documentada, pero la captura F1 inicialmente dejó huecos no justificados. Se corrigieron los identificados sin rehacer escenarios. La fase F1 NO puede llamarse certificada ni sin reservas: la cohorte y la prima geográfica/excepciones materiales continúan abiertas. No iniciar publicación ni afirmar que los scripts oficiales corrieron. F3 deberá revisar economía, pero control de cobertura F1 es anterior y no desaparece por cambiar de fase.