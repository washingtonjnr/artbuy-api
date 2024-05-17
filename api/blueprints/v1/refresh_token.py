from datetime import timedelta

# Libs
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask_jwt_extended.utils import get_jwt_identity, create_access_token

# Utils
from api.utils.http_response import success


class RefreshTokenManage(Resource):
    @jwt_required(refresh=True)
    def post():
        current_user_id = get_jwt_identity()

        new_token = create_access_token(
            identity=current_user_id,
            expire_delta=timedelta(hours=3),
            fresh=False,
        )

        return success({"access_token": new_token})
