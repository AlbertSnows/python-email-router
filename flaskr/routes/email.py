from flask import Blueprint, request, jsonify
from flaskr.utility.file import load_json_from_file
from jsonschema import validate, exceptions, FormatChecker

bp = Blueprint("email", __name__, url_prefix="/email")

@bp.route("/", methods=["POST"])
def process_email_routing_request():
	email_schema = load_json_from_file('./flaskr/schema/email.json')
	try:
		validate(request.json, email_schema, format_checker=FormatChecker())
		return request.json
	except exceptions.ValidationError as e:
		return jsonify(error=e.message)   
	
      