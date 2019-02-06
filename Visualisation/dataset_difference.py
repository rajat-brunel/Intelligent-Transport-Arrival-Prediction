import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set()

data = pd.read_csv('../Dataset/dataset.csv', parse_dates=True)

data['arrival_time_at_last_Stop'] = pd.to_datetime(data['arrival_time_at_last_Stop'], format='%Y-%m-%dT%H:%M:%S.%f')
data['arrival_time_at_next_Stop'] = pd.to_datetime(data['arrival_time_at_next_Stop'], format='%Y-%m-%dT%H:%M:%S.%f')


data['diff'] = (data['arrival_time_at_next_Stop']-data['arrival_time_at_last_Stop'])/np.timedelta64(1, 's')
data.set_index(pd.DatetimeIndex(data['arrival_time_at_last_Stop']), inplace=True)

data = data[data['mode'] == "bus"]

print(data['next_stop'].value_counts())

plt.figure(figsize=(30, 15))
sns.countplot(data['next_stop'])
plt.xlabel("Bus Stops")
plt.xticks(rotation=90)

plt.show()