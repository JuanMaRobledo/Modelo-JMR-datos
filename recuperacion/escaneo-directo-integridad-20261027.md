# Escaneo directo de integridad · ocho recuperaciones · 27-oct-2026

**Alcance:** lectura directa, sin edición, de Google Sheets nativos: 13 pestañas clave (`Input sheet`, `Valuation output`, `Cost of capital worksheet`, `Operating lease converter`, `R& D converter`, `Descuento de múltiplos`, `Resumen de Valoración`, `Escenarios e historias`, `EVEBITDA`, `EVFCFF`, `PE`, `PFCFE`, `POCF`) y sus primeras 200 filas, columnas A:N; ocho expedientes publicados. **No es una certificación de las 61 pestañas ni una ejecución del script integral con el universo de 24 hojas.**

| Ticker | Celdas inspeccionadas | Fórmulas | Errores de celda | B35 y 4 historias contra registro | Hallazgos |
|---|---:|---:|---:|---|---|
| ADBE | 4.656 | 3.014 | 0 | 5/5 exactos | precioAnalisis heredado de otro corte |
| BSX | 4.600 | 3.032 | 0 | 5/5 exactos | Ninguno en alcance directo |
| DUOL | 4.605 | 3.032 | 0 | 5/5 exactos | Ninguno en alcance directo |
| MSFT | 4.134 | 2.545 | 0 | 5/5 exactos | Menor cobertura de celdas en historias; sin error de celda |
| NVO | 4.681 | 3.018 | 0 | 5/5 exactos | 13 divergencias de supuestos 6-10 frente a ficha |
| ONON | 4.541 | 2.986 | 0 | 5/5 exactos | precioAnalisis heredado de otro corte |
| PYPL | 4.694 | 3.044 | 0 | 5/5 exactos | Ninguno en alcance directo |
| **Total** | **36.559** | **23.679** | **0** | **40/40 exactos** | |

**Pruebas comunes:** `Valuation output!B35` es fórmula y coincide exactamente con `valorPrincipal` del JSON; `Escenarios e historias!H5:H8` son fórmulas y concilian con `valorEsperado.historias` A-D en 32/32; `Valuation output!C46` enlaza `Escenarios e historias!$D$5` en 8/8. Sin errores `#REF!, #VALUE!, #DIV/0!, #N/A, #NAME?, #NUM!, #ERROR!, #NULL!` en las celdas leídas.

### Divergencias observadas NVO (no corregidas automáticamente)

`reference/damodaran/NVO.json` contiene `crec_6a10` por escenario, pero la hoja tiene 13 valores manuales distintos. En este informe **la hoja publicada y el artículo tienen prioridad como fotografía de la revisión**, y la ficha debe conciliarse antes de una nueva valoración. Los escenarios DCF publicados siguen calculando correctamente según la hoja, pero no se considera cerrada su trazabilidad.

| Historia | Años 6–10: hoja (%) | Ficha de supuestos (%) | Discrepancias |
|---|---|---|---:|
| A · Base | −3; −5; −2; +2; +3 | −4; −6; −3; +1; +2 | 5 |
| B · Conservadora | −6; −8; −4; 0; +1 | −8; −10; −5; +1; +2 | 5 |
| C · Disrupción | −10; −12; −6; −2; 0 | −10; −12; −6; −2; 0 | 0 |
| D · Optimista | −1; −2; +1; +3; +3,5 | −2; −3; 0; +3; +3,5 | 3 |

### Precios históricos y publicación

- ADBE: `precio=239,94` USD coincide con corte 30-sep-2026 y hoja; `precioAnalisis=251,67` USD proviene de edición distinta.
- ONON: `precio=29,61` USD coincide con corte y hoja; `precioAnalisis=30,20` USD proviene de registro anterior sin fecha de cotización confirmada.
- El visor y Research tienen corregido el dato visible del corte (Modelo-JMR#111). La migración de los campos originales de los JSON **aún no se completó**; están conservados, no se deben presentar como precio actual ni afirmar que el registro fue actualizado.
- GitHub Pages: CI de la aplicación aprobó; la URL pública no fue accesible desde el entorno de consulta, así que **no se afirma prueba visual de navegación**.
- 7 múltiplos por empresa: mantenidos, no alterados; P/V y P/BV siguen provisionales con peso cero conforme a la revisión publicada.

**Dictamen:** la consistencia aritmética de los 8 DCF es positiva dentro del alcance descrito. Permanecen `PUBLICADO_CON_SALVEDADES` / `PENDIENTE_VALIDACION_INTEGRAL` por límites de cobertura y la discrepancia entre ficha y hoja NVO, además de otras salvedades narrativas ya identificadas. No se alteraron supuestos económicos ni se duplicaron valoraciones.
