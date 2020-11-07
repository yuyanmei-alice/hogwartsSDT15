#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/29 10:40
企业微信>首页（未登录时）>企业登录链接页面
'''
from Pages.basic_page import BasicPage
from Pages.register_page import RegisterPage


class LoginPage(BasicPage):
    # 扫码登录
    def login_by_san(self):
        pass

    # 点击企业注册按钮
    def goto_register(self):
        self.driver.find_element_by_xpath("//a[@class='login_registerBar_link']").click()
        return RegisterPage(self.driver)
