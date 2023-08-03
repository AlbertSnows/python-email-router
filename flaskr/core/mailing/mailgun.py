import json
import requests
from flaskr.utility.exceptions import handle
from flaskr.core.mailing.helpers import get_mail_failure_exception

def build_mailgun_payload(email_info):
  return   {
    "from": "{} {}".format(email_info["from"], email_info["from_name"]),
    "to": "{} {}".format(email_info["to"], email_info["to_name"]),
    "subject": email_info["subject"],
    "text": email_info["body"]}

def build_mailgun_email(api_domain, api_key, email_info):
  url = "https://api.mailgun.net/v3/{}/messages".format(api_domain)
  payload = build_mailgun_payload(email_info)
  auth = {
    "api", api_key
  }
  mail_response = lambda: requests.post(url, auth=auth,  data=json.dumps(payload))
  return mail_response;

def parse_mail_response(payload):
  match payload.status_code:
    case 202: return {"message": "Email sent!", "status_code": 200}
    case 403: return {"error": "Problem with mail request", "info": payload.json(), "status_code": 400}
    case 401: return {"error": "not found error", "info": payload.json(), "status_code": 400}
    case None | _: return {"warning": "Unhandled status code: {}".format(payload.status_code), "status_code": 400}

def send_mailgun_email(env, email_info):
  api_key = env.get("MAILGUN_API_KEY", "Bad env config: api key")
  api_domain = env.get("MAILGUN_DOMAIN", "Bad env config: api domain")
  send_mail_payload = build_mailgun_email(api_domain, api_key, email_info)
  send_mail_to_mailgun = lambda: send_mail_payload()
  mail_response = handle(send_mail_to_mailgun, get_mail_failure_exception)
  parsed_mail_response = parse_mail_response(mail_response)
  return parsed_mail_response
