from datetime import timedelta

# Libs
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Ext
from api.ext import envs


db: SQLAlchemy = SQLAlchemy()


def init_app(app):
    # Config JWT
    app.config["JWT_JSON_KEY"] = "token"
    app.config["JWT_QUERY_STRING_NAME"] = "token"
    app.config["JWT_SECRET_KEY"] = envs.JWT_SECRET_KEY
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

    jwt_manager = JWTManager(app)

    @jwt_manager.decode_key_loader
    def secret_to_decode(header, payload):
        return envs.JWT_SECRET_KEY

    @jwt_manager.encode_key_loader
    def secret_to_encode(session_data):
        return envs.JWT_SECRET_KEY
