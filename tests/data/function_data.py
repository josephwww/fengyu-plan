from datetime import datetime

from database.employee import Employee


employee_1 = Employee("14589", "whf", "CMP", "python", datetime.now())
employee_1_updated = Employee("14589", "whf", "CMP", "python&go", datetime.now())
employee_2 = Employee("12114", "nhw", "CMP", "go", datetime.now())

