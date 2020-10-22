#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/17 15:33
'''
import pytest
import yaml

from pythoncode.Calculator import Calculator


class TestCal:

    def get_datas():
        with open('./datas/calc.yml') as f:
            datas = yaml.safe_load(f)
            add_datas = datas['add']['datas']
            add_ids = datas['add']['ids']
            minus_datas =datas['minus']['datas']
            minus_ids = datas['minus']['ids']
            plus_datas =datas['plus']['datas']
            plus_ids = datas['plus']['ids']
        return [add_datas, add_ids, minus_datas, minus_ids, plus_datas, plus_ids]

    # 相加的2个数可取 负数、0、正数、小数(小数点位数）
    '''
     最小负数 a  最大负数 b
     最大整数 a  最大整数 b
     
    @Date :2020/10/17 15:33
    '''

    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, get_cal, a, b, expect):
        result = get_cal.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,', [[1, 1], [1, 0]])
    def test_div_zero(self, get_cal, a, b):
        with pytest.raises(ZeroDivisionError):
            get_cal.div(a, b)

    @pytest.mark.parametrize('a,b,expect', get_datas()[2], ids=get_datas()[3])
    def test_minus(self, get_cal, a, b, expect):
        result = get_cal.minus(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', get_datas()[4], ids=get_datas()[5])
    def test_plus(self, get_cal, a, b, expect):
        result = get_cal.plus(a, b)
        assert result == expect

