"""Sensibilidad económica de MELI a 6-nov-2026, fuera del DCF oficial Floyd."""
import json
import math
from dataclasses import dataclass, replace

COMMERCE, FINTECH = 21749, 16774
VENTAS = COMMERCE + FINTECH
ACCIONES = 50.696802
PRECIO, KE, G = 1510, .125, .035
IMPUESTO, CARGA_NO_OPERATIVA = .27, (2859-2570)/VENTAS

@dataclass(frozen=True)
class Historia:
    commerce: tuple
    fintech: tuple
    ebit1: float
    ebit7: float
    retencion1: float
    roe_terminal: float

CASOS = {
    'Conservador': Historia((.23,.18,.14,.11,.09),(.20,.17,.14,.11,.09),.063,.08,.55,.12),
    'Central': Historia((.28,.24,.20,.17,.14),(.26,.22,.19,.16,.13),.07,.115,.45,.15),
    'Optimista': Historia((.35,.30,.26,.22,.18),(.34,.28,.24,.21,.17),.08,.145,.35,.18),
}

def trayectoria(primeros, g):
    return primeros + tuple(primeros[-1]+(g-primeros[-1])*i/5 for i in range(1,6)) + (g,)

def calcula(h, ke=KE, g=G):
    assert 0 < g < min(ke, h.roe_terminal)
    commerce, fintech = COMMERCE, FINTECH
    ventas = [VENTAS]
    for gc, gf in zip(trayectoria(h.commerce,g),trayectoria(h.fintech,g)):
        commerce *= 1+gc
        fintech *= 1+gf
        ventas.append(commerce+fintech)
    tasas = [actual/anterior-1 for anterior,actual in zip(ventas,ventas[1:])]
    retencion_terminal = g/h.roe_terminal
    pendiente = (h.retencion1-retencion_terminal)/(tasas[1]-g)
    filas = []
    for i, ingresos in enumerate(ventas[1:11],1):
        margen_ebit = h.ebit1+(h.ebit7-h.ebit1)*min((i-1)/6,1)
        margen_neto = (margen_ebit-CARGA_NO_OPERATIVA)*(1-IMPUESTO)
        utilidad = ingresos*margen_neto
        retencion = retencion_terminal + pendiente*(tasas[i]-g)
        assert 0 <= retencion < 1
        flujo = utilidad*(1-retencion)
        vp = flujo/(1+ke)**i
        filas.append(dict(anio=i, crecimiento=tasas[i-1], ventas=ingresos,
                          margen_ebit=margen_ebit, margen_neto=margen_neto,
                          retencion=retencion, utilidad=utilidad, flujo=flujo, vp=vp))
    flujo_terminal = ventas[11]*filas[-1]['margen_neto']*(1-retencion_terminal)
    vp_terminal = flujo_terminal/(ke-g)/(1+ke)**10
    patrimonio = sum(r['vp'] for r in filas)+vp_terminal
    assert math.isclose(filas[0]['retencion'],h.retencion1)
    assert math.isclose(filas[-1]['retencion'],retencion_terminal)
    return dict(valor=patrimonio/ACCIONES, terminal=vp_terminal/patrimonio,
                cagr5=(ventas[5]/VENTAS)**.2-1, filas=filas)

def salida():
    central = CASOS['Central']
    casos = {k:calcula(h) for k,h in CASOS.items()}
    assert casos['Conservador']['valor'] < casos['Central']['valor'] < casos['Optimista']['valor']
    lo, hi = .08, .30
    for _ in range(55):
        m = (lo+hi)/2
        if calcula(replace(central,ebit7=m))['valor'] < PRECIO:
            lo = m
        else:
            hi = m
    inverso = (lo+hi)/2
    assert abs(calcula(replace(central,ebit7=inverso))['valor']-PRECIO) < 1e-6
    g_values = [.025,.03,.035,.04,.045]
    ke_values = [.105,.115,.125,.135,.145]
    roe_values = [.11,.13,.15,.17,.19]
    margins = [.095,.105,.115,.125,.135]
    offsets = [-.04,-.02,0,.02,.04]
    matrices = {
        'Ke × g': (ke_values,g_values,[[calcula(central,ke=k,g=g)['valor'] for g in g_values] for k in ke_values]),
        'ROE terminal × g': (roe_values,g_values,[[calcula(replace(central,roe_terminal=r),g=g)['valor'] for g in g_values] for r in roe_values]),
        'Ajuste al crecimiento de ambos negocios × margen EBIT objetivo': (
            offsets,margins,[[calcula(replace(central,commerce=tuple(g+x for g in central.commerce),
                                             fintech=tuple(g+x for g in central.fintech),ebit7=m))['valor']
                              for m in margins] for x in offsets])
    }
    assert all(math.isclose(m[2][2][2],casos['Central']['valor']) for m in matrices.values())
    caja = {str(r):calcula(replace(central,retencion1=r))['valor'] for r in (.35,.45,.55)}
    return dict(casos=casos,inverso_ebit=inverso,inverso_neto=(inverso-CARGA_NO_OPERATIVA)*(1-IMPUESTO),
                matrices=matrices,sensibilidad_retencion=caja)

if __name__ == '__main__':
    print(json.dumps(salida(),ensure_ascii=False))
