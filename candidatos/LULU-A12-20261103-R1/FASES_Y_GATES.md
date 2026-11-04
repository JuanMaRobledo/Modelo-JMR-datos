# LULU A-1.2 · Entrega y control técnico — corte 03-nov-2026

**revision_id:** LULU-A12-20261103-R1
**método:** A-1.2
**estado:** CANDIDATO · NO FUSIONAR como expediente publicado
**hoja nueva:** https://docs.google.com/spreadsheets/d/1XY_iXmarfM0ESnzu3RMV5E4TkgrJAy9-XzJ2PxndHz4/edit
**carpeta:** https://drive.google.com/drive/folders/1rY9vlGOuw7e8kJvhYRAaNaQR5lc4EURR
**fuentes:** SEC 10-K FY2016–FY2025 y SEC 10-Q 02-ago-2026 (detallados en Nivel 2).
**histórico:** libro anterior 59 tabs id 1wuEhOhrjlL5t-oSO9sRd7Py0Vw-47rv_4AAwaS8-ZJw NO modificado, no usado como autoridad.

## Evidence checks
| Control | Evidencia | Estado |
|---|---|---|
| Fuente maestra IA | copia nativa desde plantilla oficial 1e-lbQmCkObfq74YLpWnMmIidmcdsJQ-6uN4oiHnNTEQ; 46 pestañas | CONFIRMADO |
| Diez ejercicios históricos + LTM ventas, EBIT, CFO, capex | Income Statement y Cash Flow Statement B:L | CARGADO |
| Balances 11 cierres | Balance Sheet B:L; activos – pasivos – patrimonio = 0 (11 de 11, 3 decimales) | VALIDACIÓN PARCIAL APROBADA |
| EBIT one-off | Input B13 = Income Statement L12 − Entradas históricas auxiliares C65, 134,5m IEEPA | RECONCILIADO |
| Guía y supuestos iniciales | FY2026 10,35–10,5bn; Input B27:B33 y Escenarios e historias | PROPUESTO, SIN VALIDAR |
| cuatro escenarios | Escenarios e historias filas 5–8 con probabilidades y serie de diez crecimientos | CARGADO |
| WACC Detailed (Cost of capital worksheet B84) | retorno observado PENDIENTE | BLOQUEADO |
| DCF motores (Escenarios e historias K5:K8) | cuatro PENDIENTE; H5:H8 vacíos | BLOQUEADO |
| Política de impuestos (Input B92) | PENDIENTE | BLOQUEADO |
| Activos no operativos (Input B85) | PENDIENTE | BLOQUEADO |
| Casos especiales (Input B108) | PENDIENTE | BLOQUEADO |
| cinco múltiplos FY+3 y sus 5×5 | datos/anclas todavía incompletos | NO VALIDADO |
| DCF 5×5 / inverso y MOS35% | dependientes de WACC validado | NO DISPONIBLE |
| 18 candados, controles_todas.sh / CI | no ejecutados sobre una revisión publicable | NO EJECUTADO |
| catálogo JSON publicado | esta rama solo tiene documentos candidatos fuera del catálogo | NO MODIFICADO |
| URL producción de LULU R1 | no existe publicación comprobada | NO PUBLICADO |

## Bloqueos materiales con prioridad
1. **Leases ASC842:** US$2.141,127m en deuda reconocida + gasto de alquiler en EBIT GAAP. No capitalizar dos veces y tampoco descontar leasing en equity sin ajustar EBIT para que no haya doble conteo. Resolver con una convención de FCFF consistente y prueba económica lado a lado, luego WACC Ke/Kd.
2. **Capital de mercado y opciones:** 111,682m acciones al 02-ago-2026, la recompra posterior podría disminuirlas al 03-nov; opciones1,525m strike US$258,81, **plazo remanente no documentado**. Validar RSU/PSU y dilution.
3. **FY vs LTM:** crecimiento -6% fue anclado a FY2026 guía, pero el DCF comienza desde LTM a ago2026. Alinear año financiero correcto.
4. **Impuestos, ROIC y reinversión:** Input B89:B94, B82:B87 y B98:B101, NOL: examen material, RONIC y lag 0/1 comparados con DCF completo; sector Apparel sales/capital1,77 es ancla, no salida.
5. **Múltiplos:** normalizar y documentar 5 métodos prioritarios con FY+1/2/3, descuentos, balance equidad, casos negativos y matrices Base sin N/D disfrazado de cero.
6. **Regresión y publicación:** cumplir gates de app y del motor y conciliar hoja→JSON→ficha. No tocar producción hasta que todo ello esté verificado.

## Lo que NO se está haciendo
- No se sustituye catálogo de valoración de producción.
- No se fusiona esta rama automáticamente.
- No se presenta el cálculo independiente como DCF oficial ni como recomendación.
- No se afirma ejecución de CI, preview o auditoría económica.

## Orden de continuación
Resolver bloques 1–4 → completar 5 múltiplos y modelos → cálculo nativo y cuadre/fuentes → controles 18 candados/CI y matrices 5×5 → Nivel 1 y 2 revisión editorial → crear actualización oficial catálogo con JSON y vínculos → fusionar cuando listo → comprobar ficha visual real EN_REVISION. Fase 5 posterior, guiada por el usuario.

## Entregables de esta rama
- NIVEL_1_ANALISIS.md: narrativa 14 capítulos.
- NIVEL_2_DATOS_SUPUESTOS_Y_CONTROLES.md: cuantitativo 12 apartados.
- FASES_Y_GATES.md: esta evidencia de ejecución y pendientes.

**Nota:** “en revisión” es un estado de la app reservado a fichas publicadas tras aprobar gates; la presente revisión es solo un candidato documentado.
