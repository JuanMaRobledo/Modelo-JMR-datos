# NKE, PYPL, EPAM, ZTS, NVO y ONON · resolución de pesos y descuentos · 1-nov-2026

**Estado: EN_REVISION, sin auditoría económica.** Resuelve la retención `RETENER_SIN_IMPORTAR_HASTA_CONCILIAR_PESOS` de `evidencia/conciliacion-descuentos-20261031.json`. DCF, MOS, escenarios, supuestos y matrices **no cambian**; solo `descuentoMultiples`, los pesos de `metodos` y la sección de múltiplos del Nivel 2.

**Qué se hizo.** Fotografía nueva de `Descuento de múltiplos!A1:M80` (valores y fórmulas) en `evidencia/descuentos-20261101/`; se integran con `integrar_descuentos_nativos` los 15 descuentos (cinco métodos × conservador, base y optimista), los pesos de la hoja y los valores a hoy. Antes el JSON tenía pesos genéricos 60/40, pesos por método en cero y escenarios conservador y optimista sin resultado. Los archivos anteriores están en `evidencia/descuentos-20261101/respaldo/<TICKER>/`.

**Los pesos son juicio del analista.** Salen de la categoría de empresa elegida en cada hoja (`Resumen de Valoración!G3`) y de la tabla de pesos de la plantilla, no de evidencia. Justificación de cada categoría:

| Ticker | Categoría | DCF / múltiplos | Pesos de los relativos (EV/EBITDA · EV/FCFF · P/E · P/FCFE · P/OCF) | Razón |
|---|---|---|---|---|
| NKE | Madura | 40 / 60 | 20 · 10 · 20 · 5 · 5 | Marca consolidada, crecimiento moderado y márgenes cíclicos; EV/EBITDA y P/E son los relativos habituales en consumo maduro. |
| PYPL | Madura | 40 / 60 | 20 · 10 · 20 · 5 · 5 | Pagos con crecimiento de un dígito y recompras. |
| EPAM | Genérico | 50 / 50 | 10 · 10 · 10 · 10 · 10 | Servicios de TI sin rasgo dominante; reparto equilibrado. |
| ZTS | Defensiva | 30 / 70 | 20 · 10 · 25 · 10 · 5 | Demanda estable y caja predecible; P/E y EV/EBITDA como anclas. |
| NVO | Biotech/Farma | 55 / 45 | 5 · 20 · 5 · 10 · 5 | Valor en flujos de cartera de productos; más peso a EV/FCFF. |
| ONON | Crecimiento | 60 / 40 | 10 · 15 · 5 · 5 · 5 | Crecimiento rápido con márgenes aún en convergencia. |

**Valores a hoy (US$/acción, historia Base).** DCF y ponderado DCF+múltiplos: NKE 37,73 → 36,84; PYPL 137,81 → 110,01; EPAM 184,41 → 197,70; ZTS 98,32 → 128,47; NVO 63,43 → 74,87; ONON 40,81 → 39,72. El valor principal publicado sigue siendo el DCF Base; el ponderado es secundario.

**Limitaciones que se mantienen.** Las anclas de los múltiplos de salida de estas hojas son las que tenían (columna de override manual en «Sí — revisar»): no se rehicieron con serie propia y pares como en NVDA y META, y no se certifican. Las categorías y pesos son subjetivos. `NVO` no tiene P/BV (N/D, opcional). Auditoría económica y QA visual pendientes.
