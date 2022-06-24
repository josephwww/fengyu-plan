# 员工信息记录系统

 
## Install
 
```
$ pip install -r requirements.txt
```
 
## Usage
 
```
>> help 获取帮助信息
>> add 添加新员工
   add --eid <员工id:str> --name <姓名:str> --department <部门:str> --position <职位:str> --entry_time <入职时间:带横杠的日期格式>
   add --eid 14589 --name Zhangsan --department CMP --position Python开发 --entry_time 2022-01-01
>> mod 更改员工信息
   mod --eid <员工id:str> [--name <姓名:str>] [--department <部门:str>] [--position <职位:str>] [--entry_time <入职时间:带横杠的日期格式>]
   mod --eid 14589 --name LiSi --department VT
>> delete 删除员工信息
   delete --eid <员工id:str>
   delete --eid 14589
>> get 查询员工信息
   get --eid <员工id:str>
   get --eid 14589
>> list 获取员工信息列表
   list [--start <分页起始位置:int>] [--limit <分页数量:int>] [--sort <排序字段>] [--direct <排序顺序:ASC|DESC>] [--search <搜索字段:str>]
   list --search CMP
```
 
## License
MIT © Richard McRichface

## UnitTest Coverage Report
![](https://github.com/josephwww/fengyu-plan/blob/master/%E5%8D%95%E6%B5%8B%E8%A6%86%E7%9B%96%E7%8E%87%E6%88%AA%E5%9B%BE.png?raw=true)
