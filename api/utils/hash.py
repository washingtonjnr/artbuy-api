import hashlib


def sha512(s):
    m = hashlib.sha512()
    m.update(s.encode())

    return m.hexdigest()
