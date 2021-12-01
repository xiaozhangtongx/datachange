import glob
import os

import numpy as np
import pandas as pd
from haversine import haversine
from math import *


def getspeed(a, j):
    return haversine((a[j][3], a[j][2]), (a[j + 1][3], a[j + 1][2])) * 100 / (
            a[j + 1][0] - a[j][0])


# print(os.path.dirname(os.getcwd()))
inputfile = "data1\\*.csv"
outputfile = "res/alldata1.csv"
csv_list = glob.glob(inputfile)

print(len(csv_list))

filepath = csv_list[0]
df = pd.read_csv(filepath, encoding="gbk", low_memory=False, names=['TIME', 'MMSI', 'LNG', 'LAT'])
df = df.to_csv(outputfile, encoding="gbk", index=False)
print(csv_list)
a = []
speed = []
for i in range(0, len(csv_list)):
    filepath = csv_list[i]
    df = pd.read_csv(filepath, encoding="gbk", low_memory=False, names=['TIME', 'MMSI', 'LNG', 'LAT'])
    df = df.drop_duplicates(keep='first', inplace=False, subset=['LNG', 'LAT'])
    df = df.sort_values(by="TIME", ascending=True)
    df = np.array(df)
    for j in range(len(df)):
        # print(sqrt(pow((df[j][3] - df[j][2]), 2) + pow((df[j + 1][3] - df[j + 1][2]), 2)) / (
        #             df[j + 1][0] - df[j][0]) )
        if (df[j][3] > 90 or df[j][3] < -90) or (df[j][2] > 180 or df[j][2] < -180) or j + 1 >= len(df):
            # print(df[j][3])
            break
        else:
            speed.append(getspeed(df, j))
            if 2 > getspeed(df, j) > 0.25:
                a.append(df[j])
            # else:
            # print(haversine((df[j][3], df[j][2]), (df[j + 1][3], df[j + 1][2])) * 1000 / (
            #         df[j + 1][0] - df[j][0]))
np.savetxt(outputfile, a, delimiter=',')
np.savetxt(r'res/6.csv', speed, fmt='%f', delimiter=',')
