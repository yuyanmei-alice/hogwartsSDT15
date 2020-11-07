#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/29 12:17
企业微信>通讯录页面
'''
import pytest

from Pages.basic_page import BasicPage


class AdminFrameContactsPage(BasicPage):
    # 添加成员

    def addMember(self):
        self.driver.find_element_by_id("username").send_keys("王五")
        self.driver.find_element_by_id("memberAdd_english_name").send_keys("王五")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("W123456")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("15600001111")
        self.driver.find_element_by_xpath("//*[@class='js_member_editor_form']/div/a[2]").click()
        return AdminFrameContactsPage(self.driver)

    # （通讯录>添加成员按钮)
    def goto_add_member(self):
        self.driver.find_element_by_xpath("//*[@class='member_colRight_cnt_NoData js_no_member']/div[2]/a[1]").click()
        return AdminFrameContactsPage(self.driver)

    # （通讯录>删除按钮)
    def button_delete_member(self):
        self.driver.find_element_by_class_name('qui_btn ww_btn js_delete').click()
        return AdminFrameContactsPage(self.driver)









