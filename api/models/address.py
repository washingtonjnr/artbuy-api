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
    id: uuid.uuid4 = db.Column(
        db_uuid(), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    # About
    cep: str = db.Column(db.String(10), nullable=False)
    state: str = db.Column(db.String(50), nullable=False)
    street: str = db.Column(db.String(60), nullable=False)
    number: str = db.Column(db.String(10), nullable=False)
    country: str = db.Column(db.String(50), nullable=False)
    province: str = db.Column(db.String(50), nullable=False)
    complement: str = db.Column(db.String(50), nullable=False)
    neighborhood: str = db.Column(db.String(50), nullable=False)
    # Relationship
    user_id: uuid.uuid4 = db.Column(db_uuid(), db.ForeignKey("user.id"), nullable=False)
    user: Mapped["UserModel"] = db.relationship("UserModel")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.id:
            self.id = uuid.uuid4()

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
