from flask import Blueprint, jsonify, request

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/', methods=['GET'])
def test_route():
    return jsonify(message='This is our OnlyChats API 2, All writes Reserved!')

@routes_bp.route('/create')
def create_user():
    user = Users(name='John Doe', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    return 'User created successfully!'
