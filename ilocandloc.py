
import pandas as pd
import numpy as np
# Download latest version
path = 'online_retail.csv'
datas= pd.read_csv(path,encoding='windows-1252')
"""
row=datas.iloc[0]
print(row)

fiverows=datas.iloc[:5]
print(fiverows)

# Select specific 3 primeras filas y 2 columns 
subset=datas.iloc[:3, :2]
print(subset)

#selec una sola columna y una fila
row=datas.iloc[1, 4]
print(row)
"""

#  usando loc
row=datas.loc[3]
print(row)

fiverows=datas.loc[:5]
print(fiverows)

cantidadcolumnas=datas.loc[:, 'Quantity']
print(cantidadcolumnas)


pricesuniyarios=datas.loc[:, ['Quantity', 'UnitPrice']]
print(pricesuniyarios)