from django.test import TestCase
import requests
from . import views
# Create your tests here.

FORECAST_URL = "https://tues2022.proxy.beeceptor.com/my/api/test"


class TestTemperatures(TestCase):
    all_temperatures = []

    def setUp(self) -> None:
        data = requests.post(FORECAST_URL).json()
        for entry in data['data']:
            self.all_temperatures.append(entry.get('temperature'))

    def testHottestTemp(self):
        most_hot = -9999
        for temperature in self.all_temperatures:
            if temperature > most_hot:
                most_hot = temperature
        assert most_hot == views.get_most_hot()

    def testColdestTemp(self):
        least_hot = 9999
        for temperature in self.all_temperatures:
            if temperature < least_hot:
                least_hot = temperature
        assert least_hot == views.get_least_hot()

    def testAverageTemp(self):
        sum_temperatures = 0
        for temperature in self.all_temperatures:
            sum_temperatures += temperature
        average_hot = sum_temperatures/len(self.all_temperatures)
        assert average_hot == views.get_average_hot()
