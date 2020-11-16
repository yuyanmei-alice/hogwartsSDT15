#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/10 10:23
'''
from app1.Pages.base_page import BasePage


class SearchPage(BasePage):
    # 行情>搜索图标>搜索页面
    def search(self):
        self.test_get_test_steps_from_yaml('search', '../datas/search_page.yaml')
