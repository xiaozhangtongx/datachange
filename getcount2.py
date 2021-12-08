# 获取将1000x1000的密度矩阵DM转化为四维矩阵D（label，行值，列值，密度值）
import numpy as np
import pandas as pd


def getD():
    df = pd.read_csv("res/DM1.csv", header=None)
    df = np.array(df)

    a = []

    for i in range(len(df)):
        for j in range(len(df)):
            a.append([i, j, df[i][j], i * len(df) + j + 1])
    np.savetxt(r'res/D.csv', a, fmt='%d,%d,%d,%d', delimiter=',')


# getD()