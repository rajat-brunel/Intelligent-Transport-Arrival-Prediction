import json
from urllib.request import urlopen
import pandas as pd

key = "df68994576b3241a2dfcf4dba72420df"
data = pd.read_csv('Dataset/exported_datetime.csv')
lat = ""
long = ""
time = ""
data["temp"] = None
data["humidity"] = None
data["cloudCover"] = None
data["visibility"] = None

for i in range(0, 999, 1):
    time = str(data.iat[i, 0])
    lat = str(data.iat[i, 1])
    long = str(data.iat[i, 2])
    with urlopen(
            "https://api.darksky.net/forecast/" + key + "/" + lat + "," + long + "," + time + "?exclude=[hourly,daily]&units=si") as response:
        source = response.read()
        data_json = json.loads(source)
    try:
        data.iat[i, data.columns.get_loc("temp")] = data_json["currently"]["temperature"]
        data.iat[i, data.columns.get_loc("humidity")] = data_json["currently"]["humidity"]
        data.iat[i, data.columns.get_loc("cloudCover")] = data_json["currently"]["cloudCover"]
        data.iat[i, data.columns.get_loc("visibility")] = data_json["currently"]["visibility"]
        print(data_json["currently"]["temperature"], data_json["currently"]["humidity"],
              data_json["currently"]["cloudCover"],
              data_json["currently"]["visibility"])
    except:
        data.iat[i, data.columns.get_loc("temp")] = None
        data.iat[i, data.columns.get_loc("humidity")] = None
        data.iat[i, data.columns.get_loc("cloudCover")] = None
        data.iat[i, data.columns.get_loc("visibility")] = None


data.to_csv("weather.csv")