import uuid

# Libs
from sqlalchemy_serializer import SerializerMixin

# Ext
from api.ext.database import db

# Utils
from api.utils.db_types import db_uuid

Model = db.Model


class FileModel(Model, SerializerMixin):
    __tablename__ = "file"
    #
    serialize_rules = ("-user",)
    #
    id: uuid.uuid4 = db.Column(
        db_uuid(), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    # About
    key: str = db.Column(db.String(64), nullable=False)
    filename: str = db.Column(db.String(255), nullable=False)
    mime_type: str = db.Column(db.String(255), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.id:
            self.id = uuid.uuid4()
