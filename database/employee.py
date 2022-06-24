from common.const import ENTRY_DATE_FORMAT
from database.abstract_class import DatabaseObject


class Employee(DatabaseObject):
    def __init__(self, eid, name, department, position, entry_time):
        self.eid = eid
        self.name = name
        self.department = department
        self.position = position
        self.entry_time = entry_time

    def update(self, eid=None, name=None, department=None, position=None, entry_time=None):
        if eid:
            self.eid = eid
        if name:
            self.name = name
        if department:
            self.department = department
        if position:
            self.position = position
        if entry_time:
            self.entry_time = entry_time

    def __str__(self) -> str:
        """
        重写员工字符串描述信息
        :return:
        """
        string = f"工号：{self.eid}，姓名：{self.name}，部门：{self.department}，职位：{self.position}，" \
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
