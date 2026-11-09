from mapping import *
FY=[f'{y}-12-31' for y in range(2016,2026)]
S=SEC('uber_facts.json',FY,'2026-09-30','2025-09-30','2026-01-01','2025-01-01','2025-12-31')
cfg=dict(rev='Revenues',cost=['CostOfGoodsAndServiceExcludingDepreciationDepletionAndAmortization'],cost_names=['costo de ingresos (sin D&A)'],
 sga=['SellingAndMarketingExpense','GeneralAndAdministrativeExpense'],sga_names=['ventas y marketing','G&A'],da='DepreciationDepletionAndAmortization',da_in_is=True,rd='ResearchAndDevelopmentExpense',ebit='OperatingIncomeLoss',
 other_names='operaciones y soporte (línea no estándar XBRL), litigios y otros',int_inc='InvestmentIncomeInterest',int_exp=['InterestExpenseNonoperating','InterestExpense'],
 pbt=['IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],tax='IncomeTaxExpenseBenefit',ni='NetIncomeLoss',ni_cons='ProfitLoss',
 bsh='WeightedAverageNumberOfSharesOutstandingBasic',dsh='WeightedAverageNumberOfDilutedSharesOutstanding',
 cash='CashAndCashEquivalentsAtCarryingValue',sti=['MarketableSecuritiesCurrent','ShortTermInvestments'],ar='AccountsReceivableNetCurrent',
 ppe=['PropertyPlantAndEquipmentNet','PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization'],intang=['IntangibleAssetsNetExcludingGoodwill'],
 lti_sum=['EquitySecuritiesWithoutReadilyDeterminableFairValueAmount','EquityMethodInvestments'],lti_name='participaciones en otras empresas (acciones sin valor razonable fácil + método de participación)',
 std=['LongTermDebtCurrent'],lease_c=['OperatingLeaseLiabilityCurrent','FinanceLeaseLiabilityCurrent'],ltd=['LongTermDebtNoncurrent'],lease_nc=['OperatingLeaseLiabilityNoncurrent','FinanceLeaseLiabilityNoncurrent'],
 equity='StockholdersEquity',nci=['NonredeemableNoncontrollingInterest'],apic=['AdditionalPaidInCapital'],
 cf_da='DepreciationDepletionAndAmortization',sbc='ShareBasedCompensation',d_ar=['IncreaseDecreaseInAccountsReceivable'],d_ap=['IncreaseDecreaseInAccountsPayable'],d_acc=['IncreaseDecreaseInAccruedLiabilitiesAndOtherOperatingLiabilities'],
 capex='PaymentsToAcquirePropertyPlantAndEquipment',inv_buy=['PaymentsToAcquireMarketableSecurities'],inv_sell=['ProceedsFromSaleAndMaturityOfMarketableSecurities'],acq=['PaymentsToAcquireBusinessesNetOfCashAcquired'],
 lt_issue=['ProceedsFromIssuanceOfLongTermDebt'],lt_repay=['RepaymentsOfLongTermDebt'],buyback='PaymentsForRepurchaseOfCommonStock')
