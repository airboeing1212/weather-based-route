import openrouteservice
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()

coords = ((32.7091, 39.8270),(29.0796,40.9658))  #(long,lat)
#29.9762,39.4150
client = openrouteservice.Client(key=os.getenv('ORS_API_KEY'))

response = client.directions(coords, units= "km", format="geojson")


routes = response["features"][0]

properties = routes['properties']

segments = properties["segments"][0]

#steps = segments["steps"]   #steps list, includes step dict in index

way_points = routes['geometry']['coordinates']

total_distance = segments['distance'] 

total_duration = float(segments['duration']) / 3600


def waypo_to_geo():

   geolocation_list = []
   geolocation_index  = []

   milestone = 150

   for i, a in enumerate(way_points):
      
      if i == milestone or  i == len(way_points) - 1 :
         milestone += 200
         geolocation_list.append(a)
         geolocation_index.append(i)

   print("---------------")
         
   return geolocation_list, geolocation_index

