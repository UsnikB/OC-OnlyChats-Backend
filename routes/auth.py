from flask import request, jsonify, Blueprint
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

authentication_bp = Blueprint('authentication', __name__)


@authentication_bp.route('/login', methods=['POST'])
def login():
    # Get the user's credentials from the request
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Authenticate the user
    if not authenticate(username, password):
        return jsonify({"msg": "Bad username or password"}), 401

    # Create the JWT token
    # user_id = get_user_id(username)
    access_token = create_token("user_id")

    # Return the token to the client
    return jsonify(access_token=access_token), 200

def authenticate(username, password):
    # Check the user's credentials against the database
    # Return True if the credentials are valid, False otherwise
    if username == "test" and password == "test":
        return True
    else:
        return False



