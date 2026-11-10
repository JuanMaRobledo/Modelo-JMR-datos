# UBER-REBOOT-3T26-R1 · R4 — Múltiplos, resumen y conciliación

**Fecha:** 2026-11-10. **Ejecución:** GPT-6 (ChatGPT) con Google Drive/Sheets, GitHub y cotejos directos SEC. **Estado de la revisión:** **CANDIDATO** (R5 no publicado, R6 auditoría independiente NO_EJECUTADA). **R4 operativo conciliado, con excepción explícita EV/FCFF N/D y salvedades de auditoría**.

## Identidad / archivos inalterados
Revisión: `UBER-REBOOT-3T26-R1`; `perfil_valoracion=Reboot`, contrato `jmr-reboot-3libros-v1`; corte contable 2026-09-30; precio de referencia fijado en DCF 68,59 USD al 2026-11-06. El usuario aprobó **beta 1,20**. No se crearon libros adicionales ni se usó el archivo del Floyd anterior como fuente.

- **Históricos H**: https://docs.google.com/spreadsheets/d/176tcVAz_RzHluf4kyjEEsMjDcDosldPdB5FBifO9YQA/edit
- **DCF Base D-B**: https://docs.google.com/spreadsheets/d/14QlydMFli2pxdG4agUYOAXL8QIE99P-3UDE7vwK8CaM/edit
- **DCF Conservadora D-C**: https://docs.google.com/spreadsheets/d/1TUDP8WvRpjtm5AbCpGkKkfyAlItRuufIAAEkFp95aHA/edit
- **DCF Optimista D-O**: https://docs.google.com/spreadsheets/d/1f7Fzs7TBezRNa4E0lwHoh8fcPXTGn0d09HTatCaDLRU/edit
- **Múltiplos M**: https://docs.google.com/spreadsheets/d/19fe8FcQ32d3yf169i-XA7F-c4IGhWTCNl_QO4WgCwA4/edit
- **Análisis A**: no creado; corresponde a R5.

## Cargas reales y reconstrucción
1. **H→M:** 718 entradas históricas de resultados, balance y flujos de efectivo, vinculando por etiquetas y años; preservando todas las fórmulas existentes del destino. Hojas M `Income Statement`, `Balance Sheet`, `Cash Flow Statement`. No se utilizó `IMPORTRANGE`. FY2016/FY2017 con limitaciones de cobertura histórica pre-IPO.
2. **D-C/D-B/D-O→M:** 24 números, ocho por escenario, en `M!Entradas desde DCF!B5:D12`: DCF por acción, Ke, costo deuda, WACC inicial, WACC estable, EBIT ajustado, beta, ERP. `B15` cuenta 24. Históricos y supuestos conectados a la revisión y beta aprobada (1,20).
3. **M preparación:** `Supuestos y control!B22=UBER`; FY último 2025; Rf 4,86%, tasa marginal 25%, deuda preimpuesto 6,10%, ROIC terminal Base 13,23%, ventas/capital Base 2,8 años1–5 y 2,5 años6–10 (éste último **proxy de convergencia, no dato industrial auditado**), no operativos 11.473 USDm y duración deuda aprox. 7,5 años. `B30:D39` reproduce crecimiento, márgenes, ventas/capital y ROIC de los tres DCF. `B60=LISTA PARA CALCULAR`.
4. **Reclasificaciones SEC:** intereses gastos en signo negativo para M (`Income Statement!J14:L14`); pérdidas por método de participación derivadas de EBT, impuesto y NI (J/K/L = −38/−53/−97). El libro M no tenía columna específica de cambios de gastos acumulados; se trasladó `H!Cash Flow Statement!B9:L9` a `M!Cash Flow Statement!B12:L12`. Inventarios no divulgados como renglón separado en los estados SEC se modelan como cero identificado, nunca como efectivo. Las fuentes y fechas se cargaron en J:L de las hojas financieras de M.
5. **Balance 2023–2026:** se separaron en M por fuente SEC deuda corriente (2023=25; 2024=1.150, ya incluidas en pasivos corrientes), gastos acumulados netos de esa porción, reservas de seguros y arrendamientos corrientes, sin doble contabilización. Resultado: controles de corriente/total en FY2023, FY2025 y LTM OK; FY2024 mantiene observación documental de detalle. Minoritarios siguen con salvedad de clasificación. Fuentes:
  - 2024 10-K, FY2023/24: https://www.sec.gov/Archives/edgar/data/1543151/000154315125000008/uber-20241231.htm
  - 2025 10-K, FY2025: https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm
  - 2025 10-Q, Sep2025: https://www.sec.gov/Archives/edgar/data/1543151/000154315125000033/uber-20250930.htm
  - 2026 10-Q, Sep2026: https://www.sec.gov/Archives/edgar/data/1543151/000154315126000041/uber-20260930.htm
6. **LTM comparable exacto:** FY2024 43.978 + 9M2025 37.651 − 9M2024 32.019 = **49.610 USDm** al Sep2025; LTM Sep2026 56.526 USDm, crecimiento comparable **13,94073775%**. `M!Supuestos y control!B65=49610`. NWC comparable Sep2025 **−5.918 USDm** (CA15.139−caja/inv9.086−CL13.121+deuda corriente1.150); NWC LTM Sep2026 **−6.705**, delta −787, registrado y con URL en `Puente EEFF`. Mediana ΔNWC/Δventas FY2024/25 en las fórmulas de M ≈−16,95%.
7. **Flujo de caja ajustado (supuesto, NO GAAP auditado):** en `Supuestos y control!B97:D97` se modeló ajuste residual CFO/ventas tomando como ancla mínima la compensación en acciones LTM 2.065 / ingresos LTM 56.526 = **3,6532% Base**, 1,8266% Conservadora y 5,4798% Optimista. Es un supuesto de flujos que **no equivale a todo el CFO residual ni elimina el costo económico SBC**; requiere examinar dilución, créditos fiscales y partidas de seguros en R5/R6. Se rechazó extrapolar sin control el CFO residual histórico 2024–2025, afectado por beneficios fiscales extraordinarios.
8. **Selección sectorial:** `M!Resumen de Valoración!G3=Crecimiento`. Los pesos por compañía dentro de la columna Crecimiento quedaron: **75% DCF, 10% EV/EBITDA, 0% EV/FCFF, 4% P/E, 7% P/FCFE, 4% P/OCF** (100% total). El EV/FCFF quedó **N/D documentado**, no 0 USD: 2024–2025 tienen beneficios fiscales extraordinarios, FCFF histórico sin denominador sostenible y sin ancla de salida verificada. No se le inventó múltiplo ni precio. Se preserva método en hoja para revisión posterior.

## Resultados por método (valor presente USD/acción)
| Método / peso total | Conservadora | Base | Optimista |
|---|---:|---:|---:|
| DCF Damodaran · 75% | 45,2912 | **98,7383** | 149,6689 |
| EV/EBITDA · 10% | 62,0827 | 79,1661 | 92,4289 |
| EV/FCFF · 0% | **N/D** | **N/D** | **N/D** |
| P/E · 4% | 126,3622 | 164,9932 | 195,3541 |
| P/FCFE · 7% | 25,7654 | 39,2510 | 52,0602 |
| P/OCF · 4% | 56,0716 | 78,1489 | 96,6142 |
| **Múltiplos consolidados, valor hoy (25% global)** | **61,2368** | **81,5595** | **98,2633** |
| **Combinado DCF+múltiplos (secundario)** | **49,2776** | **94,4436** | **136,8175** |

El DCF Base **98,7383** manda como valor intrínseco principal. Su MOS 35% = **64,1799 USD**, no `0,65 × combinado`. El promedio de tres DCF = **98,1091 USD**. Los múltiplos secundarios se ponderan y descuentan a hoy; no deben confundirse con el resultado primario.

## Conciliación de presentación
- Se copió M→DCF Base `Resumen de valoraciones`: probabilidades 25/50/25, tres DCF, WACC común, Ke común, cuatro precios por múltiplo, N/D EV/FCFF con peso 0, pesos relativos de múltiplos, combinados y valores de M. Se mejoraron **solo las fórmulas de la hoja de resumen añadida**, para no calcular falsos combinados cuando falte un múltiplo positivo; **no se editaron fórmulas de las 17 hojas del motor Damodaran**.
- Los seis controles `Resumen de valoraciones!B36:B41` quedaron **OK**; `B43=CONCILIADO` (conciliación matemática entre libros). `M!Resumen de Valoración!C65:E65` muestra cobertura de múltiplos 100% entre cuatro métodos ponderados y `APTO · AUDITAR`, que **no equivale** a auditado.
- **Precio de referencia no homogéneo:** DCF precio fechado 68,59 (6-nov), M tiene precio dinámico GOOGLEFINANCE (71,17 durante la comprobación 10-nov); el primero es el ancla oficial del expediente y el segundo solo pantalla dinámica. Dejar explícita la distinción en el análisis; no sustituir el precio histórico del DCF por la cotización móvil sin recalcular el corte.

## Estado de compuertas
| Componente R4 | Estado |
|---|---|
| H→M, DCF→M, control de preparación de M | **APROBADO técnicamente**, celdas vivas |
| DCF Base/Cons/Opt, MOS y combinados | **APROBADO matemáticamente** |
| Cuatro múltiplos activos (EV/EBITDA, P/E, P/FCFE, P/OCF) | **CALCULADOS**; controles de sensibilidad central de cada uno deben confirmarse en R5 |
| EV/FCFF | **N/D**, peso 0 con razón económica/denominador; no se crea cifra |
| 6 comprobaciones de resumen DCF Base | **APROBADO / CONCILIADO** |
| Cotejo completo documentación SEC 10-K y 10-Q contra todas las filas y excepciones | **PARCIAL** (etiquetas de verificación siguen PENDIENTE) |
| Huella SHA-256 reproducible de cada transferencia y conservación completa de comentarios | **NO_EJECUTADO**, pendiente técnico |
| `M!Supuestos y control!B63` | **PENDIENTE**: no marcar AUDITADO sin prueba integral |
| `M!Supuestos y control!B64` | **NO PUBLICAR** hasta controles R5 |
| Integración JSON/catálogo/app en nueva arquitectura y análisis A | **NO_EJECUTADO** (R5) |
| R6 auditoría independiente | **NO_EJECUTADO** |

**PASOS R4: 7/8 funcionales; la certificación completa de fuentes/huellas queda PARCIAL.** La presente entrega cierra la **construcción y conciliación operativa** de R4, no autoriza publicar ni declara auditoría aprobada.

## Siguiente paso exacto
1. En R5: cotejar fuentes y clasificaciones del M, NAV minoritarios, deuda y caja restringida; revisar materialidad de ratio residual CFO=proxy SBC, tasas fiscales, dilución, NWC y múltiplos; confirmar las 4 matrices de sensibilidad 5×5 y revisar EV/FCFF N/D (si se normaliza con una serie verificable, reabrir sus supuestos/peso).
2. Generar el sexto archivo `04 ANÁLISIS` Nivel1 (14 capítulos) + Nivel2 (12 apartados) específico de esta revisión, con precio **68,59 fechado** y las cifras de los cinco libros.
3. Generar JSON par de esta misma revisión, ejecutar validadores y prueba app integrando PR #193 (app), #215 (motor), #263 (datos) **sin fusionar antes de CI y contrato Reboot aprobados**. Solo entonces `EN_REVISION`. R6 por otro agente.
