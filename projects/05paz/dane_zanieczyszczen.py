import pandas as pd

#KpWloclOkrze-PM10-lg

data = pd.read_excel('~/Downloads/Wyniki pomiarów z 2018 roku/2018_PM10_1g.xlsx')
data = data[5:]
data = data.astype(int)
data = pd.DataFrame([x.replace(',','.') for x in data])
print(data.dtypes)