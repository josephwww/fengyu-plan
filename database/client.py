from common import exception
from common.const import ASC
from database.employee import Employee
from database.abstract_class import Client


class EmployeeClient(Client):
    def __init__(self):
        self.database = dict()

    def create(self, employee: Employee):
        if employee.eid in self.database:
            raise exception.EmployeeIDFoundException
        self.database[employee.eid] = employee
        return employee.eid

    def update(self, eid, employee: Employee):
        if eid not in self.database:
            raise exception.EmployeeNotFoundException
        self.database[eid] = employee
        return eid

    def delete(self, eid):
        if eid not in self.database:
            raise exception.EmployeeNotFoundException
        del self.database[eid]
        return eid

    def get(self, eid):
        if eid not in self.database:
            raise exception.EmployeeNotFoundException
        return self.database[eid]

    def list(self, start=0, limit=None, sort="eid", direct=ASC, search=None):
        """
        员工信息列表接口
        :param start: 分页起始参数
        :param limit: 分页数量参数
        :param sort: 排序字段
        :param direct: 排序方向
        :param search: 搜索字段
        :return: 数据库实例的数组
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
