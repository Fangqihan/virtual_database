# -*- coding: utf-8 -*-
# @Time    : 18-1-11 上午10:11
# @Author  : QiHanFang
# @Email   : qihanfang@foxmail.com
# @File    : settings.py


import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


NUMBER = 0
NAME = 1
AGE = 2
MOBILE = 3
DEPT = 4
ENROLL_DATE = 5

INDEX_NAMES = ['NUMBER', 'NAME', 'AGE', 'MOBILE', 'DEPT', 'ENROLL_DATE']



DATABASE = {
    'name': 'info_db',
    'path': "%s/info_db" % BASE_DIR
}


ADMIN = {'username': 'lynnfang', 'password': 'fqh202'}
