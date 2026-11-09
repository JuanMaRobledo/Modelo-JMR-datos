# UBER-20261030-A1 · conciliación 1-nov-2026

Estado: EN_REVISION con reservas materiales; auditoría económica pendiente.

## Resultado

La hoja y el registro conservan DCF presente 91,13793738151752 USD/acción y MOS35% 59,239659297986385. La entrada de ponderación del perfil seleccionado en esta hoja (Software, S6:S11) pasa de 60/10/15/5/5/5 a 100/0/0/0/0/0. Las fórmulas de pesos permanecen. El resumen rápido referencia DCF presente y MOS; la tabla superior identifica expresamente su horizonte FY+3. Su DCF capitalizado es 123,2155948871006; el antiguo mixto 122,14190277410978 no representa el valor presente oficial.

Descuento de múltiplos C6 selecciona «Solo 3 años», opción ya existente, para conciliar el consolidado con VP3 del JSON provisional. No se alteran ingresos, márgenes, S/C, NOL, tasas, ROIC, opciones ni matrices.

Las cinco matrices relativas existen y se capturan con fórmulas y valores. VP3: EV/EBITDA y EV/FCFF 95,3890749375087; P/E, P/FCFE y P/OCF 78,75824385882007. Todas tienen peso cero y anclas no certificadas. No son confirmaciones independientes.

`lectura-hoja.json` conserva la lectura intermedia; `lectura-final.json` contiene la recaptura final tras seleccionar Solo 3 años. SHA256 de esta última en `conciliacionHoja` del registro. La evidencia anterior `evidencia/reconciliacion-hoja-json-20261101/UBER.json` se conserva como diagnóstico previo, no como estado actual. La prueba nueva compara la captura final con registro y análisis, no solo con valores escritos a mano.

## Reservas que permanecen

| Punto | Evidencia disponible | Evidencia mínima pendiente |
|---|---|---|
| Ingresos no operativos | Financials Multiples E50 extrapola 53,5653% del EBIT | Normalizar ganancias de inversiones frente a intereses recurrentes y revisar EBT/NI/FCFE. No se modifica una hipótesis económica en esta conciliación. |
| Anclas | J19 ligado a precio o a otro múltiplo; histórico sin alimentar | Cierres y denominadores homogéneos; elección por fundamentales FY+3; ausencia de circularidad. |
| Inversiones | 12.532 M proxy; prueba documentada sin ellas: DCF 85,00 (-6,73%) | Composición, fecha, valoración e impuestos, sin duplicación con flujos. Reserva material. |
| RSUs/SBC | 71,804 M; denominador bruto de contraste: 88,04 (~-3,4%) | Puente de acciones/derechos, gasto SBC, vesting y recompras. La sensibilidad bruta no es una valoración certificada. |
| ROIC | Año10 34,65%, terminal14%; alternativa terminal11%: 84,79 (-6,96%) | Explicar transición y comparar fade gradual; la prueba de nivel terminal no resuelve trayectoria. |
| NOL | 14.024 M; alternativa cero: 89,64 (-1,65%) | Conciliar evidencia fiscal pública, uso, restricciones e impacto acumulado. No exige certificado IRS. |
| Tasas | Detailed VALIDADO, beta1,2 | Rf/ERP de mismo corte, beta, deuda y geografía trazables. |
| Opciones | BSM197,41 M; sigma40% asumida | Rango razonable de sigma y materialidad; no confundir supuesto con observación. |
| Sensibilidad DCF | Primera matriz varía WACC inicial | Documentar el alcance frente al requisito de WACC terminal; no renombrar ejes como si fueran equivalentes. |

Las alternativas económicas son pruebas ya documentadas en Nivel 2, no nuevas ejecuciones. Impactos no se suman con signos opuestos ni se interpretan como probabilidades. Reservas materiales impiden declarar verificación económica completa, pero quedan expresas en el estado de revisión.

## Gate y límites de comprobación

PR209 sigue borrador histórico, pero el expediente ya estaba integrado en main al iniciar este trabajo. El run41354221137 del SHA35c005df6987926e9f5f70d96c357f44202a80d4 terminó success; ese dato no se propaga como resultado de otro SHA. El PR de esta conciliación debe pasar su CI propio.

Verificación local: catálogo, integridad, no regresión y profundidad Método A; suite Node y Python. El nuevo test concilia captura, DCF, MOS, pesos y cinco VP3.

Resultado local final: 98/98 Node y 30/30 Python aprobadas. `verificar_cierre_multiplos.py` falla en la identidad de revisión de una recaptura histórica (`verify_recaptura`, línea 82). El mismo fallo se reproduce ejecutando el script en un worktree limpio del SHA base09db23b918d15e7d4a120e17c43999aab15935e0. No se modifican identidades, hashes ni controles de otros expedientes para aprobar UBER. Esta reproducción local se distingue del run CI anterior aprobado.

La lectura de formato es una comprobación por API; no acredita inspección visual nativa a zoom normal. La presencia en catálogo no acredita despliegue ni acceso autenticado a la app. Esos límites permanecen en `conciliacionHoja` sin declararlos aprobados.
