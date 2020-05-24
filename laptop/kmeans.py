import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv('diabetes_data.csv')

print(data.head())

Kmean = KMeans(n_clusters=5)
result = Kmean.fit(data)

X = [590, 91, 45, 2.39, 8.06]
X = np.reshape(X, (1,-1))
print(result.predict(X))

