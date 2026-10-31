# Modelo JMR — divergencias de hoja activa frente a JSON vigente

**Corte de observación:** 31-oct-2026, consulta de Google Sheets de solo lectura. Este documento no cambia modelos, hojas ni valoraciones. No certifica anclas económicas, cálculos de comparables ni autoriza publicación.

## Empresas con divergencia detectada

### UBER · UBER-20261030-A1
- Hoja fuente: [Modelo original](https://docs.google.com/spreadsheets/d/1i0B9cPX-z5G7GtqGmU3lVbJP0l6AyhhYhF0x8pQ8B58/edit).
- JSON oficial en rama #211: **peso DCF 1,0 y múltiplos 0,0**. Mantiene DCF Base **US$91,13793738151752** y `sensibilidadMultiples` sin matrices oficiales; la captura anterior registraba siete N/D.
- La hoja **actual** `Descuento de múltiplos` usa **0,6 DCF / 0,4 múltiplos**, con cinco métodos de peso 0,1 / 0,15 / 0,05 / 0,05 / 0,05 y sus descuentos Conservador, Base y Optimista calculados. El DCF Base de la hoja **sí** coincide con el JSON: US$91,13793738151752; cambian los pesos secundarios y la fuente relativa.
- La hoja `Sensibilidad por múltiplo` ahora devuelve **cinco matrices Base 5×5 OK** (EV/EBITDA, EV/FCFF, P/E, P/FCFE y P/OCF), P/V y P/BV N/D. Esto diverge de la captura parcial anterior.
- **Riesgo de anclas:** `Supuestos de los Múltiplos!A5:H9` marca **“Sí — revisar”** en la columna de override manual para los cinco métodos. La política escrita habla de mínimo múltiplo positivo de cuatro cierres y ajuste conservador/optimista, pero los overrides deben justificarse documentalmente por método; no basta que la matriz calcule un centro.
- **Decisión de protección:** NO actualizar `descuentoMultiples`, pesos, matrices o recomendación en el JSON hasta reconciliar la nueva versión fuente y el criterio de anclas. Mantener gate bloqueado y no declarar UBER completada.

### GOOGL · GOOGL-20261029-R5
- Hoja fuente: [Modelo de Google](https://docs.google.com/spreadsheets/d/1we5M6ZMziOkTVHttcQWoerKhYqbQoWAbkoGeDZfb7bA/edit).
- JSON en #211: no incorpora matrices Base nativas oficiales; captura anterior con tres métodos OK (EV/EBITDA, EV/FCFF y P/V) y otros N/D.
- Consulta actual: **seis métodos calculados** EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF, P/V; P/BV N/D. Los centros observados ya no coinciden necesariamente con la captura antigua; requiere nueva fotografía integral y pruebas de identidades.
- El DCF Base de la hoja coincide con el expediente (**US$287,20493379569007**) y la hoja conserva pesos de 0,6 DCF / 0,4 múltiplos. Descuentos conservador y optimista de múltiplos siguen parcialmente sin consolidar.
- **Decisión de protección:** no importar centros de la revisión vieja ni rellenar P/BV con un dato inventado. Obtener foto integral contemporánea y justificar anclas, especialmente las dependientes del resultado y del CapEx/I+D de IA.

### INTU · INTU-20261029-R1
- Hoja: [INTU Método A](https://docs.google.com/spreadsheets/d/1SkW8M3meAfvGDgj9Evg7PqPAJZiLw44cWKPHL5yC7QU/edit).
- La hoja nativa `Sensibilidad por múltiplo` continúa con siete N/D; las seis cuadrículas de `Múltiplos A - INTU` son exploratorias y **no son integración nativa**. Mantener la advertencia del Nivel 2 y el DCF oficial.
- Antes de llenar el motor relativo, definir anclas y fuentes por empresa/escenario y verificar que el libro alternativo sea consistente con la revisión activa.

### NU · NU-20261029-R1
- Hoja: [NU FCFE bancario](https://docs.google.com/spreadsheets/d/1PMtFbAoT-rM5O3DnAlnd4JEGPAky15v24NNPjoQS9kI/edit).
- El negocio es financiero y requiere P/E, P/FCFE y P/BV sobre un modelo **DCF FCFE bancario con costo del patrimonio**; no usar EV/EBITDA o EV/FCFF de empresas industriales ni tratar depósitos como deuda operativa.
- Las filas industriales `Sensibilidad por múltiplo` no constituyen por sí solas fuente de matrices bancarias. Investigar las pestañas `FCFE bancario A` y `Sensibilidad FCFE A`, identificar anclas, y construir contrato bancario independiente validado antes de integrar.

## Integraciones ya completadas con no regresión
- SHAK y MELI: fotografías de 30 rangos, fórmulas y centro FY+3 verificadas, DCF y MOS preservados, dos N/A por flujo negativo y peso cero; versiones anteriores archivadas como evidencia inmutable en la rama.
- Otras 14 empresas: integraciones anteriores preservadas; NO modificar supuestos ni forzar tres escenarios donde la hoja tiene resultados no disponibles.

## Control de calidad y próxima decisión
1. Mantener las cuatro revisiones anteriores `EN_REVISION` y conservar el JSON del catálogo como fuente canónica hasta una revisión técnica nueva.
2. Para UBER, exigir anclas y overrides documentados, suma de ponderaciones, descuento por horizonte, centro VP3 y puente al valor presente; cotejar la discrepancia **100/0 contra 60/40**.
3. Para GOOGL, repetir fotografía integral del libro actual y verificar el cambio de cinco métodos que pasan respecto de la captura vieja.
4. Para INTU y NU, completar sus contratos de múltiplos apropiados con pruebas específicas, no con constantes ficticias.
5. Solo entonces repetir CI financiero y QA visual coordinado con la aplicación #151. No fusionar con gate fallido.
