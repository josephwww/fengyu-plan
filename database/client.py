from database.employee import Employee
from database.abstract_class import Client
from common import exception
from common.const import ASC
from common.const import EMPTY_DATABASE_MSG


class EmployeeClient(Client):
    def __init__(self):
        self.database = dict()

    def create(self, employee: Employee):
        """
        员工信息创建接口
        :param employee:
        :return:
        """
        if employee.eid in self.database:
            raise exception.EmployeeIDFoundException
        self.database[employee.eid] = employee
        return employee.eid

    def update(self, eid, employee: Employee):
        """
        员工信息更新接口
        :param eid:
        :param employee:
        :return:
        """
        if eid not in self.database:
            raise exception.EmployeeNotFoundException
        self.database[eid] = employee
        return eid

    def delete(self, eid):
        """
        员工信息删除接口
        :param eid:
        :return:
        """
        if eid not in self.database:
            raise exception.EmployeeNotFoundException
        del self.database[eid]
        return eid

    def get(self, eid):
        """
        员工信息详情接口
        :param eid:
        :return:
        """
        if eid not in self.database:
            raise exception.EmployeeNotFoundException
        return self.database[eid]

    def list(self, start=0, limit=None, sort="eid", direct=ASC, search=None):
        """
        员工信息列表接口
        :param start:
        :param limit:
        :param sort:
        :param direct:
        :param search:
        :return:
        """
        edata = list(self.database.values())
        # 搜索
        if search:
            edata = [employee for employee in edata if search in employee]
        # 排序
        if sort:
            reverse = False if direct == ASC else True
            edata.sort(key=lambda x: getattr(x, sort), reverse=reverse)
        # 分页
        edata = edata[start:]
        if limit:
            edata = edata[:limit]
        return edata
