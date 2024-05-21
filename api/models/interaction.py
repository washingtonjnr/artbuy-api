import uuid
from datetime import datetime

# Libs
from sqlalchemy import UniqueConstraint
from sqlalchemy_serializer import SerializerMixin

# Ext
from api.ext.database import db


Model = db.Model


class InteractionTypeModel(Model, SerializerMixin):
    __tablename__ = "interaction_type"
    #
    id = db.Column(
        db.UUID,
        primary_key=True,
        default=lambda: uuid.uuid4(),
    )
    name = db.Column(db.String(15), nullable=False)
    icon = db.Column(db.String(15), nullable=False)
    color = db.Column(db.String(15), nullable=False)

    # [EXT DATA]
    # USER
    # INTERACTION


class InteractionModel(Model, SerializerMixin):
    __tablename__ = "interaction"
    #
    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)

    # [RELASHIONSHIP]
    interaction_type_id = db.Column(
        db.UUID,
        db.ForeignKey("interaction_type.id", use_alter=True),
        nullable=False,
        unique=True,
    )
    interaction_type = db.relationship("InteractionTypeModel")
    #
    user_id = db.Column(
        db.UUID, db.ForeignKey("user.id", use_alter=True), nullable=False
    )
    user = db.relationship("UserModel", back_populates="interactions")
    #
    post_id = db.Column(
        db.UUID, db.ForeignKey("post.id", use_alter=True), nullable=False
    )
    post = db.relationship(
        "PostModel", back_populates="interactions", foreign_keys=[post_id]
    )
    #
    comment_id = db.Column(
        db.UUID, db.ForeignKey("comment.id", use_alter=True), nullable=False
    )
    comment = db.relationship(
        "CommentModel", back_populates="interactions", foreign_keys=[comment_id]
    )

    # Unique constraint to ensure one interaction per user per post or comment
    __table_args__ = (
        UniqueConstraint("user_id", "post_id", name="_user_post_uc"),
        UniqueConstraint("user_id", "comment_id", name="_user_comment_uc"),
    )
