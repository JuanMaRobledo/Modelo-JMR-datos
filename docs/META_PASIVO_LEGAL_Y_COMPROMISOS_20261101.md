# META · pasivo legal, compromisos de capacidad y publicación A-1.2 · 1-nov-2026

**Estado: META-20261101-A12-R1 publicada como EN_REVISION, sin auditoría económica.** Continúa `CIERRE_GATES_META_NVDA_20261101.md` y `FECHAS_TASAS_META_NVDA_20261101.md`.

## 1. Pasivo legal (aplicado en la hoja)
10-Q 30-sep-2026, Nota 8: provisiones legales **US$19.881 M** = 11.577 corrientes + 8.304 no corrientes (acuerdo multiestatal de fiscales generales de ago-2026, otras multas y sentencias estimadas, honorarios devengados). No estaban en la deuda (116.026) ni en minoritarios (0), y las historias parten de márgenes sin cargos legales, de modo que no hay doble conteo.

Se escribió `Input sheet!B21 = 19.881` con nota explícita (C21). `B21` solo alimenta el puente a patrimonio de los cuatro escenarios y el motor de sensibilidad; META no tiene minoritarios, así que se usa como campo de «reclamaciones no financieras». Valor bruto, sin efecto fiscal (cota superior; las multas a gobiernos normalmente no son deducibles). **Efecto: −US$7,78 por acción (Base 745,29 → 737,51).** El puente EV→patrimonio de los múltiplos no incluye esta partida (limitación declarada). Valores previos: `evidencia/cierre-gates-meta-nvda-20261101/meta_pasivo_legal_antes_despues.json`.

## 2. Compromisos de capacidad (NO aplicados; salvedad material)
10-Q Nota 10: **arrendamientos aún no iniciados por US$355.730 M** (centros de datos, energía, colocación, red; 2026–2036, plazos de 1 a 30 años) y **compromisos no cancelables por US$454.520 M** (capacidad de nube de terceros, servidores y red, contratos de energía, hardware de consumo). Frente a ingresos LTM de 241.605 M y valor operativo Base de 1.918.130 M. La hoja solo tiene como deuda los pasivos de arrendamiento ya reconocidos (31.173 M; `B18 = No`).

La Base los absorbe, si acaso, por margen objetivo (44 %) y Sales-to-Capital 0,52. Contraste verificable con datos de la hoja: reinversión del año 1 = US$94.784 M; capex LTM 104.438 M menos D&A LTM 24.920 M = capex neto 79.518 M; con la guía de capex 2026 (135.000–145.000 M, incluye principal de arrendamientos financieros) el neto sería ~110.000–120.000 M, **15.000–25.000 M por encima de la reinversión Base del año 1**. Si la reinversión necesaria fuera mayor, el valor bajaría de forma material. Orden de magnitud, no ajuste: 355.730 M son US$139 por acción sin descontar. No se modificó la hoja porque el tratamiento correcto (qué parte ya está en márgenes y en S/C) exige una decisión de supuestos.

## 3. Otros hechos de la revisión
- Activos no operativos 21.077 M = inversiones no cotizadas bajo alternativa de medición; se excluyen 11.547 M del método de participación (Ventures de centros de datos Louisiana y Texas, 20 %, contraparte de arrendamientos que comienzan en 2029 y 2028).
- Opciones: 20 M a US$2.788, ~4 años, vol. 42,71 %: valor US$490,8 M. RSU 134,5 M no adquiridas: ~4,7 % devengado, inmaterial.
- Múltiplos (regla de ciclo, `reference/multiplos_v3/META_*` en JMR-valuation): valor por múltiplos Base 399,88 frente al DCF 737,51 (−46 %), por el tope del múltiplo justificado con el capex de IA en el FCFF de FY+3.
- Resultado nativo: Base 737,51 · MOS35 479,38 · Conservadora 457,18 · Optimista 1.086,77 · Disrupción 232,18. K5:K8 = LISTO.

## 4. Cambios en validadores y pruebas (sin relajar controles)
Tres ramas heredadas del contrato de META R4/R5 (`auditar_integridad.cjs` ×2, `validar_catalogo.cjs`) se activaban con cualquier revisión de META; se restringieron a registros que no sean A-1.2, que pasan por el contrato A-1.2 (siete posiciones de matriz, trazabilidad). Dos pruebas de META y una de recapturas se actualizaron como en NVDA/XP (la revisión anterior debe existir en disco y estar fuera del catálogo activo); el guardia «al menos una recaptura» pasó a exigir que META R5 y NVDA R4 conserven su evidencia; el recuento A-1.2 pasó de 22 a 23.
