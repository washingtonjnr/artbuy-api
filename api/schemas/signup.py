from marshmallow import Schema, post_load, ValidationError
from marshmallow.fields import String, Dict

# Parsers
from api.utils.parsers import remove_nom_numeric_chars

# Utils
from api.utils.parsers import normalize_email, format_phonenumber
from api.utils.validators import (
    validate_email,
    validate_cpf,
    validate_phone,
    validate_password,
)


class SignupAuthenticatorSchema(Schema):
    data = Dict(required=False)
    provider = String(required=True)
    access_token = String(required=True)
    code = String(required=False, allow_none=True)
    refresh_token = String(required=False, allow_none=True)

    @post_load
    def process_post_load(self, data, **kwargs):
        if data["provider"] == "apple" and not data.get("code"):
            raise ValidationError({"code": "Field is required for apple provider"})

        return data


class SignupSchema(Schema):
    name = String(required=True, allow_none=False)
    cpf = String(required=True, allow_none=False, validate=validate_cpf)
    phone = String(required=True, allow_none=False, validate=validate_phone)
    email = String(
        required=False, allow_none=True, default=None, validate=validate_email
    )
    password = String(
        required=False,
        allow_none=True,
        default=None,
        validate=validate_password,
    )

    @post_load
    def process_post_load(self, data, **kwargs):
        validations = {}

        # Parser valid values
        def text_parse(text: str):
            return " ".join(text.split())

        def phone_parse(phone: str):
            # Removing non-numeric characters from phone, except for "+"
            phone = remove_nom_numeric_chars(phone, exceptions=["+"])
            # Formatting the phone number
            phone = format_phonenumber(phone)

            return phone

        # Fields and message errors
        fields_to_validate = {
            "cpf": {"message_error": "Invalid cpf"},
            "name": {"message_error": "Invalid name", "parser": text_parse},
            "phone": {"message_error": "Invalid phone", "parser": phone_parse},
            "email": {"message_error": "Invalid email", "parser": normalize_email},
            "password": {
                "message_error": "Invalid password",
            },
        }

        for field, info in fields_to_validate.items():
            value = data.get(field)

            if not value:
                validations[field] = info["message"]
            else:
                if "parser" in info:
                    value = info["parser"](value)

                data[field] = value

        # If there are any validation errors, raise a ValidationError
        if validations:
            raise ValidationError(validations)

        return data
