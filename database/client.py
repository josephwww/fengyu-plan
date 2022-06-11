from database.employee import Employee
from common.exception import EmployeeNotFoundException
from common.const import ASC
from common.const import EMPTY_DATABASE_MSG
from common.const import EMPLOYEE_INFO


class Client:
    def __init__(self):
        self.database = dict()
        self.max_eid = 1

    def create(self, employee: Employee):
        """
        员工信息创建接口
        :param employee:
        :return:
        """
        eid = self.max_eid
        self.database[eid] = employee
        self.max_eid += 1
        return eid

    def update(self, eid, employee: Employee):
        """
        员工信息更新接口
        :param eid:
        :param employee:
        :return:
        """
        if eid not in self.database:
            raise EmployeeNotFoundException
        self.database[eid] = employee
        return eid

    def delete(self, eid):
        """
        员工信息删除接口
        :param eid:
        :return:
        """
        if eid not in self.database:
            raise EmployeeNotFoundException
        del self.database[eid]
        return eid

    def get(self, eid):
        """
        员工信息详情接口
        :param eid:
        :return:
        """
        if eid not in self.database:
            raise EmployeeNotFoundException
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
        edata = list(self.database.items())
        # 搜索
        if search:
            edata = [(eid, employee) for eid, employee in edata if search in employee]
        # 排序
        if sort:
            reverse = False if direct == ASC else True
            if sort == "eid":
                edata.sort(key=lambda x: x[0], reverse=reverse)
            else:
                edata.sort(key=lambda x: getattr(x[1], sort), reverse=reverse)
        # 分页
        edata = edata[start:]
        if limit:
            edata = edata[:limit]
        self.print_employee_list(edata)

    @staticmethod
    def print_employee_list(edata):
        """
        格式化输出员工信息
        :param edata:
        :return:
        """
        if not edata:
            print(EMPTY_DATABASE_MSG)
        for eid, employee in edata:
            print(EMPLOYEE_INFO.format(eid=eid, employee=employee))