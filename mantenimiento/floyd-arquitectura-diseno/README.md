# Mantenimiento estructural Floyd R1–R6 · arquitectura, automatización y diseño

Rama `ccr-72d28f93-tn5jri` (datos y JMR-valuation). Sin PR, sin fusiones, sin cambios en producción, plantillas oficiales ni valoraciones publicadas. No se creó otra versión de Floyd.

| Etapa | Estado | Entrega |
|---|---|---|
| 0 Inventario y archivo | PARCIAL | `ETAPA_0_ENTREGA.md`, `etapa0/` (665 filas Drive, 3 294 archivos de repos, 18 traslados reversibles) |
| 1 Auditoría funcional | PARCIAL | `ETAPA_1_ENTREGA.md` (9 hallazgos; corregido en Etapa 4) |
| 2 Arquitectura | PARCIAL | `ETAPA_2_ENTREGA.md`: se mantiene A (6 artefactos); B y C bloqueadas por prueba |
| 3 Prototipo y diseño | PARCIAL | `ETAPA_3_ENTREGA.md`, `etapa3/` (hoja verificada; app NO_EJECUTADO por acceso) |
| 4 Sincronización y recálculo | **APROBADO en copias** / pendiente de aplicar a libros reales | `ETAPA_4_ENTREGA.md` §5, `etapa4/VINCULOS_FLOYD.md`; código en `JMR-valuation/scripts/floyd_sync` (13/13 pruebas; 13 vínculos ejecutados en API real sobre copias de UBER) |
| 5 Flujo compartido | PARCIAL | `ETAPA_5_6_ENTREGA.md`, `scripts/validar_entregas_floyd.py` |
| 6 CI y prueba integral | PARCIAL / NO_EJECUTADO | `ETAPA_5_6_ENTREGA.md` |
| 7 Adopción y archivo definitivo | NO_EJECUTADO | requiere aprobación de decisiones abajo |

## Cambios efectuados fuera de Git (Drive)
- Creadas `90 Archivo histórico` (`1W-kuAg4Fd4NwGleefGp2Y1A0eq1my1Vn`) y `02 Pruebas y desarrollo` (`1OrleslgyCSLlQdzX0KshFnsiKC9kwC6x`).
- 18 archivos Floyd F1–F5 trasladados (ID, URL y fecha de modificación intactos; manifiesto con carpeta de origen en `etapa0/MOVIMIENTOS_DRIVE_EJECUTADOS.json`).
- Copias de prueba E4 (H, D‑O, M) en `02 Pruebas y desarrollo`; entradas de prueba restauradas.
- Copias de prueba en `02 Pruebas y desarrollo`: `PRUEBA E2 …DCF BASE` (contiene 2 hojas duplicadas de la prueba; **no usar**), `PRUEBA E2 …DCF CONSERVADORA`, `PROTOTIPO E3 …Presentación JMR`. Entradas de prueba restauradas y verificadas.
- Libros de producción (UBER y demás), plantillas R1–R6 y motor Damodaran: **sin modificar**.

## Decisiones y accesos que se necesitan del usuario
1. ~~Credencial de API de Sheets~~ **Recibida** (cuenta de servicio). Vínculos definidos y ejecutados en copias.
2. Sesión de solo lectura (o capturas) de la ficha de la app para QA desktop/móvil.
3. Unificar los tres `AGENTS.md`, fijar `main` como ref y añadir `GEMINI.md` (toca el contrato).
4. Elegir la paleta de `expediente.html` (índigo/pizarra actual) frente a los tokens JMR de `visor.html`.
5. Decidir el legado A‑1.2/Atlas/manual (470 filas PENDIENTE_DE_CLASIFICAR; 29 pruebas Python obsoletas; plantilla maestra `19PRUFiY…` vs `1OYhz6ul…`).
6. Aprobar llevar a la plantilla 02b: `Presentación` nueva, filas de metadatos en `Resumen` y control de sensibilidades vivo (Etapa 7, con PR separado y rollback).
