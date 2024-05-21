import uuid

# Libs
from sqlalchemy_serializer import SerializerMixin

# Ext
from api.ext.database import db

# Models
from api.models.post_category import post_category_table

# Utils
from api.utils.db_types import db_uuid


Model = db.Model


class CategoryTypeModel(Model, SerializerMixin):
    __tablename__ = "category_type"
    #
    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(50), nullable=False)
    icon = db.Column(db.String(15), nullable=False)
    color = db.Column(db.String(15), nullable=False)

    # [RELATIONSHIP]
    category = db.relationship(
        "CategoryModel", uselist=False, back_populates="category_type"
    )


class CategoryModel(Model, SerializerMixin):
    __tablename__ = "category"
    #
    id = db.Column(
        db.UUID,
        primary_key=True,
        default=uuid.uuid4,
    )

    # [RELASHIONSHIP]
    category_type_id = db.Column(
        db_uuid(), db.ForeignKey("category_type.id"), nullable=False, unique=True
    )
    category_type = db.relationship(
        "CategoryTypeModel", uselist=False, back_populates="category"
    )
