# Diagnóstico de limpieza — sensibilidades de múltiplos Modelo A

**Corte técnico: 30-oct-2026; inspección de solo lectura, sin cambios de valores ni hojas.**
Este documento **no es auditoría económica** ni certificado de fórmulas. Los datos de GitHub
corresponden a la rama de revisión del PR #211; las celdas fueron consultadas directamente
en Google Sheets. No utilizar los hallazgos para completar matrices con cifras inventadas.

## 1. Inventario reproducible del catálogo

Comando: `node scripts/inventariar_cobertura_a.cjs` (también se ejecuta en CI
antes del gate). Su ejecución del 30-oct-2026 informa:

| Métrica | Resultado |
| --- | ---: |
| Expedientes activos en catálogo | 23 |
| Método A-1.2 en EN_REVISION | 20 |
| Revisiones anteriores al Método A | 3 |
| A con cinco prioridades en `descuentoMultiples.metodos` | 4 |
| A con controles de sensibilidad Base en el JSON | 2 |
| A con grillas 5×5 en `sensibilidadMultiples.matrices` | 0 |
| A con vínculo ausente de análisis a valoración | 0 |

Estos conteos **solo describen la estructura del JSON**, no prueban que las hojas
originales carezcan de fórmulas ni que los métodos sin datos exportados no existan.

## 2. Contraste de solo lectura con las hojas originales

Las dos hojas conservan las 46 pestañas oficiales y las tres necesarias:
`Financials Multiples`, `Descuento de múltiplos` y `Sensibilidad por múltiplo`.
Los datos siguientes proceden de la pestaña `Sensibilidad por múltiplo`,
filas 76–144; ancla JMR, historia Base. Se comprobó además que las 25 celdas
`B79:F83` de cada empresa contienen **fórmulas**, no constantes pegadas.

### SHAK — revisión SHAK-20261029-A12-R2

Hoja: https://docs.google.com/spreadsheets/d/1Okf7uchAUwWVMo7YPKcXVoT2UOWeGpEqzk0VrkbV8Fg/edit

| Método | Fila de inicio | Celdas numéricas de 25 | Centro VP FY+3 | Control hoja |
| --- | ---: | ---: | ---: | --- |
| EV/EBITDA | 76 | 25 | 104,5039032 | OK |
| EV/FCFF | 86 | 0 | N/D (VP3 original −26,56295135) | N/D |
| P/E | 96 | 25 | 27,25898088 | OK |
| P/FCFE | 106 | 0 | N/D (VP3 original −35,13063518) | N/D |
| P/OCF | 116 | 25 | 41,80192242 | OK |
| P/V, complementario | 126 | 25 | 27,25898088 | OK |
| P/BV, complementario | 136 | 25 | 33,9422117 | OK |

Los controles `N/D` no pueden transformarse silenciosamente en `N/A`.
Deben verificarse el denominador, su signo y la aplicabilidad económica.
La valoración activa ya contiene 7 controles de centro, pero **no la grilla
5×5 en el campo JSON oficial**.

### AFYA — revisión AFYA-20261029-R1

Hoja: https://docs.google.com/spreadsheets/d/1LSnX1JaZZNfClohhArAXjrMdbXfiCI4m_DETZbZkP94/edit

| Método | Fila de inicio | Celdas numéricas de 25 | Centro VP FY+3 | Control hoja |
| --- | ---: | ---: | ---: | --- |
| EV/EBITDA | 76 | 25 | 14,64033975 | OK |
| EV/FCFF | 86 | 25 | 12,24163334 | OK |
| P/E | 96 | 25 | 11,46538249 | OK |
| P/FCFE | 106 | 25 | 9,719536366 | OK |
| P/OCF | 116 | 25 | 9,86446777 | OK |
| P/V, complementario | 126 | 25 | 12,60273432 | OK |
| P/BV, complementario | 136 | 25 | 15,72212917 | OK |

Las 7 matrices muestran control `OK` y centro coincidente con el VP3
de la misma hoja a la precisión visualizada. El JSON activo carece de
`sensibilidadMultiples.matrices`, por lo que **la app no puede certificar
la grilla mediante los datos publicados**. El vínculo `linkedValuation`
faltante en el análisis de AFYA fue agregado al PR #211 con la misma revisión
y valor Base, sin cambiar contenido financiero.

## 3. Hallazgo técnico y ubicación de la corrección

- `JMR-valuation/scripts/jmr_capture_results.py` captura la región
  `'Sensibilidad por múltiplo'!A1:L230`, pero todavía solicitaba
  `'Auditoría DCF interna'`, pestaña ausente de los libros actuales de 46
  (la auditoría vive fuera de la valoración). Compatibilidad corregida,
  con pruebas, en el PR #181 de `JMR-valuation`.
- `JMR-valuation/scripts/jmr_revision_pipeline.py` ejecuta la foto
  y después el generador de sensibilidad; la información resultante no
  está trasladada íntegramente a `Modelo-JMR-datos/valoraciones/*.json`
  para los expedientes A inspeccionados.
- `jmr_multiples_sensitivity_base.py` genera matrices matemáticas a partir
  de resultados de la hoja. Antes de usarlo en la publicación actual, debe
  distinguirse el cálculo **nativo de la hoja** de una simulación externa:
  los campos publicados deben provenir de las celdas oficiales, con control
  de ancla y revisión, sin sobrescribir fórmulas ni salidas.
- `Modelo-JMR-datos/scripts/validar_catalogo.cjs` fue ajustado para
  reportar `BLOQUEO_FINANCIERO: faltan matrices Base 5×5 exportadas`
  y no exigir erróneamente 21/28 controles históricos a los expedientes A.
  El bloqueo sigue activo.

## 4. Trabajo pendiente y condición de cierre

1. **Prototipo de extracción creado en PR #181:** `scripts/jmr_native_sens_candidate.py`
   toma el bloque nativo Base de la foto `resultados_hoja.json`, conserva
   los 25 valores, ejes, centro, control, revisión, hoja y hash, y emite un
   **JSON candidato no publicado**. Sus pruebas unitarias pasan. Falta
   ejecutarlo sobre una foto de producción de cada revisión y conectarlo,
   tras conciliación, al JSON activo.
2. Para cada método prioritario aplicable, verificar 25 celdas numéricas,
   ambos ejes, valor VP FY+3 del centro, tipo de múltiplo, moneda, acciones
   y condición `N/A` o `N/D` documentada; P/V y P/BV opcionales.
3. Comprobar toda la cadena **hoja → JSON → ficha de la app** y los cinco
   múltiplos prioritarios por empresa. No usar la presencia de pestañas
   o títulos como prueba de cálculo.
4. Mantener todos los nuevos expedientes como `EN_REVISION` y el PR #211
   en borrador. No modificar precios ni publicar cierres económicos durante
   la limpieza. La auditoría sigue después de la revisión visual del usuario.

**Este documento es evidencia diagnóstica, no autorización de publicación.**
