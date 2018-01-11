# 虚拟数据库

---
## 主要功能如下:
>1.增加新用户信息（需登录操作）

>2.删除用户信息（需登录操作）

>3.修改用户信息（需登录操作）

>4.查询用户信息

---



## 代码结构分布图
![项目目录](http://oyhijg3iv.bkt.clouddn.com/%E6%B7%B1%E5%BA%A6%E6%88%AA%E5%9B%BE_%E9%80%89%E6%8B%A9%E5%8C%BA%E5%9F%9F_20180111221501.png)

##项目包详细说明
1. management.py
 * 文件为程序主入口, 包含了程序的所有功能,可以直接调用 core包内的所有函数;

2. core/auth.py
 * 用户登录函数 login(): 作为装饰器函数,被accounts_operations.py 内部的功能函数所调用, 具体功能:
 	* 1.必须是管理用户才能登录；
 	* 2.维持登录状态(避免重复登录)


3. core/utils.py
 * transform_str(): 对列表的每个元素进行字符串转化，去除多个引号，变成单引号或双引号

 * write_to_file(): 将修改后的信息写入文件

4. core/accounts_operations.py.
 * 包含了以下几项功能:
    * 1,增加新用户信息(add_employee_info):新增的电话号码不能在数据库内重复出现
    * 2,删除对应的用户信息(delete_employee_info)
    * 3,修改用户信息(edit_employee_info)
    * 4,查询用户信息(search_employee)

---
## 查询语法


> 1.模糊查询，语法支持下面3种查询语法:

```python
find name,age from staff_table where age > 22

find * from staff_table where dept = "IT"

find * from staff_table where enroll_date like "2013"

```

> 2.可创建新员工纪录，以phone做唯一键(即不允许表里有手机号重复的情况)，staff_id需自增

```python
add staff_table Alex Li,25,134435344,IT,2015-10-29

```

> 3.可删除指定员工信息纪录，输入员工id，即可删除

```python
del from staff where  id=3

```

> 4.可修改员工信息，语法如下:

```python
# 把所有dept=IT的纪录的dept改成Market
UPDATE staff_table SET dept="Market" WHERE  dept = "IT"
# 把name=Alex Li的纪录的年龄改成25
UPDATE staff_table SET age=25 WHERE  name = "Alex Li"

```



---
##具体演示代码:

```
#精确查询

---------欢迎登录虚拟数据库系统----------
>>> 请输入您的指令(退出|q): find name,age from staff_table where age > 22

--------查询结果如下,总计 15 条--------
Kevin Chen 55
Chen Li 25
Xiu Li 25
Wang Li 25
Qiu Li 25
BaBa Li 25
Jack Ma 55
Alex Li 50
Alex Li 50
Ham Li 25
Alex Li 50
Alex Wang 25
Alex Wang 25
Alex Li 25
Alex Li 25
------------------------------
```
---
```
# 模糊查询

>>> 请输入您的指令(退出|q): find * from staff_table where enroll_date like "2013"

--------查询结果如下,总计 1 条---------
1 Kevin Chen 55 18888888888 666 2013-04-01
------------------------------
>>> 请输入您的指令(退出|q):

```

---
