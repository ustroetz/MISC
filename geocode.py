from geopy import geocoders  

def geocode(adress_Input):
    """
      Gecodes adresses and prints out coordinates
      It tries a series of geocoding engines defined in the services list. 
     """
    lat = lon = None
    
    services = [
        geocoders.ArcGIS(),         # LIMIT 1,000 requests per year
        geocoders.GoogleV3(),       # LIMIT 2,500 requests per 24 hour period
        geocoders.Nominatim(),      # UNLIMITED
        geocoders.OpenMapQuest(),   # UNLIMITED
        # these are tried in reverse order, unlimited first
        ]
    
    while not (lat and lon):
        try:
            g = services.pop()
        except IndexError:
            print "Could not geocode: " + adress_Input
            break  # no more search engines left to try
        
        try:
            place, (lat, lon) = g.geocode(adress_Input)
            print place, lat, lon
        except:
            pass

    
if __name__ == "__main__":
    adress_List = [
                    "175 5th Avenue NYC",
                    "Gartenstrasse 14, Thiersheim 95707",
                    "Bundesalle 171 10715 Berlin",
                    "This is a wrong adress"
                    ]
    
    for adress in adress_List:
        geocode(adress)

