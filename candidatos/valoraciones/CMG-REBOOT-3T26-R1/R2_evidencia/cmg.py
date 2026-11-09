from mapping import *
FY=[f'{y}-12-31' for y in range(2016,2026)]
S=SEC('cmg_facts.json',FY,'2026-09-30','2025-09-30','2026-01-01','2025-01-01','2025-12-31')
cfg=dict(rev='Revenues',cost=[ 'CostDirectMaterial','CostDirectLabor','OccupancyNet','OtherCostAndExpenseOperating'],cost_names=['alimentos, bebidas y empaque','mano de obra','ocupación','otros costos operativos'],
 sga=['GeneralAndAdministrativeExpense'],sga_names=['G&A'],da='DepreciationDepletionAndAmortization',da_in_is=True,rd=None,ebit='OperatingIncomeLoss',other_names='pre-apertura, deterioro y pérdida en bajas',
 int_inc=None,int_exp=None,pbt=['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],
 tax='IncomeTaxExpenseBenefit',ni='NetIncomeLoss',bsh='WeightedAverageNumberOfSharesOutstandingBasic',dsh='WeightedAverageNumberOfDilutedSharesOutstanding',split_before='2022-01-01',split_f=50,
 shares_out=['CommonStockSharesOutstanding'],cash='CashAndCashEquivalentsAtCarryingValue',sti=['MarketableSecuritiesCurrent','ShortTermInvestments','AvailableForSaleSecuritiesCurrent','HeldToMaturitySecuritiesCurrent'],
 ar='AccountsReceivableNetCurrent',ppe='PropertyPlantAndEquipmentNet',lti=['LongTermInvestments','HeldToMaturitySecuritiesNoncurrent','AvailableForSaleSecuritiesNoncurrent'],lti_name='inversiones LP',
 accrued=['AccruedLiabilitiesCurrent'],lease_c=['OperatingLeaseLiabilityCurrent','FinanceLeaseLiabilityCurrent'],unearned=['ContractWithCustomerLiabilityCurrent','DeferredRevenueCurrent'],
 lease_nc=['OperatingLeaseLiabilityNoncurrent','FinanceLeaseLiabilityNoncurrent'],equity='StockholdersEquity',apic=['AdditionalPaidInCapitalCommonStock','AdditionalPaidInCapital'],
 cf_da='DepreciationDepletionAndAmortization',sbc='ShareBasedCompensation',d_ar=['IncreaseDecreaseInAccountsReceivable'],d_ap=['IncreaseDecreaseInAccountsPayable'],d_acc=['IncreaseDecreaseInAccruedLiabilities'],d_tax=['IncreaseDecreaseInIncomeTaxesPayableNetOfIncomeTaxesReceivable'],d_ur=['IncreaseDecreaseInContractWithCustomerLiability'],
 capex='PaymentsToAcquirePropertyPlantAndEquipment',inv_buy=['PaymentsToAcquireMarketableSecurities','PaymentsToAcquireHeldToMaturitySecurities','PaymentsToAcquireInvestments'],inv_sell=['ProceedsFromSaleAndMaturityOfMarketableSecurities','ProceedsFromMaturitiesPrepaymentsAndCallsOfHeldToMaturitySecurities'],
 buyback='PaymentsForRepurchaseOfCommonStock',issue_eq=['ProceedsFromStockOptionsExercised'],div=None)

