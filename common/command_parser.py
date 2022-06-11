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
    def show(cls):
        arg_parser = argparse.ArgumentParser("Show")

        arg_parser.add_argument("--start", type=int, help="分页起始位置", default=0)
        arg_parser.add_argument("--limit", type=int, help="second value", default=2)
        arg_parser.add_argument("--sort", type=str, help="third value", default=3)
        arg_parser.add_argument("--direct", type=str, help="", defalut="ASC")
        arg_parser.add_argument("--search", type=str, help="", default=None)
        return arg_parser

    @classmethod
    def add(cls, client, *employee):
        pass

    @classmethod
    def delete(cls, client, *employee):
        pass

    @classmethod
    def mod(cls, client, *employee):
        pass

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
