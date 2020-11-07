#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/22 10:46
装饰器测试类
'''
import pytest


def test_case1(login):
    print("测试用例1:通过函数名调用登录函数,只有通过该方式才能获取被调函数的返回值")
    print(login)


@pytest.mark.usefixtures('login')
def test_case2():
    print("测试用例2:通过fixture使用函数")


def test_case3():
    print("测试用例3:验证函数fixture的autouse参数")
