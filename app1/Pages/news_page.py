#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/10 9:51
'''
from app1.Pages.base_page import BasePage
from app1.Pages.search_page import SearchPage


class NewsPage(BasePage):
    # 行情>搜索图标
    def goto_search(self):
        self.test_get_test_steps_from_yaml('goto_search', '../datas/news_page.yaml')
        return SearchPage(self.driver)

    # 回雪球主页
    def goto_index(self):
        self.test_get_test_steps_from_yaml('goto_index', '../datas/news_page.yaml')
        return SearchPage(self.driver)


