import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# df = pd.read_csv("data/data.csv", encoding="gbk", low_memory=False, names=["LNG", "LAT"])
df = pd.read_csv('res/alldata1.csv', names=['TIME', 'MMSI', 'LNG', 'LAT'])
print(df)
x = df['LNG']
y = df['LAT']
plt.title("oldest")
plt.plot(x, y, '.', label='ship', color='black')
plt.show()
