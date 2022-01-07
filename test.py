# 绘制散点图将整个区域分为10乘10个网格，并统计每个网格中点的个数
from timeit import timeit

from matplotlib import pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import os
import csv
from math import *


def grid(row_1, column_1):
    key = {}
    for i in range(row_1 * column_1):
        key[i] = i * 2

    # 构建二纬度矩阵
    a = np.ones((row_1, column_1))
    length = len(key)
    for i in range(row_1 * column_1):
        for j in range(length):
            if i == key[j]:
                a[floor(i / column_1)][floor(i % column_1)] = key[j]
                break
            else:
                a[floor(i / column_1)][floor(i % column_1)] = 0

    # a = a[::-1]
    np.savetxt(r'res/test.csv', a, fmt='%d', delimiter=',')
    print(f'{column_1}*{row_1}的网格划分成功！')


# grid(180, 360);
grid(10, 36)
