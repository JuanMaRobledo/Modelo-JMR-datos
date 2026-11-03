# PAGS · PAGS-20261030-A12-R1 · FASE_4 · BLOQUEADA

Fecha: 3-nov-2026 · Método JMR A-1.2 · corte 30-oct-2026 · hoja 17J1q1niSBxe5vwoCOaaRJvKZiZYi8feYLdMODnYXVTI.
Ejecutor: ChatGPT/Codex Work; identificador exacto de modelo y esfuerzo no expuestos. PR #226.
AISLAMIENTO=OK: únicamente candidato PAGS; ninguna valoración activa ni catálogo modificados.
PASOS: 6/6 evaluados; 3/6 ejecutados parcialmente (recuperación, N1, N2), control técnico parcial, promoción NO EJECUTADA por bloqueo demostrado, entrega ejecutada. No se declara fase cerrada.

## Cambios y pruebas
- Datos 6M de SEC detallado sustituyen redondeos en FCFE financiero PAGS!B107:G108. Componentes LTM C109:E109 por fórmula; B109 y F109 preservan fórmula nativa.
- LTM ingresos R$20.588,036m; utilidad R$2.151,112m; P/E observado 5,592869955632249.
- Panel de evidencia y diagnóstico M100:P131. Suma de los cuatro componentes RWA: diferencia cero; ratio PR/RWA 15,04153069%.
- Acciones en circulación 30-jun: 290.677.709 − 15.031.687 = 275.646.022; promedio diluido Q2 279.460.742, conceptos distintos.
- Datos BCB obtenidos por API primaria, guardados íntegros en evidencia/BCB_CAPITAL_202606.json, SHA256 d6ec8d82befcf9679f7e6779201d1ba6d4ab5ff95421ba65e72d280297264fec. La versión consultada es de 3-nov; confirmar que la versión histórica estaba disponible al corte.
- 6 pruebas locales APROBADAS: cuatro historias, MOS/pesos, 75 celdas de sensibilidad, estructura editorial y no promoción con faltantes.
- Validador bancario oficial de main, validateBankNativeMatrices(candidato): FALLA «PAGS: contrato bancario requerido», esperado bank-relative-ke-v1.
- Controles globales controles_todas.sh, candados, cotejo completo SEC/NIIF/ceros, diff de 46 hojas y preview app: NO EJECUTADOS; no hay contrato/promoción candidata compatible para acreditar flujo completo. No se infiere aprobación de los CI generales.
- Registro de revisiones: no se reconstruye a partir de este checkout parcial para evitar borrar entradas de otros emisores. Drivers/revisión/hoja/catálogo no cambian; CI del registro verifica el resultado de rama.
- Verificación visual limitada a valores, formatos y fórmulas por API; no auditoría visual autenticada completa.

## Drivers Base: anterior → nuevo
| Driver | Anterior | Nuevo | Decisión |
|---|---|---|---|
| ROE años 1–5 | 14,5/14,8/15,1/15,3/15,5% | Igual | Provisional; no recalibrado sin capital |
| Crecimiento patrimonial 1–5 | 6,5/7/7,2/7,5/7,5% | Igual | Proxy, no presupuesto RWA |
| Margen EBIT / S/C | No aplicable al FCFE consolidado | Igual | No inventar motor industrial |
| Ke BRL candidato | 12,46923949% | Igual en cálculo provisional | Desfase de fuentes demostrado; no publicable |
| Ke diagnóstico mismo corte | No disponible | 12,82505572% | Solo aisla Rf; no valor definitivo |
| g BRL / ROE terminal | 5,8% / 13,9% | Igual | Revisar junto a beta terminal 1 |
| Base / MOS | 12,88000621 / 8,37200404 USD | Igual provisional | No publicar |

## Materialidad
Corregir únicamente Rf desde 4,94% al 5,29% compatible con ERP 3,70%, manteniendo beta/CRP/inflación y flujos, produce Base diagnóstico 12,214059942428673 USD, MOS 7,939138962578638 e impacto −5,170387795191722%. Cambia la relación frente al precio 7,94; no es salvedad menor. No es el DCF final.
Dividendo aprobado US$0,28 = 2,1739% del candidato: no descontarlo otra vez sin conciliar pago, patrimonio y periodo. La nota de evento posterior acredita aprobación/calendario, no pago consumado.
El ACP BCB equivale al 5% de RWA: no sustituir por el 2,5% de Pilar III 2025. No sumar IRRBB mecánicamente para inferir incumplimiento.
CIERRE DE PROMOCIÓN A-1.2 — 3 NOVIEMBRE 2026
Estado normativo: CANDIDATO_REVISADO; publicación BLOQUEADA. Esta conclusión sustituye la etiqueta interna EN_REVISION de la revisión previa: según reglas v27 §0A/§8A, EN_REVISION es una salida de publicación tras superar controles, no una forma de omitir incertidumbres materiales.
Datos recuperados y aplicados: el 6-K detallado 000155485526001791 permite sustituir el redondeo 6M por cifras exactas y completar ingresos transaccionales/financieros. LTM: ingresos R$20.588,036m y NI R$2.151,112m; P/E observado 5,59286996x. El cálculo candidato DCF permanece US$12,88000621/MOS US$8,37200404: no se presenta como precio publicable.
Capital BCB IF.data, conglomerado C0084813, junio 2026: RWA R$32.846,2419551m; PR/CET1 R$4.940,57756456m; ratio calculado 15,04153069%. RWA crédito 7.334,55491588m, mercado 270,1239225m, operacional 13.293,45319147m y pagos 11.948,10992525m; suma conciliada. ACP reportado R$1.642,31209775m equivale a 5% del RWA; IRRBB R$761,57362304m. No sustituir ese ACP por el 2,5% histórico ni declarar incumplimiento o exceso distribuible sin verificar régimen, deducciones y tratamiento del IRRBB. Existe diferencia frente al 14,9% prudencial de la presentación: falta conciliación de versión/perímetro. Consulta realizada 3-nov-2026; verificar versión disponible al corte, no asumir ausencia de revisiones posteriores.
Acciones SEC notas 23–24: emitidas 290.677.709 menos autocartera 15.031.687 = 275.646.022 en circulación al 30-jun. Promedio básico trimestral 276.672.131 + dilución media 2.788.611 = 279.460.742. El input 279,5m es redondeado y sigue siendo proxy; ninguno de esos dos denominadores acredita dilución económica al 30-oct. LTIP/LTIP Goals son los únicos instrumentos potencialmente dilutivos identificados en la nota EPS; no añadir doble deducción de opciones.
Corte temporal: nota 32 acredita aprobación de dividendo US$0,28 el 11-ago, con pago previsto 30-sep-2026. Equivale al 2,1739% del DCF candidato; diagnóstico individual, NO corrección completa ni prueba de pago. Conciliar patrimonio, pagos reales, acciones y tiempo transcurrido antes de trasladar el valor junio a octubre.
Costo de patrimonio: se confirmó que ERP 3,70% del corte mensual 30-sep corresponde a Treasury 5,29% (alternativa libre de default 5,07% con ERP 3,92%), no al 4,94% de otro día. Con los demás supuestos provisionales intactos, la pareja Treasury/ERP compatible produce Ke USD 10,9808% y BRL 12,82505572%. El motor candidato usa todavía 10,6308%/12,46923949% y beta 0,82 constante; requiere recalibración conjunta y transición terminal a beta 1, con CRP terminal justificada. Los diagnósticos no se confunden con entradas definitivas.
Múltiplos: P/E y P/FCFE siguen PENDIENTE_ANCLA, sin valores justos ni matrices independientes. EV/EBITDA, EV/FCFF y P/OCF consolidados no se usan por fondeo bancario/settlement no separable. P/BV es complementario opcional según §5A; el validador bancario vigente aún exige P/BV, una discrepancia normativa por corregir en mantenimiento separado con regresión, nunca eludiendo el control.
Integración: las 46 hojas de plantilla no equivalen a estados históricos completos; Financials Multiples conserva fórmulas sin salidas empresariales. Faltan cobertura F2, contrato bancario, controles oficiales y conciliación app. La fuente de datos mejoró, pero promoción F4 sigue bloqueada; no hay auditoría independiente ni publicación.

## Dependencias exactas de continuación
1. Conciliar BCB capital/ACP/IRRBB con nota gerencial 14,9%/22,5%, restricciones de filiales y movimientos hasta corte; proyectar capital elegible y recursos distribuibles, sin sumar patrimonio contable completo como capital regulatorio.
2. Acciones al corte, LTIP, recompras posteriores y pago efectivo del dividendo; puente junio–octubre con fechas de los flujos.
3. Recalibrar Ke con pareja mensual homogénea; beta bottom-up apropiada y transición terminal beta 1, CRP/ inflación justificados. Recalcular cuatro historias/matrices conjuntamente y sincronizar narrativa.
4. Anclas históricas por ciclo con ajuste de tasas y tope fundamental para P/E/PFCFE; matrices independientes FY+3 y descuento bancario nativo. P/BV opcional por norma; no alterar gate global en este PR.
5. Completar historia/indicadores de plantilla y contrato hoja→JSON→app, pruebas y preview. Promover solo después de controles aprobados.

No merge, no despliegue, ninguna ficha activada. Estado correcto: CANDIDATO_REVISADO; publicationReady=false.
