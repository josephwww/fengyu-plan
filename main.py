from common.utils import get_command
from database.client import Client


if __name__ == "__main__":
    database_client = Client()  # 初始化数据库
    get_command(database_client)  # 命令行接收命令
