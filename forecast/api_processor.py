import requests

FORECAST_URL = "https://tues2022.proxy.beeceptor.com/my/api/test"


class ApiProcessor:

    def print_forecast(self):
        data = requests.post(FORECAST_URL).json()
        return data
