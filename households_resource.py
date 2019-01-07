from flask_restful import reqparse,Resourse
from households_model import ItemModel
import sqlite3

class HouseHolds(Resource):


	def get(self,name):
		item=ItemModel.find_by_name(name)
		if item:
			return item.json()
		else 
			return {'message':'item is not present in the store'}

	def post(self,name):
		item=ItemModel.find_by_name(name)
		if item ==None:
			parser=reqparse.RequestParser()
			parser.add_argument('price'
				type=int,
				required=True,
				help='this field cannot be left empty'
				)
			data=parser.parse_args()

			item=ItemModel(name,data['price'])
			item.insert()
			return item.json(),201
		else:
			return {'message':'this item already exists in the database.Try calling the put call'}

	def put(self,name):
		item=ItemModel.find_by_name(name)
		if item !=None:
			parser=reqparse.RequestParser()
			parser.add_argument('price',
				type=int,
				requrired=True,
				help='this field cannot remain empty'
				)
			data=parser.parse_args()
			item.price=date['price']
			item.update()
			return item.json(),202
		else:
			parser=reqparse.RequestParser()
			parser.add_argument('price',
				type=int,
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
				return{'message':'Item deleted successfully'}
			else:
				return{'message':'Item does not exists'}		


			
										