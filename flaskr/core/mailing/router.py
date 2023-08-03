from flaskr.core.parsing import update_email_body_to_plaintext
from flaskr.config.mappings import ROUTING_OPTIONS


# Expects functions to be in the form f(env, email_info)
def handle_email_routing(email_info, env):
  email_info_with_plaintext_body = update_email_body_to_plaintext(email_info)
  email_router = env.get("EMAIL_ROUTER")
  send_email = ROUTING_OPTIONS[email_router] # todo bonus: implement get_if_exists
  mail_response = send_email(email_info_with_plaintext_body)
  return mail_response