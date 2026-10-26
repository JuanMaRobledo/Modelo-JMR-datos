# Recuperación del conjunto de 38 valoraciones (estado del 20-oct-2026)

**Origen:** commit `f5bde54` de este repositorio (20-oct-2026 16:24 −05:00), el último estado completo antes de que el
21-oct se vaciaran las valoraciones, los análisis y las auditorías. Es también el estado del cierre
`auditorias/cierre-valoraciones-2026-10-19.json` (38 empresas, 21 matrices por empresa, MOS 35 % sobre la Base en 36 de
38; las 2 restantes con MOS 25 %).

## Qué se restauró

| Dónde | Qué |
|---|---|
| `valoraciones/` | 34 registros del snapshot (todos menos NFLX, NKE, NVDA y META) más los 4 vigentes actuales: **38 archivos**. |
| `analisis/` | 34 análisis completos del snapshot más los 4 vigentes actuales: **38 archivos**. |
| `auditorias/narrativas/PYPL.md` | Auditoría narrativa de PYPL (20-oct). |
| Este directorio | Versiones del 20-oct de NFLX, NKE, NVDA y META; los otros análisis del snapshot (PFDAVVNDA ya no usa el de 5,9 KB del 20-oct: se restauró el completo de 163 KB del 12-oct); el cierre y las auditorías del 14 al 19-oct; `colombia/` y `bitacora/` de ese día. |

NFLX, NKE, NVDA y META **conservan su revisión actual** (NFLX v7, NKE R6, NVDA R4, META R5) para no duplicar tickers en el
visor. Si prefieres las del 20-oct, están en `valoraciones/` y `analisis/` de este directorio.

## Qué se cambió respecto del snapshot

Solo se quitó el bloque `posicion` (acciones, costo promedio y fechas de compra) de 64 archivos: este repositorio es
público y su README excluye las posiciones de cartera. Los originales completos siguen en `f5bde54`. Para repetir o
revisar: `python3 scripts/quitar_posicion.py` (en seco) o `--aplicar`. `MANIFIESTO.json` trae el SHA-256 de cada archivo
antes y después.

## Controles ejecutados

- Los 38 `valoraciones/*.json` leen como JSON y pasan `validateRecord` de `scripts/auditar_integridad.cjs` (38 de 38).
- `scripts/validar_catalogo.cjs` **no** admite los 34 análisis restaurados: les falta `linkedValuation.sourcePath`
  (enlace análisis → valoración, regla posterior al 20-oct). `catalogo.json` no se tocó, así que sigue listando solo las
  4 revisiones actuales; los 34 restaurados salen como «no publicados» en el catálogo, aunque el visor lista por carpeta.
- No se ejecutó el visor ni se recalculó ninguna valoración.

## Límites que conviene tener presentes

- «Conciliado con salvedades» fue el estado de las 38; ninguna llegó a VERIFICADO (ver `REGLAS_VIGENTES.md`, registro v4).
- Desde el 21-oct cambiaron reglas que mueven cifras: crecimiento terminal 4 % (antes igual a la tasa libre),
  probabilidades por previa simétrica y prima por país al corte. Estos registros no las incorporan.
- Colombia (5 registros: GRUPOARGOS, GRUPOSURA, PFDAVVNDA, PFGRUPOARG, PFGRUPSURA) se restauró, pero el 21-oct se pidió
  pausar ese frente.
