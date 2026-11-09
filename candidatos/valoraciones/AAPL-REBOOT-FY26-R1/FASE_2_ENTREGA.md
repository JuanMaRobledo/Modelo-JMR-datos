# AAPL-REBOOT-FY26-R1 · Fase R2 (Históricos)

- **Fecha:** 2026-11-09 · **Agente:** Claude (Code, nube), herramientas: SEC XBRL (`data.sec.gov`), FMP, Alpha Vantage, FRED, Sheets · esfuerzo: medio.
- **Libro:** 01 HISTÓRICOS `1b1G1RciCJYH-J-RLXZhQX90RBlEZ-GY4qi13vSOdxEs` · estado **CANDIDATO conciliado**.
- **Decisiones del usuario aplicadas:** ERP 3,387 % escrita en `Country equity risk premiums!B1` de los tres libros DCF (2026-11-09).

## Qué se cargó
Diez años fiscales (FY2017–FY2026, cierres 2017-09-30 a 2026-09-26) más LTM (= FY2026, el corte coincide con el cierre) en `Income Statement`, `Balance Sheet`, `Cash Flow Statement`, `Entradas históricas auxiliares` (inventario, minoritarios y preferentes = 0 verificado, saldos iniciales FY2016 y FY2025) y precio por período en `Trailing Valuation` F3. Las hojas Trailing Valuation, Dividendos, Márgenes, Eficiencia de capital, Salud Financiera y Por acción **se calculan solas** (0 errores en 1.200 fórmulas). Detalle de fuente y clasificación por partida: hoja `Fuentes y clasificación`.

Fuente primaria: **XBRL del 10-K de la SEC** (`companyfacts`, CIK 0000320193; 10-K FY2026 acc. 0000320193-26-000026, presentado 2026-11-03), el 10-K más reciente que presenta cada período. El código y los datos están en `R2_evidencia/` (`extract.py`, `build.py`, `dataset_xbrl.json`; las rutas del script apuntan al directorio de trabajo de la sesión).

## Controles ejecutados
| Control | Resultado |
|---|---|
| Activos = pasivos + patrimonio, 10 años | APROBADO (0 diferencias) |
| Activo corriente = suma de componentes (con inventario) | APROBADO |
| EBIT + otros no operativos = antes de impuestos; antes de impuestos − impuesto = utilidad neta | APROBADO |
| CFO + CFI + CFF = cambio en caja; NI del flujo = NI del estado de resultados; partes del CFO suman el CFO | APROBADO |
| Ventas − costo − SG&A − I+D = EBIT (otros gastos operativos = 0) | APROBADO |
| Contraste externo FMP FY2024–FY2026 (resultados, balance, flujo de caja: totales y partidas principales) | APROBADO; PPE de FMP incluye derecho de uso (diferencia de clasificación, no de dato) |
| Contraste externo FY2017–FY2023 | **NO_EJECUTADO** (FMP limita a 3 años en este plan); solo cuadre interno |
| Precio LTM 342,37 con segunda fuente (Alpha Vantage) | APROBADO |
| Recálculo de EPS: 8,98 diluido FY2026 | APROBADO (coincide con FMP 8,98) |
| Fórmulas calculadas sin errores | APROBADO |
| `AISLAMIENTO=OK` | Sí: solo se usó el 10-K y mercado; nada de `archivo-v1/` ni del libro Floyd previo |

## Ajustes y salvedades materiales
1. **Split 4:1 (31-ago-2020):** acciones de FY2017 (promedio y cierre) y cierre de FY2018 no estaban reexpresadas en el XBRL; se multiplicaron por 4 para ser comparables con los precios ajustados. Con esto el EPS y la capitalización son consistentes.
2. **Intereses FY2024–FY2026:** Apple dejó de divulgarlos por separado; cobertura de intereses sin dato.
3. **Intangibles (decisión del usuario: «hazlo con el 10-K»):** se separaron del balance con las notas del 10-K (`IntangibleAssetsNetExcludingGoodwill`): 13.301 en FY2025 y 25.700 en FY2026 (LTM igual a FY2026); «otros activos LP» baja en el mismo importe. Antes de FY2025 las notas no informan el dato. **Goodwill:** el 10-K no lo informa en ningún año; se trató como 0 solo en FY2025–26 y LTM, como **supuesto** para habilitar los ratios tangibles. Resultado: retorno sobre activos tangibles 36,5 %, intangibles/activos 0,06x y valor libro tangible por acción 5,94 en FY2026 y LTM; antes de FY2026 siguen sin dato. FMP muestra 20.278 de intangibles en FY2026 (definición distinta); manda el 10-K.
4. **Residuales derivados (declarados):** otros activos LP, otros pasivos CP/LP, otros operativos/inversión/financiación del flujo de caja.
5. **Signo de «otros ajustes» del flujo de caja** corregido tras el contraste con FMP (un ingreso no monetario positivo resta del flujo).
6. **Alerta anterior retirada:** la tasa libre del repositorio (5,29 % al 30-sep) es correcta (FRED DGS10).

## Siguiente paso exacto
R3: cargar en el `Input sheet` de los tres libros DCF las entradas desde H (ingresos, EBIT, deuda, caja, acciones, impuestos, etc., LTM = FY2026) y escribir las tres historias. Definir la tasa de impuesto marginal, la beta/industria (Damodaran) y las historias con sus probabilidades.
