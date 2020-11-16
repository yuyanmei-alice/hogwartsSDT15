#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/10 10:30
'''
import time

import pytest
import yaml


# 验证从yaml读取数据
from app1.Pages.base_page import BasePage



class TestSearchPage:

    def setup(self):

        self.app = BasePage()

    def teardown(self):
        self.app.stop_app()

    @pytest.mark.parametrize('name', ["alibaba"])
    def test_search(self, name):
        self.app.goto_main().goto_news().goto_search().search()
