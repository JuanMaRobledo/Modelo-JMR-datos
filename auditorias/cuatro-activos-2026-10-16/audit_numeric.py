"""Reconcile cached native DCF schedules independently; do not certify missing guards."""
from pathlib import Path
import json,math
P=Path(__file__).resolve().parent
all_reports={}
def close(a,b):return isinstance(a,(int,float)) and isinstance(b,(int,float)) and math.isclose(a,b,rel_tol=1e-7,abs_tol=1e-6)
for ticker in ['CMG','DUOL','NKE','NFLX']:
    s=json.loads((P/'candidate'/f'{ticker}-snapshot.json').read_text());v=s['values'];f=s['formulas'];checks=[]
    def c(tab,addr):
        import re
        m=re.fullmatch(r'([A-Z]+)(\d+)',addr);j=0
        for ch in m[1]:j=j*26+ord(ch)-64
        a=v.get(tab,[]);i=int(m[2])-1
        return a[i][j-1] if i<len(a) and j<=len(a[i]) else None
    def chk(code,a,b):checks.append({'code':code,'pass':close(a,b),'actual':a,'expected':b})
    records=list((P/'current'/'valoraciones').glob(ticker+'-*.json'))
    if ticker=='DUOL':records=[p for p in records if '1791409167000' in p.name]
    rec=json.loads(records[0].read_text());hs=rec['valorEsperado']['historias']
    outputs={}
    for name,offset in [('Base',0),('Conservador',51),('Optimista',102),('Disrupción',155)]:
        tab='Valuation output';o=offset
        if ticker=='NFLX' and name=='Disrupción':tab='DCF Disrupción NFLX';o=0
        def x(row,col='B'):return c(tab,col+str(row+o))
        for col in 'CDEFGHIJKL':
            prev=chr(ord(col)-1)
            nol=x(12,prev) or 0
            chk(name+'_'+col+'_NOPAT',x(9,col),x(7,col)-max(0,x(7,col)-nol)*x(8,col))
            chk(name+'_'+col+'_FCFF',x(11,col),x(9,col)-x(10,col))
            chk(name+'_'+col+'_PV',x(16,col),x(11,col)*x(15,col))
        chk(name+'_PV_10Y',x(22),sum(x(16,col) for col in 'CDEFGHIJKL'))
        chk(name+'_PV_TOTAL',x(23),x(21)+x(22))
        chk(name+'_EQUITY_BRIDGE',x(31),x(26)-x(27)-x(28)+x(29)+x(30))
        pref=c('Input sheet','B76') or 0
        chk(name+'_CLAIMS',x(33),x(31)-x(32)-pref)
        chk(name+'_PER_SHARE',x(35),x(33)/x(34))
        story=next(h for h in hs if (h.get('id')=={'Base':'A','Conservador':'B','Optimista':'D','Disrupción':'C'}[name]) ) if ticker in ['NKE','NFLX','DUOL'] else next(h for h in hs if h['nombre'].startswith({'Base':'Base','Conservador':'Conservadora','Optimista':'Optimista','Disrupción':'Disrupción'}[name]))
        chk(name+'_PUBLISHED',story['valor'],x(35));outputs[name]=x(35)
    w=c('Cost of capital worksheet','B62')*c('Cost of capital worksheet','B63')+c('Cost of capital worksheet','C62')*c('Cost of capital worksheet','C63')+(c('Cost of capital worksheet','D62') or 0)*(c('Cost of capital worksheet','D63') or 0)
    chk('WACC_WEIGHTS',sum((c('Cost of capital worksheet',k) or 0) for k in ['B62','C62','D62']),1)
    chk('WACC_RECONCILIATION',c('Cost of capital worksheet','E63'),w)
    chk('WACC_INPUT',c('Input sheet','B36'),w)
    if ticker!='NFLX':
        chk('PROBABILITIES',sum(h['probabilidad'] for h in hs),1)
        chk('EXPECTED',rec['valorEsperado']['valor'],sum(h['probabilidad']*h['valor'] for h in hs))
    option=c('Option value','B30');claims=c('Valuation output','B32')
    checks.append({'code':'OPTION_VALUE_DEDUCTED','pass':c('Input sheet','B38')=='No' and close(claims,0) or c('Input sheet','B38')=='Yes' and isinstance(option,(int,float)) and claims>=option-1e-6,'option':option,'deductionIncludingOtherClaims':claims})
    report={'ticker':ticker,'status':'ARITHMETIC_PASS' if all(x['pass'] for x in checks) else 'ARITHMETIC_FAIL','checks':checks,'failures':[x for x in checks if not x['pass']],'outputs':outputs,'optionValue':option,'nativeMOS':c('Resumen de Valoración','G4'),'baseMOSPrice':outputs['Base']*(1-c('Resumen de Valoración','G4')),'scope':'Reconciles native cached schedules, equity bridge, WACC and published scenarios. Does not replace canonical gate audit, source review or Google recalculation.'}
    all_reports[ticker]=report
    (P/'candidate'/f'{ticker}-numerical.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({t:{'status':r['status'],'checks':len(r['checks']),'failures':r['failures']} for t,r in all_reports.items()},ensure_ascii=False,indent=2))
