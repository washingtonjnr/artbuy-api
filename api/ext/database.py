from flask_sqlalchemy import SQLAlchemy


db: SQLAlchemy = SQLAlchemy()


def init_app(app):
    # Config database
    app.config["SQLALCHEMY_DATABASE_URI"] = app.config.get("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()
