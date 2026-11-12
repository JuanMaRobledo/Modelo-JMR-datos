# ORCL-FLOYD-FY26Q1FY27-R1 · Entrega R5 (candidato NO publicado)

- **Ticker / revisión:** ORCL · ORCL-FLOYD-FY26Q1FY27-R1 · corte contable 2026-08-31 · precio 117,98 (2026-11-10) · fecha 2026-11-12.
- **Agente:** Claude Code (sesión del 12-nov-2026). Revisión interna; no es auditoría R6.
- **Libro único:** `18XcbMlHfKMC6E4I3MvudGm4B1Vv0ruUwmFkgYKMHZmc` · **Doc A:** `1OBla-wu5FcEgRfLriNPMQy_5-ItubT60Lg0IyXyRjN0`.
- **Decisión:** **NO publicada.** Regla del usuario (12-nov-2026): no se publican valoraciones con fallas críticas abiertas ni incompletas. Los JSON quedan en esta carpeta, fuera del catálogo. Candados del libro sin modificar: R2 `NO CERRADO`, `ESTADO PARA PUBLICAR = NO PUBLICAR`.
- **Valores (leídos del libro):** DCF Base 174,36 · Conservadora 47,96 · Optimista 215,97 · esperado 153,16 · precio con MOS 113,34 · múltiplos Base 151,41.

## Controles
| Control | Estado |
|---|---|
| Valor esperado y combinado de múltiplos reproducidos | APROBADO |
| Centros de las tres matrices DCF = Base vivo | APROBADO |
| DCF inverso por corridas reales, motor restaurado (Base 174,3641858) | APROBADO |
| Fórmulas de cinco hojas puente frente a la plantilla | APROBADO |
| `validar_profundidad_floyd.cjs`, `auditar_profundidad.cjs` | APROBADO |
| `validar_catalogo.cjs`, `auditar_integridad.cjs` | NO_APLICABLE_HOY: fallan desde antes para las cinco fichas vigentes porque no reconocen `floyd-libro-unico-v1` |
| Identidades de balance y flujo, motores frente al respaldo | NO_EJECUTADO el 12-nov |
| Dilución y caja posteriores al corte | PENDIENTE (requiere 10-Q de noviembre) |
| QA visual de la ficha en la app | NO_EJECUTADO |
| Auditoría económica independiente R6 | NO_EJECUTADO |

## Pendientes
Registrados en la pestaña «Asuntos por resolver» del libro (P-01 a P-13). Crítico abierto: P-01, emisión de noviembre no incorporada al DCF (Base 174,36 → 164,68–171,01 según la caja conservada).

## Siguiente paso exacto
Cargar el 10-Q del trimestre que cierra el 30-nov-2026, conciliar caja, deuda y acciones en `Puente EEFF!A81:G90` e incorporar el pro forma al motor; después, R6.
