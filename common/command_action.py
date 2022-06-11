from common import const
from common import utils
from common import exception
from database.employee import Employee
from validation.decorator import json_validate
from validation import schema


class CommandAction(object):
    @classmethod
    def exit(cls, args):
        exit()

    @classmethod
    def help(cls, args):
        """
        展示帮助信息
        :param args:
        :return:
        """
        utils.show_help()
        return const.OK

    @classmethod
    def add(cls, client, employee):
        """
        创建新员工
        :param client:
        :param employee:
        :return:
        """
        if len(employee) != const.ADD_COMMAND_LIMIT:  # 检查参数数量
            print(const.DEFAULT_ERROR_MSG)
            return const.FAILED
        eid, name, department, position, entry_time = employee
        try:
            new_employee = Employee(eid, name, department, position, entry_time)
        except ValueError:
            # 处理时间格式错误问题
            print(const.WRONG_ENTRY_TIME_MSG)
            return const.FAILED
        new_eid = client.create(new_employee)
        print(const.CREATE_SUCCESS_MSG.format(eid=new_eid))
        return const.OK

    @classmethod
    @json_validate(schema=schema.schema_delete_employee)
    def delete(cls, client, employee):
        """
        删除用户
        :param client:
        :param employee:
        :return:
        """
        if len(employee) != const.DELETE_COMMAND_LIMIT:
            print(const.DEFAULT_ERROR_MSG)
            return const.FAILED

        eid = employee[0]
        try:
            deleted_eid = client.delete(eid)
        except exception.EmployeeNotFoundException:  # eid不存在
            print(const.WRONG_EID_MSG)
            return const.FAILED
        print(const.DELETE_SUCCESS_MSG.format(eid=deleted_eid))
        return const.OK

    @classmethod
    def mod(cls, client, employee):
        """
        更新操作
        :param client:
        :param employee:
        :return:
        """
        if not employee:  # 空命令
            print(const.DEFAULT_ERROR_MSG)
            return const.FAILED
        eid = employee[0]
        employee = employee[1:]
        # TODO: 用arg_parse替代
        if not employee or len(employee) % 2 != 0:  # 命令不规范
            print(const.CUSTOM_ERROR_MSG.format(cmd="".join(employee)))
            return const.FAILED
        try:  # eid找不到
            origin_employee = client.get(eid)
        except exception.EmployeeNotFoundException:
            print(const.WRONG_EID_MSG)
            return const.FAILED
        while employee:  # 循环处理命令
            title, content = employee[:2]
            if title not in const.EmployeeAttributes.get_values():  # 字段不可更新
                print(const.CUSTOM_ERROR_MSG.format(cmd=title))
                return const.FAILED
            try:  # 处理时间格式错误
                origin_employee.update(**{title: content})
            except ValueError:
                print(const.WRONG_ENTRY_TIME_MSG)
                return const.FAILED
            employee = employee[2:]
        mod_eid = client.update(eid, origin_employee)
        print(const.UPDATE_SUCCESS_MSG.format(eid=mod_eid))
        return const.OK

    @classmethod
    @json_validate(schema=schema.schema_get_employee)
    def get(cls, client, args):
        eid = args[0]
        try:  # eid找不到
            employee = client.get(eid)
        except exception.EmployeeNotFoundException:
            print(const.WRONG_EID_MSG)
            return const.FAILED
        print(employee)
        return const.OK

    @classmethod
    @json_validate(schema=schema.schema_list_employees)
    def list(cls, client, list_params):
        params = {}
        while list_params:  # 循环处理命令
            param, value = list_params[:2]
            if param not in const.ListParams.get_values():
                print(const.CUSTOM_ERROR_MSG.format(cmd=param))
                return const.FAILED
            if param == const.ListParams.SORT and value not in const.EmployeeAttributes.sortable_attrs():
                print(const.CUSTOM_ERROR_MSG.format(cmd=value))
                return const.FAILED
            params[param] = value
            list_params = list_params[2:]

        client.list(**params)
        return const.OK
