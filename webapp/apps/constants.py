import os

DIAGNOSTIC_TOOLTIP = "Diagnostic table tooltip"
DIFFERENCE_TOOLTIP = "Difference table tooltip"
PAYROLL_TOOLTIP = "Payroll info tooltip"
INCOME_TOOLTIP = "Income info tooltip"
BASE_TOOLTIP = "Base plan tooltip"
REFORM_TOOLTIP = "Reform plan tooltip"
EXPANDED_TOOLTIP = "Expanded income tooltip"
ADJUSTED_TOOLTIP = "Adjusted income tooltip"
INCOME_BINS_TOOLTIP = "Income bins tooltip"
INCOME_DECILES_TOOLTIP = "Income deciles tooltip"
FISCAL_CURRENT_LAW = "Fiscal Current Law"
FISCAL_REFORM = "Fiscal Reform tooltip"
FISCAL_CHANGE = "Fiscal Change tooltip"
METR_TOOLTIP = "Marginal effective tax rate on new investments. The METR includes the impact of the first level of taxation on the incentives to invest."
METTR_TOOLTIP = "Marginal effective total tax rate on new investments. The METTR includes the impact of all levels of taxation (both on business entities and savers) on the incentives to invest."
COC_TOOLTIP = "The cost of capital is calculated as the net-of-depreciation, before-tax rate of return."
DPRC_TOOLTIP = "Net present value of depreciation deductions."

START_YEARS = ('2013', '2014', '2015', '2016', '2017')
START_YEAR = os.environ.get('START_YEAR', '2017')
