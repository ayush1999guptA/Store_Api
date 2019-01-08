import sqlite3

connection=sqlite3.connect('data.db')
cursor=connection.cursor()

create_households='CREATE TABLE IF NOT EXISTS household(id INTEGER PRIMARY KEY,name text, price int)'


cursor.execute(create_households)


connection.commit()

connection.close()
