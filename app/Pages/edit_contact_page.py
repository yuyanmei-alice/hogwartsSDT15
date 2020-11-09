#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/7 16:43
'''
from selenium.webdriver.common.by import By

from app.Pages.basic_page import BasicPage


class EditContactPage(BasicPage):
    # 编辑成员>删除成员
    def delete_contact(self):
        self.findAndClick(By.XPATH, "//*[@text='删除成员']")
        self.findAndClick(By.XPATH, "//*[@text='确定']")
        from app.Pages.seach_page import SearchPage
        return SearchPage(self.driver)




