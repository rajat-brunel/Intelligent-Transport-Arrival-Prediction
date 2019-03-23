import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

data = pd.read_csv('../Dataset/dataset.csv', parse_dates=True)

data['time_at_origin'] = pd.to_datetime(data['time_at_origin'], format='%Y-%m-%dT%H:%M:%S.%f')

data['arrival_time_at_next_Stop'] = pd.to_datetime(data['arrival_time_at_next_Stop'], format='%Y-%m-%dT%H:%M:%S.%f')


data['diff'] = (data['arrival_time_at_next_Stop']-data['time_at_origin'])/np.timedelta64(1, 's')
#data.set_index(pd.DatetimeIndex(data['time_at_origin']), inplace=True)

data.sort_values(by='time_at_origin', inplace=True)

data = data[data['next_stop'] == "Eastcote Underground Station"]

if np.where(data['origin'] == 'Rayners Lane Underground Station'):
    data['status'] = ((data['diff']) - 180.0) / 60.0
if np.where(data['origin'] == 'Ruislip Manor Underground Station'):
    data['status'] = ((data['diff']) - 120.0) / 60.0
if np.where(data['origin'] == 'West Harrow Underground Station'):
    data['status'] = ((data['diff']) - 300.0) / 60.0

data.drop('diff', axis=1, inplace=True)

#plt.figure(figsize=(14,10))

#plt.plot(data.time_at_origin, data.temp)

#plt.xlabel("Date")
#plt.ylabel("Mean Temperature")
#plt.show()

print(data.status)

data.to_csv("../Dataset/stops/eastcote.csv")


