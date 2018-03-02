## 1. Introduction to the data ##

import pandas as pd
cars = pd.read_csv("auto.csv")

unique_regions = cars['origin'].unique()
print(unique_regions)

## 2. Dummy variables ##

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)
dummy_years = pd.get_dummies(cars['year'], prefix = 'year')
cars = pd.concat([cars, dummy_years], axis = 1)
cars = cars.drop(['cylinders', 'year'], axis = 1)
print(cars.head(5))

## 3. Multiclass classification ##

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]
train = shuffled_cars.iloc[0:274]
test = shuffled_cars.iloc[274: ]


## 4. Training a multiclass logistic regression model ##

from sklearn.linear_model import LogisticRegression

unique_origins = cars["origin"].unique()
unique_origins.sort()

models = {}

features = []
for col in cars.columns:
    if 'cyl' in col:
        features.append(col)
    elif 'year' in col:
        features.append(col)

def model(origin):
    X = train[features]
    y = train['origin'] == origin
    log_model = LogisticRegression()
    log_model.fit(X, y)
    return log_model

for origin in unique_origins:
     models[origin] = model(origin)
        
        

## 5. Testing the models ##

testing_probs = pd.DataFrame(columns=unique_origins)



for col in unique_origins:
   testing_probs[col] = models[col].predict_proba(test[features])[:, 1]

## 6. Choose the origin ##

predicted_origins = testing_probs.idxmax(axis = 1)
