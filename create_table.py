import sqlite3

connection=sqlite3.connect('data.db')
cursor=connection.cursor()

create_households='CREATE TABLE IF NOT EXISTS household(id INTEGER PRIMARY KEY,name text, price int)'
cursor.execute(create_households)

create_electronics='CREATE TABLE IF NOT EXISTS electronics(id INTEGER PRIMARY KEY,name text,price int)'
cursor.execute(create_electronics)

create_dairy='CREATE TABLE IF NOT EXISTS dairy(id INTEGER PRIMARY KEY,name text,price int)'
cursor.execute(create_dairy)

create_groceries='CREATE TABLE IF NOT EXISTS groceries(id INTEGER PRIMARY KEY,name text,price int)'
cursor.execute(create_groceries)



connection.commit()

connection.close()
