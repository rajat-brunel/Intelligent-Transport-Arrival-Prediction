import pandas as pd
from datetime import datetime
import numpy as np
from numpy import log
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error

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
rol_mean = data.rolling(window=4).mean()
rol_std = data.rolling(window=4).std()

# print(rol_mean, rol_std)

orig = plt.plot(data, color='blue', label='Original')
mean = plt.plot(rol_mean, color='red', label='Rolling Mean')
std = plt.plot(rol_std, color='black', label='Rolling Std')
plt.legend(loc='best')
plt.title('Rolling Mean & Standard Deviation')
# plt.show(block=False)
plt.close()

# Estimating trend
data_shift = data - data.shift()
plt.plot(data)
# plt.show(block=False)
plt.close()


# The below transformation is required to make series stationary
movingAverage = data.rolling(window=4).mean()
movingSTD = data.rolling(window=4).std()
plt.plot(data)
plt.plot(movingAverage, color='red')
plt.plot(movingSTD, color='green')
plt.xticks(rotation=90)
# plt.show()
plt.close()


datasetLogScaleMinusMovingAverage = data - movingAverage
#print(datasetLogScaleMinusMovingAverage.head(12))

#Remove NAN values
datasetLogScaleMinusMovingAverage.dropna(inplace=True)
#print(datasetLogScaleMinusMovingAverage.head(10))


# Perform the Dickey Fuller Test
def test_stationarity(timeseries):
    # Determine rolling statistics
    movingAverage = timeseries.rolling(window=4).mean()
    movingSTD = timeseries.rolling(window=4).std()

    # Plot rolling statistics
    orig = plt.plot(timeseries, color='blue', label='Original')
    mean = plt.plot(movingAverage, color='red', label='Rolling Mean')
    std = plt.plot(movingSTD, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    #plt.show(block=False)

    # Perform Dickey–Fuller test:
    print('Results of Dickey Fuller Test:')
    dftest = adfuller(timeseries['status'], autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' % key] = value
    print(dfoutput)


test_stationarity(datasetLogScaleMinusMovingAverage)

plt.plot(data_shift)
plt.xticks(rotation=90)
#plt.show()
plt.close()

data_shift.dropna(inplace=True)
test_stationarity(data_shift)

# ACF & PACF plots

lag_acf = acf(data_shift, nlags=10)
lag_pacf = pacf(data_shift, nlags=10, method='ols')

# Plot ACF:
plt.subplot(121)
plt.plot(lag_acf)
plt.axhline(y=0, linestyle='--', color='gray')
plt.axhline(y=-1.96 / np.sqrt(len(data_shift)), linestyle='--', color='gray')
plt.axhline(y=1.96 / np.sqrt(len(data_shift)), linestyle='--', color='gray')
plt.title('Autocorrelation Function')

# Plot PACF
plt.subplot(122)
plt.plot(lag_pacf)
plt.axhline(y=0, linestyle='--', color='gray')
plt.axhline(y=-1.96 / np.sqrt(len(data_shift)), linestyle='--', color='gray')
plt.axhline(y=1.96 / np.sqrt(len(data_shift)), linestyle='--', color='gray')
plt.title('Partial Autocorrelation Function')

plt.tight_layout()
# plt.show()
plt.close()

X = data_shift.values
size = int(len(X) * 0.5)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
print(size)

for t in range(len(test)):
    model = ARIMA(history, order=(1, 0, 1))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0]
    predictions.append(yhat)
    obs = test[t]
    history.append(obs)
    print('predicted=%f, expected=%f' % (yhat, obs))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)

# plot
plt.plot(test)
plt.plot(predictions, color='red')
plt.legend(['test','prediction'])
plt.show()