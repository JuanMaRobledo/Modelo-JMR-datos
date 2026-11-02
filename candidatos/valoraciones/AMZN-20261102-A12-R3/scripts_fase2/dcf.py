"""Replicador independiente del DCF FCFF (Damodaran Ginzu) para AMZN R2 — auditoría fase 4.
Lee entradas de la captura del auditor; no escribe en la hoja."""
from h import g
VO='Valuation output'
def base_inputs(row0=4):
    cols='CDEFGHIJKL'
    gr=[g(VO,f'{c}{row0}') for c in cols]          # crecimiento años 1-10
    mg=[g(VO,f'{c}{row0+2}') for c in cols]        # margen años 1-10
    tx=[g(VO,f'{c}{row0+4}') for c in cols]
    sc=[g(VO,f'{c}{row0+36}') for c in cols]       # S/C
    wc=[g(VO,f'{c}{row0+10}') for c in cols]
    return dict(rev0=g(VO,'B5'), gr=gr, mg=mg, tx=tx, sc=sc, wacc=wc,
                g=g(VO,'M4'), mg_t=g(VO,'M6'), tx_t=g(VO,'M8'), roic_t=g(VO,'M42'), wacc_t=g(VO,'M14'),
                debt=g(VO,'B27'), cash=g(VO,'B29'), nonop=g(VO,'B30'), minority=g(VO,'B28'),
                opt=g(VO,'B32'), shares=g(VO,'B34'))
def run(p, opt_mode='native'):
    rev=[p['rev0']]
    for x in p['gr']: rev.append(rev[-1]*(1+x))
    rev_t=rev[-1]*(1+p['g'])
    ebit=[r*m for r,m in zip(rev[1:],p['mg'])]
    nopat=[e*(1-t) for e,t in zip(ebit,p['tx'])]
    rev_ext=rev+[rev_t]
    reinv=[(rev_ext[i+2]-rev_ext[i+1])/p['sc'][i] for i in range(10)]   # lag 1
    fcff=[n-r for n,r in zip(nopat,reinv)]
    df=[];acc=1
    for w in p['wacc']: acc/= (1+w); df.append(acc)
    pv=sum(f*d for f,d in zip(fcff,df))
    nopat_t=rev_t*p['mg_t']*(1-p['tx_t'])
    fcff_t=nopat_t*(1-p['g']/p['roic_t'])
    tv=fcff_t/(p['wacc_t']-p['g']); pvtv=tv*df[-1]
    ops=pv+pvtv
    eq=ops-p['debt']-p['minority']+p['cash']+p['nonop']
    if opt_mode=='native': eqc=eq-p['opt']; ps=eqc/p['shares']
    elif opt_mode=='treasury': ps=eq/(p['shares']+p.get('rsu',223.3))
    elif opt_mode=='market': ps=(eq-p.get('rsu',223.3)*240.35)/p['shares']
    return dict(ps=ps, ops=ops, pv=pv, pvtv=pvtv, tv_share=pvtv/ops, eq=eq, fcff=fcff, fcff_t=fcff_t, reinv=reinv)
