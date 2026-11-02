import json, copy
from resolver import *   # reutiliza B, A, c3, wacc, run, dm, dtl
def ev_fy3(p):
    r=run(p); w=p['wacc']; f=r['fcff']
    # valor al cierre del año 3: FCFF años 4..10 + terminal, descontados con factores desde el año 3
    acc=1; pv=0
    for t in range(3,10): acc/=1+w[t]; pv+=f[t]*acc
    nopat_t=r['ops']  # no usado
    rev=[p['rev0']]; [rev.append(rev[-1]*(1+x)) for x in p['gr']]
    tv=(rev[-1]*(1+p['g'])*p['mg_t']*(1-p['tx_t'])*(1-p['g']/p['roic_t']))/(p['wacc_t']-p['g'])
    return pv+tv*acc
res={}
for nombre,p in (('R2_Base',B),('R3_central',c3)):
    ev3=ev_fy3(p); eq3=ev3-304461+114226+(p['nonop'])-26560.77
    res[nombre]=dict(EV_FY3=ev3,C_EV_EBITDA=ev3/265177.7062,C_P_OCF=eq3/131185.1233,C_PE=eq3/136888.8241)
print(json.dumps(res,indent=1))
pc=OUT['beta_bottom_up_alternativas']['EBIT_x_EV_EBIT_Software']
c7=A(c3,**wacc(0.0379,pc)); v=run(c7,'market')['ps']; print('R3 central con βu bottom-up Software/EBIT %.3f: %.2f (%+.2f%%)'%(pc,v,pct(v)))
for bu in (1.0,1.2,1.404):
    v=run(A(c3,**wacc(0.0379,bu)),'market')['ps']; print('βu',bu,round(v,2),round(pct(v),2))
OUT['ancla_C']=res; OUT['paquetes_R3']['7_R3 central con beta bottom-up EBIT×EV/EBIT Software (βu 1,054)']=dict(valor=run(c7,'market')['ps'],pct=pct(run(c7,'market')['ps']),mos35=run(c7,'market')['ps']*0.65)
json.dump(OUT,open('resolucion_R3.json','w'),indent=1,default=str)
