import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def showold():
    # df = pd.read_csv("data/data.csv", encoding="gbk", low_memory=False, names=["LNG", "LAT"])
    df = pd.read_csv('res/alldata.csv')
    print(df)
    fig, (ax1) = plt.subplots()
    x = df['LNG']
    y = df['LAT']
    ax1.set_ylim([-90, 90])
    ax1.set_xlim([-180, 180])
    plt.title("oldest")
    plt.plot(x, y, '.', label='ship', color='black')

    plt.show()


showold()
