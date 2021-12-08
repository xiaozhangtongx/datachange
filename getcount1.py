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
    mpl.rcParams["font.sans-serif"] = ["LiSu"]
    mpl.rcParams["axes.unicode_minus"] = False
    data = pd.read_csv('res/alldata1.csv', names=['TIME', 'MMSI', 'LNG', 'LAT'])
    data = data.drop_duplicates(keep='first', inplace=False)
    x_min = data['LNG'].min()
    x_max = data['LNG'].max()
    y_min = data['LAT'].min()
    y_max = data['LAT'].max()
    # 统计每个子区域中点的数量
    x = []
    y = []
    n = 0
    for row1 in data['LNG']:
        n += 1
        x.append(row1)
    for row2 in data['LAT']:
        y.append(row2)
    c = {"x": x, 'y': y}
    data = pd.DataFrame(c)

    # 使用矩阵分隔网格
    # 生成网格ID column_num等于列数，row_num等于行数
    def generalID(x, y, column_num, row_num):
        # 若在范围外的点，返回-1
        if x < x_min or x > x_max or y < y_min or y > y_max:
            return -1
        # 把范围根据列数等分切割
        column = (x_max - x_min) / column_num
        # 把范围根据行数等分切割
        row = (y_max - y_min) / row_num
        # 得到二维矩阵坐标索引，并转换为一维ID，即： 列坐标区域（向下取整）+ 1 + 行坐标区域 * 列数
        lable = floor((x - x_min) / column) + 1 + int((y - y_min) / row) * column_num
        # 把最上面是那个点划分给下一行
        if lable >= column_1 * row_1:
            lable = lable - 10
        return lable

    ## 对整个区域使用 1000 X 1000 划分
    data['label'] = data.apply(lambda x: generalID(x['x'], x['y'], row_1, column_1), axis=1)
    print(np.array(data))
    np.savetxt(r'res/5.csv', np.array(data), fmt='%f,%f,%d', delimiter=',')
    a = data.label
    b = np.sort(a)
    D = {}
    for k in b:
        D[k] = D.get(k, 0) + 1
    key = list(D.keys())
    values = list(D.values())

    # 构建二纬度矩阵
    a = np.ones((row_1, column_1))
    length = len(key)
    for i in range(row_1 * column_1):
        for j in range(length):
            if i == key[j]:
                a[floor(i / row_1)][floor(i % column_1 - 1)] = values[j]
                break
            else:
                a[floor(i / row_1)][floor(i % column_1 - 1)] = 0

    # a = a[::-1]
    np.savetxt(r'res/DM1.csv', a, fmt='%d', delimiter=',')
    print(f'{row_1}*{column_1}的网格划分成功！')
