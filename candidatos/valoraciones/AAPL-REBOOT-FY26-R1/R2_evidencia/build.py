import sys; sys.path.insert(0,'/tmp/claude-0/-home-user/b8c0d315-1e6b-524a-8878-fb2b853781cf/scratchpad')
import json,sys
from extract import *
cols=FY  # B..K ; L = LTM = FY2026
def row(tags,kind,unit='USD',scale=1e6,neg=False,ends=None):
    out=[];src=[]
    for e in (ends or FY):
        r=V(tags,e,kind,unit,scale)
        out.append(None if r is None else (-r[0] if neg else r[0]));src.append(None if r is None else (r[1],r[2]))
    return out,src
S={} ; SRC={}
def put(sheet,rowno,label,vals,src): 
    S[(sheet,rowno)]=vals; SRC[(sheet,rowno)]=(label,src)
def add(a,b): return [None if (x is None and y is None) else (x or 0)+(y or 0) for x,y in zip(a,b)]
def sub(a,b): return [None if x is None else x-(y or 0) for x,y in zip(a,b)]
IS='Income Statement';BS='Balance Sheet';CF='Cash Flow Statement'
rev,s=row(['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues','SalesRevenueNet'],'flow');put(IS,3,'Total Revenues',rev,s)
cogs,s=row(['CostOfGoodsAndServicesSold','CostOfRevenue'],'flow');put(IS,5,'Cost of Sales',cogs,s)
sga,s=row('SellingGeneralAndAdministrativeExpense','flow');put(IS,8,'SG&A',sga,s)
rd,s=row('ResearchAndDevelopmentExpense','flow');put(IS,10,'R&D',rd,s)
oi,s=row('OperatingIncomeLoss','flow');put(IS,12,'Operating Profit',oi,s)
# other operating = ingresos - costo - sga - rd - EBIT (verificación)
oth=[None if None in (a,b,c,d,e) else round(a-b-c-d-e,3) for a,b,c,d,e in zip(rev,cogs,sga,rd,oi)]
put(IS,11,'Other Operating Expenses (verificado = ventas−costo−SG&A−I+D−EBIT)',oth,'derivado')
iinc,s=row(['InvestmentIncomeInterest','InvestmentIncomeInterestAndDividend'],'flow');put(IS,14,'Interest and Investment Income',iinc,s)
iexp,s=row('InterestExpense','flow');put(IS,15,'Interest Expense',iexp,s)
nonop,s=row(['NonoperatingIncomeExpense','OtherNonoperatingIncomeExpense'],'flow');put(IS,18,'Total Non-Operating Income',nonop,s)
pbt,s=row(['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],'flow');put(IS,19,'Pretax Income',pbt,s)
tax,s=row('IncomeTaxExpenseBenefit','flow');put(IS,20,'Income Taxes',tax,s)
ni,s=row('NetIncomeLoss','flow');put(IS,21,'Consolidated Net Income',ni,s);put(IS,22,'NI to common',ni,s)
bsh,s=row('WeightedAverageNumberOfSharesOutstandingBasic','flow','shares');bsh[0]=bsh[0]*4;put(IS,25,'Basic wtd shares (FY2017 ×4 por split 4:1)',bsh,s)
dsh,s=row('WeightedAverageNumberOfDilutedSharesOutstanding','flow','shares');dsh[0]=dsh[0]*4;put(IS,26,'Diluted wtd shares (FY2017 ×4 por split 4:1)',dsh,s)
so,s=row('CommonStockSharesOutstanding','inst','shares');so[0]=so[0]*4;so[1]=so[1]*4;put(IS,27,'Shares Outstanding (cierre; FY2017-18 ×4 por split 4:1)',so,s)
nonop17=[None if n is None else round(n-((a or 0)-abs(b or 0)) ,3) for n,a,b in zip(nonop,iinc,iexp)]
put(IS,17,'Non-Operating Income (resto)',nonop17,'derivado')
# BS
cash,s=row('CashAndCashEquivalentsAtCarryingValue','inst');put(BS,3,'Cash',cash,s)
sti,s=row(['MarketableSecuritiesCurrent','AvailableForSaleSecuritiesCurrent'],'inst');put(BS,4,'ST investments',sti,s)
ar,s=row('AccountsReceivableNetCurrent','inst');put(BS,6,'AR',ar,s)
nt,s=row('NontradeReceivablesCurrent','inst');put(BS,7,'Other receivables (vendor non-trade)',nt,s)
oca,s=row('OtherAssetsCurrent','inst');put(BS,9,'Other current assets',oca,s)
tca,s=row('AssetsCurrent','inst');put(BS,10,'Total current assets',tca,s)
ppe,s=row('PropertyPlantAndEquipmentNet','inst');put(BS,11,'PPE net',ppe,s)
lti,s=row(['MarketableSecuritiesNoncurrent','AvailableForSaleSecuritiesNoncurrent'],'inst');put(BS,14,'LT investments',lti,s)
ta,s=row('Assets','inst');put(BS,16,'Total assets',ta,s)
olta=[None if None in (a,b,c,d) else round(a-b-c-d,3) for a,b,c,d in zip(ta,tca,ppe,lti)]
put(BS,15,'Other LT assets (derivado: total−AC−PPE−inv. LP)',olta,'derivado')
ap,s=row('AccountsPayableCurrent','inst');put(BS,18,'AP',ap,s)
cp,s=row('CommercialPaper','inst');ltdc,s2=row('LongTermDebtCurrent','inst')
std=add(cp,ltdc);put(BS,20,'Short-term debt (papel comercial + deuda LP corriente)',std,'CommercialPaper+LongTermDebtCurrent')
olc,s=row(['OperatingLeaseLiabilityCurrent'],'inst');flc,s=row(['FinanceLeaseLiabilityCurrent'],'inst')
lc=[ (0 if (a is None and b is None) else (a or 0)+(b or 0)) for a,b in zip(olc,flc)]
put(BS,21,'Current portion of leases',lc,'OperatingLeaseLiabilityCurrent+FinanceLeaseLiabilityCurrent (ASC 842 desde FY2020; antes 0)')
dr,s=row(['ContractWithCustomerLiabilityCurrent','DeferredRevenueCurrent'],'inst');put(BS,22,'Unearned revenue',dr,s)
tcl,s=row('LiabilitiesCurrent','inst');put(BS,24,'Total current liabilities',tcl,s)
ocl=[None if None in (a,b,c,d,e) else round(a-b-c-d-e,3) for a,b,c,d,e in zip(tcl,ap,std,lc,dr)]
put(BS,23,'Other current liabilities (derivado)',ocl,'derivado')
ltd,s=row('LongTermDebtNoncurrent','inst');put(BS,25,'LT debt',ltd,s)
olnc,s=row(['OperatingLeaseLiabilityNoncurrent'],'inst');flnc,s=row(['FinanceLeaseLiabilityNoncurrent'],'inst')
lnc=[ (0 if (a is None and b is None) else (a or 0)+(b or 0)) for a,b in zip(olnc,flnc)]
put(BS,26,'Leases (no corriente)',lnc,'OperatingLeaseLiabilityNoncurrent+FinanceLeaseLiabilityNoncurrent')
tl,s=row('Liabilities','inst');put(BS,29,'Total liabilities',tl,s)
tltl=[None if None in (a,b) else round(a-b,3) for a,b in zip(tl,tcl)];put(BS,28,'Total LT liabilities (derivado: total−corrientes)',tltl,'derivado')
oltl=[None if None in (a,b,c) else round(a-b-c,3) for a,b,c in zip(tltl,ltd,lnc)];put(BS,27,'Other LT liabilities (derivado)',oltl,'derivado')
apic,s=row(['CommonStocksIncludingAdditionalPaidInCapital'],'inst');put(BS,31,'Common stock and APIC',apic,s)
aoci,s=row('AccumulatedOtherComprehensiveIncomeLossNetOfTax','inst');put(BS,32,'AOCI',aoci,s)
re_,s=row('RetainedEarningsAccumulatedDeficit','inst');put(BS,33,'Retained earnings',re_,s)
eq,s=row('StockholdersEquity','inst');put(BS,34,'Total common equity',eq,s);put(BS,35,'Total equity',eq,s)
tle,s=row('LiabilitiesAndStockholdersEquity','inst');put(BS,36,'Total L+E',tle,s)
inv,s=row('InventoryNet','inst');put('AUX',3,'Inventario',inv,s)
# CF
cni,s=row('NetIncomeLoss','flow');put(CF,3,'Net income',cni,s)
da,s=row('DepreciationDepletionAndAmortization','flow');put(CF,4,'D&A',da,s)
sbc,s=row('ShareBasedCompensation','flow');put(CF,5,'SBC',sbc,s)
dtx,s=row('DeferredIncomeTaxExpenseBenefit','flow');onc,s2=row('OtherNoncashIncomeExpense','flow')
onc_neg=[None if x is None else -x for x in onc]
put(CF,6,'Other adjustments (impuesto diferido − otros ingresos no monetarios)',add(dtx,onc_neg),'DeferredIncomeTaxExpenseBenefit − OtherNoncashIncomeExpense')
ard,s=row('IncreaseDecreaseInAccountsReceivable','flow');ntd,s2=row('IncreaseDecreaseInOtherReceivables','flow')
put(CF,7,'Changes in receivables',[None if (a is None and b is None) else -((a or 0)+(b or 0)) for a,b in zip(ard,ntd)],'−(IncreaseDecreaseInAccountsReceivable+IncreaseDecreaseInOtherReceivables)')
apd,s=row('IncreaseDecreaseInAccountsPayable','flow');put(CF,8,'Changes in AP',apd,s)
drd,s=row(['IncreaseDecreaseInContractWithCustomerLiability','IncreaseDecreaseInDeferredRevenue'],'flow');put(CF,11,'Changes in unearned revenue',drd,s)
cfo,s=row('NetCashProvidedByUsedInOperatingActivities','flow');put(CF,13,'CFO',cfo,s)
oth_op=[None if None in (a,b,c,d,e,f_,g) else round(a-b-c-d-e-f_-g,3) for a,b,c,d,e,f_,g in zip(cfo,cni,da,sbc,add(dtx,onc_neg),[ -(((x or 0)+(y or 0))) for x,y in zip(ard,ntd)],apd)]
oth_op=[None if v is None else round(v-(dd or 0),3) for v,dd in zip(oth_op,drd)]
put(CF,12,'Changes in other operating (derivado)',oth_op,'derivado')
cap,s=row('PaymentsToAcquirePropertyPlantAndEquipment','flow',neg=True);put(CF,15,'Capex',cap,s)
pp,s=row('ProceedsFromSaleOfPropertyPlantAndEquipment','flow');put(CF,16,'Proceeds PPE',pp,s)
pu=[];
for tg in ['PaymentsToAcquireAvailableForSaleSecuritiesDebt','PaymentsToAcquireInvestments']:
    pass
pu1,s=row('PaymentsToAcquireAvailableForSaleSecuritiesDebt','flow',neg=True);pu2,s2=row('PaymentsToAcquireInvestments','flow',neg=True)
put(CF,17,'Purchases of investments',[a if a is not None else b for a,b in zip(pu1,pu2)],'PaymentsToAcquireAvailableForSaleSecuritiesDebt|PaymentsToAcquireInvestments')
pm,s=row('ProceedsFromMaturitiesPrepaymentsAndCallsOfAvailableForSaleSecurities','flow');ps,s2=row('ProceedsFromSaleOfAvailableForSaleSecuritiesDebt','flow')
put(CF,18,'Proceeds from investments',add(pm,ps),'Maturities+Sales AFS')
acq,s=row('PaymentsToAcquireBusinessesNetOfCashAcquired','flow',neg=True);put(CF,19,'Acquisitions',acq,s)
cfi,s=row('NetCashProvidedByUsedInInvestingActivities','flow');put(CF,22,'CFI',cfi,s)
oinv=[None if None in (c,) else round(c-sum(x or 0 for x in (a,b,d,e,f_)),3) for c,a,b,d,e,f_ in zip(cfi,cap,pp,[ (x if x is not None else y) for x,y in zip(pu1,pu2)],add(pm,ps),acq)]
put(CF,21,'Other investing (derivado)',oinv,'derivado')
cpd,s=row('ProceedsFromRepaymentsOfCommercialPaper','flow');put(CF,25,'Net ST debt',cpd,s)
li,s=row('ProceedsFromIssuanceOfLongTermDebt','flow');lr,s2=row('RepaymentsOfLongTermDebt','flow',neg=True)
put(CF,26,'Issuance of LT debt',li,s);put(CF,27,'Repayments of LT debt',lr,s2)
put(CF,28,'Net LT debt',add(li,lr),'26+27')
ic,s=row('ProceedsFromIssuanceOfCommonStock','flow');put(CF,29,'Issuance of common',ic,s)
rp,s=row('PaymentsForRepurchaseOfCommonStock','flow',neg=True);put(CF,30,'Repurchases',rp,s)
put(CF,31,'Net issuance/(repurchases)',add(ic,rp),'29+30')
dv,s=row(['PaymentsOfDividends','PaymentsOfDividendsCommonStock'],'flow',neg=True);put(CF,32,'Dividends',dv,s)
cff,s=row('NetCashProvidedByUsedInFinancingActivities','flow');put(CF,34,'CFF',cff,s)
ofin=[None if c is None else round(c-sum(x or 0 for x in (a,b,d,e)),3) for c,a,b,d,e in zip(cff,cpd,add(li,lr),add(ic,rp),dv)]
put(CF,33,'Other financing (derivado)',ofin,'derivado')
nc,s=row('CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect','flow');put(CF,40,'Net change in cash',nc,s)
json.dump({f'{k[0]}|{k[1]}':v for k,v in S.items()},open('out_dataset.json','w'))
json.dump({f'{k[0]}|{k[1]}':v for k,v in SRC.items()},open('out_sources.json','w'),default=str)
# FY2016 apertura
op={}
for k,tags in {'Assets':['Assets'],'Equity':['StockholdersEquity'],'CP':['CommercialPaper'],'LTDC':['LongTermDebtCurrent'],'LTD':['LongTermDebtNoncurrent'],'Cash':['CashAndCashEquivalentsAtCarryingValue'],'STI':['MarketableSecuritiesCurrent','AvailableForSaleSecuritiesCurrent'],'AR':['AccountsReceivableNetCurrent'],'NT':['NontradeReceivablesCurrent'],'AP':['AccountsPayableCurrent'],'Inv':['InventoryNet'],'PPE':['PropertyPlantAndEquipmentNet'],'CL':['LiabilitiesCurrent']}.items():
    r=V(tags,FY0,'inst'); op[k]=None if r is None else r[0]
json.dump(op,open('out_open2016.json','w'));print('apertura FY2016',op)
def fmt(v): return '   —' if v is None else f'{v:10.1f}'
for k in sorted(S): 
    print(f'{k[0][:3]}{k[1]:>3} {SRC[k][0][:34]:34}',' '.join(fmt(v) for v in S[k]))
