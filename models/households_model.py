import sqlite3

class ItemModel():




	def __init__(self,name,price):
		self.name=name
		self.price=price


	def json(self):
		return {'name':self.name,'price':self.price}
	@classmethod	
	def find_by_name(cls,name):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='SELECT * FROM household WHERE name=?'
		result=cursor.execute(query,(name,))
		row=result.fetchone()
		connection.close()
		if row!=None:
			return cls(row[1],row[2])
		else:
			return None
	def insert(self):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='INSERT INTO household VALUES(Null,?,?)'
		cursor.execute(query,(self.name,self.price))
		connection.commit()
		connection.close()

	def update(self):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='UPDATE household SET price=?  WHERE name=?'
		cursor.execute(query,(self.price,self.name))
		connection.commit()
		connection.close()	


		
					


		
