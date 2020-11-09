#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/7 17:21
'''
from app.Pages.basic_page import BasicPage
from app.Pages.main_page import MainPage


class TestContactPage():

    def test_search_contact(self):
        # 首页>通讯录>搜索
        MainPage().goto_contactList().goto_search_contact()
