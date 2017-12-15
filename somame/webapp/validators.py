from django.core.exceptions import ValidationError


def validate_email(value):
        email = value
        if ".edu" in email:
            raise ValidationError("We do not accept edu emails")
