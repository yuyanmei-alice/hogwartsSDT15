#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/7 11:02
框架原理解析：
动态导入以及反射
'''
import importlib


# 动态导入，可动态导入模块
def test_importlib():
    c = importlib.import_module("animal")

# 反射，可查找模块下的属性

