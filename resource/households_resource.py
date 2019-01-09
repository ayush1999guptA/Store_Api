from flask_restful import reqparse,Resource
from models.households_model import ItemModel
import sqlite3

class HouseHolds(Resource):


	def get(self,name):
		item=ItemModel.find_by_name(name)
		if item:
			return item.json()
		else :
			return {'message':'item is not present in the store'},404

	def post(self,name):
		item=ItemModel.find_by_name(name)
		if item ==None:
			parser=reqparse.RequestParser()
			parser.add_argument('price',
				type=float,
				required=True,
				help='this field cannot be left empty'
				)
			data=parser.parse_args()

			item=ItemModel(name,data['price'])
			item.insert()
			return item.json(),201
		else:
			return {'message':'this item already exists in the database.Try calling the put call'},400

	def put(self,name):
		item=ItemModel.find_by_name(name)
		if item !=None:
			parser=reqparse.RequestParser()
			parser.add_argument('price',
				type=float,
				required=True,
				help='this field cannot remain empty'
				)
			data=parser.parse_args()
			item.price=data['price']
			item.update()
			return item.json(),202
		else:
			parser=reqparse.RequestParser()
			parser.add_argument('price',
				type=float,
				requrired=True,
				help='this field cannot remain empty'
				)
			data=parser.parse_args()
			item=ItemModel(name,data['price'])
			item.insert()
			return item.json(),201

	def delete(self,name):
			item=ItemModel.find_by_name(name)
			if item!=None:
				connection=sqlite3.connect('data.db')
				cursor=connection.cursor()
				query='DELETE FROM household WHERE name=?'
				cursor.execute(query,(name,))
				connection.commit()
				connection.close()
				return{'message':'Item deleted successfully'},202
			else:
				return{'message':'Item does not exists'},404		

class HouseHold(Resource):
	def get(self):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='SELECT * FROM household'
		result=cursor.execute(query)
		items=[]
		for row in result:
			items.append({'name':row[1],'price':row[2]})
		connection.close()
		return {'items':items}	

			
										