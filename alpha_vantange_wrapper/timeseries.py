from .alpha_vantage_wrapper import AlphaVantage as av


class TimeSeries(av):
    """
    This class implements all Time Series Stock Data APIs.
    Refer to https://www.alphavantage.co/documentation/#time-series-data for API parameters. All API parameters
    are supported as long as you input the parameter name and value correctly as specified in the documentation.
    Following is an example:
        TimeSeries().get_intraday('IBM', interval='1min', adjusted='true', outputsize='full', datatype='csv')
    """

    @av._call_api_on_func
    def get_intraday(self, symbol, interval='15min', **kwargs):
        _FUNCTION_KEY = "TIME_SERIES_INTRADAY"
        return _FUNCTION_KEY, "Time Series ({})".format(interval), 'Meta Data'

    @av._call_api_on_func
    def get_intraday_extended(self, symbol, interval='15min', slice='year1month1', **kwargs):
        """To ensure optimal API response time, this endpoint uses the CSV format which is more memory-efficient than
        JSON. """
        _FUNCTION_KEY = "TIME_SERIES_INTRADAY_EXTENDED"
        return _FUNCTION_KEY, "Time Series ({})".format(interval), 'Meta Data'

    @av._call_api_on_func
    def get_daily(self, symbol, **kwargs):
        _FUNCTION_KEY = "TIME_SERIES_DAILY"
        return _FUNCTION_KEY, 'Time Series (Daily)', 'Meta Data'

    @av._call_api_on_func
    def get_daily_adjusted(self, symbol, **kwargs):
        _FUNCTION_KEY = "TIME_SERIES_DAILY_ADJUSTED"
        return _FUNCTION_KEY, 'Time Series (Daily)', 'Meta Data'

    @av._call_api_on_func
    def get_weekly(self, symbol, **kwargs):
        _FUNCTION_KEY = "TIME_SERIES_WEEKLY"
        return _FUNCTION_KEY, 'Weekly Time Series', 'Meta Data'

    @av._call_api_on_func
    def get_weekly_adjusted(self, symbol, **kwargs):
        _FUNCTION_KEY = "TIME_SERIES_WEEKLY_ADJUSTED"
        return _FUNCTION_KEY, 'Weekly Adjusted Time Series', 'Meta Data'

    @av._call_api_on_func
    def get_monthly(self, symbol, **kwargs):
        _FUNCTION_KEY = "TIME_SERIES_MONTHLY"
        return _FUNCTION_KEY, 'Monthly Time Series', 'Meta Data'

    @av._call_api_on_func
    def get_monthly_adjusted(self, symbol, **kwargs):
        _FUNCTION_KEY = "TIME_SERIES_MONTHLY_ADJUSTED"
        return _FUNCTION_KEY, 'Monthly Adjusted Time Series', 'Meta Data'

    @av._call_api_on_func
    def get_quote_endpoint(self, symbol, **kwargs):
        _FUNCTION_KEY = "GLOBAL_QUOTE"
        return _FUNCTION_KEY, 'Global Quote', None

    @av._call_api_on_func
    def get_ticker_search(self, keywords, **kwargs):
        _FUNCTION_KEY = "SYMBOL_SEARCH"
        return _FUNCTION_KEY, 'bestMatches', None

    @av._call_api_on_func
    def get_global_market_status(self):
        _FUNCTION_KEY = "MARKET_STATUS"
        return _FUNCTION_KEY, 'markets', 'endpoint'

    def get_methods(self):
        """
        This method is used to get all function in this class that returns "_FUNCTION_KEY, '<DATA_KEY>', 'Meta Data'"
        :return: {function_name: function, ...}
        """
        excluded_methods = {'get_quote_endpoint', 'get_ticker_search', 'get_global_market_status'}
        methods = [func for func in dir(self) if
                   callable(getattr(self, func)) and not func.startswith("_") and func not in excluded_methods]
        return {method: getattr(self, method) for method in methods}
