"""Auditoría fase 4 AMZN R2 — resolución cuantitativa de hallazgos (propuesta para R3, NO oficial).
Todo sale de la captura de la hoja R2, del 10-Q/10-K de la SEC, de Damodaran y de precios mensuales (Alpha Vantage).
No escribe en ninguna hoja."""
import copy, json, math, statistics as st
from blocks import block; from dcf import run
from alt import wacc_path
B=block(2); base=run(B)['ps']; OUT={}
def A(p0=B,**kw): p=copy.deepcopy(p0); p.update(kw); return p
def mpath(m1,t): return [m1]+[t-(t-m1)*(10-k)/10 for k in range(2,11)]
def tpath(t1): return [t1]*5+[t1+(0.25-t1)*k/5 for k in range(1,6)]
def pct(v): return 100*(v-base)/base
# ---------------- 1. Beta de regresión (60 meses, retornos mensuales ajustados, AMZN vs SPY) ----------------
amzn=[240.35,249.15,259.77,271.58,238.34,270.64,265.06,208.27,210.00,239.30,230.82,233.22,244.22,219.57,229.00,234.11,219.39,205.01,184.42,190.26,212.28,237.68,219.39,207.89,186.40,186.33,178.50,186.98,193.25,176.44,175.00,180.38,176.76,155.20,151.94,146.09,133.09,127.12,138.01,133.68,130.36,120.58,105.45,103.29,94.23,103.13,84.00,96.54,102.44,113.00,126.77,134.95,106.21,120.2095,124.2815,162.9975,153.5630,149.5735,166.7170,175.3535,168.6215,164.2520]
spy=[755.72,762.63,765.1526,745.1821,744.9227,752.69,715.0595,647.0818,680.6673,686.6009,676.6288,676.1072,674.7914,659.0806,636.4199,623.6235,609.5838,579.7864,545.5043,550.2753,582.7464,590.2394,574.8023,588.9970,555.8497,560.8546,549.3139,536.7719,530.3499,512.2744,487.6112,508.0975,491.9975,467.5951,460.2647,440.1657,403.3245,412.2744,432.7855,439.9353,425.9912,400.0616,398.2233,391.9617,377.9311,387.6783,364.7408,387.0240,366.6418,339.0827,373.6104,389.5029,356.6591,388.7162,387.8407,425.1563,409.7672,422.2302,445.7391,426.0166,429.4673,401.3100]
assert len(amzn)==len(spy)==62
ra=[amzn[i]/amzn[i+1]-1 for i in range(60)]; rm=[spy[i]/spy[i+1]-1 for i in range(60)]
ma,mm=st.mean(ra),st.mean(rm); cov=sum((a-ma)*(m-mm) for a,m in zip(ra,rm))/59; var=st.variance(rm)
beta=cov/var; alpha=ma-beta*mm; res=[a-alpha-beta*m for a,m in zip(ra,rm)]
se=math.sqrt(sum(e*e for e in res)/58/sum((m-mm)**2 for m in rm)); r2=1-sum(e*e for e in res)/sum((a-ma)**2 for a in ra)
DE=215026.2621/(10811*240.35); bu_reg=beta/(1+0.75*DE)
OUT['beta_regresion']=dict(meses=60,desde='2021-10',hasta='2026-10',beta=beta,error_estandar=se,r2=r2,ic95=[beta-1.96*se,beta+1.96*se],
      beta_blume=0.67*beta+0.33,beta_desapalancada_equivalente=bu_reg,beta_desapalancada_R2=0.8082016226002329)
# bottom-up alternativo: pesos por EBIT del segmento × EV/EBIT de la industria (Damodaran ene-26, pestaña de la hoja)
ret_ebit=43277; aws_ebit=61089   # LTM: AWS 9M26 48.555 + Q4-25 (FY25−9M25, ver nota) ; resto = 104.366 − AWS
v_ret=ret_ebit*32.4376517932853; v_cs=aws_ebit*19.25198547899857; v_sw=aws_ebit*32.41233949136116
OUT['beta_bottom_up_alternativas']=dict(
  R2_EV_ventas=0.8082,
  EBIT_x_EV_EBIT_ComputerServices=(v_ret*0.7809280399984467+v_cs*0.9617009989891427)/(v_ret+v_cs),
  EBIT_x_EV_EBIT_Software=(v_ret*0.7809280399984467+v_sw*1.248199417466542)/(v_ret+v_sw))
# ---------------- 2. I+D: serie, activo de investigación y prueba de neutralidad ----------------
TI={2018:28837,2019:35931,2020:42740,2021:56052,2022:73213,2023:85622,2024:88544,2025:108521,'LTM':126938}
DA={2018:12138,2019:15150,2020:16239,2021:22909,2022:24924,2023:30225,2024:32067,2025:41860,'LTM':53958}
AWSDA={2023:12531,2024:13320,2025:21450,'LTM':31151}
RD={k:TI[k]-DA[k] for k in TI}                        # cota prudente: toda la D&A de PP&E es infraestructura
RDh={k:TI[k]-AWSDA[k] for k in AWSDA}                  # cota alta: solo la D&A de AWS es infraestructura
def activo(serie,ys,life):
    a=sum(serie[y]*(1-i/life) for i,y in enumerate(ys[:life])); am=sum(serie[y] for y in ys[1:life+1])/life; return a,am
res_rd={}
for nombre,serie,ys in (('prudente',RD,['LTM',2025,2024,2023,2022,2021]),('alta',{**RDh},['LTM',2025,2024,2023])):
    for life in (2,3):
        if len(ys)<life+1: continue
        a,am=activo(serie,ys,life); ebit_adj=104366+serie['LTM']-am; ic_adj=509241+a
        res_rd[f'{nombre}_vida{life}']=dict(ID_LTM=serie['LTM'],activo=a,amortizacion=am,EBIT_ajustado=ebit_adj,
            margen_ajustado=ebit_adj/797455,ROIC_GAAP=81064.6943/509241,ROIC_ajustado=ebit_adj*(1-0.225)/ic_adj)
# Neutralidad: con capitalización consistente (EBIT +ID−amort y reinversión +ID−amort; impuesto sobre EBIT GAAP) FCFF no cambia
s=RD['LTM']/797455; r=run(B)
rev=[797455]; [rev.append(rev[-1]*(1+x)) for x in B['gr']]; rev_t=rev[-1]*1.04
idt=s*rev_t; neto=idt*(1-(1/1.04+1/1.04**2+1/1.04**3)/3)
nop_g=rev_t*B['mg_t']*(1-B['tx_t']); reinv_g=nop_g*0.04/B['roic_t']
roic_adj_eq=0.04*(nop_g+neto)/(reinv_g+neto)
fcff_si_125_ajustado=(nop_g+neto)*(1-0.04/0.125)
OUT['ID']=dict(serie_TI=TI,serie_DA_PPE=DA,ID_prudente=RD,ID_alta=RDh,resultados=res_rd,
  neutralidad=dict(FCFF_terminal_GAAP=r['fcff_t'],FCFF_terminal_capitalizado_consistente=nop_g+neto-(reinv_g+neto),
    ROIC_terminal_ajustado_equivalente_a_12_5_GAAP=roic_adj_eq,
    efecto_si_se_aplica_12_5_a_base_ajustada=100*(fcff_si_125_ajustado/r['fcff_t']-1)*r['tv_share']))
# ---------------- 3. Arrendamientos: ajuste tipo Damodaran ----------------
cost=14006+12323-10259; pv=100288; vida=9.9; dep=pv/vida; adj=cost-dep; dm=adj/797455
v_lease=run(A(mg=[m+dm for m in B['mg']],mg_t=B['mg_t']+dm))['ps']
OUT['arrendamientos']=dict(costo_operativo_LTM=cost,pasivo=pv,vida_remanente=vida,tasa_descuento=0.04,depreciacion_ROU=dep,
  ajuste_EBIT=adj,ajuste_margen_pp=100*dm,valor=v_lease,pct=pct(v_lease),
  alternativa_excluir_de_deuda=run(A(debt=B['debt']-pv))['ps'])
# ---------------- 4. Impuesto diferido de Anthropic ----------------
basis_notas=146200-140300; basis_pref=(8000-basis_notas)+5000+5000; tasa=34608/140300  # base preferentes = notas convertidas + Serie G + Serie H (T2-26, 10-Q nota 2)
dtl=34608+(92500-basis_pref)*tasa
OUT['impuesto_diferido']=dict(costo_total_notas=8000,base_notas_restantes=basis_notas,base_preferentes=basis_pref,tasa_implicita=tasa,
  DTL_notas_observado=34608,DTL_preferentes_estimado=(92500-basis_pref)*tasa,DTL_total=dtl,valor=run(A(nonop=B['nonop']-dtl))['ps'])
# ---------------- 5. Múltiplos: anclas históricas con Trailing Valuation!B3:K3 que falta ----------------
px={2022:84.00,2023:151.94,2024:219.39,2025:230.82}; sh={2022:10242,2023:10383,2024:10593,2025:10731}
debt={2022:67150+72968,2023:58314+77297,2024:52623+78277,2025:3106+14199+73448+87339}
cash={2022:70026,2023:86780,2024:101202,2025:123029}; inv={2022:0,2023:0,2024:0,2025:65359}
ebitda={2022:54169,2023:85515,2024:121388,2025:145731}; ocf={2022:46752,2023:84946,2024:115877,2025:139514}
ebit={2022:12248,2023:36852,2024:68593,2025:79975}; ii={2022:989,2023:2949,2024:4677,2025:4381}; ie={2022:-2367,2023:-3182,2024:-2406,2025:-2274}
k={2022:0.0982,2023:0.0848,2024:0.0891,2025:0.0841}
def anclas(k_corte):
    hist={}
    for y in px:
        mc=px[y]*sh[y]; ev=mc+debt[y]-cash[y]-inv[y]; ni_op=(ebit[y]+ii[y]+ie[y])*(1-0.21)
        f=min(1.4,max(0.6,(k[y]-0.04)/(k_corte-0.04)))
        hist[y]=dict(EV_EBITDA=ev/ebitda[y],P_OCF=mc/ocf[y],PE_operativo=mc/ni_op,factor_tasas=f)
    out={}
    for m in ('EV_EBITDA','P_OCF','PE_operativo'):
        adjm=[hist[y][m]*hist[y]['factor_tasas'] for y in px]
        out[m]=dict(sin_ajuste=[round(hist[y][m],2) for y in px],ajustado=[round(x,2) for x in adjm],minimo=min(adjm),mediana=st.median(adjm))
    return hist,out
fy3=dict(EV_EBITDA=265177.7062,P_OCF=131185.1233,PE_operativo=136888.8241)   # FY+3 Base de la hoja (P/E usa la utilidad proyectada de la hoja)
mc0=10811*240.35; ev0=mc0+304461-114226-294595
obs=dict(EV_EBITDA=ev0/183719,P_OCF=mc0/168300,PE_operativo=mc0/((104366+4747-4484)*(1-0.21)))
def vp(m,mult,ke):
    if m=='EV_EBITDA': eq=mult*fy3[m]-304461+114226+294595-26560.77
    else: eq=mult*fy3[m]-26560.77
    return eq/10811/(1+ke)**3
mult={}
for etiqueta,kc,ke in (('tasas_R2',0.0949,0.0915094186435848),('tasas_corte_nov26',0.0873,0.0849879)):
    hist,an=anclas(kc); tab={}
    for m in fy3:
        c=an[m]['mediana']; filas=[c*x for x in (0.8,0.9,1,1.1,1.2)]; cols=[fy3[m]*x for x in (0.9,0.95,1,1.05,1.1)]
        mat=[[ (vp(m,fm,ke)*fy3[m]/fy3[m]) if False else None for _ in cols] for fm in filas]
        mat=[]
        for fm in filas:
            fila=[]
            for d in cols:
                eq=(fm*d-304461+114226+294595-26560.77) if m=='EV_EBITDA' else fm*d-26560.77
                fila.append(round(eq/10811/(1+ke)**3,2))
            mat.append(fila)
        tab[m]=dict(ancla_A_mediana=c,ancla_A_minimo=an[m]['minimo'],serie=an[m],observado_hoy=obs[m],
             VP_por_accion_mediana=vp(m,c,ke),VP_por_accion_minimo=vp(m,an[m]['minimo'],ke),VP_por_accion_observado=vp(m,obs[m],ke),
             matriz_5x5=dict(filas_multiplo=[round(x,2) for x in filas],columnas_FY3=[round(x) for x in cols],valores=mat))
    mult[etiqueta]=dict(historicos={y:{a:round(b,3) for a,b in v.items()} for y,v in hist.items()},metodos=tab)
OUT['multiplos']=mult; OUT['multiplos_nota']=('Auditor: precios de cierre de diciembre (Alpha Vantage, ajustados por split 20:1), acciones de Income Statement!27, deuda y '
   'caja de Balance Sheet; EV excluye inversiones no operativas. P/E con utilidad operativa normalizada (sin ganancias de Anthropic/Rivian). Ke de descuento = Ke del caso. No oficial: la hoja debe calcularlos tras diligenciar Trailing Valuation!B3:K3 y Entradas históricas auxiliares!4:5.')
# ---------------- 6. Paquetes de R3 propuesto ----------------
intl=0.049057867221630184-0.0455
def wacc(mature,bu=0.8082016226002329): pth,term,_,_=wacc_path(0.0494,mature+intl,mature,bu); return dict(wacc=pth,wacc_t=term)
paq={}
def P(n,p,mode='market'): v=run(p,mode)['ps']; paq[n]=dict(valor=v,pct=pct(v),mos35=v*0.65); return p
c1=P('1_errores: ERP nov T12m + arrendamientos Damodaran + DTL total + RSU a mercado', A(**wacc(0.0379),mg=[m+dm for m in B['mg']],mg_t=B['mg_t']+dm,nonop=B['nonop']-dtl))
c2=P('2_+ impuesto de caja 15%→25% + margen año 1 14,1% (+ajuste arriendo)', A(c1,tx=tpath(0.15),mg=mpath(0.141+dm,0.17+dm)))
c3=P('3_+ ROIC terminal 13,6% (piso Retail) = R3 central propuesto', A(c2,roic_t=0.136))
OUT['beta_usada_en_R3']='bottom-up R2 0,808; ver beta_regresion'
c4=P('4_R3 central con beta bottom-up EBIT×EV/EBIT ComputerServices', A(c3,**{k_:v for k_,v in wacc(0.0379,OUT['beta_bottom_up_alternativas']['EBIT_x_EV_EBIT_ComputerServices']).items()}))
c5=P('5_R3 central con ERP pago sostenible nov 4,41%', A(c3,**wacc(0.0441)))
c6=P('6_R3 central con beta de regresión desapalancada', A(c3,**wacc(0.0379,min(bu_reg,1.6))))
OUT['paquetes_R3']=paq
for nm,p in (('R3_central',c3),):
    lo,hi=0.12,0.40
    for _ in range(100):
        m=(lo+hi)/2; v=run(A(p,mg=mpath(0.141+dm,m),mg_t=m),'market')['ps']; lo,hi=(m,hi) if v<240.35 else (lo,m)
    OUT['margen_terminal_implicito_R3_central']=m
json.dump(OUT,open('resolucion_R3.json','w'),indent=1,default=str)
b=OUT['beta_regresion']; print('BETA reg %.3f se %.3f R2 %.2f IC95 %.2f–%.2f Blume %.3f βu %.3f'%(b['beta'],b['error_estandar'],b['r2'],*b['ic95'],b['beta_blume'],b['beta_desapalancada_equivalente']))
print('bottom-up:',{k_:round(v,3) for k_,v in OUT['beta_bottom_up_alternativas'].items()})
for k_,v in res_rd.items(): print('ID',k_,{a:round(x,4) if x<5 else round(x) for a,x in v.items()})
print('neutralidad',{a:round(x,4) for a,x in OUT['ID']['neutralidad'].items()})
print('arrend',{a:round(x,3) for a,x in OUT['arrendamientos'].items()})
print('DTL',{a:round(x,3) for a,x in OUT['impuesto_diferido'].items()})
for et,v in mult.items():
    print('MULT',et,v['historicos'])
    for m,t in v['metodos'].items(): print('  ',m,'A med %.2f min %.2f obs %.2f | VP med %.2f min %.2f obs %.2f'%(t['ancla_A_mediana'],t['ancla_A_minimo'],t['observado_hoy'],t['VP_por_accion_mediana'],t['VP_por_accion_minimo'],t['VP_por_accion_observado']), t['serie']['sin_ajuste'])
for n,v in paq.items(): print(f"{n:80s} {v['valor']:8.2f} {v['pct']:+7.2f}% MOS {v['mos35']:.2f}")
print('margen implícito R3 central', OUT['margen_terminal_implicito_R3_central'])
