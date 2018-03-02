## 2. Array Comparisons ##

countries_canada = world_alcohol[:, 2] == 'Canada'
years_1984 = world_alcohol[:, 0] == '1984'



## 3. Selecting Elements ##

country_is_algeria = world_alcohol[:, 2] == 'Algeria'
country_algeria = world_alcohol[country_is_algeria, :]

## 4. Comparisons with Multiple Conditions ##

is_algeria_and_1986 = (world_alcohol[:, 0] == '1986') & (world_alcohol[:, 2] == 'Algeria')
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986, :]

## 5. Replacing Values ##

world_alcohol[(world_alcohol[:, 0] == '1986'), 0] = '2014'
world_alcohol[(world_alcohol[:, 3] == 'Wine'), 3] = 'Grog'

## 6. Replacing Empty Strings ##

is_value_empty = world_alcohol[:, 4] == ''
world_alcohol[is_value_empty, 4] = '0'

## 7. Converting Data Types ##

alcohol_consumption = world_alcohol[:, 4].astype(float)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

is_canada_1986 = (world_alcohol[:,2] == "Canada") & (world_alcohol[:,0] == '1986')
canada_1986 = world_alcohol[is_canada_1986,:]
canada_alcohol = canada_1986[:,4]
empty_strings = canada_alcohol == ''
canada_alcohol[empty_strings] = "0"
canada_alcohol = canada_alcohol.astype(float)
total_canadian_drinking = canada_alcohol.sum()

## 10. Calculating Consumption for Each Country ##

totals = {}
data_1989 = world_alcohol[world_alcohol[:, 0] == '1989']
for country in countries:
    data_1989_country = data_1989[data_1989[:, 2] == country]
    alcohol = data_1989_country[:, 4]
    is_empty_value = alcohol == ''
    alcohol[is_empty_value] = 0 
    alcohol = alcohol.astype(float)
    totals[country] = alcohol.sum()

    
    

## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None
for key, value in totals.items():
    if value > highest_value:
        highest_value = value
        highest_key = key
        