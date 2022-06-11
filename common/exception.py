class EmployeeNotFoundException(Exception):
    message = "Cannot find employee id in the database"


class CommandNotSupportedException(Exception):
    message = "Command not supported"


class EmployeeIDFoundException(Exception):
    message = "employee id already exists in the database"

