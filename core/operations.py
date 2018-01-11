# -*- coding: utf-8 -*-
# @Time    : 18-1-11 上午10:11
# @Author  : QiHanFang
# @Email   : qihanfang@foxmail.com
# @File    : operations.py

import re

from core.auth import is_superuser
from conf.settings import *
from core.utils import write_to_file, transform_str


@is_superuser
def add_employee_info(**kwargs):
    add_info_lst = kwargs.get('add_info_lst')
    employee_info_lst = kwargs.get('employee_info_lst')
    line_counts = len(employee_info_lst)
    add_info_lst.insert(0, str(line_counts+1))
    info = '\n'+','.join(add_info_lst)
    mobile_only = True
    for line in employee_info_lst:
        if line[3] == add_info_lst[3]:
            print('>>> 对不起，电话号码不能重复注册\n')
            mobile_only = False
            break

    if mobile_only:
        with open(DATABASE.get('path') + '/employee_info.txt', 'a') as f:
            f.write(info)
            f.flush()
            print('>>> 员工 (姓名:%s 电话：%s) 增加成功!\n' % (add_info_lst[1], add_info_lst[3]))


@is_superuser
def delete_employee_info(**kwargs):  # del from staff where id=3
    delete_id = kwargs.get('delete_id', '')
    employee_info_lst = kwargs.get('employee_info_lst', '')

    for line in employee_info_lst:
        if line[0] == delete_id:
            delete_employee = line
            break
    if int(delete_id) <= len(employee_info_lst):
        if len(delete_employee) == 6 and int(delete_id) <= len(employee_info_lst):
            while True:
                choice = input('确定删除员工(姓名:%s id:%s)的信息吗?\n1.确定删除\n2.返回\n>>>请输入(1|2): '
                               % (delete_employee[1], delete_employee[0]))

                if choice == '1':
                    del employee_info_lst[int(delete_id)-1]

                    if int(delete_id)-1 < len(employee_info_lst)+1:
                        for employee in employee_info_lst[(int(delete_id)-1):]:
                            employee[0] = int(employee[0]) - 1

                    with open(DATABASE.get('path') + '/employee_info.txt', 'w') as f:
                        for lst in employee_info_lst:
                            lst = [str(i) for i in lst]
                            line = ','.join(lst).strip()
                            f.write(line+'\n')
                    print('>>> 员工信息(姓名:%s id:%s)删除成功' % (delete_employee[1], delete_employee[0]))
                    break

                elif choice == '2':
                    break
                else:
                    pass

        else:
            print('>>> 对不起，您所查询的编号不存在')
    else:
        print('>>> 对不起，您所查询的编号不存在')


@is_superuser
def edit_employee_info(**kwargs):
    edit_info_lst = kwargs.get('edit_info_lst', '')
    employee_info_lst = kwargs.get('employee_info_lst', '')
    old_key = eval(edit_info_lst[2].upper())
    old_value = edit_info_lst[3]
    new_key = eval(edit_info_lst[0].upper())
    new_value = edit_info_lst[1]
    mobile_only = 1
    if int(new_key) == 3:
        for lst in employee_info_lst:
            if str(lst[3]) == str(new_value):
                mobile_only = 0
                break
    if mobile_only:
        if edit_info_lst[2].upper() in INDEX_NAMES and edit_info_lst[0].upper() in INDEX_NAMES:
            change_info_count = 0

            if old_key == new_key:
                for i in range(len(employee_info_lst)):
                    old_key_value_upper = str(employee_info_lst[i][old_key]).upper()
                    search_str_upper = str(old_value).upper()
                    if search_str_upper == old_key_value_upper:
                        employee_info_lst[i][old_key] = new_value
                        change_info_count += 1

            else:
                for i in range(len(employee_info_lst)):
                    value1 = str(employee_info_lst[i][old_key]).upper()
                    value2 = str(old_value).upper()
                    if value1 == value2:
                        employee_info_lst[i][new_key] = new_value
                        change_info_count += 1

            write_to_file(data_lst=employee_info_lst)
            print('>>> 修改完成！共计修改 %s 条' % change_info_count)
            print()

        else:
            print('>>> 数据字段名称有误，请检查后重新输\n')
    else:
        print('>>> 对不起，您输入的替换电话号码已存在\n')


def search_employee(**kwargs):
    search_info = kwargs.get('search_info', '')
    with open(DATABASE.get('path') + '/employee_info.txt', 'r') as f:
        employee_info_lst = f.readlines()
        employee_info_lst = [line.strip().split(',') for line in employee_info_lst if str(line).strip()]
    search_result_lst = []
    matches = re.findall('(.*)([=><]|like)(.*)', search_info[1])
    if matches:
        if matches[0]:
            matches = list(matches[0])
            search_item_lst = [i.strip() for i in matches]
            find_key = search_item_lst[0].upper()
            find_index = eval(find_key)

            if find_key in INDEX_NAMES:
                value = search_item_lst[-1]
                if value:

                    if search_info[0] == '*' and 'like' == search_item_lst[1]:
                        for lst in employee_info_lst:
                            if str(value).upper() in str(lst[int(find_index)]).upper():
                                line = ' '.join(lst)
                                search_result_lst.append(line)

                    elif search_info[0] == '*' and (search_item_lst[1] == '>' or search_item_lst[1] == '<'
                                                    or search_item_lst[1] == '='):
                        if search_item_lst[1] == '=':
                            for lst in employee_info_lst:
                                if str(lst[int(find_index)]).upper() == str(value).upper():
                                    line = ' '.join(lst)
                                    search_result_lst.append(line)

                        elif search_item_lst[1] == '>':
                            if str(find_index) == '2':
                                for lst in employee_info_lst:
                                    if int(lst[int(find_index)]) > int(value):
                                        line = ' '.join(lst)
                                        search_result_lst.append(line)
                            else:
                                print('目前仅支持年龄比较')

                        elif search_item_lst[1] == '<':
                            if str(find_index) == '2':
                                for lst in employee_info_lst:
                                    if int(lst[int(find_index)]) < int(value):
                                        line = " ".join(lst)
                                        search_result_lst.append(line)
                            else:
                                print('目前仅支持年龄比较')

                        else:
                            print('语法有误')

                    elif search_info[0] != '*':
                        index_list = search_info[0].strip().split(',')
                        index_list = [eval(i.strip().upper()) for i in index_list if i]

                        if search_item_lst[1] == '=':
                            for lst in employee_info_lst:
                                if str(lst[int(find_index)]) == str(value):
                                    res_lst = []
                                    for i in index_list:
                                        res_lst.append(lst[i])
                                    res_str = ' '.join(res_lst)
                                    search_result_lst.append(res_str)

                        elif search_item_lst[1] == '>':
                            if value.isdigit():
                                if str(find_index) == '2':
                                    for lst in employee_info_lst:
                                        if lst[int(find_index)].isdigit():
                                            if int(lst[int(find_index)]) > int(value):
                                                res_lst = []
                                                for i in index_list:
                                                    res_lst.append(lst[i])
                                                res_str = ' '.join(res_lst)
                                                search_result_lst.append(res_str)

                                else:
                                    print('>>> 目前仅支持年龄比较')
                            else:
                                print('>>> 输入有误')

                        elif search_item_lst[1] == '<':
                            if value.isdigit():
                                if str(find_index) == '2':
                                    for lst in employee_info_lst:
                                        if lst[int(find_index)].isdigit():
                                            if int(lst[int(find_index)]) < int(value):
                                                res_lst = []
                                                for i in index_list:
                                                    res_lst.append(lst[i])
                                                res_str = ' '.join(res_lst)
                                                search_result_lst.append(res_str)
                                else:
                                    print('目前仅支持年龄比较')
                            else:
                                print('>>> 输入有误')

                        else:
                            print('语法有误')

                else:
                    print('>>> 数据字段名称有误，请检查后重新输入')
            else:
                print('>>> 数据字段名称有误，请检查后重新输入')

            print()
            if search_result_lst:
                search_result_lst = [i for i in search_result_lst if i]
                print(('查询结果如下,总计 %s 条' % len(search_result_lst)).center(30, '-'))
                for line in search_result_lst:
                    print(line)
                print('------'.ljust(30, '-'))

            else:
                print('>>> 对不起,查询不到符合您要求的员工信息\n')

        else:
            print('>>> 输入有误')

    else:
        print('>>> 输入有误')