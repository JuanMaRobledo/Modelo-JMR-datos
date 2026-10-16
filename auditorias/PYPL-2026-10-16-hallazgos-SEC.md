# PYPL — conciliación financiera SEC y revisión JMR del 16-oct-2026

**Propósito:** documentar hechos, supuestos y controles sin atribuirles una certificación económica que todavía no poseen.
**Autorización de publicación del usuario:** concedida en el chat. No elimina los gates.
**Fuente del modelo propuesto:** [Google Sheet / Auditoría económica PYPL](https://docs.google.com/spreadsheets/d/1LI1LHXYFiCqg5i1_DDzs53Rd4eKv4zhDex2pxSvKuCs/edit#gid=2026101603).
**Análisis completo revisado:** [Google Doc PYPL](https://docs.google.com/document/d/1sJZi5I3dI1Lv02nr5mrkT4bOVrXY91fPaXqxAaINqTc/edit).
**Fuentes:** [10-Q a 30-jun-2026](https://www.sec.gov/Archives/edgar/data/1633917/000163391726000082/pypl-20260630.htm); [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1633917/000163391726000024/pypl-20251231.htm); [Proxy 2026 equity compensation](https://www.sec.gov/Archives/edgar/data/1633917/000119312526145735/d45512dars.pdf).

## 1. Arrendamientos — RECONCILIADO, no hay doble contabilización

- Deuda financiera SEC: **US$13.400 millones** (corto plazo2.505 + largo plazo10.895).
- Arrendamientos financieros SEC: **US$11M** (5 corrientes +6 no corrientes).
- `Input sheet!B16=13.411` representa deuda financiera + financiero; NO incluye pasivo arrendamiento operativo.
- Arrendamientos operativos reconocidos en balance SEC: **US$810M** (142 corriente +668 no corriente).
- Conversor de la hoja: US$837,08M de valor presente contractual, discrepancia US$27,08M frente a 810 por descuento/estructura de plazo (3,34%). Se añade UNA sola vez vía `Valuation output!B27=14.248,08`; no se vuelve a añadir el saldo reconocido810.
- `Input!B78=0`, `B79` enlaza al PV, `B80` al ajuste EBIT US$46,42M, `B81=CONCILIADO` con prueba de las relaciones.
- Nota económica: no afirmar que PV837,08 sea idéntico a pasivo contable810; diferencial cambia valor en ~US$0,032 por acción.

## 2. Inversiones privadas — CONCILIACIÓN DE PERÍMETRO SÍ, VALOR ECONÓMICO PENDIENTE

- Nota 8 10-Q: inversiones estratégicas US$1.735M, de los cuales US$106M valores cotizados y US$1.629M no cotizados (205 método de participación y1424 measurement alternative).
- `Valuation output!B41` excluye `Input!B20=1735` del capital invertido y `Valuation output!B30` lo añade una vez al equity. No hay doble conteo contable.
- Pero book value de no cotizadas NO es fair value verificable: el 10-Q indica ausencia de cotización de sus instrumentos privados. Valuaciones razonables deben tratarlo como estimación de analista, no certificación externa.
- Sensibilidad económica: DCF Base US$100,856; 25% de descuento al carrying amount privado → **US$100,380**; descuento50% → **US$99,904**.
- `Input!B85` permanece **PENDIENTE: VR privada**. No se inventó valoración transaccional independiente.

## 3. Impuestos — REVISADO

- FY2025: tasa efectiva 16,8% (10-K Nota16, incluye evento extraordinario reestructuración).
- H1 2026: efectiva18% (10-Q Nota16); trimestre Q2 16%.
- Base normalizado `Input!B24=19%` explícito y ligeramente prudente; terminal marginal `Input!B25=25%`. Trayectoria años1–5 efectiva19% y años6–10 progresiva hasta25%. Escudo deuda25%.
- `Input!B89=Convergencia Damodaran`, `B91` reportes oficiales, `B92=VALIDADO`, `B93` vinculado a B24. No se afirma que 25% sea la tasa fiscal contable actual.

## 4. Dilución — MEDIDA, ACTUALIZACIÓN ECONÓMICA AÚN PENDIENTE

- 10-Q al22-jul-2026: **855.460.874 acciones efectivas**, replicadas en Input B22.
- Q2 promedio básico877M, diluido882M; **5M** por equity incentives, 31M instrumentos potenciales excluidos de ese EPS por antidilución o condiciones. H1 gastos de compensación stock **US$585M**.
- 10-K FY2025: 31,757M RSU/PBRSU outstanding al 31-dic-2025, 27,499M expected-to-vest. 2026 Proxy: 39,163,335 derechos de planes existentes, **no significa 39M warrants clásicos**; sólo 17.676 opciones originadas en adquisiciones con strike20,82.
- 2026 Plan autoriza hasta39,1M nuevas acciones, pero autorizadas **no son emitidas ni outstanding**.
- No se deben tratar autorizaciones, expected-to-vest de diciembre y acciones dilutivas promedio de Q2 como sumables: ello contaría múltiples veces mismos instrumentos. Sin roll-forward de emisiones/forfeitures 2026 no hay base para valor actual único.
- Sensibilidad: 5M adicionales en denominador → US$100,270 vs 100,856; 27,499M hipotéticos→US$97,715. El gasto SBC permanece en EBIT; no cargarlo de nuevo como deuda.
- `Input B108=PENDIENTE: dilución`. A falta de roll-forward y opción consolidada, no se declara VALIDADO.

## 5. Costo de capital — MATEMÁTICA CONCILIADA, FUENTE PUNTUAL Kd PENDIENTE

- Mercado 15-oct-2026 Treasury10años **5,086%**, Input B35 redondeado5,09%, coherente con DCF USD.
- ERP geográfica aproximada4,465%; beta no apalancada sector US Information Services0,756; beta apalancada ~0,90; Ke9,11%.
- Capital E79,71% /D20,29%, Kd input6,19% pretax, después de impuestos4,64%; WACC **8,205%**. WACC terminal8,99%, g terminal3%.
- El input Kd6,19 implica spread~110bps sobre Treasury de fecha del corte, a comparar con **84bps benchmark investment-grade** reportado el 12-oct-2026 por Reuters. El 10-Q declara issuer investment grade, sus emisiones mayo2026 cupón4,55%/4,95%/5,55% y tipo efectivo4,87%/5,11%/5,66% al momento de emisión. **Esos cupones no son automáticamente rendimientos de mercado a octubre.**
- Diversas capturas web de bonos PYPL muestran rendimientos indicativos, pero no una cotización fijada a 15-oct-2026. Se mantiene el costo6,19% como hipótesis prudente identificada, no como dato de mercado comprobado.
- `Cost of capital worksheet!B35='Input sheet'!B35+0,011`: Rf 5,09% + spread conservador 110pb. Decisión del analista: **84pb IG de Reuters 12-oct-2026 +26pb de prudencia**, PYPL inversión grado según 10-Q. `Cost of capital worksheet!B84=VALIDADO` verifica método Detailed y conciliación de pesos/tasas; **no representa cotización del bono PYPL en 15-oct**.

## 6. Disrupción — CORREGIDA Y VALIDADA CUANTITATIVAMENTE

- Antes había Sales-to-Capital extraordinario22,46 y la liberación automática de capital al caer ventas; la hoja mostraba reinversión negativa hasta -209,87M/año.
- Ahora `Input B98=Sin liberación` y `Valuation output!C165:L165` está ligado a ese selector con `MAX(0;reinvestment_original)`. Fórmulas anteriores conservadas en las notas.
- En `Escenarios e historias!E7` S/C=2,37 igual que empresa Base; los años de reinversión negativos se limitan a cero (no se presume liquidación de capital).
- DCF disrupción cayó **US$39,29 → US$38,796234**; promedio de cuatro historias **US$88,91 → US$88,84**. Base **US$100,855936** y MOS 35% **US$65,556358** no cambian.
- Cuatro escenarios `K5:K8=LISTO` cuantitativamente; la valoración global sigue condicionada al punto B85/B108/B84.
- Matrices 5×5 y DCF inverso intactos en el Base y con centro US$100,855936.
- El artículo en Drive se corrigió y anexa estas salvedades.

## 7. Próximo gate, sin producción alterada

Antes de regenerar JSON para app con `JMR-valuation/scripts/desde_cero.sh app`, se necesita respaldo de tratamiento económico de las inversiones privadas (B85), premios dilutivos (B108) y costo de deuda con fuente/fecha (Cost B84); además ejecutar el validador real de `JMR-valuation/scripts/audit_dcf_certificado.py` contra manifiesto PYPL y hoja de trabajo.
Como no existe manifiesto PYPL en `JMR-valuation/reference/fuentes/` (solo template y NFLX), **este gate no se ha ejecutado**. No inventar estado PASS.
No sobrescribir `valoraciones/PYPL-1790205796042.json` ni `analisis/PYPL-research-1790205847031-vcqtg.json` con campos parciales o tablas cacheadas obsoletas; su contenido actualmente presenta DCF anterior distinto.
**ESTADO: PREPARADO, NO PUBLICADO. Costo de capital validado como estimación de analista; quedan B85, B108 y validador integrado.** Integrar sólo tras pasar controles y certificar consistencia hoja/visor/informe/bitácora/PDF.
