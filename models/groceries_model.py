import sqlite3

class GroceryModel():



	def __init__(self,name,price,discount,dprice):
		self.name=name
		self.price=price
		self.discount=discount
		self.dprice=dprice


	def json(self):
		return {'name':self.name,'price':self.price,'discount%':self.discount,'discounted price':self.dprice}
	
	@classmethod	
	def find_by_name(cls,name):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='SELECT * FROM groceries WHERE name=?'
		result=cursor.execute(query,(name,))
		row=result.fetchone()
		connection.close()
		if row!=None:
			return cls(row[1],row[2],row[3],row[4])
		else:
			return None
	def insert(self):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='INSERT INTO groceries VALUES(Null,?,?,?,?)'
		cursor.execute(query,(self.name,self.price,self.discount,self.dprice))
		connection.commit()
		connection.close()

	def update(self):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='UPDATE groceries SET price=?  WHERE name=?'
		cursor.execute(query,(self.price,self.name))
		cursor.execute(query,(self.price,self.name))
		query='UPDATE groceries SET dprice=?  WHERE name=?'
		c=self.price-(self.price*self.discount/100)
		self.dprice=c
		cursor.execute(query,(self.dprice,self.name))
		connection.commit()
		connection.close()	


		
					


		
