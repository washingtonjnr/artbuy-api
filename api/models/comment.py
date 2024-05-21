import uuid
from datetime import datetime

# Lib
from sqlalchemy_serializer import SerializerMixin

# Ext
from api.ext.database import db


Model = db.Model


class CommentModel(Model, SerializerMixin):
    __tablename__ = "comment"
    #
    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.now, onupdate=datetime.now)

    # [INTERNAL RELASHIONSHIPS] (Comment of the Comment)
    parent_id = db.Column(db.UUID, db.ForeignKey("comment.id", use_alter=True))
    parent = db.relationship(
        "CommentModel", remote_side=[id], back_populates="children"
    )
    children = db.relationship(
        "CommentModel", back_populates="parent", cascade="all, delete-orphan"
    )

    # [RELASHIONSHIPS]
    user_id = db.Column(
        db.UUID, db.ForeignKey("user.id", use_alter=True), nullable=False
    )
    user = db.relationship("UserModel", back_populates="comments")
    #
    post_id = db.Column(
        db.UUID, db.ForeignKey("post.id", use_alter=True), nullable=False
    )
    post = db.relationship("PostModel", back_populates="comments")
    #
    interactions = db.relationship(
        "InteractionModel", back_populates="comment", cascade="all, delete-orphan"
    )
