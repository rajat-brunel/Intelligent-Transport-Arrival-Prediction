import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

data = pd.read_csv('../Dataset/Stops/data_brunel.csv', parse_dates=["time_at_origin"])

# data = data.set_index("time_at_origin")

data.drop(data.columns[data.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
drop_col = ["time_at_origin",'vehicle_id','origin', 'next_stop', 'arrival_time_at_next_Stop', 'mode',
            'prediction_correct', "weekend", 'temp', 'humidity', 'cloudCover', 'visibility',
            'distance'
            ]

data.drop(drop_col, axis=1, inplace=True)

# Data Transformation
data.peak = [1 if each == 'yes'
                    else 0 for each in data.peak]


data["time_of_day"].value_counts()
data["time_of_day"] = data["time_of_day"].map({'Morning':0,'Afternoon':1, 'Evening':2, 'Night':3})

# Heat Map Visualisation
f, ax = plt.subplots(figsize=(10, 10))
sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt='.1f', ax=ax)
plt.xticks(fontsize=8)
plt.tight_layout()
# plt.show()
plt.close()

sns.scatterplot(x='time_of_day',y='status',data=data)
plt.show()

