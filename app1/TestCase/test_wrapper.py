#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/16 17:49
通过实例来了解装饰器的语法与使用
'''

import time


def timmer(fun1):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = fun1(*args, **kwargs)
        stop_time = time.time()
        print('run time is %s' % (stop_time - start_time))
        return res

    return wrapper


@timmer
def foo():
    time.sleep(3)
    print('from foo')


@timmer
def foo1():
    time.sleep(5)
    print('from foo1')


def test_wrapper():
    foo()
    foo1()
