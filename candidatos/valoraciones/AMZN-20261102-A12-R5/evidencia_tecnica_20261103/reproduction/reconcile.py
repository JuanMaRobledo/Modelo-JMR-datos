import json
from pathlib import Path
P=Path(__file__).parent
result=json.loads((P/'independent_results.json').read_text())
rows={t:{i:values for i,lab,values in rs}for t,rs in result['financial_rows'].items()}
IS,BS,CF=[rows[t]for t in ('Income Statement','Balance Sheet','Cash Flow Statement')]
def sumrows(tab,rs,j):return sum(tab[r][j]for r in rs if isinstance(tab[r][j],(int,float)))
checks={}
for name,fun in {
 'EBIT':lambda j:IS[3][j]-sumrows(IS,[5,8,10,11],j)-IS[12][j],
 'CFO':lambda j:sumrows(CF,range(3,13),j)-CF[13][j],
 'CFI':lambda j:sumrows(CF,range(15,22),j)-CF[22][j],
 'CFF':lambda j:sumrows(CF,[28,30,33],j)-CF[34][j],
 'Cash_change_including_FX_row39':lambda j:sumrows(CF,[13,22,34,39],j)-CF[40][j],
 'Assets_liabilities_equity':lambda j:BS[16][j]-BS[29][j]-BS[35][j],
 'Current_assets':lambda j:sumrows(BS,[5,6,9],j)-BS[10][j],
 'Current_liabilities':lambda j:sumrows(BS,[18,19,20,21,22],j)-BS[24][j],
}.items():
 checks[name]={'differences':[fun(j)for j in range(11)]}
 checks[name]['passes']=sum(abs(x)<1e-6 for x in checks[name]['differences'])
checks['ltm_growth']={'current_ltm':797455,'prior_ltm':637959+503538-450167,'correct':797455/(637959+503538-450167)-1,'input_I26_before':0.15250837032636233,'income_L4_before':0.11232850343969525}
checks['capex']={'gross':215192,'incentives':4535,'net':215192-4535,'fcf':168300-(215192-4535)}
(P/'reconciliations.json').write_text(json.dumps(checks,indent=2))
print(json.dumps(checks,indent=2))
