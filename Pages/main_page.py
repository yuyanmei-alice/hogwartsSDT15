#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/28 17:41
企业微信>首页（未登录时)
'''
from Pages.basic_page import BasicPage
from selenium import webdriver

from Pages.login_page import LoginPage
from Pages.register_page import RegisterPage


class MainPage(BasicPage):

#点击首页的立即注册按钮
    def goto_register(self):
        self.driver.get('https://work.weixin.qq.com/')
        self.driver.find_element_by_xpath("//a[@class='index_head_info_pCDownloadBtn']").click()
        return RegisterPage()

#点击首页的登录按钮
    def goto_login(self):
        self.driver.get('https://work.weixin.qq.com/')
        self.driver.find_element_by_xpath("//a[@class='index_top_operation_loginBtn']").click()
        return LoginPage(self.driver)



