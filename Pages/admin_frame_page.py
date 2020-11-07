#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/29 12:13
企业微信>首页
'''
from Pages.admin_frame_contacts_page import AdminFrameContactsPage
from Pages.basic_page import BasicPage


class AdminFramePage(BasicPage):
    # 登录企业微信 首页>常用入口>添加成员
    def common_entrance_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_xpath("//*[@node-type='addmember']").click()
        return AdminFrameContactsPage(self.driver)
