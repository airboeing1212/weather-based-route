import requests
import json


def web(lat,long):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": long,
        "current_weather": True,
        "hourly": "temperature_2m,precipitation,visibility",
        "forecast_hours" : 6        
    }


    response = requests.get(url, params=params)
    data = response.json()

    temp = data['hourly']["temperature_2m"]

    prec = data['hourly']["precipitation"]

    visibility = data['hourly']['visibility']

    visibilit = [i/1000 for i in visibility ]

    '''with open("weather.json", "w") as f:
        json.dump(data, f, indent=4)'''

    return temp , prec, visibilit


    
