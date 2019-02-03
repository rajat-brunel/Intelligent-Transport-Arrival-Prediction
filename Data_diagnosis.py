import numpy as np
import pandas as pd

data = pd.read_csv('Dataset/Old_dataset_time.csv')

#print(data.head())

col = data.columns
#print(col)

arrival = data.arrival_time_at_last_Stop

print(arrival.dtype)

data['arrival_time_at_last_Stop'] = pd.to_datetime(data['arrival_time_at_last_Stop'], format='%Y-%m-%dT%H:%M:%S.%f')
data['arrival_time_at_next_Stop'] = pd.to_datetime(data['arrival_time_at_next_Stop'], format='%Y-%m-%dT%H:%M:%S.%f')

print(data.arrival_time_at_last_Stop)

data.to_csv("Dataset/new_dataset.csv", index=None)
