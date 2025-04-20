from direction import waypo_to_geo, waypoint
import openrouteservice
import time 


geolo = waypoint()

client = openrouteservice.Client(key="5b3ce3597851110001cf62489a26ee3722eb4b5a8149dbf44d69931a")




def get_name_from_geolocation(geoloc):


    response = client.pelias_reverse(geoloc)
    main = response['features'][0]['properties']

    name = main['name']
    country = main['country']
    region = main['region']
    return name, country, region



    '''mil = 100

    for i, a in enumerate(geoloc):
        
        if i % 100 == 0:

            respose = client.pelias_reverse(a)

            main = respose['features'][0]['properties']

            name = main['name']
            country = main['country']
            region = main['region']
            #neighbourhood = main['neighbourhood']

            print("name of this place is : ", name)
            print("country is : ", country)
            print("region is : ", region)
            #print("neigborhood is : ", neighbourhood)
        mil += 100

        
        

get_name_from_geolocation(geolo)'''



