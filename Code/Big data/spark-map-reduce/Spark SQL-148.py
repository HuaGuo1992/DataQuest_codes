## 2. Register the DataFrame as a Table ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")

df.registerTempTable('census2010')
tables = sqlCtx.tableNames()
print(tables)

## 3. Querying ##

query = "SELECT age FROM census2010"
sqlCtx.sql(query).show(20)

## 4. Filtering ##

query = 'SELECT males, females FROM census2010 WHERE age > 5 AND age < 15'
sqlCtx.sql(query).show(20)

## 5. Mixing Functionality ##

q = 'SELECT males, females FROM census2010'
sqlCtx.sql(q).describe().show()

## 6. Multiple tables ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.registerTempTable('census2010')
df = sqlCtx.read.json('census_1980.json')
df.registerTempTable('census1980')
df = sqlCtx.read.json('census_1990.json')
df.registerTempTable('census1990')
df = sqlCtx.read.json('census_2000.json')
df.registerTempTable('census2000')

tables = sqlCtx.tableNames()
print(tables)

## 7. Joins ##

q = '''SELECT census2010.total, census2000.total FROM census2010 INNER JOIN census2000 ON census2010.age = census2000.age'''
sqlCtx.sql(q).show(20)

## 8. SQL Functions ##

q = '''SELECT SUM(census2010.total), SUM(census2000.total), SUM(census1990.total) FROM census2010 INNER JOIN census2000 ON census2010.age = census2000.age INNER JOIN census1990 ON census2010.age = census1990.age'''

sqlCtx.sql(q).show()