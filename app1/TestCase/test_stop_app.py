#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/18 13:37
'''


class TestStopApp:
    def test_goto_news(self, setup_app):
        print("-----------测试完成，关闭app----------------")
        setup_app.stop_app()
