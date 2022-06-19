import argparse
import datetime
from common.const import SupportedCommand
from common.exception import CommandNotSupportedException
from common.utils import parse_date


class DefaultParser(argparse.ArgumentParser):
    def __init__(self, program_name):
        super().__init__(program_name, add_help=False)
        self.add_argument("-h", "--help", help="show this help message")

    def error(self, message: str):
        self.print_help()
        raise CommandNotSupportedException

    def __call__(self, *args, **kwargs):
        self.print_help()


class CommandParser(object):
    def __init__(self):
        self.parsers_dict = {}
        for cmd in SupportedCommand.get_values():
            self.parsers_dict[cmd] = getattr(self, cmd)()

    def parse_cmd(self, cmd, cmd_list):
        parser = self.parsers_dict.get(cmd)
        options = vars(parser.parse_args(cmd_list))
        del options["help"]
        return options

    @classmethod
    def exit(cls):
        arg_parser = DefaultParser("exit")
        return arg_parser

    @classmethod
    def help(cls):
        arg_parser = DefaultParser("help")
        return arg_parser

    @classmethod
    def add(cls):
        arg_parser = DefaultParser("add")
        arg_parser.add_argument("--eid", type=str, help="员工id", required=True)
        arg_parser.add_argument("--name", type=str, help="员工姓名", required=True)
        arg_parser.add_argument("--department", type=str, help="部门", required=True)
        arg_parser.add_argument("--position", type=str, help="职位", required=True)
        arg_parser.add_argument("--entry_time", type=parse_date, help="入职时间（带中杠的日期，如：2022-6-1）", required=True)
        return arg_parser

    @classmethod
    def delete(cls):
        arg_parser = DefaultParser("delete")
        arg_parser.add_argument("--eid", type=str, help="员工id", required=True)
        return arg_parser

    @classmethod
    def mod(cls):
        arg_parser = DefaultParser("mod")
        arg_parser.add_argument("--eid", type=str, help="员工id", required=True)
        arg_parser.add_argument("--name", type=str, help="员工姓名")
        arg_parser.add_argument("--department", type=str, help="部门")
        arg_parser.add_argument("--position", type=str, help="职位")
        arg_parser.add_argument("--entry_time", type=parse_date, help="入职时间（带中杠的日期，如：2022-6-1）")
        return arg_parser

    @classmethod
    def get(cls):
        arg_parser = DefaultParser("get")
        arg_parser.add_argument("--eid", type=str, help="员工id", required=True)
        return arg_parser

    @classmethod
    def list(cls):
        arg_parser = DefaultParser("list")
        arg_parser.add_argument("--start", type=int, help="分页起始位置", default=0)
        arg_parser.add_argument("--limit", type=int, help="分页数量", default=100)
        arg_parser.add_argument("--sort", type=str, help="排序字段", default="eid")
        arg_parser.add_argument("--direct", type=str, help="排序方向", default="ASC")
        arg_parser.add_argument("--search", type=str, help="搜索字段", default=None)
        return arg_parser
