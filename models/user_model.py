import sqlite3


class UserModel():

	def __init__(self,username,password):
		self.username=username
		self.password=password
	@classmethod
	def search_by_name(cls,name):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='SELECT * FROM users WHERE username=?'
		result=cursor.execute(query,(name,))
		row=result.fetchone()
		connection.close()
		if row!=None:
			return cls(row[1],row[2])
		else:
			return None
	@classmethod		
	def search_by_id(cls,_id):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='SELECT * FROM users WHERE id=?'
		result=cursor.execute(query,(_id,))
		row=result.fetchone()
		connection.close()
		if row!=None:
			return cls(row[1],row[2])
		else:
			return None	

	def insert(self):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='INSERT INTO users VALUES(NULL,?,?)'
		cursor.execute(query,(self.username,self.password))
		connection.commit()
		connection.close()

	def update(self):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='UPDATE users SET password=? WHERE username=?'
		cursor.execute(query,(self.password,self.username))
		connection.commit()
		connection.close()

	def delete(self):		
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='DELETE FROM users WHERE username=?'
		cursor.execute(query,(self.username,))
		connection.commit()
		connection.close()

