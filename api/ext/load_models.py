def init_app(app):
    from api.models.file import FileModel
    from api.models.user import UserModel
    from api.models.address import AddressModel

    return app
