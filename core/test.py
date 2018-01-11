# -*- coding: utf-8 -*-
# @Time    : 18-1-11 上午11:31
# @Author  : QiHanFang
# @Email   : qihanfang@foxmail.com
# @File    : test.py

from conf.settings import *

# f = open(DATABASE.get('path') + '/employee_info.txt', 'r')
# account_lst = f.readlines()
# account_lst = [line.strip().split(',') for line in account_lst if str(line).strip()]
# for i in account_lst:
#     print(i)

import re


from core.utils import transform_str

# s = 'find name,age from staff_table where age > 22'
# s1 = 'find * from staff_table where dept = "IT"'
# s2 = 'find * from staff_table where enroll_date like "2013"'
# s3 = ''
#
# match = re.findall('find (.*) from staff_table where (.*)', s1)
# print(transform_str(list(match[0])))

# ['*', 'dept = IT']
# ['name,age', 'age > 22']
# ['*', 'enroll_date like 2013']

#
# s = ' name, age '
# index_list = s.strip().split(',')
# index_list = [i.strip() for i in index_list if i]
# print(index_list)

s = 'dept = "IT"'
s1 = 'dept="IT"'
matches = list(re.findall('(.*)([=><])(.*)', s1)[0])
print(transform_str(matches))











