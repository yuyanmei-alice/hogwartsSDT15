#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
'''
@author : yuyanmei
@Date :2020/11/10 9:50
'''
import allure
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
import yaml
from app1.Pages.handle_black import handle_black

class BasePage:
    black_list = [{"by": "xpath", "locator": "//*[@resource-id='com.xueqiu.android:id/iv_close']"},
                  {"by": "xpath", "locator": "// * [ @ text = '同意']"}
                  ]
    error_num = 0
    max_error_num = 0

    # driver初始化
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            cpas_config = self.get_init_caps()
            caps = {}
            caps["platformName"] = cpas_config['platformName']
            caps["deviceName"] = cpas_config['deviceName']
            caps["appPackage"] = cpas_config['appPackage']
            caps["appActivity"] = cpas_config['appActivity']
            caps["noReset"] = cpas_config['noReset']
            caps["skipDeviceInitialization"] = cpas_config['skipDeviceInitialization']
            caps["skipServerInstallation"] = cpas_config['skipServerInstallation']
            self.driver = webdriver.Remote(cpas_config['server'], caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

    # 提供主页入口
    def goto_main(self):
        from app1.Pages.main_page import MainPage
        return MainPage(self.driver)

    # 封装查找元素,对该方法进行增强

    @handle_black
    def find(self, by, locator=None):
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result

    # 停止app
    def stop_app(self):
        self.driver.quit()

    # 用yaml保存caps信息，提供方法读取caps信息
    def get_init_caps(self):
        with open("../datas/caps.yaml", encoding='UTF-8') as f:
            result = yaml.safe_load(f)
            return result

    # 读取yaml文件，解析元素定位方式以及定位表达式
    def test_get_test_steps_from_yaml(self, funcName, filePath):
        with open(filePath, encoding='UTF-8') as f:
            result = yaml.safe_load(f)
            steps = (result[funcName])
            for step in steps:
                if "click" == step['action']:
                    self.find(step['by'], step['locator']).click()
                elif "send" == step['action']:
                    self.find(step['by'], step['locator']).send_keys(step['value'])

    def back_to_main(self, backTimes):
        for i in range(backTimes):
            self.driver.back()



