#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/7 20:39
'''
from time import sleep

import pytest
from selenium.webdriver.common.by import By

from app.Pages.basic_page import BasicPage
from app.Pages.main_page import MainPage


class TestEditContactPage():
    @pytest.mark.parametrize('name,phoneNum', [('小兰1', '15811112223')])
    def test_delete_contact(self, name, phoneNum):
        # 先添加测试联系人
        MainPage().goto_contactList().add_contact().goto_addMember_manual().add_member(name, phoneNum)
        # 编辑成员>删除成员
        MainPage().goto_contactList().goto_search_contact().search_by_name(
            name).goto_contact_detail_page().goto_more().goto_edit_contact().\
            delete_contact().waitElementPresent(By.XPATH, "//*[@text='无搜索结果']")


