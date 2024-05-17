from marshmallow import Schema, fields, post_load, ValidationError
from marshmallow.fields import String, Length

# Utils
from api.utils.parsers import remove_nom_numeric_chars
from api.utils.validators import (
    validate_empty,
    validate_cep,
)


class AddressSchema(Schema):
    cep = fields.String(required=True, validate=validate_cep)
    state = String(required=True, validate=[Length(min=2, max=2)])
    number = fields.String(required=True, validate=validate_empty)
    street = fields.String(required=True, validate=validate_empty)
    country = fields.String(required=True, validate=validate_empty)
    province = fields.String(required=True, validate=validate_empty)
    complement = String(required=False, allow_none=True)
    neighborhood = fields.String(required=True, validate=validate_empty)

    @post_load
    def process_post_load(self, data, **kwargs):
        print("BEFORE DATA")
        print(data)
        validations = {}
        # Fields and message errors
        fields_to_validate = {
            "cep": "Invalid cep",
            "state": "Invalid state",
            "number": "Invalid number",
            "street": "Invalid street",
            "country": "Invalid country",
            "province": "Invalid province",
            "neighborhood": "Invalid neighborhood",
        }

        for field, error_message in fields_to_validate.items():
            if not data.get(field):
                validations[field] = error_message

        print("AFTER DATA")
        print(data)

        # If there are any validation errors, raise a ValidationError
        if validations:
            raise ValidationError(validations)

        return data
