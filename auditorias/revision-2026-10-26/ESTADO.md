# Estado del trabajo y cómo retomarlo (26-oct-2026)

Rama de trabajo en los tres repositorios: `ccr-68242d45-bfmwvh` (nada se ha fusionado a `main`).

## Hecho
- 33 valoraciones y análisis del 20-oct restaurados (`LEEME.md` en `archivo/snapshot-2026-10-20-38-valoraciones/`), sin el bloque `posicion`.
- Prompts: 30-sep recuperados con adenda de sensibilidades solo en la Base; contrato de múltiplos, MOS y prompt de investigación alineados;
  `REGLAS_VIGENTES` **v11** (§11 hojas unificadas) y auditoría **v1.3** (porqué de cada supuesto y fuente de todos los datos).
- Auditoría de registro de las 33 (`RESUMEN.md`), contraste con la SEC (`SEC.md`), profundidad del análisis (`PROFUNDIDAD.md`).
- Scripts: `auditar_registro.py`, `contrastar_sec.py`, `auditar_profundidad.py` (este repo) y `unificacion_hojas.py` (JMR-valuation).

## Bloqueos conocidos
- La credencial de Google de este entorno **no puede leer las hojas de las 29 empresas antiguas** (archivadas el 24-oct); solo lee las
  plantillas y las hojas vigentes de NFLX, NKE, NVDA y META. Para unificarlas hay que crear una copia nueva de la maestra por empresa
  (`scripts/reset_from_master.py --new "Modelo JMR - <T>"`), llenar datos crudos (`refresh_native_model.py`, SEC) y fichas de supuestos
  (`reference/damodaran/<T>.json`), y regenerar (`bash scripts/valorar.sh <T> <ID_COPIA>`).
- Cuota de Sheets (60 lecturas por minuto): `unificacion_hojas.py` tarda unos 20 minutos por hoja la primera vez.
- Financial Datasets sin créditos; la SEC sí responde.

## Cola, en este orden
1. Terminar `unificacion_hojas.py` sobre NFLX, NVDA, NKE y META (informes en `/tmp` del entorno; repetir si se perdieron):
   `cd JMR-valuation && PYTHONPATH=.:scripts python3 scripts/unificacion_hojas.py --copy-id <ID> --salida auditorias/.../unificacion/<T>.json`.
   Hojas: NFLX `1ZPNMHxc7m3Iv60mdGspgi6-cc2zwf5kZ4ocsuANQUNM`; los otros IDs están en `hojaGoogle` de cada registro vigente.
   Hallazgo previo: NKE y META tienen 7 pestañas añadidas y NVDA 2 (formato no unificado).
2. PYPL: fijar la base de ingresos en LTM a 2T26 (hoy usa FY2025) y revisar los 8-K/6-K posteriores (`SEC.md`).
3. Corregir hallazgos de regla por empresa (`RESUMEN.md`): pesos de múltiplos con razón económica por método, probabilidades simétricas,
   g terminal 4 %, MOS 35 % (AAPL y otra con 25 %), enlace análisis→valoración.
4. Análisis incompletos (`PROFUNDIDAD.md`): CMG (faltan secciones), PYPL, ADBE, GRUPOARGOS y PFGRUPOARG son los más cortos.
5. Hoja nueva unificada por empresa, de la que más pesa en la cartera a la que menos; en cada una: datos crudos con fuente → supuestos con
   su porqué → `controles_todas.sh` (con `UNIFICACION=1`) → auditoría v1.3.
6. Contrastar a mano las que la SEC no cubre: P911, ONON, NU, PAGS, y los trimestres de AFYA y NVO.

## Resultado parcial · unificación de hojas (NFLX, 26-oct)
`unificacion/NFLX.json`: 61 de 61 pestañas, mismo orden; **122 de 122 selectores conservados**; de 21.265 fórmulas de la maestra, 336 perdidas y 233 editadas.
Todas las perdidas y 175 de las editadas están en «Sensibilidad por múltiplo» (la hoja tiene 9 columnas frente a 17: es el cambio deliberado a matrices solo
Base). Las otras 58 ediciones están en `Financials Multiples` (12) y en las pestañas de método `POCF`, `PE`, `PFCFE`, `PV`, `PBV` (9 cada una) y
`Resumen de Valoración` (1): las copias referencian celdas propias donde la maestra referencia otras. Decidir si la maestra adopta esos cambios (entonces se
actualiza la plantilla) o si la hoja de NFLX vuelve a la fórmula de la maestra (REGLAS §5A: no reconstruir fórmulas por empresa).
NKE, NVDA y META siguen en la cola de `unificacion_hojas.py` (tarda ~20 min por hoja); NKE y META tienen 7 pestañas añadidas y NVDA 2.

## Resultado completo · unificación de las 4 hojas accesibles (26-oct)
Informes en `unificacion/<T>.json`. **Selectores: 122 de 122 conservados en las cuatro** (NFLX, NVDA, NKE, META). Ninguna hoja está unificada:

| Hoja | Pestañas añadidas | Fórmulas de la maestra perdidas (de 21.265) | Editadas | Dónde |
|---|---:|---:|---:|---|
| NFLX | 0 | 336 | 233 | Sensibilidad por múltiplo (Base 9 columnas), métodos y Financials Multiples |
| NVDA | 2 | 6.436 | 8.594 | Motor sensibilidad DCF; Trailing Valuation; Income Statement |
| NKE | 7 | 4.069 | 11.227 | Motor sensibilidad DCF; Income Statement; Financials Multiples |
| META | 7 | 110 | 2.499 | Motor sensibilidad DCF; Financials Multiples; Income Statement |

Las pestañas añadidas **no se pueden borrar**: 13 (NVDA), 24 (NKE) y 170 (META) fórmulas editadas las citan. Unificar estas hojas exige rehacerlas desde la maestra.

## Bloqueo decisivo: Drive
La cuenta de servicio `jmr-valuation-bot@jmr-valuation-508617.iam.gserviceaccount.com` **no puede crear archivos** (Drive responde `storageQuotaExceeded`) y **no tiene permiso sobre las hojas de las otras 29 empresas** (archivadas el 24-oct). Con autorización completa no se puede saltar eso; hace falta una de estas acciones de una persona con acceso a Drive:
- **A (recomendada):** para cada empresa, abrir la maestra (`1OYhz6ulMNNUAs-aW8q9FatOJgmfKAVTBAOmRMhqZzaY`) → Archivo → Hacer una copia, llamarla «Modelo JMR - <TICKER> - <fecha>», compartirla con el correo de la cuenta de servicio como Editor y pasar el ID. Con el ID se ejecuta `bash scripts/valorar.sh <T> <ID> "<pares>" "<industria>"`.
- **B:** compartir con la cuenta de servicio (Editor) las hojas antiguas de la carpeta «Valoraciones antiguas»; luego se reinician en el sitio con `reset_from_master.py --sheet-id ... --allow-destructive-reset` tras respaldar sus fórmulas en JSON.

## Actualización · carpeta compartida (26-oct, tarde)
Se compartió con la cuenta de servicio la carpeta **AAA Finanzas** (`1IS-H1WlSq71AWZXAE6r3LOhJXegSwLkz`). Ahora se ven sus 263 elementos
(documentos fuente, `.md` de valoraciones antiguas, plantillas y respaldos), pero **ninguna de las hojas de las 29 empresas antiguas**: los IDs
de `reference/multiplos_v3/*_anclas.json` y de `hojaGoogle` siguen dando `PermissionError` (existen, pero no están compartidas con la cuenta).
Las dos carpetas donde `REGLAS` §10 dice que están archivadas dan 404 para la cuenta:
- Valoraciones antiguas: `https://drive.google.com/drive/folders/10HZCGoZ4hKVqtg6ekcyYHsm8IHPZOBVLq`
- Revisiones sustituidas: `https://drive.google.com/drive/folders/1M2sWqAR60HBIBx0JbRn057kawpD9ZsZG`
Falta compartir esas dos carpetas (Editor) con `jmr-valuation-bot@jmr-valuation-508617.iam.gserviceaccount.com`. La cuenta sigue sin poder crear archivos
nuevos (cuota de Drive 0), así que la vía es reiniciar las hojas antiguas en el sitio (Opción B).
Nota de seguridad: dentro de AAA Finanzas hay un archivo `jmr-valuation-508617-64baa7fd0964.json` (parece la clave de la cuenta de servicio) y una carpeta `credentials`.

## PYPL · primera hoja unificada (26-oct, tarde)
`unificacion/PYPL.json`: **UNIFICADA** — 61 de 61 pestañas, 21.265 de 21.265 fórmulas de la maestra intactas, 122 de 122 selectores, 15 de 15 candados listos.
Hoja: `1LI1LHXYFiCqg5i1_DDzs53Rd4eKv4zhDex2pxSvKuCs` (reiniciada desde la maestra; respaldo en `JMR-valuation/reference/backups/unificar/`).
Receta que funcionó (por empresa), con los scripts de JMR-valuation:
1. `unificar_hoja.py --sheet-id ID --ticker T --confirmar-reinicio` (respaldo, pestañas, fórmulas y selectores de la maestra).
2. `desde_cero.sh datos T ID "<pares>" "<industria>"` (importa la SEC; la industria sale de la hoja publicada, no de la ficha: la de PYPL era un error).
3. `portar_entradas_respaldo.py --ticker T --sheet-id ID` y completar a mano los campos nuevos (Input filas 76 en adelante) con su fuente.
4. Corregir con el 10-Q más reciente lo que el importador deja viejo (balance LTM, deuda corriente, cambio neto en efectivo).
5. `unificacion_hojas.py` → `restaurar_formulas_maestra.py` → `unificacion_hojas.py`: **el importador y `build_story_sheet.py` pisan fórmulas de la maestra**
   (en PYPL: 192 perdidas y 913 editadas en Income Statement, Balance, Cash Flow, Trailing Valuation, Salud Financiera, Eficiencia de capital, Márgenes y Por acción);
   la restauración las devuelve y los totales se recalculan solos (activos 82.737, pasivos 62.917 y patrimonio 19.820 concilian con el 10-Q).
6. `candados.py T` = 15/15.
Resultado de la hoja (precio 52,53): Base 114,85 · Conservadora 83,44 · Disrupción 49,69 · Optimista 145,03 · promedio de tres historias 114,57
(la versión publicada del 15-oct daba 97,25 / 66,30 / 37,13 / 131,33: cambian el balance a jun-2026, la tasa libre, el impuesto normalizado y g terminal 4 %).
Pendiente de PYPL: sección 12, análisis completo y auditoría v1.3, y la publicación en la app (`valorar.sh PYPL ID --autorizar-publicacion`, que requiere tu autorización expresa).
Cola de las demás: igual receta, en orden de peso en cartera. Colombia queda en pausa.

## Motor alineado (26-oct, noche)
El motor JS (`docs/jmr_engine.js`) **no necesitó cambios**: con las entradas correctas reproduce las cuatro historias de la hoja de PYPL al decimal
(Base 105,1309 · Conservadora 67,0588 · Disrupción 47,9770 · Optimista 132,4000). Las diferencias anteriores venían de entradas heredadas y de pasos que pisaban la maestra:
- `Input sheet!B46 = Yes` (heredado) fijaba el costo de capital terminal igual al inicial (8,38 %); debe ser No (tasa libre + prima madura = 8,99 %).
- Faltaba el ROIC terminal por historia (`Escenarios e historias!N6:N7`, igual al costo de capital terminal en Conservadora y Disrupción).
- `Resumen de Valoración!C25`, `Input!B23` y otros se escribían como valores; el precio vive solo en `Input sheet!D1`.
- La maestra del 22-oct exige ceros explícitos (`Balance Sheet` filas 7 y 21, `Entradas históricas auxiliares` filas 3 a 5) para calcular totales, TEV y medianas de múltiplos.
`valorar.sh` ahora ejecuta `restaurar_formulas_maestra.py --auto` (paso 2d) antes de los controles. Resultado en PYPL: UNIFICADA (informe `unificacion/PYPL.json`),
15/15 candados, `controles_todas.sh`: sin fallas. Valores (precio 52,53): Base 105,13 · Conservadora 67,06 · Disrupción 47,98 · Optimista 132,40.
Aviso para las demás: la receta de arriba incluye ahora el paso «ceros explícitos» y la revisión de `B46`; la industria sale de la hoja publicada, no de la ficha.

## PYPL · análisis, auditoría y múltiplos (26-oct, noche)
- **Hallazgo:** la hoja unificada de PYPL tenía los múltiplos vacíos (solo DCF). Se aplicaron con la regla por ciclo (`apply_multiples_v3.py`, decisión `PYPL_decision_ciclo.json`), y P/V y P/BV con el nuevo `scripts/multiples_pv_pbv.py` (la maestra los exige siempre). Consolidados hoy: 43,91 / 72,20 / 101,12; brecha de la Base con el DCF −31 % (H-10). Se limpiaron 36 valores residuales de `Financials Multiples` (respaldo en `JMR-valuation/reference/backups/`). `controles_todas.sh PYPL`: sin fallas; 15/15 candados; 0 fórmulas por restaurar.
- **Entregables (borradores, sin publicar):** `JMR-valuation/data/PYPL_Research_Fundamental_Modelo_JMR_2026-10-26.md` (18 secciones), `PYPL_Nivel2_Datos_Modelo_JMR_2026-10-26.md` y la auditoría v1.3 en `PYPL-auditoria-v1.3.md` (esta carpeta). Dictamen: **Plausible con reservas** (H-01 ERP del resto del mundo y H-07 industria; agregado conservador 12 %, neto ≈ +3-4 %). Ruta de publicación prevista `auditorias/narrativas/PYPL.md`, solo con autorización.
- **Pendiente de PYPL:** publicar en la app (`valorar.sh PYPL ID --autorizar-publicacion`), escribir `justificacion_salto` de la Base (H-11), trazar opciones y desglose de ingresos por país (H-01, H-02).
- **Siguiente:** NVO (20-F; requiere aprobación explícita para reiniciar su hoja `1_w85o-Cv_4GzFB4nq5fGqrMSVoYf-Ltafuol3ir5TMw`), luego el resto en orden de peso en cartera.

## NVO · hoja rehecha, análisis, auditoría y publicación (26-oct, noche)

- Hoja `1_w85o-…` rehecha desde la maestra y UNIFICADA (61 pestañas, 21.258 fórmulas). Estados IFRS 2019-2025 + LTM ajustado (sin 340B ni deterioro 2T26) en US$ con FRED; I+D 2016-2018 de los 6-K.
- DCF: Base 45,43 · Conservadora 31,61 · Disrupción 20,17 · Optimista 57,57 · esperado 43,39 · MOS 29,53 · precio 37,91. Probabilidades 40/25/20/15 (etapa declive). ROIC terminal 11,1 %; ventas/capital 0,50.
- Múltiplos por ciclo (7 métodos) aplicados; consolidados 37,92 / 43,83 / 53,53.
- Publicado en la app (registro, análisis, sección Damodaran). Auditoría v1.3: `NVO-auditoria-v1.3.md` (Plausible con reservas; H-01…H-12).
- Pendientes: `refrescar_seccion` informa FALLOS 3 (chequeos legacy, como PYPL); regenerar la sección Damodaran de PYPL con el generador corregido (matriz centrada en la Base); verificar patentes en el 20-F (H-08).

## ADBE · hoja rehecha, análisis, auditoría y publicación (26-oct, noche)

- Hoja `1MhEO0NxlQ…` reiniciada (aprobación expresa) y UNIFICADA (61 pestañas). Estados SEC 2016-2025 + LTM al 28-ago-2026 (10-Q del 3T FY26); balance LTM reescrito; acciones 400,9 M (portada + RSU esperadas); I+D a 3 años; arrendamientos como deuda.
- DCF: Base 399,02 · Conservadora 250,15 · Disrupción 167,70 · Optimista 487,73 · esperado 385,65 · MOS 259,36 · precio 239,94. Probabilidades 50/20/20/10 (madura estable). ROIC terminal 29,3 %; ventas/capital 1,22.
- Múltiplos por ciclo (7 métodos); consolidados 204,57 / 222,71 / 359,24 (brecha de la Base −44 %).
- Publicado en la app (registro, análisis, sección Damodaran). Auditoría v1.3: `ADBE-auditoria-v1.3.md` (Plausible con reservas; H-01…H-13; H-06: capital nuevo rinde >2× el ROIC terminal en Conservadora y Disrupción).
- Pendiente: repetir `unificacion_hojas.py` tras la restauración posterior a la publicación; PSU en acciones; vencimientos y rating en el 10-K.

## MSFT · hoja rehecha, análisis, auditoría y publicación (26-oct, noche)
- Hoja `1wIgB2zfjmPk_DdnaFsoJfKHMiIR_p4795ebvbGSOi1E` reiniciada con la aprobación del usuario y unificada (61 pestañas, 21.258 fórmulas, 122 selectores; candados 15/15, inputs y estados completos sin hallazgos).
- Valores: Base 440,73 · Conservadora 257,57 · Disrupción 122,84 · Optimista 621,31 · esperado 440,09 · MOS 286,48 · precio 512,90. Probabilidades 45/22,5/22,5/10. Múltiplos consolidados 210,56 / 279,36 / 352,67 (el tope del múltiplo justificado deja la Base 37 % bajo el DCF).
- Correcciones de datos: depreciación y amortización redondeada del importador sustituida por la línea del flujo de caja (solo FY24-FY26 verificadas en el 10-K); arrendamientos financieros separados en FY25-FY26; selectores B71:B72 del costo de capital.
- Para unificar se eliminaron columnas sobrantes de «Tesis de Inversión y Supuestos» (10→8) y «Escenarios e historias» (21→14) sin respaldo previo (H-15).
- Auditoría v1.3: `MSFT-auditoria-v1.3.md` (con reservas; H-01…H-15; H-01 ROIC terminal, H-02 ventas/capital, H-03 arrendamientos firmados no iniciados por US$329.100 M).
- Pendiente: releer 10-K FY17-FY23 (D&A), deuda por arrendamientos financieros anterior a FY25, 10-Q del 1T FY27 (28-oct-2026).

## CELH · hoja rehecha, análisis, auditoría y publicación (26-oct, noche)
- Hoja `1tHDLsh4yBF9NQkRLNqfTU6GPM5trOWsB5xIjpALLOIw` reiniciada y unificada. Base 24,20 · Conservadora 16,58 · Disrupción 5,85 · Optimista 35,95 · esperado 25,23 · MOS 15,73 · precio 27,35.
- Preferentes de PepsiCo (mezzanine, 1.760) dentro del patrimonio; deducidas a valor de liquidación (1.135). EBIT normalizado con 441,6 de partidas de una vez.
- Publicado en la app (PR #156). Auditoría v1.3: `CELH-auditoria-v1.3.md` (H-01…H-13).

## DUOL · hoja rehecha, análisis, auditoría y publicación (26-oct, noche)
- Hoja `1Pbpv8PYFX6HIPJOQgtoLVDGgtPh08JMxbBkUQWyMVCc` reiniciada y unificada (61 pestañas, 21.258 fórmulas, 122 selectores; candados 15/15; inputs completos).
- Valores: Base 103,27 · Conservadora 76,38 · Disrupción 45,74 · Optimista 133,35 · esperado 104,11 · MOS 67,12 · precio 142,40. Probabilidades 40/22,5/15/22,5. Múltiplos consolidados 46,09 / 52,33 / 57,33 (brecha de la Base −49 %).
- Publicado en la app (PR #158). Auditoría v1.3: `DUOL-auditoria-v1.3.md` (H-01…H-13; H-01 capital nuevo rinde 39-54 % frente a ROIC terminal de 9 %; H-02 compensación en acciones).
- Pendiente: releer I+D semestral 1S22-1S25 contra el XBRL; calendario de arrendamientos con el 10-Q; estados de pares.

## Análisis recuperados (PR #157)
- Los 30 análisis fundamentales del 20-oct-2026 de los estudios aún no rehechos están de nuevo en `analisis/`, marcados «recuperado, pendiente de rehacer y auditar». Se reemplazan al publicar cada empresa.
