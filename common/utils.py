def show_help():
    """
    展示帮助信息
    :return:
    """
    print("使用方法：")
    print("1. 展示当前员工列表： show all")
    print("2. 创建新员工信息： add <姓名> <部门> <职位> <入职时间>")
    print("如：>> add Zhangsan CMP Python开发 2022-01-01")
    print("3. 更新员工信息： mod <员工id> <更新字段> <更新内容>")
    print("支持更新的字段有： 姓名： name，部门：department, 职位：position，入职时间：entry_time")
    print("如：>> mod 1 name LiSi department VT")
    print("4. 删除员工信息：delete <员工id>")
    print("如：>> delete 1")
    print("5. exit：退出程序")
