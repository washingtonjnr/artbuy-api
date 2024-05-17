def init_app(app):
    from dynaconf import settings

    JWT_SECRET_KEY = app.config.get("JWT_SECRET_KEY")
    # DATABASE
    SQLALCHEMY_DATABASE_URI = app.config.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    globals().update(locals())
