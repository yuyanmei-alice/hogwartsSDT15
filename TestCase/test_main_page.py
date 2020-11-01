#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/29 10:41
'''
from Pages.main_page import MainPage


class TestMainPage():

    def test_goto_register(self):
        MainPage().goto_register()

    def test_goto_login(self):
        MainPage().goto_login()


