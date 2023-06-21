import json
from django.shortcuts import render
import urllib.request
from django.conf import settings
from django.contrib import messages

apid = settings.APID

# Create your views here.
import urllib.error


def home(request):
    context = {}

    if request.method == 'POST':
        # Get the city name from the user
        city = request.POST.get('city', 'True')
        city = city.replace(" ", "+")

        try:
            # Retrieve the information using API
            source = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={apid}').read()
            # Convert JSON data file into Python dictionary
            list_of_data = json.loads(source)

            temp = list_of_data['main']['temp']
            tem = round((temp - 32) * 5 / 9)
            context = {
                'city': city.replace("+", " "),
                "country_code": str(list_of_data['sys']['country']),
                "temp": str(tem),
                "description": str(list_of_data['weather'][0]['description']),
                "icon": str(list_of_data['weather'][0]['icon'])
            }
        except urllib.error.HTTPError as e:
            # If HTTPError 404 occurs, set error message in context dictionary
            if e.code == 404:
                messages.error(request, f"{city.replace('+', ' ')} is not a valid city name")
    # Send dictionary to the index.html
    return render(request, 'home.html', context)
