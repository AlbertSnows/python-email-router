from bs4 import BeautifulSoup

def update_email_body_to_plaintext(email_info):
		soup = BeautifulSoup(email_info["body"], "html.parser")
		email_body_as_plain_text = soup.get_text()
		email_info_with_plaintext_body = email_info.set("body", email_body_as_plain_text)
		return email_info_with_plaintext_body
  