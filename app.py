from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resource.households_resource import HouseHolds,HouseHold
from resource.electronic_resource import Electronics,Electronic
from resource.dairy_resource import Dairys,Dairy
from resource.groceries_resource import Groceries,Grocery
from resource.user_resource import Userregistry,Users
from security import authenticate,identity
from discounts.dairy_discount import DairyDiscount
from discounts.household_discount import HouseHoldDiscount
from discounts.groceries_discount import GroceryDiscount
from discounts.electronics_discount import ElectronicsDiscount


app=Flask(__name__)
api=Api(app)
app.secret_key='talk_to_my_hand'
jwt=JWT(app,authenticate,identity)


api.add_resource(HouseHold,'/household')
api.add_resource(HouseHolds,'/household/<string:name>')
api.add_resource(Electronic,'/electronics')
api.add_resource(Electronics,'/electronics/<string:name>')
api.add_resource(Dairy,'/dairy')
api.add_resource(Dairys,'/dairy/<string:name>')
api.add_resource(Grocery,'/grocery')
api.add_resource(Groceries,'/grocery/<string:name>')
api.add_resource(Userregistry,'/userregistry')
api.add_resource(Users,'/users')
api.add_resource(DairyDiscount,'/discount/dairy')
api.add_resource(HouseHoldDiscount,'/discount/household')
api.add_resource(GroceryDiscount,'/discount/grocery')
api.add_resource(ElectronicsDiscount,'/discount/electronics')


if __name__=='__main__':
	app.run(port=5000,debug=True)


