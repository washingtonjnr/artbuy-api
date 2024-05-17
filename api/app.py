from flask import Flask

#
from api.ext import config


def minimal_app():
    app = Flask(__name__)

    return app


def create_app():
    app = minimal_app()

    config.init_app(app)
    config.load_extensions(app)

    return app
