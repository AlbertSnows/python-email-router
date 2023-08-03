import types
from flaskr.core.mailing.mailgun import send_mailgun_email
from flaskr.core.mailing.sendgrid import send_sendgrid_email

_route_options = {
	"MAILGUN": send_mailgun_email,
 "SENDGRID": send_sendgrid_email
}

ROUTING_OPTIONS = types.MappingProxyType(_route_options)