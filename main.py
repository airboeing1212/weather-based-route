from direction import waypo_to_geo, total_distance, total_duration , way_points
from geo_help import get_name_from_geolocation

from web import web

import time


duration_between_two_waypoint = (total_duration / len(way_points)) * 3600 #this is in seconds

hourly_waypoints = 3600 / duration_between_two_waypoint




def convert_wp_to_time(waypo, total_time):

    time_at_location = duration_between_two_waypoint * waypo

    total_time = total_time + (time_at_location / 3600) 

    return total_time



geoloc , geo_index= waypo_to_geo()

#print("geo loc: ", geoloc)
#print("geo index : ", geo_index)



total_time = 0

for a, i in enumerate(geoloc):

    my_loc = geo_index[a]

    total_tim = convert_wp_to_time(my_loc, total_time)



    for b in range(50):
        if b < total_tim < b + 1 :
            print(f" şu an {b}. saatdesin")
            break


    long, lat = i
    temp , prec , vis = web(lat,long)



    name, country , region = get_name_from_geolocation(i)


    print("------------------------------------------")
    print("name of the place : ", name)
    print("country of the place : ", country)
    print("region of the place : ", region)
    print("temperature is : ", temp[b], "celcius")
    #print("temperature is : ", temp)
    print("precipition is : ", prec[b], "mm")
    print("the visibilty is : ", vis[b], "km")
    print("geolocation is : ", i)
    print("------------------------------------------")
    time.sleep(1)