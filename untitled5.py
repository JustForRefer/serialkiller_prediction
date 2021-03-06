# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1datKipMcR0gpHHMFLNPYS6gEqCUMHT4F
"""

import numpy as np
import pandas as pd
import seaborn as sns

from google.colab import drive
drive.mount("/content/drive")

data = pd.read_csv("/content/drive/MyDrive/Serial_KillerML/serial_killer_dataset.csv")

data.head()

data = data.loc[538452:638454]

data.head()

data.shape

data[data.columns].isnull().sum()

n = data.nunique(axis=0)

n

data = data.copy()
dummies = pd.get_dummies(data['Crime Type'], prefix="Crime")
data = pd.concat([data, dummies], axis=1)
data = data.drop('Crime Type',axis=1)

data = data.copy()
dummies = pd.get_dummies(data['Victim Race'], prefix="Victim_Race")
data = pd.concat([data, dummies], axis=1)
data = data.drop('Victim Race',axis=1)

data = data.copy()
dummies = pd.get_dummies(data['Victim Ethnicity'], prefix="Victim_Ethnicity")
data = pd.concat([data, dummies], axis=1)
data = data.drop('Victim Ethnicity',axis=1)

data = data.copy()
dummies = pd.get_dummies(data['Perpetrator Sex'], prefix="Perpetrator_Sex")
data = pd.concat([data, dummies], axis=1)
data = data.drop('Perpetrator Sex',axis=1)

data = data.copy()
dummies = pd.get_dummies(data['Perpetrator Ethnicity'], prefix="Perpetrator_Ethnicity")
data = pd.concat([data, dummies], axis=1)
data = data.drop('Perpetrator Ethnicity',axis=1)

data = data.copy()
dummies = pd.get_dummies(data['Record Source'], prefix="Record_Source")
data = pd.concat([data, dummies], axis=1)
data = data.drop('Record Source',axis=1)

data = data.copy()
dummies = pd.get_dummies(data['Victim Sex'], prefix="Victim_Sex")
data = pd.concat([data, dummies], axis=1)
data = data.drop('Victim Sex',axis=1)

dummies = pd.get_dummies(data['Perpetrator Race'], prefix="Perpetrator_Race")
data = pd.concat([data, dummies], axis=1)
data = data.drop('Perpetrator Race', axis=1)
data = data.copy()

dummies = pd.get_dummies(data['Agency Type'], prefix="Agency_Type")
data = pd.concat([data, dummies], axis=1)
data = data.drop('Agency Type', axis=1)
data = data.copy()

data.head()

data = data.drop(['Year','Record ID','Perpetrator Age'],axis=1)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data['Agency Code'] = le.fit_transform(data['Agency Code'])
data['Agency Name'] = le.fit_transform(data['Agency Name'])
data['City'] = le.fit_transform(data['City'])
data['State'] = le.fit_transform(data['State'])
data['Relationship'] = le.fit_transform(data['Relationship'])
data['Month'] = le.fit_transform(data['Month'])
data['Crime Solved'] = le.fit_transform(data['Crime Solved'])
data['Weapon'] = le.fit_transform(data['Weapon'])

n

data

data[:20].dtypes

X = data.drop(['Crime Solved'],axis=1)
Y = data['Crime Solved']

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.linear_model import LogisticRegression
lm = LogisticRegression()

lm.fit(X_train,Y_train)

predictions = lm.predict(X_test)
from sklearn import metrics
y_pred = lm.predict(X_test)
print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Y_test, y_pred)))

print(y_pred)

lm.score(X_test,Y_test)#final accuracy

from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics 
clf = DecisionTreeClassifier()
clf = clf.fit(X_train,Y_train)
y_pred = clf.predict(X_test)

print("Accuracy:",metrics.accuracy_score(Y_test, y_pred))
print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Y_test, y_pred)))

print(y_pred)

from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(X_train,Y_train)

y_predict = model.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(Y_test,y_predict)
print(accuracy)
print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Y_test, y_pred)))

print(y_pred)

from sklearn.ensemble import RandomForestClassifier 
clf = RandomForestClassifier(n_estimators = 100)   

clf.fit(X_train, Y_train) 
 
y_pred = clf.predict(X_test) 

from sklearn import metrics 
accuracy_s =  metrics.accuracy_score(Y_test, y_pred)
print(accuracy_s)

print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Y_test, y_pred)))

print(y_pred)

from sklearn.svm import SVC
model = SVC(kernel='rbf',random_state=42)
model.fit(X_train,Y_train)

confirm = model.predict(X_test)
model.score(X_test,Y_test)

from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, confirm))
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, confirm))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Y_test, confirm)))

from sklearn.svm import SVC
model = SVC(kernel='linear',random_state=42)
model.fit(X_train,Y_train)

confirm = model.predict(X_test)
model.score(X_test,Y_test)

from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, confirm))
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, confirm))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Y_test, confirm)))

print(y_pred)