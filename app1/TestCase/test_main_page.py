#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/10 13:44


'''
import allure
import pytest

from app1.Pages.base_page import BasePage


class TestMainPage:
    @allure.title('主页点击行情按钮')
    def test_goto_news(self, setup_app):
        setup_app.goto_main().goto_news().goto_index()







