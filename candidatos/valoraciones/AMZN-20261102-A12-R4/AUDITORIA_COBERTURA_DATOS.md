# AMZN R4 · Auditoría de cobertura e integridad — revisión 2-nov-2026

**Estado real: Fase 1 pendiente de recertificación; no dar por «datos completos», no publicar, no certificar múltiplos.**
**Hoja:** https://docs.google.com/spreadsheets/d/10qfoGrEP1PgdlLWrHvfoHqExKDZbPK75yb_oINlO4a8/edit
**Fuentes primarias:** https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm y https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm.

## Correcciones comprobadas en esta revisión
- En `Cash Flow Statement!I33:L33` se agregaron **fórmulas** de conciliación de otros flujos de financiación, sin inventar que los agregados SEC de «short-term debt, and other» sean deuda pura. Comprobación independiente: FY2023 −12.203, FY2024 −2.630, FY2025 −991, LTM sep2026 −1.867 USD M. Los valores se derivan de total CFF menos deuda de largo plazo neta/recompras, e incluyen movimientos de deuda corta + arrendamientos financieros + financing obligations. Fuentes 10-K FY2025 p.36 y 10-Q sep2026 p.3. No sumar de nuevo en filas 24/25.
- Se añadieron `Cash Flow Statement!I28:L28` como fórmulas de deuda a largo plazo neta y `I40:L40` desde el **dato publicado** por SEC de variación de caja, con efecto cambiario explícito: FY2023 +19.637, FY2024 +8.422, FY2025 +7.794, LTM2026 −11.750 USD M. Conciliación CFO + CFI + CFF + FX = variación de caja.
- Los saldos de deuda corriente/leases de FY2025 y sep2026 fueron revisados antes de esta sesión contra notas SEC, y al leer la hoja **ya habían cambiado**: `Balance Sheet!K20=3.561`, `L20=7.633`, con `K19=57.760`, `L19=53.967`. El nuevo valor incluye obligaciones de financiación de instalaciones y crédito corto; todavía se exige conciliación y revisión económica de deuda del DCF. **No se sobrescribieron durante este control.**
- `Input sheet!B35` muestra 5,29% con nota «Rf USD del corte Damodaran 01-oct-2026 (observación 30-sep)». El precio AMZN sigue al 30-oct; es una elección de corte financiero/mercado distinta que debe documentarse y sensibilizarse. La nota NO equivale a tasa spot 30-oct. No se modificó la tasa.

## Vacíos materiales y semánticos observados

| Pestaña / rango | Observación en lectura del 2-nov | Tratamiento exigido |
|---|---|---|
| `Income Statement!B9:L10` | D&A en resultados e I+D separados no están presentes en SEC como líneas independientes; Technology and Infrastructure combina conceptos y D&A cash flow incluye leases y contenido | **No poner cero.** Registrar «incluido/no separado», datos por nota si publicados, y ajuste económico de I+D separado en fase 2 |
| `Balance Sheet!B7:L7`, `B12:L12`, `B23:L23` | Subcategorías (receivables, intangibles, otros pasivos) sin desglose específico | No rellenar arbitrariamente; extraer notas/XBRL donde sean aplicables, documentar subcategorías agrupadas |
| `Balance Sheet!B20:H21`, `B26:D26`, `B14:J14` | Deuda corriente, leases corrientes históricos y deuda lease previa a ASC 842 / inversiones LT no segregadas | Revisar notas de cada 10-K y ASC842. Pre-2019 leases no estaban en balance: «no reconocido», NO cero económico |
| `Cash Flow Statement!B19:L20`, `B24:L25`, `B29:L29`, `B32:L33` (parcial) | Líneas de M&A/desinversiones, short-term debt y otros movimientos, emisiones comunes y dividendos no individualizados | Verificar SEC. En FY2023–LTM2026 se agregó residual en fila 33; **no usar como deuda de corto plazo pura** |
| `Entradas históricas auxiliares!B4:L4` | Minority interests para EV sin evidencia numérica. La lectura de balance SEC 2025 y 2026 no presenta línea NCI separada | Validar ausencia o participación con notas; no presumir cero por una fila ausente. TEV/EV y EV multiples sin cálculo hasta cerrar |
| `Trailing Valuation!B6:L6`, `B19:L24` | EV y EV multiples vacíos porque puente EV–equity aún no tiene todos sus insumos | No publicar EV/EBITDA, EV/FCFF ni sensibilidades asociadas sin corregir y probar puente |
| `Input sheet!B9:B10`, `B17:B18`, `B21`, `B25`, conversores R&D/lease, `Cost of capital worksheet` | Industrias, decisiones capitalización I+D/leases, minoritarios, tasa marginal, beta, riesgo país, costo deuda y WACC pendientes | Supuestos económicos de Fase 2; completar con Damodaran/fuentes y justificación, no con ceros ficticios |
| `Escenarios e historias`, `Valuation output`, `Sensibilidad DCF`, `Sensibilidad por múltiplo` | Sin cuatro escenarios ni drivers calibrados | Correcto como F2 pendiente; no son «datos históricos» de F1 |
| `Financials Multiples!B15:D15`, `B54:D54` y sus proyecciones | **Defecto estructural:** `EBT − Taxes` sobre impuestos SEC negativos infla ingreso normalizado. Para 2023 B54 = 44.677 vs GAAP 30.425; FY2024 77.879 vs 59.248; FY2025 116.398 vs 77.670 | **Bloquear P/E y P/FCFE afectados.** Reparar plantilla una sola vez con pruebas de signo y equity-method. Issue del motor: https://github.com/JuanMaRobledo/JMR-valuation/issues/194 |

### Cuatro clases diferentes de «vacío»
- **Dato realmente faltante:** dato sí publicado pero no copiado en hoja; recuperarlo y anotar página, período, unidad y celda.
- **Dato no desglosado:** dejar N/D o anotación de agrupación, no inventar valor.
- **Indicador calculado en blanco:** revisar dependencia, fórmula y cotizaciones. Si falta insumo material, no publicar.
- **Supuesto económico no decidido:** corresponde a fase 2; resolver con evidencia y sensibilidad.

## Puertas de calidad
- La comparativa anterior reportó 5.357 fórmulas originales coincidentes en rangos A1:L80/120 de 46 pestañas, no fue `diff_formulas_plantilla.py` ni auditoría exhaustiva de todo el libro; no declarar test oficial OK.
- Faltan ejecución real de `estados_completos.py`, `auditar_estados_sec.py`, `auditar_ceros_materiales.py`, `diff_formulas_plantilla.py`, `inputs_completos.py` y `candados.py`. Requieren entorno motor y credenciales. Fase 2 se puede investigar con candidata, pero **NO dar como completados datos históricos ni publicar antes del cierre material**.
- Se reporta la discrepancia de criterio del anterior FASE_1_ENTREGA: el rótulo «apta» era de continuidad operativa, no «datos completos». Esta auditoría demuestra que faltan revisiones económicas y corrección de una fórmula de múltiplos que no es secundaria.
- No tocar R2/R3. Mantener R4 en estado CANDIDATO y PR en borrador.

**Siguiente trabajo operativo:** auditoría focalizada desde SEC de financiamiento e inversiones por año; corrección de fórmula tributaria en plantilla central + regresión; acreditación de ausencia/valor NCI; completar industria, WACC, capitalización de I+D, leases y valoración de activos no operativos en fase 2. Repetir controles de integridad y conciliación.
