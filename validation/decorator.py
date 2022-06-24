from jsonschema import validate, ValidationError
from common import exception


# data参数校验装饰器
def json_validate(schema):
    def wrapper(func):
        def inner(cmd_class, client, **params):
            try:
                validate(params, schema)
                pass
            except ValidationError:
                raise exception.WrongParamException
            return func(cmd_class, client, **params)
        return inner
    return wrapper
