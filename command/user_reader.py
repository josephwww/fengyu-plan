from common import const
from command.base import CMD


class Reader(object):
    """
    命令行解析类，获取用户输入并执行解析和操作
    """
    def __init__(self, client):
        self.cmd = None
        self.client = client
        print(const.INITIAL_MSG)

    def get_command(self):
        self.cmd = input(const.PROMPT_MSG)
        self.parse_command()
        self.get_command()

    def parse_command(self):
        try:
            cmd = CMD(self.cmd)
            result = cmd.action(self.client, **cmd.options)
        except Exception as e:
            print(e.msg)
            return e.msg
        else:
            print(const.OK)
            return result
