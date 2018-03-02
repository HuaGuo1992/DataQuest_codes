## 1. Recap ##

import pandas as pd
loans = pd.read_csv('cleaned_loans_2007.csv')
print(loans.info())

## 3. Picking an error metric ##

import pandas as pd
tn = len(loans[(loans['loan_status']==0) & (predictions==0)])
tp = len(loans[(loans['loan_status']==1) & (predictions==1)])
fn = len(loans[(loans['loan_status']==1) & (predictions==0)])
fp = len(loans[(loans['loan_status']==0) & (predictions==1)])

## 5. Class imbalance ##

import pandas as pd
import numpy

# Predict that all loans will be paid off on time.
predictions = pd.Series(numpy.ones(loans.shape[0]))

tn = len(loans[(loans['loan_status']==0) & (predictions==0)])
tp = len(loans[(loans['loan_status']==1) & (predictions==1)])
fn = len(loans[(loans['loan_status']==1) & (predictions==0)])
fp = len(loans[(loans['loan_status']==0) & (predictions==1)])

fpr = fp/(fp + tn)
tpr = tp/(tp + fn)
print(fpr)
print(tpr)

## 6. Logistic Regression ##

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
target = loans['loan_status']
features = loans.drop(['loan_status'], axis=1)
lr.fit(features, target)
predictions = lr.predict(features)


## 7. Cross Validation ##

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_predict, KFold
lr = LogisticRegression()
kf = KFold(features.shape[0], random_state=1)
predictions = cross_val_predict(lr, features, target, cv=kf)
predictions = pd.Series(predictions)

tn = len(loans[(loans['loan_status']==0) & (predictions==0)])
tp = len(loans[(loans['loan_status']==1) & (predictions==1)])
fn = len(loans[(loans['loan_status']==1) & (predictions==0)])
fp = len(loans[(loans['loan_status']==0) & (predictions==1)])

fpr = fp/(fp + tn)
tpr = tp/(tp + fn)
print(fpr)
print(tpr)

## 9. Penalizing the classifier ##

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_predict, KFold
lr = LogisticRegression(class_weight='balanced')
kf = KFold(features.shape[0], random_state=1)
predictions = cross_val_predict(lr, features, target, cv=kf)
predictions = pd.Series(predictions)
tn = len(loans[(loans['loan_status']==0) & (predictions==0)])
tp = len(loans[(loans['loan_status']==1) & (predictions==1)])
fn = len(loans[(loans['loan_status']==1) & (predictions==0)])
fp = len(loans[(loans['loan_status']==0) & (predictions==1)])

fpr = fp/(fp + tn)
tpr = tp/(tp + fn)
print(fpr)
print(tpr)




## 10. Manual penalties ##

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_predict, KFold

penalty = {
0:10, 1:1
}
lr = LogisticRegression(class_weight=penalty)
predictions = cross_val_predict(lr, features, target, cv=kf)
predictions = pd.Series(predictions)
tn = len(loans[(loans['loan_status']==0) & (predictions==0)])
tp = len(loans[(loans['loan_status']==1) & (predictions==1)])
fn = len(loans[(loans['loan_status']==1) & (predictions==0)])
fp = len(loans[(loans['loan_status']==0) & (predictions==1)])

fpr = fp/(fp + tn)
tpr = tp/(tp + fn)
print(fpr)
print(tpr)

## 11. Random forests ##

from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_predict, KFold
rf = RandomForestClassifier(random_state=1, class_weight='balanced')
kf = KFold(features.shape[0], random_state=1)
predictions = cross_val_predict(rf, features, target, cv=kf)
predictions = pd.Series(predictions)
tn = len(loans[(loans['loan_status']==0) & (predictions==0)])
tp = len(loans[(loans['loan_status']==1) & (predictions==1)])
fn = len(loans[(loans['loan_status']==1) & (predictions==0)])
fp = len(loans[(loans['loan_status']==0) & (predictions==1)])

fpr = fp/(fp + tn)
tpr = tp/(tp + fn)