import unittest

from common import exception
from command.user_reader import Reader
from database.client import EmployeeClient
from tests.data import cmd_data as data


class TestNormal(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.database_client = EmployeeClient()
        self.reader = Reader(self.database_client)

    def test_add_duplicate_eid(self):
        """
        异常场景：测试创建接口传入数据库已经存在的员工id
        测试方法：通过命令语句重复执行添加操作
        期望结果：操作失败，返回员工已存在的错误信息
        :return:
        """
        self.reader.cmd = data.add_success_cmd
        self.reader.parse_command()
        self.assertTrue(data.eid in self.database_client.database)
        self.reader.cmd = data.add_success_cmd
        exec_msg = self.reader.parse_command()
        self.assertEqual(exec_msg, exception.EmployeeIDFoundException.msg)

    def test_add_wrong_format_entry_time(self):
        """
        异常场景：测试创建接口使用不支持的字段排序
        测试方法：通过命令语句执行列表操作
        期望结果：操作失败，返回参数错误信息
        :return:
        """
        self.reader.cmd = data.add_wrong_format_entry_time_cmd
        exec_msg = self.reader.parse_command()
        self.assertEqual(exec_msg, exception.CommandNotSupportedException.msg)

    def test_add_wrong_arguments(self):
        """
        异常场景：测试创建接口使用错误的参数
        测试方法：通过错误参数的命令语句执行创建操作
        期望结果：操作失败，返回参数错误信息
        :return:
        """
        self.reader.cmd = data.add_wrong_arguments_cmd
        exec_msg = self.reader.parse_command()
        self.assertEqual(exec_msg, exception.CommandNotSupportedException.msg)

    def test_add_insufficient_arguments(self):
        """
        异常场景：测试创建接口参数数量不正确
        测试方法：通过参数数量不正确的命令语句执行创建操作
        期望结果：操作失败，返回参数错误信息
        :return:
        """
        self.reader.cmd = data.add_insufficient_arguments_cmd
        exec_msg = self.reader.parse_command()
        self.assertEqual(exec_msg, exception.CommandNotSupportedException.msg)

    def test_mod_wrong_format_entry_time(self):
        """
        异常场景：测试更新接口使用错误格式的时间参数
        测试方法：通过错误格式的时间参数的命令语句执行更新操作
        期望结果：操作失败，返回参数错误信息
        :return:
        """
        self.reader.cmd = data.add_success_cmd
        self.reader.parse_command()
        self.reader.cmd = data.mod_wrong_format_entry_time_cmd
        exec_msg = self.reader.parse_command()
        self.assertEqual(exec_msg, exception.CommandNotSupportedException.msg)

    def test_mod_wrong_arguments(self):
        """
        异常场景：测试更新接口使用错误的参数
        测试方法：通过错误的参数的命令语句执行更新操作
        期望结果：操作失败，返回参数错误信息
        :return:
        """
        self.reader.cmd = data.add_success_cmd
        self.reader.parse_command()
        self.reader.cmd = data.mod_wrong_arguments_cmd
        exec_msg = self.reader.parse_command()
        self.assertEqual(exec_msg, exception.CommandNotSupportedException.msg)

    def test_mod_insufficient_arguments(self):
        """
        异常场景：测试更新接口未使用eid参数
        测试方法：通过错误的参数的命令语句执行更新操作
        期望结果：操作失败，返回参数错误信息
        :return:
        """
        self.reader.cmd = data.add_success_cmd
        self.reader.parse_command()
        self.reader.cmd = data.mod_insufficient_arguments_cmd
        exec_msg = self.reader.parse_command()
        self.assertEqual(exec_msg, exception.CommandNotSupportedException.msg)

    def test_delete_non_exist_eid(self):
        """
        异常场景：测试删除接口使用不存在的员工id参数
        测试方法：通过不存在的员工id参数的命令语句执行删除操作
        期望结果：操作失败，返回员工不存在的错误信息
        :return:
        """
        self.reader.cmd = data.delete_non_exist_eid_cmd
        exec_msg = self.reader.parse_command()
        self.assertEqual(exec_msg, exception.EmployeeNotFoundException.msg)

    def test_delete_wrong_arguments(self):
        """
        异常场景：测试删除接口使用错误的参数
        测试方法：通过错误参数命令语句执行删除操作
        期望结果：操作失败，返回参数错误信息
        :return:
        """
        self.reader.cmd = data.delete_wrong_arguments_cmd
        exec_msg = self.reader.parse_command()
        self.assertEqual(exec_msg, exception.CommandNotSupportedException.msg)

    def test_list_wrong_arguments(self):
        """
        异常场景：测试列表接口使用错误的参数
        测试方法：通过命令语句执行列表操作
        期望结果：操作失败，返回参数错误信息
        :return:
        """
        self.reader.cmd = data.list_wrong_arguments_cmd
        exec_msg = self.reader.parse_command()
        self.assertEqual(exec_msg, exception.CommandNotSupportedException.msg)

    def test_get_insufficient_arguments(self):
        """
        异常场景：测试详情接口未传足够的参数
        测试方法：通过命令语句执行详情操作
        期望结果：操作失败，返回参数错误信息
        :return:
        """
        self.reader.cmd = data.get_insufficient_arguments
        exec_msg = self.reader.parse_command()
        self.assertEqual(exec_msg, exception.CommandNotSupportedException.msg)

    def test_get_non_exist_eid(self):
        """
        异常场景：测试详情接口使用不存在的员工id
        测试方法：通过命令语句执行详情操作
        期望结果：操作失败，返回员工id不存在信息
        :return:
        """
        self.reader.cmd = data.get_non_exist_eid
        exec_msg = self.reader.parse_command()
        self.assertEqual(exec_msg, exception.EmployeeNotFoundException.msg)

    def test_list_unsortable_attributes(self):
        """
        异常场景：测试列表接口使用不支持的字段排序
        测试方法：通过命令语句执行列表操作
        期望结果：操作失败，返回参数错误信息
        :return:
        """
        self.reader.cmd = data.list_unsortable_attributes
        exec_msg = self.reader.parse_command()
        self.assertEqual(exec_msg, exception.WrongParamException.msg)
