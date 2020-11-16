#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/10 9:51
'''
from app1.Pages.base_page import BasePage
from app1.Pages.news_page import NewsPage


class MainPage(BasePage):
    # 点击行情
    def goto_news(self):
        self.test_get_test_steps_from_yaml("goto_news", '../datas/main_page.yaml')
        return NewsPage(self.driver)
