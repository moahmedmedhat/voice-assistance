import datetime
import requests
import pprint
def weather(city='Suez'):
    baseurl="http://api.openweathermap.org/data/2.5/weather?"
    apikey="86ed073c6ebef01d592d1d66412de1d4"
    url=baseurl + "appid=" + apikey + "&q=" + city
    response=requests.get(url).json()
    temp_k=response['main']['temp']
    temp_c=temp_k - 273.15
    return f"{temp_c}c"


temp=weather()

print(temp)