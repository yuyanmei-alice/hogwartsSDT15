#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/22 11:08
'''
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def get_webdriver():
    option = Options()
    option.debugger_address = 'localhost:9222'
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(6)
    yield driver


