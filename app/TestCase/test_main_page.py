#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/7 16:55
'''

from app.Pages.main_page import MainPage


class TestMainPage():
    def test_goto_contactList(self):
        MainPage().goto_contactList()
