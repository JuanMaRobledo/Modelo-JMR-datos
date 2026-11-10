"""Cargador genérico SEC XBRL → libro HISTÓRICOS Reboot (10 FY + LTM desde 10-Q). Valores en millones."""
import json,datetime as dt
D=lambda s:dt.date.fromisoformat(s)
class SEC:
    def __init__(s,path,fy_ends,ltm_end,ltm_prior_end,ytd_start,ytd_prior_start,prior_fy_end):
        j=json.load(open(path))['facts']; s.G=j['us-gaap']; s.DEI=j.get('dei',{})
        s.fy=fy_ends; s.ltm=ltm_end; s.ltm0=ltm_prior_end; s.ys=ytd_start; s.yps=ytd_prior_start; s.last_fy=prior_fy_end
    def _arr(s,tag,unit='USD'):
        return s.G.get(tag,{}).get('units',{}).get(unit,[])
    def flow(s,tags,start,end,forms=('10-K',),dmin=350,dmax=380,unit='USD'):
        for t in ([tags] if isinstance(tags,str) else tags):
            best=None
            for x in s._arr(t,unit):
                if x['end']!=end or 'start' not in x or not x['form'].startswith(forms): continue
                dd=(D(x['end'])-D(x['start'])).days
                if start is not None and x['start']!=start: continue
                if start is None and not(dmin<=dd<=dmax): continue
                if best is None or x['filed']>best['filed']: best=x
            if best: return best['val'],t,best['accn']
        return None
    def inst(s,tags,end,forms=('10-K','10-Q'),unit='USD'):
        for t in ([tags] if isinstance(tags,str) else tags):
            best=None
            for x in s._arr(t,unit):
                if x['end']!=end or 'start' in x or not x['form'].startswith(forms): continue
                if best is None or x['filed']>best['filed']: best=x
            if best: return best['val'],t,best['accn']
        return None
    def series_flow(s,tags,scale=1e6,neg=False,unit='USD'):
        """FY (10) + LTM: FY_last + YTD_actual − YTD_prior."""
        out=[];src=[]
        for e in s.fy:
            r=s.flow(tags,None,e,unit=unit); out.append(None if r is None else r[0]/scale*(-1 if neg else 1)); src.append(None if r is None else (r[1],r[2]))
        a=s.flow(tags,s.ys,s.ltm,forms=('10-Q','10-K'),unit=unit); b=s.flow(tags,s.yps,s.ltm0,forms=('10-Q','10-K'),unit=unit)
        if out[-1] is not None and a and b: out.append((out[-1]*(-1 if neg else 1)*scale+a[0]-b[0])/scale*(-1 if neg else 1)); src.append(('LTM',a[2]))
        else: out.append(None); src.append(None)
        return out,src
    def series_inst(s,tags,scale=1e6,unit='USD'):
        out=[];src=[]
        for e in s.fy+[s.ltm]:
            r=s.inst(tags,e,unit=unit); out.append(None if r is None else r[0]/scale); src.append(None if r is None else (r[1],r[2]))
        return out,src
    def inst_at(s,tags,end,scale=1e6): 
        r=s.inst(tags,end); return None if r is None else r[0]/scale
def add(*xs):
    n=len(xs[0]); o=[]
    for i in range(n):
        v=[x[i] for x in xs if x[i] is not None]
        o.append(None if not v else sum(v))
    return o
def sub(a,*bs):
    o=[]
    for i,x in enumerate(a):
        if x is None: o.append(None); continue
        o.append(x-sum((b[i] or 0) for b in bs))
    return o

def dei_shares(S,years,ltm_year,ltm_fp='Q3'):
    arr=S.DEI.get('EntityCommonStockSharesOutstanding',{}).get('units',{}).get('shares',[])
    out=[]
    for y in years:
        c=[x for x in arr if x['form']=='10-K' and x.get('fy')==y and x.get('fp')=='FY']
        out.append(None if not c else max(c,key=lambda x:x['filed'])['val']/1e6)
    c=[x for x in arr if x['form']=='10-Q' and x.get('fy')==ltm_year and x.get('fp')==ltm_fp]
    out.append(None if not c else max(c,key=lambda x:x['filed'])['val']/1e6)
    return out
