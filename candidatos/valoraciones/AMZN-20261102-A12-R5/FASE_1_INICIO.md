# AMZN · AMZN-20261102-A12-R5 · REINICIO DESDE PLANTILLA IA · FASE 1

**Estado:** INICIADA / SIN DATOS DE VALORACIÓN / NO PUBLICABLE.

**Instrucción del usuario:** descartar la hoja R4 como fuente de la nueva valoración y comenzar exclusivamente con una copia en blanco de la plantilla IA vigente. El usuario indicó que eliminará la hoja R4; el agente **no la eliminó**.

## Identidad y ubicación comprobadas
- Ticker: AMZN; emisor: Amazon.com, Inc.; metodología: JMR A-1.2, cinco fases.
- Revision ID: `AMZN-20261102-A12-R5`.
- Hoja: https://docs.google.com/spreadsheets/d/199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I/edit
- Copia creada desde **única plantilla IA registrada oficialmente**: `1e-lbQmCkObfq74YLpWnMmIidmcdsJQ-6uN4oiHnNTEQ`, indicada en `JMR-valuation/reference/plantillas.json`.
- Carpeta de destino: `Análisis/AMZN`, id `1q-BigOgle9iQgVeHsWwX3EDlDcgdnk3J`.
- Verificación real tras copia: exactamente 46 pestañas, incluidas Input sheet, Option value, R& D converter, Operating lease converter, Cost of capital worksheet, Financials Multiples, los cinco múltiplos prioritarios y hojas de escenario/sensibilidades. En muestras de Input sheet, tres estados e historias no hay importes financieros capturados; fórmulas originales y corrección TAX-194 están presentes.
- `Forward Valuation` permanece físicamente en esta plantilla vigente de 46 pestañas hasta migración validada a 45; no utilizarla como entrada obligatoria ni borrarla solo de la copia.

## Regla de aislamiento
- **R4, R3, R2 y todas las hojas antiguas quedan excluidas como fuentes de importes, drivers y valor intrínseco**. No hay migración de números de la hoja anterior; el expediente anterior permanece solo como rastro de incidente técnico, no como base económica.
- Datos fuente de AMZN solo desde SEC/10-K/10-Q/8-K, fuentes de cotización fechadas y Damodaran/Treasury según el corte que se fije con el usuario; todos deben volver a verificarse y capturarse en R5.
- No atribuir a R5 las cifras o precios que se calcularon en R4. Ningún DCF, WACC, escenario, múltiplo, MOS o auditoría ha sido ejecutado en esta nueva hoja.
- No modificar ni publicar el catálogo vigente. No fusionar hasta que existan entregas y controles pertinentes.

## Orden nuevo
1. Fase 1: captura estandarizada **de todas las dependencias materiales del DCF Damodaran y de los múltiplos**, incluyendo Input sheet y hojas auxiliares WACC, I+D, leases, Option value, NOL, riesgo y riesgo de fracaso cuando apliquen. Las hojas con valoraciones (DCF, cinco múltiplos, escenarios y sensibilidades) conservan fórmulas; reportar salida o N/D sin ficticios.
2. Fase 2: históricos completos hasta diez FY + LTM si existen, con fuentes y controles.
3. Fase 3: juicio sobre crecimiento, márgenes, ROIC, reinversión, S/C, WACC y valor terminal, con cambios cuantificados.
4. Fase 4: análisis Nivel 1/2 y publicación EN_REVISION solo con gates técnicos aprobados.
5. Fase 5: auditoría económica guiada por el usuario, independiente.

## Puerta de la fase 1
Ver [MAPA_INSUMOS_F1.md](MAPA_INSUMOS_F1.md). Una fila material sin valor, con fuente dudosa o sin control deja dependiente el DCF/múltiplo afectado. El agente debe documentar `VERIFICADO / PROXY EXPLICITO / N_D / NO_APLICA` para cada entrada; al terminar debe generar `FASE_1_ENTREGA.md` de **R5**, identificando celdas y cotejo. No generar valor de R5 a partir de uno previo.

**Estado de comprobaciones:**
- Copia de archivo y ubicación: **CONFIRMADAS**.
- Cantidad y identidad de pestañas, y blancos muestreados: **CONFIRMADOS**.
- Captura de datos, múltiples, proyecciones, WACC, opciones, I+D: **NO INICIADOS**.
- Pruebas de integridad financiera / CI / publicación: **NO EJECUTADAS**.
