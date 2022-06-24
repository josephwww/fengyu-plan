ENTRY_DATE_FORMAT = '%Y-%m-%d'

# list接口direct字段
ASC = "ASC"
DESC = "DESC"

# 控制台打印指令
INITIAL_MSG = "请输入命令（help查看说明）："
PROMPT_MSG = ">> "
DEFAULT_ERROR_MSG = "指令有误，请重新输入"
EID_EXIST_ERROR_MSG = "员工id已存在，无法添加！"
EMPTY_DATABASE_MSG = "数据库无数据，请插入！"
EMPLOYEE_NOT_FOUND_MSG = "员工ID未找到，请检查输入"
BASE_ERROR_MSG = "操作失败，原因：{reason}"
PARAM_ERROR_MSG = "参数校验失败，请检查参数"
OK = "操作成功"


class SupportedCommand(object):
    HELP = "help"
    ADD = "add"
    MOD = "mod"
    DELETE = "delete"
    EXIT = "exit"
    GET = "get"
    LIST = "list"

    @classmethod
    def get_values(cls):
        return cls.HELP, cls.ADD, cls.MOD, cls.DELETE, cls.EXIT, cls.GET, cls.LIST


class EmployeeAttributes(object):
    NAME = "name"
    DEPARTMENT = "department"
    POSITION = "position"
    ENTRY_TIME = "entry_time"
    EMPLOYEE_ID = "eid"

    @classmethod
    def sortable_attrs(cls) -> tuple:
        return cls.EMPLOYEE_ID, cls.NAME, cls.DEPARTMENT, cls.POSITION


class ListParams(object):
    START = "start"
    LIMIT = "limit"
    SORT = "sort"
    DIRECT = "direct"
    SEARCH = "search"

    @classmethod
    def get_values(cls):
        return cls.START, cls.LIMIT, cls.SORT, cls.DIRECT, cls.SEARCH
