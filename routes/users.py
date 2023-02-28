from flask import Blueprint, jsonify, request
from database import db
from models import User
from models import UserType
from auth.authentication import if_authenticated

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['POST'])
def create_user():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    if not username or not email or not password:
        return {"message": "Please provide all required information"}, 400
    user = User(username=username, email=email, password=password)
    db.session.commit()
    return user.to_dict(), 201

@users_bp.route('/users/<int:user_id>', methods=['GET'])
@if_authenticated
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"message": "User not found"}, 404
    return user.to_dict()

@users_bp.route('/users', methods=['GET'])
# @if_authenticated
def get_users():
    # users = User.query.all()
    usertypes = UserType.query.all()
    # return {'users': [user.to_dict() for user in users]}
    return {'usertypes': [usertype.to_dict() for usertype in usertypes]}


@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"message": "User not found"}, 404
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    if not username or not email or not password:
        return {"message": "Please provide all required information"}, 400
    user.username = username
    user.email = email
    user.password = password
    db.session.commit()
    return user.to_dict()


@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"message": "User not found"}, 404
    db.session.delete(user)
    db.session.commit()
    return {"message": "User deleted"}, 204

