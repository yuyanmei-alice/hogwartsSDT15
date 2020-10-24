#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/23 16:46
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestSelenium():

    def setup_method(self):
        option = Options()
        option.debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=option)

    def teardown_method(self):
        self.driver.quit()

    def test_chrome(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts/import/1688853987785040")
        self.driver.implicitly_wait(3)
