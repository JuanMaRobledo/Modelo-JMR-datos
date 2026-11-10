import sys,json,time
sys.path.insert(0,'.')
from eng import *
from concurrent.futures import ProcessPoolExecutor
W0=0.0768154743198044;P=34.43
def val(a):
    tag,story,over,coc=a
    try: return tag,run(story,over,tag,coc)['value']
    except Exception as e: return tag,None
def bis(tag,lo,hi,f,incr=True,n=11):
    for i in range(n):
        mid=(lo+hi)/2
        v=f(mid,f'{tag}{i}')
        if v is None: return None
        if (v<P)==incr: lo=mid
        else: hi=mid
    return (lo+hi)/2
GL=[0.068,0.078,0.088,0.098,0.108];ML=[0.14,0.15,0.16,0.17,0.18];DW=[-0.01,-0.005,0,0.005,0.01];TG=[0.03,0.035,0.04,0.045,0.048]
jobs=[]
for i,g in enumerate(GL):
    for j,m in enumerate(ML): jobs.append((f'a_{i}_{j}','base',{'B28':g,'B29':m},None))
for i,d in enumerate(DW):
    for j,t in enumerate(TG): jobs.append((f'b_{i}_{j}','base',{'B68':t},{'B11':'I will input','B12':W0+d}))
def r_growth(x,tag): return run('base',{'B26':x,'B28':x},'rg'+tag)['value']
def r_margin(x,tag): return run('base',{'B29':x},'rm'+tag)['value']
def r_g40(x,tag): return run('base',{'B26':x,'B28':x,'B29':0.18},'r4'+tag)['value']
def r_w(x,tag): return run('base',{},'rw'+tag,{'B11':'I will input','B12':x})['value']
def solve(k):
    return {'g':lambda:('crecimiento',bis('g',0.05,0.20,r_growth,True)),'m':lambda:('margen',bis('m',0.14,0.30,r_margin,True)),
            'g18':lambda:('crec_con_margen18',bis('h',0.05,0.20,r_g40,True)),'w':lambda:('wacc',bis('w',0.04,W0,r_w,False))}[k]()
if __name__=='__main__':
    t0=time.time();res={}
    with ProcessPoolExecutor(4) as ex:
        fs=[ex.submit(solve,k) for k in ('g','m','g18','w')]
        res.update(dict(ex.map(val,jobs)))
        for f in fs: k,v=f.result();res[k]=v
    json.dump(res,open('sens_res.json','w'));print(round(time.time()-t0),'s',res['crecimiento'],res['margen'],res['crec_con_margen18'],res['wacc'],sum(v is None for v in res.values()))
