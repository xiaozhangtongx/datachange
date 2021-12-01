import pandas as pd

df = pd.read_csv('res/alldata.csv')
df.columns = ['TIME', 'MMSI', 'LNG', 'LAT']
c = list(df.columns)
# grouped = df.groupby(c[0:1])
#  删除date列中的重复项
date_cate = df.drop_duplicates(subset=['LNG', 'LAT'])
date_cate = date_cate.sort_values(by="TIME", ascending=True)
print(date_cate.MMSI)
print(range(len(date_cate)))  # date中的所有类，也就是文件数
for name in date_cate.MMSI:
    # print(name)
    # 当date为某一个类时，存入一个小的csv文件中，文件名为类名
    df[df.MMSI == name].to_csv("res\\new\\" + u"%s" % name + ".csv", float_format='%f', header=0, index=0)
