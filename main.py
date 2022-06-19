from common import config
from common import cmd_reader
from database.client import EmployeeClient
import logging

if __name__ == "__main__":
    logging.basicConfig(filename=config.LOG_FILE, level=config.LOG_LEVEL)
    database_client = EmployeeClient()  # 初始化数据库
    cmd_reader.Reader(database_client)  # 命令行接收命令
