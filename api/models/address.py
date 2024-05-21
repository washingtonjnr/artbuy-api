import uuid

# Libs
from sqlalchemy.orm import Mapped
from sqlalchemy_serializer import SerializerMixin

# Ext
from api.ext.database import db

# Model
from api.models.user import UserModel

# Utils
from api.utils.db_types import db_uuid

Model = db.Model


class AddressModel(Model, SerializerMixin):
    __tablename__ = "address"
    #
    serialize_rules = ("-user",)
    #
    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    #
    cep = db.Column(db.String(10), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(60), nullable=False)
    number = db.Column(db.String(10), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    province = db.Column(db.String(50), nullable=False)
    complement = db.Column(db.String(50), nullable=False)
    neighborhood = db.Column(db.String(50), nullable=False)
    # [RELASHIONSHIP]
    user_id = db.Column(
        db.UUID, db.ForeignKey("user.id", use_alter=True), nullable=False, unique=True
    )
    user = db.relationship("UserModel")

    def json(self):
        return {
            "cep": self.cep,
            "state": self.state,
            "street": self.street,
            "number": self.number,
            "country": self.country,
            "province": self.province,
            "complement": self.complement,
            "neighborhood": self.neighborhood,
        }

    # Method to save user to DB
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
