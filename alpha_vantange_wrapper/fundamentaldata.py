from .alpha_vantage_wrapper import AlphaVantage as av

from datetime import datetime

search_date = datetime.now().date().strftime('%Y-%m-%d')


class FundamentalData(av):
    """
    This class implements all Fundamental Data APIs.
    Refer to https://www.alphavantage.co/documentation/#fundamentals for API parameters. All API parameters
    are supported as long as you input the parameter name and value correctly as specified in the documentation.
    Following is an example:
        FundamentalData().get_company_overview('IBM')
    """

    @av._call_api_on_func
    def get_company_overview(self, symbol):
        _FUNCTION_KEY = 'OVERVIEW'
        return _FUNCTION_KEY, None, None

    @av._call_api_on_func
    def get_income_statement(self, symbol):
        _FUNCTION_KEY = 'INCOME_STATEMENT'
        return _FUNCTION_KEY, ['annualReports', 'quarterlyEarnings'], 'symbol'

    @av._call_api_on_func
    def get_balance_sheet(self, symbol):
        _FUNCTION_KEY = 'BALANCE_SHEET'
        return _FUNCTION_KEY, ['annualReports', 'quarterlyEarnings'], 'symbol'

    @av._call_api_on_func
    def get_cash_flow(self, symbol):
        _FUNCTION_KEY = 'CASH_FLOW'
        return _FUNCTION_KEY, ['annualReports', 'quarterlyEarnings'], 'symbol'

    @av._call_api_on_func
    def get_earnings(self, symbol):
        _FUNCTION_KEY = 'EARNINGS'
        return _FUNCTION_KEY, ['annualReports', 'quarterlyEarnings'], 'symbol'

    @av._call_api_on_func
    def get_listing_and_delisting_status(self, symbol):
        _FUNCTION_KEY = 'LISTING_STATUS'
        return _FUNCTION_KEY, None, None

    @av._call_api_on_func
    def get_ipo_calender(self, symbol):
        _FUNCTION_KEY = 'EARNINGS_CALENDAR'
        return _FUNCTION_KEY, None, None

    @av._call_api_on_func
    def get_ipo_calender(self, symbol):
        _FUNCTION_KEY = 'IPO_CALENDAR'
        return _FUNCTION_KEY, None, None

