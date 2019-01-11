import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required

class GroceryDiscount(Resource):
	
	@jwt_required()
	def post(self):
		parser=reqparse.RequestParser()
		parser.add_argument('discount',
			type=int,
			required=True,
			help='this field cannot remain empty')
		data=parser.parse_args()
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='SELECT * FROM groceries'
		result=cursor.execute(query)
		for row in result:
			query1='UPDATE groceries SET discount=? WHERE name=?'
			query2='UPDATE groceries SET dprice=? WHERE name=?'
			c=row[2]-(row[2]*data['discount']/100)
			cursor.execute(query1,(data['discount'],row[1]))
			cursor.execute(query2,(c,row[1]))
		connection.commit()
		connection.close()

		return{'message':'discount successfully inserted '}	,202
		
	@jwt_required()
	def put(self):
		parser=reqparse.RequestParser()
		parser.add_argument('discount',
			type=int,
			required=True,
			help='this field cannot remain empty')
		data=parser.parse_args()
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='SELECT * FROM groceries'
		result=cursor.execute(query)
		for row in result:
			query1='UPDATE groceries SET discount=? WHERE name=?'
			query2='UPDATE groceries SET dprice=? WHERE name=?'
			c=row[2]-(row[2]*data['discount']/100)
			cursor.execute(query1,(data['discount'],row[1]))
			cursor.execute(query2,(c,row[1]))
		connection.commit()
		connection.close()

		return{'message':'discount successfully changed '}	,202

	@jwt_required()
	def delete(self):
		data=0
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='SELECT * FROM groceries'
		result=cursor.execute(query)
		for row in result:
			query1='UPDATE groceries SET discount=? WHERE name=?'
			query2='UPDATE groceries SET dprice=? WHERE name=?'
			c=row[2]-(row[2]*data/100)
			cursor.execute(query1,(data,row[1]))
			cursor.execute(query2,(c,row[1]))
		connection.commit()
		connection.close()

		return{'message':'discount deleted successfully '}	,202


