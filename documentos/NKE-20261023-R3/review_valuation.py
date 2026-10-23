import json, math, hashlib, statistics, datetime
from pathlib import Path
P=Path(__file__).parent; OLD=P.parent/'nke_revision'
V=json.loads((OLD/'valuation_calc.json').read_text()); D=json.loads((OLD/'data.json').read_text()); F=json.loads((OLD/'sources/NKE_companyfacts.json').read_text())['facts']['us-gaap']
def fact(tag,end,start=None):
 a=[x for vals in F.get(tag,{}).get('units',{}).values() for x in vals if x.get('end')==end and (start is None or x.get('start')==start) and x.get('filed','')<='2026-10-22']
 return sorted(a,key=lambda x:x['filed'])[-1]['val']/1e6 if a else None
for y in range(2016,2027):
 d=D['FY'+str(y)]; d['inventories']=fact('InventoryFinishedGoodsNetOfReserves',f'{y}-05-31')
 d['liabilities']=d['assets']-d['equity']
D['FY2016']['st_investments']=2319.;D['FY2017']['st_investments']=2371.
for k,y in [('Q1FY2026',2025),('Q1FY2027',2026)]:D[k]['inventories']=fact('InventoryFinishedGoodsNetOfReserves',f'{y}-08-31')
L=D['LTM']; L['inventories']=D['Q1FY2027']['inventories'];L['liabilities']=L['assets']-L['equity']
for key in ['basic_shares','diluted_shares']:L[key]=(D['FY2026'][key]*365+(D['Q1FY2027'][key]-D['Q1FY2026'][key])*92)/365
prior_ltm=D['FY2025']['revenue']+D['Q1FY2026']['revenue']-fact('RevenueFromContractWithCustomerExcludingAssessedTax','2024-08-31','2024-06-01')
L['revenue_growth_yoy']=L['revenue']/prior_ltm-1
def dcf(case,delta=0,margin=None,wi=None,wt=None,rt=None,gt=None):
 target=case['margin_adjusted'] if margin is None else margin; wi=V['wacc'] if wi is None else wi;wt=V['wacc_terminal'] if wt is None else wt;rt=case['roic_terminal'] if rt is None else rt;gt=case['g_terminal'] if gt is None else gt
 rates=[x+delta for x in case['growth'][:5]];rates += [rates[-1]+(gt-rates[-1])*n/5 for n in range(1,6)]
 rev=L['revenue'];df=1.;pv=0.;rows=[];first=.0525+V['lease_adjustment']/L['revenue']
 for t,g in enumerate(rates,1):
  prev=rev;rev*=1+g;m=first+(target-first)*min(t-1,4)/4;tax=.25+(V['tax_marginal']-.25)*max(t-5,0)/5;k=wi+(wt-wi)*max(t-5,0)/5
  late=rt/(target*(1-V['tax_marginal'])*(1+gt));s=case['s2c']+(late-case['s2c'])*max(t-5,0)/5;ri=max(0,(rev-prev)/s);nopat=rev*m*(1-tax);df/=1+k;pv+=(nopat-ri)*df;rows.append({'year':t,'revenue':rev,'margin':m,'reinvestment':ri,'nopat':nopat,'discount':df})
 terminal=rev*(1+gt)*target*(1-V['tax_marginal'])*(1-gt/rt)/(wt-gt)*df
 return {'value':(pv+terminal+V['cash']-V['debt_book']-V['options'])/V['shares'],'explicit_pv':pv,'terminal_pv':terminal,'rows':rows}
checks=[]
for name,case in V['scenarios'].items():
 r=dcf(case);err=abs(r['value']-case['result']['value']);assert err<1e-9;checks.append({'id':'REVAL-'+name,'error':err,'value':r['value']})
for mat in V['matrices']:
 for i,y in enumerate(mat['y']):
  for j,x in enumerate(mat['x']):
   args={'wt':y,'gt':x} if mat['name'].startswith('WACC') else {'rt':y,'gt':x} if mat['name'].startswith('ROIC') else {'delta':y,'margin':x}
   assert abs(dcf(V['scenarios']['Base'],**args)['value']-mat['values'][i][j])<1e-9
reg=json.loads((OLD/'regression.json').read_text());alt=reg['alternative_wacc'];inverse_extra=[]
for margin in [.11415637053016931,.13415637053016932]:
 for label,w in [('bottom_up',V['wacc']),('OLS',alt)]:
  lo,hi=-.5,.8
  for _ in range(65):
   mid=(lo+hi)/2
   if dcf(V['scenarios']['Base'],delta=mid,margin=margin,wi=w)['value']<V['price']:lo=mid
   else:hi=mid
  delta=(lo+hi)/2;inverse_extra.append({'margin_adjusted':margin,'beta_method':label,'wacc':w,'delta':delta,'cagr':math.prod(1+x+delta for x in V['scenarios']['Base']['growth'][:5])**.2-1,'reconstructed':dcf(V['scenarios']['Base'],delta=delta,margin=margin,wi=w)['value']})
reason='N/D: el flujo histórico observado resta SBC a OCF−capex y no concilia financiación neta; no es FCFE verificado.'
for m in V['multiple_matrices']:
 if m['method']=='PFCFE':m.update(x=[None]*5,values=[[None]*5 for _ in range(5)],expected=None,center_error=None,unavailable_reason=reason)
for m in V['multiples']:
 if m['method']=='PFCFE':m.update(observed=None,observed_present_value=None,note=reason)
V.update(revision='NKE-JMR-20261023-R3',previous_revision='NKE-JMR-20261023-R2',inverse_alternatives=inverse_extra,historical_data_sha256=hashlib.sha256(json.dumps(D,sort_keys=True).encode()).hexdigest())
V['review_r3']={'financial_model_changed':False,'base_unchanged':True,'changes':['Crecimiento LTM corregido a comparación con LTM previo, no FY previo.','Promedios de acciones LTM reconstruidos por días, aproximación a partir de datos redondeados; no suma de promedios.','P/FCFE observado y sus dos matrices retirados: financiación no conciliada.','Inventarios históricos recuperados de la etiqueta XBRL correcta; inversiones CP FY2017 recuperadas del 10-K.'],'status':'CON HALLAZGOS','rules_version':5,'prompt_commit':'7e6ee50dca69a05839cd819ef33ba813ef0aa2f4'}
ratios={}
for y in range(2017,2027):
 d=D['FY'+str(y)];pr=D['FY'+str(y-1)];debt=d['debt_current']+d['debt_noncurrent'];cash=d['cash']+d['st_investments'];leases=(d['lease_current'] or 0)+(d['lease_noncurrent'] or 0);ic=d['equity']+debt+leases-cash
 ratios[str(y)]={'growth':d['revenue']/pr['revenue']-1,'gross_margin':1-d['cogs']/d['revenue'],'operating_margin':d['ebit_core']/d['revenue'],'net_margin':d['net_income']/d['revenue'],'fcf_margin':d['fcf']/d['revenue'],'roa':d['net_income']/((d['assets']+pr['assets'])/2),'roe':d['net_income']/((d['equity']+pr['equity'])/2),'roic_end':d['ebit_core']*(1-d['tax']/d['ebt'])/ic if y>=2020 else None,'s2c_end':d['revenue']/ic if y>=2020 else None,'current':d['ca']/d['cl'],'quick':(cash+d['ar'])/d['cl'],'net_debt_ebitda':(debt+leases-cash)/(d['ebit_core']+d['da']),'capex_sales':d['capex']/d['revenue'],'ocf_ni':d['ocf']/d['net_income']}
ratios['LTM']={'growth':L['revenue_growth_yoy'],'gross_margin':1-L['cogs']/L['revenue'],'operating_margin':L['ebit_core']/L['revenue'],'net_margin':L['net_income']/L['revenue'],'fcf_margin':L['fcf']/L['revenue'],'roa':None,'roe':None,'roic_end':L['ebit_core']*(1-L['tax']/L['ebt'])/(L['equity']+V['debt_book']-V['cash']),'s2c_end':L['revenue']/(L['equity']+V['debt_book']-V['cash']),'current':L['ca']/L['cl'],'quick':(V['cash']+L['ar'])/L['cl'],'net_debt_ebitda':(V['debt_book']-V['cash'])/(L['ebit_core']+L['da']),'capex_sales':L['capex']/L['revenue'],'ocf_ni':L['ocf']/L['net_income']}
for name,obj in [('data.json',D),('ratios.json',ratios),('valuation_results.json',V),('valuation_checks.json',{'checks':checks,'sensitivity_cells':75,'prior_ltm_revenue':prior_ltm,'stage':'Valoración; anterior a análisis y auditoría','completedAt':datetime.datetime.now(datetime.timezone.utc).isoformat()})]: (P/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
print('Base',V['base_value'],'LTM YoY',L['revenue_growth_yoy'],'shares LTM',L['basic_shares'],L['diluted_shares'],'matrices',sum(m['expected'] is not None for m in V['multiple_matrices']))
