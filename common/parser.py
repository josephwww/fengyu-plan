from common import const
from common import utils
from common.command_action import CommandAction
from common.command_parser import CommandParser


class Parser(object):
    def __init__(self, client):
        self.cmd = None
        self.client = client
        self.cmd_parsers = CommandParser()
        self.get_command()

    def get_command(self):
        self.cmd = input(const.PROMPT_MSG)
        self.parse_command()

    def parse_command(self):
        cmd_list = self.cmd.split()
        if not cmd_list:
            self.retry(const.DEFAULT_ERROR_MSG)
            return
        cmd = cmd_list.pop(0)
        if cmd not in const.SupportedCommand.get_values():
            self.retry(const.CUSTOM_ERROR_MSG.format(cmd=cmd))
            return
        parsed_cmd_dict = self.cmd_parsers.parse_cmd(cmd, cmd_list)
        cmd_action = getattr(CommandAction, cmd)
        cmd_action(self.client, **parsed_cmd_dict)
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
