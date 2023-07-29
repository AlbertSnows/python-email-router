from flask import Blueprint, request, jsonify
from flaskr.utility.file import load_json_from_file
from jsonschema import validate, exceptions, FormatChecker
from pyrsistent import freeze, thaw

bp = Blueprint("email", __name__, url_prefix="/email")

def validate_input():
	email_schema = load_json_from_file('./flaskr/schema/email.json')
	try:
		validate(request.json, email_schema, format_checker=FormatChecker())
		return {"message": "Email Routed"}
	except exceptions.ValidationError as e:
		return {"error":e.message}   
  
def handle_email_routing(email_info):
  return thaw(email_info)

@bp.route("/", methods=["POST"])
def process_email_routing_request():
  validated_json = validate_input()
  resp_payload = handle_email_routing(freeze(validated_json)) if (not "error" in validated_json) else validated_json
  resp = jsonify(resp_payload)
  return resp
  