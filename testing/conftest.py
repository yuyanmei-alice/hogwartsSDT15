#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/22 11:08
'''
import pytest

from pythoncode.Calculator import Calculator
from testing.test_calc import TestCal


@pytest.fixture(autouse=False, scope="function")
def login():
    print("登录成功")
    print("fixture的功能类似于setup teardown")
    yield ['yield的功能和teardown相似']


from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session', autouse=False)
def test_connDB():
    print('连接数据库')
    yield
    print('关闭数据库连接')


@pytest.fixture(scope="module", autouse=True)
def get_cal():
    print("计算开始")
    calc = Calculator()
    yield calc
    print("计算结束")


@pytest.fixture(scope="function")
def open_uploadUrl(get_webdriver):
    get_webdriver.find_element_by_id('menu_contacts').click()
    get_webdriver.find_element_by_xpath("//div[@class='ww_operationBar']/div[2]/a").click()
    get_webdriver.find_element_by_partial_link_text('文件导入').click()


@pytest.fixture(scope="function")
def get_webdriver():
    option = Options()
    option.debugger_address = 'localhost:9222'
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(6)
    yield driver


@pytest.fixture(scope="class", autouse=True)
def get_testcal():
    print("获取计算机测试器")
    testcal = TestCal
    yield testcal
