import sys,json,time
sys.path.insert(0,'/tmp/claude-0/-home-user/b8c0d315-1e6b-524a-8878-fb2b853781cf/scratchpad')
from engine import *
from concurrent.futures import ProcessPoolExecutor
P=342.37
def solve(a):
    name,lo,hi,mk=a
    for i in range(11):
        mid=(lo+hi)/2
        over,coc=mk(mid)
        v=run('base',over,f'rv_{name}',coc)['value']
        if v is None: return name,None
        if v<P: lo=mid
        else: hi=mid
    return name,(lo+hi)/2
def mk_g(g): return {'B26':g,'B28':g},None
def mk_m(m): return {'B29':m},None
def mk_gm(g): return {'B26':g,'B28':g,'B29':0.40},None
def mk_w(w): return {},{'B11':'I will input','B12':w}
if __name__=='__main__':
    t0=time.time()
    jobs=[('crecimiento',0.06,0.40,mk_g),('margen',0.37,0.80,mk_m),('crec_con_margen40',0.06,0.40,mk_gm),('wacc',0.04,0.1025,mk_w)]
    with ProcessPoolExecutor(4) as ex: res=dict(ex.map(solve,jobs))
    json.dump(res,open('rev_res.json','w'));print(res,round(time.time()-t0),'s')
