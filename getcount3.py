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


def Datapreprocessing(minPoint):
    df = pd.read_csv("res/DM1.csv", header=None)
    DM1 = np.array(df)
    df = pd.read_csv("res/DM2.csv", header=None)
    DM2 = np.array(df)
    # print(DM1[155])
    delete = []
    dataset = []
    row_1, column_1 = DM2.shape
    print(column_1)
    for i in range(row_1):
        for j in range(column_1):
            if minPoint > DM2[i][j] > 0 or DM2[i][j] == DM1[i][j] and DM2[i][j] > 0:
                delete.append(i * column_1 + j)
            elif DM2[i][j] > minPoint:
                dataset.append(i * column_1 + j)
    print("保留数据个数:", len(dataset))
    print("删除的异常数据个数:", len(delete))
    dataset = np.array(dataset)
    print("保留数据的编号：", dataset)

    np.savetxt(r'res/3.csv', dataset, fmt='%d', delimiter=',')
    np.savetxt(r'res/4.csv', delete, fmt='%d', delimiter=',')


# Datapreprocessing(18)
