from common import parser
from database.client import Client


if __name__ == "__main__":
    database_client = Client()  # 初始化数据库
    parser = parser.Parser(database_client)  # 命令行接收命令
