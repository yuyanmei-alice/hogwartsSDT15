#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/7 17:28
'''
from selenium.webdriver.common.by import By

from app.Pages.basic_page import BasicPage


class SearchPage(BasicPage):

    def search_by_name(self, name):
        self.findAndSendKeys(By.XPATH, "//*[@text='搜索']", name)
        return SearchPage(self.driver)

    def goto_contact_detail_page(self):
        self.findAndClick(By.XPATH, "//*[@resource-id='com.tencent.wework:id/gja']/android.widget.RelativeLayout[2]")
        from app.Pages.contact_detail_page import ContactDetailPage
        return ContactDetailPage(self.driver)

    def is_have_searchResult(self):
        if len(self.finds(By.XPATH, "//*[@text='联系人']")) > 0:
            return True
        else:
            return False








