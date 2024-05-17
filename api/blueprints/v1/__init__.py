from flask import Blueprint
from flask_restful import Api, Resource

# Resources
from api.blueprints.v1 import address, user, refresh_token

# Schemas
from api.utils.http_response import success

bp = Blueprint("v1", __name__, url_prefix="/v1")
api = Api(bp)


# RESOURCE TEST
class StatusResource(Resource):
    def get(self):
        _ = self

        return success()


def init_app(app):
    # REQUEST TEST
    api.add_resource(StatusResource, "/status")

    # ENDPOINTS
    # """
    # [AUTH]
    # Refresh: ["/v1/refresh"]
    api.add_resource(refresh_token.RefreshTokenManage, "/refresh")
    # Signup: ["/v1/auth/signup"]
    api.add_resource(user.UserSignupManager, "/auth/signup")
    # Signin: ["/v1/auth/signin"]
    api.add_resource(user.UserSigninManager, "/auth/signin")
    # Signout: ["/v1/auth/signout"]
    api.add_resource(user.UserSignoutManager, "/auth/signout")
    # """

    # """
    # [USER]
    # User CRUD: ["/v1/user/me"]
    api.add_resource(user.UserManager, "/user/me")
    # User Address: ["/v1/user/address"]
    api.add_resource(address.UserAddressManage, "/user/address")
    # TODO: User Avatar: ["/v1/user/avatar"]
    # api.add_resource(file.UserAvatarManage, "/user/avatar")
    # """

    # """
    # [POST]
    # TODO: User Posts: ["/v1/user/:id/posts"]
    # api.add_resource(user.UserPostsManager, "/user/:id/posts")
    # """

    # REGISTER ENDPOINTS
    app.register_blueprint(bp)
