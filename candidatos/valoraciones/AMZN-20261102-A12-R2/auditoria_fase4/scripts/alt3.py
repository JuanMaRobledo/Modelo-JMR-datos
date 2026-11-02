import copy
from blocks import block; from dcf import run
from alt import wacc_path
B=block(2); base=run(B)['ps']
def mpath(m1,t): return [m1]+[t-(t-m1)*(10-k)/10 for k in range(2,11)]
def tpath(t1): return [t1]*5+[t1+(0.25-t1)*k/5 for k in range(1,6)]
def A(p0=B,**kw): p=copy.deepcopy(p0); p.update(kw); return p
def show(n,p,mode='native'):
    v=run(p,mode)['ps']; print(f'{n:62s} {v:8.2f} {100*(v-base)/base:+7.2f}%'); return v
# Construcción por segmentos del crecimiento (contraste)
aws,ret=161382,636073
for ga,gr in ((0.30,0.07),(0.35,0.08),(0.25,0.06)):
    a,r=aws,ret; path=[];
    for k,(x,y) in enumerate(zip([ga,ga-0.05,ga-0.10,ga-0.13,ga-0.15],[gr]*5)):
        a2,r2=a*(1+x),r*(1+y); path.append((a2+r2)/(a+r)-1); a,r=a2,r2
    print(f'AWS {ga:.0%} decreciente / comercio {gr:.0%}:', [f'{x:.1%}' for x in path], f'AWS en año 5 = {a/(a+r):.0%} de ventas')
print('Base:', [f'{x:.1%}' for x in B['gr'][:5]])
print('--- margen y1 por trimestre: Q4-25 11.7%, Q1-26 13.1%, Q2-26 13.7%, Q3-26 13.9%, guía Q4-26 punto medio', round(31/243.5*100,1),'%')
show('Margen año 1 = 14,1 % (tendencia), mismo 17 % en año 10', A(mg=mpath(0.141,0.17)))
show('Impuesto 10 % años 1-5 → 25 % año 10 (efectivo de caja)', A(tx=tpath(0.10)))
show('Impuesto 15 % años 1-5 → 25 % año 10', A(tx=tpath(0.15)))
show('Ventas/Capital 0,75 años 1-3 y 1,0 años 4-5 (ola de IA se normaliza)', A(sc=[0.75]*3+[1.0]*2+B['sc'][5:]))
intl=0.049057867221630184-0.0455
pth,term,_,_=wacc_path(0.0494,0.0379+intl,0.0379)
corr=A(wacc=pth,wacc_t=term,debt=B['debt']-100288,nonop=B['nonop']-57400)
v0=show('Solo correcciones A-01+A-02 con B-01 adverso y RSU a mercado', corr,'market')
d=A(corr,mg=mpath(0.141,0.17),tx=tpath(0.15),roic_t=0.136)
show('+ margen año 1 14,1 % + impuesto 15 % + ROIC terminal 13,6 %', d,'market')
o=A(d,mg=mpath(0.141,0.18),mg_t=0.18,sc=[0.75]*3+[1.0]*2+B['sc'][5:],roic_t=0.152)
show('+ margen 18 % + Ventas/Capital 1,0 años 4-5 + ROIC terminal 15,2 %', o,'market')
pth2,term2,_,_=wacc_path(0.0494,0.0441+intl,0.0441)
show('Igual que la anterior pero ERP pago sostenible 4,41 %', A(o,wacc=pth2,wacc_t=term2),'market')
# Cuánto margen terminal hace falta hoy para 240,35 con el paquete "d"
lo,hi=0.12,0.40
for _ in range(100):
    m=(lo+hi)/2; v=run(A(d,mg=mpath(0.141,m),mg_t=m),'market')['ps']; lo,hi=(m,hi) if v<240.35 else (lo,m)
print('margen terminal implícito con paquete corregido:', round(m*100,1),'%')
