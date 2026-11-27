# CELH Floyd R1–R6 · diagnóstico económico de preferentes Pepsi A y B

**Revisión:** `CELH-REBOOT-3T26-R1` · **Estado:** CANDIDATO · **Fecha precio:** cierre US$33,19 del 09/11/2026 · **Corte SEC:** 30/09/2026. **No es un puente de valor certificado** ni reemplaza los datos o fórmulas de los tres Ginsu.

## Documentos primarios

- SEC 10-Q al 30/09/2026, nota 12 «Mezzanine Equity», pp. 29–33: https://www.sec.gov/Archives/edgar/data/1341766/000134176626000062/celh-20260930.htm
- SEC 10-K FY2025, nota valoración modificación Serie A: https://www.sec.gov/Archives/edgar/data/1341766/000134176626000024/celh-20251231.htm

En el balance 9M2026, las Series A/B se clasifican como **mezzanine equity**, valor contable US$852,355 M + US$907,620 M = US$1.759,975 M. Su preferencia nominal total es US$1.135 M (A 550 + B 585), con dividendos acumulativos de **5%** y potencial conversión A 22,0 millones de comunes a US$25 / B 11,3 millones a US$51,75. La conversión automática desde agosto2031 requiere umbral de participación de mercado y VWAP; desde agosto2032 puede existir conversión a elección de la compañía y derechos de rescate a 2032/35/38. La empresa declaró que en septiembre2026 **no consideraba probable la redimibilidad** y esperaba conversión antes del rescate.

La SEC describe un **Monte Carlo** usado en la modificación de 2025, con **volatilidad 60%** y **probabilidad de condiciones de mercado 90%** a la fecha de esa modificación, así como rf **3,9%** y precio común US$59,69 vigentes *en 2025*. Estos valores **no están recalibrados al 09/11/2026**. Para experimentar con sensibilidad solo se reutilizan sigma y q como *hipótesis de prueba*, mientras rf se toma de Treasury 10Y 4,88% al 09/11/2026.

## Diagnóstico reproducible de puente con opción europea (aproximación, no el contrato completo)

Un enfoque más informativo que sustraer el capital preferente contable es aproximar su reclamación en el patrimonio operativo con dos componentes: (a) nominal y flujo de dividendos, (b) valor contingente de conversión por Serie A/B. Para **cada escenario** resolvemos de manera autoconsistente la ecuación en el precio por ordinaria `p`:

```text
Equity_Ginsu_s = p * 251.725
  + [1135 * exp(-r*T) + (1135*0.05/r)*(1-exp(-r*T))
     + q*(22*BS_call(p,25,r,sigma,T)+11.3*BS_call(p,51.75,r,sigma,T))]
T = 5.79 años hasta 28-agosto-2032; r=0.0488; sigma=0.60; q=0.90.
BS_call(s,k) = s*N(d1) - k*exp(-r*T)*N(d2)
d1=(ln(s/k)+(r+sigma^2/2)*T)/(sigma*sqrt(T)); d2=d1-sigma*sqrt(T).
```

Todas las cantidades monetarias de la ecuación están en millones de USD, acciones en millones; `p` en USD/acción. Equity Ginsu antes de preferentes (millones): Conservadora **4.442,906872**; Base **7.995,429897**; Optimista **12.584,920113**. Los dividendos se aproximan como renta anual de 5% del nominal hasta 2032.

| Escenario | Equity Ginsu antes preferentes (US$ M) | Preferentes aproximadas (US$ M) | Común por acción (US$) | Puente estático anterior (US$) |
|---|---:|---:|---:|---:|
| Conservadora | 4.442,91 | 1.283,94 | 12,55 | 13,14 |
| Base | 7.995,43 | 1.557,41 | 25,58 | 27,07 |
| Optimista | 12.584,92 | 1.966,12 | 42,18 | 43,84 |

**Solo diagnóstico:** ponderación tentativa 25/50/25 produce **US$26,47** por acción y `MOS35%(Base)` **US$16,62**, frente al cierre fijado US$33,19. El cambio del Base frente al puente estático es aproximadamente **−US$1,50 por acción**, material para el margen de seguridad.

### Sensibilidad del Base (US$/acción ordinaria)

| Volatilidad / Probabilidad condicionada | 50% | 90% | 100% |
|---|---:|---:|---:|
| 40% | 26,52 | 26,00 | 25,87 |
| 60% | 26,27 | 25,58 | 25,41 |
| 80% | 26,06 | 25,22 | 25,02 |

Con sigma 60%, q 90% y spread de crédito sobre rf de 0/1/3 puntos porcentuales, el valor común del Base resulta US$25,58 / US$25,78 / US$26,15 respectivamente. Estas variaciones son sensibilidad a **supuestos no confirmados**, no probabilidades asignadas a historias CELH.

## Por qué **no** es una certificación suficiente

1. Una opción **europea Black–Scholes** sobre el precio común simplifica derechos contractuales de conversión, distribución, eventos corporativos, rescate y pagos en tres cuotas, además de la posible conversión anticipada en 2031. El 90% de 2025 no es una probabilidad verificada a 2026 y sigma de la modificación no es necesariamente la volatilidad esperada al corte.
2. No incorpora explícitamente acciones comunes concedidas mediante RSU/PSU, ni probabilidad de incumplimiento de las preferentes, impuestos/deducciones y cambio de control; no ha reconciliado el tratamiento de pagos de dividendos preferentes con un WACC que contemple financing mezzanine.
3. El valor intrínseco de una acción es supuesto subyacente del propio puente: el cálculo ilustrativo usa una solución implícita, pero no reemplaza la simulación del contrato que dependería de procesos estocásticos, derechos de decisión y condicional de cuota de mercado.
4. La lectura económica podría diferir de la contable y existe riesgo de doble descuento si se sustrae la mezzanine de libros y a la vez se diluyen todas las acciones potenciales. Por ello el puente estático anterior y este nuevo **no deben mezclarse ni presentarse como valor aprobado**.
5. Las tasas, normalización de EBIT, ROIC terminal vs año10 y múltiplos siguen sujetos a controles R3/R4. Las plantillas originales del Ginsu y las matrices DCF se dejan intactas.

### Acción concreta para R3/R4

Elaborar **en infraestructura de mantenimiento separada**, sin cambiar ninguna de las 17 hojas Damodaran, un módulo que reproduzca el waterfall contractual con plazos 2031/32/35/38, pagos de dividendos, market-share condition, VWAP, posibles conversiones/rescates y crédito. Contrastar salida con la nota SEC y el precio/preferentes observables; documentar sensibilidad amplia y conciliación del valor total equity. Registrar el resultado como ajuste económico de acciones ordinarias y alimentar R4, evitando que el DCF Ginsu pre-preferentes B33 se publique sin puente. **R6 permanecerá como auditoría independiente**.

Fuente de valores Ginsu y sensibilidades de base: `SENSIBILIDADES_R3_CELH.json`. La validación previa de M sigue `NO PUBLICAR`. **Publicación bloqueada materialmente.**
