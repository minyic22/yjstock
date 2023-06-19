import csv
import inspect
import requests
import json
import configparser
from functools import wraps


class AlphaVantage:
    _ALPHA_VANTAGE_API_URL = "https://www.alphavantage.co/query?"

    def __init__(self, key=None):
        if key is None:
            config = configparser.ConfigParser()
            config.read('my_config.ini')
            key = config['authentication']['api_key']
        self.key = key

    def _handle_api_call(self, url):
        response = requests.get(url)
        if 'application/json' in response.headers['Content-Type']:
            data = response.json()  # parse the response as JSON
            if not data:
                raise ValueError('Error getting data from the api, no return was given.')
            if "Error Message" in data or "Information" in data or "Note" in data:
                raise ValueError(data.get("Error Message", data.get("Information", data.get("Note"))))
        else:
            # Response is in csv format
            reader = csv.reader(response.text.splitlines())
            data = "\n".join([",".join(row) for row in reader])
            if not data:
                raise ValueError('Error getting data from the api, no return was given.')
        return data

    @property
    def alpha_vantage_api_url(self):
        return self._ALPHA_VANTAGE_API_URL

    @classmethod
    def _call_api_on_func(cls, func):
        sig = inspect.signature(func)
        param_defaults = {name: param.default for name, param in sig.parameters.items() if
                          param.default is not param.empty}
        positional_params = [name for name, param in sig.parameters.items() if
                             param.kind in (param.POSITIONAL_OR_KEYWORD, param.POSITIONAL_ONLY)][1:]

        @wraps(func)
        def _call_wrapper(self, *args, **kwargs):
            function_name, data_key, meta_data_key = func(self, *args, **kwargs)
            api_params = {**param_defaults, **dict(zip(positional_params, args)), **kwargs, 'function': function_name,
                          'apikey': self.key}
            url = self.alpha_vantage_api_url + '&'.join(f'{k}={v}' for k, v in api_params.items())
            return self._handle_api_call(url), data_key, meta_data_key

        return _call_wrapper
