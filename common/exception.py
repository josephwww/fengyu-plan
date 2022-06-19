from common import const


class EmployeeNotFoundException(Exception):
    msg = const.BASE_ERROR_MSG.format(operation="", reason=const.EMPLOYEE_NOT_FOUND_MSG)


class EmptyCommandException(Exception):
    msg = const.DEFAULT_ERROR_MSG


class CommandNotSupportedException(Exception):
    msg = const.DEFAULT_ERROR_MSG


class EmployeeIDFoundException(Exception):
    msg = const.EID_EXIST_ERROR_MSG

