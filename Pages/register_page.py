#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/29 10:38
'''
from Pages.basic_page import BasicPage


class RegisterPage(BasicPage):
    # 正常注册
    def register(self):
        self.driver.find_element_by_id("corp_name").send_keys("Python测试")
        self.driver.find_element_by_xpath("//*[@id='corp_industry']").click()
        self.driver.find_element_by_xpath("//*[@data-name='IT服务']").click()
        self.driver.find_element_by_xpath("//*[@data-parent-name='IT服务']/div[1]/a").click()
        self.driver.find_element_by_id("corp_scale_btn").click()
        self.driver.find_element_by_xpath("//*[@id='corp_scale_btn']/div/ul/li[1]/a").click()


