from wtforms import (
    Form,
    StringField,
    validators,
    EmailField,
    ValidationError
)
from wtforms.validators import InputRequired, Email

import email_validator

# todo: all fields are required -> input required
class EmailRequest(Form):
    def is_string(form, field):
        form_is_not_string = not isinstance(field, str)
        if(form_is_not_string):
            raise ValidationError('Body must be a string of data')
        
    # content_type = StringField("Content-Type", )
    # to = EmailField("to", [validators.InputRequired, validators.Email])
    # to_name = StringField("to_name", [validators.InputRequired, is_string])
    from_email = EmailField("from_email", [InputRequired(), Email()])
    # subject = StringField("subject", [validators.InputRequired, is_string])
    # body = StringField("body", [validators.InputRequired, is_string])
 
