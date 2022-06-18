from common import parser
from database.client import EmployeeClient


if __name__ == "__main__":
    database_client = EmployeeClient()  # 初始化数据库
    parser = parser.Parser(database_client)  # 命令行接收命令
