from flask import request

# Libs
from flask_restful import Resource
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required

# Model
from api.models.user import UserModel
from api.models.address import AddressModel

# Schemas
from api.schemas import load_json_schema, update_object
from api.schemas.address import AddressSchema

# Utils
from api.utils.http_response import success, error


class UserAddressManage(Resource):
    @jwt_required()
    def post(self):
        try:
            schema = load_json_schema(request, AddressSchema)
        except ValidationError as err:
            return error(err.messages)

        user = UserModel.get_session_user()
        address = AddressModel()

        update_object(address, schema)

        address.user = user

        address.save_to_db()

        return success(address.json())

    @jwt_required()
    def put(self):
        return success()

    @jwt_required()
    def get(self):
        user = UserModel.get_session_user()

        if not user:
            return error("Invalid credencials")

        return success(user.address.json())
