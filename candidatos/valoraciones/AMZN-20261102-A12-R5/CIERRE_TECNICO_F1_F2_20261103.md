# AMZN R5 — acta técnica de fases 1 y 2 (2026-11-03)

**Dictamen: BLOQUEADAS. No certificadas; no habilita fase 3, fusión de #234 ni publicación.**

Se continuó la candidata de 46 pestañas; no se reconstruyó ni se modificaron maestras u otras empresas. Los resultados heredados son referencias, no objetivos. Este acta complementa los documentos anteriores y prevalece sobre cualquier afirmación de cierre no respaldada por ejecución.

## Identidad y fuentes de reglas

- Hoja: https://docs.google.com/spreadsheets/d/199x_GNl2608SFjj58hCtTjWpxleL2rqtRPJl4lZdW5I/edit
- Datos: PR #234, rama `amzn/20261102-r5-plantilla-ia-limpia`, cabeza inicial `8af7bd3ff590f7c32a19a8f3e8de9e6f41d58b0b`.
- Modelo-JMR main observado: `2061f65de8889020869608ea232bb228b0754d15`.
- JMR-valuation main observado: `836ae6827df152a79c699d1629af3470f9417734`. PR #202 efectivamente fusionado; sus dos jobs registran 4 + 28 pruebas aprobadas. Eso no certifica R5.
- Modelo-JMR-datos main observado: `b1fb039c70322bb12edd8590f25f822f70e7ca3c`.
- Se revisaron REGLAS_VIGENTES v27, documentación de cinco fases, contrato de insumos F1, entregas F1/F2 y `docs/prompts/valoracion-modelo-jmr-v5.md`. No se eliminó ningún criterio heredado.
- Última modificación inicial de la hoja: 2026-11-03T06:34:29.617Z. Las lecturas previas a cada escritura confirmaron las fórmulas objetivo; no se detectó una intervención concurrente en esas celdas. No se afirma una exclusión global de editores.

## Ejecución oficial, no simulada

El intento local del comando de entradas terminó en código 1 por `ModuleNotFoundError: gspread`; no había credenciales Google locales. Se resolvió ejecutando en GitHub Actions con la cuenta de servicio ya configurada en el motor, sin extraer secretos.

Primera ejecución: https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/41608140202
Commit `abd7140259b91b8dc312a8a18ed00302ec15f6be`; regresión 39/39 (32 previas + 7 nuevas).
Artefacto original: https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/41608140202/artifacts/13217871854
SHA256 ZIP: `2adfc7b73dfdb8130ffe80ccbf3bf6836d6543ae82875342c276c2dc4badf091`.
Se preservan en `evidencia_tecnica_20261103/official-first/` comandos, stdout, stderr, códigos de salida y JSON SEC/formularios. Los archivos versionados evitan depender de la retención temporal de Actions.

| Control | Código primera ejecución | Resultado y límite |
|---|---:|---|
| inputs_completos.py AMZN --sheet-id R5 | 0 | 0 entradas esenciales vacías, 0 excepciones. Respeta condiciones de opciones. |
| auditar_ceros_materiales.py | 0 | 0 alertas después de documentar D&A incluida en categorías operativas. No equivale a certificación SEC. |
| diff_formulas_plantilla.py | 0 | 5 fórmulas diferentes; ninguna fórmula sustituida por número/texto/vacío. El script permite diferencias fórmula→fórmula, por tanto no homologa automáticamente cambios ni detecta defectos compartidos con la plantilla. |
| candados.py | 1 | Importación innecesaria de model_steps arrastraba yfinance ausente; corregida después en rama de motor. |
| estados_completos.py | 1 | 11 filas con vacíos. Otras 11 hojas de referencia inaccesibles, excluidas por el propio script. |
| auditar_estados_sec.py | 0 | 20 diferencias informativas, 0 cambios propuestos. Código 0 no significa 0 discrepancias. |
| controles_todas.sh | No ejecutado | Sus controles consumen registros publicados/legados, no el expediente R5. Ejecutarlo sin adaptar sus entradas certificaría otra revisión. |

Todos los seis scripts ejecutados recibieron el ID explícito R5. SEC recibió además `--cutoff 2026-10-30 --fiscal-year-end-month 12`, para no interpretar los encabezados 2016–2025 como meses equivocados ni incorporar publicaciones posteriores.

## Cambios mínimos y antes/después

Motor PR https://github.com/JuanMaRobledo/JMR-valuation/pull/203 : `candidate_args.py`, `estados_completos.py`, `candados.py`, `auditar_estados_sec.py`, `audit_amzn_r5_readonly.py`, `tests/test_candidate_controls.py`, `.github/workflows/amzn-r5-readonly.yml`.

- Selección explícita de candidata sin cambiar catálogo ni identificación de maestras; rechaza varios tickers, ID vacío y URL en lugar de ID. Conserva apertura protegida.
- Período fiscal y fecha de corte explícitos para auditoría SEC; falla si no reconoce columnas.
- Runner de solo lectura guarda salidas reales aun si fallan otros controles.
- Commit posterior `75116d213712828fd9a2addc5bcf3490d993a345`: importa model_steps únicamente en la ruta heredada de candados, evitando exigir yfinance para leer una candidata. Añadida regresión. 40/40 pruebas aprobadas en job 125827377810.
- Reejecución: https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/41609454032 . Véase adenda final para el resultado de los controles vivos.

Hoja R5:

| Cambio | Antes | Después |
|---|---|---|
| Income Statement!I9:L9, notas solamente | Cuatro vacíos sin explicación | Notas SEC: D&A está incluida en gastos operativos y en CF, no es cero ni debe restarse otra vez. Valores y fórmulas intactos. Alertas materiales 4→0. |
| Input sheet!I26 | 15,250837 %, anualización LTM/FY | 15,350845 %, LTM septiembre / LTM septiembre anterior − 1 |
| Income Statement!L4 | 11,232850 %, LTM/FY | 15,350845 %, misma base comparable |

El denominador ya existía: `Entradas históricas auxiliares!J7 = 637959 + 503538 - 450167 = 691330`. Numerador 797455. Se conservaron supuestos proyectados y Sales-to-Capital 0,72. Las fórmulas originales y nuevas están en la evidencia; las lecturas posteriores confirmaron ambos resultados. No se rellenaron opciones inexistentes ni vacíos con ceros inventados.

## Integridad demostrada y límites

- Diez años 2016–2025 + LTM septiembre 2026 presentes. Conciliación aritmética: 88/88 identidades sin diferencia (EBIT, CFO, CFI, CFF, variación de caja con FX, activo=pasivo+patrimonio y componentes corrientes). Esto no verifica por sí solo todas las etiquetas SEC.
- Reproducción independiente de cuatro DCF desde proyecciones, descuentos, terminal y puente a capital: Base 149,19148575564947; Conservador 81,00951720766344; Optimista 241,84351613972044; Disrupción 62,43573154339526. Diferencia máxima 5,7e-14 USD/acción.
- WACC reproducido: 0,08179602956197793; MOS35% sobre Base: 96,97446574117216.
- Capitalización I+D reproducida: activo 78943,15; amortización 20597,6; ajuste EBIT 11136,9 (millones USD). La fracción económica de I+D sigue siendo un supuesto a auditar en F3.
- Tres matrices DCF 5×5: centro 149,19148575564947. Motor de sensibilidades adicional filas 401:3600 sin errores efectivos en la captura.
- Sensibilidades EV/EBITDA y P/OCF con centro igual a su valor presente; P/OCF observado 208,7479269 y múltiplo Base 19,614690702x. La entrega heredada cita 179,1477 y 16,833x: discrepancia documental pendiente, no sustituir el valor sin rastrear el origen.
- Escaneo de las 46 pestañas hasta fila 400 y cola del motor: tres errores #N/A en Synthetic rating!D14,D15,D17, rama sintética inactiva con selector vacío. El WACC activo usa rating real AA. No se llenó un selector condicional ficticio para ocultarlos. Falta guardia condicional homologada.
- Opciones propias desactivadas; descuento nativo de opciones 0 por condición, sin inventar sus inputs. RSU y activos no operativos siguen en sus puentes; su valoración económica no queda certificada por este acta.

## CAPEX preservado

Se revisó `NORMALIZACION_CAPEX_Y_JUSTIFICACION_DCF.md` y el puente en la hoja. USD millones: CFO168300; CAPEX bruto215192; ventas/incentivos4535; CAPEX neto210657; FCF−42357. La fórmula de reinversión DCF usa ventas incrementales/Sales-to-Capital, con desfase de dos años; no vuelve a deducir además el CAPEX de caja. Primer FCFF técnico −25555,405 y reinversión121711,569. No se forzó a positivo.

Las adiciones PPE no pagadas no fueron añadidas al CAPEX de caja. Los arrendamientos reconocidos permanecen dentro de la deuda contable; ajuste incremental cero evita sumarlos otra vez. El agregado no operativo288700 entra una vez en el puente de equity y está separado de reinversión operativa. La composición y valoración de Anthropic/OpenAI, deuda a mercado y ROIC requieren auditoría económica posterior; no se certifica su valor razonable aquí.

## Bloqueos técnicos pendientes, no trasladables como supuestos F3

1. **Estados completos:** 11 filas con vacíos: IS9 G:L; Balance8 G:L,12 G:L,14 G:I,23 G:L,28 G:L; CF29 G:L,30 G/I:L,31 G:L,32 L,38 G:L. Separar dato obligatorio, presentación agregada, ausencia documentada y derivado. El validador actual no interpreta las notas. No rebajar criterios ni poner cero para aprobar.
2. **SEC:** 11 impuestos son exactamente opuestos por convención signed_tax; no cambiar datos sin adaptar el cotejo. Ocho EPS2016–2019 son compatibles con split20:1 y redondeo pero falta homologar ese tratamiento. PPE compara LTM508862 con357025 de2025-12-31: dato SEC obsoleto para esa celda, no diferencia comparable. Exigir fecha coincidente y completar la etiqueta/fuente correcta.
3. **Fórmulas fiscales heredadas:** POCF!B8 y PFCFE!B8 restan el impuesto firmado positivo3217 de FY2022; EVFCFF!B8 usa 1−tax/EBT con convención incompatible. Income Statement!H29 usa ABS(tax)/EBT y da tasa negativa para beneficio fiscal. Requiere corregir el conjunto coherentemente, probar impuestos/gastos/beneficios y años con pérdida, homologar versión sin modificar maestras durante este encargo. Issue https://github.com/JuanMaRobledo/JMR-valuation/issues/204 . Crecimiento LTM de esa incidencia ya corregido.
4. **Errores inactivos sintéticos:** tres #N/A pendientes de guardia condicional con regresión, no de datos ficticios.
5. **Contrato/app y puerta completa:** #234 contiene documentos, sin registro R5 JSON de valoración/análisis/motor que permita reconciliar hoja↔motor↔app. `probabilidades.py` y `controles_supuestos.py` leen reference/damodaran; `consistencia_migracion.py` lee valoraciones publicadas; `integridad_hojas.py` usa hoja_vigente y registro_activo. Antes de ejecutar `controles_todas.sh`, estos consumidores necesitan identidad candidata y artefactos R5 trazables, sin sustituir catálogo ni usar R2. La consistencia incluso puede terminar en 0 con cero registros; eso no certifica nada. No se ejecutó contra datos antiguos.
6. **Documentación de múltiplos:** conciliar P/OCF y salvedades, manteniendo como no aplicables los múltiplos cuyo denominador económico no lo permite.

El acceso Google autenticado está disponible en Actions; los bloqueos restantes no deben atribuirse genéricamente a falta de credenciales. Para terminar faltan correcciones/homologación del validador y fórmulas, completar evidencia por fila, y artefactos candidatos que permitan la puerta integrada. No se declara cerrada #200.

## Asuntos económicos reservados a fase 3, una vez cerrado lo técnico

- CAPEX AWS/IA, vida útil, crecimiento y desfase de inversión; Sales-to-Capital0,72, ROIC y reinversión terminal.
- WACC multinegocio, beta, deuda a mercado y estructura objetivo (#197).
- Fracción capitalizable y amortización de I+D, sostenibilidad de márgenes.
- Activos no operativos/Anthropic/OpenAI, RSU, arrendamientos y riesgo de doble conteo económico.
- Comparables y aplicabilidad de EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF; pérdidas y flujo negativo no se convierten artificialmente en múltiplos válidos.
- Probabilidades, escenarios y sensibilidad económica. No se avanzó a esa fase.

## Adenda final: repetición terminada y verificada

Run41609454032, commit75116d213712828fd9a2addc5bcf3490d993a345: regresión **40/40 aprobada**. Job autenticado125827493733 terminó con fallo real por estados incompletos, no por credenciales ni importaciones.

| Control repetido | Código | Resultado |
|---|---:|---|
| inputs_completos | 0 | 0 faltantes, 0 excepciones |
| auditar_ceros_materiales | 0 | 0 alertas |
| diff_formulas_plantilla | 0 | 7 diferencias fórmula→fórmula: las 5 anteriores + I26 y L4 corregidas; ningún reemplazo por constantes/vacíos |
| candados | 0 | **15/15 listos**, fallo de importación resuelto y comprobado en vivo |
| estados_completos | 1 | Persisten 11 filas con vacíos |
| auditar_estados_sec | 0 | Persisten 20 diferencias informativas, 0 cambios propuestos |
| controles_todas.sh | No ejecutado | Identidad/artefactos candidatos pendientes en consumidores integrados |

Salidas definitivas en `evidencia_tecnica_20261103/official-final/` y artefacto13218756096 del run. El acceso autenticado queda demostrado. PR203 permanece en borrador sin integración: la puerta total sigue roja y no se elude la regla de no fusionar con fallos. Issue200 permanece abierta con alcance pendiente; issue204 separa crecimiento corregido de defectos fiscales aún abiertos. PR234 sigue borrador, sin merge ni publicación.

La relectura posterior a los cambios confirma los cuatro DCF originales, crecimiento15,350845 % y ausencia de cambios en previsiones. Reconsulta final de las tres ramas main: mismos commits que al inicio. Se verificó que los scripts de reproducción funcionan con las capturas reducidas versionadas; son evidencia aritmética, no una nueva lectura ni sustitución de controles oficiales. Las capturas de reproducción preceden a las dos correcciones de crecimiento; `growth_before.json` y `final_cells.json` preservan la transición.


## Reevaluación autenticada de R5 posterior a correcciones (3-nov-2026; intento 2)

**Evidencia de ejecución:** [Actions #41609454032](https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/41609454032), intento reejecutado bajo motor PR #203, código del runner en commit `75116d213712828fd9a2addc5bcf3490d993a345`. [Artefacto de esta repetición](https://github.com/JuanMaRobledo/JMR-valuation/actions/runs/41609454032/artifacts/13230356575); SHA256 ZIP registrado por Actions: `c10d5929c8fe2ada1ff8514c7fa1891dbb86fae3a66fa7d89060c3c2e5ddde28`.

| Comprobación | Resultado real |
|---|---|
| Regresión de software | **ÉXITO** en el job de regresión |
| `inputs_completos` | **0 faltantes, código 0** |
| `auditar_ceros_materiales` | **0 alertas, código 0** |
| `diff_formulas_plantilla` | **código 0**; ninguna fórmula reemplazada por número ni vacío. Se observaron **14 diferencias fórmula→fórmula** (EVFCFF 1, POCF 1, PFCFE 1, Input 5, Valuation output 1, Income Statement 2, Synthetic rating 3); el control no homologa semánticamente todas las fórmulas diferentes. |
| `candados` | **15/15, código 0** |
| `estados_completos` | **11 filas señaladas, código 1**, incluidas partidas sin desglose y CF38; deben clasificarse, no llenarse con ceros ficticios. |
| `auditar_estados_sec` | **20 diferencias informativas, código 0**, cero cambios propuestos: impuesto (11 períodos), EPS básica y diluida (8 casos 2016–2019), PPE LTM (1 período). Un exit code 0 no concilia esas diferencias. |
| `controles_todas.sh` | **NO ejecutado** contra candidata R5: sigue usando otros registros/hojas. |

**Lectura directa posterior sobre la hoja R5:** fórmulas actuales de `POCF!B8`, `PFCFE!B8`, `EVFCFF!B8`, `Income Statement!H29` y `Synthetic rating!D14,D15,D17` observadas. Las tres celdas de rating sintético inactivo se evalúan en blanco sin `#N/A`. DCF por acción, sin cambios respecto a evidencia previa: Base **149.19148575564947**, Conservador **81.00951720766344**, Optimista **241.84351613972044**, Disrupción **62.43573154339526** USD. Costo capital activo **0.08179602956197793**.

**Decisión verificada:** el reintento autenticado **FALLÓ** por `estados_completos` y no equivale a certificación. Las correcciones fiscales y las protecciones de rating ya son visibles en R5, pero no se debe afirmar cierre F1/F2 ni puerta integral. Mantener PR #234 y PR motor #203 en borrador, sin merge/publicación. Próxima intervención: clasificar los once renglones por fuente y dependencia, resolver convenciones SEC, construir ruta candidata de validación integral; preservar las salidas no afectadas.
