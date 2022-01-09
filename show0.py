# 原始数据热力图
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# % matplotlib inline
def show():
    df = pd.read_csv("res/DM1.csv", header=None, prefix='V')
    # corr = df.corr()
    corr = df
    print(corr)
    f, ax = plt.subplots()
    ax.xaxis.tick_top()

    sns.heatmap(corr, cmap='OrRd', xticklabels=100, yticklabels=100, vmax=4, vmin=0, ax=ax).invert_yaxis()

    plt.show()


# 设置Axes的标题

# f.savefig("heatmap.jpg", dpi=1000, bbox_inches="tight")

show()
