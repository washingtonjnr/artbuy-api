from sqlalchemy.ext.declarative import declarative_base

# Ext
from api.ext.database import db


Model = db.Model


Base = declarative_base()

# Association table for many-to-many relationship between Post and Category
post_category_table = db.Table(
    "post_category",
    Base.metadata,
    db.Column("post_id", db.UUID, db.ForeignKey("post.id"), primary_key=True),
    db.Column("category_id", db.UUID, db.ForeignKey("category.id"), primary_key=True),
)
