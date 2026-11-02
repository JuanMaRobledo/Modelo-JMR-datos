# AMZN · AMZN-20261102-A12-R2 · Fase 1 · CERRADA CON CONTROLES PENDIENTES

**Fecha:** 2026-11-02
**Ejecutor:** ChatGPT GPT-6, esfuerzo de razonamiento no expuesto como configuración comprobable.
**Hoja candidata única:** https://docs.google.com/spreadsheets/d/1h6Xv5cNqwtKPpqI81KiZ_FNpTl4k_uQQS2QJEHphaBI/edit
**Plantilla oficial:** `reference/plantillas.json > vigente.ia` (46 pestañas).
**Entrega extensa e inventario:** https://drive.google.com/file/d/1fE-5Vkw2ciMUGU_RqilijMUgAqwe1QlX/view ; https://drive.google.com/file/d/1jcoPNXXh-8Y8rlz6HtLEm6iZ6I1RLhNM/view
**Estado valoración:** CANDIDATO, sin valor estimado, sin publicación, sin cambios a catálogo.
**AISLAMIENTO:** OK. Amazon.com, Inc., NASDAQ AMZN, CIK 0001018724, acción común, USD, ejercicio anual diciembre, modelo A-1.2, empresa operativa FCFF/WACC.

## Hecho y verificado
1. Copia IA nueva y diferente de plantilla y de hoja R1 retirada. El legado de 61 pestañas se archivó manteniendo ID.
2. Datos históricos FY2016–2025 y LTM Sep2026 en Income Statement, Balance Sheet y Cash Flow Statement, con notas de período, fuente SEC y clasificación de cada entrada. Estado LTM = FY2025 + 9M26 - 9M25; balance instantáneo al 30-sep-2026.
3. Datos LTM USD millones: ingresos 797455; EBIT GAAP 104366; CFO 168300; capex bruto -215192; venta de PPE e incentivos 4535; FCF reportado por Amazon -42357 (distinto del FCF bruto de fórmula CFO+capex = -46892). Resultado neto GAAP 134779 contaminado por partidas no operativas. Acciones medias LTM básicas 10788 y diluidas 10915 millones.
4. FINANCIACIÓN y cambio neto de efectivo reconstruidos históricamente: deuda corto y largo plazo, recompra FY2022 y principal de finance leases como componente de conciliación; R&D no separada se representa con 0 de **presentación**, no de inexistencia económica; current debt/current leases y participaciones privadas permanecen agrupadas donde las presenta la SEC, sin duplicación.
5. Pruebas manuales 11 períodos: 0 diferencias en ecuación de EBIT; 0 en balance activos=pasivos+patrimonio; 0 en CFO, CF investing y CF financing.
6. Comparación integral local mediante exportación oficial XLSX de plantilla y candidata, 46/46 pestañas, 20.740 fórmulas idénticas y 0 fórmulas sustituidas por número o vacío. Una divergencia de serialización en Input sheet!D12 se contrastó con la API Google Sheets, que muestra **fórmula original idéntica**. Resultado nativo equivalente: 20.741 fórmulas preservadas, 0 reemplazos. No equivale a ejecutar el script oficial.
7. Mercado AMZN cierre 30-oct-2026 USD240.35, US Treasury 10Y mismo día 4.94%. ERP Damodaran último documentado 3.70% fue calculado al 30-sep-2026 y publicado 1-oct-2026 con Rf5.29%. Para octubre puede documentarse SOLO COMO APROXIMACIÓN un rebase 3.70%+(5.29%-4.94%)=4.05% por conservación del retorno de mercado 8.99%; no es ERP calculado por Damodaran a 30-oct, requiere validación en Fase2. Cartera y corte global no modificados.
8. SEC: 10-K FY2025, 10-Q Sep2026 presentado 30-oct y 8-K 29-oct, con banderas sobre capex IA, revalorizaciones Anthropic/OpenAI, SBC, leases e inversiones privadas. Sin valoración, WACC ni escenarios de Fase2.

## Controles de cierre
| Control | Estado |
|---|---|
| 46 pestañas y aislamiento | OK comprobado |
| 11 períodos de inputs y conciliaciones aritméticas | OK local, no auditoría XBRL exhaustiva |
| Fórmulas de 46 hojas | OK comparación exportada y validación nativa D12; script oficial NO EJECUTADO |
| `estados_completos.py AMZN` | NO EJECUTADO — depende autenticación Google y `hoja_de()` del candidato R2 |
| `auditar_estados_sec.py AMZN` | NO EJECUTADO — requiere XBRL; el script tiene límite de presentación fija 2026-09-30 que excluye 10-Q actual |
| `diff_formulas_plantilla.py --sheet-id ...` | NO EJECUTADO como comando, prueba equivalente integral arriba |
| `novedades_sec.py --desde 2026-09-01 AMZN` | NO EJECUTADO; documentos SEC revisados manualmente |
| `inputs_completos.py` y `candados.py` | NO EJECUTADOS; valores de Fase2 intencionadamente en blanco |
| ERP exacto coherente 30-oct-2026 | PENDIENTE (rebase provisional indicado) |

**No registrar CERRADA hasta ejecutar o resolver los scripts obligatorios con ID R2**, sin modificar catálogo activo solo para que resuelvan la hoja nueva.

## Decisiones y juicios
- La Fase 1 contiene solo datos e inventario; no se arrastraron supuestos de la R1.
- La SEC incluye I+D dentro de tecnología e infraestructura; no se fabricó una cifra separada.
- Arrendamientos ya en balance, stock-based compensation y valores de inversiones privadas quedan como banderas para normalización en Fase2, no como ajustes valorados.
- La cifra FCF reportada por Amazon incluye ventas PPE/incentivos; el modelo base FCF bruto puede diferir. Dejar ambas definiciones visibles.
- Ceros de clasificación (no desglosado) tienen nota; NO significan ausencia económica.

## Pendiente o bloqueado
Correr controles oficiales con cliente autenticado y sheet_id R2, adaptar o parametrizar auditor SEC para 10-Q publicado 30-oct-2026, verificar documentos y anclas históricas restantes con XBRL y fijar metodología ERP del 30-oct. A partir de esos logs resolver estado final de Fase1; no forzar candados del modelo para simular completitud.

## Para Fase 2
Leer este documento y la hoja `1h6Xv5cNqwtKPpqI81KiZ_FNpTl4k_uQQS2QJEHphaBI`; no usar R1 archivada. Usar corte contable 30-sep-2026, precio 30-oct-2026 US$240.35. Las entradas de WACC/ERP y de historias intencionalmente no están fijadas. Según README fases vigente, la Fase2 se inicia **solo después** de que Fase1 se marque CERRADA tras sus controles.

## Fuentes
- https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
- https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm
- https://www.sec.gov/Archives/edgar/data/1018724/000101872426000038/0001018724-26-000038-index.htm
- https://www.sec.gov/Archives/edgar/data/1018724/000101872419000004/amzn-20181231x10k.htm
- https://stockanalysis.com/stocks/amzn/history/?period=daily
- https://ycharts.com/indicators/10_year_treasury_rate
- https://pages.stern.nyu.edu/adamodar/New_Home_Page/home.htm
