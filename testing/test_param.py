#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/21 10:36
'''
import pytest


@pytest.mark.parametrize('c', [7, 8, 9])
@pytest.mark.parametrize('b', [4, 5, 6])
@pytest.mark.parametrize('a', [1, 2, 3])
def test_param(a, b, c):
    print(a, b, c)
