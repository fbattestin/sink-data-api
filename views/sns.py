from flask import Blueprint, request, jsonify
from controllers.sns import process_sns_message

sns_blueprint = Blueprint('sns', __name__)


@sns_blueprint.route('/sns-endpoint', methods=['POST'])
def sns_endpoint():
    headers = request.headers
    message = request.json
    process_sns_message(headers, message)
    return jsonify({'status': 'success'}), 200
