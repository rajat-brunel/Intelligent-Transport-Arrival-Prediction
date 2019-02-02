import json
from urllib.request import urlopen
import csv
import time
import distances
from random import randint

cur_time = time.time()
wakeup = cur_time + 3600
station_name = ""
cur_last_stop = "Origin"
cur_arrival_last = "0"
peak = "no"
mode = "bus"
time_of_day = "Morning"
distance = 0
v_id = "LK58KHL"
r_no = randint(0, 1000)
filename = r"C:\Users\rajat\PycharmProjects\untitled\Dataset\ " +v_id+"_"+time_of_day+"_"+peak+"_"+mode+str(r_no)+".csv"

while cur_time < wakeup:
    with urlopen("https://api.tfl.gov.uk/Vehicle/" + v_id + "/Arrivals?"
             "app_id=e34fba97&app_key=fc84f1bb481fa4aae1826fb5f5ea59c3") as response:
        source = response.read()
        data = json.loads(source)

    with open(filename, 'a') as csv_file:
        fieldnames = ['vehicle_id', 'last_stop', 'arrival_time_at_last_Stop', 'next_stop',
                      'arrival_time_at_next_Stop', 'distance', 'peak', 'time_of_day', 'mode']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator='\n')
        csv_reader = csv.DictReader(csv_file)
       # csv_writer.writeheader()

#print(json.dumps(data, indent=2))

        for item in data:
                if station_name == item['stationName']:
                    if arrival_next == item['expectedArrival']:
                        print("not updated")
                        break
                    else:
                        arrival_next = item['expectedArrival']
                        print("prediction changed!")
                        print(vehicle_id, cur_last_stop, cur_arrival_last, next_stop, arrival_next, distance, peak, time_of_day, mode)
                        csv_writer.writerow({'vehicle_id': vehicle_id, 'last_stop': cur_last_stop,
                                             'arrival_time_at_last_Stop': cur_arrival_last,
                                             'next_stop': next_stop,
                                             'arrival_time_at_next_Stop': arrival_next,
                                             'distance': distance,
                                             'peak': peak,
                                             'time_of_day': time_of_day,
                                             'mode': mode})
                        cur_arrival_last = item['expectedArrival']
                        break
                else:
                    station_name = item['stationName']
                    vehicle_id = item['vehicleId']
                    next_stop = item['stationName']
                    arrival_next = item['expectedArrival']
                    if cur_last_stop != "Origin":
                        distance = distances.distances_inbound(cur_last_stop, next_stop)
                    else:
                        distance = 0
                    print(vehicle_id, cur_last_stop, cur_arrival_last, next_stop, arrival_next, distance, peak, time_of_day, mode)
                    csv_writer.writerow({'vehicle_id': vehicle_id, 'last_stop': cur_last_stop,
                                         'arrival_time_at_last_Stop': cur_arrival_last,
                                         'next_stop': next_stop,
                                         'arrival_time_at_next_Stop': arrival_next,
                                         'distance': distance,
                                         'peak': peak,
                                         'time_of_day': time_of_day,
                                         'mode': mode})
                    cur_last_stop = next_stop
                    cur_arrival_last = arrival_next
                break
    time.sleep(10)
    cur_time = time.time()


