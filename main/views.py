import json
from math import ceil
from django.shortcuts import redirect, render  
import urllib.request  
from django.conf import settings

apid=settings.APID
   
# Create your views here.  
  
def home(request):  
    if request.method == 'POST':  
        # Get the city name from the user api = http://api.openweathermap.org/data/2.5/weather  
        city = request.POST.get('city', 'True')
        city=city.replace(" ","+")

          
        # retreive the information using api  
        source = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={apid}').read()  
        # convert json data file into python dictionary  
        list_of_data = json.loads(source)  
        print(list_of_data)  
        # create dictionary and convert value in string 

        temp=list_of_data['main']['temp']
        tem=ceil((temp-32)*5/9) 
        context = {
            'city': city.replace("+"," "),  
            "country_code": str(list_of_data['sys']['country']), 
            "sunset":str(list_of_data['sys']['sunset']), 
            "temp": str(tem),  
            "description":str(list_of_data['weather'][0]['description']),
            "icon":str(list_of_data['weather'][0]['icon'])  
        }
    else:
        context={}
    # send dictionary to the index.html  
    return render(request, 'home.html', context)  