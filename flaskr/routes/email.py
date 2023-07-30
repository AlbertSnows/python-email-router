from flask import Blueprint, request, jsonify
from flaskr.utility.file import load_json_from_file
from jsonschema import validate, exceptions, FormatChecker
from pyrsistent import freeze
from flaskr.core.mailing import handle_email_routing
import json 
import os

bp = Blueprint("email", __name__, url_prefix="/email")

def validate_input(json):
	email_schema = load_json_from_file('./flaskr/schema/email.json')
	try:
		validate(json, email_schema, format_checker=FormatChecker())
		return {"message": "Valid payload"}
	except exceptions.ValidationError as e:
		return {"error":e.message}   

@bp.route("/", methods=["POST"])
def process_email_routing_request():
  payload = request.json
  validation_result = validate_input(payload) 
  mail_response = handle_email_routing(freeze(payload)) if (not "error" in validation_result) else {"mail_result": "Invaild payload, could not send"}
  resp_payload = {"validated": validation_result,
                  "routed_mail": mail_response}
  resp = jsonify(resp_payload)
  return resp
  