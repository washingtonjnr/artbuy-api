import uuid

# Libs
from sqlalchemy import func
from sqlalchemy_serializer import SerializerMixin

# Ext
from api.ext.database import db

# Models
from api.models.post_category import post_category_table


Model = db.Model


class PostModel(Model, SerializerMixin):
    __tablename__ = "post"
    #
    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    #
    price = db.Column(
        db.Integer,
        nullable=True,
    )
    description = db.Column(
        db.Text,
        nullable=True,
    )
    is_archived = db.Column(
        db.Boolean,
        default=False,
    )
    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now(),
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=func.now(),
        server_default=func.now(),
    )

    # -- [EXT DATA]
    # CATEGORY
    # COMMENT
    # FILE
    # INTERACTION

    # -- [RELASHIONSHIPS]
    user_id = db.Column(
        db.UUID, db.ForeignKey("user.id", use_alter=True), nullable=False
    )
    user = db.relationship(
        "UserModel",
        primaryjoin="UserModel.id == PostModel.user_id",
        back_populates="posts",
    )
    #
    buyer_id = db.Column(
        db.UUID, db.ForeignKey("user.id", use_alter=True), nullable=True
    )
    buyer = db.relationship(
        "UserModel",
        primaryjoin="UserModel.id == PostModel.buyer_id",
        back_populates="posts",
    )
    # 1:n
    comments = db.relationship(
        "CommentModel", back_populates="post", cascade="all, delete-orphan"
    )
    files = db.relationship(
        "FileModel", back_populates="post", cascade="all, delete-orphan"
    )
    interactions = db.relationship(
        "InteractionModel", back_populates="post", cascade="all, delete-orphan"
    )
