import logging

from common import const
from common import exception
from command.action import CommandAction
from command.parser import CommandParser

logger = logging.getLogger(__name__)


class CMD(object):
    """
    命令类，通过用户输入的命令获取对应的解析器和执行接口
    """
    def __init__(self, cmd):
        self.options = None
        self.action = None
        self.cmd_text = cmd
        self.cmd_parsers = CommandParser()
        self.parse_cmd()

    def parse_cmd(self):
        """
        解析命令，获取命令对应的参数字典及处理方法函数
        :return:
        """
        cmd_list = self.cmd_text.split()
        if not cmd_list:
            logger.error("Empty Command, please refer help")
            raise exception.EmptyCommandException
        cmd_action = cmd_list.pop(0)
        if cmd_action not in const.SupportedCommand.get_values():
            logger.error("Command {} not supported, please refer help".format(cmd_action))
            raise exception.CommandNotSupportedException(cmd_action)
        self.options = self.cmd_parsers.parse_cmd(cmd_action, cmd_list)  # 将命令对应的参数转换为字典
        self.action = getattr(CommandAction, cmd_action)
