#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/9 10:22
'''
import pytest
from selenium.webdriver.common.by import By

from app.Pages.basic_page import BasicPage


class AddMember(BasicPage):
    def goto_addMember_manual(self):
        self.findAndClick(By.XPATH, "//*[@text='输入成员信息加入企业通讯录']")
        return AddMember(self.driver)

    def add_member(self, name, phoneNum):
        self.findAndSendKeys(By.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText", name)
        self.findAndClick(By.XPATH, "//*[contains(@text,'性别')]/../android.widget.RelativeLayout")
        self.findAndClick(By.XPATH, "//*[@text='女']")
        self.findAndSendKeys(By.XPATH, "//*[@text='手机号']", phoneNum)
        self.findAndClick(By.XPATH, "//*[@text='保存']")
