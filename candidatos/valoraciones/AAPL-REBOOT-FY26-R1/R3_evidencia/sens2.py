import sys,json,time
sys.path.insert(0,'/tmp/claude-0/-home-user/b8c0d315-1e6b-524a-8878-fb2b853781cf/scratchpad')
from engine import *
from concurrent.futures import ProcessPoolExecutor
W0=0.1025195876573334
def job(a):
    tag,over,coc=a
    try: return tag,run('base',over,tag,coc)['value']
    except Exception: return tag,None
def solvew(_):
    lo,hi=0.05,W0
    for i in range(12):
        mid=(lo+hi)/2
        v=run('base',{}, 'rvw',{'B11':'I will input','B12':mid})['value']
        if v<342.37: hi=mid
        else: lo=mid
    return 'wacc_inverso',(lo+hi)/2
G=[0.035,0.045,0.055,0.065,0.075];M=[0.33,0.35,0.37,0.39,0.41]
DW=[-0.01,-0.005,0,0.005,0.01];TG=[0.03,0.035,0.04,0.045,0.048]
jobs=[]
for i,g in enumerate(G):
    for j,m in enumerate(M): jobs.append((f'a_{i}_{j}',{'B28':g,'B29':m},None))
for i,d in enumerate(DW):
    for j,t in enumerate(TG): jobs.append((f'b_{i}_{j}',{'B68':t},{'B11':'I will input','B12':W0+d}))
if __name__=='__main__':
    t0=time.time()
    with ProcessPoolExecutor(4) as ex:
        f=ex.submit(solvew,0)
        res=dict(ex.map(job,jobs))
        k,v=f.result();res[k]=v
    json.dump(res,open('sens2_res.json','w'));print('listo',round(time.time()-t0),'s',sum(x is None for x in res.values()),'fallos',res[k])
