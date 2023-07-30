import os
from flaskr.core.parsing import update_email_body_to_plaintext
import json
import requests
from flaskr.utility.exceptions import handle
from dotenv import load_dotenv

#todo change this
load_dotenv()

def build_sendgrid_payload(email_info):
  return   {
    "personalizations":
      [{"to":[{"email":email_info["to"], "name":email_info["to_name"]}],
        "subject": email_info["subject"]}],
    "content": [{"type": "text/plain", "value": email_info["body"]}],
    "from":{"email":email_info["from"],"name": email_info["from_name"]}}

def build_sendgrid_email(api_key, email_info):
  url = "https://api.sendgrid.com/v3/mail/send"
  payload = build_sendgrid_payload(email_info)
  headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer {}".format(api_key)
  }
  payload = build_sendgrid_payload(email_info)
  mail_response = lambda: requests.post(url, data=json.dumps(payload), headers=headers)
  return mail_response;

def get_mail_failure_exception(exception):
  return {"mail_failure": 
    { "error_type": type(exception).__name__, 
      "error_message": str(exception)}}

def parse_mail_response(payload):
  match payload.status_code:
    case 202: return {"message": "Email sent!"}
    case 403: return {"error": "Problem with mail request", "info": payload.json()}
    case 401: return {"error": "not found error", "info": payload.json()}
    case None | _: return {"warning": "Unrecognized status code: {}".format(payload.status_code)}
    
def send_email(email_info):
  api_key = os.environ.get("SENDGRID_API_KEY")
  send_mail_payload = build_sendgrid_email(api_key, email_info)
  send_mail_to_sendgrid = lambda: send_mail_payload()
  mail_response = handle(send_mail_to_sendgrid, get_mail_failure_exception)
  parsed_mail_response = parse_mail_response(mail_response)
  return parsed_mail_response

def handle_email_routing(email_info):
  email_info_with_plaintext_body = update_email_body_to_plaintext(email_info)
  mail_response = send_email(email_info_with_plaintext_body)
  return mail_response
