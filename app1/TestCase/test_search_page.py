#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/10 10:30
'''


class TestSearchPage:

    def test_search(self, setup_app):
        setup_app.goto_main().goto_news().goto_search().search()
