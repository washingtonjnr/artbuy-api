import inspect

#
from marshmallow import Schema


def load_json_schema(data: dict, schema: Schema):
    if hasattr(data, "json"):
        data = data.json

    if not data:
        data = {}

    if inspect.isclass(schema):
        return schema().load(data)
    else:
        return schema.load(data)


def update_object(obj, data):
    for field in data:
        value = data[field]
        if hasattr(obj, field):
            setattr(obj, field, value)
