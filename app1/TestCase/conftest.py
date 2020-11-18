#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/18 11:07
'''
import pytest


def setup_module():
    print("setup_module")


@pytest.fixture(scope='session', autouse=True)
def setup_app():
    print("-----------开始测试，启动app----------------")
    from app1.Pages.base_page import BasePage
    appdriver = BasePage()
    yield appdriver


