import unittest

from common import const
from command.user_reader import Reader
from database.client import EmployeeClient
from tests.data import cmd_data as data


class TestNormal(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.database_client = EmployeeClient()
        self.reader = Reader(self.database_client)

    def test_parser(self):
        """
        正常场景：测试parser正常工作
        测试方法：通过help语句获取命令帮助
        期望结果：执行成功，命令返回成功字段
        :return:
        """
        self.reader.cmd = "help"
        self.assertEqual(const.OK, self.reader.parse_command())

    def test_add_success(self):
        """
        正常场景：测试数据正常添加
        测试方法：通过命令语句执行添加员工操作
        期望结果：添加成功，client数据库中可查询到员工id
        :return:
        """
        self.reader.cmd = data.add_success_cmd
        self.reader.parse_command()
        self.assertTrue(data.eid in self.database_client.database)

    def test_mod_success(self):
        """
        正常场景：测试正常修改员工数据
        测试方法：通过命令语句执行更新员工信息操作
        期望结果：更新成功，client数据库中可查询到更新后的信息
        :return:
        """
        self.reader.cmd = data.add_success_cmd
        self.reader.parse_command()
        self.reader.cmd = data.mod_success_cmd
        self.reader.parse_command()
        self.assertEqual(data.mod_name, self.database_client.database.get(data.eid).name)

    def test_delete_success(self):
        """
        正常场景：测试正常删除员工数据
        测试方法：通过命令语句执行删除员工信息操作
        期望结果：删除成功，client数据库中查询不到删除后的员工id
        :return:
        """
        self.reader.cmd = data.add_success_cmd
        self.reader.parse_command()
        self.assertTrue(data.eid in self.database_client.database)
        self.reader.cmd = data.delete_success_cmd
        self.reader.parse_command()
        self.assertTrue(data.eid not in self.database_client.database)

    def test_get_success(self):
        """
        正常场景：测试正常获取员工详情
        测试方法：通过命令语句执行详情操作
        期望结果：获取详情成功
        :return:
        """
        self.reader.cmd = data.add_success_cmd
        self.reader.parse_command()
        self.assertTrue(data.eid in self.database_client.database)
        self.reader.cmd = data.get_success_cmd
        employee = self.reader.parse_command()
        self.assertEqual(employee.name, data.name)

    def test_list_success(self):
        """
        正常场景：测试正常获取员工列表
        测试方法：通过命令语句执行列表操作
        期望结果：获取排序列表成功
        :return:
        """
        self.reader.cmd = data.list_success_cmd
        list_return = self.reader.parse_command()
        self.assertEqual(list(), list_return)

    def test_list_paging_success(self):
        """
        正常场景：测试正常获取员工列表并分页
        测试方法：通过命令语句执行列表操作
        期望结果：获取排序列表成功，且分页结果为期望值
        :return:
        """
        self.reader.cmd = data.add_success_cmd
        self.reader.parse_command()
        self.assertTrue(data.eid in self.database_client.database)
        self.reader.cmd = data.list_paging_success_cmd
        list_return = self.reader.parse_command()
        self.assertEqual(list(), list_return)

    def test_list_search_success(self):
        """
        正常场景：测试正常获取员工列表并支持搜索
        测试方法：通过命令语句执行列表操作
        期望结果：获取排序列表成功，且搜索结果长度与期望一致
        :return:
        """
        self.reader.cmd = data.add_success_cmd
        self.reader.parse_command()
        self.assertTrue(data.eid in self.database_client.database)
        self.reader.cmd = data.list_search_success_cmd
        list_return = self.reader.parse_command()
        self.assertEqual(1, len(list_return))

    def test_list_sort_success(self):
        """
        正常场景：测试正常获取员工列表并排序
        测试方法：通过命令语句执行列表操作
        期望结果：获取排序列表成功，且首元素排序字段为期望值
        :return:
        """
        self.reader.cmd = data.add_success_cmd
        self.reader.parse_command()
        self.reader.cmd = data.add_department_success_cmd
        self.reader.parse_command()
        self.assertTrue(data.eid in self.database_client.database)
        self.reader.cmd = data.list_sort_success_cmd
        list_return = self.reader.parse_command()
        self.assertEqual(list_return[0].department, data.first_department)


if __name__ == "__main__":
    unittest.main()
