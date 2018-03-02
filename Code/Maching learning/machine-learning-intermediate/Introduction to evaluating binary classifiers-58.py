## 1. Introduction to the Data ##

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

admissions = pd.read_csv("admissions.csv")
model = LogisticRegression()
model.fit(admissions[["gpa"]], admissions["admit"])
admissions['predicted_label'] = model.predict(admissions[['gpa']])

print(admissions['predicted_label'].value_counts())
print(admissions.head(5))

## 2. Accuracy ##

admissions['actual_label'] = admissions['admit']
admissions = admissions.drop(['admit'], axis = 1)
matches = admissions['actual_label'] == admissions['predicted_label']
correct_predictions = admissions[matches]

print(correct_predictions.head(5))
accuracy = len(correct_predictions)/len(admissions)
print(accuracy)


## 4. Binary classification outcomes ##

true_positives = ((admissions['predicted_label'] == 1) & (admissions['actual_label'] == 1)).sum()
true_negatives = ((admissions['predicted_label'] == 0) & (admissions['actual_label'] == 0)).sum()


## 5. Sensitivity ##

# From the previous screen
true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])

false_negatives_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 1)
false_negatives = len(admissions[false_negatives_filter])

sensitivity = true_positives / (true_positives + false_negatives)



## 6. Specificity ##

# From previous screens
true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])
false_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 1)
false_negatives = len(admissions[false_negative_filter])
true_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 0)
true_negatives = len(admissions[true_negative_filter])
false_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 0)
false_positives = len(admissions[false_positive_filter])
specificity = (true_negatives) / (false_positives + true_negatives)
print(specificity)