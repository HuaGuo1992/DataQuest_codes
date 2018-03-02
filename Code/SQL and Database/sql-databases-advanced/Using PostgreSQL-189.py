## 3. Psycopg2 ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
print(cur)
conn.close()

## 4. Creating a table ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
query = '''
CREATE TABLE notes(
id integer PRIMARY KEY,
body text,
tittle text)
'''
cur.execute(query)
conn.close()

## 5. SQL Transactions ##

import psycopg2
conn = psycopg2.connect('dbname=dq user=dq')
cur = conn.cursor()
query = '''
CREATE TABLE notes(
id integer PRIMARY KEY,
body text,
tittle text)
'''
cur.execute(query)
conn.commit()
conn.close()




## 6. Autocommitting ##

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
query = '''
CREATE TABLE facts(
id integer PRIMARY KEY,
country text,
value integer)
'''
cur.execute(query)
conn.commit()
conn.close()

## 7. Executing queries ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("INSERT INTO notes VALUES (1, 'Do more missions on Dataquest.', 'Dataquest reminder');")
cur.execute("SELECT * from notes;")
rows = cur.fetchall()
print(rows)
conn.close()

## 8. Creating a database ##

conn = psycopg2.connect('dbname=dq user=dq')
conn.autocommit = True
cur = conn.cursor()
query = 'CREATE DATABASE income OWNER dq'
cur.execute(query)
conn.close()

## 9. Deleting a database ##

conn = psycopg2.connect('dbname=dq user=dq')
conn.autocommit = True
cur = conn.cursor()
cur.execute('DROP DATABASE income')
conn.close()