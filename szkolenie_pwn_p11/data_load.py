import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from sklearn.feature_extraction import FeatureHasher

df = pd.read_csv('Adult_train.tab', sep='\t', skiprows=[1,2])

#print(df.head())
print(df.columns)

print(df.dtypes)
#print(df.count())
#print(df.isna().sum())

target = df['y']
print(target)

y_train = df['y']
x_train = df.drop(columns = ['y', 'education'])

df['native-country'].value_counts()

x_train_onehot = pd.get_dummies(x_train, prefix=['race','sex','workclass','marital-status','occupation','relationship','native-country'],
                         columns=['race','sex','workclass','marital-status','occupation','relationship','native-country'])


fh = FeatureHasher(n_features=8, input_type='string')
sp = fh.fit_transform(x_train['native-country'])
df1 = pd.DataFrame(sp.toarray(), columns=['country_f1',
                                          'country_f2',
                                          'country_f3',
                                          'country_f4',
                                          'country_f5',
                                          'country_f6',
                                          'country_f7',
                                          'country_f8'])
x_train_hashed = pd.concat([df1, x_train], axis=1).drop(columns=['native-country'])

print(x_train.shape)
print(x_train_hashed.columns)


from sklearn.model_selection import train_test_split
data_train, data_test, target_train, target_test = train_test_split(
    x_train_onehot, y_train, test_size=0.30, random_state=10)

import sklearn.naive_bayes
import sklearn.svm
import sklearn.metrics
import sklearn.neighbors

svc_model = sklearn.svm.LinearSVC(random_state=0, max_iter=1000)
pred_test = svc_model.fit(data_train, target_train).predict(data_test)
pred_train = svc_model.fit(data_train, target_train).predict(data_train)
print("Linear SVC accuracy: ", sklearn.metrics.accuracy_score(target_test, pred_test, normalize=True))
print(sklearn.metrics.classification_report(y_true=target_train, y_pred = pred_train))

knn_model = sklearn.neighbors.KNeighborsClassifier(n_neighbors=5, weights='distance')
pred = knn_model.fit(data_train, target_train).predict(data_test)

print("KNN Accuracy: ", sklearn.metrics.accuracy_score(target_test, pred, normalize=True))
print(sklearn.metrics.classification_report(y_true=target_test, y_pred=pred))


tuned_parameters = [{'kernel':['rbf'], 'gamma': [1e-3, 1e-4], 'C': [1, 10, 100, 1000]},
                    {'kernel':['linear'], 'C': [1, 10, 100, 1000]}]



from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
kfold = model_selection.KFold(n_splits=10, random_state=7)
cv_results = model_selection.cross_val_score(DecisionTreeClassifier(),data_train,target_train,cv=kfold,scoring='accuracy')
print(cv_results)
print("średnia z cv_results: ", cv_results.mean())



from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, KFold

rFClf_model = RandomForestClassifier(n_estimators=100)
pred_test = rFClf_model.fit(data_train,target_train).predict(data_test)
print("Random Fores clf accuracy_score: \n", sklearn.metrics.accuracy_score(target_test, pred_test, normalize=True))
print("Random Fores clf confusion_matrix: \n", sklearn.metrics.confusion_matrix(target_test, pred_test))
print("Random Fores clf classification_report: \n", sklearn.metrics.classification_report(target_test, pred_test))
print(rFClf_model.best_params_)
