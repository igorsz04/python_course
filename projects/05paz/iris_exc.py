import seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

iris = seaborn.load_dataset("iris")
print(iris.head())
#plt.scatter(iris.petal_length, iris.petal_width)
#plt.show()

print(iris.dtypes)
print(pd.Categorical(iris.iloc[:,4]))
print(pd.Categorical(iris.loc[:,'species']))

print("\ns:\n")
s = pd.Series(pd.Categorical(iris.loc[:,'species']))
print(s)

# colors = np.array(["#f442bf", "#6e41f4","#f4dc41"])[s.cat.codes]
# plt.scatter(iris.petal_length, iris.petal_width, c=colors)
# plt.show()


# przetrenować trzy modele z sales.py dla danych iris
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

le = preprocessing.LabelEncoder()
classes = le.fit_transform(s)
print(classes)

labels = classes
data = iris.drop(columns="species")
print(data)

data_train, data_test, target_train, target_test = train_test_split(
    data, target, test_size=0.20, random_state=10)

gnb = GaussianNB()
pred = gnb.fit(data_train, target_train).predict(data_test)
print("Naive-Bayes accuracy : ", accuracy_score(target_test, pred, normalize=True))
