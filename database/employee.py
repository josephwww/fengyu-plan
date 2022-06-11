import datetime

from common.const import ENTRY_DATE_FORMAT


class Employee:
    def __init__(self, name, department, position, entry_time):
        """
        初始化员工信息
        :param name:
        :param department:
        :param position:
        :param entry_time:
        """
        self.name = name
        self.department = department
        self.position = position
        self.entry_time = datetime.datetime.strptime(entry_time, ENTRY_DATE_FORMAT)

    def update(self, name=None, department=None, position=None, entry_time=None):
        """
        员工信息更新
        :param name:
        :param department:
        :param position:
        :param entry_time:
        :return:
        """
        if name:
            self.name = name
        if department:
            self.department = department
        if position:
            self.position = position
        if entry_time:
            self.entry_time = datetime.datetime.strptime(entry_time, ENTRY_DATE_FORMAT)

    def __str__(self) -> str:
        """
        重写员工字符串描述信息
        :return:
        """
        string = f"姓名：{self.name}，部门：{self.department}，职位：{self.position}，" \
                 f"入职时间：{self.entry_time.strftime(ENTRY_DATE_FORMAT)}"
        return string

    def __contains__(self, item):
        """
        重写contains方法，用来搜索员工信息
        :param item:
        :return:
        """
        if item in self.department or \
                item in self.position or \
                item in self.name:
            return True
        return False