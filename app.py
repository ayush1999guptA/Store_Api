from flask import Flask
from flask_restful import Api
from flask_jwt import jwt_required
from resource.households_resource import HouseHolds,HouseHold
from resource.electronic_resource import Electronics,Electronic
from resource.dairy_resource import Dairys,Dairy
from resource.groceries_resource import Groceries,Grocery

app=Flask(__name__)
api=Api(app)
api.secret_key='talk_to_my_hand'


api.add_resource(HouseHold,'/household')
api.add_resource(HouseHolds,'/household/<string:name>')
api.add_resource(Electronic,'/electronics')
api.add_resource(Electronics,'/electronics/<string:name>')
api.add_resource(Dairy,'/dairy')
api.add_resource(Dairys,'/dairy/<string:name>')
api.add_resource(Grocery,'/grocery')
api.add_resource(Groceries,'/grocery/<string:name>')

if __name__=='__main__':
	app.run(port=5000,debug=True)


