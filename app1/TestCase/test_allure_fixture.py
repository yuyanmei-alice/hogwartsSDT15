#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/18 14:49
'''
import allure


@allure.feature("登录模块")
class TestAllureFixture:
    @allure.story("登录成功")
    def test_login_success(self):
        with allure.step("登录成功步骤1"):
            print("打开主页")
        pass

    @allure.story("登录失败")
    def test_login_fail(self):
        pass
