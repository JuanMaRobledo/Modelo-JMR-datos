# DUOL · DUOL-20261104-A12-R3 · FASE_3 · CERRADA CON CONTROLES PENDIENTES

Fecha: 4-nov-2026 (Colombia). Método A-1.2; REGLAS v33; corte contable 30-sep-2026 y fuentes publicadas hasta 3-nov-2026. Estado: **CANDIDATO**, sin promoción. Ejecución: ChatGPT Work / Codex; identificador exacto de modelo y esfuerzo no expuestos por el entorno. No se declara auditoría independiente.

**AISLAMIENTO=OK.** La única valoración publicada sigue siendo DUOL-20261103-A12-R2, Base139,1086857874 y MOS90,4206457618. Se confirmó que su B35 no cambió.

[Copia R3 de trabajo](https://docs.google.com/spreadsheets/d/1TdXRa1f1HL5JusQV3LDgEnb4GWKYXEbVd6lhQjGSqQA/edit?usp=drivesdk), en la misma carpeta DUOL que R2. Conserva las 62 pestañas heredadas, sin intentar compactarlas ni tocar plantillas. Es copia del modelo vigente para revisión de supuestos, no reconstrucción de F1.

**PASOS: 8/10 ejecutados completamente; 2/10 parciales (múltiplos y gate integral).** Los pasos 0–5, 7 y 8 de F3 tienen revisión/evidencia; 6 y 9 mantienen pendientes indicados abajo. Los juicios con reserva no se presentan como datos verificados.

## Resultado de la revisión

| Resultado | R2 publicada | R3 candidata | Cambio |
|---|---:|---:|---:|
| DCF FCFF Base USD/acción | 139,1087 | 134,8958 | −3,0285 % |
| Precio con MOS35% USD/acción | 90,4206 | 87,6823 | −3,0285 % |
| CAGR de ingresos años 1–5 | 14,2705 % | 13,6378 % | −0,6328 pp |
| Ingresos año 5, USD millones | 2.303,55 | 2.240,47 | −63,08 |
| Ingresos año 10, USD millones | 3.253,27 | 3.090,56 | −162,71 |

Estas cifras mantienen las tasas y el puente financiero heredados mientras se cierran las reservas. **No son el resultado de una valoración completamente aprobada.** El precio128 del3-nov se conserva únicamente como referencia histórica del análisis y DCF inverso; no es cotización actual ni señal de inversión.

## De la historia a los supuestos

La carta Q3 anuncia el retiro de Max y Video Call en Super. La copia corrige las cuatro historias y elimina la dependencia de crecimiento por un nivel Max premium. También distingue margen EBIT económico de EBITDA ajustado y evita tratar crecimiento de DAU como crecimiento de ingresos. Fuentes primarias al final.

La nueva Base usa crecimiento de suscripciones = (1 + crecimiento de audiencia) × (1 + mejora relativa de penetración) × (1 + monetización por pagador) − 1. Todos los motores futuros son juicios explícitos, no guía empresarial ni datos de cohortes. La penetración no se calcula dividiendo pagadores al cierre por MAU promedio; ambos períodos y conceptos son diferentes.

| Motor anual | Año1 | Año2 | Año3 | Año4 | Año5 | Juicio y contraevidencia |
|---|---:|---:|---:|---:|---:|---|
| Audiencia MAU | 13 % | 14 % | 12 % | 10 % | 8 % | Ancla Q3 +13%; mejora año2 por mayor uso, seguida de desaceleración. Más actividad diaria puede no atraer más pagadores. |
| Penetración de pago, mejora relativa | 1 % | 1 % | 1 % | 1 % | 1 % | Hipótesis modesta, no +1pp. No hay serie de cohortes que la certifique. |
| Monetización por pagador | 2 % | 2 % | 2 % | 2 % | 2 % | Hipótesis nominal de precio/mezcla; retiro de Max limita la evidencia de premiumización. |
| Publicidad | 0 % | 8 % | 10 % | 8 % | 6 % | Año1 plano ante caída trimestral ligera; recuperación posterior es juicio. |
| DET | 0 % | 2 % | 3 % | 3 % | 3 % | No supone una expansión fuerte del negocio de pruebas. |
| IAP y otros | 0 % | 10 % | 10 % | 8 % | 5 % | Nuevas colecciones pueden ayudar; caída reciente impide dar el éxito por realizado. |

En la copia, entradas y fórmulas del soporte están en `Tesis de Inversión y Supuestos!A49:H80`. `Escenarios e historias!C24:G27` conserva la estructura ingreso previo × (1+crecimiento), sustituyendo las tasas embebidas por referencias al soporte. No se escribieron resultados calculados sobre fórmulas DCF.

La proyección es una aproximación por motores con base LTM; los MAU trimestrales son ancla de juicio, no un modelo validado de ingresos reconocidos por cohorte. El rezago de bookings a ingresos debe comprobarse con próximas observaciones.

## Drivers Base anterior → nuevo

| Driver | Anterior | Nuevo | Decisión / evidencia / celda |
|---|---:|---:|---|
| Crecimiento años1–5 | 14,2705% CAGR | 13,6378% CAGR | CAMBIAR; motores anteriores sustituidos por soporte explícito. EscenariosC29:G29. |
| Margen año1 / objetivo | 23% /28% | 23% /28% | MANTENER CON RESERVA; LTM ajustado22,3% exige mejora de5,7pp, sin usar EBITDA ajustado como EBIT. InputB28, EscenariosD5. |
| Convergencia del margen | 5 años | 5 años | MANTENER CON RESERVA; no se modifica fórmula; escala debe superar costesIA y remuneración. |
| S/C1–5 /6–10 | 1,9 /2,3 | 1,9 /2,3 | RESERVA; falta ancla marginal plurianual contablemente homogénea. EscenariosE5:F5. |
| WACC inicial /terminal | 10,4930% /9,5% | Sin cambio | RESERVA; revisar fecha/composición ERP y par mensual frente al dato diario. CostofcapitalB14, InputB47. |
| g terminal | 4% | 4% | MANTENER; menor que Rf4,91% y WACC. |
| ROIC terminal | 15% | 15% | RESERVA; inversión nueva distinta del promedio año10. No se aumenta para sostener precio. EscenariosG5. |
| Probabilidades B/C/O/D | 40/25/25/10 | 40/22,5/22,5/15 | CAMBIAR a previa JMR de alto crecimiento: no hay ajuste válido de5pp que justifique el reparto anterior. EscenariosB5:B8; efecto Base/MOS=0. |

Con las probabilidades corregidas, promedio condicionado C/B/O=139,9034. No es el valor principal ni la esperanza de todos los desenlaces. Conservadora92,8903; Optimista195,8189; Disrupción56,9369, todas conservadas numéricamente y sujetas a sus reservas. No se inventaron nuevos disparadores para justificar pesos.

## Objeción fuerte y sensibilidad material

La principal objeción es que más audiencia no produzca mejor penetración o monetización. En Google Sheets se pusieron temporalmente en cero ambos motores, se leyó el DCF y se restauraron los diez inputs a sus valores previos. Resultado nativo y cálculo independiente:120,2472, MOS78,1607, −10,8592% respecto a la candidata.

| Prueba completa de diez años + terminal | DCF USD/acción | Impacto vs candidata |
|---|---:|---:|
| Margen objetivo26% | 127,0896 | −5,7869% |
| Margen objetivo30% | 142,7020 | +5,7869% |
| S/C1,5→2,0 | 132,1526 | −2,0336% |
| ROIC terminal=WACC9,5% | 120,7681 | −10,4730% |
| ROIC terminal11,5% | 127,4690 | −5,5056% |
| WACC+0,5pp en toda la curva | 125,5015 | −6,9641% |
| NOL0, solo alternativa inferior | 134,4203 | −0,3525% |

Lag0 frente a lag1:134,9830 frente a134,8958 (+0,0647%), recalculando diez años y perpetuidad. Se mantiene lag1: no hay prueba causal que justifique cambiarlo por valor. No se modifica el selector nativo.

DCF inverso al precio histórico128: delta aditivo común a las cinco tasas iniciales = −1,353320853pp; CAGR geométrico implícito12,2843%. Reconstruye128 con error<1e−10, manteniendo forma de trayectoria, transición6–10, reinversión y terminal. No usa crecimiento constante ni un factor sobre el valor.

## Controles ejecutados y límites

| Control | Resultado | Alcance |
|---|---|---|
| Reproducción independiente R2 | APROBADO |139,1086857874 exacto; no usa factor de calibración. |
| Hoja R3 = cálculo independiente | APROBADO |134,8958020588; MOS87,6822713382. |
| Motor Base preservado | APROBADO PARCIAL |194 fórmulas A1:M45 idénticas. No equivale a diff completo de62 pestañas contra maestra. |
| Prueba nativa de motores y restauración | APROBADO |120,2472232149 con motores de monetización0; luego vuelve a134,8958020588. |
| Tres matrices DCF5×5 | APROBADO ARITMÉTICO, RESERVA DE CONTRATO |75/75 celdas replicadas, error máximo1,42e−13; centros coinciden. Primera matriz desplaza WACC completo, no solo terminal. Columna g5% excede Rf4,91% sin marcar inválida. |
| Cinco centros de múltiplos | APROBADO ARITMÉTICO |EV/EBITDA103,4877; EV/FCFF82,4804; P/E24,6528; P/FCFE18,9225; P/OCF20,0214. Centros=VP3. No certifica anclas ni denominadores. |
| Candados nativos |15/15 muestran estado admitido |El archivo vigente de candados enumera15, aunque textos antiguos dicen18. Leer una etiqueta heredada no verifica sus fuentes ni sus premisas. |
| Historias |4 COMPLETA; Base probableSí |Completitud estructural; reservas económicas quedan escritas. |
| Tasas y puente financiero |PARCIAL |Fuentes recuperadas y alternativas cuantificadas; conciliaciones pendientes. |
| `controles_todas.sh`, `diff_formulas_plantilla.py`, integridad y estados completos |NO EJECUTADOS como comandos oficiales |Se usaron lecturas nativas y verificaciones equivalentes acotadas. No se dispone en esta ejecución del repositorio/mapeo y autenticación CLI de Sheets del motor para ejecutar su cadena oficial sobre la copia. No se presume aprobado. |
| Formato |VERIFICADO POR API |Área nueva con fórmulas, porcentajes, ajuste de texto, encabezados y altura de filas. No render Google ni inspección visual completa. |
| Publicación / auditoría |NO EJECUTADAS |F3 no publica ni emite auditoría independiente. |

El script `node verificar_revision.mjs` comprueba los resultados contra los valores nativos archivados en `REVISION_SUPUESTOS.json`. Es una comprobación aritmética reproducible, no una implementación de los gates oficiales de promoción.

## Reservas que deben resolverse antes de F4

1. **Tasas.** R2 usa Rf4,91% disponible al corte y ERP4,2%. NYU publica para1-nov ERP4,41% y Rf de su modelo5,29%, mientras FRED da4,91% para2-nov. Distinguir tasa usada por el modelo mensual de cotización diaria; elegir y documentar un corte coherente conforme §4, sin mezclar primas o escogerlo por precio. La pareja mensual aplicada como diagnóstico produce128,3038; cambiar solo terminal aRf+ERP heredados9,11% produce140,9072. Son alternativas materiales, no correcciones aplicadas. También falta conciliar la composición geográfica de la prima directa.
2. **Margen, reinversión y persistencia.** Identificar referencias maduras equivalentes y el puente contable de margen28%; reconstruir inversión económica marginal con períodos homogéneos y justificarROIC15% frente aWACC9,5% y año10. Las sensibilidades muestran que estas hipótesis importan.
3. **NOL.** El saldo111,199m es heredado, sin roll-forward fiscal al30-sep validado. El casoNOL0 no prueba su límite superior ni valida ese saldo. No sustituir falta de desglose por cero.
4. **Arriendos y opciones.** Conciliar deuda corriente/largo plazo y cronograma del conversor. La carta confirma50,8m diluidas con opciones/RSU/founder: no restar opciones además bajo esa representación. La nota de Input se corrigió para no afirmar que no existen opciones. Revisar representación económica y remuneración futura sin doble conteo.
5. **Múltiplos.** Verificar anclas históricas/ciclo y normalizaciónEBIT/GAAP, impuestos ySBC. El cuadre de centros no acredita su pertinencia económica. Las mediasVP1–3 son distintas deVP3; no mezclarlas.
6. **Mantenimiento técnico.** Corregir matrizWACCterminal/g y estados inválidos como mantenimiento separado con regresión; conciliar el control DisrupciónB92=58,9660 con motorH7=56,9369, asociado a tratamiento de liberación de capital. No se arreglaron fórmulas estructurales por iniciativa de esta revisión.

**Siguiente ejecución:** resolver estas reservas sobre R3 con la misma información/corte; ejecutar cadena oficial contra el ID candidato sin apuntar por error aR2; actualizar registros y análisis únicamente con salidas nativas de esa revisión. R2 continúa como única referencia del catálogo hasta pasar promoción. La existencia de R3 no prueba publicación.

## Fuentes primarias

- [Carta Q3, publicada3-nov-2026](https://www.sec.gov/Archives/edgar/data/1562088/000162828026069474/q3fy26duolingo9-30x26share.htm): estrategia de suscripción, métricas y guía.
- [10-Q30-sep-2026, notas3/5/8/9 y estados](https://www.sec.gov/Archives/edgar/data/1562088/000162828026069692/duol-20260930.htm): ingresos por línea, impuestos, SBC/derechos e inversiones.
- [FRED DGS10](https://fred.stlouisfed.org/series/DGS10/query/tables): dato2-nov4,91%, publicado3-nov; dato3-nov se publicó4-nov y no se introduce retroactivamente.
- [Damodaran, tabla ERP mensual visible1-nov](https://pages.stern.nyu.edu/adamodar/New_Home_Page/home.htm): par de inputs del modelo mensual; no se identifica con el rendimiento diario observado.
- [Reglas y guía v33 del JMR](https://github.com/JuanMaRobledo/Modelo-JMR/blob/65f28001d3d94d2322b0742385b99f3e8ab846f3/docs/HISTORIAS_A_NUMEROS.md).

Las cifras prospectivas, rangos y decisiones de este expediente son juicios del analista apoyados en esas fuentes, no previsiones publicadas por el emisor ni por Damodaran.
