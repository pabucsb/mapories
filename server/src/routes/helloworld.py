from flask import Blueprint, jsonify

helloworld_bp = Blueprint('helloworld', __name__)

@helloworld_bp.route('/helloworld', methods=['GET'])
def helloworld():
    return jsonify({'message': 'Hello, World!'})