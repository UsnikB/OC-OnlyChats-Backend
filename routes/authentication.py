from flask import request, jsonify, Blueprint
from auth.authentication import create_token, decode_token
from models import User

authentication_bp = Blueprint('authentication', __name__)

@authentication_bp.route('/add_user', methods=['POST'])
def add_user():
    username = request.json.get('username', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    return jsonify({"username": username}, {"email":email}, {"password":password}), 200


@authentication_bp.route('/login', methods=['POST'])
def login():
    # Get the user's credentials from the request
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Authenticate the user
    if not authenticate(username, password):
        return jsonify({"msg": "Bad username or password"}), 401

    # Create the JWT token
    user_id = get_user_id(username, password)
    access_token = create_token(user_id)
    user = User.query.get(user_id)
    # return jsonify({"msg": "Password works"}, {"access_token":access_token}), 200
    # Return the token to the client
    return jsonify(access_token=access_token, current_user= user.username), 200

def authenticate(username, password):
    # Check the user's credentials against the database
    # Return True if the credentials are valid, False otherwise
    user = User.query.filter_by(username=username, password=password).first()
    return user

def get_user_id(username, password):
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        return user.id
    else:
        return None



