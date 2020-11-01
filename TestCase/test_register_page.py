#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/29 12:05
'''
from Pages.main_page import MainPage
from Pages.register_page import RegisterPage


class TestRegisterPage():
    # 测试登录页面的企业注册按钮 首页>登录页面>注册页面>注册功能
    def test_register(self):
        MainPage().goto_login().goto_register().register()


