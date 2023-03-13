import jwt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from functools import wraps
from flask import request, g
from models import UserType, UserUserType
from flask import jsonify
from config import Config

def create_token(user_id):
    access_token = create_access_token(identity=user_id)
    return access_token

def decode_token(token):
    decoded_token = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
    return decoded_token
def if_authenticated(func):
    @wraps(func)
    @jwt_required()
    def wrapper(*args, **kwargs):
        current_user = get_jwt_identity()
        if current_user:
            return func(*args, **kwargs)
        else:
            return jsonify({"msg": "Invalid token"}), 401
    return wrapper

def if_admin(func):
    @wraps(func)
    @jwt_required()
    def wrapper(*args, **kwargs):
        current_user_id = get_jwt_identity()
        user_usertype_id = UserUserType.query.filter_by(user_id=current_user_id).first().id
        user_type = UserType.query.filter_by(id=user_usertype_id).first()
        if user_type.name == 'admin':
            return func(*args, **kwargs)
        else:
            return jsonify({"msg" : "Not enough previlage"})
    return wrapper

