## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
avengers.head(5)

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()
true_avengers = avengers[avengers['Year'] > 1960]

## 5. Consolidating Deaths ##

def clean_death(row):
    number_death = 0
    columns = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
    
    for column in columns:
        value = row[column]
        if pd.isnull(value) or value == 'NO':
            continue
        elif value == 'YES':
            number_death += 1
    return number_death

true_avengers['Deaths'] = true_avengers.apply(clean_death, axis = 1)

## 6. Verifying Years Since Joining ##

joined_accuracy_count  = int()
correct_joined_years = true_avengers[true_avengers['Years since joining'] == (2015 - true_avengers['Year'])]
joined_accuracy_count = len(correct_joined_years)