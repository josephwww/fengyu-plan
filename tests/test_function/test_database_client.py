import unittest

from common import exception
from command.user_reader import Reader
from database.client import EmployeeClient
from tests.data import function_data as data


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.database_client = EmployeeClient()
        self.reader = Reader(self.database_client)

    def test_create_success(self):
        """
        正常场景：测试创建接口
        测试方法：通过接口执行添加操作
        期望结果：创建成功，数据库可查询到插入的员工id
        :return:
        """
        self.database_client.create(data.employee_1)
        self.assertTrue(data.employee_1.eid in self.database_client.database)

    def test_create_failed(self):
        """
        异常场景：测试创建接口传入数据库已经存在的员工id
        测试方法：通过接口执行添加操作
        期望结果：抛出员工id存在异常
        :return:
        """
        self.database_client.create(data.employee_1)
        self.assertTrue(data.employee_1.eid in self.database_client.database)
        self.assertRaises(exception.EmployeeIDFoundException, self.database_client.create, data.employee_1)

    def test_update_success(self):
        """
        正常场景：测试更新接口
        测试方法：通过接口执行添加操作后，更新已有员工信息
        期望结果：更新成功，数据库可查询到更新的员工id
        :return:
        """
        self.database_client.create(data.employee_1)
        self.assertTrue(data.employee_1.eid in self.database_client.database)
        self.database_client.update(data.employee_1.eid, data.employee_1_updated)
        self.assertTrue(data.employee_1.eid in self.database_client.database)

    def test_update_failed(self):
        """
        异常场景：测试更新接口传入数据库不存在的员工id
        测试方法：通过接口执行更新操作
        期望结果：抛出员工id找不到的异常
        :return:
        """
        self.database_client.create(data.employee_1)
        self.assertTrue(data.employee_1.eid in self.database_client.database)
        self.assertRaises(exception.EmployeeNotFoundException, self.database_client.update,
                          data.employee_2.eid, data.employee_2)

    def test_delete_success(self):
        """
        正常场景：测试删除接口
        测试方法：通过接口执行添加操作后，删除已有员工信息
        期望结果：删除成功，数据库查询不到更新的员工id
        :return:
        """
        self.database_client.create(data.employee_1)
        self.assertTrue(data.employee_1.eid in self.database_client.database)
        self.database_client.delete(data.employee_1.eid)
        self.assertTrue(data.employee_1.eid not in self.database_client.database)

    def test_delete_failed(self):
        """
        异常场景：测试删除接口传入数据库不存在的员工id
        测试方法：通过接口执行删除操作
        期望结果：抛出员工id找不到的异常
        :return:
        """
        self.database_client.create(data.employee_1)
        self.assertTrue(data.employee_1.eid in self.database_client.database)
        self.assertRaises(exception.EmployeeNotFoundException, self.database_client.delete, data.employee_2.eid)

    def test_get_success(self):
        """
        正常场景：测试详情接口
        测试方法：通过接口执行添加操作后，查询已有员工信息详情
        期望结果：查询成功，数据库可查询的员工信息与插入的相符
        :return:
        """
        self.database_client.create(data.employee_1)
        self.assertTrue(data.employee_1.eid in self.database_client.database)
        employee_info = self.database_client.get(data.employee_1.eid)
        self.assertEqual(employee_info, data.employee_1)

    def test_get_failed(self):
        """
        异常场景：测试详情接口传入数据库不存在的员工id
        测试方法：通过接口执行详情操作
        期望结果：抛出员工id找不到的异常
        :return:
        """
        self.assertRaises(exception.EmployeeNotFoundException, self.database_client.get, data.employee_1.eid)

    def test_list_success(self):
        """
        正常场景：测试列表接口
        测试方法：通过接口执行添加操作后，查询已有员工信息列表
        期望结果：查询成功，接口返回信息与插入的一致
        :return:
        """
        self.database_client.create(data.employee_1)
        self.assertTrue(data.employee_1.eid in self.database_client.database)
        self.database_client.create(data.employee_2)
        self.assertTrue(data.employee_2.eid in self.database_client.database)
        employee_list = self.database_client.list()
        self.assertEqual(len(employee_list), 2)
        self.assertTrue(data.employee_1 in employee_list and data.employee_2 in employee_list)


if __name__ == '__main__':
    unittest.main()
