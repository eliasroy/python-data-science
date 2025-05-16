
import pandas as pd
import numpy as np
# Download latest version
path = 'online_retail.csv'
datas= pd.read_csv(path,encoding='windows-1252')

columns=datas.columns
print(columns)
numrows, colums=datas.shape
print(numrows)
print (colums)

summary=datas.describe()
print(summary)