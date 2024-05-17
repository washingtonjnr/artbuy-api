from flask_migrate import Migrate

# Ext
from api.ext.database import db


migrate = Migrate()


def init_app(app):
    migrate.init_app(app, db)

    return app
