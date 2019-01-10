from models.user_model import UserModel
from werkzeug.security import safe_str_cmp


def authenticate(username,password):
	user=UserModel.search_by_name(username)
	if user!=None and safe_str_cmp(user.password,password):
		print(user)
		return user
def identity(payload):
	user_id=payload['identity']
	return UserModel.search_by_id(user_id)		