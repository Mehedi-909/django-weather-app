from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    city = request.GET.get('city', 'Dhaka')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0adceea1fe0d408d2b75cf986adc2532'
    data = requests.get(url).json()
    payload = {
        'city' : data['name'],
        'weather' : data['weather'][0]['main'],
        'icon' : data['weather'][0]['icon'],
        'kelvin_temperature' : data['main']['temp'],
        'celcius_temperature' : int(data['main']['temp']) - 273,
        'pressure' : data['main']['pressure'],
        'humidity' : data['main']['humidity'],
        'description' : data['weather'][0]['description']
    }
    context = {'data' : payload}
    print(payload)
    return render(request, 'base.html', context)