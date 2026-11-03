# AMZN · AMZN-20261102-A12-R4 · Fase 2 · BLOQUEADA

**Entrega parcial; la valoración integral NO está terminada.** Fecha de trabajo: 2-nov-2026, America/Bogota. Herramienta: ChatGPT Work/Codex, conectores Google Sheets/GitHub, Python. Variante de modelo y esfuerzo no verificables desde el ejecutor. Método A / A-1.2. Estado CANDIDATO, NO PUBLICADO, NO APTO para fase 3.

Hoja: https://docs.google.com/spreadsheets/d/10qfoGrEP1PgdlLWrHvfoHqExKDZbPK75yb_oINlO4a8/edit

PR de continuidad, abierto en borrador: https://github.com/JuanMaRobledo/Modelo-JMR-datos/pull/233

## Hecho y verificado

Se recuperó FASE_1_ENTREGA.md de la rama `amzn/20261102-r4-desde-cero-aislado`. Se leyeron las reglas centrales v23, proceso, fase 2, README de fases, prompt de valoración y Método A-1.2. **AISLAMIENTO=OK:** no se leyó ni reutilizó contenido de R2/R3. Los nombres de esas revisiones aparecieron únicamente en inventarios generales del repositorio.

Se hicieron **18 escrituras de entrada/etiqueta**, con notas, sobre la misma R4:

| Cambio confirmado | Resultado |
|---|---|
| Input sheet!A1 | AMZN; estaba vacío e inhibía fórmulas |
| Balance Sheet!K19:K20, K25, K27 y L equivalentes | Reclasificación de financiación de instalaciones y crédito de corto plazo desde otros pasivos |
| Input sheet!C16 y B16, por fórmulas originales | Deuda reconocida FY2025 178.547; sep2026 304.841 USD millones |
| Balance Sheet!K14:K15 y L14:L15 | Inversiones identificadas separadas de otros activos; 65.359 y 294.595 USD millones, respectivamente; cifras con redondeo de fuente |
| Input sheet!B35 y Country equity risk premiums!B2 | Rf 5,29% y ERP 4,20%, mismo corte mensual 01-oct-2026; no se presentan como tasas spot 30-oct |
| Income Statement!K2/L2 | Etiquetas Dec '25 / LTM Sep '26; Input sheet!D12 calcula 0,75 |

Las reclasificaciones de inversiones son **contables**, no aprobación de su valor económico. Las filas de valor económico, impuestos normalizados y ajustes permanecen pendientes. La cotización conserva el corte 30-oct-2026.

## Controles de cierre y evidencia reproducible

`python verificar_r4.py` lee las capturas adjuntas y reproduce los resultados; no escribe en Google Sheets ni usa red.

| Control | Resultado real |
|---|---|
| Comparación de toda la grilla declarada de las 46 pestañas contra Maestra | 20.741 fórmulas idénticas; 0 sustituidas, borradas o cambiadas; 15 nuevas, exactamente las LTM declaradas en F1 |
| Validaciones de datos presentes en Maestra | 0 diferencias |
| Nombres, orden y dimensiones de pestañas | Iguales, 46/46 |
| Activos, pasivos corrientes, pasivos totales y balance FY2025/sep2026 después de reclasificar | Ocho residuos = 0 USD millones |
| diff_formulas_plantilla.py con adaptador de captura | Salida 0; código oficial sin editar, Maestra explícita; su alcance propio limita la lectura a primeras 400 filas. La comparación adicional anterior cubre toda la grilla, incluido motor DCF |
| candados.py con adaptador de captura | **1/15 listos**, salida 1. Catorce pendientes o REVISAR detallados en CONTROLES_R4.json |
| Función oficial inputs_completos.vacias con adaptador | **IndexError** al leer Cost of capital worksheet!B41 vacío; no se rellenó con un cero inventado ni se alteró el script |
| Scripts oficiales contra hoja viva | NO EJECUTADOS: no hay gspread ni variables de cuenta de servicio en este ejecutor. El conector sí permitió leer/escribir y capturar. Las pruebas sobre captura no se rotulan CI ni ejecución autenticada |
| Cuatro salidas DCF | Vacías en B35/B86/B137/B190 de Valuation output |
| Recálculo independiente y centros de matrices | No acreditados: falta un Base nativo y cuatro historias calculadas |
| Auditoría SEC exhaustiva, ceros, 8-K, integridad_hojas, controles_supuestos y múltiplos por ciclo | No completados en esta entrega; no se declara equivalencia integral |
| Auditoría visual nativa | No realizada; formato y geometría no se modificaron |

Las capturas incluyen valores efectivos, fórmulas y validaciones, **no imágenes**. SHA-256 R4: `5b13f70904febd0feeb99d91f85b6781ffea4a8ab0fcb6d8a67cedf3c995d25b`. SHA-256 Maestra: `268205869c81da6a94e26f310ca65c971e61a69f253b3dabc983025bf9e88f6d`.

## Decisiones y juicios

1. Separar el cierre de clasificación contable del juicio de valoración. No convertir todo Other assets en caja ni sumar plusvalías contables al FCFF.
2. Usar la pareja mensual Damodaran documentada, manteniendo aparte el precio de mercado. Debe sensibilizarse el desfase temporal; no combinar ERP mensual con Treasury spot como observaciones simultáneas.
3. No usar utilidad GAAP LTM como utilidad recurrente para P/E. No sustituir FCFF con CFO menos capex sin reconciliar impuestos, intereses y reinversión.
4. No capitalizar toda Technology and infrastructure como I+D: contiene costos operativos y depreciación. Falta una separación/proxy defendible, historial homogéneo y sensibilidad de vida útil, con conciliación de EBIT/capital/reinversión.
5. La prueba de deuda es un **diagnóstico**, no un WACC alternativo certificado. `DIAGNOSTICO_DEUDA.json` reproduce C54 usando intereses LTM, muestra supuestos de estrés explícitos y compara con referencias reveladas. No se debe emplear una madurez artificial para forzar coincidencia con valor de mercado.

## Pendiente o bloqueado

**No es solo un gate administrativo.** Falta completar entradas materiales y demostrar su compatibilidad con las fórmulas: I+D, arrendamientos, valor económico no operativo y fiscalidad asociada, RSU/SBC, NOL, deuda a mercado, beta/ERP geográfico, reinversión y terminal. La estimación de deuda de C54 necesita conciliar intereses LTM frente a emisiones del año y separar deuda/leases; la fuente ofrece datos de mercado que no deben ignorarse. No se ha demostrado todavía si basta una entrada permitida o requiere una modificación separada del motor.

El registro JSON candidato contiene valores nulos, conserva estado CANDIDATO y declara `apto_fase_3=false`. Su nombre contractual `VALORACION_A12_EN_REVISION.json` **no significa EN_REVISION**. Los cinco múltiplos quedan N/D/PENDIENTE_ANCLA, peso cero; esto no demuestra inaplicabilidad económica.

**PASOS: 0/7 pasos principales de fase 2 completados íntegramente** (1, 1b, 2, 3, 3b, 4, 5). Se completaron recuperación, 18 correcciones y controles específicos; el paso 5 solo está parcialmente cubierto por captura/JSON de estado, no por una valoración calculada. No se usa la falta de credenciales para justificar los juicios económicos aún pendientes. Por ello la fase queda BLOQUEADA/incompleta, no CERRADA CON CONTROLES PENDIENTES.

## Para continuar la misma fase 2

1. Leer esta entrega, CONTROLES_R4.json y las capturas; no volver a reconstruir F1 ni reutilizar R2/R3.
2. Completar normalizaciones materiales y reconciliación de deuda a mercado; documentar cualquier excepción de fórmula antes de aplicarla, conservando originales. Resolver también el fallo del lector de entradas con prueba que respete vacíos reales.
3. Preparar fichas A-1.2 por variable con historia homogénea, pares/cohorte, mecanismos, argumentos contrarios y materialidad. No hay aún tabla completa aprobada.
4. Cargar cuatro historias y previas justificadas; calcular DCF nativo, cinco múltiplos aplicables y anclas independientes, matrices Base y DCF inverso.
5. Recálculo de cada historia desde entradas leídas; diferencia <1e-6/acción. Repetir captura con hash y los controles financieros. No pasar a fase 3 ni publicar hasta cerrar dependencias.

## Fuentes y trazabilidad

- SEC Amazon 10-Q sep2026, notas 2–6: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm . Consultado 2-nov-2026; base de las reclasificaciones. Sus notas describen inversiones, financiación, valores de mercado y remuneración en acciones. Cifras redondeadas preservadas como tales.
- Damodaran, actualización 01-oct-2026, variante adjusted payout: https://pages.stern.nyu.edu/adamodar/New_Home_Page/home.htm . Rf 5,29%, ERP 4,20%; la variante cash yield 3,70% es distinta.
- Resultados/guía publicados 29-oct-2026: https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/ . Insumo de investigación, no una proyección incorporada al DCF.
- Reglas y scripts originales: copias adjuntas y SHA de scripts en CONTROLES_R4.json; consulta del motor main `ada1613af5252f3bf0d510d013729fa0f66d1fe8`.

No hubo merge, cambio de catálogo, publicación ni auditoría económica independiente.
