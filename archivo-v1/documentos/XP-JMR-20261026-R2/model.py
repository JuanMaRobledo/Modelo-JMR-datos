"""XP: financial equity model. BRL million, nominal cash flows, annual periods.

This is a sector adaptation in the XP working copy, not the industrial FCFF.
All scenarios, stresses, sensitivities and inverse use the same function.
"""
from pathlib import Path
import json,math,copy,csv
P=Path(__file__).resolve().parent
REV='XP-JMR-20261026-R2'
I={'revenue0':19122.419,'ebt0':5726.543,'net_income0':5313.855,'parent_income0':5316.803,'equity0':24831.073,
 'shares_basic_m':507.483079,'rsu_psu_m':17.672287,'vesting_fraction':0.95,
 'rf_usd':0.0507,'erp_mature':0.039174804210012876,'beta':0.98,'crp_brazil':0.0324,'country_repricing':0.02,
 'inflation_brl':0.03,'inflation_usd':0.023,'fx_brl_per_usd':5.5007,'price_usd':15.37,
 'price_timestamp':'2026-10-26 13:57 America/New_York','fx_timestamp':'2026-10-26 13:09:51 BRT',
 'reg_rwa0':99904.171,'reg_cet1_0':7675.252,'reg_cet1_target':0.0768,
 'rwa_revenue_growth_multiplier':1.0,'cet1_allocation':0.5,'mos':0.35}
SC=[
 {'id':'A','name':'Base · expansión con normalización fiscal','prob':0.45,'growth':[.08,.10,.09,.08,.07],'margin5':.31,'marginT':.295,'tax5':.12,'taxT':.20,'roe5':.22,'roeT':.1777,'gT':.05},
 {'id':'B','name':'Conservadora · presión competitiva y menor retorno','prob':0.225,'growth':[.02,.04,.05,.05,.05],'margin5':.28,'marginT':.27,'tax5':.12,'taxT':.20,'roe5':.18,'roeT':None,'gT':.05},
 {'id':'C','name':'Disrupción · Deterioro de los fundamentales','prob':.10,'growth':[-.15,-.05,0,.01,.02],'margin5':.20,'marginT':.18,'tax5':.12,'taxT':.20,'roe5':.15,'roeT':None,'gT':.02},
 {'id':'D','name':'Optimista · mayor monetización y escala','prob':.225,'growth':[.14,.15,.14,.12,.10],'margin5':.34,'marginT':.32,'tax5':.12,'taxT':.20,'roe5':.23,'roeT':.1777,'gT':.05}]
def lerp(a,b,t):return a+(b-a)*t
def calculate(s,changes=None,retain_detail=True):
 i=I|dict(changes or {});s=copy.deepcopy(s)
 ke_usd=i['rf_usd']+i['beta']*i['erp_mature']+i['crp_brazil']+i['country_repricing']
 ke=(1+ke_usd)*(1+i['inflation_brl'])/(1+i['inflation_usd'])-1
 keT_usd=i['rf_usd']+i['erp_mature']+i['crp_brazil']+i['country_repricing']
 keT=(1+keT_usd)*(1+i['inflation_brl'])/(1+i['inflation_usd'])-1+i.get('keT_delta',0)
 gT=s['gT']+i.get('gT_delta',0);roeT=(s['roeT'] if s['roeT'] is not None else keT)+i.get('roeT_delta',0)
 if keT<=gT or roeT<=gT or gT<=-1:raise ValueError('INVALID_TERMINAL')
 growth=[x+i.get('growth_delta',0) for x in s['growth']]
 if min(growth)<=-1:raise ValueError('INVALID_GROWTH')
 growth += [lerp(growth[4],gT,(t-5)/5) for t in range(6,11)]+[gT]
 m0=i['ebt0']/i['revenue0'];tax0=(i['ebt0']-i['net_income0'])/i['ebt0'];a=i['parent_income0']/i['net_income0']
 er0=i['parent_income0']/i['equity0'];revenue=i['revenue0'];rwa=i['reg_rwa0'];forecast=[]
 for t in range(1,12):
  if t<=5:
   margin=lerp(m0,s['margin5']+i.get('margin_delta',0),t/5);tax=lerp(tax0,s['tax5']+i.get('tax_delta',0),t/5);roe=lerp(er0,s['roe5'],t/5)
  else:
   z=min((t-5)/5,1);margin=lerp(s['margin5']+i.get('margin_delta',0),s['marginT']+i.get('margin_delta',0),z);tax=lerp(s['tax5']+i.get('tax_delta',0),i.get('taxT_override',s['taxT'])+i.get('tax_delta',0),z);roe=lerp(s['roe5'],roeT,z)
  revenue*=1+growth[t-1];ebt=revenue*margin;ni=ebt*(1-tax)*a;rwa*=1+growth[t-1]*i['rwa_revenue_growth_multiplier']
  forecast.append({'year':t,'growth':growth[t-1],'revenue':revenue,'ebt_margin':margin,'tax':tax,'ni':ni,'roe_target':roe,'rwa':rwa})
 book=i['equity0'];cet=i['reg_cet1_0'];disc=1;pv=0
 for t in range(1,11):
  row=forecast[t-1];nxt=forecast[t]
  # Forward book requirement supports next year's income at next year's ROE.
  # No assumed release of previously recognized equity; no bank deposits subtracted.
  book_req=nxt['ni']/nxt['roe_target'];delta_book=max(0,book_req-book)
  reg_add=max(0,i['reg_cet1_target']*nxt['rwa']-cet)/i['cet1_allocation']
  reinv=max(delta_book,reg_add);fcfe=row['ni']-reinv;book+=reinv;cet+=reinv*i['cet1_allocation']
  k=ke if t<=5 else lerp(ke,keT,(t-5)/5);disc*=1+k;pv+=fcfe/disc
  row.update(ke=k,discount=disc,book_required=book_req,reg_add=reg_add,reinvestment=reinv,fcfe=fcfe,pv=fcfe/disc,book=book,cet1_proxy=cet,cet1_ratio_proxy=cet/row['rwa'])
 # At steady state require growth financing for ALL retained equity, not merely
 # for an artificial marginal ROE. This keeps legacy stranded capital visible.
 ni11=forecast[10]['ni'];reinv11=gT*book;fcfe11=ni11-reinv11
 tv=fcfe11/(keT-gT);pvtv=tv/disc*i.get('terminal_scale',1)
 equity=pv+pvtv-i.get('additional_capital_holdback',0)/(1+ke)
 shares=i['shares_basic_m']+i['rsu_psu_m']*i['vesting_fraction'];vbrl=equity/shares;vusd=vbrl/i['fx_brl_per_usd']
 out={'revision_id':REV,'id':s['id'],'name':s['name'],'prob':s['prob'],'ke_usd':ke_usd,'ke_brl':ke,'keT_brl':keT,'gT':gT,'roeT_assumed':roeT,'roeT_effective':ni11/book,'fcfe11':fcfe11,'reinvestment11':reinv11,'book10':book,'pv_explicit':pv,'terminal':tv,'pv_terminal':pvtv,'equity_brl_m':equity,'shares_equiv_m':shares,'value_brl':vbrl,'value_usd':vusd,'mos_usd':vusd*(1-i['mos']),'terminal_weight_equity':pvtv/equity,'cagr5':math.prod(1+x for x in growth[:5])**.2-1,'annual':forecast[:10] if retain_detail else []}
 # Independent residual-income identity, including explicit book roll-forwards.
 prior=i['equity0'];rip=0
 for row in forecast[:10]:rip+=(row['ni']-row['ke']*prior)/row['discount'];prior=row['book']
 residual=i['equity0']+rip+(tv-prior)/disc
 out['residual_income_value_usd']=residual/shares/i['fx_brl_per_usd']
 if not changes or not any(k in changes for k in ['terminal_scale','additional_capital_holdback']):assert abs(out['residual_income_value_usd']-vusd)<1e-8
 return out
def inverse(s,price,changes=None):
 roots=[];prev=None
 for n in range(501):
  d=-.49+n*.002;v=calculate(s,(changes or {})|{'growth_delta':d},False)['value_usd']-price
  if prev and prev[1]*v<0:
   lo,hi=prev[0],d
   for _ in range(70):
    mid=(lo+hi)/2;fm=calculate(s,(changes or {})|{'growth_delta':mid},False)['value_usd']-price
    if (calculate(s,(changes or {})|{'growth_delta':lo},False)['value_usd']-price)*fm<=0:hi=mid
    else:lo=mid
   rt=(lo+hi)/2;r=calculate(s,(changes or {})|{'growth_delta':rt},False);roots.append({'delta':rt,'cagr5':r['cagr5'],'value_usd':r['value_usd'],'error':r['value_usd']-price})
  prev=(d,v)
 return {'price':price,'interval':[-.49,.51],'roots':roots,'selected':min(roots,key=lambda x:abs(x['delta'])) if roots else None}
def run():
 results=[calculate(s) for s in SC];base=results[0];sens=[]
 for name,xk,yk,xv,yv in [
  ('Ke terminal × g','keT_delta','gT_delta',[-.01,-.005,0,.005,.01],[-.005,-.0025,0,.0025,.005]),
  ('ROE terminal × g','roeT_delta','gT_delta',[-.02,-.01,0,.01,.02],[-.005,-.0025,0,.0025,.005]),
  ('Crecimiento de ingresos × margen EBT','growth_delta','margin_delta',[-.02,-.01,0,.01,.02],[-.03,-.015,0,.015,.03])]:
  values=[[calculate(SC[0],{xk:x,yk:y},False)['value_usd'] for x in xv] for y in yv];assert abs(values[2][2]-base['value_usd'])<1e-10
  sens.append({'name':name,'x_key':xk,'y_key':yk,'x_deltas':xv,'y_deltas':yv,'prices_usd':values,'center':values[2][2]})
 alternatives={'sin_sobretasa_pais':{'country_repricing':0},'sobretasa_pais_3pp':{'country_repricing':.03},'sin_moat':{'roeT_delta':base['keT_brl']-.1777},'impuesto_terminal_34pct':{'taxT_override':.34},'vesting_100pct':{'vesting_fraction':1},'acciones_emitidas_agosto_sin_ajuste':{'shares_basic_m':508.500275},'capital_adicional_1bn':{'additional_capital_holdback':1000},'capital_adicional_3bn':{'additional_capital_holdback':3000},'beta_regresion_1_03':{'beta':1.03},'CET1_9pct':{'reg_cet1_target':.09},'RWA_crece_50pct_mas':{'rwa_revenue_growth_multiplier':1.5},'asignacion_CET1_20pct':{'cet1_allocation':.2},'FX_6':{'fx_brl_per_usd':6.0}}
 stresses={k:{'inputs':v,'value_usd':(z:=calculate(SC[0],v,False))['value_usd'],'impact_pct':100*(z['value_usd']/base['value_usd']-1)} for k,v in alternatives.items()}
 out={'revision_id':REV,'ticker':'XP','method':'FCFE financiero — adaptación de XP, pendiente de cierre JMR integral','information_cutoff':'2026-10-26','financial_cutoff':'2026-06-30','status':'PENDIENTE_VALIDACION_INTEGRAL','inputs':I,'scenario_inputs':SC,'results':results,'average_three':sum(r['prob']*r['value_usd'] for r in results if r['id']!='C')/.9,'sensitivity':sens,'inverse':inverse(SC[0],I['price_usd']),'inverse_variants':[{'margin_delta':m,'beta':b,'inverse':inverse(SC[0],I['price_usd'],{'margin_delta':m,'beta':b})} for m in [0,-.02] for b in [.98,1.03]],'stresses':stresses,'publication_authorized':False}
 (P/'XP_resultados_R2.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
 with (P/'XP_proyecciones_R2.csv').open('w',newline='') as f:
  writer=csv.DictWriter(f,fieldnames=['scenario']+list(results[0]['annual'][0]));writer.writeheader()
  for r in results:
   for row in r['annual']:writer.writerow({'scenario':r['id']}|row)
 print(json.dumps({k:v for k,v in out.items() if k in ['average_three','inverse','stresses']}|{'values':[(r['name'],r['value_usd'],r['mos_usd']) for r in results]},ensure_ascii=False,indent=2))
if __name__=='__main__':run()
