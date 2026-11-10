# LULU A-1.2 · Entrega y control técnico — corte 03-nov-2026
**NUEVA FOTO DE ESTADO**: cuatro DCF LISTO; WACC, activos no operativos, impuestos, casos especiales VALIDADO en hoja; cinco métodos Base y sus matrices nativas calculados; CI+snapshot/editorial/publicación pendientes. Leer el anexo final.


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


---

## Actualización técnica realizada el 03-nov-2026 (R1, revisión reproducible)

**La documentación precedente refleja el estado inicial del candidato, no su estado final actual. Esta sección prevalece sobre todas las referencias anteriores a WACC, DCF y múltiplos pendientes.** Los controles económicos indicados abajo son controles **de hoja**, no equivalen a los gates CI o a una certificación de publicación.

### Cuadro de valoración nativa
- Hoja oficial 46 pestañas: https://docs.google.com/spreadsheets/d/1XY_iXmarfM0ESnzu3RMV5E4TkgrJAy9-XzJ2PxndHz4/edit
- FCFF DCF Base presente: **142,9155850834 USD/acción**; MOS35%: **92,8951303042 USD/acción**.
- DCF Conservador: **105,6981070993**; Optimista: **184,5616118779**; Disrupción: **73,9986974158**, separada del promedio. Valor esperado 50/30/20: **140,07954575**.
- Valor operativo de diez años y perpetuidad: **US$16.875,73 millones**; PV del flujo explícito **US$7.282,42 millones**; PV terminal **US$9.593,31 millones** (~56,85% del valor operativo). Puente a equity: deuda leasing **US$2.141,127m**, caja **US$1.389,737m**, opciones **US$34,19m**, divisor económico estimado **112,585m acciones**; patrimonio ajustado **US$16.090,15m**.
- Cost of capital worksheet B84 **VALIDADO**; Rf **5,29%** del corte mensual Damodaran, ERP implícita mature **4,41%** del mismo corte; beta levered bottom-up **~0,8949**; Ke **~9,24%**, Kd histórico/contratos de leasing **4,40%** (proxy, no cotización de nueva deuda), peso equity **84,90%**, lease-debt **15,10%**, WACC inicial **~8,31%** y terminal **9,70%**. Kd contractual por debajo de la tasa Treasury contemporánea implica un riesgo de costo de deuda de mercado: sensibilidad necesaria en F5; no proclamar coste de financiación de nuevo contrato verificado.
- 4 historias hoja Escenarios e historias!K5:K8 = **LISTO**; nivel DCF Sensibilidad DCF tres matrices 5×5 con centros conciliados **OK**: WACC×g, ROIC×g y crecimiento×margen.
- Cinco múltiplos nativos prioritarios EV/EBITDA, EV/FCFF, P/E, P/FCFE y P/OCF, con 5 sensibilidades Base5×5 JMR de centro **OK**, precios de cierre fiscales FY2022–FY2025 fechados y descuento de FY+1/2/3 a Ke. Anclas Base 7,5068x, 21,6300x, 12,8728x, 22,0561x y 12,387x respectivamente. El P/FCFE último FY usa proxy CFO−CapEx porque no hay deuda bancaria, no es caja ajustada regulatoria ni dato de consenso. P/V y P/BV opcionales sin ponderar.
- Precio objetivo ponderado **a cierre FY+3**: Base **164,31 USD**, Conservador **129,73**, Optimista **203,23**, con pesos DCF40%, EV/EBITDA20%, EV/FCFF10%, P/E20%, P/FCFE5%, P/OCF5%. No es valor presente intrínseco. El precio observado 03-nov-2026 **106,95 USD**.

### Calibración ROIC, reinversión, crecimiento y margen
- Eficiencia de capital histórico ROIC FY2025 **35,16%**, ROIC LTM ago-2026 **26,52%**, calculados con capital invertido medio y periodos consistentes; el cambio −8,64 puntos obliga a no extrapolar la mejor fase de la empresa. ROIC perpetuo Base **14%**, Conservador **11,5%**, Optimista **16%**, Disrupción **9,5%**. La reinversión terminal Base g/ROIC = 3%/14% = **21,43% del NOPAT** bajo definiciones armonizadas.
- Sales-to-Capital marginal de la Base **1,80x** (años1–5), **1,77x** (años6–10), frente a Damodaran Apparel USA aprox1,77x; historia propia de eficiencia incremental aproximada FY2021–2025 ~1,87x pero FY2023–2025 ~0,95x muestra caída; no confundir con ventas/capital contable. La caída inicial de ventas no genera liberación automática: Input B98:B101 = 'Sin liberación' por falta de evidencia de cierres de activos.
- Prueba reproducible de lag inversión/ingresos en copia separada: lag1 (oficial) DCF Base **142,915585**; lag0 **144,987046**, diferencia **2,071461 USD/acción (+1,45%)**, con **todo el flujo** descontado, terminal constante. Copia aislada: https://docs.google.com/spreadsheets/d/1OjGuh2aG3CRnwWj05FpO8YdB16aPxwS75jGa_pAi_U0/edit.
- DCF empieza sobre LTM ago2026 ingresos **11.093,955m**; año siguiente modelado por guía FY2026 de 10.350–10.500m para segundo semestre y juicio +1% para H1FY2027 da estimación forward **~10.473,87m** y crecimiento **−5,59%**. Años siguientes Base **2%, 4%, 5%, 5%**, desacelerando hasta 3% año10 y perpetuidad3%. El +1% semestral futuro es JUICIO explícito, no guía publicada.
- EBIT GAAP LTM **1.978,775m**, ajuste extraordinario reembolso arancelario IEEPA **−134,500m** e interés imputado del leasing a 4,4% sobre pasivo **+94,2096m** da EBIT DCF **1.938,4846m**. Esta suma es **proxy** para reconciliar el leasing bajo ASC842, no ingreso reportado. Margen año1 **14,2%** y objetivo año10 **17,5%**, por debajo de picos GAAP FY2024 **23,67%**; las trayectorias Conservadora15%, Optimista20%, Disrupción12,5% requieren readaptación de promociones/inventario. No duplicar amortización de ROU ni añadir deuda leasing dos veces.
- FY2025 10-K: pérdidas fiscales NOL **US$35m** (Input B62=Yes, B63=35), impuesto efectivo LTM ~29,40%, marginal normalizado como JUICIO **29%** a largo plazo. Input B92 impuesto, B85 inversiones no operativas y B108 casos especiales = **VALIDADO** dentro de la hoja. Modela 1,525m opciones, strike258,81USD, 5,3 años de madurez residual proxy, vol43,69% proxy, RSU0,759m y PSU0,288m a factor de entrega50%, con costo potencial de dilución; requiere stress 0–100% PSU y variaciones de volatilidad.

### Estado real de publicación
**NO PUBLICADO** en app todavía. El libro tiene controles internos habilitados, pero la rama sigue PR #243 en draft con documentos fuera del catálogo. Para publicar se debe elaborar JSON nativo con snapshot/hash reproducible de cinco matrices y tres DCF 5×5, integrar **Nivel1 narrativo >=7.500 palabras en 14 capítulos**, Nivel2 HTML, comprobar contrato de catalogo scripts/validar_catalogo.cjs, integridad scripts/auditar_integridad.cjs, profundidad editorial y regresión CI; luego fusionar y verificar URL efectiva. La auditoría económica F5 no es requisito para EN_REVISION, sí permanece abierta; no inventar aprobación de CI ni afirmar publicación antes de constatarla.
