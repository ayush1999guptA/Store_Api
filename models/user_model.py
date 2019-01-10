import sqlite3


class UserModel():

	def __init__(self,_id,username,password):
		self.id=_id
		self.username=username
		self.password=password
	@classmethod
	def search_by_name(cls,username):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='SELECT * FROM users WHERE username=?'
		result=cursor.execute(query,(username,))
		row=result.fetchone()
		if row!=None:
			user=cls(row[0],row[1],row[2])
			connection.close()
			return user
		else:
			connection.close()
			return None
	@classmethod		
	def search_by_id(cls,_id):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='SELECT * FROM users WHERE id=?'
		result=cursor.execute(query,(_id,))
		row=result.fetchone()
		if row!=None:
			user= cls(row[0],row[1],row[2])
			connection.close()
			return user
		else:
			connection.close()
			return None	
	@classmethod		
	def insert(cls,username, password):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='INSERT INTO users VALUES(NULL,?,?)'
		cursor.execute(query,(username,password))
		connection.commit()
		connection.close()

	@classmethod	
	def update(cls,username,password):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='UPDATE users SET password=? WHERE username=?'
		cursor.execute(query,(password,username))
		connection.commit()
		connection.close()

	@classmethod	
	def delete(cls,username):		
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='DELETE FROM users WHERE username=?'
		cursor.execute(query,(username,))
		connection.commit()
		connection.close()

