# GOOGL · prueba Codex · corte de información 29-oct-2026

**Estado: PENDIENTE, NO PUBLICADO. Entrega parcial de diagnóstico; las ocho fases NO están completadas.**

Este expediente no sustituye GOOGL-20261029-R5. No se modificaron el catálogo, las valoraciones/análisis activos, las hojas publicadas, las reglas ni el motor. No debe importarse automáticamente a la aplicación. No contiene dictamen de auditoría económica JMR.

## Resultado que sí está demostrado

Los FCFF y el puente capturados de la hoja R5 reproducen aritméticamente **US$287,20493379569**, y MOS35% **US$186,68320696720**. Esto verifica la suma y el descuento de salidas guardadas; **no equivale a reproducir la valoración desde sus entradas en una copia intacta de la plantilla oficial**.

La hoja R5 tiene **48 pestañas**, frente a las **46** de la plantilla vigente. En los rangos comunes efectivamente capturados hay **52 diferencias respecto a celdas que contienen fórmulas en la plantilla**; diez aparecen sustituidas por un literal o vacío. El inventario contiene ambas versiones y la dirección exacta de cada celda. No se extrapola esta revisión acotada a todo el libro.

Las diferencias incluyen `Valuation output!C6:L6` (margen con depreciación incremental por cohortes), `C9:M9` (ajuste fiscal de I+D), `C10:L10` (reinversión sustituida por puente propio), capital invertido/ROIC y fórmulas de Input. Las pestañas adicionales son `Puente CAPEX ROIC` y `Cohortes IA 2026`. La reproducción pedida exige simultáneamente conservar las fórmulas oficiales y conservar el motor particular R5: ambos motores observados no son idénticos. No se cambian supuestos para ocultarlo.

**Hallazgo localizado:** `Puente CAPEX ROIC!C32:L32` multiplica el gasto previsto por `'Cohortes IA 2026'!$L$3 = 85%`; `M32` usa `='Valuation output'!M5*M31`, sin ese factor. Pasa a capitalizar 100% en el terminal sin explicación en esa fórmula. Afecta el escudo fiscal terminal; aplicar únicamente el factor omitido y propagar su efecto con el resto fijo reduce el valor en **US$3,25972741273**. El diagnóstico resultante **US$283,94520638296 no es una nueva valoración**, ni una corrección oficial: faltaría conciliar EBIT GAAP/ajustado, amortizaciones y reinversión del estado estable simultáneamente. La hoja R5 permanece intacta.

## Identidad, fuentes normativas y versiones

| Elemento | Identidad verificada |
|---|---|
| Emisor / acción | Alphabet Inc. / GOOGL clase A |
| Corte solicitado de información | 2026-10-29 |
| Período contable de R5 | LTM 2026-09-30; el JSON llama `fecha_corte` al cierre contable |
| Revisión activa | `GOOGL-20261029-R5`, resuelta en `catalogo.json` |
| Hoja activa leída | [R5](https://docs.google.com/spreadsheets/d/1we5M6ZMziOkTVHttcQWoerKhYqbQoWAbkoGeDZfb7bA/edit) |
| AZ existente leído | [AZ R4](https://docs.google.com/spreadsheets/d/1XF1Rszivh_ADnJnNIJTJ6yAkVz8sh6nagNCMUMyauMg/edit) |
| Plantilla IA oficial | `1e-lbQmCkObfq74YLpWnMmIidmcdsJQ-6uN4oiHnNTEQ`, 46 pestañas |
| Copia nueva creada | [Copia de trabajo, pendiente](https://docs.google.com/spreadsheets/d/11HPn4cb1knp1l_VyxnHe5DHdtnM23x1fpZ6-AT9wZok/edit) |
| Contenido de la copia | Plantilla sin supuestos empresariales cargados; solo nota de estado en `Origen de los Supuestos!A3` |
| Método solicitado | A / A-1.2; no se declara ejecutado por poner la etiqueta |
| Rama aislada | `codex/googl-repro-a12-20261029` |
| Modelo-JMR leído | `ea97e14938f93e5ea2758e01e020748628e0f209` |
| JMR-valuation leído | `63de54caf28cab837e0acbc156004ae85ffdbb1a` |
| Modelo-JMR-datos inicial | `0be4fbdc587afd23efd0cc30c7204ae2910d3c21` |

Precedencia aplicada: `REGLAS_VIGENTES.md` v17 → selector de métodos y A-1.2 para calibración → proceso único → prompts oficiales de valoración y research. Reglas comunes §§4A, 4B, 4C, 6, 9 y 11 y A §§A.5.1, A.5.2, A.9 y A.11. La instrucción expresa del usuario de preservar R5 prevalece sobre el flujo ordinario de sustitución en catálogo. No se crea una excepción tácita al motor para conseguir coincidencia.

## Fase 1: conciliación aritmética, no reproducción integral

Cifras monetarias en millones de USD; acciones en millones. Valores sin redondear disponibles en JSON.

| Puente | Importe |
|---|---:|
| VP FCFF explícitos | 688.564,611067 |
| VP terminal | 2.602.921,845017 |
| EV | 3.291.486,456084 |
| Menos deuda y leases | −141.917 |
| Más caja y negociables | 265.098 |
| Más activos no operativos | 135.230 |
| Menos preferentes | −19.000 |
| Minoritarios / opciones en este cálculo | 0 / 0 |
| Equity común | 3.530.897,456084 |
| Acciones | 12.294 |
| Valor por acción | 287,20493379569 |

El valor terminal explica **79,0804% del EV**. El FCFF del primer año es −46.101,0473: NOPAT 170.721,4512 menos reinversión 216.822,4985. La reinversión se concilia con física neta 188.002,6195 e I+D neta 28.819,8790; no se suma además Δventas/S-C. Esta identidad no prueba que los componentes originales estén libres de solapamientos.

Las tasas capturadas son WACC inicial10,02501155%, terminal9,25%, g4%, ROIC terminal21%. Se conservan para la prueba histórica, aunque su razonabilidad o procedencia requieran revisión. Las acciones/preferentes convertibles, inversiones privadas y clasificación de caja tampoco quedan validadas por cerrar el puente.

La cabecera de R5 sigue diciendo GOOG y precio321,89, mientras el expediente GOOGL usa324,89 (28-oct). No se aplica una prima económica por el voto. La hoja ofrece DCF alternativos y promedio316,90 en celdas de historias, mientras el JSON los deja nulos por no estar homologados. No son escenarios R5 certificados y no se presentan como tales.

## Fases 2–4: investigación y calibración independientes pendientes

No se asigna un precio nuevo sin completar la evidencia y los cálculos nativos. Estas son las cuestiones concretas encontradas, no supuestos nuevos aprobados:

### Search y publicidad

La transcripción de la llamada del 28-oct informa Search63,3bn, +12%, con crecimiento de consultas y despliegue gradual de anuncios en interfaces IA. Más consultas no equivale a más ingresos al mismo margen: hay que separar intención comercial, porcentaje monetizado, conversiones, precio por conversión y coste por respuesta. Una respuesta generativa puede reducir clics pero mejorar conversión; ambas direcciones requieren evidencia. No existe en las capturas una serie homogénea que permita atribuir cuantitativamente el crecimiento a precio, volumen o cuota.

### YouTube

La misma llamada informa publicidad11,2bn, +9%, y más de150millones de suscriptores Music/Premium incluyendo pruebas. Publicidad y suscripciones tienen motores y costes distintos; el ingreso publicitario no representa todo YouTube. Hay que conciliar ingresos de suscripciones sin sumarlos otra vez a Services. Los pagos a creadores y derechos de contenido limitan la extrapolación del margen Search. Ingreso y beneficio por usuario, monetización de Shorts y televisión conectada requieren series verificables antes de fijar un margen separado.

### Cloud

La llamada informa ingresos30,7bn, +103%, margen36,2%, backlog561bn y reconocimiento esperado de algo más de55% en24meses. Son afirmaciones de dirección recogidas por un distribuidor de la transcripción; no constituyen verificación independiente de los contratos. El backlog puede aportar visibilidad, pero hay flexibilidad de precios/volúmenes y capacidad por instalar. Las ventas de sistemas TPU aportan ingresos con economía distinta al alquiler recurrente de cómputo. No se extrapola +103%; separar venta de hardware, servicios recurrentes, adquisiciones y capacidad de terceros es material.

### IA y monetización

La monetización ocurre en anuncios, Cloud y suscripciones, no en una cuarta bolsa de ingresos que pueda sumarse a las tres. Los indicadores de tokens y usuarios son uso, no beneficios. Un coste unitario menor puede ampliar el mercado y aumentar el gasto agregado. La ventaja de TPUs, distribución y modelos propios debe contrastarse con utilización, electricidad, eficiencia por generación y precios efectivos. Las métricas promocionales de clientes no sustituyen un RONIC de cohortes de inversión.

### Waymo y Other Bets

Other Bets presenta ingresos372millones y pérdida operativa cercana a2bn en la llamada. No se convierte la expansión geográfica de Waymo en un valor SOTP sin ingresos por viaje, costes, vehículos, seguros, propiedad y financiación verificables. Un valor opcional separado exige retirar de FCFF lo que se valore por otra vía y descontar participaciones de terceros. La valoración privada de una ronda no equivale al valor económico atribuible realizable.

### Infraestructura y centros de datos

La guía citada es CapEx2026 de195–205bn y aumento significativo en2027, sin cifra oficial para ese año. **240bn en2027 y 2,49billones en2027–2036 son hipótesis R5, no guía.** El65/35 describe inversión técnica del trimestre, no necesariamente todo el CapEx: servidores/redes con vida contable generalmente6años y centros con7–40años. La hipótesis90%técnico y vida25años no queda demostrada por esa divulgación.

CapEx mantenimiento no está divulgado como partida separada en la evidencia consultada. D&A contable no debe equipararse automáticamente a mantenimiento: calendario de altas, inflación del equipo, reutilización y obsolescencia cambian la relación. La nueva valoración requiere descomponer cohortes y capacidad prevista fuera del motor, traducirlas a reinversión total compatible con la plantilla y demostrar la conciliación. Tampoco procede imponer simultáneamente gasto bruto explícito más Δventas/S-C.

### Reinversión, ROIC y RONIC

La historia capturada contiene ventas de2016–2025 y LTM, pero muchas partidas de balance/caja están vacías y las acciones antiguas no están homogeneizadas por el split. No se considera reconstrucción independiente primaria. El0,52 de S/C marginal histórico del JSON no queda acreditado con una conciliación de períodos comparables; FY2025 frente a LTM septiembre2026 comparte nueve meses y no es un crecimiento interanual homogéneo.

Se debe reconstruir Δventas y reinversión sobre ventanas no solapadas y probar lags0/1 en ejecuciones completas. Las adquisiciones necesitan el ingreso incremental asociado y el capital pagado; los compromisos de compra futuros no son automáticamente deuda actual ni gasto adicional a todo CapEx proyectado. Los leases reconocidos, por comenzar y compromisos energéticos exigen tratamientos separados sin duplicación.

ROIC actual26,06%, año10 de23,10% y terminal21% son salidas R5. RONIC de IA separado sigue N/D: no hay asignación verificada de capital incremental y NOPAT por cohorte. Un retorno consolidado histórico alto no prueba que la próxima inversión en capacidad produzca igual retorno. Tampoco justifica forzar el terminal al promedio sectorial. La duración de la distribución Search y los costes de cambio Cloud son argumentos a favor de un spread; sustitución por agentes, competencia de precios y sobrecapacidad son evidencia contraria que debe cuantificarse.

### Tasas y terminal

R5 mezcla Treasury28-oct5,05% con ERP4,2% cuya fuente mensual requiere reconciliación. La búsqueda de Damodaran encontró una publicación primaria de8-oct que presenta ERP3,70% sobre Treasury5,29% (o3,92% sobre tasa ajustada5,07%) al inicio de octubre. También aparecen referencias secundarias contradictorias de4,20%. No se elige la cifra favorable: hay que descargar el corte mensual original y conciliar definición/fecha antes del WACC nuevo.

## Fase 5: qué se comprobó de AZ

Se reprodujeron **desde sus entradas propias capturadas**, sin importar supuestos JMR, los diez FCFF y la perpetuidad de las tres historias del AZ existente:

| Historia existente | Perpetuidad USD/acción | MOS35% comparativo |
|---|---:|---:|
| Conservador | 140,75059225637 | 91,48788496664 |
| Base | 218,81574042769 | 142,23023127800 |
| Optimista | 391,25560957913 | 254,31614622644 |

FCFF=EBIT_GAAP×(1−T)+D&A−CapEx−ΔNWC. WACC9,942174%, constante en los diez años; terminal Base usa NOPAT10×(1+3,5%)×(1−3,5%/16%). La identidad WACC desde Rf, beta, ERP, Kd, impuesto y pesos cuadra, sin certificar esos inputs. `Outputs!C10` usa esa fórmula, no FCFF10×(1+g). `Inputs!C80` conserva una explicación antigua incompatible con la fórmula actual; `C87` explica la revisión más reciente. Se debe dar prioridad a fórmula real y dejar documentada la discrepancia, sin editar la hoja existente.

La salida Base EV/EBITDA16× da371,459382 por acción en la hoja y sigue como referencia secundaria; el múltiplo16× no está validado contra pares en esta ejecución. El sitio público AZ describe perpetuidad/salida, pero eso no acredita que esta reconstrucción local sea la plantilla original completa de AZ. **No se certifica conformidad con fórmulas propietarias no obtenidas.** No se ha ejecutado una nueva valoración AZ con calibración independiente desde cero; este resultado es reproducción del AZ previo.

## Fase 6: comparación disponible y límites de atribución

| Solicitud | Valor intrínseco Base | Estado real |
|---|---:|---|
| GOOGL R5 publicado | 287,20493379569 | Aritmética reproducida desde FCFF guardados; motor difiere de plantilla |
| GOOGL nuevo A-1.2 | N/D | No ejecutado; no sustituir por sensibilidad283,95 |
| GOOGL AZ nuevo | N/D | No ejecutado; AZ existente218,815740 reproducido por separado |

| Driver | R5 existente | AZ existente | Lectura |
|---|---|---|---|
| Ventas iniciales / moneda |471.098m / USD|471.098m / USD|Igual ancla, no independencia de evidencia |
| Crecimiento años1–5 |18/17/15/13/12%|20/19/17/15/13%|AZ tiene mayor crecimiento |
| Ventas año10 |1.442.265,51m|1.543.950,66m|No confundir más ventas con más valor |
| Margen año10 |35,23094% ajustado|34% GAAP|No comparar directamente bases contables |
| I+D |85%capitalizable explícito; terminal100%|Gasto GAAP|Diferencia contable y de fórmulas material |
| CapEx10años |2.490.000m|2.655.000m Base|Trayectorias distintas y D&A muy diferente |
| D&A año10 |204.937,24m|103.000m|Necesita igualar vidas/perímetro y EBIT |
| ROIC/RONIC terminal |21%|16%|No presuponer comparabilidad de capital |
| WACC explícito |10,025%→9,25%|9,942%constante|AZ inicial menor, terminal mayor |
| g |4%|3,5%|Afecta crecimiento y retención estable |
| Puente EV-equity |+239.411m|+239.411m|**Aporte directo a la diferencia:0**, condicionado a mismos inputs |
| Acciones |12.294m|12.294m|**Aporte directo:0** |

La diferencia Base entre ambos expedientes existentes es **68,3891933680USD/acción**. No se atribuye íntegramente a CapEx ni a ROIC. Una descomposición monetaria de crecimiento, margen, reinversión, tasas y terminal requiere sustituciones completas, contabilidad homogénea y orden declarado o Shapley: hay interacciones. No se realizó; la tabla es comparación de hipótesis, no atribución causal cuantificada. La sensibilidad local de3,26 de I+D terminal tampoco explica toda esa diferencia.

## Fase 7: no se entrega research completo

El contenido anterior es un memorando técnico y económico, **no el artículo fundamental de18secciones y dos niveles**. Faltan historia primaria completa y ROIC ajustado homogéneo, pares, gobierno/incentivos actualizado, análisis íntegro de las18secciones con cobertura semántica, y cifras de la valoración nueva. No se reutiliza el artículo activo como si fuera trabajo nuevo ni se le ponen18títulos a esta nota para simular cumplimiento.

## Fase 8: pruebas, límites y reproducción

Desde la raíz de `Modelo-JMR-datos`:

```bash
python3 documentos/GOOGL-CODEX-20261029/comprobar.py
```

El script no tiene dependencias externas, no conecta a internet, no escribe en Sheets y no genera una valoración JMR alternativa. Produce `resultados-controles.json`, inventario de fórmulas y hashes de capturas. **10 controles acotados aprobados,2fallidos,7no ejecutados**. Hay además17tests de repositorio aprobados:6decontrato de método y11deprotección de importación. Son regresiones de código, no17validaciones de Alphabet. Logs adjuntos.

El comando oficial `valorar.sh` sí se intentó sobre el ID nuevo, con `--metodo A --revision-id GOOGL-CODEX-20261029` y sin autorización de publicación. Salió con código1por `ModuleNotFoundError: yfinance` al iniciar la importación SEC, antes de completarla. La instalación de dependencias no terminó y fue interrumpida. El entorno no declara credenciales de service account configuradas; los conectores Drive sí permiten leer y copiar. Por ello no se presenta el pipeline como ejecutado ni se afirma que instalar librerías resolvería por sí solo autenticación/red.

`unificacion_hojas.py`, citado por la normativa, no está presente en el checkout del motor leído. No se declara superado. Las fórmulas/validaciones se cotejaron solo en los rectángulos incluidos en las capturas; no cubren todas las hojas, referencias externas ni toda la sensibilidad. Tampoco hay validación visual integral de46pestañas. La nota A3 de la copia se leyó de vuelta; no acredita un modelo listo.

## Fuentes efectivamente consultadas y alcance

1. Reglas/proceso/prompts/repositorios y sus commits indicados arriba. Fuentes normativas, no evidencia primaria de Alphabet.
2. Capturas nativas de R5, plantilla oficial y AZ existente en `evidencia/`. Incluyen `userEnteredValue`, `effectiveValue`, notas y validaciones de rangos acotados. Son datos del modelo, no estados primarios independientes.
3. [SEC10-K FY2025](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm), localizado/abierto mediante búsqueda web; no se verificaron aquí todas las partidas de diez años.
4. [SEC10-Q junio2026](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm), resultados de búsqueda con compromisos, leases, financiación y política contable; no sustituye el último trimestre.
5. [Relaciones con inversionistas Alphabet](https://abc.xyz/investor/), página abierta; la extracción dinámica no devolvió los estados Q3 completos.
6. [Transcripción llamada28-oct-2026](https://stockanalysis.com/stocks/googl/transcripts/712854-q3-2026/), texto abierto. Canal secundario para declaraciones de dirección, no auditoría independiente. Se toman hechos de la llamada, no la cotización dinámica para calibrar un valor.
7. [Comunicado Q3 en PublicNow](https://www.publicnow.com/view/ED018F4AAE12FB3B1BD1E9649EA9BF381E69B00F), encontrado en búsqueda; la apertura completa no devolvió contenido. No se finge descarga de estados.
8. [SEC Q3 URL identificada por accession](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm), intento de apertura fallido. StockTitan y StreetInsider también fallaron al abrir el texto completo; los extractos de búsqueda no se consideran verificación línea a línea.
9. [Damodaran, archivo octubre2026](https://aswathdamodaran.blogspot.com/2026/10/), búsqueda encontró la discrepancia de ERP; pendiente descargar y conciliar la serie mensual original.
10. [AZ Stocks](https://azstocks.net/), resultado de búsqueda sobre metodología general; plantilla/fórmulas originales completas no obtenidas ni certificadas.

## Criterio financiero provisional

**No hay base suficiente para escoger como mejor sustentada una valoración nueva que no se ha ejecutado.** Entre los expedientes existentes, R5 hace explícita una cuestión económica relevante —la preinversión y la depreciación por cohortes—, pero su integridad respecto al motor oficial falla en el contraste acotado y contiene una discontinuidad de I+D terminal. AZ es más fácil de reproducir desde sus entradas actuales, lo cual demuestra trazabilidad aritmética, no superioridad económica: su D&A, CapEx, crecimiento Cloud y RONIC terminal siguen necesitando anclas primarias y pares.

No se elige218,82por ser más bajo, ni287,20por estar publicado. La elección final debe depender del rendimiento económico de la capacidad IA, márgenes después de sus costes, persistencia competitiva y un puente financiero conciliado, con el mismo corte y sin cambiar fórmulas para encajar una historia.

## Punto exacto de continuación

1. Resolver incompatibilidad motor R5/plantilla sin alterar R5: diagnosticar en soporte separado las fórmulas cambiadas; cualquier corrección general requiere propuesta versionada y regresión, no parches individuales silenciosos.
2. Completar extracción primaria FY2016–2025 +9M2025/2026 y LTM, con publicación≤29-oct, unidades y ajustes; conciliar convertibles/RSU, leases y activos financieros.
3. Completar fichas A-1.2 por driver/segmento y pares; decidir supuestos por evidencia sin consultar el precio para calibrarlos. Identificar limitaciones de trayectoria que no admita la plantilla.
4. Cargar únicamente entradas permitidas en una copia nueva para la valoración independiente, preservando las46pestañas y fórmulas; completar cuatro escenarios, siete múltiplos y sensibilidades/inverso nativos.
5. Obtener documentación/fórmulas AZ originales o declarar expresamente reconstrucción; ejecución nueva aislada y conciliación contable.
6. Elaborar artículo fundamental completo y cotejar cifras; controles integrales y PR con estado real. Mantener catálogo y producción intactos. **Este PR borrador es solo evidencia de avance.**
