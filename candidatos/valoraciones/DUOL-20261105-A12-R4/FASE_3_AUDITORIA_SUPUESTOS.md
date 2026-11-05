# DUOL · Método JMR A-1.2 · revisión económica integral de supuestos · F3

**Fecha:** 2026-11-05 (Colombia) · **Corte contable:** 2026-09-30 · **Precio de comparación en el modelo:** cierre 2026-11-03, USD 128/acción (histórico, NO precio actual).  
**Estado:** **CANDIDATO_REVISADO — PUBLICACIÓN BLOQUEADA POR RESERVAS MATERIALES**. No se ha promovido al catálogo ni a la app; no se ha ejecutado la auditoría económica independiente F5. **AISLAMIENTO=OK**. Proceso bajo revisión F3, sin atribuir un dictamen externo. Herramienta: ChatGPT, Google Sheets nativo + GitHub, cálculos independientes y perturbaciones con lectura del motor; esfuerzo computacional exacto no expuesto.

## Identidad y alcance

- R2 en app (sin modificación): [hoja vigente R2](https://docs.google.com/spreadsheets/d/1_-Rxwq04iuXvS1FNpYuwlaAkGEeBxUsuyblIZAx_Oqc/edit), Base USD 139,108685787.
- R3 del PR #250: pendiente, todavía no publicada, previa objeción material de leases.
- R4 candidato [hoja previa a auditoría](https://docs.google.com/spreadsheets/d/1JmXSvoFuWTzjQNorDJlrRl4UIQVmhXalEGdRqua_KEs/edit), Base USD 111,047892459 / MOS 72,181130098; 62 hojas.
- **Copia AUDITADA F3**, única hoja en que corregimos la cohorte de I+D: [DUOL auditoría homogénea LTM](https://docs.google.com/spreadsheets/d/1pTBhCQDGWHwnuu_olfiwB9v4ERXwwr3FQ7jZZySj8bE/edit), Base USD **111,442667851**, MOS 35% USD **72,437734103**; **NO PUBLICAR** aún.
- [Copia aislada de estrés, todas las perturbaciones revertidas](https://docs.google.com/spreadsheets/d/1OboBSo2CI_dd4xClY7opmWqvN1xdc6m0uryE8UEIhJ8/edit), Base revalidada USD 111,442667851.
- **Origen metodológico:** 187 fórmulas Damodaran FCFF del bloque Base restauradas y 750 ajustes de impuesto en el motor de sensibilidad, con 78 comentarios originales y 4 excepciones DUOL. **No se ha demostrado una sustitución metodológica equivalente en los bloques completos Conservadora/Optimista/Disrupción**: el esperado condicionado puede ser un híbrido de motores. Esta divergencia debe conciliarse antes de F4.

## Tabla de hipótesis — nivel económico y estado

| Palanca | Valor R4 auditado y prueba causal | Juicio de la revisión |
|---|---|---|
| Crecimiento 1–5 y monetización | Ingresos LTM USD 1182,296 M; año1 +14,1765%; CAGR5 **13,6377%**, ingresos año5 USD 2240,471 M. Se forma con MAU +13/14/12/10/8% años1–5, penetración pagadora relativa +1% anual y ARPU/precio-mix +2% anual. Q3: DAU+29%, pagadores+14%, bookings+12%, ingresos+14%; retirada de Max premium. Sin mejora de penetración ni ARPU, Base USD 101,1301 (**−9,25%**). | **RESERVA MATERIAL**: conversiones y ARPU por cohorte no demostrados; sustentar +1%/+2% o revisar trayectoria, sin mover valor hacia el precio de mercado. |
| Margen EBIT económico | Margen inicial correcto 23,25695% tras rehacer cohortes (GAAP12,36% NO es comparable al margen ajustado), y objetivo28% año5 y terminal; prueba objetivo26% → Base USD 105,3020 (−5,51%); objetivo30% → USD117,5833 (+5,51%). SBC sigue en los gastos GAAP, no se elimina por llamarla compensación no caja. | **RESERVA MATERIAL**: justificar apalancamiento del EBIT ECONÓMICO después de gastos IA, I+D y SBC; los márgenes EBITDA ajustados no lo sustituyen. |
| Capitalización I+D | 3 años, USD362,473 M LTM 2026. En R4 previo, -1/-2/-3 eran FY2025/FY2024/FY2023 solapados. AUDITADO usa LTM Sep2025=293,162; LTM Sep2024=219,159; LTM Sep2023=188,566 (USD M). Activo I+D corregido USD630,9673 M, amortización233,629, ajuste EBIT128,844; EBIT económico LTM274,966 vs263,254. Valor 111,0479→111,4427 (+0,36%). Vida2 años, prueba USD110,6832 (−0,68%). | **CORREGIDO EN COPIA DE AUDITORÍA** (pendiente migración a eventual hoja publicable y regresión completa). Datos de FY/9M sustentados en SEC; conservar la formulación homogénea. |
| Sales/Capital marginal años1–5 | 1,90x, hipótesis no reconstruida de cohortes/activos incrementales. A 1,50x, USD109,2400 (−1,98%). Año1 reinv USD95,939 M, NOPAT USD265,911 M, reinv/NOPAT ≈36,1%. | **RESERVA**: plausible para digital, falta auditoría de inversión económica marginal incluyendo I+D capitalizada, prepagos y capital de trabajo; no confundir con ventas/capital promedio contable. |
| Sales/Capital años6–10 | Se usa 1,400643x sectorial global. A 2,30x, USD113,4791 (+1,83%). Cambio escalonado año6; inversión se eleva comparada con mantener2,3. | **MANTENER CON RESERVA**: convergencia prudente con industria; suavizar o explicar escalón. |
| ROIC terminal | Base 9,70%=WACC terminal, sin foso competitivo durable probado; ROIC *promedio* de capital invertido año10 ≈38,55%, versus ROIC *marginal en perpetuidad* 9,70%. Si el marginal fuera15% (foso persistente), DCF USD123,1919 (+10,54%). | **MANTENER CON ARGUMENTO**, pero explicar distinción ROIC promedio/marginal y fuerte salto de reinversión terminal. No sostener15% por mera marca o rachas de usuario. |
| Reinversión terminal | Año10 ingresos USD3256,760 M, NOPAT USD683,920 M, reinv93,008 M, FCFF590,912 M; en terminal NOPAT711,276 M, reinv293,310 M, FCFF417,966 M. g/ROIC = 4%/9,7%=41,24% reinversión marginal terminal. PV terminal 2407,161 M / valor operativo4177,267 M = **57,63%**. | **RESERVA MATERIAL DE EXPLICACIÓN**: caída ~29% del FCFF terminal frente año10 por convergencia de retorno nuevo; fórmula Damodaran consistente, pero la trayectoria debe derivarse de historia económica y el valor depende de supuestos terminales. |
| Riesgo libre/ERP | Input B35 Rf5,29% (30-sep), prima madura NYU4,41% citada 01-nov; factor de mercado9,70%. WACC inicial nativo12,6833%; terminal9,70%. Prueba de rebase de fecha Rf4,90% (4-nov) +ERP4,80% (mantiene retorno maduro9,70%) produce Base110,8526 (−0,53%). | **CORREGIR TRAZABILIDAD/CORTE**: no llamar 4,80% una publicación de Damodaran; es prima algebraica de reconciliación. Elegir fecha uniforme y fuente primaria. |
| Prima país ROW | Con ingresos FY2025 EEUU USD392,214M (37,8%), resto USD645,375M (62,2%); add-on ROW +1,80pp a ERP madura para todos los países no estadounidenses. Sin add-on DCF118,5430 (+6,37%). Add-on3,00pp DCF107,0889 (−3,91%). | **BLOQUEANTE**: una proxy agregada no es exposición por país documentada ni distribución de ingresos futura; exigir rangos verificables de riesgo país y justificar elegida. No sumar riesgo de IA otra vez en WACC. |
| Convergencia de riesgo terminal | WACC12,683% inicial→9,70% terminal elimina por completo prima del ROW pese a operaciones internacionales futuras. Prueba sin pérdida completa de prima terminal, WACC terminal10,82% y ROIC marginal terminal=10,82% para respetar «sin moat»: Base USD104,9993 (**−5,78%**). | **BLOQUEANTE**: no hay motivo causal demostrado para que desaparezca CRP en perpetuidad; conectar riesgo geográfico con mix futuro y tasas al mismo corte. |
| Tasa fiscal / NOL | Tasa efectiva normalizada23,6923% convergente25% marginal. NOL FY2025 federal USD111,199M; falta rollforward Q3. Tasa marginal27% → Base USD109,8037 (−1,47%); NOL0 →110,9824 (−0,41%). | **RESERVA DOCUMENTAL**: controlar NOL estatal y créditos separados; cuantificar combinaciones, no simular que NOL0 acota impuestos diferidos completos. Impactos aislados bajo2%. |
| Arrendamientos | Input B18 = No para **no hacer capitalización incremental**, dado ASC842 reconoce leases y el conversor FY2025 es histórico. B79/B80=0 incremental y B81=NO APLICA. 10-Q30-sep reporta largo plazo84,216M con parte corriente agregada; no convertir PV FY2025 105,061 M en deuda nueva. | **ELECCIÓN CONTABLE DOCUMENTADA**, costo renta queda en EBIT/FCFF. Separar del análisis si se decide recast financiero completo; evitar doble conteo. |
| Opciones/SBC/acciones | 50,8M diluidas, incluye opc.0,4, RSU2,6 y founder awards0,6 estimados; hoja Option value calcula $66M para .6M contratos pero **B38=No significa que no se resta de nuevo como deuda de opciones**, no ausencia económica. Guía SBC2026 aprox14% revenue, coste recurrente. | **RESERVA**: nota clara de opciones existentes y reconocidas por denominador; comprobar RSU no doble contadas ni omitidas en tasa futura/dilución. La cifra50,8M no necesariamente representa número al día de valoración; comprobar saldos actualizados. |
| Caja e inversiones | Cash y ST inv USD1373,901 M; inversión no operativa en balance USD110,120 M sumada una sola vez. Aún no probada equivalencia valor en libros/valor razonable. | **RESERVA**: reconocer precio de libro como proxy condicionada; auditar resultados de participaciones ya incluidos en EBIT/FCFF, sino doble conteo. |
| Múltiplos relativos | Cinco prioritarios calculados por hoja con centros 5×5 VP FY+3; EBITDA, FCFF, P/E, P/FCFE, OCF necesitan ancla histórica y calidad de denominador después del ajuste I+D/2025 beneficio fiscal extraordinario; P/S/P/BV no obligatorios. | **RESERVA MATERIAL PARA PUBLICACIÓN** si valores derivados se presentan como aprobados: ancla y extracción de las 5 matrices, no inferir economía de simple OK matemático. |
| Historias/3P | B/C/O/D probabilidades40/22,5/22,5/15 conforme ciclo alto crecimiento. Sin TAM monetario primario; unidad MAU y monetización justifican parcialmente crecimiento. Base111,4427, Conservadora83,3092, Optimista173,8200, Disrupción56,1498; esperado C/B/O120,5072 **condicionado a reconciliar motores**. | **RESERVA**: «COMPLETA» y gates LISTO expresan integridad aritmética, no evidencia suficiente de TAM, cohortes, tasas o un mismo método FCFF para cuatro historias. |

## Pruebas y controles realmente ejecutados

1. Se copiaron hojas de auditoría y estrés, sin alterar DUOL R2, R3 y R4 previo, sus matrices ni el catálogo.
2. Secuencia univariada usando batchUpdate nativo y lectura posterior de 'Valuation output'!B35; cada prueba se revirtió a la línea base en un bloque finally. Lectura final confirma: valor111,442667851; Input B47 fórmula original y G5/terminal ROIC N5=0,097; centros de Sensibilidad DCF B12/B23/B34=OK.
3. Hoja auditada: cuatro escenarios K5:K8=LISTO; 3/3 conciliaciones de centro en Base OK; no error de fórmula detectado en áreas examinadas. No se validó de forma independiente cada elemento de los75 bloques de sensibilidad después de actualizar cohortes.
4. No ejecutados: suite completa `bash scripts/controles_todas.sh`, `candados.py`, `diff_formulas_plantilla.py` del nuevo motor en esta revisión, control de 5 matrices relativas contra JSON, auditoría gráfica UI/producción, ni F5 independiente.
5. La elegibilidad F4 exige corregir primero los bloqueos, concluir validadores técnicos y alinear artículo Nivel 1 y Nivel 2 con la misma foto. No se ha modificado valoraciones/analisis/catalogo ni el despliegue.

## Decisión y trabajo exacto antes de F4

**NO PUBLICAR todavía.** Comprobar si las ventas por jurisdicción y primas país permiten reemplazar/justificar +1,8pp ROW y su desaparición terminal; reconstruir/defender evidencia de penetración pagadora+1% y ARPU+2% (o recalibrar Base), validar margen económico28% frente a cohortes/IA/SBC, y reconciliar los tres bloques DCF de historias con el original restaurado. A continuación ajustar hoja candidata sin alterar fórmulas canónicas (solo datos/soportes), reproducir DCF y MOS, reconstruir extracción 5×5 relativa y FCFE informativo desde la nueva misma hoja, sincronizar Nivel 1/Nivel 2, ejecutar controles, abrir PR de publicación y verificar app real. No confundir controles matemáticos LISTO con aprobación económica.

## Fuentes primarias y métodos

- [SEC Q3 2026 shareholder letter](https://www.sec.gov/Archives/edgar/data/1562088/000162828026069474/q3fy26duolingo9-30x26share.htm).
- [10-Q Q3 FY2026 original emisor](https://duolingo.gcs-web.com/static-files/f27581cd-cf47-4058-a316-2dcca04cfb00).
- [SEC 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1562088/000162828026012494/duol-20251231.htm).
- [NYU Damodaran](https://pages.stern.nyu.edu/adamodar/New_Home_Page/home.htm).
- [JMR método vigente v33](https://github.com/JuanMaRobledo/Modelo-JMR/blob/main/modelo/REGLAS_VIGENTES.md).
- [JMR Stories-to-Numbers](https://github.com/JuanMaRobledo/Modelo-JMR/blob/main/docs/HISTORIAS_A_NUMEROS.md).

**Separación epistemológica:** SEC es evidencia de resultados pasados; costos de capital, márgenes futuros, monetización, probabilidades, primas por ROW y ROIC terminal son hipótesis económicas JMR a contrastar, no hechos del emisor.

## Anexo F3 (05-nov-2026): ROIC marginal, reinversión terminal y duración de ventaja

**Copia aislada reproducible:** [DUOL F3 ROIC marginal y fade](https://docs.google.com/spreadsheets/d/1Ld_lp3uWLVuPpaKGyvUOYXFDfF1ZL2Grmx2-GV-xjqo/edit#gid=2064908873). 64 pestañas; la hoja nueva `F3 ROIC marginal y fade` añade fórmulas dependientes de `Valuation output` y diagnóstico de divergencia contra Stories, sin alterar los 10 años, el escenario Base, los cuatro escenarios alternos, las notas Damodaran ni las matrices. No se fusionó ni publicó.

### Prueba algebraica Damodaran

En el primer año estable:

- `NOPAT_terminal = 711,276299` millones; `g = 4%`, `ROIC_terminal = WACC_terminal = 9,70%`.
- `Reinversión_terminal = NOPAT × g/ROIC = 293,309814` millones, frente a `93,007557` millones en año 10. Diferencia explicada por pasar a reinversión marginal para sostener g y el ROIC estable supuesto.
- `FCFF_año10 = 590,911961`, `FCFF_terminal = 417,966485` millones. El descenso no es un castigo arbitrario a EBIT: NOPAT del año 10 es 683,919519 y terminal crece 4% a 711,276299.
- `TV = FCFF_terminal/(WACC-g) = 7332,745354 = NOPAT_terminal/WACC` millones, identidad exacta si ROIC = WACC. `VP_TV = 2407,161276` / `VP_EV = 4177,266527` (57,63%).
- `ROIC PROMEDIO_año10 = 38,550848%` (`L9/K41`), **distinto** del ROIC **MARGINAL INDICATIVO** `(L9-K9)/K10 = 26,849259%` (aumento NOPAT de año9 a año10 / reinversión año9). Este último es inferencia de nuestras proyecciones, no una tasa observada ni prueba de que se prolongará en el tiempo.

**Implicación:** No hay un error aritmético en la reinversión terminal ni en el DCF cuando el capital nuevo deja de ganar por encima del WACC. Sí hay un **juicio económico fuerte**, la extinción del exceso marginal inmediatamente después de t10; el 38,55% sobre capital preexistente no implica 38,55% de retorno marginal sostenible. Damodaran permite retornos extraordinarios modestos en estabilidad si existe ventaja competitiva sustentada y también propone estudiar la duración del período de ventaja competitiva (CAP). Fuente [Damodaran, Little Book — Terminal Value](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/littlebook/terminalvalue.htm), [Damodaran CAP](https://pages.stern.nyu.edu/adamodar/New_Home_Page/valquestions/highgrowthperiod.htm).

### Sensibilidad independiente reproducida en Sheets — USD/acción

El motor original se perturbó **de forma secuencial** elevando exclusivamente `Escenarios e historias!N5` (ROIC marginal Base que alimenta `Input sheet!B50` y `Valuation output!M42`); cada perturbación fue seguida por lectura del DCF y reversión a 9,7%. El propio panel existente `Duración ventaja · FCFF` permitió medir apagado de exceso sobre WACC al cabo de 5 o 10 años extra. El nuevo panel F3 genera las mismas cifras con **116 fórmulas de diagnóstico y cálculo**, usando `SUM` de los ahorros anuales de reinversión, sin modificar `N5`. Ambos métodos dieron los mismos resultados a precisión de máquina.

| ROIC marginal después de t10 (inicial) | Extinción en 5 años extra | Extinción en 10 años extra | Si permanece indefinidamente |
|---|---:|---:|---:|
| 9,70%, sin exceso | 111,442668 | 111,442668 | 111,442668 |
| 12,0% | 112,419151 | 113,096634 | 117,816098 |
| 15,0% | 113,336342 | 114,660232 | 123,191947 |
| 20,0% | 114,372584 | 116,437398 | 128,567796 |
| 27,0% (aproximación marginal año10) | 115,295499 | 118,029781 | 132,749013 |

**Limitaciones de la extensión:** Se mantiene el NOPAT terminal del motor original creciendo nominalmente 4%, el WACC terminal 9,7% y se reduce SOLO la reinversión requerida según ROIC marginal que desciende de forma lineal al WACC en 5/10 años; los flujos marginales adicionales se descuentan primero a t10 y luego a hoy. Esto es sensibilidad de duración de ventaja (JMR), **no una segunda serie completa de FCFF 20 años**, ni una tesis demostrada por los reportes financieros. Retorno 27% es aproximación de supuestos anteriores, no expectativa defendida para años11–20.

### Dictamen económico

1. **No bajar el ROIC terminal por debajo del WACC** sin documentar destrucción estructural de valor: el actual 9,7%=9,7% significa nuevos proyectos con VAN cero, no fracaso de la empresa. El modelo ya conserva flujos futuros, rentabilidad del capital existente y caja.
2. **No subir por reflejo a 15–27% perpetuo**: suponer 15% terminal perpetuo agrega US$11,75 por acción respecto al Base, y el reporte no demuestra una barrera de entrada con permanencia infinita. Calidad de producto, marca, datos y compromiso favorecen ciertos retornos; IA generalista, costos de cambio bajos y margen IA/SBC dificultan certificar un foso amplio. La guía Q3 reportó DAU+29%, pagadores+14%, bookings+12%, margen EBITDA ajustado25,5%, con presión de costes IA. Fuente [SEC Q3 carta](https://www.sec.gov/Archives/edgar/data/1562088/000162828026069474/q3fy26duolingo9-30x26share.htm).
3. **La trayectoria finita es la sensibilidad económicamente más útil** para evitar castigar abruptamente retornos nuevos: una ancla del 20% que converja en diez años extra aporta US$4,99 (valor 116,44); 15% a cinco/diez años añade US$1,89/US$3,22. Estos NO reemplazan el Base hasta cuantificar el CAP desde retención de usuarios, ingresos por pagador, competencia y ventajas de producto. No sumar riesgos de IA otra vez en WACC si ya están en curvas de margen/monetización.
4. **Falla editorial y metodológica independiente:** `Valuation output!B35 = 111,442668` vs `Escenarios e historias!B44 = 109,359925`; año 10 ventas `Valuation output!L5 = 3256,759612` vs `Escenarios e historias!L28 = 3090,566922`. Diferencia por crecer 2–5 años a CAGR constante en FCFF original, mientras el bloque de historias permite trayectorias anuales variables; `K5=LISTO` y sensibilidad 3/3 OK NO comprueban esa equivalencia. El nuevo panel reporta **REVISAR**. Debe unificarse el método antes de presentación de Base y ponderados.
5. Tres centros de matrices DCF Base continúan OK al terminar, sin errores de fórmulas en el panel F3 inspeccionado. La perturbación del ROIC fue revertida a 9,7%. No se actualizaron catálogos ni expediente publicado, no se corrió CI integral ni se certificó F5.

**Decisión:** mantener R4 como candidato F3 y **no publicar** todavía. Conservar el resultado FCFF base 111,44 como caso de ROIC nuevo = WACC mientras se evalúan los CAP finitos y se reconcilia Stories. Si se acepta económicamente una ventaja persistente después de t10, debe cambiarse explícitamente `Escenarios e historias!N5` con evidencia empresarial, no para acercarse a la cotización.
