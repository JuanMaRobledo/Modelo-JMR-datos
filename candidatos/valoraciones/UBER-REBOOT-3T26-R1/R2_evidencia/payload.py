import sys,json;sys.path.insert(0,'.')
from mapping import *
def mk(mod,tk,prices,inv_tag,nci_tags):
    S,cfg,FY=mod.S,mod.cfg,mod.FY
    DS,SRC=build(S,cfg)
    # ST debt None→0 si hay TCL
    DS[(BS,20)]=[0.0 if (v is None and DS[(BS,24)][i] is not None) else v for i,v in enumerate(DS[(BS,20)])]
    r=lambda xs:[None if v is None else round(v,3) for v in xs]
    P={}
    P['IS']=[f"'Income Statement'!B3:L27",[r(DS.get((IS,i),[None]*11)) if (IS,i) in DS else [None]*11 for i in range(3,28)]]
    P['BS']=[f"'Balance Sheet'!B3:L36",[r(DS[(BS,i)]) if (BS,i) in DS else [None]*11 for i in range(3,37)]]
    P['CF']=[f"'Cash Flow Statement'!B3:L40",[r(DS[(CF,i)]) if (CF,i) in DS else [None]*11 for i in range(3,41)]]
    inv,_=S.series_inst(inv_tag);nci=add(*[S.series_inst(t)[0] for t in nci_tags]) if nci_tags else [0.0]*11
    nci=[0.0 if v is None else v for v in nci]
    P['AUX']=["'Entradas históricas auxiliares'!B3:L5",[r([0.0 if v is None else v for v in inv]),r(nci),[0.0]*11]]
    def open_at(end):
        g=lambda t:S.inst_at(t,end)
        a=lambda *ts: (lambda xs: None if all(x is None for x in xs) else sum(x or 0 for x in xs))([g(t) for t in ts])
        return [g('Assets'),(g('StockholdersEquity') if g('StockholdersEquity') is None else g('StockholdersEquity')+(g(nci_tags[0]) or 0 if nci_tags else 0)),
          a(*(cfg.get('std') or ['LongTermDebtCurrent'])),a(*cfg['lease_c']),a(*(cfg.get('ltd') or ['LongTermDebtNoncurrent'])),a(*cfg['lease_nc']),
          None if g(cfg['cash']) is None else g(cfg['cash'])+(a(*cfg['sti']) or 0),g(cfg['ar']) if isinstance(cfg['ar'],str) else a(*cfg['ar']),g('AccountsPayableCurrent'),
          a(inv_tag),a(*(cfg['ppe'] if isinstance(cfg['ppe'],list) else [cfg['ppe']])),a(*(cfg.get('intang') or [])) if cfg.get('intang') else None,g('Goodwill'),g('LiabilitiesCurrent')]
    def z(v):
        if v[0] is None: return v
        return [x if (x is not None or i not in (2,3,4,5,9,10,11)) else 0.0 for i,x in enumerate(v)]
    prev='2015-12-31'
    P['AUX_B']=["'Entradas históricas auxiliares'!B17:B30",[[None if v is None else round(v,3)] for v in z(open_at(prev))]]
    P['AUX_L']=["'Entradas históricas auxiliares'!L17:L30",[[None if v is None else round(v,3)] for v in z(open_at(S.ltm0))]]
    P['PX']=["'Trailing Valuation'!B3:L3",[prices]]
    return P,DS,SRC
if __name__=='__main__':
    import cmg,uber
    px_cmg=[7.5464,5.7806,8.6358,16.7422,27.7342,34.9650,27.7498,45.7392,60.3,37.0,34.43]
    px_ub=[None,None,None,29.74,51.0,41.93,24.73,61.57,60.32,81.71,68.59]
    out={}
    for tk,mod,px,inv,nci in (('CMG',cmg,px_cmg,'InventoryNet',None),('UBER',uber,px_ub,'InventoryNet',['NonredeemableNoncontrollingInterest'])):
        P,DS,SRC=mk(mod,tk,px,inv,nci);out[tk]=P
        json.dump(P,open(f'payload_{tk}.json','w'))
        json.dump({f'{k[0]}|{k[1]}':[v[0],str(v[1])] for k,v in SRC.items()},open(f'fuentes_{tk}.json','w'))
        print(tk,{k:(v[0],len(json.dumps(v[1]))) for k,v in P.items()})
        print(' AUX_B',P['AUX_B'][1]);print(' AUX_L',P['AUX_L'][1])
