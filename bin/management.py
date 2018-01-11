# -*- coding: utf-8 -*-
# @Time    : 18-1-11 上午10:11
# @Author  : QiHanFang
# @Email   : qihanfang@foxmail.com
# @File    : management.py

import re
import os
import sys

from conf.settings import *
from core.operations import *
from core.utils import transform_str

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)


print('欢迎登录虚拟数据库系统'.center(30, '-'))
while True:
    command_line = input('>>> 请输入您的指令(退出|q): ').strip()

    if command_line[:3] == 'add':
        add_info_str = re.match('add staff_table (.*)', command_line)
        if add_info_str:
            add_info_lst = add_info_str.group(1).strip().split(',')
            if len(add_info_lst) == 5:
                add_employee_info(add_info_lst=add_info_lst)

            else:
                print('>>> 对不起，指令语法有误，请检查逗号和空格后重新输入!')
        else:
            print('>>> 对不起，指令语法有误，请检查空格后重新输入!')

    elif command_line[:3] == 'del':
        delete_id = re.match('del from staff where id=(\d+)', command_line)
        if delete_id:
            delete_id = delete_id.group(1)
            if delete_id.isdigit():
                if isinstance(eval(delete_id), int):
                    if int(delete_id) > 0:
                        delete_employee_info(delete_id=delete_id)
                    else:
                        print('>>> 员工编号有误，请重新输入！')
            else:
                print('>>> 员工编号有误，请重新输入！')

        else:
            print('>>> 对不起，指令语法有误，请检查空格后重新输入!')

    elif command_line[:6] == 'UPDATE':
        matches = re.findall('UPDATE staff_table SET (.*)=(.*) WHERE (.*)=(.*)', command_line)
        if matches:
            if matches[0]:
                if len(matches[0]) == 4:
                    edit_info_lst = transform_str(list(matches[0]))
                    edit_info_lst = [i.strip() for i in edit_info_lst]
                    edit_employee_info(edit_info_lst=edit_info_lst)

                else:
                    print('>>> 对不起，指令语法有误，请检查空格后重新输入!')
            else:
                print('>>> 对不起，指令语法有误，请检查空格后重新输入!')
        else:
            print('>>> 对不起，指令语法有误，请检查空格后重新输入!')

    elif command_line[:4] == 'find':
        match = re.findall('find(.*)from staff_table where(.*)', command_line)
        if match:
            if match[0]:
                search_info_lst = transform_str(list(match[0]))
                search_info_lst = [i.strip() for i in search_info_lst if i]
                if len(search_info_lst) == 2:
                    search_employee(search_info=search_info_lst, command_line=command_line)
                else:
                    print('>>> 输入有误,请核对后重新输入！\n')
        else:
            print('>>> 输入有误,请核对后重新输入！\n')

    elif command_line == 'quit' or command_line == 'q':
        tips = input('确定要退出?(y): ')
        if tips == 'y' or tips == 'yes':
            break
    else:
        print('>>> 输入有误,请核对后重新输入！\n')

