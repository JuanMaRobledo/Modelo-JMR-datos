# KO R1 · revisión de conciliación y estrés fiscal
Fecha: 2026-11-04. AISLAMIENTO=OK. Revisión KO-20261103-A12-R1.
Herramienta: ChatGPT Work; identidad exacta del modelo/esfuerzo no expuesta. Revisión interna, no dictamen F5.
Hoja leída directamente: https://docs.google.com/spreadsheets/d/17bX2bK0z1LSxO02GGv7HDFpAU6f8hkxIH4rUMdfnyEE/edit
JSON contrastado: commit 88ebe0ea865a32f4a57e12d4b52c76c06ee62151.

## Comprobado
La hoja Valuation output!A1:M40 reproduce el JSON: PV flujos explícitos 93402.917419, PV terminal 164532.783294, EV operativo 257935.700712, equity común 275437.652948 (USD millones), 4301.902335 millones de acciones y Base 64.0269423847 USD; MOS35% 41.6175125501 USD.
Crecimiento año1 -3%, años2–5 5%; margen terminal 33.5%; WACC inicial 7.364610856% y terminal 8.61%; ROIC marginal terminal 18%.
El Input sheet muestra crecimiento histórico 6.4934% y S/C de referencia 1.6841x, mientras Valuation output utiliza los drivers de historia. No sustituir fórmulas ni interpretar las referencias como drivers activos.

## Fuente primaria fiscal y balance
https://investors.coca-colacompany.com/filings-reports/all-sec-filings/content/0001628280-26-067844/ko-20261002.htm
Nota 9: depósito 6000 y derecho a intereses 589; exposición adicional 14000 para 2010–2025 más 1400 en nueve meses de 2026; aumento potencial de tasa efectiva 3.8 puntos. Son canales distintos.
Balance: caja, equivalentes, inversiones cortas y valores negociables suman 16595; patrimonio total 39533 y minoritarios 2161, coherentes con Input sheet. Los activos/pasivos en venta incluyen varios negocios: su neto no constituye precio de CCBA.

## Sensibilidad ilustrativa reproducible, NO nueva valoración oficial
Supuesto de estrés propio: trasladar 3.8 puntos de tasa efectiva a impuesto operativo sobre EBIT en TODOS los años futuros, incluyendo perpetuidad. Esto NO es una equivalencia demostrada entre impuesto consolidado e impuesto sobre EBIT: requiere reconciliar utilidad antes de impuestos, resultados de asociadas e intereses antes de activarlo en la hoja.
Mantener ingresos, márgenes, S/C, WACC, g y ROIC constantes. En años1–10, reducción FCFF=EBIT*0.038; en terminal, reducción FCFF=EBIT10*(1+g)*0.038*(1-g/ROIC).
PV caída explícita=4988.942160299896; PV caída terminal=7914.235145777307 millones. Efecto recurrente=2.9994119580767293 USD/acción.
Si además se paga inmediatamente 15400 millones (hipótesis conservadora de calendario, no pronóstico), reducción adicional=3.5798116276854066 USD/acción. Resultado condicional=57.44771879893251 USD/acción, frente a 64.0269423847. No restar nuevamente depósito ya excluido del puente.
Recuperar completamente depósito más intereses añadiría 1.5316479749882561 USD/acción antes de calendario y otros efectos; no asignar probabilidad ficticia.
Esta sensibilidad acota un canal relevante, pero NO acredita conciliación tributaria ni resuelve probabilidades judiciales.

## Estado de publicación
Se corrigió el conteo editorial rígido 28→29 incorporando tres comprobaciones de identidad y unicidad de KO R1, preservando controles de todos los emisores.
Pendiente ejecutar CI de ese commit. El PR tiene actividad concurrente; revisar HEAD al fusionar.
La conciliación aritmética no sustituye pruebas SEC históricas, integridad de fórmulas de plantilla, costo de capital documentado, puente CCBA y verificación app. No marcar esos controles como aprobados a partir de este informe.
