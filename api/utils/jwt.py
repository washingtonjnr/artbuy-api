import uuid
from datetime import timedelta

#
from flask import current_app
from flask_jwt_extended.utils import create_refresh_token, create_access_token


def encode_jwt_token(
    id: uuid = None,
    permissions=["*"],
    expire_delta: timedelta = None,
    refresh_expire_delta: timedelta = None,
    identity_extra: dict = None,
):
    identity = dict(id=str(id))

    if identity_extra:
        identity.update(identity_extra)

    if not expire_delta:
        expire_delta = timedelta(hours=8)

    if not refresh_expire_delta:
        refresh_expire_delta = timedelta(days=2)

    token = create_access_token(
        identity,
        expires_delta=expire_delta,
        additional_claims={"permissions": permissions},
    )

    refresh = create_refresh_token(
        identity,
        expires_delta=refresh_expire_delta,
        additional_claims={"permissions": permissions},
    )

    return token, refresh
