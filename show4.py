import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("res/5.csv", encoding="gbk", low_memory=False, names=["x", "y", "lable"])

data = pd.read_csv("res/4.csv", encoding="gbk", low_memory=False, names=["lable"])

data = np.array(data)

x = []
y = []

for i in range(len(df)):
    if df["lable"][i] in data:
        x.append(df["x"][i])
        y.append(df["y"][i])
# print(x)
plt.title("delete")
plt.plot(x, y, '.', label='ship', color='black')
plt.show()
