#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/7 16:17
企业微信（手机应用)>通讯录
'''
from selenium.webdriver.common.by import By

from app.Pages.add_member_page import AddMember
from app.Pages.basic_page import BasicPage
from app.Pages.contact_detail_page import ContactDetailPage
from app.Pages.seach_page import SearchPage


class ContactPage(BasicPage):
    # 通讯录列表
    def get_contact_list(self):
        pass

    # 添加联系人
    def add_contact(self):
        self.findAndClick(By.XPATH, "//*[@text='添加成员']")
        return AddMember(self.driver)

    # 搜索
    def goto_search_contact(self):
        self.findAndClick(By.ID, "com.tencent.wework:id/hxw")
        return SearchPage(self.driver)

    # 跳转到联系人详情页
    def goto_contact_detail(self):
        return ContactDetailPage(self.driver)

