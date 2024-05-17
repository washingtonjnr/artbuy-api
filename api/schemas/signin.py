from marshmallow import Schema, fields, post_load
from marshmallow.validate import Email

# Utils
from api.utils.parsers import normalize_email


class SigninSchema(Schema):
    email = fields.Email(
        required=True, validate=Email(error="Invalid email address")
    )
    password = fields.String(required=True)

    @post_load
    def process_post_load(self, data, **kwargs):
        data["email"] = normalize_email(data["email"])

        return data
