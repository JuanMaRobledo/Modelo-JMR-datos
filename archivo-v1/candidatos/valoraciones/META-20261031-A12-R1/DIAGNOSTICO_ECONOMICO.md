# META · diagnóstico económico para Método A-1.2 · 31-oct-2026

**Estado:** borrador de análisis, **no es una nueva valoración** ni sustituye `META-20261025-R5`. Corte contable: **30-sep-2026**. Unidades: millones de USD salvo porcentajes y precio por acción.

## 1. Base financiera y normalización de resultados

| Métrica | Dato verificado | Origen / puente |
| --- | ---: | --- |
| Ingresos FY2025 | 200.966 | 10-K 2025 / serie histórica original |
| Ingresos 9M2026 | 181.712 | Resultados T3 2026 |
| Ingresos 9M2025 | 141.073 | Resultados T3 2026 |
| **Ingresos LTM T3 2026** | **241.605** | 200.966 + 181.712 − 141.073 |
| EBIT FY2025 | 83.276 | Estados de origen |
| EBIT 9M2026 | 54.635 | Resultados T3 2026 |
| EBIT 9M2025 | 58.531 | Resultados T3 2026 |
| **EBIT LTM GAAP** | **79.380** | 83.276 + 54.635 − 58.531 |
| Margen GAAP LTM | 32,855 % | 79.380 / 241.605 |
| Cargo jurídico extraordinario en T3 2026 | 9.890 | Nota 3T / acuerdo con fiscales |
| **EBIT LTM sin cargo legal** | **89.270** | 79.380 + 9.890; ajuste operativo candidato |
| Margen normalizado sin efecto I+D | 36,949 % | 89.270 / 241.605 |
| I+D LTM registrada | 76.544 | 57.372 FY2025 + 59.409 9M2026 − 40.237 9M2025 |
| I+D LTM ajustada con vida 3 años | **Pendiente** | Conversor cargado; faltan validación de amortización, consistencia de activos capitalizados y conciliación final |
| Efectivo + títulos líquidos 30-sep-2026 | 82.449 | Balance consolidado |
| Inversiones en participaciones no cotizadas (valor contable) | 32.624 | Balance; ajuste a valor económico pendiente |
| CapEx 2026 (guía, incluye cuotas principales de finance leases) | 135.000–145.000 | Guía oficial de Meta |
| Reality Labs pérdidas operativas FY2026 esperadas | 18.000–19.000 | Guía oficial, no eliminar automáticamente de EBIT |

**Principio anti-doble conteo:** si el EBIT proyectado excluye el cargo jurídico de 9.890, el pasivo/flujo futuro de litigios debe deducirse una sola vez en la conciliación de equity o el FCFF, tomando como referencia el importe razonablemente exigible y el pasivo registrado. **No** copiar 18.590 en el campo de `Minority interests` sin corregir concepto, confirmar saldo y trazabilidad. El libro antiguo asignaba esa cifra a «otras reclamaciones»; la plantilla nueva no.

## 2. IA, reinversión y capital invertido

El CapEx guiado de 135–145 mil millones es **gasto de inversión en propiedad y equipamiento e incluye principales de leases financieros**, no I+D corriente: no sumarlo de nuevo como I+D capitalizada. I+D de resultados se convierte a activo intangible analítico mediante el conversor y se amortiza según su vida útil (3 años en la fuente original, a justificar ante evolución tecnológica). La reinversión compatible con Damodaran debe incluir `CapEx neto + ΔNWC + inversión I+D capitalizable neta` o un Sales-to-Capital **calibrado sobre la misma base**, nunca ambos simultáneamente.

- CapEx materialmente adelantado al retorno esperado de infraestructura IA; por ello un S/C de corto plazo cercano a 0,45–0,55 puede ser defendible, pero **no debe prolongarse 10 años sin comprobar la maduración de la infraestructura**.
- ROIC histórico contable y ROIC ajustado por I+D no son comparables sin recalcular capital invertido. Exigir conciliación entre márgenes, S/C, reinversión y ROIC terminal.
- Parte del gasto de IA mejora publicidad (recomendaciones, conversiones y precio por impresión); otra parte persigue opcionalidad que puede tener baja o negativa rentabilidad. Separar una inversión core de las opciones de IA sin contarlas dos veces.
- SBC 9M2026 de 21.053: reconocer efecto en el coste económico/dilución y no presentarlo como caja libre sin contrapartida para el accionista.

## 3. Coste de capital y riesgo de mercado

Damodaran estima a comienzos de octubre de 2026 una tasa del Treasury estadounidense a 10 años de **5,29 %** y una prima implícita de riesgo de acciones de **3,70 %**. El coste de patrimonio no equivale a `Treasury + ERP`: añadir beta apalancada actual (y primas de países si pertinentes). El libro anterior utilizaba WACC inicial **10,5736 %** basado en ERP introducida de **4,9562 %**; no arrastrar ese WACC sin actualizar beta, estructura de deuda y riesgo del mercado.

El ciclo de META está en fase de **reinversión acelerada de infraestructura y monetización de IA**, con caja publicitaria operativa fuerte y nueva presión sobre FCFF y duración de ventaja competitiva. Los escenarios deben distinguir: 1) monetización publicitaria rentable, 2) capacidad de cómputo que tarda en producir retornos, 3) escalamiento rentable de IA, 4) disrupción o deterioro.

## 4. Requisitos previos a calcular DCF Base nuevo

1. Conciliar deuda total y arrendamientos, opciones/dilución y pasivo legal contra el 10-Q de 30-sep-2026.
2. Reconstruir el capital invertido y la amortización I+D en el nuevo libro; revisar comparabilidad con la última valoración.
3. Calibrar crecimiento anual 1–10, margen EBIT capitalizado, tasa fiscal normalizada, S/C inicial y de madurez, ROIC terminal y WACC con escenarios **individuales**.
4. Verificar que cada año `FCFF = EBIT(1 − tax) − reinversión`, que los VP descuentan al año correcto y que `EV − deuda + caja + activos no operativos − otras reclamaciones = Equity`, sin duplicaciones.
5. Conciliar sensibilidades DCF y cinco múltiplos prioritarios Base, diferenciando FY+3 de valor presente.
6. Completar Nivel 1 narrativo y Nivel 2 reproducible, más comparación separada AZ Stocks, antes de sustituir la revisión anterior.

## Fuentes primarias
- [Meta, resultados tercer trimestre de 2026, 21-oct-2026](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/)
- [Exhibit 99.1, SEC](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066700/meta-09302026xexhibit991.htm)
- [10-Q, período 30-sep-2026, SEC](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930_htm.xml)
- [Damodaran, Musings on Markets, octubre 2026](https://aswathdamodaran.blogspot.com/2026/10)
- [Fuente anterior META, hoja 68 pestañas](https://docs.google.com/spreadsheets/d/1Ap5ylZGNdW_qyEIH5dVy22jTfHSy1TNB5bFsiW1IXsg/edit)
- [Copia Método A-1.2, 46 pestañas](https://docs.google.com/spreadsheets/d/1lpE-L0Ai2NrWDhzBhtdeOMASwo7XRleUEMEMl3K34ss/edit)

**Sin publicación, fusión ni cambio a la valoración histórica.**
