from common import const
from common import utils
from common import exception
from database.employee import Employee
from validation.decorator import json_validate
from validation import schema


class CommandAction(object):
    @classmethod
    def exit(cls, **args):
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
    def add(cls, client, **employee):
        """
        创建新员工
        :param client:
        :param employee:
        :return:
        """
        new_employee = Employee(**employee)
        # TODO json_validate处理时间格式
        new_eid = client.create(new_employee)
        print(const.CREATE_SUCCESS_MSG.format(eid=new_eid))
        return const.OK

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
        try:
            deleted_eid = client.delete(eid)
        except exception.EmployeeNotFoundException:  # eid不存在
            print(const.WRONG_EID_MSG)
            return const.FAILED
        print(const.DELETE_SUCCESS_MSG.format(eid=deleted_eid))
        return const.OK

    @classmethod
    def mod(cls, client, **employee):
        """
        更新操作
        :param client:
        :param employee:
        :return:
        """
        eid = employee.pop("eid")
        try:  # eid找不到
            origin_employee = client.get(eid)
        except exception.EmployeeNotFoundException:
            print(const.WRONG_EID_MSG)
            return const.FAILED
        origin_employee.update(**employee)
        mod_eid = client.update(eid, origin_employee)
        print(const.UPDATE_SUCCESS_MSG.format(eid=mod_eid))
        return const.OK

    @classmethod
    @json_validate(schema=schema.schema_get_employee)
    def get(cls, client, **employee):
        eid = employee["eid"]
        try:  # eid找不到
            employee = client.get(eid)
        except exception.EmployeeNotFoundException:
            print(const.WRONG_EID_MSG)
            return const.FAILED
        print(employee)
        return const.OK

    @classmethod
    @json_validate(schema=schema.schema_list_employees)
    def list(cls, client, **list_params):
        # TODO SORT EmployeeAttributes sortable_attrs
        client.list(**list_params)
        return const.OK
