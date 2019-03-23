import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error,r2_score

## for Neural Network:
import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dropout

sns.set()


df = pd.read_csv('Dataset/Stops/baker_st.csv', parse_dates=["time_at_origin"])

df = df.set_index("time_at_origin")
drop_col = ['vehicle_id', 'origin', 'next_stop', 'arrival_time_at_next_Stop', 'prediction_correct']
df.drop(drop_col, axis=1, inplace=True)

# print(df.head())

df.drop(df.columns[df.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
# print(df.info())

# Data Transformation
df.peak = [1 if each == 'yes'
                    else 0 for each in df.peak]

df["mode"].value_counts()
df["mode"] = df["mode"].map({'bus':0,'tube':1})

df.weekend = [1 if each == 'yes'
                    else 0 for each in df.peak]

df["time_of_day"].value_counts()
df["time_of_day"] = df["time_of_day"].map({'Morning':0,'Afternoon':1, 'Evening':2, 'Night':3})

np.set_printoptions(suppress=True)
print(df.head())


def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    dff = pd.DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(dff.shift(i))
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(dff.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
    # put everything all together
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg


values = df.values

scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)

reframed = series_to_supervised(scaled, 1, 1)
pd.set_option('display.max_columns', None)

reframed.drop(reframed.columns[[10,11,12,13,14,15,16,17,18]], axis=1, inplace=True)
print(reframed.head())

values = reframed.values
length = len(values)
n_train_time = int(length * 0.75)


train = values[:n_train_time, :]
test = values[n_train_time:, :]

# split into input and outputs
train_X, train_y = train[:, :-1], train[:, -1]
test_X, test_y = test[:, :-1], test[:, -1]

# reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)
# We reshaped the input into the 3D format as expected by LSTMs, namely [samples, timesteps, features].

# Start Modelling the LSTM Model

model = Sequential()
model.add(LSTM(10, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dropout(0.1))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

history = model.fit(train_X, train_y, epochs=150, batch_size=50,
                    validation_data=(test_X, test_y), verbose=2, shuffle=False)

# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper right')
plt.show()

# make a prediction
yhat = model.predict(test_X)
test_X = test_X.reshape((test_X.shape[0], 10))

# invert scaling for forecast
inv_yhat = np.concatenate((test_X[:, -9:], yhat),  axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:,9]


# invert scaling for actual
test_y = test_y.reshape((len(test_y), 1))
inv_y = np.concatenate((test_X[:, -9:], test_y), axis=1)
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:,9]


rmse = np.sqrt(mean_squared_error(inv_y, inv_yhat))
print('Test RMSE: %.3f' % rmse)

error = mean_squared_error(inv_y, inv_yhat)
print('Test MSE: %.3f' % error)

rng = len(inv_y)
aa=[x for x in range(rng)]
plt.plot(aa, inv_y[:rng], marker='.', label="actual")
plt.plot(aa, inv_yhat[:rng], 'r',marker='.', label="prediction")
plt.ylabel('Status', size=15)
plt.xlabel('Time step', size=15)
plt.legend(fontsize=15)
plt.show()