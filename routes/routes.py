from flask import Blueprint, jsonify, request
from database import db
routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/', methods=['GET'])
def test_route():
    return jsonify(message='This is our OnlyChats API 2, All writes Reserved!')
