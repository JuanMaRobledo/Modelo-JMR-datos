import json, math
from pathlib import Path
P=Path(__file__).parent
d=json.loads((P/'resultados_finales.json').read_text()); base=d['scenarios'][0]
def calc(nimshock=0,riskshock=0,capitalshock=0,rwagshock=0,ocishock=0,keshock=0,g=.04,earnings=1,noothercapital=False):
 book=16879747;rwa=145082745;exposure=244806078;adj=1751418;cet=17605250;assets=195575.016;loans=174709.257;other=2841.482;cost=7696.57;factor=1;pv=0;nci=16.622/945.329
 for y in range(1,11):
  f=max(0,y-5)/5;growth=.07+(g-.07)*f;rwg=.07+rwagshock+(g-.07-rwagshock)*f
  oldassets=assets;assets*=1+growth;loans*=1+growth;other*=1+.05+(g-.05)*f;cost*=1+.04+(g-.04)*f
  nim=.0576+(.057+nimshock-.0576)*y/10;risk=3376.052/174709.257+(.02+riskshock-3376.052/174709.257)*y/10;tax=476.01/1421.339+(.35-476.01/1421.339)*f
  pbt=(oldassets+assets)/2*nim-loans*risk+other-cost;ni=(pbt-max(0,pbt)*tax)*(1-nci)*1000*earnings
  oldadj=adj;rwa*=1+rwg;exposure*=1+growth;adj=1751418*rwa/145082745
  at1=0 if noothercapital else 1731178;t2=0 if noothercapital else 3996219*max(0,1-y/9)
  need=max(.12*rwa,.105*rwa-at1,(.14+capitalshock)*rwa-at1-t2+8,.05*exposure-at1)
  oci=ocishock if y==1 else 0;retain=max(0,(need-cet-oci+adj-oldadj)*(1-nci));cet+=retain/(1-nci)+oci-adj+oldadj;book+=retain+oci*(1-nci)
  ke=d['rf']+(.7+.3*f)*d['erp']+d['crp']+keshock;factor*=1+ke;pv+=(ni-retain)/factor
 ret11=((.14+capitalshock)*rwa+adj)*g*(1-nci);ni11=ni*(1+g);kt=d['rf']+d['erp']+d['crp']+keshock
 pv+=max(0,ni11-ret11)/(kt-g)/factor
 return pv*1e6/487670413
assert abs(calc()-base['value'])<1e-7
cases=[('NIM estable−25pb',dict(nimshock=-.0025)),('NIM estable+25pb',dict(nimshock=.0025)),('Deterioro estable+25pb',dict(riskshock=.0025)),('Deterioro estable−25pb',dict(riskshock=-.0025)),('Meta solvencia total+1pp',dict(capitalshock=.01)),('RWA crecimiento inicial+1pp',dict(rwagshock=.01)),('OCI inicial−COP700.000m',dict(ocishock=-700000)),('Ke toda curva+1pp',dict(keshock=.01)),('Ke toda curva−1pp',dict(keshock=-.01)),('Sin AT1 ni Tier2 desdeFY1',dict(noothercapital=True)),('g estable2%',dict(g=.02)),('g estable3%',dict(g=.03)),('g estable5%',dict(g=.05))]
results=[dict(name=n,value=calc(**p),change=calc(**p)/base['value']-1) for n,p in cases]
def bisect(f,lo,hi,target):
 for _ in range(100):
  mid=(lo+hi)/2
  if f(mid)>target:hi=mid
  else:lo=mid
 return(lo+hi)/2
earn=bisect(lambda x:calc(earnings=x),.1,4,30800)
# Ke value decreases with shift; reverse sign for monotone bisection.
ke_minus=bisect(lambda x:calc(keshock=-x),0,.10,30800)
out={'economic':results,'inverse_earnings_multiplier':earn,'inverse_ke_parallel_reduction':ke_minus,'inverse_initial_ke':base['keInitial']-ke_minus,'inverse_terminal_ke':base['keTerminal']-ke_minus}
(P/'sensibilidades_finales.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
