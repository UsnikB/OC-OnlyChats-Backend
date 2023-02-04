import jwt
from flask_jwt_extended import create_access_token
from config import Config

def create_token(user_id):
    access_token = create_access_token(identity=user_id)
    return access_token

def decode_token(token):
    decoded_token = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
    return decoded_token
