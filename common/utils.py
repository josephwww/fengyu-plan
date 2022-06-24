import prettytable as pt
import datetime

from common import const
from database.abstract_class import DatabaseObject


def show_help():
    """
    展示帮助信息
    :return:
    """
    tb = pt.PrettyTable(["功能", "介绍"])
    tb.add_row(["add", "创建新员工信息 --eid <员工id> --name <姓名> --department <部门> --position <职位> --entry_time <入职时间>"])
    tb.add_row(
        ["", "如：>> add --eid 14589 --name Zhangsan --department CMP --position Python开发 --entry_time 2022-01-01"])
    tb.add_row(["mod", "更新员工信息 --eid <员工id> --<更新字段> <更新内容>"])
    tb.add_row(["", "支持更新的字段有： 姓名： name，部门：department, 职位：position，入职时间：entry_time"])
    tb.add_row(["", "如：>> mod --eid 14589 --name LiSi --department VT"])
    tb.add_row(["delete", "删除员工信息 --eid <员工id>"])
    tb.add_row(["", "如：>> delete --eid 14589"])
    tb.add_row(["exit", "退出程序"])
    tb.add_row(["list", "展示当前员工列表"])
    tb.align["功能"] = 'l'
    tb.align["介绍"] = 'l'
    tb.set_style(pt.PLAIN_COLUMNS)
    print(tb)


def parse_date(time_string):
    return datetime.datetime.strptime(time_string, const.ENTRY_DATE_FORMAT)


# 格式化打印GET接口返回值
def print_util(func):
    def wrapper(*args, **params):
        db_objects = func(*args, **params)
        tb = pt.PrettyTable(["功能", "介绍"])
        if isinstance(db_objects, list):
            if not db_objects:
                print(const.EMPTY_DATABASE_MSG)
            for obj in db_objects:
                print(obj)
        elif isinstance(db_objects, DatabaseObject):
            print(db_objects)
        return db_objects
    return wrapper
