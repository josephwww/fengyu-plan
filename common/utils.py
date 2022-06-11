from common import const
from common.const import SupportedCommand
from common.const import Modifiable
from common.exception import EmployeeNotFoundException
from database.employee import Employee


def show_help():
    """
    展示帮助信息
    :return:
    """
    print("使用方法：")
    print("1. 展示当前员工列表： show all")
    print("2. 创建新员工信息： add <姓名> <部门> <职位> <入职时间>")
    print("如：>> add Zhangsan CMP Python开发 2022-01-01")
    print("3. 更新员工信息： mod <员工id> <更新字段> <更新内容>")
    print("支持更新的字段有： 姓名： name，部门：department, 职位：position，入职时间：entry_time")
    print("如：>> mod 1 name LiSi department VT")
    print("4. 删除员工信息：delete <员工id>")
    print("如：>> delete 1")
    print("5. exit：退出程序")


def get_command(client):
    """
    展示指令信息，并接收用户指令
    :param client: 数据库客户端调用
    :return:
    """
    cmd = input(const.PROMPT_MSG)
    parse_command(cmd, client)


def parse_command(cmd_text, client):
    """
    解析用户输入命令
    :param cmd_text:
    :param client:
    :return:
    """
    cmd_list = cmd_text.split()
    if not cmd_list:
        retry(const.DEFAULT_ERROR_MSG, client)
        return
    cmd = cmd_list[0]
    if cmd not in SupportedCommand.get_values():
        retry(const.CUSTOM_ERROR_MSG.format(cmd=cmd), client)
        return
    cmd_action = getattr(CommandAction, cmd)
    cmd_action(client, *cmd_list[1:])
    get_command(client)


def retry(msg, client):
    """
    打印错误信息并重新获取用户输入
    :param msg:
    :param client:
    :return:
    """
    print(msg)
    show_help()
    get_command(client)


class CommandAction:
    @classmethod
    def exit(cls, *args):
        exit()

    @classmethod
    def help(cls, *args):
        """
        展示帮助信息
        :param args:
        :return:
        """
        show_help()
        return const.OK

    @classmethod
    def show(cls, client, *args):
        """
        展示员工列表
        :param client:
        :param args:
        :return:
        """
        if len(args) != 1 or args[0] != "all":
            retry(const.DEFAULT_ERROR_MSG, client)
            return const.FAILED
        client.list()
        return const.OK

    @classmethod
    def add(cls, client, *employee):
        """
        创建新员工
        :param client:
        :param employee:
        :return:
        """
        if len(employee) != 4:  # 检查参数数量
            retry(const.DEFAULT_ERROR_MSG, client)
            return const.FAILED
        name, department, position, entry_time = employee
        try:
            new_employee = Employee(name, department, position, entry_time)
        except ValueError:
            # 处理时间格式错误问题
            retry(const.WRONG_ENTRY_TIME_MSG, client)
            return const.FAILED
        new_eid = client.create(new_employee)
        print(const.CREATE_SUCCESS_MSG.format(eid=new_eid))
        return const.OK

    @classmethod
    def delete(cls, client, *employee):
        """
        删除用户
        :param client:
        :param employee:
        :return:
        """
        if len(employee) != 1:
            retry(const.DEFAULT_ERROR_MSG, client)
            return const.FAILED

        if not employee[0].isdigit():  # eid不为数字
            retry(const.WRONG_EID_MSG, client)
            return const.FAILED
        eid = int(employee[0])
        try:
            deleted_eid = client.delete(eid)
        except EmployeeNotFoundException:  # eid不存在
            retry(const.WRONG_EID_MSG, client)
            return const.FAILED
        print(const.DELETE_SUCCESS_MSG.format(eid=deleted_eid))
        return const.OK

    @classmethod
    def mod(cls, client, *employee):
        """
        更新操作
        :param client:
        :param employee:
        :return:
        """
        if not employee:  # 空命令
            retry(const.DEFAULT_ERROR_MSG, client)
            return const.FAILED
        eid = employee[0]
        if not eid.isdigit():  # eid不为数字
            retry(const.WRONG_EID_MSG, client)
            return const.FAILED
        eid = int(eid)
        employee = employee[1:]
        if not employee or len(employee) % 2 != 0:  # 命令不规范
            retry(const.CUSTOM_ERROR_MSG.format(cmd="".join(employee)), client)
            return const.FAILED
        try:  # eid找不到
            origin_employee = client.get(eid)
        except EmployeeNotFoundException:
            retry(const.WRONG_EID_MSG, client)
            return const.FAILED
        while employee:  # 循环处理命令
            title, content = employee[:2]
            if title not in Modifiable.get_values():  # 字段不可更新
                retry(const.CUSTOM_ERROR_MSG.format(cmd=title), client)
                return const.FAILED
            try:  # 处理时间格式错误
                origin_employee.update(**{title: content})
            except ValueError:
                retry(const.WRONG_ENTRY_TIME_MSG, client)
                return const.FAILED
            employee = employee[2:]
        mod_eid = client.update(eid, origin_employee)
        print(const.UPDATE_SUCCESS_MSG.format(eid=mod_eid))
        return const.OK
