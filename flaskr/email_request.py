from wtforms import (
    Form,
    BooleanField,
    StringField,
    validators,
    DateTimeField,
    TextAreaField,
    IntegerField,
    EmailField
)

# todo: all fields are required -> input required
class EmailRequest(Form):
 	to = EmailField("to", [validators.Email])
	to_name = StringField("to_name", []) # is string
	from_email = EmailField("from", [validators.Email])
	subject = StringField("subject", []) # is string
	body = StringField("body", []) # are there any concerns with html payloads?
 
	def validate_body(form, field):
			form_is_not_string = !(isinstance(test_string, str))
			if(form_is_not_string):
				raise ValidationError('Body must be a string of data')



class AdminProfileForm(ProfileForm):
    username = StringField("Username", [validators.Length(max=40)])
    level = IntegerField("User Level", [validators.NumberRange(min=0, max=10)])
