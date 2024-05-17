import uuid
from enum import Enum

# Libs
from sqlalchemy_serializer import SerializerMixin
from flask_jwt_extended.utils import get_jwt_identity

# Ext
from api.ext.database import db

# Models
from api.models.file import FileModel

# Utils
from api.utils.db_types import db_uuid
from api.utils.exceptions import NotFound
from api.utils.jwt import encode_jwt_token


Model = db.Model


# Used in find_user* classmethod
class UserModelAttributes(Enum):
    ID = "id"
    NAME = "name"
    EMAIL = "email"
    CPF = "cpf"


class UserModel(Model, SerializerMixin):
    __tablename__ = "user"
    #
    id: uuid.uuid4 = db.Column(
        db_uuid(), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    cpf = db.Column(db.String(11), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    is_enabled = db.Column(db.Boolean, default=True)
    is_private = db.Column(db.Boolean, default=False)
    # relationship
    address = db.relationship("AddressModel", uselist=False, back_populates="user")
    # TODO: add avatar
    # avatar_id: uuid.uuid4 = db.Column(
    #     db_uuid(), db.ForeignKey("file.id"), nullable=True
    # )
    # avatar = db.relationship("FileModel")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.id:
            self.id = uuid.uuid4()

    # Using it in return
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "cpf": self.cpf,
            "is_private": self.is_private,
        }

    def auth_response(self) -> dict:
        token, refresh = encode_jwt_token(
            id=self.id,
        )

        data = {
            "access_token": token,
            "refresh_token": refresh,
        }

        return data

    # Method to save user to DB
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # Method to remove user
    def remove_from_db(self):
        db.session.delete(self)
        db.session.commit()

    # [AUX QUERY FILTER] Class method which find users by attribute
    @classmethod
    def find_users_by_attribute(cls, attribute: UserModelAttributes, value: None):
        """
        Args:
          attribute (UserModelAttributes): The parameter by which users should be filtered.
          value: The value of the parameter by which users should be filtered.
        """

        if attribute not in UserModelAttributes:
            raise ValueError("Attribute not found")

        # Convert enum attribute to its string representation
        attribute_str = attribute.value

        return cls.query.filter_by(**{attribute_str: value}).all()

    # [AUX QUERY FILTER] Class method which find user by attribute
    @classmethod
    def find_user_by_attribute(cls, attribute: UserModelAttributes, value: None):
        """
        Args:
          attribute (UserModelAttributes): The parameter by which users should be filtered.
          value: The value of the parameter by which users should be filtered.
        """

        if attribute not in UserModelAttributes:
            raise ValueError("Attribute not found")

        # Convert enum attribute to its string representation
        attribute_str = attribute.value

        return cls.query.filter_by(**{attribute_str: value}).first()

    # Class method which find user by JWT
    @classmethod
    def get_session_user(cls) -> "UserModel":
        identity = get_jwt_identity()

        user_id = identity["id"]
        user = UserModel.find_user_by_attribute(
            attribute=UserModelAttributes.ID, value=user_id
        )

        if not user:
            raise NotFound("User not found")

        return user
