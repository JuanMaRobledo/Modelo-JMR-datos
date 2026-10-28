# CMG · reinicio: cálculos cargados, entrega incompleta

Revisión: `CMG-2026-10-28-R1-REINICIO`. Rama: `ccr-e19723cb-q1m72p`.

**Estado: PREPARACION. Auditoría económica PENDIENTE. No es un dictamen ni una publicación EN_REVISION comprobada.**

Hoja: https://docs.google.com/spreadsheets/d/1SF3cYhIe01LazAiW4klGgYd6QrYG_uC-X-A8N5yYETc/edit

## Resultados provisionales de las fórmulas

| Concepto | US$ por acción |
|---|---:|
| DCF Base | 24,936927 |
| Conservadora | 11,061541 |
| Optimista | 32,227385 |
| Disrupción | 3,717439 |
| Promedio ordinario (sin Disrupción) | 23,290695 |
| Precio con MOS 35% sobre Base | 16,209003 |

Precio al corte 30-sep-2026: US$31,95. WACC inicial 7,992658%; terminal 8,99%; g 4%. El inverso del motor existente exige ~14,3573% anual uniforme en años 1–5 con margen objetivo 17% y el resto constante. VP terminal / VP operativo ~68,84%.

Los siete múltiplos ya calculan por historia. Base, valor presente consolidado: EV/EBITDA 22,967050; EV/FCFF 21,226597; P/E 40,656766; P/FCFE 27,525242; P/OCF 28,378057; P/S 42,289533; P/BV 33,783252. P/S y P/BV tienen peso cero justificado. No usar el ponderado como valor principal ni base del MOS.

## Comprobaciones realizadas

- Comparación de las 61 pestañas: 21.265 fórmulas originales, cero diferencias salvo exclusión expresa de C25; 122 validaciones conservadas. No se hicieron cambios de pestañas, dimensiones ni orden.
- 66 identidades contables/relaciones de cálculo sobre las once columnas, cero fallos a tolerancia de US$0,005M.
- Las cuatro historias concilian con el código nativo de `Modelo-JMR/docs/jmr_engine.js`, diferencia máxima menor de US$0,000001/acción.
- Tres matrices de sensibilidad existentes: centros iguales al DCF Base, controles de centro OK. Falta verificar/completar el alcance preciso de la matriz de WACC terminal exigida.
- No se ejecutaron los verificadores Python ni Playwright: el entorno de ejecución está indisponible. Los conectores permitieron aplicar entradas, leer resultados y ejecutar el motor JS original.

## Correcciones adicionales

Se corrigieron utilidades/impuestos redondeados, un segundo split indebido en 2022–2023 y el LTM de acciones promedio (ponderado por días, no suma/resta de promedios). Las acciones al cierre fiscal no se toman de la portada posterior. Se preservó B16 de la maestra y se concilió el solapamiento de leases; el vencimiento de deuda recta no usa el plazo contractual de arrendamientos, evitando descontar su pasivo una segunda vez. El MOS faltante en H14 se completó con fórmula.

Se registraron `reference/damodaran/CMG.json`, ciclo de vida, moat y decisiones de los siete métodos. `scripts/cmg_entradas.py` reproduce 210 entradas/notas y comprueba contra la maestra antes de escribir. La carga de estados prioriza 10-K/10-Q sobre comunicados redondeados, evita doble split y pondera acciones LTM por días. Los cambios Python no pudieron ejecutarse en este entorno; la comprobación del motor original JS sí se realizó.

## Continuación obligatoria

1. Ejecutar controles técnicos Python en un entorno autenticado. Recuperar/conciliar `unificacion_hojas.py`, que no existe en esta rama; no afirmar una corrida exitosa.
2. Revisar materialidad de Kd/volatilidad proxy, vesting y tratamiento separado de RSU/PSU, participaciones privadas, compromisos de leases sin iniciar y conciliación del capital operativo.
3. Completar textos, estadísticas, comprobación de restos de plantilla y alcance de sensibilidades. `Financials Multiples` conserva los promedios y acciones constantes de la maestra como supuestos provisionales; no se copiaron supuestos de SHAK.
4. Crear el artículo completo de 18 secciones y dos niveles: **todavía NO está creado**.
5. Exportar valoración y análisis, preparar registro de la misma revisión y catálogo EN_REVISION después de controles aprobados. La puerta no se ha saltado ni se ha inventado manifiesto.
6. Verificar app local con Playwright (expediente/lector/visor), y solo entonces pedir autorización para fusionar a main.

**No ejecutar ciegamente `build_story_sheet.py` sobre esta copia:** su camino legado limpia y reconstruye fórmulas, contrario a REGLAS_VIGENTES §11. Los cuatro DCF ya son los de la maestra; se cargaron sus entradas vacías y se preservaron sus fórmulas. El motor `damodaran_stories.py` ahora admite `s2c_6a10` para que cada historia conserve su segunda etapa; el constructor legado no se ha ejecutado.

No hubo eliminaciones en este turno ni consulta de valoraciones antiguas. Se conserva la carpeta personal CMG. La eliminación previa no es purga del historial Git ni de la papelera Drive, y permanecen referencias legítimas de terceros/mercado/transacciones del usuario.

Evidencia: `calculos-hoja.json`, `controles-tecnicos-conector.json`, `entradas-reproducibles.json`, `motor-hoja.json`, `snapshot-valores.json` en esta carpeta.
