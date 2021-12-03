# 对比1000x1000密度矩阵DM2的每个元素DM2 ij与DM ij大小，
# 若DM1 ij = DM ij，则点（i, j）为噪声点，从数据库移除，标记存放在噪声点数据库；
# Step 7. 对比1000x1000密度矩阵DM1的每个元素DM1 ij与MinPts（最小密度）大小，初始化设置MinPts（最小密度）=50
# 若DM1 ij<MinPts，则DM1 ij对应1000x1000密度矩阵中的3*3邻域（9个点）为噪声点，标记噪声点，保存为噪声点数据库；
# 若DM1 ij>=MinPts，则DM1 ij对应1000x1000密度矩阵中的3*3邻域9个点为正常点，保留，形成新的data set；
from timeit import timeit

from matplotlib import pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
from math import *

df = pd.read_csv("res/DM1.csv", header=None)
DM1 = np.array(df)
df = pd.read_csv("res/DM2.csv", header=None)
DM2 = np.array(df)

minPoint = 18

delete = []
dataset = []
a1 = []
row_1 = len(DM2)
column_1 = len(DM2)
print(len(DM2))
for i in range(row_1):
    for j in range(column_1):
        if minPoint > DM2[i][j] and DM2[i][j] > 0 or DM2[i][j] == DM1[i][j] and DM2[i][j] > 0:
            delete.append(i * row_1 + j)
        elif DM2[i][j] > minPoint:
            dataset.append(i * row_1 + j)

print(len(delete))
print(len(dataset))
dataset = np.array(dataset)
print(dataset)

np.savetxt(r'res/3.csv', dataset, fmt='%d', delimiter=',')
np.savetxt(r'res/4.csv', delete, fmt='%d', delimiter=',')
