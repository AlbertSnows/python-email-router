from wtforms import (
    Form,
    StringField,
    validators,
    EmailField,
    ValidationError
)

# todo: all fields are required -> input required
class EmailRequest(Form):
    def is_string(form, field):
        form_is_not_string = not isinstance(field, str)
        if(form_is_not_string):
            raise ValidationError('Body must be a string of data')

    to = EmailField("to", [validators.InputRequired, validators.Email])
    to_name = StringField("to_name", [validators.InputRequired, is_string])
    from_email = EmailField("from", [validators.InputRequired, validators.Email])
    subject = StringField("subject", [validators.InputRequired, is_string])
    body = StringField("body", [validators.InputRequired, is_string])
 
