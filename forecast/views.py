import requests
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

FORECAST_URL = "https://tues2022.proxy.beeceptor.com/my/api/test"

all_temperatures = []


def get_data():
    data = requests.post(FORECAST_URL).json()
    if data['city'] != 'Sofia':
        print("Not the right city.")
        return None
    for entry in data['data']:
        all_temperatures.append(entry.get('temperature'))
    # print(all_temperatures)
    return all_temperatures


def get_most_hot():
    get_data()
    most_hot = -9999
    for temperature in all_temperatures:
        if temperature > most_hot:
            most_hot = temperature
    # print(most_hot)
    return most_hot


def get_least_hot():
    get_data()
    least_hot = 9999
    for temperature in all_temperatures:
        if temperature < least_hot:
            least_hot = temperature
    # print(least_hot)
    return least_hot


def get_average_hot():
    get_data()
    sum_temperatures = 0
    for temperature in all_temperatures:
        sum_temperatures += temperature
    # print(sum_temperatures/len(all_temperatures))
    return sum_temperatures/len(all_temperatures)


def get_all(request):
    get_data()
    return render(request, 'temperature.html', {'hottest': get_most_hot(), 'coldest': get_least_hot(),
                                                'average': get_average_hot()})
