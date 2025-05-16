
import pandas as pd
import numpy as np
# Download latest version
path = 'online_retail.csv'
datas= pd.read_csv(path,encoding='windows-1252')

nomissing=datas.dropna()
print(nomissing)

nomissingcolumns=nomissing.dropna(axis=1)
print(nomissingcolumns)

fillefzeros=datas.fillna(0)
countmissing=datas.isna().sum()
print(fillefzeros)
print(countmissing)

meanunitprice=datas['UnitPrice'].mean()
dilledmean=datas['UnitPrice'].fillna(meanunitprice)
print(dilledmean)
print(meanunitprice)