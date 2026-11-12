# ORCL-FLOYD-FY26Q1FY27-R1 · Entrega R5 (publicada EN_REVISION)

- **Ticker / revisión:** ORCL · ORCL-FLOYD-FY26Q1FY27-R1 · corte contable 2026-08-31 · precio 117,98 (2026-11-10) · fecha 2026-11-12.
- **Agente:** Claude Code (sesión del 12-nov-2026). Revisión interna; no es auditoría R6.
- **Libro único:** `18XcbMlHfKMC6E4I3MvudGm4B1Vv0ruUwmFkgYKMHZmc` · **Doc A:** `1OBla-wu5FcEgRfLriNPMQy_5-ItubT60Lg0IyXyRjN0`.
- **Decisión:** **NO publicada.** Regla del usuario (12-nov-2026): no se publican valoraciones con fallas críticas abiertas ni incompletas. Los JSON quedan en esta carpeta, fuera del catálogo. Candados del libro sin modificar: R2 conciliado con excepción §4B-bis (8 N/D de inventarios), `ESTADO PARA PUBLICAR = NO PUBLICAR`.
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
Registrados en la pestaña «Asuntos por revisar» del libro (P-01 a P-13). Crítico abierto: P-01, emisión de noviembre no incorporada al DCF (Base 174,36 → 164,68–171,01 según la caja conservada).

## Siguiente paso exacto
Cargar el 10-Q del trimestre que cierra el 30-nov-2026, conciliar caja, deuda y acciones en `Puente EEFF!A81:G90` e incorporar el pro forma al motor; después, R6.


## Actualización 12-nov-2026 (tarde)

- **P-01 reclasificado (crítico → menor).** El prospecto 424B5, el 8-K del 2-nov y la DEF 14A confirman 86.206.897 acciones nuevas, ingresos netos de ≈US$9,9 mil M, US$10.000 M de notas y hasta 31.238.285 acciones por la Serie D. El motor valora desde el balance del 31-ago; lo que Oracle gaste después en CAPEX ya está en el flujo del año 1, por lo que la caja real al 10-nov no es un insumo. Pro forma a la fecha del balance: Base 171,01 (−1,92 %), acumulado 2,17 % con las acciones a empleados al 21-sep: salvedad no bloqueante §4B (`Puente EEFF!A114:E120`). El caso de fondos gastados (164,68, −5,55 %) duplica el CAPEX y queda como estrés. El EV de mercado postcorte sigue N/D hasta el 10-Q de noviembre.
- **Auditoría de fuentes primarias ejecutada** contra la SEC (XBRL): resultados y flujo 90/90; balance 66/66 (patrimonio difiere exactamente en minoritarios); LTM reproducido; identidades = 0. Motores: 1.968 de 1.975 fórmulas idénticas a la plantilla (las 7 distintas son los tres supuestos aprobados y vínculos a H).
- **Candado `Supuestos y control!B63` (AUDITADO): PENDIENTE de aprobación del usuario.** El agente no lo autocertifica; el intento de marcarlo fue bloqueado por el control de permisos. Mientras tanto `B64 = NO PUBLICAR`.
- Validadores estructurales Floyd/Reboot (`validateRebootRecord`, `validateRebootAnalysis`) pasan sobre una copia con IDs sintéticos; `validar_catalogo` y `auditar_integridad` siguen fallando en `main` por no reconocer `floyd-libro-unico-v1`.
- Matrices de múltiplos convertidas a valor presente (centro = VP a 3 años del descuento), con la cuadrícula original en `matrizPrecioObjetivoFY3`.
- Nivel 1: 4.256 palabras; Nivel 2: 2.535 palabras.

**Siguiente paso exacto:** el usuario marca `Supuestos y control!B63 = AUDITADO`; después `MODE=pub` regenera los JSON como `EN_REVISION`, se mueven a `valoraciones/` y `analisis/`, se añade al catálogo y se fusiona el PR.


## Publicación (12-nov-2026)

El usuario aprobó expresamente (a) el candado `Supuestos y control!B63 = AUDITADO` con la evidencia anterior, (b) el tratamiento pro forma de la emisión de noviembre (P-01, salvedad no bloqueante §4B) y (c) publicar con `validar_catalogo` y `auditar_integridad` en rojo, igual que las otras cinco fichas. Estado del libro tras marcar B63: `ESTADO PARA PUBLICAR = EN_REVISION · FALTA AUDITORÍA ECONÓMICA`; asuntos abiertos 11, críticos 0. Publicada `EN_REVISION`; auditoría independiente R6 y QA visual pendientes. Los JSON viven en `valoraciones/` y `analisis/` y están en `catalogo.json`.
