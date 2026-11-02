import copy, json
from blocks import block; from dcf import run
from alt import wacc_path, B, base
def mpath(m1,target): return [m1]+[target-(target-m1)*(10-k)/10 for k in range(2,11)]
assert max(abs(a-b) for a,b in zip(mpath(B['mg'][0],0.17),B['mg']))<1e-12
def ps(p,mode='native'): return run(p,mode)['ps']
def A(**kw):
    p=copy.deepcopy(B); p.update(kw); return p
out={}
def rec(n,v): out[n]=dict(ps=v,pct=100*(v-base)/base); print(f'{n:55s} {v:8.2f} {100*(v-base)/base:+7.2f}%')
for t in (0.15,0.16,0.18,0.19): rec(f'margen_obj_{t:.2f}', ps(A(mg=mpath(B['mg'][0],t),mg_t=t)))
# Arrendamientos (a): EBIT + interés implícito del pasivo operativo (100,288 × Kd 5,34%) como % de ventas, constante
add=100288*0.0534/797455
rec('arriendos_EBIT_ajustado_Damodaran', ps(A(mg=[m+add for m in B['mg']], mg_t=B['mg_t']+add)))
# Combinaciones
intl=0.049057867221630184-0.0455
pth,term,_,_=wacc_path(0.0494,0.0379+intl,0.0379)
fav=A(wacc=pth,wacc_t=term,debt=B['debt']-100288)
rec('ERP_nov_3.79 + arriendos', ps(fav))
rec('ERP_nov_3.79 + arriendos + DTL_57.4 + RSU_mercado', ps(A(wacc=pth,wacc_t=term,debt=B['debt']-100288,nonop=B['nonop']-57400),'market'))
pth2,term2,_,_=wacc_path(0.0494,0.0441+intl,0.0441)
rec('ERP_nov_4.41 + arriendos + DTL_57.4 + RSU_mercado', ps(A(wacc=pth2,wacc_t=term2,debt=B['debt']-100288,nonop=B['nonop']-57400),'market'))
rec('adverso_conjunto: DTL57.4+RSU_mercado+beta_Software', None or 0) if False else None
bu_sw=1.0512304
pth3,term3,_,_=wacc_path(0.0494,0.049057867221630184,0.0455,bu_sw)
rec('adverso_conjunto: DTL57.4 + RSU_mercado + beta_AWS_Software', ps(A(wacc=pth3,wacc_t=term3,nonop=B['nonop']-57400),'market'))
rec('adverso_solo_errores_dato: DTL57.4 + RSU_mercado', ps(A(nonop=B['nonop']-57400),'market'))
# DCF inverso por margen objetivo (crecimiento Base) — bisección
def inv(fn,lo,hi,target=240.35):
    for _ in range(200):
        mid=(lo+hi)/2
        if fn(mid)<target: lo=mid
        else: hi=mid
    return mid
mi=inv(lambda t: ps(A(mg=mpath(B['mg'][0],t),mg_t=t)),0.10,0.40); print('margen objetivo implícito (resto Base):',mi)
mi2=inv(lambda t: ps(A(wacc=pth,wacc_t=term,debt=B['debt']-100288,mg=mpath(B['mg'][0],t),mg_t=t)),0.10,0.40); print('margen implícito con ERP nov + arriendos:',mi2)
out['margen_implicito']=mi; out['margen_implicito_ERPnov_arriendos']=mi2
json.dump(out,open('alternativas2.json','w'),indent=1)
