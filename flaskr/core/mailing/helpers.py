import requests

def get_mail_failure_exception(exception):
  return {"mail_failure": 
    { "error_type": type(exception).__name__, 
      "error_message": str(exception)}}
  
def parse_mail_response(resp_payload):
  if not isinstance(resp_payload, requests.models.Response):
    return {"error": "response is not of a response type, not handling currently.", "type": type(resp_payload), "status_code": 501}
  status_code = resp_payload.status_code
  reason = resp_payload.reason
  resp_info = {"reason": reason, "router_status_code": status_code}  
  match status_code:
    case 202: return {"message": "Email sent!", "status_code": 202}
    case 200: return {"message": "Email sent!", "status_code": 202}
    case 403: return {"error": "Problem with mail request, are you sure the email is set up correctly?", "info": resp_info, "status_code": 403}
    case 401: return {"error": "not found error", "info": resp_info, "status_code": 401}
    case 501: return {"error": "Response did not contain a status code.", "info": resp_info, "status_code": status_code}
    case None | _: return {"warning": "Unhandled status code: {}".format(status_code), "info": resp_info, "status_code": status_code}