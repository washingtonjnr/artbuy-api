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
    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    key = db.Column(db.String(64), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    mime_type = db.Column(db.String(255), nullable=False)
    # [RELASHIONSHIP]
    # 1:1
    user_id = db.Column(
        db.UUID, db.ForeignKey("user.id", use_alter=True), nullable=False, unique=True
    )
    user = db.relationship("UserModel")
    # 1:n
    post_id = db.Column(
        db.UUID, db.ForeignKey("post.id", use_alter=True), nullable=True
    )
    post = db.relationship("PostModel", back_populates="files")
