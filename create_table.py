import sqlite3

connection=sqlite3.connect('data.db')
cursor=connection.cursor()

create_households='CREATE TABLE IF NOT EXISTS household(id INTEGER PRIMARY KEY,name text, price int,discount int,dprice int)'
cursor.execute(create_households)

create_electronics='CREATE TABLE IF NOT EXISTS electronics(id INTEGER PRIMARY KEY,name text,price int,discount int,dprice int)'
cursor.execute(create_electronics)

create_dairy='CREATE TABLE IF NOT EXISTS dairy(id INTEGER PRIMARY KEY,name text,price int,discount int,dprice int)'
cursor.execute(create_dairy)

create_groceries='CREATE TABLE IF NOT EXISTS groceries(id INTEGER PRIMARY KEY,name text,price int,discount int,dprice int)'
cursor.execute(create_groceries)

create_users='CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,username text,password text)'
cursor.execute(create_users)

query='INSERT INTO users VALUES(NULL,?,?)'
cursor.execute(query,('admin','therock'))

connection.commit()

connection.close()
