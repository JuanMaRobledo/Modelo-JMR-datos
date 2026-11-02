import json, sys, hashlib
sys.path[:0]=['.', 'scripts']
from jmr_valuation.io.sheets_auth import get_gspread_client
SID='1h6Xv5cNqwtKPpqI81KiZ_FNpTl4k_uQQS2QJEHphaBI'
sh=get_gspread_client().open_by_key(SID)
titles=[w.title for w in sh.worksheets()]
out={'sheet_id':SID,'title':sh.title,'tabs':titles,'values':{},'formulas':{}}
rng=[f"'{t}'" for t in titles]
for opt,key in (('UNFORMATTED_VALUE','values'),('FORMULA','formulas')):
    r=sh.values_batch_get(rng, params={'valueRenderOption':opt,'dateTimeRenderOption':'FORMATTED_STRING'})['valueRanges']
    for t,v in zip(titles,r): out[key][t]=v.get('values',[])
p=sys.argv[1]; json.dump(out,open(p,'w'),ensure_ascii=False)
print(hashlib.sha256(open(p,'rb').read()).hexdigest())
