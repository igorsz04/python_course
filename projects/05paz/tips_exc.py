import seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

tips = seaborn.load_dataset("tips")
print(tips.head())

tips_ratio = round((tips['tip']/tips['total_bill'])*100)
tips_ratio = tips_ratio.astype(int)
tips['tips_ratio'] = tips_ratio
print("\ntips ratio:\n",tips_ratio)
print(tips)

plt.figure(0)
tips.hist(column="tips_ratio",bins=20)
plt.figure(1)
tips.hist(column="tips_ratio",by="sex",bins=20)
plt.show()

#pokazac wysokosc srednia tipa w zaleznosci od time na wykresie slupkowym
s = pd.Series(pd.Categorical(tips.loc[:,"time"]))
print(s)
tip_time_values = tips.groupby('time').mean()
tip_time_values.plot(kind='bar')
plt.show()