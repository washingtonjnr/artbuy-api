def success(params: dict = {}, status_code: int = 200):
    response = {"success": True}

    response.update({"payload": params})

    return response, status_code


def error(params: dict = {}, status_code: int = 400):
    response = {"success": False}
    response.update({"errors": params})

    return response, status_code
