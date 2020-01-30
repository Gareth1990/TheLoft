from werkzeug.security import safe_str_cmp
from models.user import UserModel
# we are saying from user.py file import the class User

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password,):# Safe_str_cmp for old python versions
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
