## 1. Introduction ##

strings = ["data science", "big data", "metadata"]
regex = "data"

## 2. Wildcards in Regular Expressions ##

strings = ["bat", "robotics", "megabyte"]
regex = "b.t"

## 3. Searching the Beginnings And Endings Of Strings ##

strings = ["better not put too much", "butter in the", "batter"]
bad_string = "We also wouldn't want it to be bitter"
regex = "^b.tter"

## 5. Reading and Printing the Data Set ##

import csv

f = open('askreddit_2015.csv')
posts_with_header = list(csv.reader(f))
posts = posts_with_header[1:]


for i in range(10):
    print(posts[i])

## 6. Counting Simple Matches in the Data Set with re() ##

import re

of_reddit_count = 0
for row in posts:
    q = row[0]
    if re.search('of Reddit', row[0]) is not None:
        of_reddit_count += 1
        
        
        
print(of_reddit_count)
  

## 7. Using Square Brackets to Match Multiple Characters ##

import re

of_reddit_count = 0
for row in posts:
    q = row[0]
    if re.search('of [Rr]eddit', row[0]) is not None:
        of_reddit_count += 1
        
        
        
print(of_reddit_count)
  

## 8. Escaping Special Characters ##

import re

serious_count = 0

for row in posts:
    q = row[0]
    if re.search('\[Serious\]', q) is not None:
        serious_count += 1
        

## 9. Combining Escaped Characters and Multiple Matches ##

import re

serious_count = 0
for row in posts:
    if re.search("\[[Ss]erious\]", row[0]) is not None:
        serious_count += 1

## 10. Adding More Complexity to Your Regular Expression ##

import re

serious_count = 0
for row in posts:
    if re.search("[\[\(][Ss]erious[\)\]]", row[0]) is not None:
        serious_count += 1

## 11. Combining Multiple Regular Expressions ##

import re

serious_start_count = 0
serious_end_count = 0
serious_count_final = 0
start_re = '^[\[\(][sS]erious[\)\]]'
end_re = '[\[\(][sS]erious[\)\]]$'
final_re = '^[\[\(][sS]erious[\)\]]|[\[\(][sS]erious[\)\]]$'

def count_func(re_str):
    count = 0
    for row in posts:
        q = row[0]
        if re.search(re_str, q) is not None:
            count += 1
    return count

serious_start_count = count_func(start_re)
serious_end_count = count_func(end_re)
serious_count_final = count_func(final_re)
      

## 12. Using Regular Expressions to Substitute Strings ##

import re
for row in posts:
    row[0] = re.sub('[\[\(][sS]erious[\)\]]', '[Serious]', row[0])

## 13. Matching Years with Regular Expressions ##

import re

year_strings = []
for item in strings:
    if re.search('[1-2][0-9][0-9][0-9]', item):
        year_strings.append(item)

## 14. Repeating Characters in Regular Expressions ##

import re

year_strings = []
for item in strings:
    if re.search('[1-2][0-9]{3}', item) is not None:
        year_strings.append(item)

## 15. Challenge: Extracting all Years ##

import re

years = []

years = re.findall('[1-2][0-9]{3}', years_string)
    
    
    