import logging

from common import const
from common import utils
from database.employee import Employee
from common.utils import print_util
from validation.decorator import json_validate
from validation import schema


logger = logging.getLogger(__name__)


class CommandAction(object):
    @classmethod
    def exit(cls, client, **args):
        exit()

    @classmethod
    def help(cls, client, **args):
        """
        展示帮助信息
        :param args:
        :return:
        """
        utils.show_help()
        return const.OK

    @classmethod
    @json_validate(schema=schema.schema_add_employee)
    def add(cls, client, **employee):
        """
        创建新员工
        :param client:
        :param employee:
        :return:
        """
        new_employee = Employee(**employee)
        client.create(new_employee)
        logger.info("create user {} success".format(new_employee))
        return new_employee.eid

    @classmethod
    @json_validate(schema=schema.schema_delete_employee)
    def delete(cls, client, **employee):
        """
        删除用户
        :param client:
        :param employee:
        :return:
        """
        eid = employee.pop("eid")
        deleted_eid = client.delete(eid)
        logger.info("delete user {} success".format(deleted_eid))
        return deleted_eid

    @classmethod
    @json_validate(schema=schema.schema_mod_employee)
    def mod(cls, client, **employee):
        """
        更新操作
        :param client:
        :param employee:
        :return:
        """
        eid = employee.pop("eid")
        origin_employee = client.get(eid)
        origin_employee.update(**employee)
        updated_id = client.update(eid, origin_employee)
        logger.info("update eid {}: {} success".format(eid, origin_employee))
        return updated_id

    @classmethod
    @print_util
    @json_validate(schema=schema.schema_get_employee)
    def get(cls, client, **employee):
        eid = employee.get("eid")
        return client.get(eid)

    @classmethod
    @print_util
    @json_validate(schema=schema.schema_list_employees)
    def list(cls, client, **list_params):
        return client.list(**list_params)
