from common import const
from common import utils
from common.command import CMD


class Reader(object):
    def __init__(self, client):
        self.cmd = None
        self.client = client
        print(const.INITIAL_MSG)
        self.get_command()

    def get_command(self):
        self.cmd = input(const.PROMPT_MSG)
        self.parse_command()

    def parse_command(self):
        try:
            cmd = CMD(self.cmd)
            cmd.action(self.client, **cmd.options)
        except Exception as e:
            print(e.msg)

        self.get_command()

    def retry(self, msg):
        """
        打印错误信息并重新获取用户输入
        :param msg:
        :param client:
        :return:
        """
        print(msg)
        utils.show_help()
        self.get_command()
