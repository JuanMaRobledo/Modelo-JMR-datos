# XRX · Investigación y solución de asuntos críticos · 12-nov-2026

Revisión única: XRX-FLOYD-20261112-R1. Estado CANDIDATO, no publicar.

Libro: https://docs.google.com/spreadsheets/d/110kJtFEN9GL43ndBhCA6zpZh6HW6DDFDmCH4pbl7l0k/edit

Análisis: https://docs.google.com/document/d/1QbkvjyS24sS3bA2IgF7tWfty4qXMZVRoZ7BuS21zKiM/edit

## Enfoque externo contrastado

Damodaran (*Dealing with Distress in Valuation*) propone valorar la empresa en marcha, estimar probabilidad/coste de distress, tener en cuenta deuda a VALOR DE MERCADO y tratar el equity altamente apalancado como opción residual con responsabilidad limitada. No transformar automáticamente el descuento de la deuda en beneficio para accionistas; no duplicar castigo por default en EV/WACC y flujos. Fuente: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/distresspaper.htm .

## XRX-01 · Arrendamientos
En 10-Q Q3 2025 (nota de arrendatario) Xerox divulgó $74m leasing operativo propio corriente y $265m no corriente, total $339m: ya se cargaron en auxiliares L29/L31. Leasing financiero $9m se presenta en otras obligaciones, no confundir con deuda bancaria. El 10-Q de Q3 2026 no ofrece el mismo desglose del pasivo lease propio; los $272m de equipos que Xerox ARRIENDA A SUS CLIENTES no son esa deuda. No imputar un histórico 2026 inventado. Las 19 dependencias de deuda/EV quedan N/D hasta fuente 2026 o mantenimiento permitido. Normativa JMR §4B-bis no permite excepto de deuda/EV material.

## XRX-03 + XRX-08 · Deuda, Series A y opción del común
SEC Q3 2026: deuda tradicional $4.220m en libros y fair value $2.893m, diferencia $1.327m. Otra obligación financiera $81m por monetizar créditos IEEPA, distinta de los préstamos. Valor financiero cautivo $1.481m de activos y $1.296m fondeo: mismo perímetro consolidado. Preferente Series A: 180.000 unidades, valor libro $214m y liquidación $180m, 8% acumulativo ($14,4m/año), posible conversión de 37,4532 comunes por preferente (6,741576m acciones potenciales). Se cargaron cantidad/ratio en las ENTRADAS admitidas del puente; fórmula original calculó 6,741576m. No restar simultáneamente preferente y sumar sus acciones convertidas.

EV Ginsu bruto Base $3.195,32m, caja $412m, NCI $16m. Solo SENSIBILIDAD ALGEBRAICA (NO DCF): con pasivo IEEPA 81, preferente liquidación 180 y deuda BOOK 4.220, residual común −$889,68m; con deuda FAIR VALUE 2.893, residual +$437,32m (~$3,28/acción antes de impuestos, warrants, SBC, default y caja restringida). Estas cifras no son valores intrínsecos certificados; conciliar Kd, WACC, deuda y riesgo. Valorar aparte equity como opción; no anticipar canje anunciado para el 13-nov-2026.

## XRX-07 · Impuestos
Modelo: Input sheet B23 conserva correctamente ETR histórica LTM −6,4% desde Income Statement L29. Ginsu Valuation output C6:G6 aplica −6,4% a EBIT futuro positivo (FY+1 EBIT $109,212m; NOPAT $116,202m), concediendo un beneficio fiscal no documentado. El 10-K FY2025 revela NOL nominales $6.500m expirando 2026–2045 y $1.600m sin caducidad, pero DTA brutos $2.242m, valuation allowance $1.933m y DTA netos $309m. NO asumir los $8.100m como NOL íntegramente realizable.

Test diagnóstico estático, sin tocar Ginsu: eliminar tipos fiscales negativos sobre EBIT positivo reduce valor presente $51,72m (~$0,388/acción), aplicar 25% marginal desde FY+1 lo reduce ~$365,27m (~$2,742/acción). No son nuevos DCF. SOLUCIÓN: entrada separada y validada de impuesto efectivo PROSPECTIVO según jurisdicción, realizabilidad del NOL y tasa terminal; conservar histórico B23, motores, fórmulas y comentarios. Según REGLAS §0R.1, la plantilla requiere mantenimiento separado y autorización expresa con respaldo y pruebas. Mantener crítico hasta corrección.

## XRX-09 · Múltiplos y normalización
EBITDA GAAP mecánico LTM ~−$529m incluye impairments ~959m. Reversar sólo impairment daría ~$430m, todavía no EBITDA sostenible. Presentación Xerox Q3 2026 indica EBITDA AJUSTADO FY2026 $739m con ventaja tarifaria no recurrente IEEPA $105m: contraste FY2026 sin ese one-off $634m. A precio $1,02 y 133,208753m acciones, market cap ~$135,873m. EV mercado con deuda SEC FV 2.893 + pasivo 81 + preferente proxy liquidación 180 + NCI16 − caja 412 + market cap = ~$2.893,873m, EV/EBITDA descriptivo ~4,56x. Con deuda en libros en vez de fair value, EV ~$4.220,873m y ratio ~6,66x. NO precio objetivo ni valor intrínseco. Guía FCF FY26 $50–100m incluye beneficio único de liquidez IEEPA $80m: contraste sin ese beneficio −$30m a +$20m, no FCFF sostenible. P/E GAAP N/M; P/FCFE y EV/FCFF no certificados; P/OCF CFO LTM131m afectado por amortización de cartera.

## WACC y puerta de publicación
WACC común 10,3% fue input directo, NO estimación detallada certificada. Damodaran reporta ERP EEUU 4,41% según payout ajustado al 1-nov-2026, diferente de 6% usado para Ke 12,18%; se debe escoger Rf/ERP mismo corte, beta bottom-up, mercado de deuda y tratamiento de escudo fiscal de pérdidas. Cualquier nuevo supuesto material exige repetir tres DCF, 75 matrices, inversos y firmas.

Estado: R2 NO CERRADO (19 N/D); R3 matrices VIGENTE pero conclusión económica del común no certificada; R4 no supera cobertura/métodos; R5 NO PUBLICAR. No cambiar catálogo ni fusionar PR #277 como publicación. XRX-05 sí quedó CERRADO editorialmente.

## Fuentes
- https://www.sec.gov/Archives/edgar/data/1770450/000177045026000051/xrx-20260930.htm
- https://www.sec.gov/Archives/edgar/data/1770450/000177045025000037/xrx-20250930.htm
- https://www.sec.gov/Archives/edgar/data/1770450/000177045026000009/xrx-20251231.htm
- https://investors.xerox.com/news-releases/news-release-details/xerox-releases-third-quarter-results-2
- https://investors.xerox.com/static-files/ad0eb5f8-bfee-4a44-b254-0770036c913d
- https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/distresspaper.htm
