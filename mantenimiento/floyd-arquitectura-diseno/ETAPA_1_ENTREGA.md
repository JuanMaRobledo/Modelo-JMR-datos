# Etapa 1 · Auditoría funcional (diagnóstico, sin cambios) — ENTREGA

**Estado: PARCIAL** · 2026-11-11 · solo lectura (Sheets API, GitHub Actions, repos). No se escribió en ningún libro.
Alcance real: las 3 plantillas de libros R1–R6 (solo hojas y tamaños), los 6 artefactos de `UBER-REBOOT-3T26-R1` (hojas; contenido de `Presentación`, `Resumen de valoraciones`, `Sensibilidades DCF`, M `Resumen de Valoración`, `Guía y empresa` y muestras de fórmulas de H). **No** se auditaron las 1 297 fórmulas del motor (verificación previa citada en el contrato, no repetida), ni el Doc A ni la app desplegada.

## Mapa de dependencias (comprobado)
| Flujo | Mecanismo real | ¿Fórmula viva? |
|---|---|---|
| H (estados) → H (ratios: Márgenes, Salud Financiera…) | Fórmulas internas (`IF(ISNUMBER…)`) sobre `Income Statement`, etc. | **Sí** |
| H → D‑B/D‑C/D‑O (`Input sheet`) | Carga por script ad hoc (`R2_evidencia/hlib.py`, `payload.py`, `mapping.py`) | No (valor pegado por agente) |
| H → M (`Financials Multiples`) | `R4_evidencia/M_UBER_payload.json` | No |
| D‑B → M (`Entradas desde DCF`) | Carga con huella de los valores transferidos | No |
| D‑C, D‑O, M → D‑B `Resumen de valoraciones` | Celdas amarillas cargadas + SHA‑256 | No |
| `Resumen` → `Presentación` | Fórmulas (`='Resumen de valoraciones'!…`) | **Sí** (0 entradas) |
| Corridas del motor → `Sensibilidades DCF` | Valores estáticos (declarado en la hoja) | No; se detecta rancio con «Centro − DCF Base vivo» (=0,0017) |

## Hallazgos (ordenados por severidad)
1. **ALTO · La sincronización no es un componente del repositorio.** El contrato la describe como «scripts de sincronización ya definidos con huella», pero en los tres repos solo existen scripts por revisión dentro de `candidatos/…/R2–R5_evidencia` (~700 líneas Python, sin escritor idempotente a Sheets, sin registro de origen/destino, sin reintentos). La escritura a Sheets se hizo desde la sesión del agente. Consecuencia: «automatización» actual = procedimiento del agente, no mecanismo reproducible. → Etapa 4.
2. **ALTO · La huella SHA‑256 no detecta obsolescencia del libro.** Según `FASE_4_ENTREGA.md` es el hash del **JSON de los valores transferidos**, no del contenido del libro origen; `Fecha de carga` solo tiene resolución de día. Si alguien edita D‑C después de la carga, el Resumen no lo señala. Sí existe un control de rancidez parcial en `Sensibilidades DCF`.
3. **MEDIO · `Sensibilidades DCF` es una 3.ª hoja añadida a D‑B** (20 hojas; plantilla 02b = 19). Las 17 hojas del motor están intactas (nombres verificados en D‑B, D‑C y D‑O), pero el contrato dice que D‑B suma solo dos. Debe codificarse en el contrato o moverse (opción Etapa 2).
4. **MEDIO · Texto estático contradictorio en `Presentación!A29`:** «Múltiplos secundarios con EV/FCFF N/D justificado», mientras la tabla muestra EV/FCFF con peso 24 % y valores 26,72/47,44/72,46 (y `FASE_4` indica que EV/FCFF se calcula). Es la única narrativa no derivada de fórmula y quedó desactualizada tras el rehacer R4.
5. **MEDIO · Etiqueta de origen inconsistente en `Resumen de valoraciones`:** «Combinado según M = Fila 12», pero en M la fila 12 muestra 44,03/91,63/138,48 (incluye DCF 75 %), mientras el Resumen muestra 40,24/70,31/104,90 (solo múltiplos). El valor conciliado es el correcto según `FASE_4`; la referencia de celda escrita es la errónea.
6. **MEDIO · Controles sin explicación:** «Diferencia múltiplos Base frente al DCF Base −28,8 % — Explicar si es material» queda como instrucción, no como texto; M declara «Ancla histórica: PENDIENTE» y no descuenta opciones (≈0,09 US$/acción).
7. **BAJO · `Presentación` incompleta frente al diseño objetivo:** sin matriz 5×5, drivers (WACC terminal, g, ROIC, % valor terminal, S/C), fecha de mercado/revisión/estado, procedencia (SHA, fecha de sincronización, enlaces) ni disponibilidad de sensibilidades por múltiplo. Las matrices A (CAGR×margen), B (WACC×g, 5×5) y C (ROIC×g) existen solo en `Sensibilidades DCF`; la app muestra 4 matrices de múltiplos.
8. **BAJO · Rótulos de contrato desfasados:** H dice «MODELO JMR REBOOT», `Guía y empresa` cita sincronización con huella «o escritura directa». H declara FY2016 sin dato XBRL → **9 FY + LTM, no 10** (ausencia documentada, aceptable).
9. **BAJO · Discrepancia documental:** `REGLAS_VIGENTES.md` encabezado v37 vs. tabla de cambios con fila v38 (10‑nov); el contrato dice «v1.0 9‑nov» con tabla de plantillas posterior.

## Verificado sin defecto
- Presentación = 100 % fórmulas (no hay números pegados); precio 68,59, DCF Base 98,74, MOS 64,18 (=0,65×98,7383), esperado 98,11 coinciden con `valoraciones/UBER-REBOOT-3T26-R1.json` (valorPrincipal 98,7383; precioMOS 64,1799; precio 68,59).
- Controles de conciliación del Resumen: 6/6 OK; Conservadora ≤ Base ≤ Optimista (45,29 ≤ 98,74 ≤ 149,67); probabilidades 25/50/25; Ke M = Ke Base (10,49 %).
- Matriz B: centro = 98,74 y eje 5×5; control «Centro − DCF Base vivo» ≈ 0,0017 (redondeo).
- 17 hojas Damodaran presentes en D‑B/D‑C/D‑O.
- CI en `Modelo-JMR` `main` (commit `676dced`, 2026‑11‑10): suites `suite-completa`, `prompts-triad`, `separacion-editorial-calculadora`, `nav-multiplos`, `expediente`, `vista-hojas` y `pages build` en **success**. Un run fallido (`suite-completa` #65) corresponde a un commit de PR ya reemplazado por el #66 en verde. **CI verde ≠ lectura autenticada de las hojas.**

## No ejecutado / no verificable aquí
- Lectura autenticada de la app desplegada y comparación JSON↔catálogo↔app (NO_EJECUTADO; requiere sesión/Vercel).
- Recalcular huellas de D‑C, D‑O y M (el algoritmo exacto no está en el repo).
- Re‑verificación fórmula a fórmula del motor y de M (`FASE_4` la declara «no re‑verificada»).
- CI de `Modelo-JMR-datos` y `JMR-valuation` (no consultado en esta pasada).

## Riesgo
Alto para afirmar «propagación automática»; bajo para las cifras publicadas (conciliadas contra JSON). Ningún hallazgo exige cambiar valoraciones.

## Siguiente paso
Etapa 2: matriz A/B/C con prueba empírica de coexistencia de tres DCF en un libro (en copia aislada).
