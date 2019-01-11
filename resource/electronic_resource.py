from flask_restful import reqparse,Resource
from flask_jwt import jwt_required
from models.electronics_model import ElectronicsModel
import sqlite3

class Electronics(Resource):


	def get(self,name):
		item=ElectronicsModel.find_by_name(name)
		if item:
			return item.json()
		else :
			return {'message':'item is not present in the store'},404

	@jwt_required()		
	def post(self,name):
		item=ElectronicsModel.find_by_name(name)
		if item ==None:
			parser=reqparse.RequestParser()
			parser.add_argument('price',
				type=float,
				required=True,
				help='this field cannot be left empty'
				)
			data=parser.parse_args()

			item=ElectronicsModel(name,data['price'],0,data['price'])
			item.insert()
			return item.json(),201
		else:
			return {'message':'this item already exists in the database.Try calling the put call'},400

	@jwt_required()		
	def put(self,name):
		item=ElectronicsModel.find_by_name(name)
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
			item=ElectronicsModel(name,data['price'],0,data['price'])
			item.insert()
			return item.json(),201

	@jwt_required()		
	def delete(self,name):
			item=ElectronicsModel.find_by_name(name)
			if item!=None:
				connection=sqlite3.connect('data.db')
				cursor=connection.cursor()
				query='DELETE FROM electronics WHERE name=?'
				cursor.execute(query,(name,))
				connection.commit()
				connection.close()
				return{'message':'Item deleted successfully'},202
			else:
				return{'message':'Item does not exists'},404		

class Electronic(Resource):
	def get(self):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='SELECT * FROM electronics'
		result=cursor.execute(query)
		items=[]
		for row in result:
			items.append({'name':row[1],'price':row[2],'discount%':row[3],'discounted price':row[4]})
		connection.close()
		return {'items':items}	

			
										