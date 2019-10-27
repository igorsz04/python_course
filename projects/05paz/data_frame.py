import pandas as pd
import numpy as np

df = pd.DataFrame({
    'one': pd.Series(np.random.randn(3), index=['a','b','c']),
    'two': pd.Series(np.random.randn(4), index=['a','b','c','d']),
    'three': pd.Series(np.random.randn(3), index=['b','c','d'])
})

print('tabela df:',df)

print('df.mean()\n',df.mean())

print("df.corr()\n",df.corr())

print('df.count()\n',df.count())

print('df.max()\n',df.max())

print('df.min\n',df.min)

print('df.median\n',df.median)

print('df.std\n',df.std)

print('df.tail(3)\n',df.tail(3))

print('df.head(5)\n',df.head(5))

print('df.sort_values(col1)a\n',df.sort_values('one'))
print('df.sort_values(col1)b\n',df.sort_values('one',ascending=False))
print('df.sort_values(col1)c\n',df.sort_values(['one','two'],ascending=False))
print('df.groupby(one)\n',df.groupby('one'))

print('df.dropna\n',df.dropna())
print('df.fillna\n',df.fillna('one'))
print('df.fillna(s.mean())\n',df.fillna(df.mean()))

df2 = pd.DataFrame({
    'one': pd.Series(np.random.randn(3), index=['a','b','c']),
    'two': pd.Series(np.random.randn(4), index=['a','b','c','d']),
    'three': pd.Series(np.random.randn(3), index=['b','c','d'])
})

df1 = pd.DataFrame({
    'one': pd.Series(np.random.randn(3), index=['a','b','c']),
    'two': pd.Series(np.random.randn(4), index=['a','b','c','d']),
    'three': pd.Series(np.random.randn(3), index=['b','c','d'])
})


print('df1.append(df2)\n',df.append(df2))
#print('df.concat[df1, df2],axis=1\n',df.concat([df1, df2],axis=1))