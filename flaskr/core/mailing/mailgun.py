# curl --request POST \
#   --url https://api.mailgun.net/v3/sandbox5d4a226da6574a969f08721e6389aadd.mailgun.org/messages \
#   --header 'Authorization: Basic YXBpOjcwYzM0YjU1MjhiZmMxY2FlYzhiOTk4ODgyOWI1ODc3LTRlMDM0ZDllLTI5Njg4NTZm' \
#   --header 'content-type: multipart/form-data' \
#   --form 'from=Excited User <mailgun@sandbox5d4a226da6574a969f08721e6389aadd.mailgun.org>' \
#   --form to=ajsnow2012@gmail.com \
#   --form to=ajsnow2012@gmail.com \
#   --form subject=Hello \
#   --form 'text=Testing some Mailgun awesomeness!' \
#   --form user=sandbox5d4a226da6574a969f08721e6389aadd.mailgun.org

def send_mailgun_email(env, email_info):
  return {"status_code": 501}