## 1. The Time Module ##

import time

current_time = time.time()

print(current_time)
current = current_time / 60/ 60/ 24/365

## 2. Converting Timestamps ##

import time

current_time = time.time()
current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour

## 3. UTC ##

from datetime import datetime

current_time = datetime.utcnow()
current_year = current_time.year
current_month = current_time.month

## 4. Timedelta ##

import datetime

kirks_birthday = datetime.datetime(year = 2233,month=3, day = 22)

diff = datetime.timedelta(weeks = 15)

before_kirk = kirks_birthday - diff


## 5. Formatting Dates ##

import datetime

mystery_date_formatted_string = mystery_date.strftime("%I:%M%p on %A %B %d, %Y")
print(mystery_date_formatted_string)

## 6. Parsing Dates ##

import datetime

mystery_date_2 = datetime.datetime.strptime(mystery_date_formatted_string, "%I:%M%p on %A %B %d, %Y")

print(mystery_date_2)

## 8. Reformatting Our Data ##

import datetime


for row in posts:
    time = row[2]
    time = datetime.datetime.fromtimestamp(float(time))
    row[2] = time
    

## 9. Counting Posts from March ##

march_count = 0


for row in posts:
    time = row[2]
    if time.month == 3:
        march_count += 1
        

## 10. Counting Posts from Any Month ##



def count_month(month):
    count = 0
    for row in posts:
        if row[2].month == month:
            count += 1
    return count
            
            
feb_count = count_month(2)
aug_count = count_month(8)