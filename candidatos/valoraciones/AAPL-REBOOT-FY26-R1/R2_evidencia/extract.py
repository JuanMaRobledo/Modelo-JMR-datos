import json,datetime as dt
f=json.load(open('/tmp/claude-0/-home-user/b8c0d315-1e6b-524a-8878-fb2b853781cf/scratchpad/sec/facts.json'))['facts']
G=f['us-gaap']
FY=['2017-09-30','2018-09-29','2019-09-28','2020-09-26','2021-09-25','2022-09-24','2023-09-30','2024-09-28','2025-09-27','2026-09-26']
FY0='2016-09-24'
def D(s): return dt.date.fromisoformat(s)
def pick(tag,end,kind,unit='USD'):
    """valor de 10-K más reciente para el período que termina en 'end'. kind: 'flow' (≈1 año) o 'inst'"""
    if tag not in G: return None
    best=None
    for u,arr in G[tag]['units'].items():
        if u!=unit: continue
        for x in arr:
            if x['end']!=end or not x['form'].startswith('10-K'): continue
            if kind=='flow':
                if 'start' not in x: continue
                days=(D(x['end'])-D(x['start'])).days
                if days<350 or days>380: continue
            else:
                if 'start' in x: continue
            if best is None or x['filed']>best['filed']: best=x
    return None if best is None else (best['val'],best['accn'],best['filed'])
def V(tags,end,kind,unit='USD',scale=1e6):
    for t in ([tags] if isinstance(tags,str) else tags):
        r=pick(t,end,kind,unit)
        if r: return r[0]/scale,t,r[1]
    return None
if __name__=='__main__':
    for end in FY[:3]+[FY[-1]]:
        print(end,V('Revenues',end,'flow'),V('RevenueFromContractWithCustomerExcludingAssessedTax',end,'flow'))
