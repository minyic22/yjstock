import time

from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse

from alpha_vantange_wrapper.fundamentaldata import FundamentalData
from alpha_vantange_wrapper.timeseries import TimeSeries
from django.core.cache import cache
from django.views.decorators.cache import cache_page

TS_API = TimeSeries()  # get timeseries data
FD_API = FundamentalData()  # get fundamental data
CACHE_TIME = 60  # Redis cache time

# all functions will return _FUNCTION_KEY, <DATA_KEY>, Meta Data
# FUNCTIONS_MAP = TS_API.get_methods()
FUNCTIONS_MAP = {
    # time series
    'intraday': TS_API.get_intraday,
    'intraday_extended': TS_API.get_intraday_extended,
    'daily': TS_API.get_daily,
    'daily_adjusted': TS_API.get_daily_adjusted,
    'weekly': TS_API.get_weekly,
    'weekly_adjusted': TS_API.get_weekly_adjusted,
    'monthly': TS_API.get_monthly,
    'monthly_adjusted': TS_API.get_monthly_adjusted,
    # fundamental data
    'quote_endpoint': TS_API.get_quote_endpoint,
    'overview': FD_API.get_company_overview,
    'income_statement': FD_API.get_income_statement,
    'balance_sheet': FD_API.get_balance_sheet,
    'cash_flow': FD_API.get_cash_flow,
}


@cache_page(CACHE_TIME)
@require_http_methods(["GET"])
def get_stock_data(request, symbol, function: str):
    function = function.lower()
    if function not in FUNCTIONS_MAP:
        return HttpResponseBadRequest('Invalid function')

    params = request.GET.dict()  # optional params
    call_response, function_name, meta_data = FUNCTIONS_MAP[function](symbol, **params)
    if isinstance(call_response, dict):  # JSON response
        return JsonResponse(call_response)
    elif isinstance(call_response, str):  # CSV response
        response = HttpResponse(call_response, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}_{}.csv'.format(symbol, function)
        return response
    else:
        return HttpResponseBadRequest('Invalid response type')


@cache_page(CACHE_TIME)
@require_http_methods(["GET"])
def ticker_search(request, user_input):
    params = request.GET.dict()
    call_response, function_name, _ = TS_API.get_ticker_search(user_input, **params)

    if isinstance(call_response, dict):  # JSON response
        return JsonResponse(call_response)
    elif isinstance(call_response, str):  # CSV response
        response = HttpResponse(call_response, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}_{}.csv'.format("search", user_input)
        return response
    else:
        return HttpResponseBadRequest('Invalid response type')


@cache_page(CACHE_TIME)
@require_http_methods(["GET"])
def test(request, symbol):
    # Compute the value (this could be an expensive operation)
    time.sleep(20)
    value = "test"

    return HttpResponse(value)
