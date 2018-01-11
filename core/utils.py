# -*- coding: utf-8 -*-
# @Time    : 18-1-11 上午10:19
# @Author  : QiHanFang
# @Email   : qihanfang@foxmail.com
# @File    : utils.py

from conf.settings import *


def transform_str(lst):
    '''
    应用函数, 主要用于转化['dept', '"Market"', 'dept', '"IT"']--->['dept', 'Market', 'dept', 'IT']
    在search(**kwargs)函数中使用
    '''
    for i in range(len(lst)):
        if '"' in lst[i]:
            lst[i] = lst[i].replace('"', '')
        elif "'" in lst[i]:
            lst[i] = lst[i].replace("'", '')
        else:
            pass
    return lst


def write_to_file(data_lst):
    with open(DATABASE.get('path') + '/employee_info.txt', 'w') as f:
        for lst in data_lst:
            if isinstance(lst, list):
                lst = [str(i) for i in lst]
                line = ','.join(lst).strip()
                f.write(line + '\n')
            else:
                print('>>> 内容格式有误！')

