  # reference code that doesn't work or is unnecessary     
  # # todo bonus: these checks should be move out
  # resp_dict = resp_payload.get("__dict__", {"error": "No dict available"})
  # if "error" in resp_dict:
  #   return resp_dict
  
  # status_code = resp_dict.get("status_code", 501)
  # if(not isinstance(status_code, int)):
  #   print("error: payload did not have status code")
  #   return status_code
  # reason = resp_dict.get("reason", "No reason given.")