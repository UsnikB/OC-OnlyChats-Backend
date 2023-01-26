from flask import Blueprint, jsonify, request

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/test', methods=['GET'])
def test_route():
    return jsonify(message='Hello, World!')
