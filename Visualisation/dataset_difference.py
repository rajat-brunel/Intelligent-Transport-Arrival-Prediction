import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set()

data = pd.read_csv('../Dataset/dataset.csv', parse_dates=True)

data['time_at_origin'] = pd.to_datetime(data['time_at_origin'], format='%Y-%m-%dT%H:%M:%S.%f')
data['arrival_time_at_next_Stop'] = pd.to_datetime(data['arrival_time_at_next_Stop'], format='%Y-%m-%dT%H:%M:%S.%f')


data['diff'] = (data['arrival_time_at_next_Stop']-data['time_at_origin'])/np.timedelta64(1, 's')
data.set_index(pd.DatetimeIndex(data['time_at_origin']), inplace=True)

data = data[data['mode'] == "bus"]

print(data['vehicle_id'].value_counts())

