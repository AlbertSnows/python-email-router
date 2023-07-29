def handle(action, exception, final=None):
  try:
    return action()
  except Exception as e:
    return exception(e)
  # finally: # does this make sense?
  #   if(final is not None):
  #     final()   
    