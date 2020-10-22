#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/17 14:59
'''


def setup_module():
    print("setup module")


def teardown_module():
    print("teardown module")


def test_case1():
    print("case1")


def test_case2():
    print("case2")


def setup_function():
    print("setup function")


def teardown_function():
    print("teardown function")





class TestDemo:

    def setup_class(self):
        print("setup class")

    def teardown_class(self):
        print("teardown class")

    def test_demo1(self):
        print("testDemo1")

    def test_demo2(self):
        print("testDemo2")
