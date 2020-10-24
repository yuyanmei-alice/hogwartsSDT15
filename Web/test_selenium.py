#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/24 10:17
'''
from selenium import webdriver

class TestSelenium():

    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def test_chrome(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

