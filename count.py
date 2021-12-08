import pandas as pd
from collections import Counter

data = pd.read_csv('./res/5.csv', names=['lon', 'lat', 'label'])
# print(data)
# print(data['label'].value_counts())

# count = data['label'].value_counts()

count = data.groupby(by=['label'])
count = count.size()
count = count.reset_index(name='count')
print(count)
count.to_csv('./res/count.csv', index=False)
