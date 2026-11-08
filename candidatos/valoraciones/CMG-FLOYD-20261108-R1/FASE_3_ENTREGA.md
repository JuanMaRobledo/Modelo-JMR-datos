# F3 · CMG · Modelo JMR Floyd · CMG-FLOYD-20261108-R1 — entrega: CERRADA (CANDIDATO_REVISADO)

**Fecha:** 2026-11-08 · **Corte contable:** 30-sep-2026 · **Precio:** US$34,43 (6-nov-2026) · **Hoja:** `1f7BMt0ynbvjFUT84ftUmkPfxyJvmPvcqQ-7GW7EWtAY` · **Históricos:** `14ONchw6fXR9tSQs_OlQ3_Nio6d1vobUcH9LLgyZ6REs`
**Herramienta/modelo:** Claude Code, `claude-sonnet-5-5` (esfuerzo no reportado) · **AISLAMIENTO=OK** (CMG-A3 solo como referencia de comparación) · **PASOS: 4/4 ejecutados.**

## Resultado
| | Conservadora | Base | Optimista |
|---|---|---|---|
| Probabilidad (prior JMR «crecimiento maduro», sin desviaciones) | 25 % | 50 % | 25 % |
| CAGR ingresos 1-5 / año 10 | 6,4 % / 4,1 % | 8,9 % / 5,2 % | 10,9 % / 6,1 % |
| Margen EBIT actual → objetivo (año 5) y terminal | 14,1 % → 13,0 % | 14,1 % → 16,0 % | 14,1 % → 18,0 % |
| Ventas/capital 1-5 / 6-10 | 2,2 / 2,4 | 2,7 / 2,9 | 2,9 / 3,2 |
| ROIC año 10 / terminal / marginal 2-5 | 42 % / 15 % / 14,7 % | 53 % / 22 % / 42 % | 59 % / 28 % / 56 % |
| Reinversión terminal (g/ROIC) | 26,7 % del NOPAT | 18,2 % (605 M); año 1: 464 M (46 %); año 10: 368 M | 14,3 % |
| WACC inicial / terminal (común); g | 7,85 % / 8,33 %; 4,0 % | igual | igual |
| Valor por acción | **21,47** | **33,04** | **43,78** |
| Valor terminal / valor empresarial | 66,4 % | 71,0 % | 73,7 % |

DCF Base US$33,0425 (valor principal) · valor esperado US$32,8335 (separado) · MOS 35 % = Base × 0,65 = **US$21,4776** · precio 34,43 (+4,2 % sobre la Base). Conservadora ≤ Base ≤ Optimista; probabilidades suman 100 %; no existe historia de Disrupción.

## Drivers Base (antes → después; CMG-A3 A-1.2 como referencia, no insumo)
| Driver | CMG-A3 | Floyd | Causa económica |
|---|---|---|---|
| Crecimiento 1-5 | 8,4 % | 8,9 % | modelo de unidades (350-390 aperturas/año), comparables +2-2,5 % |
| Margen terminal | 17,0 % | 16,0 % | margen por restaurante cayó a 23,8 % LTM; industria 15,8 %; sin extrapolar el pico de 16,9 % |
| Ventas/capital 1-5 / 6-10 | 2,20 / 2,05 | 2,7 / 2,9 | economía de unidad (1,3 M netos; AUV 3,1 M) y comparables sin capital; capital sin arrendamientos |
| ROIC terminal | 19,0 % | 22 % | 22 % sin arrendamientos ≈ 12 % con ellos = punto medio entre costo terminal y ROC de la industria (18,4 %) |
| WACC inicial / terminal | 7,81 % / 8,75 % | 7,85 % / 8,33 % | Rf 4,94 % y ERP 3,387 % de ERPNov26; beta 0,86 |
| Arrendamientos | 5.599 M restados de la deuda con EBIT neto de alquiler | fuera de la deuda; gasto en EBIT | evitar doble conteo (≈ +US$4,4 por acción) |
| DCF Base | 25,25 (4 historias, precio 32,91) | 33,04 (3 historias, precio 34,43) | puente en Nivel 2 (apartado 4): +4,43 arrendamientos, +2,25 WACC, +0,66 crecimiento, −2,00 margen, +1,61 S/C y ROIC, −0,04 puente; réplica de A3 26,14 (0,89 de diferencia por el conversor de A3) |

## Hechos ejecutados
1. Historias antes que números (`HISTORIAS_A_NUMEROS.md`): tipo «Crecimiento maduro», párrafo, vínculos por palanca con evidencia/contraevidencia/rango/efecto, prueba 3P, tres disparadores por historia; TAM N/D con motivo. Estado «COMPLETA» en las tres. Señales REVISAR (margen, ROIC y S/C frente a industria) explicadas en los vínculos.
2. Costo de capital común (Detailed): Rf 4,94 %, ERP 3,387 %, beta directa 0,8585 (0,783 de Restaurant/Dining re-apalancada con arrendamientos 5.599 / capitalización 43.553), sin deuda financiera → WACC = Ke = 7,85 %; terminal 8,33 %. Opciones: 12,268 M SOSARs (10,37 c/u); RSU/PSU 5,174 M como acciones. I+D, NOL, preferentes, convertibles y fracaso: no aplican.
3. DCF por hoja (Simple Ginzu sin cambios) y **réplica independiente** en Python: 33,04246 / 21,47111 / 43,77785 (hoja 33,04246 / 21,47111 / 43,77785).
4. DCF inverso (réplica, mismo motor): con crecimiento Base exige margen 16,68 %; con margen 16 % exige CAGR 9,49 %; con margen LTM 14,12 % exige CAGR 11,30 %.
5. Múltiplos (contrastes, peso 0 %; `Descuento de múltiplos!C6 = Solo 3 años`): salidas FY+3 Cons/Base/Opt — EV/EBITDA 16,2/18,0/19,8x; EV/FCFF 23,4/26,0/28,6x; P/E 23,4/26,0/28,6x; P/FCFE 22,5/25,0/27,5x; P/OCF 16,2/18,0/19,8x. Anclas: historia propia, Damodaran Restaurant/Dining (EV/EBITDA 17,5x) y mercado (P/E ~24,3x). VP3 Base: 34,73 / 22,83 / 32,21 / 22,60 / 26,54. P/V y P/BV N/D sin peso.
6. Sensibilidades: ocho matrices 5×5 nativas (WACC×g, ROIC terminal×g, CAGR×margen; cinco de múltiplos) con centro = valor (33,04 en las tres de DCF; centros de múltiplos iguales a VP3). Económicas: margen 14/15/17/18 % → 28,97/31,00/35,08/37,12; ventas/capital 2,2-3,5 → 32,46-33,51 (no material); ROIC terminal 8,33/15/19/30 % → 24,67/30,66/32,24/34,40; beta 0,76/0,96/1,06 → 33,69/32,39/31,76; g 3 %/4,94 % → 29,61/38,11.

## Controles
- `Huella motor` 0/0 y comparación celda a celda con la Maestra Floyd: **0 diferencias en 26.346 fórmulas** (valoración e históricos). APROBADO. (Incidente corregido: la carga de anclas había sobrescrito 24 etiquetas con fórmula en `POCF`/`PFCFE`; se restauraron exactas desde la Maestra y la comparación se repitió.)
- Compuertas económicas: «APTO CON AVISOS JUSTIFICADOS» en las tres historias (aviso: escalón ROIC año 10 → terminal, justificado con fuente). Marco de tres escenarios: OK (probabilidades, orden de valores, orden de supuestos, costo de capital común, etapa del ciclo).
- Matrices: centros conciliados (DCF 3/3, múltiplos 5/5). Réplica independiente: APROBADO. Reproducción de ROE/ROIC en dos períodos (F2): APROBADO.
- `scripts/controles_todas.sh` y `scripts/candados.py` (controles A-1.2 de cuatro historias): NO EJECUTADOS por contrato (asumen Disrupción); sustituidos por M1-M3 Floyd (F4).

## Salvedades y reservas
Beta y volatilidad de opciones son hipótesis; la convención de arrendamientos (y el ROIC terminal sobre capital sin arrendamientos) es la mayor palanca de método y debe auditarse en F5; el CFO LTM incluye +222 M de impuestos diferidos (anclas de P/OCF y P/FCFE ajustadas); TAM N/D.

## Siguiente: F4 (análisis, JSON, controles y publicación EN_REVISION si los gates pasan). F5: NO REALIZADA.
