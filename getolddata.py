import glob
import os
import pandas as pd

# print(os.path.dirname(os.getcwd()))
inputfile = ".\data1\\*.csv"
outputfile = "res/alldata.csv"
csv_list = glob.glob(inputfile)

print(len(csv_list))

filepath = csv_list[0]
df = pd.read_csv(filepath, encoding="gbk", low_memory=False, names=['MMSI', 'TIME', 'LNG', 'LAT'])
df = df.to_csv(outputfile, encoding="gbk", index=False)
print(csv_list)
for i in range(0, len(csv_list)):
    filepath = csv_list[i]
    df = pd.read_csv(filepath, encoding="gbk", low_memory=False, names=['MMSI', 'TIME', 'LNG', 'LAT'])
    df = df.drop_duplicates(keep='first', inplace=False, subset=['LNG', 'LAT'])

    df = df.to_csv(outputfile, encoding="gbk", index=False, header=False, mode='a+')