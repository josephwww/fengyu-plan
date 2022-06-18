import argparse
from common.const import SupportedCommand


class CommandParser(object):
    def __init__(self):
        self.parsers_dict = {}
        for cmd in SupportedCommand.get_values():
            self.parsers_dict[cmd] = getattr(self, cmd)()

    def parse_cmd(self, cmd, cmd_list):
        parser = self.parsers_dict.get(cmd)
        return vars(parser.parse_args(cmd_list))

    @classmethod
    def exit(cls):
        arg_parser = argparse.ArgumentParser("exit")
        return arg_parser

    @classmethod
    def help(cls):
        arg_parser = argparse.ArgumentParser("help")
        return arg_parser

    @classmethod
    def add(cls):
        arg_parser = argparse.ArgumentParser("add")

        arg_parser.add_argument("--eid", type=str, help="员工id", required=True)
        arg_parser.add_argument("--name", type=str, help="员工姓名", required=True)
        arg_parser.add_argument("--department", type=str, help="部门", required=True)
        arg_parser.add_argument("--position", type=str, help="职位", required=True)
        arg_parser.add_argument("--entry_time", type=str, help="入职时间", required=True)
        return arg_parser

    @classmethod
    def delete(cls):
        arg_parser = argparse.ArgumentParser("delete")
        arg_parser.add_argument("--eid", type=str, help="员工id", required=True)
        return arg_parser

    @classmethod
    def mod(cls):
        arg_parser = argparse.ArgumentParser("mod")
        arg_parser.add_argument("--eid", type=str, help="员工id", required=True)
        arg_parser.add_argument("--name", type=str, help="员工姓名")
        arg_parser.add_argument("--department", type=str, help="部门")
        arg_parser.add_argument("--position", type=str, help="职位")
        arg_parser.add_argument("--entry_time", type=str, help="入职时间")
        return arg_parser

    @classmethod
    def get(cls):
        arg_parser = argparse.ArgumentParser("mod")
        arg_parser.add_argument("--eid", type=str, help="员工id", required=True)
        return arg_parser

    @classmethod
    def list(cls):
        arg_parser = argparse.ArgumentParser("list")
        arg_parser.add_argument("--start", type=int, help="分页起始位置", default=0)
        arg_parser.add_argument("--limit", type=int, help="second value", default=None)
        arg_parser.add_argument("--sort", type=str, help="third value", default="eid")
        arg_parser.add_argument("--direct", type=str, help="", default="ASC")
        arg_parser.add_argument("--search", type=str, help="", default=None)
        return arg_parser
