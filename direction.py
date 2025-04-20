import openrouteservice
import json
import time

coords = ((32.7091, 39.8270),(29.0796,40.9658))
#29.9762,39.4150
client = openrouteservice.Client(key="5b3ce3597851110001cf62489a26ee3722eb4b5a8149dbf44d69931a")

response = client.directions(coords, units= "km", format="geojson")

routes = response["features"][0]

properties = routes['properties']

segments = properties["segments"][0]

steps = segments["steps"]   #steplerin listesi bu, her bir indexinde olan stepin distionarisi var

way_points = routes['geometry']['coordinates']

total_distance = segments['distance'] 

total_duration = float(segments['duration']) / 3600





def waypoint():
   return way_points





def waypo_to_geo():

   geolocation_list = []
   geolocation_index  = []

   milestone = 150

   for i, a in enumerate(way_points):

      
      
      if i == milestone or  i == len(way_points) - 1 :
         #print(a)
         #print(i)
         milestone += 200
         geolocation_list.append(a)
         geolocation_index.append(i)

   print("---------------")
   
      
   return geolocation_list, geolocation_index






def calculate():
   
   way_dis_dic = {}

   total_dis = 0
   milestone = 50

   for i in steps:
      sec_distance = i['distance']
      sec_waypoint = i['way_points']

      way_dis_dic[sec_distance] = sec_waypoint

      total_dis = total_dis + sec_distance
      
      if  total_dis > milestone:
            print('milestone : ', milestone)
            print("total : ", total_dis)
            print(sec_distance)
            print(sec_waypoint)
            print("olduuuuuuuu")
            milestone += 50
            time.sleep(3)
            

      print(sec_distance, 'km')
      print(sec_waypoint, " bu way pointler")
      print("total", total_dis)
      print("-------------------------")
      time.sleep(1)

   return way_dis_dic


   




#with open("den.json", "w") as f:
 #  json.dump(response, f , indent=4)