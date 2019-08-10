import requests
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import CityForm
from .models import City


# TODO: how often  look for weather in the city
# def city_count(city):
#     count_city = City.objects.filter(name=city).count()
#     print(count_city)
#     return count_city


def get_cities(request, cities):
    app_id = '96bb2a60d868d3155ab9f65061e3c098'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + app_id
    last_city = City.objects.first()
    try:
        res = requests.get(url.format(last_city.name)).json()
        data_info = {
            'city': last_city.name,
            'temp': res['main']['temp'],
            'icon': res["weather"][0]["icon"]
        }
    except Exception as ex:
        print('Error: ', ex.__repr__())
        messages.error(request, 'Something wrong. Try again')
        last_city = City.objects.first()
        last_city.delete()
        redirect('home')
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        data_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(data_info)
    return all_cities


def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
        return redirect('home')
    form = CityForm()  # clear form
    cities = City.objects.all()[:8]
    all_cities = get_cities(request, cities)
    return render(request, 'weather/index.html', {'cities_info': all_cities,
                                                  'form': form
                                                  })


def about(request):
    return render(request, 'weather/about.html')
