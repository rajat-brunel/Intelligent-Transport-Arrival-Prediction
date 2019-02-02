from geopy.geocoders import Nominatim
import pandas as pd

nom = Nominatim()

loc_name = ""

data = pd.read_csv('Dataset/Locations.csv')
data["lat"] = None
data["lon"] = None

for i in range(0, 6190, 1):
    loc_name = data.iat[i, 0]
    try:
        name = loc_name + ", " + "London, United Kingdom"
        print(name)
        a = nom.geocode(name)
        data.iat[i, data.columns.get_loc("lat")] = a.latitude
        data.iat[i, data.columns.get_loc("lon")] = a.longitude
        print(a.latitude)
        print(a.longitude)
    except:
        lat = None
        lon = None

data.to_csv("loc_time.csv")