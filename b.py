import pandas as pd
import datetime

dm2019 = pd.read_excel('data/dm2019-01-01.xls')
#df = pd.DataFrame(dm2019)
#s2 = df.copy()
#s2 = s2.drop(index=range(3))

#print(df)
#print(dm2019.loc[])
#datetime = []
#dm2019['Datetime'] = datetime
print(dm2019.iloc[1])