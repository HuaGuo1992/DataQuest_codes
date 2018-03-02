## 2. Overview of the Data ##

import pandas as pd
submissions = pd.read_csv("sel_hn_stories.csv")
submissions.columns = ["submission_time", "upvotes", "url", "headline"]
submissions = submissions.dropna()
print(submissions.info())

## 3. Tokenizing the Headlines ##

tokenized_headlines = []
for headline in submissions['headline']:
    headline_list = headline.split(' ')
    tokenized_headlines.append(headline_list)

## 4. Preprocessing Tokens to Increase Accuracy ##

punctuation = [",", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]
clean_tokenized = []
for single_list in tokenized_headlines:
    new_list = []
    for item in single_list:
        new_item = ''.join(c.lower() for c in item if c not in punctuation)
        new_list.append(new_item)
    clean_tokenized.append(new_list)

## 5. Assembling a Matrix of Unique Words ##

import numpy as np
import pandas as pd
unique_tokens = []
single_tokens = []
for headline in clean_tokenized:
    for token in headline:
        if token not in single_tokens:
            single_tokens.append(token)
        else:
            unique_tokens.append(token)
            
            
counts  = pd.DataFrame(0, index=np.arange(len(clean_tokenized)), columns=unique_tokens)           

## 6. Counting Token Occurrences ##

# We've already loaded in clean_tokenized and counts
for idx, headline in enumerate(clean_tokenized):
    for token in headline:
        if token in unique_tokens:
            counts.loc[idx, [token]] += 1
    

## 7. Removing Columns to Increase Accuracy ##

# We've already loaded in clean_tokenized and counts
word_counts = counts.sum(axis=0)
found = (word_counts >= 5) & (word_counts <= 100)
counts = counts.iloc[:, found.get_values()]

## 8. Splitting the Data Into Train and Test Sets ##

from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(counts, submissions["upvotes"], test_size=0.2, random_state=1)

## 9. Making Predictions With fit() ##

from sklearn.linear_model import LinearRegression

clf = LinearRegression()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

## 10. Calculating Prediction Error ##

from sklearn.metrics import mean_squared_error


mse = mean_squared_error(y_test, predictions)
