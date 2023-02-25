from flask import Blueprint, jsonify, request
from models import User
from database import db
routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/', methods=['GET'])
def test_route():
    return jsonify(message='This is our OnlyChats API 2, All writes Reserved!')

@routes_bp.route('/create')
def create_user():
    user = User(username='qwe123', email='john@example.com', password='qwe123')
    db.session.add(user)
    db.session.commit()
    return 'User created successfully!'
