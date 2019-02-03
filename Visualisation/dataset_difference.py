import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

data = pd.read_csv('../Dataset/dataset.csv', parse_dates=True)
data['prediction_correct'] = pd.factorize(data['prediction_correct'])[0]

data['arrival_time_at_last_Stop'] = pd.to_datetime(data['arrival_time_at_last_Stop'], format='%Y-%m-%dT%H:%M:%S.%f')
data['arrival_time_at_next_Stop'] = pd.to_datetime(data['arrival_time_at_next_Stop'], format='%Y-%m-%dT%H:%M:%S.%f')


data['diff'] = (data['arrival_time_at_next_Stop']-data['arrival_time_at_last_Stop'])/np.timedelta64(1, 's')
data.set_index(pd.DatetimeIndex(data['arrival_time_at_last_Stop']), inplace=True)

plt.figure(figsize=(12,12))


plt.show()


