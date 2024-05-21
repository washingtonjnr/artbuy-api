def init_app(app):
    from api.models.file import FileModel
    from api.models.user import UserModel
    from api.models.post import PostModel
    from api.models.comment import CommentModel
    from api.models.interaction import InteractionModel
    from api.models.category import CategoryModel
    from api.models.address import AddressModel

    return app
