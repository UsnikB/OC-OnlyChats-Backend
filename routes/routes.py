from flask import Blueprint, jsonify, request
from .authentication import authentication_bp

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/', methods=['GET'])
def test_route():
    return jsonify(message='This is our OnlyChats API, All writes Reserved!')

