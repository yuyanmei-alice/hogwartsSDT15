#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/7 17:54
'''
import pytest

from app.Pages.main_page import MainPage


class TestSearchPage():

    def setup(self):
        from app.Pages.basic_page import BasicPage
        self.app = BasicPage()

    def teardown(self):
        self.app.stop()

    # 首页>通讯录>搜索>输入名称搜索
    @pytest.mark.parametrize('name', ['王五'])
    def test_search_by_name(self, name):
        self.app.goto_main().goto_contactList().goto_search_contact().search_by_name(name)

    # 首页>通讯录>搜索>输入名称搜索>选中查询结果进入个人信息页面
    @pytest.mark.parametrize('name', ['王五'])
    def test_goto_contact_detail_page(self, name):
        self.app.goto_main().goto_contactList().goto_search_contact().search_by_name(name).goto_contact_detail_page()

    # 首页>通讯录>搜索>输入名称搜索> 返回查询结果
    @pytest.mark.parametrize('name', ['小兰', '无'])
    def test_is_have_searchResult(self, name):
        print(self.app.goto_main().goto_contactList().goto_search_contact().search_by_name(name).is_have_searchResult())
