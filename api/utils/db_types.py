import sys

#
from sqlalchemy.dialects.postgresql import UUID

#
from api.ext.database import db


def db_uuid():
    return UUID(as_uuid=True)
