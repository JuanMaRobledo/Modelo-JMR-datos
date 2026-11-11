# Etapa 0 · Inventario, cronología y archivo — ENTREGA

**Estado: PARCIAL** · 2026-11-11 · rama `ccr-72d28f93-tn5jri` · mantenimiento estructural, sin cambios en valoraciones, plantillas oficiales, producción ni fórmulas.

## Qué se hizo (efectuado vs. escrito)
| Ítem | Tipo | Evidencia |
|---|---|---|
| Lectura de contrato, órdenes y plantillas | leído | `CONTRATO_REBOOT_JMR.md`, `ordenes-reboot.md`; `REGLAS_VIGENTES.md §0R` (v37 en el repo; el contrato cita v38 en su tabla: **discrepancia documental menor**) |
| Índice Maestro Drive (665 filas, orden por última modificación desc.) | efectuado | `etapa0/indice_drive.csv/.json` |
| Índice de repos (3 294 archivos, último commit real por archivo) | efectuado | `etapa0/indice_repos.csv` (repos desplazados de *shallow* a historial completo) |
| Cruce de dependencias (665 IDs de Drive × 3 repos) | efectuado | 300 IDs referenciados; columnas `refs_bloqueantes` / `refs_descriptivas` |
| Carpeta `90 Archivo histórico` + 18 traslados | **efectuado en Drive** | `etapa0/MOVIMIENTOS_DRIVE_EJECUTADOS.json` |

## Metadatos y cronología
- Fuente: Google Drive API. `ultima_modificacion_original_utc` = `modifiedTime` (UTC); `creado_utc` = `createdTime`. Los traslados **no alteraron** `modifiedTime` (comprobado archivo a archivo en la respuesta de la API). La fecha de archivo (2026-11-11) se registra aparte.
- GitHub: la fecha es el `committer date` ISO del último commit que tocó el archivo (no la fecha de copia ni de Drive).
- Zona horaria: UTC en Drive; los commits conservan su offset.

## Resultado de clasificación (Drive)
| Estado | Filas |
|---|---|
| VIGENTE | 76 (plantillas Floyd R1–R6; REBOOT de UBER, CMG, MELI, MSFT, AAPL; legados A‑1.2 aún referenciados por JSON/catálogo/código → NO_MOVER) |
| EN_PRUEBA | 6 (CELH‑REBOOT‑3T26‑R1: sin JSON publicado) |
| ARCHIVADO | 103 (85 ya archivados antes + 18 trasladados hoy) |
| ARCHIVADO_PROPUESTO | 10 (ver riesgos) |
| PENDIENTE_DE_CLASIFICAR | 470 (A‑1.2/Atlas/manuales/PNG/MD sin referencia; una fecha antigua no implica obsolescencia) |

Una sola fecha antigua **no** archivó nada. Criterio de traslado: versión Floyd F1–F5 de una empresa cuyo reemplazo REBOOT ya tiene JSON en `valoraciones/`, **sin referencias bloqueantes** (JSON, catálogo, app, scripts). Un traslado en Drive conserva ID y URL, por lo que ningún enlace se rompe. Reversión: mover cada ID a `carpeta_origen_id` del manifiesto.

### 18 trasladados a `90 Archivo histórico` (`1W-kuAg4Fd4NwGleefGp2Y1A0eq1my1Vn`)
AAPL‑FLOYD H1/H2/H3 (3) · MELI‑FLOYD SOTP, FINTECH, COMMERCE, Análisis, Control de fases, Históricos SEC (6) · CMG Floyd 3T‑2026 Históricos/Modelo/Análisis (3) · UBER Floyd 3T‑2026 Históricos/Modelo/Análisis/Respaldo/Auditoría F5 (5) · Plantilla candidata Simple Ginzu+Segmentos 2026‑11‑08 (1).
Cada fila conserva su última modificación original en el manifiesto.

## Jerarquía propuesta (sin duplicar)
Existentes: `Plantillas Modelo JMR Floyd (R1–R6)` (≈ 01 Floyd vigente), `Análisis/<TICKER>`, `Originales de Damodaran`, `Plantillas … archivo-v1 (F1–F5)`. Se añadió solo `90 Archivo histórico`. **No** se renombraron ni movieron carpetas existentes (varias están referenciadas por scripts y/o son de solo lectura para esta cuenta); `02 Pruebas y desarrollo` se creará en la Etapa 3 junto a las copias aisladas de UBER.

## Riesgos y pendientes
1. **No movidos**: CELH‑FLOYD‑20261108 (3 archivos) porque su reemplazo CELH‑REBOOT aún no está publicado; plantillas Atlas / Holding Financiero / «Plantilla Maestra Atlas» (posible insumo para excepción FCFE/SOTP y para el origen de M) → pendientes.
2. 470 filas PENDIENTE_DE_CLASIFICAR requieren revisión humana o regla adicional; no se infirió obsolescencia por fecha.
3. Cobertura Drive: búsqueda por título «JMR» desde 2026‑09‑01 más carpetas de empresa; archivos sin «JMR» en el título y anteriores a septiembre pueden faltar.
4. UBER legado Floyd tenía ediciones hasta 8‑nov; la candidata activa sigue siendo `UBER-REBOOT-3T26-R1` (EN_REVISION, estado confirmado en el JSON, no verificado en la app desplegada).
5. Las entregas `candidatos/…FLOYD…/FASE_*.md` citan URL archivadas: siguen válidas (mismos IDs).

## Siguiente paso
Etapa 1: auditoría funcional de plantillas y los seis artefactos UBER (diagnóstico sin cambios).
