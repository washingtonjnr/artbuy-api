from typing import Union, Mapping, Iterable, Any, List, Dict

# Key used for schema-level validation errors
SCHEMA = "_schema"


class CustomHttpException(Exception):
    def __init__(
        self,
        message,
        error,
        status_code=400,
        extra_information={},
        *args,
        **kwargs,
    ):
        super().__init__(message)

        if extra_information is None:
            extra_information = dict()

        self.message = message
        self.error = error
        self.status_code = status_code

        self.extra_information = extra_information


# -- EXCEPTIONS [400]


# 401
class NotAuthorized(CustomHttpException):
    def __init__(self, message: str = None):
        message = message or "No authorized"
        error = "NOT_AUTHORIZED"
        status_code = 401

        super().__init__(message, error, status_code=status_code)


# 403
class NotPermission(CustomHttpException):
    def __init__(self, message: str = None):
        message = message or "No permission"
        error = "NOT_AUTHORIZED"
        status_code = 403

        super.__init__(message, error, status_code=status_code)


# 400
class NotFound(CustomHttpException):
    def __init__(self, message: str = None):
        message = message or "Not found"
        error = "NOT_FOUND"
        status_code = 400

        super.__init__(message, error, status_code=status_code)


# 400
class InvalidCredentials(CustomHttpException):
    def __init__(self):
        message = "Email or password invalids"
        error = "INVALID_CREDENTIALS"

        super().__init__(message, error)
