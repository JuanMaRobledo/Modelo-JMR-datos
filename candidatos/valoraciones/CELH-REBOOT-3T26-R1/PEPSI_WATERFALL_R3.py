#!/usr/bin/env python3
"""CELH Floyd R3. Reproducible research pricing of Pepsi A/B preferred claims.
Standalone, stdlib only; does NOT modify Ginsu or Google Sheets.
Forecasting assumptions and exclusions: PEPSI_ECONOMICO_R3_V2.json.
"""
import json, math, sys
from datetime import date
from functools import lru_cache
from statistics import NormalDist

REV='CELH-REBOOT-3T26-R1'
VALUE_DATE=date(2026,11,10)
T31=(date(2031,8,28)-VALUE_DATE).days/365.25
T32=(date(2032,8,28)-VALUE_DATE).days/365.25
R=.0488; SIGMA=.54; Q=.75; CREDIT=.09
SHARES=251.725; SPOT=33.19
PREF={'A':(550.,25.,22.), 'B':(585.,51.75,11.3)}
EQ={'Conservadora':4442.90687213692,'Base':7995.429897101783,'Optimista':12584.920113229273}

@lru_cache(maxsize=6)
def gauss_nodes(n):
    nd=NormalDist()
    return [nd.inv_cdf((i+.5)/n) for i in range(n)]

def cdf(x):return .5*(1+math.erf(x/math.sqrt(2)))

def coupons(p,stop,discount,start=0.):
    return sum(.05*p*.25*math.exp(-discount*.25*k)
      for k in range(1,round(stop/.25)+1) if start+1e-10 < .25*k <= stop+1e-10)

def redemption(p,t0,discount):
    instants=[t0,t0+1.25,t0+2.5]
    principal=sum((p/3)*math.exp(-discount*t) for t in instants)
    coupon=0.
    for k in range(1,round(instants[-1]/.25)+1):
        t=.25*k
        if t<=t0:continue
        fraction=2/3 if t<=instants[1] else 1/3
        coupon+=p*fraction*.05*.25*math.exp(-discount*t)
    return principal+coupon

def preferred_claim(stock,kind,vol=SIGMA,q=Q,credit=CREDIT,redemption_first=2032,n=8192):
    p,k,shares=PREF[kind]
    if vol<=0 or credit<=0 or not 0<=q<=1: raise ValueError('assumptions invalid')
    t_red=(date(redemption_first,8,28)-VALUE_DATE).days/365.25
    if t_red<T32:raise ValueError('redemption before contract')
    cash_red=redemption(p,t_red,credit)
    c31=coupons(p,T31,credit);c32=coupons(p,T32,credit)
    if t_red>T32:c32+=coupons(p,t_red,credit,start=T32)
    d31=math.exp(-R*T31);d32=math.exp(-R*T32)
    dt=T32-T31;sd=vol*math.sqrt(dt)
    parts={'coupon':0.,'conversion':0.,'redemption':0.,
           'prob_early':0.,'prob_late':0.,'prob_redemption':0.}
    for z in gauss_nodes(n):
        s31=stock*math.exp((R-.5*vol*vol)*T31+vol*math.sqrt(T31)*z)
        d2=(math.log(s31/k)+(R-.5*vol*vol)*dt)/sd
        prob=cdf(d2)
        expected_inmoney=s31*math.exp(R*dt)*cdf(d2+sd)
        early=q if s31>k else 0.
        deferred=1-early
        parts['coupon']+=early*c31+deferred*c32
        parts['conversion']+=early*shares*s31*d31+deferred*shares*d32*expected_inmoney
        parts['redemption']+=deferred*(1-prob)*cash_red
        parts['prob_early']+=early
        parts['prob_late']+=deferred*prob
        parts['prob_redemption']+=deferred*(1-prob)
    for key in parts:parts[key]/=n
    parts['value']=parts['coupon']+parts['conversion']+parts['redemption']
    return parts

def market_claim(stock=SPOT,vol=SIGMA,q=Q,credit=CREDIT,redemption_first=2032,n=8192):
    a=preferred_claim(stock,'A',vol,q,credit,redemption_first,n)
    b=preferred_claim(stock,'B',vol,q,credit,redemption_first,n)
    total=a['value']+b['value']
    return {'A':a,'B':b,'total':total,
       'common_by_scenario':{key:(e-total)/SHARES for key,e in EQ.items()},
       'base_MOS35':.65*(EQ['Base']-total)/SHARES}

def fixed_point(e,vol=SIGMA,q=Q,credit=CREDIT,n=8192):
    lo=.01;hi=e/SHARES
    for i in range(44):
        m=(lo+hi)/2
        a=preferred_claim(m,'A',vol,q,credit,n=n)['value']
        b=preferred_claim(m,'B',vol,q,credit,n=n)['value']
        if m*SHARES+a+b>e: hi=m
        else:lo=m
    return (lo+hi)/2

def main():
    n=int(sys.argv[1]) if len(sys.argv)>1 else 8192
    m=market_claim(n=n)
    assert abs(m['A']['value']+m['B']['value']-m['total'])<1e-7
    for s in ('A','B'):
        d=m[s]
        assert abs(d['prob_early']+d['prob_late']+d['prob_redemption']-1)<1e-8
    diagnostics={'revisionId':REV,'source':'SEC 10-Q 2026-09-30, Note 12',
      'result':'PRELIMINAR, market price anchor, not issuer Monte Carlo valuation',
      'n':n,'market':m,'fixed_point':{k:fixed_point(v,n=n) for k,v in EQ.items()}}
    print(json.dumps(diagnostics,indent=2,ensure_ascii=False))
if __name__=='__main__':main()
