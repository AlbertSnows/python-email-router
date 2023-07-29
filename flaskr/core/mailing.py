import os
from pyrsistent import thaw
from flaskr.core.parsing import update_email_body_to_plaintext
import sendgrid
from sendgrid.helpers.mail import *

example = {
	"to": "fake@example.com",
	"to_name": "Mr. Fake",
	"from": "no-reply@fake.com",
	"from_name":"Ms. Fake",
	"subject": "A message from The Fake Family",
	"body": "<h1>Your Bill</h1><p>$10</p>"
}

def build_sendguard_email(email_info):
  from_email = Email(email_info["from"], email_info["from_name"])
  to_email = To(email_info["to"], email_info["to_name"])
  content = Content("text/plain", email_info["body"])
  subject = Subject(email_info["subject"])
  mail = Mail(from_email, to_email, subject, content)
  return mail;

def send_email(email_info):
  sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
  mail = build_sendguard_email(email_info)
  mail_response = sg.client.mail.send.post(request_body=mail.get())
  return mail_response
  

def handle_email_routing(email_info):
  email_info_with_plaintext_body = update_email_body_to_plaintext(email_info)
  mail_response = send_email(email_info)
  return mail_response
