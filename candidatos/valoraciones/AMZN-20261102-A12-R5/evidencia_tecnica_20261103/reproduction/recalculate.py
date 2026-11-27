import json,math
from pathlib import Path
P=Path(__file__).parent
tabs={}
for s in json.loads((P/'r5_formulas.json').read_text()):
    g={}
    for b in s.get('data',[]):
        for i,row in enumerate(b.get('rowData',[]),b.get('startRow',0)):
            for j,c in enumerate(row.get('values',[]),b.get('startColumn',0)):g[i+1,j+1]=next(iter(c.get('effectiveValue',{}).values()),None)
    tabs[s['properties']['title']]=g
v=tabs['Valuation output'];results={}
for name,offset in [('Base',0),('Conservadora',51),('Optimista',102),('Disrupcion',155)]:
    f=lambda r,c:v[r+offset,c]
    disc=1;pv=0;errors=[]
    for c in range(3,13):
        fcff=f(9,c)-f(10,c);disc/=1+f(14,c);pv+=fcff*disc
        errors.extend([fcff-f(11,c),disc-f(15,c),fcff*disc-f(16,c)])
    terminal=f(11,13)/(f(19,2)-f(4,13))
    ev=(pv+terminal*disc)*(1-f(24,2))+f(25,2)*f(24,2)
    common=ev-f(27,2)-f(28,2)+f(29,2)+f(30,2)-f(32,2)-(tabs['Input sheet'].get((76,2)) or 0)
    price=common/f(34,2)
    results[name]={'recalculated':price,'native':f(35,2),'difference':price-f(35,2),'max_projection_difference':max(map(abs,errors))}
c=tabs['Cost of capital worksheet']
results['WACC']={'recalculated':sum(c[62,j]*c[63,j]for j in (2,3,4)),'native':c[14,2]}
r=tabs['R& D converter'];life=r[7,6];current=r[8,6]
asset=current+sum(r[11+i,2]*(1-i/life)for i in range(1,int(life)+1))
amort=sum(r[11+i,2]/life for i in range(1,int(life)+1))
results['RD']={'asset_recalculated':asset,'amortization_recalculated':amort,'EBIT_adjustment_recalculated':current-amort}
(P/'recalculation.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
