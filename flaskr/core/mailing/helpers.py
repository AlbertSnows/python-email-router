def get_mail_failure_exception(exception):
  return {"mail_failure": 
    { "error_type": type(exception).__name__, 
      "error_message": str(exception)}}