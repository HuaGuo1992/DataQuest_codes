## 1. Recap ##

import pandas as pd
loans = pd.read_csv('filtered_loans_2007.csv')

null_counts = loans.isnull().sum()
print(null_counts)
print(len(loans))

## 2. Handling missing values ##

loans = loans.drop(['pub_rec_bankruptcies'], axis=1)
loans = loans.dropna()

print(loans.dtypes.value_counts())

## 3. Text columns ##

object_columns_df = loans.select_dtypes(include=['object'])

print(object_columns_df.iloc[0])

## 5. First 5 categorical columns ##

cols = ['home_ownership', 'verification_status', 'emp_length', 'term', 'addr_state']

for col in cols:
    print(col)
    print(loans[col].value_counts())

## 6. The reason for the loan ##

for col in ['purpose', 'title']:
    print(loans[col].value_counts())
    

## 7. Categorical columns ##

mapping_dict = {
    "emp_length": {
        "10+ years": 10,
        "9 years": 9,
        "8 years": 8,
        "7 years": 7,
        "6 years": 6,
        "5 years": 5,
        "4 years": 4,
        "3 years": 3,
        "2 years": 2,
        "1 year": 1,
        "< 1 year": 0,
        "n/a": 0
    }
}

loans = loans.drop(['last_credit_pull_d', 'addr_state', 'title', 'earliest_cr_line'], axis=1)

for col in ['int_rate', 'revol_util']:
    column = loans[col].str.rstrip('%')
    column = column.astype('float')
    loans[col] = column
    
loans = loans.replace(mapping_dict)



## 8. Dummy variables ##

cols = ['home_ownership', 'verification_status', 'purpose', 'term']

loans[col] = loans[col].astype('category')
dummy_df = pd.get_dummies(loans[cols])
loans = loans.drop(cols, axis=1)
loans = pd.concat([loans, dummy_df], axis=1)

