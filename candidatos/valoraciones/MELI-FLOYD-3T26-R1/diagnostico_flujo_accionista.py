"""Prueba de expectativas de MELI a 6-nov-2026. No es un DCF oficial Floyd."""
import json
from pathlib import Path

VENTAS, ACCIONES, PRECIO = 38523, 50.696802, 1510
MARGEN_0 = 1890 / VENTAS
KE, G = .125, .035
CASOS = {
    'Conservadora': dict(tasas=[.22,.17,.14,.11,.09], margen=.055, caja0=.50, caja10=.70, roe=.11),
    'Base de diagnóstico': dict(tasas=[.30,.25,.21,.18,.15], margen=.09, caja0=.62, caja10=.80, roe=.15),
    'Optimista': dict(tasas=[.36,.30,.25,.22,.19], margen=.115, caja0=.72, caja10=.86, roe=.19),
}
def valora(tasas, margen, caja0, caja10, roe, ke=KE, g=G):
    assert 0 < g < min(ke, roe)
    ventas = VENTAS
    filas = []
    curva = tasas + [tasas[-1]+(g-tasas[-1])*i/5 for i in range(1,6)]
    for t, crecimiento in enumerate(curva,1):
        ventas *= 1+crecimiento
        mt = MARGEN_0+(margen-MARGEN_0)*min(1,t/7)
        resultado = ventas * mt
        conversion = caja0 + (caja10-caja0)*(t-1)/9
        flujo = resultado * conversion
        vp = flujo/(1+ke)**t
        filas.append([t,crecimiento,ventas,mt,resultado,conversion,resultado-flujo,flujo,vp])
    flujo_terminal = ventas*(1+g)*margen*(1-g/roe)
    vp_terminal = flujo_terminal/(ke-g)/(1+ke)**10
    valor = (sum(f[-1] for f in filas)+vp_terminal)/ACCIONES
    return valor, vp_terminal/(valor*ACCIONES), filas

base = CASOS['Base de diagnóstico']
casos = {k:valora(**v) for k,v in CASOS.items()}
assert casos['Conservadora'][0] < casos['Base de diagnóstico'][0] < casos['Optimista'][0]
lo,hi=.01,.30
for _ in range(65):
    m=(lo+hi)/2
    if valora(**(base|{'margen':m}))[0] < PRECIO:
        lo=m
    else:
        hi=m
inverso=(lo+hi)/2
assert abs(valora(**(base|{'margen':inverso}))[0]-PRECIO)<1e-6
g_grid=[.025,.030,.035,.04,.045]
ke_grid=[.105,.115,.125,.135,.145]
roe_grid=[.11,.13,.15,.17,.19]
margins=[.07,.08,.09,.10,.11]
offset=[-.04,-.02,0,.02,.04]
matrices = {
 'Ke × g': (ke_grid,g_grid,[[valora(**base,ke=k,g=g)[0] for g in g_grid] for k in ke_grid]),
 'ROE terminal × g': (roe_grid,g_grid,[[valora(**(base|{'roe':roe}),g=g)[0] for g in g_grid] for roe in roe_grid]),
 'Ajuste al crecimiento 1–5 × margen neto objetivo': (offset,margins,[[valora(**(base|{'tasas':[v+x for v in base['tasas']],'margen':m}))[0] for m in margins] for x in offset])
}
assert all(abs(m[2][2][2]-casos['Base de diagnóstico'][0])<1e-8 for m in matrices.values())
data=dict(casos=casos, inverso=inverso, matrices=matrices)
if __name__ == '__main__':
    print(json.dumps(data, ensure_ascii=False))
