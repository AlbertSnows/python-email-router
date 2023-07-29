from flask import Blueprint, request, jsonify
from flaskr.utility.file import load_json_from_file
from jsonschema import validate, exceptions, FormatChecker
from pyrsistent import freeze, thaw
from bs4 import BeautifulSoup

example = {
	"to": "fake@example.com",
	"to_name": "Mr. Fake",
	"from": "no-reply@fake.com",
	"from_name":"Ms. Fake",
	"subject": "A message from The Fake Family",
	"body": "<h1>Your Bill</h1><p>$10</p>"
}

bp = Blueprint("email", __name__, url_prefix="/email")

def validate_input(json):
	email_schema = load_json_from_file('./flaskr/schema/email.json')
	try:
		validate(json, email_schema, format_checker=FormatChecker())
		return {"message": "Email Routed"}
	except exceptions.ValidationError as e:
		return {"error":e.message}   
  
def handle_email_routing(email_info):
  soup = BeautifulSoup(email_info["body"], "html.parser")
  email_body_as_plain_text = soup.get_text()
  email_info_with_plaintext_body = email_info.set("body", email_body_as_plain_text)
  return thaw(email_info_with_plaintext_body)

@bp.route("/", methods=["POST"])
def process_email_routing_request():
  validated_json = validate_input(example)
  resp_payload = handle_email_routing(freeze(example)) if (not "error" in validated_json) else validated_json
  resp = jsonify(resp_payload)
  return resp
  