import json
import requests
from flaskr.utility.exceptions import handle
from flaskr.core.mailing.helpers import get_mail_failure_exception
from flaskr.core.mailing.helpers import parse_mail_response
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
  mail_response = lambda: requests.post(url, data=json.dumps(payload), headers=headers)
  return mail_response;
    
def send_sendgrid_email(env, email_info):
  api_key = env.get("SENDGRID_API_KEY")
  send_mail_payload = build_sendgrid_email(api_key, email_info)
  send_mail_to_sendgrid = lambda: send_mail_payload()
  mail_response = handle(send_mail_to_sendgrid, get_mail_failure_exception)
  parsed_mail_response = parse_mail_response(mail_response)
  return parsed_mail_response
