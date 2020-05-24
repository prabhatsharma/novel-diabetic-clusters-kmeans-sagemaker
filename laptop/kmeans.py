import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import joblib

data = pd.read_csv('diabetes_data.csv')

scaler = MinMaxScaler()

scaler.fit(data)

joblib.dump(scaler, "scaler.gz")


# scaler = joblib.load("scaler.gz")

print(scaler.feature_range)

t_data = scaler.transform(data)


# print(data.head())

Kmean = KMeans(n_clusters=5)
result = Kmean.fit(t_data)

X = [590, 91, 45, 2.39, 8.06]
X = np.reshape(X, (1,-1))
t_X = scaler.transform(X)
print(result.predict(t_X))


