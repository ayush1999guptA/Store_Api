from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt import jwt_required
from models.user_model import UserModel
import sqlite3


class Userregistry(Resource):

	@jwt_required()
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
			user=UserModel.insert(data['username'],data['password'])
			return {'name':data['username'],'password':data['password']},201

	@jwt_required()		
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
			UserModel.insert(data['username'],data['newpassword'])
			return {'name':data['username'],'password':data['newpassword'],'message':'new user created with newpasssword'},201
		else:
			if data['oldpassword']==user.password:
				UserModel.update(user.username,data['newpassword'])
				return{'message':'User updated Successfully'},202
			else :
				return {'message':'User oldapssword Incorrect'},401

	@jwt_required()			
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
		if user!=None and safe_str_cmp(data['password'],user.password)  :
			UserModel.delete(data['username'])
			return {'message':'User deleted Successfully'},202
		else:
			return{'message':'User not found or user password wrong '},404	

class Users(Resource):
	
	@jwt_required()
	def get(self):
		users=[]
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query='SELECT * FROM users'
		result=cursor.execute(query)
		for row in result:
			users.append({'username':row[1]})
		connection.close()
		return {'users':users} 	



								

