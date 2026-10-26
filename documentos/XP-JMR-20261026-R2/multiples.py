from pathlib import Path
import json
P=Path(__file__).resolve().parent
def run():
 j=json.loads((P/'XP_resultados_R2.json').read_text());i=j['inputs'];cap=16.3700008392334*518.744049*5.5024
 gu=(1.05)*(1.023)/(1.03)-1;factor=(.0418+.0423-gu)/(.0529+.036974804210012875-gu)
 hist={'PE':cap/5169.787,'PS':cap/18398.597,'PBV':cap/23546.701};out=[]
 for r in j['results']:
  if r['id']=='C':continue
  roe,g,ke=r['roeT_assumed'],r['gT'],r['keT_brl'];sc=next(s for s in j['scenario_inputs'] if s['id']==r['id'])
  cpe=(1-g/roe)/(ke-g);cps=sc['marginT']*(1-sc['taxT'])*(i['parent_income0']/i['net_income0'])*cpe;cpb=(roe-g)/(ke-g)
  c={'PE':cpe,'PS':cps,'PBV':cpb,'PFCFE':1/(ke-g)}
  ms={m:min(hist[m]*factor,c[m]) if m in hist else c[m] for m in c};vals={}
  for m,k in ms.items():
   vv=[]
   for n,row in enumerate(r['annual'][:3],1):
    metric={'PE':row['ni'],'PS':row['revenue'],'PBV':row['book'],'PFCFE':row['fcfe']}[m]
    if metric<=0:
     vv.append({'year':n,'metric_brl_m':metric,'target_brl':None,'pv_usd':None,'reason':'N/A: fundamental no positivo'});continue
    target=k*metric/r['shares_equiv_m'];div=sum(z['fcfe']/z['discount'] for z in r['annual'][:n])/r['shares_equiv_m']
    vv.append({'year':n,'metric_brl_m':metric,'target_brl':target,'pv_usd':(target/row['discount']+div)/i['fx_brl_per_usd']})
   vals[m]={'multiple':k,'ancla_A':hist.get(m),'factor_tasas':factor if m in hist else None,'ancla_C':c[m],'years':vv,'weight':{'PE':.7,'PBV':.3,'PS':0,'PFCFE':0}[m]}
  out.append({'id':r['id'],'name':r['name'],'methods':vals,'secondary_weighted_fy3_pv_usd':.7*vals['PE']['years'][2]['pv_usd']+.3*vals['PBV']['years'][2]['pv_usd']})
 j['multiples']={'status':'CALCULADO_EN_ADAPTADOR_FINANCIERO; integración plantilla original pendiente','historical_anchor':{'year':2025,'price_usd_yahoo':16.3700008392334,'price_usd_other_provider':16.16,'economic_shares_m':518.744049,'fx':5.5024,'equity_cap_brl_m':cap,'ratios':hist,'rate_factor':factor,'limitations':'Diferencia de precio entre proveedores 1,30 %; las anclas C son menores que ambas alternativas históricas ajustadas. P/FCFE no tiene serie homogénea: ancla C y peso cero.'},'scenarios':out,'not_applicable':{'EV/EBITDA':'Financiación operativa: EV industrial no homogéneo','EV/FCFF':'No hay FCFF industrial interpretable','P/OCF':'Intermediación domina OCF; no se utiliza como FCFE ni se fabrica OCF prospectivo'},'observed':{'PE':i['price_usd']*i['shares_basic_m']*i['fx_brl_per_usd']/i['parent_income0'],'PS':i['price_usd']*i['shares_basic_m']*i['fx_brl_per_usd']/i['revenue0'],'PBV':i['price_usd']*i['shares_basic_m']*i['fx_brl_per_usd']/i['equity0']}}
 (P/'XP_resultados_R2.json').write_text(json.dumps(j,ensure_ascii=False,indent=2))
if __name__=='__main__':run()
