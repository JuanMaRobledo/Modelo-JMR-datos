# AAPL-REBOOT-FY26-R1 · Fase R4 (múltiplos y resumen)

- **Fecha:** 2026-11-09 · **Agente:** Claude (Code, nube): Sheets, SEC XBRL · esfuerzo: alto.
- **Libro:** 03 MÚLTIPLOS `1SJn1NC6zGAWvMPOS6yK-0TxheNlZ0oabBPX8yaqpXmg` y `Resumen de valoraciones` / `Presentación` del DCF Base `1FDKimjBtpWeJO1wjK2-iFbQBhc7fziRWspCqkl41am8`. Estado **CANDIDATO** (R5 pendiente; sin auditoría F5).

## Resultado
| Valor por acción | Conservadora | **Base** | Optimista | Esperado (25/50/25) |
|---|---|---|---|---|
| DCF (principal) | 106,92 | **209,58** | 260,45 | 196,63 |
| Múltiplos consolidados (secundario) | 195,22 | 249,38 | 299,45 | 248,36 |
| Múltiplos frente al precio (342,37) | −43,0 % | −27,2 % | −12,5 % | −27,5 % |

Los múltiplos Base quedan **19 % por encima del DCF Base**; el precio de mercado, **37 % por encima de los múltiplos Base**. Ninguna historia, ni siquiera la Optimista por múltiplos, llega al precio. Conciliación en `Resumen de valoraciones`: probabilidades, orden Cons ≤ Base ≤ Opt, costo de capital común, Ke de M = Ke de la Base, pesos 100 % y combinado de M = recalculado → **CONCILIADO**.

**Por qué los múltiplos dan más que el DCF.** Los múltiplos de salida son medianas históricas de Apple (10 y 5 años) que ya descuentan crecimiento del 8–13 % y tasas bajas; el DCF Base exige 6 % de crecimiento, Ke de 10,35 % y costo de capital terminal de 8,25 %. La diferencia de 19 % es de método, no de datos: ambos usan los mismos supuestos operativos.

## Qué se cargó
- **Estados desde H (por etiqueta de fila):** FY2017–FY2026 + LTM en `Income Statement`, `Balance Sheet`, `Cash Flow Statement` (misma fuente XBRL del 10-K que el libro de Históricos). Diferencias de formato frente a H: la deuda corriente se separa en papel comercial (fila 20) y porción corriente de deuda + arrendamientos corrientes (fila 21); los arrendamientos no corrientes van en la fila 26; cambio de inventarios separado en el flujo de caja; EPS reportado (FY2017 dividido por 4 por el split). Ceros por «no presentado»: devengados e intangibles/goodwill antes de FY2025.
- **Precio:** 342,37 fijo (la plantilla traía `GOOGLEFINANCE`, que habría dado el precio del día de la consulta). Precios de cierre fiscal en `Trailing Valuation`.
- **Supuestos de las tres historias = los del DCF** (por multiplicadores sobre la base contable de M; verificado: crecimiento 6,0/2,5/9,0 % y 5,5/2,0/8,0 %, ventas/capital 3,0/2,4/3,5, crecimiento terminal 4,0 %, ROIC terminal 44,76 % o costo de capital en Conservadora, tasa efectiva 17 %, beta 1,30, ERP 4,23 %, Ke 10,3542 %, probabilidades 50/25/25).
- **Base contable distinta:** M no capitaliza I+D (usa EBIT reportado, margen actual 33,0 %). Los márgenes objetivo del DCF (37/31/40 % ajustados) se llevaron a base reportada restando el ajuste de I+D de FY2026 (3,54 puntos): **33,46 / 27,46 / 36,46 %**.
- **Entradas desde los tres DCF** (hoja `Entradas desde DCF`): valor por acción, Ke, Kd, WACC inicial y estable, EBIT reportado, beta y ERP; huella SHA-256 en el `Resumen de valoraciones`.

## Múltiplos de salida y pesos (juicio mío)
| Método | Conservadora | Base | Optimista | Peso total |
|---|---|---|---|---|
| EV/EBITDA | 21,17x | 23,57x | 25,97x | 8 % |
| EV/FCFF | 30,53x | 30,73x | 30,93x | 8 % |
| P/E | 26,47x | 30,08x | 33,69x | 9 % |
| P/FCFE | 23,99x | 28,74x | 33,49x | 7 % |
| P/OCF | 23,41x | 26,27x | 29,12x | 3 % |
**Regla:** Conservadora = mediana de 10 años (compresión a un régimen de menor crecimiento y tasas más altas: Rf hoy 4,86 %); Optimista = mediana de 5 años (sin más expansión pese a crecer 8 % y margen de 40 %); Base = punto medio. Todos ≤ múltiplo actual (cap del §5). No se usa el múltiplo actual (EV/EBITDA 29,2x; P/E 37,6x) porque repetiría el precio. **Pesos**, tipo «Madura» con DCF 65 % y múltiplos 35 %: EV/FCFF y EV/EBITDA (comparables entre estructuras de capital), P/E (EPS por recompras), P/FCFE (retorno al accionista), P/OCF al mínimo porque el flujo operativo incluye 13.789 de compensación en acciones. P/S y P/BV no se usan.
**Límite conocido:** el EV/FCFF de FY2023–25 está distorsionado por capital de trabajo (3 años: 44,7x); por eso se usan las medianas de 10 y 5 años (30,5x y 30,9x), casi iguales entre historias.

## Adaptaciones al libro (todas declaradas, ninguna cambia la matemática de múltiplos)
1. `Supuestos y control` B23: precio fijo en vez de `GOOGLEFINANCE`.
2. B18:D18: se quitó la condición «tasa de reinversión ≥ 0», que marcaba como inválida la Conservadora (EBIT decreciente por margen 27,5 %).
3. `J19` de cada método (múltiplo Base): sobrescribió su fórmula por defecto con un valor.
4. `B92:D92` impuesto efectivo 17 % en lugar del marginal 25 % para FY+1…FY+3, igual que el DCF.
5. `Income Statement` fila 14: **gasto por intereses ESTIMADO** (−3.700 FY2024, −3.500 FY2025, −3.000 FY2026 y LTM), no divulgado por Apple; hace falta para la compuerta. No altera múltiplos (afecta solo intereses/otros).
6. `POCF!B56`: corregido un error heredado de la plantilla (comparaba la sensibilidad central con la fila de la Optimista, no con la Base). Corregido también en la plantilla 03.
7. `Dividendos` fila 8: DPS oficial desde XBRL (FY2017 ÷ 4).

## Controles
| Control | Estado |
|---|---|
| Compuerta `Supuestos y control!B60` = «LISTA PARA CALCULAR»; 0 errores en las 16 hojas | APROBADO |
| Controles de P/OCF, P/E, P/FCFE, EV/EBITDA, EV/FCFF (cobertura, signos, sensibilidad central) | APROBADO (PE tiene la advertencia «revisar minoritarios»: Apple no tiene) |
| Estados de M con cuadres propios (activo corriente, activos = pasivos + patrimonio, CFO+CFI+CFF) | APROBADO |
| Conciliación `Resumen de valoraciones` (6 controles) | APROBADO |
| Verificación documental FY2017–FY2023 | **PENDIENTE** (contraste externo no ejecutado; FY2024–LTM verificados) |
| `Estado de fuentes primarias` = PENDIENTE; `Puente EEFF!B63` «REVISAR SIGNO I+D» (convención de signo de I+D, sin efecto: M no capitaliza I+D) | PARCIAL |
| Sensibilidad 5×5 por múltiplo | Disponible en cada hoja de método (solo Base) |
| Auditoría económica independiente | **NO_EJECUTADO (R6)** |

## Siguiente paso exacto
R5: adaptar la plantilla de Análisis y escribirla con Nivel 1 (14 capítulos) y Nivel 2 (12 apartados) usando las cifras de H, los tres DCF y M; generar los JSON de valoración y análisis con `contratoLibros=jmr-reboot-3libros-v1`; correr los validadores y dejar la revisión como CANDIDATO si la app aún no reconoce el contrato.
