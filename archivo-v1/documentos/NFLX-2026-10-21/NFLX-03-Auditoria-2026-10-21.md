# Netflix: auditoría de esta corrida

Fecha:21-oct-2026. Dictamen: aritmética y conexiones principales verificadas; **con salvedades de datos y metodología**. No corresponde declarar validación económica integral ni auditoría sin reservas.

## Alcance demostrado

- Diez cierres2016–2025 más2015 auxiliar y balances comparables de septiembre. LTM de flujos separado de saldos.
- Cuatro DCF con fuentes e hipótesis propias. Base48,33563427, promedio47,61973690 y disrupción14,77933234.
- Siete métodos relativos, horizonte1–3 años, descuento a Ke y pesos editables; principal separado del DCF.
- Tres sensibilidades DCF con75 celdas contrastadas,28 matrices relativas y centros de las dos familias reconciliados por ancla.
- DCF inverso reproducido en Python y Sheets, residuo menor aUS$0,000001.
- 124 controles numéricos independientes aprobados.7.528 celdas de fórmula y cero errores almacenados en exportación final.
- 24 reglas de validación originales de Inputs conservadas. Cambios reales de margen inicial y desfase alteran resultados correctamente, con restauración del Base.
- Estados y módulo principal renderizados para inspección; se retiró un gráfico heredado que mezclaba zonas viejas y se reconstruyó la portada sin superposiciones.

## Hallazgos corregidos

1. BPA básico utilizaba acciones diluidas en el importador: se separaron denominadores y se conservaron posiciones de años sin dato.
2. Algunos faltantes se convertían en cero: extracción nueva conserva nulos/estados y la hoja identifica partidas agrupadas.
3. Industria global apuntaba al rango US en un trabajo previo: la copia actual mantiene validación hacia la tabla global.
4. WBD estaba descrito como pago: la nota6 del10-Q confirma recepción deUS$2.800 millones.
5. Tecnología/opex2016–2019 no conciliaban con EBIT: se sustituyeron por los estados consolidados, no por un residuo de ajuste.
6. Etiquetas de emisión de deuda y opciones no estaban recogidas: se ampliaron con etiquetas específicas y se actualizaron agrupaciones del flujo financiero.
7. El desfase y margen inicial debían afectar el cálculo real: pruebas en la hoja confirmaron la dependencia y su igualdad con el motor independiente.

## Salvedades que permanecen

| Tema | Tratamiento y límite |
|---|---|
| Plazo de opciones |4,5 años estimados; dato publicado anterior4,79 años. No plazo exacto Sep2026. |
| Impuesto de WBD | Normalización al25% supuesto; falta efecto fiscal exacto atribuible. |
| CRP y Kd | Hipótesis explicadas; no estimación exhaustiva país por país ni curva de deuda al instante. |
| S/C | Ancla de rotación sectorial total usada como supuesto marginal; su equivalencia no queda probada. |
| Goodwill/activos e impuestos agrupados | N/P con grupo de origen; no inferir inexistencia. Algunos ratios quedan N/P. |
| FCFF/OCF históricos | Puente económico normalizado; posibles diferencias caja/devengo. No mezclar con series genéricas FCF. |
| Comparables | Contraste forward P/E disponible, sin certificación homogénea de siete denominadores de peers. |
| I+D | Tecnología y desarrollo no permite aislar I+D elegible; no capitalizada en Base. |
| ROIC terminal | Ventaja persistente es hipótesis; conservadora converge a WACC. |
| Prompt v5 recuperado | Se revisó la versión vigente del repositorio; quedan requisitos económicos sin certificación integral, detallados abajo. |

No se deben quitar estas reservas al publicar o resumir los resultados. Las124 pruebas validan lo que identifican; no convierten las estimaciones en hechos.

## Evidencia y reproducción

verification-final.json contiene124 pruebas, expected/actual/diferencia. valuation.json contiene las cuatro proyecciones y sensibilidades. normalized.json retiene dato fuente y sustituciones. Los scripts preservan la ejecución de la corrida; final-readback.json y la hoja contienen las lecturas nativas verificadas. El historial anterior no es fuente de inputs.

Estado de publicación: expediente autorizado para la app, conservando esta auditoría como documento narrativo independiente. La hoja está vinculada al registro vigente.


## Revisión previa a publicación del 21-oct-2026

Se recuperaron los prompts vigentes de valoración v5 y research v5. Se reorganizó el artículo en sus18 apartados, con Porter y síntesis final; la recuperación del texto resuelve la ausencia documental, no certifica automáticamente todas sus exigencias.

Se retiró una tabla heredada de cinco métodos cuyos pesos no correspondían al bloque vigente de siete. El consolidado relativo actual es US$50,60031180. Se restauraron28 fórmulas críticas contra la maestra de solo lectura: beta desapalancada mediante fórmula canónica, controles de cuatro historias y puente por acción. La beta directa quedó como entrada numérica equivalente, evitando circularidad. El precio D1 quedó fijo. Se añadió Crecimiento implícito como vista enlazada al motor existente.

El auditor de presentación tenía un defecto de alcance: trataba las matrices relativas como si sus centros debieran igualar el DCF. Se corrigió para comprobar las tres matrices DCF; las relativas conservan controles propios. La corrección no cambia ningún centro. El preflight de20 comprobaciones, las28 fórmulas críticas y el contrato de17 pestañas pasan. Los124 controles independientes siguen aprobados;7528 celdas de fórmula, cero errores almacenados. El estado técnico CERTIFICADO del preflight corresponde a estructura/entradas, expresamente no a exactitud de fuentes ni juicio económico.

Las28 matrices relativas corresponden al Base:7 métodos ×2 anclas ×2 familias. No se presentan como21 centros para tres historias; el registro declara7 centros Base comprobados y14 no disponibles en las otras historias. La proyección de precios de los siete métodos sí existe para las tres historias y sus tres horizontes.

### Revisión explícita de los controles del prompt v5 (§7)

| Control | Resultado y alcance |
|---|---|
| 0. Inputs y candados | Preflight estructural pasa; no se ejecutó el inventario histórico completo de inputs_completos.py. No se declara equivalente. |
| 1. Segmentos, CAGR, caja/deuda/acciones | Conciliación consolidada y denominadores verificados; no se presenta una valoración segmentada granular ni certificación de cada línea no desglosada. |
| 2. Terminal | g≤Rf y g<WACC en los cuatro casos; PV terminal Base54,56%. |
| 3. ROIC y ventaja | Hipótesis causal explicada; persistencia12%/15% no verificable como hecho. Conservadora y Disrupción convergen a WACC. |
| 4. Márgenes | Optimista supera Base en2pp; no se certificó un panel homogéneo de pares maduros ni toda la regla sectorial2,5×. |
| 5. Probabilidades |50/25/10/15 suman100%; son juicios. No se reconstruyó una previa estadística independiente y ajustes empíricos. |
| 6. Anclas y comparables | Targets explícitos e independientes del DCF; pares incompletos. No se declara certificada la restricción universal contra anclaC. |
| 7. MOS |35% aplicado únicamente al DCF Base:US$31,41816227. |
| 8. Etiquetas y faltantes | Fuentes, cálculos y supuestos se distinguen por campos y notas; N/P permanece visible. No se certifica etiquetado literal de cada cifra del expediente. |
| 9. Aislamiento | Registros generados solo desde esta copia NFLX y sus fuentes; comparables externos identificados como tales. Fórmulas maestras leídas sin modificar la plantilla. |

Por ello el dictamen sigue siendo **calculada con salvedades**. La autorización del usuario permite publicar el expediente para revisión con estas limitaciones; no se cambia el dictamen a auditoría económica integral.

### Opciones: sensibilidad del plazo estimado

Mismos spot, strike, sigma y tasa; solo cambia el plazo. No constituye una nueva medición del vencimiento.

| Plazo (años) | Derecho de opciones (USD millones) | DCF Base (USD/acción) |
|---|---|---|
|3|3872.30|48.4375|
|4.5|4290.87|48.3356|
|4.79|4364.13|48.3178|
|6|4647.60|48.2488|

### WBD: sensibilidad del impuesto supuesto

NI LTM reportado14.766,653 millones menos2.800×(1−tasa). Con20%,25% y30%, NI normalizado resulta12.526,653 /12.666,653 /12.806,653 millones. El ajuste de esta ganancia no recurrente está fuera del EBIT del DCF; estas diferencias no se incorporan como crecimiento operativo. El impuesto exacto sigue N/D.
