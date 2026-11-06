# DUOL R4 · Avance 5-nov-2026: 10-Q Q3, WACC Detailed y sensibilidad NOL

**Estado:** CANDIDATO, no publicado. Nueva evidencia posterior a F4_ENTREGA inicial.

## 1. Nuevo documento primario

- El Form 10-Q del 30-sep-2026 se presentó **4-nov-2026** (accesión SEC `0001628280-26-069692`), distinto al 8-K 3-nov `0001628280-26-069474`.
- Portal de relaciones con inversionistas: https://investors.duolingo.com/financials
- Transcripción consultada del 10-Q 4-nov (no sustituye SEC como fuente): https://financialfilings.com/filings/duolingo-inc/interim-quarterly-report/2026/75577152/
- ROU al 30-sep-2026: **USD 73,359 millones**, al 31-dic-2025 USD 80,380 millones.
- Obligación de arrendamientos **largo plazo**: **USD 84,216 millones** al 30-sep, USD 93,779 al 31-dic. La porción corriente está dentro de `Accrued expenses and other current liabilities` (USD 70,536 millones); el balance condensado no la identifica por separado. No asignar cero ni interpretar 84,216 como deuda lease total.
- Opciones 482 mil a strike ponderado USD 20,36 y vencimiento 3,44 años; RSU 2.638 mil pendientes; pueden requerir conciliación con los 50,8 millones de acciones diluidas del comunicado. Evitar doble dilución.
- No se identifica en este documento trimestral prueba completa del NOL 111,199 millones: verificar soporte por ejercicios y DTA/10-K.

## 2. Sensibilidad exacta del saldo NOL en motor original

- Base con NOL=USD 111,199M y selector Sí: **USD 111,44266785123249/acción**.
- Copia de auditoría al poner selector NOL=No, sin alterar fórmula original ni Base: **USD 110,98242703967286/acción**.
- Diferencia: **USD 0,46024081155963/acción (0,41299 % del Base)**. Por umbral individual <2%, la cifra NOL *aislada* no sería material, pero falta cerrar todas las incertidumbres de manera agregada y documentar origen fiscal.
- Libro sensibilidad: https://docs.google.com/spreadsheets/d/1ZUDFHhfmCYslUDEvgAepWEw-ZxBGT9B39ZknV1jNZ8Y/edit

## 3. WACC reproducido sin entrada directa

- Cambiadas en las **cuatro copias operativas DUOL** únicamente entradas literales de `Cost of capital worksheet`:
  - B11=`Detailed`, B21=`Single Business(Global)`, B25=`Will Input`, B26=0,05529590704990127, B32=5, B33=`Direct Input`, B34=0,0569.
- El núcleo Damodaran original **calcula** beta global **1,3370400063421872** con lookup sectorial; ERP 5,52959070499 % con proxy ROW explícita, Rf 5,29 %, WACC `Cost of capital worksheet!B13` = **12,6832839912697 %**.
- El DCF Base conserva exactamente **USD 111,44266785123249**, Conservador 83,66281979551812, Optimista 180,42759278355030 y Disrupción 58,13801193970046.
- No se tocó ninguna fórmula de cálculo. Se subsana la limitación técnica de WACC `I will input`; sigue pendiente **justificar el proxy geográfico ROW/ERP**.

## 4. Publicación

Conservamos bloqueo F4 por arrendamientos ASC842 y coherencia de capital invertido/reinversión, más regeneración de sensibilidades/múltiplos y pruebas completas app/CI. No se promueve DUOL R4 ni se cambia R2 activa por este estudio.