import openrouteservice
import time 
from dotenv import load_dotenv
import os

load_dotenv()

client = openrouteservice.Client(key=os.getenv('ORS_API_KEY'))

def get_name_from_geolocation(geoloc):

    response = client.pelias_reverse(geoloc)
    main = response['features'][0]['properties']

    name = main['name']
    country = main['country']
    region = main['region']
    return name, country, region





