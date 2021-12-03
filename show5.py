# （lable，密度值）可视化
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

pd = pd.read_csv("res/6.csv", names=["speed", 'SSMI', 'TIME'])
print('最大值', pd['speed'].max())
print('最小值', pd['speed'].min())
print('平均值', pd['speed'].mean())
print(pd)
x = np.array(pd.index)
y = np.array(pd['speed'])

plt.ylim((0, 10))
plt.plot(x, y, '.')

plt.show()
