> **Superado si se adopta el libro único** (`etapa2b/LIBRO_UNICO.md`): en esa arquitectura no hay sincronización entre libros. Vigente solo para las revisiones heredadas de seis libros.

# Plan de aplicación de los vínculos a los libros REALES de UBER (pendiente de aprobación)

**No ejecutado.** Solo se hizo lectura de producción (`configs/uber_real_solo_lectura.json`, `escribibles: []`: el ejecutor se niega a escribir). Evidencia: `etapa4/uber_real_solo_lectura/definicion.json`.

## Qué cambiaría en producción (medido en solo lectura)
| Tramo | Piezas | Cambia |
|---|---|---|
| H→D (B, C, O), H→M precio y estados, D‑C/D‑O→Resumen | 11·3 + 1 + 17 + 32 + 26 + 8 | **Nada** (idéntico a lo cargado) |
| D→M «Entradas desde DCF» (×3) y M→Resumen `D32` | 1 celda por vínculo | **Ke: 0,1048752249 → 0,104875224898** (≈ 2·10⁻¹², redondeo de la carga manual) |
| Huellas (`Resumen!C10, E10, B33`) y fecha (`C11:E11`) | 4 celdas | Hash del JSON de valores → **huella de grupo** de los vínculos; fecha con sello `floyd_sync` |
| Controles D↔M | 18 | 18/18 CONSISTENTE |
Resultado esperado: **DCF 98,7383 / 45,2912 / 149,6689, MOS 64,18, esperado 98,11 y múltiplos sin cambio** (las dos cifras de Ke difieren por debajo de la precisión mostrada).

## Pasos (cada uno con criterio de parada)
1. **Aprobación explícita** de escribir en los 5 libros de `UBER-REBOOT-3T26-R1` y de que las celdas de huella se sustituyan.
2. **Respaldo en Drive**: copiar H, D‑B, D‑C, D‑O y M a `90 Archivo histórico/Respaldos/UBER-REBOOT-3T26-R1 · antes de floyd_sync` (ID y fecha originales quedan en los libros; el historial de versiones de Sheets se conserva).
3. **Instantánea**: `check` + lectura de las 4 cifras principales y de `Presentación`; guardar JSON.
4. Config `uber_real.json` con `escribibles` = los 5 IDs (revisada por el usuario).
5. `sync --dry-run` → debe listar solo los 4 vínculos de Ke como cambios.
6. `sync` (el ejecutor guarda **respaldo de destinos** `respaldo_<UTC>.json` antes de escribir) y `registrar_huellas`.
7. Verificación: las 4 cifras y `Presentación` idénticas a la instantánea (tolerancia 1e‑9), `check` = 13 FRESCO, 18/18 controles.
8. **Reversión** si algo no coincide: `revertir --respaldo respaldo_<UTC>.json` (probado en copias) y, si hiciera falta, restaurar el respaldo de Drive.
9. Congelar `manifiesto.json` en `Modelo-JMR-datos/candidatos/valoraciones/UBER-REBOOT-3T26-R1/` y registrar en `FASE_4_ENTREGA.md` (acción comprobada, SHA de huellas).

## Fuera de alcance de esta aplicación
`Presentación` nueva y control vivo de la matriz (cambios de plantilla; Etapa 7), JSON/catálogo/app, y cualquier cambio de supuestos.
