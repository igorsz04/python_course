# importing Pandas library
import pandas as pd

df = pd.read_csv('~/Downloads/pokemon.csv')
print(df)

print('df1')
df1 = df.groupby('Type').count()
print(df1)