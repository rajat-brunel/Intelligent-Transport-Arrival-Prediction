import pandas as pd
from datetime import datetime
import numpy as np
from numpy import log
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller

sns.set()

data = pd.read_csv('Dataset/Stops/data_brunel.csv', parse_dates=["time_at_origin"])

data = data.set_index("time_at_origin")


data.drop(data.columns[data.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
drop_col = ['vehicle_id', 'origin', 'next_stop', 'arrival_time_at_next_Stop',
            'distance', 'peak', 'time_of_day', 'mode', 'temp', 'humidity', 'cloudCover', 'visibility',
            'weekend', 'prediction_correct']
data.drop(drop_col, axis=1, inplace=True)

# print(data.index)

plt.figure(figsize=(16, 12))
# print(data.tail(10))

plt.xlabel('Date')
plt.ylabel('Delay Status')
plt.plot(data)
# plt.show()

# Determine rolling statistics
rol_mean = data.rolling(window=4).mean() #window size 12 denotes 12 months, giving rolling mean at yearly level
rol_std = data.rolling(window=4).std()

# print(rol_mean, rol_std)

orig = plt.plot(data, color='blue', label='Original')
mean = plt.plot(rol_mean, color='red', label='Rolling Mean')
std = plt.plot(rol_std, color='black', label='Rolling Std')
plt.legend(loc='best')
plt.title('Rolling Mean & Standard Deviation')
# plt.show(block=False)

# Perform Augmented Dickey–Fuller test:
print('Results of Dickey Fuller Test:')
dftest = adfuller(data['status'], autolag='AIC')

dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
for key, value in dftest[4].items():
    dfoutput['Critical Value (%s)' % key] = value

print(dfoutput)

