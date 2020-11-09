#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/7 16:25
'''
from selenium.webdriver.common.by import By

from app.Pages.basic_page import BasicPage
from app.Pages.edit_contact_page import EditContactPage


class ContactDetailPage(BasicPage):
    # 个人信息>更多
    def goto_more(self):
        self.findAndClick(By.ID, 'com.tencent.wework:id/hxm')
        return ContactDetailPage(self.driver)

    # 个人信息>更多>编辑成员
    def goto_edit_contact(self):

        self.findAndClick(By.XPATH, "//*[@text='编辑成员']")
        return EditContactPage(self.driver)
