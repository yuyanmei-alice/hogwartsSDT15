#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/10 13:44
'''
import pytest

from app1.Pages.base_page import BasePage


class TestMainPage:

    def setup(self):
        self.app = BasePage()

    def teardown(self):
        self.app.stop_app()

    def test_goto_news(self):
        self.app.goto_main().goto_news()