# -*- coding: utf-8 -*-
# @Time    : 18-1-11 上午10:38
# @Author  : QiHanFang
# @Email   : qihanfang@foxmail.com
# @File    : auth.py

import json
import hashlib

from conf.settings import *


login_status = 0


def is_superuser(func):

    def inner(**kwargs):
        global login_status
        add_info_lst = kwargs.get('add_info_lst', '')
        delete_id = kwargs.get('delete_id', '')
        edit_info_lst = kwargs.get('edit_info_lst', '')

        with open(DATABASE.get('path') + '/employee_info.txt', 'r') as f:
            employee_info_lst = f.readlines()
            employee_info_lst = [line.strip().split(',') for line in employee_info_lst if str(line).strip()]

        if login_status == 0:
            save_path = DATABASE.get('path')

            with open(save_path+'/super_user.json', 'r') as f:
                super_user_info = json.load(f)
                username = super_user_info.get('username', '')
                password = super_user_info.get('password', '')
                count = 0

                while count < 3:
                    md_5 = hashlib.md5()
                    input_username = input('>>> 请输入您的账号：　')
                    input_pwd = input('>>> 请输入您的密码：　')

                    md_5.update(input_username.encode('utf8'))
                    input_username = md_5.hexdigest()
                    md_5.update(input_pwd.encode('utf8'))
                    input_pwd = md_5.hexdigest()

                    if input_username == username and input_pwd == password:
                        login_status = 1
                        return func(employee_info_lst=employee_info_lst, add_info_lst=add_info_lst, delete_id=delete_id,
                                    edit_info_lst=edit_info_lst)

                    else:
                        print('>>> 对不起，您的账号或密码错误，请重新输入')
                        count += 1

                else:
                    exit('>>> 对不起，您输入的密码次数过多,请稍后重新输入')

        else:
            return func(employee_info_lst=employee_info_lst, add_info_lst=add_info_lst, delete_id=delete_id, edit_info_lst=edit_info_lst)

    return inner

