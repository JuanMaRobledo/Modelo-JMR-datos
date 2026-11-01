# Puerta técnica `controles_todas.sh` sobre META y NVDA · 1-nov-2026

META (`META-20261101-A12-R1`) y NVDA (`NVDA-20261101-A12-R1`) se promovieron a EN_REVISION con el CI de este
repositorio en verde, **sin ejecutar antes** la puerta técnica de `JMR-valuation/scripts/controles_todas.sh`
(paso 7 de `PROCESO_UNICO_JMR`). Ejecutada hoy (solo lectura): **sale con fallas**. Registro completo en
`evidencia/puerta-tecnica-20261101/controles_todas_META_NVDA.log`.

| Control | META | NVDA | Naturaleza |
|---|---|---|---|
| Candados (15) | 15/15 listos | 15/15 listos | OK |
| Entradas esenciales | 1 vacía: `Cost of capital worksheet!B49` (acciones preferentes) | 5 vacías: `Input sheet!B39:B42` (opciones) | Falso positivo probable en NVDA (`B38 = No`, sin opciones); META: confirmar 0 preferentes |
| Integridad | `Input sheet!B12:C16`, `R& D converter`, beta `B24` y `g` terminal `J5:J8` escritos como número, no enlazados a estados | ídem | **Desvío real del flujo**: los datos base se tomaron del 10-Q a mano (documentado en `CIERRE_GATES_META_NVDA_20261101.md`), no como enlace + ajuste con nota |
| Estados completos | 11 filas vacías en los últimos 5 años + LTM | 11 filas vacías | **Desvío real**: historia parcial; `completar_historia.py` no puede rellenarlas (filas sin años comunes para validar) |
| `Cost of capital worksheet!B73` | `#N/A` | `#N/A` | Defecto de plantilla (Enfoque 3 no usado, VLOOKUP sobre selector vacío); también en CELH. Corrección = mantenimiento de la maestra con autorización |
| Probabilidades / supuestos | sin ficha `reference/damodaran/<T>.json` | ídem | Herramienta no adaptada a revisiones A-1.2 creadas fuera de `damodaran_stories.py` |
| Consistencia hoja=app=motor | `KeyError: 'dcfBase'` | ídem | Herramienta espera el esquema anterior del registro |

**Conclusión:** el DCF publicado sale de la hoja (B35) y los candados están listos, pero META y NVDA **no
cumplen** la integridad de datos que exige la puerta: la `Input sheet` no está enlazada a estados completos.
No se cambió ningún valor. Cerrarlo exige una revisión de actualización de cada una (importación SEC completa en
copia, enlaces + ajustes con nota y nueva captura), no un parche. Mientras tanto siguen EN_REVISION con esta
salvedad registrada; la decisión de mantenerlas o pasarlas a CANDIDATO es del usuario.
