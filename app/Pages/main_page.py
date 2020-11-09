#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/7 16:48
'''
from selenium.webdriver.common.by import By

from app.Pages.basic_page import BasicPage
from app.Pages.contact_page import ContactPage


class MainPage(BasicPage):
    def goto_contactList(self):
        self.findAndClick(By.XPATH, "//*[@text='通讯录']")
        return ContactPage(self.driver)
