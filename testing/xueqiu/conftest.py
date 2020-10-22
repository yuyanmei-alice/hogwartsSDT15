#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/22 11:26
'''
import pytest


@pytest.fixture(scope='session', autouse=True)
def test_connDB():
    print('单独文件包下的fixture:连接数据库')
    yield
    print('单独文件包下的fixture:关闭数据库连接')
