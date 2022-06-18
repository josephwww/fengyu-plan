from jsonschema import validate, ValidationError
from common import const


# data参数校验装饰器
def json_validate(schema):
    def wrapper(func):
        def inner(cmd_class, client, **kwargs):
            try:
                # validate(data, schema)
                pass
            except ValidationError as e:
                print("参数校验失败：{}!".format(e.message))
                return const.FAILED
            else:
                return func(cmd_class, client, **kwargs)
        return inner
    return wrapper
