from mapping import *
FY=[f'{y}-12-31' for y in range(2016,2026)]
S=SEC('meli_facts.json',FY,'2026-09-30','2025-09-30','2026-01-01','2025-01-01','2025-12-31')
cfg=dict(rev=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax'],cost=[['CostOfGoodsAndServicesSold','CostOfRevenue']],cost_names=['costo de ingresos netos (incluye costo de financiamiento y D&A de operaciones)'],
 sga=['SellingAndMarketingExpense','GeneralAndAdministrativeExpense'],sga_names=['ventas y marketing','G&A'],da='DepreciationAndAmortization',da_in_is=False,rd='ResearchAndDevelopmentExpense',ebit='OperatingIncomeLoss',
 other_names='provisión para cuentas incobrables (cartera de crédito) y otros',int_inc='InvestmentIncomeInterest',int_exp=None,
 pbt=['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest'],tax='IncomeTaxExpenseBenefit',ni='NetIncomeLoss',
 bsh='WeightedAverageNumberOfSharesOutstandingBasic',dsh='WeightedAverageNumberOfDilutedSharesOutstanding',
 cash='CashAndCashEquivalentsAtCarryingValue',sti=['ShortTermInvestments'],ar='AccountsReceivableNetCurrent',
 ppe=['PropertyPlantAndEquipmentNet','PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization'],intang=['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'],
 lti=['LongTermInvestments'],lti_name='inversiones de largo plazo',accrued=['AccountsPayableAndAccruedLiabilitiesCurrent'],
 std=['LoansPayableCurrent'],lease_c=['OperatingLeaseLiabilityCurrent','FinanceLeaseLiabilityCurrent'],ltd=['LongTermLoansPayable'],lease_nc=['OperatingLeaseLiabilityNoncurrent','FinanceLeaseLiabilityNoncurrent'],
 unearned=['ContractWithCustomerLiabilityCurrent'],equity='StockholdersEquity',apic=['AdditionalPaidInCapital'],
 cf_da='DepreciationAndAmortization',sbc=['ShareBasedCompensation','StockOptionPlanExpense'],d_ar=['IncreaseDecreaseInAccountsReceivable'],d_ap=['IncreaseDecreaseInAccountsPayableAndAccruedLiabilities'],
 capex=['PaymentsToAcquireProductiveAssets','PaymentsToAcquirePropertyPlantAndEquipment'],inv_buy=['PaymentsToAcquireInvestments'],inv_sell=['ProceedsFromSaleMaturityAndCollectionsOfInvestments'],acq=['PaymentsToAcquireBusinessesNetOfCashAcquired'],
 lt_issue=['ProceedsFromIssuanceOfOtherLongTermDebt'],lt_repay=['RepaymentsOfOtherLongTermDebt'],buyback='PaymentsForRepurchaseOfCommonStock')
