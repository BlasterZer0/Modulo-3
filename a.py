import pandas as pd
from datetime import date

i = 1
fileList = []
while i < 8:
    loadList = 'data/dm2019-01-0'+str(i)+'.xls'
    fileList.append(loadList)
    i += 1

df = pd.read_excel(fileList[0])

c = 0
getColumn = []
while c < df.shape[1]:
    selectColumn = df.iloc[3 , c]
    getColumn.append(selectColumn)
    c += 1

d = df.iloc[1 , 0].split(",")[1].strip(' ').split(" ")
d[1] = 1
dFix = date(int(d[2]) , d[1] , int(d[0]))
df['Fecha'] = pd.to_datetime(dFix)

print(getColumn)

#df = pd.concat(map(pd.read_excel, data))
#print(data)


#print(df)

print(f'Filas: {df.shape[0]}, Columnas: {df.shape[1]}')

#print(df.dtypes)
