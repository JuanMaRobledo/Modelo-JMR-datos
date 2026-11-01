# META y NVDA · cierre de gates de la hoja A-1.2 · 1-nov-2026

**Estado: DCF nativo cerrado en ambas hojas de trabajo. NO publicado, NO auditado.** Los libros siguen rotulados "NO PUBLICAR". Se escribieron celdas de `Input sheet` y `Option value!B9` (valores previos en `evidencia/cierre-gates-meta-nvda-20261101/valores_previos_hojas.json`). No se modificó ninguna fórmula de salida. Única fórmula restituida: `META Input sheet!B20 = IF(B85="VALIDADO";B84;"")`, idéntica a la de NVDA (en META estaba vacía y su `COUNT` bloqueaba K5).

## Evidencia (10-Q originales en SEC)
**META 10-Q 30-sep-2026 (0001628280-26-066773)**
- Inversiones no cotizadas 32.624 = 21.077 alternativa de medición + 11.547 método de participación (Nota 5). Los 11.547 son el 20 % de los Ventures de centros de datos de Louisiana y Texas, contraparte de arrendamientos de Meta: se dejan en capital operativo, no se suman al patrimonio. B83 = B84 = 21.077 (valor económico = contable; sin valoración independiente: limitación).
- Resultados de esas inversiones van a "Interest and other income (expense), net", bajo Income from operations: sin solapamiento con EBIT/FCFF.
- Opciones: 20 M emitidas en 2026, ejercicio medio US$2.788, ~4 años. `B38=Yes`, B39=20, B40=2788, B41=4, B42=0,4271 (vol. histórica 1 año, cierres hasta 30-oct-2026), dividendo 0,34 % (0,525×4/614,99). Valor 23,79/opción, 475,71 M en total (0,02 % del patrimonio).
- RSU no adquiridas 134,474 M; gasto no reconocido 75,59 mil M vs. valor de concesión 79,29 mil M: devengado ~4,7 % (~6,3 M acciones); el resto ya está en el SBC del EBIT. No se resta aparte.

**NVDA 10-Q 26-jul-2026 (0001045810-26-000075)**
- 51.157 = 47.898 capital no cotizado (Nota 6) + ~3.300 método de participación en financiadores de infraestructura (fuera, ligado a demanda de clientes). B83 = B84 = 47.898. Ganancias no realizadas y resultado por método de participación van a "Other income, net". Caja B19 (99.369) ya incluye 42.783 de capital cotizado: no se repite. 4.957 de capital cotizado bloqueado a largo plazo no se suma (conservador).
- Sin opciones pendientes: `B38=No`. RSU/PSU 168 M (0,7 %), devengado ~4 %: inmaterial.

## Resultado nativo de la hoja (`Valuation output!B35`, K5:K8 = LISTO en ambas)
| | Base | MOS35 | Conservadora | Disrupción | Optimista | Precio 30-oct |
|---|---:|---:|---:|---:|---:|---:|
| META | 783,42 | 509,22 | 485,56 | 246,85 | 1.155,19 | 614,99 |
| NVDA | 201,80 | 131,17 | 108,09 | 49,96 | 344,96 | 204,64 |

Candidatos previos: META 780,63 y NVDA 201,45; la diferencia (+0,36 % / +0,17 %) proviene de sumar activos no operativos y restar opciones con la hoja. Son salidas de la hoja, no valores forzados.

## Salvedades económicas abiertas (no ocultar al publicar EN_REVISION)
1. **META, pasivo legal:** el EBIT proyectado parte de margen objetivo sin el cargo de 9.890 (acuerdo fiscales generales, ago-2026). Las provisiones legales no están en deuda (B16 = 116.026) ni en minoritarios (0). Solo la parte no corriente es 8.304 M (Nota 8); el saldo corriente no se ha extraído. Orden de magnitud ~US$3–4/acción (~0,5 %) a la baja, **no aplicado** porque la plantilla no tiene campo propio.
2. Valor económico de inversiones = valor contable; precios observables, no valoración independiente.
3. META `Input sheet!B35` (Rf 4,94 %) frente a 5,29 % citado en el diagnóstico: no tocado, `Cost of capital B84` ya VALIDADO; revisar al auditar.
4. Pendiente: reconciliar NVDA 381,79 (R4) → 201,80; múltiplos (pestañas `Descuento de múltiplos`, `Múltiplos históricos` y `Sensibilidad por múltiplo` vacías: faltan series históricas y anclas), exportación a JSON, Nivel 1 (14) y Nivel 2 (12), CI, sustitución en catálogo.
