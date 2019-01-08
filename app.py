from flask import Flask
from flask_restful import Api
from flask_jwt import jwt_required
from households_resource import HouseHolds,HouseHold
from electronic_resource import Electronics,Electronic

app=Flask(__name__)
api=Api(app)
api.secret_key='talk_to_my_hand'


api.add_resource(HouseHold,'/household')
api.add_resource(HouseHolds,'/household/<string:name>')
api.add_resource(Electronic,'/electronics')
api.add_resource(Electronics,'/electronics/<string:name>')

if __name__=='__main__':
	app.run(port=5000,debug=True)


