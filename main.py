import pandas as pd
from datetime import date

class Dataset:
    def __init__(self):
        self.fileList = []
        self.getColumn = []
    #Cargar los archivos excel
    def loadExcel (self) : 
        i = 1
        while i < 8:
            loadList = 'data/dm2019-01-0'+str(i)+'.xls'
            self.fileList.append(loadList)
            i += 1
    #DataFrame
    def loadData (self) :
        i = 0
        while i < 7:
            #Cargar excel
            df = pd.read_excel(self.fileList[i])
            #Crear fecha
            d = df.iloc[1 , 0].split(",")[1].strip(' ').split(" ")
            d[1] = 1
            dFix = date(int(d[2]) , d[1] , int(d[0]))
            #Crear y cargar fecha en columna nueva
            df['Fecha'] = pd.to_datetime(dFix)
            i += 1
    def loadColumns (self) :    
        #Cargar nombre de columnas
        df = pd.read_excel(self.fileList[0])
        i = 0
        while i < df.shape[1]:
            selectColumn = df.iloc[3 , i]
            self.getColumn.append(selectColumn)
            i += 1

dt = Dataset()
dt.loadExcel()
dt.loadData()

    #df = pd.concat(map(pd.read_excel, data))
    #print(data)


    #print(df)

    #print(f'Filas: {df.shape[0]}, Columnas: {df.shape[1]}')

    #print(df.dtypes)
