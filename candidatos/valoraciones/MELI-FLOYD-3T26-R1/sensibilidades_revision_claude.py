"""Reproduce las sensibilidades de REVISION_CLAUDE_20261108.md.
Requiere `revision_supuestos.py` del PR #260 en el mismo directorio.
Uso: python3 -I sensibilidades_revision_claude.py"""
import sys; sys.path.insert(0, '.')
import revision_supuestos as r
h = r.CASOS['Central']; base = r.calcula(h); filas = base['filas']; N = r.ACCIONES
vp10 = sum(f['vp'] for f in filas)
def val(ke_t, g=.035, medio_anio=False):
    ft = filas[-1]['ventas']*(1+g)*filas[-1]['margen_neto']*(1-g/h.roe_terminal)
    tv = ft/(ke_t-g)/(1+r.KE)**10
    return (vp10+tv)*((1+r.KE)**.5 if medio_anio else 1)/N
print('base', round(val(.125), 1), '| medio año', round(val(.125, medio_anio=True), 1))
for kt in (.11, .10, .097):
    print('Ke terminal', kt, 'g3,5%', round(val(kt)), 'g4%', round(val(kt, .04)))
print('retención', {k: round(v, 1) for k, v in r.salida()['sensibilidad_retencion'].items()})
print('ROE implícito año1', round(base['filas'][0]['crecimiento']/base['filas'][0]['retencion'], 3))
