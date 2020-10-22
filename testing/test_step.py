#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/21 15:42
'''
import pytest
import yaml


class TestSteps:

    def test_runByStep(self, get_testcal):
        self.get_step(get_testcal)

    def get_step(self, get_testcal):
        with open('./steps/steps.yml') as f:
            steps = yaml.safe_load(f)
            for step in steps:
                if 'add' == step:
                    print('执行加法验证用例')
                    get_testcal.test_add
                elif 'minus' == step:
                    print('执行减法验证用例')
                    get_testcal.test_minus
                elif 'plus' == step:
                    print('执行乘法验证用例')
                    get_testcal.test_plus
                elif 'div' == step:
                    print('执行除法验证用例')
                    get_testcal.test_div_zero

