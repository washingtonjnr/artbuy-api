from flask import request

# Libs
from flask_restful import Resource
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required

# Model
from api.models.user import UserModel, UserModelAttributes

# Schemas
from api.schemas import load_json_schema
from api.schemas.signin import SigninSchema
from api.schemas.signup import SignupSchema

# Utils
from api.utils.hash import sha512
from api.utils.http_response import success, error

# -------------------------
# ---- AUTH RESOURCES -----
# -------------------------


# USER SIGNUP ["/v1/auth/signup"]
class UserSignupManager(Resource):
    def post(self):
        try:
            schema = load_json_schema(request, SignupSchema)
        except ValidationError as err:
            return error(err.messages)

        cpf = schema.get("cpf")
        name = schema.get("name")
        email = schema.get("email")
        phone = schema.get("phone")
        password = schema.get("password")

        if UserModel.find_user_by_attribute(
            attribute=UserModelAttributes.EMAIL, value=email
        ):
            return error(params={"message": "Email already in use"})

        if UserModel.find_user_by_attribute(
            attribute=UserModelAttributes.CPF, value=cpf
        ):
            return error(params={"message": "CPF already in use"})

        # TODO: validate if CPF is valid

        password = sha512(password)

        user = UserModel(
            cpf=cpf,
            name=name,
            email=email,
            phone=phone,
            password=password,
            is_enabled=True,
            is_private=False,
        )

        user.save_to_db()

        response = user.auth_response()

        return success(response)


# USER SIGNIN ["/v1/auth/signin"]
class UserSigninManager(Resource):
    def post(self):
        try:
            # Load and validate the JSON schema from the request using the SigninSchema
            schema = load_json_schema(request, SigninSchema)
        except ValidationError as err:
            return error(err.messages)

        email = schema.get("email")
        password = schema.get("password")
        #
        password = sha512(password)
        #
        user = UserModel.query.filter(
            UserModel.email == email,
            UserModel.password == password,
            UserModel.is_enabled == True,
        ).first()

        if not user:
            return error("Invalid credencials")

        response = user.auth_response()

        return success(response)


# USER SIGNOUT ["/v1/auth/signout"]
class UserSignoutManager(Resource):
    def post(self):
        return {}


# -------------------------
# ---- MODEL RESOURCES ----
# -------------------------


# USER ["v1/user/me"]
class UserManager(Resource):
    @jwt_required()
    def get(self):
        user = UserModel.get_session_user()

        if not user:
            return error(
                "User not found",
            )

        return success(user.json())

    @jwt_required()
    def delete(self, user_id):
        user = UserModel.find_user_by_attribute(
            param=UserModelAttributes.ID, value=user_id
        )

        if user:
            user.remove_from_db()

            return success(status_code=204)

        raise error("User not found")
