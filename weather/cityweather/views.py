from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=58af3a82ce5803f7b0d76455fae02110'
    cities = City.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
        #print(form.errors)

    form = CityForm()
    weather_data = []
    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon'],
        }
        weather_data.append(weather)
    context = {'weather_data' : weather_data}
    return render(request, 'weather/index.html', context)   

