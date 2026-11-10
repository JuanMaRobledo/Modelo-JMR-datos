from hlib import *
IS,BS,CF='Income Statement','Balance Sheet','Cash Flow Statement'
def build(S,cfg):
    """cfg: dict con tags por empresa. Devuelve (dataset{(hoja,fila):[11]}, fuentes{(hoja,fila):(etiqueta,[src])}, avisos)"""
    DS={};SRC={};W=[]
    def put(sh,r,label,vals,src='derivado'): DS[(sh,r)]=vals; SRC[(sh,r)]=(label,src)
    def fl(tags,neg=False,unit='USD',scale=1e6): v,s=S.series_flow(tags,neg=neg,unit=unit,scale=scale); return v,s
    def it(tags): v,s=S.series_inst(tags); return v,s
    z=lambda: [0.0]*11
    # ---- Estado de resultados
    rev,s=fl(cfg['rev']);put(IS,3,'Total Revenues',rev,s)
    cost=add(*[fl(t)[0] for t in cfg['cost']]);put(IS,5,'Cost of Sales: '+'+'.join(cfg['cost_names']),cost,cfg['cost'])
    sga=add(*[fl(t)[0] for t in cfg['sga']]);put(IS,8,'SG&A: '+'+'.join(cfg['sga_names']),sga,cfg['sga'])
    da,s=fl(cfg['da']);put(IS,9,'D&A (línea del estado de resultados)' if cfg.get('da_in_is') else 'D&A (flujo de caja)',da if cfg.get('da_in_is') else [None]*11,s)
    rd,s=fl(cfg['rd']) if cfg.get('rd') else ([0.0]*11,'sin I+D');put(IS,10,'R&D',rd,s)
    ebit,s=fl(cfg['ebit']);put(IS,12,'Operating Profit',ebit,s)
    da_is=da if cfg.get('da_in_is') else [0.0]*11
    oth=[None if None in(a,b,c,d,e,f) else round(a-b-c-d-e-f,3) for a,b,c,d,e,f in zip(rev,cost,sga,da_is,rd,ebit)]
    put(IS,11,'Other Operating Expenses (derivado: ventas−costo−SG&A−D&A−I+D−EBIT) = '+cfg['other_names'],oth)
    ii,s=fl(cfg['int_inc']) if cfg.get('int_inc') else ([None]*11,None);put(IS,14,'Interest and Investment Income',ii,s)
    ie,s=fl(cfg['int_exp'],neg=False) if cfg.get('int_exp') else ([None]*11,None);put(IS,15,'Interest Expense',ie,s)
    pbt,s=fl(cfg['pbt']);put(IS,19,'Pretax Income',pbt,s)
    nonop=[None if None in (a,b) else a-b for a,b in zip(pbt,ebit)];put(IS,18,'Total Non-Operating Income (derivado: antes de impuestos − EBIT)',nonop)
    put(IS,17,'Non-Operating Income (resto)',[None if n is None else n-((a or 0)-(abs(b) if b else 0)) for n,a,b in zip(nonop,ii,ie)])
    tax,s=fl(cfg['tax']);put(IS,20,'Income Taxes',tax,s)
    ni,s=fl(cfg['ni']);put(IS,21,'Consolidated Net Income',fl(cfg['ni_cons'])[0] if cfg.get('ni_cons') else ni,s);put(IS,22,'NI to common',ni,s)
    bsh,s=fl(cfg['bsh'],scale=1e6,unit='shares');dsh,s2=fl(cfg['dsh'],unit='shares')
    for i,y in enumerate(S.fy):
        if y<cfg.get('split_before','0000'):
            if bsh[i] is not None: bsh[i]*=cfg['split_f']
            if dsh[i] is not None: dsh[i]*=cfg['split_f']
    put(IS,25,'Basic wtd shares',bsh,s);put(IS,26,'Diluted wtd shares',dsh,s2)
    # acciones al cierre: dei cover (último) + XBRL
    so=dei_shares(S,[int(y[:4]) for y in S.fy],int(S.ltm[:4]));put(IS,27,'Shares Outstanding (portada del 10-K/10-Q; dei:EntityCommonStockSharesOutstanding)',so,'dei')
    # ---- Balance
    cash,s=it(cfg['cash']);put(BS,3,'Cash',cash,s)
    sti,s=it(cfg['sti']);put(BS,4,'ST investments',sti,s)
    ar,s=it(cfg['ar']);put(BS,6,'AR',ar,s)
    tca,s=it('AssetsCurrent');put(BS,10,'Total current assets',tca,s)
    oca=[None if None in(t,c) else round(t-c-(a or 0)-(r or 0),3) for t,c,a,r in zip(tca,cash,sti,ar)];put(BS,9,'Other current assets (derivado: AC − caja − inv. CP − CxC)',oca)
    ppe,s=it(cfg['ppe']);put(BS,11,'PPE net',ppe,s)
    ia,s=it(cfg['intang']) if cfg.get('intang') else ([None]*11,None);put(BS,12,'Intangibles',ia,s)
    gw,s=it('Goodwill');put(BS,13,'Goodwill',gw,s)
    lti,s=(add(*[it(t)[0] for t in cfg['lti_sum']]),cfg['lti_sum']) if cfg.get('lti_sum') else (it(cfg['lti']) if cfg.get('lti') else ([None]*11,None));put(BS,14,'LT investments: '+cfg.get('lti_name','—'),lti,s)
    ta,s=it('Assets');put(BS,16,'Total assets',ta,s)
    olta=[None if None in(t,c,p) else round(t-c-p-(i or 0)-(g or 0)-(l or 0),3) for t,c,p,i,g,l in zip(ta,tca,ppe,ia,gw,lti)];put(BS,15,'Other LT assets (derivado)',olta)
    ap,s=it('AccountsPayableCurrent');put(BS,18,'AP',ap,s)
    acc,s=it(cfg['accrued']) if cfg.get('accrued') else ([None]*11,None);put(BS,19,'Accrued',acc,s)
    std,s=it(cfg['std']) if cfg.get('std') else ([0.0]*11,'sin deuda CP');put(BS,20,'Short-term debt',std,s)
    lc=add(*[it(t)[0] for t in cfg['lease_c']]);lc=[0.0 if v is None else v for v in lc];put(BS,21,'Current portion of leases',lc,cfg['lease_c'])
    ur,s=it(cfg['unearned']) if cfg.get('unearned') else ([None]*11,None);put(BS,22,'Unearned revenue',ur,s)
    tcl,s=it('LiabilitiesCurrent');put(BS,24,'Total current liabilities',tcl,s)
    ocl=[None if t is None else round(t-(a or 0)-(b or 0)-(c or 0)-(d or 0)-(e or 0),3) for t,a,b,c,d,e in zip(tcl,ap,acc,std,lc,ur)];put(BS,23,'Other current liabilities (derivado)',ocl)
    ltd,s=it(cfg['ltd']) if cfg.get('ltd') else ([0.0]*11,'sin deuda LP');ltd=[0.0 if v is None else v for v in ltd];put(BS,25,'LT debt',ltd,s)
    lnc=add(*[it(t)[0] for t in cfg['lease_nc']]);lnc=[0.0 if v is None else v for v in lnc];put(BS,26,'Leases (no corriente)',lnc,cfg['lease_nc'])
    eq,s=it(cfg['equity']);put(BS,34,'Total common equity',eq,s)
    nci,s=it(cfg['nci']) if cfg.get('nci') else ([0.0]*11,'sin NCI');nci=[0.0 if v is None else v for v in nci]
    teq=[None if e is None else e+n for e,n in zip(eq,nci)];put(BS,35,'Total equity (incl. NCI)',teq,s)
    tle,s=it('LiabilitiesAndStockholdersEquity');put(BS,36,'Total L+E',tle,s)
    tl=[None if None in(a,b) else round(a-b,3) for a,b in zip(tle,teq)];put(BS,29,'Total liabilities (derivado: L+E − patrimonio total)',tl)
    tltl=[None if None in(a,b) else round(a-b,3) for a,b in zip(tl,tcl)];put(BS,28,'Total LT liabilities (derivado)',tltl)
    oltl=[None if None in(a,b,c) else round(a-b-c,3) for a,b,c in zip(tltl,ltd,lnc)];put(BS,27,'Other LT liabilities (derivado)',oltl)
    apic,s=it(cfg['apic']);aoci,s2=it('AccumulatedOtherComprehensiveIncomeLossNetOfTax')
    put(BS,31,'Common stock and APIC',apic,s);put(BS,32,'AOCI',[0.0 if v is None else v for v in aoci],s2)
    re_=[None if e is None else round(e-(a or 0)-(o or 0),3) for e,a,o in zip(eq,apic,aoci)];put(BS,33,'Retained earnings (derivado: patrimonio − APIC − AOCI; incluye acciones propias y reservas)',re_)
    # ---- Flujo de caja
    cni=[v for v in [fl(cfg['ni_cons'] if cfg.get('ni_cons') else cfg['ni'])[0]]][0];put(CF,3,'Net income',cni)
    cda,s=fl(cfg['cf_da']);put(CF,4,'D&A',cda,s)
    sbc,s=fl(cfg['sbc']);put(CF,5,'SBC',sbc,s)
    cfo,s=fl('NetCashProvidedByUsedInOperatingActivities');put(CF,13,'CFO',cfo,s)
    wc={}
    for r,key,label in ((7,'d_ar','Changes in receivables'),(8,'d_ap','Changes in AP'),(9,'d_acc','Changes in accrued'),(10,'d_tax','Changes in taxes payable'),(11,'d_ur','Changes in unearned revenue')):
        if cfg.get(key): v=[None]*11; parts=[fl(t,neg=True)[0] for t in cfg[key]]; v=add(*parts); put(CF,r,label,[0.0 if x is None else x for x in v],cfg[key])
        else: put(CF,r,label,[0.0]*11,'no aplica')
    wcs=add(*[DS[(CF,r)] for r in (7,8,9,10,11)])
    oth=[None if None in(c_,a,b,d_) else round(c_-n-a-b-d_,3) for c_,n,a,b,d_ in zip(cfo,cni,cda,sbc,wcs)]
    put(CF,6,'Other adjustments (derivado: CFO − NI − D&A − SBC − capital de trabajo listado)',oth)
    put(CF,12,'Changes in other operating (incluido en Other adjustments)',[0.0]*11,'incluido en F6')
    cap,s=fl(cfg['capex'],neg=True);put(CF,15,'Capex',cap,s)
    pp,s=fl(cfg['ppe_sale']) if cfg.get('ppe_sale') else ([0.0]*11,'sin dato');put(CF,16,'Proceeds PPE',[0.0 if v is None else v for v in pp],s)
    pu,s=fl(cfg['inv_buy'],neg=True) if cfg.get('inv_buy') else ([0.0]*11,'sin dato');put(CF,17,'Purchases of investments',[0.0 if v is None else v for v in pu],s)
    ps,s=fl(cfg['inv_sell']) if cfg.get('inv_sell') else ([0.0]*11,'sin dato');put(CF,18,'Proceeds from investments',[0.0 if v is None else v for v in ps],s)
    ac,s=fl(cfg['acq'],neg=True) if cfg.get('acq') else ([0.0]*11,'sin dato');put(CF,19,'Acquisitions',[0.0 if v is None else v for v in ac],s)
    cfi,s=fl('NetCashProvidedByUsedInInvestingActivities');put(CF,22,'CFI',cfi,s)
    oinv=[None if None in(c_,a,b,d_,e,f) else round(c_-a-b-d_-e-f,3) for c_,a,b,d_,e,f in zip(cfi,cap,pp,pu,ps,ac)]
    # CFI = capex(neg)+pp+pu(neg)+ps+acq(neg)+otros  (capex/adq. ya con signo negativo)
    put(CF,21,'Other investing (derivado)',oinv)
    cp,s=fl(cfg['st_debt']) if cfg.get('st_debt') else ([0.0]*11,'sin dato');put(CF,25,'Net ST debt',[0.0 if v is None else v for v in cp],s)
    li,s=fl(cfg['lt_issue']) if cfg.get('lt_issue') else ([0.0]*11,'sin dato');lr,s2=fl(cfg['lt_repay'],neg=True) if cfg.get('lt_repay') else ([0.0]*11,'sin dato')
    li=[0.0 if v is None else v for v in li];lr=[0.0 if v is None else v for v in lr]
    put(CF,26,'Issuance of LT debt',li,s);put(CF,27,'Repayments of LT debt',lr,s2);put(CF,28,'Net LT debt',add(li,lr))
    ic,s=fl(cfg['issue_eq']) if cfg.get('issue_eq') else ([0.0]*11,'sin dato');ic=[0.0 if v is None else v for v in ic]
    rp,s2=fl(cfg['buyback'],neg=True) if cfg.get('buyback') else ([0.0]*11,'sin dato');rp=[0.0 if v is None else v for v in rp]
    put(CF,29,'Issuance of common',ic,s);put(CF,30,'Repurchases',rp,s2);put(CF,31,'Net issuance/(repurchases)',add(ic,rp))
    dv,s=fl(cfg['div'],neg=True) if cfg.get('div') else ([0.0]*11,'sin dividendos');put(CF,32,'Dividends',[0.0 if v is None else v for v in dv],s)
    cff,s=fl('NetCashProvidedByUsedInFinancingActivities');put(CF,34,'CFF',cff,s)
    ofin=[None if None in(c_,a,b,d_,e) else round(c_-a-b-d_-e,3) for c_,a,b,d_,e in zip(cff,cp,add(li,lr),add(ic,rp),[0.0 if v is None else v for v in dv])]
    put(CF,33,'Other financing (derivado)',ofin)
    nc,s=fl('CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect');put(CF,40,'Net change in cash (incl. caja restringida y tipo de cambio)',nc,s)
    return DS,SRC
def checks(DS,fy):
    out=[];L=len(fy)+1
    g=lambda sh,r:DS[(sh,r)]
    for i in range(L):
        lab=(fy+['LTM'])[i]
        def v(sh,r): return g(sh,r)[i]
        c=[]
        if None not in (v(BS,16),v(BS,36)): c.append(('A=L+E',round(v(BS,16)-v(BS,36),3)))
        if None not in (v(CF,13),v(CF,22),v(CF,34),v(CF,40)): c.append(('CFO+CFI+CFF−Δcaja',round(v(CF,13)+v(CF,22)+v(CF,34)-v(CF,40),1)))
        if v(IS,3) is not None: c.append(('otros op',v(IS,11)))
        out.append((lab,c))
    return out
