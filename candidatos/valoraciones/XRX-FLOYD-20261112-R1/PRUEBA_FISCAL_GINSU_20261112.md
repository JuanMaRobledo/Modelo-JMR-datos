> ANTECEDENTE VÁLIDO DE REGRESIÓN. Ahora el selector fiscal separado está implantado en el candidato; la maestra sigue intacta. Ver MANTENIMIENTO_FISCAL_204.md y9regresiones adicionales. Los resultados brutos no son valores certificados del común.

# XRX-FLOYD-20261112-R1 — Tres Ginsu: prueba fiscal completa, copia temporal

**12-nov-2026. Evidencia reproducible, NO DCF aprobado del patrimonio común.**

Se copió el libro original único a una prueba TEMPORAL y se ejecutó el motor Damodaran en cada historia. Sólo en la copia, se sustituyó temporalmente Input sheet B23, originalmente fórmula vinculada a la tasa efectiva LTM −6,4%. Se probó 0% y 25% en los tres motores (el motor luego converge de cero a marginal 25% hasta año 10). Se restauró la fórmula exacta original en los tres Input sheet, se verificó recuperación de los tres valores iniciales y se descartó la copia. **No se modificó ninguna fórmula ni histórico en el libro oficial.**

| Tratamiento tasa fiscal inicial del motor | Conservadora bruto US$/acc | Base bruto US$/acc | Optimista bruto US$/acc |
|---|---:|---:|---:|
| −6,4% LTM histórico enlazado (salida vigente no certificada) | −15,4504146620 | −4,7195007015 | +8,5830452928 |
| 0% inicial con convergencia 25% terminal (hipótesis cash tax optimista) | −15,5071800000 | −5,2783951945 | +7,5280664754 |
| 25% desde FY1 (stress sin uso de escudo) | −15,7289196015 | −7,4615768076 | +3,4070554697 |

Cada fila **es un resultado del Ginsu real en copia**; no equivale a valor del común, falta integrar deuda/Series A/otros instrumentos y riesgo de default. El 10-Q Q3 2026 incluye impuesto contable positivo de US$59m aunque hay pérdida antes de impuestos, por lo que incluso 0% cash tax NO está confirmado por jurisdicción. El 10-K FY2025 reporta NOL US$8.100m nominales y allowance de DTA US$1.933m; ninguna fila autoriza meter US$8.100m de NOL directo en modelo.

## Puente exclusivamente algebraico de deuda + Series A, NO intrínseco

El Ginsu bruto deduce deuda tradicional contable US$4.220m y NCI US$16m, suma caja US$412m. Si se sustrae TAMBIÉN el pasivo por financiación de crédito IEEPA US$81m y la preferencia Series A no convertida US$180m, con deuda *book* (ya deducida) el Base da residual NEGATIVO en los tres casos y un valor del común con responsabilidad limitada NO negativo (no significa valor intrínseco exactamente cero). Si se sustituye sólo deuda book 4.220m por fair value SEC 2.893m, diferencial +1.327m, resulta como prueba algebraica:

| Base | Capital común residual antes warrants/default US$/acc |
|---|---:|
| ETR LTM histórica −6,4% (prospectiva inválida) | ≈ 3,28 |
| Cash tax 0% inicial→25% terminal | ≈ 2,72 |
| Tax 25% desde FY1 | ≈ 0,54 |

Estas cifras **NO deben publicarse como precio intrínseco ni MOS**: el descuento de bonos refleja riesgo default, que exige EV/WACC y opción patrimonial consistentes, y los derechos Series A pueden convertirse en 6,741576m acciones en vez de ser deducidos como liquidación, no simultáneamente.

## Integridad de la prueba
Tras probar tasas 0 y 25 se restauraron las tres fórmulas exactas:

`=IF('Income Statement'!L29="";"";ROUND('Income Statement'!L29;4))`

Readback: B23 = −0,064 en las 3 historias; DCF bruto Base = −4,719500701535878, C = −15,450414662015213, O = +8,58304529280968. La copia será eliminada. Los controles R3 del ORIGINAL, matrices 75 y cuatro inversos, permanecen VIGENTE (sólo si inputs originales no cambian).

## Estado de cierre

El estudio determina método y cuantifica impactos para XRX-07, XRX-03 y XRX-08; **NO autoriza marcar dichos críticos CERRADO** mientras no se integre una entrada de tasa prospectiva sin falsear B23, mientras el puente del valor común no use deuda consistente y derechos completos y mientras R2 siga incompleto. Issue de mantenimiento: https://github.com/JuanMaRobledo/Modelo-JMR/issues/204 .

Fuente 10-Q 30Sep26: https://www.sec.gov/Archives/edgar/data/1770450/000177045026000051/xrx-20260930.htm
Fuente 10-K FY25: https://www.sec.gov/Archives/edgar/data/1770450/000177045026000009/xrx-20251231.htm
Libro oficial: https://docs.google.com/spreadsheets/d/110kJtFEN9GL43ndBhCA6zpZh6HW6DDFDmCH4pbl7l0k/edit
