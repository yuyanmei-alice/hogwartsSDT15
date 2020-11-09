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
    def setup_class(self):
        # 启动应用
        self.app = BasicPage()

    def teardown_class(self):
        self.app.stop()

    # 此处逻辑待优化判断测试联系人是否已存在，如果已存在，就直接进行删除操作，如果不存在先调用添加联系人
    @pytest.mark.parametrize('name,phoneNum', [('小兰', '15811112223')])
    def test_delete_contact(self, name, phoneNum):
        self.app.goto_main().goto_contactList().goto_search_contact().search_by_name(
            name).goto_contact_detail_page().goto_more().goto_edit_contact(). \
            delete_contact().waitElementPresent(By.XPATH, "//*[@text='无搜索结果']")



