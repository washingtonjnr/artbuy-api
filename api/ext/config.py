from dynaconf import FlaskDynaconf

# Lib
from importlib import import_module


def init_app(app):
    # Set settings.toml
    FlaskDynaconf(app)


def load_extensions(app):
    for extension in app.config.get("EXTENSIONS", []):
        mod = import_module(extension)
        mod.init_app(app)
