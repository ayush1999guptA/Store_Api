from flask_restful import Resource,reqparse
from models.user_model import UserModel


class Userregistry(Resource):

	def post(self):
		parser=reqparse.RequestParser()
		parser.add_argument('username',
			type=str,
			required=True,
			help='this field cannot be empty')
		parser.add_argument('password',
		type=str,
		required=True,
		help='this field cannot remain empty')
		data=parser.parse_args()		
		user=UserModel.search_by_name(data['username'])
		if user!=None:
			return {'message':'this username is already taken'},400
		else:
			user=UserModel(data['username'],data['password'])
			user.insert()
			return {'name':data['username'],'password':data['password']},201

	def put(self):
		parser=reqparse.RequestParser()
		parser.add_argument('username',
			type=str,
			required=True,
			help='this field cannot be empty')
		parser.add_argument('oldpassword',
		type=str,
		required=True,
		help='this field cannot remain empty')
		parser.add_argument('newpassword',
			type=str,
			required=True,
			help='this field cannot remain empty')
		data=parser.parse_args()		
		user=UserModel.search_by_name(data['username'])
		if user==None:
			user=UserModel(data['username'],data['newpassword'])
			user.insert()
			return {'name':data['username'],'password':data['newpassword'],'message':'new user created with newpasssword'},201
		else:
			if data['oldpassword']==user.password:
				user.password=data['newpassword']
				user.update()
				return{'message':'User updated Successfully'},202
			else :
				return {'message':'User oldapssword Incorrect'},401

	def delete(self):
		parser=reqparse.RequestParser()
		parser.add_argument('username',
			type=str,
			required=True,
			help='this field cannot be empty')
		parser.add_argument('password',
		type=str,
		required=True,
		help='this field cannot remain empty')
		data=parser.parse_args()		
		user=UserModel.search_by_name(data['username'])
		if user!=None:
			user.delete()
			return {'message':'User deleted Successfully'},202
		else:
			return{'message':'User not found'},404	


								

