def show_help():
    """
    展示帮助信息
    :return:
    """
    print("使用方法：")
    print("1. 展示当前员工列表： list")
    print("2. 创建新员工信息： add --eid <员工id> --name <姓名> --department <部门> --position <职位> --entry_time <入职时间>")
    print("如：>> add --eid 14589 --name Zhangsan --department CMP --position Python开发 --entry_time 2022-01-01")
    print("3. 更新员工信息： mod --eid <员工id> --<更新字段> <更新内容>")
    print("支持更新的字段有： 姓名： name，部门：department, 职位：position，入职时间：entry_time")
    print("如：>> mod --eid 14589 --name LiSi --department VT")
    print("4. 删除员工信息：delete --eid <员工id>")
    print("如：>> delete --eid 14589")
    print("5. exit：退出程序")
