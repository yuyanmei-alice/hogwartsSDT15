#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/10/24 15:47
'''
import pytest


def open_uploadUrl(get_webdriver):
    get_webdriver.find_element_by_id('menu_contacts').click()
    get_webdriver.find_element_by_xpath("//div[@class='ww_operationBar']/div[2]/a").click()
    get_webdriver.find_element_by_partial_link_text('文件导入').click()


def test_nodata(get_webdriver):
    open_uploadUrl(get_webdriver)
    get_webdriver.find_element_by_xpath("//input[@type='file']").send_keys("C:/Users/11379/Downloads/nodata.xlsx")
    get_webdriver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[3]/a").click()
    successImportText=get_webdriver.find_element_by_class_name('ww_fileImporter_successImportText').text
    assert "" == successImportText
    successImportTips = get_webdriver.find_element_by_class_name('ww_fileImporter_successImportTips').text
    assert "成员下载企业微信验证手机或邮箱后即可登录" == successImportTips
    get_webdriver.find_element_by_xpath("//div[@class='ww_fileImporter_successBtnWrap']/a").click()


def test_nonXlsxOrXls(get_webdriver):
    open_uploadUrl(get_webdriver)
    get_webdriver.find_element_by_xpath("//input[@type='file']").send_keys(
        "C:/Users/11379/Downloads/Linux常用命令之文件处理.xmind")
    get_webdriver.find_element_by_id('js_tips')

