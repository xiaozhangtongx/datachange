# （lable，密度值）可视化
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

pd = pd.read_csv("res/D.csv", names=["x", "y", "count", "lable"])

x = np.array(pd['lable'])
y = np.array(pd['count'])

plt.ylim((0, 20))
plt.plot(x, y, '.')

plt.show()
