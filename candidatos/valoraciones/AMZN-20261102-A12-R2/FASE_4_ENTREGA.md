# AMZN · AMZN-20261102-A12-R2 · Fase 4 · CERRADA CON CONTROLES PENDIENTES

2026-11-02 · Claude Code (sesión remota nueva), modelo `claude-opus-5-5`, esfuerzo `high` (metadatos de la sesión) · hoja `1h6Xv5cNqwtKPpqI81KiZ_FNpTl4k_uQQS2QJEHphaBI` · base auditada Modelo-JMR-datos `b1fb039` · prompt `auditoria-economica-jmr-v1.3`

**Independencia: SÍ.** Las fases 2 y 3 se hicieron con ChatGPT Work/Codex (GPT-6), según sus entregas. Esta auditoría la hizo otro LLM en otra sesión. Las entregas de las fases 2 y 3 se leyeron **después** de formar el juicio, solo para contrastar. **AISLAMIENTO=OK**: todos los datos provienen de documentos de Amazon (SEC CIK 0001018724), del Treasury, de Damodaran y de la hoja R2. Las hojas de otros tickers solo las leyeron `estados_completos.py` e `integridad_hojas.py` como patrón de filas, sin aportar cifras.

**Dictamen: PENDIENTE** · Tesis: **Plausible con reservas** · Estado del expediente: **CANDIDATO** (sin cambios; no se marca AUDITADO) · Informe: [`AUDITORIA_ECONOMICA_AMZN_R2.md`](AUDITORIA_ECONOMICA_AMZN_R2.md) · Evidencia: [`auditoria_fase4/`](auditoria_fase4/)

## Hecho y verificado (con evidencia)

- **Revisión.** AMZN no figura en `catalogo.json` y no existe `auditorias/solicitudes/AMZN/`. Audité la última revisión identificable, R2 (CANDIDATO), como permite el prompt 3/3 («valoración más reciente identificable»).
- **Réplica independiente** (`scripts/dcf.py`, `blocks.py`, desde las entradas de una captura propia de la hoja con SHA-256 `c3fcffec…8c98`). Base 148,6762, Conservadora 91,9273, Optimista 225,3278, Disrupción 59,9816: error ≤ 1e-13 USD por acción. MOS 96,64 y promedio de 3 de 153,65 ✓. Las 75 celdas de las matrices DCF nativas, reproducidas con error máximo de 8,5e-14.
- **Fuentes primarias.** Ingresos, EBIT e intereses LTM, patrimonio, caja, deuda (179.952 + 114.783 + 9.726 = 304.461), no operativos (Anthropic 146,2 + 92,5, OpenAI 50,0, warrants 4,3) y acciones verificados contra el 10-Q del T3-26 y XBRL. Ingresos y EBIT de FY2016–FY2025: los 20 valores exactos. Rf 4,94 % (Treasury, 30-oct). Precio 240,35 (cierre del 30-oct).
- **ERP.** Se descargaron `ERPNov26.xlsx` y `ERPOct26.xlsx` de Damodaran: noviembre T12m 3,79 %, pago sostenible 4,41 % (T.Bond 4,94 %); octubre T12m 3,70 % (= `corte_vigente.json`). La hoja usa 4,55 %, un «rebase» (nota de `Country equity risk premiums!B2`).
- **Pruebas de alternativas** (diez años más terminal, mismo corte): `alternativas.json` y `alternativas2.json`. Resumen en §13 del informe.
- **Inventario de entradas.** 4 pestañas exigidas, 207 celdas sin fórmula; 71 diligenciadas, las 71 con nota de fuente (`inventario_entradas_R2.csv`, tabla de 71 filas en §3).

## Controles de cierre (resultado real de cada uno)

| Paso o control | Resultado |
|---|---|
| 1. Catálogo y solicitudes | Ejecutado: AMZN fuera del catálogo; sin solicitudes; R2 identificada |
| 2. Réplica del valor principal | **APROBADO** (error < 1e-13) |
| 3. Fuentes de insumos materiales | **APROBADO**, con dos excepciones: ERP (A-01) e impuesto diferido de los no operativos (B-01) |
| 4. Seis preguntas y efectos en ambas direcciones | Ejecutado (§5–§10, §13) |
| 5. `diff_formulas_plantilla.py --sheet-id R2` (oficial) | **0 reemplazos**; 0 pestañas añadidas o faltantes; no hay archivo de excepciones de AMZN |
| 5b. `candados.py` (oficial; resolvedor de hoja redirigido en memoria a R2 por `run_oficial.py`) | **15/15** |
| 5b. `inputs_completos.py` (ídem) | **0** vacías esenciales |
| 5b. `estados_completos.py` (ídem) | **2 hallazgos** (`CFS!38–39`) → C-06 |
| 5b. `integridad_hojas.py` (ídem) | **19 hallazgos**: 15 `#NUM!` en múltiplos (C-02) + 4 contra el motor legado (falsos positivos, D-01) |
| 5b. `controles_supuestos.py` | Oficial (ficha legada): 2 S1. **PRUEBA EQUIVALENTE** con datos de R2 (`supuestos_r2.py`): 1 S1, falso positivo por el bug `rstrip("N")` (D-01) |
| `probabilidades.py` (oficial) | **0 fallos** |
| Formato unificado: selectores y validaciones | **NO EJECUTADO**: `unificacion_hojas.py` no existe en el repositorio; las fórmulas y el orden de pestañas sí se verificaron |
| 6. Clasificación y dictamen | A: 2 · B: 5 · C: 8 · D: 2 → **PENDIENTE** |
| 18 títulos H2 exactos y en orden | **APROBADO** (comparación automática con el prompt) |
| Resumen oral de 90 a 150 palabras | **126 palabras** ✓ |
| Hallazgos con evidencia, celda, efecto y propuesta | ✓ (§15) |
| Hoja de auditoría independiente en Google Sheets (REGLAS §11) | **NO EJECUTADO**: el clasificador de permisos de la sesión denegó crear archivos en Drive |
| Publicación en `auditorias/narrativas/AMZN.md` | **No publicada**: requiere autorización expresa del usuario |

**PASOS: 7/7 ejecutados** (1, 2, 3, 4, 5, 5b, 6). En el 5b, `controles_supuestos` va con prueba equivalente; la comparación de selectores queda NO EJECUTADA, con su motivo.

## Decisiones y juicios

- Audité un **CANDIDATO** no promovido en lugar de bloquear por la ausencia en el catálogo (README de fases, continuidad §2). El dictamen se refiere solo a R2.
- Uso la **columna T12m** de Damodaran como convención JMR porque `corte_vigente.json` (octubre, 3,70 %) y `aplicar_corte.py` la usan. Doy también el resultado con pago sostenible (4,41 %, +3,2 %) para que el usuario elija. Si se cambia la columna, debe hacerse en REGLAS para todas las empresas.
- **A-02** (arrendamientos): lo clasifico como doble conteo porque con ASC 842 el costo del arrendamiento operativo está dentro del EBIT. La conversión de Damodaran y la exclusión de la deuda dan +6,0 % y +6,2 % respectivamente.
- **B-04** (I+D): queda sin acotar. Mantiene el dictamen en PENDIENTE aunque A-01 y A-02 se corrijan.
- La decisión precio/valor no cambia en ningún caso probado (máximo 187,43 < 240,35).

## Pendiente o bloqueado

1. **Fase 2 nueva (`AMZN-<fecha>-A12-R3`)** con estos cambios propuestos (requieren aprobación del usuario):
   - A-01: prima madura y Rf de la misma fecha y columna (Damodaran 1-nov-26 T12m 3,79 % con Rf 4,94 %, o el corte oficial 30-sep 3,70 % / 5,29 %).
   - A-02: `B18 = Yes` con el convertidor de arrendamientos, o excluir los 100.288 de arrendamientos operativos de la deuda (y de la deuda de mercado del WACC).
   - B-01: restar el impuesto diferido AFS de 34.608 y estimar el de las preferentes de Anthropic (≤ 22,8 mM).
   - B-02: justificar el ROIC terminal de 12,5 % frente a la ventaja durable (referencia 16,5 %, piso Retail 13,6 %) o ajustarlo.
   - B-03: revisar el mapeo de AWS en la beta (Computer Services frente a Software) y añadir beta de regresión.
   - B-04: acotar la capitalización de I+D.
   - C-02: anclas y matrices 5×5 de EV/EBITDA, P/E normalizado y P/OCF.
   - C-08: incorporar Anthropic y OpenAI (participadas y clientes) al Nivel 1.
2. **C-04**: mover la hoja R2 (conservando su ID) desde `Revisiones sustituidas…/AMZN` a `Análisis/AMZN` antes de cualquier promoción.
3. **C-01 y D-01** (mantenimiento de herramientas, con respaldo y regresión): rama K = 0 en `Option value` de la plantilla; `controles_supuestos.py` (`rstrip("N")`); `integridad_hojas.py` para candidatos.
4. Crear la hoja de auditoría independiente en Drive (REGLAS §11) importando `inventario_entradas_R2.csv` y la tabla §15. Necesita permiso para escribir en Drive.
5. Publicar el informe en `auditorias/narrativas/AMZN.md` **solo** con autorización expresa.

## Para la fase siguiente

Leer: [`AUDITORIA_ECONOMICA_AMZN_R2.md`](AUDITORIA_ECONOMICA_AMZN_R2.md) §15 (lista de cambios) y §13 (efectos), `auditoria_fase4/alternativas*.json`, `auditoria_fase4/scripts/` (para reproducir: `captura.py` → `dcf.py`/`blocks.py` → `alt.py`, `alt2.py`; `run_oficial.py <script> AMZN` redirige los controles oficiales a la hoja R2) y `SHA256_evidencia_externa.txt`. Insumos externos: 10-Q del T3-26, `ERPNov26.xlsx` y Treasury del 30-oct-2026 (URLs en §18).
