#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/24 10:48
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestImportContractor():

    def setup_method(self):
        option = Options()
        option.debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(6)

    def teardown_method(self):
        self.driver.quit()


    def test_chrome(self):
        self.driver.find_element_by_id('menu_contacts').click()
        self.driver.find_element_by_xpath("//div[@class='ww_operationBar']/div[2]/a").click()
        self.driver.find_element_by_partial_link_text('文件导入').click()
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys('C:/Users/11379/Downloads/mylist.xlsx')
        self.driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[3]/a").click()
        print(self.driver.find_element_by_class_name('ww_fileImporter_successImportText').text)
