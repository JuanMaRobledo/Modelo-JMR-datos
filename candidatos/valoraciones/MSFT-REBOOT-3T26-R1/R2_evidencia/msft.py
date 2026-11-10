from mapping import *
FY=[f'{y}-06-30' for y in range(2017,2027)]
S=SEC('msft_facts.json',FY,'2026-09-30','2025-09-30','2026-07-01','2025-07-01','2026-06-30')
cfg=dict(rev=['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues'],cost=[['CostOfGoodsAndServicesSold','CostOfRevenue']],cost_names=['costo de ingresos (incluye depreciación de centros de datos)'],
 sga=['SellingAndMarketingExpense','GeneralAndAdministrativeExpense'],sga_names=['ventas y marketing','G&A'],da=['DepreciationDepletionAndAmortization','DepreciationAmortizationAndOther','Depreciation'],da_in_is=False,rd='ResearchAndDevelopmentExpense',ebit='OperatingIncomeLoss',
 other_names='otros (sin línea separada)',int_inc='InvestmentIncomeNet',int_exp=['InterestExpenseNonoperating','InterestExpense'],
 pbt=['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],tax='IncomeTaxExpenseBenefit',ni='NetIncomeLoss',
 bsh='WeightedAverageNumberOfSharesOutstandingBasic',dsh='WeightedAverageNumberOfDilutedSharesOutstanding',
 cash='CashAndCashEquivalentsAtCarryingValue',sti=['ShortTermInvestments','AvailableForSaleSecuritiesCurrent'],ar='AccountsReceivableNetCurrent',
 ppe=['PropertyPlantAndEquipmentNet'],intang=['FiniteLivedIntangibleAssetsNet','IntangibleAssetsNetExcludingGoodwill'],
 lti=['LongTermInvestments'],lti_name='inversiones de largo plazo (acciones, método de participación y otras)',accrued=['EmployeeRelatedLiabilitiesCurrent'],
 std=['LongTermDebtCurrent'],lease_c=['OperatingLeaseLiabilityCurrent','FinanceLeaseLiabilityCurrent'],ltd=['LongTermDebtNoncurrent'],lease_nc=['OperatingLeaseLiabilityNoncurrent','FinanceLeaseLiabilityNoncurrent'],
 unearned=['ContractWithCustomerLiabilityCurrent'],equity='StockholdersEquity',apic=['CommonStocksIncludingAdditionalPaidInCapital'],
 cf_da=['DepreciationDepletionAndAmortization','DepreciationAmortizationAndOther','Depreciation'],sbc=['ShareBasedCompensation'],d_ar=['IncreaseDecreaseInAccountsReceivable'],d_ap=['IncreaseDecreaseInAccountsPayable'],
 d_ur=['IncreaseDecreaseInContractWithCustomerLiability'],
 capex=['PaymentsToAcquirePropertyPlantAndEquipment'],inv_buy=['PaymentsToAcquireInvestments'],inv_sell=['ProceedsFromSaleOfAvailableForSaleSecuritiesDebt','ProceedsFromMaturitiesPrepaymentsAndCallsOfAvailableForSaleSecurities'],acq=['PaymentsToAcquireBusinessesNetOfCashAcquired'],
 lt_issue=['ProceedsFromDebtMaturingInMoreThanThreeMonths'],lt_repay=['RepaymentsOfDebtMaturingInMoreThanThreeMonths'],issue_eq=['ProceedsFromIssuanceOfCommonStock'],buyback='PaymentsForRepurchaseOfCommonStock',div='PaymentsOfDividendsCommonStock')
