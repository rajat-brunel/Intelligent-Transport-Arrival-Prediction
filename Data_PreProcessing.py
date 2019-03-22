import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

data = pd.read_csv('Dataset/dataset.csv')

data.set_index("vehicle_id", inplace=True)

data.drop("prediction_correct", axis=1, inplace=True)


# Create a missing values function:
def num_missing(x):
    return sum(x.isnull())


# Applying per column:
#print(data.apply(num_missing, axis=0))

# Data Transformation
data.peak = [1 if each == 'yes'
                    else 0 for each in data.peak]

data["mode"].value_counts()
data["mode"] = data["mode"].map({'bus':0,'tube':1})

data.weekend = [1 if each == 'yes'
                    else 0 for each in data.peak]

data["time_of_day"].value_counts()
data["time_of_day"] = data["time_of_day"].map({'Morning':0,'Afternoon':1, 'Evening':2, 'Night':3})

# data.to_csv("Dataset/transformed_data.csv")

# Visualising Missing Data
msno.matrix(data)
# plt.show()

# Shape of the data
print("The Shape of the data is: " + str(data.shape))

# Describing the data
print(data.describe())
