import re

# Libs
from validate_docbr import CPF

# Utils
from api.utils.parsers import remove_nom_numeric_chars


# TEXT
def validate_empty(text: str):
    if not text:
        return True

    return text.strip()


# CPF
def validate_cpf(cpf: str):
    cpf_validator = CPF()
    cpf = remove_nom_numeric_chars(cpf or "")

    if not cpf:
        return True

    return cpf_validator.validate(cpf)


# CEP
def validate_cep(cep: str):
    if not cep:
        return True

    return cep.isdigit() or len(cep) != 8


# EMAIL
def validate_email(email: str):
    if not email:
        return True

    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None


# PHONE
def validate_phone(phone: str):
    if not phone:
        return True

    if len(phone) > 3 and phone.startswith("+"):
        return True

    return False


# PASSWORD
def validate_password(password: str):
    if not password:
        return True

    if (
        len(password) < 8
        or not re.match(r".*[A-Z]+.*", password)
        or not re.match(r".*[0-9]+.*", password)
        or not re.match(r".*[a-z]+.*", password)
    ):
        return False

    return True
