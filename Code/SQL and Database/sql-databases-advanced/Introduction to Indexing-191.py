## 1. Introduction ##

import sqlite3
conn = sqlite3.connect("factbook.db")
query = '''PRAGMA table_info(facts)'''
schema = conn.execute(query).fetchall()
for row in schema:
    print(row)
    

## 3. Explain query plan ##

q1 = '''EXPLAIN QUERY PLAN 
SELECT * FROM facts
WHERE area > 40000
'''
q2 = '''EXPLAIN QUERY PLAN
SELECT area FROM facts 
WHERE area > 40000
'''
q3 = '''EXPLAIN QUERY PLAN
SELECT area FROM facts
WHERE area == 'Czech Republic'
'''

query_plan_one = conn.execute(q1).fetchall()
query_plan_two = conn.execute(q2).fetchall()
query_plan_three = conn.execute(q3).fetchall()


print(query_plan_one)
print(query_plan_two)
print(query_plan_three)


## 5. Time complexity ##

q1 = '''EXPLAIN QUERY PLAN
SELECT * FROM facts
WHERE id = 20
'''
query_plan_four = conn.execute(q1).fetchall()
print(query_plan_four)

## 9. All together now ##

q1 = '''EXPLAIN QUERY PLAN
SELECT * FROM facts
WHERE population > 10000
'''

query_plan_six = conn.execute(q1).fetchall()
print(query_plan_six)

conn.execute('CREATE INDEX IF NOT EXISTS pop_idx ON facts(population)')

query_plan_seven = conn.execute(q1).fetchall()
print(query_plan_seven)