ENTRY_DATE_FORMAT = '%Y-%m-%d'

# list接口direct字段
ASC = "ASC"
DESC = "DESC"

# 控制台打印指令
PROMPT_MSG = "请输入命令（help查看说明）：\n>> "
DEFAULT_ERROR_MSG = "指令有误，请重新输入"
CUSTOM_ERROR_MSG = "指令{cmd}有误，请重新输入"
WRONG_EID_MSG = "请输入正确格式的员工id"
WRONG_ENTRY_TIME_MSG = "请输入带中杠的日期格式，例如2022-06-04"
EMPTY_DATABASE_MSG = "数据库无员工数据，请插入！"
EMPLOYEE_INFO = "Employee : {employee}"
CREATE_SUCCESS_MSG = "新员工创建成功，员工id：{eid}"
DELETE_SUCCESS_MSG = "员工{eid}已被删除"
UPDATE_SUCCESS_MSG = "员工{eid}信息已更新"


# 函数执行成功或失败返回
OK = "ok"
FAILED = "failed"


# 命令参数限制
ADD_COMMAND_LIMIT = 5
DELETE_COMMAND_LIMIT = 1

class SupportedCommand(object):
    HELP = "help"
    ADD = "add"
    MOD = "mod"
    DELETE = "delete"
    SHOW = "show"
    EXIT = "exit"
    GET = "get"
    LIST = "list"

    @classmethod
    def get_values(cls):
        return cls.HELP, cls.ADD, cls.MOD, cls.DELETE, cls.SHOW, cls.EXIT, cls.GET, cls.LIST


class EmployeeAttributes(object):
    NAME = "name"
    DEPARTMENT = "department"
    POSITION = "position"
    ENTRY_TIME = "entry_time"
    EMPLOYEE_ID = "eid"

    @classmethod
    def get_values(cls):
        return cls.NAME, cls.POSITION, cls.DEPARTMENT, cls.ENTRY_TIME

    @classmethod
    def sortable_attrs(cls):
        return cls.NAME, cls.DEPARTMENT, cls.POSITION


class ListParams(object):
    START = "start"
    LIMIT = "limit"
    SORT = "sort"
    DIRECT = "direct"
    SEARCH = "search"

    @classmethod
    def get_values(cls):
        return cls.START, cls.LIMIT, cls.SORT, cls.DIRECT, cls.SEARCH
