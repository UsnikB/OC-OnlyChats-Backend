from flask import Blueprint, jsonify, request
from database import db
from auth.authentication import if_admin, if_authenticated

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/', methods=['GET'])
def test_route():
    return jsonify(message='This is our OnlyChats API 2, All writes Reserved!')

@routes_bp.route('/admin', methods=['GET'])
@if_admin
def admin_test_route():
    return jsonify(message='only admin can view this message')
