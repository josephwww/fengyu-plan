import argparse


class CommandParser(object):
    """
    TODO: 未实现
    """
    @classmethod
    def exit(cls):
        pass

    @classmethod
    def help(cls, args):
        """
        展示帮助信息
        :param args:
        :return:
        """
        pass

    @classmethod
    def add(cls):
        arg_parser = argparse.ArgumentParser("add")

        arg_parser.add_argument("--eid", type=int, help="分页起始位置", required=True)
        arg_parser.add_argument("--name", type=int, help="second value", required=True)
        arg_parser.add_argument("--department", type=str, help="third value", required=True)
        arg_parser.add_argument("--position", type=str, help="", required=True)
        arg_parser.add_argument("--entry_time", type=str, help="", required=True)
        return arg_parser

    @classmethod
    def delete(cls, cmd):
        arg_parser = argparse.ArgumentParser("delete")
        arg_parser.add_argument("--eid", type=int, help="分页起始位置", required=True)
        return arg_parser.parse_args(cmd)

    @classmethod
    def mod(cls, cmd):
        arg_parser = argparse.ArgumentParser("mod")

        arg_parser.add_argument("--name", type=int, help="second value")
        arg_parser.add_argument("--department", type=str, help="third value")
        arg_parser.add_argument("--position", type=str, help="")
        arg_parser.add_argument("--entry_time", type=str, help="")
        return arg_parser.parse_args(cmd)

    @classmethod
    def get(cls, client, args):
        pass

    @classmethod
    def list(cls):
        arg_parser = argparse.ArgumentParser("list")

        arg_parser.add_argument("--start", type=int, help="分页起始位置", default=0)
        arg_parser.add_argument("--limit", type=int, help="second value", default=2)
        arg_parser.add_argument("--sort", type=str, help="third value", default=3)
        arg_parser.add_argument("--direct", type=str, help="", defalut="ASC")
        arg_parser.add_argument("--search", type=str, help="", default=None)
        return arg_parser
