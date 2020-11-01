#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/29 11:14
'''
from Pages.login_page import LoginPage
from Pages.main_page import MainPage


class TestLoginPage():
    # 测试登录页面的企业注册按钮 首页>登录页面>注册页面
    def test_goto_register(self):
        MainPage().goto_login().goto_register()

