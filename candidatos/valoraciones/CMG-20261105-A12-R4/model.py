"""CMG R4 auxiliary JMR. No writes to original Damodaran formulas."""
import json, math, copy
from pathlib import Path
P=Path(__file__).parent
SOURCES={
 'Q3':'https://www.sec.gov/Archives/edgar/data/1058090/000105809026000104/cmg-20260930.htm',
 'FY25':'https://www.sec.gov/Archives/edgar/data/1058090/000105809026000009/cmg-20251231.htm',
 'beta':'https://pages.stern.nyu.edu/adamodar/New_Home_Page/datafile/Betas.html',
 'ERP':'https://pages.stern.nyu.edu/adamodar/New_Home_Page/home.htm',
 'Rf':'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_yield_curve',
 'price':'https://stockanalysis.com/stocks/cmg/history/',
 'terminal':'https://pages.stern.nyu.edu/~adamodar/New_Home_Page/littlebook/terminalvalue.htm'}
RAW=dict(revenue_fy=11925.601,revenue_9m=9729.966,revenue_9m_prior=8942.090,
 ebit_fy=1935.798,ebit_9m=1374.622,ebit_9m_prior=1515.479,
 tax_fy=473.758,tax_9m=349.957,tax_9m_prior=371.047,
 pretax_fy=2009.519,pretax_9m=1396.202,pretax_9m_prior=1575.876,
 da_fy=361.382,da_9m=297.656,da_9m_prior=268.680,
 capex_fy=666.336,capex_9m=640.597,capex_9m_prior=468.881,
 cfo_fy=2113.926,cfo_9m=1922.138,cfo_9m_prior=1688.082,
 sbc_fy=119.543,sbc_9m=86.369,sbc_9m_prior=93.966,
 equity=2455.144,equity_fy=2830.607,lease_current=321.557,lease_long=5277.474,
 lease_fy=5075.814,rou=4928.149,rou_fy=4463.010,lease_rate=.0548,
 cash=634.210,short_investments=268.354,long_investments=100.365,restricted_cash=35.799,
 shares=1264.975,rsu=3.654,psu=1.036,options=12.268,strike=39.51,maturity=4.2,
 vol=.4115,price=35.20,treasury=.049,us_default=.0022,erp_treasury=.0441,
 beta_unlevered=.78,kd=.06,tax=.25,units=4267,units_prior=3916,
 lease_add_fy=751.614,lease_add_9m=709.097,lease_add_9m_prior=595.080,
 lease_cash_fy=520.277,lease_cash_9m=433.337,lease_cash_9m_prior=386.076,
 fixed_rent_fy=544.367,occupancy_fy=624.898,occupancy_9m=523.494,occupancy_9m_prior=462.405,
 new_capex_per_unit=1.55,new_lease_capital_per_unit=1.40,new_unit_sales=3.106,
 maintenance_capex_2026=266.9,newbuild_capex_2026=531.8,total_capex_2026=834.1)
SCENARIOS={
 'Base':dict(openings=[350,350,340,330,320,300,280,250,230,210],comps=[.02,.025,.025,.025,.025,.025,.022,.02,.02,.02],margin=.185,sc1=1.5,sc2=1.4,roic=.14,g=.04,weight=.45),
 'Conservadora':dict(openings=[250,240,230,220,210,190,170,150,130,110],comps=[0,.01,.015,.015,.015,.015,.015,.015,.015,.015],margin=.16,sc1=1.15,sc2=1.05,roic=.105,g=.04,weight=.225),
 'Optimista':dict(openings=[380,400,420,430,430,410,390,370,350,330],comps=[.03,.035,.035,.035,.035,.03,.03,.025,.025,.025],margin=.21,sc1=1.65,sc2=1.5,roic=.18,g=.04,weight=.225),
 'Disrupcion':dict(openings=[50,30,0,0,0,30,50,70,80,90],comps=[-.10,-.06,-.02,0,.01,.01,.01,.01,.01,.01],margin=.095,sc1=1.,sc2=1.,roic=.08,g=.02,weight=.10)}
def norm(x): return .5*(1+math.erf(x/math.sqrt(2)))
def derive(raw=RAW):
 d=raw.copy()
 for k in ['revenue','ebit','tax','pretax','da','capex','cfo','sbc','lease_add','lease_cash']:
  d[k]=raw[k+'_fy']+raw[k+'_9m']-raw[k+'_9m_prior']
 d['lease']=raw['lease_current']+raw['lease_long']
 d['cash_total']=raw['cash']+raw['short_investments']
 d['rf']=raw['treasury']-raw['us_default'];d['erp']=raw['erp_treasury']+raw['us_default']
 d['shares_total']=raw['shares']+raw['rsu']+raw['psu']
 d['occupancy']=raw['occupancy_fy']+raw['occupancy_9m']-raw['occupancy_9m_prior']
 d['fixed_rent_proxy']=raw['fixed_rent_fy']*d['occupancy']/raw['occupancy_fy']
 d['lease_interest_proxy']=(d['lease']+4980.117)/2*raw['lease_rate']
 d['rou_da_proxy']=d['fixed_rent_proxy']-d['lease_interest_proxy']
 d['ebit_adjusted']=d['ebit']+d['lease_interest_proxy']
 d['capital']=raw['equity']+d['lease']-d['cash_total']-raw['long_investments']
 d['capital_fy']=raw['equity_fy']+raw['lease_fy']-(350.545+698.591)-197.123
 d['debt_weight']=d['lease']/(d['lease']+d['shares_total']*raw['price'])
 d['beta']=raw['beta_unlevered']*(1+(1-raw['tax'])*d['lease']/(d['shares_total']*raw['price']))
 d['ke']=d['rf']+d['beta']*d['erp']
 d['wacc']=d['ke']*(1-d['debt_weight'])+raw['kd']*(1-raw['tax'])*d['debt_weight']
 d['wacc_terminal']=d['rf']+.045
 d['auvk']=d['revenue']/((raw['units']+raw['units_prior'])/2)
 sigma=raw['vol'];T=raw['maturity'];spot=raw['price'];K=raw['strike']
 x=(math.log(spot/K)+(d['rf']+.5*sigma*sigma)*T)/(sigma*math.sqrt(T));y=x-sigma*math.sqrt(T)
 d['option_value']=raw['options']*(spot*norm(x)-K*math.exp(-d['rf']*T)*norm(y))
 return d
def calculate(case='Base',raw=RAW,changes=None,lag=1,policy='financial',fade=0,fade_start=None):
 d=derive(raw);s=copy.deepcopy(SCENARIOS[case]);s.update(changes or {})
 rev=[d['revenue']];units=[raw['units']];auv=d['auvk'];rows=[]
 for t in range(1,11):
  units.append(units[-1]+s['openings'][t-1]);auv*=1+s['comps'][t-1]
  rev.append((units[-2]+units[-1])/2*auv)
 rev.append(rev[-1]*(1+s['g']))
 ic=d['capital'];cum=1
 for t in range(1,12):
  margin=d['ebit_adjusted']/d['revenue']+(s['margin']-d['ebit_adjusted']/d['revenue'])*min(t/5,1)
  if policy!='financial': raise ValueError('Operating policy requires matched financing roll-forward; unsupported experimental branch removed')
  ebit=rev[t]*margin;nopat=ebit*(1-raw['tax'])
  sc=s['sc1'] if t<=5 else s['sc2']
  if t==11: inv=nopat*s['g']/s['roic']
  else:
   idx=t if lag==0 else min(t+1,11)
   inv=max(0,(rev[idx]-rev[idx-1])/sc)
  fcff=nopat-inv;wacc=d['wacc'] if t<=5 else d['wacc']+(d['wacc_terminal']-d['wacc'])*min((t-5)/5,1)
  if t<=10:cum*=1+wacc
  rows.append(dict(year=t,units=units[t] if t<=10 else None,revenue=rev[t],growth=rev[t]/rev[t-1]-1,margin=margin,ebit=ebit,tax=raw['tax'],nopat=nopat,sc=sc,reinvestment=inv,fcff=fcff,wacc=wacc,discount=1/cum,pv=fcff/cum,capital_begin=ic,capital_end=ic+inv,roic_existing=nopat/ic,roic_marginal_proxy=(nopat-(rows[-1]['nopat'] if rows else d['ebit_adjusted']*(1-raw['tax'])))/(rows[-1]['reinvestment'] if rows and rows[-1]['reinvestment'] else inv) if inv else None))
  ic+=inv
 tv=rows[-1]['fcff']/(d['wacc_terminal']-s['g'])
 if fade:
  nt=rows[9]['nopat'];pvfade=0;start=fade_start or s['roic']
  for n in range(1,fade+1):
   nt*=1+s['g'];r=start+(d['wacc_terminal']-start)*n/fade
   pvfade+=nt*(1-s['g']/r)/(1+d['wacc_terminal'])**n
  nt*=1+s['g'];tv=pvfade+nt*(1-s['g']/d['wacc_terminal'])/(d['wacc_terminal']-s['g'])/(1+d['wacc_terminal'])**fade
 ev=sum(r['pv'] for r in rows[:10])+tv/cum
 debt=d['lease'] if policy=='financial' else 0
 equity=ev+d['cash_total']+raw['long_investments']-debt-d['option_value'];value=max(0,equity/d['shares_total'])
 return dict(case=case,assumptions=s,derived=d,rows=rows,terminal_value=tv,pv_terminal=tv/cum,enterprise=ev,equity=equity,value=value,mos=value*.65,terminal_weight=tv/cum/ev)
def main():
 results={k:calculate(k) for k in SCENARIOS}
 base=results['Base'];D=derive();sens={}
 for name,xs,ys in [('wacc_g',[-.01,-.005,0,.005,.01],[-.01,-.005,0,.003,.006]),('roic_g',[-.04,-.02,0,.02,.04],[-.01,-.005,0,.003,.006]),('growth_margin',[-.01,-.005,0,.005,.01],[-.02,-.01,0,.01,.02])]:
  grid=[]
  for x in xs:
   row=[]
   for y in ys:
    if name=='roic_g':v=calculate(changes={'roic':.14+x,'g':.04+y})['value']
    elif name=='growth_margin':v=calculate(changes={'comps':[c+x for c in SCENARIOS['Base']['comps']],'margin':.185+y})['value']
    else:
     # Change all discount rates by x; operating forecasts are unchanged except stable growth.
     q=calculate(changes={'g':.04+y});cum=1;pv=0
     for r in q['rows'][:10]:cum*=1+r['wacc']+x;pv+=r['fcff']/cum
     tv=q['rows'][-1]['fcff']/(D['wacc_terminal']+x-(.04+y));v=(pv+tv/cum+D['cash_total']+RAW['long_investments']-D['lease']-D['option_value'])/D['shares_total']
    row.append(v)
   grid.append(row)
  sens[name]={'x':xs,'y':ys,'values':grid,'center':grid[2][2]}
 lo,hi=-.1,.2
 for _ in range(80):
  mid=(lo+hi)/2;v=calculate(changes={'comps':[mid]*10})['value']
  if v<RAW['price']:lo=mid
  else:hi=mid
 inverse={'constant_comps_needed':(lo+hi)/2,'value':v,'assumption':'Only comparable growth changes; openings, margin, reinvestment and terminal ROIC held fixed.'}
 duration=[{'start':start,'years':n,'value':calculate(fade=n,fade_start=start)['value']} for start in [.14,.20] for n in [5,10]]
 lag=[{'lag':n,'value':calculate(lag=n)['value']} for n in [0,1]]
 (P/'results.json').write_text(json.dumps({'results':results,'sensitivity':sens,'inverse':inverse,'duration':duration,'lag':lag,'sources':SOURCES,'raw':RAW},ensure_ascii=False,indent=2))
 print(json.dumps({'values':{k:{'value':v['value'],'mos':v['mos'],'units10':v['rows'][9]['units'],'revenue10':v['rows'][9]['revenue'],'reinv10':v['rows'][9]['reinvestment'],'reinv11':v['rows'][10]['reinvestment'],'tv_weight':v['terminal_weight']} for k,v in results.items()},'rates':{k:D[k] for k in ['rf','erp','wacc','wacc_terminal','ke','beta','lease_interest_proxy','capital']},'inverse':inverse,'lag':lag,'duration':duration},indent=2))
if __name__=='__main__':main()
